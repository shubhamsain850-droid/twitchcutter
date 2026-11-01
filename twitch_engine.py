"""
TwitchCutter Engine - Video Clipping & Trimming for Twitch.tv
Supports:
- Twitch VODs (twitch.tv/videos/ID)
- Twitch Clips (clips.twitch.tv/ID or twitch.tv/channel/clip/ID)
- Twitch Livestreams & Channels (twitch.tv/channel)
- Automatic extraction of video resolutions (1080p60, 720p60, 480p, 360p, 160p)
- Direct stream preview URL generation (HLS / m3u8 or MP4)
- Real-time progress percentage callback (0% - 100%) during clipping
- High-speed keyframe-accurate slicing via yt-dlp and ffmpeg
"""

import os
import re
import json
import datetime
import subprocess
from pathlib import Path
from typing import Dict, Any, Tuple, Callable, Optional, List


# -------------------------------------------------------------
# TIME HELPERS
# -------------------------------------------------------------
def time_to_seconds(t_str: str) -> int:
    """Converts strings like '01:30', '1:02:45', or '90' into integer seconds."""
    t_str = str(t_str).strip()
    if not t_str:
        return 0
    if t_str.isdigit():
        return int(t_str)
    
    parts = t_str.split(":")
    try:
        parts = [int(p) for p in parts]
        if len(parts) == 1:
            return parts[0]
        elif len(parts) == 2:
            return parts[0] * 60 + parts[1]
        elif len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
    except Exception:
        pass
    return 0


def seconds_to_time(seconds: int) -> str:
    """Converts integer seconds into HH:MM:SS format."""
    seconds = max(0, int(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


# -------------------------------------------------------------
# RESOLUTION HELPERS
# -------------------------------------------------------------
def get_default_resolutions() -> List[Dict[str, Any]]:
    return [
        {"id": "best", "height": 9999, "label": "⚡ Best Available Source (Original)", "format_id": "best"},
        {"id": "1080p", "height": 1080, "label": "⚡ 1080p60 Full HD", "format_id": "1080p"},
        {"id": "720p", "height": 720, "label": "⚡ 720p60 HD", "format_id": "720p"},
        {"id": "480p", "height": 480, "label": "⚡ 480p SD", "format_id": "480p"},
        {"id": "360p", "height": 360, "label": "⚡ 360p", "format_id": "360p"},
        {"id": "160p", "height": 160, "label": "⚡ 160p (Data Saver)", "format_id": "160p"},
    ]


# -------------------------------------------------------------
# TWITCH INFO EXTRACTOR
# -------------------------------------------------------------
def clean_twitch_url(raw_url: str) -> str:
    """Standardizes input URLs into valid Twitch URLs."""
    url = raw_url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        if "/" in url or "twitch" in url:
            url = "https://" + url.lstrip("/")
        else:
            url = f"https://www.twitch.tv/{url.replace('@', '')}"
    return url


def get_twitch_info(url: str) -> Dict[str, Any]:
    """
    Extracts Twitch video, clip, or stream metadata using yt-dlp.
    Returns: title, uploader, duration, thumbnail, resolutions, preview_url.
    """
    target_url = clean_twitch_url(url)

    cmd = [
        "yt-dlp",
        "--dump-json",
        "--skip-download",
        "--no-warnings",
        "--no-playlist",
        target_url
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        if proc.returncode != 0:
            err_msg = proc.stderr.strip() or "Twitch stream/video not found or unavailable."
            return {"success": False, "error": err_msg}

        data = json.loads(proc.stdout)

        title = data.get("title") or "Twitch Video"
        uploader = data.get("uploader") or data.get("channel") or "Twitch Streamer"
        duration = data.get("duration") or 0
        thumbnail = data.get("thumbnail")
        is_live = data.get("is_live", False)
        stream_id = str(data.get("id") or "")

        formats = data.get("formats", [])
        available_resolutions = [
            {"id": "best", "height": 9999, "label": "⚡ Best Available Source (Original)", "format_id": "best"}
        ]
        seen_res = set()

        preview_url = None
        # Try to find preview URL from formats
        for f in formats:
            f_url = f.get("url")
            if f_url and not preview_url:
                if ".m3u8" in f_url or ".mp4" in f_url:
                    preview_url = f_url

            h = f.get("height")
            if h and h not in seen_res:
                seen_res.add(h)
                fps = f.get("fps") or 0
                fps_str = f"{int(fps)}" if fps >= 50 else ""
                if h >= 1080:
                    label = f"⚡ 1080p{fps_str} Full HD"
                elif h >= 720:
                    label = f"⚡ 720p{fps_str} HD"
                elif h >= 480:
                    label = f"⚡ 480p SD"
                else:
                    label = f"⚡ {h}p"

                available_resolutions.append({
                    "id": f"{h}p",
                    "height": h,
                    "label": label,
                    "format_id": f.get("format_id") or f"{h}p"
                })

        # Sort resolutions descending by height
        available_resolutions = sorted(available_resolutions, key=lambda x: x["height"], reverse=True)

        if not available_resolutions or len(available_resolutions) <= 1:
            available_resolutions = get_default_resolutions()

        return {
            "success": True,
            "title": title,
            "uploader": uploader,
            "stream_id": stream_id,
            "duration": int(duration),
            "duration_str": seconds_to_time(int(duration)),
            "thumbnail": thumbnail,
            "is_live": is_live,
            "preview_url": preview_url or "",
            "available_resolutions": available_resolutions,
            "webpage_url": data.get("webpage_url", target_url)
        }

    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Request timed out while connecting to Twitch."}
    except Exception as e:
        return {"success": False, "error": f"Error fetching Twitch data: {str(e)}"}


# -------------------------------------------------------------
# VIDEO CLIPPER WITH REAL-TIME PROGRESS TRACKING
# -------------------------------------------------------------
def clip_twitch_video(
    url: str,
    start_time: str,
    end_time: str,
    quality: str = "720p",
    output_dir: str = "/tmp/twitchcutter",
    progress_callback: Optional[Callable[[float, str], None]] = None
) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Clips a Twitch VOD, clip, or stream segment between start_time and end_time.
    Uses yt-dlp --download-sections and stream-copy keyframe slicing.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    start_sec = time_to_seconds(start_time)
    end_sec = time_to_seconds(end_time)

    if end_sec <= start_sec:
        return False, "End time must be greater than Start time.", {}

    clip_duration = end_sec - start_sec
    if clip_duration > 7200:  # 2 hours max
        return False, "Clip duration cannot exceed 2 hours at a time.", {}

    timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_filename = f"twitch_clip_{timestamp_str}.mp4"
    final_output = out_path / out_filename

    target_url = clean_twitch_url(url)

    # Format quality selector for yt-dlp
    q_lower = quality.lower().strip()
    if q_lower == "best":
        format_selector = "best"
    elif "1080" in q_lower:
        format_selector = "best[height<=1080]/best"
    elif "720" in q_lower:
        format_selector = "best[height<=720]/best"
    elif "480" in q_lower:
        format_selector = "best[height<=480]/best"
    elif "360" in q_lower:
        format_selector = "best[height<=360]/best"
    elif "160" in q_lower:
        format_selector = "best[height<=160]/best"
    else:
        format_selector = f"{quality}/best"

    section_arg = f"*{seconds_to_time(start_sec)}-{seconds_to_time(end_sec)}"

    cmd = [
        "yt-dlp",
        "--download-sections", section_arg,
        "-f", format_selector,
        "--force-keyframes-at-cuts",
        "-o", str(final_output),
        "--no-playlist",
        "--merge-output-format", "mp4",
        "--newline",
        target_url
    ]

    if progress_callback:
        progress_callback(5.0, "Connecting to Twitch servers...")

    last_pct = 5.0

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in proc.stdout:
            line_str = line.strip()
            if not line_str:
                continue

            # Check for ffmpeg transcoding time (e.g. time=00:00:11.93)
            m_time = re.search(r'time=(\d+):(\d+):([\d\.]+)', line_str)
            if m_time:
                sec = int(m_time.group(1)) * 3600 + int(m_time.group(2)) * 60 + float(m_time.group(3))
                if clip_duration > 0:
                    calc_pct = min(98.0, (sec / clip_duration) * 100.0)
                    if calc_pct > last_pct:
                        last_pct = round(calc_pct, 1)
                        if progress_callback:
                            progress_callback(last_pct, f"Slicing clip: {last_pct}%")
                continue

            # Check for yt-dlp download percentage (e.g. [download]  45.0% of ...)
            m_dl = re.search(r'\[download\]\s+([\d\.]+)%', line_str)
            if m_dl:
                try:
                    val = float(m_dl.group(1))
                    calc_pct = min(98.0, val)
                    if calc_pct > last_pct:
                        last_pct = round(calc_pct, 1)
                        if progress_callback:
                            progress_callback(last_pct, f"Downloading stream segments: {last_pct}%")
                except ValueError:
                    pass
                continue

            # Check for container fixup / final packaging
            if "[FixupM3u8]" in line_str or "Fixing" in line_str or "Merging" in line_str:
                if last_pct < 96.0:
                    last_pct = 96.0
                    if progress_callback:
                        progress_callback(96.0, "Packaging MP4 clip...")

        proc.wait(timeout=300)

        if proc.returncode == 0 and final_output.exists() and final_output.stat().st_size > 1000:
            if progress_callback:
                progress_callback(100.0, "100% Complete! Ready for download.")
            return True, "Clip successfully generated!", {
                "filename": out_filename,
                "file_path": str(final_output),
                "duration": clip_duration,
                "size_mb": round(final_output.stat().st_size / (1024 * 1024), 2)
            }
        else:
            return False, "Failed to slice clip from Twitch stream. Please check video availability.", {}

    except subprocess.TimeoutExpired:
        if 'proc' in locals():
            proc.kill()
        return False, "Processing timed out (5 minutes limit). Please try a shorter duration.", {}
    except Exception as e:
        return False, f"Unexpected error during slicing: {str(e)}", {}


"""
TwitchCutter Backend API (FastAPI)
Provides endpoints for:
- POST /info: Get video title, thumbnail, duration, streamer name, resolutions, preview URL.
- POST /clip: Start background video clipping job with real-time percentage tracking.
- GET /status/{job_id}: Check job status, progress percentage (0-100%), download URL.
- GET /download/{filename}: Download trimmed MP4 video file.
- GET /health: API health check.
"""

from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import datetime
from pathlib import Path
import os
import sys
import asyncio

# Import core clipping engine
from twitch_engine import (
    get_twitch_info,
    clip_twitch_video,
    time_to_seconds,
    seconds_to_time
)

app = FastAPI(title="TwitchCutter API", description="Backend API for Twitch.tv Video Trimming & Slicing")

# Enable CORS for Cloudflare Pages frontend & localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLIPS_DIR = Path("/tmp/twitchcutter" if sys.platform != "win32" else os.path.expanduser("~/.twitchcutter_tmp"))
CLIPS_DIR.mkdir(parents=True, exist_ok=True)

# In-memory jobs tracking
jobs = {}

class InfoRequest(BaseModel):
    url: str

class ClipRequest(BaseModel):
    url: str
    start: str
    end: str
    quality: str = "720p"

@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok", "service": "TwitchCutter API", "version": "1.0.0"}

@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}

@app.post("/info")
def get_info(req: InfoRequest):
    url = req.url.strip()
    if not url:
        raise HTTPException(status_code=400, detail="Twitch URL is required.")
    
    info = get_twitch_info(url)
    if not info.get("success"):
        raise HTTPException(status_code=400, detail=info.get("error", "Failed to fetch video information."))
    
    return {
        "success": True,
        "title": info.get("title", "Twitch Video"),
        "uploader": info.get("uploader", "Creator"),
        "stream_id": info.get("stream_id", "N/A"),
        "duration": info.get("duration", 0),
        "duration_str": info.get("duration_str", "00:00"),
        "thumbnail": info.get("thumbnail"),
        "is_live": info.get("is_live", False),
        "preview_url": info.get("preview_url", ""),
        "available_resolutions": info.get("available_resolutions", []),
        "webpage_url": info.get("webpage_url", url)
    }

def run_clip_job(job_id: str, url: str, start: str, end: str, quality: str):
    jobs[job_id]["status"] = "processing"
    jobs[job_id]["progress"] = 5.0
    jobs[job_id]["message"] = "Connecting to Twitch stream..."

    def on_progress(pct: float, message: str):
        if job_id in jobs:
            jobs[job_id]["progress"] = round(pct, 1)
            jobs[job_id]["message"] = message

    try:
        success, msg, meta = clip_twitch_video(
            url=url,
            start_time=start,
            end_time=end,
            quality=quality,
            output_dir=str(CLIPS_DIR),
            progress_callback=on_progress
        )

        if success and "filename" in meta:
            jobs[job_id]["status"] = "done"
            jobs[job_id]["progress"] = 100.0
            jobs[job_id]["message"] = "Clip generated successfully!"
            jobs[job_id]["download_url"] = f"/download/{meta['filename']}"
            jobs[job_id]["meta"] = meta
        else:
            jobs[job_id]["status"] = "error"
            jobs[job_id]["progress"] = 0.0
            jobs[job_id]["message"] = msg or "Failed to clip video."

    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["progress"] = 0.0
        jobs[job_id]["message"] = f"Server processing error: {str(e)}"

@app.post("/clip")
def start_clip(req: ClipRequest, background_tasks: BackgroundTasks):
    url = req.url.strip()
    if not url:
        raise HTTPException(status_code=400, detail="Twitch URL is required.")
    
    start_sec = time_to_seconds(req.start)
    end_sec = time_to_seconds(req.end)

    if end_sec <= start_sec:
        raise HTTPException(status_code=400, detail="End time must be greater than Start time.")
    
    if (end_sec - start_sec) > 7200:
        raise HTTPException(status_code=400, detail="Clip duration cannot exceed 2 hours.")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "status": "queued",
        "progress": 0.0,
        "message": "Queued for processing...",
        "download_url": None,
        "created_at": datetime.datetime.now().isoformat()
    }

    background_tasks.add_task(run_clip_job, job_id, url, req.start, req.end, req.quality)

    return {
        "success": True,
        "job_id": job_id,
        "status": "queued",
        "message": "Clip job has been queued."
    }

@app.get("/status/{job_id}")
def get_status(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job ID not found.")
    return job

async def remove_file_after_delay(file_path: Path, delay_seconds: int = 900):
    """Deletes temporary clip file after 15 minutes to save disk space."""
    await asyncio.sleep(delay_seconds)
    try:
        if file_path.exists():
            file_path.unlink()
    except Exception:
        pass

@app.get("/download/{filename}")
def download_clip(filename: str, background_tasks: BackgroundTasks):
    safe_name = os.path.basename(filename)
    file_path = CLIPS_DIR / safe_name

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Requested clip not found or expired.")

    # Schedule cleanup in 15 minutes
    background_tasks.add_task(remove_file_after_delay, file_path, 900)

    return FileResponse(
        path=str(file_path),
        filename=safe_name,
        media_type="video/mp4"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=7860, reload=True)


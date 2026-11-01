import os
import sys

BASE_DIR = r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend"

def get_tool_html(custom_h1, custom_sub, default_placeholder):
    return f"""
    <section class="hero">
      <div class="hero-pill">⚡ Slices VODs in seconds &bull; No watermark &bull; 100% Free</div>
      <h1>{custom_h1}</h1>
      <p>{custom_sub}</p>
    </section>

    <!-- Input Card -->
    <div class="input-card">
      <div class="input-wrapper">
        <input 
          type="text" 
          id="urlInput" 
          class="url-input" 
          placeholder="{default_placeholder}"
          autocomplete="off"
        >
        <button id="fetchBtn" class="fetch-btn" onclick="handleFetch()">
          <span id="fetchBtnText">Fetch Stream</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
      <div class="quick-examples">
        <span>Try sample:</span>
        <span class="example-tag" onclick="loadSample('https://www.twitch.tv/eslcs')">ESLCS Channel</span>
        <span class="example-tag" onclick="loadSample('https://www.twitch.tv/videos/2914038727')">Shroud 8.7h VOD</span>
        <span class="example-tag" onclick="loadSample('https://www.twitch.tv/videos/2916013156')">ESLCS 23.6h VOD</span>
      </div>
    </div>

    <!-- Video Preview & Trimmer Card -->
    <div id="playerCard" class="player-card">
      <div class="video-info-header">
        <div>
          <h2 id="videoTitle" class="video-title">Stream Title</h2>
          <div class="video-meta">
            <span id="videoCreator" class="uploader-badge">Streamer</span>
            <span>&bull;</span>
            <span id="videoDuration">00:00:00</span>
            <span>&bull;</span>
            <span id="videoTypeBadge" class="badge-vod">📼 VOD</span>
          </div>
        </div>
      </div>

      <!-- STRICT 16:9 PREVIEW FRAME (Twitch Interactive Player + HTML5 Fallback) -->
      <div class="video-frame-wrapper">
        <div id="twitchPlayerEmbed" style="width:100%; height:100%;"></div>
        <video id="previewVideo" controls playsinline preload="metadata" style="display:none; width:100%; height:100%;"></video>
        <div id="videoLoadingOverlay" class="video-loading-overlay">
          <div class="spinner"></div>
          <span id="videoLoadingText">Loading Twitch Stream Player (16:9)...</span>
        </div>
      </div>

      <!-- Playback Controls (Play from Start Timestamp) -->
      <div class="player-action-bar">
        <div style="display:flex; align-items:center; gap:0.6rem; flex-wrap:wrap;">
          <button type="button" class="play-start-btn" onclick="playFromStart()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
            <span>Play from Start Timestamp</span>
          </button>
          <button type="button" class="nudge-btn" onclick="seekToStart()" title="Seek video to start timestamp">
            <span>↺ Seek to Start</span>
          </button>
        </div>
        <div class="player-info-hint">
          ⏱️ Video previews starting at your chosen in-point
        </div>
      </div>

      <!-- Dual Range Slider Controls -->
      <div class="slider-section">
        <div class="slider-header">
          <span style="font-weight: 800; font-size: 0.95rem; color:#fff;">✂️ Select Clip Segment</span>
          <div id="selectedDurationBadge" class="selected-duration-badge">
            <span id="rangeTimesBadge">00:00:00 ➔ 00:01:00</span>
            <span class="badge-divider">&bull;</span>
            <span class="clip-len-label">Clip Length: <strong id="clipLengthText" style="color:var(--green-success);">1 min 0s</strong></span>
          </div>
        </div>

        <div class="dual-slider-track-wrap">
          <div class="slider-bg-bar"></div>
          <div id="sliderHighlight" class="slider-highlight-bar" style="left: 0%; right: 90%;"></div>
          <input type="range" id="rangeStart" class="range-input" min="0" max="3600" value="0">
          <input type="range" id="rangeEnd" class="range-input" min="0" max="3600" value="60">
        </div>

        <!-- Precise Time Inputs (Guaranteed No-Overflow Grid) -->
        <div class="timestamps-grid">
          <!-- Start Box -->
          <div class="timestamp-box">
            <div class="timestamp-header-row">
              <span class="timestamp-title" style="color:#bf94ff;">Start Timestamp</span>
              <div class="nudge-group">
                <button type="button" class="nudge-btn" onclick="nudgeTime('start', -5)" title="Rewind 5s">-5s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('start', -1)" title="Rewind 1s">-1s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('start', 1)" title="Forward 1s">+1s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('start', 5)" title="Forward 5s">+5s</button>
              </div>
            </div>
            <input type="text" id="startTime" class="time-input" value="00:00:00" autocomplete="off">
          </div>

          <!-- End Box -->
          <div class="timestamp-box">
            <div class="timestamp-header-row">
              <span class="timestamp-title" style="color:#00f59b;">End Timestamp</span>
              <div class="nudge-group">
                <button type="button" class="nudge-btn" onclick="nudgeTime('end', -5)" title="Minus 5s">-5s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('end', -1)" title="Minus 1s">-1s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('end', 1)" title="Plus 1s">+1s</button>
                <button type="button" class="nudge-btn" onclick="nudgeTime('end', 5)" title="Plus 5s">+5s</button>
              </div>
            </div>
            <input type="text" id="endTime" class="time-input" value="00:01:00" autocomplete="off">
          </div>
        </div>

        <!-- Quick Length Shortcuts -->
        <div class="quick-lengths-wrap">
          <span style="font-size:0.82rem; color:var(--text-muted); font-weight:600;">Quick Add Duration:</span>
          <button type="button" class="quick-pill" onclick="quickAdd(30)">+30s</button>
          <button type="button" class="quick-pill" onclick="quickAdd(60)">+1 Min</button>
          <button type="button" class="quick-pill" onclick="quickAdd(180)">+3 Min</button>
          <button type="button" class="quick-pill" onclick="quickAdd(300)">+5 Min</button>
          <button type="button" class="quick-pill" onclick="quickAdd(600)">+10 Min</button>
        </div>

        <!-- Action & Quality Row -->
        <div class="action-row">
          <div class="quality-select-wrapper">
            <label for="qualitySelect" style="white-space:nowrap; font-weight:700;">Resolution:</label>
            <select id="qualitySelect" class="quality-select">
              <option value="best">⚡ Best Available Source (Original)</option>
              <option value="1080p">⚡ 1080p60 Full HD</option>
              <option value="720p">⚡ 720p60 HD</option>
              <option value="480p">⚡ 480p SD</option>
              <option value="360p">⚡ 360p</option>
            </select>
          </div>

          <button id="cutBtn" class="cut-btn" onclick="startClipping()">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 12a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm9-15 5 5-5 5M6 6l12 12M6 18l12-12"/></svg>
            <span>Cut &amp; Download Clip</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Real-Time Percentage Progress Card -->
    <div id="progressCard" class="progress-card">
      <div class="progress-header">
        <div id="progressTitle" class="progress-title">Processing Twitch Stream...</div>
        <div id="percentBadge" class="percent-badge">0%</div>
      </div>
      <div class="progress-bar-wrap">
        <div id="progressBarFill" class="progress-bar-fill"></div>
      </div>
      <div class="progress-meta">
        <span id="progressMessage">Connecting to cloud slicer...</span>
        <span id="progressPercentage" style="font-weight:700; color:var(--green-success);">0%</span>
      </div>
      <a id="downloadBtn" class="download-btn" href="#" download>
        ⬇️ Download Trimmed MP4 (<span id="downloadSize">0 MB</span>)
      </a>
    </div>
"""

print("build_site_pages.py loaded with updated layout.")

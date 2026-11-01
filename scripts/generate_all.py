import os

TOOL_JS = """
    const API = window.location.origin.includes("localhost") || window.location.origin.includes("127.0.0.1")
      ? "http://127.0.0.1:7860"
      : "https://shubhamsain858-kickcuttr-api.hf.space";

    let totalVideoDuration = 3600;
    let hlsInstance = null;
    let activeJobId = null;
    let pollInterval = null;
    let isSeekingFromCode = false;

    function switchFaqTab(tabId, btn) {
      document.querySelectorAll('.faq-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.faq-pane').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const pane = document.getElementById(tabId);
      if (pane) pane.classList.add('active');
    }

    function toggleFaq(el) {
      const a = el.nextElementSibling;
      const span = el.querySelector('span');
      if (a.style.display === 'block') {
        a.style.display = 'none';
        span.textContent = '+';
      } else {
        a.style.display = 'block';
        span.textContent = '−';
      }
    }

    function loadSample(url) {
      document.getElementById('urlInput').value = url;
      handleFetch();
    }

    function timeToSec(t) {
      const parts = String(t).trim().split(":").map(Number);
      if (parts.length === 3) return parts[0] * 3600 + parts[1] * 60 + parts[2];
      if (parts.length === 2) return parts[0] * 60 + parts[1];
      return Number(t) || 0;
    }

    function secToTime(s) {
      s = Math.max(0, Math.floor(s));
      const h = Math.floor(s / 3600);
      const m = Math.floor((s % 3600) / 60);
      const sec = s % 60;
      if (h > 0) return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
      return `${String(m).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
    }

    const rangeStart = document.getElementById('rangeStart');
    const rangeEnd = document.getElementById('rangeEnd');
    const sliderHighlight = document.getElementById('sliderHighlight');
    const startTimeInput = document.getElementById('startTime');
    const endTimeInput = document.getElementById('endTime');
    const selectedDurationBadge = document.getElementById('selectedDurationBadge');
    const previewVideo = document.getElementById('previewVideo');

    // SEEK VIDEO DIRECTLY TO START TIMESTAMP
    function seekToTime(sec) {
      if (!previewVideo) return;
      isSeekingFromCode = true;
      try {
        previewVideo.currentTime = sec;
      } catch (e) {
        console.warn('Seek error:', e);
      }
      setTimeout(() => { isSeekingFromCode = false; }, 120);
    }

    function seekToStart() {
      const sVal = Number(rangeStart.value) || 0;
      seekToTime(sVal);
    }

    function playFromStart() {
      if (!previewVideo) return;
      const sVal = Number(rangeStart.value) || 0;
      seekToTime(sVal);
      previewVideo.play().catch(e => console.log('Playback error:', e));
    }

    // Video Player Event Listeners to ensure video plays from selected start point
    if (previewVideo) {
      previewVideo.addEventListener('play', () => {
        const sVal = Number(rangeStart.value) || 0;
        const eVal = Number(rangeEnd.value) || totalVideoDuration;
        // If current video playback is outside the selected clip range, jump straight to start
        if (previewVideo.currentTime < sVal - 0.5 || previewVideo.currentTime >= eVal - 0.5) {
          seekToTime(sVal);
        }
      });

      previewVideo.addEventListener('timeupdate', () => {
        if (isSeekingFromCode) return;
        const sVal = Number(rangeStart.value) || 0;
        const eVal = Number(rangeEnd.value) || totalVideoDuration;
        // When video reaches end of selected clip, automatically loop back to start
        if (eVal > sVal && previewVideo.currentTime >= eVal) {
          previewVideo.pause();
          seekToTime(sVal);
        }
      });
    }

    function updateSliderUi(shouldSeek = false) {
      if (!rangeStart || !rangeEnd) return;
      const max = Number(rangeEnd.max) || totalVideoDuration;
      let sVal = Number(rangeStart.value);
      let eVal = Number(rangeEnd.value);

      if (sVal >= eVal) {
        sVal = Math.max(0, eVal - 1);
        rangeStart.value = sVal;
      }
      if (eVal <= sVal) {
        eVal = Math.min(max, sVal + 1);
        rangeEnd.value = eVal;
      }

      const leftPct = (sVal / max) * 100;
      const rightPct = 100 - (eVal / max) * 100;

      if (sliderHighlight) {
        sliderHighlight.style.left = `${leftPct}%`;
        sliderHighlight.style.right = `${rightPct}%`;
      }

      const startFormatted = secToTime(sVal);
      const endFormatted = secToTime(eVal);

      if (startTimeInput) startTimeInput.value = startFormatted;
      if (endTimeInput) endTimeInput.value = endFormatted;

      const clipSec = Math.max(0, eVal - sVal);
      if (selectedDurationBadge) {
        selectedDurationBadge.textContent = `${startFormatted} ➔ ${endFormatted} (${clipSec}s)`;
      }
      const labelS = document.getElementById('sliderLabelStart');
      const labelE = document.getElementById('sliderLabelEnd');
      if (labelS) labelS.textContent = startFormatted;
      if (labelE) labelE.textContent = endFormatted;

      if (shouldSeek) {
        seekToTime(sVal);
      }
    }

    if (rangeStart && rangeEnd) {
      rangeStart.addEventListener('input', () => {
        let sVal = Number(rangeStart.value);
        let eVal = Number(rangeEnd.value);
        if (sVal >= eVal) {
          sVal = Math.max(0, eVal - 1);
          rangeStart.value = sVal;
        }
        updateSliderUi(true); // Seek preview to start timestamp immediately
      });

      rangeEnd.addEventListener('input', () => {
        let sVal = Number(rangeStart.value);
        let eVal = Number(rangeEnd.value);
        if (eVal <= sVal) {
          eVal = Math.min(Number(rangeEnd.max), sVal + 1);
          rangeEnd.value = eVal;
        }
        updateSliderUi(false);
      });
    }

    if (startTimeInput) {
      startTimeInput.addEventListener('change', () => {
        const sec = timeToSec(startTimeInput.value);
        if (rangeStart) rangeStart.value = Math.min(sec, Number(rangeEnd.value) - 1);
        updateSliderUi(true); // Seek to new start
      });
    }

    if (endTimeInput) {
      endTimeInput.addEventListener('change', () => {
        const sec = timeToSec(endTimeInput.value);
        if (rangeEnd) rangeEnd.value = Math.max(sec, Number(rangeStart.value) + 1);
        updateSliderUi(false);
      });
    }

    function nudgeTime(which, delta) {
      if (which === 'start') {
        let cur = timeToSec(startTimeInput.value) + delta;
        cur = Math.max(0, Math.min(cur, timeToSec(endTimeInput.value) - 1));
        if (rangeStart) rangeStart.value = cur;
        updateSliderUi(true); // Seek to start
      } else {
        let cur = timeToSec(endTimeInput.value) + delta;
        cur = Math.min(totalVideoDuration, Math.max(cur, timeToSec(startTimeInput.value) + 1));
        if (rangeEnd) rangeEnd.value = cur;
        updateSliderUi(false);
      }
    }

    function quickAdd(seconds) {
      const curStart = timeToSec(startTimeInput.value);
      const newEnd = Math.min(totalVideoDuration, curStart + seconds);
      if (rangeEnd) rangeEnd.value = newEnd;
      updateSliderUi(false);
    }

    function showSpinner() {
      const ov = document.getElementById('videoLoadingOverlay');
      if (ov) ov.style.display = 'flex';
    }

    function hideSpinner() {
      const ov = document.getElementById('videoLoadingOverlay');
      if (ov) ov.style.display = 'none';
    }

    async function handleFetch() {
      const input = document.getElementById('urlInput');
      const url = input.value.trim();
      if (!url) {
        alert('Please enter a valid Twitch stream, VOD, or clip URL.');
        return;
      }

      const fetchBtn = document.getElementById('fetchBtn');
      const fetchBtnText = document.getElementById('fetchBtnText');
      fetchBtn.disabled = true;
      fetchBtnText.textContent = 'Fetching...';

      const playerCard = document.getElementById('playerCard');
      showSpinner();

      try {
        const resp = await fetch(`${API}/info`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ url })
        });
        const data = await resp.json();

        if (resp.ok && data.success) {
          playerCard.style.display = 'block';

          document.getElementById('videoTitle').textContent = data.title || 'Twitch Stream';
          document.getElementById('videoCreator').textContent = data.uploader || 'Twitch Channel';

          totalVideoDuration = data.duration_seconds || data.duration || 3600;
          document.getElementById('videoDuration').textContent = secToTime(totalVideoDuration);

          const badge = document.getElementById('videoTypeBadge');
          if (data.is_live) {
            badge.textContent = '🔴 LIVE';
            badge.style.background = 'rgba(235, 4, 0, 0.2)';
            badge.style.color = '#ff6b6b';
          } else {
            badge.textContent = '📼 VOD';
            badge.style.background = '#27272a';
            badge.style.color = '#e4e4e7';
          }

          // CONFIGURE RANGE SLIDER DURATION
          if (rangeStart && rangeEnd) {
            rangeStart.max = totalVideoDuration;
            rangeEnd.max = totalVideoDuration;
            rangeStart.value = 0;
            const initialClip = Math.min(60, totalVideoDuration);
            rangeEnd.value = initialClip;
            updateSliderUi(false);
          }

          // DYNAMICALLY POPULATE ALL AVAILABLE RESOLUTIONS
          const qSelect = document.getElementById('qualitySelect');
          if (qSelect) {
            qSelect.innerHTML = '';
            const resList = (data.available_resolutions && data.available_resolutions.length > 0)
              ? data.available_resolutions
              : (data.formats && data.formats.length > 0)
                ? data.formats.map(f => ({
                    id: f.format_id || f.resolution || 'best',
                    label: `${f.format_note || f.resolution || 'Source'} (${f.ext || 'mp4'})`
                  }))
                : [
                    { id: 'best', label: 'Best Available Source (Original)' },
                    { id: '1080p', label: '1080p60 Full HD' },
                    { id: '720p', label: '720p60 HD' },
                    { id: '480p', label: '480p SD' },
                    { id: '360p', label: '360p' }
                  ];

            resList.forEach((r, idx) => {
              const opt = document.createElement('option');
              opt.value = r.id || r.format_id || 'best';
              const cleanLabel = r.label.startsWith('⚡') ? r.label : `⚡ ${r.label}`;
              opt.textContent = cleanLabel;
              if (idx === 0 || r.id === 'best' || r.id.includes('1080')) {
                opt.selected = true;
              }
              qSelect.appendChild(opt);
            });
          }

          // INITIALIZE HLS 16:9 PREVIEW VIDEO
          if (data.preview_url && previewVideo) {
            if (hlsInstance) {
              hlsInstance.destroy();
              hlsInstance = null;
            }

            const onVideoReady = () => {
              hideSpinner();
              // Seek video to initial start timestamp (0)
              seekToTime(0);
            };

            if (Hls.isSupported() && data.preview_url.includes('.m3u8')) {
              hlsInstance = new Hls({ enableWorker: true, lowLatencyMode: true });
              hlsInstance.loadSource(data.preview_url);
              hlsInstance.attachMedia(previewVideo);
              hlsInstance.on(Hls.Events.MANIFEST_PARSED, onVideoReady);
              hlsInstance.on(Hls.Events.ERROR, hideSpinner);
            } else {
              previewVideo.src = data.preview_url;
              previewVideo.onloadeddata = onVideoReady;
              setTimeout(hideSpinner, 3000);
            }
          } else {
            hideSpinner();
          }

          playerCard.scrollIntoView({ behavior: 'smooth' });
        } else {
          alert(data.detail || data.error || 'Failed to fetch Twitch stream. Please check the URL.');
          hideSpinner();
        }
      } catch (err) {
        alert('Network error connecting to backend API: ' + err.message);
        hideSpinner();
      } finally {
        fetchBtn.disabled = false;
        fetchBtnText.textContent = 'Fetch Stream';
      }
    }

    // CLIPPING JOB WITH REAL-TIME PERCENTAGE TRACKING
    async function startClipping() {
      const url = document.getElementById('urlInput').value.trim();
      const start = document.getElementById('startTime').value.trim();
      const end = document.getElementById('endTime').value.trim();
      const quality = document.getElementById('qualitySelect').value;

      if (timeToSec(end) <= timeToSec(start)) {
        alert('End timestamp must be greater than start timestamp.');
        return;
      }

      const cutBtn = document.getElementById('cutBtn');
      cutBtn.disabled = true;

      const progressCard = document.getElementById('progressCard');
      const progressBar = document.getElementById('progressBarFill');
      const progressPercent = document.getElementById('progressPercentage');
      const percentBadge = document.getElementById('percentBadge');
      const progressMsg = document.getElementById('progressMessage');
      const downloadBtn = document.getElementById('downloadBtn');

      progressCard.style.display = 'block';
      progressBar.style.width = '5%';
      progressPercent.textContent = '5%';
      if (percentBadge) percentBadge.textContent = '5%';
      progressMsg.textContent = 'Connecting to cloud video slicer...';
      downloadBtn.style.display = 'none';
      progressCard.scrollIntoView({ behavior: 'smooth' });

      try {
        const resp = await fetch(`${API}/clip`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ url, start, end, quality })
        });
        const data = await resp.json();

        if (resp.ok && data.success) {
          activeJobId = data.job_id;
          pollJobStatus(activeJobId);
        } else {
          alert(data.detail || 'Failed to start clipping job.');
          cutBtn.disabled = false;
        }
      } catch (err) {
        alert('Error communicating with backend: ' + err.message);
        cutBtn.disabled = false;
      }
    }

    function pollJobStatus(jobId) {
      if (pollInterval) clearInterval(pollInterval);

      pollInterval = setInterval(async () => {
        try {
          const resp = await fetch(`${API}/status/${jobId}`);
          const data = await resp.json();

          if (resp.ok) {
            const rawPct = data.progress || 0;
            const pct = Math.max(5, Math.min(100, Math.round(rawPct)));
            
            document.getElementById('progressBarFill').style.width = `${pct}%`;
            document.getElementById('progressPercentage').textContent = `${pct}%`;
            const pBadge = document.getElementById('percentBadge');
            if (pBadge) pBadge.textContent = `${pct}%`;
            document.getElementById('progressMessage').textContent = data.message || `Slicing stream segments... ${pct}%`;

            if (data.status === 'done' || data.status === 'completed') {
              clearInterval(pollInterval);
              document.getElementById('cutBtn').disabled = false;
              document.getElementById('progressBarFill').style.width = '100%';
              document.getElementById('progressPercentage').textContent = '100%';
              if (pBadge) pBadge.textContent = '100%';
              document.getElementById('progressTitle').textContent = '🎉 100% Complete! Clip Ready';
              document.getElementById('progressMessage').textContent = 'Clip generated successfully!';

              const dl = document.getElementById('downloadBtn');
              dl.href = `${API}${data.download_url}`;
              const size = (data.meta && data.meta.size_mb) || data.size_mb || '';
              if (size) {
                const sEl = document.getElementById('downloadSize');
                if (sEl) sEl.textContent = `${size} MB`;
              }
              dl.style.display = 'block';
            } else if (data.status === 'error') {
              clearInterval(pollInterval);
              document.getElementById('cutBtn').disabled = false;
              alert('Clipping error: ' + (data.message || 'Unknown error occurred.'));
            }
          }
        } catch (e) {
          console.error('Polling error:', e);
        }
      }, 1500);
    }
"""

print("generate_all.py TOOL_JS updated.")

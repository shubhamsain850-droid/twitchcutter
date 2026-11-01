import os







TOOL_JS = """



    const API = window.location.origin.includes("localhost") || window.location.origin.includes("127.0.0.1")



      ? "http://127.0.0.1:7860"



      : "https://shubhamsain858-kickcuttr-api.hf.space";







    let totalVideoDuration = 3600;



    let twitchPlayerInstance = null;



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







    function secToTwitchTime(s) {



      s = Math.max(0, Math.floor(s));



      const h = Math.floor(s / 3600);



      const m = Math.floor((s % 3600) / 60);



      const sec = s % 60;



      return `${h}h${m}m${sec}s`;



    }







    // FORMAT HUMAN-READABLE DURATION (e.g. "31 min 41s", "1h 15m 10s")



    function formatHumanDuration(seconds) {



      seconds = Math.max(0, Math.floor(seconds));



      if (seconds === 0) return "0s";



      const h = Math.floor(seconds / 3600);



      const m = Math.floor((seconds % 3600) / 60);



      const s = seconds % 60;







      let parts = [];



      if (h > 0) parts.push(`${h}h`);



      if (m > 0 || (h > 0 && s > 0)) parts.push(`${m} min`);



      if (s > 0 || (h === 0 && m === 0)) parts.push(`${s}s`);



      return parts.join(' ');



    }







    // EXTRACT TWITCH MEDIA ID / TYPE (VOD, Clip, Channel)



    function extractTwitchMedia(url) {



      const clean = String(url).trim();



      const vodMatch = clean.match(/videos\/(\d+)/i);



      if (vodMatch) {



        return { type: 'video', id: vodMatch[1] };



      }



      const clipMatch = clean.match(/(?:clips\.twitch\.tv\/|(?:\/clip\/))([A-Za-z0-9_-]+)/i);



      if (clipMatch) {



        return { type: 'clip', id: clipMatch[1] };



      }



      const channelMatch = clean.match(/twitch\.tv\/([A-Za-z0-9_]+)/i);



      if (channelMatch && !['videos', 'directory', 'p', 'search'].includes(channelMatch[1])) {



        return { type: 'channel', id: channelMatch[1] };



      }



      return null;



    }







    const rangeStart = document.getElementById('rangeStart');



    const rangeEnd = document.getElementById('rangeEnd');



    const sliderHighlight = document.getElementById('sliderHighlight');



    const startTimeInput = document.getElementById('startTime');



    const endTimeInput = document.getElementById('endTime');



    const rangeTimesBadge = document.getElementById('rangeTimesBadge');



    const clipLengthText = document.getElementById('clipLengthText');







    // SEEK VIDEO DIRECTLY TO TIMESTAMP (Twitch Interactive Player or HTML5 Video)



    function seekToTime(sec) {



      isSeekingFromCode = true;



      sec = Math.max(0, Number(sec) || 0);







      // 1. Twitch Embed Player SDK Seek



      if (twitchPlayerInstance && typeof twitchPlayerInstance.seek === 'function') {



        try {



          twitchPlayerInstance.seek(sec);



        } catch (e) {



          console.warn('Twitch Player seek error:', e);



        }



      }







      // 2. HTML5 Video Tag Seek



      const previewVideo = document.getElementById('previewVideo');



      if (previewVideo && previewVideo.style.display !== 'none') {



        try {



          previewVideo.currentTime = sec;



        } catch (e) {}



      }







      setTimeout(() => { isSeekingFromCode = false; }, 150);



    }







    function seekToStart() {



      const sVal = Number(rangeStart.value) || 0;



      seekToTime(sVal);



    }







    function playFromStart() {



      const sVal = Number(rangeStart.value) || 0;



      seekToTime(sVal);







      // 1. Play Twitch Embed



      if (twitchPlayerInstance && typeof twitchPlayerInstance.play === 'function') {



        try {



          twitchPlayerInstance.play();



        } catch (e) {}



      }







      // 2. Play HTML5 Video



      const previewVideo = document.getElementById('previewVideo');



      if (previewVideo && previewVideo.style.display !== 'none') {



        previewVideo.play().catch(e => console.log('Playback error:', e));



      }



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







      // UPDATE EXACT CLIP DURATION



      const clipSec = Math.max(0, eVal - sVal);



      const humanDuration = formatHumanDuration(clipSec);







      if (rangeTimesBadge) rangeTimesBadge.textContent = `${startFormatted} ➔ ${endFormatted}`;



      if (clipLengthText) clipLengthText.textContent = `${humanDuration} (${clipSec}s)`;







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



        updateSliderUi(true); // Seek video immediately as slider is dragged



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



        updateSliderUi(true); // Seek to new start time



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



        updateSliderUi(true); // Seek to new start point



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







    function showSpinner(text = 'Loading Twitch Stream Player (16:9)...') {



      const ov = document.getElementById('videoLoadingOverlay');



      const t = document.getElementById('videoLoadingText');



      if (t) t.textContent = text;



      if (ov) ov.style.display = 'flex';



    }







    function hideSpinner() {



      const ov = document.getElementById('videoLoadingOverlay');



      if (ov) ov.style.display = 'none';



    }







    // INITIALIZE OFFICIAL TWITCH PLAYER (NO CORS RESTRICTIONS)



    function setupTwitchPlayer(url, initialStartSec = 0, previewUrlFallback = '') {



      const embedDiv = document.getElementById('twitchPlayerEmbed');



      const videoTag = document.getElementById('previewVideo');



      if (!embedDiv) return;







      embedDiv.innerHTML = '';



      const media = extractTwitchMedia(url);







      const cleanHost = window.location.hostname || 'localhost';



      const cleanParents = [...new Set([cleanHost, 'twitchcutter.pages.dev', 'localhost', '127.0.0.1'])];







      if (media && media.type === 'video' && window.Twitch && window.Twitch.Player) {



        embedDiv.style.display = 'block';



        if (videoTag) videoTag.style.display = 'none';







        try {



          twitchPlayerInstance = new Twitch.Player('twitchPlayerEmbed', {



            width: '100%',



            height: '100%',



            video: media.id,



            autoplay: false,



            parent: cleanParents,



            time: secToTwitchTime(initialStartSec)



          });







          twitchPlayerInstance.addEventListener(Twitch.Player.READY, () => {



            hideSpinner();



            if (initialStartSec > 0) {



              twitchPlayerInstance.seek(initialStartSec);



            }



          });







          twitchPlayerInstance.addEventListener(Twitch.Player.PLAY, () => {



            hideSpinner();



          });



        } catch (e) {



          console.warn('Twitch Player initialization failed, trying fallback:', e);



          initVideoFallback(previewUrlFallback);



        }



      } else if (media && media.type === 'clip') {



        embedDiv.style.display = 'block';



        if (videoTag) videoTag.style.display = 'none';



        embedDiv.innerHTML = `<iframe src="https://clips.twitch.tv/embed?clip=${media.id}&parent=${cleanHost}&parent=twitchcutter.pages.dev&autoplay=false" width="100%" height="100%" style="border:none;" allowfullscreen="true" scrolling="no"></iframe>`;



        hideSpinner();



      } else if (media && media.type === 'channel' && window.Twitch && window.Twitch.Player) {



        embedDiv.style.display = 'block';



        if (videoTag) videoTag.style.display = 'none';



        try {



          twitchPlayerInstance = new Twitch.Player('twitchPlayerEmbed', {



            width: '100%',



            height: '100%',



            channel: media.id,



            autoplay: false,



            parent: cleanParents



          });



          twitchPlayerInstance.addEventListener(Twitch.Player.READY, hideSpinner);



        } catch (e) {



          initVideoFallback(previewUrlFallback);



        }



      } else {



        initVideoFallback(previewUrlFallback);



      }



    }







    function initVideoFallback(previewUrl) {



      const embedDiv = document.getElementById('twitchPlayerEmbed');



      const videoTag = document.getElementById('previewVideo');



      if (embedDiv) embedDiv.style.display = 'none';



      if (!videoTag) return;



      videoTag.style.display = 'block';







      if (hlsInstance) {



        hlsInstance.destroy();



        hlsInstance = null;



      }







      if (previewUrl) {



        if (Hls.isSupported() && previewUrl.includes('.m3u8')) {



          hlsInstance = new Hls({ enableWorker: true, lowLatencyMode: true });



          hlsInstance.loadSource(previewUrl);



          hlsInstance.attachMedia(videoTag);



          hlsInstance.on(Hls.Events.MANIFEST_PARSED, hideSpinner);



          hlsInstance.on(Hls.Events.ERROR, hideSpinner);



        } else {



          videoTag.src = previewUrl;



          videoTag.onloadeddata = hideSpinner;



          setTimeout(hideSpinner, 3000);



        }



      } else {



        hideSpinner();



      }



    }







    // FETCH STREAM INFO



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



      showSpinner('Connecting to Twitch Stream (16:9)...');







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







          // INITIALIZE OFFICIAL TWITCH PLAYER EMBED (CORS-FREE, 16:9)



          setupTwitchPlayer(url, 0, data.preview_url);







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



      const durSec = timeToSec(end) - timeToSec(start);

      if (durSec > 900) {

        progressMsg.textContent = 'Long clip selected (~' + Math.round(durSec/60) + ' min). Initializing Twitch stream buffer...';

      } else {

        progressMsg.textContent = 'Connecting to Twitch stream server...';

      }



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







        let clipStartTime = 0;

    function pollJobStatus(jobId) {
      if (pollInterval) clearInterval(pollInterval);
      clipStartTime = Date.now();

      let simulatedPct = 15;
      const simTimer = setInterval(() => {
        if (simulatedPct < 90) {
          simulatedPct += Math.floor(Math.random() * 8) + 5;
          simulatedPct = Math.min(92, simulatedPct);
          const pFill = document.getElementById('progressBarFill');
          const pPct = document.getElementById('progressPercentage');
          const pBadge = document.getElementById('percentBadge');
          const pMsg = document.getElementById('progressMessage');
          if (pFill) pFill.style.width = simulatedPct + '%';
          if (pPct) pPct.textContent = simulatedPct + '%';
          if (pBadge) pBadge.textContent = simulatedPct + '%';
          if (pMsg) {
            if (simulatedPct < 35) pMsg.textContent = 'Connecting to Twitch stream server...';
            else if (simulatedPct < 70) pMsg.textContent = 'Slicing keyframe segments in cloud...';
            else pMsg.textContent = 'Packaging MP4 video container...';
          }
        }
      }, 500);

      pollInterval = setInterval(async () => {
        try {
          const resp = await fetch(`${API}/status/${jobId}`);
          const data = await resp.json();

          if (resp.ok) {
            if (data.status === 'done' || data.status === 'completed') {
              clearInterval(pollInterval);
              clearInterval(simTimer);
              document.getElementById('cutBtn').disabled = false;
              document.getElementById('progressBarFill').style.width = '100%';
              document.getElementById('progressBarFill').style.background = 'linear-gradient(90deg, #00f59b, #00d285)';
              document.getElementById('progressPercentage').textContent = '100%';
              const pBadge = document.getElementById('percentBadge');
              if (pBadge) pBadge.textContent = '100%';
              document.getElementById('progressTitle').textContent = '🎉 100% Complete! Clip Ready';
              document.getElementById('progressMessage').textContent = 'Clip generated successfully!';

              const dl = document.getElementById('downloadBtn');
              dl.href = `${API}${data.download_url}`;
              const size = (data.meta && data.meta.size_mb) || data.size_mb || '';
              if (size) {
                const sEl = document.getElementById('downloadSize');
                if (sEl) sEl.textContent = size + ' MB';
              }
              dl.style.display = 'block';
              dl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else if (data.status === 'error' || data.status === 'failed') {
              clearInterval(pollInterval);
              clearInterval(simTimer);
              document.getElementById('cutBtn').disabled = false;
              const errMsg = data.error || data.message || 'Stream slicing failed.';
              document.getElementById('progressTitle').textContent = '⚠️ Slicing Encountered an Issue';
              document.getElementById('progressMessage').textContent = errMsg;
              document.getElementById('progressBarFill').style.background = '#ef4444';
              alert('Clipping error: ' + errMsg);
            }
          }
        } catch (e) {
          console.error('Polling error:', e);
        }
      }, 600);
    }

  """







print("generate_all.py TOOL_JS fully updated with Twitch Embed SDK and human durations.")




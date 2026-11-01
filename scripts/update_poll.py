import os

new_poll_code = """    let clipStartTime = 0;

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

target_search = "function pollJobStatus(jobId) {"

files = [
    r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend\index.html",
    r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend\twitch-clip-cutter.html",
    r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend\twitch-vod-downloader.html",
    r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\scripts\generate_all.py"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    idx = content.find(target_search)
    if idx != -1:
        end_idx = content.find("</script>", idx)
        if end_idx == -1:
            end_idx = content.find('"""', idx)
        if end_idx != -1:
            updated = content[:idx] + new_poll_code + "\n  " + content[end_idx:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated)
            print("Successfully updated pollJobStatus in:", filepath)

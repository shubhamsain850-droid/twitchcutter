# Common styling, header, footer for TwitchCutter pages
LOGO_SVG = """<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="twPurple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#bf94ff"/>
      <stop offset="50%" stop-color="#9146ff"/>
      <stop offset="100%" stop-color="#6424c9"/>
    </linearGradient>
    <linearGradient id="bladeSteel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <filter id="cutGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="1.5" flood-color="#00f59b" flood-opacity="0.8"/>
    </filter>
  </defs>
  <rect width="64" height="64" rx="15" fill="#0e0e10"/>
  <rect x="1" y="1" width="62" height="62" rx="14" stroke="#9146ff" stroke-width="1.8" stroke-opacity="0.4"/>
  <g transform="translate(2.2, -3.0)">
    <path d="M12 10 H48 V19.5 L12 34.5 Z" fill="url(#twPurple)"/>
    <rect x="21" y="19" width="4.5" height="10" rx="1" fill="#ffffff"/>
    <path d="M31.5 19 H36 V24.8 L31.5 26.5 Z" fill="#ffffff"/>
  </g>
  <g transform="translate(-2.2, 3.0)">
    <path d="M12 35.5 L48 20.5 V30 L38 40 H28 L22 48 V40 H12 Z" fill="url(#twPurple)"/>
    <rect x="21" y="32" width="4.5" height="2.5" rx="0.8" fill="#ffffff"/>
    <path d="M31.5 27.8 L36 26.2 V33 H31.5 Z" fill="#ffffff"/>
  </g>
  <line x1="8" y1="36.5" x2="52" y2="18" stroke="#00f59b" stroke-width="1.4" stroke-dasharray="2.5 2" filter="url(#cutGlow)"/>
  <circle cx="53" cy="15" r="5.5" stroke="#ffffff" stroke-width="2.4" fill="#0e0e10"/>
  <path d="M49 19 L43 24.5" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round"/>
  <circle cx="53" cy="34" r="5.5" stroke="#ffffff" stroke-width="2.4" fill="#0e0e10"/>
  <path d="M49 30 L43 25.5" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M42 25 L21 31 L23 28.5 L43 23.5 Z" fill="url(#bladeSteel)"/>
  <path d="M42 25 L21 31" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M42 25 L23 35 L25 37 L43 26.5 Z" fill="url(#bladeSteel)"/>
  <path d="M42 25 L23 35" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round"/>
  <circle cx="43" cy="25" r="3.2" fill="#0e0e10" stroke="#00f59b" stroke-width="1.6"/>
  <circle cx="43" cy="25" r="1.1" fill="#ffffff"/>
  <path d="M22 31 L23.5 27.5 L25 31 L28.5 32.5 L25 34 L23.5 37.5 L22 34 L18.5 32.5 Z" fill="#00f59b" filter="url(#cutGlow)"/>
</svg>"""

HEADER_HTML = f"""<header>
  <div style="display:flex; align-items:center; gap: 2rem; flex-wrap: wrap;">
    <a href="/" class="brand">
      <div class="brand-icon">
        {LOGO_SVG}
      </div>
      <div class="brand-name">Twitch<span>Cutter</span></div>
    </a>
    <nav class="nav-links">
      <a href="/">Home</a>
      <a href="/twitch-clip-cutter">Clip Cutter</a>
      <a href="/twitch-vod-downloader">VOD Downloader</a>
      <a href="/faq">FAQ</a>
      <a href="/blog/">Guides</a>
    </nav>
  </div>
  <span class="header-badge">Ultra-Fast Clipper</span>
</header>"""

FOOTER_HTML = """<footer>
  <div class="footer-links">
    <a href="/">Home</a>
    <a href="/twitch-clip-cutter">Twitch Clip Cutter</a>
    <a href="/twitch-vod-downloader">Twitch VOD Downloader</a>
    <a href="/faq">FAQ</a>
    <a href="/blog/">Guides &amp; Tutorials</a>
    <a href="/about">About</a>
    <a href="/privacy">Privacy Policy</a>
    <a href="/terms">Terms &amp; DMCA</a>
    <a href="/contact">Contact Support</a>
    <a href="https://github.com/shubhamsain850-droid/twitchcutter" target="_blank" rel="noopener">GitHub</a>
  </div>
  <p style="margin-bottom:0.4rem;">&copy; 2026 TwitchCutter &bull; Fast, Free &amp; Open Source Online Video Clipper &amp; VOD Downloader for Twitch.tv.</p>
  <p style="font-size:0.75rem; color:#64748b;">Disclaimer: TwitchCutter is an independent open-source tool and is not affiliated with, endorsed by, or sponsored by Twitch Interactive, Inc. or Amazon.</p>
</footer>"""

FAVICON_HEAD = """  <link rel="icon" type="image/svg+xml" href="/favicon.svg?v=4">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png?v=4">
  <link rel="shortcut icon" href="/favicon.ico?v=4">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=4">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">"""

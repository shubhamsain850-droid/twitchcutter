import os
import sys

BASE_DIR = r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend"
BLOG_DIR = os.path.join(BASE_DIR, "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

sys.path.append(r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\scripts")
from common_elements import LOGO_SVG, HEADER_HTML, FOOTER_HTML, FAVICON_HEAD
from build_full_site import COMMON_CSS
from generate_all import TOOL_JS
from build_site_pages import get_tool_html

# ==============================================================================
# 1. INDEX.HTML (HOMEPAGE)
# ==============================================================================
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Twitch VOD Cutter &amp; Clip Downloader Online | TwitchCutter</title>
  <meta name="title" content="Free Twitch VOD Cutter &amp; Clip Downloader Online | TwitchCutter">
  <meta name="description" content="Free online Twitch VOD cutter &amp; stream clip downloader. Cut any segment by timestamp or download clips in 1080p60 MP4 — no software, no watermark, no login.">
  <meta name="keywords" content="twitch vod cutter, cut twitch vod, twitch clip cutter, trim twitch vod, download part of twitch vod, twitch vod downloader, free twitch clip downloader, twitch stream cutter, untwitch alternative, twitch to mp4">
  <meta name="author" content="TwitchCutter">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://twitchcutter.pages.dev/">

{FAVICON_HEAD}

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://twitchcutter.pages.dev/">
  <meta property="og:title" content="Free Twitch VOD Cutter &amp; Clip Downloader Online | TwitchCutter">
  <meta property="og:description" content="Cut, trim &amp; download Twitch VODs and clips online for free. No login, no watermark, no software. Set timestamps and export to MP4.">
  <meta property="og:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">
  <meta property="og:site_name" content="TwitchCutter">

  <!-- Twitter / X -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://twitchcutter.pages.dev/">
  <meta property="twitter:title" content="Free Twitch VOD Cutter &amp; Clip Downloader Online | TwitchCutter">
  <meta property="twitter:description" content="Cut, trim &amp; download Twitch VODs by timestamp. 1080p60 MP4, no watermark, 100% free online tool.">
  <meta property="twitter:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">

  <!-- Google Structured Data: WebApplication -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "TwitchCutter",
    "url": "https://twitchcutter.pages.dev/",
    "description": "Free online Twitch VOD cutter and clip downloader. Slice any segment by start and end timestamp with live preview, 1080p quality, and no watermarks.",
    "applicationCategory": "MultimediaApplication",
    "operatingSystem": "All",
    "browserRequirements": "Requires JavaScript",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "TwitchCutter",
      "url": "https://twitchcutter.pages.dev/"
    }}
  }}
  </script>

  <!-- Google Structured Data: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://twitchcutter.pages.dev/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Twitch Clip Cutter",
        "item": "https://twitchcutter.pages.dev/twitch-clip-cutter"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "Twitch VOD Downloader",
        "item": "https://twitchcutter.pages.dev/twitch-vod-downloader"
      }}
    ]
  }}
  </script>

  <!-- Google Structured Data: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How do I cut a Twitch VOD online by timestamp?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Paste any Twitch VOD URL into TwitchCutter, click Fetch Stream, set your start and end timestamps using the visual dual slider or manual time boxes, then click Cut & Download Clip. Only the selected segment will download as an MP4."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I clip longer than 60 seconds on Twitch?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes! Twitch's native clipping button caps clips at 60 seconds. TwitchCutter removes this limit, letting you cut clips from 5 seconds to over 2 hours from any public VOD."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How long do Twitch VODs last before expiring?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Standard Twitch broadcasters' VODs expire in 7 days. Affiliates have 14 days, while Partners, Prime, and Turbo users get 60 days before past broadcasts are deleted."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Does TwitchCutter add any watermark to clips?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "No. All MP4 video downloads are 100% clean and watermark-free, preserving the streamer's original broadcast quality up to 1080p60."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Is TwitchCutter free to use?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "TwitchCutter is 100% free with no registration, no subscription, and no software download required."
        }}
      }}
    ]
  }}
  </script>

  <!-- HLS.js for interactive stream preview -->
  <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

  <style>
{COMMON_CSS}
  </style>
</head>
<body>
  <div class="ambient-glow"></div>

{HEADER_HTML}

  <main>
{get_tool_html(
  'Cut Twitch Streams &amp; VODs <br><span class="highlight">By Exact Timestamps</span>',
  'Paste any Twitch VOD, clip, or stream link. Visually choose start and end times, and download an original 1080p60 MP4 without downloading giant 30GB files.',
  'Paste Twitch URL (e.g. https://www.twitch.tv/videos/12345678 or clip link)...'
)}

    <!-- How It Works Section -->
    <section class="steps-section">
      <h2 class="section-title">How to Cut &amp; Download Twitch VODs in 3 Steps</h2>
      <p class="section-subtitle">No software, no heavy downloads, no complicated setup. Just paste, select timestamps, and download.</p>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <h3>Paste Twitch URL</h3>
          <p>Copy the link of any public Twitch VOD, livestream, or clip and click <strong>Fetch Stream</strong>. The video info, live player preview, and available resolutions load immediately.</p>
        </div>
        <div class="step-card">
          <div class="step-num">2</div>
          <h3>Set Clip Timestamps</h3>
          <p>Drag the dual range scrubber or type exact start and end times (e.g. 01:15:00 to 01:18:30). Use the nudge buttons or quick add shortcuts (+1 min, +5 min) to fine-tune.</p>
        </div>
        <div class="step-card">
          <div class="step-num">3</div>
          <h3>Export 1080p MP4</h3>
          <p>Click <strong>Cut &amp; Download Clip</strong>. Our cloud engine slices only your selected stream segments — saving your bandwidth and hard drive space. Zero watermark.</p>
        </div>
      </div>
    </section>

    <!-- Why TwitchCutter Features -->
    <section class="features-section">
      <h2 class="section-title">Why TwitchCutter Is the Best Twitch VOD &amp; Clip Cutter</h2>
      <p class="section-subtitle">Engineered specifically for esports editors, YouTube Shorts creators, and Twitch fans.</p>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">⏱️</div>
          <h3>Break the 60-Second Limit</h3>
          <p>Twitch's native clipping button limits you to 60 seconds. TwitchCutter lets you cut clips of any length — 2 minutes, 10 minutes, or even a full 2-hour tournament match.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🚀</div>
          <h3>Server-Side Stream Slicing</h3>
          <p>Never download a 30 GB 10-hour VOD just to get a 30-second funny moment. Our backend downloads and splices only the exact chunks you request.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">✨</div>
          <h3>100% Watermark Free</h3>
          <p>Get clean, pristine MP4 video files ready to edit in Premiere Pro, DaVinci Resolve, or upload straight to TikTok and YouTube Shorts.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🎯</div>
          <h3>1080p60 Source Quality</h3>
          <p>Preserve high-framerate gameplay. If the streamer broadcasted in 1080p at 60 FPS, your output clip will match that exact crystal-clear quality.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📱</div>
          <h3>Works on iPhone &amp; Android</h3>
          <p>No desktop apps or FFmpeg commands needed. TwitchCutter runs smoothly directly inside mobile Safari, Chrome, and desktop browsers.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔒</div>
          <h3>No Account &amp; No Login</h3>
          <p>Zero friction. You do not need to link your Twitch account or enter any login credentials. Just paste and cut instantly.</p>
        </div>
      </div>
    </section>

    <!-- Categorized FAQ Section -->
    <section class="faq-section">
      <h2 class="section-title">Twitch VOD &amp; Clip Cutter — FAQ</h2>
      <p class="section-subtitle">Common questions about cutting Twitch VODs, downloading clips, and saving past broadcasts.</p>

      <div class="faq-tabs">
        <button class="faq-tab-btn active" onclick="switchFaqTab('tab-cutter', this)">✂️ Cutting &amp; Trimming</button>
        <button class="faq-tab-btn" onclick="switchFaqTab('tab-downloader', this)">📥 VOD Downloading</button>
        <button class="faq-tab-btn" onclick="switchFaqTab('tab-tech', this)">⚙️ Quality &amp; Tech</button>
        <button class="faq-tab-btn" onclick="switchFaqTab('tab-privacy', this)">🔒 Legal &amp; DMCA</button>
      </div>

      <!-- Tab 1: Cutting & Trimming -->
      <div id="tab-cutter" class="faq-pane active">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How do I download part of a Twitch VOD? <span>+</span></div>
          <div class="faq-a">To download part of a Twitch VOD: (1) Copy the Twitch VOD URL and paste it into TwitchCutter. (2) Click Fetch Stream. (3) Set your start and end timestamps using the slider or type them in. (4) Click Cut &amp; Download Clip. Only that selected portion is sliced and exported as an MP4.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I clip longer than 60 seconds on Twitch? <span>+</span></div>
          <div class="faq-a">Yes! Twitch's native clip creator limits clips to a maximum of 60 seconds. TwitchCutter removes this limitation entirely, letting you slice any length from 5 seconds up to 2 hours from any public VOD.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I cut a Twitch VOD without downloading the full video? <span>+</span></div>
          <div class="faq-a">Yes, that is TwitchCutter's core superpower. Because 8-hour Twitch VODs can exceed 25–40 GB, downloading the whole file is painful. Our cloud server extracts only the HLS segments matching your start and end times, saving your bandwidth and time.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How do I trim a Twitch stream online? <span>+</span></div>
          <div class="faq-a">TwitchCutter is a free online Twitch stream trimmer. Open TwitchCutter in your browser, enter the broadcast link, use the interactive dual slider to set your in and out points, and download your trimmed clip as an MP4.</div>
        </div>
      </div>

      <!-- Tab 2: VOD Downloading -->
      <div id="tab-downloader" class="faq-pane">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How long do Twitch VODs last before getting deleted? <span>+</span></div>
          <div class="faq-a">Twitch VOD expiration periods are: Standard streamers: 7 days. Twitch Affiliates: 14 days. Twitch Partners, Turbo, and Prime members: 60 days. Once expired, Twitch permanently deletes past broadcasts. Use TwitchCutter to save your favorite streams before they disappear!</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How do I download a Twitch VOD? <span>+</span></div>
          <div class="faq-a">Paste the Twitch VOD link into TwitchCutter and click Fetch Stream. Set the start timestamp to 00:00:00 and the end timestamp to the full duration of the stream, pick your resolution (1080p, 720p), and click Cut &amp; Download Clip.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I download someone else's Twitch VOD? <span>+</span></div>
          <div class="faq-a">Yes, you can download clips or segments from any public Twitch VOD or stream. Note that subscriber-only VODs require channel subscription credentials and are not publicly scrapable.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Do Twitch clips expire like VODs do? <span>+</span></div>
          <div class="faq-a">No, Twitch clips do not automatically expire like VODs do. However, streamers can manually delete clips or delete the source VOD, which can occasionally orphan clips. Saving them as local MP4 files guarantees you never lose them.</div>
        </div>
      </div>

      <!-- Tab 3: Tech & Quality -->
      <div id="tab-tech" class="faq-pane">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I download Twitch clips in 1080p 60FPS? <span>+</span></div>
          <div class="faq-a">Yes! TwitchCutter automatically queries all broadcast resolutions provided by Twitch's HLS streams. You can download clips in 1080p60 Full HD, 720p60 HD, 480p, or 360p.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">What video format does TwitchCutter export? <span>+</span></div>
          <div class="faq-a">All clips are packaged in universal H.264 MP4 format with AAC audio. This ensures instant compatibility with Windows, Mac, iOS, Android, DaVinci Resolve, Adobe Premiere Pro, and CapCut.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Do I need to install FFmpeg, Python, or extensions? <span>+</span></div>
          <div class="faq-a">No. All stream slicing, FFmpeg processing, and packaging happen remotely in our high-speed cloud infrastructure. You just click download.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Does TwitchCutter work on mobile phones? <span>+</span></div>
          <div class="faq-a">Yes! TwitchCutter is designed to be mobile-first and responsive. You can paste a Twitch link in mobile Safari on iPhone or Chrome on Android and save MP4 clips straight to your device gallery.</div>
        </div>
      </div>

      <!-- Tab 4: Legal & DMCA -->
      <div id="tab-privacy" class="faq-pane">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Is TwitchCutter legal to use? <span>+</span></div>
          <div class="faq-a">Yes. Using TwitchCutter to create clips and save moments for personal archiving or fair-use commentary and transformative editing is generally acceptable. Always respect streamers' intellectual property and credit original creators when reposting content.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Why are parts of some Twitch VODs muted? <span>+</span></div>
          <div class="faq-a">Twitch has an automated Audible Magic system that scans streams for copyrighted music and mutes offending audio sections in the VOD. If a section is muted on Twitch, any downloaded clip of that section will also be muted because the source audio was permanently stripped.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Is TwitchCutter affiliated with Twitch.tv or Amazon? <span>+</span></div>
          <div class="faq-a">No. TwitchCutter is an independent open-source web application designed for gaming editors and fans. It is not affiliated with, endorsed by, or sponsored by Twitch Interactive, Inc. or Amazon.com.</div>
        </div>
      </div>
    </section>

    <!-- SEO Content Section -->
    <section class="seo-article">
      <h2>Free Online Twitch VOD Cutter &amp; Clip Downloader</h2>
      <p>
        <strong>TwitchCutter</strong> is the ultimate free online utility for gamers, esports video editors, and content creators looking to <strong>cut Twitch VODs by timestamp</strong> and <strong>download Twitch clips without watermarks</strong>. Whether you need a 15-second clutch moment for TikTok, a 2-minute tournament highlight for YouTube Shorts, or want to archive a full past broadcast before it gets deleted, TwitchCutter makes it seamless and lightning fast.
      </p>

      <h3>Why Use a Dedicated Twitch VOD Cutter?</h3>
      <p>
        Twitch livestreams frequently last between 6 and 12 hours. A standard high-bitrate 1080p60 broadcast can easily result in a raw video file exceeding <strong>20 GB to 40 GB</strong>. Downloading an entire broadcast just to edit a single two-minute highlight is a massive waste of bandwidth, time, and hard drive space.
      </p>
      <p>
        TwitchCutter solves this problem with <strong>server-side stream slicing</strong>. When you input your desired start and end timestamps (for example, from <code>01:23:45</code> to <code>01:26:10</code>), our cloud backend queries the exact HLS video segments and splices only those seconds into a pristine MP4 file. You download only the file you actually need.
      </p>

      <h3>How to Clip Longer Than 60 Seconds on Twitch</h3>
      <p>
        Twitch's built-in clip button has a hard restriction: clips cannot exceed <strong>60 seconds</strong>. For esports highlights, funny team comms, or lengthy story times, 60 seconds is rarely enough. TwitchCutter allows creators to bypass this limitation completely. Simply paste the VOD URL and specify any duration — from 5 seconds to over 2 hours — and download the full uncut moment in source 1080p resolution.
      </p>

      <h3>The Modern Untwitch Alternative</h3>
      <p>
        For years, users relied on older utilities like Untwitch to download stream segments. However, older tools frequently suffer from 1-hour length caps, intrusive advertisements, slow queue times, and a lack of interactive video player previews. TwitchCutter was built from the ground up as a modern alternative, featuring a real-time HLS video preview player, dual range scrubber, and zero artificial length limits.
      </p>
    </section>
  </main>

{FOOTER_HTML}

  <script>
{TOOL_JS}
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("index.html created.")


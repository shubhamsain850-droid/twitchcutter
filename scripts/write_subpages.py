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
# 2. TWITCH-CLIP-CUTTER.HTML
# ==============================================================================
clip_cutter_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Twitch Clip Cutter Online — 1080p MP4, No Watermark | TwitchCutter</title>
  <meta name="title" content="Free Twitch Clip Cutter Online — 1080p MP4, No Watermark | TwitchCutter">
  <meta name="description" content="Free online Twitch clip cutter and downloader. Download Twitch clips in 1080p MP4 with no watermark, or cut longer clips beyond the 60-second limit. No login required.">
  <meta name="keywords" content="twitch clip cutter, twitch clip downloader, download twitch clips, twitch clip downloader mp4, download twitch clips without watermark, twitch clip 1080p, clip longer than 60 seconds twitch, save twitch clips">
  <meta name="author" content="TwitchCutter">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://twitchcutter.pages.dev/twitch-clip-cutter">

{FAVICON_HEAD}

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://twitchcutter.pages.dev/twitch-clip-cutter">
  <meta property="og:title" content="Free Twitch Clip Cutter Online — 1080p MP4, No Watermark | TwitchCutter">
  <meta property="og:description" content="Download and cut Twitch clips in original 1080p quality. No watermark, no software, bypass the 60s limit.">
  <meta property="og:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">
  <meta property="og:site_name" content="TwitchCutter">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://twitchcutter.pages.dev/twitch-clip-cutter">
  <meta property="twitter:title" content="Free Twitch Clip Cutter Online — 1080p MP4 | TwitchCutter">
  <meta property="twitter:description" content="Download and trim Twitch clips without watermarks in 1080p MP4. Free online tool.">
  <meta property="twitter:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">

  <!-- BreadcrumbList Schema -->
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
      }}
    ]
  }}
  </script>

  <!-- WebApplication Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Twitch Clip Cutter — TwitchCutter",
    "url": "https://twitchcutter.pages.dev/twitch-clip-cutter",
    "description": "Download and trim Twitch clips in 1080p MP4 without watermarks. Free online tool to bypass Twitch's 60-second clip cap.",
    "applicationCategory": "MultimediaApplication",
    "operatingSystem": "All",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }}
  }}
  </script>

  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How do I download a Twitch clip as MP4?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Copy the clip URL from Twitch, paste it into TwitchCutter, click Fetch Stream, and click Download. You will receive an unbranded 1080p MP4 file directly to your device."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How do I make a Twitch clip longer than 60 seconds?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Twitch's clip button has a hard 60-second cap. To capture a longer segment, paste the full VOD link into TwitchCutter, set any start and end time (up to 2 hours), and download your extended clip in MP4."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Does TwitchCutter add any watermark to clips?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "No. All downloaded clips are 100% clean with zero watermarks or credit overlays, ready for editing or posting to social media."
        }}
      }}
    ]
  }}
  </script>

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
  'Twitch Clip Cutter &amp; Downloader <br><span class="highlight">1080p MP4, No Watermark</span>',
  'Download pre-made Twitch clips instantly or slice custom long clips directly from past broadcasts. Clean, unbranded MP4 export in source quality.',
  'Paste Twitch clip or VOD link (e.g. https://www.twitch.tv/streamer/clip/Abc123Xyz)...'
)}

    <!-- Steps -->
    <section class="steps-section">
      <h2 class="section-title">How to Cut &amp; Download Twitch Clips</h2>
      <p class="section-subtitle">Get your clip in crisp 1080p60 MP4 in seconds.</p>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <h3>Paste Clip or VOD Link</h3>
          <p>Copy the link of any Twitch clip or full broadcast VOD and paste it into the search box above. Click <strong>Fetch Stream</strong>.</p>
        </div>
        <div class="step-card">
          <div class="step-num">2</div>
          <h3>Choose Length &amp; Quality</h3>
          <p>Download the clip as-is or adjust timestamps to capture extra context before or after the moment. Select up to 1080p60 Full HD.</p>
        </div>
        <div class="step-card">
          <div class="step-num">3</div>
          <h3>Download MP4 Instantly</h3>
          <p>Click <strong>Cut &amp; Download Clip</strong>. Save a clean, watermark-free MP4 directly to your computer or phone camera roll.</p>
        </div>
      </div>
    </section>

    <!-- Clip Specific FAQs -->
    <section class="faq-section">
      <h2 class="section-title">Twitch Clip Cutter — FAQs</h2>
      <p class="section-subtitle">Answers to the most common questions about downloading and clipping Twitch moments.</p>

      <div class="faq-pane active">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How do I download a Twitch clip on my phone (iPhone / Android)? <span>+</span></div>
          <div class="faq-a">Open Safari on iPhone or Chrome on Android, visit twitchcutter.pages.dev/twitch-clip-cutter, paste your Twitch clip URL, and tap Download. On iOS, tap the download icon in Safari and save to Files or your Photos app.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How do I clip longer than 60 seconds on Twitch? <span>+</span></div>
          <div class="faq-a">Twitch strictly caps native clips at 60 seconds. With TwitchCutter, simply open the streamer's VOD, copy the VOD link, and set your desired in/out timestamps. You can slice clips of 2 minutes, 5 minutes, 30 minutes, or longer with zero restrictions.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Are clips downloaded with audio? <span>+</span></div>
          <div class="faq-a">Yes! All downloaded clips include full stereo high-bitrate game and microphone audio, perfectly synchronized with video. If a portion was muted by Twitch due to DMCA music, that specific section will remain muted in the source.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I download deleted Twitch clips? <span>+</span></div>
          <div class="faq-a">If a clip has been completely purged from Twitch's CDN servers by the streamer, it cannot be downloaded. We recommend clipping and downloading memorable moments as soon as they happen.</div>
        </div>
      </div>
    </section>

    <!-- SEO Content -->
    <section class="seo-article">
      <h2>Free Online Twitch Clip Downloader &amp; Cutter</h2>
      <p>
        Twitch clips are the lifeblood of gaming culture — from insane esports aces in CS2 and Valorant to hilarious moments in GTA RP and Just Chatting. However, Twitch does not provide an official download button for viewers, and the built-in clipping tool strictly limits recordings to 60 seconds.
      </p>
      <p>
        <strong>TwitchCutter's Clip Cutter</strong> gives you complete control over Twitch video content. You can download any pre-made clip with a single click, or paste a full VOD URL to extract extended moments that exceed Twitch's 60-second limit.
      </p>
      <h3>Zero Watermarks &bull; Ready for TikTok &amp; YouTube Shorts</h3>
      <p>
        Many online downloaders slap unwanted brand watermarks onto your videos. TwitchCutter keeps every export 100% clean and pristine. Download your MP4 files in full 1080p at 60 frames per second, drop them straight into CapCut, Premiere Pro, or DaVinci Resolve, reformat to 9:16 vertical video, and post to TikTok, Instagram Reels, and YouTube Shorts.
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

with open(os.path.join(BASE_DIR, "twitch-clip-cutter.html"), "w", encoding="utf-8") as f:
    f.write(clip_cutter_html)
print("twitch-clip-cutter.html created.")

# ==============================================================================
# 3. TWITCH-VOD-DOWNLOADER.HTML
# ==============================================================================
vod_downloader_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Twitch VOD Downloader Online — Save Past Broadcasts | TwitchCutter</title>
  <meta name="title" content="Free Twitch VOD Downloader Online — Save Past Broadcasts | TwitchCutter">
  <meta name="description" content="Download Twitch VODs and past broadcasts online for free before they expire. Cut any segment by timestamp or save full streams in 1080p MP4. No software required.">
  <meta name="keywords" content="twitch vod downloader, download twitch vod, download part of twitch vod, twitch stream downloader, save twitch vod before expires, download twitch broadcast, untwitch alternative, twitch vod to mp4">
  <meta name="author" content="TwitchCutter">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://twitchcutter.pages.dev/twitch-vod-downloader">

{FAVICON_HEAD}

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://twitchcutter.pages.dev/twitch-vod-downloader">
  <meta property="og:title" content="Free Twitch VOD Downloader Online — Save Past Broadcasts | TwitchCutter">
  <meta property="og:description" content="Download Twitch VODs before they get deleted. Cut any section by timestamp or download full streams as 1080p MP4. Free &amp; no watermark.">
  <meta property="og:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">
  <meta property="og:site_name" content="TwitchCutter">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://twitchcutter.pages.dev/twitch-vod-downloader">
  <meta property="twitter:title" content="Free Twitch VOD Downloader Online | TwitchCutter">
  <meta property="twitter:description" content="Download Twitch past broadcasts before they expire. Free, no watermark, fast cloud slicing.">
  <meta property="twitter:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">

  <!-- BreadcrumbList Schema -->
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
        "name": "Twitch VOD Downloader",
        "item": "https://twitchcutter.pages.dev/twitch-vod-downloader"
      }}
    ]
  }}
  </script>

  <!-- WebApplication Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Twitch VOD Downloader — TwitchCutter",
    "url": "https://twitchcutter.pages.dev/twitch-vod-downloader",
    "description": "Download and slice Twitch VODs (past broadcasts) before they expire. Save any segment by timestamp as 1080p MP4.",
    "applicationCategory": "MultimediaApplication",
    "operatingSystem": "All",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }}
  }}
  </script>

  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How long do Twitch VODs last before being deleted?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Twitch automatically deletes past broadcasts after 7 days for standard streamers, 14 days for Twitch Affiliates, and 60 days for Twitch Partners, Turbo, and Prime Gaming members."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How do I download part of a Twitch VOD?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Paste the VOD link into TwitchCutter, select your desired start and end timestamps, and click Cut & Download. Our server slices only that segment, saving you from downloading a massive 30GB file."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I download full Twitch VODs?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes! Set the start time to 00:00:00 and end time to the full stream duration, pick your resolution (up to 1080p), and download the broadcast as an MP4."
        }}
      }}
    ]
  }}
  </script>

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
  'Twitch VOD Downloader <br><span class="highlight">Save Streams Before They Expire</span>',
  'Download Twitch past broadcasts before the 7 to 60 day expiration timer runs out. Cut any segment by timestamp or save full streams as 1080p MP4.',
  'Paste Twitch VOD URL (e.g. https://www.twitch.tv/videos/2914038727)...'
)}

    <!-- Expiration Table -->
    <section class="seo-article" style="margin-top: 2rem;">
      <h2 style="text-align: center; margin-bottom: 1.5rem;">Twitch VOD Expiration Schedule — When Do Streams Delete?</h2>
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem;">
          <thead>
            <tr style="border-bottom: 2px solid var(--card-border); color: #fff;">
              <th style="padding: 0.75rem 1rem;">Broadcaster Tier</th>
              <th style="padding: 0.75rem 1rem;">VOD Storage Duration</th>
              <th style="padding: 0.75rem 1rem;">What Happens After?</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem 1rem; color: #fff; font-weight: 600;">Regular Broadcaster</td>
              <td style="padding: 0.75rem 1rem; color: #ff6b6b; font-weight: 700;">7 Days</td>
              <td style="padding: 0.75rem 1rem;">Permanently deleted from Twitch servers</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem 1rem; color: #fff; font-weight: 600;">Twitch Affiliate</td>
              <td style="padding: 0.75rem 1rem; color: #ffb86c; font-weight: 700;">14 Days</td>
              <td style="padding: 0.75rem 1rem;">Permanently deleted from Twitch servers</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem 1rem; color: #fff; font-weight: 600;">Twitch Partner / Prime / Turbo</td>
              <td style="padding: 0.75rem 1rem; color: var(--green-success); font-weight: 700;">60 Days</td>
              <td style="padding: 0.75rem 1rem;">Permanently deleted unless highlighted or exported</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top: 1rem; font-size: 0.88rem; color: var(--text-muted); text-align: center;">
        💡 <em>Pro Tip: Use TwitchCutter to archive your favorite streams to MP4 before they hit the expiration date!</em>
      </p>
    </section>

    <!-- FAQs -->
    <section class="faq-section">
      <h2 class="section-title">Twitch VOD Downloader — Frequently Asked Questions</h2>
      <p class="section-subtitle">Everything you need to know about archiving past broadcasts.</p>

      <div class="faq-pane active">
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I download a Twitch VOD after it was deleted? <span>+</span></div>
          <div class="faq-a">No. Once Twitch's storage window closes or a streamer deletes a VOD, the files are permanently purged from Twitch's HLS CDN. There is no official recovery method. You should always download important VODs before the deadline.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">Can I download subscriber-only Twitch VODs? <span>+</span></div>
          <div class="faq-a">No. If a streamer has enabled "Subscriber-Only VODs", Twitch restricts access behind authenticated user sessions. TwitchCutter operates anonymously without requiring your login, so only publicly accessible VODs can be fetched and downloaded.</div>
        </div>
        <div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">How long does it take to download a Twitch VOD? <span>+</span></div>
          <div class="faq-a">Short clips under 5 minutes typically process within 10 to 20 seconds. Slicing longer segments (e.g. 1 hour) depends on stream resolution and backend processing load, but is dramatically faster than downloading the entire 30GB broadcast file.</div>
        </div>
      </div>
    </section>
  </main>

{FOOTER_HTML}

  <script>
{TOOL_JS}
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "twitch-vod-downloader.html"), "w", encoding="utf-8") as f:
    f.write(vod_downloader_html)
print("twitch-vod-downloader.html created.")


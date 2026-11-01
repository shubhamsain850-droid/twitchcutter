import os
import sys

BASE_DIR = r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend"
BLOG_DIR = os.path.join(BASE_DIR, "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

sys.path.append(r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\scripts")
from common_elements import LOGO_SVG, HEADER_HTML, FOOTER_HTML, FAVICON_HEAD
from build_full_site import COMMON_CSS

# ==============================================================================
# 10. BLOG/INDEX.HTML (GUIDES HUB)
# ==============================================================================
blog_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Twitch Video Guides &amp; Tutorials | TwitchCutter Blog</title>
  <meta name="title" content="Twitch Video Guides &amp; Tutorials | TwitchCutter Blog">
  <meta name="description" content="In-depth guides on cutting Twitch VODs, making clips longer than 60 seconds, saving streams before they expire, and best editing practices.">
  <link rel="canonical" href="https://twitchcutter.pages.dev/blog/">
{FAVICON_HEAD}
  <style>{COMMON_CSS}
    .blog-card {{
      background: var(--bg-card);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      text-decoration: none;
      color: inherit;
    }}
    .blog-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(145, 70, 255, 0.4);
    }}
    .blog-tag {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      color: #bf94ff;
      background: rgba(145, 70, 255, 0.15);
      padding: 0.2rem 0.6rem;
      border-radius: 999px;
      align-self: flex-start;
    }}
    .blog-card h2 {{
      font-size: 1.35rem;
      color: #fff;
      margin: 0;
    }}
    .blog-card p {{
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.6;
      margin: 0;
    }}
    .blog-meta {{
      font-size: 0.8rem;
      color: #64748b;
    }}
  </style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <section class="hero">
      <div class="hero-pill">📚 Knowledge Base</div>
      <h1>Twitch Video Guides &amp; Tutorials</h1>
      <p>Master Twitch clipping, stream archiving, VOD trimming, and content repurposing for TikTok, Reels, and YouTube Shorts.</p>
    </section>

    <div style="max-width: 820px; margin: 0 auto;">
      <a href="/blog/how-to-clip-longer-than-60-seconds-twitch.html" class="blog-card">
        <span class="blog-tag">Clipping Guide</span>
        <h2>How to Clip Longer Than 60 Seconds on Twitch (Complete 2024 Guide)</h2>
        <p>Twitch's native clip tool strictly caps you at 60 seconds. Learn how to effortlessly capture 2-minute, 5-minute, or 30-minute highlights from any VOD without software.</p>
        <span class="blog-meta">5 min read &bull; Nov 2026 &bull; By TwitchCutter Team</span>
      </a>

      <a href="/blog/download-twitch-vod-before-expires.html" class="blog-card">
        <span class="blog-tag">VOD Archiving</span>
        <h2>How to Download Twitch VODs Before They Expire &amp; Get Deleted</h2>
        <p>Twitch deletes past broadcasts after 7, 14, or 60 days. Understand the expiration schedule and learn the fastest way to save streams before they're gone forever.</p>
        <span class="blog-meta">6 min read &bull; Nov 2026 &bull; By TwitchCutter Team</span>
      </a>

      <a href="/blog/untwitch-alternative.html" class="blog-card">
        <span class="blog-tag">Tool Comparison</span>
        <h2>Best Untwitch Alternative in 2024: Why Editors Are Switching to TwitchCutter</h2>
        <p>Tired of Untwitch's 1-hour length cap, missing video preview, and slow downloads? Discover why TwitchCutter is the ultimate modern alternative for video creators.</p>
        <span class="blog-meta">4 min read &bull; Nov 2026 &bull; By TwitchCutter Team</span>
      </a>
    </div>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(blog_index_html)
print("blog/index.html created.")

# ==============================================================================
# 11. BLOG 1: HOW TO CLIP LONGER THAN 60 SECONDS
# ==============================================================================
blog1_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How to Clip Longer Than 60 Seconds on Twitch (2024 Guide) | TwitchCutter</title>
  <meta name="title" content="How to Clip Longer Than 60 Seconds on Twitch (2024 Guide) | TwitchCutter">
  <meta name="description" content="Learn how to clip longer than 60 seconds on Twitch for free. Step-by-step tutorial on capturing extended moments and tournament highlights in 1080p MP4.">
  <meta name="keywords" content="how to clip longer than 60 seconds twitch, twitch clip longer than 60 seconds, bypass twitch 60 second clip limit, twitch clip limit workaround, long twitch clips">
  <link rel="canonical" href="https://twitchcutter.pages.dev/blog/how-to-clip-longer-than-60-seconds-twitch.html">
{FAVICON_HEAD}

  <!-- Article Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "How to Clip Longer Than 60 Seconds on Twitch (2024 Guide)",
    "description": "Twitch limits clips to 60 seconds. Here is the easiest way to cut clips of any length from any Twitch VOD.",
    "author": {{
      "@type": "Organization",
      "name": "TwitchCutter"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "TwitchCutter",
      "url": "https://twitchcutter.pages.dev"
    }},
    "datePublished": "2026-11-01"
  }}
  </script>

  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <article class="seo-article" style="max-width: 820px; margin: 2rem auto;">
      <div style="font-size: 0.85rem; color: #bf94ff; font-weight: 700; margin-bottom: 0.5rem;">TUTORIAL &amp; GUIDE</div>
      <h1 style="font-size: 2.2rem; line-height: 1.25; margin-bottom: 1rem; color: #fff;">How to Clip Longer Than 60 Seconds on Twitch</h1>
      <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 2rem;">Published Nov 2026 &bull; 5 min read &bull; By TwitchCutter Team</div>

      <p>
        If you have ever tried clipping an intense CS2 overtime clutch, a hilarious 5-minute story, or a lengthy roleplay scene on Twitch, you have inevitably slammed into Twitch's biggest restriction: <strong>the 60-second clip cap</strong>.
      </p>
      <p>
        Twitch's native clipping button (Alt + X) only allows users to capture between 5 and 60 seconds of video. For complex gaming plays, creator banter, and esports highlights, 60 seconds is nowhere near enough time.
      </p>

      <h3>Why Does Twitch Have a 60-Second Limit?</h3>
      <p>
        Twitch introduced the 60-second limit to optimize server bandwidth and encourage quick virality across social feeds. While 60 seconds works fine for single funny jokes, it actively hinders video editors, TikTok content creators, and tournament archivists who need multi-minute footage.
      </p>

      <h3>The Solution: Clip from the VOD Using TwitchCutter</h3>
      <p>
        You do not need to settle for 60 seconds, nor do you need to download a 30 GB full broadcast file. By using <strong>TwitchCutter</strong>, you can extract any length clip directly from the broadcaster's past broadcast (VOD).
      </p>

      <h3>Step-by-Step: Cutting Long Clips with TwitchCutter</h3>
      <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-muted); line-height: 1.8;">
        <li><strong>Find the Stream VOD:</strong> Go to the creator's Twitch channel, click on the <em>Videos</em> tab, and open the past broadcast where the moment occurred.</li>
        <li><strong>Copy the VOD URL:</strong> Copy the URL from your address bar (e.g. <code>https://www.twitch.tv/videos/123456789</code>).</li>
        <li><strong>Open TwitchCutter:</strong> Navigate to <a href="/" style="color:var(--accent); font-weight:600;">TwitchCutter Homepage</a> and paste the link into the search box.</li>
        <li><strong>Set Exact Timestamps:</strong> Use the interactive player and dual range scrubber to set your start time and end time. You can choose a 2-minute, 5-minute, or even 45-minute span!</li>
        <li><strong>Click Cut &amp; Download:</strong> Choose your quality (up to 1080p60) and hit <em>Cut &amp; Download Clip</em>. Our server slices only that segment and downloads a watermark-free MP4.</li>
      </ol>

      <div style="background: rgba(145, 70, 255, 0.1); border: 1px solid rgba(145, 70, 255, 0.3); border-radius: 12px; padding: 1.5rem; margin: 2rem 0; text-align: center;">
        <h3 style="margin-top:0; color:#fff;">Ready to make an extended Twitch clip?</h3>
        <p style="margin-bottom:1.25rem;">Cut any length clip in 1080p MP4 with zero watermarks now.</p>
        <a href="/" class="cut-btn" style="display:inline-flex; text-decoration:none;">Try TwitchCutter Free</a>
      </div>

      <h3>Alternative Workarounds Compared</h3>
      <p>
        Other methods include using OBS Replay Buffer (which only works if you're the one streaming) or downloading the full 10-hour VOD via command-line yt-dlp (which eats up 30 GB of storage and takes hours to download). TwitchCutter offers the best balance: zero software required and server-side stream slicing in seconds.
      </p>
    </article>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BLOG_DIR, "how-to-clip-longer-than-60-seconds-twitch.html"), "w", encoding="utf-8") as f:
    f.write(blog1_html)
print("blog 1 created.")

# ==============================================================================
# 12. BLOG 2: DOWNLOAD TWITCH VOD BEFORE EXPIRES
# ==============================================================================
blog2_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How to Download Twitch VODs Before They Expire (2024 Guide) | TwitchCutter</title>
  <meta name="title" content="How to Download Twitch VODs Before They Expire (2024 Guide) | TwitchCutter">
  <meta name="description" content="Twitch deletes past broadcasts after 7, 14, or 60 days. Learn how to save your favorite streams before they get deleted permanently.">
  <meta name="keywords" content="download twitch vod before expires, how long do twitch vods last, twitch vod deletion policy, save twitch stream before deleted, twitch vod expiration time">
  <link rel="canonical" href="https://twitchcutter.pages.dev/blog/download-twitch-vod-before-expires.html">
{FAVICON_HEAD}

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "How to Download Twitch VODs Before They Expire (2024 Guide)",
    "description": "Twitch VOD expiration schedule and how to download broadcasts before they are deleted.",
    "author": {{
      "@type": "Organization",
      "name": "TwitchCutter"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "TwitchCutter",
      "url": "https://twitchcutter.pages.dev"
    }},
    "datePublished": "2026-11-01"
  }}
  </script>

  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <article class="seo-article" style="max-width: 820px; margin: 2rem auto;">
      <div style="font-size: 0.85rem; color: #bf94ff; font-weight: 700; margin-bottom: 0.5rem;">VOD ARCHIVING</div>
      <h1 style="font-size: 2.2rem; line-height: 1.25; margin-bottom: 1rem; color: #fff;">How to Download Twitch VODs Before They Expire &amp; Get Deleted</h1>
      <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 2rem;">Published Nov 2026 &bull; 6 min read &bull; By TwitchCutter Team</div>

      <p>
        Every week, millions of hours of iconic livestream moments, esports tournaments, and memorable broadcasts are permanently deleted from Twitch forever. Many creators and fans only realize a stream has disappeared weeks later when it's already too late.
      </p>

      <h3>How Long Do Twitch VODs Actually Last?</h3>
      <p>
        Twitch does not store past broadcasts indefinitely. Storage periods depend strictly on the streamer's subscription and partnership tier:
      </p>
      <ul>
        <li><strong>Standard Broadcasters:</strong> VODs are stored for only <strong>7 days</strong> before automated deletion.</li>
        <li><strong>Twitch Affiliates:</strong> VODs are stored for <strong>14 days</strong>.</li>
        <li><strong>Twitch Partners, Turbo &amp; Prime Members:</strong> VODs are kept for <strong>60 days</strong>.</li>
      </ul>

      <h3>Can Deleted Twitch VODs Be Recovered?</h3>
      <p>
        <strong>No.</strong> Once Twitch's automated deletion worker triggers, the video files and HLS playlists are permanently removed from Twitch's cloud storage infrastructure. Neither Twitch support nor third-party scrapers can recover deleted broadcasts unless someone exported it to YouTube beforehand.
      </p>

      <h3>How to Save VODs with TwitchCutter</h3>
      <p>
        With <a href="/twitch-vod-downloader" style="color:var(--accent); font-weight:600;">TwitchCutter's VOD Downloader</a>, you can download the entire stream or slice specific memorable segments without hassle:
      </p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-muted); line-height: 1.8;">
        <li>Copy the VOD link from Twitch before the expiration deadline.</li>
        <li>Paste the URL into TwitchCutter and click <em>Fetch Stream</em>.</li>
        <li>Choose whether to save the entire broadcast or trim out the pre-stream intro and ending screens.</li>
        <li>Select 1080p60 Full HD and click <em>Cut &amp; Download Clip</em>.</li>
      </ol>

      <div style="background: rgba(145, 70, 255, 0.1); border: 1px solid rgba(145, 70, 255, 0.3); border-radius: 12px; padding: 1.5rem; margin: 2rem 0; text-align: center;">
        <h3 style="margin-top:0; color:#fff;">Save your favorite stream today</h3>
        <p style="margin-bottom:1.25rem;">Download any Twitch VOD as a high-quality 1080p MP4 before it expires.</p>
        <a href="/twitch-vod-downloader" class="cut-btn" style="display:inline-flex; text-decoration:none;">Go to VOD Downloader</a>
      </div>
    </article>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BLOG_DIR, "download-twitch-vod-before-expires.html"), "w", encoding="utf-8") as f:
    f.write(blog2_html)
print("blog 2 created.")

# ==============================================================================
# 13. BLOG 3: UNTWITCH ALTERNATIVE
# ==============================================================================
blog3_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Best Untwitch Alternative 2024: Free Twitch VOD Cutter | TwitchCutter</title>
  <meta name="title" content="Best Untwitch Alternative 2024: Free Twitch VOD Cutter | TwitchCutter">
  <meta name="description" content="Looking for an Untwitch alternative? TwitchCutter provides faster speeds, no 1-hour length cap, interactive video preview, and zero intrusive ads.">
  <meta name="keywords" content="untwitch alternative, untwitch not working, untwitch vs twitchcutter, sites like untwitch, twitch vod trimmer alternative">
  <link rel="canonical" href="https://twitchcutter.pages.dev/blog/untwitch-alternative.html">
{FAVICON_HEAD}

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Best Untwitch Alternative in 2024: Why Editors Are Switching to TwitchCutter",
    "description": "Comparison of Untwitch.com and TwitchCutter for cutting and downloading Twitch VODs.",
    "author": {{
      "@type": "Organization",
      "name": "TwitchCutter"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "TwitchCutter",
      "url": "https://twitchcutter.pages.dev"
    }},
    "datePublished": "2026-11-01"
  }}
  </script>

  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <article class="seo-article" style="max-width: 820px; margin: 2rem auto;">
      <div style="font-size: 0.85rem; color: #bf94ff; font-weight: 700; margin-bottom: 0.5rem;">TOOL COMPARISON</div>
      <h1 style="font-size: 2.2rem; line-height: 1.25; margin-bottom: 1rem; color: #fff;">Best Untwitch Alternative in 2024: Why Editors Are Switching to TwitchCutter</h1>
      <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 2rem;">Published Nov 2026 &bull; 4 min read &bull; By TwitchCutter Team</div>

      <p>
        For nearly a decade, <strong>Untwitch.com</strong> was the go-to web utility for downloading sections of Twitch past broadcasts. But as stream resolutions increased to 1080p60 and broadcasts grew to 12+ hours, Untwitch began showing its age.
      </p>

      <h3>Common Problems with Untwitch</h3>
      <ul>
        <li><strong>Strict 1-Hour Segment Limit:</strong> Untwitch forces you to download VODs in 1-hour chunks. If your tournament or podcast segment is 1 hour and 10 minutes, you have to download two separate files and manually stitch them together.</li>
        <li><strong>No Video Preview Player:</strong> You cannot visually preview the stream on the page to verify your timestamps. You have to scrub blindly or check timestamps on Twitch in another tab.</li>
        <li><strong>Outdated UI &amp; Ad Clutter:</strong> Heavy ad banners and popups slow down page load times and clutter mobile screens.</li>
      </ul>

      <h3>Why TwitchCutter Is the #1 Alternative</h3>
      <div style="overflow-x: auto; margin: 1.5rem 0;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;">
          <thead>
            <tr style="border-bottom: 2px solid var(--card-border); color: #fff;">
              <th style="padding: 0.75rem;">Feature</th>
              <th style="padding: 0.75rem; color: #bf94ff;">TwitchCutter</th>
              <th style="padding: 0.75rem; color: #adadb8;">Untwitch</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem; font-weight: 600;">Max Segment Length</td>
              <td style="padding: 0.75rem; color: var(--green-success); font-weight: 700;">No artificial limit (Up to 2+ hrs)</td>
              <td style="padding: 0.75rem; color: #ff6b6b;">Capped at 1 Hour</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem; font-weight: 600;">Interactive Video Preview</td>
              <td style="padding: 0.75rem; color: var(--green-success); font-weight: 700;">Yes (HLS Live Player)</td>
              <td style="padding: 0.75rem; color: #ff6b6b;">No Preview</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem; font-weight: 600;">Watermarks</td>
              <td style="padding: 0.75rem; color: var(--green-success); font-weight: 700;">100% Watermark Free</td>
              <td style="padding: 0.75rem;">Watermark Free</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--card-border);">
              <td style="padding: 0.75rem; font-weight: 600;">Dual Range Scrubber</td>
              <td style="padding: 0.75rem; color: var(--green-success); font-weight: 700;">Yes (Visual Sliders + Nudge)</td>
              <td style="padding: 0.75rem; color: #ff6b6b;">Manual Dropdowns Only</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem; font-weight: 600;">Mobile Experience</td>
              <td style="padding: 0.75rem; color: var(--green-success); font-weight: 700;">Optimized for Safari &amp; Chrome</td>
              <td style="padding: 0.75rem; color: #ffb86c;">Cluttered by ads</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div style="background: rgba(145, 70, 255, 0.1); border: 1px solid rgba(145, 70, 255, 0.3); border-radius: 12px; padding: 1.5rem; margin: 2rem 0; text-align: center;">
        <h3 style="margin-top:0; color:#fff;">Experience the difference</h3>
        <p style="margin-bottom:1.25rem;">Try TwitchCutter — modern, fast, and cap-free.</p>
        <a href="/" class="cut-btn" style="display:inline-flex; text-decoration:none;">Open TwitchCutter</a>
      </div>
    </article>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BLOG_DIR, "untwitch-alternative.html"), "w", encoding="utf-8") as f:
    f.write(blog3_html)
print("blog 3 created.")

# ==============================================================================
# 14. SITEMAP.XML
# ==============================================================================
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://twitchcutter.pages.dev/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/twitch-clip-cutter</loc>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/twitch-vod-downloader</loc>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/faq</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/blog/</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/blog/how-to-clip-longer-than-60-seconds-twitch.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/blog/download-twitch-vod-before-expires.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/blog/untwitch-alternative.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/about</loc>
    <changefreq>yearly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/privacy</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/terms</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://twitchcutter.pages.dev/contact</loc>
    <changefreq>yearly</changefreq>
    <priority>0.4</priority>
  </url>
</urlset>
"""
with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("sitemap.xml created.")

# ==============================================================================
# 15. ROBOTS.TXT
# ==============================================================================
robots_txt = """User-agent: *
Allow: /

Sitemap: https://twitchcutter.pages.dev/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("robots.txt created.")


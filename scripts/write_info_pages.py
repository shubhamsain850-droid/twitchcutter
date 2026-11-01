import os
import sys

BASE_DIR = r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\frontend"

sys.path.append(r"c:\Users\ss\.gemini\antigravity\scratch\twitchcutter\scripts")
from common_elements import LOGO_SVG, HEADER_HTML, FOOTER_HTML, FAVICON_HEAD
from build_full_site import COMMON_CSS

# ==============================================================================
# 4. FAQ.HTML (ALL 22 QUESTIONS + FAQPAGE SCHEMA)
# ==============================================================================
faq_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TwitchCutter FAQ — All Twitch Clip &amp; VOD Questions Answered</title>
  <meta name="title" content="TwitchCutter FAQ — All Twitch Clip &amp; VOD Questions Answered">
  <meta name="description" content="Answers to all 22 questions about cutting Twitch VODs, downloading clips, bypassing the 60-second limit, VOD expiration rules, 1080p MP4 quality, and mobile support.">
  <meta name="keywords" content="twitch cutter faq, twitch vod downloader faq, twitch clip cutter questions, how long do twitch vods last, clip longer than 60 seconds twitch, twitch vod expiry">
  <meta name="author" content="TwitchCutter">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://twitchcutter.pages.dev/faq">

{FAVICON_HEAD}

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://twitchcutter.pages.dev/faq">
  <meta property="og:title" content="TwitchCutter FAQ — All Twitch Clip &amp; VOD Questions Answered">
  <meta property="og:description" content="Complete guide &amp; FAQ for cutting Twitch VODs, saving clips, and downloading past broadcasts.">
  <meta property="og:image" content="https://twitchcutter.pages.dev/favicon.svg?v=4">
  <meta property="og:site_name" content="TwitchCutter">

  <!-- Full FAQPage Schema -->
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
          "text": "Standard users: 7 days. Affiliates: 14 days. Partners, Turbo, and Prime Gaming users: 60 days. Once deleted, they cannot be recovered."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I download a Twitch VOD for free?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes! TwitchCutter lets you cut and download any segment of a public Twitch VOD as an MP4 for free with zero watermarks."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How do I download a Twitch VOD before it expires?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Paste the VOD link into TwitchCutter, set your start and end timestamps, and click Cut & Download Clip to save an MP4 to your device."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can you download someone else's Twitch VOD?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes, any publicly viewable VOD on Twitch can be downloaded with TwitchCutter. Sub-only VODs require an active subscription and are not accessible."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What format are Twitch VODs downloaded in?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Universal H.264 MP4 format with AAC audio, compatible with all devices and editing software."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Is there a limit to how long a Twitch VOD segment I can cut?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "No! Unlike older tools like Untwitch which cap clips at 1 hour, TwitchCutter can slice any length segment."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I clip longer than 60 seconds on Twitch?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes. Twitch's native clip creator limits clips to 60 seconds. TwitchCutter allows you to cut clips of 2 minutes, 5 minutes, 30 minutes, or longer from any VOD."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I download Twitch clips without a watermark?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes. TwitchCutter produces 100% clean video files without watermarks, branding, or credit overlays."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Can I download Twitch clips on iPhone or Android?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes. TwitchCutter is fully mobile responsive and works directly inside mobile Safari and Google Chrome."
        }}
      }}
    ]
  }}
  </script>

  <style>
{COMMON_CSS}
  </style>
</head>
<body>
  <div class="ambient-glow"></div>

{HEADER_HTML}

  <main>
    <section class="hero">
      <div class="hero-pill">📖 Knowledge Base &amp; FAQ</div>
      <h1>Frequently Asked Questions</h1>
      <p>Everything you need to know about cutting Twitch streams, downloading VODs, audio muting, and video formats.</p>
    </section>

    <!-- FAQ Accordion List -->
    <div style="max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem;">
      <h2 style="font-size: 1.3rem; color: #bf94ff; margin-top: 1rem;">📼 Twitch VODs &amp; Stream Archiving</h2>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">1. How long do Twitch VODs last before being deleted? <span>+</span></div>
        <div class="faq-a">Twitch stores past broadcasts based on account status: Regular streamers get <strong>7 days</strong>. Twitch Affiliates get <strong>14 days</strong>. Twitch Partners, Turbo subscribers, and Prime Gaming members get <strong>60 days</strong>. After this retention window, Twitch permanently purges the video files from their servers.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">2. Can I download a Twitch VOD for free? <span>+</span></div>
        <div class="faq-a">Yes! TwitchCutter is 100% free with no hidden charges, premium tiers, or download quotas. You can cut and download as many stream moments as you need.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">3. How do I download a Twitch VOD before it expires? <span>+</span></div>
        <div class="faq-a">Simply copy the VOD link from Twitch before the expiration date, paste it into TwitchCutter, set your start and end timestamps, and hit Cut &amp; Download Clip. Your MP4 will be saved safely on your device.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">4. Can I download someone else's Twitch VOD? <span>+</span></div>
        <div class="faq-a">Yes. You can download segments from any public Twitch broadcast. Sub-only VODs require an active subscription on the streamer's channel and cannot be fetched anonymously.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">5. What format are Twitch VODs downloaded in? <span>+</span></div>
        <div class="faq-a">All videos are downloaded in standard H.264 MP4 format with AAC audio, compatible across iPhone, Android, Mac, Windows, and video editing software like DaVinci Resolve and Adobe Premiere.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">6. Is there a limit to how long a VOD segment I can cut? <span>+</span></div>
        <div class="faq-a">No! While older tools like Untwitch cap downloads to 1-hour segments, TwitchCutter allows you to slice segments of any duration — from 10 seconds to several hours.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">7. What happens to Twitch VODs after they expire? <span>+</span></div>
        <div class="faq-a">They are permanently erased from Twitch's CDN servers. Neither Twitch support nor third-party tools can recover a VOD once deleted, making early downloading essential.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">8. Can I download Twitch VODs in 1080p? <span>+</span></div>
        <div class="faq-a">Yes! TwitchCutter automatically detects all stream qualities provided by the streamer and lets you download in full 1080p60 Source resolution.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">9. Do Twitch highlights expire? <span>+</span></div>
        <div class="faq-a">No! Unlike standard past broadcasts, Twitch Highlights are stored permanently until the broadcaster manually deletes them.</div>
      </div>

      <h2 style="font-size: 1.3rem; color: #bf94ff; margin-top: 2rem;">✂️ Twitch Clips &amp; Workarounds</h2>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">10. How do I clip longer than 60 seconds on Twitch? <span>+</span></div>
        <div class="faq-a">Twitch's native clipping tool strictly enforces a 60-second limit. To bypass this, paste the full VOD link into TwitchCutter, set your start and end times to any duration (e.g. 5 minutes or 20 minutes), and download the extended clip as an MP4.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">11. Do Twitch clips expire? <span>+</span></div>
        <div class="faq-a">No, Twitch clips do not have an automatic expiration timer. However, streamers can manually delete clips, or deleting the underlying VOD may sometimes render the clip unavailable. Downloading the MP4 gives you permanent offline ownership.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">12. How do I download Twitch clips to my phone (iPhone &amp; Android)? <span>+</span></div>
        <div class="faq-a">Visit twitchcutter.pages.dev on Safari or Chrome on your mobile device, paste the clip URL, and tap Download. You can save the MP4 directly into your Photos library or Files folder.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">13. Can I download Twitch clips without a watermark? <span>+</span></div>
        <div class="faq-a">Yes! TwitchCutter adds zero watermarks, brand logos, or credit text. You get a clean, unbranded video export.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">14. Is there a Twitch clip downloader with no signup required? <span>+</span></div>
        <div class="faq-a">Yes, TwitchCutter requires absolutely no signup, login, email, or Twitch account authorization.</div>
      </div>

      <h2 style="font-size: 1.3rem; color: #bf94ff; margin-top: 2rem;">⚙️ Technical &amp; Legal</h2>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">15. Do I need to install FFmpeg or any software? <span>+</span></div>
        <div class="faq-a">No. All stream segment fetching, slicing, and MP4 packaging occur entirely in the cloud.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">16. Why is my Twitch VOD audio muted? <span>+</span></div>
        <div class="faq-a">Twitch automatically mutes sections containing copyrighted music (DMCA). The downloaded video will reflect these muted sections because the original audio was stripped at the source by Twitch.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">17. Is TwitchCutter legal to use? <span>+</span></div>
        <div class="faq-a">Yes. Using TwitchCutter for personal archiving or transformative fair-use editing is lawful. Please credit streamers when repurposing content publicly.</div>
      </div>

      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">18. How is TwitchCutter better than Untwitch? <span>+</span></div>
        <div class="faq-a">TwitchCutter features a modern dark-mode UI, real-time HLS video preview, zero segment length caps (Untwitch caps at 1 hour), no intrusive ads, and faster download speeds.</div>
      </div>
    </div>
  </main>

{FOOTER_HTML}

  <script>
    function toggleFaq(el) {{
      const a = el.nextElementSibling;
      const span = el.querySelector('span');
      if (a.style.display === 'block') {{
        a.style.display = 'none';
        span.textContent = '+';
      }} else {{
        a.style.display = 'block';
        span.textContent = '−';
      }}
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "faq.html"), "w", encoding="utf-8") as f:
    f.write(faq_html)
print("faq.html created.")

# ==============================================================================
# 5. ABOUT.HTML
# ==============================================================================
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About TwitchCutter — Free Online Twitch Video Clipper</title>
  <meta name="description" content="Learn about TwitchCutter. The fastest free online video clipper and VOD downloader for Twitch.tv, designed for esports editors and content creators.">
  <link rel="canonical" href="https://twitchcutter.pages.dev/about">
{FAVICON_HEAD}
  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <section class="seo-article" style="max-width: 800px; margin: 2rem auto;">
      <h2>About TwitchCutter</h2>
      <p>
        <strong>TwitchCutter</strong> was created out of frustration with existing Twitch downloading solutions. For years, video editors and highlight channels had only two options: download a massive 30 GB 10-hour VOD just to cut a 30-second clip, or use outdated web tools that impose 1-hour limits, plaster watermarks, and spam users with intrusive ads.
      </p>
      <h3>Our Mission</h3>
      <p>
        Our goal is simple: provide the fastest, cleanest, and most reliable browser-based stream slicing tool for the gaming community. With server-side stream slicing, TwitchCutter queries the exact HLS segments you need and packages them into high-framerate 1080p MP4 files in seconds.
      </p>
      <h3>Core Principles</h3>
      <ul>
        <li><strong>100% Free:</strong> No paywalls, subscription tiers, or hidden export limits.</li>
        <li><strong>No Watermarks:</strong> Clean video outputs ready for professional editing.</li>
        <li><strong>Privacy First:</strong> No user tracking, no mandatory accounts, and temporary cloud storage that auto-purges files after download.</li>
        <li><strong>Open &amp; Accessible:</strong> Works across mobile Safari, Android Chrome, and all desktop operating systems.</li>
      </ul>
      <h3>Disclaimer</h3>
      <p style="font-size:0.85rem; color:var(--text-muted);">
        TwitchCutter is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Twitch Interactive, Inc. or Amazon.com. All trademarks belong to their respective owners.
      </p>
    </section>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)
print("about.html created.")

# ==============================================================================
# 6. PRIVACY.HTML
# ==============================================================================
privacy_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy — TwitchCutter</title>
  <meta name="description" content="Privacy Policy for TwitchCutter. Learn how we handle URLs, temporary video processing files, and user privacy.">
  <link rel="canonical" href="https://twitchcutter.pages.dev/privacy">
{FAVICON_HEAD}
  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <section class="seo-article" style="max-width: 800px; margin: 2rem auto;">
      <h2>Privacy Policy</h2>
      <p><em>Last updated: November 2026</em></p>
      <p>Your privacy is of paramount importance to us. This policy outlines how TwitchCutter handles data when you use our service.</p>
      
      <h3>1. Information We Do NOT Collect</h3>
      <p>TwitchCutter does not require registration, accounts, or payment credentials. We do not collect names, email addresses, or personal contact info.</p>

      <h3>2. Video Processing &amp; Ephemeral Storage</h3>
      <p>When you submit a Twitch URL to slice a video segment, our server downloads only the specific video chunks required to assemble your clip. Generated MP4 files are stored in temporary memory and are automatically and permanently purged from server disks shortly after completion to prevent data retention.</p>

      <h3>3. Cookies &amp; Tracking</h3>
      <p>TwitchCutter does not use tracking cookies or sell your browsing history to third-party data brokers.</p>

      <h3>4. External Links</h3>
      <p>Our website may reference external platforms such as Twitch.tv or GitHub. We encourage users to review the privacy practices of external platforms.</p>
    </section>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BASE_DIR, "privacy.html"), "w", encoding="utf-8") as f:
    f.write(privacy_html)
print("privacy.html created.")

# ==============================================================================
# 7. TERMS.HTML
# ==============================================================================
terms_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Service &amp; DMCA — TwitchCutter</title>
  <meta name="description" content="Terms of Service, acceptable use guidelines, and DMCA takedown procedures for TwitchCutter.">
  <link rel="canonical" href="https://twitchcutter.pages.dev/terms">
{FAVICON_HEAD}
  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <section class="seo-article" style="max-width: 800px; margin: 2rem auto;">
      <h2>Terms of Service &amp; DMCA Policy</h2>
      <p><em>Last updated: November 2026</em></p>
      
      <h3>1. Acceptance of Terms</h3>
      <p>By accessing or using TwitchCutter (twitchcutter.pages.dev), you agree to comply with and be bound by these Terms of Service.</p>

      <h3>2. Purpose &amp; Fair Use</h3>
      <p>TwitchCutter is provided solely as a technical utility for streamers, content creators, and editors to trim and save publicly available video streams. Users are solely responsible for ensuring that their use complies with applicable copyright laws, fair use standards, and Twitch's Terms of Service.</p>

      <h3>3. Intellectual Property &amp; DMCA</h3>
      <p>TwitchCutter does not host, index, or maintain an archive of video content. All streams remain hosted on Twitch's content delivery networks. If you are a copyright holder and wish to request the blocking of specific URLs or channels from processing, please contact us with relevant documentation.</p>

      <h3>4. Limitation of Liability</h3>
      <p>TwitchCutter is provided "as is" without warranty of any kind. In no event shall TwitchCutter or its contributors be liable for any damages resulting from the use or inability to use the service.</p>
    </section>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BASE_DIR, "terms.html"), "w", encoding="utf-8") as f:
    f.write(terms_html)
print("terms.html created.")

# ==============================================================================
# 8. CONTACT.HTML
# ==============================================================================
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Support — TwitchCutter</title>
  <meta name="description" content="Get in touch with the TwitchCutter development team for bug reports, feature requests, or support.">
  <link rel="canonical" href="https://twitchcutter.pages.dev/contact">
{FAVICON_HEAD}
  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main>
    <section class="seo-article" style="max-width: 700px; margin: 2rem auto;">
      <h2>Contact Support &amp; Feedback</h2>
      <p>Have a question, encountered a bug, or want to suggest a new feature? We'd love to hear from you!</p>
      
      <div style="background:#111114; border:1px solid var(--card-border); border-radius:12px; padding:1.5rem; margin-top:1.5rem;">
        <h3 style="margin-top:0; color:#fff;">GitHub Issues &amp; Community</h3>
        <p style="margin-bottom:1rem;">The fastest way to report stream fetching bugs or request new clipping features is via our open-source GitHub repository:</p>
        <a href="https://github.com/shubhamsain850-droid/twitchcutter" target="_blank" rel="noopener" class="cut-btn" style="display:inline-flex; text-decoration:none;">
          Visit TwitchCutter on GitHub
        </a>
      </div>

      <div style="background:#111114; border:1px solid var(--card-border); border-radius:12px; padding:1.5rem; margin-top:1.5rem;">
        <h3 style="margin-top:0; color:#fff;">Email Inquiries</h3>
        <p>For DMCA notices, partnership inquiries, or general support, you can reach out to our team at:</p>
        <p style="font-family:var(--font-mono); color:var(--accent); font-weight:600;">support@twitchcutter.pages.dev</p>
      </div>
    </section>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)
print("contact.html created.")

# ==============================================================================
# 9. 404.HTML
# ==============================================================================
not_found_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 — Page Not Found | TwitchCutter</title>
  <meta name="robots" content="noindex, follow">
{FAVICON_HEAD}
  <style>{COMMON_CSS}</style>
</head>
<body>
  <div class="ambient-glow"></div>
{HEADER_HTML}
  <main style="text-align: center; padding: 5rem 1rem;">
    <div style="font-size: 5rem; font-weight: 800; color: var(--accent); margin-bottom: 1rem;">404</div>
    <h1 style="font-size: 2rem; margin-bottom: 1rem;">Stream Moment Not Found</h1>
    <p style="color: var(--text-muted); max-width: 500px; margin: 0 auto 2rem;">
      The page you're looking for doesn't exist or has been moved. Use the quick links below to cut your Twitch clips.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="/" class="cut-btn" style="text-decoration: none;">Go to Twitch Cutter</a>
      <a href="/twitch-clip-cutter" class="nudge-btn" style="text-decoration: none; padding: 0.75rem 1.25rem; font-size: 0.95rem;">Twitch Clip Cutter</a>
    </div>
  </main>
{FOOTER_HTML}
</body>
</html>
"""
with open(os.path.join(BASE_DIR, "404.html"), "w", encoding="utf-8") as f:
    f.write(not_found_html)
print("404.html created.")

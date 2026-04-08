#!/usr/bin/env python3
"""
Static site generator for Budget3DPrint SEO site.
Converts markdown posts -> HTML pages, builds homepage with article grid.
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
SITE_NAME = "Print3DBuddy"
SITE_TAGLINE = "Honest reviews and guides for budget 3D printing"
SITE_DOMAIN = "print3dbuddy.com"
POSTS_DIR = Path("content/posts")
OUTPUT_DIR = Path("public")
STATIC_DIR = Path("static")

NAV_LINKS = [
    ("Home", "/"),
    ("All Guides", "/posts/"),
    ("Find a Fix", "/find-a-fix/"),
    ("Services", "https://tools.print3dbuddy.com/dashboard"),
    ("Quick Guides", "https://tools.print3dbuddy.com/guides"),
    ("About", "/about/"),
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')


def parse_frontmatter(content):
    """Extract optional YAML-style frontmatter between --- markers."""
    meta = {}
    body = content
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm = content[3:end].strip()
            for line in fm.splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip()
            body = content[end+3:].strip()
    return meta, body


def md_to_html(text):
    """Minimal markdown -> HTML converter (no dependencies)."""
    lines = text.split('\n')
    html = []
    in_ul = False
    in_ol = False
    in_table = False
    in_blockquote = False
    i = 0

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            html.append('</ul>')
            in_ul = False
        if in_ol:
            html.append('</ol>')
            in_ol = False

    def close_table():
        nonlocal in_table
        if in_table:
            html.append('</tbody></table>')
            in_table = False

    def inline(t):
        # bold+italic
        t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
        # bold
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'__(.+?)__', r'<strong>\1</strong>', t)
        # italic
        t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
        t = re.sub(r'_(.+?)_', r'<em>\1</em>', t)
        # inline code
        t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
        # links
        t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
        # strikethrough
        t = re.sub(r'~~(.+?)~~', r'<del>\1</del>', t)
        return t

    table_header_done = False

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if line.startswith('```'):
            close_lists()
            close_table()
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                i += 1
            lang_attr = f' class="language-{lang}"' if lang else ''
            html.append(f'<pre><code{lang_attr}>' + '\n'.join(code_lines) + '</code></pre>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', line.strip()):
            close_lists()
            close_table()
            html.append('<hr>')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            close_lists()
            close_table()
            level = len(m.group(1))
            text = inline(m.group(2))
            anchor = slugify(m.group(2))
            html.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            i += 1
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and re.match(r'^\|?[\s\-|:]+\|?$', lines[i+1]):
            close_lists()
            if not in_table:
                html.append('<table><thead><tr>')
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                for c in cells:
                    html.append(f'<th>{inline(c)}</th>')
                html.append('</tr></thead><tbody>')
                in_table = True
                table_header_done = True
            i += 2  # skip separator row
            continue

        if in_table and '|' in line:
            html.append('<tr>')
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            for c in cells:
                html.append(f'<td>{inline(c)}</td>')
            html.append('</tr>')
            i += 1
            continue

        if in_table and '|' not in line:
            close_table()

        # Unordered list
        m = re.match(r'^(\s*)[-*+]\s+(.*)', line)
        if m:
            close_table()
            if not in_ul:
                if in_ol:
                    html.append('</ol>')
                    in_ol = False
                html.append('<ul>')
                in_ul = True
            html.append(f'<li>{inline(m.group(2))}</li>')
            i += 1
            continue

        # Ordered list
        m = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if m:
            close_table()
            if not in_ol:
                if in_ul:
                    html.append('</ul>')
                    in_ul = False
                html.append('<ol>')
                in_ol = True
            html.append(f'<li>{inline(m.group(2))}</li>')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            close_lists()
            close_table()
            text = inline(line[1:].strip())
            html.append(f'<blockquote><p>{text}</p></blockquote>')
            i += 1
            continue

        # Empty line
        if line.strip() == '':
            close_lists()
            close_table()
            i += 1
            continue

        # Paragraph
        close_lists()
        close_table()
        html.append(f'<p>{inline(line.strip())}</p>')
        i += 1

    close_lists()
    close_table()
    return '\n'.join(html)


def nav_html(active=None):
    links = ''
    for label, href in NAV_LINKS:
        external = href.startswith('http')
        target = ' target="_blank" rel="noopener"' if external else ''
        if label == 'Services':
            links += f'<li><a href="{href}" class="nav-tools-btn"{target}>{label}</a></li>'
        else:
            links += f'<li><a href="{href}"{target}>{label}</a></li>'
    return f'''<header>
  <nav>
    <a href="/" class="logo">Print3D<span>Buddy</span></a>
    <ul>{links}</ul>
  </nav>
</header>'''


def footer_html():
    year = datetime.now().year
    return f'''<footer>
  <p>&copy; {year} {SITE_NAME} - Independent guides, no fluff.</p>
  <p><a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a> &middot; <a href="/contact/">Contact</a> &middot; <a href="mailto:CobyCane01@outlook.com">Email us</a></p>
</footer>'''


def base_html(title, body, description='', canonical=''):
    meta_desc = f'<meta name="description" content="{description}">' if description else ''
    canon_tag = f'<link rel="canonical" href="https://{SITE_DOMAIN}{canonical}">' if canonical else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {meta_desc}
  {canon_tag}
  <link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
  <link rel="stylesheet" href="/static/css/style.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-LKWD1FJNP3"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-LKWD1FJNP3');</script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5408659965693947" crossorigin="anonymous"></script>
</head>
<body>
{nav_html()}
{body}
{footer_html()}
</body>
</html>'''


# ── Post metadata extraction ─────────────────────────────────────────────────

POST_TAGS = {
    'how-to-calibrate-your-first-3d-printer': ('Beginner Guide', 'Learn how to properly calibrate your first 3D printer  -  bed levelling, E-steps, flow rate, and more.'),
    'how-to-fix-3d-printer-stringing': ('Troubleshooting', 'Stringing ruining your prints? Here\'s how to fix it fast  -  retraction settings, temperature, and travel speed explained.'),
    'pla-vs-petg-vs-abs-which-filament-for-beginners': ('Filament Guide', 'PLA, PETG or ABS? A plain-English comparison to help beginners pick the right filament for their project.'),
    'best-filament-for-outdoor-use': ('Filament Guide', 'Which filaments survive UV, heat, and moisture? A practical guide to outdoor 3D printing materials.'),
    '10-useful-things-to-3d-print-for-your-home': ('Ideas & Inspiration', '10 genuinely useful things you can 3D print for around the house  -  practical, functional, beginner-friendly.'),
    'best-budget-3d-printers-under-200': ('Printer Reviews', 'The best 3D printers under $200 in 2025  -  Bambu A1 Mini, Ender 3 V3 SE, Neptune 4 Pro compared for beginners.'),
    'best-slicer-software-for-beginners': ('Software Guide', 'Bambu Studio, PrusaSlicer, or Cura? A plain-English comparison of the best free slicer software for beginners.'),
    'how-to-fix-3d-print-warping': ('Troubleshooting', 'Warping ruining your prints? Here\'s how to fix it  -  bed adhesion, enclosures, brims, and material-specific tips.'),
    'where-to-download-free-3d-print-files': ('Resources', 'The best sites to download free 3D print files in 2025  -  Printables, Thingiverse, Makerworld and more compared.'),
    '3d-printing-speed-vs-quality-guide': ('Settings Guide', 'How to balance 3D printing speed and quality  -  what limits speed, key settings, and profiles for different goals.'),
    'how-to-store-filament-properly': ('Filament Guide', 'How to store 3D printer filament properly  -  airtight containers, desiccant, drying wet filament, and which materials need the most care.'),
    'best-3d-printer-upgrades-under-50': ('Upgrades', 'The best 3D printer upgrades under $50  -  PEI sheets, Capricorn tubes, BLTouch, calipers, and more ranked by impact.'),
    'how-to-post-process-3d-prints': ('Finishing Guide', 'How to sand, prime, paint, and finish 3D prints  -  from removing supports to a professional painted result.'),
    'tpu-flexible-filament-beginners-guide': ('Filament Guide', 'TPU flexible filament guide for beginners  -  settings, direct drive vs Bowden, avoiding jams, and what to print.'),
    'how-to-design-3d-models-for-beginners': ('Software Guide', 'How to design your own 3D models  -  Tinkercad, Fusion 360, FreeCAD compared for beginners.'),
    '3d-printing-layer-adhesion-problems-fixes': ('Troubleshooting', 'Layer adhesion problems in 3D printing  -  causes, fixes, and a checklist to get strong, bonded prints every time.'),
    'complete-nozzle-guide-3d-printing': ('Hardware Guide', 'Complete 3D printer nozzle guide  -  sizes, materials (brass, hardened steel, ruby), when to replace, and how to clean.'),
    '3d-printing-first-layer-problems-fixes': ('Troubleshooting', 'Every first layer problem in 3D printing and how to fix it  -  not sticking, warping, gaps, blobs and more.'),
    'best-3d-printers-for-beginners-2025': ('Printer Reviews', 'Best 3D printers for beginners in 2025  -  Bambu Lab A1 Mini, Ender 3 V3 SE, Prusa MK4 compared honestly.'),
    '3d-printing-infill-patterns-guide': ('Settings Guide', 'Complete guide to 3D printing infill  -  patterns, percentages, and which to use for strength, speed, or flexibility.'),
    'how-to-reduce-3d-print-time': ('Settings Guide', 'How to reduce 3D print time without ruining quality  -  layer height, infill, speed, and nozzle changes that actually work.'),
    'learn-3d-printing-faster-with-tools': ('Beginner Guide', 'The fastest way to learn 3D printing  -  how to test variables and build real knowledge without wasting filament on failed prints.'),
    'how-to-fix-under-extrusion': ('Troubleshooting', 'Under-extrusion causes gaps, weak layers, and failed prints. Here\'s every cause and fix  -  extruder gear, clogs, temperature, E-steps, and filament quality.'),
    '3d-printing-supports-guide': ('Settings Guide', 'When to use 3D printing supports, how to set them up, and how to remove them cleanly  -  tree vs normal supports, Z distance, interface layers explained.'),
    'best-websites-for-cheap-3d-printing-services': ('Resources', 'The best websites for cheap 3D printing services  -  Craftcloud, JLCPCB, Treatstock, Shapeways compared for hobbyists on a budget.'),
    'best-filament-brands-for-3d-printing': ('Filament Guide', 'The best 3D printer filament brands in 2025  -  eSUN, Polymaker, Bambu Lab, Sunlu compared honestly for PLA, PETG, ABS and more.'),
    'best-filament-dryers-for-3d-printing': ('Buyer\'s Guide', 'The best filament dryers for 3D printing in 2025  -  Sunlu S4, S1 Plus, EIBOS, PolyDryer compared. Fix wet filament problems for good.'),
    'best-3d-printer-enclosures': ('Buyer\'s Guide', 'The best 3D printer enclosures in 2025  -  budget fabric tents to rigid builds compared. Essential for ABS, ASA, and large PETG prints.'),
    'best-pei-sheets-for-3d-printers': ('Buyer\'s Guide', 'The best PEI sheets for 3D printers in 2025  -  Energetic, Fysetc, Bambu Lab compared. The cheapest upgrade for perfect bed adhesion.'),
    'best-tools-for-3d-printing': ('Buyer\'s Guide', 'The best tools for 3D printing  -  calipers, spatulas, flush cutters, and everything else worth having. Build the right kit from the start.'),
    'best-resin-3d-printers-for-beginners': ('Printer Reviews', 'Best resin 3D printers for beginners in 2025  -  Elegoo Saturn 4, Mars 4, Phrozen Sonic Mini 8K compared for detail, value, and ease of use.'),
    'best-3d-printing-accessories-under-30': ('Buyer\'s Guide', 'The best 3D printing accessories under £30  -  bed adhesion, filament handling, maintenance, and finishing tools that actually make a difference.'),
    'resin-3d-printing-beginners-guide': ('Beginner Guide', 'Complete resin 3D printing guide for beginners  -  how it works, safety, settings, wash and cure, and common problems fixed.'),
    '3d-print-orientation-part-strength-guide': ('Settings Guide', 'How to orient 3D prints for maximum strength  -  why layer direction matters, practical examples, and which settings to pair with it.'),
    '3d-prints-stuck-to-build-plate-fixes': ('Troubleshooting', 'Prints stuck to the build plate? Every cause and fix  -  z-offset, bed temp, PETG on PEI, and when to replace the surface.'),
    'how-to-fix-layer-shifting': ('Troubleshooting', 'Layer shifting in 3D printing - every cause and fix. Loose belts, high acceleration, obstructions, and stepper driver heat all explained.'),
    'how-to-fix-over-extrusion': ('Troubleshooting', 'Over-extrusion causing blobs, bulging walls, or dimensional inaccuracy? Every cause and fix - flow rate, E-steps, temperature, and elephant foot.'),
    'how-to-fix-ghosting-ringing': ('Troubleshooting', 'Ghosting and ringing artefacts on 3D prints - how to fix wavy ripples near corners. Speed, acceleration, belt tension, and input shaper explained.'),
    'how-to-fix-wet-filament': ('Filament Guide', 'Wet filament causing crackling, rough surfaces, or poor layer adhesion? How to identify, dry, and store filament to prevent moisture problems.'),
    'abs-asa-printing-guide': ('Filament Guide', 'ABS and ASA printing guide - enclosure requirements, settings, warping fixes, bed adhesion, fumes, and acetone finishing for ABS.'),
    'petg-printing-guide': ('Filament Guide', 'PETG printing guide - settings, stringing fixes, bed adhesion tips, moisture storage, and when to use PETG instead of PLA or ABS.'),
    'how-to-maintain-3d-printer': ('Maintenance Guide', 'How to maintain your 3D printer - lubrication, belt tension, nozzle cleaning, bed care, and a simple schedule to prevent most common problems.'),
    'how-to-calibrate-pressure-advance': ('Settings Guide', 'How to calibrate pressure advance (Klipper) and linear advance (Marlin) - fix corner blobs, crisp edges, and print faster without losing quality.'),
    'how-to-calibrate-flow-rate-extrusion-multiplier': ('Settings Guide', 'How to calibrate flow rate (extrusion multiplier) - fix rough top surfaces, dimensional inaccuracy, and weak layers in one simple test.'),
    'how-to-fix-3d-printer-grinding-noise': ('Troubleshooting', '3D printer grinding noise? Diagnose by location - extruder, hotend, Z axis, or rails - and fix the right cause first time.'),
    '3d-printing-emissions-indoor-safety': ('Safety Guide', 'Is 3D printing safe indoors? What research shows about UFPs and VOCs from FDM printers, material comparisons, and practical steps to reduce exposure.'),
    'resin-3d-printing-safety': ('Safety Guide', 'Resin 3D printing safety - PPE requirements, VOC emissions, handling uncured resin, safe disposal, and ventilation. What you actually need to know.'),
    'how-to-print-tpu-hinges-living-hinges': ('Filament Guide', 'How to print TPU hinges and living hinges - design principles, slicer settings, and fixes for the most common problems.'),
    '3d-printing-for-cosplay': ('Ideas & Inspiration', '3D printing for cosplay - materials, design workflow, post-processing, and practical tips for props, armour, and wearable pieces.'),
    'how-to-finish-resin-prints': ('Finishing Guide', 'How to finish and paint resin 3D prints - cleaning, support removal, sanding, priming, painting, and a final topcoat step by step.'),
    'how-to-fix-elephant-foot': ('Troubleshooting', 'How to fix elephant foot in 3D printing - every cause and fix for a flared base, from Z offset to live adjust and first layer settings.'),
    'what-to-do-when-3d-print-fails-mid-print': ('Troubleshooting', 'What to do when a 3D print fails mid-print - diagnosing spaghetti, layer shifts, adhesion failures, and how to prevent each from happening again.'),
    'petg-on-pei-problems-fixes': ('Troubleshooting', 'PETG on PEI bed - every common problem fixed. Prints sticking too well, not sticking, stringing, rough surfaces, and weak layers all covered.'),
    'nylon-3d-printing-guide': ('Filament Guide', 'Nylon 3D printing guide - settings, enclosure requirements, drying, bed adhesion, warping fixes, and when Nylon is the right material choice.'),
    'cura-vs-prusaslicer-vs-bambu-studio': ('Software Guide', 'Cura vs PrusaSlicer vs Bambu Studio - which slicer should you use? A plain-English comparison for beginners and switchers.'),
    'how-to-tension-3d-printer-belts': ('Maintenance Guide', 'How to tension 3D printer belts - checking tension, tightening methods for common printers, pulley grub screws, and when to replace belts.'),
    'useful-things-to-3d-print-for-your-workshop': ('Ideas & Inspiration', '15 genuinely useful things to 3D print for your workshop or garage - tool holders, jigs, cable management, dust adapters, and more.'),
    'input-shaper-resonance-compensation-guide': ('Settings Guide', 'Input shaper and resonance compensation guide - how to set up on Klipper, Bambu, and Prusa to eliminate ghosting and print faster.'),
    'how-to-upgrade-3d-printer-hot-end': ('Hardware Guide', 'How to upgrade your 3D printer hot end - E3D V6, Revo, Volcano, and Sprite compared. What to upgrade and whether it is worth it.'),
    '3d-printer-fire-safety-guide': ('Safety Guide', '3D printer fire safety - thermal runaway protection, smoke detectors, wiring inspection, resin risks, and safe printing habits explained.'),
}


def get_post_tag(slug):
    return POST_TAGS.get(slug, ('Guide', ''))[0]


def get_post_desc(slug, fallback=''):
    return POST_TAGS.get(slug, ('', fallback))[1] or fallback


# ── Build individual post pages ───────────────────────────────────────────────

def build_posts():
    posts = []
    posts_out = OUTPUT_DIR / 'posts'
    posts_out.mkdir(parents=True, exist_ok=True)

    for md_file in sorted(POSTS_DIR.glob('*.md')):
        raw = md_file.read_text(encoding='utf-8')
        meta, body = parse_frontmatter(raw)

        # Extract title from first H1
        title_match = re.match(r'^#\s+(.+)', body)
        if title_match:
            title = title_match.group(1).strip()
            body_no_title = body[title_match.end():].strip()
        else:
            title = md_file.stem.replace('-', ' ').title()
            body_no_title = body

        slug = md_file.stem
        tag = get_post_tag(slug)
        desc = get_post_desc(slug, title)

        # First paragraph as excerpt
        first_para = ''
        for line in body_no_title.splitlines():
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                first_para = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
                first_para = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', first_para)
                first_para = first_para[:160] + ('...' if len(first_para) > 160 else '')
                break

        content_html = md_to_html(body_no_title)

        article_body = f'''<div class="article-wrap">
  <a href="/posts/" class="back-link">&larr; All Guides</a>
  <div class="article-meta">
    <span class="tag">{tag}</span>
    &nbsp;&middot;&nbsp; Print3DBuddy
  </div>
  <h1>{title}</h1>
  {content_html}
</div>'''

        page = base_html(
            title=f'{title} | {SITE_NAME}',
            body=article_body,
            description=desc,
            canonical=f'/posts/{slug}/'
        )

        out_dir = posts_out / slug
        out_dir.mkdir(exist_ok=True)
        (out_dir / 'index.html').write_text(page, encoding='utf-8')
        print(f'  Built: /posts/{slug}/')

        posts.append({
            'slug': slug,
            'title': title,
            'tag': tag,
            'excerpt': first_para,
            'url': f'/posts/{slug}/',
        })

    return posts


# ── Build homepage ─────────────────────────────────────────────────────────

def build_homepage(posts):
    body = '''<div class="home-hero">
  <div class="home-logo">Print3D<span>Buddy</span></div>
  <p class="home-tagline">Your 3D Printing Buddy on a Budget</p>
  <p class="home-sub">Honest guides, filament comparisons, and beginner tips - without the jargon or the upsells.</p>

  <div class="home-search-wrap">
    <input type="text" id="home-search" placeholder="Search guides - e.g. stringing, PETG, first layer..." autocomplete="off">
    <p style="font-size:0.8rem; color:#aaa; margin-top:8px;">Searches guide titles - for specific problems try <a href="/find-a-fix/" style="color:#aaa; text-decoration:underline;">Find a Fix</a>.</p>
    <div id="home-results"></div>
  </div>
</div>

<main class="home-main">

  <section class="home-section">
    <h2>What we do</h2>
    <p>Print3DBuddy is a free resource for anyone getting into 3D printing. We write clear, practical guides that skip the filler and get straight to what you actually need to know - whether you are setting up your first printer, troubleshooting a failed print, or trying to understand which filament to buy.</p>
    <p>Every guide is written to be genuinely useful. No sponsored opinions, no padding, no assuming you already know the jargon.</p>
  </section>

  <section class="home-section">
    <h2>What we provide</h2>
    <div class="home-features">
      <div class="home-feature">
        <div class="home-feature-icon">&#128196;</div>
        <h3>In-depth guides</h3>
        <p>Step-by-step articles covering troubleshooting, materials, settings, slicers, and more. Written for beginners but useful at any level.</p>
      </div>
      <div class="home-feature">
        <div class="home-feature-icon">&#128269;</div>
        <h3>Find a Fix</h3>
        <p>Tell us your problem - printer type, material, what is going wrong - and we will point you straight to the right guide.</p>
      </div>
      <div class="home-feature">
        <div class="home-feature-icon">&#129518;</div>
        <h3>Tools &amp; calculators</h3>
        <p>Filament cost calculators, print settings cheat sheets, slicer recommendations, and STL estimators to help you print smarter.</p>
      </div>
      <div class="home-feature">
        <div class="home-feature-icon">&#128424;</div>
        <h3>Calibration test prints</h3>
        <p>Seven targeted test prints with full guides to dial in your FDM printer - overhang, stringing, bridging, first layer, and more.</p>
      </div>
    </div>
  </section>

  <section class="home-section home-mission">
    <h2>Our goal</h2>
    <p>3D printing is one of the most useful skills a person can pick up - but it has a reputation for being complicated, frustrating, and expensive to get into. We think that reputation puts a lot of people off unnecessarily.</p>
    <p>Our goal is simple: make 3D printing accessible. Not just to hobbyists and engineers, but to anyone who wants to make something, fix something, or stop throwing things away because a small part broke.</p>
    <p>We believe in the right to repair. A broken appliance, a worn-out component, a part that costs &pound;50 to replace - these are problems a 3D printer can solve for pennies. The more people who understand that, the better.</p>
    <p>So whether you are unboxing your first printer or trying to figure out why your prints keep warping - you are in the right place.</p>
    <a href="/posts/" class="btn" style="margin-top:8px;">Browse all guides &rarr;</a>
  </section>

</main>

<style>
  .home-hero {
    background: var(--dark);
    padding: 56px 20px 48px;
    text-align: center;
  }
  .home-logo {
    font-size: 3rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -1px;
    margin-bottom: 10px;
  }
  .home-logo span { color: var(--accent); }
  .home-tagline {
    font-size: 1.15rem;
    color: #ccc;
    font-weight: 600;
    margin-bottom: 8px;
  }
  .home-sub {
    font-size: 0.97rem;
    color: #888;
    max-width: 520px;
    margin: 0 auto 32px;
  }
  .home-search-wrap {
    max-width: 620px;
    margin: 0 auto;
    position: relative;
  }
  .home-search-wrap input {
    width: 100%;
    padding: 16px 22px;
    font-size: 1rem;
    border: none;
    border-radius: 10px;
    outline: none;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
    color: var(--text);
  }
  #home-results {
    position: absolute;
    top: calc(100% + 6px);
    left: 0; right: 0;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    z-index: 50;
    overflow: hidden;
    text-align: left;
  }
  .home-result-item {
    display: block;
    padding: 13px 18px;
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    transition: background 0.1s;
  }
  .home-result-item:last-child { border-bottom: none; }
  .home-result-item:hover { background: #fff8f5; text-decoration: none; }
  .home-result-tag { font-size: 0.72rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 3px; }
  .home-result-title { font-size: 0.95rem; font-weight: 600; color: var(--dark); display: block; }
  .home-result-more { display: block; padding: 11px 18px; font-size: 0.88rem; color: var(--accent); font-weight: 600; text-align: center; background: #fff8f5; text-decoration: none; }
  .home-result-more:hover { text-decoration: underline; }

  .home-main { max-width: 860px; margin: 0 auto; padding: 52px 20px 60px; }
  .home-section { margin-bottom: 52px; }
  .home-section h2 { font-size: 1.5rem; font-weight: 800; margin-bottom: 14px; color: var(--dark); }
  .home-section p { color: var(--muted); line-height: 1.75; margin-bottom: 12px; font-size: 1rem; }

  .home-features { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }
  .home-feature { background: var(--bg-alt); border: 1px solid var(--border); border-radius: 10px; padding: 22px 24px; }
  .home-feature-icon { font-size: 1.8rem; margin-bottom: 10px; }
  .home-feature h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; color: var(--dark); }
  .home-feature p { font-size: 0.9rem; color: var(--muted); margin: 0; line-height: 1.55; }

  .home-mission { background: var(--bg-alt); border: 1px solid var(--border); border-radius: 12px; padding: 32px 36px; }
  .home-mission p { color: var(--text); }
</style>

<script>
  const homeInput = document.getElementById('home-search');
  const homeResults = document.getElementById('home-results');
  let searchIndex = [];

  fetch('/search-index.json')
    .then(r => r.json())
    .then(data => { searchIndex = data; });

  homeInput.addEventListener('input', () => {
    const q = homeInput.value.trim().toLowerCase();
    if (q.length < 2) { homeResults.innerHTML = ''; return; }
    const matches = searchIndex.filter(p =>
      p.title.toLowerCase().includes(q) ||
      p.excerpt.toLowerCase().includes(q) ||
      p.tag.toLowerCase().includes(q)
    );
    if (matches.length === 0) {
      homeResults.innerHTML = '<a href="/posts/" class="home-result-more">No results - browse all guides &rarr;</a>';
      return;
    }
    const top = matches.slice(0, 5);
    homeResults.innerHTML = top.map(p => `
      <a href="${p.url}" class="home-result-item">
        <span class="home-result-tag">${p.tag}</span>
        <span class="home-result-title">${p.title}</span>
      </a>
    `).join('') + (matches.length > 5 ? `<a href="/posts/" class="home-result-more">See all ${matches.length} results &rarr;</a>` : '');
  });

  document.addEventListener('click', e => {
    if (!homeInput.contains(e.target)) homeResults.innerHTML = '';
  });
</script>'''

    page = base_html(
        title=f'{SITE_NAME} - 3D Printing Guides for Beginners',
        body=body,
        description='Free 3D printing guides, troubleshooting help, and tools for beginners. No jargon, no upsells - just practical help.',
        canonical='/'
    )
    (OUTPUT_DIR / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /index.html')


# ── Build posts index ──────────────────────────────────────────────────────

def build_posts_index(posts):
    # Group posts by tag/category
    categories = {}
    for p in posts:
        cat = p['tag']
        categories.setdefault(cat, []).append(p)

    sections = ''
    for cat, cat_posts in categories.items():
        cards = ''
        for p in cat_posts:
            cards += f'''<article class="card">
  <span class="tag">{p["tag"]}</span>
  <h2><a href="{p["url"]}">{p["title"]}</a></h2>
  <p>{p["excerpt"]}</p>
  <a href="{p["url"]}" class="read-more">Read more &rarr;</a>
</article>
'''
        sections += f'''<section class="cat-section">
  <h2 class="section-title">{cat}</h2>
  <div class="articles">
{cards}  </div>
</section>
'''

    body = f'''<main>
  <h1 class="section-title">All Guides</h1>
  <p class="section-sub">Every article on Print3DBuddy  -  practical help for 3D printing on a budget.</p>

  {sections}

  <section style="margin:48px 0 0; padding:32px 36px; background:#fff8f5; border:2px solid var(--accent); border-radius:12px; text-align:center;">
    <h2 style="font-size:1.2rem; font-weight:700; margin-bottom:8px;">Missing a guide?</h2>
    <p style="color:var(--muted); font-size:0.95rem; margin-bottom:18px;">If there is a topic you think we should cover, let us know and we will add it to the list.</p>
    <a href="/feedback/?type=missing-guide" class="btn">Suggest a guide &rarr;</a>
  </section>

  <section class="resources-box">
    <h2 class="section-title">Useful External Resources</h2>
    <p class="section-sub">Trusted sites we reference and recommend</p>
    <div class="resources-grid">
      <a href="https://www.printables.com" target="_blank" rel="noopener" class="resource-card">
        <strong>Printables</strong>
        <span>The best place to find free 3D models  -  run by Prusa Research</span>
      </a>
      <a href="https://www.reddit.com/r/3Dprinting/" target="_blank" rel="noopener" class="resource-card">
        <strong>r/3Dprinting</strong>
        <span>Huge community for troubleshooting, inspiration, and advice</span>
      </a>
      <a href="https://www.thingiverse.com" target="_blank" rel="noopener" class="resource-card">
        <strong>Thingiverse</strong>
        <span>Largest library of free 3D print files  -  3 million+ models</span>
      </a>
      <a href="https://github.com/prusa3d/PrusaSlicer/releases" target="_blank" rel="noopener" class="resource-card">
        <strong>PrusaSlicer</strong>
        <span>Free, open-source slicer trusted by the community</span>
      </a>
      <a href="https://www.bambulab.com/en/software" target="_blank" rel="noopener" class="resource-card">
        <strong>Bambu Studio</strong>
        <span>Fast, modern slicer  -  works with any printer, not just Bambu</span>
      </a>
      <a href="https://reprap.org/wiki/RepRap" target="_blank" rel="noopener" class="resource-card">
        <strong>RepRap Wiki</strong>
        <span>The original open-source 3D printing knowledge base</span>
      </a>
    </div>
  </section>
</main>'''

    page = base_html(
        title=f'All Guides | {SITE_NAME}',
        body=body,
        description='All 3D printing guides, filament reviews, and beginner tutorials on Print3DBuddy. Organised by category.',
        canonical='/posts/'
    )
    posts_index = OUTPUT_DIR / 'posts'
    posts_index.mkdir(exist_ok=True)
    (posts_index / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /posts/index.html')


# ── Build about page ───────────────────────────────────────────────────────

def build_about():
    body = '''<div class="article-wrap">
  <h1>About Print3DBuddy</h1>

  <div class="author-card">
    <img src="/static/img/joshua-spencer.jpg" alt="Joshua Spencer" class="author-avatar" onerror="this.style.display='none'">
    <div class="author-info">
      <h2 class="author-name">Joshua Spencer</h2>
      <p class="author-title">Founder &amp; Lead Writer</p>
    </div>
  </div>

  <p>Hi, I'm Joshua. I've spent years working with 3D printers professionally  -  diagnosing faults, calibrating machines, and getting them running reliably for the companies that rely on them. From entry-level FDM printers to industrial machines, there's very little I haven't had to take apart, tune, or troubleshoot at some point. My personal printer right now is a Bambu Lab P1S, which I use daily.</p>

  <p>I started Print3DBuddy because most of the help online is either buried in forum threads, assumes you already know what you're doing, or is written by someone who has clearly never touched a printer. I wanted a single place with straight-talking, practical guides that actually reflect how these machines behave in the real world  -  not just what the spec sheet says.</p>

  <p>Whether you're setting up your first printer or trying to track down why your prints keep failing, the goal here is simple: give you the same advice I'd give a colleague standing next to me at the machine.</p>

  <h2>What Print3DBuddy Covers</h2>
  <ul>
    <li>Calibration guides  -  flow rate, pressure advance, first layer, bed levelling</li>
    <li>Troubleshooting  -  stringing, warping, layer adhesion, under-extrusion, and more</li>
    <li>Filament guides  -  PLA, PETG, ABS, ASA, TPU, and when to use each</li>
    <li>Beginner setup walkthroughs</li>
    <li>Hardware and buyer's guides focused on real-world value</li>
  </ul>

  <p>I don't take money from manufacturers, and I don't soften criticism to keep affiliate commissions. If something isn't worth buying, I'll say so.</p>

  <p>Have a question, spotted an error, or want to suggest a topic? <a href="/contact/">Get in touch</a>  -  I read every message.</p>
</div>'''

    page = base_html(
        title=f'About Joshua Spencer | {SITE_NAME}',
        body=body,
        description='Print3DBuddy is run by Joshua Spencer, a professional 3D printer technician with years of hands-on experience calibrating and repairing FDM printers across multiple industries.',
        canonical='/about/'
    )
    about_dir = OUTPUT_DIR / 'about'
    about_dir.mkdir(exist_ok=True)
    (about_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /about/')


# ── Build privacy page ─────────────────────────────────────────────────────

def build_contact():
    body = '''<div class="article-wrap">
  <h1>Contact</h1>
  <p>Got a question, a topic suggestion, or spotted an error in one of our guides? I'd love to hear from you.</p>
  <p>Email: <a href="mailto:print3dbuddywork@outlook.com">print3dbuddywork@outlook.com</a></p>
  <p>I aim to reply within 24 hours.</p>
</div>'''

    page = base_html(
        title=f'Contact | {SITE_NAME}',
        body=body,
        description='Get in touch with Print3DBuddy  -  questions, suggestions, and corrections welcome.',
        canonical='/contact/'
    )
    contact_dir = OUTPUT_DIR / 'contact'
    contact_dir.mkdir(exist_ok=True)
    (contact_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /contact/')


def build_privacy():
    body = f'''<div class="article-wrap">
  <h1>Privacy Policy</h1>
  <p>Last updated: {datetime.now().strftime("%B %Y")}</p>
  <h2>What we collect</h2>
  <p>This site uses standard web analytics (Google Analytics or similar) to understand which pages are read. This collects anonymised data such as page views, country, and device type. No personally identifiable information is collected.</p>
  <h2>Affiliate links</h2>
  <p>Some links on this site are affiliate links. If you buy through them, we may earn a small commission at no extra cost to you. This helps keep the site running. We only link to products we would genuinely recommend.</p>
  <h2>Cookies</h2>
  <p>Analytics tools may set cookies. You can disable cookies in your browser settings at any time.</p>
  <h2>Contact</h2>
  <p>Questions about this policy? <a href="/contact/">Contact us</a>.</p>
</div>'''

    page = base_html(
        title=f'Privacy Policy | {SITE_NAME}',
        body=body,
        description='Privacy policy for Budget3DPrint.',
        canonical='/privacy/'
    )
    priv_dir = OUTPUT_DIR / 'privacy'
    priv_dir.mkdir(exist_ok=True)
    (priv_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /privacy/')


# ── Copy static assets ─────────────────────────────────────────────────────

def copy_static():
    out_static = OUTPUT_DIR / 'static'
    if out_static.exists():
        shutil.rmtree(out_static)
    shutil.copytree(STATIC_DIR, out_static)
    print('  Copied: /static/')


# ── Build robots.txt and sitemap ───────────────────────────────────────────

def build_search(posts):
    import json as _json
    index = [{'title': p['title'], 'url': p['url'], 'tag': p['tag'], 'excerpt': p['excerpt']} for p in posts]
    (OUTPUT_DIR / 'search-index.json').write_text(_json.dumps(index), encoding='utf-8')
    print('  Built: /search-index.json')


def build_seo_files(posts):
    # robots.txt
    (OUTPUT_DIR / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\nSitemap: https://{SITE_DOMAIN}/sitemap.xml\n',
        encoding='utf-8'
    )

    # sitemap.xml
    urls = ['/', '/posts/', '/about/', '/contact/', '/privacy/', '/find-a-fix/', '/feedback/']
    for p in posts:
        urls.append(p['url'])

    today = datetime.now().strftime('%Y-%m-%d')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f'  <url><loc>https://{SITE_DOMAIN}{url}</loc><lastmod>{today}</lastmod></url>\n'
    xml += '</urlset>\n'
    (OUTPUT_DIR / 'sitemap.xml').write_text(xml, encoding='utf-8')

    # ads.txt
    (OUTPUT_DIR / 'ads.txt').write_text(
        'google.com, pub-5408659965693947, DIRECT, f08c47fec0942fa0\n',
        encoding='utf-8'
    )
    print('  Built: robots.txt + sitemap.xml + ads.txt')


# ── Main ───────────────────────────────────────────────────────────────────

PDF_GUIDES = [
    {
        'title': 'The Complete FDM Troubleshooting Guide',
        'description': 'A concise quick-reference guide covering every common FDM printing problem. Includes troubleshooting tables, material settings reference, calibration checklist and more. Instant PDF download.',
        'price': '£4.99',
        'preview': '/static/img/fdm-guide-preview-v2.jpg',
        'url': 'https://ko-fi.com/s/c36b362b04',
        'pages': '8 pages',
    },
]

def build_pdf_guides():
    cards = ''
    for g in PDF_GUIDES:
        cards += f'''
<div class="guide-card">
  <div class="guide-preview-wrap">
    <img src="{g["preview"]}" alt="{g["title"]} preview" class="guide-preview">
    <div class="guide-overlay">
      <a href="{g["url"]}" target="_blank" rel="noopener" class="btn">Buy for {g["price"]}</a>
    </div>
  </div>
  <div class="guide-info">
    <h2>{g["title"]}</h2>
    <p>{g["description"]}</p>
    <div class="guide-meta">
      <span>{g["pages"]}</span>
      <span class="guide-price">{g["price"]}</span>
    </div>
    <a href="{g["url"]}" target="_blank" rel="noopener" class="btn">Get the Guide &rarr;</a>
  </div>
</div>'''

    body = f'''<div class="article-wrap">
  <h1>PDF Guides</h1>
  <p class="section-sub">Downloadable quick-reference guides for 3D printing. Packed with tables, checklists and settings - no fluff.</p>
  <div class="guides-list">
    {cards}
  </div>
</div>'''

    page = base_html(
        title='PDF Guides - Print3DBuddy',
        body=body,
        description='Downloadable 3D printing PDF guides from Print3DBuddy. Quick-reference tables, troubleshooting, material settings and calibration checklists.',
        canonical='/pdf-guides/'
    )
    guides_dir = OUTPUT_DIR / 'pdf-guides'
    guides_dir.mkdir(exist_ok=True)
    (guides_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /pdf-guides/')


TEST_PRINTS = [
    {
        'id': 'overhang-test',
        'title': 'Overhang Test',
        'tagline': 'Find your printer\'s maximum overhang angle',
        'tag': 'Overhang',
        'summary': 'Prints 11 fins angled from 20° to 70° so you can see exactly where your printer starts to struggle with overhangs. Print it once without supports, check which fins look clean, and you\'ll know the precise angle at which to set your slicer\'s support threshold - no more guessing.',
        'stl': 'overhang_test.stl',
        'related': '/posts/how-to-calibrate-your-first-3d-printer/',
        'related_label': 'Calibration guide',
    },
    {
        'id': 'retraction-test',
        'title': 'Retraction / Stringing Test',
        'tagline': 'Dial in retraction and eliminate stringing for good',
        'tag': 'Retraction',
        'summary': 'Seven thin towers spaced 20mm apart force the printhead to travel across open air on every pass. Any excess filament oozing from the nozzle shows up as strings or blobs between the towers. Adjust retraction distance and temperature until the towers print clean - that\'s your dialled-in setting.',
        'stl': 'retraction_test.stl',
        'related': '/posts/how-to-fix-3d-printer-stringing/',
        'related_label': 'Stringing fix guide',
    },
    {
        'id': 'bridging-test',
        'title': 'Bridging Test',
        'tagline': 'Find the longest span your printer can cross without supports',
        'tag': 'Bridging',
        'summary': 'Five bridge sections spanning 10mm to 50mm, printed with nothing underneath. Flip the finished print and inspect each underside - a successful bridge is flat and smooth, a failing one sags. Knowing your bridge limit means you can model and slice with or without supports intelligently.',
        'stl': 'bridging_test.stl',
        'related': '/posts/3d-printing-supports-guide/',
        'related_label': 'Supports guide',
    },
    {
        'id': 'first-layer-test',
        'title': 'First Layer Calibration',
        'tagline': 'Get your Z offset right and nail first layer adhesion',
        'tag': 'First Layer',
        'summary': 'A thin 60×60mm grid square that makes your first layer immediately readable. Lines that merge together mean the nozzle is too close; lines that won\'t stick mean it\'s too far. Takes under 5 minutes to print and gives you a concrete target to tune your Z offset against.',
        'stl': 'first_layer_test.stl',
        'related': '/posts/3d-printing-first-layer-problems-fixes/',
        'related_label': 'First layer problems guide',
    },
    {
        'id': 'temp-tower',
        'title': 'Temperature Tower',
        'tagline': 'Find the ideal printing temperature for any filament',
        'tag': 'Temperature',
        'summary': 'Six stacked segments printed at descending temperatures from 220°C to 195°C - each with a small overhang tab. Compare surface finish, stringing, and overhang quality across the segments to find the sweet spot for a specific filament brand. Useful every time you switch to an unfamiliar spool.',
        'stl': 'temp_tower.stl',
        'related': '/posts/pla-vs-petg-vs-abs-which-filament-for-beginners/',
        'related_label': 'Filament comparison guide',
    },
    {
        'id': 'flow-rate-test',
        'title': 'Flow Rate Test',
        'tagline': 'Dial in your extrusion multiplier for clean, accurate prints',
        'tag': 'Flow Rate',
        'summary': 'Five flat tiles labelled 90% to 110% - each sliced with its corresponding flow rate in the slicer. Print all five, compare the top surfaces, and the smoothest tile with no gaps or ridges tells you your correct extrusion multiplier. Takes about 20 minutes and removes the guesswork from flow calibration.',
        'stl': 'flow_rate_test.stl',
        'related': '/posts/how-to-calibrate-flow-rate-extrusion-multiplier/',
        'related_label': 'Flow rate calibration guide',
    },
    {
        'id': 'ironing-test',
        'title': 'Ironing Test',
        'tagline': 'Find the right ironing settings for glass-smooth top surfaces',
        'tag': 'Ironing',
        'summary': 'Four flat tiles - one with no ironing as a baseline, then three with ironing enabled at 10%, 15%, and 20% flow. Split them in your slicer, assign the settings, and print all four. The tile with the smoothest, most glossy top surface is your ideal ironing flow rate.',
        'stl': 'ironing_test.stl',
        'related': '/posts/3d-printing-ironing-guide/',
        'related_label': 'Ironing settings guide',
    },
    {
        'id': 'tolerance-test',
        'title': 'Tolerance / Fit Test',
        'tagline': 'Find the right clearance for press fits, snap fits, and sliding joints',
        'tag': 'Dimensional',
        'summary': 'A set of labelled peg-and-hole pairs with clearances from 0.1mm to 0.5mm in 0.1mm steps. Print once and test each pair - press fit, light friction, and sliding clearance all reveal themselves immediately. Use the result to add the right offset to any functional part that needs to mate with another.',
        'stl': 'tolerance_test.stl',
        'related': '/posts/how-to-calibrate-flow-rate-extrusion-multiplier/',
        'related_label': 'Flow rate calibration guide',
    },
    {
        'id': 'elephant-foot-test',
        'title': 'Elephant Foot Calibration',
        'tagline': 'Dial in your first layer to eliminate base flare',
        'tag': 'First Layer',
        'summary': 'A flat disc with a precision cylinder rising from the centre. Measure the disc diameter and the cylinder diameter with calipers - if the disc is wider than designed, you have elephant foot. The amount of difference tells you exactly how much to adjust your Z offset or first layer flow. Takes under 10 minutes to print.',
        'stl': 'elephant_foot_test.stl',
        'related': '/posts/how-to-fix-elephant-foot/',
        'related_label': 'Elephant foot fix guide',
    },
]


def build_test_prints():
    cards = ''
    for i, t in enumerate(TEST_PRINTS, 1):
        download_url = f'https://tools.print3dbuddy.com/download/stl/{t["id"]}'
        cards += f'''
<div class="test-card" id="{t["id"]}">
  <div class="test-card-header">
    <span class="test-card-num">{i:02d}</span>
    <div class="test-card-titles">
      <h2>{t["title"]}</h2>
      <p class="test-tagline">{t["tagline"]}</p>
    </div>
    <span class="test-card-tag">{t["tag"]}</span>
  </div>
  <div class="test-card-body">
    <p class="test-summary">{t["summary"]}</p>
    <div class="test-card-actions">
      <div class="test-action-box">
        <strong>Full How-To Guide</strong>
        <p>Step-by-step instructions for running this test, reading the results, and adjusting your settings accordingly.</p>
        <div class="test-action-gate">
          <span class="lock-badge">&#9679; Paid members</span>
          <a href="https://tools.print3dbuddy.com/upgrade" class="test-upgrade-link">Upgrade &rarr;</a>
        </div>
      </div>
      <div class="test-action-box test-action-download">
        <strong>Download STL File</strong>
        <p>Print-ready calibration model. Works with any FDM printer and slicer.</p>
        <a href="{download_url}" class="btn-stl">Download STL &darr;</a>
        <p class="test-access-note">No account? <a href="https://tools.print3dbuddy.com/register">Register free</a><br>Have an account? <a href="https://tools.print3dbuddy.com/upgrade">Upgrade from &pound;2/mo</a></p>
      </div>
    </div>
    <p class="test-footer-link">Related reading: <a href="{t["related"]}">{t["related_label"]} &rarr;</a></p>
  </div>
</div>'''

    body = f'''<div class="article-wrap">
  <h1>Test Prints</h1>
  <p class="section-sub">Five calibration prints to dial in your FDM printer. Each one targets a specific setting - print it, read the result, fix the problem. Full how-to guides and STL downloads are available to paid members.</p>
  <div class="test-prints-list">
    {cards}
  </div>
</div>'''

    page = base_html(
        title='Test Prints - Print3DBuddy',
        body=body,
        description='Calibration test prints for FDM 3D printers. Overhang test, retraction test, bridging test, first layer calibration and temperature tower with full guides.',
        canonical='/test-prints/'
    )
    test_dir = OUTPUT_DIR / 'test-prints'
    test_dir.mkdir(exist_ok=True)
    (test_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /test-prints/')


def build_feedback():
    body = '''<div class="article-wrap" style="max-width:620px;">
  <a href="javascript:history.back()" class="back-link">&larr; Go back</a>
  <h1>Send Feedback</h1>
  <p style="color:var(--muted); margin-bottom:28px;">Got a problem to report, a guide suggestion, or something else? Fill in the form below and we will get back to you.</p>

  <div id="fb-limit-msg" style="display:none; background:#fffbeb; border:1px solid #fcd34d; border-radius:8px; padding:16px 20px; margin-bottom:24px; color:#92400e; font-size:0.93rem;">
    <strong>One submission per day.</strong> You have already sent feedback today - please come back tomorrow. This limit is in place to prevent spam.
  </div>

  <form id="fb-form" action="https://formspree.io/f/mnjgkqjg" method="POST">

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
      <div>
        <label for="fb-name">Name <span style="color:var(--muted); font-weight:400;">(optional)</span></label>
        <input type="text" id="fb-name" name="name" placeholder="Your name" style="margin-bottom:0;">
      </div>
      <div>
        <label for="fb-email">Email <span style="color:var(--muted); font-weight:400;">(optional)</span></label>
        <input type="email" id="fb-email" name="email" placeholder="So we can follow up" style="margin-bottom:0;">
      </div>
    </div>

    <div style="margin-bottom:16px;">
      <label for="fb-type">Issue type</label>
      <select id="fb-type" name="issue_type" style="margin-bottom:0;">
        <option value="not-listed">Issue not on list</option>
        <option value="missing-guide">Missing guide</option>
        <option value="tool-problem">Tool or calculator problem</option>
        <option value="other">Other / General feedback</option>
      </select>
    </div>

    <div style="margin-bottom:24px;">
      <label for="fb-message">Message</label>
      <textarea id="fb-message" name="message" rows="5" placeholder="Describe your issue or suggestion..." style="width:100%; padding:10px 12px; border:1px solid var(--border); border-radius:6px; font-size:1rem; font-family:inherit; resize:vertical;"></textarea>
    </div>

    <p style="font-size:0.82rem; color:var(--muted); margin-bottom:16px;">&#9432; Limited to one submission per day to prevent spam.</p>
    <button type="submit" class="btn" style="width:100%; padding:14px; font-size:1.05rem;">Send feedback</button>
  </form>

  <div id="fb-success" style="display:none; background:#f0fdf4; border:1px solid #86efac; border-radius:10px; padding:28px; text-align:center; margin-top:16px;">
    <p style="font-size:1.1rem; font-weight:700; color:#166534; margin-bottom:8px;">&#10003; Feedback sent - thank you!</p>
    <p style="color:var(--muted); font-size:0.93rem;">We read every submission and will follow up if you left an email.</p>
  </div>
</div>

<script>
  // Pre-fill issue type from URL param
  const params = new URLSearchParams(window.location.search);
  const type = params.get('type');
  if (type) {
    const sel = document.getElementById('fb-type');
    for (let i = 0; i < sel.options.length; i++) {
      if (sel.options[i].value === type) { sel.selectedIndex = i; break; }
    }
  }

  // Rate limit: one submission per day via localStorage
  const LIMIT_KEY = 'p3b_fb_last';
  const ONE_DAY = 86400000;
  const last = parseInt(localStorage.getItem(LIMIT_KEY) || '0');
  if (Date.now() - last < ONE_DAY) {
    document.getElementById('fb-limit-msg').style.display = 'block';
    document.getElementById('fb-form').style.display = 'none';
  }

  // Handle Formspree submission via fetch to show success message
  document.getElementById('fb-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      });
      if (res.ok) {
        localStorage.setItem(LIMIT_KEY, Date.now().toString());
        form.style.display = 'none';
        document.getElementById('fb-success').style.display = 'block';
      }
    } catch(err) {
      alert('Something went wrong. Please try again or email us directly.');
    }
  });
</script>'''

    page = base_html(
        title=f'Feedback | {SITE_NAME}',
        body=body,
        description='Send feedback to Print3DBuddy - report a missing guide, a site issue, or any suggestion.',
        canonical='/feedback/'
    )
    fb_dir = OUTPUT_DIR / 'feedback'
    fb_dir.mkdir(exist_ok=True)
    (fb_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /feedback/')


def build_find_a_fix():
    body = '''<div class="search-hero">
  <h1>Find a Fix</h1>
  <p>Tell us about your problem and we'll point you to the right guide.</p>
</div>

<div class="article-wrap" style="max-width:680px; margin-top:0; padding-top:40px;">

  <div class="faf-form">

    <div class="faf-group">
      <label class="faf-label">1. What type of printer do you have?</label>
      <div class="faf-toggle">
        <button class="faf-btn active" data-value="fdm" onclick="setPrinter('fdm')">FDM (filament)</button>
        <button class="faf-btn" data-value="resin" onclick="setPrinter('resin')">Resin (SLA/MSLA)</button>
      </div>
    </div>

    <div class="faf-group">
      <label class="faf-label">2. What's the problem?</label>
      <select id="problem-select" class="faf-select">
        <option value="">-- Select a problem --</option>
      </select>
    </div>

    <div class="faf-group" id="material-group">
      <label class="faf-label">3. What filament are you using?</label>
      <select id="material-select" class="faf-select">
        <option value="any">Any / Not sure</option>
        <option value="pla">PLA / PLA+</option>
        <option value="petg">PETG</option>
        <option value="abs">ABS / ASA</option>
        <option value="tpu">TPU / Flexible</option>
        <option value="nylon">Nylon / PC</option>
      </select>
    </div>

    <div class="faf-group">
      <label class="faf-label" id="exp-label">4. What's your experience level?</label>
      <select id="exp-select" class="faf-select">
        <option value="any">Any</option>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate / Advanced</option>
      </select>
    </div>

    <button class="btn" onclick="findFix()" style="width:100%; padding:14px; font-size:1.05rem; margin-top:8px;">Find articles &rarr;</button>
  </div>

  <div id="faf-results" style="margin-top:40px;"></div>

</div>

<style>
  .faf-form { display: flex; flex-direction: column; gap: 28px; }
  .faf-group { display: flex; flex-direction: column; gap: 10px; }
  .faf-label { font-weight: 700; font-size: 1rem; color: var(--text); }
  .faf-toggle { display: flex; gap: 10px; }
  .faf-btn {
    flex: 1; padding: 12px 20px; border: 2px solid var(--border); border-radius: 8px;
    background: #fff; font-size: 0.95rem; font-weight: 600; cursor: pointer;
    color: var(--muted); transition: all 0.15s;
  }
  .faf-btn.active { border-color: var(--accent); background: #fff3ed; color: var(--accent); }
  .faf-btn:hover:not(.active) { border-color: #ccc; color: var(--text); }
  .faf-select {
    width: 100%; padding: 12px 14px; border: 1px solid var(--border); border-radius: 8px;
    font-size: 0.97rem; color: var(--text); background: #fff; cursor: pointer;
    appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23666' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: right 14px center;
    padding-right: 38px;
  }
  .faf-select:focus { outline: 2px solid var(--accent); border-color: var(--accent); }
  .faf-results-title { font-size: 1.15rem; font-weight: 700; margin-bottom: 16px; color: var(--text); }
  .faf-card {
    border: 1px solid var(--border); border-radius: 10px; padding: 22px 24px;
    margin-bottom: 16px; transition: box-shadow 0.2s; background: #fff;
  }
  .faf-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
  .faf-card .tag { display: inline-block; background: #fff3ed; color: var(--accent); font-size: 0.75rem; font-weight: 600; padding: 2px 9px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; }
  .faf-card h3 { font-size: 1.05rem; margin-bottom: 6px; }
  .faf-card h3 a { color: var(--dark); text-decoration: none; }
  .faf-card h3 a:hover { color: var(--accent); }
  .faf-card p { color: var(--muted); font-size: 0.9rem; margin: 0 0 12px; line-height: 1.5; }
  .faf-no-results { background: var(--bg-alt); border: 1px solid var(--border); border-radius: 10px; padding: 24px; text-align: center; color: var(--muted); }
</style>

<script>
const FDM_PROBLEMS = [
  { value: 'stringing',      label: 'Stringing / oozing between parts' },
  { value: 'warping',        label: 'Warping / corners lifting off the bed' },
  { value: 'first-layer',    label: 'First layer not sticking' },
  { value: 'stuck',          label: 'Print stuck to the build plate' },
  { value: 'layer-adhesion', label: 'Weak layers / layers splitting apart' },
  { value: 'under-extrusion',label: 'Under-extrusion / gaps in the print' },
  { value: 'supports',       label: 'Supports (when to use / how to remove)' },
  { value: 'surface-quality',label: 'Poor surface quality or finish' },
  { value: 'strength',       label: 'Part not strong enough / breaking' },
  { value: 'speed-quality',  label: 'Speed vs quality tradeoff' },
  { value: 'slow-prints',    label: 'Prints are taking too long' },
  { value: 'calibration',    label: 'Printer calibration / new printer setup' },
  { value: 'layer-shifting', label: 'Layer shifting / print moving mid-print' },
  { value: 'over-extrusion', label: 'Over-extrusion / blobs and bulging walls' },
  { value: 'ghosting',       label: 'Ghosting / ringing / wavy artefacts near corners' },
  { value: 'material',       label: 'Choosing the right filament' },
  { value: 'slicer',         label: 'Slicer setup / getting started with software' },
  { value: 'maintenance',    label: 'Printer maintenance / keeping it running well' },
  { value: 'safety',        label: 'Safety / emissions / printing indoors' },
];

const RESIN_PROBLEMS = [
  { value: 'getting-started', label: 'Getting started with resin printing' },
  { value: 'general',         label: 'Choosing a resin printer' },
  { value: 'safety',          label: 'Safety / emissions / handling resin' },
];

const ARTICLES = [
  { slug: 'how-to-fix-3d-printer-stringing',         title: 'How to Fix 3D Printer Stringing',                tag: 'Troubleshooting', desc: 'Retraction settings, temperature, and travel speed explained clearly.',                            printer: 'fdm',   problems: ['stringing'],                          materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-3d-print-warping',             title: 'How to Fix 3D Print Warping',                    tag: 'Troubleshooting', desc: 'Bed adhesion, enclosures, brims, and material-specific tips.',                                   printer: 'fdm',   problems: ['warping'],                            materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-first-layer-problems-fixes',  title: 'First Layer Problems & Fixes',                   tag: 'Troubleshooting', desc: 'Every first layer problem - not sticking, warping, gaps, blobs - and how to fix each.',           printer: 'fdm',   problems: ['first-layer', 'calibration'],          materials: ['any'], exp: ['any'] },
  { slug: '3d-prints-stuck-to-build-plate-fixes',    title: 'Prints Stuck to the Build Plate: Fixes',         tag: 'Troubleshooting', desc: 'Z-offset, bed temp, PETG on PEI, and when to replace your build surface.',                        printer: 'fdm',   problems: ['stuck', 'first-layer'],               materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-layer-adhesion-problems-fixes', title: 'Layer Adhesion Problems & Fixes',              tag: 'Troubleshooting', desc: 'Causes, fixes, and a checklist to get strong, well-bonded prints every time.',                    printer: 'fdm',   problems: ['layer-adhesion', 'strength'],          materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-under-extrusion',              title: 'How to Fix Under-Extrusion',                     tag: 'Troubleshooting', desc: 'Every cause covered - extruder gear, clogs, temperature, E-steps, and filament quality.',        printer: 'fdm',   problems: ['under-extrusion', 'layer-adhesion'],  materials: ['any'], exp: ['any'] },
  { slug: 'complete-nozzle-guide-3d-printing',       title: 'Complete Nozzle Guide',                          tag: 'Hardware Guide',  desc: 'Sizes, materials, when to replace, and how to clear a clogged nozzle.',                         printer: 'fdm',   problems: ['under-extrusion', 'surface-quality'], materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-supports-guide',              title: '3D Printing Supports Guide',                     tag: 'Settings Guide',  desc: 'When to use supports, how to set them up, and how to remove them without damaging the print.',    printer: 'fdm',   problems: ['supports'],                           materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-speed-vs-quality-guide',      title: 'Speed vs Quality Guide',                         tag: 'Settings Guide',  desc: 'What actually limits speed, which settings to change, and profiles for different goals.',          printer: 'fdm',   problems: ['speed-quality', 'slow-prints', 'surface-quality'], materials: ['any'], exp: ['any'] },
  { slug: 'how-to-reduce-3d-print-time',             title: 'How to Reduce 3D Print Time',                    tag: 'Settings Guide',  desc: 'Layer height, infill, speed, and nozzle changes that make the biggest difference.',               printer: 'fdm',   problems: ['slow-prints', 'speed-quality'],        materials: ['any'], exp: ['any'] },
  { slug: '3d-print-orientation-part-strength-guide', title: 'Print Orientation & Part Strength',             tag: 'Settings Guide',  desc: 'Why orientation matters more than infill, with practical examples for common parts.',             printer: 'fdm',   problems: ['strength', 'layer-adhesion'],          materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-infill-patterns-guide',       title: 'Infill Patterns Guide',                          tag: 'Settings Guide',  desc: 'Which infill patterns to use for strength, speed, or flexibility - and what percentages to set.',  printer: 'fdm',   problems: ['strength', 'speed-quality'],           materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-ironing-guide',               title: 'Ironing Settings Guide',                         tag: 'Settings Guide',  desc: 'How to get glass-smooth top surfaces using ironing - settings, flow rates, when to skip it.',       printer: 'fdm',   problems: ['surface-quality'],                    materials: ['any'], exp: ['intermediate'] },
  { slug: 'how-to-post-process-3d-prints',           title: 'How to Post-Process 3D Prints',                  tag: 'Finishing Guide', desc: 'Sanding, priming, painting, and finishing 3D prints to a professional standard.',                  printer: 'fdm',   problems: ['surface-quality'],                    materials: ['any'], exp: ['any'] },
  { slug: 'how-to-calibrate-your-first-3d-printer',  title: 'How to Calibrate Your First 3D Printer',         tag: 'Beginner Guide',  desc: 'Bed levelling, E-steps, flow rate, and first layer - the complete calibration walkthrough.',       printer: 'fdm',   problems: ['calibration', 'first-layer'],          materials: ['any'], exp: ['beginner'] },
  { slug: 'best-pei-sheets-for-3d-printers',         title: 'Best PEI Sheets for 3D Printers',                tag: "Buyer\'s Guide",  desc: 'The cheapest single upgrade for better bed adhesion - top options compared.',                      printer: 'fdm',   problems: ['first-layer', 'warping', 'stuck'],     materials: ['any'], exp: ['any'] },
  { slug: 'best-3d-printer-upgrades-under-50',       title: 'Best Printer Upgrades Under £50',                tag: "Buyer\'s Guide",  desc: 'PEI sheets, Capricorn tubes, BLTouch, calipers - ranked by actual impact on print quality.',       printer: 'fdm',   problems: ['calibration', 'under-extrusion'],      materials: ['any'], exp: ['any'] },
  { slug: 'pla-vs-petg-vs-abs-which-filament-for-beginners', title: 'PLA vs PETG vs ABS - Which to Choose?', tag: 'Filament Guide',  desc: 'A plain-English comparison to help you pick the right material for your project.',                   printer: 'fdm',   problems: ['material'],                           materials: ['pla', 'petg', 'abs'], exp: ['beginner'] },
  { slug: 'tpu-flexible-filament-beginners-guide',   title: 'TPU Flexible Filament Guide',                    tag: 'Filament Guide',  desc: 'Settings, direct drive vs Bowden, avoiding jams, and what TPU is actually good for.',              printer: 'fdm',   problems: ['material', 'stringing', 'under-extrusion'], materials: ['tpu'], exp: ['any'] },
  { slug: 'best-filament-for-outdoor-use',           title: 'Best Filament for Outdoor Use',                  tag: 'Filament Guide',  desc: 'Which filaments survive UV, heat, and moisture - PETG, ASA, PC compared.',                        printer: 'fdm',   problems: ['material'],                           materials: ['petg', 'abs', 'nylon'], exp: ['any'] },
  { slug: 'how-to-store-filament-properly',          title: 'How to Store Filament Properly',                 tag: 'Filament Guide',  desc: 'Damp filament causes stringing and weak layers. Here is how to store and dry it properly.',         printer: 'fdm',   problems: ['material', 'stringing', 'layer-adhesion', 'under-extrusion'], materials: ['any'], exp: ['any'] },
  { slug: 'best-filament-brands-for-3d-printing',   title: 'Best Filament Brands',                           tag: 'Filament Guide',  desc: 'eSUN, Polymaker, Bambu Lab, Sunlu honestly compared for PLA, PETG, ABS and more.',                 printer: 'fdm',   problems: ['material'],                           materials: ['any'], exp: ['any'] },
  { slug: 'best-slicer-software-for-beginners',      title: 'Best Slicer Software for Beginners',             tag: 'Software Guide',  desc: 'Bambu Studio, PrusaSlicer, or Cura? A plain-English comparison with a clear recommendation.',      printer: 'fdm',   problems: ['slicer'],                             materials: ['any'], exp: ['beginner'] },
  { slug: 'how-to-design-3d-models-for-beginners',   title: 'How to Design Your Own 3D Models',               tag: 'Software Guide',  desc: 'Tinkercad, Fusion 360, FreeCAD - which to start with and why.',                                    printer: 'fdm',   problems: ['slicer'],                             materials: ['any'], exp: ['beginner'] },
  { slug: 'resin-3d-printing-beginners-guide',       title: 'Resin 3D Printing: Beginner Guide',              tag: 'Beginner Guide',  desc: 'How resin printing works, safety, settings, wash and cure, and the most common problems fixed.',    printer: 'resin', problems: ['getting-started', 'general'],         materials: ['any'], exp: ['beginner', 'any'] },
  { slug: 'best-resin-3d-printers-for-beginners',    title: 'Best Resin Printers for Beginners',              tag: 'Printer Reviews', desc: 'Elegoo Saturn 4, Mars 4, Phrozen Sonic Mini 8K honestly compared for value and ease of use.',       printer: 'resin', problems: ['general', 'getting-started'],         materials: ['any'], exp: ['beginner', 'any'] },
  { slug: 'how-to-fix-layer-shifting',               title: 'How to Fix Layer Shifting',                      tag: 'Troubleshooting', desc: 'Print shifting position mid-print? Loose belts, high acceleration, and stepper heat all explained.',  printer: 'fdm',   problems: ['layer-shifting'],                     materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-over-extrusion',               title: 'How to Fix Over-Extrusion',                      tag: 'Troubleshooting', desc: 'Blobs, bulging walls, or parts that do not fit? Flow rate, E-steps, temperature, and elephant foot.',  printer: 'fdm',   problems: ['over-extrusion', 'surface-quality'],  materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-ghosting-ringing',             title: 'How to Fix Ghosting and Ringing',                tag: 'Troubleshooting', desc: 'Wavy ripples near corners and text? Speed, acceleration, belt tension, and input shaper explained.',   printer: 'fdm',   problems: ['surface-quality', 'ghosting'],        materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-wet-filament',                 title: 'How to Fix Wet Filament',                        tag: 'Filament Guide',  desc: 'Crackling, rough surfaces, blobs? How to identify wet filament, dry it, and stop it happening again.', printer: 'fdm',   problems: ['stringing', 'surface-quality', 'layer-adhesion', 'under-extrusion'], materials: ['any'], exp: ['any'] },
  { slug: 'abs-asa-printing-guide',                  title: 'ABS and ASA Printing Guide',                     tag: 'Filament Guide',  desc: 'Enclosure requirements, settings, warping fixes, and bed adhesion tips for printing ABS and ASA.',      printer: 'fdm',   problems: ['warping', 'material', 'layer-adhesion'],  materials: ['abs'], exp: ['any'] },
  { slug: 'petg-printing-guide',                     title: 'PETG Printing Guide',                            tag: 'Filament Guide',  desc: 'Settings, stringing, bed adhesion, and storage tips - everything you need to print PETG reliably.',     printer: 'fdm',   problems: ['stringing', 'stuck', 'material', 'layer-adhesion'], materials: ['petg'], exp: ['any'] },
  { slug: 'how-to-maintain-3d-printer',              title: 'How to Maintain Your 3D Printer',                tag: 'Maintenance',     desc: 'Lubrication, belt checks, nozzle cleaning, and a simple schedule to prevent the most common problems.',  printer: 'fdm',   problems: ['calibration', 'under-extrusion', 'layer-shifting', 'maintenance'], materials: ['any'], exp: ['any'] },
  { slug: 'how-to-calibrate-pressure-advance',       title: 'How to Calibrate Pressure Advance',              tag: 'Settings Guide',  desc: 'Fix corner blobs and rounded edges on Klipper and Marlin printers with pressure advance calibration.',   printer: 'fdm',   problems: ['over-extrusion', 'surface-quality', 'calibration'], materials: ['any'], exp: ['intermediate'] },
  { slug: 'how-to-calibrate-flow-rate-extrusion-multiplier', title: 'How to Calibrate Flow Rate',             tag: 'Settings Guide',  desc: 'Fix rough top surfaces, weak prints, and dimensional inaccuracy with a simple flow rate calibration.',   printer: 'fdm',   problems: ['over-extrusion', 'surface-quality', 'calibration', 'under-extrusion'], materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-3d-printer-grinding-noise',    title: 'How to Fix 3D Printer Grinding Noises',          tag: 'Troubleshooting', desc: 'Grinding from the extruder, hotend, Z axis, or rails - diagnose by location and fix the right cause.',    printer: 'fdm',   problems: ['under-extrusion', 'maintenance', 'layer-shifting'],  materials: ['any'], exp: ['any'] },
  { slug: '3d-printing-emissions-indoor-safety',     title: 'Is 3D Printing Safe Indoors?',                   tag: 'Safety Guide',    desc: 'What research shows about FDM printer emissions - UFPs, VOCs, material comparisons, and how to reduce exposure.', printer: 'fdm',  problems: ['safety'],                             materials: ['any'], exp: ['any'] },
  { slug: 'resin-3d-printing-safety',                title: 'Resin 3D Printing Safety Guide',                 tag: 'Safety Guide',    desc: 'PPE, VOC emissions, handling uncured resin, safe disposal, and ventilation - the full safety guide.',         printer: 'resin', problems: ['safety', 'getting-started'],          materials: ['any'], exp: ['any'] },
  { slug: 'how-to-print-tpu-hinges-living-hinges',   title: 'How to Print TPU Hinges and Living Hinges',      tag: 'Filament Guide',  desc: 'Design principles, slicer settings, and fixes for the most common TPU living hinge problems.',                 printer: 'fdm',   problems: ['material', 'under-extrusion'],        materials: ['tpu'], exp: ['any'] },
  { slug: '3d-printing-for-cosplay',                 title: '3D Printing for Cosplay',                        tag: 'Ideas',           desc: 'Materials, workflow, post-processing, and practical tips for props, armour, and wearable cosplay pieces.',     printer: 'fdm',   problems: ['surface-quality', 'general'],         materials: ['any'], exp: ['any'] },
  { slug: 'how-to-finish-resin-prints',              title: 'How to Finish and Paint Resin 3D Prints',        tag: 'Finishing Guide', desc: 'Cleaning, support removal, sanding, priming, painting, and a final topcoat - the complete finishing workflow.',  printer: 'resin', problems: ['surface-quality', 'getting-started'], materials: ['any'], exp: ['any'] },
  { slug: 'how-to-fix-elephant-foot',                title: 'How to Fix Elephant Foot',                       tag: 'Troubleshooting', desc: 'Flared base ruining dimensional accuracy? Every cause and fix for elephant foot in FDM printing.',               printer: 'fdm',   problems: ['first-layer', 'calibration', 'over-extrusion'], materials: ['any'], exp: ['any'] },
  { slug: 'what-to-do-when-3d-print-fails-mid-print', title: 'What to Do When a Print Fails Mid-Print',      tag: 'Troubleshooting', desc: 'Spaghetti, layer shifts, adhesion failures - how to diagnose what went wrong and stop it happening again.',      printer: 'fdm',   problems: ['warping', 'layer-shifting', 'under-extrusion', 'general'], materials: ['any'], exp: ['any'] },
  { slug: 'petg-on-pei-problems-fixes',                title: 'PETG on PEI: Every Problem Fixed',               tag: 'Troubleshooting', desc: 'PETG fusing to PEI, not sticking, stringing, and Z-offset tips - every common PETG bed problem solved.',         printer: 'fdm',   problems: ['stuck', 'first-layer', 'stringing', 'material'],             materials: ['petg'], exp: ['any'] },
  { slug: 'nylon-3d-printing-guide',                   title: 'Nylon 3D Printing Guide',                         tag: 'Filament Guide',  desc: 'Settings, enclosure and drying requirements, bed adhesion, and hardware you need to print Nylon reliably.',       printer: 'fdm',   problems: ['material', 'warping', 'under-extrusion', 'layer-adhesion'],  materials: ['nylon'], exp: ['any'] },
  { slug: 'cura-vs-prusaslicer-vs-bambu-studio',        title: 'Cura vs PrusaSlicer vs Bambu Studio',             tag: 'Software Guide',  desc: 'An honest comparison for beginners and experienced users - which slicer to use and when to switch.',               printer: 'fdm',   problems: ['slicer', 'speed-quality'],                                   materials: ['any'], exp: ['any'] },
  { slug: 'how-to-tension-3d-printer-belts',            title: 'How to Tension 3D Printer Belts',                 tag: 'Maintenance',     desc: 'How to identify loose or over-tight belts, how to tension them correctly, and what to check after.',               printer: 'fdm',   problems: ['layer-shifting', 'ghosting', 'maintenance', 'calibration'],  materials: ['any'], exp: ['any'] },
  { slug: 'useful-things-to-3d-print-for-your-workshop', title: '15 Useful Things to 3D Print for Your Workshop', tag: 'Ideas',           desc: '15 genuinely useful workshop prints - tool holders, jigs, dust adapters, and organisers that earn their time.',      printer: 'fdm',   problems: ['general'],                                                   materials: ['any'], exp: ['any'] },
  { slug: 'input-shaper-resonance-compensation-guide',  title: 'Input Shaper and Resonance Compensation Guide',   tag: 'Settings Guide',  desc: 'Measure resonant frequencies, calibrate input shaper on Klipper or Bambu, and eliminate ghosting at higher speeds.',  printer: 'fdm',   problems: ['ghosting', 'surface-quality', 'calibration', 'speed-quality'], materials: ['any'], exp: ['intermediate'] },
  { slug: 'how-to-upgrade-3d-printer-hot-end',          title: 'How to Upgrade Your 3D Printer Hot End',          tag: 'Hardware Guide',  desc: 'E3D V6, Revo, Volcano - which hot end upgrade is worth it and what it actually changes.',                            printer: 'fdm',   problems: ['under-extrusion', 'material', 'maintenance'],                materials: ['any'], exp: ['any'] },
  { slug: '3d-printer-fire-safety-guide',               title: '3D Printer Fire Safety Guide',                    tag: 'Safety Guide',    desc: 'Thermal runaway, wiring checks, smoke detectors, and safe habits to prevent 3D printer fires.',                      printer: 'fdm',   problems: ['safety'],                                                    materials: ['any'], exp: ['any'] },
];

let currentPrinter = 'fdm';

function setPrinter(type) {
  currentPrinter = type;
  document.querySelectorAll('.faf-btn').forEach(b => b.classList.toggle('active', b.dataset.value === type));
  document.getElementById('material-group').style.display = type === 'fdm' ? 'flex' : 'none';
  const label = document.getElementById('exp-label');
  label.textContent = (type === 'fdm' ? '4.' : '3.') + ' What is your experience level?';
  buildProblemOptions(type);
  document.getElementById('faf-results').innerHTML = '';
}

function buildProblemOptions(type) {
  const sel = document.getElementById('problem-select');
  const problems = type === 'fdm' ? FDM_PROBLEMS : RESIN_PROBLEMS;
  sel.innerHTML = '<option value="">-- Select a problem --</option>' +
    problems.map(p => `<option value="${p.value}">${p.label}</option>`).join('');
}

function findFix() {
  const problem  = document.getElementById('problem-select').value;
  const material = document.getElementById('material-select').value;
  const exp      = document.getElementById('exp-select').value;
  const resultsEl = document.getElementById('faf-results');

  if (!problem) {
    resultsEl.innerHTML = '<div class="faf-no-results"><strong>Please select a problem first.</strong></div>';
    return;
  }

  const scored = ARTICLES
    .filter(a => a.printer === currentPrinter)
    .map(a => {
      let score = 0;
      if (a.problems.includes(problem)) score += 10;
      if (a.materials.includes(material) && material !== 'any') score += 3;
      else if (a.materials.includes('any')) score += 1;
      if (a.exp.includes(exp) && exp !== 'any') score += 2;
      return { ...a, score };
    })
    .filter(a => a.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 3);

  if (scored.length === 0) {
    resultsEl.innerHTML = '<div class="faf-no-results"><strong>No specific guides found for that combination.</strong><br><br><a href="/posts/">Browse all guides &rarr;</a></div>';
    return;
  }

  resultsEl.innerHTML = `<p class="faf-results-title">Recommended guides</p>` +
    scored.map(a => `
      <div class="faf-card">
        <span class="tag">${a.tag}</span>
        <h3><a href="/posts/${a.slug}/">${a.title}</a></h3>
        <p>${a.desc}</p>
        <a href="/posts/${a.slug}/" class="btn" style="padding:9px 20px; font-size:0.9rem;">Read guide &rarr;</a>
      </div>
    `).join('');

  resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Initialise
buildProblemOptions('fdm');
</script>

<div style="margin-top:40px; padding:28px 32px; background:#fff8f5; border:2px solid var(--accent); border-radius:12px; text-align:center;">
  <h2 style="font-size:1.1rem; font-weight:700; margin-bottom:8px;">Your issue not listed?</h2>
  <p style="color:var(--muted); font-size:0.93rem; margin-bottom:18px;">Let us know what problem you are having and we will look into adding a guide for it.</p>
  <a href="/feedback/?type=not-listed" class="btn">Report a missing issue &rarr;</a>
</div>'''

    page = base_html(
        title='Find a Fix | Print3DBuddy',
        body=body,
        description='Tell us your 3D printing problem and we will find the right guide for you - stringing, warping, first layer, under-extrusion, and more.',
        canonical='/find-a-fix/'
    )
    faf_dir = OUTPUT_DIR / 'find-a-fix'
    faf_dir.mkdir(exist_ok=True)
    (faf_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /find-a-fix/')


def main():
    print(f'\nBuilding {SITE_NAME}...')
    OUTPUT_DIR.mkdir(exist_ok=True)

    copy_static()
    posts = build_posts()
    build_homepage(posts)
    build_posts_index(posts)
    build_about()
    build_contact()
    build_privacy()
    build_search(posts)
    build_feedback()
    build_find_a_fix()
    build_test_prints()
    build_seo_files(posts)

    print(f'\nDone. {len(posts)} posts built -> {OUTPUT_DIR}/')


if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    main()

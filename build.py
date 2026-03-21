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
    ("All Guides", "/posts/"),
    ("Services", "https://tools.print3dbuddy.com"),
    ("Quick Guides", "https://tools.print3dbuddy.com/guides"),
    ("About", "/about/"),
    ("Search", "/search/"),
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
  <p>&copy; {year} {SITE_NAME} &mdash; Independent guides, no fluff.</p>
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
    cards = ''
    for p in posts:
        cards += f'''<article class="card">
  <span class="tag">{p["tag"]}</span>
  <h2><a href="{p["url"]}">{p["title"]}</a></h2>
  <p>{p["excerpt"]}</p>
  <a href="{p["url"]}" class="read-more">Read more &rarr;</a>
</article>
'''

    body = f'''<div class="hero">
  <h1>Your <span>3D Printing</span><br>Buddy on a Budget</h1>
  <p>Honest guides, filament comparisons, and beginner tips  -  without the jargon or the upsells.</p>
  <a href="/posts/" class="btn">Browse All Guides</a>
</div>
<main>
  <h2 class="section-title">Latest Guides</h2>
  <p class="section-sub">Practical help for 3D printing on a budget</p>
  <div class="articles">
{cards}  </div>
</main>'''

    page = base_html(
        title=f'{SITE_NAME}  -  {SITE_TAGLINE}',
        body=body,
        description='Honest guides, filament reviews, and beginner tips for budget 3D printing. No jargon, no upsells.',
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
  <p>Print3DBuddy is an independent site covering everything a beginner needs to get started with 3D printing  -  without spending a fortune.</p>
  <p>We cover printer calibration, filament selection, troubleshooting, and practical ideas for what to actually print. Our goal is plain-English guides that get you from "unboxing" to "printing confidently" as fast as possible.</p>
  <p>We don't take money from manufacturers and we don't pad reviews. If something is bad value, we say so.</p>
  <h2>What We Cover</h2>
  <ul>
    <li>Beginner setup and calibration guides</li>
    <li>Filament comparisons (PLA, PETG, ABS, ASA, TPU)</li>
    <li>Troubleshooting  -  stringing, warping, layer adhesion, and more</li>
    <li>Printer reviews focused on value for money</li>
    <li>Practical print ideas for home use</li>
  </ul>
  <p>Have a question or topic suggestion? <a href="/contact/">Get in touch</a>.</p>
</div>'''

    page = base_html(
        title=f'About | {SITE_NAME}',
        body=body,
        description='About Budget3DPrint  -  independent 3D printing guides for beginners on a budget.',
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
  <p>Email: <a href="mailto:CobyCane01@outlook.com">CobyCane01@outlook.com</a></p>
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
    # Write search index JSON
    index = [{'title': p['title'], 'url': p['url'], 'tag': p['tag'], 'excerpt': p['excerpt']} for p in posts]
    (OUTPUT_DIR / 'search-index.json').write_text(_json.dumps(index), encoding='utf-8')

    body = '''<div class="search-hero">
  <h1>Search Guides</h1>
  <p>Find articles on printers, filament, troubleshooting and more.</p>
  <div class="search-input-wrap">
    <input type="text" id="search-input" placeholder="e.g. stringing, filament, calibration..." autofocus>
  </div>
</div>
<div class="search-results-wrap">
  <div id="search-results"></div>
</div>
<script>
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  let index = [];

  fetch('/search-index.json')
    .then(r => r.json())
    .then(data => { index = data; });

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    if (q.length < 2) { results.innerHTML = ''; return; }
    const matches = index.filter(p =>
      p.title.toLowerCase().includes(q) ||
      p.excerpt.toLowerCase().includes(q) ||
      p.tag.toLowerCase().includes(q)
    );
    if (matches.length === 0) {
      results.innerHTML = '<p class="no-results">No articles found. Try a different search term.</p>';
      return;
    }
    results.innerHTML = matches.map(p => `
      <article class="search-result">
        <span class="search-result-tag">${p.tag}</span>
        <div class="search-result-body">
          <h2><a href="${p.url}">${p.title}</a></h2>
          <p>${p.excerpt}</p>
        </div>
      </article>
    `).join('');
  });
</script>'''

    page = base_html(
        title=f'Search | {SITE_NAME}',
        body=body,
        description='Search all 3D printing guides on Print3DBuddy.',
        canonical='/search/'
    )
    search_dir = OUTPUT_DIR / 'search'
    search_dir.mkdir(exist_ok=True)
    (search_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /search/')


def build_seo_files(posts):
    # robots.txt
    (OUTPUT_DIR / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\nSitemap: https://{SITE_DOMAIN}/sitemap.xml\n',
        encoding='utf-8'
    )

    # sitemap.xml
    urls = ['/', '/posts/', '/about/', '/contact/', '/privacy/', '/search/']
    for p in posts:
        urls.append(p['url'])

    today = datetime.now().strftime('%Y-%m-%d')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f'  <url><loc>https://{SITE_DOMAIN}{url}</loc><lastmod>{today}</lastmod></url>\n'
    xml += '</urlset>\n'
    (OUTPUT_DIR / 'sitemap.xml').write_text(xml, encoding='utf-8')
    print('  Built: robots.txt + sitemap.xml')


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
        'summary': 'Prints 11 fins angled from 20° to 70° so you can see exactly where your printer starts to struggle with overhangs. Print it once without supports, check which fins look clean, and you\'ll know the precise angle at which to set your slicer\'s support threshold — no more guessing.',
        'stl': 'overhang_test.stl',
        'related': '/posts/how-to-calibrate-your-first-3d-printer/',
        'related_label': 'Calibration guide',
    },
    {
        'id': 'retraction-test',
        'title': 'Retraction / Stringing Test',
        'tagline': 'Dial in retraction and eliminate stringing for good',
        'tag': 'Retraction',
        'summary': 'Seven thin towers spaced 20mm apart force the printhead to travel across open air on every pass. Any excess filament oozing from the nozzle shows up as strings or blobs between the towers. Adjust retraction distance and temperature until the towers print clean — that\'s your dialled-in setting.',
        'stl': 'retraction_test.stl',
        'related': '/posts/how-to-fix-3d-printer-stringing/',
        'related_label': 'Stringing fix guide',
    },
    {
        'id': 'bridging-test',
        'title': 'Bridging Test',
        'tagline': 'Find the longest span your printer can cross without supports',
        'tag': 'Bridging',
        'summary': 'Five bridge sections spanning 10mm to 50mm, printed with nothing underneath. Flip the finished print and inspect each underside — a successful bridge is flat and smooth, a failing one sags. Knowing your bridge limit means you can model and slice with or without supports intelligently.',
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
        'summary': 'Six stacked segments printed at descending temperatures from 220°C to 195°C — each with a small overhang tab. Compare surface finish, stringing, and overhang quality across the segments to find the sweet spot for a specific filament brand. Useful every time you switch to an unfamiliar spool.',
        'stl': 'temp_tower.stl',
        'related': '/posts/pla-vs-petg-vs-abs-which-filament-for-beginners/',
        'related_label': 'Filament comparison guide',
    },
    {
        'id': 'flow-rate-test',
        'title': 'Flow Rate Test',
        'tagline': 'Dial in your extrusion multiplier for clean, accurate prints',
        'tag': 'Flow Rate',
        'summary': 'Five flat tiles labelled 90% to 110% — each sliced with its corresponding flow rate in the slicer. Print all five, compare the top surfaces, and the smoothest tile with no gaps or ridges tells you your correct extrusion multiplier. Takes about 20 minutes and removes the guesswork from flow calibration.',
        'stl': 'flow_rate_test.stl',
        'related': '/posts/how-to-calibrate-flow-rate-extrusion-multiplier/',
        'related_label': 'Flow rate calibration guide',
    },
    {
        'id': 'ironing-test',
        'title': 'Ironing Test',
        'tagline': 'Find the right ironing settings for glass-smooth top surfaces',
        'tag': 'Ironing',
        'summary': 'Four flat tiles — one with no ironing as a baseline, then three with ironing enabled at 10%, 15%, and 20% flow. Split them in your slicer, assign the settings, and print all four. The tile with the smoothest, most glossy top surface is your ideal ironing flow rate.',
        'stl': 'ironing_test.stl',
        'related': '/posts/3d-printing-ironing-guide/',
        'related_label': 'Ironing settings guide',
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
  <p class="section-sub">Five calibration prints to dial in your FDM printer. Each one targets a specific setting &mdash; print it, read the result, fix the problem. Full how-to guides and STL downloads are available to paid members.</p>
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
    build_test_prints()
    build_seo_files(posts)

    print(f'\nDone. {len(posts)} posts built -> {OUTPUT_DIR}/')


if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    main()

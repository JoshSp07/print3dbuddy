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
        t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
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
        links += f'<li><a href="{href}">{label}</a></li>'
    return f'''<header>
  <nav>
    <a href="/" class="logo">Print3D<span>Buddy</span></a>
    <ul>{links}</ul>
  </nav>
</header>'''


def footer_html():
    year = datetime.now().year
    return f'''<footer>
  <p>&copy; {year} {SITE_NAME} &mdash; Independent reviews, no fluff.</p>
  <p><a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a> &middot; <a href="/contact/">Contact</a></p>
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
</head>
<body>
{nav_html()}
{body}
{footer_html()}
</body>
</html>'''


# ── Post metadata extraction ─────────────────────────────────────────────────

POST_TAGS = {
    'how-to-calibrate-your-first-3d-printer': ('Beginner Guide', 'Learn how to properly calibrate your first 3D printer — bed levelling, E-steps, flow rate, and more.'),
    'how-to-fix-3d-printer-stringing': ('Troubleshooting', 'Stringing ruining your prints? Here\'s how to fix it fast — retraction settings, temperature, and travel speed explained.'),
    'pla-vs-petg-vs-abs-which-filament-for-beginners': ('Filament Guide', 'PLA, PETG or ABS? A plain-English comparison to help beginners pick the right filament for their project.'),
    'best-filament-for-outdoor-use': ('Filament Guide', 'Which filaments survive UV, heat, and moisture? A practical guide to outdoor 3D printing materials.'),
    '10-useful-things-to-3d-print-for-your-home': ('Ideas & Inspiration', '10 genuinely useful things you can 3D print for around the house — practical, functional, beginner-friendly.'),
    'best-budget-3d-printers-under-200': ('Printer Reviews', 'The best 3D printers under $200 in 2025 — Bambu A1 Mini, Ender 3 V3 SE, Neptune 4 Pro compared for beginners.'),
    'best-slicer-software-for-beginners': ('Software Guide', 'Bambu Studio, PrusaSlicer, or Cura? A plain-English comparison of the best free slicer software for beginners.'),
    'how-to-fix-3d-print-warping': ('Troubleshooting', 'Warping ruining your prints? Here\'s how to fix it — bed adhesion, enclosures, brims, and material-specific tips.'),
    'where-to-download-free-3d-print-files': ('Resources', 'The best sites to download free 3D print files in 2025 — Printables, Thingiverse, Makerworld and more compared.'),
    '3d-printing-speed-vs-quality-guide': ('Settings Guide', 'How to balance 3D printing speed and quality — what limits speed, key settings, and profiles for different goals.'),
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
  <p>Honest guides, filament comparisons, and beginner tips — without the jargon or the upsells.</p>
  <a href="/posts/" class="btn">Browse All Guides</a>
</div>
<main>
  <h2 class="section-title">Latest Guides</h2>
  <p class="section-sub">Practical help for 3D printing on a budget</p>
  <div class="articles">
{cards}  </div>
</main>'''

    page = base_html(
        title=f'{SITE_NAME} — {SITE_TAGLINE}',
        body=body,
        description='Honest guides, filament reviews, and beginner tips for budget 3D printing. No jargon, no upsells.',
        canonical='/'
    )
    (OUTPUT_DIR / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /index.html')


# ── Build posts index ──────────────────────────────────────────────────────

def build_posts_index(posts):
    cards = ''
    for p in posts:
        cards += f'''<article class="card">
  <span class="tag">{p["tag"]}</span>
  <h2><a href="{p["url"]}">{p["title"]}</a></h2>
  <p>{p["excerpt"]}</p>
  <a href="{p["url"]}" class="read-more">Read more &rarr;</a>
</article>
'''
    body = f'''<main>
  <h1 class="section-title">All Guides</h1>
  <p class="section-sub">Every article on Budget3DPrint</p>
  <div class="articles">
{cards}  </div>
</main>'''

    page = base_html(
        title=f'All Guides | {SITE_NAME}',
        body=body,
        description='All 3D printing guides, filament reviews, and beginner tutorials on Budget3DPrint.',
        canonical='/posts/'
    )
    posts_index = OUTPUT_DIR / 'posts'
    posts_index.mkdir(exist_ok=True)
    (posts_index / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /posts/index.html')


# ── Build about page ───────────────────────────────────────────────────────

def build_about():
    body = '''<div class="article-wrap">
  <h1>About Budget3DPrint</h1>
  <p>Budget3DPrint is an independent site covering everything a beginner needs to get started with 3D printing — without spending a fortune.</p>
  <p>We cover printer calibration, filament selection, troubleshooting, and practical ideas for what to actually print. Our goal is plain-English guides that get you from "unboxing" to "printing confidently" as fast as possible.</p>
  <p>We don't take money from manufacturers and we don't pad reviews. If something is bad value, we say so.</p>
  <h2>What We Cover</h2>
  <ul>
    <li>Beginner setup and calibration guides</li>
    <li>Filament comparisons (PLA, PETG, ABS, ASA, TPU)</li>
    <li>Troubleshooting — stringing, warping, layer adhesion, and more</li>
    <li>Printer reviews focused on value for money</li>
    <li>Practical print ideas for home use</li>
  </ul>
  <p>Have a question or topic suggestion? <a href="/contact/">Get in touch</a>.</p>
</div>'''

    page = base_html(
        title=f'About | {SITE_NAME}',
        body=body,
        description='About Budget3DPrint — independent 3D printing guides for beginners on a budget.',
        canonical='/about/'
    )
    about_dir = OUTPUT_DIR / 'about'
    about_dir.mkdir(exist_ok=True)
    (about_dir / 'index.html').write_text(page, encoding='utf-8')
    print('  Built: /about/')


# ── Build privacy page ─────────────────────────────────────────────────────

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

def build_seo_files(posts):
    # robots.txt
    (OUTPUT_DIR / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\nSitemap: https://{SITE_DOMAIN}/sitemap.xml\n',
        encoding='utf-8'
    )

    # sitemap.xml
    urls = ['/', '/posts/', '/about/', '/privacy/']
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

def main():
    print(f'\nBuilding {SITE_NAME}...')
    OUTPUT_DIR.mkdir(exist_ok=True)

    copy_static()
    posts = build_posts()
    build_homepage(posts)
    build_posts_index(posts)
    build_about()
    build_privacy()
    build_seo_files(posts)

    print(f'\nDone. {len(posts)} posts built -> {OUTPUT_DIR}/')


if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    main()

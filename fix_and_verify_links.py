"""
1. Convert all 'text (https://url)' patterns in markdown to '[text](https://url)'
2. Verify every URL returns a valid response
"""

import re
import requests
from pathlib import Path

POSTS_DIR = Path("content/posts")

# Regex: captures "some text (https://url)" -> "[some text](https://url)"
# Handles **bold** text before the URL too
URL_PATTERN = re.compile(
    r'([A-Za-z\*_][^\n(]{1,80}?)\s+\(https://([\w.\-/?=&+%:,#@!~]+)\)'
)

def convert_links(text):
    """Convert 'text (https://url)' -> '[text](https://url)'"""
    def replace(m):
        link_text = m.group(1).strip()
        url = 'https://' + m.group(2)
        # Don't double-wrap already-formatted markdown links
        if link_text.startswith('['):
            return m.group(0)
        return f'[{link_text}]({url})'
    return URL_PATTERN.sub(replace, text)


def extract_urls(text):
    """Extract all https:// URLs from markdown text."""
    return re.findall(r'https://[\w.\-/?=&+%:,#@!~]+', text)


def check_url(url):
    """Return (url, status, ok)"""
    try:
        r = requests.get(url, timeout=10, allow_redirects=True,
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        ok = r.status_code < 400
        return url, r.status_code, ok
    except Exception as e:
        return url, str(e), False


def main():
    import os
    os.chdir(Path(__file__).parent)

    all_urls = set()

    print("Converting link format in markdown files...")
    for md in sorted(POSTS_DIR.glob("*.md")):
        text = md.read_text(encoding='utf-8')
        new_text = convert_links(text)
        if new_text != text:
            md.write_text(new_text, encoding='utf-8')
            print(f"  Converted: {md.name}")
        # Collect all URLs
        for url in extract_urls(new_text):
            all_urls.add(url.rstrip('.,)'))

    print(f"\nVerifying {len(all_urls)} unique URLs...")
    print("-" * 60)
    failed = []
    for url in sorted(all_urls):
        url_check, status, ok = check_url(url)
        icon = "OK " if ok else "FAIL"
        print(f"  [{icon}] {status:>3}  {url[:80]}")
        if not ok:
            failed.append((url, status))

    print("-" * 60)
    if failed:
        print(f"\n{len(failed)} failed URLs:")
        for url, status in failed:
            print(f"  FAIL {status} - {url}")
    else:
        print(f"\nAll {len(all_urls)} URLs verified OK.")


if __name__ == '__main__':
    main()

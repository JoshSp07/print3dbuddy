"""
Adds Amazon UK affiliate tag to all Amazon links in every article.
Converts amazon.com links to amazon.co.uk and appends the tag.
Run once from the 3dsite directory.
"""

import re
from pathlib import Path

ASSOCIATE_TAG = 'print3dbuddy21-21'
POSTS_DIR = Path('content/posts')

def add_tag(url):
    # Already has this tag - skip
    if ASSOCIATE_TAG in url:
        return url
    # Convert to UK store
    url = url.replace('www.amazon.com', 'www.amazon.co.uk')
    url = url.replace('amazon.com', 'amazon.co.uk')
    # Append tag
    if '?' in url:
        return url + f'&tag={ASSOCIATE_TAG}'
    else:
        return url + f'?tag={ASSOCIATE_TAG}'

total = 0
for md_file in sorted(POSTS_DIR.glob('*.md')):
    content = md_file.read_text(encoding='utf-8')
    # Find all amazon URLs inside markdown links or plain text
    new_content = re.sub(
        r'(https?://(?:www\.)?amazon\.co(?:m|\.uk)/[^\s\)\"\']+)',
        lambda m: add_tag(m.group(1)),
        content
    )
    count = new_content.count(ASSOCIATE_TAG) - content.count(ASSOCIATE_TAG)
    if count > 0:
        md_file.write_text(new_content, encoding='utf-8')
        print(f'  {md_file.name}: {count} link(s) updated')
        total += count

print(f'\nDone. {total} affiliate links added across all articles.')

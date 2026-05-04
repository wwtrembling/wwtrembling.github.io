"""
SRI (Subresource Integrity) hash injector.

Scans built HTML pages for known CDN <script src="..."> tags, fetches each
URL once, computes a sha384 base64 hash, and rewrites the tag to include
`integrity="sha384-..." crossorigin="anonymous"`.

Run after `build.py`:

    python3 _scripts/build.py
    python3 _scripts/inject_sri.py

If a CDN host is unreachable (sandboxed/offline), the script logs the URL
and leaves the tag unchanged so the build still works locally without
network access.
"""

from __future__ import annotations

import base64
import hashlib
import os
import re
import sys
import urllib.error
import urllib.request


CDN_URLS = [
    'https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js',
    'https://cdn.jsdelivr.net/npm/sql-formatter@15.0.2/dist/sql-formatter.min.js',
    'https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js',
    'https://cdn.jsdelivr.net/npm/diff@5.1.0/dist/diff.min.js',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_DIRS = ['ko', 'en', 'ja', 'zh-cn', 'zh-tw', 'hi', 'id', 'vi', 'th', 'de', 'pt']


def fetch_sri(url: str, timeout: int = 10) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            data = r.read()
    except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
        print(f"  unreachable ({type(e).__name__}): {url}")
        return None
    digest = hashlib.sha384(data).digest()
    return 'sha384-' + base64.b64encode(digest).decode('ascii')


def patch_file(path: str, integrity_by_url: dict[str, str]) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = 0
    for url, integrity in integrity_by_url.items():
        # Match <script ... src="URL"...></script> when integrity is missing.
        pattern = re.compile(
            r'(<script\b[^>]*\bsrc=["\']' + re.escape(url) + r'["\'][^>]*?)(\s*></script>)',
            re.DOTALL,
        )

        def repl(m):
            tag_open, tag_close = m.group(1), m.group(2)
            if 'integrity=' in tag_open:
                return m.group(0)
            return tag_open + f' integrity="{integrity}" crossorigin="anonymous"' + tag_close

        new, n = pattern.subn(repl, content)
        if n:
            content = new
            changed += n

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    return changed


def iter_html_files() -> list[str]:
    out: list[str] = []
    for d in LANG_DIRS:
        for root, _dirs, files in os.walk(os.path.join(BASE_DIR, d)):
            for f in files:
                if f.endswith('.html'):
                    out.append(os.path.join(root, f))
    out.append(os.path.join(BASE_DIR, 'index.html'))
    return out


def main() -> int:
    print("Fetching SRI hashes...")
    integrity_by_url: dict[str, str] = {}
    for url in CDN_URLS:
        h = fetch_sri(url)
        if h:
            print(f"  {h}  {url}")
            integrity_by_url[url] = h

    if not integrity_by_url:
        print("No CDN hosts reachable. Run this script in an environment with network access.")
        return 1

    print("\nInjecting integrity attributes...")
    total = 0
    for path in iter_html_files():
        n = patch_file(path, integrity_by_url)
        if n:
            total += n
    print(f"\nUpdated {total} <script> tag(s).")
    return 0


if __name__ == '__main__':
    sys.exit(main())

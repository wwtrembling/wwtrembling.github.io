import os
import re
from pathlib import Path

def main():
    base_dir = Path(r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf')
    target_langs = ['ko', 'en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']
    
    # Fragments
    manifest_link = '    <link rel="manifest" href="/manifest.json">\n'
    
    # We will inject the badge and install button inside the <header> or top of <main>
    # Actually, user asked for "Client-side Secure" messaging on all pages. 
    # Best place is typically under the H1.
    
    # We will look for </h1> and append the badge after it.
    
    # Badge HTML (using inline CSS for simplicity or we can add to main.css - inline is safer for injection)
    # Also added PWA install button (hidden by default)
    security_badge_html = """
            <div class="security-badge" style="display: flex; align-items: center; justify-content: center; gap: 8px; margin: 10px 0; font-size: 14px; color: var(--text-secondary);">
                <span title="Processed securely in client-side">🔒 Secure & Client-side</span>
                <button id="pwaInstallBtn" class="btn btn-primary" style="display: none; padding: 4px 12px; font-size: 12px;">📲 Install App</button>
            </div>
"""

    count = 0
    
    for lang in target_langs:
        lang_dir = base_dir / lang
        if not lang_dir.exists(): continue
        
        for file_path in lang_dir.rglob('*.html'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig_content = content
            
            # 1. Inject Manifest Link (in Head)
            if '/manifest.json' not in content:
                # Insert before </head>
                if '</head>' in content:
                    content = content.replace('</head>', manifest_link + '</head>')
            
            # 2. Inject Security Badge (After H1)
            if 'security-badge' not in content:
                # Find the closing h1 tag: </h1>
                # We can use regex to be safe about attributes in h1
                # But simple replace </h1> -> </h1> + badge is usually fine
                content = re.sub(r'(</h1>)', r'\1' + security_badge_html, content, count=1)
                
            # 3. Inject SEO Description update
            # Search for <meta name="description" content="...">
            # We want to append " (Processed securely in client-side)" inside the content attribute
            # But only if it's not already there
            if 'Processed securely' not in content:
                 def meta_replacer(match):
                     full_tag = match.group(0)
                     desc_content = match.group(1)
                     if "Processed securely" in desc_content: return full_tag
                     
                     new_desc = desc_content.rstrip('"') + " (Processed securely in client-side)"
                     return full_tag.replace(desc_content, new_desc)
                     
                 # Regex match <meta name="description" content="...something...">
                 content = re.sub(r'<meta name="description" content="([^"]+)">', meta_replacer, content)

            if content != orig_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                # print(f"Updated {file_path.name}")

    print(f"✅ Injected PWA & Security elements into {count} files.")

if __name__ == '__main__':
    main()

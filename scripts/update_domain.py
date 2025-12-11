"""
Replace all domain references with actual GitHub Pages URL
"""

import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent
OLD_DOMAIN = 'yourdomain.com'
NEW_DOMAIN = 'wwtrembling.github.io'

def update_domain_in_file(file_path):
    """Update domain in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if old domain exists
        if OLD_DOMAIN not in content:
            return False
        
        # Replace domain
        updated_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    print(f"🚀 Updating domain from {OLD_DOMAIN} to {NEW_DOMAIN}...\n")
    
    updated_count = 0
    total_count = 0
    
    # Update all HTML files
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file):
            continue
        
        total_count += 1
        if update_domain_in_file(html_file):
            print(f"✅ Updated: {html_file.relative_to(BASE_DIR)}")
            updated_count += 1
    
    # Update sitemap.xml
    sitemap = BASE_DIR / 'sitemap.xml'
    if sitemap.exists():
        total_count += 1
        if update_domain_in_file(sitemap):
            print(f"✅ Updated: sitemap.xml")
            updated_count += 1
    
    # Update robots.txt
    robots = BASE_DIR / 'robots.txt'
    if robots.exists():
        total_count += 1
        if update_domain_in_file(robots):
            print(f"✅ Updated: robots.txt")
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"✨ Domain Update Complete!")
    print(f"{'='*60}")
    print(f"📊 Total files checked: {total_count}")
    print(f"✅ Files updated: {updated_count}")
    print(f"🌐 New domain: https://{NEW_DOMAIN}/")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

"""
Insert Google AdSense code into all HTML files
"""

import os
from pathlib import Path

# AdSense script to insert in <head>
ADSENSE_SCRIPT = '''  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631"
     crossorigin="anonymous"></script>
'''

def insert_adsense_in_file(file_path):
    """Insert AdSense code into a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if AdSense is already inserted
        if 'pagead2.googlesyndication.com' in content:
            print(f"⏭️  Skipped (already has AdSense): {file_path}")
            return False
        
        # Find </head> tag and insert before it
        if '</head>' in content:
            content = content.replace('</head>', f'{ADSENSE_SCRIPT}\n</head>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated: {file_path}")
            return True
        else:
            print(f"⚠️  No </head> tag found: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Process all HTML files in the project"""
    base_dir = Path(__file__).parent
    
    print("🚀 Starting Google AdSense insertion...")
    print(f"📁 Base directory: {base_dir}\n")
    
    updated_count = 0
    skipped_count = 0
    total_count = 0
    
    # Find all HTML files
    for html_file in base_dir.rglob('*.html'):
        # Skip if it's in .git directory
        if '.git' in str(html_file):
            continue
            
        total_count += 1
        if insert_adsense_in_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"✨ AdSense Insertion Complete!")
    print(f"{'='*60}")
    print(f"📊 Total HTML files found: {total_count}")
    print(f"✅ Files updated: {updated_count}")
    print(f"⏭️  Files skipped: {skipped_count}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

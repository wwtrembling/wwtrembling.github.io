
import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

OLD_SNIPPET_PATTERN = r'<script\s+async\s+src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\?client=ca-pub-[\d]+"\s+crossorigin="anonymous"></script>'
NEW_SNIPPET = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631"\n     crossorigin="anonymous"></script>'

def update_adsense_in_file(file_path):
    """Update AdSense snippet in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if old snippet exists using regex because client id might vary or formatting might vary slightly
        if not re.search(OLD_SNIPPET_PATTERN, content, re.DOTALL):
            # If explicit pattern match fails, try a simpler check if the ID was just different or if it was already updated
             if 'client=ca-pub-6334819180242631' in content:
                 return False # Already has the new ID
             
             # If it has *any* adsbygoogle but not the specific one we are targeting, we might need to be careful.
             # But the user asked to change *all* pages.
             # Let's try to match a broader pattern if the specific one fails, 
             # essentially finding any adsbygoogle script block.
             
             BROADER_PATTERN = r'<script\s+async\s+src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js[^>]*>\s*</script>'
             if not re.search(BROADER_PATTERN, content, re.DOTALL):
                return False

        # Replace using regex to handle whitespace variations
        # We need to construct a regex that matches the tag safely
        # The user provided snippet has a specific ID.
        # I will replace ANY adsbygoogle script tag with the new one to be safe and uniform.
        
        REGEX_PATTERN = r'<script\s+async\s+src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-\d+"\s+crossorigin="anonymous"></script>'
        
        # Note: The existing file has it on two lines in some cases or one line.
        # Let's use a robust regex.
        ROBUST_REGEX = r'<script\s+async\s+src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=[^"]+"\s+crossorigin="anonymous"></script>'
        
        # Actually, looking at the grep output, it seems consistent.
        # But let's handle multiline potential.
        
        updated_content = re.sub(ROBUST_REGEX, NEW_SNIPPET, content, flags=re.DOTALL)
        
        # Also check for the exact formatting the user gave vs what might be in file (lines breaks)
        # The grep showed it might be on multiple lines in the file I viewed:
        # <script async src="...adsbygoogle.js?client=..."
        #      crossorigin="anonymous"></script>
        
        # Let's try to normalize it.
        
        if content == updated_content:
            # Try a slightly more flexible regex for multiline attributes if the first one failed
            ROBUST_REGEX_MULTILINE = r'<script\s+async\s+src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=[^"]+"\s+crossorigin="anonymous">\s*</script>'
            updated_content = re.sub(ROBUST_REGEX_MULTILINE, NEW_SNIPPET, content, flags=re.DOTALL | re.MULTILINE)
            
        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    print(f"🚀 Updating AdSense Snippets...\n")
    
    updated_count = 0
    total_count = 0
    
    # Update all HTML files
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file):
            continue
        
        total_count += 1
        if update_adsense_in_file(html_file):
            print(f"✅ Updated: {html_file.relative_to(BASE_DIR)}")
            updated_count += 1
            
    print(f"\n{'='*60}")
    print(f"✨ AdSense Update Complete!")
    print(f"{'='*60}")
    print(f"📊 Total files checked: {total_count}")
    print(f"✅ Files updated: {updated_count}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

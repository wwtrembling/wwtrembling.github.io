import os
import re
from pathlib import Path

def remove_ads():
    base_dir = Path(os.getcwd())
    # Target file pattern: */daily-verse/index.html
    # We'll just search for all daily-verse folder index.htmls
    
    count = 0
    for file_path in base_dir.rglob('daily-verse/index.html'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove Meta Tag
            # <meta name="google-adsense-account" content="ca-pub-6334819180242631">
            content = re.sub(r'\s*<meta name="google-adsense-account"[^>]*>', '', content)
            
            # Remove Script Tag
            # <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631"
            #    crossorigin="anonymous"></script>
            # Use dotall to match across lines
            content = re.sub(r'\s*<!-- Google AdSense -->\s*<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=[^"]+"\s+crossorigin="anonymous"></script>', '', content, flags=re.DOTALL)
            
            # Fallback regex if the comment is missing or slightly different
            content = re.sub(r'\s*<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=[^"]+"\s+crossorigin="anonymous"></script>', '', content, flags=re.DOTALL)

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Removed ads from: {file_path}")
                count += 1
            else:
                print(f"ℹ️ No ads found in: {file_path}")
                
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

    print(f"\n🎉 Finished. Processed {count} files.")

if __name__ == "__main__":
    remove_ads()

import os
import re
from pathlib import Path

def main():
    base_dir = Path(r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf')
    target_tools = ['sql-formatter', 'json-formatter'] # Start with known ones, but valid to scan all
    
    print("☕ Removing Coffee Banner...")
    
    count = 0
    # Scan all HTML files
    for file_path in base_dir.rglob('*.html'):
        if 'node_modules' in str(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        orig_content = content
        
        # Remove the HTML block (lenient regex)
        # <div style="margin: 20px 0;">\n                <a href="https://buymeacoffee.com/utilify" ... </a>\n            </div>
        
        # Regex to find the div wrapping the bmc-btn
        # We search for <a href="...buymeacoffee..." class="bmc-btn">...</a>
        # And the surrounding div if it exists.
        
        # Pattern 1: The specific block I saw
        pattern_div = r'<div style="margin: 20px 0;">\s*<a href="https://buymeacoffee\.com/utilify"[^>]*class="bmc-btn"[^>]*>[\s\S]*?</a>\s*</div>'
        content = re.sub(pattern_div, '', content)
        
        # Pattern 2: Javascript embedded CSS for bmc-btn
        # .bmc-btn { ... } .bmc-btn:hover { ... }
        # This is harder to regex safely without breaking other CSS.
        # But looking at the file, it was inside <style> tags in the head.
        
        # Let's try to remove the class definition if found
        pattern_css = r'\.bmc-btn\s*\{[\s\S]*?\}\s*\.bmc-btn:hover\s*\{[\s\S]*?\}'
        content = re.sub(pattern_css, '', content)
        
        if content != orig_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            # print(f"Cleaned {file_path.name}")
            
    print(f"✅ Removed Coffee Banner from {count} files.")

if __name__ == '__main__':
    main()

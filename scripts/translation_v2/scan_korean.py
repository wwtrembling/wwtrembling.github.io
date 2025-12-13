import os
import re
from pathlib import Path

def scan_korean_text(directory):
    korean_pattern = re.compile(r'[가-힣]+')
    unique_strings = set()
    
    print(f"Scanning {directory}...")
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                path = Path(root) / file
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Find all matches
                    # We want to capture the full context of the Korean text, usually between tags or in attributes
                    # Simplified approach: Look for lines with Korean
                    for line in content.split('\n'):
                        if korean_pattern.search(line):
                           # Clean up the line to extract the core string if possible
                           # But for now, just printing the line stripped is enough to see
                           stripped = line.strip()
                           # Extract content between tags >...<
                           tag_matches = re.findall(r'>([^<]*[가-힣]+[^<]*)<', stripped)
                           for m in tag_matches:
                               unique_strings.add(m.strip())
                               
                           # Extract attributes (placeholder="...", value="...", label="...")
                           attr_matches = re.findall(r'placeholder="([^"]*[가-힣]+[^"]*)"', stripped)
                           for m in attr_matches:
                               unique_strings.add(m.strip())

                           # NEW: Extract single/double quoted strings (for JS)
                           quote_matches = re.findall(r'[\'"]([^\'"]*[가-힣]+[^\'"]*)[\'"]', stripped)
                           for m in quote_matches:
                               unique_strings.add(m.strip())
                               
                           # Just raw korean words if missed by above
                           # (Optional, might be too noisy)
                           
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    print(f"\nFound {len(unique_strings)} unique Korean strings. Saving to korean_strings.txt...")
    with open('korean_strings.txt', 'w', encoding='utf-8') as f:
        for s in sorted(unique_strings):
            f.write(f"{s}\n")

if __name__ == "__main__":
    scan_korean_text(r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf\en')

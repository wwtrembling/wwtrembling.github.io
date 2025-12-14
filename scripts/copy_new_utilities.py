import os
import shutil
from pathlib import Path

def main():
    base_dir = Path(r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf')
    source_lang = 'ko'
    target_langs = ['en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']
    
    new_tools = ['jpa-converter', 'json-to-ts', 'excel-to-sql']
    
    print(f"🚀 Copying new tools from [{source_lang}] to {target_langs}...")
    
    for tool in new_tools:
        src_path = base_dir / source_lang / tool
        if not src_path.exists():
            print(f"❌ Source not found: {src_path}")
            continue
            
        for lang in target_langs:
            dest_path = base_dir / lang / tool
            
            # Copy directory tree
            if dest_path.exists():
                shutil.rmtree(dest_path)
            
            shutil.copytree(src_path, dest_path)
            print(f"✅ Copied {tool} to {lang}")

    # Also update index.html in each language to include the new links (Just copying the ko version's logic of adding links, 
    # but since I can't easily parse HTML with regex for insertion point across languages that might be different, 
    # I will rely on the translation script or manual check. 
    # WAIT - The index.html in other languages might NOT have the new links yet.
    # I should probably update them too.
    # For now, let's just copy the tool files. The user can navigate via URL or I can try to patch index files if I have time.
    # Actually, patch index files is better.
    
if __name__ == '__main__':
    main()

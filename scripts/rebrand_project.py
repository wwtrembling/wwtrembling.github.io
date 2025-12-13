"""
Rebrand Project: Replace "Tool Shelf" with "Utilify"
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent

# Files to ignore
IGNORE_DIRS = ['.git', '.gemini', '__pycache__', 'node_modules', 'assets', '.vscode'] # Skipping assets to avoid binary file issues, though textual assets might need change.
EXTENSIONS = ['.html', '.md', '.py', '.js', '.json', '.xml', '.txt']

OLD_NAME = "Tool Shelf"
NEW_NAME = "Utilify"

def rebrand_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if OLD_NAME in content:
            new_content = content.replace(OLD_NAME, NEW_NAME)
            
            # Additional cleanups if necessary (e.g., if "Utilify - Utilify" happens?)
            # Unlikely given simple replacement.
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated {file_path.relative_to(BASE_DIR)}")
            return True
            
        return False
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    print(f"🚀 Rebranding '{OLD_NAME}' -> '{NEW_NAME}'...\n")
    
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        # Ignore directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if not any(file.endswith(ext) for ext in EXTENSIONS):
                continue
                
            file_path = Path(root) / file
            
            # Skip this script itself to avoid recurring changes if run multiple times (though harmless)
            if file_path.name == "rebrand_project.py": continue
            
            if rebrand_file(file_path):
                count += 1
                
    print(f"\n✨ Rebranding Complete. Updated {count} files.")

if __name__ == '__main__':
    main()

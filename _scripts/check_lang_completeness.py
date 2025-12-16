
import sys
import os

# Add the parent directory to sys.path to import _data.lang
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from _data import lang
except ImportError:
    # If running from root
    sys.path.append(os.getcwd())
    from _data import lang

def check_missing_languages():
    languages = set(lang.LANGUAGES)
    print(f"Target languages: {languages}")
    
    missing_entries = {}
    
    for name, value in vars(lang).items():
        if name.isupper() and isinstance(value, dict) and name != "COMMON":
            # Check if it looks like a translation dict (has at least one lang key)
            keys = set(value.keys())
            if not keys.intersection(languages):
                continue
                
            missing = languages - keys
            if missing:
                missing_entries[name] = list(missing)
                output_str = f"[MISSING] {name}: {missing}\n"
                print(output_str.strip())
                with open(os.path.join(os.path.dirname(__file__), 'missing_lang_utf8.txt'), 'a', encoding='utf-8') as f:
                    f.write(output_str)

    return missing_entries

if __name__ == "__main__":
    # Clear file first
    with open(os.path.join(os.path.dirname(__file__), 'missing_lang_utf8.txt'), 'w', encoding='utf-8') as f:
        f.write("")
    check_missing_languages()

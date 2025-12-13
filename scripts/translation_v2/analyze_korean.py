import re

def analyze_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    categories = {
        'bible_verse': [],
        'date_month': [],
        'short_word': [],
        'sentence': [],
        'other': []
    }

    # Regex patterns
    bible_pattern = re.compile(r'^[가-힣]\s?\d+-\d+$') # e.g. 겔 1-3
    bible_abbr_pattern = re.compile(r'^[가-힣]{1,3}$') # e.g. 겔, 갈
    month_pattern = re.compile(r'^\d+월$')
    
    for line in lines:
        if bible_pattern.match(line):
            categories['bible_verse'].append(line)
        elif month_pattern.match(line):
            categories['date_month'].append(line)
        elif bible_abbr_pattern.match(line):
            # Could be bible abbr or just a short word like '금', '은'
            categories['short_word'].append(line)
        elif len(line) > 10:
            categories['sentence'].append(line)
        else:
            categories['other'].append(line)

    print("Summary:")
    for cat, items in categories.items():
        print(f"  {cat}: {len(items)}")
        if cat == 'sentence' or cat == 'other':
            print(f"    Examples: {items[:5]}")

if __name__ == '__main__':
    analyze_strings('korean_strings.txt')

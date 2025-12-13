import re

def extract_critical():
    with open('korean_strings.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    critical = []
    
    # Exclude basic patterns to focus on UI
    bible_pattern = re.compile(r'^[가-힣]\s?\d+-\d+$') 
    month_pattern = re.compile(r'^\d+월$')
    
    for line in lines:
        if not bible_pattern.match(line) and not month_pattern.match(line):
             critical.append(line)
             
    with open('critical_korean_strings.txt', 'w', encoding='utf-8') as f:
        for c in sorted(critical):
            f.write(f"{c}\n")
            
    print(f"Extracted {len(critical)} critical strings to critical_korean_strings.txt")

if __name__ == '__main__':
    extract_critical()


import os
import sys

# Add parent directory to path to import _data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from _data.lang import LANGUAGES, COMMON, INDEX_PAGE, SQL_FORMATTER, JSON_FORMATTER, BASE64_CONVERTER, PASSWORD_GENERATOR, UNIT_CONVERTER, DIFF_CHECKER, IMAGE_CONVERTER, QR_GENERATOR, COLOR_CONVERTER, LOREM_IPSUM, MARKDOWN_PREVIEWER, REGEX_TESTER, TEXT_UTILS, BMI_CALCULATOR, DATE_CALCULATOR, TIMER, IMAGE_WATERMARK, FAVICON_GENERATOR, THUMBNAIL_DOWNLOADER, REACTION_TEST, JSON_TO_EXCEL, JSON_LD_GENERATOR, PDF_TOOLS, TEXT_TO_DIAGRAM, DAILY_VERSE, IMAGE_EDITOR, JPA_CONVERTER, JSON_TO_TS, EXCEL_TO_SQL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, '_templates')

TOOLS_CONFIG = [
    ('json-to-excel', '📊', JSON_TO_EXCEL),
    ('image-watermark', '🛡️', IMAGE_WATERMARK),
    ('json-ld-generator', '🔍', JSON_LD_GENERATOR),
    ('pdf-tools', '📑', PDF_TOOLS),
    ('text-to-diagram', '📊', TEXT_TO_DIAGRAM),
    ('unit-converter', '📏', UNIT_CONVERTER),
    ('image-converter', '🖼️', IMAGE_CONVERTER),
    ('daily-verse', '📖', DAILY_VERSE),
    ('bmi-calculator', '⚖️', BMI_CALCULATOR),
    ('date-calculator', '📅', DATE_CALCULATOR),
    ('text-utils', '📝', TEXT_UTILS),
    ('json-formatter', '{ }', JSON_FORMATTER),
    ('color-converter', '🎨', COLOR_CONVERTER),
    ('timer', '⏱️', TIMER),
    ('base64-converter', '🔤', BASE64_CONVERTER),
    ('qr-generator', '📱', QR_GENERATOR),
    ('regex-tester', '🔍', REGEX_TESTER),
    ('sql-formatter', '🗄️', SQL_FORMATTER),
    ('image-editor', '✂️', IMAGE_EDITOR),
    ('lorem-ipsum', '📋', LOREM_IPSUM),
    ('favicon-generator', '🎯', FAVICON_GENERATOR),
    ('diff-checker', '🔀', DIFF_CHECKER),
    ('password-generator', '🔐', PASSWORD_GENERATOR),
    ('thumbnail-downloader', '📺', THUMBNAIL_DOWNLOADER),
    ('markdown-previewer', '📝', MARKDOWN_PREVIEWER),
    ('reaction-test', '⚡', REACTION_TEST),
    ('jpa-converter', '🏛️', JPA_CONVERTER),
    ('json-to-ts', '📜', JSON_TO_TS),
    ('excel-to-sql', '📊', EXCEL_TO_SQL),
]

def load_template(template_name):
    with open(os.path.join(TEMPLATE_DIR, template_name), 'r', encoding='utf-8') as f:
        return f.read()

def build_index_page():
    print("Building index pages...")
    template = load_template('index.html')
    
    for lang in LANGUAGES:
        # Prepare data
        data = COMMON.get(lang, COMMON['en']).copy()
        idx_data = INDEX_PAGE.get(lang, INDEX_PAGE['en'])
        data.update(idx_data)
        data['lang_code'] = lang
        
        # Generate alternate links
        alt_links = []
        for l in LANGUAGES:
            if l == 'zh-cn':
                hreflang = 'zh-Hans'
            elif l == 'zh-tw':
                hreflang = 'zh-Hant'
            else:
                hreflang = l
            alt_links.append(f'<link rel="alternate" hreflang="{hreflang}" href="https://utilifyapp.net/{l}/">')
            
        alt_links.append('<link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/">')
        data['alternate_links'] = '\n  '.join(alt_links)

        # Generate tool cards
        cards_html = []
        for tool_path, icon, tool_dict in TOOLS_CONFIG:
            t_data = tool_dict.get(lang, tool_dict.get('en', {}))
            title = t_data.get('title', tool_dict.get('en', {}).get('title', ''))
            
            # Try page_desc first, then meta_desc
            desc = t_data.get('page_desc', t_data.get('meta_desc', ''))
            
            # Fallback to English if missing
            if not title:
                title = tool_dict['en']['title']
            if not desc:
                desc = tool_dict['en'].get('page_desc', tool_dict['en'].get('meta_desc', ''))

            card = f'''
        <a href="/{lang}/{tool_path}/" class="card">
          <div class="card-icon">{icon}</div>
          <h3 class="card-title">{title}</h3>
          <p class="card-description">{desc}</p>
        </a>'''
            cards_html.append(card)
        
        data['tool_cards'] = '\n'.join(cards_html)
        
        # Replace placeholders
        content = template
        for key, value in data.items():
             content = content.replace(f'{{{{ {key} }}}}', str(value))
             
        # Write
        output_dir = os.path.join(BASE_DIR, lang)
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"  Generated {lang}/index.html")

def build_tool(tool_name, tool_data, template_file):
    print(f"Building {tool_name}...")
    template = load_template(template_file)
    
    for lang in LANGUAGES:
        # Merge common and specific data
        data = COMMON.get(lang, COMMON['en']).copy()
        specific_data = tool_data.get(lang, tool_data['en'])
        data.update(specific_data)
        data['lang_code'] = lang
        
        # Replace placeholders
        content = template
        for key, value in data.items():
            content = content.replace(f'{{{{ {key} }}}}', str(value))
            
        # Write to file
        output_dir = os.path.join(BASE_DIR, lang, tool_name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'index.html')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Generated {lang}/{tool_name}/index.html")

if __name__ == '__main__':
    # Build Index Pages
    build_index_page()

    # Build Tool Pages
    build_tool('sql-formatter', SQL_FORMATTER, 'sql-formatter.html')
    build_tool('json-formatter', JSON_FORMATTER, 'json-formatter.html')
    build_tool('base64-converter', BASE64_CONVERTER, 'base64-converter.html')
    build_tool('password-generator', PASSWORD_GENERATOR, 'password-generator.html')
    build_tool('unit-converter', UNIT_CONVERTER, 'unit-converter.html')
    build_tool('diff-checker', DIFF_CHECKER, 'diff-checker.html')
    build_tool('image-converter', IMAGE_CONVERTER, 'image-converter.html')
    build_tool('qr-generator', QR_GENERATOR, 'qr-generator.html')
    build_tool('color-converter', COLOR_CONVERTER, 'color-converter.html')
    build_tool('lorem-ipsum', LOREM_IPSUM, 'lorem-ipsum.html')
    build_tool('markdown-previewer', MARKDOWN_PREVIEWER, 'markdown-previewer.html')
    build_tool('regex-tester', REGEX_TESTER, 'regex-tester.html')
    build_tool('text-utils', TEXT_UTILS, 'text-utils.html')
    build_tool('bmi-calculator', BMI_CALCULATOR, 'bmi-calculator.html')
    build_tool('date-calculator', DATE_CALCULATOR, 'date-calculator.html')
    build_tool('timer', TIMER, 'timer.html')
    build_tool('image-watermark', IMAGE_WATERMARK, 'image-watermark.html')
    build_tool('favicon-generator', FAVICON_GENERATOR, 'favicon-generator.html')
    build_tool('thumbnail-downloader', THUMBNAIL_DOWNLOADER, 'thumbnail-downloader.html')
    build_tool('reaction-test', REACTION_TEST, 'reaction-test.html')
    print("Build complete!")


import os
import sys

# Add parent directory to path to import _data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from _data.lang import LANGUAGES, COMMON, INDEX_PAGE, SQL_FORMATTER, JSON_FORMATTER, BASE64_CONVERTER, PASSWORD_GENERATOR, UNIT_CONVERTER, DIFF_CHECKER, IMAGE_CONVERTER, QR_GENERATOR, COLOR_CONVERTER, LOREM_IPSUM, MARKDOWN_PREVIEWER, REGEX_TESTER, TEXT_UTILS, BMI_CALCULATOR, DATE_CALCULATOR, TIMER, IMAGE_WATERMARK, FAVICON_GENERATOR, THUMBNAIL_DOWNLOADER, REACTION_TEST

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, '_templates')

TOOLS_CONFIG = [
    ('image-watermark', '🛡️', IMAGE_WATERMARK),
    ('unit-converter', '📏', UNIT_CONVERTER),
    ('image-converter', '🖼️', IMAGE_CONVERTER),
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
    ('lorem-ipsum', '📋', LOREM_IPSUM),
    ('favicon-generator', '🎯', FAVICON_GENERATOR),
    ('diff-checker', '🔀', DIFF_CHECKER),
    ('password-generator', '🔐', PASSWORD_GENERATOR),
    ('thumbnail-downloader', '📺', THUMBNAIL_DOWNLOADER),
    ('markdown-previewer', '📝', MARKDOWN_PREVIEWER),
    ('reaction-test', '⚡', REACTION_TEST),
]

def load_template(template_name):
    path = os.path.join(TEMPLATE_DIR, template_name)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"  WARN: template not found, skipping: {template_name}")
        return None

def build_index_page():
    print("Building index pages...")
    template = load_template('index.html')
    
    for lang in LANGUAGES:
        # Prepare data: English fallback for any missing sub-keys
        data = COMMON.get('en', {}).copy()
        data.update(COMMON.get(lang, {}))
        data.update(INDEX_PAGE.get('en', {}))
        data.update(INDEX_PAGE.get(lang, {}))
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

def build_alt_links(tool_path):
    alt = []
    for l in LANGUAGES:
        if l == 'zh-cn':
            hreflang = 'zh-Hans'
        elif l == 'zh-tw':
            hreflang = 'zh-Hant'
        else:
            hreflang = l
        alt.append(f'<link rel="alternate" hreflang="{hreflang}" href="https://utilifyapp.net/{l}/{tool_path}/">')
    alt.append(f'<link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/{tool_path}/">')
    return '\n    '.join(alt)


def build_tool(tool_name, tool_data, template_file):
    print(f"Building {tool_name}...")
    template = load_template(template_file)
    if template is None:
        return

    alt_links_html = build_alt_links(tool_name)

    for lang in LANGUAGES:
        # Merge common and specific data with English as fallback for missing sub-keys
        data = COMMON.get('en', {}).copy()
        data.update(COMMON.get(lang, {}))
        data.update(tool_data.get('en', {}))
        data.update(tool_data.get(lang, {}))
        data['lang_code'] = lang
        data['alternate_links'] = alt_links_html

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


def hreflang_for(lang):
    if lang == 'zh-cn':
        return 'zh-Hans'
    if lang == 'zh-tw':
        return 'zh-Hant'
    return lang


def build_sitemap(today=None):
    print("Building sitemap.xml...")
    from datetime import date
    lastmod = (today or date.today()).isoformat()

    paths = ['']  # root
    paths += [f'{l}/' for l in LANGUAGES]
    for tool_path, _icon, _data in TOOLS_CONFIG:
        for l in LANGUAGES:
            paths.append(f'{l}/{tool_path}/')

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']

    def emit(loc, alternates=None):
        lines.append('  <url>')
        lines.append(f'    <loc>{loc}</loc>')
        lines.append(f'    <lastmod>{lastmod}</lastmod>')
        if alternates:
            for hl, href in alternates:
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{href}"/>')
        lines.append('  </url>')

    # Root
    emit('https://utilifyapp.net/')

    # Language home pages with hreflang siblings
    home_alts = [(hreflang_for(l), f'https://utilifyapp.net/{l}/') for l in LANGUAGES]
    home_alts.append(('x-default', 'https://utilifyapp.net/en/'))
    for l in LANGUAGES:
        emit(f'https://utilifyapp.net/{l}/', home_alts)

    # Tool pages with hreflang siblings
    for tool_path, _icon, _data in TOOLS_CONFIG:
        tool_alts = [(hreflang_for(l), f'https://utilifyapp.net/{l}/{tool_path}/') for l in LANGUAGES]
        tool_alts.append(('x-default', f'https://utilifyapp.net/en/{tool_path}/'))
        for l in LANGUAGES:
            emit(f'https://utilifyapp.net/{l}/{tool_path}/', tool_alts)

    lines.append('</urlset>')
    out = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"  Generated sitemap.xml ({len(paths)} urls)")


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

    # Build sitemap.xml
    build_sitemap()

    print("Build complete!")

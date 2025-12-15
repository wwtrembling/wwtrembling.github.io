
import os
import sys

# Add parent directory to path to import _data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from _data.lang import LANGUAGES, COMMON, SQL_FORMATTER, JSON_FORMATTER, BASE64_CONVERTER, PASSWORD_GENERATOR, UNIT_CONVERTER, DIFF_CHECKER, IMAGE_CONVERTER, QR_GENERATOR, COLOR_CONVERTER, LOREM_IPSUM, MARKDOWN_PREVIEWER, REGEX_TESTER, TEXT_UTILS, BMI_CALCULATOR, DATE_CALCULATOR, TIMER, IMAGE_WATERMARK, FAVICON_GENERATOR, THUMBNAIL_DOWNLOADER, REACTION_TEST

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, '_templates')

def load_template(template_name):
    with open(os.path.join(TEMPLATE_DIR, template_name), 'r', encoding='utf-8') as f:
        return f.read()

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

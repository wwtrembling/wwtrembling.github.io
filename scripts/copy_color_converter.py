"""
Copy functional color converter implementation to all languages
"""

import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent

# Language configurations with translations
TRANSLATIONS = {
    'ko': {
        'title': '색상 변환기',
        'desc': 'HEX, RGB, HSL 색상 형식 간 변환을 수행하세요. 실시간 색상 미리보기와 간편한 복사 기능.',
        'formats_title': '색상 형식',
        'copy_btn': '복사',
        'sliders_title': 'RGB 슬라이더',
        'red': '빨강',
        'green': '초록',
        'blue': '파랑',
        'popular_title': '인기 색상',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Color Converter',
        'desc': 'Convert between HEX, RGB, and HSL color formats. Real-time preview and easy copying.',
        'formats_title': 'Color Formats',
        'copy_btn': 'Copy',
        'sliders_title': 'RGB Sliders',
        'red': 'Red',
        'green': 'Green',
        'blue': 'Blue',
        'popular_title': 'Popular Colors',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': 'カラーコンバーター',
        'desc': 'HEX、RGB、HSLカラー形式間で変換します。リアルタイムプレビューと簡単なコピー機能。',
        'formats_title': 'カラーフォーマット',
        'copy_btn': 'コピー',
        'sliders_title': 'RGBスライダー',
        'red': '赤',
        'green': '緑',
        'blue': '青',
        'popular_title': '人気の色',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'रंग कनवर्टर',
        'desc': 'HEX, RGB और HSL रंग प्रारूपों के बीच बदलें। रीयल-टाइम पूर्वावलोकन और आसान कॉपी करना।',
        'formats_title': 'रंग प्रारूप',
        'copy_btn': 'कॉपी',
        'sliders_title': 'RGB स्लाइडर',
        'red': 'लाल',
        'green': 'हरा',
        'blue': 'नीला',
        'popular_title': 'लोकप्रिय रंग',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Konverter Warna',
        'desc': 'Konversi antara format warna HEX, RGB, dan HSL. Pratinjau real-time dan penyalinan mudah.',
        'formats_title': 'Format Warna',
        'copy_btn': 'Salin',
        'sliders_title': 'Slider RGB',
        'red': 'Merah',
        'green': 'Hijau',
        'blue': 'Biru',
        'popular_title': 'Warna Populer',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Chuyển Đổi Màu',
        'desc': 'Chuyển đổi giữa các định dạng màu HEX, RGB và HSL. Xem trước thời gian thực và sao chép dễ dàng.',
        'formats_title': 'Định Dạng Màu',
        'copy_btn': 'Sao chép',
        'sliders_title': 'Thanh Trượt RGB',
        'red': 'Đỏ',
        'green': 'Xanh lá',
        'blue': 'Xanh dương',
        'popular_title': 'Màu Phổ Biến',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'ตัวแปลงสี',
        'desc': 'แปลงระหว่างรูปแบบสี HEX, RGB และ HSL ดูตัวอย่างแบบเรียลไทม์และคัดลอกง่าย',
        'formats_title': 'รูปแบบสี',
        'copy_btn': 'คัดลอก',
        'sliders_title': 'แถบเลื่อน RGB',
        'red': 'แดง',
        'green': 'เขียว',
        'blue': 'น้ำเงิน',
        'popular_title': 'สียอดนิยม',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Farbkonverter',
        'desc': 'Konvertieren zwischen HEX-, RGB- und HSL-Farbformaten. Echtzeit-Vorschau und einfaches Kopieren.',
        'formats_title': 'Farbformate',
        'copy_btn': 'Kopieren',
        'sliders_title': 'RGB-Schieberegler',
        'red': 'Rot',
        'green': 'Grün',
        'blue': 'Blau',
        'popular_title': 'Beliebte Farben',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Conversor de Cores',
        'desc': 'Converta entre formatos de cores HEX, RGB e HSL. Visualização em tempo real e cópia fácil.',
        'formats_title': 'Formatos de Cores',
        'copy_btn': 'Copiar',
        'sliders_title': 'Controles RGB',
        'red': 'Vermelho',
        'green': 'Verde',
        'blue': 'Azul',
        'popular_title': 'Cores Populares',
        'ad_text': 'Espaço Publicitário'
    }
}

def read_english_template():
    """Read the English color converter as template"""
    en_file = BASE_DIR / 'en' / 'color-converter' / 'index.html'
    with open(en_file, 'r', encoding='utf-8') as f:
        return f.read()

def generate_color_converter(lang, template):
    """Generate color converter for a specific language"""
    t = TRANSLATIONS[lang]
    
    content = template
    
    # Replace lang attribute
    content = content.replace('lang="en"', f'lang="{lang}"')
    
    # Replace title and description
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{t["title"]} - Utilify</title>',
        content
    )
    content = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{t["desc"]}">',
        content
    )
    
    # Replace Open Graph
    content = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="{t["title"]} - Utilify">',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content=".*?">',
        f'<meta property="og:description" content="{t["desc"]}">',
        content
    )
    
    # Replace URLs
    content = content.replace('/en/color-converter/', f'/{lang}/color-converter/')
    content = content.replace('href="/en/"', f'href="/{lang}/"')
    content = content.replace('"inLanguage": "en"', f'"inLanguage": "{lang}"')
    content = content.replace('"name": "Color Converter"', f'"name": "{t["title"]}"')
    content = re.sub(
        r'"description": "Convert between HEX.*?"',
        f'"description": "{t["desc"]}"',
        content,
        count=1
    )
    
    # Replace UI text
    content = content.replace('<h1>🎨 Color Converter</h1>', f'<h1>🎨 {t["title"]}</h1>')
    content = re.sub(
        r'<p>Convert between HEX.*?</p>',
        f'<p>{t["desc"]}</p>',
        content,
        count=1
    )
    
    # Replace form labels
    content = content.replace('<h3>Color Formats</h3>', f'<h3>{t["formats_title"]}</h3>')
    content = content.replace('>Copy</button>', f'>{t["copy_btn"]}</button>')
    content = content.replace('<h3>RGB Sliders</h3>', f'<h3>{t["sliders_title"]}</h3>')
    content = content.replace('<span>Red</span>', f'<span>{t["red"]}</span>')
    content = content.replace('<span>Green</span>', f'<span>{t["green"]}</span>')
    content = content.replace('<span>Blue</span>', f'<span>{t["blue"]}</span>')
    content = content.replace('<h3>Popular Colors</h3>', f'<h3>{t["popular_title"]}</h3>')
    content = content.replace('<p>Ad Space</p>', f'<p>{t["ad_text"]}</p>')
    
    return content

def main():
    print("🚀 Copying color converter functionality to all languages...\n")
    
    # Read English template
    template = read_english_template()
    print("✅ Read English template\n")
    
    # Generate for each language except English
    updated = 0
    for lang in TRANSLATIONS.keys():
        if lang == 'en':
            continue
            
        output_file = BASE_DIR / lang / 'color-converter' / 'index.html'
        content = generate_color_converter(lang, template)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {lang}/color-converter/index.html")
        updated += 1
    
    print(f"\n{'='*60}")
    print(f"✨ Complete! Updated {updated} language versions")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

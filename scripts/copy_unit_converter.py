"""
Copy functional unit converter implementation to all languages
"""

import os
from pathlib import Path
import re

# Base directory
BASE_DIR = Path(__file__).parent

# Language configurations with translations
TRANSLATIONS = {
    'ko': {
        'title': '단위 변환기',
        'desc': '길이, 무게, 온도, 부피 등 다양한 단위를 간편하게 변환하세요. 미터, 피트, 킬로그램, 파운드, 섭씨, 화씨 등 모든 주요 단위 지원.',
        'category_label': '변환 카테고리',
        'from_label': '변환할 값',
        'to_label': '변환된 값',
        'input_placeholder': '숫자 입력',
        'result_placeholder': '결과',
        'swap_title': '단위 교환',
        'quick_ref_title': '자주 사용하는 변환',
        'ad_text': '광고 영역',
        'categories': {
            'length': '길이',
            'weight': '무게',
            'temperature': '온도',
            'volume': '부피',
            'area': '면적',
            'speed': '속도'
        }
    },
    'en': {
        'title': 'Unit Converter',
        'desc': 'Convert length, weight, temperature, volume and more. Supports all major units including meters, feet, kilograms, pounds, Celsius, Fahrenheit.',
        'category_label': 'Conversion Category',
        'from_label': 'From',
        'to_label': 'To',
        'input_placeholder': 'Enter number',
        'result_placeholder': 'Result',
        'swap_title': 'Swap units',
        'quick_ref_title': 'Quick Reference',
        'ad_text': 'Ad Space',
        'categories': {
            'length': 'Length',
            'weight': 'Weight',
            'temperature': 'Temperature',
            'volume': 'Volume',
            'area': 'Area',
            'speed': 'Speed'
        }
    },
    'ja': {
        'title': '単位変換器',
        'desc': '長さ、重さ、温度、体積などを簡単に変換できます。メートル、フィート、キログラム、ポンド、摂氏、華氏などすべての主要単位をサポート。',
        'category_label': '変換カテゴリ',
        'from_label': '変換元',
        'to_label': '変換先',
        'input_placeholder': '数値を入力',
        'result_placeholder': '結果',
        'swap_title': '単位を交換',
        'quick_ref_title': 'クイックリファレンス',
        'ad_text': '広告スペース',
        'categories': {
            'length': '長さ',
            'weight': '重さ',
            'temperature': '温度',
            'volume': '体積',
            'area': '面積',
            'speed': '速度'
        }
    },
    'hi': {
        'title': 'यूनिट कनवर्टर',
        'desc': 'लंबाई, वजन, तापमान, आयतन और अधिक परिवर्तित करें। मीटर, फीट, किलोग्राम, पाउंड, सेल्सियस, फ़ारेनहाइट सहित सभी प्रमुख इकाइयों का समर्थन करता है।',
        'category_label': 'रूपांतरण श्रेणी',
        'from_label': 'से',
        'to_label': 'तक',
        'input_placeholder': 'संख्या दर्ज करें',
        'result_placeholder': 'परिणाम',
        'swap_title': 'इकाइयाँ बदलें',
        'quick_ref_title': 'त्वरित संदर्भ',
        'ad_text': 'विज्ञापन स्थान',
        'categories': {
            'length': 'लंबाई',
            'weight': 'वजन',
            'temperature': 'तापमान',
            'volume': 'आयतन',
            'area': 'क्षेत्रफल',
            'speed': 'गति'
        }
    },
    'id': {
        'title': 'Konverter Satuan',
        'desc': 'Konversi panjang, berat, suhu, volume dan lainnya. Mendukung semua unit utama termasuk meter, kaki, kilogram, pon, Celsius, Fahrenheit.',
        'category_label': 'Kategori Konversi',
        'from_label': 'Dari',
        'to_label': 'Ke',
        'input_placeholder': 'Masukkan angka',
        'result_placeholder': 'Hasil',
        'swap_title': 'Tukar satuan',
        'quick_ref_title': 'Referensi Cepat',
        'ad_text': 'Ruang Iklan',
        'categories': {
            'length': 'Panjang',
            'weight': 'Berat',
            'temperature': 'Suhu',
            'volume': 'Volume',
            'area': 'Luas',
            'speed': 'Kecepatan'
        }
    },
    'vi': {
        'title': 'Chuyển Đổi Đơn Vị',
        'desc': 'Chuyển đổi độ dài, trọng lượng, nhiệt độ, thể tích và hơn thế nữa. Hỗ trợ tất cả các đơn vị chính bao gồm mét, feet, kilogram, pound, Celsius, Fahrenheit.',
        'category_label': 'Danh Mục Chuyển Đổi',
        'from_label': 'Từ',
        'to_label': 'Đến',
        'input_placeholder': 'Nhập số',
        'result_placeholder': 'Kết quả',
        'swap_title': 'Hoán đổi đơn vị',
        'quick_ref_title': 'Tham Khảo Nhanh',
        'ad_text': 'Không Gian Quảng Cáo',
        'categories': {
            'length': 'Độ dài',
            'weight': 'Trọng lượng',
            'temperature': 'Nhiệt độ',
            'volume': 'Thể tích',
            'area': 'Diện tích',
            'speed': 'Tốc độ'
        }
    },
    'th': {
        'title': 'ตัวแปลงหน่วย',
        'desc': 'แปลงความยาว น้ำหนัก อุณหภูมิ ปริมาตร และอื่นๆ รองรับหน่วยหลักทั้งหมด รวมถึงเมตร ฟุต กิโลกรัม ปอนด์ เซลเซียส ฟาเรนไฮต์',
        'category_label': 'หมวดหมู่การแปลง',
        'from_label': 'จาก',
        'to_label': 'ไปยัง',
        'input_placeholder': 'ป้อนตัวเลข',
        'result_placeholder': 'ผลลัพธ์',
        'swap_title': 'สลับหน่วย',
        'quick_ref_title': 'ข้อมูลอ้างอิงด่วน',
        'ad_text': 'พื้นที่โฆษณา',
        'categories': {
            'length': 'ความยาว',
            'weight': 'น้ำหนัก',
            'temperature': 'อุณหภูมิ',
            'volume': 'ปริมาตร',
            'area': 'พื้นที่',
            'speed': 'ความเร็ว'
        }
    },
    'de': {
        'title': 'Einheitenumrechner',
        'desc': 'Konvertieren Sie Länge, Gewicht, Temperatur, Volumen und mehr. Unterstützt alle wichtigen Einheiten einschließlich Meter, Fuß, Kilogramm, Pfund, Celsius, Fahrenheit.',
        'category_label': 'Umrechnungskategorie',
        'from_label': 'Von',
        'to_label': 'Nach',
        'input_placeholder': 'Zahl eingeben',
        'result_placeholder': 'Ergebnis',
        'swap_title': 'Einheiten tauschen',
        'quick_ref_title': 'Schnellreferenz',
        'ad_text': 'Werbefläche',
        'categories': {
            'length': 'Länge',
            'weight': 'Gewicht',
            'temperature': 'Temperatur',
            'volume': 'Volumen',
            'area': 'Fläche',
            'speed': 'Geschwindigkeit'
        }
    },
    'pt': {
        'title': 'Conversor de Unidades',
        'desc': 'Converta comprimento, peso, temperatura, volume e mais. Suporta todas as unidades principais incluindo metros, pés, quilogramas, libras, Celsius, Fahrenheit.',
        'category_label': 'Categoria de Conversão',
        'from_label': 'De',
        'to_label': 'Para',
        'input_placeholder': 'Digite o número',
        'result_placeholder': 'Resultado',
        'swap_title': 'Trocar unidades',
        'quick_ref_title': 'Referência Rápida',
        'ad_text': 'Espaço Publicitário',
        'categories': {
            'length': 'Comprimento',
            'weight': 'Peso',
            'temperature': 'Temperatura',
            'volume': 'Volume',
            'area': 'Área',
            'speed': 'Velocidade'
        }
    }
}

def read_korean_template():
    """Read the Korean unit converter as template"""
    ko_file = BASE_DIR / 'ko' / 'unit-converter' / 'index.html'
    with open(ko_file, 'r', encoding='utf-8') as f:
        return f.read()

def generate_unit_converter(lang, template):
    """Generate unit converter for a specific language"""
    t = TRANSLATIONS[lang]
    
    # Replace Korean text with target language
    content = template
    
    # Replace lang attribute
    content = content.replace('lang="ko"', f'lang="{lang}"')
    
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
    content = content.replace('/ko/unit-converter/', f'/{lang}/unit-converter/')
    content = content.replace('href="/ko/"', f'href="/{lang}/"')
    content = content.replace('"inLanguage": "ko"', f'"inLanguage": "{lang}"')
    content = content.replace('"name": "단위 변환기"', f'"name": "{t["title"]}"')
    content = re.sub(
        r'"description": ".*?"',
        f'"description": "{t["desc"]}"',
        content,
        count=1
    )
    
    # Replace UI text
    content = content.replace('<h1>📏 단위 변환기</h1>', f'<h1>📏 {t["title"]}</h1>')
    content = re.sub(
        r'<p>길이, 무게, 온도.*?</p>',
        f'<p>{t["desc"]}</p>',
        content,
        count=1
    )
    
    # Replace form labels
    content = content.replace('변환 카테고리', t['category_label'])
    content = content.replace('변환할 값', t['from_label'])
    content = content.replace('변환된 값', t['to_label'])
    content = content.replace('숫자 입력', t['input_placeholder'])
    content = content.replace('결과', t['result_placeholder'])
    content = content.replace('단위 교환', t['swap_title'])
    content = content.replace('자주 사용하는 변환', t['quick_ref_title'])
    content = content.replace('광고 영역', t['ad_text'])
    
    # Replace category options
    content = content.replace('>길이<', f'>{t["categories"]["length"]}<')
    content = content.replace('>무게<', f'>{t["categories"]["weight"]}<')
    content = content.replace('>온도<', f'>{t["categories"]["temperature"]}<')
    content = content.replace('>부피<', f'>{t["categories"]["volume"]}<')
    content = content.replace('>면적<', f'>{t["categories"]["area"]}<')
    content = content.replace('>속도<', f'>{t["categories"]["speed"]}<')
    
    # Replace JavaScript category names
    js_categories = f'''      length: {{
        name: '{t["categories"]["length"]}','''
    content = re.sub(
        r"length: \{\s*name: '.*?',",
        js_categories,
        content
    )
    
    return content

def main():
    print("🚀 Copying unit converter functionality to all languages...\n")
    
    # Read Korean template
    template = read_korean_template()
    print("✅ Read Korean template\n")
    
    # Generate for each language except Korean
    updated = 0
    for lang in TRANSLATIONS.keys():
        if lang == 'ko':
            continue
            
        output_file = BASE_DIR / lang / 'unit-converter' / 'index.html'
        content = generate_unit_converter(lang, template)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {lang}/unit-converter/index.html")
        updated += 1
    
    print(f"\n{'='*60}")
    print(f"✨ Complete! Updated {updated} language versions")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

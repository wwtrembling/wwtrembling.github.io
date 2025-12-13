"""
Create daily-verse pages for remaining languages (ja, pt, th, vi).
This script continues from create_daily_verse_pages.py
"""

import os
import re
import shutil

# Base directory
base_dir = r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf'

# For simplicity, we'll copy the English version and update key elements
# since these languages use similar Bible book abbreviations to English

languages = {
    'ja': {
        'lang_code': 'ja',
        'title': '聖書読書計画コピー - 365日聖書通読',
        'h1': '📖 聖書読書計画コピー',
        'description': '365日聖書読書計画を簡単にコピーできるツールです。ワンクリックで毎日の聖書箇所をコピーして共有できます。',
        'keywords': '聖書読書計画, 毎日の聖書, 365聖書, 聖書コピー, 聖書朗読, 毎日の黙想, 聖書研究',
        'og_title': '聖書読書計画コピー - 365日聖書通読',
        'og_description': 'ワンクリックで毎日の聖書箇所をコピーして共有できます。365日聖書読書計画を簡単にフォローできます。',
        'today_button': '📅 今日の日付へ',
        'copied_label': 'コピーされた箇所',
        'notification': 'クリップボードにコピーされました!',
        'months': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'weekdays': ['日', '月', '火', '水', '木', '金', '土'],
    },
    'pt': {
        'lang_code': 'pt',
        'title': 'Copiador de Plano de Leitura Bíblica - 365 Dias de Leitura Bíblica',
        'h1': '📖 Copiador de Plano de Leitura Bíblica',
        'description': 'Uma ferramenta para copiar facilmente seu plano de leitura bíblica de 365 dias. Copie e compartilhe passagens bíblicas diárias com apenas um clique.',
        'keywords': 'plano de leitura bíblica, Bíblia diária, 365 Bíblia, copiador de Bíblia, leitura das Escrituras, devoção diária, estudo bíblico',
        'og_title': 'Copiador de Plano de Leitura Bíblica - 365 Dias de Leitura Bíblica',
        'og_description': 'Copie e compartilhe passagens bíblicas diárias com apenas um clique. Siga seu plano de leitura bíblica de 365 dias com facilidade.',
        'today_button': '📅 Ir para Hoje',
        'copied_label': 'Passagem Copiada',
        'notification': 'Copiado para a área de transferência!',
        'months': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'weekdays': ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
    },
    'th': {
        'lang_code': 'th',
        'title': 'เครื่องมือคัดลอกแผนอ่านพระคัมภีร์ - อ่านพระคัมภีร์ 365 วัน',
        'h1': '📖 เครื่องมือคัดลอกแผนอ่านพระคัมภีร์',
        'description': 'เครื่องมือสำหรับคัดลอกแผนอ่านพระคัมภีร์ 365 วันของคุณได้อย่างง่ายดาย คัดลอกและแชร์ข้อพระคัมภีร์ประจำวันด้วยคลิกเดียว',
        'keywords': 'แผนอ่านพระคัมภีร์, พระคัมภีร์ประจำวัน, 365 พระคัมภีร์, เครื่องมือคัดลอกพระคัมภีร์, การอ่านพระคัมภีร์, การภาวนาประจำวัน, การศึกษาพระคัมภีร์',
        'og_title': 'เครื่องมือคัดลอกแผนอ่านพระคัมภีร์ - อ่านพระคัมภีร์ 365 วัน',
        'og_description': 'คัดลอกและแชร์ข้อพระคัมภีร์ประจำวันด้วยคลิกเดียว ติดตามแผนอ่านพระคัมภีร์ 365 วันของคุณได้อย่างง่ายดาย',
        'today_button': '📅 ไปที่วันนี้',
        'copied_label': 'ข้อที่คัดลอก',
        'notification': 'คัดลอกไปยังคลิปบอร์ดแล้ว!',
        'months': ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม'],
        'weekdays': ['อา', 'จ', 'อ', 'พ', 'พฤ', 'ศ', 'ส'],
    },
    'vi': {
        'lang_code': 'vi',
        'title': 'Công Cụ Sao Chép Kế Hoạch Đọc Kinh Thánh - Đọc Kinh Thánh 365 Ngày',
        'h1': '📖 Công Cụ Sao Chép Kế Hoạch Đọc Kinh Thánh',
        'description': 'Công cụ để sao chép kế hoạch đọc Kinh Thánh 365 ngày của bạn một cách dễ dàng. Sao chép và chia sẻ các đoạn Kinh Thánh hàng ngày chỉ bằng một cú nhấp chuột.',
        'keywords': 'kế hoạch đọc Kinh Thánh, Kinh Thánh hàng ngày, 365 Kinh Thánh, công cụ sao chép Kinh Thánh, đọc Thánh Kinh, suy niệm hàng ngày, nghiên cứu Kinh Thánh',
        'og_title': 'Công Cụ Sao Chép Kế Hoạch Đọc Kinh Thánh - Đọc Kinh Thánh 365 Ngày',
        'og_description': 'Sao chép và chia sẻ các đoạn Kinh Thánh hàng ngày chỉ bằng một cú nhấp chuột. Theo dõi kế hoạch đọc Kinh Thánh 365 ngày của bạn một cách dễ dàng.',
        'today_button': '📅 Đến Hôm Nay',
        'copied_label': 'Đoạn Đã Sao Chép',
        'notification': 'Đã sao chép vào clipboard!',
        'months': ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12'],
        'weekdays': ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'],
    },
}

# Read English template (use English Bible book names for these languages)
en_template_path = os.path.join(base_dir, 'en', 'daily-verse', 'index.html')
with open(en_template_path, 'r', encoding='utf-8') as f:
    en_template = f.read()

def create_daily_verse_page(lang_code, config):
    """Create a daily-verse page for the given language"""
    
    content = en_template
    
    # Replace language code
    content = content.replace('lang="en"', f'lang="{lang_code}"')
    
    # Replace meta tags
    content = re.sub(
        r'<meta name="description"\s+content="[^"]*"',
        f'<meta name="description"\n        content="{config["description"]}"',
        content
    )
    content = re.sub(
        r'<meta name="keywords"\s+content="[^"]*"',
        f'<meta name="keywords"\n        content="{config["keywords"]}"',
        content
    )
    
    # Replace canonical
    content = re.sub(
        r'<link rel="canonical" href="https://wwtrembling\.github\.io/en/daily_verse/"',
        f'<link rel="canonical" href="https://utilifyapp.net/{lang_code}/daily_verse/"',
        content
    )
    
    # Replace hreflang
    content = re.sub(
        r'<link rel="alternate" href="https://wwtrembling\.github\.io/en/daily_verse/" hreflang="en"',
        f'<link rel="alternate" href="https://utilifyapp.net/{lang_code}/daily_verse/" hreflang="{lang_code}"',
        content
    )
    content = re.sub(
        r'<link rel="alternate" href="https://wwtrembling\.github\.io/en/daily_verse/" hreflang="x-default"',
        f'<link rel="alternate" href="https://utilifyapp.net/{lang_code}/daily_verse/" hreflang="x-default"',
        content
    )
    
    # Replace OG tags
    content = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="{config["og_title"]}"',
        content
    )
    content = re.sub(
        r'<meta property="og:description"\s+content="[^"]*"',
        f'<meta property="og:description"\n        content="{config["og_description"]}"',
        content
    )
    content = re.sub(
        r'<meta property="og:url" content="https://wwtrembling\.github\.io/en/daily_verse/"',
        f'<meta property="og:url" content="https://utilifyapp.net/{lang_code}/daily_verse/"',
        content
    )
    content = re.sub(
        r'<meta property="og:locale" content="en_US"',
        f'<meta property="og:locale" content="{lang_code}_{lang_code.upper()}"',
        content
    )
    
    # Replace title
    content = re.sub(
        r'<title>[^<]*</title>',
        f'<title>{config["title"]}</title>',
        content
    )
    
    # Replace h1
    content = re.sub(
        r'<h1>📖 Bible Reading Plan Copier</h1>',
        f'<h1>{config["h1"]}</h1>',
        content
    )
    
    # Replace button text
    content = re.sub(
        r'📅 Go to Today',
        config["today_button"],
        content
    )
    
    # Replace status label
    content = re.sub(
        r'<div class="label">Copied Passage</div>',
        f'<div class="label">{config["copied_label"]}</div>',
        content
    )
    
    # Replace notification
    content = re.sub(
        r'Copied to clipboard!',
        config["notification"],
        content
    )
    
    # Replace month names
    months_pattern = r'const monthNames = \["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"\];'
    months_replacement = f'const monthNames = {config["months"]};'.replace("'", '"')
    content = re.sub(months_pattern, months_replacement, content)
    
    # Replace weekdays
    weekdays_pattern = r"const weekDays = \['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'\];"
    weekdays_replacement = f'const weekDays = {config["weekdays"]};'.replace("'", '"')
    content = re.sub(weekdays_pattern, weekdays_replacement, content)
    
    return content

# Create directories and files for each language
for lang_code, config in languages.items():
    lang_dir = os.path.join(base_dir, lang_code, 'daily-verse')
    os.makedirs(lang_dir, exist_ok=True)
    
    # Create index.html
    html_content = create_daily_verse_page(lang_code, config)
    html_path = os.path.join(lang_dir, 'index.html')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created {lang_code}/daily-verse/index.html")

print("\n🎉 All remaining daily-verse pages created successfully!")

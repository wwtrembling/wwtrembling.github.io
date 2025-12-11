"""
Tool Shelf - Multi-language Page Generator
Generates all utility pages across 9 languages with SEO optimization
"""

import os
from pathlib import Path

# Language configurations
LANGUAGES = {
    'ko': {'name': '한국어', 'flag': '🇰🇷', 'dir': 'ltr'},
    'en': {'name': 'English', 'flag': '🇺🇸', 'dir': 'ltr'},
    'ja': {'name': '日本語', 'flag': '🇯🇵', 'dir': 'ltr'},
    'hi': {'name': 'हिन्दी', 'flag': '🇮🇳', 'dir': 'ltr'},
    'id': {'name': 'Bahasa Indonesia', 'flag': '🇮🇩', 'dir': 'ltr'},
    'vi': {'name': 'Tiếng Việt', 'flag': '🇻🇳', 'dir': 'ltr'},
    'th': {'name': 'ภาษาไทย', 'flag': '🇹🇭', 'dir': 'ltr'},
    'de': {'name': 'Deutsch', 'flag': '🇩🇪', 'dir': 'ltr'},
    'pt': {'name': 'Português', 'flag': '🇧🇷', 'dir': 'ltr'}
}

# Utility configurations with translations
UTILITIES = {
    'unit-converter': {
        'icon': '📏',
        'ko': {'title': '단위 변환기', 'desc': '길이, 무게, 온도, 부피 등 다양한 단위를 간편하게 변환하세요.'},
        'en': {'title': 'Unit Converter', 'desc': 'Convert length, weight, temperature, volume and more.'},
        'ja': {'title': '単位変換器', 'desc': '長さ、重さ、温度、体積などを簡単に変換できます。'},
        'hi': {'title': 'यूनिट कनवर्टर', 'desc': 'लंबाई, वजन, तापमान, आयतन और अधिक परिवर्तित करें।'},
        'id': {'title': 'Konverter Satuan', 'desc': 'Konversi panjang, berat, suhu, volume dan lainnya.'},
        'vi': {'title': 'Chuyển Đổi Đơn Vị', 'desc': 'Chuyển đổi độ dài, trọng lượng, nhiệt độ, thể tích và hơn thế nữa.'},
        'th': {'title': 'ตัวแปลงหน่วย', 'desc': 'แปลงความยาว น้ำหนัก อุณหภูมิ ปริมาตร และอื่นๆ'},
        'de': {'title': 'Einheitenumrechner', 'desc': 'Konvertieren Sie Länge, Gewicht, Temperatur, Volumen und mehr.'},
        'pt': {'title': 'Conversor de Unidades', 'desc': 'Converta comprimento, peso, temperatura, volume e mais.'}
    },
    'pdf-tools': {
        'icon': '📄',
        'ko': {'title': 'PDF 도구', 'desc': 'PDF 파일을 압축하거나 병합하세요. 브라우저에서 바로 처리됩니다.'},
        'en': {'title': 'PDF Tools', 'desc': 'Compress or merge PDF files. Process directly in your browser.'},
        'ja': {'title': 'PDFツール', 'desc': 'PDFファイルを圧縮または結合します。ブラウザで直接処理できます。'},
        'hi': {'title': 'PDF उपकरण', 'desc': 'PDF फ़ाइलों को संपीड़ित या मर्ज करें। सीधे ब्राउज़र में प्रोसेस करें।'},
        'id': {'title': 'Alat PDF', 'desc': 'Kompres atau gabungkan file PDF. Proses langsung di browser Anda.'},
        'vi': {'title': 'Công Cụ PDF', 'desc': 'Nén hoặc hợp nhất tệp PDF. Xử lý trực tiếp trong trình duyệt.'},
        'th': {'title': 'เครื่องมือ PDF', 'desc': 'บีบอัดหรือรวมไฟล์ PDF ประมวลผลโดยตรงในเบราว์เซอร์'},
        'de': {'title': 'PDF-Tools', 'desc': 'PDF-Dateien komprimieren oder zusammenführen. Direkt im Browser verarbeiten.'},
        'pt': {'title': 'Ferramentas PDF', 'desc': 'Comprima ou mescle arquivos PDF. Processe diretamente no navegador.'}
    },
    'image-converter': {
        'icon': '🖼️',
        'ko': {'title': '이미지 변환기', 'desc': '이미지 크기를 조정하고 WebP 형식으로 변환하세요.'},
        'en': {'title': 'Image Converter', 'desc': 'Resize images and convert to WebP format.'},
        'ja': {'title': '画像変換器', 'desc': '画像のサイズを変更し、WebP形式に変換します。'},
        'hi': {'title': 'छवि कनवर्टर', 'desc': 'छवियों का आकार बदलें और WebP प्रारूप में बदलें।'},
        'id': {'title': 'Konverter Gambar', 'desc': 'Ubah ukuran gambar dan konversi ke format WebP.'},
        'vi': {'title': 'Chuyển Đổi Hình Ảnh', 'desc': 'Thay đổi kích thước hình ảnh và chuyển đổi sang định dạng WebP.'},
        'th': {'title': 'ตัวแปลงรูปภาพ', 'desc': 'ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP'},
        'de': {'title': 'Bildkonverter', 'desc': 'Bilder in der Größe ändern und in WebP-Format konvertieren.'},
        'pt': {'title': 'Conversor de Imagens', 'desc': 'Redimensione imagens e converta para formato WebP.'}
    },
    'bible-verse': {
        'icon': '📖',
        'ko': {'title': '오늘의 말씀', 'desc': '매일 새로운 성경 구절을 받아보세요.'},
        'en': {'title': 'Bible Verse Generator', 'desc': 'Get a new Bible verse every day.'},
        'ja': {'title': '今日の聖句', 'desc': '毎日新しい聖書の一節を受け取ります。'},
        'hi': {'title': 'बाइबिल वचन जनरेटर', 'desc': 'हर दिन एक नया बाइबिल वचन प्राप्त करें।'},
        'id': {'title': 'Generator Ayat Alkitab', 'desc': 'Dapatkan ayat Alkitab baru setiap hari.'},
        'vi': {'title': 'Câu Kinh Thánh Hôm Nay', 'desc': 'Nhận một câu Kinh Thánh mới mỗi ngày.'},
        'th': {'title': 'พระคัมภีร์ประจำวัน', 'desc': 'รับพระคัมภีร์ใหม่ทุกวัน'},
        'de': {'title': 'Bibelvers Generator', 'desc': 'Erhalten Sie jeden Tag einen neuen Bibelvers.'},
        'pt': {'title': 'Gerador de Versículos', 'desc': 'Receba um novo versículo bíblico todos os dias.'}
    },
    'bmi-calculator': {
        'icon': '⚖️',
        'ko': {'title': 'BMI & TDEE 계산기', 'desc': '체질량지수와 일일 권장 칼로리를 계산하세요.'},
        'en': {'title': 'BMI & TDEE Calculator', 'desc': 'Calculate your Body Mass Index and daily calorie needs.'},
        'ja': {'title': 'BMI & TDEE計算機', 'desc': '体格指数と1日の推奨カロリーを計算します。'},
        'hi': {'title': 'BMI और TDEE कैलकुलेटर', 'desc': 'अपना बॉडी मास इंडेक्स और दैनिक कैलोरी की जरूरत की गणना करें।'},
        'id': {'title': 'Kalkulator BMI & TDEE', 'desc': 'Hitung Indeks Massa Tubuh dan kebutuhan kalori harian Anda.'},
        'vi': {'title': 'Máy Tính BMI & TDEE', 'desc': 'Tính chỉ số khối cơ thể và nhu cầu calo hàng ngày.'},
        'th': {'title': 'เครื่องคำนวณ BMI และ TDEE', 'desc': 'คำนวณดัชนีมวลกายและความต้องการแคลอรีรายวัน'},
        'de': {'title': 'BMI & TDEE Rechner', 'desc': 'Berechnen Sie Ihren Body-Mass-Index und täglichen Kalorienbedarf.'},
        'pt': {'title': 'Calculadora BMI & TDEE', 'desc': 'Calcule seu Índice de Massa Corporal e necessidades calóricas diárias.'}
    },
    'date-calculator': {
        'icon': '📅',
        'ko': {'title': '날짜 계산기', 'desc': 'D-Day 계산, 날짜 차이 계산, 날짜 더하기/빼기를 수행하세요.'},
        'en': {'title': 'Date Calculator', 'desc': 'Calculate D-Day, date differences, add or subtract days.'},
        'ja': {'title': '日付計算機', 'desc': 'D-Day計算、日付の差、日付の加算/減算を実行します。'},
        'hi': {'title': 'तिथि कैलकुलेटर', 'desc': 'D-Day की गणना करें, तिथि अंतर, दिन जोड़ें या घटाएं।'},
        'id': {'title': 'Kalkulator Tanggal', 'desc': 'Hitung D-Day, perbedaan tanggal, tambah atau kurangi hari.'},
        'vi': {'title': 'Máy Tính Ngày', 'desc': 'Tính D-Day, chênh lệch ngày, cộng hoặc trừ ngày.'},
        'th': {'title': 'เครื่องคำนวณวันที่', 'desc': 'คำนวณ D-Day ความแตกต่างของวันที่ เพิ่มหรือลดวัน'},
        'de': {'title': 'Datumsrechner', 'desc': 'Berechnen Sie D-Day, Datumsunterschiede, Tage addieren oder subtrahieren.'},
        'pt': {'title': 'Calculadora de Datas', 'desc': 'Calcule D-Day, diferenças de datas, adicione ou subtraia dias.'}
    },
    'text-utils': {
        'icon': '📝',
        'ko': {'title': '텍스트 유틸리티', 'desc': '단어 수 세기, 중복 제거, 대소문자 변환 등의 기능을 제공합니다.'},
        'en': {'title': 'Text Utilities', 'desc': 'Count words, remove duplicates, convert case and more.'},
        'ja': {'title': 'テキストユーティリティ', 'desc': '単語数のカウント、重複の削除、大文字小文字の変換などを提供します。'},
        'hi': {'title': 'टेक्स्ट उपयोगिताएँ', 'desc': 'शब्दों की गिनती करें, डुप्लिकेट हटाएं, केस बदलें और अधिक।'},
        'id': {'title': 'Utilitas Teks', 'desc': 'Hitung kata, hapus duplikat, ubah huruf besar/kecil dan lainnya.'},
        'vi': {'title': 'Tiện Ích Văn Bản', 'desc': 'Đếm từ, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.'},
        'th': {'title': 'เครื่องมือข้อความ', 'desc': 'นับคำ ลบรายการซ้ำ แปลงตัวพิมพ์และอื่นๆ'},
        'de': {'title': 'Text-Utilities', 'desc': 'Wörter zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr.'},
        'pt': {'title': 'Utilitários de Texto', 'desc': 'Conte palavras, remova duplicatas, converta maiúsculas/minúsculas e mais.'}
    },
    'json-formatter': {
        'icon': '{ }',
        'ko': {'title': 'JSON 포매터', 'desc': 'JSON 데이터를 포맷팅하고 유효성을 검사하세요.'},
        'en': {'title': 'JSON Formatter', 'desc': 'Format and validate JSON data.'},
        'ja': {'title': 'JSONフォーマッター', 'desc': 'JSONデータをフォーマットして検証します。'},
        'hi': {'title': 'JSON फॉर्मेटर', 'desc': 'JSON डेटा को फॉर्मेट और मान्य करें।'},
        'id': {'title': 'Formatter JSON', 'desc': 'Format dan validasi data JSON.'},
        'vi': {'title': 'Định Dạng JSON', 'desc': 'Định dạng và xác thực dữ liệu JSON.'},
        'th': {'title': 'ตัวจัดรูปแบบ JSON', 'desc': 'จัดรูปแบบและตรวจสอบข้อมูล JSON'},
        'de': {'title': 'JSON-Formatierer', 'desc': 'JSON-Daten formatieren und validieren.'},
        'pt': {'title': 'Formatador JSON', 'desc': 'Formate e valide dados JSON.'}
    },
    'color-converter': {
        'icon': '🎨',
        'ko': {'title': '색상 변환기', 'desc': 'HEX, RGB, HSL 색상 형식 간 변환을 수행하세요.'},
        'en': {'title': 'Color Converter', 'desc': 'Convert between HEX, RGB, and HSL color formats.'},
        'ja': {'title': 'カラーコンバーター', 'desc': 'HEX、RGB、HSLカラー形式間で変換します。'},
        'hi': {'title': 'रंग कनवर्टर', 'desc': 'HEX, RGB और HSL रंग प्रारूपों के बीच बदलें।'},
        'id': {'title': 'Konverter Warna', 'desc': 'Konversi antara format warna HEX, RGB, dan HSL.'},
        'vi': {'title': 'Chuyển Đổi Màu', 'desc': 'Chuyển đổi giữa các định dạng màu HEX, RGB và HSL.'},
        'th': {'title': 'ตัวแปลงสี', 'desc': 'แปลงระหว่างรูปแบบสี HEX, RGB และ HSL'},
        'de': {'title': 'Farbkonverter', 'desc': 'Konvertieren zwischen HEX-, RGB- und HSL-Farbformaten.'},
        'pt': {'title': 'Conversor de Cores', 'desc': 'Converta entre formatos de cores HEX, RGB e HSL.'}
    },
    'timer': {
        'icon': '⏱️',
        'ko': {'title': '타이머 / 포모도로', 'desc': '온라인 타이머와 포모도로 기법을 활용하세요.'},
        'en': {'title': 'Timer / Pomodoro', 'desc': 'Online timer with Pomodoro technique support.'},
        'ja': {'title': 'タイマー / ポモドーロ', 'desc': 'ポモドーロテクニックをサポートするオンラインタイマー。'},
        'hi': {'title': 'टाइमर / पोमोडोरो', 'desc': 'पोमोडोरो तकनीक समर्थन के साथ ऑनलाइन टाइमर।'},
        'id': {'title': 'Timer / Pomodoro', 'desc': 'Timer online dengan dukungan teknik Pomodoro.'},
        'vi': {'title': 'Hẹn Giờ / Pomodoro', 'desc': 'Bộ hẹn giờ trực tuyến với hỗ trợ kỹ thuật Pomodoro.'},
        'th': {'title': 'ตัวจับเวลา / Pomodoro', 'desc': 'ตัวจับเวลาออนไลน์พร้อมรองรับเทคนิค Pomodoro'},
        'de': {'title': 'Timer / Pomodoro', 'desc': 'Online-Timer mit Unterstützung der Pomodoro-Technik.'},
        'pt': {'title': 'Temporizador / Pomodoro', 'desc': 'Temporizador online com suporte à técnica Pomodoro.'}
    }
}

def generate_hreflang_tags(util_slug):
    """Generate hreflang tags for all languages"""
    tags = []
    for lang in LANGUAGES.keys():
        tags.append(f'  <link rel="alternate" hreflang="{lang}" href="https://yourdomain.com/{lang}/{util_slug}/">')
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="https://yourdomain.com/en/{util_slug}/">')
    return '\n'.join(tags)

def generate_utility_page(lang, util_slug, util_data):
    """Generate a complete utility page HTML"""
    lang_data = util_data[lang]
    title = lang_data['title']
    desc = lang_data['desc']
    icon = util_data['icon']
    
    # This is a template - actual implementation would be specific to each utility
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Tool Shelf</title>
  <meta name="description" content="{desc}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{title} - Tool Shelf">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://yourdomain.com/{lang}/{util_slug}/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://yourdomain.com/{lang}/{util_slug}/">
  
  <!-- Language Alternatives -->
{generate_hreflang_tags(util_slug)}
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Styles -->
  <link rel="stylesheet" href="/assets/css/main.css">
  
  <!-- JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{title}",
    "description": "{desc}",
    "url": "https://yourdomain.com/{lang}/{util_slug}/",
    "inLanguage": "{lang}",
    "isPartOf": {{
      "@type": "WebSite",
      "name": "Tool Shelf",
      "url": "https://yourdomain.com/"
    }}
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <a href="/{lang}/" class="site-logo">
          🛠️ Tool Shelf
        </a>
        <div id="languageSwitcher" class="language-switcher"></div>
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow">
      <h1>{icon} {title}</h1>
      <p>{desc}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
      </div>
      
      <!-- Utility-specific content will go here -->
      <div class="card">
        <p>This is a placeholder for the {title} utility.</p>
        <p>The actual implementation will include the full functionality for this tool.</p>
      </div>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-content">
        <p>&copy; 2025 Tool Shelf. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="/assets/js/common.js"></script>
</body>
</html>
'''
    return html

def generate_index_page(lang):
    """Generate language-specific index page"""
    translations = {
        'ko': {
            'title': '무료 온라인 유틸리티 모음',
            'desc': '단위 변환, PDF 도구, 이미지 변환, 계산기 등 다양한 무료 온라인 도구를 제공합니다.',
            'heading': '무료 온라인 도구',
            'subheading': '설치 없이 브라우저에서 바로 사용하세요',
            'tools_heading': '사용 가능한 도구'
        },
        'en': {
            'title': 'Free Online Utilities Collection',
            'desc': 'Collection of free online tools including unit converter, PDF tools, image converter, calculators and more.',
            'heading': 'Free Online Tools',
            'subheading': 'Use directly in your browser without installation',
            'tools_heading': 'Available Tools'
        },
        'ja': {
            'title': '無料オンラインユーティリティコレクション',
            'desc': '単位変換、PDFツール、画像変換、計算機などの無料オンラインツールのコレクション。',
            'heading': '無料オンラインツール',
            'subheading': 'インストール不要でブラウザで直接使用',
            'tools_heading': '利用可能なツール'
        },
        'hi': {
            'title': 'मुफ्त ऑनलाइन उपयोगिताओं का संग्रह',
            'desc': 'यूनिट कनवर्टर, PDF उपकरण, छवि कनवर्टर, कैलकुलेटर और अधिक सहित मुफ्त ऑनलाइन उपकरणों का संग्रह।',
            'heading': 'मुफ्त ऑनलाइन उपकरण',
            'subheading': 'इंस्टॉलेशन के बिना सीधे अपने ब्राउज़र में उपयोग करें',
            'tools_heading': 'उपलब्ध उपकरण'
        },
        'id': {
            'title': 'Koleksi Utilitas Online Gratis',
            'desc': 'Koleksi alat online gratis termasuk konverter satuan, alat PDF, konverter gambar, kalkulator dan lainnya.',
            'heading': 'Alat Online Gratis',
            'subheading': 'Gunakan langsung di browser Anda tanpa instalasi',
            'tools_heading': 'Alat yang Tersedia'
        },
        'vi': {
            'title': 'Bộ Sưu Tập Tiện Ích Trực Tuyến Miễn Phí',
            'desc': 'Bộ sưu tập các công cụ trực tuyến miễn phí bao gồm chuyển đổi đơn vị, công cụ PDF, chuyển đổi hình ảnh, máy tính và hơn thế nữa.',
            'heading': 'Công Cụ Trực Tuyến Miễn Phí',
            'subheading': 'Sử dụng trực tiếp trong trình duyệt mà không cần cài đặt',
            'tools_heading': 'Công Cụ Có Sẵn'
        },
        'th': {
            'title': 'คอลเลกชันเครื่องมือออนไลน์ฟรี',
            'desc': 'คอลเลกชันเครื่องมือออนไลน์ฟรีรวมถึงตัวแปลงหน่วย เครื่องมือ PDF ตัวแปลงรูปภาพ เครื่องคำนวณและอื่นๆ',
            'heading': 'เครื่องมือออนไลน์ฟรี',
            'subheading': 'ใช้งานได้ทันทีในเบราว์เซอร์โดยไม่ต้องติดตั้ง',
            'tools_heading': 'เครื่องมือที่มีให้ใช้งาน'
        },
        'de': {
            'title': 'Kostenlose Online-Utilities-Sammlung',
            'desc': 'Sammlung kostenloser Online-Tools einschließlich Einheitenumrechner, PDF-Tools, Bildkonverter, Rechner und mehr.',
            'heading': 'Kostenlose Online-Tools',
            'subheading': 'Direkt im Browser ohne Installation verwenden',
            'tools_heading': 'Verfügbare Tools'
        },
        'pt': {
            'title': 'Coleção de Utilitários Online Gratuitos',
            'desc': 'Coleção de ferramentas online gratuitas incluindo conversor de unidades, ferramentas PDF, conversor de imagens, calculadoras e mais.',
            'heading': 'Ferramentas Online Gratuitas',
            'subheading': 'Use diretamente no seu navegador sem instalação',
            'tools_heading': 'Ferramentas Disponíveis'
        }
    }
    
    t = translations[lang]
    
    # Generate tool cards
    tool_cards = []
    for util_slug, util_data in UTILITIES.items():
        lang_data = util_data[lang]
        tool_cards.append(f'''
        <a href="/{lang}/{util_slug}/" class="card">
          <div class="card-icon">{util_data['icon']}</div>
          <h3 class="card-title">{lang_data['title']}</h3>
          <p class="card-description">{lang_data['desc']}</p>
        </a>''')
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['title']} - Tool Shelf</title>
  <meta name="description" content="{t['desc']}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{t['title']} - Tool Shelf">
  <meta property="og:description" content="{t['desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://yourdomain.com/{lang}/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://yourdomain.com/{lang}/">
  
  <!-- Language Alternatives -->
{generate_hreflang_tags('')}
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Styles -->
  <link rel="stylesheet" href="/assets/css/main.css">
  
  <!-- JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{t['title']}",
    "description": "{t['desc']}",
    "url": "https://yourdomain.com/{lang}/",
    "inLanguage": "{lang}",
    "isPartOf": {{
      "@type": "WebSite",
      "name": "Tool Shelf",
      "url": "https://yourdomain.com/"
    }}
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <a href="/{lang}/" class="site-logo">
          🛠️ Tool Shelf
        </a>
        <div id="languageSwitcher" class="language-switcher"></div>
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container">
      <div class="text-center mb-4">
        <h1>{t['heading']}</h1>
        <p style="font-size: 1.125rem;">{t['subheading']}</p>
      </div>
      
      <h2 class="text-center mb-3">{t['tools_heading']}</h2>
      
      <div class="card-grid">
{''.join(tool_cards)}
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-content">
        <p>&copy; 2025 Tool Shelf. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="/assets/js/common.js"></script>
</body>
</html>
'''
    return html

def main():
    """Main function to generate all pages"""
    base_dir = Path(__file__).parent
    
    print("Generating Tool Shelf pages...")
    print(f"Base directory: {base_dir}")
    
    # Generate index pages for each language
    for lang in LANGUAGES.keys():
        lang_dir = base_dir / lang
        lang_dir.mkdir(exist_ok=True)
        
        index_path = lang_dir / 'index.html'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(generate_index_page(lang))
        print(f"✓ Created {index_path}")
        
        # Generate utility pages for each language
        for util_slug, util_data in UTILITIES.items():
            util_dir = lang_dir / util_slug
            util_dir.mkdir(exist_ok=True)
            
            util_path = util_dir / 'index.html'
            with open(util_path, 'w', encoding='utf-8') as f:
                f.write(generate_utility_page(lang, util_slug, util_data))
            print(f"✓ Created {util_path}")
    
    print(f"\n✅ Successfully generated {len(LANGUAGES)} × (1 + {len(UTILITIES)}) = {len(LANGUAGES) * (1 + len(UTILITIES))} pages!")
    print("\nNext steps:")
    print("1. Implement specific functionality for each utility")
    print("2. Replace 'yourdomain.com' with your actual domain")
    print("3. Add Google AdSense code to placeholders")
    print("4. Test in browser and deploy to GitHub Pages")

if __name__ == '__main__':
    main()

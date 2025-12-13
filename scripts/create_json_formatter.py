"""
Create fully functional JSON Formatter for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

TRANSLATIONS = {
    'ko': {
        'title': 'JSON 포매터',
        'desc': 'JSON 데이터를 포맷팅하고 유효성을 검사하세요. 압축, 포맷, 검증 기능을 제공합니다.',
        'input_label': 'JSON 입력',
        'input_placeholder': 'JSON 데이터를 입력하세요...',
        'format_btn': '포맷',
        'minify_btn': '압축',
        'validate_btn': '검증',
        'copy_btn': '복사',
        'clear_btn': '지우기',
        'output_label': '결과',
        'valid_json': '✓ 유효한 JSON입니다',
        'invalid_json': '✗ 유효하지 않은 JSON입니다',
        'error_label': '오류:',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'JSON Formatter',
        'desc': 'Format and validate JSON data. Provides formatting, minification, and validation features.',
        'input_label': 'JSON Input',
        'input_placeholder': 'Enter JSON data...',
        'format_btn': 'Format',
        'minify_btn': 'Minify',
        'validate_btn': 'Validate',
        'copy_btn': 'Copy',
        'clear_btn': 'Clear',
        'output_label': 'Output',
        'valid_json': '✓ Valid JSON',
        'invalid_json': '✗ Invalid JSON',
        'error_label': 'Error:',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': 'JSONフォーマッター',
        'desc': 'JSONデータをフォーマットして検証します。フォーマット、圧縮、検証機能を提供します。',
        'input_label': 'JSON入力',
        'input_placeholder': 'JSONデータを入力してください...',
        'format_btn': 'フォーマット',
        'minify_btn': '圧縮',
        'validate_btn': '検証',
        'copy_btn': 'コピー',
        'clear_btn': 'クリア',
        'output_label': '出力',
        'valid_json': '✓ 有効なJSON',
        'invalid_json': '✗ 無効なJSON',
        'error_label': 'エラー:',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'JSON फॉर्मेटर',
        'desc': 'JSON डेटा को फॉर्मेट और मान्य करें। फॉर्मेटिंग, संक्षिप्तीकरण और सत्यापन सुविधाएं प्रदान करता है।',
        'input_label': 'JSON इनपुट',
        'input_placeholder': 'JSON डेटा दर्ज करें...',
        'format_btn': 'फॉर्मेट',
        'minify_btn': 'संक्षिप्त',
        'validate_btn': 'सत्यापित',
        'copy_btn': 'कॉपी',
        'clear_btn': 'साफ़',
        'output_label': 'आउटपुट',
        'valid_json': '✓ मान्य JSON',
        'invalid_json': '✗ अमान्य JSON',
        'error_label': 'त्रुटि:',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Formatter JSON',
        'desc': 'Format dan validasi data JSON. Menyediakan fitur format, minifikasi, dan validasi.',
        'input_label': 'Input JSON',
        'input_placeholder': 'Masukkan data JSON...',
        'format_btn': 'Format',
        'minify_btn': 'Minify',
        'validate_btn': 'Validasi',
        'copy_btn': 'Salin',
        'clear_btn': 'Hapus',
        'output_label': 'Output',
        'valid_json': '✓ JSON Valid',
        'invalid_json': '✗ JSON Tidak Valid',
        'error_label': 'Error:',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Định Dạng JSON',
        'desc': 'Định dạng và xác thực dữ liệu JSON. Cung cấp tính năng định dạng, nén và xác thực.',
        'input_label': 'Nhập JSON',
        'input_placeholder': 'Nhập dữ liệu JSON...',
        'format_btn': 'Định dạng',
        'minify_btn': 'Nén',
        'validate_btn': 'Xác thực',
        'copy_btn': 'Sao chép',
        'clear_btn': 'Xóa',
        'output_label': 'Kết quả',
        'valid_json': '✓ JSON hợp lệ',
        'invalid_json': '✗ JSON không hợp lệ',
        'error_label': 'Lỗi:',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'ตัวจัดรูปแบบ JSON',
        'desc': 'จัดรูปแบบและตรวจสอบข้อมูล JSON ให้บริการการจัดรูปแบบ การย่อขนาด และการตรวจสอบ',
        'input_label': 'ป้อน JSON',
        'input_placeholder': 'ป้อนข้อมูล JSON...',
        'format_btn': 'จัดรูปแบบ',
        'minify_btn': 'ย่อขนาด',
        'validate_btn': 'ตรวจสอบ',
        'copy_btn': 'คัดลอก',
        'clear_btn': 'ล้าง',
        'output_label': 'ผลลัพธ์',
        'valid_json': '✓ JSON ถูกต้อง',
        'invalid_json': '✗ JSON ไม่ถูกต้อง',
        'error_label': 'ข้อผิดพลาด:',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'JSON-Formatierer',
        'desc': 'JSON-Daten formatieren und validieren. Bietet Formatierung, Minifizierung und Validierung.',
        'input_label': 'JSON-Eingabe',
        'input_placeholder': 'JSON-Daten eingeben...',
        'format_btn': 'Formatieren',
        'minify_btn': 'Minifizieren',
        'validate_btn': 'Validieren',
        'copy_btn': 'Kopieren',
        'clear_btn': 'Löschen',
        'output_label': 'Ausgabe',
        'valid_json': '✓ Gültiges JSON',
        'invalid_json': '✗ Ungültiges JSON',
        'error_label': 'Fehler:',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Formatador JSON',
        'desc': 'Formate e valide dados JSON. Fornece recursos de formatação, minificação e validação.',
        'input_label': 'Entrada JSON',
        'input_placeholder': 'Digite dados JSON...',
        'format_btn': 'Formatar',
        'minify_btn': 'Minificar',
        'validate_btn': 'Validar',
        'copy_btn': 'Copiar',
        'clear_btn': 'Limpar',
        'output_label': 'Saída',
        'valid_json': '✓ JSON Válido',
        'invalid_json': '✗ JSON Inválido',
        'error_label': 'Erro:',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_json_formatter(lang):
    t = TRANSLATIONS[lang]
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["title"]} - Tool Shelf</title>
  <meta name="description" content="{t["desc"]}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{t["title"]} - Tool Shelf">
  <meta property="og:description" content="{t["desc"]}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utilifyapp.net/{lang}/json-formatter/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/json-formatter/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/json-formatter/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/json-formatter/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/json-formatter/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/json-formatter/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/json-formatter/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/json-formatter/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/json-formatter/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/json-formatter/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/json-formatter/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/json-formatter/">
  
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
    "@type": "WebApplication",
    "name": "{t["title"]}",
    "description": "{t["desc"]}",
    "url": "https://utilifyapp.net/{lang}/json-formatter/",
    "inLanguage": "{lang}",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Any",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }}
  }}
  </script>
  
  <style>
    .editor-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-lg);
      margin-top: var(--spacing-lg);
    }}
    
    .editor-panel {{
      display: flex;
      flex-direction: column;
      gap: var(--spacing-md);
    }}
    
    .json-textarea {{
      font-family: var(--font-mono);
      min-height: 400px;
      resize: vertical;
    }}
    
    .validation-status {{
      padding: var(--spacing-md);
      border-radius: var(--radius-md);
      font-weight: 500;
      text-align: center;
    }}
    
    .validation-status.valid {{
      background: #d1fae5;
      color: #065f46;
      border: 1px solid #10b981;
    }}
    
    .validation-status.invalid {{
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #ef4444;
    }}
    
    .error-message {{
      background: var(--bg-tertiary);
      padding: var(--spacing-md);
      border-radius: var(--radius-md);
      font-family: var(--font-mono);
      font-size: 0.875rem;
      color: var(--text-secondary);
      white-space: pre-wrap;
      word-break: break-word;
    }}
    
    @media (max-width: 768px) {{
      .editor-container {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631"
     crossorigin="anonymous"></script>

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
      <h1>{{{{ }}}} {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <!-- Action Buttons -->
      <div class="btn-group">
        <button class="btn btn-primary" onclick="formatJSON()">{t["format_btn"]}</button>
        <button class="btn btn-secondary" onclick="minifyJSON()">{t["minify_btn"]}</button>
        <button class="btn btn-secondary" onclick="validateJSON()">{t["validate_btn"]}</button>
        <button class="btn btn-secondary" onclick="copyOutput()">{t["copy_btn"]}</button>
        <button class="btn btn-secondary" onclick="clearAll()">{t["clear_btn"]}</button>
      </div>
      
      <!-- Editors -->
      <div class="editor-container">
        <div class="editor-panel">
          <label class="form-label">{t["input_label"]}</label>
          <textarea id="jsonInput" class="form-textarea json-textarea" placeholder="{t["input_placeholder"]}"></textarea>
        </div>
        
        <div class="editor-panel">
          <label class="form-label">{t["output_label"]}</label>
          <textarea id="jsonOutput" class="form-textarea json-textarea" readonly></textarea>
        </div>
      </div>
      
      <!-- Validation Status -->
      <div id="validationStatus" style="display: none;"></div>
      <div id="errorMessage" style="display: none;"></div>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
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
  <script>
    const input = document.getElementById('jsonInput');
    const output = document.getElementById('jsonOutput');
    const validationStatus = document.getElementById('validationStatus');
    const errorMessage = document.getElementById('errorMessage');
    
    function formatJSON() {{
      try {{
        const json = JSON.parse(input.value);
        output.value = JSON.stringify(json, null, 2);
        showValidation(true);
      }} catch (e) {{
        showValidation(false, e.message);
      }}
    }}
    
    function minifyJSON() {{
      try {{
        const json = JSON.parse(input.value);
        output.value = JSON.stringify(json);
        showValidation(true);
      }} catch (e) {{
        showValidation(false, e.message);
      }}
    }}
    
    function validateJSON() {{
      try {{
        JSON.parse(input.value);
        showValidation(true);
        output.value = '';
      }} catch (e) {{
        showValidation(false, e.message);
        output.value = '';
      }}
    }}
    
    function copyOutput() {{
      if (output.value) {{
        Utils.copyToClipboard(output.value);
      }} else {{
        Utils.showToast('{t["invalid_json"]}');
      }}
    }}
    
    function clearAll() {{
      input.value = '';
      output.value = '';
      validationStatus.style.display = 'none';
      errorMessage.style.display = 'none';
    }}
    
    function showValidation(isValid, error = '') {{
      validationStatus.style.display = 'block';
      validationStatus.className = 'validation-status ' + (isValid ? 'valid' : 'invalid');
      validationStatus.textContent = isValid ? '{t["valid_json"]}' : '{t["invalid_json"]}';
      
      if (error) {{
        errorMessage.style.display = 'block';
        errorMessage.className = 'error-message';
        errorMessage.textContent = '{t["error_label"]} ' + error;
      }} else {{
        errorMessage.style.display = 'none';
      }}
    }}
    
    // Auto-validate on input
    input.addEventListener('input', Utils.debounce(() => {{
      if (input.value.trim()) {{
        try {{
          JSON.parse(input.value);
          showValidation(true);
        }} catch (e) {{
          // Don't show error while typing
        }}
      }} else {{
        validationStatus.style.display = 'none';
        errorMessage.style.display = 'none';
      }}
    }}, 500));
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating JSON Formatter for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'json-formatter'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_json_formatter(lang))
        
        print(f"✅ Created: {lang}/json-formatter/index.html")
    
    print(f"\n{'='*60}")
    print(f"✨ Complete! Created JSON Formatter for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

"""
Create fully functional Password Generator for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '안전한 비밀번호 생성기',
        'desc': '강력하고 안전한 비밀번호를 생성하세요. 생성된 비밀번호는 서버로 전송되지 않습니다 (100% 클라이언트 처리).',
        'length_label': '비밀번호 길이',
        'options_label': '옵션',
        'opt_uppercase': '대문자 포함 (A-Z)',
        'opt_lowercase': '소문자 포함 (a-z)',
        'opt_numbers': '숫자 포함 (0-9)',
        'opt_symbols': '특수문자 포함 (@#$%)',
        'generate_btn': '비밀번호 생성',
        'copy_btn': '복사',
        'result_label': '생성된 비밀번호',
        'strength_label': '보안 강도',
        'security_note': '🔒 모든 비밀번호는 브라우저에서 생성되며 외부로 전송되지 않습니다.',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Strong Password Generator',
        'desc': 'Generate strong and secure passwords. Passwords are generated locally and never sent to a server.',
        'length_label': 'Password Length',
        'options_label': 'Options',
        'opt_uppercase': 'Uppercase (A-Z)',
        'opt_lowercase': 'Lowercase (a-z)',
        'opt_numbers': 'Numbers (0-9)',
        'opt_symbols': 'Symbols (@#$%)',
        'generate_btn': 'Generate Password',
        'copy_btn': 'Copy',
        'result_label': 'Generated Password',
        'strength_label': 'Strength',
        'security_note': '🔒 All passwords are generated in your browser and verify sent remotely.',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': '強力なパスワード生成ツール',
        'desc': '強力で安全なパスワードを生成します。パスワードはローカルで生成され、サーバーに送信されることはありません。',
        'length_label': 'パスワードの長さ',
        'options_label': 'オプション',
        'opt_uppercase': '大文字 (A-Z)',
        'opt_lowercase': '小文字 (a-z)',
        'opt_numbers': '数字 (0-9)',
        'opt_symbols': '記号 (@#$%)',
        'generate_btn': 'パスワードを生成',
        'copy_btn': 'コピー',
        'result_label': '生成されたパスワード',
        'strength_label': '強度',
        'security_note': '🔒 すべてのパスワードはブラウザ内で生成され、外部に送信されることはありません。',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'मजबूत पासवर्ड जनरेटर',
        'desc': 'मजबूत और सुरक्षित पासवर्ड बनाएं। पासवर्ड स्थानीय रूप से बनाए जाते हैं और कभी भी सर्वर पर नहीं भेजे जाते हैं।',
        'length_label': 'पासवर्ड की लंबाई',
        'options_label': 'विकल्प',
        'opt_uppercase': 'बड़े अक्षर (A-Z)',
        'opt_lowercase': 'छोटे अक्षर (a-z)',
        'opt_numbers': 'संख्याएँ (0-9)',
        'opt_symbols': 'प्रतीक (@#$%)',
        'generate_btn': 'पासवर्ड जनरेट करें',
        'copy_btn': 'कॉपी',
        'result_label': 'जनरेट किया गया पासवर्ड',
        'strength_label': 'ताकत',
        'security_note': '🔒 सभी पासवर्ड आपके ब्राउज़र में जनरेट होते हैं और दूरस्थ रूप से नहीं भेजे जाते।',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Pembuat Kata Sandi Kuat',
        'desc': 'Buat kata sandi yang kuat dan aman. Kata sandi dibuat secara lokal dan tidak pernah dikirim ke server.',
        'length_label': 'Panjang Kata Sandi',
        'options_label': 'Opsi',
        'opt_uppercase': 'Huruf Besar (A-Z)',
        'opt_lowercase': 'Huruf Kecil (a-z)',
        'opt_numbers': 'Angka (0-9)',
        'opt_symbols': 'Simbol (@#$%)',
        'generate_btn': 'Buat Kata Sandi',
        'copy_btn': 'Salin',
        'result_label': 'Kata Sandi Dibuat',
        'strength_label': 'Kekuatan',
        'security_note': '🔒 Semua kata sandi dibuat di browser Anda dan tidak pernah dikirim keluar.',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Trình Tạo Mật Khẩu Mạnh',
        'desc': 'Tạo mật khẩu mạnh và an toàn. Mật khẩu được tạo cục bộ và không bao giờ được gửi đến máy chủ.',
        'length_label': 'Độ dài mật khẩu',
        'options_label': 'Tùy chọn',
        'opt_uppercase': 'Chữ hoa (A-Z)',
        'opt_lowercase': 'Chữ thường (a-z)',
        'opt_numbers': 'Số (0-9)',
        'opt_symbols': 'Ký hiệu (@#$%)',
        'generate_btn': 'Tạo Mật Khẩu',
        'copy_btn': 'Sao chép',
        'result_label': 'Mật khẩu đã tạo',
        'strength_label': 'Độ mạnh',
        'security_note': '🔒 Tất cả mật khẩu được tạo trong trình duyệt của bạn và không bao giờ được gửi đi xa.',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'เครื่องมือสร้างรหัสผ่านที่รัดกุม',
        'desc': 'สร้างรหัสผ่านที่รัดกุมและปลอดภัย รหัสผ่านจะถูกสร้างขึ้นในเครื่องและไม่ส่งไปยังเซิร์ฟเวอร์',
        'length_label': 'ความยาวรหัสผ่าน',
        'options_label': 'ตัวเลือก',
        'opt_uppercase': 'ตัวพิมพ์ใหญ่ (A-Z)',
        'opt_lowercase': 'ตัวพิมพ์เล็ก (a-z)',
        'opt_numbers': 'ตัวเลข (0-9)',
        'opt_symbols': 'สัญลักษณ์ (@#$%)',
        'generate_btn': 'สร้างรหัสผ่าน',
        'copy_btn': 'คัดลอก',
        'result_label': 'รหัสผ่านที่สร้าง',
        'strength_label': 'ความคาดเดายาก',
        'security_note': '🔒 รหัสผ่านทั้งหมดสร้างขึ้นในเบราว์เซอร์ของคุณและไม่ส่งออกไปภายนอก',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Sicherer Passwort-Generator',
        'desc': 'Generieren Sie starke und sichere Passwörter. Passwörter werden lokal generiert und niemals an einen Server gesendet.',
        'length_label': 'Passwortlänge',
        'options_label': 'Optionen',
        'opt_uppercase': 'Großbuchstaben (A-Z)',
        'opt_lowercase': 'Kleinbuchstaben (a-z)',
        'opt_numbers': 'Zahlen (0-9)',
        'opt_symbols': 'Symbole (@#$%)',
        'generate_btn': 'Passwort generieren',
        'copy_btn': 'Kopieren',
        'result_label': 'Generiertes Passwort',
        'strength_label': 'Stärke',
        'security_note': '🔒 Alle Passwörter werden in Ihrem Browser generiert.',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Gerador de Senha Forte',
        'desc': 'Gere senhas fortes e seguras. As senhas são geradas localmente e nunca enviadas a um servidor.',
        'length_label': 'Tamanho da Senha',
        'options_label': 'Opções',
        'opt_uppercase': 'Maiúsculas (A-Z)',
        'opt_lowercase': 'Minúsculas (a-z)',
        'opt_numbers': 'Números (0-9)',
        'opt_symbols': 'Símbolos (@#$%)',
        'generate_btn': 'Gerar Senha',
        'copy_btn': 'Copiar',
        'result_label': 'Senha Gerada',
        'strength_label': 'Força',
        'security_note': '🔒 Todas as senhas são geradas no seu navegador.',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_password_generator(lang):
    t = TRANSLATIONS[lang]
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6334819180242631">
  <title>{t["title"]} - Tool Shelf</title>
  <meta name="description" content="{t["desc"]}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{t["title"]} - Tool Shelf">
  <meta property="og:description" content="{t["desc"]}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utilifyapp.net/{lang}/password-generator/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/password-generator/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/password-generator/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/password-generator/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/password-generator/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/password-generator/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/password-generator/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/password-generator/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/password-generator/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/password-generator/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/password-generator/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/password-generator/">
  
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
    "url": "https://utilifyapp.net/{lang}/password-generator/",
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
    .generator-container {{
      max-width: 600px;
      margin: 0 auto;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-xl);
      margin-top: var(--spacing-lg);
    }}
    
    .password-display {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: var(--spacing-lg);
      margin-bottom: var(--spacing-lg);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: var(--spacing-md);
    }}
    
    .password-value {{
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--primary-color);
      word-break: break-all;
    }}
    
    .copy-icon-btn {{
      background: none;
      border: none;
      color: var(--text-secondary);
      cursor: pointer;
      padding: var(--spacing-sm);
      transition: color var(--transition-fast);
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    
    .copy-icon-btn:hover {{
      color: var(--primary-color);
    }}
    
    .controls-grid {{
      display: grid;
      gap: var(--spacing-lg);
    }}
    
    .range-container {{
      display: flex;
      align-items: center;
      gap: var(--spacing-md);
    }}
    
    .range-slider {{
      flex: 1;
      height: 6px;
      background: var(--border-color);
      border-radius: 3px;
      appearance: none;
      outline: none;
    }}
    
    .range-slider::-webkit-slider-thumb {{
      appearance: none;
      width: 20px;
      height: 20px;
      background: var(--primary-color);
      border-radius: 50%;
      cursor: pointer;
    }}
    
    .options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-md);
    }}
    
    .checkbox-label {{
      display: flex;
      align-items: center;
      gap: var(--spacing-sm);
      cursor: pointer;
      user-select: none;
    }}
    
    .security-badge {{
      margin-top: var(--spacing-lg);
      padding: var(--spacing-md);
      background: #ecfdf5;
      color: #065f46;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: var(--spacing-sm);
    }}
    
    .generator-btn {{
      width: 100%;
      padding: var(--spacing-lg);
      font-size: 1.2rem;
      margin-top: var(--spacing-lg);
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
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow">
      <h1>🔐 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <div class="generator-container">
        <!-- Display -->
        <label class="form-label">{t["result_label"]}</label>
        <div class="password-display">
          <div id="passwordOutput" class="password-value">Click Generate</div>
          <button class="copy-icon-btn" onclick="copyPassword()">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            {t["copy_btn"]}
          </button>
        </div>
        
        <!-- Controls -->
        <div class="controls-grid">
          <!-- Length -->
          <div>
            <div class="flex justify-between mb-2">
              <label class="form-label">{t["length_label"]}: <span id="lengthValue">16</span></label>
            </div>
            <div class="range-container">
              <input type="range" id="lengthSlider" min="4" max="64" value="16" class="range-slider" oninput="updateLength(this.value)">
            </div>
          </div>
          
          <!-- Options -->
          <div>
            <label class="form-label mb-2">{t["options_label"]}</label>
            <div class="options-grid">
              <label class="checkbox-label">
                <input type="checkbox" id="useUppercase" checked> {t["opt_uppercase"]}
              </label>
              <label class="checkbox-label">
                <input type="checkbox" id="useLowercase" checked> {t["opt_lowercase"]}
              </label>
              <label class="checkbox-label">
                <input type="checkbox" id="useNumbers" checked> {t["opt_numbers"]}
              </label>
              <label class="checkbox-label">
                <input type="checkbox" id="useSymbols" checked> {t["opt_symbols"]}
              </label>
            </div>
          </div>
          
          <button class="btn btn-primary generator-btn" onclick="generatePassword()">{t["generate_btn"]}</button>
        </div>
        
        <div class="security-badge">
          {t["security_note"]}
        </div>
      </div>
      
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
    const passwordOutput = document.getElementById('passwordOutput');
    const lengthSlider = document.getElementById('lengthSlider');
    const lengthValue = document.getElementById('lengthValue');
    
    // Character sets
    const chars = {{
      upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
      lower: 'abcdefghijklmnopqrstuvwxyz',
      numbers: '0123456789',
      symbols: '!@#$%^&*()_+-=[]{{}}|;:,.<>?'
    }};
    
    function updateLength(val) {{
      lengthValue.textContent = val;
      generatePassword();
    }}
    
    function generatePassword() {{
      const length = parseInt(lengthSlider.value);
      const useUpper = document.getElementById('useUppercase').checked;
      const useLower = document.getElementById('useLowercase').checked;
      const useNumbers = document.getElementById('useNumbers').checked;
      const useSymbols = document.getElementById('useSymbols').checked;
      
      let charPool = '';
      if (useUpper) charPool += chars.upper;
      if (useLower) charPool += chars.lower;
      if (useNumbers) charPool += chars.numbers;
      if (useSymbols) charPool += chars.symbols;
      
      if (charPool === '') {{
        passwordOutput.textContent = 'Select Option';
        return;
      }}
      
      let password = '';
      const poolLength = charPool.length;
      
      // Use crypto for better randomness
      const randomValues = new Uint32Array(length);
      window.crypto.getRandomValues(randomValues);
      
      for (let i = 0; i < length; i++) {{
        password += charPool[randomValues[i] % poolLength];
      }}
      
      passwordOutput.textContent = password;
    }}
    
    function copyPassword() {{
      const text = passwordOutput.textContent;
      if (text && text !== 'Select Option') {{
        Utils.copyToClipboard(text);
      }}
    }}
    
    // Generate on load
    generatePassword();
    
    // Add event listeners for checkboxes
    document.querySelectorAll('input[type="checkbox"]').forEach(box => {{
      box.addEventListener('change', generatePassword);
    }});
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Password Generator for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'password-generator'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_password_generator(lang))
        
        print(f"✅ Created: {lang}/password-generator/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Password Generator for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

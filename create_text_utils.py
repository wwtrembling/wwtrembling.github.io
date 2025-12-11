"""
Create Text Utilities for all 9 languages
Features: Word count, character count, remove duplicates, case conversion
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

TRANSLATIONS = {
    'ko': {
        'title': '텍스트 유틸리티',
        'desc': '단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.',
        'input_label': '텍스트 입력',
        'input_placeholder': '텍스트를 입력하세요...',
        'stats_title': '통계',
        'characters': '문자 수',
        'words': '단어 수',
        'lines': '줄 수',
        'actions_title': '작업',
        'uppercase': '대문자로',
        'lowercase': '소문자로',
        'remove_duplicates': '중복 줄 제거',
        'sort_lines': '줄 정렬',
        'reverse_text': '텍스트 뒤집기',
        'copy': '복사',
        'clear': '지우기'
    },
    'en': {
        'title': 'Text Utilities',
        'desc': 'Word count, character count, remove duplicates, case conversion and more text processing features.',
        'input_label': 'Text Input',
        'input_placeholder': 'Enter text...',
        'stats_title': 'Statistics',
        'characters': 'Characters',
        'words': 'Words',
        'lines': 'Lines',
        'actions_title': 'Actions',
        'uppercase': 'Uppercase',
        'lowercase': 'Lowercase',
        'remove_duplicates': 'Remove Duplicate Lines',
        'sort_lines': 'Sort Lines',
        'reverse_text': 'Reverse Text',
        'copy': 'Copy',
        'clear': 'Clear'
    },
    'ja': {
        'title': 'テキストユーティリティ',
        'desc': '単語数、文字数、重複削除、大文字小文字変換などのテキスト処理機能を提供します。',
        'input_label': 'テキスト入力',
        'input_placeholder': 'テキストを入力してください...',
        'stats_title': '統計',
        'characters': '文字数',
        'words': '単語数',
        'lines': '行数',
        'actions_title': 'アクション',
        'uppercase': '大文字',
        'lowercase': '小文字',
        'remove_duplicates': '重複行削除',
        'sort_lines': '行ソート',
        'reverse_text': 'テキスト反転',
        'copy': 'コピー',
        'clear': 'クリア'
    },
    'hi': {
        'title': 'टेक्स्ट उपयोगिताएँ',
        'desc': 'शब्द गणना, वर्ण गणना, डुप्लिकेट हटाएं, केस रूपांतरण और अधिक टेक्स्ट प्रोसेसिंग सुविधाएं।',
        'input_label': 'टेक्स्ट इनपुट',
        'input_placeholder': 'टेक्स्ट दर्ज करें...',
        'stats_title': 'सांख्यिकी',
        'characters': 'वर्ण',
        'words': 'शब्द',
        'lines': 'पंक्तियाँ',
        'actions_title': 'क्रियाएं',
        'uppercase': 'बड़े अक्षर',
        'lowercase': 'छोटे अक्षर',
        'remove_duplicates': 'डुप्लिकेट पंक्तियाँ हटाएं',
        'sort_lines': 'पंक्तियाँ सॉर्ट करें',
        'reverse_text': 'टेक्स्ट उल्टा करें',
        'copy': 'कॉपी',
        'clear': 'साफ़'
    },
    'id': {
        'title': 'Utilitas Teks',
        'desc': 'Hitung kata, hitung karakter, hapus duplikat, konversi huruf besar/kecil dan fitur pemrosesan teks lainnya.',
        'input_label': 'Input Teks',
        'input_placeholder': 'Masukkan teks...',
        'stats_title': 'Statistik',
        'characters': 'Karakter',
        'words': 'Kata',
        'lines': 'Baris',
        'actions_title': 'Aksi',
        'uppercase': 'Huruf Besar',
        'lowercase': 'Huruf Kecil',
        'remove_duplicates': 'Hapus Baris Duplikat',
        'sort_lines': 'Urutkan Baris',
        'reverse_text': 'Balik Teks',
        'copy': 'Salin',
        'clear': 'Hapus'
    },
    'vi': {
        'title': 'Tiện Ích Văn Bản',
        'desc': 'Đếm từ, đếm ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và nhiều tính năng xử lý văn bản khác.',
        'input_label': 'Nhập Văn Bản',
        'input_placeholder': 'Nhập văn bản...',
        'stats_title': 'Thống Kê',
        'characters': 'Ký tự',
        'words': 'Từ',
        'lines': 'Dòng',
        'actions_title': 'Hành Động',
        'uppercase': 'Chữ Hoa',
        'lowercase': 'Chữ Thường',
        'remove_duplicates': 'Xóa Dòng Trùng Lặp',
        'sort_lines': 'Sắp Xếp Dòng',
        'reverse_text': 'Đảo Ngược Văn Bản',
        'copy': 'Sao chép',
        'clear': 'Xóa'
    },
    'th': {
        'title': 'เครื่องมือข้อความ',
        'desc': 'นับคำ นับตัวอักษร ลบรายการซ้ำ แปลงตัวพิมพ์ และคุณสมบัติการประมวลผลข้อความอื่นๆ',
        'input_label': 'ป้อนข้อความ',
        'input_placeholder': 'ป้อนข้อความ...',
        'stats_title': 'สถิติ',
        'characters': 'ตัวอักษร',
        'words': 'คำ',
        'lines': 'บรรทัด',
        'actions_title': 'การดำเนินการ',
        'uppercase': 'ตัวพิมพ์ใหญ่',
        'lowercase': 'ตัวพิมพ์เล็ก',
        'remove_duplicates': 'ลบบรรทัดซ้ำ',
        'sort_lines': 'เรียงบรรทัด',
        'reverse_text': 'กลับข้อความ',
        'copy': 'คัดลอก',
        'clear': 'ล้าง'
    },
    'de': {
        'title': 'Text-Utilities',
        'desc': 'Wörter zählen, Zeichen zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr Textverarbeitungsfunktionen.',
        'input_label': 'Texteingabe',
        'input_placeholder': 'Text eingeben...',
        'stats_title': 'Statistiken',
        'characters': 'Zeichen',
        'words': 'Wörter',
        'lines': 'Zeilen',
        'actions_title': 'Aktionen',
        'uppercase': 'Großbuchstaben',
        'lowercase': 'Kleinbuchstaben',
        'remove_duplicates': 'Doppelte Zeilen entfernen',
        'sort_lines': 'Zeilen sortieren',
        'reverse_text': 'Text umkehren',
        'copy': 'Kopieren',
        'clear': 'Löschen'
    },
    'pt': {
        'title': 'Utilitários de Texto',
        'desc': 'Conte palavras, conte caracteres, remova duplicatas, converta maiúsculas/minúsculas e mais recursos de processamento de texto.',
        'input_label': 'Entrada de Texto',
        'input_placeholder': 'Digite o texto...',
        'stats_title': 'Estatísticas',
        'characters': 'Caracteres',
        'words': 'Palavras',
        'lines': 'Linhas',
        'actions_title': 'Ações',
        'uppercase': 'Maiúsculas',
        'lowercase': 'Minúsculas',
        'remove_duplicates': 'Remover Linhas Duplicadas',
        'sort_lines': 'Ordenar Linhas',
        'reverse_text': 'Inverter Texto',
        'copy': 'Copiar',
        'clear': 'Limpar'
    }
}

def generate_text_utils(lang):
    t = TRANSLATIONS[lang]
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["title"]} - Tool Shelf</title>
  <meta name="description" content="{t["desc"]}">
  
  <link rel="canonical" href="https://wwtrembling.github.io/{lang}/text-utils/">
  <link rel="alternate" hreflang="ko" href="https://wwtrembling.github.io/ko/text-utils/">
  <link rel="alternate" hreflang="en" href="https://wwtrembling.github.io/en/text-utils/">
  <link rel="alternate" hreflang="ja" href="https://wwtrembling.github.io/ja/text-utils/">
  <link rel="alternate" hreflang="hi" href="https://wwtrembling.github.io/hi/text-utils/">
  <link rel="alternate" hreflang="id" href="https://wwtrembling.github.io/id/text-utils/">
  <link rel="alternate" hreflang="vi" href="https://wwtrembling.github.io/vi/text-utils/">
  <link rel="alternate" hreflang="th" href="https://wwtrembling.github.io/th/text-utils/">
  <link rel="alternate" hreflang="de" href="https://wwtrembling.github.io/de/text-utils/">
  <link rel="alternate" hreflang="pt" href="https://wwtrembling.github.io/pt/text-utils/">
  <link rel="alternate" hreflang="x-default" href="https://wwtrembling.github.io/en/text-utils/">
  
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.css">
  
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631" crossorigin="anonymous"></script>
</head>
<body>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <a href="/{lang}/" class="site-logo">🛠️ Tool Shelf</a>
        <div id="languageSwitcher" class="language-switcher"></div>
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow">
      <h1>📝 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <div class="card">
        <label class="form-label">{t["input_label"]}</label>
        <textarea id="textInput" class="form-textarea" style="min-height: 300px;" placeholder="{t["input_placeholder"]}"></textarea>
      </div>
      
      <div class="card">
        <h3>{t["stats_title"]}</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
          <div class="result-box">
            <div class="result-value" id="charCount">0</div>
            <div>{t["characters"]}</div>
          </div>
          <div class="result-box">
            <div class="result-value" id="wordCount">0</div>
            <div>{t["words"]}</div>
          </div>
          <div class="result-box">
            <div class="result-value" id="lineCount">0</div>
            <div>{t["lines"]}</div>
          </div>
        </div>
      </div>
      
      <div class="card">
        <h3>{t["actions_title"]}</h3>
        <div class="btn-group">
          <button class="btn btn-secondary" onclick="toUpperCase()">{t["uppercase"]}</button>
          <button class="btn btn-secondary" onclick="toLowerCase()">{t["lowercase"]}</button>
          <button class="btn btn-secondary" onclick="removeDuplicates()">{t["remove_duplicates"]}</button>
          <button class="btn btn-secondary" onclick="sortLines()">{t["sort_lines"]}</button>
          <button class="btn btn-secondary" onclick="reverseText()">{t["reverse_text"]}</button>
          <button class="btn btn-primary" onclick="copyText()">{t["copy"]}</button>
          <button class="btn btn-secondary" onclick="clearText()">{t["clear"]}</button>
        </div>
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
    const textInput = document.getElementById('textInput');
    const charCount = document.getElementById('charCount');
    const wordCount = document.getElementById('wordCount');
    const lineCount = document.getElementById('lineCount');
    
    function updateStats() {{
      const text = textInput.value;
      charCount.textContent = text.length;
      wordCount.textContent = text.trim() ? text.trim().split(/\\s+/).length : 0;
      lineCount.textContent = text ? text.split('\\n').length : 0;
    }}
    
    function toUpperCase() {{
      textInput.value = textInput.value.toUpperCase();
      updateStats();
    }}
    
    function toLowerCase() {{
      textInput.value = textInput.value.toLowerCase();
      updateStats();
    }}
    
    function removeDuplicates() {{
      const lines = textInput.value.split('\\n');
      const unique = [...new Set(lines)];
      textInput.value = unique.join('\\n');
      updateStats();
    }}
    
    function sortLines() {{
      const lines = textInput.value.split('\\n');
      lines.sort();
      textInput.value = lines.join('\\n');
      updateStats();
    }}
    
    function reverseText() {{
      textInput.value = textInput.value.split('').reverse().join('');
      updateStats();
    }}
    
    function copyText() {{
      Utils.copyToClipboard(textInput.value);
    }}
    
    function clearText() {{
      textInput.value = '';
      updateStats();
    }}
    
    textInput.addEventListener('input', updateStats);
    updateStats();
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Text Utilities for all languages...\\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'text-utils'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_text_utils(lang))
        
        print(f"✅ Created: {lang}/text-utils/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Text Utilities for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

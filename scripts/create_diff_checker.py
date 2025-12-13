"""
Create fully functional Text Diff Checker for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '텍스트 비교기 (Diff Checker)',
        'desc': '두 텍스트의 차이점을 쉽고 빠르게 비교하세요. 변경된 부분을 색깔로 표시해줍니다.',
        'original_label': '원본 텍스트',
        'changed_label': '변경된 텍스트',
        'compare_btn': '비교하기',
        'clear_btn': '지우기',
        'result_label': '비교 결과',
        'placeholder_orig': '여기에 원본 텍스트를 입력하세요...',
        'placeholder_changed': '여기에 변경된 텍스트를 입력하세요...',
        'no_diff': '차이점이 없습니다.',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Text Diff Checker',
        'desc': 'Compare two texts difference easily. Highlights added and removed parts.',
        'original_label': 'Original Text',
        'changed_label': 'Changed Text',
        'compare_btn': 'Compare',
        'clear_btn': 'Clear',
        'result_label': 'Comparison Result',
        'placeholder_orig': 'Enter original text here...',
        'placeholder_changed': 'Enter changed text here...',
        'no_diff': 'No differences found.',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': 'テキスト比較ツール (Diff Checker)',
        'desc': '2つのテキストの違いを簡単に比較します。追加および削除された部分をハイライトします。',
        'original_label': '元のテキスト',
        'changed_label': '変更後のテキスト',
        'compare_btn': '比較する',
        'clear_btn': 'クリア',
        'result_label': '比較結果',
        'placeholder_orig': '元のテキストをここに入力...',
        'placeholder_changed': '変更後のテキストをここに入力...',
        'no_diff': '違いは見つかりませんでした。',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'टेक्स्ट अंतर चेकर (Diff Checker)',
        'desc': 'दो टेक्स्ट के बीच अंतर की आसानी से तुलना करें। जोड़े गए और हटाए गए भागों को हाइलाइट करता है।',
        'original_label': 'मूल पाठ',
        'changed_label': 'बदला हुआ पाठ',
        'compare_btn': 'तुलना करें',
        'clear_btn': 'साफ़ करें',
        'result_label': 'तुलना परिणाम',
        'placeholder_orig': 'मूल पाठ यहाँ दर्ज करें...',
        'placeholder_changed': 'बदला हुआ पाठ यहाँ दर्ज करें...',
        'no_diff': 'कोई अंतर नहीं मिला।',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Pemeriksa Perbedaan Teks (Diff Checker)',
        'desc': 'Bandingkan perbedaan dua teks dengan mudah. Soroti bagian yang ditambahkan dan dihapus.',
        'original_label': 'Teks Asli',
        'changed_label': 'Teks Diubah',
        'compare_btn': 'Bandingkan',
        'clear_btn': 'Hapus',
        'result_label': 'Hasil Perbandingan',
        'placeholder_orig': 'Masukkan teks asli di sini...',
        'placeholder_changed': 'Masukkan teks yang diubah di sini...',
        'no_diff': 'Tidak ada perbedaan ditemukan.',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Kiểm Tra Khác Biệt Văn Bản (Diff)',
        'desc': 'So sánh sự khác biệt giữa hai văn bản dễ dàng. Đánh dấu các phần đã thêm và đã xóa.',
        'original_label': 'Văn bản gốc',
        'changed_label': 'Văn bản đã thay đổi',
        'compare_btn': 'So sánh',
        'clear_btn': 'Xóa',
        'result_label': 'Kết quả so sánh',
        'placeholder_orig': 'Nhập văn bản gốc tại đây...',
        'placeholder_changed': 'Nhập văn bản đã thay đổi tại đây...',
        'no_diff': 'Không tìm thấy sự khác biệt.',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'เครื่องมือเปรียบเทียบข้อความ (Diff Checker)',
        'desc': 'เปรียบเทียบความแตกต่างของข้อความสองชุดอย่างง่ายดาย เน้นส่วนที่เพิ่มและลบออก',
        'original_label': 'ข้อความต้นฉบับ',
        'changed_label': 'ข้อความที่เปลี่ยนแปลง',
        'compare_btn': 'เปรียบเทียบ',
        'clear_btn': 'ล้าง',
        'result_label': 'ผลการเปรียบเทียบ',
        'placeholder_orig': 'ป้อนข้อความต้นฉบับที่นี่...',
        'placeholder_changed': 'ป้อนข้อความที่เปลี่ยนแปลงที่นี่...',
        'no_diff': 'ไม่พบความแตกต่าง',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Text-Vergleich (Diff Checker)',
        'desc': 'Vergleichen Sie zwei Texte einfach. Hebt hinzugefügte und entfernte Teile hervor.',
        'original_label': 'Originaltext',
        'changed_label': 'Geänderter Text',
        'compare_btn': 'Vergleichen',
        'clear_btn': 'Löschen',
        'result_label': 'Vergleichsergebnis',
        'placeholder_orig': 'Originaltext hier eingeben...',
        'placeholder_changed': 'Geänderten Text hier eingeben...',
        'no_diff': 'Keine Unterschiede gefunden.',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Comparador de Texto (Diff Checker)',
        'desc': 'Compare a diferença entre dois textos facilmente. Destaca partes adicionadas e removidas.',
        'original_label': 'Texto Original',
        'changed_label': 'Texto Alterado',
        'compare_btn': 'Comparar',
        'clear_btn': 'Limpar',
        'result_label': 'Resultado da Comparação',
        'placeholder_orig': 'Digite o texto original aqui...',
        'placeholder_changed': 'Digite o texto alterado aqui...',
        'no_diff': 'Nenhuma diferença encontrada.',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_diff_checker(lang):
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
  <meta property="og:url" content="https://utilifyapp.net/{lang}/diff-checker/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/diff-checker/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/diff-checker/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/diff-checker/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/diff-checker/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/diff-checker/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/diff-checker/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/diff-checker/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/diff-checker/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/diff-checker/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/diff-checker/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/diff-checker/">
  
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
    "url": "https://utilifyapp.net/{lang}/diff-checker/",
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
    
    .diff-textarea {{
      font-family: var(--font-mono);
      min-height: 250px;
      resize: vertical;
      padding: var(--spacing-md);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      background-color: var(--bg-primary);
      color: var(--text-primary);
    }}
    
    .result-container {{
      margin-top: var(--spacing-xl);
      background-color: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-lg);
      min-height: 100px;
    }}
    
    .diff-result {{
      font-family: var(--font-mono);
      white-space: pre-wrap;
      line-height: 1.6;
    }}
    
    .diff-added {{
      background-color: #d1fae5;
      color: #065f46;
      text-decoration: none;
    }}
    
    .diff-removed {{
      background-color: #fee2e2;
      color: #991b1b;
      text-decoration: line-through;
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
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow">
      <h1>🔀 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <!-- Editors -->
      <div class="editor-container">
        <div class="editor-panel">
          <label class="form-label">{t["original_label"]}</label>
          <textarea id="origText" class="diff-textarea" placeholder="{t["placeholder_orig"]}"></textarea>
        </div>
        
        <div class="editor-panel">
          <label class="form-label">{t["changed_label"]}</label>
          <textarea id="changedText" class="diff-textarea" placeholder="{t["placeholder_changed"]}"></textarea>
        </div>
      </div>
      
      <div class="btn-group" style="margin-top: var(--spacing-lg);">
        <button class="btn btn-primary" onclick="computeDiff()">{t["compare_btn"]}</button>
        <button class="btn btn-secondary" onclick="clearAll()">{t["clear_btn"]}</button>
      </div>
      
      <div class="result-container">
        <h3 style="margin-bottom: var(--spacing-md);">{t["result_label"]}</h3>
        <div id="diffOutput" class="diff-result"></div>
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
  <!-- jsdiff CDN -->
  <script src="https://cdn.jsdelivr.net/npm/diff@5.1.0/dist/diff.min.js"></script>
  <script>
    const origInput = document.getElementById('origText');
    const changedInput = document.getElementById('changedText');
    const output = document.getElementById('diffOutput');
    
    function computeDiff() {{
      const text1 = origInput.value;
      const text2 = changedInput.value;
      
      if (!text1 && !text2) {{
        output.innerHTML = '';
        return;
      }}
      
      const diff = Diff.diffChars(text1, text2);
      const fragment = document.createDocumentFragment();
      let hasDiff = false;

      diff.forEach((part) => {{
        // color added text in green and removed text in red
        const colorClass = part.added ? 'diff-added' :
          part.removed ? 'diff-removed' : '';
        
        if (part.added || part.removed) hasDiff = true;
          
        const span = document.createElement('span');
        span.className = colorClass;
        span.appendChild(document.createTextNode(part.value));
        fragment.appendChild(span);
      }});
      
      output.innerHTML = '';
      if (!hasDiff && text1 === text2 && text1 !== '') {{
          output.textContent = '{t["no_diff"]}';
      }} else {{
          output.appendChild(fragment);
      }}
    }}
    
    function clearAll() {{
      origInput.value = '';
      changedInput.value = '';
      output.innerHTML = '';
    }}
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Diff Checker for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'diff-checker'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_diff_checker(lang))
        
        print(f"✅ Created: {lang}/diff-checker/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Diff Checker for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

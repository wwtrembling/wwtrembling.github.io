"""
Create fully functional Markdown Previewer for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '마크다운 에디터 & 미리보기',
        'desc': '실시간 마크다운 미리보기 도구. 손쉽게 마크다운 문서를 작성하고 변환된 HTML 결과를 확인하세요.',
        'editor_label': '마크다운 입력',
        'preview_label': '미리보기',
        'placeholder': '# 제목을 입력하세요\n\n**굵은 글씨**와 *이탤릭*...',
        'copy_html_btn': 'HTML 복사',
        'download_md_btn': 'MD 다운로드',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Markdown Editor & Preview',
        'desc': 'Real-time Markdown preview tool. Write Markdown effortlessly and see converted HTML instantly.',
        'editor_label': 'Markdown Input',
        'preview_label': 'Preview',
        'placeholder': '# Enter Title\n\n**Bold** and *Italic*...',
        'copy_html_btn': 'Copy HTML',
        'download_md_btn': 'Download .md',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': 'Markdownエディタ＆プレビュー',
        'desc': 'リアルタイムMarkdownプレビューツール。Markdownを簡単に記述し、変換されたHTMLを即座に確認できます。',
        'editor_label': 'Markdown入力',
        'preview_label': 'プレビュー',
        'placeholder': '# タイトルを入力\n\n**太字** と *イタリック*...',
        'copy_html_btn': 'HTMLをコピー',
        'download_md_btn': 'MDをダウンロード',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'मार्कडाउन एडिटर और पूर्वावलोकन',
        'desc': 'रीयल-टाइम मार्कडाउन पूर्वावलोकन उपकरण। आसानी से मार्कडाउन लिखें और परिवर्तित HTML तुरंत देखें।',
        'editor_label': 'मार्कडाउन इनपुट',
        'preview_label': 'पूर्वावलोकन',
        'placeholder': '# शीर्षक दर्ज करें\n\n**बोल्ड** और *इटैलिक*...',
        'copy_html_btn': 'HTML कॉपी करें',
        'download_md_btn': 'MD डाउनलोड करें',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Editor & Pratinjau Markdown',
        'desc': 'Alat pratinjau Markdown waktu nyata. Tulis Markdown dengan mudah dan lihat HTML yang dikonversi secara instan.',
        'editor_label': 'Input Markdown',
        'preview_label': 'Pratinjau',
        'placeholder': '# Masukkan Judul\n\n**Tebal** dan *Miring*...',
        'copy_html_btn': 'Salin HTML',
        'download_md_btn': 'Unduh .md',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Trình Biên Tập & Xem Trước Markdown',
        'desc': 'Công cụ xem trước Markdown thời gian thực. Viết Markdown dễ dàng và xem HTML đã chuyển đổi ngay lập tức.',
        'editor_label': 'Nhập Markdown',
        'preview_label': 'Xem trước',
        'placeholder': '# Nhập tiêu đề\n\n**In đậm** và *In nghiêng*...',
        'copy_html_btn': 'Sao chép HTML',
        'download_md_btn': 'Tải xuống .md',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'ตัวแก้ไขและดูตัวอย่าง Markdown',
        'desc': 'เครื่องมือดูตัวอย่าง Markdown แบบเรียลไทม์ เขียน Markdown อย่างง่ายดายและดู HTML ที่แปลงแล้วทันที',
        'editor_label': 'ป้อน Markdown',
        'preview_label': 'ดูตัวอย่าง',
        'placeholder': '# ป้อนชื่อเรื่อง\n\n**ตัวหนา** และ *ตัวเอียง*...',
        'copy_html_btn': 'คัดลอก HTML',
        'download_md_btn': 'ดาวน์โหลด .md',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Markdown Editor & Vorschau',
        'desc': 'Echtzeit-Markdown-Vorschau-Tool. Schreiben Sie Markdown mühelos und sehen Sie sofort das konvertierte HTML.',
        'editor_label': 'Markdown Eingabe',
        'preview_label': 'Vorschau',
        'placeholder': '# Titel eingeben\n\n**Fett** und *Kursiv*...',
        'copy_html_btn': 'HTML kopieren',
        'download_md_btn': 'MD herunterladen',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Editor e Visualizador Markdown',
        'desc': 'Ferramenta de visualização Markdown em tempo real. Escreva Markdown sem esforço e veja o HTML convertido instantaneamente.',
        'editor_label': 'Entrada Markdown',
        'preview_label': 'Visualização',
        'placeholder': '# Digite o Título\n\n**Negrito** e *Itálico*...',
        'copy_html_btn': 'Copiar HTML',
        'download_md_btn': 'Baixar .md',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_markdown_previewer(lang):
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
  <meta property="og:url" content="https://utilifyapp.net/{lang}/markdown-previewer/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/markdown-previewer/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/markdown-previewer/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/markdown-previewer/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/markdown-previewer/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/markdown-previewer/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/markdown-previewer/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/markdown-previewer/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/markdown-previewer/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/markdown-previewer/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/markdown-previewer/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/markdown-previewer/">
  
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
    "url": "https://utilifyapp.net/{lang}/markdown-previewer/",
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
      height: 70vh;
      min-height: 500px;
    }}
    
    .panel {{
      display: flex;
      flex-direction: column;
      gap: var(--spacing-sm);
      height: 100%;
    }}
    
    .md-textarea {{
      flex: 1;
      font-family: var(--font-mono);
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: var(--spacing-md);
      resize: none;
    }}
    
    .md-preview {{
      flex: 1;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: var(--spacing-xl);
      overflow-y: auto;
      /* Basic Markdown Styling */
    }}

    .md-preview h1 {{ font-size: 2em; margin-bottom: 0.5em; }}
    .md-preview h2 {{ font-size: 1.5em; margin-bottom: 0.5em; }}
    .md-preview p {{ margin-bottom: 1em; line-height: 1.6; }}
    .md-preview code {{ background: #f1f5f9; padding: 2px 4px; border-radius: 4px; }}
    .md-preview pre {{ background: #f1f5f9; padding: 1em; border-radius: 8px; overflow-x: auto; }}
    .md-preview blockquote {{ border-left: 4px solid var(--border-color); padding-left: 1em; color: var(--text-secondary); }}
    
    @media (max-width: 768px) {{
      .editor-container {{
        grid-template-columns: 1fr;
        height: auto;
      }}
      .md-textarea {{
        min-height: 300px;
      }}
      .md-preview {{
        min-height: 300px;
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
      <h1>📝 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <div class="btn-group">
        <button class="btn btn-secondary" onclick="copyHTML()">{t["copy_html_btn"]}</button>
        <button class="btn btn-secondary" onclick="downloadMD()">{t["download_md_btn"]}</button>
      </div>

      <div class="editor-container">
        <div class="panel">
          <label class="form-label">{t["editor_label"]}</label>
          <textarea id="markdownInput" class="md-textarea" placeholder="{t["placeholder"]}"></textarea>
        </div>
        
        <div class="panel">
          <label class="form-label">{t["preview_label"]}</label>
          <div id="preview" class="md-preview"></div>
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
  <!-- marked.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js"></script>
  <script>
    const input = document.getElementById('markdownInput');
    const preview = document.getElementById('preview');
    
    function updatePreview() {{
      const text = input.value;
      preview.innerHTML = marked.parse(text);
    }}
    
    input.addEventListener('input', Utils.debounce(updatePreview, 300));
    
    // Initial Render
    updatePreview();
    
    function copyHTML() {{
      const html = preview.innerHTML;
      if (html) {{
        Utils.copyToClipboard(html);
      }}
    }}
    
    function downloadMD() {{
      const text = input.value;
      if (!text) return;
      
      const blob = new Blob([text], {{ type: 'text/markdown' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'document.md';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }}
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Markdown Previewer for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'markdown-previewer'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_markdown_previewer(lang))
        
        print(f"✅ Created: {lang}/markdown-previewer/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Markdown Previewer for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

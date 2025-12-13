"""
Create fully functional YouTube Thumbnail Downloader for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '유튜브 썸네일 다운로더',
        'desc': '유튜브 영상의 썸네일 이미지를 고화질(4K, HD)로 추출하고 다운로드하세요. 무료, 간편한 도구.',
        'input_label': '유튜브 영상 주소 (URL)',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': '썸네일 가져오기',
        'download_btn': '이미지 다운로드',
        'quality_max': '최대 화질 (MaxRes - 1280x720+)',
        'quality_high': '고화질 (High - 480x360)',
        'quality_medium': '중간 화질 (Medium - 320x180)',
        'error_invalid_url': '잘못된 유튜브 URL입니다.',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'YouTube Thumbnail Downloader',
        'desc': 'Extract and download YouTube video thumbnails in high quality (4K, HD). Free and easy tool.',
        'input_label': 'YouTube Video URL',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'Get Thumbnail',
        'download_btn': 'Download Image',
        'quality_max': 'Maximum Resolution (1280x720+)',
        'quality_high': 'High Quality (480x360)',
        'quality_medium': 'Medium Quality (320x180)',
        'error_invalid_url': 'Invalid YouTube URL.',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': 'YouTubeサムネイルダウンローダー',
        'desc': 'YouTube動画のサムネイル画像を高品質（4K、HD）で抽出してダウンロードします。無料のかんたんツール。',
        'input_label': 'YouTube動画URL',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'サムネイルを取得',
        'download_btn': '画像をダウンロード',
        'quality_max': '最大解像度 (1280x720+)',
        'quality_high': '高画質 (480x360)',
        'quality_medium': '中画質 (320x180)',
        'error_invalid_url': '無効なYouTube URLです。',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'YouTube थंबनेल डाउनलोडर',
        'desc': 'YouTube वीडियो थंबनेल छवियों को उच्च गुणवत्ता (4K, HD) में निकालें और डाउनलोड करें। मुफ्त और आसान उपकरण।',
        'input_label': 'YouTube वीडियो URL',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'थंबनेल प्राप्त करें',
        'download_btn': 'छवि डाउनलोड करें',
        'quality_max': 'अधिकतम रिज़ॉल्यूशन (1280x720+)',
        'quality_high': 'उच्च गुणवत्ता (480x360)',
        'quality_medium': 'मध्यम गुणवत्ता (320x180)',
        'error_invalid_url': 'अमान्य YouTube URL.',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Pengunduh Thumbnail YouTube',
        'desc': 'Ekstrak dan unduh thumbnail video YouTube dalam kualitas tinggi (4K, HD). Alat gratis dan mudah.',
        'input_label': 'URL Video YouTube',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'Dapatkan Thumbnail',
        'download_btn': 'Unduh Gambar',
        'quality_max': 'Resolusi Maksimum (1280x720+)',
        'quality_high': 'Kualitas Tinggi (480x360)',
        'quality_medium': 'Kualitas Sedang (320x180)',
        'error_invalid_url': 'URL YouTube tidak valid.',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Trình Tải Thumbnail YouTube',
        'desc': 'Trích xuất và tải xuống hình thu nhỏ video YouTube chất lượng cao (4K, HD). Công cụ miễn phí và dễ dàng.',
        'input_label': 'URL Video YouTube',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'Lấy Thumbnail',
        'download_btn': 'Tải xuống hình ảnh',
        'quality_max': 'Độ phân giải tối đa (1280x720+)',
        'quality_high': 'Chất lượng cao (480x360)',
        'quality_medium': 'Chất lượng trung bình (320x180)',
        'error_invalid_url': 'URL YouTube không hợp lệ.',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'เครื่องมือดาวน์โหลดภาพปก YouTube',
        'desc': 'ดึงและดาวน์โหลดภาพขนาดย่อวิดีโอ YouTube ด้วยคุณภาพสูง (4K, HD) เครื่องมือฟรีและง่ายดาย',
        'input_label': 'URL วิดีโอ YouTube',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'ดึงภาพปก',
        'download_btn': 'ดาวน์โหลดรูปภาพ',
        'quality_max': 'ความละเอียดสูงสุด (1280x720+)',
        'quality_high': 'คุณภาพสูง (480x360)',
        'quality_medium': 'คุณภาพปานกลาง (320x180)',
        'error_invalid_url': 'URL YouTube ไม่ถูกต้อง',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'YouTube Thumbnail Downloader',
        'desc': 'Extrahieren und laden Sie YouTube-Video-Thumbnails in hoher Qualität (4K, HD) herunter. Kostenloses Tool.',
        'input_label': 'YouTube Video URL',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'Thumbnail abrufen',
        'download_btn': 'Bild herunterladen',
        'quality_max': 'Maximale Auflösung (1280x720+)',
        'quality_high': 'Hohe Qualität (480x360)',
        'quality_medium': 'Mittlere Qualität (320x180)',
        'error_invalid_url': 'Ungültige YouTube-URL.',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Baixar Thumbnail do YouTube',
        'desc': 'Extraia e baixe miniaturas de vídeos do YouTube em alta qualidade (4K, HD). Ferramenta gratuita e fácil.',
        'input_label': 'URL do Vídeo YouTube',
        'input_placeholder': 'https://www.youtube.com/watch?v=...',
        'get_btn': 'Obter Miniatura',
        'download_btn': 'Baixar Imagem',
        'quality_max': 'Resolução Máxima (1280x720+)',
        'quality_high': 'Alta Qualidade (480x360)',
        'quality_medium': 'Qualidade Média (320x180)',
        'error_invalid_url': 'URL do YouTube inválido.',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_thumbnail_downloader(lang):
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
  <meta property="og:url" content="https://utilifyapp.net/{lang}/thumbnail-downloader/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/thumbnail-downloader/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/thumbnail-downloader/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/thumbnail-downloader/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/thumbnail-downloader/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/thumbnail-downloader/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/thumbnail-downloader/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/thumbnail-downloader/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/thumbnail-downloader/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/thumbnail-downloader/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/thumbnail-downloader/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/thumbnail-downloader/">
  
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
    "url": "https://utilifyapp.net/{lang}/thumbnail-downloader/",
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
    .downloader-container {{
      max-width: 800px;
      margin: 0 auto;
      margin-top: var(--spacing-lg);
    }}
    
    .input-section {{
      display: flex;
      gap: var(--spacing-md);
      margin-bottom: var(--spacing-xl);
    }}
    
    .input-wrapper {{
      flex: 1;
    }}
    
    .results-grid {{
      display: grid;
      gap: var(--spacing-xl);
    }}
    
    .thumb-card {{
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-lg);
    }}
    
    .thumb-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--spacing-md);
    }}
    
    .thumb-img {{
      width: 100%;
      height: auto;
      border-radius: var(--radius-md);
      background: #eee;
    }}
    
    .download-link {{
      text-decoration: none;
    }}
    
    @media (max-width: 768px) {{
      .input-section {{
        flex-direction: column;
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
      <h1>📺 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <div class="downloader-container">
        <div class="input-section">
          <div class="input-wrapper">
            <input type="text" id="urlInput" class="form-input" placeholder="{t["input_placeholder"]}">
          </div>
          <button class="btn btn-primary" onclick="getThumbnails()">{t["get_btn"]}</button>
        </div>
        
        <div id="results" class="results-grid"></div>
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
    const urlInput = document.getElementById('urlInput');
    const results = document.getElementById('results');
    
    function extractVideoID(url) {{
      if (!url) return null;
      var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
      var match = url.match(regExp);
      return (match && match[2].length == 11) ? match[2] : null;
    }}
    
    function getThumbnails() {{
      const url = urlInput.value.trim();
      const videoId = extractVideoID(url);
      
      if (!videoId) {{
        Utils.showToast('{t["error_invalid_url"]}');
        return;
      }}
      
      renderThumbnails(videoId);
    }}
    
    function renderThumbnails(videoId) {{
      const qualities = [
        {{ label: '{t["quality_max"]}', suffix: 'maxresdefault' }},
        {{ label: '{t["quality_high"]}', suffix: 'hqdefault' }},
        {{ label: '{t["quality_medium"]}', suffix: 'mqdefault' }},
      ];
      
      results.innerHTML = qualities.map(q => {{
        const imgUrl = `https://img.youtube.com/vi/${{videoId}}/${{q.suffix}}.jpg`;
        return `
          <div class="thumb-card">
            <div class="thumb-header">
              <h3>${{q.label}}</h3>
              <a href="${{imgUrl}}" target="_blank" download="thumbnail.jpg" class="download-link">
                <button class="btn btn-secondary">{t["download_btn"]}</button>
              </a>
            </div>
            <img src="${{imgUrl}}" class="thumb-img" alt="Thumbnail">
          </div>
        `;
      }}).join('');
    }}
    
    // Auto-search on paste
    urlInput.addEventListener('paste', (e) => {{
      setTimeout(getThumbnails, 100);
    }});
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating YouTube Thumbnail Downloader for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'thumbnail-downloader'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_thumbnail_downloader(lang))
        
        print(f"✅ Created: {lang}/thumbnail-downloader/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Thumbnail Downloader for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

"""
Create fully functional Image Editor with Crop, Rotate, Flip using Cropper.js for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '이미지 편집기 (자르기/회전/필터)',
        'desc': '이미지 자르기, 회전, 뒤집기 및 필터 적용을 한 번에! 간편한 온라인 무료 사진 편집 도구.',
        'upload_title': '이미지 업로드',
        'upload_desc': '클릭하거나 드래그하여 업로드',
        'tab_crop': '자르기 & 회전',
        'tab_filter': '필터 효과',
        'btn_rotate_left': '좌회전',
        'btn_rotate_right': '우회전',
        'btn_flip_h': '좌우반전',
        'btn_flip_v': '상하반전',
        'btn_reset': '초기화',
        'label_aspect': '비율:',
        'ratio_free': '자유',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': '밝기',
        'label_contrast': '대비',
        'label_saturation': '채도',
        'btn_download': '편집된 이미지 다운로드',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Image Editor (Crop/Rotate/Filter)',
        'desc': 'Crop, Rotate, Flip and Filter images easily online. Free and secure photo editor.',
        'upload_title': 'Upload Image',
        'upload_desc': 'Click or Drag to Upload',
        'tab_crop': 'Crop & Rotate',
        'tab_filter': 'Filters',
        'btn_rotate_left': 'Rotate Left',
        'btn_rotate_right': 'Rotate Right',
        'btn_flip_h': 'Flip Horizontally',
        'btn_flip_v': 'Flip Vertically',
        'btn_reset': 'Reset',
        'label_aspect': 'Ratio:',
        'ratio_free': 'Free',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'Brightness',
        'label_contrast': 'Contrast',
        'label_saturation': 'Saturation',
        'btn_download': 'Download Image',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': '画像編集ツール (トリミング/回転/フィルター)',
        'desc': '画像のトリミング、回転、反転、フィルター適用が簡単にできます。無料のオンライン写真編集ツール。',
        'upload_title': '画像アップロード',
        'upload_desc': 'クリックまたはドラッグしてアップロード',
        'tab_crop': 'トリミング & 回転',
        'tab_filter': 'フィルター',
        'btn_rotate_left': '左回転',
        'btn_rotate_right': '右回転',
        'btn_flip_h': '左右反転',
        'btn_flip_v': '上下反転',
        'btn_reset': 'リセット',
        'label_aspect': '比率:',
        'ratio_free': '自由',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': '明るさ',
        'label_contrast': 'コントラスト',
        'label_saturation': '彩度',
        'btn_download': '画像をダウンロード',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'इमेज एडिटर (क्रॉप/रोटेट/फिल्टर)',
        'desc': 'इमेज क्रॉप, रोटेट, फ्लिप और फिल्टर आसानी से ऑनलाइन करें। मुफ्त और सुरक्षित फोटो एडिटर।',
        'upload_title': 'इमेज अपलोड करें',
        'upload_desc': 'अपलोड करने के लिए क्लिक या ड्रैग करें',
        'tab_crop': 'क्रॉप और रोटेट',
        'tab_filter': 'फिल्टर',
        'btn_rotate_left': 'बाएं घुमाएं',
        'btn_rotate_right': 'दाएं घुमाएं',
        'btn_flip_h': 'क्षैतिज पलटें',
        'btn_flip_v': 'लंबवत पलटें',
        'btn_reset': 'रीसेट',
        'label_aspect': 'अनुपात:',
        'ratio_free': 'निःशुल्क',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'चमक',
        'label_contrast': 'कंट्रास्ट',
        'label_saturation': 'संतृप्ति',
        'btn_download': 'इमेज डाउनलोड करें',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Editor Gambar (Potong/Putar/Filter)',
        'desc': 'Potong, Putar, Balik, dan Filter gambar dengan mudah secara online. Editor foto gratis dan aman.',
        'upload_title': 'Unggah Gambar',
        'upload_desc': 'Klik atau Seret untuk Mengunggah',
        'tab_crop': 'Potong & Putar',
        'tab_filter': 'Filter',
        'btn_rotate_left': 'Putar Kiri',
        'btn_rotate_right': 'Putar Kanan',
        'btn_flip_h': 'Balik Horizontal',
        'btn_flip_v': 'Balik Vertikal',
        'btn_reset': 'Atur Ulang',
        'label_aspect': 'Rasio:',
        'ratio_free': 'Bebas',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'Kecerahan',
        'label_contrast': 'Kontras',
        'label_saturation': 'Saturasi',
        'btn_download': 'Unduh Gambar',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Trình Biên Tập Ảnh (Cắt/Xoay/Bộ Lọc)',
        'desc': 'Cắt, Xoay, Lật và Lọc hình ảnh dễ dàng trực tuyến. Trình chỉnh sửa ảnh miễn phí và bảo mật.',
        'upload_title': 'Tải ảnh lên',
        'upload_desc': 'Nhấp hoặc Kéo để tải lên',
        'tab_crop': 'Cắt & Xoay',
        'tab_filter': 'Bộ lọc',
        'btn_rotate_left': 'Xoay Trái',
        'btn_rotate_right': 'Xoay Phải',
        'btn_flip_h': 'Lật Ngang',
        'btn_flip_v': 'Lật Dọc',
        'btn_reset': 'Đặt lại',
        'label_aspect': 'Tỷ lệ:',
        'ratio_free': 'Tự do',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'Độ sáng',
        'label_contrast': 'Độ tương phản',
        'label_saturation': 'Độ bão hòa',
        'btn_download': 'Tải xuống hình ảnh',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'โปรแกรมแก้ไขรูปภาพ (ตัด/หมุน/ฟิลเตอร์)',
        'desc': 'ตัด หมุน พลิก และใส่ฟิลเตอร์รูปภาพออนไลน์ได้ง่ายๆ เครื่องมือแก้ไขภาพฟรีและปลอดภัย',
        'upload_title': 'อัปโหลดรูปภาพ',
        'upload_desc': 'คลิกหรือลากเพื่ออัปโหลด',
        'tab_crop': 'ตัด & หมุน',
        'tab_filter': 'ฟิลเตอร์',
        'btn_rotate_left': 'หมุนซ้าย',
        'btn_rotate_right': 'หมุนขวา',
        'btn_flip_h': 'พลิกแนวนอน',
        'btn_flip_v': 'พลิกแนวตั้ง',
        'btn_reset': 'รีเซ็ต',
        'label_aspect': 'สัดส่วน:',
        'ratio_free': 'อิสระ',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'ความสว่าง',
        'label_contrast': 'ความคมชัด',
        'label_saturation': 'ความอิ่มตัว',
        'btn_download': 'ดาวน์โหลดรูปภาพ',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Bildeditor (Zuschneiden/Drehen/Filter)',
        'desc': 'Bilder online einfach zuschneiden, drehen, spiegeln und filtern. Kostenloser Fotoeditor.',
        'upload_title': 'Bild hochladen',
        'upload_desc': 'Klicken oder Ziehen zum Hochladen',
        'tab_crop': 'Zuschneiden & Drehen',
        'tab_filter': 'Filter',
        'btn_rotate_left': 'Links drehen',
        'btn_rotate_right': 'Rechts drehen',
        'btn_flip_h': 'Horizontal spiegeln',
        'btn_flip_v': 'Vertikal spiegeln',
        'btn_reset': 'Zurücksetzen',
        'label_aspect': 'Verhältnis:',
        'ratio_free': 'Frei',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'Helligkeit',
        'label_contrast': 'Kontrast',
        'label_saturation': 'Sättigung',
        'btn_download': 'Bild herunterladen',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Editor de Imagem (Cortar/Girar/Filtros)',
        'desc': 'Corte, Gire, Inverta e Filtre imagens facilmente online. Editor de fotos gratuito e seguro.',
        'upload_title': 'Carregar Imagem',
        'upload_desc': 'Clique ou Arraste para Carregar',
        'tab_crop': 'Cortar e Girar',
        'tab_filter': 'Filtros',
        'btn_rotate_left': 'Girar Esq',
        'btn_rotate_right': 'Girar Dir',
        'btn_flip_h': 'Inverter Horz',
        'btn_flip_v': 'Inverter Vert',
        'btn_reset': 'Redefinir',
        'label_aspect': 'Proporção:',
        'ratio_free': 'Livre',
        'ratio_169': '16:9',
        'ratio_43': '4:3',
        'ratio_11': '1:1',
        'label_brightness': 'Brilho',
        'label_contrast': 'Contraste',
        'label_saturation': 'Saturação',
        'btn_download': 'Baixar Imagem',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_image_editor(lang):
    t = TRANSLATIONS[lang]
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6334819180242631">
  <title>{t["title"]} - Utilify</title>
  <meta name="description" content="{t["desc"]}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{t["title"]} - Utilify">
  <meta property="og:description" content="{t["desc"]}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utilifyapp.net/{lang}/image-editor/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/image-editor/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/image-editor/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/image-editor/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/image-editor/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/image-editor/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/image-editor/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/image-editor/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/image-editor/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/image-editor/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/image-editor/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/image-editor/">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Cropper.js CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.css">
  
  <!-- Styles -->
  <link rel="stylesheet" href="/assets/css/main.css">
  
  <!-- JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "{t["title"]}",
    "description": "{t["desc"]}",
    "url": "https://utilifyapp.net/{lang}/image-editor/",
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
    .editor-wrapper {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: var(--spacing-lg);
      margin-top: var(--spacing-lg);
      align-items: start;
    }}
    
    .sidebar {{
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-lg);
      position: sticky;
      top: 20px;
    }}
    
    .canvas-container {{
      background: #333; /* Dark background for canvas */
      border-radius: var(--radius-lg);
      padding: var(--spacing-md);
      min-height: 400px;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      position: relative;
    }}
    
    img#image {{
      max-width: 100%;
      max-height: 600px;
      display: block;
    }}
    
    .upload-box {{
      border: 2px dashed var(--border-color);
      padding: var(--spacing-xl);
      text-align: center;
      cursor: pointer;
      border-radius: var(--radius-lg);
      background: var(--bg-secondary);
      transition: all 0.2s;
      width: 100%;
      height: 400px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }}
    
    .upload-box:hover {{
      border-color: var(--primary-color);
      background: var(--bg-primary);
    }}
    
    .tool-section {{
      margin-bottom: var(--spacing-lg);
      padding-bottom: var(--spacing-lg);
      border-bottom: 1px solid var(--border-color);
    }}
    
    .tool-section:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}
    
    .tool-title {{
      font-weight: 600;
      margin-bottom: var(--spacing-md);
      display: block;
      color: var(--text-primary);
    }}
    
    .btn-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-sm);
    }}
    
    .btn-tool {{
      padding: 8px;
      font-size: 0.9rem;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.1s;
    }}
    
    .btn-tool:hover {{
      background: var(--bg-primary);
      border-color: var(--primary-color);
    }}

    .btn-tool.active {{
      background: var(--primary-color);
      color: white;
      border-color: var(--primary-color);
    }}
    
    .slider-container {{
      margin-bottom: var(--spacing-md);
    }}
    
    .slider-header {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 4px;
      font-size: 0.9rem;
      color: var(--text-secondary);
    }}
    
    .download-btn {{
      width: 100%;
      margin-top: var(--spacing-md);
    }}
    
    @media (max-width: 900px) {{
      .editor-wrapper {{
        grid-template-columns: 1fr;
      }}
      
      .sidebar {{
        order: 2;
        position: static;
      }}
      
      .canvas-container {{
        order: 1;
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
          🛠️ Utilify
        </a>
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow" style="max-width: 1200px;">
      <h1>🎨 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>

      <div id="uploadScreen">
        <div class="upload-box" onclick="document.getElementById('fileInput').click()">
          <span style="font-size: 3rem;">📁</span>
          <h3>{t["upload_title"]}</h3>
          <p>{t["upload_desc"]}</p>
          <input type="file" id="fileInput" accept="image/*" hidden>
        </div>
      </div>
      
      <div id="editorScreen" class="editor-wrapper" style="display: none;">
        <!-- Sidebar Controls -->
        <aside class="sidebar">
          
          <!-- Crop / Rotate Tools -->
          <div class="tool-section">
            <span class="tool-title">{t["tab_crop"]}</span>
            <div class="btn-grid">
              <button class="btn-tool" onclick="rotate(-90)" title="{t["btn_rotate_left"]}">↺ 90°</button>
              <button class="btn-tool" onclick="rotate(90)" title="{t["btn_rotate_right"]}">↻ 90°</button>
              <button class="btn-tool" onclick="flipX()" title="{t["btn_flip_h"]}">⇄ Flip</button>
              <button class="btn-tool" onclick="flipY()" title="{t["btn_flip_v"]}">⇅ Flip</button>
            </div>
            
            <div style="margin-top: var(--spacing-md);">
              <span class="tool-title" style="font-size: 0.9rem;">{t["label_aspect"]}</span>
              <div class="btn-grid" style="grid-template-columns: 1fr 1fr 1fr;">
                <button class="btn-tool active" onclick="setAspectRatio(NaN)">{t["ratio_free"]}</button>
                <button class="btn-tool" onclick="setAspectRatio(1.777)">16:9</button>
                <button class="btn-tool" onclick="setAspectRatio(1.333)">4:3</button>
                <button class="btn-tool" onclick="setAspectRatio(1)">1:1</button>
              </div>
            </div>
          </div>
          
          <!-- Filter Tools -->
          <div class="tool-section">
            <span class="tool-title">{t["tab_filter"]}</span>
            
            <!-- Brightness -->
            <div class="slider-container">
              <div class="slider-header">
                <span>{t["label_brightness"]}</span>
                <span id="valBrightness">0</span>
              </div>
              <input type="range" id="rngBrightness" class="range-slider" min="-100" max="100" value="0" oninput="updateFilters()">
            </div>
            
            <!-- Contrast -->
            <div class="slider-container">
              <div class="slider-header">
                <span>{t["label_contrast"]}</span>
                <span id="valContrast">0</span>
              </div>
              <input type="range" id="rngContrast" class="range-slider" min="-100" max="100" value="0" oninput="updateFilters()">
            </div>
            
            <!-- Saturation -->
            <div class="slider-container">
              <div class="slider-header">
                <span>{t["label_saturation"]}</span>
                <span id="valSaturation">0</span>
              </div>
              <input type="range" id="rngSaturation" class="range-slider" min="-100" max="100" value="0" oninput="updateFilters()">
            </div>
            
            <button class="btn-tool" style="width: 100%;" onclick="resetFilters()">{t["btn_reset"]}</button>
          </div>
          
          <button class="btn btn-primary download-btn" onclick="downloadImage()">{t["btn_download"]}</button>
          <button class="btn btn-secondary" style="width: 100%; margin-top: 8px;" onclick="location.reload()">New Image</button>
        </aside>
        
        <!-- Canvas Area -->
        <div class="canvas-container">
          <img id="image" src="">
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
        <p>&copy; 2025 Utilify. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="/assets/js/common.js"></script>
  <!-- Cropper.js JS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.js"></script>
  
  <script>
    // Variables
    const fileInput = document.getElementById('fileInput');
    const uploadScreen = document.getElementById('uploadScreen');
    const editorScreen = document.getElementById('editorScreen');
    const imageElement = document.getElementById('image');
    
    // Sliders
    const rngBrightness = document.getElementById('rngBrightness');
    const rngContrast = document.getElementById('rngContrast');
    const rngSaturation = document.getElementById('rngSaturation');
    const valBrightness = document.getElementById('valBrightness');
    const valContrast = document.getElementById('valContrast');
    const valSaturation = document.getElementById('valSaturation');
    
    let cropper = null;
    let scaleX = 1;
    let scaleY = 1;
    
    // 1. Upload
    fileInput.addEventListener('change', (e) => {{
      const file = e.target.files[0];
      if (file) {{
        const reader = new FileReader();
        reader.onload = (evt) => {{
          imageElement.src = evt.target.result;
          uploadScreen.style.display = 'none';
          editorScreen.style.display = 'grid';
          initCropper();
        }};
        reader.readAsDataURL(file);
      }}
    }});
    
    // 2. Initialize Cropper
    function initCropper() {{
      if (cropper) {{
        cropper.destroy();
      }}
      
      cropper = new Cropper(imageElement, {{
        viewMode: 1, // Restrict crop box to canvas
        dragMode: 'move',
        autoCropArea: 0.8,
        restore: false,
        guides: true,
        center: true,
        highlight: false,
        cropBoxMovable: true,
        cropBoxResizable: true,
        toggleDragModeOnDblclick: false,
      }});
    }}
    
    // 3. Crop/Rotate Tools
    function rotate(deg) {{
      if(cropper) cropper.rotate(deg);
    }}
    
    function flipX() {{
      if(cropper) {{
        scaleX = -scaleX;
        cropper.scaleX(scaleX);
      }}
    }}
    
    function flipY() {{
      if(cropper) {{
        scaleY = -scaleY;
        cropper.scaleY(scaleY);
      }}
    }}
    
    function setAspectRatio(ratio) {{
      if(cropper) cropper.setAspectRatio(ratio);
      
      // Update UI active state
      const buttons = document.querySelectorAll('.tool-section button');
      buttons.forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
    }}
    
    // 4. Filters (Visual Preview on Canvas DOM)
    // Cropper wraps the image. We can apply CSS filters to the cropper-container or the image wrapper for preview.
    // However, for correct preview during cropping, it's best to apply to the .cropper-canvas container?
    // Actually, simple CSS filter on the 'cropper-view-box img' gives a good preview.
    
    function updateFilters() {{
      const b = rngBrightness.value;
      const c = rngContrast.value;
      const s = rngSaturation.value;
      
      valBrightness.textContent = b;
      valContrast.textContent = c;
      valSaturation.textContent = s;
      
      // Calculate CSS filter string
      // Brightness: 100% is default. Range -100 to 100 => 0% to 200%
      // Contrast: 100% is default. 0% to 200%
      // Saturation: 100% default. 0% to 200%
      
      const cssB = (100 + parseInt(b)) + '%';
      const cssC = (100 + parseInt(c)) + '%';
      const cssS = (100 + parseInt(s)) + '%';
      
      const filterString = `brightness(${{cssB}}) contrast(${{cssC}}) saturate(${{cssS}})`;
      
      // Apply to the relevant Cropper elements for preview
      const uploadedImg = document.querySelector('.cropper-hide'); // Original
      const viewBoxImg = document.querySelector('.cropper-view-box img'); // The one inside crop box
      const canvasImg = document.querySelector('.cropper-canvas img'); // The dim one outside
      
      if (viewBoxImg) viewBoxImg.style.filter = filterString;
      if (canvasImg) canvasImg.style.filter = filterString;
    }}
    
    function resetFilters() {{
      rngBrightness.value = 0;
      rngContrast.value = 0;
      rngSaturation.value = 0;
      updateFilters();
    }}
    
    // 5. Download
    function downloadImage() {{
      if (!cropper) return;
      
      // 1. Get Cropped Canvas (this applies crop, rotate, flip)
      const canvas = cropper.getCroppedCanvas({{
        maxWidth: 4096,
        maxHeight: 4096,
        imageSmoothingQuality: 'high'
      }});
      
      if (!canvas) return;
      
      // 2. Apply Filters using Context (Pixel Manipulation) to the result canvas
      // Because CSS filters on the DOM don't export to the canvas automatically.
      
      const ctx = canvas.getContext('2d');
      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      const data = imageData.data;
      
      const b = parseInt(rngBrightness.value);     // -100 to 100
      const c = parseInt(rngContrast.value);       // -100 to 100
      const s = parseInt(rngSaturation.value);     // -100 to 100
      
      // Optimization: If all are 0, skip loop
      if (b !== 0 || c !== 0 || s !== 0) {{
         // Convert ranges to factors
         // Contrast: formula is usually factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
         // let's use a simplified logical approach or standard formula
         
         const contrastFactor = (259 * (c + 255)) / (255 * (259 - c));
         // Saturation: more complex. 
         const satFactor = (100 + s) / 100;
         
         for (let i = 0; i < data.length; i += 4) {{
            let r = data[i];
            let g = data[i+1];
            let bl = data[i+2];
            
            // 1. Brightness (Simple additive)
            r += b * 2.55; // mapping 100 to 255 roughly
            g += b * 2.55;
            bl += b * 2.55;
            
            // 2. Contrast
            r = contrastFactor * (r - 128) + 128;
            g = contrastFactor * (g - 128) + 128;
            bl = contrastFactor * (bl - 128) + 128;
            
            // 3. Saturation (Gray scale interpolation)
            const gray = 0.2989 * r + 0.5870 * g + 0.1140 * bl;
            r = gray + satFactor * (r - gray);
            g = gray + satFactor * (g - gray);
            bl = gray + satFactor * (bl - gray);
            
            // Clamp
            data[i] = Math.max(0, Math.min(255, r));
            data[i+1] = Math.max(0, Math.min(255, g));
            data[i+2] = Math.max(0, Math.min(255, bl));
         }}
         
         ctx.putImageData(imageData, 0, 0);
      }}
      
      // 3. Export to Blob/DataURL
      const link = document.createElement('a');
      link.download = 'edited-image.png';
      link.href = canvas.toDataURL('image/png', 1.0);
      link.click();
    }}
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Upgraded Image Editor for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'image-editor'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_image_editor(lang))
        
        print(f"✅ Created: {lang}/image-editor/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Image Editor for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

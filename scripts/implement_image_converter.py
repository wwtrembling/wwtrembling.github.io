"""
Create Image Converter implementation for all languages.
Uses Canvas API for resize and WebP conversion.
"""

import os
import re

base_dir = r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf'

# Read Korean unit-converter as template for structure
template_path = os.path.join(base_dir, 'ko', 'unit-converter', 'index.html')
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Extract head section for SEO structure
head_end = template.find('</head>')
head_section = template[:head_end]

# Image Converter HTML template
image_converter_template = '''<!DOCTYPE html>
<html lang="{lang}">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">

  <!-- Open Graph -->
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utilifyapp.net/{lang}/image-converter/">

  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/image-converter/">

  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/image-converter/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/image-converter/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/image-converter/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/image-converter/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/image-converter/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/image-converter/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/image-converter/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/image-converter/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/image-converter/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/image-converter/">

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
    "name": "{app_name}",
    "description": "{description}",
    "url": "https://utilifyapp.net/{lang}/image-converter/",
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
    .upload-area {{
      border: 2px dashed var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-xl);
      text-align: center;
      cursor: pointer;
      transition: all var(--transition-fast);
      background: var(--bg-secondary);
    }}

    .upload-area:hover {{
      border-color: var(--primary-color);
      background: var(--bg-primary);
    }}

    .upload-area.dragover {{
      border-color: var(--primary-color);
      background: rgba(102, 126, 234, 0.1);
    }}

    .preview-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--spacing-lg);
      margin-top: var(--spacing-lg);
    }}

    .preview-box {{
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: var(--spacing-md);
      background: var(--bg-primary);
    }}

    .preview-box h3 {{
      margin-bottom: var(--spacing-md);
      color: var(--text-primary);
    }}

    .preview-box img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-sm);
    }}

    .controls {{
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: var(--spacing-lg);
      margin-top: var(--spacing-lg);
    }}

    .control-group {{
      margin-bottom: var(--spacing-md);
    }}

    .slider-container {{
      display: flex;
      align-items: center;
      gap: var(--spacing-md);
    }}

    .slider-container input[type="range"] {{
      flex: 1;
    }}

    .slider-value {{
      min-width: 60px;
      text-align: right;
      font-weight: 600;
      color: var(--primary-color);
    }}

    .button-group {{
      display: flex;
      gap: var(--spacing-md);
      margin-top: var(--spacing-lg);
    }}

    .btn {{
      flex: 1;
      padding: var(--spacing-md) var(--spacing-lg);
      border: none;
      border-radius: var(--radius-md);
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .btn-primary {{
      background: var(--primary-color);
      color: white;
    }}

    .btn-primary:hover {{
      background: var(--primary-dark);
      transform: translateY(-2px);
    }}

    .btn-secondary {{
      background: var(--bg-secondary);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
    }}

    .btn-secondary:hover {{
      background: var(--bg-primary);
    }}

    .info-text {{
      font-size: 0.875rem;
      color: var(--text-secondary);
      margin-top: var(--spacing-sm);
    }}

    @media (max-width: 768px) {{
      .preview-container {{
        grid-template-columns: 1fr;
      }}

      .button-group {{
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
      <h1>🖼️ {h1}</h1>
      <p>{subtitle}</p>

      <!-- Upload Area -->
      <div class="upload-area" id="uploadArea">
        <input type="file" id="fileInput" accept="image/*" style="display: none;">
        <div>
          <p style="font-size: 3rem; margin: 0;">📁</p>
          <p style="font-size: 1.25rem; font-weight: 600; margin: var(--spacing-md) 0;">{upload_text}</p>
          <p class="info-text">{upload_hint}</p>
        </div>
      </div>

      <!-- Controls -->
      <div class="controls" id="controls" style="display: none;">
        <div class="control-group">
          <label class="form-label">{width_label}</label>
          <div class="slider-container">
            <input type="range" id="widthSlider" min="100" max="4000" value="1920">
            <span class="slider-value" id="widthValue">1920px</span>
          </div>
        </div>

        <div class="control-group">
          <label class="form-label">{height_label}</label>
          <div class="slider-container">
            <input type="range" id="heightSlider" min="100" max="4000" value="1080">
            <span class="slider-value" id="heightValue">1080px</span>
          </div>
        </div>

        <div class="control-group">
          <label class="form-label">{format_label}</label>
          <select id="formatSelect" class="form-select">
            <option value="image/webp">WebP</option>
            <option value="image/jpeg">JPEG</option>
            <option value="image/png">PNG</option>
          </select>
        </div>

        <div class="control-group">
          <label class="form-label">{quality_label}</label>
          <div class="slider-container">
            <input type="range" id="qualitySlider" min="1" max="100" value="90">
            <span class="slider-value" id="qualityValue">90%</span>
          </div>
        </div>

        <div class="button-group">
          <button class="btn btn-primary" id="convertBtn">{convert_btn}</button>
          <button class="btn btn-secondary" id="resetBtn">{reset_btn}</button>
        </div>
      </div>

      <!-- Preview -->
      <div class="preview-container" id="previewContainer" style="display: none;">
        <div class="preview-box">
          <h3>{original_label}</h3>
          <img id="originalPreview" alt="Original">
          <p class="info-text" id="originalInfo"></p>
        </div>
        <div class="preview-box">
          <h3>{converted_label}</h3>
          <img id="convertedPreview" alt="Converted">
          <p class="info-text" id="convertedInfo"></p>
          <button class="btn btn-primary" id="downloadBtn" style="margin-top: var(--spacing-md); width: 100%;">{download_btn}</button>
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
    let originalImage = null;
    let originalFile = null;

    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const controls = document.getElementById('controls');
    const previewContainer = document.getElementById('previewContainer');
    const widthSlider = document.getElementById('widthSlider');
    const heightSlider = document.getElementById('heightSlider');
    const qualitySlider = document.getElementById('qualitySlider');
    const formatSelect = document.getElementById('formatSelect');
    const widthValue = document.getElementById('widthValue');
    const heightValue = document.getElementById('heightValue');
    const qualityValue = document.getElementById('qualityValue');
    const originalPreview = document.getElementById('originalPreview');
    const convertedPreview = document.getElementById('convertedPreview');
    const originalInfo = document.getElementById('originalInfo');
    const convertedInfo = document.getElementById('convertedInfo');
    const convertBtn = document.getElementById('convertBtn');
    const resetBtn = document.getElementById('resetBtn');
    const downloadBtn = document.getElementById('downloadBtn');

    // Upload area click
    uploadArea.addEventListener('click', () => fileInput.click());

    // Drag and drop
    uploadArea.addEventListener('dragover', (e) => {{
      e.preventDefault();
      uploadArea.classList.add('dragover');
    }});

    uploadArea.addEventListener('dragleave', () => {{
      uploadArea.classList.remove('dragover');
    }});

    uploadArea.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadArea.classList.remove('dragover');
      const files = e.dataTransfer.files;
      if (files.length > 0) handleFile(files[0]);
    }});

    // File input change
    fileInput.addEventListener('change', (e) => {{
      if (e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    // Handle file
    function handleFile(file) {{
      if (!file.type.startsWith('image/')) {{
        alert('{error_not_image}');
        return;
      }}

      originalFile = file;
      const reader = new FileReader();
      reader.onload = (e) => {{
        const img = new Image();
        img.onload = () => {{
          originalImage = img;
          widthSlider.value = img.width;
          heightSlider.value = img.height;
          widthSlider.max = img.width * 2;
          heightSlider.max = img.height * 2;
          updateSliderValues();
          
          originalPreview.src = e.target.result;
          originalInfo.textContent = `${{img.width}} × ${{img.height}}px, ${{formatFileSize(file.size)}}`;
          
          controls.style.display = 'block';
          previewContainer.style.display = 'grid';
        }};
        img.src = e.target.result;
      }};
      reader.readAsDataURL(file);
    }}

    // Update slider values
    function updateSliderValues() {{
      widthValue.textContent = widthSlider.value + 'px';
      heightValue.textContent = heightSlider.value + 'px';
      qualityValue.textContent = qualitySlider.value + '%';
    }}

    widthSlider.addEventListener('input', updateSliderValues);
    heightSlider.addEventListener('input', updateSliderValues);
    qualitySlider.addEventListener('input', updateSliderValues);

    // Convert image
    convertBtn.addEventListener('click', () => {{
      if (!originalImage) return;

      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      
      canvas.width = parseInt(widthSlider.value);
      canvas.height = parseInt(heightSlider.value);
      
      ctx.drawImage(originalImage, 0, 0, canvas.width, canvas.height);
      
      const format = formatSelect.value;
      const quality = parseInt(qualitySlider.value) / 100;
      
      canvas.toBlob((blob) => {{
        const url = URL.createObjectURL(blob);
        convertedPreview.src = url;
        convertedInfo.textContent = `${{canvas.width}} × ${{canvas.height}}px, ${{formatFileSize(blob.size)}}`;
        
        downloadBtn.onclick = () => {{
          const a = document.createElement('a');
          a.href = url;
          const ext = format.split('/')[1];
          a.download = `converted.${{ext}}`;
          a.click();
        }};
      }}, format, quality);
    }});

    // Reset
    resetBtn.addEventListener('click', () => {{
      originalImage = null;
      originalFile = null;
      fileInput.value = '';
      controls.style.display = 'none';
      previewContainer.style.display = 'none';
    }});

    // Format file size
    function formatFileSize(bytes) {{
      if (bytes < 1024) return bytes + ' B';
      if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + ' KB';
      return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
    }}
  </script>
</body>

</html>'''

# Language configurations
languages = {{
    'ko': {{
        'title': '이미지 변환기 - Tool Shelf',
        'description': '이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요. 브라우저에서 바로 처리됩니다.',
        'og_title': '이미지 변환기 - Tool Shelf',
        'og_description': '이미지 크기를 조정하고 다양한 형식으로 변환하세요.',
        'app_name': '이미지 변환기',
        'h1': '이미지 변환기',
        'subtitle': '이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요.',
        'upload_text': '이미지를 클릭하거나 드래그하여 업로드',
        'upload_hint': 'JPG, PNG, GIF, WebP 등 모든 이미지 형식 지원',
        'width_label': '너비',
        'height_label': '높이',
        'format_label': '출력 형식',
        'quality_label': '품질',
        'convert_btn': '변환하기',
        'reset_btn': '초기화',
        'original_label': '원본 이미지',
        'converted_label': '변환된 이미지',
        'download_btn': '다운로드',
        'error_not_image': '이미지 파일만 업로드할 수 있습니다.'
    }},
    'en': {{
        'title': 'Image Converter - Tool Shelf',
        'description': 'Resize images and convert to WebP, JPEG, PNG formats. Process directly in your browser.',
        'og_title': 'Image Converter - Tool Shelf',
        'og_description': 'Resize images and convert to various formats.',
        'app_name': 'Image Converter',
        'h1': 'Image Converter',
        'subtitle': 'Resize images and convert to WebP, JPEG, PNG formats.',
        'upload_text': 'Click or drag image to upload',
        'upload_hint': 'Supports all image formats: JPG, PNG, GIF, WebP, etc.',
        'width_label': 'Width',
        'height_label': 'Height',
        'format_label': 'Output Format',
        'quality_label': 'Quality',
        'convert_btn': 'Convert',
        'reset_btn': 'Reset',
        'original_label': 'Original Image',
        'converted_label': 'Converted Image',
        'download_btn': 'Download',
        'error_not_image': 'Please upload an image file only.'
    }}
}}

# Create for all 9 languages (ko and en have custom translations, others use English)
all_langs = ['ko', 'en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']

for lang in all_langs:
    config = languages.get(lang, languages['en'])
    
    html = image_converter_template.format(
        lang=lang,
        **config
    )
    
    output_path = os.path.join(base_dir, lang, 'image-converter', 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Created {{lang}}/image-converter/index.html")

print("\n🎉 All Image Converter pages created!")

print("Image Converter implementation complete. Now removing PDF Tools...")

# Remove PDF Tools directories
import shutil

for lang in all_langs:
    pdf_tools_path = os.path.join(base_dir, lang, 'pdf-tools')
    if os.path.exists(pdf_tools_path):
        shutil.rmtree(pdf_tools_path)
        print(f"🗑️ Removed {lang}/pdf-tools/")

print("\n✅ PDF Tools removed from all languages!")

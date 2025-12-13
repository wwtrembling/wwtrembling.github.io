"""
Update Color Converter UI/UX: Compact Layout, Click-to-Copy, Sync Logic
"""

import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent

# Translations reused from copy_color_converter.py + slight additions if needed
TRANSLATIONS = {
    'ko': {'title': '색상 변환기', 'desc': 'HEX, RGB, HSL 색상 형식 간 변환 및 실시간 미리보기.', 'formats_title': '색상 값', 'copy_btn': '복사', 'sliders_title': 'RGB 조절', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': '인기 색상', 'ad_text': '광고 영역', 'copied_msg': '복사됨!'},
    'en': {'title': 'Color Converter', 'desc': 'Convert between HEX, RGB, HSL color formats.', 'formats_title': 'Color Values', 'copy_btn': 'Copy', 'sliders_title': 'RGB Adjust', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'Popular Colors', 'ad_text': 'Ad Space', 'copied_msg': 'Copied!'},
    'ja': {'title': 'カラーコンバーター', 'desc': 'HEX、RGB、HSLカラー形式間で変換します。', 'formats_title': 'カラー値', 'copy_btn': 'コピー', 'sliders_title': 'RGB調整', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': '人気の色', 'ad_text': '広告スペース', 'copied_msg': 'コピーしました！'},
    'hi': {'title': 'रंग कनवर्टर', 'desc': 'HEX, RGB और HSL रंग प्रारूपों के बीच बदलें।', 'formats_title': 'रंग मान', 'copy_btn': 'कॉपी', 'sliders_title': 'RGB समायोजन', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'लोकप्रिय रंग', 'ad_text': 'विज्ञापन स्थान', 'copied_msg': 'कॉपी किया गया!'},
    'id': {'title': 'Konverter Warna', 'desc': 'Konversi antara format warna HEX, RGB, dan HSL.', 'formats_title': 'Nilai Warna', 'copy_btn': 'Salin', 'sliders_title': 'Penyesuaian RGB', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'Warna Populer', 'ad_text': 'Ruang Iklan', 'copied_msg': 'Disalin!'},
    'vi': {'title': 'Chuyển Đổi Màu', 'desc': 'Chuyển đổi giữa các định dạng màu HEX, RGB và HSL.', 'formats_title': 'Giá Trị Màu', 'copy_btn': 'Sao chép', 'sliders_title': 'Điều Chỉnh RGB', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'Màu Phổ Biến', 'ad_text': 'Không Gian Quảng Cáo', 'copied_msg': 'Đã sao chép!'},
    'th': {'title': 'ตัวแปลงสี', 'desc': 'แปลงระหว่างรูปแบบสี HEX, RGB และ HSL', 'formats_title': 'ค่าสี', 'copy_btn': 'คัดลอก', 'sliders_title': 'ปรับ RGB', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'สียอดนิยม', 'ad_text': 'พื้นที่โฆษณา', 'copied_msg': 'คัดลอกแล้ว!'},
    'de': {'title': 'Farbkonverter', 'desc': 'Konvertieren zwischen HEX-, RGB- und HSL-Farbformaten.', 'formats_title': 'Farbwerte', 'copy_btn': 'Kopieren', 'sliders_title': 'RGB-Anpassung', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'Beliebte Farben', 'ad_text': 'Werbefläche', 'copied_msg': 'Kopiert!'},
    'pt': {'title': 'Conversor de Cores', 'desc': 'Converta entre formatos de cores HEX, RGB e HSL.', 'formats_title': 'Valores de Cor', 'copy_btn': 'Copiar', 'sliders_title': 'Ajuste RGB', 'red': 'R', 'green': 'G', 'blue': 'B', 'popular_title': 'Cores Populares', 'ad_text': 'Espaço Publicitário', 'copied_msg': 'Copiado!'}
}

# New HTML Template with Compact Layout
# Using Grid: Top (Preview), Bottom Left (Inputs), Bottom Right (Sliders/Palette) or
# Left (Preview + Sliders), Right (Inputs)
# User asked for: "Top color area is too big, layout is not efficient."
# Let's try:
# ------------------------------
# [       Color Preview        ] (Click to Copy) - Reduced Height
# ------------------------------
# [ HEX Input ] [ RGB Sliders  ]
# [ RGB Input ] [              ]
# [ HSL Input ] [ Palette Grid ]
# ------------------------------

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6334819180242631">
  <title>{title} - Utilify</title>
  <meta name="description" content="{desc}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title} - Utilify">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://utilifyapp.net/{lang}/color-converter/">

  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/color-converter/">

  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/color-converter/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/color-converter/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/color-converter/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/color-converter/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/color-converter/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/color-converter/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/color-converter/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/color-converter/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/color-converter/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/color-converter/">

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
    "name": "{title}",
    "description": "{desc}",
    "url": "https://utilifyapp.net/{lang}/color-converter/",
    "inLanguage": "{lang}",
    "applicationCategory": "UtilitiesApplication"
  }}
  </script>

  <style>
    /* Compact Layout Styles */
    .converter-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }}
    
    @media (min-width: 768px) {{
      .converter-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .color-preview-container {{
      grid-column: 1 / -1; /* Full width on top */
      margin-bottom: 0.5rem;
    }}

    .color-preview {{
      width: 100%;
      height: 120px; /* Reduced height */
      border-radius: var(--radius-lg);
      border: 2px solid var(--border-color);
      box-shadow: var(--shadow-md);
      cursor: pointer;
      position: relative;
      transition: transform 0.1s;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    
    .color-preview:active {{
      transform: scale(0.98);
    }}
    
    .color-preview::after {{
      content: '{copy_btn} HEX';
      background: rgba(0,0,0,0.6);
      color: white;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.9rem;
      opacity: 0;
      transition: opacity 0.2s;
    }}
    
    .color-preview:hover::after {{
      opacity: 1;
    }}

    .input-section {{
      background: var(--bg-secondary);
      padding: 1.5rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
    }}

    .slider-section {{
      background: var(--bg-secondary);
      padding: 1.5rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
    }}

    .color-input-row {{
      margin-bottom: 1rem;
      display: flex;
      gap: 0.5rem;
      align-items: center;
    }}
    
    .color-input-row label {{
      width: 40px;
      font-weight: 600;
      color: var(--text-secondary);
    }}
    
    .color-input-row input {{
      flex: 1;
      font-family: monospace;
      font-size: 1rem;
    }}

    .copy-icon-btn {{
      background: none;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      cursor: pointer;
      padding: 6px;
      color: var(--text-secondary);
      transition: all 0.2s;
    }}
    
    .copy-icon-btn:hover {{
      background: var(--primary-color);
      color: white;
      border-color: var(--primary-color);
    }}

    .slider-row {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    
    .slider-label {{
      width: 20px;
      font-weight: bold;
    }}
    
    .slider-input {{
      flex: 1;
      height: 6px;
      border-radius: 3px;
      -webkit-appearance: none;
      cursor: pointer;
    }}
    
    .slider-val {{
      width: 30px;
      text-align: right;
      font-variant-numeric: tabular-nums;
    }}

    /* Slider Colors */
    #rSlider {{ background: linear-gradient(90deg, #000, #f00); }}
    #gSlider {{ background: linear-gradient(90deg, #000, #0f0); }}
    #bSlider {{ background: linear-gradient(90deg, #000, #00f); }}

    .palette-grid {{
      display: grid;
      grid-template-columns: repeat(8, 1fr); /* More swatches per row */
      gap: 8px;
      margin-top: 1rem;
    }}

    .swatch {{
      aspect-ratio: 1;
      border-radius: var(--radius-md);
      cursor: pointer;
      border: 1px solid rgba(0,0,0,0.1);
      transition: transform 0.1s;
    }}
    
    .swatch:hover {{
      transform: scale(1.15);
      z-index: 2;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }}
  </style>
  
  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631" crossorigin="anonymous"></script>
</head>

<body>
  <header class="site-header">
    <div class="container">
      <div class="header-content">
        <a href="/{lang}/" class="site-logo">🛠️ Utilify</a>
      </div>
    </div>
  </header>

  <main class="main-content">
    <div class="container-narrow">
      <h1>🎨 {title}</h1>
      <p>{desc}</p>
      
      <div class="converter-grid">
        <!-- Top: Preview -->
        <div class="color-preview-container">
          <div id="colorPreview" class="color-preview" title="{copy_btn} HEX" onclick="copyHexFromPreview()"></div>
        </div>

        <!-- Left: Inputs -->
        <div class="input-section">
          <h3>{formats_title}</h3>
          
          <div class="color-input-row">
            <label>HEX</label>
            <input type="text" id="hexInput" class="form-input" value="#6366f1" placeholder="#000000" spellcheck="false">
            <button class="copy-icon-btn" onclick="copyColor('hex')" title="{copy_btn}">📋</button>
          </div>
          
          <div class="color-input-row">
            <label>RGB</label>
            <input type="text" id="rgbInput" class="form-input" readonly>
            <button class="copy-icon-btn" onclick="copyColor('rgb')" title="{copy_btn}">📋</button>
          </div>
          
          <div class="color-input-row">
            <label>HSL</label>
            <input type="text" id="hslInput" class="form-input" readonly>
            <button class="copy-icon-btn" onclick="copyColor('hsl')" title="{copy_btn}">📋</button>
          </div>
        </div>

        <!-- Right: Sliders & Palette -->
        <div class="slider-section">
          <h3>{sliders_title}</h3>
          
          <div class="slider-row">
            <span class="slider-label" style="color: #ef4444">{red}</span>
            <input type="range" id="rSlider" class="slider-input" min="0" max="255" value="99">
            <span id="rValue" class="slider-val">99</span>
          </div>
          
          <div class="slider-row">
            <span class="slider-label" style="color: #22c55e">{green}</span>
            <input type="range" id="gSlider" class="slider-input" min="0" max="255" value="102">
            <span id="gValue" class="slider-val">102</span>
          </div>
          
          <div class="slider-row">
            <span class="slider-label" style="color: #3b82f6">{blue}</span>
            <input type="range" id="bSlider" class="slider-input" min="0" max="255" value="241">
            <span id="bValue" class="slider-val">241</span>
          </div>

          <h3 style="margin-top: 1.5rem; font-size: 0.95rem;">{popular_title}</h3>
          <div id="paletteGrid" class="palette-grid"></div>
        </div>
      </div>

       <!-- Related Tools Injection Point (We need to preserve this if it existed, but we are overwriting. 
           We should auto-inject it again or just hardcode it for now since we have the logic in the other script. 
           Actually, the user asked to FIX styling, so reusing the generation script pattern is best. 
           I will Re-inject simple links here using the same logic as inject_internal_links if I can, 
           or just leave a placeholder and run the injection script again?
           Running injection script again is safer and cleaner.)
       -->
       <!-- Placeholder for re-injection -->
       <div style="margin-top: 2rem;"></div>

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
  <script>
    // Logic
    const popularColors = [
      '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2',
      '#F8B739', '#52B788', '#E63946', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557', '#264653'
    ];

    const els = {{
      preview: document.getElementById('colorPreview'),
      hex: document.getElementById('hexInput'),
      rgb: document.getElementById('rgbInput'),
      hsl: document.getElementById('hslInput'),
      r: document.getElementById('rSlider'),
      g: document.getElementById('gSlider'),
      b: document.getElementById('bSlider'),
      rv: document.getElementById('rValue'),
      gv: document.getElementById('gValue'),
      bv: document.getElementById('bValue'),
      palette: document.getElementById('paletteGrid')
    }};

    function rgbToHex(r, g, b) {{
      return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
    }}

    function hexToRgb(hex) {{
      const result = /^#?([a-f\d]{{2}})([a-f\d]{{2}})([a-f\d]{{2}})$/i.exec(hex);
      return result ? {{
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
      }} : null;
    }}

    function rgbToHsl(r, g, b) {{
      r /= 255; g /= 255; b /= 255;
      const max = Math.max(r, g, b), min = Math.min(r, g, b);
      let h, s, l = (max + min) / 2;
      if (max === min) {{ h = s = 0; }} 
      else {{
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {{
          case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
          case g: h = ((b - r) / d + 2) / 6; break;
          case b: h = ((r - g) / d + 4) / 6; break;
        }}
      }}
      return {{ h: Math.round(h * 360), s: Math.round(s * 100), l: Math.round(l * 100) }};
    }}

    function updateFromSliders() {{
      const r = parseInt(els.r.value);
      const g = parseInt(els.g.value);
      const b = parseInt(els.b.value);
      
      updateAll(r, g, b, 'sliders');
    }}

    function updateFromHex() {{
      let hex = els.hex.value;
      if(!hex.startsWith('#')) hex = '#' + hex;
      
      // Basic validation
      if(/^#[0-9A-F]{{6}}$/i.test(hex)) {{
        const rgb = hexToRgb(hex);
        if(rgb) updateAll(rgb.r, rgb.g, rgb.b, 'hex');
      }}
    }}

    function updateAll(r, g, b, source) {{
      // Update Sliders if not source
      if(source !== 'sliders') {{
        els.r.value = r; els.g.value = g; els.b.value = b;
      }}
      
      // Update Values
      els.rv.textContent = r;
      els.gv.textContent = g;
      els.bv.textContent = b;
      
      // Update Inputs
      const hex = rgbToHex(r, g, b);
      if(source !== 'hex') els.hex.value = hex;
      
      els.rgb.value = `rgb(${{r}}, ${{g}}, ${{b}})`;
      
      const hsl = rgbToHsl(r, g, b);
      els.hsl.value = `hsl(${{hsl.h}}, ${{hsl.s}}%, ${{hsl.l}}%)`;
      
      // Update Preview
      els.preview.style.backgroundColor = hex;
    }}

    function copyColor(type) {{
      let val = '';
      if(type === 'hex') val = els.hex.value;
      if(type === 'rgb') val = els.rgb.value;
      if(type === 'hsl') val = els.hsl.value;
      if(val) Utils.copyToClipboard(val);
    }}
    
    function copyHexFromPreview() {{
       const val = els.hex.value;
       if(val) {{
          Utils.copyToClipboard(val);
          // Simple feedback (could use toast, but existing Utils might handle it)
          // Let's perform a small visual feedback on the preview box
          els.preview.style.transform = 'scale(0.95)';
          setTimeout(() => els.preview.style.transform = 'scale(1)', 100);
       }}
    }}

    // Init Palette
    popularColors.forEach(c => {{
      const div = document.createElement('div');
      div.className = 'swatch';
      div.style.backgroundColor = c;
      div.title = c;
      div.onclick = () => {{
        els.hex.value = c;
        updateFromHex();
      }};
      els.palette.appendChild(div);
    }});

    // Listeners
    els.r.addEventListener('input', updateFromSliders);
    els.g.addEventListener('input', updateFromSliders);
    els.b.addEventListener('input', updateFromSliders);
    els.hex.addEventListener('input', updateFromHex);

    // Initial Trigger
    updateFromSliders();
  </script>
</body>
</html>
'''

def generate_file(lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    # Safe fallback if key missing
    if lang not in TRANSLATIONS:
         t = TRANSLATIONS['en']
         
    # Format
    html = HTML_TEMPLATE.format(
        lang=lang,
        title=t['title'],
        desc=t['desc'],
        formats_title=t['formats_title'],
        copy_btn=t['copy_btn'],
        sliders_title=t['sliders_title'],
        red=t['red'],
        green=t['green'],
        blue=t['blue'],
        popular_title=t['popular_title'],
        copied_msg=t.get('copied_msg', 'Copied!')
    )
    return html

def main():
    print("🚀 Updating Color Converter UI across all languages...")
    for lang in TRANSLATIONS.keys():
        path = BASE_DIR / lang / 'color-converter' / 'index.html'
        if not path.parent.exists():
            print(f"⚠️ Skipping {lang} (dir not found)")
            continue
            
        content = generate_file(lang)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {lang}")
    
    print("\n✨ UI Update Complete. (Don't forget to run injection script for internal links again if needed)")

if __name__ == '__main__':
    main()

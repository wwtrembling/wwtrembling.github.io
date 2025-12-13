"""
Create fully functional Reaction Speed Test for all 9 languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TRANSLATIONS = {
    'ko': {
        'title': '반응 속도 테스트',
        'desc': '당신의 반응 속도는 얼마입니까? 화면이 초록색으로 바뀔 때 최대한 빨리 클릭하세요!',
        'instruction_start': '화면을 클릭하여 시작하세요.',
        'instruction_wait': '초록색이 될 때까지 기다리세요...',
        'instruction_click': '클릭하세요!',
        'result_prefix': '당신의 기록:',
        'result_suffix': 'ms',
        'too_soon': '너무 빨라요! 파란색 화면을 클릭해서 다시 시도하세요.',
        'play_again': '다시 하기',
        'rank_top': '상위 1% 수준입니다! 🏆',
        'rank_good': '훌륭한 반응 속도입니다! 🚀',
        'rank_avg': '평균적인 반응 속도입니다. 👌',
        'rank_slow': '조금 더 집중해보세요! 🐢',
        'ad_text': '광고 영역'
    },
    'en': {
        'title': 'Reaction Speed Test',
        'desc': 'Test your reaction time. Click as fast as you can when the screen turns green!',
        'instruction_start': 'Click anywhere to Start.',
        'instruction_wait': 'Wait for Green...',
        'instruction_click': 'CLICK!',
        'result_prefix': 'Your Time:',
        'result_suffix': 'ms',
        'too_soon': 'Too Soon! Click to try again.',
        'play_again': 'Play Again',
        'rank_top': 'Godlike Reflexes! 🏆',
        'rank_good': 'Great Speed! 🚀',
        'rank_avg': 'Average Speed. 👌',
        'rank_slow': 'Focus! You can do better. 🐢',
        'ad_text': 'Ad Space'
    },
    'ja': {
        'title': '反応速度テスト',
        'desc': 'あなたの反応速度をテストします。画面が緑色になったらできるだけ早くクリックしてください！',
        'instruction_start': 'クリックしてスタート',
        'instruction_wait': '緑色になるまで待って...',
        'instruction_click': 'クリック！',
        'result_prefix': '記録:',
        'result_suffix': 'ms',
        'too_soon': '早すぎます！クリックしてリトライ。',
        'play_again': 'もう一度',
        'rank_top': '神レベルの反射神経！ 🏆',
        'rank_good': '素晴らしい速さ！ 🚀',
        'rank_avg': '平均的です。 👌',
        'rank_slow': '集中して！ 🐢',
        'ad_text': '広告スペース'
    },
    'hi': {
        'title': 'प्रतिक्रिया गति परीक्षण',
        'desc': 'अपनी प्रतिक्रिया समय का परीक्षण करें। स्क्रीन हरी होने पर जितनी जल्दी हो सके क्लिक करें!',
        'instruction_start': 'शुरू करने के लिए क्लिक करें।',
        'instruction_wait': 'हरे रंग का इंतजार करें...',
        'instruction_click': 'क्लिक करें!',
        'result_prefix': 'आपका समय:',
        'result_suffix': 'ms',
        'too_soon': 'बहुत जल्दी! फिर से प्रयास करने के लिए क्लिक करें।',
        'play_again': 'पुनः प्रयास करें',
        'rank_top': 'अद्भुत सजगता! 🏆',
        'rank_good': 'बहुत बढ़िया! 🚀',
        'rank_avg': 'औसत गति। 👌',
        'rank_slow': 'ध्यान दें! 🐢',
        'ad_text': 'विज्ञापन स्थान'
    },
    'id': {
        'title': 'Tes Kecepatan Reaksi',
        'desc': 'Uji waktu reaksi Anda. Klik secepat mungkin saat layar berubah menjadi hijau!',
        'instruction_start': 'Klik untuk Mulai.',
        'instruction_wait': 'Tunggu Hijau...',
        'instruction_click': 'KLIK!',
        'result_prefix': 'Waktu Anda:',
        'result_suffix': 'ms',
        'too_soon': 'Terlalu Cepat! Klik untuk mencoba lagi.',
        'play_again': 'Main Lagi',
        'rank_top': 'Refleks Dewa! 🏆',
        'rank_good': 'Kecepatan Hebat! 🚀',
        'rank_avg': 'Rata-rata. 👌',
        'rank_slow': 'Fokus! 🐢',
        'ad_text': 'Ruang Iklan'
    },
    'vi': {
        'title': 'Kiểm Tra Tốc Độ Phản Xạ',
        'desc': 'Kiểm tra thời gian phản xạ của bạn. Nhấp nhanh nhất có thể khi màn hình chuyển sang màu xanh!',
        'instruction_start': 'Nhấp để bắt đầu.',
        'instruction_wait': 'Chờ màu xanh...',
        'instruction_click': 'NHẤP NGAY!',
        'result_prefix': 'Thời gian:',
        'result_suffix': 'ms',
        'too_soon': 'Quá sớm! Nhấp để thử lại.',
        'play_again': 'Chơi lại',
        'rank_top': 'Phản xạ thần thánh! 🏆',
        'rank_good': 'Tốc độ tuyệt vời! 🚀',
        'rank_avg': 'Tốc độ trung bình. 👌',
        'rank_slow': 'Tập trung nào! 🐢',
        'ad_text': 'Không Gian Quảng Cáo'
    },
    'th': {
        'title': 'ทดสอบความเร็วปฏิกิริยา',
        'desc': 'ทดสอบเวลาปฏิกิริยาของคุณ คลิกให้เร็วที่สุดเมื่อหน้าจอเปลี่ยนเป็นสีเขียว!',
        'instruction_start': 'คลิกเพื่อเริ่ม',
        'instruction_wait': 'รอสีเขียว...',
        'instruction_click': 'คลิกเลย!',
        'result_prefix': 'เวลาของคุณ:',
        'result_suffix': 'ms',
        'too_soon': 'เร็วเกินไป! คลิกเพื่อลองใหม่',
        'play_again': 'เล่นอีกครั้ง',
        'rank_top': 'ปฏิกิริยาขั้นเทพ! 🏆',
        'rank_good': 'ยอดเยี่ยม! 🚀',
        'rank_avg': 'ปานกลาง 👌',
        'rank_slow': 'มีสมาธิหน่อย! 🐢',
        'ad_text': 'พื้นที่โฆษณา'
    },
    'de': {
        'title': 'Reaktionszeittest',
        'desc': 'Testen Sie Ihre Reaktionszeit. Klicken Sie so schnell wie möglich, wenn der Bildschirm grün wird!',
        'instruction_start': 'Klicken zum Starten.',
        'instruction_wait': 'Warten auf Grün...',
        'instruction_click': 'KLICKEN!',
        'result_prefix': 'Ihre Zeit:',
        'result_suffix': 'ms',
        'too_soon': 'Zu früh! Klicken für Neustart.',
        'play_again': 'Nochmal spielen',
        'rank_top': 'Göttliche Reflexe! 🏆',
        'rank_good': 'Super schnell! 🚀',
        'rank_avg': 'Durchschnitt. 👌',
        'rank_slow': 'Konzentrieren! 🐢',
        'ad_text': 'Werbefläche'
    },
    'pt': {
        'title': 'Teste de Tempo de Reação',
        'desc': 'Teste seu tempo de reação. Clique o mais rápido possível quando a tela ficar verde!',
        'instruction_start': 'Clique para Começar.',
        'instruction_wait': 'Aguarde o Verde...',
        'instruction_click': 'CLIQUE!',
        'result_prefix': 'Seu Tempo:',
        'result_suffix': 'ms',
        'too_soon': 'Muito cedo! Clique para tentar novamente.',
        'play_again': 'Jogar Novamente',
        'rank_top': 'Reflexos Divinos! 🏆',
        'rank_good': 'Ótima Velocidade! 🚀',
        'rank_avg': 'Média. 👌',
        'rank_slow': 'Concentre-se! 🐢',
        'ad_text': 'Espaço Publicitário'
    }
}

def generate_reaction_test(lang):
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
  <meta property="og:url" content="https://utilifyapp.net/{lang}/reaction-test/">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://utilifyapp.net/{lang}/reaction-test/">
  
  <!-- Language Alternatives -->
  <link rel="alternate" hreflang="ko" href="https://utilifyapp.net/ko/reaction-test/">
  <link rel="alternate" hreflang="en" href="https://utilifyapp.net/en/reaction-test/">
  <link rel="alternate" hreflang="ja" href="https://utilifyapp.net/ja/reaction-test/">
  <link rel="alternate" hreflang="hi" href="https://utilifyapp.net/hi/reaction-test/">
  <link rel="alternate" hreflang="id" href="https://utilifyapp.net/id/reaction-test/">
  <link rel="alternate" hreflang="vi" href="https://utilifyapp.net/vi/reaction-test/">
  <link rel="alternate" hreflang="th" href="https://utilifyapp.net/th/reaction-test/">
  <link rel="alternate" hreflang="de" href="https://utilifyapp.net/de/reaction-test/">
  <link rel="alternate" hreflang="pt" href="https://utilifyapp.net/pt/reaction-test/">
  <link rel="alternate" hreflang="x-default" href="https://utilifyapp.net/en/reaction-test/">
  
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
    "url": "https://utilifyapp.net/{lang}/reaction-test/",
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
    .game-area {{
      height: 400px;
      border-radius: var(--radius-lg);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: white;
      font-size: 2rem;
      font-weight: 700;
      cursor: pointer;
      user-select: none;
      transition: background-color 0.2s;
      margin: var(--spacing-lg) 0;
      padding: var(--spacing-xl);
    }}
    
    .state-start {{
      background-color: #3b82f6; /* Blue */
    }}
    
    .state-wait {{
      background-color: #ef4444; /* Red */
    }}
    
    .state-click {{
      background-color: #22c55e; /* Green */
    }}
    
    .state-result {{
      background-color: #3b82f6; /* Blue */
    }}
    
    .result-text {{
      font-size: 4rem;
      margin-bottom: var(--spacing-md);
    }}
    
    .rank-text {{
      font-size: 1.5rem;
      opacity: 0.9;
    }}

    .sub-text {{
        font-size: 1rem; 
        font-weight: 400; 
        margin-top: 1rem; 
        opacity: 0.8;
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
    <div class="container-narrow">
      <h1>⚡ {t["title"]}</h1>
      <p>{t["desc"]}</p>
      
      <!-- AdSense Placeholder -->
      <div class="adsense-placeholder">
        <!-- AdSense Ad Unit -->
        <p>{t["ad_text"]}</p>
      </div>
      
      <div id="gameArea" class="game-area state-start">
        <div id="message">{t["instruction_start"]}</div>
      </div>
      
      <div class="card">
        <h3>Ranking</h3>
        <p>• < 200 ms: {t["rank_top"]}</p>
        <p>• 200 - 300 ms: {t["rank_good"]}</p>
        <p>• 300 - 450 ms: {t["rank_avg"]}</p>
        <p>• > 450 ms: {t["rank_slow"]}</p>
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
  <script>
    const gameArea = document.getElementById('gameArea');
    const message = document.getElementById('message');
    
    let startTime;
    let endTime;
    let timeoutId;
    let state = 'start'; // start, wait, click, result
    
    gameArea.addEventListener('mousedown', handleClick);
    gameArea.addEventListener('touchstart', (e) => {{
        e.preventDefault(); // prevent double firing
        handleClick();
    }});
    
    function handleClick() {{
      if (state === 'start' || state === 'result') {{
        startGame();
      }} else if (state === 'wait') {{
        tooSoon();
      }} else if (state === 'click') {{
        endGame();
      }}
    }}
    
    function startGame() {{
      state = 'wait';
      gameArea.className = 'game-area state-wait';
      message.textContent = '{t["instruction_wait"]}';
      
      const randomTime = Math.floor(Math.random() * 3000) + 2000; // 2-5 seconds
      timeoutId = setTimeout(() => {{
        state = 'click';
        gameArea.className = 'game-area state-click';
        message.textContent = '{t["instruction_click"]}';
        startTime = performance.now();
      }}, randomTime);
    }}
    
    function tooSoon() {{
      clearTimeout(timeoutId);
      state = 'start'; // Click to restart
      gameArea.className = 'game-area state-wait'; // Keep red
      message.innerHTML = '{t["too_soon"]}';
    }}
    
    function endGame() {{
      endTime = performance.now();
      const time = Math.round(endTime - startTime);
      state = 'result';
      
      let rankMsg = '';
      if (time < 200) rankMsg = '{t["rank_top"]}';
      else if (time < 300) rankMsg = '{t["rank_good"]}';
      else if (time < 450) rankMsg = '{t["rank_avg"]}';
      else rankMsg = '{t["rank_slow"]}';
      
      gameArea.className = 'game-area state-result';
      message.innerHTML = `
        <div class="result-text">${{time}} {t["result_suffix"]}</div>
        <div class="rank-text">${{rankMsg}}</div>
        <div class="sub-text">{t["play_again"]}</div>
      `;
    }}
  </script>
</body>
</html>
'''

def main():
    print("🚀 Creating Reaction Test for all languages...\n")
    
    for lang in TRANSLATIONS.keys():
        output_dir = BASE_DIR / lang / 'reaction-test'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generate_reaction_test(lang))
        
        print(f"✅ Created: {lang}/reaction-test/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created Reaction Test for {len(TRANSLATIONS)} languages")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

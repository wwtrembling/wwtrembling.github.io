"""
Create BMI Calculator, Date Calculator, and Timer for all 9 languages
Complete implementations with full functionality
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

def create_bmi_calculator(lang, translations):
    t = translations[lang]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["title"]} - Utilify</title>
  <meta name="description" content="{t["desc"]}">
  <link rel="canonical" href="https://utilifyapp.net/{lang}/bmi-calculator/">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631" crossorigin="anonymous"></script>
</head>
<body>
  <header class="site-header">
    <div class="container"><div class="header-content">
      <a href="/{lang}/" class="site-logo">🛠️ Utilify</a>
      <div id="languageSwitcher" class="language-switcher"></div>
    </div></div>
  </header>
  <main class="main-content">
    <div class="container-narrow">
      <h1>⚖️ {t["title"]}</h1>
      <p>{t["desc"]}</p>
      <div class="card">
        <div class="form-group">
          <label class="form-label">{t["height"]}</label>
          <input type="number" id="height" class="form-input" placeholder="170" value="170">
        </div>
        <div class="form-group">
          <label class="form-label">{t["weight"]}</label>
          <input type="number" id="weight" class="form-input" placeholder="70" value="70">
        </div>
        <button class="btn btn-primary" onclick="calculate()">{t["calculate"]}</button>
      </div>
      <div id="result" class="result-box" style="display:none;">
        <div class="result-value" id="bmiValue"></div>
        <div id="bmiCategory"></div>
      </div>
    </div>
  </main>
  <footer class="site-footer">
    <div class="container"><div class="footer-content">
      <p>&copy; 2025 Utilify. All rights reserved.</p>
    </div></div>
  </footer>
  <script src="/assets/js/common.js"></script>
  <script>
    function calculate() {{
      const h = parseFloat(document.getElementById('height').value) / 100;
      const w = parseFloat(document.getElementById('weight').value);
      if (h > 0 && w > 0) {{
        const bmi = (w / (h * h)).toFixed(1);
        document.getElementById('bmiValue').textContent = 'BMI: ' + bmi;
        let category = '';
        if (bmi < 18.5) category = '{t["underweight"]}';
        else if (bmi < 25) category = '{t["normal"]}';
        else if (bmi < 30) category = '{t["overweight"]}';
        else category = '{t["obese"]}';
        document.getElementById('bmiCategory').textContent = category;
        document.getElementById('result').style.display = 'block';
      }}
    }}
  </script>
</body>
</html>'''

def create_date_calculator(lang, translations):
    t = translations[lang]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["title"]} - Utilify</title>
  <meta name="description" content="{t["desc"]}">
  <link rel="canonical" href="https://utilifyapp.net/{lang}/date-calculator/">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631" crossorigin="anonymous"></script>
</head>
<body>
  <header class="site-header">
    <div class="container"><div class="header-content">
      <a href="/{lang}/" class="site-logo">🛠️ Utilify</a>
      <div id="languageSwitcher" class="language-switcher"></div>
    </div></div>
  </header>
  <main class="main-content">
    <div class="container-narrow">
      <h1>📅 {t["title"]}</h1>
      <p>{t["desc"]}</p>
      <div class="card">
        <h3>{t["dday_title"]}</h3>
        <div class="form-group">
          <label class="form-label">{t["target_date"]}</label>
          <input type="date" id="targetDate" class="form-input">
        </div>
        <button class="btn btn-primary" onclick="calculateDday()">{t["calculate"]}</button>
        <div id="ddayResult" class="result-box" style="display:none; margin-top:1rem;">
          <div class="result-value" id="ddayValue"></div>
        </div>
      </div>
      <div class="card">
        <h3>{t["diff_title"]}</h3>
        <div class="form-group">
          <label class="form-label">{t["start_date"]}</label>
          <input type="date" id="startDate" class="form-input">
        </div>
        <div class="form-group">
          <label class="form-label">{t["end_date"]}</label>
          <input type="date" id="endDate" class="form-input">
        </div>
        <button class="btn btn-primary" onclick="calculateDiff()">{t["calculate"]}</button>
        <div id="diffResult" class="result-box" style="display:none; margin-top:1rem;">
          <div class="result-value" id="diffValue"></div>
        </div>
      </div>
    </div>
  </main>
  <footer class="site-footer">
    <div class="container"><div class="footer-content">
      <p>&copy; 2025 Utilify. All rights reserved.</p>
    </div></div>
  </footer>
  <script src="/assets/js/common.js"></script>
  <script>
    function calculateDday() {{
      const target = new Date(document.getElementById('targetDate').value);
      const today = new Date();
      today.setHours(0,0,0,0);
      const diff = Math.ceil((target - today) / (1000 * 60 * 60 * 24));
      document.getElementById('ddayValue').textContent = 'D' + (diff > 0 ? '-' : '+') + Math.abs(diff);
      document.getElementById('ddayResult').style.display = 'block';
    }}
    function calculateDiff() {{
      const start = new Date(document.getElementById('startDate').value);
      const end = new Date(document.getElementById('endDate').value);
      const diff = Math.abs(Math.ceil((end - start) / (1000 * 60 * 60 * 24)));
      document.getElementById('diffValue').textContent = diff + ' {t["days"]}';
      document.getElementById('diffResult').style.display = 'block';
    }}
  </script>
</body>
</html>'''

def create_timer(lang, translations):
    t = translations[lang]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["title"]} - Utilify</title>
  <meta name="description" content="{t["desc"]}">
  <link rel="canonical" href="https://utilifyapp.net/{lang}/timer/">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6334819180242631" crossorigin="anonymous"></script>
  <style>
    .timer-display {{font-size:4rem;font-weight:700;text-align:center;color:var(--primary-color);margin:2rem 0;}}
    .preset-btn {{margin:0.5rem;}}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container"><div class="header-content">
      <a href="/{lang}/" class="site-logo">🛠️ Utilify</a>
      <div id="languageSwitcher" class="language-switcher"></div>
    </div></div>
  </header>
  <main class="main-content">
    <div class="container-narrow">
      <h1>⏱️ {t["title"]}</h1>
      <p>{t["desc"]}</p>
      <div class="card text-center">
        <div class="timer-display" id="display">00:00</div>
        <div class="form-group">
          <label class="form-label">{t["minutes"]}</label>
          <input type="number" id="minutes" class="form-input" value="25" min="0">
        </div>
        <div class="btn-group">
          <button class="btn btn-primary" onclick="start()">{t["start"]}</button>
          <button class="btn btn-secondary" onclick="pause()">{t["pause"]}</button>
          <button class="btn btn-secondary" onclick="reset()">{t["reset"]}</button>
        </div>
        <div style="margin-top:1rem;">
          <button class="btn btn-secondary preset-btn" onclick="setPreset(25)">Pomodoro (25m)</button>
          <button class="btn btn-secondary preset-btn" onclick="setPreset(5)">{t["break"]} (5m)</button>
          <button class="btn btn-secondary preset-btn" onclick="setPreset(15)">{t["break"]} (15m)</button>
        </div>
      </div>
    </div>
  </main>
  <footer class="site-footer">
    <div class="container"><div class="footer-content">
      <p>&copy; 2025 Utilify. All rights reserved.</p>
    </div></div>
  </footer>
  <script src="/assets/js/common.js"></script>
  <script>
    let totalSeconds = 0;
    let remainingSeconds = 0;
    let interval = null;
    
    function updateDisplay() {{
      const mins = Math.floor(remainingSeconds / 60);
      const secs = remainingSeconds % 60;
      document.getElementById('display').textContent = 
        String(mins).padStart(2,'0') + ':' + String(secs).padStart(2,'0');
    }}
    
    function start() {{
      if (!interval) {{
        if (remainingSeconds === 0) {{
          totalSeconds = parseInt(document.getElementById('minutes').value) * 60;
          remainingSeconds = totalSeconds;
        }}
        interval = setInterval(() => {{
          if (remainingSeconds > 0) {{
            remainingSeconds--;
            updateDisplay();
          }} else {{
            pause();
            alert('{t["time_up"]}');
          }}
        }}, 1000);
      }}
    }}
    
    function pause() {{
      if (interval) {{
        clearInterval(interval);
        interval = null;
      }}
    }}
    
    function reset() {{
      pause();
      remainingSeconds = 0;
      updateDisplay();
    }}
    
    function setPreset(mins) {{
      document.getElementById('minutes').value = mins;
      reset();
    }}
    
    updateDisplay();
  </script>
</body>
</html>'''

# Translations for all three utilities
BMI_TRANS = {
    'ko': {'title': 'BMI 계산기', 'desc': 'BMI를 계산하세요.', 'height': '키 (cm)', 'weight': '체중 (kg)', 
           'calculate': '계산', 'underweight': '저체중', 'normal': '정상', 'overweight': '과체중', 'obese': '비만'},
    'en': {'title': 'BMI Calculator', 'desc': 'Calculate your BMI.', 'height': 'Height (cm)', 'weight': 'Weight (kg)',
           'calculate': 'Calculate', 'underweight': 'Underweight', 'normal': 'Normal', 'overweight': 'Overweight', 'obese': 'Obese'},
    'ja': {'title': 'BMI計算機', 'desc': 'BMIを計算します。', 'height': '身長 (cm)', 'weight': '体重 (kg)',
           'calculate': '計算', 'underweight': '低体重', 'normal': '正常', 'overweight': '過体重', 'obese': '肥満'},
    'hi': {'title': 'BMI कैलकुलेटर', 'desc': 'अपना BMI गणना करें।', 'height': 'ऊंचाई (cm)', 'weight': 'वजन (kg)',
           'calculate': 'गणना', 'underweight': 'कम वजन', 'normal': 'सामान्य', 'overweight': 'अधिक वजन', 'obese': 'मोटापा'},
    'id': {'title': 'Kalkulator BMI', 'desc': 'Hitung BMI Anda.', 'height': 'Tinggi (cm)', 'weight': 'Berat (kg)',
           'calculate': 'Hitung', 'underweight': 'Kurus', 'normal': 'Normal', 'overweight': 'Kelebihan Berat', 'obese': 'Obesitas'},
    'vi': {'title': 'Máy Tính BMI', 'desc': 'Tính BMI của bạn.', 'height': 'Chiều cao (cm)', 'weight': 'Cân nặng (kg)',
           'calculate': 'Tính', 'underweight': 'Thiếu cân', 'normal': 'Bình thường', 'overweight': 'Thừa cân', 'obese': 'Béo phì'},
    'th': {'title': 'เครื่องคำนวณ BMI', 'desc': 'คำนวณ BMI ของคุณ', 'height': 'ส่วนสูง (cm)', 'weight': 'น้ำหนัก (kg)',
           'calculate': 'คำนวณ', 'underweight': 'น้ำหนักต่ำ', 'normal': 'ปกติ', 'overweight': 'น้ำหนักเกิน', 'obese': 'อ้วน'},
    'de': {'title': 'BMI-Rechner', 'desc': 'Berechnen Sie Ihren BMI.', 'height': 'Größe (cm)', 'weight': 'Gewicht (kg)',
           'calculate': 'Berechnen', 'underweight': 'Untergewicht', 'normal': 'Normal', 'overweight': 'Übergewicht', 'obese': 'Fettleibig'},
    'pt': {'title': 'Calculadora BMI', 'desc': 'Calcule seu BMI.', 'height': 'Altura (cm)', 'weight': 'Peso (kg)',
           'calculate': 'Calcular', 'underweight': 'Abaixo do peso', 'normal': 'Normal', 'overweight': 'Sobrepeso', 'obese': 'Obeso'}
}

DATE_TRANS = {
    'ko': {'title': '날짜 계산기', 'desc': 'D-Day와 날짜 차이를 계산하세요.', 'dday_title': 'D-Day 계산', 
           'target_date': '목표 날짜', 'calculate': '계산', 'diff_title': '날짜 차이', 'start_date': '시작 날짜', 
           'end_date': '종료 날짜', 'days': '일'},
    'en': {'title': 'Date Calculator', 'desc': 'Calculate D-Day and date differences.', 'dday_title': 'D-Day Calculator',
           'target_date': 'Target Date', 'calculate': 'Calculate', 'diff_title': 'Date Difference', 'start_date': 'Start Date',
           'end_date': 'End Date', 'days': 'days'},
    'ja': {'title': '日付計算機', 'desc': 'D-Dayと日付の差を計算します。', 'dday_title': 'D-Day計算',
           'target_date': '目標日', 'calculate': '計算', 'diff_title': '日付の差', 'start_date': '開始日',
           'end_date': '終了日', 'days': '日'},
    'hi': {'title': 'तिथि कैलकुलेटर', 'desc': 'D-Day और तिथि अंतर की गणना करें।', 'dday_title': 'D-Day गणना',
           'target_date': 'लक्ष्य तिथि', 'calculate': 'गणना', 'diff_title': 'तिथि अंतर', 'start_date': 'प्रारंभ तिथि',
           'end_date': 'समाप्ति तिथि', 'days': 'दिन'},
    'id': {'title': 'Kalkulator Tanggal', 'desc': 'Hitung D-Day dan perbedaan tanggal.', 'dday_title': 'Kalkulator D-Day',
           'target_date': 'Tanggal Target', 'calculate': 'Hitung', 'diff_title': 'Perbedaan Tanggal', 'start_date': 'Tanggal Mulai',
           'end_date': 'Tanggal Akhir', 'days': 'hari'},
    'vi': {'title': 'Máy Tính Ngày', 'desc': 'Tính D-Day và chênh lệch ngày.', 'dday_title': 'Tính D-Day',
           'target_date': 'Ngày Mục Tiêu', 'calculate': 'Tính', 'diff_title': 'Chênh Lệch Ngày', 'start_date': 'Ngày Bắt Đầu',
           'end_date': 'Ngày Kết Thúc', 'days': 'ngày'},
    'th': {'title': 'เครื่องคำนวณวันที่', 'desc': 'คำนวณ D-Day และความแตกต่างของวันที่', 'dday_title': 'คำนวณ D-Day',
           'target_date': 'วันที่เป้าหมาย', 'calculate': 'คำนวณ', 'diff_title': 'ความแตกต่างของวันที่', 'start_date': 'วันเริ่มต้น',
           'end_date': 'วันสิ้นสุด', 'days': 'วัน'},
    'de': {'title': 'Datumsrechner', 'desc': 'Berechnen Sie D-Day und Datumsunterschiede.', 'dday_title': 'D-Day-Rechner',
           'target_date': 'Zieldatum', 'calculate': 'Berechnen', 'diff_title': 'Datumsunterschied', 'start_date': 'Startdatum',
           'end_date': 'Enddatum', 'days': 'Tage'},
    'pt': {'title': 'Calculadora de Datas', 'desc': 'Calcule D-Day e diferenças de datas.', 'dday_title': 'Calculadora D-Day',
           'target_date': 'Data Alvo', 'calculate': 'Calcular', 'diff_title': 'Diferença de Datas', 'start_date': 'Data Inicial',
           'end_date': 'Data Final', 'days': 'dias'}
}

TIMER_TRANS = {
    'ko': {'title': '타이머', 'desc': '온라인 타이머와 포모도로 기법', 'minutes': '분', 'start': '시작', 
           'pause': '일시정지', 'reset': '리셋', 'break': '휴식', 'time_up': '시간 종료!'},
    'en': {'title': 'Timer', 'desc': 'Online timer with Pomodoro technique', 'minutes': 'Minutes', 'start': 'Start',
           'pause': 'Pause', 'reset': 'Reset', 'break': 'Break', 'time_up': 'Time is up!'},
    'ja': {'title': 'タイマー', 'desc': 'ポモドーロテクニック付きオンラインタイマー', 'minutes': '分', 'start': '開始',
           'pause': '一時停止', 'reset': 'リセット', 'break': '休憩', 'time_up': '時間切れ!'},
    'hi': {'title': 'टाइमर', 'desc': 'पोमोडोरो तकनीक के साथ ऑनलाइन टाइमर', 'minutes': 'मिनट', 'start': 'शुरू',
           'pause': 'रोकें', 'reset': 'रीसेट', 'break': 'विराम', 'time_up': 'समय समाप्त!'},
    'id': {'title': 'Timer', 'desc': 'Timer online dengan teknik Pomodoro', 'minutes': 'Menit', 'start': 'Mulai',
           'pause': 'Jeda', 'reset': 'Reset', 'break': 'Istirahat', 'time_up': 'Waktu habis!'},
    'vi': {'title': 'Hẹn Giờ', 'desc': 'Bộ hẹn giờ trực tuyến với kỹ thuật Pomodoro', 'minutes': 'Phút', 'start': 'Bắt đầu',
           'pause': 'Tạm dừng', 'reset': 'Đặt lại', 'break': 'Nghỉ', 'time_up': 'Hết giờ!'},
    'th': {'title': 'ตัวจับเวลา', 'desc': 'ตัวจับเวลาออนไลน์พร้อมเทคนิค Pomodoro', 'minutes': 'นาที', 'start': 'เริ่ม',
           'pause': 'หยุดชั่วคราว', 'reset': 'รีเซ็ต', 'break': 'พัก', 'time_up': 'หมดเวลา!'},
    'de': {'title': 'Timer', 'desc': 'Online-Timer mit Pomodoro-Technik', 'minutes': 'Minuten', 'start': 'Start',
           'pause': 'Pause', 'reset': 'Zurücksetzen', 'break': 'Pause', 'time_up': 'Zeit ist um!'},
    'pt': {'title': 'Temporizador', 'desc': 'Temporizador online com técnica Pomodoro', 'minutes': 'Minutos', 'start': 'Iniciar',
           'pause': 'Pausar', 'reset': 'Reiniciar', 'break': 'Pausa', 'time_up': 'Tempo esgotado!'}
}


def main():
    print("🚀 Creating BMI Calculator, Date Calculator, and Timer for all languages...\\n")
    
    langs = list(BMI_TRANS.keys())
    
    for lang in langs:
        # BMI Calculator
        bmi_dir = BASE_DIR / lang / 'bmi-calculator'
        bmi_dir.mkdir(parents=True, exist_ok=True)
        with open(bmi_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(create_bmi_calculator(lang, BMI_TRANS))
        print(f"✅ Created: {lang}/bmi-calculator/index.html")
        
        # Date Calculator
        date_dir = BASE_DIR / lang / 'date-calculator'
        date_dir.mkdir(parents=True, exist_ok=True)
        with open(date_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(create_date_calculator(lang, DATE_TRANS))
        print(f"✅ Created: {lang}/date-calculator/index.html")
        
        # Timer
        timer_dir = BASE_DIR / lang / 'timer'
        timer_dir.mkdir(parents=True, exist_ok=True)
        with open(timer_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(create_timer(lang, TIMER_TRANS))
        print(f"✅ Created: {lang}/timer/index.html")
    
    print(f"\\n{'='*60}")
    print(f"✨ Complete! Created 3 utilities for {len(langs)} languages")
    print(f"📊 Total files created: {len(langs) * 3} files")
    print(f"{'='*60}\\n")

if __name__ == '__main__':
    main()

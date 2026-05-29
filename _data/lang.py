
# Language data for the SSG system
# Key: Language Code (en, ko, vi, th, etc.)
# Value: Dictionary of translation strings

LANGUAGES = ['en', 'ko', 'vi', 'th', 'de', 'pt', 'id', 'hi', 'ja', 'zh-cn', 'zh-tw']

COMMON = {
    "en": {
        "brand": "🛠️ Utilify",
        "footer": "&copy; 2025 Utilify. All rights reserved.",
        "secure_badge": "🔒 Secure & Client-side",
        "install_app": "📲 Install App",
        "link_about": "About",
        "link_privacy": "Privacy",
        "link_terms": "Terms",
        "skip_link": "Skip to content",
        "fav_add_aria": "Add to favorites",
        "fav_remove_aria": "Remove from favorites",
        "theme_toggle_aria": "Toggle dark mode",
        "theme_to_dark_aria": "Switch to dark mode",
        "theme_to_light_aria": "Switch to light mode",
        "breadcrumb_home": "Home",
    },
    "ko": {
        "brand": "🛠️ Utilify",
        "footer": "&copy; 2025 Utilify. All rights reserved.",
        "secure_badge": "🔒 Secure & Client-side",
        "install_app": "📲 Install App",
        "link_about": "소개",
        "link_privacy": "개인정보",
        "link_terms": "이용약관",
        "skip_link": "본문으로 건너뛰기",
        "fav_add_aria": "즐겨찾기에 추가",
        "fav_remove_aria": "즐겨찾기에서 제거",
        "theme_toggle_aria": "다크 모드 전환",
        "theme_to_dark_aria": "다크 모드로 전환",
        "theme_to_light_aria": "라이트 모드로 전환",
        "breadcrumb_home": "홈",
    },
    "vi": {
        "brand": "🛠️ Utilify",
        "footer": "&copy; 2025 Utilify. All rights reserved.",
        "secure_badge": "🔒 An toàn & Phía máy khách",
        "install_app": "📲 Cài đặt ứng dụng",
    },
    "th": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. All rights reserved.", "secure_badge": "🔒 Secure & Client-side", "install_app": "📲 Install App"},
    "de": {"brand": "Utilify", "footer": "", "secure_badge": "🔒 Sicher & Clientseitig", "install_app": "📲 App installieren"},
    "pt": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. All rights reserved.", "secure_badge": "🔒 Seguro e Cliente-side", "install_app": "📲 Instalar App"},
    "id": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. All rights reserved.", "secure_badge": "🔒 Secure & Client-side", "install_app": "📲 Install App"},
    "hi": {"brand": "Utilify", "footer": "", "secure_badge": "🔒 सुरक्षित और क्लाइंट-साइड", "install_app": "📲 ऐप इंस्टॉल करें"},
    "ja": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. All rights reserved.", "secure_badge": "🔒 Secure & Client-side", "install_app": "📲 Install App"},
    "zh-cn": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. 保留所有权利。", "secure_badge": "🔒 安全 & 客户端处理", "install_app": "📲 安装应用"},
    "zh-tw": {"brand": "🛠️ Utilify", "footer": "&copy; 2025 Utilify. 版權所有。", "secure_badge": "🔒 安全 & 用戶端處理", "install_app": "📲 安裝應用"},
}


JSON_TO_EXCEL = {
    "en": {"title": "JSON to Excel Converter", "page_desc": "Convert JSON data to Excel and download. (Secure)"},
    "ko": {"title": "JSON to Excel 변환기", "page_desc": "JSON 데이터를 엑셀로 변환하고 다운로드하세요. (보안)"},
    "zh-cn": {"title": "JSON 转 Excel", "page_desc": "将 JSON 数据转换为 Excel 并下载。（安全）"},
    "zh-tw": {"title": "JSON 轉 Excel", "page_desc": "將 JSON 數據轉換為 Excel 並下載。（安全）"},
    "ja": {"title": "JSON Excel 変換", "page_desc": "JSONデータをExcelに変換してダウンロードします。（安全）"},
    "vi": {"title": "Chuyển đổi JSON sang Excel", "page_desc": "Chuyển đổi dữ liệu JSON sang Excel và tải xuống. (An toàn)"},
    "th": {"title": "แปลง JSON เป็น Excel", "page_desc": "แปลงข้อมูล JSON เป็น Excel และดาวน์โหลด (ปลอดภัย)"},
    "de": {"title": "JSON zu Excel Konverter", "page_desc": "JSON-Daten in Excel konvertieren und herunterladen. (Sicher)"},
    "pt": {"title": "Conversor JSON para Excel", "page_desc": "Converter dados JSON para Excel e baixar. (Seguro)"},
    "id": {"title": "Konverter JSON ke Excel", "page_desc": "Konversi data JSON ke Excel dan unduh. (Aman)"},
    "hi": {"title": "JSON से Excel कनवर्टर", "page_desc": "JSON डेटा को Excel में बदलें और डाउनलोड करें। (सुरक्षित)"}
}

JSON_LD_GENERATOR = {
    "en": {"title": "SEO JSON-LD Generator", "page_desc": "Create structured data (schema) for Google/Naver exposure."},
    "ko": {"title": "SEO JSON-LD 생성기", "page_desc": "구글/네이버 노출을 위한 구조화된 데이터(스키마)를 만드세요."},
    "zh-cn": {"title": "SEO JSON-LD 生成器", "page_desc": "生成用于 Google/Naver 曝光的结构化数据（Schema）。"},
    "zh-tw": {"title": "SEO JSON-LD 生成器", "page_desc": "生成用於 Google/Naver 曝光的結構化數據（Schema）。"},
    "ja": {"title": "SEO JSON-LD ジェネレーター", "page_desc": "Google/Naver公開用の構造化データ（スキーマ）を作成します。"},
    "vi": {"title": "Trình tạo SEO JSON-LD", "page_desc": "Tạo dữ liệu có cấu trúc (schema) cho hiển thị trên Google/Naver."},
    "th": {"title": "ตัวสร้าง SEO JSON-LD", "page_desc": "สร้างข้อมูลโครงสร้าง (schema) สำหรับการแสดงผลบน Google/Naver"},
    "de": {"title": "SEO JSON-LD Generator", "page_desc": "Erstellen Sie strukturierte Daten (Schema) für Google/Naver-Sichtbarkeit."},
    "pt": {"title": "Gerador SEO JSON-LD", "page_desc": "Crie dados estruturados (schema) para exposição no Google/Naver."},
    "id": {"title": "Generator SEO JSON-LD", "page_desc": "Buat data terstruktur (skema) untuk eksposur Google/Naver."},
    "hi": {"title": "SEO JSON-LD जेनरेटर", "page_desc": "Google/Naver एक्सपोजर के लिए स्ट्रक्चर्ड डेटा (schema) बनाएं।"}
}

PDF_TOOLS = {
    "en": {"title": "PDF Merge/Split", "page_desc": "Merge and split PDFs securely in your browser without server upload."},
    "ko": {"title": "PDF 병합/분리", "page_desc": "서버 전송 없이 브라우저에서 안전하게 PDF를 합치고 나누세요."},
    "zh-cn": {"title": "PDF 合并/拆分", "page_desc": "在浏览器中安全地合并和拆分 PDF，无需上传到服务器。"},
    "zh-tw": {"title": "PDF 合併/拆分", "page_desc": "在瀏覽器中安全地合併和拆分 PDF，無需上傳到伺服器。"},
    "ja": {"title": "PDF 結合/分割", "page_desc": "サーバーにアップロードせず、ブラウザで安全にPDFを結合・分割します。"},
    "vi": {"title": "Ghép/Tách PDF", "page_desc": "Ghép và tách PDF an toàn ngay trên trình duyệt mà không cần tải lên máy chủ."},
    "th": {"title": "รวม/แยก PDF", "page_desc": "รวมและแยก PDF อย่างปลอดภัยในเบราว์เซอร์ของคุณโดยไม่ต้องอัปโหลดไปยังเซิร์ฟเวอร์"},
    "de": {"title": "PDF zusammenfügen/teilen", "page_desc": "Fügen Sie PDFs sicher in Ihrem Browser zusammen und teilen Sie sie ohne Server-Upload."},
    "pt": {"title": "Juntar/Dividir PDF", "page_desc": "Junte e divida PDFs de forma segura no seu navegador sem upload para o servidor."},
    "id": {"title": "Gabung/Pisah PDF", "page_desc": "Gabungkan dan pisahkan PDF secara aman di browser Anda tanpa unggah ke server."},
    "hi": {"title": "PDF मर्ज/स्प्लिट", "page_desc": "सर्वर पर अपलोड किए बिना अपने ब्राउज़र में सुरक्षित रूप से PDF को मर्ज और स्प्लिट करें।"}
}

TEXT_TO_DIAGRAM = {
    "en": {"title": "Text to Diagram", "page_desc": "Create flowcharts and sequence diagrams from text."},
    "ko": {"title": "텍스트로 다이어그램 그리기", "page_desc": "텍스트만 입력하면 순서도, 시퀀스 다이어그램이 완성됩니다."},
    "zh-cn": {"title": "文本转图表", "page_desc": "从文本创建流程图和时序图。"},
    "zh-tw": {"title": "文本轉圖表", "page_desc": "從文本創建流程圖和時序圖。"},
    "ja": {"title": "テキスト図解作成", "page_desc": "テキストからフローチャートやシーケンス図を作成します。"},
    "vi": {"title": "Văn bản sang Sơ đồ", "page_desc": "Tạo lưu đồ và biểu đồ tuần tự từ văn bản."},
    "th": {"title": "ข้อความเป็นแผนภาพ", "page_desc": "สร้างผังงานและแผนภาพลำดับจากข้อความ"},
    "de": {"title": "Text zu Diagramm", "page_desc": "Erstellen Sie Flussdiagramme und Sequenzdiagramme aus Text."},
    "pt": {"title": "Texto para Diagrama", "page_desc": "Crie fluxogramas e diagramas de sequência a partir de texto."},
    "id": {"title": "Teks ke Diagram", "page_desc": "Buat diagram alur dan diagram urutan dari teks."},
    "hi": {"title": "टेक्स्ट टू डायग्राम", "page_desc": "टेक्स्ट से फ्लोचार्ट और सीक्वेंस डायग्राम बनाएं।"}
}

DAILY_VERSE = {
    "en": {"title": "Daily Bible Verse", "page_desc": "Get a new Bible verse every day."},
    "ko": {"title": "오늘의 말씀", "page_desc": "매일 새로운 성경 구절을 받아보세요."},
    "zh-cn": {"title": "每日经文", "page_desc": "每天获取一句新的圣经经文。"},
    "zh-tw": {"title": "每日經文", "page_desc": "每天獲取一句新的聖經經文。"},
    "ja": {"title": "今日の聖書", "page_desc": "毎日新しい聖書の一節を受け取ります。"},
    "vi": {"title": "Câu Kinh Thánh hàng ngày", "page_desc": "Nhận một câu Kinh Thánh mới mỗi ngày."},
    "th": {"title": "ข้อพระคัมภีร์ประจำวัน", "page_desc": "รับข้อพระคัมภีร์ใหม่ทุกวัน"},
    "de": {"title": "Täglicher Bibelvers", "page_desc": "Erhalten Sie jeden Tag einen neuen Bibelvers."},
    "pt": {"title": "Versículo Bíblico Diário", "page_desc": "Receba um novo versículo bíblico todos os dias."},
    "id": {"title": "Ayat Alkitab Harian", "page_desc": "Dapatkan ayat Alkitab baru setiap hari."},
    "hi": {"title": "दैनिक बाइबिल वचन", "page_desc": "हर दिन एक नया बाइबिल वचन प्राप्त करें।"}
}

IMAGE_EDITOR = {
    "en": {"title": "Image Editor", "page_desc": "Crop, rotate, and apply filters to images."},
    "ko": {"title": "이미지 편집기", "page_desc": "이미지를 자르고, 회전하고, 필터를 적용하세요."},
    "zh-cn": {"title": "图片编辑器", "page_desc": "裁剪、旋转图片并应用滤镜。"},
    "zh-tw": {"title": "圖片編輯器", "page_desc": "裁剪、旋轉圖片並應用濾鏡。"},
    "ja": {"title": "画像エディタ", "page_desc": "画像のトリミング、回転、フィルター適用ができます。"},
    "vi": {"title": "Trình sửa ảnh", "page_desc": "Cắt, xoay và áp dụng bộ lọc cho hình ảnh."},
    "th": {"title": "โปรแกรมแก้ไขรูปภาพ", "page_desc": "ตัด หมุน และใช้ฟิลเตอร์กับรูปภาพ"},
    "de": {"title": "Bildbearbeitung", "page_desc": "Bilder zuschneiden, drehen und Filter anwenden."},
    "pt": {"title": "Editor de Imagens", "page_desc": "Recorte, gire e aplique filtros às imagens."},
    "id": {"title": "Editor Gambar", "page_desc": "Pangkas, putar, dan terapkan filter pada gambar."},
    "hi": {"title": "इमेज एडिटर", "page_desc": "छवियों को काटें, घुमाएं और फ़िल्टर लागू करें।"}
}

JPA_CONVERTER = {
    "en": {"title": "DB to JPA Converter", "page_desc": "Convert SQL schema to JPA Entity and DTO classes."},
    "ko": {"title": "DB to JPA 변환기", "page_desc": "SQL 스키마를 JPA Entity, DTO 클래스로 자동 변환합니다."},
    "zh-cn": {"title": "DB 转 JPA 转换器", "page_desc": "将 SQL 模式转换为 JPA 实体和 DTO 类。"},
    "zh-tw": {"title": "DB 轉 JPA 轉換器", "page_desc": "將 SQL 模式轉換為 JPA 實體和 DTO 類。"},
    "ja": {"title": "DB JPA 変換", "page_desc": "SQLスキーマをJPAエンティティとDTOクラスに変換します。"},
    "vi": {"title": "Chuyển đổi DB sang JPA", "page_desc": "Chuyển đổi lược đồ SQL sang lớp JPA Entity và DTO."},
    "th": {"title": "แปลง DB เป็น JPA", "page_desc": "แปลงสคีมา SQL เป็นคลาส JPA Entity และ DTO"},
    "de": {"title": "DB zu JPA Konverter", "page_desc": "Konvertieren Sie SQL-Schema in JPA-Entity- und DTO-Klassen."},
    "pt": {"title": "Conversor DB para JPA", "page_desc": "Converta esquema SQL para classes JPA Entity e DTO."},
    "id": {"title": "Konverter DB ke JPA", "page_desc": "Konversi skema SQL ke kelas JPA Entity dan DTO."},
    "hi": {"title": "DB से JPA कनवर्टर", "page_desc": "SQL स्कीमा को JPA एंटिटी और DTO क्लास में बदलें।"}
}

JSON_TO_TS = {
    "en": {"title": "JSON to TS/DTO", "page_desc": "Convert JSON to TypeScript Interface and NestJS DTO."},
    "ko": {"title": "JSON to TS/DTO", "page_desc": "JSON을 TypeScript Interface 및 NestJS DTO로 변환합니다."},
    "zh-cn": {"title": "JSON 转 TS/DTO", "page_desc": "将 JSON 转换为 TypeScript 接口和 NestJS DTO。"},
    "zh-tw": {"title": "JSON 轉 TS/DTO", "page_desc": "將 JSON 轉換為 TypeScript 介面和 NestJS DTO。"},
    "ja": {"title": "JSON TS/DTO 変換", "page_desc": "JSONをTypeScriptインターフェースとNestJS DTOに変換します。"},
    "vi": {"title": "JSON sang TS/DTO", "page_desc": "Chuyển đổi JSON sang giao diện TypeScript và NestJS DTO."},
    "th": {"title": "JSON เป็น TS/DTO", "page_desc": "แปลง JSON เป็น TypeScript Interface และ NestJS DTO"},
    "de": {"title": "JSON zu TS/DTO", "page_desc": "Konvertieren Sie JSON in TypeScript Interface und NestJS DTO."},
    "pt": {"title": "JSON para TS/DTO", "page_desc": "Converta JSON para TypeScript Interface e NestJS DTO."},
    "id": {"title": "JSON ke TS/DTO", "page_desc": "Konversi JSON ke TypeScript Interface dan NestJS DTO."},
    "hi": {"title": "JSON से TS/DTO", "page_desc": "JSON को TypeScript Interface और NestJS DTO में बदलें।"}
}

EXCEL_TO_SQL = {
    "en": {"title": "Excel to SQL", "page_desc": "Convert Excel data to SQL INSERT queries."},
    "ko": {"title": "Excel to SQL", "page_desc": "엑셀 데이터를 SQL INSERT 쿼리로 변환하는 도구."},
    "zh-cn": {"title": "Excel 转 SQL", "page_desc": "将 Excel 数据转换为 SQL INSERT 查询。"},
    "zh-tw": {"title": "Excel 轉 SQL", "page_desc": "將 Excel 數據轉換為 SQL INSERT 查詢。"},
    "ja": {"title": "Excel SQL 変換", "page_desc": "ExcelデータをSQL INSERTクエリに変換します。"},
    "vi": {"title": "Excel sang SQL", "page_desc": "Chuyển đổi dữ liệu Excel sang truy vấn SQL INSERT."},
    "th": {"title": "Excel เป็น SQL", "page_desc": "แปลงข้อมูล Excel เป็นคำสั่ง SQL INSERT"},
    "de": {"title": "Excel zu SQL", "page_desc": "Konvertieren Sie Excel-Daten in SQL INSERT-Abfragen."},
    "pt": {"title": "Excel para SQL", "page_desc": "Converta dados do Excel em consultas SQL INSERT."},
    "id": {"title": "Excel ke SQL", "page_desc": "Konversi data Excel ke kueri SQL INSERT."},
    "hi": {"title": "Excel से SQL", "page_desc": "Excel डेटा को SQL INSERT क्वेरी में बदलें।"}
}

INDEX_PAGE = {
    "en": {
        "title": "Utilify - Free Online Utilities",
        "meta_desc": "Privacy-first online tools that run entirely in your browser. JSON formatter, JWT decoder, Base64 converter, unit conversion, and 30+ more. No signup, no upload.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "Privacy-first online tools — runs entirely in your browser. JSON · JWT · Base64 · UUID · 110+ unit converters. No signup, no upload.",
        "trust_client": "🔒 Client-side only",
        "trust_oss": "⭐ Open source",
        "trust_langs": "🌐 11 languages",
        "trust_pwa": "📲 Installable PWA",
        "h2_featured": "Featured Tools",
        "h2_tools": "All Tools",
        "h2_popular_conv": "Popular Conversions",
        "h2_lang": "Choose Your Language",
        "cat_all": "All",
        "cat_dev": "Developer",
        "cat_text": "Text",
        "cat_image": "Image",
        "cat_convert": "Converters",
        "cat_calc": "Calculators",
        "cat_ai": "AI",
        "github_label": "GitHub",
        "favorites_label": "★ Favorites",
        "favorites_empty": "No favorites yet. Click ☆ on any tool card to save it.",
        "fav_add_aria": "Add to favorites",
        "fav_remove_aria": "Remove from favorites",
        "subcat_all": "All",
        "subcat_finance": "Finance",
        "subcat_health": "Health",
        "subcat_filter_aria": "Subcategory filter",
        "search_placeholder": "Search tools…",
        "search_no_results": "No tools match your search.",
        "hub_link_finance": "Finance hub",
        "hub_link_health": "Health hub",
        "favorites_export": "⬇ Export favorites",
        "favorites_import": "⬆ Import favorites",
        "favorites_export_empty": "No favorites to export yet.",
        "favorites_import_success": "Favorites imported",
        "favorites_import_error": "Couldn't read that file."
    },
    "ko": {
        "title": "무료 온라인 유틸리티 모음 - Utilify",
        "meta_desc": "브라우저에서 모두 실행되는 프라이버시 우선 온라인 도구. JSON 포매터, JWT 디코더, Base64 변환기, 단위 변환 등 30개 이상. 가입·업로드 불필요.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "프라이버시 우선 온라인 도구 — 모든 처리는 브라우저에서. JSON · JWT · Base64 · UUID · 110개+ 단위 변환. 가입·업로드 없음.",
        "trust_client": "🔒 클라이언트 전용",
        "trust_oss": "⭐ 오픈소스",
        "trust_langs": "🌐 11개 언어",
        "trust_pwa": "📲 PWA 설치 가능",
        "h2_featured": "주요 도구",
        "h2_tools": "전체 도구",
        "h2_popular_conv": "인기 변환",
        "h2_lang": "언어 선택",
        "cat_all": "전체",
        "cat_dev": "개발자",
        "cat_text": "텍스트",
        "cat_image": "이미지",
        "cat_convert": "변환기",
        "cat_calc": "계산기",
        "cat_ai": "AI",
        "github_label": "GitHub",
        "favorites_label": "★ 즐겨찾기",
        "favorites_empty": "즐겨찾기가 없습니다. 도구 카드의 ☆를 눌러 추가하세요.",
        "fav_add_aria": "즐겨찾기에 추가",
        "fav_remove_aria": "즐겨찾기에서 제거",
        "subcat_all": "전체",
        "subcat_finance": "금융",
        "subcat_health": "건강",
        "subcat_filter_aria": "하위 카테고리 필터",
        "search_placeholder": "도구 검색…",
        "search_no_results": "검색 결과가 없습니다.",
        "hub_link_finance": "금융 허브",
        "hub_link_health": "건강 허브",
        "favorites_export": "⬇ 즐겨찾기 내보내기",
        "favorites_import": "⬆ 즐겨찾기 가져오기",
        "favorites_export_empty": "내보낼 즐겨찾기가 없습니다.",
        "favorites_import_success": "즐겨찾기를 가져왔습니다",
        "favorites_import_error": "파일을 읽을 수 없습니다."
    },
    "vi": {
        "title": "Bộ tiện ích trực tuyến miễn phí - Utilify",
        "meta_desc": "Bộ sưu tập các tiện ích trực tuyến miễn phí bao gồm chuyển đổi đơn vị, công cụ PDF, chuyển đổi hình ảnh, máy tính và nhiều hơn nữa.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "Các tiện ích trực tuyến miễn phí cho công việc hàng ngày. Không cần cài đặt.",
        "h2_tools": "Công cụ có sẵn",
        "h2_lang": "Chọn ngôn ngữ"
    },
    "th": {
        "title": "รวมเครื่องมือออนไลน์ฟรี - Utilify",
        "meta_desc": "รวมเครื่องมือออนไลน์ฟรี รวมถึงแปลงหน่วย เครื่องมือ PDF แปลงรูปภาพ เครื่องคิดเลข และอื่นๆ",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "เครื่องมือออนไลน์ฟรีสำหรับงานประจำวัน ไม่ต้องติดตั้ง",
        "h2_tools": "เครื่องมือที่มีอยู่",
        "h2_lang": "เลือกภาษา"
    },
    "de": {
        "title": "Kostenlose Online-Dienstprogramme - Utilify",
        "meta_desc": "Sammlung kostenloser Online-Dienstprogramme wie Einheitenumrechner, PDF-Tools, Bildkonverter, Rechner und mehr.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "Kostenlose Online-Dienstprogramme für tägliche Aufgaben. Keine Installation erforderlich.",
        "h2_tools": "Verfügbare Tools",
        "h2_lang": "Sprache wählen"
    },
    "pt": {
        "title": "Utilitários Online Gratuitos - Utilify",
        "meta_desc": "Coleção de utilitários online gratuitos, incluindo conversor de unidades, ferramentas PDF, conversor de imagens, calculadoras e muito mais.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "Utilitários online gratuitos para tarefas diárias. Nenhuma instalação necessária.",
        "h2_tools": "Ferramentas Disponíveis",
        "h2_lang": "Escolha seu idioma"
    },
    "id": {
        "title": "Utilitas Online Gratis - Utilify",
        "meta_desc": "Kumpulan utilitas online gratis termasuk konverter unit, alat PDF, konverter gambar, kalkulator, dan banyak lagi.",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "Utilitas online gratis untuk tugas sehari-hari. Tidak perlu instalasi.",
        "h2_tools": "Alat yang Tersedia",
        "h2_lang": "Pilih Bahasa"
    },
    "hi": {
        "title": "मुफ्त ऑनलाइन उपयोगिताएँ - Utilify",
        "meta_desc": "यूनिट कन्वर्टर, पीडीएफ टूल्स, इमेज कन्वर्टर, कैलकुलेटर, और अधिक सहित मुफ्त ऑनलाइन उपयोगिताओं का संग्रह।",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "रोज़मर्रा के कार्यों के लिए मुफ्त ऑनलाइन उपयोगिताएँ। कोई स्थापना की आवश्यकता नहीं है।",
        "h2_tools": "उपलब्ध उपकरण",
        "h2_lang": "अपनी भाषा चुनें"
    },
    "ja": {
        "title": "無料オンラインユーティリティ - Utilify",
        "meta_desc": "単位変換、PDFツール、画像変換、計算機など、無料のオンラインユーティリティコレクション。",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "日常業務のための無料オンラインユーティリティ。インストール不要。",
        "h2_tools": "利用可能なツール",
        "h2_lang": "言語を選択",
        "favorites_export": "⬇ お気に入りをエクスポート",
        "favorites_import": "⬆ お気に入りをインポート",
        "favorites_export_empty": "エクスポートするお気に入りがありません。",
        "favorites_import_success": "お気に入りをインポートしました",
        "favorites_import_error": "ファイルを読み込めませんでした。"
    },
    "zh-cn": {
        "title": "免费在线工具箱 - Utilify",
        "meta_desc": "免费在线工具集合，包括单位转换、PDF 工具、图片转换、计算器等。无需安装。",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "用于日常任务的免费在线工具。无需安装，浏览器直接使用。",
        "h2_tools": "可用工具",
        "h2_lang": "选择语言"
    },
    "zh-tw": {
        "title": "免費線上工具箱 - Utilify",
        "meta_desc": "免費線上工具集合，包括單位轉換、PDF 工具、圖片轉換、計算器等。無需安裝。",
        "hero_title": "🛠️ Utilify",
        "hero_desc": "用於日常任務的免費線上工具。無需安裝，瀏覽器直接使用。",
        "h2_tools": "可用工具",
        "h2_lang": "選擇語言"
    }
}

SQL_FORMATTER = {
    "en": {
        "title": "SQL Formatter",
        "meta_title": "SQL Formatter & Beautifier for PostgreSQL, MySQL - Utilify",
        "meta_desc": "Free Online SQL Formatter. Beautify and Minify SQL queries for PostgreSQL, MySQL, Oracle. Ad-free tool for developers.",
        "og_title": "SQL Formatter & Beautifier - Utilify",
        "og_desc": "Format, Beautify and Minify SQL queries. Ad-free tool for developers.",
        "json_name": "SQL Formatter",
        "json_desc": "Format, Beautify and Minify SQL queries.",
        "page_desc": "Format, Beautify and Minify SQL queries. Ad-free for developers.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "label_input": "Input (SQL)",
        "label_output": "Output (Formatted)",
        "related_header": "Related Tools",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "Please enter SQL query.",
        "alert_copy_empty": "Nothing to copy."
    },
    "ko": {
        "title": "SQL 포매터",
        "meta_title": "SQL 포매터 & 정렬기 (Beautifier, Minifier) - Utilify",
        "meta_desc": "SQL 쿼리를 자동으로 정렬(Beautify)하고 압축(Minify)하세요. 개발자를 위한 광고 없는 SQL 도구. MySQL, PostgreSQL 지원.",
        "og_title": "SQL 포매터 & 정렬기 - Utilify",
        "og_desc": "SQL 쿼리를 자동으로 정렬하고 포맷팅하세요. 개발자를 위한 광고 없는 도구.",
        "json_name": "SQL 포매터",
        "json_desc": "SQL 쿼리를 자동으로 정렬하고 포맷팅하세요.",
        "page_desc": "SQL 쿼리를 자동으로 정렬하고 포맷팅하세요. 개발자를 위해 광고를 제거했습니다.",
        "label_dialect": "SQL 언어:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "📋 복사",
        "btn_clear": "🗑️ 초기화",
        "label_input": "입력 (SQL)",
        "label_output": "출력 (포맷된 SQL)",
        "related_header": "함께 보면 좋은 도구",
        "related_json": "JSON 포매터",
        "related_base64": "Base64 변환기",
        "related_pw": "비밀번호 생성기",
        "alert_input": "SQL 쿼리를 입력해주세요.",
        "alert_copy_empty": "복사할 내용이 없습니다."
    },
    "vi": {
        "title": "Định dạng SQL",
        "meta_title": "Định dạng SQL - Utilify",
        "meta_desc": "Format, Beautify and Minify SQL queries.",
        "og_title": "Định dạng SQL - 🛠️ Utilify",
        "og_desc": "Định dạng, làm đẹp và tối ưu hóa truy vấn SQL.",
        "json_name": "Định dạng SQL",
        "json_desc": "Tự động định dạng và làm đẹp các truy vấn SQL.",
        "page_desc": "Định dạng, làm đẹp và tối ưu hóa truy vấn SQL.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "Sao chép",
        "btn_clear": "Clear",
        "label_input": "Đầu vào (SQL)",
        "label_output": "Đầu ra (Đã định dạng)",
        "related_header": "Công cụ liên quan",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "Vui lòng nhập truy vấn SQL.",
        "alert_copy_empty": "Không có nội dung để sao chép."
    },
    "th": {
        "title": "ตัวจัดรูปแบบ SQL",
        "meta_title": "ตัวจัดรูปแบบ SQL - Utilify",
        "meta_desc": "จัดรูปแบบ ตกแต่ง และย่อขนาดคำสั่ง SQL",
        "og_title": "ตัวจัดรูปแบบ SQL - 🛠️ Utilify",
        "og_desc": "จัดรูปแบบ ตกแต่ง และย่อขนาดคำสั่ง SQL",
        "json_name": "ตัวจัดรูปแบบ SQL",
        "json_desc": "จัดรูปแบบ ตกแต่ง และย่อขนาดคำสั่ง SQL",
        "page_desc": "จัดรูปแบบ ตกแต่ง และย่อขนาดคำสั่ง SQL",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ ทำสวย",
        "btn_minify": "📦 ย่อขนาด",
        "btn_copy": "คัดลอก",
        "btn_clear": "ล้าง",
        "label_input": "นำเข้า (SQL)",
        "label_output": "ผลลัพธ์ (จัดรูปแบบแล้ว)",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "กรุณาป้อนคิวรี SQL",
        "alert_copy_empty": "ไม่มีเนื้อหาให้คัดลอก"
    },
    "de": {
        "title": "SQL-Formatierer",
        "meta_title": "SQL-Formatierer - Utilify",
        "meta_desc": "Format, Beautify and Minify SQL queries.",
        "og_title": "SQL-Formatierer - 🛠️ Utilify",
        "og_desc": "Kostenlos SQL-Abfragen formatieren, verschönern und minimieren.",
        "json_name": "SQL-Formatierer",
        "json_desc": "Kostenlos SQL-Abfragen formatieren, verschönern und minimieren.",
        "page_desc": "Format, Beautify and Minify SQL queries.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "Kopieren",
        "btn_clear": "Löschen",
        "label_input": "Eingabe (SQL)",
        "label_output": "Ausgabe (Formatiert)",
        "related_header": "Verwandte Tools",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "Bitte geben Sie eine SQL-Abfrage ein.",
        "alert_copy_empty": "Kein Inhalt zum Kopieren vorhanden."
    },
    "pt": {
        "title": "Formatador SQL",
        "meta_title": "Formatador SQL - Utilify",
        "meta_desc": "Format, Beautify and Minify SQL queries.",
        "og_title": "Formatador SQL - 🛠️ Utilify",
        "og_desc": "Formatar, embelezar e minificar consultas SQL.",
        "json_name": "Formatador SQL",
        "json_desc": "Formatar, embelezar e minificar consultas SQL.",
        "page_desc": "Format, Beautify and Minify SQL queries.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "Copiar",
        "btn_clear": "Clear",
        "label_input": "Entrada (SQL)",
        "label_output": "Saída (Formatada)",
        "related_header": "Ferramentas Relacionadas",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "Por favor, insira a consulta SQL.",
        "alert_copy_empty": "Não há conteúdo para copiar."
    },
    "id": {
        "title": "Pemformat SQL",
        "meta_title": "Pemformat SQL - Utilify",
        "meta_desc": "Format, Beautify and Minify SQL queries.",
        "og_title": "Pemformat SQL - 🛠️ Utilify",
        "og_desc": "Format, percantik, dan perkecil kueri SQL.",
        "json_name": "Pemformat SQL",
        "json_desc": "Format, percantik, dan perkecil kueri SQL.",
        "page_desc": "Format, Beautify and Minify SQL queries.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "Salin",
        "btn_clear": "Clear",
        "label_input": "Input (SQL)",
        "label_output": "Output (Terformat)",
        "related_header": "Alat Terkait",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "Silakan masukkan kueri SQL.",
        "alert_copy_empty": "Tidak ada konten untuk disalin."
    },
    "hi": {
        "title": "SQL फॉर्मेटर",
        "meta_title": "SQL फॉर्मेटर - Utilify",
        "meta_desc": "Format, Beautify and Minify SQL queries.",
        "og_title": "SQL फॉर्मेटर - 🛠️ Utilify",
        "og_desc": "SQL क्वेरीज को फॉर्मेट, सुंदर और छोटा करें।",
        "json_name": "SQL फॉर्मेटर",
        "json_desc": "SQL क्वेरीज को फॉर्मेट, सुंदर और छोटा करें।",
        "page_desc": "Format, Beautify and Minify SQL queries.",
        "label_dialect": "SQL Dialect:",
        "btn_format": "✨ Beautify",
        "btn_minify": "📦 Minify",
        "btn_copy": "कॉपी करें",
        "btn_clear": "साफ़ करें",
        "label_input": "इनपुट (SQL)",
        "label_output": "आउटपुट (फॉर्मेट किया गया)",
        "related_header": "संबंधित उपकरण",
        "related_json": "JSON Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_input": "कृपया SQL क्वेरी दर्ज करें।",
        "alert_copy_empty": "कॉपी करने के लिए कोई सामग्री नहीं है।"
    },
    "ja": {
        "title": "SQLフォーマッター",
        "meta_title": "SQLフォーマッター - Utilify",
        "meta_desc": "SQLクエリを自動的に整形・圧縮。",
        "og_title": "SQLフォーマッター - Utilify",
        "og_desc": "SQLクエリを自動的に整形・圧縮。",
        "json_name": "SQLフォーマッター",
        "json_desc": "SQLクエリを自動的に整形・圧縮。",
        "page_desc": "SQLクエリを自動的に整形・圧縮。",
        "label_dialect": "SQLダイアレクト:",
        "btn_format": "✨ 整形",
        "btn_minify": "📦 圧縮",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "label_input": "入力 (SQL)",
        "label_output": "出力 (整形済み)",
        "related_header": "関連ツール",
        "related_json": "JSONフォーマッター",
        "related_base64": "Base64変換",
        "related_pw": "パスワード生成",
        "alert_input": "SQLクエリを入力してください。",
        "alert_copy_empty": "コピーする内容がありません。"
    },
    "zh-cn": {
        "title": "SQL 格式化",
        "meta_title": "SQL 格式化 & 美化工具 (PostgreSQL, MySQL) - Utilify",
        "meta_desc": "免费在线 SQL 格式化工具。美化和压缩 PostgreSQL, MySQL, Oracle 的 SQL 查询。开发者无广告工具。",
        "og_title": "SQL 格式化 & 美化工具 - Utilify",
        "og_desc": "格式化，美化和压缩 SQL 查询。开发者无广告工具。",
        "json_name": "SQL 格式化",
        "json_desc": "格式化，美化和压缩 SQL 查询。",
        "page_desc": "格式化，美化和压缩 SQL 查询。开发者零广告。",
        "label_dialect": "SQL 方言:",
        "btn_format": "✨ 美化",
        "btn_minify": "📦 压缩",
        "btn_copy": "复制",
        "btn_clear": "清除",
        "label_input": "输入 (SQL)",
        "label_output": "输出 (已格式化)",
        "related_header": "相关工具",
        "related_json": "JSON 格式化",
        "related_base64": "Base64 转换器",
        "related_pw": "密码生成器",
        "alert_input": "请输入 SQL 查询。",
        "alert_copy_empty": "没有可复制的内容。"
    },
    "zh-tw": {
        "title": "SQL 格式化",
        "meta_title": "SQL 格式化 & 美化工具 (PostgreSQL, MySQL) - Utilify",
        "meta_desc": "免費線上 SQL 格式化工具。美化和壓縮 PostgreSQL, MySQL, Oracle 的 SQL 查詢。開發者無廣告工具。",
        "og_title": "SQL 格式化 & 美化工具 - Utilify",
        "og_desc": "格式化，美化和壓縮 SQL 查詢。開發者無廣告工具。",
        "json_name": "SQL 格式化",
        "json_desc": "格式化，美化和壓縮 SQL 查詢。",
        "page_desc": "格式化，美化和壓縮 SQL 查詢。開發者零廣告。",
        "label_dialect": "SQL 方言:",
        "btn_format": "✨ 美化",
        "btn_minify": "📦 壓縮",
        "btn_copy": "複製",
        "btn_clear": "清除",
        "label_input": "輸入 (SQL)",
        "label_output": "輸出 (已格式化)",
        "related_header": "相關工具",
        "related_json": "JSON 格式化",
        "related_base64": "Base64 轉換器",
        "related_pw": "密碼生成器",
        "alert_input": "請輸入 SQL 查詢。",
        "alert_copy_empty": "沒有可複製的內容。"
    }
}

JSON_FORMATTER = {
    "en": {
        "title": "JSON Formatter",
        "meta_title": "JSON Formatter & Validator (Pretty Print) - Utilify",
        "meta_desc": "Format (Pretty Print), Minify, and Validate JSON data. Ad-free tool for developers.",
        "og_title": "JSON Formatter & Validator - Utilify",
        "og_desc": "Format, Minify, and Validate JSON data. Ad-free tool for developers.",
        "json_name": "JSON Formatter",
        "json_desc": "Format and validate JSON data. Features include minification, formatting, and validation.",
        "page_desc": "Format, validate, and minify JSON data. Ad-free for developers.",
        "btn_format": "Format",
        "btn_minify": "Minify",
        "btn_validate": "Validate",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "label_input": "Input JSON",
        "label_output": "Result",
        "ph_input": "Enter JSON data...",
        "related_header": "Related Tools",
        "related_sql": "SQL Formatter",
        "related_base64": "Base64 Converter",
        "related_pw": "Password Generator",
        "alert_valid": "✓ Valid JSON",
        "alert_invalid": "✗ Invalid JSON",
        "alert_error": "Error: ",
        "alert_empty": "Input is empty.",
        "alert_too_large": "Input is over 1 MB. Processing may freeze the browser. Continue?",
        "alert_bigint_warn": "Heads up: integers longer than 15 digits may lose precision (JavaScript Number limit).",
        "alert_copy_empty": "Nothing to copy.",
        "howto_header": "How to use",
        "howto_html": '<ol><li>Paste your JSON into the input panel on the left.</li><li>Click <strong>Format</strong> to pretty-print with 2-space indentation, <strong>Minify</strong> to strip whitespace, or <strong>Validate</strong> to check syntax without changing the output.</li><li>Click <strong>Copy</strong> to copy the result to your clipboard.</li><li>Everything runs in your browser — your JSON is never uploaded to a server.</li></ol><p>Large inputs (over 1 MB) trigger a confirmation prompt because parsing them may briefly freeze the page. Numbers longer than 15 digits will trigger a precision warning since JavaScript stores them as 64-bit floats.</p>',
        "examples_header": "Examples",
        "examples_html": '<p><strong>Pretty-print compact JSON:</strong></p><pre><code>Input:  {"name":"Ada","tags":["dev","math"]}\nOutput: {\n  "name": "Ada",\n  "tags": [\n    "dev",\n    "math"\n  ]\n}</code></pre><p><strong>Minify with trailing-comma error:</strong></p><pre><code>Input:  {"a": 1, "b": 2,}\nResult: ✗ Invalid JSON — Unexpected token } in JSON</code></pre>'
    },
    "ko": {
        "title": "JSON 포매터",
        "meta_title": "JSON 포매터 & 검증기 (Pretty Print, Minify) - Utilify",
        "meta_desc": "JSON 데이터를 포맷팅(Pretty Print)하고 유효성을 검사(Validator)하세요. 개발자를 위한 광고 없는 깔끔한 도구.",
        "og_title": "JSON 포매터 & 검증기 - Utilify",
        "og_desc": "JSON 데이터를 포맷팅하고 유효성을 검사하세요. 개발자를 위한 광고 없는 도구.",
        "json_name": "JSON 포매터",
        "json_desc": "JSON 데이터를 포맷팅하고 유효성을 검사하세요. 압축, 포맷, 검증 기능을 제공합니다.",
        "page_desc": "JSON 데이터를 포맷팅하고 유효성을 검사하세요. 개발자를 위해 광고를 제거했습니다.",
        "btn_format": "포맷",
        "btn_minify": "압축",
        "btn_validate": "검증",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "label_input": "JSON 입력",
        "label_output": "결과",
        "ph_input": "JSON 데이터를 입력하세요...",
        "related_header": "함께 보면 좋은 도구",
        "related_sql": "SQL 포매터",
        "related_base64": "Base64 변환기",
        "related_pw": "비밀번호 생성기",
        "alert_valid": "✓ 유효한 JSON입니다",
        "alert_invalid": "✗ 유효하지 않은 JSON입니다",
        "alert_error": "오류: ",
        "alert_empty": "입력이 비어있습니다.",
        "alert_too_large": "입력이 1MB를 초과합니다. 브라우저가 잠시 멈출 수 있습니다. 진행할까요?",
        "alert_bigint_warn": "참고: 16자리 이상 정수는 JavaScript Number 한계로 정밀도가 손실될 수 있습니다.",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>왼쪽 패널에 JSON 데이터를 붙여넣으세요.</li><li><strong>Format</strong>으로 2-space 들여쓰기 적용, <strong>Minify</strong>로 공백 제거, <strong>Validate</strong>로 문법만 검사할 수 있습니다.</li><li><strong>Copy</strong> 버튼으로 결과를 클립보드에 복사하세요.</li><li>모든 처리는 브라우저에서만 이루어지며 데이터가 서버로 전송되지 않습니다.</li></ol><p>1 MB 이상 입력은 페이지가 잠깐 멈출 수 있어 확인 창이 표시됩니다. 15자리 초과 정수는 JavaScript의 64-bit float 한계로 정밀도 손실 경고가 표시됩니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>축약된 JSON을 보기 좋게 정렬:</strong></p><pre><code>입력:  {"name":"Ada","tags":["dev","math"]}\n출력: {\n  "name": "Ada",\n  "tags": [\n    "dev",\n    "math"\n  ]\n}</code></pre><p><strong>후행 쉼표 오류 검출:</strong></p><pre><code>입력:  {"a": 1, "b": 2,}\n결과: ✗ Invalid JSON — Unexpected token } in JSON</code></pre>'
    },
    "zh-cn": {
        "title": "JSON 格式化",
        "meta_title": "JSON 格式化 & 校验器 (美化) - Utilify",
        "meta_desc": "格式化 (美化)，压缩，和校验 JSON 数据。开发者无广告工具。",
        "og_title": "JSON 格式化 & 校验器 - Utilify",
        "og_desc": "格式化，压缩，和校验 JSON 数据。开发者无广告工具。",
        "json_name": "JSON 格式化",
        "json_desc": "格式化和校验 JSON 数据。功能包括压缩，格式化和校验。",
        "page_desc": "格式化，校验，和压缩 JSON 数据。开发者零广告。",
        "btn_format": "格式化",
        "btn_minify": "压缩",
        "btn_validate": "校验",
        "btn_copy": "复制",
        "btn_clear": "清除",
        "label_input": "输入 JSON",
        "label_output": "结果",
        "ph_input": "输入 JSON 数据...",
        "related_header": "相关工具",
        "related_sql": "SQL 格式化",
        "related_base64": "Base64 转换器",
        "related_pw": "密码生成器",
        "alert_valid": "✓ 有效的 JSON",
        "alert_invalid": "✗ 无效的 JSON",
        "alert_error": "错误: "
    },
    "zh-tw": {
        "title": "JSON 格式化",
        "meta_title": "JSON 格式化 & 檢查工具 (美化) - Utilify",
        "meta_desc": "格式化 (美化)，壓縮，和檢查 JSON 數據。開發者無廣告工具。",
        "og_title": "JSON 格式化 & 檢查工具 - Utilify",
        "og_desc": "格式化，壓縮，和檢查 JSON 數據。開發者無廣告工具。",
        "json_name": "JSON 格式化",
        "json_desc": "格式化和檢查 JSON 數據。功能包括壓縮，格式化和檢查。",
        "page_desc": "格式化，檢查，和壓縮 JSON 數據。開發者零廣告。",
        "btn_format": "格式化",
        "btn_minify": "壓縮",
        "btn_validate": "檢查",
        "btn_copy": "複製",
        "btn_clear": "清除",
        "label_input": "輸入 JSON",
        "label_output": "結果",
        "ph_input": "輸入 JSON 數據...",
        "related_header": "相關工具",
        "related_sql": "SQL 格式化",
        "related_base64": "Base64 轉換器",
        "related_pw": "密碼生成器",
        "alert_valid": "✓ 有效的 JSON",
        "alert_invalid": "✗ 無效的 JSON",
        "alert_error": "錯誤: "
    },
    "ja": {
        "title": "JSONフォーマッター",
        "meta_title": "JSONフォーマッター & バリデーター (整形) - Utilify",
        "meta_desc": "JSONデータの整形（Pretty Print）、圧縮、検証を行います。開発者向けの広告なしツール。",
        "og_title": "JSONフォーマッター & バリデーター - Utilify",
        "og_desc": "JSONデータの整形、圧縮、検証を行います。開発者向けの広告なしツール。",
        "json_name": "JSONフォーマッター",
        "json_desc": "JSONデータの整形、圧縮、検証を行います。圧縮、整形、検証機能を含みます。",
        "page_desc": "JSONデータの整形、検証、圧縮を行います。開発者向けの広告なしツール。",
        "btn_format": "整形",
        "btn_minify": "圧縮",
        "btn_validate": "検証",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "label_input": "入力JSON",
        "label_output": "結果",
        "ph_input": "JSONデータを入力...",
        "related_header": "関連ツール",
        "related_sql": "SQLフォーマッター",
        "related_base64": "Base64変換",
        "related_pw": "パスワード生成",
        "alert_valid": "✓ 有効なJSON",
        "alert_invalid": "✗ 無効なJSON",
        "alert_error": "エラー: "
    },
    "vi": {
        "title": "Trình định dạng JSON",
        "meta_title": "Trình định dạng JSON & Xác thực (Pretty Print) - Utilify",
        "meta_desc": "Định dạng (Pretty Print), Thu nhỏ và Xác thực dữ liệu JSON. Công cụ không quảng cáo cho nhà phát triển.",
        "og_title": "Trình định dạng JSON & Xác thực - Utilify",
        "og_desc": "Định dạng, Thu nhỏ và Xác thực dữ liệu JSON. Công cụ không quảng cáo cho nhà phát triển.",
        "json_name": "Trình định dạng JSON",
        "json_desc": "Định dạng và xác thực dữ liệu JSON. Các tính năng bao gồm thu nhỏ, định dạng và xác thực.",
        "page_desc": "Định dạng, xác thực và thu nhỏ dữ liệu JSON. Không quảng cáo cho nhà phát triển.",
        "btn_format": "Định dạng",
        "btn_minify": "Thu nhỏ",
        "btn_validate": "Xác thực",
        "btn_copy": "Sao chép",
        "btn_clear": "Xóa",
        "label_input": "Đầu vào JSON",
        "label_output": "Kết quả",
        "ph_input": "Nhập dữ liệu JSON...",
        "related_header": "Công cụ liên quan",
        "related_sql": "Định dạng SQL",
        "related_base64": "Chuyển đổi Base64",
        "related_pw": "Tạo mật khẩu",
        "alert_valid": "✓ JSON hợp lệ",
        "alert_invalid": "✗ JSON không hợp lệ",
        "alert_error": "Lỗi: "
    },
    "th": {
        "title": "ตัวจัดรูปแบบ JSON",
        "meta_title": "ตัวจัดรูปแบบ JSON & ตัวตรวจสอบ (Pretty Print) - Utilify",
        "meta_desc": "จัดรูปแบบ (Pretty Print), ย่อขนาด และตรวจสอบข้อมูล JSON เครื่องมือปลอดโฆษณาสำหรับนักพัฒนา",
        "og_title": "ตัวจัดรูปแบบ JSON & ตัวตรวจสอบ - Utilify",
        "og_desc": "จัดรูปแบบ, ย่อขนาด และตรวจสอบข้อมูล JSON เครื่องมือปลอดโฆษณาสำหรับนักพัฒนา",
        "json_name": "ตัวจัดรูปแบบ JSON",
        "json_desc": "จัดรูปแบบและตรวจสอบข้อมูล JSON ฟีเจอร์รวมถึงการย่อขนาด การจัดรูปแบบ และการตรวจสอบ",
        "page_desc": "จัดรูปแบบ, ตรวจสอบ และย่อขนาดข้อมูล JSON ปลอดโฆษณาสำหรับนักพัฒนา",
        "btn_format": "จัดรูปแบบ",
        "btn_minify": "ย่อขนาด",
        "btn_validate": "ตรวจสอบ",
        "btn_copy": "คัดลอก",
        "btn_clear": "ล้าง",
        "label_input": "นำเข้า JSON",
        "label_output": "ผลลัพธ์",
        "ph_input": "ป้อนข้อมูล JSON...",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_sql": "ตัวจัดรูปแบบ SQL",
        "related_base64": "ตัวแปลง Base64",
        "related_pw": "ตัวสร้างรหัสผ่าน",
        "alert_valid": "✓ JSON ถูกต้อง",
        "alert_invalid": "✗ JSON ไม่ถูกต้อง",
        "alert_error": "ข้อผิดพลาด: "
    },
    "de": {
        "title": "JSON Formatierer",
        "meta_title": "JSON Formatierer & Validator (Pretty Print) - Utilify",
        "meta_desc": "Formatieren (Pretty Print), Minimieren und Validieren von JSON-Daten. Werbefreies Tool für Entwickler.",
        "og_title": "JSON Formatierer & Validator - Utilify",
        "og_desc": "Formatieren, Minimieren und Validieren von JSON-Daten. Werbefreies Tool für Entwickler.",
        "json_name": "JSON Formatierer",
        "json_desc": "Formatieren und Validieren von JSON-Daten. Funktionen umfassen Minimierung, Formatierung und Validierung.",
        "page_desc": "Formatieren, Validieren und Minimieren von JSON-Daten. Werbefrei für Entwickler.",
        "btn_format": "Formatieren",
        "btn_minify": "Minimieren",
        "btn_validate": "Validieren",
        "btn_copy": "Kopieren",
        "btn_clear": "Löschen",
        "label_input": "Eingabe JSON",
        "label_output": "Ergebnis",
        "ph_input": "JSON-Daten eingeben...",
        "related_header": "Ähnliche Tools",
        "related_sql": "SQL-Formatierer",
        "related_base64": "Base64 Konverter",
        "related_pw": "Passwort Generator",
        "alert_valid": "✓ Gültiges JSON",
        "alert_invalid": "✗ Ungültiges JSON",
        "alert_error": "Fehler: "
    },
    "pt": {
        "title": "Formatador JSON",
        "meta_title": "Formatador JSON & Validador (Pretty Print) - Utilify",
        "meta_desc": "Formatar (Pretty Print), Minificar e Validar dados JSON. Ferramenta sem anúncios para desenvolvedores.",
        "og_title": "Formatador JSON & Validador - Utilify",
        "og_desc": "Formatar, Minificar e Validar dados JSON. Ferramenta sem anúncios para desenvolvedores.",
        "json_name": "Formatador JSON",
        "json_desc": "Formatar e validar dados JSON. Funcionalidades incluem minificação, formatação e validação.",
        "page_desc": "Formatar, validar e minificar dados JSON. Sem anúncios para desenvolvedores.",
        "btn_format": "Formatar",
        "btn_minify": "Minificar",
        "btn_validate": "Validar",
        "btn_copy": "Copiar",
        "btn_clear": "Limpar",
        "label_input": "Entrada JSON",
        "label_output": "Resultado",
        "ph_input": "Inserir dados JSON...",
        "related_header": "Ferramentas Relacionadas",
        "related_sql": "Formatador SQL",
        "related_base64": "Conversor Base64",
        "related_pw": "Gerador de Senha",
        "alert_valid": "✓ JSON Válido",
        "alert_invalid": "✗ JSON Inválido",
        "alert_error": "Erro: "
    },
    "id": {
        "title": "Pemformat JSON",
        "meta_title": "Pemformat JSON & Validator (Pretty Print) - Utilify",
        "meta_desc": "Format (Pretty Print), Perkecil, dan Validasi data JSON. Alat bebas iklan untuk pengembang.",
        "og_title": "Pemformat JSON & Validator - Utilify",
        "og_desc": "Format, Perkecil, dan Validasi data JSON. Alat bebas iklan untuk pengembang.",
        "json_name": "Pemformat JSON",
        "json_desc": "Format dan validasi data JSON. Fitur termasuk pengecilan, pemformatan, dan validasi.",
        "page_desc": "Format, validasi, dan perkecil data JSON. Bebas iklan untuk pengembang.",
        "btn_format": "Format",
        "btn_minify": "Perkecil",
        "btn_validate": "Validasi",
        "btn_copy": "Salin",
        "btn_clear": "Bersihkan",
        "label_input": "Input JSON",
        "label_output": "Hasil",
        "ph_input": "Masukkan data JSON...",
        "related_header": "Alat Terkait",
        "related_sql": "Pemformat SQL",
        "related_base64": "Konverter Base64",
        "related_pw": "Generator Kata Sandi",
        "alert_valid": "✓ JSON Valid",
        "alert_invalid": "✗ JSON Tidak Valid",
        "alert_error": "Kesalahan: "
    },
    "hi": {
        "title": "JSON फॉर्मेटर",
        "meta_title": "JSON फॉर्मेटर और वैलिडेटर (Pretty Print) - Utilify",
        "meta_desc": "JSON डेटा को फॉर्मेट (Pretty Print), छोटा और मान्य करें। डेवलपर्स के लिए विज्ञापन-मुक्त उपकरण।",
        "og_title": "JSON फॉर्मेटर और वैलिडेटर - Utilify",
        "og_desc": "JSON डेटा को फॉर्मेट, छोटा और मान्य करें। डेवलपर्स के लिए विज्ञापन-मुक्त उपकरण।",
        "json_name": "JSON फॉर्मेटर",
        "json_desc": "JSON डेटा को फॉर्मेट और मान्य करें। सुविधाओं में छोटा करना, फॉर्मेट करना और मान्य करना शामिल है।",
        "page_desc": "JSON डेटा को फॉर्मेट, मान्य और छोटा करें। डेवलपर्स के लिए विज्ञापन-मुक्त।",
        "btn_format": "फॉर्मेट",
        "btn_minify": "छोटा करें",
        "btn_validate": "मान्य करें",
        "btn_copy": "कॉपी करें",
        "btn_clear": "साफ़ करें",
        "label_input": "इनपुट JSON",
        "label_output": "परिणाम",
        "ph_input": "JSON डेटा दर्ज करें...",
        "related_header": "संबंधित उपकरण",
        "related_sql": "SQL फॉर्मेटर",
        "related_base64": "Base64 कनवर्टर",
        "related_pw": "पासवर्ड जेनरेटर",
        "alert_valid": "✓ मान्य JSON",
        "alert_invalid": "✗ अमान्य JSON",
        "alert_error": "त्रुटि: "
    }
}

BASE64_CONVERTER = {
    "en": {
        "title": "Base64 Encoder/Decoder",
        "meta_title": "Base64 Encoder/Decoder - Utilify",
        "meta_desc": "Encode or decode text to Base64.",
        "og_title": "Base64 Encoder/Decoder - Utilify",
        "og_desc": "Encode or decode text to Base64.",
        "page_desc": "Encode or decode text to Base64.",
        "label_input": "Input Text",
        "label_output": "Output Result",
        "ph_input": "Enter text to encode",
        "btn_encode": "⬇️ Encode",
        "btn_decode": "⬆️ Decode",
        "btn_copy": "📋 Copy",
        "btn_clear": "🗑️ Clear",
        "related_header": "Related Tools",
        "related_json": "JSON Formatter",
        "related_sql": "SQL Formatter",
        "related_pw": "Password Generator",
        "alert_encode_error": "Encoding Error: ",
        "alert_decode_error": "Decoding Error: ",
        "alert_copy_empty": "Nothing to copy.",
        "howto_header": "How to use",
        "howto_html": '<ol><li>Type or paste text into the input box.</li><li>Click <strong>Encode</strong> to convert text to Base64, or <strong>Decode</strong> to reverse it.</li><li>Multi-byte characters (emoji, CJK) are handled correctly via <code>TextEncoder</code>/<code>TextDecoder</code>.</li><li>Click <strong>Copy</strong> to send the result to your clipboard.</li></ol><p>Base64 is commonly used in HTTP Basic Auth headers, Data URIs (<code>data:image/png;base64,...</code>), email attachments (MIME), and JWT segments. It is <em>encoding</em>, not encryption — anyone can decode it.</p>',
        "examples_header": "Examples",
        "examples_html": '<p><strong>UTF-8 round-trip:</strong></p><pre><code>Encode: "Hello 🌍" → SGVsbG8g8J+MjQ==\nDecode: SGVsbG8g8J+MjQ== → "Hello 🌍"</code></pre><p><strong>Decoding a JWT payload:</strong></p><pre><code>eyJzdWIiOiIxMjMiLCJuYW1lIjoiQWRhIn0\n→ {"sub":"123","name":"Ada"}</code></pre>'
    },
    "ko": {
        "title": "Base64 인코더/디코더",
        "meta_title": "Base64 인코더/디코더 - Utilify",
        "meta_desc": "텍스트를 Base64로 인코딩하거나 디코딩하세요.",
        "og_title": "Base64 인코더/디코더 - Utilify",
        "og_desc": "텍스트를 Base64로 인코딩하거나 디코딩하세요.",
        "page_desc": "텍스트를 Base64로 인코딩하거나 디코딩하세요.",
        "label_input": "입력 텍스트",
        "label_output": "출력 결과",
        "ph_input": "인코딩할 텍스트를 입력하세요",
        "btn_encode": "⬇️ Encode",
        "btn_decode": "⬆️ Decode",
        "btn_copy": "📋 복사",
        "btn_clear": "🗑️ 초기화",
        "related_header": "함께 보면 좋은 도구",
        "related_json": "JSON 포매터",
        "related_sql": "SQL 포매터",
        "related_pw": "비밀번호 생성기",
        "alert_encode_error": "인코딩 오류: ",
        "alert_decode_error": "디코딩 오류: ",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>입력 칸에 텍스트를 입력하거나 붙여넣으세요.</li><li><strong>Encode</strong>로 Base64 인코딩, <strong>Decode</strong>로 디코딩합니다.</li><li>이모지·한글 등 멀티바이트 문자도 <code>TextEncoder/TextDecoder</code>로 정확히 처리됩니다.</li><li><strong>Copy</strong>로 결과를 복사할 수 있습니다.</li></ol><p>Base64는 HTTP Basic Auth 헤더, Data URI(<code>data:image/png;base64,...</code>), 이메일 첨부(MIME), JWT 세그먼트 등에 널리 쓰입니다. 암호화가 아니라 단순 인코딩이므로 누구나 디코딩할 수 있습니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>UTF-8 라운드트립:</strong></p><pre><code>Encode: "안녕 🌍" → 7JWI64WVIPCfjI0=\nDecode: 7JWI64WVIPCfjI0= → "안녕 🌍"</code></pre><p><strong>JWT 페이로드 디코딩:</strong></p><pre><code>eyJzdWIiOiIxMjMiLCJuYW1lIjoiQWRhIn0\n→ {"sub":"123","name":"Ada"}</code></pre>'
    },
    "zh-cn": {
        "title": "Base64 编码/解码",
        "meta_title": "Base64 编码/解码 - Utilify",
        "meta_desc": "将文本编码或解码为 Base64。",
        "og_title": "Base64 编码/解码 - Utilify",
        "og_desc": "将文本编码或解码为 Base64。",
        "page_desc": "将文本编码或解码为 Base64。",
        "label_input": "输入文本",
        "label_output": "输出结果",
        "ph_input": "输入要编码的文本",
        "btn_encode": "⬇️ 编码",
        "btn_decode": "⬆️ 解码",
        "btn_copy": "📋 复制",
        "btn_clear": "🗑️ 清除",
        "related_header": "相关工具",
        "related_json": "JSON 格式化",
        "related_sql": "SQL 格式化",
        "related_pw": "密码生成器",
        "alert_encode_error": "编码错误: ",
        "alert_decode_error": "解码错误: ",
        "alert_copy_empty": "没有可复制的内容。"
    },
    "zh-tw": {
        "title": "Base64 編碼/解碼",
        "meta_title": "Base64 編碼/解碼 - Utilify",
        "meta_desc": "將文本編碼或解碼為 Base64。",
        "og_title": "Base64 編碼/解碼 - Utilify",
        "og_desc": "將文本編碼或解碼為 Base64。",
        "page_desc": "將文本編碼或解碼為 Base64。",
        "label_input": "輸入文本",
        "label_output": "輸出結果",
        "ph_input": "輸入要編碼的文本",
        "btn_encode": "⬇️ 編碼",
        "btn_decode": "⬆️ 解碼",
        "btn_copy": "📋 複製",
        "btn_clear": "🗑️ 清除",
        "related_header": "相關工具",
        "related_json": "JSON 格式化",
        "related_sql": "SQL 格式化",
        "related_pw": "密碼生成器",
        "alert_encode_error": "編碼錯誤: ",
        "alert_decode_error": "解碼錯誤: ",
        "alert_copy_empty": "沒有可複製的內容。"
    },
    "ja": {
        "title": "Base64エンコーダー/デコーダー",
        "meta_title": "Base64エンコーダー/デコーダー - Utilify",
        "meta_desc": "テキストをBase64にエンコードまたはデコードします。",
        "og_title": "Base64エンコーダー/デコーダー - Utilify",
        "og_desc": "テキストをBase64にエンコードまたはデコードします。",
        "page_desc": "テキストをBase64にエンコードまたはデコードします。",
        "label_input": "入力テキスト",
        "label_output": "出力結果",
        "ph_input": "エンコードするテキストを入力",
        "btn_encode": "⬇️ エンコード",
        "btn_decode": "⬆️ デコード",
        "btn_copy": "📋 コピー",
        "btn_clear": "🗑️ クリア",
        "related_header": "関連ツール",
        "related_json": "JSONフォーマッター",
        "related_sql": "SQLフォーマッター",
        "related_pw": "パスワード生成",
        "alert_encode_error": "エンコードエラー: ",
        "alert_decode_error": "デコードエラー: ",
        "alert_copy_empty": "コピーする内容がありません。"
    },
    "vi": {
        "title": "Bộ mã hóa/giải mã Base64",
        "meta_title": "Bộ mã hóa/giải mã Base64 - Utilify",
        "meta_desc": "Mã hóa hoặc giải mã văn bản sang Base64.",
        "og_title": "Bộ mã hóa/giải mã Base64 - Utilify",
        "og_desc": "Mã hóa hoặc giải mã văn bản sang Base64.",
        "page_desc": "Mã hóa hoặc giải mã văn bản sang Base64.",
        "label_input": "Văn bản đầu vào",
        "label_output": "Kết quả đầu ra",
        "ph_input": "Nhập văn bản để mã hóa",
        "btn_encode": "⬇️ Mã hóa",
        "btn_decode": "⬆️ Giải mã",
        "btn_copy": "📋 Sao chép",
        "btn_clear": "🗑️ Xóa",
        "related_header": "Công cụ liên quan",
        "related_json": "Trình định dạng JSON",
        "related_sql": "Định dạng SQL",
        "related_pw": "Tạo mật khẩu",
        "alert_encode_error": "Lỗi mã hóa: ",
        "alert_decode_error": "Lỗi giải mã: ",
        "alert_copy_empty": "Không có gì để sao chép."
    },
    "th": {
        "title": "ตัวแปลง Base64",
        "meta_title": "ตัวแปลง Base64 เข้ารหัส/ถอดรหัส - Utilify",
        "meta_desc": "เข้ารหัสหรือถอดรหัสข้อความไปยัง Base64",
        "og_title": "ตัวแปลง Base64 เข้ารหัส/ถอดรหัส - Utilify",
        "og_desc": "เข้ารหัสหรือถอดรหัสข้อความไปยัง Base64",
        "page_desc": "เข้ารหัสหรือถอดรหัสข้อความไปยัง Base64",
        "label_input": "ข้อความนำเข้า",
        "label_output": "ผลลัพธ์",
        "ph_input": "ป้อนข้อความเพื่อเข้ารหัส",
        "btn_encode": "⬇️ เข้ารหัส",
        "btn_decode": "⬆️ ถอดรหัส",
        "btn_copy": "📋 คัดลอก",
        "btn_clear": "🗑️ ล้าง",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_json": "ตัวจัดรูปแบบ JSON",
        "related_sql": "ตัวจัดรูปแบบ SQL",
        "related_pw": "ตัวสร้างรหัสผ่าน",
        "alert_encode_error": "ข้อผิดพลาดการเข้ารหัส: ",
        "alert_decode_error": "ข้อผิดพลาดการถอดรหัส: ",
        "alert_copy_empty": "ไม่มีอะไรให้คัดลอก"
    },
    "de": {
        "title": "Base64 Konverter",
        "meta_title": "Base64 Encoder/Decoder - Utilify",
        "meta_desc": "Text in Base64 kodieren oder dekodieren.",
        "og_title": "Base64 Encoder/Decoder - Utilify",
        "og_desc": "Text in Base64 kodieren oder dekodieren.",
        "page_desc": "Text in Base64 kodieren oder dekodieren.",
        "label_input": "Eingabetext",
        "label_output": "Ausgabeergebnis",
        "ph_input": "Text zum Kodieren eingeben",
        "btn_encode": "⬇️ Kodieren",
        "btn_decode": "⬆️ Dekodieren",
        "btn_copy": "📋 Kopieren",
        "btn_clear": "🗑️ Löschen",
        "related_header": "Ähnliche Tools",
        "related_json": "JSON Formatierer",
        "related_sql": "SQL-Formatierer",
        "related_pw": "Passwort Generator",
        "alert_encode_error": "Kodierungsfehler: ",
        "alert_decode_error": "Dekodierungsfehler: ",
        "alert_copy_empty": "Nichts zu kopieren."
    },
    "pt": {
        "title": "Conversor Base64",
        "meta_title": "Codificador/Decodificador Base64 - Utilify",
        "meta_desc": "Codificar ou decodificar texto para Base64.",
        "og_title": "Codificador/Decodificador Base64 - Utilify",
        "og_desc": "Codificar ou decodificar texto para Base64.",
        "page_desc": "Codificar ou decodificar texto para Base64.",
        "label_input": "Texto de Entrada",
        "label_output": "Resultado de Saída",
        "ph_input": "Digite o texto para codificar",
        "btn_encode": "⬇️ Codificar",
        "btn_decode": "⬆️ Decodificar",
        "btn_copy": "📋 Copiar",
        "btn_clear": "🗑️ Limpar",
        "related_header": "Ferramentas Relacionadas",
        "related_json": "Formatador JSON",
        "related_sql": "Formatador SQL",
        "related_pw": "Gerador de Senha",
        "alert_encode_error": "Erro de Codificação: ",
        "alert_decode_error": "Erro de Decodificação: ",
        "alert_copy_empty": "Nada para copiar."
    },
    "id": {
        "title": "Konverter Base64",
        "meta_title": "Enkoder/Dekoder Base64 - Utilify",
        "meta_desc": "Enkode atau dekode teks ke Base64.",
        "og_title": "Enkoder/Dekoder Base64 - Utilify",
        "og_desc": "Enkode atau dekode teks ke Base64.",
        "page_desc": "Enkode atau dekode teks ke Base64.",
        "label_input": "Teks Input",
        "label_output": "Hasil Output",
        "ph_input": "Masukkan teks untuk dienkode",
        "btn_encode": "⬇️ Enkode",
        "btn_decode": "⬆️ Dekode",
        "btn_copy": "📋 Salin",
        "btn_clear": "🗑️ Bersihkan",
        "related_header": "Alat Terkait",
        "related_json": "Pemformat JSON",
        "related_sql": "Pemformat SQL",
        "related_pw": "Generator Kata Sandi",
        "alert_encode_error": "Kesalahan Enkode: ",
        "alert_decode_error": "Kesalahan Dekode: ",
        "alert_copy_empty": "Tidak ada yang bisa disalin."
    },
    "hi": {
        "title": "Base64 कनवर्टर",
        "meta_title": "Base64 एनकोडर/डिकोडर - Utilify",
        "meta_desc": "टेक्स्ट को Base64 में एनकोड या डिकोड करें।",
        "og_title": "Base64 एनकोडर/डिकोडर - Utilify",
        "og_desc": "टेक्स्ट को Base64 में एनकोड या डिकोड करें।",
        "page_desc": "टेक्स्ट को Base64 में एनकोड या डिकोड करें।",
        "label_input": "इनपुट टेक्स्ट",
        "label_output": "आउटपुट परिणाम",
        "ph_input": "एनकोड करने के लिए टेक्स्ट दर्ज करें",
        "btn_encode": "⬇️ एनकोड",
        "btn_decode": "⬆️ डिकोड",
        "btn_copy": "📋 कॉपी करें",
        "btn_clear": "🗑️ साफ़ करें",
        "related_header": "संबंधित उपकरण",
        "related_json": "JSON फॉर्मेटर",
        "related_sql": "SQL फॉर्मेटर",
        "related_pw": "पासवर्ड जेनरेटर",
        "alert_encode_error": "एनकोडिंग त्रुटि: ",
        "alert_decode_error": "डिकोडिंग त्रुटि: ",
        "alert_copy_empty": "कॉपी करने के लिए कुछ नहीं।"
    }
}

PASSWORD_GENERATOR = {
    "en": {
        "title": "Strong Password Generator",
        "meta_title": "Strong Password Generator - Utilify",
        "meta_desc": "Generate strong and secure passwords. Passwords are generated locally and never sent to a server. (Processed securely in client-side)",
        "og_title": "Strong Password Generator - Utilify",
        "og_desc": "Generate strong and secure passwords. Passwords are generated locally and never sent to a server.",
        "json_name": "Strong Password Generator",
        "json_desc": "Generate strong and secure passwords. Passwords are generated locally and never sent to a server.",
        "page_desc": "Generate strong and secure passwords. Passwords are generated locally and never sent to a server.",
        "adsense_text": "Ad Space",
        "label_generated": "Generated Password",
        "btn_copy": "Copy",
        "label_length": "Password Length:",
        "label_options": "Options",
        "opt_upper": "Uppercase (A-Z)",
        "opt_lower": "Lowercase (a-z)",
        "opt_number": "Numbers (0-9)",
        "opt_symbol": "Symbols (@#$%)",
        "btn_generate": "Generate Password",
        "security_note": "🔒 All passwords are generated in your browser and verify sent remotely.",
        "related_header": "Related Tools",
        "related_json": "JSON Formatter",
        "related_sql": "SQL Formatter",
        "related_base64": "Base64 Converter",
        "ph_select": "Select Option"
    },
    "ko": {
        "title": "안전한 비밀번호 생성기",
        "meta_title": "안전한 비밀번호 생성기 - Utilify",
        "meta_desc": "강력하고 안전한 비밀번호를 생성하세요. 생성된 비밀번호는 서버로 전송되지 않습니다 (100% 클라이언트 처리). (Processed securely in client-side)",
        "og_title": "안전한 비밀번호 생성기 - Utilify",
        "og_desc": "강력하고 안전한 비밀번호를 생성하세요. 생성된 비밀번호는 서버로 전송되지 않습니다 (100% 클라이언트 처리).",
        "json_name": "안전한 비밀번호 생성기",
        "json_desc": "강력하고 안전한 비밀번호를 생성하세요. 생성된 비밀번호는 서버로 전송되지 않습니다 (100% 클라이언트 처리).",
        "page_desc": "강력하고 안전한 비밀번호를 생성하세요. 생성된 비밀번호는 서버로 전송되지 않습니다 (100% 클라이언트 처리).",
        "adsense_text": "광고 영역",
        "label_generated": "생성된 비밀번호",
        "btn_copy": "복사",
        "label_length": "비밀번호 길이:",
        "label_options": "옵션",
        "opt_upper": "대문자 포함 (A-Z)",
        "opt_lower": "소문자 포함 (a-z)",
        "opt_number": "숫자 포함 (0-9)",
        "opt_symbol": "특수문자 포함 (@#$%)",
        "btn_generate": "비밀번호 생성",
        "security_note": "🔒 모든 비밀번호는 브라우저에서 생성되며 외부로 전송되지 않습니다.",
        "related_header": "함께 보면 좋은 도구",
        "related_json": "JSON 포매터",
        "related_sql": "SQL 포매터",
        "related_base64": "Base64 변환기",
        "ph_select": "Select Option"
    },
    "zh-cn": {
        "title": "强密码生成器",
        "meta_title": "强密码生成器 - Utilify",
        "meta_desc": "生成强大且安全的密码。密码在本地生成，绝不发送到服务器。（客户端安全处理）",
        "og_title": "强密码生成器 - Utilify",
        "og_desc": "生成强大且安全的密码。密码在本地生成，绝不发送到服务器。",
        "json_name": "强密码生成器",
        "json_desc": "生成强大且安全的密码。密码在本地生成，绝不发送到服务器。",
        "page_desc": "生成强大且安全的密码。密码在本地生成，绝不发送到服务器。",
        "adsense_text": "广告位",
        "label_generated": "生成的密码",
        "btn_copy": "复制",
        "label_length": "密码长度:",
        "label_options": "选项",
        "opt_upper": "大写字母 (A-Z)",
        "opt_lower": "小写字母 (a-z)",
        "opt_number": "数字 (0-9)",
        "opt_symbol": "符号 (@#$%)",
        "btn_generate": "生成密码",
        "security_note": "🔒 所有密码均在您的浏览器中生成，不会远程发送。",
        "related_header": "相关工具",
        "related_json": "JSON 格式化",
        "related_sql": "SQL 格式化",
        "related_base64": "Base64 转换器",
        "ph_select": "选择选项"
    },
    "zh-tw": {
        "title": "強密碼生成器",
        "meta_title": "強密碼生成器 - Utilify",
        "meta_desc": "生成強大且安全的密碼。密碼在本地生成，絕不發送到服務器。（客戶端安全處理）",
        "og_title": "強密碼生成器 - Utilify",
        "og_desc": "生成強大且安全的密碼。密碼在本地生成，絕不發送到服務器。",
        "json_name": "強密碼生成器",
        "json_desc": "生成強大且安全的密碼。密碼在本地生成，絕不發送到服務器。",
        "page_desc": "生成強大且安全的密碼。密碼在本地生成，絕不發送到服務器。",
        "adsense_text": "廣告位",
        "label_generated": "生成的密碼",
        "btn_copy": "複製",
        "label_length": "密碼長度:",
        "label_options": "選項",
        "opt_upper": "大寫字母 (A-Z)",
        "opt_lower": "小寫字母 (a-z)",
        "opt_number": "數字 (0-9)",
        "opt_symbol": "符號 (@#$%)",
        "btn_generate": "生成密碼",
        "security_note": "🔒 所有密碼均在您的瀏覽器中生成，不會遠程發送。",
        "related_header": "相關工具",
        "related_json": "JSON 格式化",
        "related_sql": "SQL 格式化",
        "related_base64": "Base64 轉換器",
        "ph_select": "選擇選項"
    },
    "ja": {
        "title": "強力なパスワード生成ツール",
        "meta_title": "強力なパスワード生成ツール - Utilify",
        "meta_desc": "強力で安全なパスワードを生成します。パスワードはローカルで生成され、サーバーに送信されることはありません（クライアントサイドで安全に処理）。",
        "og_title": "強力なパスワード生成ツール - Utilify",
        "og_desc": "強力で安全なパスワードを生成します。パスワードはローカルで生成され、サーバーに送信されることはありません。",
        "json_name": "強力なパスワード生成ツール",
        "json_desc": "強力で安全なパスワードを生成します。パスワードはローカルで生成され、サーバーに送信されることはありません。",
        "page_desc": "強力で安全なパスワードを生成します。パスワードはローカルで生成され、サーバーに送信されることはありません。",
        "adsense_text": "広告スペース",
        "label_generated": "生成されたパスワード",
        "btn_copy": "コピー",
        "label_length": "パスワードの長さ:",
        "label_options": "オプション",
        "opt_upper": "大文字 (A-Z)",
        "opt_lower": "小文字 (a-z)",
        "opt_number": "数字 (0-9)",
        "opt_symbol": "記号 (@#$%)",
        "btn_generate": "パスワードを生成",
        "security_note": "🔒 すべてのパスワードはブラウザ内で生成され、外部に送信されることはありません。",
        "related_header": "関連ツール",
        "related_json": "JSONフォーマッター",
        "related_sql": "SQLフォーマッター",
        "related_base64": "Base64変換",
        "ph_select": "オプションを選択"
    },
    "vi": {
        "title": "Trình tạo mật khẩu mạnh",
        "meta_title": "Trình tạo mật khẩu mạnh - Utilify",
        "meta_desc": "Tạo mật khẩu mạnh và an toàn. Mật khẩu được tạo cục bộ và không bao giờ gửi đến máy chủ. (Xử lý an toàn phía máy khách)",
        "og_title": "Trình tạo mật khẩu mạnh - Utilify",
        "og_desc": "Tạo mật khẩu mạnh và an toàn. Mật khẩu được tạo cục bộ và không bao giờ gửi đến máy chủ.",
        "json_name": "Trình tạo mật khẩu mạnh",
        "json_desc": "Tạo mật khẩu mạnh và an toàn. Mật khẩu được tạo cục bộ và không bao giờ gửi đến máy chủ.",
        "page_desc": "Tạo mật khẩu mạnh và an toàn. Mật khẩu được tạo cục bộ và không bao giờ gửi đến máy chủ.",
        "adsense_text": "Không gian quảng cáo",
        "label_generated": "Mật khẩu đã tạo",
        "btn_copy": "Sao chép",
        "label_length": "Độ dài mật khẩu:",
        "label_options": "Tùy chọn",
        "opt_upper": "Chữ hoa (A-Z)",
        "opt_lower": "Chữ thường (a-z)",
        "opt_number": "Số (0-9)",
        "opt_symbol": "Ký hiệu (@#$%)",
        "btn_generate": "Tạo mật khẩu",
        "security_note": "🔒 Tất cả mật khẩu được tạo trong trình duyệt của bạn và không gửi đi xa.",
        "related_header": "Công cụ liên quan",
        "related_json": "Trình định dạng JSON",
        "related_sql": "Định dạng SQL",
        "related_base64": "Chuyển đổi Base64",
        "ph_select": "Chọn Tùy chọn"
    },
    "th": {
        "title": "ตัวสร้างรหัสผ่านที่รัดกุม",
        "meta_title": "ตัวสร้างรหัสผ่านที่รัดกุม - Utilify",
        "meta_desc": "สร้างรหัสผ่านที่รัดกุมและปลอดภัย รหัสผ่านถูกสร้างขึ้นในเครื่องและไม่ส่งไปยังเซิร์ฟเวอร์ (ประมวลผลอย่างปลอดภัยในฝั่งไคลเอ็นต์)",
        "og_title": "ตัวสร้างรหัสผ่านที่รัดกุม - Utilify",
        "og_desc": "สร้างรหัสผ่านที่รัดกุมและปลอดภัย รหัสผ่านถูกสร้างขึ้นในเครื่องและไม่ส่งไปยังเซิร์ฟเวอร์",
        "json_name": "ตัวสร้างรหัสผ่านที่รัดกุม",
        "json_desc": "สร้างรหัสผ่านที่รัดกุมและปลอดภัย รหัสผ่านถูกสร้างขึ้นในเครื่องและไม่ส่งไปยังเซิร์ฟเวอร์",
        "page_desc": "สร้างรหัสผ่านที่รัดกุมและปลอดภัย รหัสผ่านถูกสร้างขึ้นในเครื่องและไม่ส่งไปยังเซิร์ฟเวอร์",
        "adsense_text": "พื้นที่โฆษณา",
        "label_generated": "รหัสผ่านที่สร้างขึ้น",
        "btn_copy": "คัดลอก",
        "label_length": "ความยาวรหัสผ่าน:",
        "label_options": "ตัวเลือก",
        "opt_upper": "ตัวพิมพ์ใหญ่ (A-Z)",
        "opt_lower": "ตัวพิมพ์เล็ก (a-z)",
        "opt_number": "ตัวเลข (0-9)",
        "opt_symbol": "สัญลักษณ์ (@#$%)",
        "btn_generate": "สร้างรหัสผ่าน",
        "security_note": "🔒 รหัสผ่านทั้งหมดถูกสร้างขึ้นในเบราว์เซอร์ของคุณและไม่ส่งออกไป",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_json": "ตัวจัดรูปแบบ JSON",
        "related_sql": "ตัวจัดรูปแบบ SQL",
        "related_base64": "ตัวแปลง Base64",
        "ph_select": "เลือกตัวเลือก"
    },
    "de": {
        "title": "Starker Passwort Generator",
        "meta_title": "Starker Passwort Generator - Utilify",
        "meta_desc": "Erstellen Sie starke und sichere Passwörter. Passwörter werden lokal erstellt und niemals an einen Server gesendet. (Sicher clientseitig verarbeitet)",
        "og_title": "Starker Passwort Generator - Utilify",
        "og_desc": "Erstellen Sie starke und sichere Passwörter. Passwörter werden lokal erstellt und niemals an einen Server gesendet.",
        "json_name": "Starker Passwort Generator",
        "json_desc": "Erstellen Sie starke und sichere Passwörter. Passwörter werden lokal erstellt und niemals an einen Server gesendet.",
        "page_desc": "Erstellen Sie starke und sichere Passwörter. Passwörter werden lokal erstellt und niemals an einen Server gesendet.",
        "adsense_text": "Werbefläche",
        "label_generated": "Erstelltes Passwort",
        "btn_copy": "Kopieren",
        "label_length": "Passwortlänge:",
        "label_options": "Optionen",
        "opt_upper": "Großbuchstaben (A-Z)",
        "opt_lower": "Kleinbuchstaben (a-z)",
        "opt_number": "Zahlen (0-9)",
        "opt_symbol": "Symbole (@#$%)",
        "btn_generate": "Passwort erstellen",
        "security_note": "🔒 Alle Passwörter werden in Ihrem Browser erstellt und nicht gesendet.",
        "related_header": "Ähnliche Tools",
        "related_json": "JSON Formatierer",
        "related_sql": "SQL-Formatierer",
        "related_base64": "Base64 Konverter",
        "ph_select": "Option auswählen"
    },
    "pt": {
        "title": "Gerador de Senha Forte",
        "meta_title": "Gerador de Senha Forte - Utilify",
        "meta_desc": "Gere senhas fortes e seguras. As senhas são geradas localmente e nunca enviadas a um servidor. (Processado com segurança no cliente)",
        "og_title": "Gerador de Senha Forte - Utilify",
        "og_desc": "Gere senhas fortes e seguras. As senhas são geradas localmente e nunca enviadas a um servidor.",
        "json_name": "Gerador de Senha Forte",
        "json_desc": "Gere senhas fortes e seguras. As senhas são geradas localmente e nunca enviadas a um servidor.",
        "page_desc": "Gere senhas fortes e seguras. As senhas são geradas localmente e nunca enviadas a um servidor.",
        "adsense_text": "Espaço Publicitário",
        "label_generated": "Senha Gerada",
        "btn_copy": "Copiar",
        "label_length": "Comprimento da Senha:",
        "label_options": "Opções",
        "opt_upper": "Maiúsculas (A-Z)",
        "opt_lower": "Minúsculas (a-z)",
        "opt_number": "Números (0-9)",
        "opt_symbol": "Símbolos (@#$%)",
        "btn_generate": "Gerar Senha",
        "security_note": "🔒 Todas as senhas são geradas no seu navegador e não enviadas externamente.",
        "related_header": "Ferramentas Relacionadas",
        "related_json": "Formatador JSON",
        "related_sql": "Formatador SQL",
        "related_base64": "Conversor Base64",
        "ph_select": "Selecionar Opção"
    },
    "id": {
        "title": "Generator Kata Sandi Kuat",
        "meta_title": "Generator Kata Sandi Kuat - Utilify",
        "meta_desc": "Hasilkan kata sandi kuat dan aman. Kata sandi dibuat secara lokal dan tidak pernah dikirim ke server. (Diproses aman di sisi klien)",
        "og_title": "Generator Kata Sandi Kuat - Utilify",
        "og_desc": "Hasilkan kata sandi kuat dan aman. Kata sandi dibuat secara lokal dan tidak pernah dikirim ke server.",
        "json_name": "Generator Kata Sandi Kuat",
        "json_desc": "Hasilkan kata sandi kuat dan aman. Kata sandi dibuat secara lokal dan tidak pernah dikirim ke server.",
        "page_desc": "Hasilkan kata sandi kuat dan aman. Kata sandi dibuat secara lokal dan tidak pernah dikirim ke server.",
        "adsense_text": "Ruang Iklan",
        "label_generated": "Kata Sandi Dibuat",
        "btn_copy": "Salin",
        "label_length": "Panjang Kata Sandi:",
        "label_options": "Opsi",
        "opt_upper": "Huruf Besar (A-Z)",
        "opt_lower": "Huruf Kecil (a-z)",
        "opt_number": "Angka (0-9)",
        "opt_symbol": "Simbol (@#$%)",
        "btn_generate": "Hasilkan Kata Sandi",
        "security_note": "🔒 Semua kata sandi dibuat di browser Anda dan tidak dikirim dari jarak jauh.",
        "related_header": "Alat Terkait",
        "related_json": "Pemformat JSON",
        "related_sql": "Pemformat SQL",
        "related_base64": "Konverter Base64",
        "ph_select": "Pilih Opsi"
    },
    "hi": {
        "title": "मजबूत पासवर्ड जेनरेटर",
        "meta_title": "मजबूत पासवर्ड जेनरेटर - Utilify",
        "meta_desc": "मजबूत और सुरक्षित पासवर्ड बनाएं। पासवर्ड स्थानीय रूप से बनाए जाते हैं और कभी भी सर्वर पर नहीं भेजे जाते हैं। (क्लाइंट-साइड में सुरक्षित रूप से संसाधित)",
        "og_title": "मजबूत पासवर्ड जेनरेटर - Utilify",
        "og_desc": "मजबूत और सुरक्षित पासवर्ड बनाएं। पासवर्ड स्थानीय रूप से बनाए जाते हैं और कभी भी सर्वर पर नहीं भेजे जाते हैं।",
        "json_name": "मजबूत पासवर्ड जेनरेटर",
        "json_desc": "मजबूत और सुरक्षित पासवर्ड बनाएं। पासवर्ड स्थानीय रूप से बनाए जाते हैं और कभी भी सर्वर पर नहीं भेजे जाते हैं।",
        "page_desc": "मजबूत और सुरक्षित पासवर्ड बनाएं। पासवर्ड स्थानीय रूप से बनाए जाते हैं और कभी भी सर्वर पर नहीं भेजे जाते हैं।",
        "adsense_text": "विज्ञापन स्थान",
        "label_generated": "जेनरेट किया गया पासवर्ड",
        "btn_copy": "कॉपी करें",
        "label_length": "पासवर्ड की लंबाई:",
        "label_options": "विकल्प",
        "opt_upper": "बड़े अक्षर (A-Z)",
        "opt_lower": "छोटे अक्षर (a-z)",
        "opt_number": "संख्याएं (0-9)",
        "opt_symbol": "प्रतीक (@#$%)",
        "btn_generate": "पासवर्ड बनाएं",
        "security_note": "🔒 सभी पासवर्ड आपके ब्राउज़र में बनाए जाते हैं और दूरस्थ रूप से नहीं भेजे जाते हैं।",
        "related_header": "संबंधित उपकरण",
        "related_json": "JSON फॉर्मेटर",
        "related_sql": "SQL फॉर्मेटर",
        "related_base64": "Base64 कनवर्टर",
        "ph_select": "विकल्प चुनें"
    }
}

UNIT_CONVERTER = {
    "en": {
        "title": "Unit Converter",
        "meta_title": "Unit Converter (cm to inch, kg to lbs) - Utilify",
        "meta_desc": "Convert Length (cm to inch), Weight (kg to lbs), Temperature (Celsius to Fahrenheit), Volume, and more. Easy height and weight conversion.",
        "og_title": "Unit Converter (cm to inch, kg to lbs) - 🛠️ Utilify",
        "og_desc": "Convert Length (cm to inch), Weight (kg to lbs), Temperature (Celsius to Fahrenheit), Volume, and more.",
        "json_name": "Unit Converter",
        "json_desc": "Convert Length, Weight, Temperature, Volume, and more.",
        "page_desc": "Convert Length, Weight, Temperature, Volume, and more.",
        "label_category": "Category",
        "opt_length": "Length",
        "opt_weight": "Weight",
        "opt_temperature": "Temperature",
        "opt_volume": "Volume",
        "opt_area": "Area",
        "opt_speed": "Speed",
        "label_from": "Value to Convert",
        "ph_from": "Enter number",
        "btn_swap": "Swap Units",
        "label_to": "Converted Value",
        "ph_to": "Result",
        "header_quick": "Common Conversions",
        "related_header": "Related Tools",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_timer": "Timer",
        "related_reaction": "Reaction Test"
    },
    "ko": {
        "title": "단위 변환기",
        "meta_title": "단위 변환기 (cm to inch, kg to lbs) - Utilify",
        "meta_desc": "길이(cm to inch), 무게(kg to lbs), 온도(섭씨 화씨), 부피 등 다양한 단위를 간편하게 변환하세요. 키 변환, 평수 계산 등 실생활 단위 변환.",
        "og_title": "단위 변환기 (cm to inch, kg to lbs) - Utilify",
        "og_desc": "길이(cm to inch), 무게(kg to lbs), 온도(섭씨 화씨) 등 다양한 단위를 간편하게 변환하세요.",
        "json_name": "단위 변환기",
        "json_desc": "길이, 무게, 온도, 부피 등 다양한 단위를 간편하게 변환하세요.",
        "page_desc": "길이, 무게, 온도, 부피 등 다양한 단위를 간편하게 변환하세요.",
        "label_category": "변환 카테고리",
        "opt_length": "길이",
        "opt_weight": "무게",
        "opt_temperature": "온도",
        "opt_volume": "부피",
        "opt_area": "면적",
        "opt_speed": "속도",
        "label_from": "변환할 값",
        "ph_from": "숫자 입력",
        "btn_swap": "단위 교환",
        "label_to": "변환된 값",
        "ph_to": "결과",
        "header_quick": "자주 사용하는 변환",
        "related_header": "함께 보면 좋은 도구",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_timer": "타이머",
        "related_reaction": "반응 속도"
    },
    "zh-cn": {
        "title": "单位转换器",
        "meta_title": "单位转换器 (厘米转英寸, 公斤转磅) - Utilify",
        "meta_desc": "转换长度 (厘米转英寸), 重量 (公斤转磅), 温度 (摄氏度转华氏度), 体积等。轻松进行身高和体重转换。",
        "og_title": "单位转换器 - Utilify",
        "og_desc": "转换长度, 重量, 温度, 体积等。",
        "json_name": "单位转换器",
        "json_desc": "转换长度, 重量, 温度, 体积等。",
        "page_desc": "转换长度, 重量, 温度, 体积等。",
        "label_category": "转换类别",
        "opt_length": "长度",
        "opt_weight": "重量",
        "opt_temperature": "温度",
        "opt_volume": "体积",
        "opt_area": "面积",
        "opt_speed": "速度",
        "label_from": "要转换的值",
        "ph_from": "输入数字",
        "btn_swap": "交换单位",
        "label_to": "转换后的值",
        "ph_to": "结果",
        "header_quick": "常用转换",
        "related_header": "相关工具",
        "related_bmi": "BMI 计算器",
        "related_date": "日期计算器",
        "related_timer": "计时器",
        "related_reaction": "反应测试"
    },
    "zh-tw": {
        "title": "單位轉換器",
        "meta_title": "單位轉換器 (公分轉英寸, 公斤轉磅) - Utilify",
        "meta_desc": "轉換長度 (公分轉英寸), 重量 (公斤轉磅), 溫度 (攝氏轉華氏), 體積等。輕鬆進行身高和體重轉換。",
        "og_title": "單位轉換器 - Utilify",
        "og_desc": "轉換長度, 重量, 溫度, 體積等。",
        "json_name": "單位轉換器",
        "json_desc": "轉換長度, 重量, 溫度, 體積等。",
        "page_desc": "轉換長度, 重量, 溫度, 體積等。",
        "label_category": "轉換類別",
        "opt_length": "長度",
        "opt_weight": "重量",
        "opt_temperature": "溫度",
        "opt_volume": "體積",
        "opt_area": "面積",
        "opt_speed": "速度",
        "label_from": "要轉換的值",
        "ph_from": "輸入數字",
        "btn_swap": "交換單位",
        "label_to": "轉換後的值",
        "ph_to": "結果",
        "header_quick": "常用轉換",
        "related_header": "相關工具",
        "related_bmi": "BMI 計算器",
        "related_date": "日期計算器",
        "related_timer": "計時器",
        "related_reaction": "反應測試"
    },
    "ja": {
        "title": "単位変換ツール",
        "meta_title": "単位変換ツール (cm to inch, kg to lbs) - Utilify",
        "meta_desc": "長さ (cmからインチ), 重量 (kgからポンド), 温度 (摂氏から華氏), 体積などを変換します。身長や体重の変換も簡単。",
        "og_title": "単位変換ツール - Utilify",
        "og_desc": "長さ, 重量, 温度, 体積などを変換できます。",
        "json_name": "単位変換ツール",
        "json_desc": "長さ, 重量, 温度, 体積などを変換できます。",
        "page_desc": "長さ, 重量, 温度, 体積などを変換できます。",
        "label_category": "カテゴリー",
        "opt_length": "長さ",
        "opt_weight": "重量",
        "opt_temperature": "温度",
        "opt_volume": "体積",
        "opt_area": "面積",
        "opt_speed": "速度",
        "label_from": "変換する値",
        "ph_from": "数値を入力",
        "btn_swap": "単位を交換",
        "label_to": "変換結果",
        "ph_to": "結果",
        "header_quick": "よく使う変換",
        "related_header": "関連ツール",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算",
        "related_timer": "タイマー",
        "related_reaction": "反応速度テスト"
    },
    "vi": {
        "title": "Chuyển đổi đơn vị",
        "meta_title": "Chuyển đổi đơn vị (cm sang inch, kg sang lbs) - Utilify",
        "meta_desc": "Chuyển đổi Chiều dài (cm sang inch), Cân nặng (kg sang lbs), Nhiệt độ (Độ C sang Độ F), Thể tích, và hơn thế nữa. Chuyển đổi chiều cao và cân nặng dễ dàng.",
        "og_title": "Chuyển đổi đơn vị - Utilify",
        "og_desc": "Chuyển đổi Chiều dài, Cân nặng, Nhiệt độ, Thể tích, và hơn thế nữa.",
        "json_name": "Chuyển đổi đơn vị",
        "json_desc": "Chuyển đổi Chiều dài, Cân nặng, Nhiệt độ, Thể tích, và hơn thế nữa.",
        "page_desc": "Chuyển đổi Chiều dài, Cân nặng, Nhiệt độ, Thể tích, và hơn thế nữa.",
        "label_category": "Danh mục",
        "opt_length": "Chiều dài",
        "opt_weight": "Cân nặng",
        "opt_temperature": "Nhiệt độ",
        "opt_volume": "Thể tích",
        "opt_area": "Diện tích",
        "opt_speed": "Tốc độ",
        "label_from": "Giá trị cần chuyển đổi",
        "ph_from": "Nhập số",
        "btn_swap": "Đổi đơn vị",
        "label_to": "Giá trị đã chuyển đổi",
        "ph_to": "Kết quả",
        "header_quick": "Chuyển đổi phổ biến",
        "related_header": "Công cụ liên quan",
        "related_bmi": "Máy tính BMI",
        "related_date": "Máy tính ngày",
        "related_timer": "Hẹn giờ",
        "related_reaction": "Kiểm tra phản xạ"
    },
    "th": {
        "title": "เครื่องมือแปลงหน่วย",
        "meta_title": "เครื่องมือแปลงหน่วย (ซม. เป็น นิ้ว, กก. เป็น ปอนด์) - Utilify",
        "meta_desc": "แปลงความยาว (ซม. เป็น นิ้ว), น้ำหนัก (กก. เป็น ปอนด์), อุณหภูมิ (เซลเซียส เป็น ฟาเรนไฮต์), ปริมาตร และอื่นๆ แปลงส่วนสูงและน้ำหนักได้ง่าย",
        "og_title": "เครื่องมือแปลงหน่วย - Utilify",
        "og_desc": "แปลงความยาว, น้ำหนัก, อุณหภูมิ, ปริมาตร และอื่นๆ",
        "json_name": "เครื่องมือแปลงหน่วย",
        "json_desc": "แปลงความยาว, น้ำหนัก, อุณหภูมิ, ปริมาตร และอื่นๆ",
        "page_desc": "แปลงความยาว, น้ำหนัก, อุณหภูมิ, ปริมาตร และอื่นๆ",
        "label_category": "หมวดหมู่",
        "opt_length": "ความยาว",
        "opt_weight": "น้ำหนัก",
        "opt_temperature": "อุณหภูมิ",
        "opt_volume": "ปริมาตร",
        "opt_area": "พื้นที่",
        "opt_speed": "ความเร็ว",
        "label_from": "ค่าที่จะแปลง",
        "ph_from": "ป้อนตัวเลข",
        "btn_swap": "สลับหน่วย",
        "label_to": "ค่าที่แปลงแล้ว",
        "ph_to": "ผลลัพธ์",
        "header_quick": "การแปลงทั่วไป",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_bmi": "เครื่องคำนวณ BMI",
        "related_date": "เครื่องคำนวณวันที่",
        "related_timer": "ตัวจับเวลา",
        "related_reaction": "ทดสอบปฏิกิริยา"
    },
    "de": {
        "title": "Einheitenumrechner",
        "meta_title": "Einheitenumrechner (cm in Zoll, kg in Pfund) - Utilify",
        "meta_desc": "Konvertieren Sie Länge (cm in Zoll), Gewicht (kg in Pfund), Temperatur (Celsius in Fahrenheit), Volumen und mehr. Einfache Größen- und Gewichtsumrechnung.",
        "og_title": "Einheitenumrechner - Utilify",
        "og_desc": "Konvertieren Sie Länge, Gewicht, Temperatur, Volumen und mehr.",
        "json_name": "Einheitenumrechner",
        "json_desc": "Konvertieren Sie Länge, Gewicht, Temperatur, Volumen und mehr.",
        "page_desc": "Konvertieren Sie Länge, Gewicht, Temperatur, Volumen und mehr.",
        "label_category": "Kategorie",
        "opt_length": "Länge",
        "opt_weight": "Gewicht",
        "opt_temperature": "Temperatur",
        "opt_volume": "Volumen",
        "opt_area": "Fläche",
        "opt_speed": "Geschwindigkeit",
        "label_from": "Wert zum Umrechnen",
        "ph_from": "Zahl eingeben",
        "btn_swap": "Einheiten tauschen",
        "label_to": "Umgerechneter Wert",
        "ph_to": "Ergebnis",
        "header_quick": "Häufige Umrechnungen",
        "related_header": "Ähnliche Tools",
        "related_bmi": "BMI Rechner",
        "related_date": "Datumsrechner",
        "related_timer": "Timer",
        "related_reaction": "Reaktionstest"
    },
    "pt": {
        "title": "Conversor de Unidades",
        "meta_title": "Conversor de Unidades (cm para polegada, kg para lbs) - Utilify",
        "meta_desc": "Converta Comprimento (cm para polegada), Peso (kg para lbs), Temperatura (Celsius para Fahrenheit), Volume e mais. Conversão fácil de altura e peso.",
        "og_title": "Conversor de Unidades - Utilify",
        "og_desc": "Converta Comprimento, Peso, Temperatura, Volume e mais.",
        "json_name": "Conversor de Unidades",
        "json_desc": "Converta Comprimento, Peso, Temperatura, Volume e mais.",
        "page_desc": "Converta Comprimento, Peso, Temperatura, Volume e mais.",
        "label_category": "Categoria",
        "opt_length": "Comprimento",
        "opt_weight": "Peso",
        "opt_temperature": "Temperatura",
        "opt_volume": "Volume",
        "opt_area": "Área",
        "opt_speed": "Velocidade",
        "label_from": "Valor para Converter",
        "ph_from": "Digite o número",
        "btn_swap": "Trocar Unidades",
        "label_to": "Valor Convertido",
        "ph_to": "Resultado",
        "header_quick": "Conversões Comuns",
        "related_header": "Ferramentas Relacionadas",
        "related_bmi": "Calculadora de IMC",
        "related_date": "Calculadora de Data",
        "related_timer": "Cronômetro",
        "related_reaction": "Teste de Reação"
    },
    "id": {
        "title": "Konverter Unit",
        "meta_title": "Konverter Unit (cm ke inci, kg ke lbs) - Utilify",
        "meta_desc": "Konversi Panjang (cm ke inci), Berat (kg ke lbs), Suhu (Celcius ke Fahrenheit), Volume, dan banyak lagi. Konversi tinggi dan berat badan yang mudah.",
        "og_title": "Konverter Unit - Utilify",
        "og_desc": "Konversi Panjang, Berat, Suhu, Volume, dan banyak lagi.",
        "json_name": "Konverter Unit",
        "json_desc": "Konversi Panjang, Berat, Suhu, Volume, dan banyak lagi.",
        "page_desc": "Konversi Panjang, Berat, Suhu, Volume, dan banyak lagi.",
        "label_category": "Kategori",
        "opt_length": "Panjang",
        "opt_weight": "Berat",
        "opt_temperature": "Suhu",
        "opt_volume": "Volume",
        "opt_area": "Area",
        "opt_speed": "Kecepatan",
        "label_from": "Nilai untuk Dikonversi",
        "ph_from": "Masukkan angka",
        "btn_swap": "Tukar Unit",
        "label_to": "Nilai Dikonversi",
        "ph_to": "Hasil",
        "header_quick": "Konversi Umum",
        "related_header": "Alat Terkait",
        "related_bmi": "Kalkulator BMI",
        "related_date": "Kalkulator Tanggal",
        "related_timer": "Timer",
        "related_reaction": "Tes Reaksi"
    },
    "hi": {
        "title": "इकाई परिवर्तक",
        "meta_title": "इकाई परिवर्तक (सेमी से इंच, किग्रा से पाउंड) - Utilify",
        "meta_desc": "लंबाई (सेमी से इंच), वजन (किग्रा से पाउंड), तापमान (सेल्सियस से फारेनहाइट), आयतन और बहुत कुछ बदलें। आसान ऊंचाई और वजन रूपांतरण।",
        "og_title": "इकाई परिवर्तक - Utilify",
        "og_desc": "लंबाई, वजन, तापमान, आयतन और बहुत कुछ बदलें।",
        "json_name": "इकाई परिवर्तक",
        "json_desc": "लंबाई, वजन, तापमान, आयतन और बहुत कुछ बदलें।",
        "page_desc": "लंबाई, वजन, तापमान, आयतन और बहुत कुछ बदलें।",
        "label_category": "श्रेणी",
        "opt_length": "लंबाई",
        "opt_weight": "वजन",
        "opt_temperature": "तापमान",
        "opt_volume": "आयतन",
        "opt_area": "क्षेत्रफल",
        "opt_speed": "गति",
        "label_from": "बदलने के लिए मान",
        "ph_from": "संख्या दर्ज करें",
        "btn_swap": "इकाइलें बदलें",
        "label_to": "परिवर्तित मान",
        "ph_to": "परिणाम",
        "header_quick": "सामान्य रूपांतरण",
        "related_header": "संबंधित उपकरण",
        "related_bmi": "BMI कैलकुलेटर",
        "related_date": "दिनांक कैलकुलेटर",
        "related_timer": "टाइमर",
        "related_reaction": "प्रतिक्रिया परीक्षण"
    }
}

DIFF_CHECKER = {
    "en": {
        "title": "Text Diff Checker",
        "meta_title": "Text Diff Checker - Utilify",
        "meta_desc": "Compare two texts difference easily. Highlights added and removed parts.",
        "og_title": "Text Diff Checker - Utilify",
        "og_desc": "Compare two texts difference easily. Highlights added and removed parts.",
        "json_name": "Text Diff Checker",
        "json_desc": "Compare two texts difference easily. Highlights added and removed parts.",
        "page_desc": "Compare two texts difference easily. Highlights added and removed parts.",
        "adsense_text": "Ad Space",
        "label_orig": "Original Text",
        "ph_orig": "Enter original text here...",
        "label_changed": "Changed Text",
        "ph_changed": "Enter changed text here...",
        "btn_compare": "Compare",
        "btn_clear": "Clear",
        "header_result": "Comparison Result",
        "related_header": "Related Tools",
        "related_text": "Text Utils",
        "related_regex": "Regex Tester",
        "related_md": "Markdown Preview",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "No differences found."
    },
    "ko": {
        "title": "텍스트 비교기 (Diff Checker)",
        "meta_title": "텍스트 비교기 (Diff Checker) - Utilify",
        "meta_desc": "두 텍스트의 차이점을 쉽고 빠르게 비교하세요. 변경된 부분을 색깔로 표시해줍니다.",
        "og_title": "텍스트 비교기 (Diff Checker) - Utilify",
        "og_desc": "두 텍스트의 차이점을 쉽고 빠르게 비교하세요. 변경된 부분을 색깔로 표시해줍니다.",
        "json_name": "텍스트 비교기 (Diff Checker)",
        "json_desc": "두 텍스트의 차이점을 쉽고 빠르게 비교하세요. 변경된 부분을 색깔로 표시해줍니다.",
        "page_desc": "두 텍스트의 차이점을 쉽고 빠르게 비교하세요. 변경된 부분을 색깔로 표시해줍니다.",
        "adsense_text": "광고 영역",
        "label_orig": "원본 텍스트",
        "ph_orig": "여기에 원본 텍스트를 입력하세요...",
        "label_changed": "변경된 텍스트",
        "ph_changed": "여기에 변경된 텍스트를 입력하세요...",
        "btn_compare": "비교하기",
        "btn_clear": "지우기",
        "header_result": "비교 결과",
        "related_header": "함께 보면 좋은 도구",
        "related_text": "텍스트 유틸리티",
        "related_regex": "정규식 테스터",
        "related_md": "마크다운 미리보기",
        "related_lorem": "입숨 생성기",
        "msg_no_diff": "차이점이 없습니다."
    },
    "zh-cn": {
        "title": "文本差异对比",
        "meta_title": "文本差异对比工具 - Utilify",
        "meta_desc": "在线比较两个文本文件的差异。高亮显示变化、新增和删除的内容。",
        "og_title": "文本差异对比工具 - Utilify",
        "og_desc": "在线比较两个文本文件的差异。高亮显示变化。",
        "json_name": "文本差异对比",
        "json_desc": "在线比较两个文本文件的差异。",
        "page_desc": "在线比较两个文本文件的差异。高亮显示变化。",
        "label_original": "原始文本",
        "label_modified": "修改后文本",
        "btn_compare": "比较差异",
        "btn_clear": "清除",
        "header_result": "比较结果",
        "legend_add": "新增",
        "legend_remove": "删除",
        "related_header": "相关工具",
        "related_text": "文本工具箱",
        "related_md": "Markdown 预览",
        "related_regex": "正则表达式测试"
    },
    "zh-tw": {
        "title": "文本差異比對",
        "meta_title": "文本差異比對工具 - Utilify",
        "meta_desc": "線上比較兩個文本文件的差異。高亮顯示變化、新增和刪除的內容。",
        "og_title": "文本差異比對工具 - Utilify",
        "og_desc": "線上比較兩個文本文件的差異。高亮顯示變化。",
        "json_name": "文本差異比對",
        "json_desc": "線上比較兩個文本文件的差異。",
        "page_desc": "線上比較兩個文本文件的差異。高亮顯示變化。",
        "label_original": "原始文本",
        "label_modified": "修改後文本",
        "btn_compare": "比較差異",
        "btn_clear": "清除",
        "header_result": "比較結果",
        "legend_add": "新增",
        "legend_remove": "刪除",
        "related_header": "相關工具",
        "related_text": "文本工具箱",
        "related_md": "Markdown 預覽",
        "related_regex": "正則表達式測試"
    },
    "ja": {
        "title": "テキスト差分チェッカー",
        "meta_title": "テキスト差分チェッカー (Diff) - Utilify",
        "meta_desc": "2つのテキストの差分を簡単に比較します。追加および削除された部分をハイライト表示します。",
        "og_title": "テキスト差分チェッカー - Utilify",
        "og_desc": "2つのテキストの差分を簡単に比較します。追加および削除された部分をハイライト表示します。",
        "json_name": "テキスト差分チェッカー",
        "json_desc": "2つのテキストの差分を簡単に比較します。追加および削除された部分をハイライト表示します。",
        "page_desc": "2つのテキストの差分を簡単に比較します。追加および削除された部分をハイライト表示します。",
        "adsense_text": "広告スペース",
        "label_orig": "元のテキスト",
        "ph_orig": "元のテキストをここに入力...",
        "label_changed": "変更後のテキスト",
        "ph_changed": "変更後のテキストをここに入力...",
        "btn_compare": "比較",
        "btn_clear": "クリア",
        "header_result": "比較結果",
        "related_header": "関連ツール",
        "related_text": "テキストユーティリティ",
        "related_regex": "正規表現テスター",
        "related_md": "Markdownプレビュー",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "差分は見つかりませんでした。"
    },
    "vi": {
        "title": "Kiểm tra sự khác biệt văn bản",
        "meta_title": "Kiểm tra sự khác biệt văn bản - Utilify",
        "meta_desc": "So sánh sự khác biệt giữa hai văn bản dễ dàng. Đánh dấu các phần đã thêm và bị xóa.",
        "og_title": "Kiểm tra sự khác biệt văn bản - Utilify",
        "og_desc": "So sánh sự khác biệt giữa hai văn bản dễ dàng. Đánh dấu các phần đã thêm và bị xóa.",
        "json_name": "Kiểm tra sự khác biệt văn bản",
        "json_desc": "So sánh sự khác biệt giữa hai văn bản dễ dàng. Đánh dấu các phần đã thêm và bị xóa.",
        "page_desc": "So sánh sự khác biệt giữa hai văn bản dễ dàng. Đánh dấu các phần đã thêm và bị xóa.",
        "adsense_text": "Không gian quảng cáo",
        "label_orig": "Văn bản gốc",
        "ph_orig": "Nhập văn bản gốc tại đây...",
        "label_changed": "Văn bản đã thay đổi",
        "ph_changed": "Nhập văn bản đã thay đổi tại đây...",
        "btn_compare": "So sánh",
        "btn_clear": "Xóa",
        "header_result": "Kết quả so sánh",
        "related_header": "Công cụ liên quan",
        "related_text": "Tiện ích văn bản",
        "related_regex": "Kiểm tra Regex",
        "related_md": "Xem trước Markdown",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "Không tìm thấy sự khác biệt."
    },
    "th": {
        "title": "ตัวตรวจสอบความแตกต่างของข้อความ",
        "meta_title": "ตัวตรวจสอบความแตกต่างของข้อความ - Utilify",
        "meta_desc": "เปรียบเทียบความแตกต่างระหว่างข้อความสองชุดได้อย่างง่ายดาย เน้นส่วนที่เพิ่มและลบออก",
        "og_title": "ตัวตรวจสอบความแตกต่างของข้อความ - Utilify",
        "og_desc": "เปรียบเทียบความแตกต่างระหว่างข้อความสองชุดได้อย่างง่ายดาย เน้นส่วนที่เพิ่มและลบออก",
        "json_name": "ตัวตรวจสอบความแตกต่างของข้อความ",
        "json_desc": "เปรียบเทียบความแตกต่างระหว่างข้อความสองชุดได้อย่างง่ายดาย เน้นส่วนที่เพิ่มและลบออก",
        "page_desc": "เปรียบเทียบความแตกต่างระหว่างข้อความสองชุดได้อย่างง่ายดาย เน้นส่วนที่เพิ่มและลบออก",
        "adsense_text": "พื้นที่โฆษณา",
        "label_orig": "ข้อความต้นฉบับ",
        "ph_orig": "ป้อนข้อความต้นฉบับที่นี่...",
        "label_changed": "ข้อความที่เปลี่ยนแปลง",
        "ph_changed": "ป้อนข้อความที่เปลี่ยนแปลงที่นี่...",
        "btn_compare": "เปรียบเทียบ",
        "btn_clear": "ล้าง",
        "header_result": "ผลการเปรียบเทียบ",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_text": "ยูทิลิตี้ข้อความ",
        "related_regex": "ตัวทดสอบ Regex",
        "related_md": "ดูตัวอย่าง Markdown",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "ไม่พบความแตกต่าง"
    },
    "de": {
        "title": "Text-Diff-Checker",
        "meta_title": "Text-Diff-Checker - Utilify",
        "meta_desc": "Vergleichen Sie zwei Texte einfach auf Unterschiede. Hebt hinzugefügte und entfernte Teile hervor.",
        "og_title": "Text-Diff-Checker - Utilify",
        "og_desc": "Vergleichen Sie zwei Texte einfach auf Unterschiede. Hebt hinzugefügte und entfernte Teile hervor.",
        "json_name": "Text-Diff-Checker",
        "json_desc": "Vergleichen Sie zwei Texte einfach auf Unterschiede. Hebt hinzugefügte und entfernte Teile hervor.",
        "page_desc": "Vergleichen Sie zwei Texte einfach auf Unterschiede. Hebt hinzugefügte und entfernte Teile hervor.",
        "adsense_text": "Werbefläche",
        "label_orig": "Originaltext",
        "ph_orig": "Originaltext hier eingeben...",
        "label_changed": "Geänderter Text",
        "ph_changed": "Geänderten Text hier eingeben...",
        "btn_compare": "Vergleichen",
        "btn_clear": "Löschen",
        "header_result": "Vergleichsergebnis",
        "related_header": "Ähnliche Tools",
        "related_text": "Text-Utils",
        "related_regex": "Regex-Tester",
        "related_md": "Markdown-Vorschau",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "Keine Unterschiede gefunden."
    },
    "pt": {
        "title": "Verificador de Diferença de Texto",
        "meta_title": "Verificador de Diferença de Texto - Utilify",
        "meta_desc": "Compare a diferença entre dois textos facilmente. Destaca partes adicionadas e removidas.",
        "og_title": "Verificador de Diferença de Texto - Utilify",
        "og_desc": "Compare a diferença entre dois textos facilmente. Destaca partes adicionadas e removidas.",
        "json_name": "Verificador de Diferença de Texto",
        "json_desc": "Compare a diferença entre dois textos facilmente. Destaca partes adicionadas e removidas.",
        "page_desc": "Compare a diferença entre dois textos facilmente. Destaca partes adicionadas e removidas.",
        "adsense_text": "Espaço Publicitário",
        "label_orig": "Texto Original",
        "ph_orig": "Digite o texto original aqui...",
        "label_changed": "Texto Alterado",
        "ph_changed": "Digite o texto alterado aqui...",
        "btn_compare": "Comparar",
        "btn_clear": "Limpar",
        "header_result": "Resultado da Comparação",
        "related_header": "Ferramentas Relacionadas",
        "related_text": "Utilitários de Texto",
        "related_regex": "Testador de Regex",
        "related_md": "Pré-visualização Markdown",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "Nenhuma diferença encontrada."
    },
    "id": {
        "title": "Pemeriksa Perbedaan Teks",
        "meta_title": "Pemeriksa Perbedaan Teks - Utilify",
        "meta_desc": "Bandingkan perbedaan dua teks dengan mudah. Menyoroti bagian yang ditambahkan dan dihapus.",
        "og_title": "Pemeriksa Perbedaan Teks - Utilify",
        "og_desc": "Bandingkan perbedaan dua teks dengan mudah. Menyoroti bagian yang ditambahkan dan dihapus.",
        "json_name": "Pemeriksa Perbedaan Teks",
        "json_desc": "Bandingkan perbedaan dua teks dengan mudah. Menyoroti bagian yang ditambahkan dan dihapus.",
        "page_desc": "Bandingkan perbedaan dua teks dengan mudah. Menyoroti bagian yang ditambahkan dan dihapus.",
        "adsense_text": "Ruang Iklan",
        "label_orig": "Teks Asli",
        "ph_orig": "Masukkan teks asli di sini...",
        "label_changed": "Teks yang Diubah",
        "ph_changed": "Masukkan teks yang diubah di sini...",
        "btn_compare": "Bandingkan",
        "btn_clear": "Bersihkan",
        "header_result": "Hasil Perbandingan",
        "related_header": "Alat Terkait",
        "related_text": "Utilitas Teks",
        "related_regex": "Penguji Regex",
        "related_md": "Pratinjau Markdown",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "Tidak ada perbedaan ditemukan."
    },
    "hi": {
        "title": "टेक्स्ट अंतर परीक्षक",
        "meta_title": "टेक्स्ट अंतर परीक्षक - Utilify",
        "meta_desc": "दो टेक्स्ट अंतर की तुलना आसानी से करें। जोड़े गए और हटाए गए भागों को हाइलाइट करता है।",
        "og_title": "टेक्स्ट अंतर परीक्षक - Utilify",
        "og_desc": "दो टेक्स्ट अंतर की तुलना आसानी से करें। जोड़े गए और हटाए गए भागों को हाइलाइट करता है।",
        "json_name": "टेक्स्ट अंतर परीक्षक",
        "json_desc": "दो टेक्स्ट अंतर की तुलना आसानी से करें। जोड़े गए और हटाए गए भागों को हाइलाइट करता है।",
        "page_desc": "दो टेक्स्ट अंतर की तुलना आसानी से करें। जोड़े गए और हटाए गए भागों को हाइलाइट करता है।",
        "adsense_text": "विज्ञापन स्थान",
        "label_orig": "मूल पाठ",
        "ph_orig": "मूल पाठ यहाँ दर्ज करें...",
        "label_changed": "बदला हुआ पाठ",
        "ph_changed": "बदला हुआ पाठ यहाँ दर्ज करें...",
        "btn_compare": "तुलना करें",
        "btn_clear": "साफ़ करें",
        "header_result": "तुलना परिणाम",
        "related_header": "संबंधित उपकरण",
        "related_text": "टेक्स्ट यूटिलिटीज",
        "related_regex": "Regex टेस्टर",
        "related_md": "Markdown पूर्वावलोकन",
        "related_lorem": "Lorem Ipsum",
        "msg_no_diff": "कोई अंतर नहीं मिला।"
    }
}

IMAGE_CONVERTER = {
    "en": {
        "title": "Image Converter",
        "meta_title": "Image Converter - Utilify",
        "meta_desc": "Resize images and convert to WebP, JPEG, PNG formats.",
        "og_title": "Image Converter - Utilify",
        "og_desc": "Resize images and convert to WebP, JPEG, PNG formats.",
        "json_name": "Image Converter",
        "json_desc": "Resize images and convert to WebP, JPEG, PNG formats.",
        "page_desc": "Resize images and convert to WebP, JPEG, PNG formats.",
        "drag_text": "Click or drag to upload image",
        "drag_sub": "Supports all image formats including JPG, PNG, GIF, WebP.",
        "label_width": "Width (px)",
        "label_height": "Height (px)",
        "label_format": "Output Format",
        "label_quality": "Quality (%)",
        "btn_convert": "Convert",
        "btn_reset": "Reset",
        "header_orig": "Original Image",
        "header_conv": "Converted Image",
        "btn_download": "Download",
        "related_header": "Related Tools",
        "related_img_editor": "Image Editor",
        "related_thumb": "Thumbnail Downloader",
        "related_favicon": "Favicon Generator",
        "related_color": "Color Converter",
        "alert_type": "Only image files can be uploaded."
    },
    "ko": {
        "title": "이미지 변환기",
        "meta_title": "이미지 변환기 - Utilify",
        "meta_desc": "이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요. 브라우저에서 바로 처리됩니다.",
        "og_title": "이미지 변환기 - Utilify",
        "og_desc": "이미지 크기를 조정하고 다양한 형식으로 변환하세요.",
        "json_name": "이미지 변환기",
        "json_desc": "이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요.",
        "page_desc": "이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요.",
        "drag_text": "이미지를 클릭하거나 드래그하여 업로드",
        "drag_sub": "JPG, PNG, GIF, WebP 등 모든 이미지 형식 지원",
        "label_width": "너비 (px)",
        "label_height": "높이 (px)",
        "label_format": "출력 형식",
        "label_quality": "품질 (%)",
        "btn_convert": "변환하기",
        "btn_reset": "초기화",
        "header_orig": "원본 이미지",
        "header_conv": "변환된 이미지",
        "btn_download": "다운로드",
        "related_header": "함께 보면 좋은 도구",
        "related_img_editor": "이미지 편집기",
        "related_thumb": "썸네일 다운로더",
        "related_favicon": "파비콘 생성기",
        "related_color": "색상 변환기",
        "alert_type": "이미지 파일만 업로드할 수 있습니다."
    },
    "zh-cn": {
        "title": "图片格式转换器",
        "meta_title": "图片格式转换器 (JPG, PNG, WebP) - Utilify",
        "meta_desc": "免费在线将图片转换为 JPG, PNG, WebP 格式。支持批量转换。",
        "og_title": "图片格式转换器 - Utilify",
        "og_desc": "免费在线将图片转换为 JPG, PNG, WebP 格式。",
        "json_name": "图片格式转换器",
        "json_desc": "免费在线将图片转换为 JPG, PNG, WebP 格式。",
        "page_desc": "免费在线将图片转换为 JPG, PNG, WebP 格式。",
        "label_upload": "上传图片 (支持拖拽)",
        "btn_convert": "转换为",
        "format_jpg": "JPG",
        "format_png": "PNG",
        "format_webp": "WebP",
        "btn_download": "下载",
        "btn_clear": "清除",
        "related_header": "相关工具",
        "related_watermark": "图片水印",
        "related_favicon": "Favicon 生成器",
        "related_thumb": "缩略图下载",
        "related_qr": "QR 码生成器"
    },
    "zh-tw": {
        "title": "圖片格式轉換器",
        "meta_title": "圖片格式轉換器 (JPG, PNG, WebP) - Utilify",
        "meta_desc": "免費線上將圖片轉換為 JPG, PNG, WebP 格式。支持批量轉換。",
        "og_title": "圖片格式轉換器 - Utilify",
        "og_desc": "免費線上將圖片轉換為 JPG, PNG, WebP 格式。",
        "json_name": "圖片格式轉換器",
        "json_desc": "免費線上將圖片轉換為 JPG, PNG, WebP 格式。",
        "page_desc": "免費線上將圖片轉換為 JPG, PNG, WebP 格式。",
        "label_upload": "上傳圖片 (支持拖拽)",
        "btn_convert": "轉換為",
        "format_jpg": "JPG",
        "format_png": "PNG",
        "format_webp": "WebP",
        "btn_download": "下載",
        "btn_clear": "清除",
        "related_header": "相關工具",
        "related_watermark": "圖片浮水印",
        "related_favicon": "Favicon 生成器",
        "related_thumb": "縮圖下載",
        "related_qr": "QR 碼生成器"
    },
    "ja": {
        "title": "画像変換ツール",
        "meta_title": "画像変換ツール - Utilify",
        "meta_desc": "画像のサイズを変更し、WebP、JPEG、PNG形式に変換します。",
        "og_title": "画像変換ツール - Utilify",
        "og_desc": "画像のサイズを変更し、WebP、JPEG、PNG形式に変換します。",
        "json_name": "画像変換ツール",
        "json_desc": "画像のサイズを変更し、WebP、JPEG、PNG形式に変換します。",
        "page_desc": "画像のサイズを変更し、WebP、JPEG、PNG形式に変換します。",
        "drag_text": "クリックまたはドラッグして画像をアップロード",
        "drag_sub": "JPG、PNG、GIF、WebPを含むすべての画像形式をサポート。",
        "label_width": "幅 (px)",
        "label_height": "高さ (px)",
        "label_format": "出力形式",
        "label_quality": "品質 (%)",
        "btn_convert": "変換",
        "btn_reset": "リセット",
        "header_orig": "元の画像",
        "header_conv": "変換された画像",
        "btn_download": "ダウンロード",
        "related_header": "関連ツール",
        "related_img_editor": "画像編集ツール",
        "related_thumb": "サムネイルダウンローダー",
        "related_favicon": "ファビコン生成",
        "related_color": "色変換ツール",
        "alert_type": "画像ファイルのみアップロードできます。"
    },
    "vi": {
        "title": "Chuyển đổi hình ảnh",
        "meta_title": "Chuyển đổi hình ảnh - Utilify",
        "meta_desc": "Thay đổi kích thước hình ảnh và chuyển đổi sang các định dạng WebP, JPEG, PNG.",
        "og_title": "Chuyển đổi hình ảnh - Utilify",
        "og_desc": "Thay đổi kích thước hình ảnh và chuyển đổi sang các định dạng WebP, JPEG, PNG.",
        "json_name": "Chuyển đổi hình ảnh",
        "json_desc": "Thay đổi kích thước hình ảnh và chuyển đổi sang các định dạng WebP, JPEG, PNG.",
        "page_desc": "Thay đổi kích thước hình ảnh và chuyển đổi sang các định dạng WebP, JPEG, PNG.",
        "drag_text": "Nhấp hoặc kéo để tải lên hình ảnh",
        "drag_sub": "Hỗ trợ tất cả các định dạng hình ảnh bao gồm JPG, PNG, GIF, WebP.",
        "label_width": "Chiều rộng (px)",
        "label_height": "Chiều cao (px)",
        "label_format": "Định dạng đầu ra",
        "label_quality": "Chất lượng (%)",
        "btn_convert": "Chuyển đổi",
        "btn_reset": "Đặt lại",
        "header_orig": "Hình ảnh gốc",
        "header_conv": "Hình ảnh đã chuyển đổi",
        "btn_download": "Tải xuống",
        "related_header": "Công cụ liên quan",
        "related_img_editor": "Trình sửa ảnh",
        "related_thumb": "Trình tải xuống hình thu nhỏ",
        "related_favicon": "Tạo Favicon",
        "related_color": "Chuyển đổi màu sắc",
        "alert_type": "Chỉ có thể tải lên tệp hình ảnh."
    },
    "th": {
        "title": "ตัวแปลงรูปภาพ",
        "meta_title": "ตัวแปลงรูปภาพ - Utilify",
        "meta_desc": "ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP, JPEG, PNG",
        "og_title": "ตัวแปลงรูปภาพ - Utilify",
        "og_desc": "ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP, JPEG, PNG",
        "json_name": "ตัวแปลงรูปภาพ",
        "json_desc": "ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP, JPEG, PNG",
        "page_desc": "ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP, JPEG, PNG",
        "drag_text": "คลิกหรือลากเพื่ออัปโหลดรูปภาพ",
        "drag_sub": "รองรับรูปแบบรูปภาพทั้งหมดรวมถึง JPG, PNG, GIF, WebP",
        "label_width": "ความกว้าง (px)",
        "label_height": "ความสูง (px)",
        "label_format": "รูปแบบผลลัพธ์",
        "label_quality": "คุณภาพ (%)",
        "btn_convert": "แปลง",
        "btn_reset": "รีเซ็ต",
        "header_orig": "รูปภาพต้นฉบับ",
        "header_conv": "รูปภาพที่แปลงแล้ว",
        "btn_download": "ดาวน์โหลด",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_img_editor": "ตัวแก้ไขรูปภาพ",
        "related_thumb": "ดาวน์โหลดรูปขนาดย่อ",
        "related_favicon": "สร้าง Favicon",
        "related_color": "ตัวแปลงสี",
        "alert_type": "อัปโหลดได้เฉพาะไฟล์รูปภาพเท่านั้น"
    },
    "de": {
        "title": "Bildkonverter",
        "meta_title": "Bildkonverter - Utilify",
        "meta_desc": "Bildergröße ändern und in WebP, JPEG, PNG Formate konvertieren.",
        "og_title": "Bildkonverter - Utilify",
        "og_desc": "Bildergröße ändern und in WebP, JPEG, PNG Formate konvertieren.",
        "json_name": "Bildkonverter",
        "json_desc": "Bildergröße ändern und in WebP, JPEG, PNG Formate konvertieren.",
        "page_desc": "Bildergröße ändern und in WebP, JPEG, PNG Formate konvertieren.",
        "drag_text": "Klicken oder ziehen, um Bild hochzuladen",
        "drag_sub": "Unterstützt alle Bildformate einschließlich JPG, PNG, GIF, WebP.",
        "label_width": "Breite (px)",
        "label_height": "Höhe (px)",
        "label_format": "Ausgabeformat",
        "label_quality": "Qualität (%)",
        "btn_convert": "Konvertieren",
        "btn_reset": "Zurücksetzen",
        "header_orig": "Originalbild",
        "header_conv": "Konvertiertes Bild",
        "btn_download": "Herunterladen",
        "related_header": "Ähnliche Tools",
        "related_img_editor": "Bildbearbeiter",
        "related_thumb": "Thumbnail-Downloader",
        "related_favicon": "Favicon-Generator",
        "related_color": "Farbkonverter",
        "alert_type": "Nur Bilddateien können hochgeladen werden."
    },
    "pt": {
        "title": "Conversor de Imagem",
        "meta_title": "Conversor de Imagem - Utilify",
        "meta_desc": "Redimensione imagens e converta para formatos WebP, JPEG, PNG.",
        "og_title": "Conversor de Imagem - Utilify",
        "og_desc": "Redimensione imagens e converta para formatos WebP, JPEG, PNG.",
        "json_name": "Conversor de Imagem",
        "json_desc": "Redimensione imagens e converta para formatos WebP, JPEG, PNG.",
        "page_desc": "Redimensione imagens e converta para formatos WebP, JPEG, PNG.",
        "drag_text": "Clique ou arraste para enviar imagem",
        "drag_sub": "Suporta todos os formatos de imagem, incluindo JPG, PNG, GIF, WebP.",
        "label_width": "Largura (px)",
        "label_height": "Altura (px)",
        "label_format": "Formato de Saída",
        "label_quality": "Qualidade (%)",
        "btn_convert": "Converter",
        "btn_reset": "Redefinir",
        "header_orig": "Imagem Original",
        "header_conv": "Imagem Convertida",
        "btn_download": "Baixar",
        "related_header": "Ferramentas Relacionadas",
        "related_img_editor": "Editor de Imagem",
        "related_thumb": "Baixador de Miniaturas",
        "related_favicon": "Gerador de Favicon",
        "related_color": "Conversor de Cores",
        "alert_type": "Apenas arquivos de imagem podem ser enviados."
    },
    "id": {
        "title": "Konverter Gambar",
        "meta_title": "Konverter Gambar - Utilify",
        "meta_desc": "Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.",
        "og_title": "Konverter Gambar - Utilify",
        "og_desc": "Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.",
        "json_name": "Konverter Gambar",
        "json_desc": "Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.",
        "page_desc": "Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.",
        "drag_text": "Klik atau seret untuk mengunggah gambar",
        "drag_sub": "Mendukung semua format gambar termasuk JPG, PNG, GIF, WebP.",
        "label_width": "Lebar (px)",
        "label_height": "Tinggi (px)",
        "label_format": "Format Output",
        "label_quality": "Kualitas (%)",
        "btn_convert": "Konversi",
        "btn_reset": "Atur Ulang",
        "header_orig": "Gambar Asli",
        "header_conv": "Gambar Dikonversi",
        "btn_download": "Unduh",
        "related_header": "Alat Terkait",
        "related_img_editor": "Editor Gambar",
        "related_thumb": "Pengunduh Thumbnail",
        "related_favicon": "Generator Favicon",
        "related_color": "Konverter Warna",
        "alert_type": "Hanya file gambar yang dapat diunggah."
    },
    "hi": {
        "title": "छवि परिवर्तक",
        "meta_title": "छवि परिवर्तक - Utilify",
        "meta_desc": "छवियों का आकार बदलें और WebP, JPEG, PNG प्रारूपों में बदलें।",
        "og_title": "छवि परिवर्तक - Utilify",
        "og_desc": "छवियों का आकार बदलें और WebP, JPEG, PNG प्रारूपों में बदलें।",
        "json_name": "छवि परिवर्तक",
        "json_desc": "छवियों का आकार बदलें और WebP, JPEG, PNG प्रारूपों में बदलें।",
        "page_desc": "छवियों का आकार बदलें और WebP, JPEG, PNG प्रारूपों में बदलें।",
        "drag_text": "छवि अपलोड करने के लिए क्लिक करें या खींचें",
        "drag_sub": "JPG, PNG, GIF, WebP सहित सभी छवि प्रारूपों का समर्थन करता है।",
        "label_width": "चौड़ाई (px)",
        "label_height": "ऊंचाई (px)",
        "label_format": "आउटपुट प्रारूप",
        "label_quality": "गुणवत्ता (%)",
        "btn_convert": "बदलें",
        "btn_reset": "रीसेट करें",
        "header_orig": "मूल छवि",
        "header_conv": "परिवर्तित छवि",
        "btn_download": "डाउनलोड करें",
        "related_header": "संबंधित उपकरण",
        "related_img_editor": "छवि संपादक",
        "related_thumb": "थंबनेल डाउनलोडर",
        "related_favicon": "फेविकॉन जेनरेटर",
        "related_color": "रंग परिवर्तक",
        "alert_type": "केवल छवि फ़ाइलें अपलोड की जा सकती हैं।"
    }
}

QR_GENERATOR = {
    "en": {
        "title": "QR Code Generator",
        "meta_title": "QR Code Generator - Utilify",
        "meta_desc": "Convert text or URL to QR code.",
        "og_title": "QR Code Generator - Utilify",
        "og_desc": "Convert text or URL to QR code.",
        "json_name": "QR Code Generator",
        "json_desc": "Convert text or URL to QR code.",
        "page_desc": "Convert text or URL to QR code.",
        "label_text": "Text or URL",
        "ph_text": "https://example.com",
        "label_size": "Size",
        "btn_generate": "Generate",
        "btn_download": "Download",
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_timer": "Timer",
        "alert_empty": "Enter text.",
        "alert_no_qr": "Generate QR code first."
    },
    "ko": {
        "title": "QR 코드 생성기",
        "meta_title": "QR 코드 생성기 - Utilify",
        "meta_desc": "텍스트나 URL을 QR 코드로 변환하세요.",
        "og_title": "QR 코드 생성기 - Utilify",
        "og_desc": "텍스트나 URL을 QR 코드로 변환하세요.",
        "json_name": "QR 코드 생성기",
        "json_desc": "텍스트나 URL을 QR 코드로 변환하세요.",
        "page_desc": "텍스트나 URL을 QR 코드로 변환하세요.",
        "label_text": "텍스트 또는 URL",
        "ph_text": "https://example.com",
        "label_size": "크기",
        "btn_generate": "생성",
        "btn_download": "다운로드",
        "related_header": "함께 보면 좋은 도구",
        "related_unit": "단위 변환기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_timer": "타이머",
        "alert_empty": "텍스트를 입력하세요.",
        "alert_no_qr": "먼저 QR 코드를 생성하세요."
    },
    "zh-cn": {
        "title": "QR 码生成器",
        "meta_title": "QR 码生成器 - Utilify",
        "meta_desc": "将文本或 URL 转换为 QR 码。",
        "og_title": "QR 码生成器 - Utilify",
        "og_desc": "将文本或 URL 转换为 QR 码。",
        "json_name": "QR 码生成器",
        "json_desc": "将文本或 URL 转换为 QR 码。",
        "page_desc": "将文本或 URL 转换为 QR 码。",
        "label_text": "文本或 URL",
        "ph_text": "https://example.com",
        "label_size": "大小",
        "btn_generate": "生成",
        "btn_download": "下载",
        "related_header": "相关工具",
        "related_unit": "单位转换器",
        "related_bmi": "BMI 计算器",
        "related_date": "日期计算器",
        "alert_empty": "请输入文本。",
        "alert_no_qr": "请先生成 QR 码。"
    },
    "zh-tw": {
        "title": "QR 碼生成器",
        "meta_title": "QR 碼生成器 - Utilify",
        "meta_desc": "將文本或 URL 轉換為 QR 碼。",
        "og_title": "QR 碼生成器 - Utilify",
        "og_desc": "將文本或 URL 轉換為 QR 碼。",
        "json_name": "QR 碼生成器",
        "json_desc": "將文本或 URL 轉換為 QR 碼。",
        "page_desc": "將文本或 URL 轉換為 QR 碼。",
        "label_text": "文本或 URL",
        "ph_text": "https://example.com",
        "label_size": "大小",
        "btn_generate": "生成",
        "btn_download": "下載",
        "related_header": "相關工具",
        "related_unit": "單位轉換器",
        "related_bmi": "BMI 計算器",
        "related_date": "日期計算器",
        "alert_empty": "請輸入文本。",
        "alert_no_qr": "請先生成 QR 碼。"
    },
    "ja": {
        "title": "QRコード生成",
        "meta_title": "QRコード生成 - Utilify",
        "meta_desc": "テキストまたはURLをQRコードに変換します。",
        "og_title": "QRコード生成 - Utilify",
        "og_desc": "テキストまたはURLをQRコードに変換します。",
        "json_name": "QRコード生成",
        "json_desc": "テキストまたはURLをQRコードに変換します。",
        "page_desc": "テキストまたはURLをQRコードに変換します。",
        "label_text": "テキストまたはURL",
        "ph_text": "https://example.com",
        "label_size": "サイズ",
        "btn_generate": "生成",
        "btn_download": "ダウンロード",
        "related_header": "関連ツール",
        "related_unit": "単位変換ツール",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算",
        "alert_empty": "テキストを入力してください。",
        "alert_no_qr": "まずQRコードを生成してください。"
    },
    "vi": {
        "title": "Tạo mã QR",
        "meta_title": "Tạo mã QR - Utilify",
        "meta_desc": "Chuyển đổi văn bản hoặc URL thành mã QR.",
        "og_title": "Tạo mã QR - Utilify",
        "og_desc": "Chuyển đổi văn bản hoặc URL thành mã QR.",
        "json_name": "Tạo mã QR",
        "json_desc": "Chuyển đổi văn bản hoặc URL thành mã QR.",
        "page_desc": "Chuyển đổi văn bản hoặc URL thành mã QR.",
        "label_text": "Văn bản hoặc URL",
        "ph_text": "https://example.com",
        "label_size": "Kích thước",
        "btn_generate": "Tạo",
        "btn_download": "Tải xuống",
        "related_header": "Công cụ liên quan",
        "related_unit": "Chuyển đổi đơn vị",
        "related_bmi": "Máy tính BMI",
        "related_date": "Máy tính ngày",
        "alert_empty": "Nhập văn bản.",
        "alert_no_qr": "Tạo mã QR trước."
    },
    "th": {
        "title": "สร้าง QR Code",
        "meta_title": "สร้าง QR Code - Utilify",
        "meta_desc": "แปลงข้อความหรือ URL เป็น QR Code",
        "og_title": "สร้าง QR Code - Utilify",
        "og_desc": "แปลงข้อความหรือ URL เป็น QR Code",
        "json_name": "สร้าง QR Code",
        "json_desc": "แปลงข้อความหรือ URL เป็น QR Code",
        "page_desc": "แปลงข้อความหรือ URL เป็น QR Code",
        "label_text": "ข้อความหรือ URL",
        "ph_text": "https://example.com",
        "label_size": "ขนาด",
        "btn_generate": "สร้าง",
        "btn_download": "ดาวน์โหลด",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_unit": "เครื่องมือแปลงหน่วย",
        "related_bmi": "เครื่องคำนวณ BMI",
        "related_date": "เครื่องคำนวณวันที่",
        "alert_empty": "ป้อนข้อความ",
        "alert_no_qr": "สร้าง QR Code ก่อน"
    },
    "de": {
        "title": "QR-Code-Generator",
        "meta_title": "QR-Code-Generator - Utilify",
        "meta_desc": "Text oder URL in QR-Code konvertieren.",
        "og_title": "QR-Code-Generator - Utilify",
        "og_desc": "Text oder URL in QR-Code konvertieren.",
        "json_name": "QR-Code-Generator",
        "json_desc": "Text oder URL in QR-Code konvertieren.",
        "page_desc": "Text oder URL in QR-Code konvertieren.",
        "label_text": "Text oder URL",
        "ph_text": "https://example.com",
        "label_size": "Größe",
        "btn_generate": "Generieren",
        "btn_download": "Herunterladen",
        "related_header": "Ähnliche Tools",
        "related_unit": "Einheitenumrechner",
        "related_bmi": "BMI Rechner",
        "related_date": "Datumsrechner",
        "alert_empty": "Text eingeben.",
        "alert_no_qr": "Zuerst QR-Code generieren."
    },
    "pt": {
        "title": "Gerador de QR Code",
        "meta_title": "Gerador de QR Code - Utilify",
        "meta_desc": "Converta texto ou URL para código QR.",
        "og_title": "Gerador de QR Code - Utilify",
        "og_desc": "Converta texto ou URL para código QR.",
        "json_name": "Gerador de QR Code",
        "json_desc": "Converta texto ou URL para código QR.",
        "page_desc": "Converta texto ou URL para código QR.",
        "label_text": "Texto ou URL",
        "ph_text": "https://example.com",
        "label_size": "Tamanho",
        "btn_generate": "Gerar",
        "btn_download": "Baixar",
        "related_header": "Ferramentas Relacionadas",
        "related_unit": "Conversor de Unidades",
        "related_bmi": "Calculadora de IMC",
        "related_date": "Calculadora de Data",
        "alert_empty": "Digite o texto.",
        "alert_no_qr": "Gere o código QR primeiro."
    },
    "id": {
        "title": "Generator Kode QR",
        "meta_title": "Generator Kode QR - Utilify",
        "meta_desc": "Konversi teks atau URL ke kode QR.",
        "og_title": "Generator Kode QR - Utilify",
        "og_desc": "Konversi teks atau URL ke kode QR.",
        "json_name": "Generator Kode QR",
        "json_desc": "Konversi teks atau URL ke kode QR.",
        "page_desc": "Konversi teks atau URL ke kode QR.",
        "label_text": "Teks atau URL",
        "ph_text": "https://example.com",
        "label_size": "Ukuran",
        "btn_generate": "Hasilkan",
        "btn_download": "Unduh",
        "related_header": "Alat Terkait",
        "related_unit": "Konverter Unit",
        "related_bmi": "Kalkulator BMI",
        "related_date": "Kalkulator Tanggal",
        "alert_empty": "Masukkan teks.",
        "alert_no_qr": "Hasilkan kode QR terlebih dahulu."
    },
    "hi": {
        "title": "QR कोड जनरेटर",
        "meta_title": "QR कोड जनरेटर - Utilify",
        "meta_desc": "टेक्स्ट या URL को QR कोड में बदलें।",
        "og_title": "QR कोड जनरेटर - Utilify",
        "og_desc": "टेक्स्ट या URL को QR कोड में बदलें।",
        "json_name": "QR कोड जनरेटर",
        "json_desc": "टेक्स्ट या URL को QR कोड में बदलें।",
        "page_desc": "टेक्स्ट या URL को QR कोड में बदलें।",
        "label_text": "टेक्स्ट या URL",
        "ph_text": "https://example.com",
        "label_size": "आकार",
        "btn_generate": "उत्पन्न करें",
        "btn_download": "डाउनलोड करें",
        "related_header": "संबंधित उपकरण",
        "related_unit": "इकाई परिवर्तक",
        "related_bmi": "BMI कैलकुलेटर",
        "related_date": "दिनांक कैलकुलेटर",
        "alert_empty": "टेक्स्ट दर्ज करें।",
        "alert_no_qr": "पहले QR कोड उत्पन्न करें।"
    }
}

FAVICON_GENERATOR = {
    "en": {
        "title": "Favicon Generator",
        "meta_title": "Favicon Generator - Utilify",
        "meta_desc": "Convert images to favicons of various sizes.",
        "og_title": "Favicon Generator - Utilify",
        "og_desc": "Convert images to favicons of various sizes.",
        "json_name": "Favicon Generator",
        "json_desc": "Convert images to favicons of various sizes.",
        "page_desc": "Convert images to favicons of various sizes.",
        "label_image": "Select Image",
        "header_preview": "Preview",
        "btn_generate": "Generate Favicon",
        "btn_download": "Download",
        "btn_download_all": "Download All (.zip)",
        "drop_text": "Drop an image here or click to upload",
        "related_header": "Related Tools",
        "related_watermark": "Image Watermark",
        "related_img": "Image Converter",
        "related_color": "Color Converter",
        "related_thumb": "Thumbnail Downloader",
        "related_qr": "QR Code Generator"
    },
    "ko": {
        "title": "파비콘 생성기",
        "meta_title": "파비콘 생성기 - Utilify",
        "meta_desc": "이미지를 다양한 크기의 파비콘으로 변환하세요.",
        "og_title": "파비콘 생성기 - Utilify",
        "og_desc": "이미지를 다양한 크기의 파비콘으로 변환하세요.",
        "json_name": "파비콘 생성기",
        "json_desc": "이미지를 다양한 크기의 파비콘으로 변환하세요.",
        "page_desc": "이미지를 다양한 크기의 파비콘으로 변환하세요.",
        "label_image": "이미지 선택",
        "header_preview": "미리보기",
        "btn_generate": "파비콘 생성",
        "btn_download_all": "전체 다운로드 (.zip)",
        "related_header": "함께 보면 좋은 도구",
        "related_watermark": "이미지 워터마크",
        "related_img": "이미지 변환기",
        "related_thumb": "썸네일 다운로더",
        "related_qr": "QR 코드 생성기"
    },
    "zh-cn": {
        "title": "Favicon 生成器",
        "meta_title": "Favicon 生成器 - Utilify",
        "meta_desc": "将图片转换为 Favicon 图标。支持多种尺寸。",
        "og_title": "Favicon 生成器 - Utilify",
        "og_desc": "将图片转换为 Favicon 图标。",
        "json_name": "Favicon 生成器",
        "json_desc": "将图片转换为 Favicon 图标。",
        "page_desc": "将图片转换为 Favicon 图标。",
        "label_image": "选择图片",
        "header_preview": "预览",
        "btn_generate": "生成 Favicon",
        "btn_download_all": "下载全部 (.zip)",
        "related_header": "相关工具",
        "related_watermark": "图片水印",
        "related_img": "图片格式转换器",
        "related_thumb": "缩略图下载",
        "related_qr": "QR 码生成器"
    },
    "zh-tw": {
        "title": "Favicon 生成器",
        "meta_title": "Favicon 生成器 - Utilify",
        "meta_desc": "將圖片轉換為 Favicon 圖標。支持多種尺寸。",
        "og_title": "Favicon 生成器 - Utilify",
        "og_desc": "將圖片轉換為 Favicon 圖標。",
        "json_name": "Favicon 生成器",
        "json_desc": "將圖片轉換為 Favicon 圖標。",
        "page_desc": "將圖片轉換為 Favicon 圖標。",
        "label_image": "選擇圖片",
        "header_preview": "預覽",
        "btn_generate": "生成 Favicon",
        "btn_download_all": "下載全部 (.zip)",
        "related_header": "相關工具",
        "related_watermark": "圖片浮水印",
        "related_img": "圖片格式轉換器",
        "related_thumb": "縮圖下載",
        "related_qr": "QR 碼生成器"
    },
    "ja": {
        "title": "ファビコン生成",
        "meta_title": "ファビコン生成 - Utilify",
        "meta_desc": "画像をさまざまなサイズのファビコンに変換します。",
        "og_title": "ファビコン生成 - Utilify",
        "og_desc": "画像をさまざまなサイズのファビコンに変換します。",
        "json_name": "ファビコン生成",
        "json_desc": "画像をさまざまなサイズのファビコンに変換します。",
        "page_desc": "画像をさまざまなサイズのファビコンに変換します。",
        "label_image": "画像を選択",
        "header_preview": "プレビュー",
        "btn_generate": "ファビコンを生成",
        "btn_download_all": "すべてダウンロード (.zip)",
        "related_header": "関連ツール",
        "related_watermark": "画像透かし",
        "related_img": "画像変換",
        "related_thumb": "サムネイルダウンローダー",
        "related_qr": "QRコード生成"
    },
    "hi": {
        "title": "फेविकॉन जेनरेटर",
        "meta_title": "फेविकॉन जेनरेटर - Utilify",
        "meta_desc": "छवियों को विभिन्न आकारों के फेविकॉन में बदलें।",
        "og_title": "फेविकॉन जेनरेटर - Utilify",
        "og_desc": "छवियों को विभिन्न आकारों के फेविकॉन में बदलें।",
        "json_name": "फेविकॉन जेनरेटर",
        "json_desc": "छवियों को विभिन्न आकारों के फेविकॉन में बदलें।",
        "page_desc": "छवियों को विभिन्न आकारों के फेविकॉन में बदलें।",
        "label_image": "छवि चुनें",
        "header_preview": "पूर्वावलोकन",
        "btn_generate": "फेविकॉन उत्पन्न करें",
        "btn_download_all": "सभी डाउनलोड करें (.zip)",
        "related_header": "संबंधित उपकरण",
        "related_watermark": "छवि वाटरमार्क",
        "related_img": "छवि परिवर्तक",
        "related_thumb": "थंबनेल डाउनलोडर",
        "related_qr": "QR कोड जनरेटर"
    },
    "id": {
        "title": "Generator Favicon",
        "meta_title": "Generator Favicon - Utilify",
        "meta_desc": "Konversi gambar menjadi favicon dengan berbagai ukuran.",
        "og_title": "Generator Favicon - Utilify",
        "og_desc": "Konversi gambar menjadi favicon dengan berbagai ukuran.",
        "json_name": "Generator Favicon",
        "json_desc": "Konversi gambar menjadi favicon dengan berbagai ukuran.",
        "page_desc": "Konversi gambar menjadi favicon dengan berbagai ukuran.",
        "label_image": "Pilih Gambar",
        "header_preview": "Pratinjau",
        "btn_generate": "Hasilkan Favicon",
        "btn_download_all": "Unduh Semua (.zip)",
        "related_header": "Alat Terkait",
        "related_watermark": "Tanda Air Gambar",
        "related_img": "Konverter Gambar",
        "related_thumb": "Pengunduh Thumbnail",
        "related_qr": "Generator Kode QR"
    },
    "vi": {
        "title": "Tạo Favicon",
        "meta_title": "Tạo Favicon - Utilify",
        "meta_desc": "Chuyển đổi hình ảnh thành favicon với nhiều kích thước khác nhau.",
        "og_title": "Tạo Favicon - Utilify",
        "og_desc": "Chuyển đổi hình ảnh thành favicon với nhiều kích thước khác nhau.",
        "json_name": "Tạo Favicon",
        "json_desc": "Chuyển đổi hình ảnh thành favicon với nhiều kích thước khác nhau.",
        "page_desc": "Chuyển đổi hình ảnh thành favicon với nhiều kích thước khác nhau.",
        "label_image": "Chọn hình ảnh",
        "header_preview": "Xem trước",
        "btn_generate": "Tạo Favicon",
        "btn_download_all": "Tải xuống tất cả (.zip)",
        "related_header": "Công cụ liên quan",
        "related_watermark": "Đóng dấu ảnh",
        "related_img": "Chuyển đổi hình ảnh",
        "related_thumb": "Trình tải xuống hình thu nhỏ",
        "related_qr": "Tạo mã QR"
    },
    "th": {
        "title": "สร้าง Favicon",
        "meta_title": "สร้าง Favicon - Utilify",
        "meta_desc": "แปลงรูปภาพเป็น favicon ในขนาดต่างๆ",
        "og_title": "สร้าง Favicon - Utilify",
        "og_desc": "แปลงรูปภาพเป็น favicon ในขนาดต่างๆ",
        "json_name": "สร้าง Favicon",
        "json_desc": "แปลงรูปภาพเป็น favicon ในขนาดต่างๆ",
        "page_desc": "แปลงรูปภาพเป็น favicon ในขนาดต่างๆ",
        "label_image": "เลือกรูปภาพ",
        "header_preview": "ตัวอย่าง",
        "btn_generate": "สร้าง Favicon",
        "btn_download_all": "ดาวน์โหลดทั้งหมด (.zip)",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_watermark": "ลายน้ำรูปภาพ",
        "related_img": "แปลงรูปภาพ",
        "related_thumb": "ดาวน์โหลดรูปขนาดย่อ",
        "related_qr": "สร้าง QR Code"
    },
    "de": {
        "title": "Favicon-Generator",
        "meta_title": "Favicon-Generator - Utilify",
        "meta_desc": "Konvertieren Sie Bilder in Favicons verschiedener Größen.",
        "og_title": "Favicon-Generator - Utilify",
        "og_desc": "Konvertieren Sie Bilder in Favicons verschiedener Größen.",
        "json_name": "Favicon-Generator",
        "json_desc": "Konvertieren Sie Bilder in Favicons verschiedener Größen.",
        "page_desc": "Konvertieren Sie Bilder in Favicons verschiedener Größen.",
        "label_image": "Bild auswählen",
        "header_preview": "Vorschau",
        "btn_generate": "Favicon generieren",
        "btn_download_all": "Alle herunterladen (.zip)",
        "related_header": "Ähnliche Tools",
        "related_watermark": "Bild-Wasserzeichen",
        "related_img": "Bildkonverter",
        "related_thumb": "Thumbnail-Downloader",
        "related_qr": "QR-Code-Generator"
    },
    "pt": {
        "title": "Gerador de Favicon",
        "meta_title": "Gerador de Favicon - Utilify",
        "meta_desc": "Converta imagens em favicons de vários tamanhos.",
        "og_title": "Gerador de Favicon - Utilify",
        "og_desc": "Converta imagens em favicons de vários tamanhos.",
        "json_name": "Gerador de Favicon",
        "json_desc": "Converta imagens em favicons de vários tamanhos.",
        "page_desc": "Converta imagens em favicons de vários tamanhos.",
        "label_image": "Selecionar Imagem",
        "header_preview": "Visualização",
        "btn_generate": "Gerar Favicon",
        "btn_download_all": "Baixar Tudo (.zip)",
        "related_header": "Ferramentas Relacionadas",
        "related_watermark": "Marca D'água em Imagem",
        "related_img": "Conversor de Imagem",
        "related_thumb": "Baixador de Miniaturas",
        "related_qr": "Gerador de QR Code"
    }
}

IMAGE_WATERMARK = {
    "en": {
        "title": "Image Watermark",
        "meta_title": "Image Watermark - Utilify",
        "meta_desc": "Add watermarks to your images.",
        "og_title": "Image Watermark - Utilify",
        "og_desc": "Add watermarks to your images.",
        "json_name": "Image Watermark",
        "json_desc": "Add watermarks to your images.",
        "page_desc": "Add watermarks to your images.",
        "label_image": "Select Image",
        "label_text": "Watermark Text",
        "ph_text": "Copyright text...",
        "header_settings": "Settings",
        "header_preview": "Preview",
        "preview_sub": "Watermark preview is shown below.",
        "drop_text": "Drop images here or click to upload",
        "drop_sub": "Multiple images supported (PNG, JPG, WebP)",
        "selected_files": "Selected files:",
        "label_format": "Output Format",
        "label_pos": "Position",
        "label_size": "Size",
        "opt_webp": "WebP",
        "opt_tl": "Top Left",
        "opt_tr": "Top Right",
        "opt_bl": "Bottom Left",
        "opt_br": "Bottom Right",
        "opt_center": "Center",
        "opt_tile": "Tile",
        "val_text": "© Utilify",
        "btn_process": "Add Watermark",
        "btn_download": "Download",
        "btn_reset": "Reset",
        "prog_proc": "Processing",
        "prog_zip": "Building ZIP archive...",
        "prog_done": "Done.",
        "alert_img": "Please select at least one image.",
        "confirm_reset": "Reset all selected files and settings?",
        "related_header": "Related Tools",
        "related_favicon": "Favicon Generator",
        "related_thumb": "Thumbnail Downloader",
        "related_img": "Image Converter",
        "related_color": "Color Converter",
        "related_qr": "QR Code Generator"
    },
    "ko": {
        "title": "이미지 워터마크",
        "meta_title": "이미지 워터마크 - Utilify",
        "meta_desc": "이미지에 워터마크를 추가하여 저작권을 보호하세요.",
        "og_title": "이미지 워터마크 - Utilify",
        "og_desc": "이미지에 워터마크를 추가하여 저작권을 보호하세요.",
        "json_name": "이미지 워터마크",
        "json_desc": "이미지에 워터마크를 추가하여 저작권을 보호하세요.",
        "page_desc": "이미지에 워터마크를 추가하여 저작권을 보호하세요.",
        "label_image": "이미지 선택",
        "label_text": "워터마크 텍스트",
        "ph_text": "저작권 텍스트...",
        "header_settings": "설정",
        "btn_process": "워터마크 추가",
        "btn_download": "다운로드",
        "related_header": "함께 보면 좋은 도구",
        "related_favicon": "파비콘 생성기",
        "related_thumb": "썸네일 다운로더",
        "related_img": "이미지 변환기",
        "related_qr": "QR 코드 생성기"
    },
    "zh-cn": {
        "title": "图片水印",
        "meta_title": "图片水印工具 - Utilify",
        "meta_desc": "给图片添加自定义水印。保护版权。",
        "og_title": "图片水印工具 - Utilify",
        "og_desc": "给图片添加自定义水印。",
        "json_name": "图片水印",
        "json_desc": "给图片添加自定义水印。",
        "page_desc": "给图片添加自定义水印。",
        "label_image": "选择图片",
        "label_text": "水印文字",
        "ph_text": "输入版权文字...",
        "header_settings": "设置",
        "btn_process": "添加水印",
        "btn_download": "下载",
        "related_header": "相关工具",
        "related_favicon": "Favicon 生成器",
        "related_thumb": "缩略图下载",
        "related_img": "图片格式转换器",
        "related_qr": "QR 码生成器"
    },
    "zh-tw": {
        "title": "圖片浮水印",
        "meta_title": "圖片浮水印工具 - Utilify",
        "meta_desc": "給圖片添加自定義浮水印。保護版權。",
        "og_title": "圖片浮水印工具 - Utilify",
        "og_desc": "給圖片添加自定義浮水印。",
        "json_name": "圖片浮水印",
        "json_desc": "給圖片添加自定義浮水印。",
        "page_desc": "給圖片添加自定義浮水印。",
        "label_image": "選擇圖片",
        "label_text": "浮水印文字",
        "ph_text": "輸入版權文字...",
        "header_settings": "設置",
        "btn_process": "添加浮水印",
        "btn_download": "下載",
        "related_header": "相關工具",
        "related_favicon": "Favicon 生成器",
        "related_thumb": "縮圖下載",
        "related_img": "圖片格式轉換器",
        "related_qr": "QR 碼生成器"
    },
    "ja": {
        "title": "画像透かし",
        "meta_title": "画像透かし - Utilify",
        "meta_desc": "画像に透かしを追加して著作権を保護します。",
        "og_title": "画像透かし - Utilify",
        "og_desc": "画像に透かしを追加して著作権を保護します。",
        "json_name": "画像透かし",
        "json_desc": "画像に透かしを追加して著作権を保護します。",
        "page_desc": "画像に透かしを追加して著作権を保護します。",
        "label_image": "画像を選択",
        "label_text": "透かしテキスト",
        "ph_text": "著作権テキスト...",
        "header_settings": "設定",
        "btn_process": "透かしを追加",
        "btn_download": "ダウンロード",
        "related_header": "関連ツール",
        "related_favicon": "ファビコン生成",
        "related_thumb": "サムネイルダウンローダー",
        "related_img": "画像変換",
        "related_qr": "QRコード生成"
    },
    "hi": {
        "title": "छवि वाटरमार्क",
        "meta_title": "छवि वाटरमार्क - Utilify",
        "meta_desc": "अपनी छवियों में वाटरमार्क जोड़ें।",
        "og_title": "छवि वाटरमार्क - Utilify",
        "og_desc": "अपनी छवियों में वाटरमार्क जोड़ें।",
        "json_name": "छवि वाटरमार्क",
        "json_desc": "अपनी छवियों में वाटरमार्क जोड़ें।",
        "page_desc": "अपनी छवियों में वाटरमार्क जोड़ें।",
        "label_image": "छवि चुनें",
        "label_text": "वाटरमार्क टेक्स्ट",
        "ph_text": "कॉपीराइट टेक्स्ट...",
        "header_settings": "सेटिंग्स",
        "btn_process": "वाटरमार्क जोड़ें",
        "btn_download": "डाउनलोड करें",
        "related_header": "संबंधित उपकरण",
        "related_favicon": "फेविकॉन जेनरेटर",
        "related_thumb": "थंबनेल डाउनलोडर",
        "related_img": "छवि परिवर्तक",
        "related_qr": "QR कोड जनरेटर"
    },
    "id": {
        "title": "Tanda Air Gambar",
        "meta_title": "Tanda Air Gambar - Utilify",
        "meta_desc": "Tambahkan tanda air ke gambar Anda untuk melindungi hak cipta.",
        "og_title": "Tanda Air Gambar - Utilify",
        "og_desc": "Tambahkan tanda air ke gambar Anda untuk melindungi hak cipta.",
        "json_name": "Tanda Air Gambar",
        "json_desc": "Tambahkan tanda air ke gambar Anda untuk melindungi hak cipta.",
        "page_desc": "Tambahkan tanda air ke gambar Anda untuk melindungi hak cipta.",
        "label_image": "Pilih Gambar",
        "label_text": "Teks Tanda Air",
        "ph_text": "Teks Hak Cipta...",
        "header_settings": "Pengaturan",
        "btn_process": "Tambahkan Tanda Air",
        "btn_download": "Unduh",
        "related_header": "Alat Terkait",
        "related_favicon": "Generator Favicon",
        "related_thumb": "Pengunduh Thumbnail",
        "related_img": "Konverter Gambar",
        "related_qr": "Generator Kode QR"
    },
    "vi": {
        "title": "Đóng dấu ảnh",
        "meta_title": "Đ đóng dấu ảnh - Utilify",
        "meta_desc": "Thêm hình mờ vào hình ảnh của bạn.",
        "og_title": "Đóng dấu ảnh - Utilify",
        "og_desc": "Thêm hình mờ vào hình ảnh của bạn.",
        "json_name": "Đóng dấu ảnh",
        "json_desc": "Thêm hình mờ vào hình ảnh của bạn.",
        "page_desc": "Thêm hình mờ vào hình ảnh của bạn.",
        "label_image": "Chọn hình ảnh",
        "label_text": "Văn bản hình mờ",
        "ph_text": "Văn bản bản quyền...",
        "header_settings": "Cài đặt",
        "btn_process": "Thêm hình mờ",
        "btn_download": "Tải xuống",
        "related_header": "Công cụ liên quan",
        "related_favicon": "Tạo Favicon",
        "related_thumb": "Trình tải xuống hình thu nhỏ",
        "related_img": "Chuyển đổi hình ảnh",
        "related_qr": "Tạo mã QR"
    },
    "th": {
        "title": "ลายน้ำรูปภาพ",
        "meta_title": "ลายน้ำรูปภาพ - Utilify",
        "meta_desc": "เพิ่มลายน้ำให้กับรูปภาพของคุณ",
        "og_title": "ลายน้ำรูปภาพ - Utilify",
        "og_desc": "เพิ่มลายน้ำให้กับรูปภาพของคุณ",
        "json_name": "ลายน้ำรูปภาพ",
        "json_desc": "เพิ่มลายน้ำให้กับรูปภาพของคุณ",
        "page_desc": "เพิ่มลายน้ำให้กับรูปภาพของคุณ",
        "label_image": "เลือกรูปภาพ",
        "label_text": "ข้อความลายน้ำ",
        "ph_text": "ข้อความลิขสิทธิ์...",
        "header_settings": "การตั้งค่า",
        "btn_process": "เพิ่มลายน้ำ",
        "btn_download": "ดาวน์โหลด",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_favicon": "สร้าง Favicon",
        "related_thumb": "ดาวน์โหลดรูปขนาดย่อ",
        "related_img": "แปลงรูปภาพ",
        "related_qr": "สร้าง QR Code"
    },
    "de": {
        "title": "Bild-Wasserzeichen",
        "meta_title": "Bild-Wasserzeichen - Utilify",
        "meta_desc": "Fügen Sie Ihren Bildern Wasserzeichen hinzu.",
        "og_title": "Bild-Wasserzeichen - Utilify",
        "og_desc": "Fügen Sie Ihren Bildern Wasserzeichen hinzu.",
        "json_name": "Bild-Wasserzeichen",
        "json_desc": "Fügen Sie Ihren Bildern Wasserzeichen hinzu.",
        "page_desc": "Fügen Sie Ihren Bildern Wasserzeichen hinzu.",
        "label_image": "Bild auswählen",
        "label_text": "Wasserzeichen-Text",
        "ph_text": "Copyright-Text...",
        "header_settings": "Einstellungen",
        "btn_process": "Wasserzeichen hinzufügen",
        "btn_download": "Herunterladen",
        "related_header": "Ähnliche Tools",
        "related_favicon": "Favicon-Generator",
        "related_thumb": "Thumbnail-Downloader",
        "related_img": "Bildkonverter",
        "related_qr": "QR-Code-Generator"
    },
    "pt": {
        "title": "Marca D'água em Imagem",
        "meta_title": "Marca D'água em Imagem - Utilify",
        "meta_desc": "Adicione marcas d'água às suas imagens.",
        "og_title": "Marca D'água em Imagem - Utilify",
        "og_desc": "Adicione marcas d'água às suas imagens.",
        "json_name": "Marca D'água em Imagem",
        "json_desc": "Adicione marcas d'água às suas imagens.",
        "page_desc": "Adicione marcas d'água às suas imagens.",
        "label_image": "Selecionar Imagem",
        "label_text": "Texto da Marca D'água",
        "ph_text": "Texto de direitos autorais...",
        "header_settings": "Configurações",
        "btn_process": "Adicionar Marca D'água",
        "btn_download": "Baixar",
        "related_header": "Ferramentas Relacionadas",
        "related_favicon": "Gerador de Favicon",
        "related_thumb": "Baixador de Miniaturas",
        "related_img": "Conversor de Imagem",
        "related_qr": "Gerador de QR Code"
    }
}

COLOR_CONVERTER = {
    "en": {
        "title": "Color Converter",
        "meta_title": "Color Converter - Utilify",
        "meta_desc": "Convert between HEX, RGB, HSL color formats.",
        "og_title": "Color Converter - Utilify",
        "og_desc": "Convert between HEX, RGB, HSL color formats.",
        "json_name": "Color Converter",
        "json_desc": "Convert between HEX, RGB, HSL color formats.",
        "page_desc": "Convert between HEX, RGB, HSL color formats.",
        "header_inputs": "Color Values",
        "header_sliders": "RGB Adjust",
        "header_palette": "Popular Colors",
        "btn_copy": "Copy",
        "preview_copy": "Copy HEX",
        "related_header": "Related Tools",
        "related_img_conv": "Image Converter",
        "related_img_editor": "Image Editor",
        "related_thumb": "Thumbnail Downloader",
        "related_favicon": "Favicon Generator"
    },
    "ko": {
        "title": "색상 변환기",
        "meta_title": "색상 변환기 - Utilify",
        "meta_desc": "HEX, RGB, HSL 색상 형식 간 변환 및 실시간 미리보기.",
        "og_title": "색상 변환기 - Utilify",
        "og_desc": "HEX, RGB, HSL 색상 형식 간 변환 및 실시간 미리보기.",
        "json_name": "색상 변환기",
        "json_desc": "HEX, RGB, HSL 색상 형식 간 변환 및 실시간 미리보기.",
        "page_desc": "HEX, RGB, HSL 색상 형식 간 변환 및 실시간 미리보기.",
        "header_inputs": "색상 값",
        "header_sliders": "RGB 조절",
        "header_palette": "인기 색상",
        "btn_copy": "복사",
        "preview_copy": "복사 HEX",
        "related_header": "함께 보면 좋은 도구",
        "related_img_conv": "이미지 변환기",
        "related_img_editor": "이미지 편집기",
        "related_thumb": "썸네일 다운로더",
        "related_favicon": "파비콘 생성기"
    },
    "zh-cn": {
        "title": "颜色格式转换",
        "meta_title": "颜色格式转换 (HEX, RGB, HSL) - Utilify",
        "meta_desc": "转换 HEX, RGB, HSL, CMYK 颜色格式。颜色选择器和预览。",
        "og_title": "颜色格式转换 - Utilify",
        "og_desc": "转换 HEX, RGB, HSL, CMYK 颜色格式。",
        "json_name": "颜色格式转换",
        "json_desc": "转换 HEX, RGB, HSL, CMYK 颜色格式。",
        "page_desc": "转换 HEX, RGB, HSL, CMYK 颜色格式。",
        "header_inputs": "颜色值",
        "header_sliders": "RGB 调节",
        "header_palette": "常用颜色",
        "btn_copy": "复制",
        "preview_copy": "复制 HEX",
        "related_header": "相关工具",
        "related_img_conv": "图片格式转换器",
        "related_img_editor": "图片编辑器",
        "related_thumb": "缩略图下载",
        "related_favicon": "Favicon 生成器"
    },
    "zh-tw": {
        "title": "顏色格式轉換",
        "meta_title": "顏色格式轉換 (HEX, RGB, HSL) - Utilify",
        "meta_desc": "轉換 HEX, RGB, HSL, CMYK 顏色格式。顏色選擇器和預覽。",
        "og_title": "顏色格式轉換 - Utilify",
        "og_desc": "轉換 HEX, RGB, HSL, CMYK 顏色格式。",
        "json_name": "顏色格式轉換",
        "json_desc": "轉換 HEX, RGB, HSL, CMYK 顏色格式。",
        "page_desc": "轉換 HEX, RGB, HSL, CMYK 顏色格式。",
        "header_inputs": "顏色值",
        "header_sliders": "RGB 調節",
        "header_palette": "常用顏色",
        "btn_copy": "複製",
        "preview_copy": "複製 HEX",
        "related_header": "相關工具",
        "related_img_conv": "圖片格式轉換器",
        "related_img_editor": "圖片編輯器",
        "related_thumb": "縮圖下載",
        "related_favicon": "Favicon 生成器"
    },
    "ja": {
        "title": "色変換ツール",
        "meta_title": "色変換ツール (HEX, RGB, HSL) - Utilify",
        "meta_desc": "HEX、RGB、HSL、CMYKカラー形式を変換します。カラーピッカーとプレビュー。",
        "og_title": "色変換ツール - Utilify",
        "og_desc": "HEX、RGB、HSL、CMYKカラー形式を変換します。",
        "json_name": "色変換ツール",
        "json_desc": "HEX、RGB、HSL、CMYKカラー形式を変換します。",
        "page_desc": "HEX、RGB、HSL、CMYKカラー形式を変換します。",
        "header_inputs": "カラー値",
        "header_sliders": "RGB調整",
        "header_palette": "人気の色",
        "btn_copy": "コピー",
        "preview_copy": "HEXをコピー",
        "related_header": "関連ツール",
        "related_img_conv": "画像変換ツール",
        "related_img_editor": "画像編集ツール",
        "related_thumb": "サムネイルダウンローダー",
        "related_favicon": "ファビコン生成"
    },
    "vi": {
        "title": "Chuyển đổi màu sắc",
        "meta_title": "Chuyển đổi màu sắc (HEX, RGB, HSL) - Utilify",
        "meta_desc": "Chuyển đổi các định dạng màu HEX, RGB, HSL, CMYK. Bộ chọn màu và xem trước.",
        "og_title": "Chuyển đổi màu sắc - Utilify",
        "og_desc": "Chuyển đổi các định dạng màu HEX, RGB, HSL, CMYK.",
        "json_name": "Chuyển đổi màu sắc",
        "json_desc": "Chuyển đổi các định dạng màu HEX, RGB, HSL, CMYK.",
        "page_desc": "Chuyển đổi các định dạng màu HEX, RGB, HSL, CMYK.",
        "header_inputs": "Giá trị màu",
        "header_sliders": "Điều chỉnh RGB",
        "header_palette": "Màu phổ biến",
        "btn_copy": "Sao chép",
        "preview_copy": "Sao chép HEX",
        "related_header": "Công cụ liên quan",
        "related_img_conv": "Chuyển đổi hình ảnh",
        "related_img_editor": "Trình sửa ảnh",
        "related_thumb": "Trình tải xuống hình thu nhỏ",
        "related_favicon": "Tạo Favicon"
    },
    "th": {
        "title": "ตัวแปลงสี",
        "meta_title": "ตัวแปลงสี (HEX, RGB, HSL) - Utilify",
        "meta_desc": "แปลงรูปแบบสี HEX, RGB, HSL, CMYK ตัวเลือกสีและตัวอย่าง",
        "og_title": "ตัวแปลงสี - Utilify",
        "og_desc": "แปลงรูปแบบสี HEX, RGB, HSL, CMYK",
        "json_name": "ตัวแปลงสี",
        "json_desc": "แปลงรูปแบบสี HEX, RGB, HSL, CMYK",
        "page_desc": "แปลงรูปแบบสี HEX, RGB, HSL, CMYK",
        "header_inputs": "ค่าสี",
        "header_sliders": "ปรับ RGB",
        "header_palette": "สียอดนิยม",
        "btn_copy": "คัดลอก",
        "preview_copy": "คัดลอก HEX",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_img_conv": "ตัวแปลงรูปภาพ",
        "related_img_editor": "ตัวแก้ไขรูปภาพ",
        "related_thumb": "ดาวน์โหลดรูปขนาดย่อ",
        "related_favicon": "สร้าง Favicon"
    },
    "de": {
        "title": "Farbkonverter",
        "meta_title": "Farbkonverter (HEX, RGB, HSL) - Utilify",
        "meta_desc": "Konvertieren Sie HEX, RGB, HSL, CMYK Farbformate. Farbwähler und Vorschau.",
        "og_title": "Farbkonverter - Utilify",
        "og_desc": "Konvertieren Sie HEX, RGB, HSL, CMYK Farbformate.",
        "json_name": "Farbkonverter",
        "json_desc": "Konvertieren Sie HEX, RGB, HSL, CMYK Farbformate.",
        "page_desc": "Konvertieren Sie HEX, RGB, HSL, CMYK Farbformate.",
        "header_inputs": "Farbwerte",
        "header_sliders": "RGB anpassen",
        "header_palette": "Beliebte Farben",
        "btn_copy": "Kopieren",
        "preview_copy": "HEX kopieren",
        "related_header": "Ähnliche Tools",
        "related_img_conv": "Bildkonverter",
        "related_img_editor": "Bildbearbeiter",
        "related_thumb": "Thumbnail-Downloader",
        "related_favicon": "Favicon-Generator"
    },
    "pt": {
        "title": "Conversor de Cores",
        "meta_title": "Conversor de Cores (HEX, RGB, HSL) - Utilify",
        "meta_desc": "Converta formatos de cor HEX, RGB, HSL, CMYK. Seletor de cores e visualização.",
        "og_title": "Conversor de Cores - Utilify",
        "og_desc": "Converta formatos de cor HEX, RGB, HSL, CMYK.",
        "json_name": "Conversor de Cores",
        "json_desc": "Converta formatos de cor HEX, RGB, HSL, CMYK.",
        "page_desc": "Converta formatos de cor HEX, RGB, HSL, CMYK.",
        "header_inputs": "Valores de Cor",
        "header_sliders": "Ajuste RGB",
        "header_palette": "Cores Populares",
        "btn_copy": "Copiar",
        "preview_copy": "Copiar HEX",
        "related_header": "Ferramentas Relacionadas",
        "related_img_conv": "Conversor de Imagem",
        "related_img_editor": "Editor de Imagem",
        "related_thumb": "Baixador de Miniaturas",
        "related_favicon": "Gerador de Favicon"
    },
    "id": {
        "title": "Konverter Warna",
        "meta_title": "Konverter Warna (HEX, RGB, HSL) - Utilify",
        "meta_desc": "Konversi format warna HEX, RGB, HSL, CMYK. Pemilih warna dan pratinjau.",
        "og_title": "Konverter Warna - Utilify",
        "og_desc": "Konversi format warna HEX, RGB, HSL, CMYK.",
        "json_name": "Konverter Warna",
        "json_desc": "Konversi format warna HEX, RGB, HSL, CMYK.",
        "page_desc": "Konversi format warna HEX, RGB, HSL, CMYK.",
        "header_inputs": "Nilai Warna",
        "header_sliders": "Sesuaikan RGB",
        "header_palette": "Warna Populer",
        "btn_copy": "Salin",
        "preview_copy": "Salin HEX",
        "related_header": "Alat Terkait",
        "related_img_conv": "Konverter Gambar",
        "related_img_editor": "Editor Gambar",
        "related_thumb": "Pengunduh Thumbnail",
        "related_favicon": "Generator Favicon"
    },
    "hi": {
        "title": "रंग परिवर्तक",
        "meta_title": "रंग परिवर्तक (HEX, RGB, HSL) - Utilify",
        "meta_desc": "HEX, RGB, HSL, CMYK रंग प्रारूपों को बदलें। रंग चयनकर्ता और पूर्वावलोकन।",
        "og_title": "रंग परिवर्तक - Utilify",
        "og_desc": "HEX, RGB, HSL, CMYK रंग प्रारूपों को बदलें।",
        "json_name": "रंग परिवर्तक",
        "json_desc": "HEX, RGB, HSL, CMYK रंग प्रारूपों को बदलें।",
        "page_desc": "HEX, RGB, HSL, CMYK रंग प्रारूपों को बदलें।",
        "header_inputs": "रंग मान",
        "header_sliders": "RGB समायोजन",
        "header_palette": "लोकप्रिय रंग",
        "btn_copy": "कॉपी",
        "preview_copy": "HEX कॉपी करें",
        "related_header": "संबंधित उपकरण",
        "related_img_conv": "छवि परिवर्तक",
        "related_img_editor": "छवि संपादक",
        "related_thumb": "थंबनेल डाउनलोडर",
        "related_favicon": "फेविकॉन जेनरेटर"
    }
}

LOREM_IPSUM = {
    "en": {
        "title": "Lorem Ipsum Generator",
        "meta_title": "Lorem Ipsum Generator - Utilify",
        "meta_desc": "Generate Lorem Ipsum dummy text.",
        "og_title": "Lorem Ipsum Generator - Utilify",
        "og_desc": "Generate Lorem Ipsum dummy text.",
        "json_name": "Lorem Ipsum Generator",
        "json_desc": "Generate Lorem Ipsum dummy text.",
        "page_desc": "Generate Lorem Ipsum dummy text.",
        "label_type": "Type:",
        "opt_para": "Paragraphs",
        "opt_word": "Words",
        "opt_sent": "Sentences",
        "label_count": "Count:",
        "btn_generate": "Generate",
        "btn_copy": "Copy",
        "related_header": "Related Tools",
        "related_text": "Text Utils",
        "related_diff": "Diff Checker",
        "related_regex": "Regex Tester",
        "related_md": "Markdown Preview",
        "alert_empty": "Generate text first."
    },
    "ko": {
        "title": "Lorem Ipsum 생성기",
        "meta_title": "Lorem Ipsum 생성기 - Utilify",
        "meta_desc": "Lorem Ipsum 더미 텍스트를 생성하세요.",
        "og_title": "Lorem Ipsum 생성기 - Utilify",
        "og_desc": "Lorem Ipsum 더미 텍스트를 생성하세요.",
        "json_name": "Lorem Ipsum 생성기",
        "json_desc": "Lorem Ipsum 더미 텍스트를 생성하세요.",
        "page_desc": "Lorem Ipsum 더미 텍스트를 생성하세요.",
        "label_type": "타입:",
        "opt_para": "단락",
        "opt_word": "단어",
        "opt_sent": "문장",
        "label_count": "개수:",
        "btn_generate": "생성",
        "btn_copy": "복사",
        "related_header": "함께 보면 좋은 도구",
        "related_text": "텍스트 유틸리티",
        "related_diff": "텍스트 비교기",
        "related_regex": "정규식 테스터",
        "related_md": "마크다운 미리보기",
        "alert_empty": "먼저 텍스트를 생성하세요."
    },
    "zh-cn": {
        "title": "Lorem Ipsum 生成器",
        "meta_title": "Lorem Ipsum 生成器 - Utilify",
        "meta_desc": "生成 Lorem Ipsum 占位符文本。段落，句子，单词。",
        "og_title": "Lorem Ipsum 生成器 - Utilify",
        "og_desc": "生成 Lorem Ipsum 占位符文本。",
        "json_name": "Lorem Ipsum 生成器",
        "json_desc": "生成 Lorem Ipsum 占位符文本。",
        "page_desc": "生成 Lorem Ipsum 占位符文本。",
        "label_type": "类型:",
        "opt_para": "段落",
        "opt_word": "单词",
        "opt_sent": "句子",
        "label_count": "数量:",
        "btn_generate": "生成",
        "btn_copy": "复制",
        "related_header": "相关工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差异对比",
        "related_regex": "正则表达式测试",
        "related_md": "Markdown 预览",
        "alert_empty": "请先生成文本。"
    },
    "zh-tw": {
        "title": "Lorem Ipsum 生成器",
        "meta_title": "Lorem Ipsum 生成器 - Utilify",
        "meta_desc": "生成 Lorem Ipsum 佔位符文本。段落，句子，單詞。",
        "og_title": "Lorem Ipsum 生成器 - Utilify",
        "og_desc": "生成 Lorem Ipsum 佔位符文本。",
        "json_name": "Lorem Ipsum 生成器",
        "json_desc": "生成 Lorem Ipsum 佔位符文本。",
        "page_desc": "生成 Lorem Ipsum 佔位符文本。",
        "label_type": "類型:",
        "opt_para": "段落",
        "opt_word": "單字",
        "opt_sent": "句子",
        "label_count": "數量:",
        "btn_generate": "生成",
        "btn_copy": "複製",
        "related_header": "相關工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差異比對",
        "related_regex": "正則表達式測試",
        "related_md": "Markdown 預覽",
        "alert_empty": "請先生成文本。"
    },
    "ja": {
        "title": "Lorem Ipsum生成",
        "meta_title": "Lorem Ipsum生成 - Utilify",
        "meta_desc": "Lorem Ipsumダミーテキストを生成します。段落、文、単語。",
        "og_title": "Lorem Ipsum生成 - Utilify",
        "og_desc": "Lorem Ipsumダミーテキストを生成します。",
        "json_name": "Lorem Ipsum生成",
        "json_desc": "Lorem Ipsumダミーテキストを生成します。",
        "page_desc": "Lorem Ipsumダミーテキストを生成します。",
        "label_type": "タイプ:",
        "opt_para": "段落",
        "opt_word": "単語",
        "opt_sent": "文",
        "label_count": "数:",
        "btn_generate": "生成",
        "btn_copy": "コピー",
        "related_header": "関連ツール",
        "related_text": "テキストユーティリティ",
        "related_diff": "テキスト比較",
        "related_regex": "正規表現テスター",
        "related_md": "Markdownプレビュー",
        "alert_empty": "まずテキストを生成してください。"
    },
    "vi": {
        "title": "Tạo Lorem Ipsum",
        "meta_title": "Tạo Lorem Ipsum - Utilify",
        "meta_desc": "Tạo văn bản giả Lorem Ipsum. Đoạn văn, câu, từ.",
        "og_title": "Tạo Lorem Ipsum - Utilify",
        "og_desc": "Tạo văn bản giả Lorem Ipsum.",
        "json_name": "Tạo Lorem Ipsum",
        "json_desc": "Tạo văn bản giả Lorem Ipsum.",
        "page_desc": "Tạo văn bản giả Lorem Ipsum.",
        "label_type": "Loại:",
        "opt_para": "Đoạn văn",
        "opt_word": "Từ",
        "opt_sent": "Câu",
        "label_count": "Số lượng:",
        "btn_generate": "Tạo",
        "btn_copy": "Sao chép",
        "related_header": "Công cụ liên quan",
        "related_text": "Tiện ích văn bản",
        "related_diff": "Kiểm tra sự khác biệt",
        "related_regex": "Kiểm tra Regex",
        "related_md": "Xem trước Markdown",
        "alert_empty": "Tạo văn bản trước."
    },
    "th": {
        "title": "สร้าง Lorem Ipsum",
        "meta_title": "สร้าง Lorem Ipsum - Utilify",
        "meta_desc": "สร้างข้อความจำลอง Lorem Ipsum ย่อหน้า ประโยค คำ",
        "og_title": "สร้าง Lorem Ipsum - Utilify",
        "og_desc": "สร้างข้อความจำลอง Lorem Ipsum",
        "json_name": "สร้าง Lorem Ipsum",
        "json_desc": "สร้างข้อความจำลอง Lorem Ipsum",
        "page_desc": "สร้างข้อความจำลอง Lorem Ipsum",
        "label_type": "ประเภท:",
        "opt_para": "ย่อหน้า",
        "opt_word": "คำ",
        "opt_sent": "ประโยค",
        "label_count": "จำนวน:",
        "btn_generate": "สร้าง",
        "btn_copy": "คัดลอก",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_text": "เครื่องมือข้อความ",
        "related_diff": "ตรวจสอบความแตกต่าง",
        "related_regex": "ทดสอบ Regex",
        "related_md": "ดูตัวอย่าง Markdown",
        "alert_empty": "สร้างข้อความก่อน"
    },
    "de": {
        "title": "Lorem Ipsum Generator",
        "meta_title": "Lorem Ipsum Generator - Utilify",
        "meta_desc": "Generieren Sie Lorem Ipsum Blindtext. Absätze, Sätze, Wörter.",
        "og_title": "Lorem Ipsum Generator - Utilify",
        "og_desc": "Generieren Sie Lorem Ipsum Blindtext.",
        "json_name": "Lorem Ipsum Generator",
        "json_desc": "Generieren Sie Lorem Ipsum Blindtext.",
        "page_desc": "Generieren Sie Lorem Ipsum Blindtext.",
        "label_type": "Typ:",
        "opt_para": "Absätze",
        "opt_word": "Wörter",
        "opt_sent": "Sätze",
        "label_count": "Anzahl:",
        "btn_generate": "Generieren",
        "btn_copy": "Kopieren",
        "related_header": "Ähnliche Tools",
        "related_text": "Text-Dienstprogramme",
        "related_diff": "Text-Diff-Checker",
        "related_regex": "Regex-Tester",
        "related_md": "Markdown-Vorschau",
        "alert_empty": "Zuerst Text generieren."
    },
    "pt": {
        "title": "Gerador de Lorem Ipsum",
        "meta_title": "Gerador de Lorem Ipsum - Utilify",
        "meta_desc": "Gere texto fictício Lorem Ipsum. Parágrafos, frases, palavras.",
        "og_title": "Gerador de Lorem Ipsum - Utilify",
        "og_desc": "Gere texto fictício Lorem Ipsum.",
        "json_name": "Gerador de Lorem Ipsum",
        "json_desc": "Gere texto fictício Lorem Ipsum.",
        "page_desc": "Gere texto fictício Lorem Ipsum.",
        "label_type": "Tipo:",
        "opt_para": "Parágrafos",
        "opt_word": "Palavras",
        "opt_sent": "Frases",
        "label_count": "Contagem:",
        "btn_generate": "Gerar",
        "btn_copy": "Copiar",
        "related_header": "Ferramentas Relacionadas",
        "related_text": "Utilitários de Texto",
        "related_diff": "Verificador de Diferenças",
        "related_regex": "Testador de Regex",
        "related_md": "Pré-visualização Markdown",
        "alert_empty": "Gere o texto primeiro."
    },
    "id": {
        "title": "Generator Lorem Ipsum",
        "meta_title": "Generator Lorem Ipsum - Utilify",
        "meta_desc": "Hasilkan teks dummy Lorem Ipsum. Paragraf, kalimat, kata.",
        "og_title": "Generator Lorem Ipsum - Utilify",
        "og_desc": "Hasilkan teks dummy Lorem Ipsum.",
        "json_name": "Generator Lorem Ipsum",
        "json_desc": "Hasilkan teks dummy Lorem Ipsum.",
        "page_desc": "Hasilkan teks dummy Lorem Ipsum.",
        "label_type": "Tipe:",
        "opt_para": "Paragraf",
        "opt_word": "Kata",
        "opt_sent": "Kalimat",
        "label_count": "Jumlah:",
        "btn_generate": "Hasilkan",
        "btn_copy": "Salin",
        "related_header": "Alat Terkait",
        "related_text": "Utilitas Teks",
        "related_diff": "Pemeriksa Perbedaan Teks",
        "related_regex": "Penguji Regex",
        "related_md": "Pratinjau Markdown",
        "alert_empty": "Hasilkan teks terlebih dahulu."
    },
    "hi": {
        "title": "लोरेम इप्सम जनरेटर",
        "meta_title": "लोरेम इप्सम जनरेटर - Utilify",
        "meta_desc": "लोरेम इप्सम डमी टेक्स्ट जनरेट करें। पैराग्राफ, वाक्य, शब्द।",
        "og_title": "लोरेम इप्सम जनरेटर - Utilify",
        "og_desc": "लोरेम इप्सम डमी टेक्स्ट जनरेट करें।",
        "json_name": "लोरेम इप्सम जनरेटर",
        "json_desc": "लोरेम इप्सम डमी टेक्स्ट जनरेट करें।",
        "page_desc": "लोरेम इप्सम डमी टेक्स्ट जनरेट करें।",
        "label_type": "प्रकार:",
        "opt_para": "पैराग्राफ",
        "opt_word": "शब्द",
        "opt_sent": "वाक्य",
        "label_count": "गिनती:",
        "btn_generate": "उत्पन्न करें",
        "btn_copy": "कॉपी",
        "related_header": "संबंधित उपकरण",
        "related_text": "टेक्स्ट यूटिलिटीज",
        "related_diff": "टेक्स्ट डिफ चेकर",
        "related_regex": "रेगेक्स टेस्टर",
        "related_md": "मार्कडाउन पूर्वावलोकन",
        "alert_empty": "पहले टेक्स्ट उत्पन्न करें।"
    }
}

MARKDOWN_PREVIEWER = {
    "en": {
        "title": "Markdown Editor & Preview",
        "meta_title": "Markdown Editor & Preview - Utilify",
        "meta_desc": "Real-time Markdown preview tool. Write Markdown effortlessly and see converted HTML instantly.",
        "og_title": "Markdown Editor & Preview - Utilify",
        "og_desc": "Real-time Markdown preview tool. Write Markdown effortlessly and see converted HTML instantly.",
        "json_name": "Markdown Editor & Preview",
        "json_desc": "Real-time Markdown preview tool. Write Markdown effortlessly and see converted HTML instantly.",
        "page_desc": "Real-time Markdown preview tool. Write Markdown effortlessly and see converted HTML instantly.",
        "adsense_text": "Ad Space",
        "btn_html": "Copy HTML",
        "btn_download": "Download .md",
        "label_input": "Markdown Input",
        "ph_input": "# Enter Title\n\n**Bold** and *Italic*...",
        "label_preview": "Preview",
        "related_header": "Related Tools",
        "related_text": "Text Utils",
        "related_diff": "Diff Checker",
        "related_regex": "Regex Tester",
        "related_lorem": "Lorem Ipsum"
    },
    "ko": {
        "title": "마크다운 에디터 & 미리보기",
        "meta_title": "마크다운 에디터 & 미리보기 - Utilify",
        "meta_desc": "실시간 마크다운 미리보기 도구. 손쉽게 마크다운 문서를 작성하고 변환된 HTML 결과를 확인하세요.",
        "og_title": "마크다운 에디터 & 미리보기 - Utilify",
        "og_desc": "실시간 마크다운 미리보기 도구. 손쉽게 마크다운 문서를 작성하고 변환된 HTML 결과를 확인하세요.",
        "json_name": "마크다운 에디터 & 미리보기",
        "json_desc": "실시간 마크다운 미리보기 도구. 손쉽게 마크다운 문서를 작성하고 변환된 HTML 결과를 확인하세요.",
        "page_desc": "실시간 마크다운 미리보기 도구. 손쉽게 마크다운 문서를 작성하고 변환된 HTML 결과를 확인하세요.",
        "adsense_text": "광고 영역",
        "btn_html": "HTML 복사",
        "btn_download": "MD 다운로드",
        "label_input": "마크다운 입력",
        "ph_input": "# 제목을 입력하세요\n\n**굵은 글씨**와 *이탤릭*...",
        "label_preview": "미리보기",
        "related_header": "함께 보면 좋은 도구",
        "related_text": "텍스트 유틸리티",
        "related_diff": "텍스트 비교기",
        "related_regex": "정규식 테스터",
        "related_lorem": "입숨 생성기"
    },
    "ja": {
        "title": "マークダウンエディタ＆プレビュー",
        "meta_title": "マークダウンエディタ＆プレビュー - Utilify",
        "meta_desc": "リアルタイムマークダウンプレビューツール。マークダウンを簡単に作成し、変換されたHTMLを即座に確認できます。",
        "og_title": "マークダウンエディタ＆プレビュー - Utilify",
        "og_desc": "リアルタイムマークダウンプレビューツール。マークダウンを簡単に作成し、変換されたHTMLを即座に確認できます。",
        "json_name": "マークダウンエディタ＆プレビュー",
        "json_desc": "リアルタイムマークダウンプレビューツール。マークダウンを簡単に作成し、変換されたHTMLを即座に確認できます。",
        "page_desc": "リアルタイムマークダウンプレビューツール。マークダウンを簡単に作成し、変換されたHTMLを即座に確認できます。",
        "adsense_text": "広告スペース",
        "btn_html": "HTMLをコピー",
        "btn_download": "MDをダウンロード",
        "label_input": "マークダウン入力",
        "ph_input": "# タイトルを入力\n\n**太字** と *イタリック*...",
        "label_preview": "プレビュー",
        "related_header": "関連ツール",
        "related_text": "テキストユーティリティ",
        "related_diff": "テキスト比較",
        "related_regex": "正規表現テスター",
        "related_lorem": "Lorem Ipsum生成"
    },
    "hi": {
        "title": "मार्कडाउन एडिटर और पूर्वावलोकन",
        "meta_title": "मार्कडाउन एडिटर और पूर्वावलोकन - Utilify",
        "meta_desc": "रीयल-टाइम मार्कडाउन पूर्वावलोकन टूल। आसानी से मार्कडाउन लिखें और तुरंत परिवर्तित HTML देखें।",
        "og_title": "मार्कडाउन एडिटर और पूर्वावलोकन - Utilify",
        "og_desc": "रीयल-टाइम मार्कडाउन पूर्वावलोकन टूल। आसानी से मार्कडाउन लिखें और तुरंत परिवर्तित HTML देखें।",
        "json_name": "मार्कडाउन एडिटर और पूर्वावलोकन",
        "json_desc": "रीयल-टाइम मार्कडाउन पूर्वावलोकन टूल। आसानी से मार्कडाउन लिखें और तुरंत परिवर्तित HTML देखें।",
        "page_desc": "रीयल-टाइम मार्कडाउन पूर्वावलोकन टूल। आसानी से मार्कडाउन लिखें और तुरंत परिवर्तित HTML देखें।",
        "adsense_text": "विज्ञापन स्थान",
        "btn_html": "HTML कॉपी करें",
        "btn_download": "MD डाउनलोड करें",
        "label_input": "मार्कडाउन इनपुट",
        "ph_input": "# शीर्षक दर्ज करें\n\n**बोल्ड** और *इटैलिक*...",
        "label_preview": "पूर्वावलोकन",
        "related_header": "संबंधित उपकरण",
        "related_text": "टेक्स्ट यूटिलिटीज",
        "related_diff": "टेक्स्ट डिफ चेकर",
        "related_regex": "रेगेक्स टेस्टर",
        "related_lorem": "लोरेम इप्सम"
    },
    "id": {
        "title": "Editor & Pratinjau Markdown",
        "meta_title": "Editor & Pratinjau Markdown - Utilify",
        "meta_desc": "Alat pratinjau Markdown waktu nyata. Tulis Markdown dengan mudah dan lihat hasil HTML yang dikonversi secara instan.",
        "og_title": "Editor & Pratinjau Markdown - Utilify",
        "og_desc": "Alat pratinjau Markdown waktu nyata. Tulis Markdown dengan mudah dan lihat hasil HTML yang dikonversi secara instan.",
        "json_name": "Editor & Pratinjau Markdown",
        "json_desc": "Alat pratinjau Markdown waktu nyata. Tulis Markdown dengan mudah dan lihat hasil HTML yang dikonversi secara instan.",
        "page_desc": "Alat pratinjau Markdown waktu nyata. Tulis Markdown dengan mudah dan lihat hasil HTML yang dikonversi secara instan.",
        "adsense_text": "Ruang Iklan",
        "btn_html": "Salin HTML",
        "btn_download": "Unduh MD",
        "label_input": "Input Markdown",
        "ph_input": "# Masukkan Judul\n\n**Tebal** dan *Miring*...",
        "label_preview": "Pratinjau",
        "related_header": "Alat Terkait",
        "related_text": "Utilitas Teks",
        "related_diff": "Pemeriksa Perbedaan Teks",
        "related_regex": "Penguji Regex",
        "related_lorem": "Generator Lorem Ipsum"
    },
    "vi": {
        "title": "Trình biên tập & Xem trước Markdown",
        "meta_title": "Trình biên tập & Xem trước Markdown - Utilify",
        "meta_desc": "Công cụ xem trước Markdown thời gian thực. Viết Markdown dễ dàng và xem kết quả HTML được chuyển đổi ngay lập tức.",
        "og_title": "Trình biên tập & Xem trước Markdown - Utilify",
        "og_desc": "Công cụ xem trước Markdown thời gian thực. Viết Markdown dễ dàng và xem kết quả HTML được chuyển đổi ngay lập tức.",
        "json_name": "Trình biên tập & Xem trước Markdown",
        "json_desc": "Công cụ xem trước Markdown thời gian thực. Viết Markdown dễ dàng và xem kết quả HTML được chuyển đổi ngay lập tức.",
        "page_desc": "Công cụ xem trước Markdown thời gian thực. Viết Markdown dễ dàng và xem kết quả HTML được chuyển đổi ngay lập tức.",
        "adsense_text": "Không gian quảng cáo",
        "btn_html": "Sao chép HTML",
        "btn_download": "Tải xuống MD",
        "label_input": "Đầu vào Markdown",
        "ph_input": "# Nhập tiêu đề\n\n**Đậm** và *Nghiêng*...",
        "label_preview": "Xem trước",
        "related_header": "Công cụ liên quan",
        "related_text": "Tiện ích văn bản",
        "related_diff": "Kiểm tra sự khác biệt",
        "related_regex": "Kiểm tra Regex",
        "related_lorem": "Tạo Lorem Ipsum"
    },
    "th": {
        "title": "ตัวแก้ไขและแสดงตัวอย่าง Markdown",
        "meta_title": "ตัวแก้ไขและแสดงตัวอย่าง Markdown - Utilify",
        "meta_desc": "เครื่องมือแสดงตัวอย่าง Markdown แบบเรียลไทม์ เขียน Markdown ได้อย่างง่ายดายและดูผลลัพธ์ HTML ที่แปลงแล้วได้ทันที",
        "og_title": "ตัวแก้ไขและแสดงตัวอย่าง Markdown - Utilify",
        "og_desc": "เครื่องมือแสดงตัวอย่าง Markdown แบบเรียลไทม์ เขียน Markdown ได้อย่างง่ายดายและดูผลลัพธ์ HTML ที่แปลงแล้วได้ทันที",
        "json_name": "ตัวแก้ไขและแสดงตัวอย่าง Markdown",
        "json_desc": "เครื่องมือแสดงตัวอย่าง Markdown แบบเรียลไทม์ เขียน Markdown ได้อย่างง่ายดายและดูผลลัพธ์ HTML ที่แปลงแล้วได้ทันที",
        "page_desc": "เครื่องมือแสดงตัวอย่าง Markdown แบบเรียลไทม์ เขียน Markdown ได้อย่างง่ายดายและดูผลลัพธ์ HTML ที่แปลงแล้วได้ทันที",
        "adsense_text": "พื้นที่โฆษณา",
        "btn_html": "คัดลอก HTML",
        "btn_download": "ดาวน์โหลด MD",
        "label_input": "อินพุต Markdown",
        "ph_input": "# ใส่หัวข้อ\n\n**ตัวหนา** และ *ตัวเอียง*...",
        "label_preview": "ตัวอย่าง",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_text": "เครื่องมือข้อความ",
        "related_diff": "ตรวจสอบความแตกต่าง",
        "related_regex": "ทดสอบ Regex",
        "related_lorem": "สร้าง Lorem Ipsum"
    },
    "de": {
        "title": "Markdown-Editor & Vorschau",
        "meta_title": "Markdown-Editor & Vorschau - Utilify",
        "meta_desc": "Echtzeit-Markdown-Vorschau-Tool. Schreiben Sie Markdown mühelos und sehen Sie sofort das konvertierte HTML.",
        "og_title": "Markdown-Editor & Vorschau - Utilify",
        "og_desc": "Echtzeit-Markdown-Vorschau-Tool. Schreiben Sie Markdown mühelos und sehen Sie sofort das konvertierte HTML.",
        "json_name": "Markdown-Editor & Vorschau",
        "json_desc": "Echtzeit-Markdown-Vorschau-Tool. Schreiben Sie Markdown mühelos und sehen Sie sofort das konvertierte HTML.",
        "page_desc": "Echtzeit-Markdown-Vorschau-Tool. Schreiben Sie Markdown mühelos und sehen Sie sofort das konvertierte HTML.",
        "adsense_text": "Werbefläche",
        "btn_html": "HTML kopieren",
        "btn_download": "MD herunterladen",
        "label_input": "Markdown Eingabe",
        "ph_input": "# Titel eingeben\n\n**Fett** und *Kursiv*...",
        "label_preview": "Vorschau",
        "related_header": "Ähnliche Tools",
        "related_text": "Text-Dienstprogramme",
        "related_diff": "Text-Diff-Checker",
        "related_regex": "Regex-Tester",
        "related_lorem": "Lorem Ipsum Generator"
    },
    "pt": {
        "title": "Editor e Visualização de Markdown",
        "meta_title": "Editor e Visualização de Markdown - Utilify",
        "meta_desc": "Ferramenta de visualização Markdown em tempo real. Escreva Markdown sem esforço e veja o HTML convertido instantaneamente.",
        "og_title": "Editor e Visualização de Markdown - Utilify",
        "og_desc": "Ferramenta de visualização Markdown em tempo real. Escreva Markdown sem esforço e veja o HTML convertido instantaneamente.",
        "json_name": "Editor e Visualização de Markdown",
        "json_desc": "Ferramenta de visualização Markdown em tempo real. Escreva Markdown sem esforço e veja o HTML convertido instantaneamente.",
        "page_desc": "Ferramenta de visualização Markdown em tempo real. Escreva Markdown sem esforço e veja o HTML convertido instantaneamente.",
        "adsense_text": "Espaço Publicitário",
        "btn_html": "Copiar HTML",
        "btn_download": "Baixar MD",
        "label_input": "Entrada Markdown",
        "ph_input": "# Digite o Título\n\n**Negrito** e *Itálico*...",
        "label_preview": "Visualização",
        "related_header": "Ferramentas Relacionadas",
        "related_text": "Utilitários de Texto",
        "related_diff": "Verificador de Diferenças",
        "related_regex": "Testador de Regex",
        "related_lorem": "Gerador de Lorem Ipsum"
    },
    "zh-cn": {
        "title": "Markdown 编辑器 & 预览",
        "meta_title": "Markdown 编辑器 & 预览 - Utilify",
        "meta_desc": "实时 Markdown 预览工具。轻松编写 Markdown 并立即查看转换后的 HTML。",
        "og_title": "Markdown 编辑器 & 预览 - Utilify",
        "og_desc": "实时 Markdown 预览工具。轻松编写 Markdown 并立即查看转换后的 HTML。",
        "json_name": "Markdown 编辑器 & 预览",
        "json_desc": "实时 Markdown 预览工具。轻松编写 Markdown 并立即查看转换后的 HTML。",
        "page_desc": "实时 Markdown 预览工具。轻松编写 Markdown 并立即查看转换后的 HTML。",
        "adsense_text": "广告位",
        "btn_html": "复制 HTML",
        "btn_download": "下载 .md",
        "label_input": "Markdown 输入",
        "ph_input": "# 输入标题\n\n**粗体** 和 *斜体*...",
        "label_preview": "预览",
        "related_header": "相关工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差异对比",
        "related_regex": "正则表达式测试",
        "related_lorem": "Lorem Ipsum 生成器"
    },
    "zh-tw": {
        "title": "Markdown 編輯器 & 預覽",
        "meta_title": "Markdown 編輯器 & 預覽 - Utilify",
        "meta_desc": "實時 Markdown 預覽工具。輕鬆編寫 Markdown 並立即查看轉換後的 HTML。",
        "og_title": "Markdown 編輯器 & 預覽 - Utilify",
        "og_desc": "實時 Markdown 預覽工具。輕鬆編寫 Markdown 並立即查看轉換後的 HTML。",
        "json_name": "Markdown 編輯器 & 預覽",
        "json_desc": "實時 Markdown 預覽工具。輕鬆編寫 Markdown 並立即查看轉換後的 HTML。",
        "page_desc": "實時 Markdown 預覽工具。輕鬆編寫 Markdown 並立即查看轉換後的 HTML。",
        "adsense_text": "廣告位",
        "btn_html": "複製 HTML",
        "btn_download": "下載 .md",
        "label_input": "Markdown 輸入",
        "ph_input": "# 輸入標題\n\n**粗體** 和 *斜體*... ",
        "label_preview": "預覽",
        "related_header": "相關工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差異比對",
        "related_regex": "正則表達式測試",
        "related_lorem": "Lorem Ipsum 生成器"
    }
}

REGEX_TESTER = {
    "en": {
        "title": "Regex Tester",
        "meta_title": "Regex Tester - Utilify",
        "meta_desc": "Test regular expressions in real-time.",
        "og_title": "Regex Tester - Utilify",
        "og_desc": "Test regular expressions in real-time.",
        "json_name": "Regex Tester",
        "json_desc": "Test regular expressions in real-time.",
        "page_desc": "Test regular expressions in real-time.",
        "label_pattern": "Pattern",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Case insensitive)",
        "label_m": "m (Multiline)",
        "label_test": "Test String",
        "ph_test": "Enter test string",
        "related_header": "Related Tools",
        "related_text": "Text Utils",
        "related_diff": "Diff Checker",
        "related_md": "Markdown Preview",
        "related_lorem": "Lorem Ipsum",
        "res_no_match": "No matches found",
        "res_match": "Matches",
        "res_highlight": "Highlight",
        "res_error": "Error"
    },
    "ko": {
        "title": "정규식 테스터",
        "meta_title": "정규식 테스터 - Utilify",
        "meta_desc": "정규식 패턴을 테스트하고 매칭 결과를 실시간으로 확인하세요.",
        "og_title": "정규식 테스터 - Utilify",
        "og_desc": "정규식 패턴을 테스트하고 매칭 결과를 실시간으로 확인하세요.",
        "json_name": "정규식 테스터",
        "json_desc": "정규식 패턴을 테스트하고 매칭 결과를 실시간으로 확인하세요.",
        "page_desc": "정규식 패턴을 테스트하고 매칭 결과를 실시간으로 확인하세요.",
        "label_pattern": "정규식 패턴",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (전역)",
        "label_i": "i (대소문자 무시)",
        "label_m": "m (여러 줄)",
        "label_test": "테스트 문자열",
        "ph_test": "테스트할 문자열을 입력하세요",
        "related_header": "함께 보면 좋은 도구",
        "related_text": "텍스트 유틸리티",
        "related_diff": "텍스트 비교기",
        "related_md": "마크다운 미리보기",
        "related_lorem": "입숨 생성기",
        "res_no_match": "매칭 결과 없음",
        "res_match": "매칭 결과",
        "res_highlight": "하이라이트",
        "res_error": "오류"
    },
    "ja": {
        "title": "正規表現テスター",
        "meta_title": "正規表現テスター - Utilify",
        "meta_desc": "リアルタイムで正規表現パターンをテストします。",
        "og_title": "正規表現テスター - Utilify",
        "og_desc": "リアルタイムで正規表現パターンをテストします。",
        "json_name": "正規表現テスター",
        "json_desc": "リアルタイムで正規表現パターンをテストします。",
        "page_desc": "リアルタイムで正規表現パターンをテストします。",
        "label_pattern": "パターン",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (グローバル)",
        "label_i": "i (大文字小文字無視)",
        "label_m": "m (複数行)",
        "label_test": "テスト文字列",
        "ph_test": "テスト文字列を入力",
        "related_header": "関連ツール",
        "related_text": "テキストユーティリティ",
        "related_diff": "テキスト比較",
        "related_md": "マークダウンプレビュー",
        "related_lorem": "Lorem Ipsum生成",
        "res_no_match": "一致は見つかりませんでした",
        "res_match": "一致",
        "res_highlight": "ハイライト",
        "res_error": "エラー"
    },
    "hi": {
        "title": "रे제क्स टेस्टर (Regex Tester)",
        "meta_title": "रे제क्स टेस्टर - Utilify",
        "meta_desc": "रीयल-टाइम में रेगुलर एक्सप्रेशन पैटर्न का परीक्षण करें।",
        "og_title": "रे제क्स टेस्टर - Utilify",
        "og_desc": "रीयल-टाइम में रेगुलर एक्सप्रेशन पैटर्न का परीक्षण करें।",
        "json_name": "रे제क्स टेस्टर",
        "json_desc": "रीयल-टाइम में रेगुलर एक्सप्रेशन पैटर्न का परीक्षण करें।",
        "page_desc": "रीयल-टाइम में रेगुलर एक्सप्रेशन पैटर्न का परीक्षण करें।",
        "label_pattern": "पैटर्न",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Case insensitive)",
        "label_m": "m (Multiline)",
        "label_test": "परीक्षण स्ट्रिंग",
        "ph_test": "परीक्षण स्ट्रिंग दर्ज करें",
        "related_header": "संबंधित उपकरण",
        "related_text": "टेक्स्ट यूटिलिटीज",
        "related_diff": "टेक्स्ट डिफ चेकर",
        "related_md": "मार्कडाउन पूर्वावलोकन",
        "related_lorem": "लोरेम इप्सम",
        "res_no_match": "कोई मेल नहीं मिला",
        "res_match": "मेल",
        "res_highlight": "हाइलाइट",
        "res_error": "त्रुटि"
    },
    "id": {
        "title": "Penguji Regex",
        "meta_title": "Penguji Regex - Utilify",
        "meta_desc": "Uji ekspresi reguler secara waktu nyata.",
        "og_title": "Penguji Regex - Utilify",
        "og_desc": "Uji ekspresi reguler secara waktu nyata.",
        "json_name": "Penguji Regex",
        "json_desc": "Uji ekspresi reguler secara waktu nyata.",
        "page_desc": "Uji ekspresi reguler secara waktu nyata.",
        "label_pattern": "Pola",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Tidak peka huruf besar/kecil)",
        "label_m": "m (Banyak baris)",
        "label_test": "String Tes",
        "ph_test": "Masukkan string tes",
        "related_header": "Alat Terkait",
        "related_text": "Utilitas Teks",
        "related_diff": "Pemeriksa Perbedaan Teks",
        "related_md": "Pratinjau Markdown",
        "related_lorem": "Generator Lorem Ipsum",
        "res_no_match": "Tidak ada kecocokan ditemukan",
        "res_match": "Cocok",
        "res_highlight": "Sorot",
        "res_error": "Kesalahan"
    },
    "vi": {
        "title": "Kiểm tra Regex",
        "meta_title": "Kiểm tra Regex - Utilify",
        "meta_desc": "Kiểm tra các biểu thức chính quy trong thời gian thực.",
        "og_title": "Kiểm tra Regex - Utilify",
        "og_desc": "Kiểm tra các biểu thức chính quy trong thời gian thực.",
        "json_name": "Kiểm tra Regex",
        "json_desc": "Kiểm tra các biểu thức chính quy trong thời gian thực.",
        "page_desc": "Kiểm tra các biểu thức chính quy trong thời gian thực.",
        "label_pattern": "Mẫu",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Toàn cẩu)",
        "label_i": "i (Không phân biệt hoa thường)",
        "label_m": "m (Nhiều dòng)",
        "label_test": "Chuỗi kiểm tra",
        "ph_test": "Nhập chuỗi kiểm tra",
        "related_header": "Công cụ liên quan",
        "related_text": "Tiện ích văn bản",
        "related_diff": "Kiểm tra sự khác biệt",
        "related_md": "Xem trước Markdown",
        "related_lorem": "Tạo Lorem Ipsum",
        "res_no_match": "Không tìm thấy kết quả",
        "res_match": "Kết quả",
        "res_highlight": "Nổi bật",
        "res_error": "Lỗi"
    },
    "th": {
        "title": "เครื่องมือทดสอบ Regex",
        "meta_title": "เครื่องมือทดสอบ Regex - Utilify",
        "meta_desc": "ทดสอบนิพจน์ทั่วไป (Regular Expressions) แบบเรียลไทม์",
        "og_title": "เครื่องมือทดสอบ Regex - Utilify",
        "og_desc": "ทดสอบนิพจน์ทั่วไป (Regular Expressions) แบบเรียลไทม์",
        "json_name": "เครื่องมือทดสอบ Regex",
        "json_desc": "ทดสอบนิพจน์ทั่วไป (Regular Expressions) แบบเรียลไทม์",
        "page_desc": "ทดสอบนิพจน์ทั่วไป (Regular Expressions) แบบเรียลไทม์",
        "label_pattern": "รูปแบบ (Pattern)",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Case insensitive)",
        "label_m": "m (Multiline)",
        "label_test": "ข้อความทดสอบ",
        "ph_test": "ป้อนข้อความทดสอบ",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_text": "เครื่องมือข้อความ",
        "related_diff": "ตรวจสอบความแตกต่าง",
        "related_md": "แสดงตัวอย่าง Markdown",
        "related_lorem": "สร้าง Lorem Ipsum",
        "res_no_match": "ไม่พบการจับคู่",
        "res_match": "การจับคู่",
        "res_highlight": "ไฮไลท์",
        "res_error": "ข้อผิดพลาด"
    },
    "de": {
        "title": "Regex-Tester",
        "meta_title": "Regex-Tester - Utilify",
        "meta_desc": "Testen Sie reguläre Ausdrücke in Echtzeit.",
        "og_title": "Regex-Tester - Utilify",
        "og_desc": "Testen Sie reguläre Ausdrücke in Echtzeit.",
        "json_name": "Regex-Tester",
        "json_desc": "Testen Sie reguläre Ausdrücke in Echtzeit.",
        "page_desc": "Testen Sie reguläre Ausdrücke in Echtzeit.",
        "label_pattern": "Muster",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Groß-/Kleinschreibung ignorieren)",
        "label_m": "m (Mehrzeilig)",
        "label_test": "Test-String",
        "ph_test": "Test-String eingeben",
        "related_header": "Ähnliche Tools",
        "related_text": "Text-Dienstprogramme",
        "related_diff": "Text-Diff-Checker",
        "related_md": "Markdown-Vorschau",
        "related_lorem": "Lorem Ipsum Generator",
        "res_no_match": "Keine Übereinstimmungen gefunden",
        "res_match": "Übereinstimmungen",
        "res_highlight": "Hervorheben",
        "res_error": "Fehler"
    },
    "pt": {
        "title": "Testador de Regex",
        "meta_title": "Testador de Regex - Utilify",
        "meta_desc": "Teste expressões regulares em tempo real.",
        "og_title": "Testador de Regex - Utilify",
        "og_desc": "Teste expressões regulares em tempo real.",
        "json_name": "Testador de Regex",
        "json_desc": "Teste expressões regulares em tempo real.",
        "page_desc": "Teste expressões regulares em tempo real.",
        "label_pattern": "Padrão",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (Global)",
        "label_i": "i (Ignorar maiúsculas/minúsculas)",
        "label_m": "m (Multilinha)",
        "label_test": "Texto de Teste",
        "ph_test": "Digite o texto de teste",
        "related_header": "Ferramentas Relacionadas",
        "related_text": "Utilitários de Texto",
        "related_diff": "Verificador de Diferenças",
        "related_md": "Visualização de Markdown",
        "related_lorem": "Gerador de Lorem Ipsum",
        "res_no_match": "Nenhuma correspondência encontrada",
        "res_match": "Correspondências",
        "res_highlight": "Destaque",
        "res_error": "Erro"
    },
    "zh-cn": {
        "title": "正则表达式测试",
        "meta_title": "正则表达式测试 - Utilify",
        "meta_desc": "实时测试正则表达式。",
        "og_title": "正则表达式测试 - Utilify",
        "og_desc": "实时测试正则表达式。",
        "json_name": "正则表达式测试",
        "json_desc": "实时测试正则表达式。",
        "page_desc": "实时测试正则表达式。",
        "label_pattern": "模式",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (全局)",
        "label_i": "i (忽略大小写)",
        "label_m": "m (多行)",
        "label_test": "测试字符串",
        "ph_test": "输入测试字符串",
        "related_header": "相关工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差异对比",
        "related_md": "Markdown 预览",
        "related_lorem": "Lorem Ipsum 生成器",
        "res_no_match": "未找到匹配项",
        "res_match": "匹配项",
        "res_highlight": "高亮",
        "res_error": "错误"
    },
    "zh-tw": {
        "title": "正則表達式測試",
        "meta_title": "正則表達式測試 - Utilify",
        "meta_desc": "實時測試正則表達式。",
        "og_title": "正則表達式測試 - Utilify",
        "og_desc": "實時測試正則表達式。",
        "json_name": "正則表達式測試",
        "json_desc": "實時測試正則表達式。",
        "page_desc": "實時測試正則表達式。",
        "label_pattern": "模式",
        "ph_pattern": "/[a-z]+/gi",
        "label_g": "g (全局)",
        "label_i": "i (忽略大小寫)",
        "label_m": "m (多行)",
        "label_test": "測試字符串",
        "ph_test": "輸入測試字符串",
        "related_header": "相關工具",
        "related_text": "文本工具箱",
        "related_diff": "文本差異比對",
        "related_md": "Markdown 預覽",
        "related_lorem": "Lorem Ipsum 生成器",
        "res_no_match": "未找到匹配項",
        "res_match": "匹配項",
        "res_highlight": "高亮",
        "res_error": "錯誤"
    }
}

TEXT_UTILS = {
    "en": {
        "title": "Text Utilities",
        "meta_title": "Text Utilities - Utilify",
        "meta_desc": "Count words, characters, remove duplicates, convert case, and more.",
        "og_title": "Text Utilities - Utilify",
        "og_desc": "Count words, characters, remove duplicates, convert case, and more.",
        "json_name": "Text Utilities",
        "json_desc": "Count words, characters, remove duplicates, convert case, and more.",
        "page_desc": "Count words, characters, remove duplicates, convert case, and more.",
        "label_input": "Input Text",
        "ph_input": "Enter text...",
        "header_stats": "Statistics",
        "label_char": "Characters",
        "label_word": "Words",
        "label_line": "Lines",
        "header_action": "Action",
        "btn_upper": "UPPERCASE",
        "btn_lower": "lowercase",
        "btn_dup": "Remove Duplicate Lines",
        "btn_sort": "Sort Lines",
        "btn_reverse": "Reverse Text",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "related_header": "Related Tools",
        "related_diff": "Diff Checker",
        "related_regex": "Regex Tester",
        "related_md": "Markdown Preview",
        "related_lorem": "Lorem Ipsum"
    },
    "ko": {
        "title": "텍스트 유틸리티",
        "meta_title": "텍스트 유틸리티 - Utilify",
        "meta_desc": "단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.",
        "og_title": "텍스트 유틸리티 - Utilify",
        "og_desc": "단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.",
        "json_name": "텍스트 유틸리티",
        "json_desc": "단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.",
        "page_desc": "단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.",
        "label_input": "텍스트 입력",
        "ph_input": "텍스트를 입력하세요...",
        "header_stats": "통계",
        "label_char": "문자 수",
        "label_word": "단어 수",
        "label_line": "줄 수",
        "header_action": "작업",
        "btn_upper": "대문자로",
        "btn_lower": "소문자로",
        "btn_dup": "중복 줄 제거",
        "btn_sort": "줄 정렬",
        "btn_reverse": "텍스트 뒤집기",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "related_header": "함께 보면 좋은 도구",
        "related_diff": "텍스트 비교기",
        "related_regex": "정규식 테스터",
        "related_md": "마크다운 미리보기",
        "related_lorem": "입숨 생성기"
    },
    "ja": {
        "title": "テキストユーティリティ",
        "meta_title": "テキストユーティリティ - Utilify",
        "meta_desc": "単語数、文字数のカウント、重複削除、大文字小文字変換など。",
        "og_title": "テキストユーティリティ - Utilify",
        "og_desc": "単語数、文字数のカウント、重複削除、大文字小文字変換など。",
        "json_name": "テキストユーティリティ",
        "json_desc": "単語数、文字数のカウント、重複削除、大文字小文字変換など。",
        "page_desc": "単語数、文字数のカウント、重複削除、大文字小文字変換など。",
        "label_input": "テキスト入力",
        "ph_input": "テキストを入力...",
        "header_stats": "統計",
        "label_char": "文字数",
        "label_word": "単語数",
        "label_line": "行数",
        "header_action": "操作",
        "btn_upper": "大文字",
        "btn_lower": "小文字",
        "btn_dup": "重複行削除",
        "btn_sort": "行ソート",
        "btn_reverse": "反転",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "related_header": "関連ツール",
        "related_diff": "テキスト比較",
        "related_regex": "正規表現テスター",
        "related_md": "マークダウンプレビュー",
        "related_lorem": "Lorem Ipsum生成"
    },
    "hi": {
        "title": "टेक्स्ट यूटिलिटीज",
        "meta_title": "टेक्स्ट यूटिलिटीज - Utilify",
        "meta_desc": "शब्द गिनें, अक्षर गिनें, डुप्लिकेट हटाएँ, केस बदलें, और बहुत कुछ।",
        "og_title": "टेक्स्ट यूटिलिटीज - Utilify",
        "og_desc": "शब्द गिनें, अक्षर गिनें, डुप्लिकेट हटाएँ, केस बदलें, और बहुत कुछ।",
        "json_name": "टेक्स्ट यूटिलिटीज",
        "json_desc": "शब्द गिनें, अक्षर गिनें, डुप्लिकेट हटाएँ, केस बदलें, और बहुत कुछ।",
        "page_desc": "शब्द गिनें, अक्षर गिनें, डुप्लिकेट हटाएँ, केस बदलें, और बहुत कुछ।",
        "label_input": "इनपुट टेक्स्ट",
        "ph_input": "टेक्स्ट दर्ज करें...",
        "header_stats": "सांख्यिकी (Statistics)",
        "label_char": "अक्षर (Characters)",
        "label_word": "शब्द (Words)",
        "label_line": "पंक्तियाँ (Lines)",
        "header_action": "कार्रवाई (Action)",
        "btn_upper": "बड़े अक्षरों में (UPPER)",
        "btn_lower": "छोटे अक्षरों में (lower)",
        "btn_dup": "डुप्लिकेट हटाएँ",
        "btn_sort": "सॉर्ट करें",
        "btn_reverse": "उल्टा करें",
        "btn_copy": "कॉपी करें",
        "btn_clear": "साफ़ करें",
        "related_header": "संबंधित उपकरण",
        "related_diff": "टेक्स्ट डिफ चेकर",
        "related_regex": "रेगेक्स टेस्टर",
        "related_md": "मार्कडाउन पूर्वावलोकन",
        "related_lorem": "लोरेम इप्सम"
    },
    "id": {
        "title": "Utilitas Teks",
        "meta_title": "Utilitas Teks - Utilify",
        "meta_desc": "Hitung kata, karakter, hapus duplikat, ubah kapitalisasi, dan banyak lagi.",
        "og_title": "Utilitas Teks - Utilify",
        "og_desc": "Hitung kata, karakter, hapus duplikat, ubah kapitalisasi, dan banyak lagi.",
        "json_name": "Utilitas Teks",
        "json_desc": "Hitung kata, karakter, hapus duplikat, ubah kapitalisasi, dan banyak lagi.",
        "page_desc": "Hitung kata, karakter, hapus duplikat, ubah kapitalisasi, dan banyak lagi.",
        "label_input": "Teks Input",
        "ph_input": "Masukkan teks...",
        "header_stats": "Statistik",
        "label_char": "Karakter",
        "label_word": "Kata",
        "label_line": "Baris",
        "header_action": "Aksi",
        "btn_upper": "HURUF BESAR",
        "btn_lower": "huruf kecil",
        "btn_dup": "Hapus Duplikat",
        "btn_sort": "Urutkan",
        "btn_reverse": "Balikkan",
        "btn_copy": "Salin",
        "btn_clear": "Bersihkan",
        "related_header": "Alat Terkait",
        "related_diff": "Pemeriksa Perbedaan Teks",
        "related_regex": "Penguji Regex",
        "related_md": "Pratinjau Markdown",
        "related_lorem": "Generator Lorem Ipsum"
    },
    "vi": {
        "title": "Tiện ích văn bản",
        "meta_title": "Tiện ích văn bản - Utilify",
        "meta_desc": "Đếm từ, ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.",
        "og_title": "Tiện ích văn bản - Utilify",
        "og_desc": "Đếm từ, ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.",
        "json_name": "Tiện ích văn bản",
        "json_desc": "Đếm từ, ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.",
        "page_desc": "Đếm từ, ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.",
        "label_input": "Văn bản đầu vào",
        "ph_input": "Nhập văn bản...",
        "header_stats": "Thống kê",
        "label_char": "Ký tự",
        "label_word": "Từ",
        "label_line": "Dòng",
        "header_action": "Hành động",
        "btn_upper": "CHỮ HOA",
        "btn_lower": "chữ thường",
        "btn_dup": "Xóa trùng lặp",
        "btn_sort": "Sắp xếp",
        "btn_reverse": "Đảo ngược",
        "btn_copy": "Sao chép",
        "btn_clear": "Xóa",
        "related_header": "Công cụ liên quan",
        "related_diff": "Kiểm tra sự khác biệt",
        "related_regex": "Kiểm tra Regex",
        "related_md": "Xem trước Markdown",
        "related_lorem": "Tạo Lorem Ipsum"
    },
    "th": {
        "title": "เครื่องมือจัดการข้อความ",
        "meta_title": "เครื่องมือจัดการข้อความ - Utilify",
        "meta_desc": "นับคำ ตัวอักษร ลบข้อความที่ซ้ำกัน เปลี่ยนตัวพิมพ์ใหญ่-เล็ก และอื่นๆ",
        "og_title": "เครื่องมือจัดการข้อความ - Utilify",
        "og_desc": "นับคำ ตัวอักษร ลบข้อความที่ซ้ำกัน เปลี่ยนตัวพิมพ์ใหญ่-เล็ก และอื่นๆ",
        "json_name": "เครื่องมือจัดการข้อความ",
        "json_desc": "นับคำ ตัวอักษร ลบข้อความที่ซ้ำกัน เปลี่ยนตัวพิมพ์ใหญ่-เล็ก และอื่นๆ",
        "page_desc": "นับคำ ตัวอักษร ลบข้อความที่ซ้ำกัน เปลี่ยนตัวพิมพ์ใหญ่-เล็ก และอื่นๆ",
        "label_input": "ข้อความอินพุต",
        "ph_input": "ใส่ข้อความ...",
        "header_stats": "สถิติ",
        "label_char": "ตัวอักษร",
        "label_word": "คำ",
        "label_line": "บรรทัด",
        "header_action": "การกระทำ",
        "btn_upper": "ตัวพิมพ์ใหญ่",
        "btn_lower": "ตัวพิมพ์เล็ก",
        "btn_dup": "ลบรายการซ้ำ",
        "btn_sort": "เรียงลำดับ",
        "btn_reverse": "ย้อนกลับ",
        "btn_copy": "คัดลอก",
        "btn_clear": "ล้างค่า",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_diff": "ตรวจสอบความแตกต่าง",
        "related_regex": "ทดสอบ Regex",
        "related_md": "แสดงตัวอย่าง Markdown",
        "related_lorem": "สร้าง Lorem Ipsum"
    },
    "de": {
        "title": "Text-Dienstprogramme",
        "meta_title": "Text-Dienstprogramme - Utilify",
        "meta_desc": "Wörter und Zeichen zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr.",
        "og_title": "Text-Dienstprogramme - Utilify",
        "og_desc": "Wörter und Zeichen zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr.",
        "json_name": "Text-Dienstprogramme",
        "json_desc": "Wörter und Zeichen zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr.",
        "page_desc": "Wörter und Zeichen zählen, Duplikate entfernen, Groß-/Kleinschreibung ändern und mehr.",
        "label_input": "Eingabetext",
        "ph_input": "Text eingeben...",
        "header_stats": "Statistik",
        "label_char": "Zeichen",
        "label_word": "Wörter",
        "label_line": "Zeilen",
        "header_action": "Aktion",
        "btn_upper": "GROSSBUCHSTABEN",
        "btn_lower": "kleinbuchstaben",
        "btn_dup": "Duplikate entfernen",
        "btn_sort": "Sortieren",
        "btn_reverse": "Umkehren",
        "btn_copy": "Kopieren",
        "btn_clear": "Löschen",
        "related_header": "Ähnliche Tools",
        "related_diff": "Text-Diff-Checker",
        "related_regex": "Regex-Tester",
        "related_md": "Markdown-Vorschau",
        "related_lorem": "Lorem Ipsum Generator"
    },
    "pt": {
        "title": "Utilitários de Texto",
        "meta_title": "Utilitários de Texto - Utilify",
        "meta_desc": "Conte palavras, caracteres, remova duplicatas, converta maiúsculas/minúsculas e muito mais.",
        "og_title": "Utilitários de Texto - Utilify",
        "og_desc": "Conte palavras, caracteres, remova duplicatas, converta maiúsculas/minúsculas e muito mais.",
        "json_name": "Utilitários de Texto",
        "json_desc": "Conte palavras, caracteres, remova duplicatas, converta maiúsculas/minúsculas e muito mais.",
        "page_desc": "Conte palavras, caracteres, remova duplicatas, converta maiúsculas/minúsculas e muito mais.",
        "label_input": "Texto de Entrada",
        "ph_input": "Digite o texto...",
        "header_stats": "Estatísticas",
        "label_char": "Caracteres",
        "label_word": "Palavras",
        "label_line": "Linhas",
        "header_action": "Ação",
        "btn_upper": "MAIÚSCULAS",
        "btn_lower": "minúsculas",
        "btn_dup": "Remover Duplicatas",
        "btn_sort": "Ordenar",
        "btn_reverse": "Inverter",
        "btn_copy": "Copiar",
        "btn_clear": "Limpar",
        "related_header": "Ferramentas Relacionadas",
        "related_diff": "Verificador de Diferenças",
        "related_regex": "Testador de Regex",
        "related_md": "Visualização de Markdown",
        "related_lorem": "Gerador de Lorem Ipsum"
    },
    "zh-cn": {
        "title": "文本工具箱",
        "meta_title": "文本工具箱 - Utilify",
        "meta_desc": "统计单词，字符，删除重复项，转换大小写等。",
        "og_title": "文本工具箱 - Utilify",
        "og_desc": "统计单词，字符，删除重复项，转换大小写等。",
        "json_name": "文本工具箱",
        "json_desc": "统计单词，字符，删除重复项，转换大小写等。",
        "page_desc": "统计单词，字符，删除重复项，转换大小写等。",
        "label_input": "输入文本",
        "ph_input": "输入文本...",
        "header_stats": "统计",
        "label_char": "字符数",
        "label_word": "单词数",
        "label_line": "行数",
        "header_action": "操作",
        "btn_upper": "大写",
        "btn_lower": "小写",
        "btn_dup": "删除重复行",
        "btn_sort": "排序行",
        "btn_reverse": "反转文本",
        "btn_copy": "复制",
        "btn_clear": "清除",
        "related_header": "相关工具",
        "related_diff": "文本差异对比",
        "related_regex": "正则表达式测试",
        "related_md": "Markdown 预览",
        "related_lorem": "Lorem Ipsum 生成器"
    },
    "zh-tw": {
        "title": "文本工具箱",
        "meta_title": "文本工具箱 - Utilify",
        "meta_desc": "統計單詞，字符，刪除重複項，轉換大小寫等。",
        "og_title": "文本工具箱 - Utilify",
        "og_desc": "統計單詞，字符，刪除重複項，轉換大小寫等。",
        "json_name": "文本工具箱",
        "json_desc": "統計單詞，字符，刪除重複項，轉換大小寫等。",
        "page_desc": "統計單詞，字符，刪除重複項，轉換大小寫等。",
        "label_input": "輸入文本",
        "ph_input": "輸入文本...",
        "header_stats": "統計",
        "label_char": "字符數",
        "label_word": "單詞數",
        "label_line": "行數",
        "header_action": "操作",
        "btn_upper": "大寫",
        "btn_lower": "小寫",
        "btn_dup": "刪除重複行",
        "btn_sort": "排序行",
        "btn_reverse": "反轉文本",
        "btn_copy": "複製",
        "btn_clear": "清除",
        "related_header": "相關工具",
        "related_diff": "文本差異比對",
        "related_regex": "正則表達式測試",
        "related_md": "Markdown 預覽",
        "related_lorem": "Lorem Ipsum 生成器"
    }
}

BMI_CALCULATOR = {
    "en": {
        "title": "BMI Calculator",
        "meta_title": "BMI Calculator - Utilify",
        "meta_desc": "Calculate your Body Mass Index (BMI).",
        "og_title": "BMI Calculator - Utilify",
        "og_desc": "Calculate your Body Mass Index (BMI).",
        "json_name": "BMI Calculator",
        "json_desc": "Calculate your Body Mass Index (BMI).",
        "page_desc": "Calculate your Body Mass Index (BMI).",
        "label_height": "Height (cm)",
        "label_weight": "Weight (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "Calculate",
        "res_prefix": "BMI: ",
        "cat_under": "Underweight",
        "cat_normal": "Normal",
        "cat_over": "Overweight",
        "cat_obese": "Obese",
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_date": "Date Calculator",
        "related_timer": "Timer",
        "related_reaction": "Reaction Test"
    },
    "ko": {
        "title": "BMI 계산기",
        "meta_title": "BMI 계산기 - Utilify",
        "meta_desc": "BMI를 계산하세요.",
        "og_title": "BMI 계산기 - Utilify",
        "og_desc": "BMI를 계산하세요.",
        "json_name": "BMI 계산기",
        "json_desc": "BMI를 계산하세요.",
        "page_desc": "BMI를 계산하세요.",
        "label_height": "키 (cm)",
        "label_weight": "체중 (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "계산",
        "res_prefix": "BMI: ",
        "cat_under": "저체중",
        "cat_normal": "정상",
        "cat_over": "과체중",
        "cat_obese": "비만",
        "related_header": "함께 보면 좋은 도구",
        "related_unit": "단위 변환기",
        "related_date": "날짜 계산기",
        "related_timer": "타이머",
        "related_reaction": "반응 속도"
    },
    "ja": {
        "title": "BMI計算機",
        "meta_title": "BMI計算機 - Utilify",
        "meta_desc": "BMI（ボディマス指数）を計算します。",
        "og_title": "BMI計算機 - Utilify",
        "og_desc": "BMI（ボディマス指数）を計算します。",
        "json_name": "BMI計算機",
        "json_desc": "BMI（ボディマス指数）を計算します。",
        "page_desc": "BMI（ボディマス指数）を計算します。",
        "label_height": "身長 (cm)",
        "label_weight": "体重 (kg)",
        "ph_height": "170",
        "ph_weight": "60",
        "btn_calculate": "計算する",
        "res_prefix": "BMI: ",
        "cat_under": "低体重",
        "cat_normal": "普通体重",
        "cat_over": "過体重",
        "cat_obese": "肥満",
        "related_header": "関連ツール",
        "related_unit": "単位変換",
        "related_date": "日付計算",
        "related_timer": "タイマー",
        "related_reaction": "反応速度テスト"
    },
    "hi": {
        "title": "BMI कैलकुलेटर",
        "meta_title": "BMI कैलकुलेटर - Utilify",
        "meta_desc": "अपना बॉडी मास इंडेक्स (BMI) की गणना करें।",
        "og_title": "BMI कैलकुलेटर - Utilify",
        "og_desc": "अपना बॉडी मास इंडेक्स (BMI) की गणना करें।",
        "json_name": "BMI कैलकुलेटर",
        "json_desc": "अपना बॉडी मास इंडेक्स (BMI) की गणना करें।",
        "page_desc": "अपना बॉडी मास इंडेक्स (BMI) की गणना करें।",
        "label_height": "ऊंचाई (cm)",
        "label_weight": "वजन (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "गणना करें",
        "res_prefix": "BMI: ",
        "cat_under": "कम वजन",
        "cat_normal": "साधारण",
        "cat_over": "अधिक वजन",
        "cat_obese": "मोटापा",
        "related_header": "संबंधित उपकरण",
        "related_unit": "इकाई परिवर्तक",
        "related_date": "दिनांक कैलकुलेटर",
        "related_timer": "टाइमर",
        "related_reaction": "प्रतिक्रिया परीक्षण"
    },
    "id": {
        "title": "Kalkulator BMI",
        "meta_title": "Kalkulator BMI - Utilify",
        "meta_desc": "Hitung Indeks Massa Tubuh (BMI) Anda.",
        "og_title": "Kalkulator BMI - Utilify",
        "og_desc": "Hitung Indeks Massa Tubuh (BMI) Anda.",
        "json_name": "Kalkulator BMI",
        "json_desc": "Hitung Indeks Massa Tubuh (BMI) Anda.",
        "page_desc": "Hitung Indeks Massa Tubuh (BMI) Anda.",
        "label_height": "Tinggi (cm)",
        "label_weight": "Berat (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "Hitung",
        "res_prefix": "BMI: ",
        "cat_under": "Berat badan kurang",
        "cat_normal": "Normal",
        "cat_over": "Kelebihan berat badan",
        "cat_obese": "Obesitas",
        "related_header": "Alat Terkait",
        "related_unit": "Konverter Unit",
        "related_date": "Kalkulator Tanggal",
        "related_timer": "Timer",
        "related_reaction": "Tes Reaksi"
    },
    "vi": {
        "title": "Máy tính BMI",
        "meta_title": "Máy tính BMI - Utilify",
        "meta_desc": "Tính Chỉ số Khối cơ thể (BMI) của bạn.",
        "og_title": "Máy tính BMI - Utilify",
        "og_desc": "Tính Chỉ số Khối cơ thể (BMI) của bạn.",
        "json_name": "Máy tính BMI",
        "json_desc": "Tính Chỉ số Khối cơ thể (BMI) của bạn.",
        "page_desc": "Tính Chỉ số Khối cơ thể (BMI) của bạn.",
        "label_height": "Chiều cao (cm)",
        "label_weight": "Cân nặng (kg)",
        "ph_height": "170",
        "ph_weight": "60",
        "btn_calculate": "Tính toán",
        "res_prefix": "BMI: ",
        "cat_under": "Thiếu cân",
        "cat_normal": "Bình thường",
        "cat_over": "Thừa cân",
        "cat_obese": "Béo phì",
        "related_header": "Công cụ liên quan",
        "related_unit": "Chuyển đổi đơn vị",
        "related_date": "Máy tính ngày",
        "related_timer": "Hẹn giờ",
        "related_reaction": "Kiểm tra phản xạ"
    },
    "th": {
        "title": "เครื่องคำนวณ BMI",
        "meta_title": "เครื่องคำนวณ BMI - Utilify",
        "meta_desc": "คำนวณดัชนีมวลกาย (BMI) ของคุณ",
        "og_title": "เครื่องคำนวณ BMI - Utilify",
        "og_desc": "คำนวณดัชนีมวลกาย (BMI) ของคุณ",
        "json_name": "เครื่องคำนวณ BMI",
        "json_desc": "คำนวณดัชนีมวลกาย (BMI) ของคุณ",
        "page_desc": "คำนวณดัชนีมวลกาย (BMI) ของคุณ",
        "label_height": "ส่วนสูง (cm)",
        "label_weight": "น้ำหนัก (kg)",
        "ph_height": "170",
        "ph_weight": "60",
        "btn_calculate": "คำนวณ",
        "res_prefix": "BMI: ",
        "cat_under": "น้ำหนักน้อยเกินไป",
        "cat_normal": "ปกติ",
        "cat_over": "น้ำหนักเกิน",
        "cat_obese": "อ้วน",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_unit": "แปลงหน่วย",
        "related_date": "เครื่องคำนวณวันที่",
        "related_timer": "ตัวจับเวลา",
        "related_reaction": "ทดสอบปฏิกิริยา"
    },
    "de": {
        "title": "BMI Rechner",
        "meta_title": "BMI Rechner - Utilify",
        "meta_desc": "Berechnen Sie Ihren Body Mass Index (BMI).",
        "og_title": "BMI Rechner - Utilify",
        "og_desc": "Berechnen Sie Ihren Body Mass Index (BMI).",
        "json_name": "BMI Rechner",
        "json_desc": "Berechnen Sie Ihren Body Mass Index (BMI).",
        "page_desc": "Berechnen Sie Ihren Body Mass Index (BMI).",
        "label_height": "Größe (cm)",
        "label_weight": "Gewicht (kg)",
        "ph_height": "175",
        "ph_weight": "75",
        "btn_calculate": "Berechnen",
        "res_prefix": "BMI: ",
        "cat_under": "Untergewicht",
        "cat_normal": "Normalgewicht",
        "cat_over": "Übergewicht",
        "cat_obese": "Adipositas",
        "related_header": "Ähnliche Tools",
        "related_unit": "Einheitenumrechner",
        "related_date": "Datumsrechner",
        "related_timer": "Timer",
        "related_reaction": "Reaktionstest"
    },
    "pt": {
        "title": "Calculadora de IMC",
        "meta_title": "Calculadora de IMC - Utilify",
        "meta_desc": "Calcule seu Índice de Massa Corporal (IMC).",
        "og_title": "Calculadora de IMC - Utilify",
        "og_desc": "Calcule seu Índice de Massa Corporal (IMC).",
        "json_name": "Calculadora de IMC",
        "json_desc": "Calcule seu Índice de Massa Corporal (IMC).",
        "page_desc": "Calcule seu Índice de Massa Corporal (IMC).",
        "label_height": "Altura (cm)",
        "label_weight": "Peso (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "Calcular",
        "res_prefix": "IMC: ",
        "cat_under": "Abaixo do peso",
        "cat_normal": "Normal",
        "cat_over": "Sobrepeso",
        "cat_obese": "Obesidade",
        "related_header": "Ferramentas Relacionadas",
        "related_unit": "Conversor de Unidades",
        "related_date": "Calculadora de Data",
        "related_timer": "Cronômetro",
        "related_reaction": "Teste de Reação"
    },
    "zh-cn": {
        "title": "BMI 计算器",
        "meta_title": "BMI 计算器 - Utilify",
        "meta_desc": "计算身体质量指数 (BMI)。",
        "og_title": "BMI 计算器 - Utilify",
        "og_desc": "计算身体质量指数 (BMI)。",
        "json_name": "BMI 计算器",
        "json_desc": "计算身体质量指数 (BMI)。",
        "page_desc": "计算身体质量指数 (BMI)。",
        "label_height": "身高 (cm)",
        "label_weight": "体重 (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "计算",
        "res_prefix": "BMI: ",
        "cat_under": "体重过轻",
        "cat_normal": "正常",
        "cat_over": "超重",
        "cat_obese": "肥胖",
        "related_header": "相关工具",
        "related_unit": "单位转换器",
        "related_date": "日期计算器",
        "related_timer": "计时器",
        "related_reaction": "反应测试"
    },
    "zh-tw": {
        "title": "BMI 計算器",
        "meta_title": "BMI 計算器 - Utilify",
        "meta_desc": "計算身體質量指數 (BMI)。",
        "og_title": "BMI 計算器 - Utilify",
        "og_desc": "計算身體質量指數 (BMI)。",
        "json_name": "BMI 計算器",
        "json_desc": "計算身體質量指數 (BMI)。",
        "page_desc": "計算身體質量指數 (BMI)。",
        "label_height": "身高 (cm)",
        "label_weight": "體重 (kg)",
        "ph_height": "170",
        "ph_weight": "70",
        "btn_calculate": "計算",
        "res_prefix": "BMI: ",
        "cat_under": "體重過輕",
        "cat_normal": "正常",
        "cat_over": "超重",
        "cat_obese": "肥胖",
        "related_header": "相關工具",
        "related_unit": "單位轉換器",
        "related_date": "日期計算器",
        "related_timer": "計時器",
        "related_reaction": "反應測試"
    }
}

DATE_CALCULATOR = {
    "en": {
        "title": "Date Calculator",
        "meta_title": "Date Calculator - Utilify",
        "meta_desc": "Calculate D-Day and date differences.",
        "og_title": "Date Calculator - Utilify",
        "og_desc": "Calculate D-Day and date differences.",
        "json_name": "Date Calculator",
        "json_desc": "Calculate D-Day and date differences.",
        "page_desc": "Calculate D-Day and date differences.",
        "header_dday": "D-Day Calculation",
        "label_target": "Target Date",
        "btn_calculate": "Calculate",
        "header_diff": "Date Difference",
        "label_start": "Start Date",
        "label_end": "End Date",
        "res_suffix": " Days",
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_bmi": "Calculadora de IMC",
        "related_date": "Calculadora de Data",
        "related_timer": "Cronômetro",
        "related_reaction": "Teste de Reação"
    },
    "ko": {
        "title": "날짜 계산기",
        "meta_title": "날짜 계산기 - Utilify",
        "meta_desc": "D-Day 및 날짜 차이를 계산하세요.",
        "og_title": "날짜 계산기 - Utilify",
        "og_desc": "D-Day 및 날짜 차이를 계산하세요.",
        "json_name": "날짜 계산기",
        "json_desc": "D-Day 및 날짜 차이를 계산하세요.",
        "page_desc": "D-Day 및 날짜 차이를 계산하세요.",
        "header_dday": "D-Day 계산",
        "label_target": "목표 날짜",
        "btn_calculate": "계산하기",
        "header_diff": "날짜 차이",
        "label_start": "시작 날짜",
        "label_end": "종료 날짜",
        "res_suffix": " 일",
        "related_header": "함께 보면 좋은 도구",
        "related_unit": "단위 변환기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_timer": "타이머",
        "related_reaction": "반응 속도 테스트"
    },
    "ja": {
        "title": "日付計算",
        "meta_title": "日付計算 - Utilify",
        "meta_desc": "D-Dayと日付の差を計算します。",
        "og_title": "日付計算 - Utilify",
        "og_desc": "D-Dayと日付の差を計算します。",
        "json_name": "日付計算",
        "json_desc": "D-Dayと日付の差を計算します。",
        "page_desc": "D-Dayと日付の差を計算します。",
        "header_dday": "D-Day計算",
        "label_target": "目標日",
        "btn_calculate": "計算する",
        "header_diff": "日付の差",
        "label_start": "開始日",
        "label_end": "終了日",
        "res_suffix": " 日",
        "related_header": "関連ツール",
        "related_unit": "単位変換",
        "related_bmi": "BMI計算機",
        "related_timer": "タイマー",
        "related_reaction": "反応速度テスト"
    },
    "hi": {
        "title": "दिनांक कैलकुलेटर",
        "meta_title": "दिनांक कैलकुलेटर - Utilify",
        "meta_desc": "डी-डे और दिनांक अंतर की गणना करें।",
        "og_title": "दिनांक कैलकुलेटर - Utilify",
        "og_desc": "डी-डे और दिनांक अंतर की गणना करें।",
        "json_name": "दिनांक कैलकुलेटर",
        "json_desc": "डी-डे और दिनांक अंतर की गणना करें।",
        "page_desc": "डी-डे और दिनांक अंतर की गणना करें।",
        "header_dday": "डी-डे गणना",
        "label_target": "लक्ष्य तिथि",
        "btn_calculate": "गणना करें",
        "header_diff": "तारीख का अंतर",
        "label_start": "आरंभ करने की तिथि",
        "label_end": "अंतिम तिथि",
        "res_suffix": " दिन",
        "related_header": "संबंधित उपकरण",
        "related_unit": "इकाई परिवर्तक",
        "related_bmi": "BMI कैलकुलेटर",
        "related_timer": "टाइमर",
        "related_reaction": "प्रतिक्रिया परीक्षण"
    },
    "id": {
        "title": "Kalkulator Tanggal",
        "meta_title": "Kalkulator Tanggal - Utilify",
        "meta_desc": "Hitung D-Day dan selisih tanggal.",
        "og_title": "Kalkulator Tanggal - Utilify",
        "og_desc": "Hitung D-Day dan selisih tanggal.",
        "json_name": "Kalkulator Tanggal",
        "json_desc": "Hitung D-Day dan selisih tanggal.",
        "page_desc": "Hitung D-Day dan selisih tanggal.",
        "header_dday": "Perhitungan D-Day",
        "label_target": "Tanggal Target",
        "btn_calculate": "Hitung",
        "header_diff": "Selisih Tanggal",
        "label_start": "Tanggal Mulai",
        "label_end": "Tanggal Akhir",
        "res_suffix": " Hari",
        "related_header": "Alat Terkait",
        "related_unit": "Konverter Unit",
        "related_bmi": "Kalkulator BMI",
        "related_timer": "Timer",
        "related_reaction": "Tes Reaksi"
    },
    "vi": {
        "title": "Máy tính ngày",
        "meta_title": "Máy tính ngày - Utilify",
        "meta_desc": "Tính ngày D-Day và chênh lệch ngày.",
        "og_title": "Máy tính ngày - Utilify",
        "og_desc": "Tính ngày D-Day và chênh lệch ngày.",
        "json_name": "Máy tính ngày",
        "json_desc": "Tính ngày D-Day và chênh lệch ngày.",
        "page_desc": "Tính ngày D-Day và chênh lệch ngày.",
        "header_dday": "Tính ngày D-Day",
        "label_target": "Ngày mục tiêu",
        "btn_calculate": "Tính toán",
        "header_diff": "Chênh lệch ngày",
        "label_start": "Ngày bắt đầu",
        "label_end": "Ngày kết thúc",
        "res_suffix": " Ngày",
        "related_header": "Công cụ liên quan",
        "related_unit": "Chuyển đổi đơn vị",
        "related_bmi": "Máy tính BMI",
        "related_timer": "Hẹn giờ",
        "related_reaction": "Kiểm tra phản xạ"
    },
    "th": {
        "title": "เครื่องคำนวณวันที่",
        "meta_title": "เครื่องคำนวณวันที่ - Utilify",
        "meta_desc": "คำนวณ D-Day และความแตกต่างของวันที่",
        "og_title": "เครื่องคำนวณวันที่ - Utilify",
        "og_desc": "คำนวณ D-Day และความแตกต่างของวันที่",
        "json_name": "เครื่องคำนวณวันที่",
        "json_desc": "คำนวณ D-Day และความแตกต่างของวันที่",
        "page_desc": "คำนวณ D-Day และความแตกต่างของวันที่",
        "header_dday": "การคำนวณ D-Day",
        "label_target": "วันที่เป้าหมาย",
        "btn_calculate": "คำนวณ",
        "header_diff": "ความแตกต่างของวันที่",
        "label_start": "วันที่เริ่มต้น",
        "label_end": "วันที่สิ้นสุด",
        "res_suffix": " วัน",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_unit": "แปลงหน่วย",
        "related_bmi": "เครื่องคำนวณ BMI",
        "related_timer": "ตัวจับเวลา",
        "related_reaction": "ทดสอบปฏิกิริยา"
    },
    "de": {
        "title": "Datumsrechner",
        "meta_title": "Datumsrechner - Utilify",
        "meta_desc": "Berechnen Sie D-Day und Datumsdifferenzen.",
        "og_title": "Datumsrechner - Utilify",
        "og_desc": "Berechnen Sie D-Day und Datumsdifferenzen.",
        "json_name": "Datumsrechner",
        "json_desc": "Berechnen Sie D-Day und Datumsdifferenzen.",
        "page_desc": "Berechnen Sie D-Day und Datumsdifferenzen.",
        "header_dday": "D-Day Berechnung",
        "label_target": "Zieldatum",
        "btn_calculate": "Berechnen",
        "header_diff": "Datumsdifferenz",
        "label_start": "Startdatum",
        "label_end": "Enddatum",
        "res_suffix": " Tage",
        "related_header": "Ähnliche Tools",
        "related_unit": "Einheitenumrechner",
        "related_bmi": "BMI Rechner",
        "related_timer": "Timer",
        "related_reaction": "Reaktionstest"
    },
    "pt": {
        "title": "Calculadora de Data",
        "meta_title": "Calculadora de Data - Utilify",
        "meta_desc": "Calcule D-Day e diferenças de datas.",
        "og_title": "Calculadora de Data - Utilify",
        "og_desc": "Calcule D-Day e diferenças de datas.",
        "json_name": "Calculadora de Data",
        "json_desc": "Calcule D-Day e diferenças de datas.",
        "page_desc": "Calcule D-Day e diferenças de datas.",
        "header_dday": "Cálculo de D-Day",
        "label_target": "Data Alvo",
        "btn_calculate": "Calcular",
        "header_diff": "Diferença de Data",
        "label_start": "Data de Início",
        "label_end": "Data Final",
        "res_suffix": " Dias",
        "related_header": "Ferramentas Relacionadas",
        "related_unit": "Conversor de Unidades",
        "related_bmi": "Calculadora de IMC",
        "related_timer": "Cronômetro",
        "related_reaction": "Teste de Reação"
    },
    "zh-cn": {
        "title": "日期计算器",
        "meta_title": "日期计算器 - Utilify",
        "meta_desc": "计算 D-Day 和日期差异。",
        "og_title": "日期计算器 - Utilify",
        "og_desc": "计算 D-Day 和日期差异。",
        "json_name": "日期计算器",
        "json_desc": "计算 D-Day 和日期差异。",
        "page_desc": "计算 D-Day 和日期差异。",
        "header_dday": "D-Day 计算",
        "label_target": "目标日期",
        "btn_calculate": "计算",
        "header_diff": "日期差异",
        "label_start": "开始日期",
        "label_end": "结束日期",
        "res_suffix": " 天",
        "related_header": "相关工具",
        "related_unit": "单位转换器",
        "related_bmi": "BMI 计算器",
        "related_timer": "计时器",
        "related_reaction": "反应测试"
    },
    "zh-tw": {
        "title": "日期計算器",
        "meta_title": "日期計算器 - Utilify",
        "meta_desc": "計算 D-Day 和日期差異。",
        "og_title": "日期計算器 - Utilify",
        "og_desc": "計算 D-Day 和日期差異。",
        "json_name": "日期計算器",
        "json_desc": "計算 D-Day 和日期差異。",
        "page_desc": "計算 D-Day 和日期差異。",
        "header_dday": "D-Day 計算",
        "label_target": "目標日期",
        "btn_calculate": "計算",
        "header_diff": "日期差異",
        "label_start": "開始日期",
        "label_end": "結束日期",
        "res_suffix": " 天",
        "related_header": "相關工具",
        "related_unit": "單位轉換器",
        "related_bmi": "BMI 計算器",
        "related_timer": "計時器",
        "related_reaction": "反應測試"
    }
}

TIMER = {
    "en": {
        "title": "Timer / Pomodoro",
        "meta_title": "Timer / Pomodoro - Utilify",
        "meta_desc": "Online Timer and Pomodoro technique.",
        "og_title": "Timer / Pomodoro - Utilify",
        "og_desc": "Online Timer and Pomodoro technique.",
        "json_name": "Timer",
        "json_desc": "Online Timer and Pomodoro technique.",
        "page_desc": "Online Timer and Pomodoro technique.",
        "label_minutes": "Minutes",
        "btn_start": "Start",
        "btn_pause": "Pause",
        "btn_reset": "Reset",
        "pre_25": "Pomodoro (25m)",
        "pre_5": "Break (5m)",
        "pre_15": "Break (15m)",
        "alert_end": "Time is up!",
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_reaction": "Reaction Test"
    },
    "ko": {
        "title": "타이머",
        "meta_title": "타이머 - Utilify",
        "meta_desc": "온라인 타이머와 포모도로 기법",
        "og_title": "타이머 - Utilify",
        "og_desc": "온라인 타이머와 포모도로 기법",
        "json_name": "타이머",
        "json_desc": "온라인 타이머와 포모도로 기법",
        "page_desc": "온라인 타이머와 포모도로 기법",
        "label_minutes": "분",
        "btn_start": "시작",
        "btn_pause": "일시정지",
        "btn_reset": "리셋",
        "pre_25": "Pomodoro (25m)",
        "pre_5": "휴식 (5m)",
        "pre_15": "휴식 (15m)",
        "alert_end": "시간 종료!",
        "related_header": "함께 보면 좋은 도구",
        "related_unit": "단위 변환기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_reaction": "반응 속도"
    },
    "ja": {
        "title": "タイマー / ポモドーロ",
        "meta_title": "タイマー / ポモドーロ - Utilify",
        "meta_desc": "オンラインタイマーとポモドーロテクニック。",
        "og_title": "タイマー / ポモドーロ - Utilify",
        "og_desc": "オンラインタイマーとポモドーロテクニック。",
        "json_name": "タイマー",
        "json_desc": "オンラインタイマーとポモドーロテクニック。",
        "page_desc": "オンラインタイマーとポモドーロテクニック。",
        "label_minutes": "分",
        "btn_start": "スタート",
        "btn_pause": "一時停止",
        "btn_reset": "リセット",
        "pre_25": "ポモドーロ (25分)",
        "pre_5": "休憩 (5分)",
        "pre_15": "休憩 (15分)",
        "alert_end": "時間です！",
        "related_header": "関連ツール",
        "related_unit": "単位変換",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算",
        "related_reaction": "反応速度テスト"
    },
    "hi": {
        "title": "टाइमर / पोमोडोरो",
        "meta_title": "टाइमर / पोमोडोरो - Utilify",
        "meta_desc": "ऑनलाइन टाइमर और पोमोडोरो तकनीक।",
        "og_title": "टाइमर / पोमोडोरो - Utilify",
        "og_desc": "ऑनलाइन टाइमर और पोमोडोरो तकनीक।",
        "json_name": "टाइमर",
        "json_desc": "ऑनलाइन टाइमर और पोमोडोरो तकनीक।",
        "page_desc": "ऑनलाइन टाइमर और पोमोडोरो तकनीक।",
        "label_minutes": "मिनट",
        "btn_start": "शुरू करें",
        "btn_pause": "विराम",
        "btn_reset": "रीसेट",
        "pre_25": "पोमोडोरो (25 मिनट)",
        "pre_5": "ब्रेक (5 मिनट)",
        "pre_15": "ब्रेक (15 मिनट)",
        "alert_end": "समय समाप्त!",
        "related_header": "संबंधित उपकरण",
        "related_unit": "इकाई परिवर्तक",
        "related_bmi": "BMI कैलकुलेटर",
        "related_date": "दिनांक कैलकुलेटर",
        "related_reaction": "प्रतिक्रिया परीक्षण"
    },
    "id": {
        "title": "Timer / Pomodoro",
        "meta_title": "Timer / Pomodoro - Utilify",
        "meta_desc": "Timer online dan teknik Pomodoro.",
        "og_title": "Timer / Pomodoro - Utilify",
        "og_desc": "Timer online dan teknik Pomodoro.",
        "json_name": "Timer",
        "json_desc": "Timer online dan teknik Pomodoro.",
        "page_desc": "Timer online dan teknik Pomodoro.",
        "label_minutes": "Menit",
        "btn_start": "Mulai",
        "btn_pause": "Jeda",
        "btn_reset": "Reset",
        "pre_25": "Pomodoro (25m)",
        "pre_5": "Istirahat (5m)",
        "pre_15": "Istirahat (15m)",
        "alert_end": "Waktu habis!",
        "related_header": "Alat Terkait",
        "related_unit": "Konverter Unit",
        "related_bmi": "Kalkulator BMI",
        "related_date": "Kalkulator Tanggal",
        "related_reaction": "Tes Reaksi"
    },
    "vi": {
        "title": "Bộ hẹn giờ / Pomodoro",
        "meta_title": "Bộ hẹn giờ / Pomodoro - Utilify",
        "meta_desc": "Hẹn giờ trực tuyến và kỹ thuật Pomodoro.",
        "og_title": "Bộ hẹn giờ / Pomodoro - Utilify",
        "og_desc": "Hẹn giờ trực tuyến và kỹ thuật Pomodoro.",
        "json_name": "Bộ hẹn giờ",
        "json_desc": "Hẹn giờ trực tuyến và kỹ thuật Pomodoro.",
        "page_desc": "Hẹn giờ trực tuyến và kỹ thuật Pomodoro.",
        "label_minutes": "Phút",
        "btn_start": "Bắt đầu",
        "btn_pause": "Tạm dừng",
        "btn_reset": "Đặt lại",
        "pre_25": "Pomodoro (25 phút)",
        "pre_5": "Nghỉ ngơi (5 phút)",
        "pre_15": "Nghỉ ngơi (15 phút)",
        "alert_end": "Hết giờ!",
        "related_header": "Công cụ liên quan",
        "related_unit": "Chuyển đổi đơn vị",
        "related_bmi": "Máy tính BMI",
        "related_date": "Máy tính ngày",
        "related_reaction": "Kiểm tra phản xạ"
    },
    "th": {
        "title": "ตัวจับเวลา / Pomodoro",
        "meta_title": "ตัวจับเวลา / Pomodoro - Utilify",
        "meta_desc": "ตัวจับเวลาออนไลน์และเทคนิค Pomodoro",
        "og_title": "ตัวจับเวลา / Pomodoro - Utilify",
        "og_desc": "ตัวจับเวลาออนไลน์และเทคนิค Pomodoro",
        "json_name": "ตัวจับเวลา",
        "json_desc": "ตัวจับเวลาออนไลน์และเทคนิค Pomodoro",
        "page_desc": "ตัวจับเวลาออนไลน์และเทคนิค Pomodoro",
        "label_minutes": "นาที",
        "btn_start": "เริ่ม",
        "btn_pause": "หยุดชั่วคราว",
        "btn_reset": "รีเซ็ต",
        "pre_25": "Pomodoro (25 นาที)",
        "pre_5": "พักเบรค (5 นาที)",
        "pre_15": "พักเบรค (15 นาที)",
        "alert_end": "หมดเวลา!",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_unit": "แปลงหน่วย",
        "related_bmi": "เครื่องคำนวณ BMI",
        "related_date": "เครื่องคำนวณวันที่",
        "related_reaction": "ทดสอบปฏิกิริยา"
    },
    "de": {
        "title": "Timer / Pomodoro",
        "meta_title": "Timer / Pomodoro - Utilify",
        "meta_desc": "Online-Timer und Pomodoro-Technik.",
        "og_title": "Timer / Pomodoro - Utilify",
        "og_desc": "Online-Timer und Pomodoro-Technik.",
        "json_name": "Timer",
        "json_desc": "Online-Timer und Pomodoro-Technik.",
        "page_desc": "Online-Timer und Pomodoro-Technik.",
        "label_minutes": "Minuten",
        "btn_start": "Start",
        "btn_pause": "Pause",
        "btn_reset": "Zurücksetzen",
        "pre_25": "Pomodoro (25 Min)",
        "pre_5": "Pause (5 Min)",
        "pre_15": "Pause (15 Min)",
        "alert_end": "Zeit ist um!",
        "related_header": "Ähnliche Tools",
        "related_unit": "Einheitenumrechner",
        "related_bmi": "BMI Rechner",
        "related_date": "Datumsrechner",
        "related_reaction": "Reaktionstest"
    },
    "pt": {
        "title": "Cronômetro / Pomodoro",
        "meta_title": "Cronômetro / Pomodoro - Utilify",
        "meta_desc": "Cronômetro online e técnica Pomodoro.",
        "og_title": "Cronômetro / Pomodoro - Utilify",
        "og_desc": "Cronômetro online e técnica Pomodoro.",
        "json_name": "Cronômetro",
        "json_desc": "Cronômetro online e técnica Pomodoro.",
        "page_desc": "Cronômetro online e técnica Pomodoro.",
        "label_minutes": "Minutos",
        "btn_start": "Começar",
        "btn_pause": "Pausar",
        "btn_reset": "Resetar",
        "pre_25": "Pomodoro (25m)",
        "pre_5": "Pausa (5m)",
        "pre_15": "Pausa (15m)",
        "alert_end": "O tempo acabou!",
        "related_header": "Ferramentas Relacionadas",
        "related_unit": "Conversor de Unidades",
        "related_bmi": "Calculadora de IMC",
        "related_date": "Calculadora de Data",
        "related_reaction": "Teste de Reação"
    },
    "zh-cn": {
        "title": "计时器 / 番茄钟",
        "meta_title": "计时器 / 番茄钟 - Utilify",
        "meta_desc": "在线计时器和番茄工作法。",
        "og_title": "计时器 / 番茄钟 - Utilify",
        "og_desc": "在线计时器和番茄工作法。",
        "json_name": "计时器",
        "json_desc": "在线计时器和番茄工作法。",
        "page_desc": "在线计时器和番茄工作法。",
        "label_minutes": "分钟",
        "btn_start": "开始",
        "btn_pause": "暂停",
        "btn_reset": "重置",
        "pre_25": "番茄钟 (25分)",
        "pre_5": "休息 (5分)",
        "pre_15": "休息 (15分)",
        "alert_end": "时间到！",
        "related_header": "相关工具",
        "related_unit": "单位转换器",
        "related_bmi": "BMI 计算器",
        "related_date": "日期计算器",
        "related_reaction": "反应测试"
    },
    "zh-tw": {
        "title": "計時器 / 番茄鐘",
        "meta_title": "計時器 / 番茄鐘 - Utilify",
        "meta_desc": "線上計時器和番茄工作法。",
        "og_title": "計時器 / 番茄鐘 - Utilify",
        "og_desc": "線上計時器和番茄工作法。",
        "json_name": "計時器",
        "json_desc": "線上計時器和番茄工作法。",
        "page_desc": "線上計時器和番茄工作法。",
        "label_minutes": "分鐘",
        "btn_start": "開始",
        "btn_pause": "暫停",
        "btn_reset": "重置",
        "pre_25": "番茄鐘 (25分)",
        "pre_5": "休息 (5分)",
        "pre_15": "休息 (15分)",
        "alert_end": "時間到！",
        "related_header": "相關工具",
        "related_unit": "單位轉換器",
        "related_bmi": "BMI 計算器",
        "related_date": "日期計算器",
        "related_reaction": "反應測試"
    }
}

THUMBNAIL_DOWNLOADER = {
    "en": {
        "title": "YouTube Thumbnail Downloader",
        "meta_title": "YouTube Thumbnail Downloader - Utilify",
        "meta_desc": "Extract and download YouTube video thumbnails in high quality (4K, HD). Free and easy tool.",
        "og_title": "YouTube Thumbnail Downloader - Utilify",
        "og_desc": "Extract and download YouTube video thumbnails in high quality (4K, HD). Free and easy tool.",
        "json_name": "YouTube Thumbnail Downloader",
        "json_desc": "Extract and download YouTube video thumbnails in high quality (4K, HD). Free and easy tool.",
        "page_desc": "Extract and download YouTube video thumbnails in high quality (4K, HD). Free and easy tool.",
        "btn_get": "Get Thumbnail",
        "label_max": "Maximum Resolution (1280x720+)",
        "label_high": "High Quality (480x360)",
        "label_med": "Medium Quality (320x180)",
        "btn_dl": "Download Image",
        "toast_invalid": "Invalid YouTube URL.",
        "adsense_text": "Advertisement",
        "related_header": "Related Tools",
        "related_img": "Image Converter",
        "related_favicon": "Favicon Generator",
        "related_color": "Color Converter",
        "related_watermark": "Image Watermark"
    },
    "ko": {
        "title": "유튜브 썸네일 다운로더",
        "meta_title": "유튜브 썸네일 다운로더 - Utilify",
        "meta_desc": "유튜브 영상의 썸네일 이미지를 고화질(4K, HD)로 추출하고 다운로드하세요. 무료, 간편한 도구.",
        "og_title": "유튜브 썸네일 다운로더 - Utilify",
        "og_desc": "유튜브 영상의 썸네일 이미지를 고화질(4K, HD)로 추출하고 다운로드하세요. 무료, 간편한 도구.",
        "json_name": "유튜브 썸네일 다운로더",
        "json_desc": "유튜브 영상의 썸네일 이미지를 고화질(4K, HD)로 추출하고 다운로드하세요. 무료, 간편한 도구.",
        "page_desc": "유튜브 영상의 썸네일 이미지를 고화질(4K, HD)로 추출하고 다운로드하세요. 무료, 간편한 도구.",
        "btn_get": "썸네일 가져오기",
        "label_max": "최대 화질 (MaxRes - 1280x720+)",
        "label_high": "고화질 (High - 480x360)",
        "label_med": "중간 화질 (Medium - 320x180)",
        "btn_dl": "이미지 다운로드",
        "toast_invalid": "잘못된 유튜브 URL입니다.",
        "related_header": "함께 보면 좋은 도구",
        "related_img": "이미지 변환기",
        "related_favicon": "파비콘 생성기",
        "related_color": "색상 변환기",
        "related_watermark": "워터마크 생성기"
    },
    "ja": {
        "title": "YouTubeサムネイルダウンローダー",
        "meta_title": "YouTubeサムネイルダウンローダー - Utilify",
        "meta_desc": "YouTube動画のサムネイルを高画質（4K, HD）で抽出してダウンロード。無料で簡単なツール。",
        "og_title": "YouTubeサムネイルダウンローダー - Utilify",
        "og_desc": "YouTube動画のサムネイルを高画質（4K, HD）で抽出してダウンロード。無料で簡単なツール。",
        "json_name": "YouTubeサムネイルダウンローダー",
        "json_desc": "YouTube動画のサムネイルを高画質（4K, HD）で抽出してダウンロード。無料で簡単なツール。",
        "page_desc": "YouTube動画のサムネイルを高画質（4K, HD）で抽出してダウンロード。無料で簡単なツール。",
        "btn_get": "サムネイルを取得",
        "label_max": "最大解像度 (MaxRes - 1280x720+)",
        "label_high": "高画質 (High - 480x360)",
        "label_med": "中画質 (Medium - 320x180)",
        "btn_dl": "画像をダウンロード",
        "toast_invalid": "無効なYouTube URLです。",
        "related_header": "関連ツール",
        "related_img": "画像変換",
        "related_favicon": "ファビコン生成",
        "related_color": "色変換",
        "related_watermark": "透かし追加"
    },
    "hi": {
        "title": "YouTube थंबनेल डाउनलोडर",
        "meta_title": "YouTube थंबनेल डाउनलोडर - Utilify",
        "meta_desc": "YouTube वीडियो थंबनेल को उच्च गुणवत्ता (4K, HD) में निकालें और डाउनलोड करें। नि:शुल्क और आसान उपकरण।",
        "og_title": "YouTube थंबनेल डाउनलोडर - Utilify",
        "og_desc": "YouTube वीडियो थंबनेल को उच्च गुणवत्ता (4K, HD) में निकालें और डाउनलोड करें। नि:शुल्क और आसान उपकरण।",
        "json_name": "YouTube थंबनेल डाउनलोडर",
        "json_desc": "YouTube वीडियो थंबनेल को उच्च गुणवत्ता (4K, HD) में निकालें और डाउनलोड करें। नि:शुल्क और आसान उपकरण।",
        "page_desc": "YouTube वीडियो थंबनेल को उच्च गुणवत्ता (4K, HD) में निकालें और डाउनलोड करें। नि:शुल्क और आसान उपकरण।",
        "btn_get": "थंबनेल प्राप्त करें",
        "label_max": "अधिकतम रिज़ॉल्यूशन (MaxRes - 1280x720+)",
        "label_high": "उच्च गुणवत्ता (High - 480x360)",
        "label_med": "मध्यम गुणवत्ता (Medium - 320x180)",
        "btn_dl": "छवि डाउनलोड करें",
        "toast_invalid": "अमान्य YouTube URL.",
        "related_header": "संबंधित उपकरण",
        "related_img": "छवि परिवर्तक",
        "related_favicon": "फ़ेविकॉन जेनरेटर",
        "related_color": "रंग परिवर्तक",
        "related_watermark": "छवि वॉटरमार्क"
    },
    "id": {
        "title": "Pengunduh Thumbnail YouTube",
        "meta_title": "Pengunduh Thumbnail YouTube - Utilify",
        "meta_desc": "Ekstrak dan unduh thumbnail video YouTube dalam kualitas tinggi (4K, HD). Alat gratis dan mudah.",
        "og_title": "Pengunduh Thumbnail YouTube - Utilify",
        "og_desc": "Ekstrak dan unduh thumbnail video YouTube dalam kualitas tinggi (4K, HD). Alat gratis dan mudah.",
        "json_name": "Pengunduh Thumbnail YouTube",
        "json_desc": "Ekstrak dan unduh thumbnail video YouTube dalam kualitas tinggi (4K, HD). Alat gratis dan mudah.",
        "page_desc": "Ekstrak dan unduh thumbnail video YouTube dalam kualitas tinggi (4K, HD). Alat gratis dan mudah.",
        "btn_get": "Dapatkan Thumbnail",
        "label_max": "Resolusi Maksimum (1280x720+)",
        "label_high": "Kualitas Tinggi (480x360)",
        "label_med": "Kualitas Sedang (320x180)",
        "btn_dl": "Unduh Gambar",
        "toast_invalid": "URL YouTube tidak valid.",
        "related_header": "Alat Terkait",
        "related_img": "Konverter Gambar",
        "related_favicon": "Pembuat Favicon",
        "related_color": "Konverter Warna",
        "related_watermark": "Tanda Air Gambar"
    },
    "vi": {
        "title": "Trình tải xuống hình thu nhỏ YouTube",
        "meta_title": "Trình tải xuống hình thu nhỏ YouTube - Utilify",
        "meta_desc": "Trích xuất và tải xuống hình thu nhỏ video YouTube ở chất lượng cao (4K, HD). Công cụ miễn phí và dễ dàng.",
        "og_title": "Trình tải xuống hình thu nhỏ YouTube - Utilify",
        "og_desc": "Trích xuất và tải xuống hình thu nhỏ video YouTube ở chất lượng cao (4K, HD). Công cụ miễn phí và dễ dàng.",
        "json_name": "Trình tải xuống hình thu nhỏ YouTube",
        "json_desc": "Trích xuất và tải xuống hình thu nhỏ video YouTube ở chất lượng cao (4K, HD). Công cụ miễn phí và dễ dàng.",
        "page_desc": "Trích xuất và tải xuống hình thu nhỏ video YouTube ở chất lượng cao (4K, HD). Công cụ miễn phí và dễ dàng.",
        "btn_get": "Lấy hình thu nhỏ",
        "label_max": "Độ phân giải tối đa (1280x720+)",
        "label_high": "Chất lượng cao (480x360)",
        "label_med": "Chất lượng trung bình (320x180)",
        "btn_dl": "Tải xuống hình ảnh",
        "toast_invalid": "URL YouTube không hợp lệ.",
        "related_header": "Công cụ liên quan",
        "related_img": "Chuyển đổi hình ảnh",
        "related_favicon": "Tạo Favicon",
        "related_color": "Chuyển đổi màu sắc",
        "related_watermark": "Đóng dấu ảnh"
    },
    "th": {
        "title": "เครื่องมือดาวน์โหลดภาพปก YouTube",
        "meta_title": "เครื่องมือดาวน์โหลดภาพปก YouTube - Utilify",
        "meta_desc": "ดึงและดาวน์โหลดภาพปกวิดีโอ YouTube ในคุณภาพสูง (4K, HD) เครื่องมือฟรีและง่ายดาย",
        "og_title": "เครื่องมือดาวน์โหลดภาพปก YouTube - Utilify",
        "og_desc": "ดึงและดาวน์โหลดภาพปกวิดีโอ YouTube ในคุณภาพสูง (4K, HD) เครื่องมือฟรีและง่ายดาย",
        "json_name": "เครื่องมือดาวน์โหลดภาพปก YouTube",
        "json_desc": "ดึงและดาวน์โหลดภาพปกวิดีโอ YouTube ในคุณภาพสูง (4K, HD) เครื่องมือฟรีและง่ายดาย",
        "page_desc": "ดึงและดาวน์โหลดภาพปกวิดีโอ YouTube ในคุณภาพสูง (4K, HD) เครื่องมือฟรีและง่ายดาย",
        "btn_get": "รับภาพปก",
        "label_max": "ความละเอียดสูงสุด (1280x720+)",
        "label_high": "คุณภาพสูง (480x360)",
        "label_med": "คุณภาพปานกลาง (320x180)",
        "btn_dl": "ดาวน์โหลดรูปภาพ",
        "toast_invalid": "URL YouTube ไม่ถูกต้อง",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_img": "แปลงรูปภาพ",
        "related_favicon": "สร้าง Favicon",
        "related_color": "แปลงสี",
        "related_watermark": "ลายน้ำรูปภาพ"
    },
    "de": {
        "title": "YouTube Thumbnail Downloader",
        "meta_title": "YouTube Thumbnail Downloader - Utilify",
        "meta_desc": "Extrahieren und laden Sie YouTube-Video-Thumbnails in hoher Qualität (4K, HD) herunter. Kostenloses und einfaches Tool.",
        "og_title": "YouTube Thumbnail Downloader - Utilify",
        "og_desc": "Extrahieren und laden Sie YouTube-Video-Thumbnails in hoher Qualität (4K, HD) herunter. Kostenloses und einfaches Tool.",
        "json_name": "YouTube Thumbnail Downloader",
        "json_desc": "Extrahieren und laden Sie YouTube-Video-Thumbnails in hoher Qualität (4K, HD) herunter. Kostenloses und einfaches Tool.",
        "page_desc": "Extrahieren und laden Sie YouTube-Video-Thumbnails in hoher Qualität (4K, HD) herunter. Kostenloses und einfaches Tool.",
        "btn_get": "Thumbnail abrufen",
        "label_max": "Maximale Auflösung (1280x720+)",
        "label_high": "Hohe Qualität (480x360)",
        "label_med": "Mittlere Qualität (320x180)",
        "btn_dl": "Bild herunterladen",
        "toast_invalid": "Ungültige YouTube-URL.",
        "related_header": "Ähnliche Tools",
        "related_img": "Bildkonverter",
        "related_favicon": "Favicon-Generator",
        "related_color": "Farbkonverter",
        "related_watermark": "Bild-Wasserzeichen"
    },
    "pt": {
        "title": "Baixador de Thumbnail do YouTube",
        "meta_title": "Baixador de Thumbnail do YouTube - Utilify",
        "meta_desc": "Extraia e baixe thumbnails de vídeos do YouTube em alta qualidade (4K, HD). Ferramenta gratuita e fácil.",
        "og_title": "Baixador de Thumbnail do YouTube - Utilify",
        "og_desc": "Extraia e baixe thumbnails de vídeos do YouTube em alta qualidade (4K, HD). Ferramenta gratuita e fácil.",
        "json_name": "Baixador de Thumbnail do YouTube",
        "json_desc": "Extraia e baixe thumbnails de vídeos do YouTube em alta qualidade (4K, HD). Ferramenta gratuita e fácil.",
        "page_desc": "Extraia e baixe thumbnails de vídeos do YouTube em alta qualidade (4K, HD). Ferramenta gratuita e fácil.",
        "btn_get": "Obter Thumbnail",
        "label_max": "Resolução Máxima (1280x720+)",
        "label_high": "Alta Qualidade (480x360)",
        "label_med": "Média Qualidade (320x180)",
        "btn_dl": "Baixar Imagem",
        "toast_invalid": "URL do YouTube inválida.",
        "related_header": "Ferramentas Relacionadas",
        "related_img": "Conversor de Imagem",
        "related_favicon": "Gerador de Favicon",
        "related_color": "Conversor de Cores",
        "related_watermark": "Marca d'água em Imagem"
    },
    "zh-cn": {
        "title": "YouTube 缩略图下载",
        "meta_title": "YouTube 缩略图下载 - Utilify",
        "meta_desc": "提取并下载高质量 (4K, HD) YouTube 视频缩略图。免费且简单。",
        "og_title": "YouTube 缩略图下载 - Utilify",
        "og_desc": "提取并下载高质量 YouTube 视频缩略图。",
        "json_name": "YouTube 缩略图下载",
        "json_desc": "提取并下载高质量 YouTube 视频缩略图。",
        "page_desc": "提取并下载高质量 (4K, HD) YouTube 视频缩略图。",
        "btn_get": "获取缩略图",
        "label_max": "最大分辨率 (1280x720+)",
        "label_high": "高质量 (480x360)",
        "label_med": "中等质量 (320x180)",
        "btn_dl": "下载图片",
        "toast_invalid": "无效的 YouTube URL。",
        "related_header": "相关工具",
        "related_img": "图片格式转换器",
        "related_favicon": "Favicon 生成器",
        "related_color": "颜色格式转换",
        "related_watermark": "图片水印"
    },
    "zh-tw": {
        "title": "YouTube 縮圖下載",
        "meta_title": "YouTube 縮圖下載 - Utilify",
        "meta_desc": "提取並下載高質量 (4K, HD) YouTube 視頻縮圖。免費且簡單。",
        "og_title": "YouTube 縮圖下載 - Utilify",
        "og_desc": "提取並下載高質量 YouTube 視頻縮圖。",
        "json_name": "YouTube 縮圖下載",
        "json_desc": "提取並下載高質量 YouTube 視頻縮圖。",
        "page_desc": "提取並下載高質量 (4K, HD) YouTube 視頻縮圖。",
        "btn_get": "獲取縮圖",
        "label_max": "最大分辨率 (1280x720+)",
        "label_high": "高質量 (480x360)",
        "label_med": "中等質量 (320x180)",
        "btn_dl": "下載圖片",
        "toast_invalid": "無效的 YouTube URL。",
        "related_header": "相關工具",
        "related_img": "圖片格式轉換器",
        "related_favicon": "Favicon 生成器",
        "related_color": "顏色格式轉換",
        "related_watermark": "圖片水印"
    }
}

REACTION_TEST = {
    "en": {
        "title": "Reaction Speed Test",
        "meta_title": "Reaction Speed Test - Utilify",
        "meta_desc": "Test your reaction time. Click as fast as you can when the screen turns green!",
        "og_title": "Reaction Speed Test - Utilify",
        "og_desc": "Test your reaction time. Click as fast as you can when the screen turns green!",
        "json_name": "Reaction Speed Test",
        "json_desc": "Test your reaction time. Click as fast as you can when the screen turns green!",
        "page_desc": "Test your reaction time. Click as fast as you can when the screen turns green!",
        "msg_start": "Click anywhere to Start.",
        "msg_wait": "Wait for Green...",
        "msg_click": "CLICK!",
        "msg_soon": "Too Soon! Click to try again.",
        "header_rank": "Ranking",
        "rank_1": "< 200 ms: Godlike Reflexes! 🏆",
        "rank_2": "200 - 300 ms: Great Speed! 🚀",
        "rank_3": "300 - 450 ms: Average Speed. 👌",
        "rank_4": "> 450 ms: Focus! You can do better. 🐢",
        "sub_play": "Play Again",
        "adsense_text": "Advertisement",
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_timer": "Timer"
    },
    "ko": {
        "title": "반응 속도 테스트",
        "meta_title": "반응 속도 테스트 - Utilify",
        "meta_desc": "당신의 반응 속도는 얼마입니까? 화면이 초록색으로 바뀔 때 최대한 빨리 클릭하세요!",
        "og_title": "반응 속도 테스트 - Utilify",
        "og_desc": "당신의 반응 속도는 얼마입니까? 화면이 초록색으로 바뀔 때 최대한 빨리 클릭하세요!",
        "json_name": "반응 속도 테스트",
        "json_desc": "당신의 반응 속도는 얼마입니까? 화면이 초록색으로 바뀔 때 최대한 빨리 클릭하세요!",
        "page_desc": "당신의 반응 속도는 얼마입니까? 화면이 초록색으로 바뀔 때 최대한 빨리 클릭하세요!",
        "msg_start": "화면을 클릭하여 시작하세요.",
        "msg_wait": "초록색이 될 때까지 기다리세요...",
        "msg_click": "클릭하세요!",
        "msg_soon": "너무 빨라요! 파란색 화면을 클릭해서 다시 시도하세요.",
        "header_rank": "Ranking",
        "rank_1": "< 200 ms: 상위 1% 수준입니다! 🏆",
        "rank_2": "200 - 300 ms: 훌륭한 반응 속도입니다! 🚀",
        "rank_3": "300 - 450 ms: 평균적인 반응 속도입니다. 👌",
        "rank_4": "> 450 ms: 조금 더 집중해보세요! 🐢",
        "sub_play": "다시 하기",
        "related_header": "함께 보면 좋은 도구",
        "related_unit": "단위 변환기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_timer": "타이머"
    },
    "ja": {
        "title": "反応速度テスト",
        "meta_title": "反応速度テスト - Utilify",
        "meta_desc": "あなたの反応速度をテストします。画面が緑色になったらできるだけ早くクリックしてください！",
        "og_title": "反応速度テスト - Utilify",
        "og_desc": "あなたの反応速度をテストします。画面が緑色になったらできるだけ早くクリックしてください！",
        "json_name": "反応速度テスト",
        "json_desc": "あなたの反応速度をテストします。画面が緑色になったらできるだけ早くクリックしてください！",
        "page_desc": "あなたの反応速度をテストします。画面が緑色になったらできるだけ早くクリックしてください！",
        "msg_start": "クリックして開始",
        "msg_wait": "緑色になるまで待機...",
        "msg_click": "クリック！",
        "msg_soon": "早すぎます！クリックしてやり直してください。",
        "header_rank": "ランキング",
        "rank_1": "< 200 ms: 神レベルの反応速度！ 🏆",
        "rank_2": "200 - 300 ms: 素晴らしい速さです！ 🚀",
        "rank_3": "300 - 450 ms: 平均的な速度です。 👌",
        "rank_4": "> 450 ms: もっと集中しましょう！ 🐢",
        "sub_play": "もう一度プレイ",
        "related_header": "関連ツール",
        "related_unit": "単位変換",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算",
        "related_timer": "タイマー"
    },
    "hi": {
        "title": "प्रतिक्रिया गति परीक्षण",
        "meta_title": "प्रतिक्रिया गति परीक्षण - Utilify",
        "meta_desc": "अपनी प्रतिक्रिया समय का परीक्षण करें। स्क्रीन हरी होने पर जितनी जल्दी हो सके क्लिक करें!",
        "og_title": "प्रतिक्रिया गति परीक्षण - Utilify",
        "og_desc": "अपनी प्रतिक्रिया समय का परीक्षण करें। स्क्रीन हरी होने पर जितनी जल्दी हो सके क्लिक करें!",
        "json_name": "प्रतिक्रिया गति परीक्षण",
        "json_desc": "अपनी प्रतिक्रिया समय का परीक्षण करें। स्क्रीन हरी होने पर जितनी जल्दी हो सके क्लिक करें!",
        "page_desc": "अपनी प्रतिक्रिया समय का परीक्षण करें। स्क्रीन हरी होने पर जितनी जल्दी हो सके क्लिक करें!",
        "msg_start": "शुरू करने के लिए क्लिक करें",
        "msg_wait": "हरे होने की प्रतीक्षा करें...",
        "msg_click": "क्लिक करें!",
        "msg_soon": "बहुत जल्दी! फिर से प्रयास करने के लिए क्लिक करें।",
        "header_rank": "रैंकिंग",
        "rank_1": "< 200 ms: भगवान जैसी सजगता! 🏆",
        "rank_2": "200 - 300 ms: शानदार गति! 🚀",
        "rank_3": "300 - 450 ms: औसत गति। 👌",
        "rank_4": "> 450 ms: ध्यान दें! आप बेहतर कर सकते हैं। 🐢",
        "sub_play": "फिर से खेलें",
        "related_header": "संबंधित उपकरण",
        "related_unit": "इकाई परिवर्तक",
        "related_bmi": "BMI कैलकुलेटर",
        "related_date": "दिनांक कैलकुलेटर",
        "related_timer": "टाइमर"
    },
    "id": {
        "title": "Tes Kecepatan Reaksi",
        "meta_title": "Tes Kecepatan Reaksi - Utilify",
        "meta_desc": "Uji waktu reaksi Anda. Klik secepat mungkin saat layar berubah menjadi hijau!",
        "og_title": "Tes Kecepatan Reaksi - Utilify",
        "og_desc": "Uji waktu reaksi Anda. Klik secepat mungkin saat layar berubah menjadi hijau!",
        "json_name": "Tes Kecepatan Reaksi",
        "json_desc": "Uji waktu reaksi Anda. Klik secepat mungkin saat layar berubah menjadi hijau!",
        "page_desc": "Uji waktu reaksi Anda. Klik secepat mungkin saat layar berubah menjadi hijau!",
        "msg_start": "Klik untuk Mulai",
        "msg_wait": "Tunggu Hijau...",
        "msg_click": "KLIK!",
        "msg_soon": "Terlalu Cepat! Klik untuk mencoba lagi.",
        "header_rank": "Peringkat",
        "rank_1": "< 200 ms: Refleks Dewa! 🏆",
        "rank_2": "200 - 300 ms: Kecepatan Hebat! 🚀",
        "rank_3": "300 - 450 ms: Kecepatan Rata-rata. 👌",
        "rank_4": "> 450 ms: Fokus! Kamu bisa lebih baik. 🐢",
        "sub_play": "Main Lagi",
        "related_header": "Alat Terkait",
        "related_unit": "Konverter Unit",
        "related_bmi": "Kalkulator BMI",
        "related_date": "Kalkulator Tanggal",
        "related_timer": "Timer"
    },
    "vi": {
        "title": "Kiểm tra tốc độ phản ứng",
        "meta_title": "Kiểm tra tốc độ phản ứng - Utilify",
        "meta_desc": "Kiểm tra thời gian phản ứng của bạn. Nhấp càng nhanh càng tốt khi màn hình chuyển sang màu xanh lá cây!",
        "og_title": "Kiểm tra tốc độ phản ứng - Utilify",
        "og_desc": "Kiểm tra thời gian phản ứng của bạn. Nhấp càng nhanh càng tốt khi màn hình chuyển sang màu xanh lá cây!",
        "json_name": "Kiểm tra tốc độ phản ứng",
        "json_desc": "Kiểm tra thời gian phản ứng của bạn. Nhấp càng nhanh càng tốt khi màn hình chuyển sang màu xanh lá cây!",
        "page_desc": "Kiểm tra thời gian phản ứng của bạn. Nhấp càng nhanh càng tốt khi màn hình chuyển sang màu xanh lá cây!",
        "msg_start": "Nhấp để bắt đầu",
        "msg_wait": "Chờ màu xanh...",
        "msg_click": "NHẤP!",
        "msg_soon": "Quá sớm! Nhấp để thử lại.",
        "header_rank": "Xếp hạng",
        "rank_1": "< 200 ms: Phản xạ thần thánh! 🏆",
        "rank_2": "200 - 300 ms: Tốc độ tuyệt vời! 🚀",
        "rank_3": "300 - 450 ms: Tốc độ trung bình. 👌",
        "rank_4": "> 450 ms: Tập trung! Bạn có thể làm tốt hơn. 🐢",
        "sub_play": "Chơi lại",
        "related_header": "Công cụ liên quan",
        "related_unit": "Chuyển đổi đơn vị",
        "related_bmi": "Máy tính BMI",
        "related_date": "Máy tính ngày",
        "related_timer": "Hẹn giờ"
    },
    "th": {
        "title": "ทดสอบความเร็วในการตอบสนอง",
        "meta_title": "ทดสอบความเร็วในการตอบสนอง - Utilify",
        "meta_desc": "ทดสอบเวลาตอบสนองของคุณ คลิกให้เร็วที่สุดเมื่อหน้าจอเปลี่ยนเป็นสีเขียว!",
        "og_title": "ทดสอบความเร็วในการตอบสนอง - Utilify",
        "og_desc": "ทดสอบเวลาตอบสนองของคุณ คลิกให้เร็วที่สุดเมื่อหน้าจอเปลี่ยนเป็นสีเขียว!",
        "json_name": "ทดสอบความเร็วในการตอบสนอง",
        "json_desc": "ทดสอบเวลาตอบสนองของคุณ คลิกให้เร็วที่สุดเมื่อหน้าจอเปลี่ยนเป็นสีเขียว!",
        "page_desc": "ทดสอบเวลาตอบสนองของคุณ คลิกให้เร็วที่สุดเมื่อหน้าจอเปลี่ยนเป็นสีเขียว!",
        "msg_start": "คลิกเพื่อเริ่ม",
        "msg_wait": "รอสีเขียว...",
        "msg_click": "คลิก!",
        "msg_soon": "เร็วเกินไป! คลิกเพื่อลองอีกครั้ง",
        "header_rank": "อันดับ",
        "rank_1": "< 200 ms: ปฏิกิริยาขั้นเทพ! 🏆",
        "rank_2": "200 - 300 ms: ความเร็วเยี่ยม! 🚀",
        "rank_3": "300 - 450 ms: ความเร็วปานกลาง 👌",
        "rank_4": "> 450 ms: ตั้งสมาธิ! คุณทำได้ดีกว่านี้ 🐢",
        "sub_play": "เล่นอีกครั้ง",
        "related_header": "เครื่องมือที่เกี่ยวข้อง",
        "related_unit": "แปลงหน่วย",
        "related_bmi": "เครื่องคำนวณ BMI",
        "related_date": "เครื่องคำนวณวันที่",
        "related_timer": "ตัวจับเวลา"
    },
    "de": {
        "title": "Reaktionstest",
        "meta_title": "Reaktionstest - Utilify",
        "meta_desc": "Testen Sie Ihre Reaktionszeit. Klicken Sie so schnell wie möglich, wenn der Bildschirm grün wird!",
        "og_title": "Reaktionstest - Utilify",
        "og_desc": "Testen Sie Ihre Reaktionszeit. Klicken Sie so schnell wie möglich, wenn der Bildschirm grün wird!",
        "json_name": "Reaktionstest",
        "json_desc": "Testen Sie Ihre Reaktionszeit. Klicken Sie so schnell wie möglich, wenn der Bildschirm grün wird!",
        "page_desc": "Testen Sie Ihre Reaktionszeit. Klicken Sie so schnell wie möglich, wenn der Bildschirm grün wird!",
        "msg_start": "Klicken zum Starten",
        "msg_wait": "Warten auf Grün...",
        "msg_click": "KLICKEN!",
        "msg_soon": "Zu früh! Klicken, um es erneut zu versuchen.",
        "header_rank": "Rangliste",
        "rank_1": "< 200 ms: Gottgleiche Reflexe! 🏆",
        "rank_2": "200 - 300 ms: Tolle Geschwindigkeit! 🚀",
        "rank_3": "300 - 450 ms: Durchschnittliche Geschwindigkeit. 👌",
        "rank_4": "> 450 ms: Konzentrieren! Das kannst du besser. 🐢",
        "sub_play": "Nochmal spielen",
        "related_header": "Ähnliche Tools",
        "related_unit": "Einheitenumrechner",
        "related_bmi": "BMI Rechner",
        "related_date": "Datumsrechner",
        "related_timer": "Timer"
    },
    "pt": {
        "title": "Teste de Velocidade de Reação",
        "meta_title": "Teste de Velocidade de Reação - Utilify",
        "meta_desc": "Teste seu tempo de reação. Clique o mais rápido que puder quando a tela ficar verde!",
        "og_title": "Teste de Velocidade de Reação - Utilify",
        "og_desc": "Teste seu tempo de reação. Clique o mais rápido que puder quando a tela ficar verde!",
        "json_name": "Teste de Velocidade de Reação",
        "json_desc": "Teste seu tempo de reação. Clique o mais rápido que puder quando a tela ficar verde!",
        "page_desc": "Teste seu tempo de reação. Clique o mais rápido que puder quando a tela ficar verde!",
        "msg_start": "Clique para Iniciar",
        "msg_wait": "Espere pelo Verde...",
        "msg_click": "CLIQUE!",
        "msg_soon": "Muito Cedo! Clique para tentar novamente.",
        "header_rank": "Classificação",
        "rank_1": "< 200 ms: Reflexos Divinos! 🏆",
        "rank_2": "200 - 300 ms: Ótima Velocidade! 🚀",
        "rank_3": "300 - 450 ms: Velocidade Média. 👌",
        "rank_4": "> 450 ms: Foco! Você pode fazer melhor. 🐢",
        "sub_play": "Jogar Novamente",
        "related_header": "Ferramentas Relacionadas",
        "related_unit": "Conversor de Unidades",
        "related_bmi": "Calculadora de IMC",
        "related_date": "Calculadora de Data",
        "related_timer": "Cronômetro"
    },
    "zh-cn": {
        "title": "反应速度测试",
        "meta_title": "反应速度测试 - Utilify",
        "meta_desc": "测试您的反应速度。屏幕变绿时尽快点击！",
        "og_title": "反应速度测试 - Utilify",
        "og_desc": "测试您的反应速度。屏幕变绿时尽快点击！",
        "json_name": "反应速度测试",
        "json_desc": "测试您的反应速度。屏幕变绿时尽快点击！",
        "page_desc": "测试您的反应速度。屏幕变绿时尽快点击！",
        "msg_start": "点击任意位置开始。",
        "msg_wait": "等待变绿...",
        "msg_click": "点击!",
        "msg_soon": "太快了! 点击重试。",
        "header_rank": "Ranking",
        "rank_1": "< 200 ms: 神级反应! 🏆",
        "rank_2": "200 - 300 ms: 极速! 🚀",
        "rank_3": "300 - 450 ms: 平均速度。 👌",
        "rank_4": "> 450 ms: 集中注意力! 🐢",
        "sub_play": "再玩一次",
        "related_header": "相关工具",
        "related_unit": "单位转换器",
        "related_bmi": "BMI 计算器",
        "related_date": "日期计算器",
        "related_timer": "计时器"
    },
    "zh-tw": {
        "title": "反應速度測試",
        "meta_title": "反應速度測試 - Utilify",
        "meta_desc": "測試您的反應速度。屏幕變綠時儘快點擊！",
        "og_title": "反應速度測試 - Utilify",
        "og_desc": "測試您的反應速度。屏幕變綠時儘快點擊！",
        "json_name": "反應速度測試",
        "json_desc": "測試您的反應速度。屏幕變綠時儘快點擊！",
        "page_desc": "測試您的反應速度。屏幕變綠時儘快點擊！",
        "msg_start": "點擊任意位置開始。",
        "msg_wait": "等待變綠...",
        "msg_click": "點擊!",
        "msg_soon": "太快了! 點擊重試。",
        "header_rank": "Ranking",
        "rank_1": "< 200 ms: 神級反應! 🏆",
        "rank_2": "200 - 300 ms: 極速! 🚀",
        "rank_3": "300 - 450 ms: 平均速度。 👌",
        "rank_4": "> 450 ms: 集中注意力! 🐢",
        "sub_play": "再玩一次",
        "related_header": "相關工具",
        "related_unit": "單位轉換器",
        "related_bmi": "BMI 計算器",
        "related_date": "日期計算器",
        "related_timer": "計時器"
    }
}


JWT_DECODER = {
    "en": {
        "title": "JWT Decoder",
        "meta_title": "JWT Decoder & Inspector - Utilify",
        "meta_desc": "Decode and inspect JSON Web Tokens (JWT) in your browser. Header, payload, and expiry checked locally — your token never leaves the page.",
        "json_name": "JWT Decoder",
        "json_desc": "Client-side JWT decoder that displays the header and payload and verifies expiry.",
        "page_desc": "Paste a JWT to decode its header and payload. Tokens are processed locally and never sent to a server.",
        "label_input": "JWT",
        "ph_input": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0...",
        "btn_decode": "Decode",
        "btn_clear": "Clear",
        "label_header": "Header",
        "label_payload": "Payload",
        "label_signature": "Signature (raw)",
        "signature_note": "Signature verification requires the issuer's secret/public key and is not performed here.",
        "alert_empty": "Paste a JWT to decode.",
        "alert_format": "Not a valid JWT — expected three dot-separated segments.",
        "alert_decode_error": "Decode error: ",
        "alert_valid": "Valid token. Expires in ",
        "alert_expired": "Token expired at ",
        "alert_no_exp": "Decoded successfully. No 'exp' claim — expiry not checked.",
        "related_header": "Related Tools",
        "related_base64": "Base64 Converter",
        "related_json": "JSON Formatter",
        "related_hash": "Hash Generator",
        "howto_header": "How to use",
        "howto_html": "<ol><li>Paste a JWT (three Base64URL segments separated by dots) into the input.</li><li>Click <strong>Decode</strong> to view the header and payload as JSON.</li><li>If the payload contains an <code>exp</code> claim, the page checks expiry against your local clock and shows valid / expired status.</li><li>Signature verification requires the issuer's secret or public key and is NOT performed here — this tool inspects the contents only.</li></ol><p>JWTs are <em>not encrypted</em>. Anyone with the token can read its contents. Treat the payload as public information unless it's wrapped in JWE.</p>",
        "examples_header": "Examples",
        "examples_html": '<p><strong>Sample token:</strong></p><pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\neyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkYSJ9.\nTJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ</code></pre><p><strong>Decoded:</strong></p><pre><code>Header:  {"alg":"HS256","typ":"JWT"}\nPayload: {"sub":"1234567890","name":"Ada"}</code></pre>'
    },
    "ko": {
        "title": "JWT 디코더",
        "meta_title": "JWT 디코더 & 검사기 - Utilify",
        "meta_desc": "JSON Web Token(JWT)을 브라우저에서 디코딩하고 검사하세요. 헤더, 페이로드, 만료 시간을 로컬에서 확인합니다.",
        "json_name": "JWT 디코더",
        "json_desc": "브라우저에서 동작하는 JWT 디코더. 헤더와 페이로드를 표시하고 만료 시간을 확인합니다.",
        "page_desc": "JWT를 붙여넣어 헤더와 페이로드를 디코딩하세요. 토큰은 로컬에서만 처리되며 서버로 전송되지 않습니다.",
        "label_input": "JWT",
        "ph_input": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0...",
        "btn_decode": "디코딩",
        "btn_clear": "지우기",
        "label_header": "Header",
        "label_payload": "Payload",
        "label_signature": "Signature (원본)",
        "signature_note": "서명 검증은 발급자의 비밀키/공개키가 필요하므로 여기에서 수행하지 않습니다.",
        "alert_empty": "디코딩할 JWT를 입력하세요.",
        "alert_format": "유효한 JWT 형식이 아닙니다. 점(.)으로 구분된 세 부분이 필요합니다.",
        "alert_decode_error": "디코딩 오류: ",
        "alert_valid": "유효한 토큰입니다. 남은 시간 ",
        "alert_expired": "만료된 토큰입니다. 만료 시각: ",
        "alert_no_exp": "디코딩 완료. 'exp' 클레임이 없어 만료 시각을 확인하지 못했습니다.",
        "related_header": "관련 도구",
        "related_base64": "Base64 변환기",
        "related_json": "JSON 포매터",
        "related_hash": "해시 생성기",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>JWT(점으로 구분된 Base64URL 3개)를 입력 창에 붙여넣으세요.</li><li><strong>Decode</strong>를 눌러 header와 payload를 JSON으로 확인합니다.</li><li>payload에 <code>exp</code> 클레임이 있으면 로컬 시각과 비교해 유효/만료 여부를 표시합니다.</li><li>서명 검증은 발급자의 비밀키/공개키가 필요하므로 여기서는 수행하지 않습니다 — 내용 검사 전용입니다.</li></ol><p>JWT는 <em>암호화된 것이 아닙니다</em>. 토큰을 가진 누구나 내용을 읽을 수 있으므로 JWE로 감싸지 않은 이상 payload는 공개 정보로 취급해야 합니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>샘플 토큰:</strong></p><pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\neyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkYSJ9.\nTJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ</code></pre><p><strong>디코딩 결과:</strong></p><pre><code>Header:  {"alg":"HS256","typ":"JWT"}\nPayload: {"sub":"1234567890","name":"Ada"}</code></pre>'
    },
    "ja": {
        "title": "JWTデコーダー",
        "meta_title": "JWTデコーダー & インスペクター - Utilify",
        "meta_desc": "JSON Web Token（JWT）をブラウザでデコード・検査します。ヘッダー、ペイロード、有効期限をローカルで確認 — トークンはページ外に送信されません。",
        "json_name": "JWTデコーダー",
        "json_desc": "ブラウザで動作するJWTデコーダー。ヘッダーとペイロードを表示し、有効期限を確認します。",
        "page_desc": "JWTを貼り付けてヘッダーとペイロードをデコードします。トークンはローカルでのみ処理され、サーバーには送信されません。",
        "label_input": "JWT",
        "ph_input": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0...",
        "btn_decode": "デコード",
        "btn_clear": "クリア",
        "label_header": "Header",
        "label_payload": "Payload",
        "label_signature": "Signature (生)",
        "signature_note": "署名の検証には発行者の秘密鍵または公開鍵が必要なため、ここでは行いません。",
        "alert_empty": "デコードするJWTを入力してください。",
        "alert_format": "有効なJWT形式ではありません。ドット区切りの3つのセグメントが必要です。",
        "alert_decode_error": "デコードエラー: ",
        "alert_valid": "有効なトークンです。有効期限まで ",
        "alert_expired": "トークンの有効期限が切れています。期限: ",
        "alert_no_exp": "デコード成功。'exp' クレームがないため、有効期限は確認されませんでした。",
        "related_header": "関連ツール",
        "related_base64": "Base64変換",
        "related_json": "JSONフォーマッター",
        "related_hash": "ハッシュ生成",
        "howto_header": "使い方",
        "howto_html": '<ol><li>JWT（ドット区切りのBase64URL 3セグメント）を入力欄に貼り付けます。</li><li><strong>デコード</strong>をクリックするとHeaderとPayloadがJSONで表示されます。</li><li>ペイロードに<code>exp</code>クレームがある場合、ローカルの時刻と比較して有効／期限切れを表示します。</li><li>署名の検証には発行者の秘密鍵または公開鍵が必要なため、ここでは行いません — 内容の検査専用です。</li></ol><p>JWTは<em>暗号化されていません</em>。トークンを持つ誰でも内容を読めるため、JWEで包まない限りペイロードは公開情報として扱ってください。</p>',
        "examples_header": "例",
        "examples_html": '<p><strong>サンプルトークン:</strong></p><pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\neyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkYSJ9.\nTJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ</code></pre><p><strong>デコード結果:</strong></p><pre><code>Header:  {"alg":"HS256","typ":"JWT"}\nPayload: {"sub":"1234567890","name":"Ada"}</code></pre>'
    }
}


HASH_GENERATOR = {
    "en": {
        "title": "Hash Generator",
        "meta_title": "Hash Generator (MD5, SHA-1, SHA-256, SHA-384, SHA-512) - Utilify",
        "meta_desc": "Generate MD5, SHA-1, SHA-256, SHA-384, and SHA-512 hashes of any text — entirely in your browser.",
        "json_name": "Hash Generator",
        "json_desc": "Compute MD5 and SHA-family hashes from text input, all client-side.",
        "page_desc": "Type any text to instantly compute MD5 and SHA-1/256/384/512 digests. Nothing is uploaded — all hashing runs locally.",
        "label_input": "Text",
        "ph_input": "Type text to hash...",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "alert_copy_empty": "Nothing to copy.",
        "related_header": "Related Tools",
        "related_pw": "Password Generator",
        "related_base64": "Base64 Converter",
        "related_jwt": "JWT Decoder",
        "howto_header": "How to use",
        "howto_html": "<ol><li>Type or paste text into the input area.</li><li>MD5 and SHA-1/256/384/512 digests are computed live as you type.</li><li>Click <strong>Copy</strong> next to any digest to copy it.</li><li>SHA family uses the browser's built-in <code>crypto.subtle.digest()</code>; MD5 is implemented inline since the Web Crypto API does not include it.</li></ol><p><strong>Security note:</strong> MD5 and SHA-1 are <em>broken</em> for cryptographic use (collisions exist). Use them only for non-security integrity checks. For passwords, use a slow KDF like bcrypt, scrypt, or argon2 on the server, never plain hashes.</p>",
        "examples_header": "Examples",
        "examples_html": '<p><strong>"abc" digests:</strong></p><pre><code>MD5    : 900150983cd24fb0d6963f7d28e17f72\nSHA-1  : a9993e364706816aba3e25717850c26c9cd0d89d\nSHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad</code></pre><p><strong>Empty string:</strong></p><pre><code>MD5    : d41d8cd98f00b204e9800998ecf8427e\nSHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code></pre>'
    },
    "ko": {
        "title": "해시 생성기",
        "meta_title": "해시 생성기 (MD5, SHA-1, SHA-256, SHA-384, SHA-512) - Utilify",
        "meta_desc": "임의의 텍스트로부터 MD5, SHA-1, SHA-256, SHA-384, SHA-512 해시를 브라우저에서 바로 생성합니다.",
        "json_name": "해시 생성기",
        "json_desc": "텍스트 입력에 대해 MD5와 SHA 계열 해시를 클라이언트에서 계산합니다.",
        "page_desc": "텍스트를 입력하면 MD5와 SHA-1/256/384/512 다이제스트가 즉시 계산됩니다. 데이터는 외부로 전송되지 않습니다.",
        "label_input": "텍스트",
        "ph_input": "해시할 텍스트를 입력하세요...",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "related_header": "관련 도구",
        "related_pw": "비밀번호 생성기",
        "related_base64": "Base64 변환기",
        "related_jwt": "JWT 디코더",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>텍스트를 입력하거나 붙여넣으세요.</li><li>MD5와 SHA-1/256/384/512 다이제스트가 입력하는 즉시 계산됩니다.</li><li>각 다이제스트 옆 <strong>Copy</strong> 버튼으로 복사할 수 있습니다.</li><li>SHA 계열은 브라우저 내장 <code>crypto.subtle.digest()</code>를 사용하며, Web Crypto API에 없는 MD5만 인라인 구현되어 있습니다.</li></ol><p><strong>보안 주의:</strong> MD5와 SHA-1은 충돌이 발견되어 암호학적 용도로 <em>부적합</em>합니다. 보안과 무관한 무결성 검사에만 사용하세요. 비밀번호는 항상 bcrypt·scrypt·argon2 같은 KDF를 서버에서 사용해야 합니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>"abc" 다이제스트:</strong></p><pre><code>MD5    : 900150983cd24fb0d6963f7d28e17f72\nSHA-1  : a9993e364706816aba3e25717850c26c9cd0d89d\nSHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad</code></pre><p><strong>빈 문자열:</strong></p><pre><code>MD5    : d41d8cd98f00b204e9800998ecf8427e\nSHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code></pre>'
    },
    "ja": {
        "title": "ハッシュ生成",
        "meta_title": "ハッシュ生成 (MD5, SHA-1, SHA-256, SHA-384, SHA-512) - Utilify",
        "meta_desc": "任意のテキストからMD5・SHA-1・SHA-256・SHA-384・SHA-512ハッシュをブラウザで即生成します。",
        "json_name": "ハッシュ生成",
        "json_desc": "テキスト入力からMD5とSHAファミリーハッシュをクライアントサイドで計算します。",
        "page_desc": "テキストを入力するとMD5・SHA-1/256/384/512ダイジェストを即座に計算します。データはアップロードされません — すべてローカルで処理されます。",
        "label_input": "テキスト",
        "ph_input": "ハッシュするテキストを入力...",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "alert_copy_empty": "コピーする内容がありません。",
        "related_header": "関連ツール",
        "related_pw": "パスワード生成",
        "related_base64": "Base64変換",
        "related_jwt": "JWTデコーダー",
        "howto_header": "使い方",
        "howto_html": '<ol><li>テキストを入力または貼り付けます。</li><li>MD5とSHA-1/256/384/512ダイジェストが入力に合わせてリアルタイムで計算されます。</li><li>各ダイジェスト横の<strong>コピー</strong>ボタンでコピーできます。</li><li>SHAファミリーはブラウザ内蔵の<code>crypto.subtle.digest()</code>を使用し、Web Crypto APIに含まれないMD5のみインラインで実装されています。</li></ol><p><strong>セキュリティ注意</strong>: MD5とSHA-1は衝突が発見されており、暗号学的用途には<em>不適切</em>です。セキュリティに無関係な整合性チェックにのみ使用してください。パスワードには必ずサーバー側でbcrypt・scrypt・argon2などのKDFを使用してください。</p>',
        "examples_header": "例",
        "examples_html": '<p><strong>"abc" ダイジェスト:</strong></p><pre><code>MD5    : 900150983cd24fb0d6963f7d28e17f72\nSHA-1  : a9993e364706816aba3e25717850c26c9cd0d89d\nSHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad</code></pre><p><strong>空文字列:</strong></p><pre><code>MD5    : d41d8cd98f00b204e9800998ecf8427e\nSHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code></pre>'
    }
}


UNIX_TIMESTAMP = {
    "en": {
        "title": "Unix Timestamp Converter",
        "meta_title": "Unix Timestamp ↔ Date Converter - Utilify",
        "meta_desc": "Convert Unix timestamps (seconds or milliseconds) to ISO 8601 dates and back. Live current timestamp included.",
        "json_name": "Unix Timestamp Converter",
        "json_desc": "Bidirectional conversion between Unix timestamps and human-readable dates.",
        "page_desc": "Convert between Unix timestamps and dates. Auto-detects seconds vs. milliseconds and shows both UTC and your local time zone.",
        "label_now": "Current Unix time (UTC)",
        "label_ts_input": "Unix timestamp → Date",
        "ph_ts_input": "e.g. 1700000000 or 1700000000000",
        "btn_convert_ts": "Convert",
        "btn_use_now": "Use Now",
        "label_local": "Local",
        "label_date_input": "Date → Unix timestamp",
        "ph_date_input": "e.g. 2024-01-15T12:00:00Z or 2024-01-15",
        "btn_convert_date": "Convert",
        "label_seconds": "Seconds",
        "label_ms": "Milliseconds",
        "alert_invalid_ts": "Invalid timestamp.",
        "alert_invalid_date": "Invalid date string.",
        "related_header": "Related Tools",
        "related_date": "Date Calculator",
        "related_timer": "Timer",
        "related_jwt": "JWT Decoder",
        "howto_header": "How to use",
        "howto_html": "<ol><li>The current Unix time updates live at the top — click <strong>Use Now</strong> to copy it into the converter.</li><li>To convert a timestamp to a date: paste the number and press <strong>Convert</strong>. Seconds (10 digits) and milliseconds (13 digits) are auto-detected.</li><li>To convert a date string to a timestamp: paste an ISO 8601 string (<code>2024-01-15T12:00:00Z</code>) or just <code>2024-01-15</code> and press <strong>Convert</strong>.</li><li>Both UTC and your local time-zone are shown so you don't need to do time-zone math.</li></ol><p>Unix time counts seconds since 1970-01-01 UTC, ignoring leap seconds. The 32-bit signed range overflows in 2038 — most modern systems use 64-bit and are unaffected.</p>",
        "examples_header": "Examples",
        "examples_html": '<p><strong>Timestamp → date:</strong></p><pre><code>1700000000      → 2023-11-14T22:13:20Z (UTC)\n1700000000000   → 2023-11-14T22:13:20.000Z\n0               → 1970-01-01T00:00:00Z (Unix epoch)</code></pre><p><strong>Date → timestamp:</strong></p><pre><code>2024-01-15T12:00:00Z → 1705320000  (seconds)\n                     → 1705320000000 (ms)</code></pre>'
    },
    "ko": {
        "title": "Unix 타임스탬프 변환기",
        "meta_title": "Unix 타임스탬프 ↔ 날짜 변환기 - Utilify",
        "meta_desc": "Unix 타임스탬프(초 또는 밀리초)와 ISO 8601 날짜를 양방향으로 변환합니다. 현재 시각도 실시간 표시.",
        "json_name": "Unix 타임스탬프 변환기",
        "json_desc": "Unix 타임스탬프와 사람이 읽기 좋은 날짜 사이의 양방향 변환.",
        "page_desc": "Unix 타임스탬프와 날짜를 변환합니다. 초/밀리초를 자동 감지하고 UTC와 로컬 시간을 함께 보여줍니다.",
        "label_now": "현재 Unix 시간 (UTC)",
        "label_ts_input": "Unix 타임스탬프 → 날짜",
        "ph_ts_input": "예: 1700000000 또는 1700000000000",
        "btn_convert_ts": "변환",
        "btn_use_now": "현재 시각",
        "label_local": "로컬",
        "label_date_input": "날짜 → Unix 타임스탬프",
        "ph_date_input": "예: 2024-01-15T12:00:00Z 또는 2024-01-15",
        "btn_convert_date": "변환",
        "label_seconds": "초",
        "label_ms": "밀리초",
        "alert_invalid_ts": "유효하지 않은 타임스탬프입니다.",
        "alert_invalid_date": "유효하지 않은 날짜 문자열입니다.",
        "related_header": "관련 도구",
        "related_date": "날짜 계산기",
        "related_timer": "타이머",
        "related_jwt": "JWT 디코더",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>상단에 현재 Unix 시간이 실시간 표시됩니다 — <strong>Use Now</strong>로 변환기에 입력할 수 있습니다.</li><li>타임스탬프를 날짜로: 숫자를 붙여넣고 <strong>Convert</strong>를 누르세요. 초(10자리)와 밀리초(13자리)가 자동 감지됩니다.</li><li>날짜를 타임스탬프로: ISO 8601(<code>2024-01-15T12:00:00Z</code>) 또는 <code>2024-01-15</code> 형식을 입력하고 <strong>Convert</strong>를 누르세요.</li><li>UTC와 로컬 타임존이 함께 표시되어 시간대 계산이 불필요합니다.</li></ol><p>Unix time은 1970-01-01 UTC 이후의 초를 세며 윤초는 무시합니다. 32-bit signed는 2038년에 오버플로하지만 대부분의 현대 시스템은 64-bit이므로 영향이 없습니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>타임스탬프 → 날짜:</strong></p><pre><code>1700000000      → 2023-11-14T22:13:20Z (UTC)\n1700000000000   → 2023-11-14T22:13:20.000Z\n0               → 1970-01-01T00:00:00Z (Unix epoch)</code></pre><p><strong>날짜 → 타임스탬프:</strong></p><pre><code>2024-01-15T12:00:00Z → 1705320000  (초)\n                     → 1705320000000 (밀리초)</code></pre>'
    },
    "ja": {
        "title": "Unixタイムスタンプ変換",
        "meta_title": "Unixタイムスタンプ ↔ 日付変換 - Utilify",
        "meta_desc": "Unixタイムスタンプ（秒またはミリ秒）とISO 8601日付を相互変換します。現在時刻のリアルタイム表示付き。",
        "json_name": "Unixタイムスタンプ変換",
        "json_desc": "Unixタイムスタンプと人が読める日付の双方向変換。",
        "page_desc": "Unixタイムスタンプと日付を相互変換します。秒・ミリ秒を自動判別し、UTCとローカルタイムゾーンを両方表示します。",
        "label_now": "現在のUnix時刻 (UTC)",
        "label_ts_input": "Unixタイムスタンプ → 日付",
        "ph_ts_input": "例: 1700000000 または 1700000000000",
        "btn_convert_ts": "変換",
        "btn_use_now": "現在時刻",
        "label_local": "ローカル",
        "label_date_input": "日付 → Unixタイムスタンプ",
        "ph_date_input": "例: 2024-01-15T12:00:00Z または 2024-01-15",
        "btn_convert_date": "変換",
        "label_seconds": "秒",
        "label_ms": "ミリ秒",
        "alert_invalid_ts": "無効なタイムスタンプです。",
        "alert_invalid_date": "無効な日付文字列です。",
        "related_header": "関連ツール",
        "related_date": "日付計算機",
        "related_timer": "タイマー",
        "related_jwt": "JWTデコーダー",
        "howto_header": "使い方",
        "howto_html": '<ol><li>現在のUnix時刻が上部にリアルタイム表示されます — <strong>現在時刻</strong>をクリックすると変換欄に入力できます。</li><li>タイムスタンプを日付に変換するには: 数値を貼り付けて<strong>変換</strong>をクリック。秒(10桁)とミリ秒(13桁)は自動判別されます。</li><li>日付をタイムスタンプに変換するには: ISO 8601(<code>2024-01-15T12:00:00Z</code>)または<code>2024-01-15</code>を入力して<strong>変換</strong>をクリック。</li><li>UTCとローカルタイムゾーンが両方表示されるため、時差計算は不要です。</li></ol><p>Unix時刻は1970-01-01 UTC以降の秒数をカウントし、うるう秒は無視します。32ビット符号付きは2038年にオーバーフローしますが、最新のシステムは64ビットのため影響ありません。</p>',
        "examples_header": "例",
        "examples_html": '<p><strong>タイムスタンプ → 日付:</strong></p><pre><code>1700000000      → 2023-11-14T22:13:20Z (UTC)\n1700000000000   → 2023-11-14T22:13:20.000Z\n0               → 1970-01-01T00:00:00Z (Unix epoch)</code></pre><p><strong>日付 → タイムスタンプ:</strong></p><pre><code>2024-01-15T12:00:00Z → 1705320000  (秒)\n                     → 1705320000000 (ミリ秒)</code></pre>'
    }
}


UUID_GENERATOR = {
    "en": {
        "title": "UUID Generator",
        "meta_title": "UUID Generator (v4 / v1) - Utilify",
        "meta_desc": "Generate RFC 4122 UUIDs (v4 random and v1 time-based) in your browser. Bulk generate 1, 10, or 100 at a time.",
        "json_name": "UUID Generator",
        "json_desc": "Client-side UUID generator supporting v4 (random) and v1 (time-based) variants.",
        "page_desc": "Generate cryptographically random UUIDs locally. v4 (random) is the most common choice; v1 embeds a timestamp. Format options for hyphens, casing, and braces.",
        "label_count": "Count",
        "label_version": "Version",
        "option_nil": "Nil UUID",
        "option_upper": "Uppercase",
        "option_braces": "Wrap in braces",
        "option_nohyphen": "No hyphens",
        "btn_generate": "Generate",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "alert_copy_empty": "Nothing to copy.",
        "related_header": "Related Tools",
        "related_hash": "Hash Generator",
        "related_pw": "Password Generator",
        "related_jwt": "JWT Decoder",
        "howto_header": "How to use",
        "howto_html": '<ol><li>Choose how many UUIDs to generate (1, 10, or 100) and which version.</li><li>Click <strong>Generate</strong> — UUIDs appear in the output box.</li><li>Use the format toggles for uppercase, brace-wrapping (<code>{...}</code>), or hyphen-stripped output.</li><li>Generation uses <code>crypto.randomUUID()</code> when available, falling back to <code>crypto.getRandomValues()</code> with the v4 bit pattern applied.</li></ol><p><strong>v4 vs v1:</strong> v4 is purely random (122 bits of entropy, collision probability essentially zero). v1 embeds a timestamp + clock-seq + node ID, making UUIDs roughly time-ordered — useful for database indexes that benefit from temporal locality. The Nil UUID (<code>00000000-0000-0000-0000-000000000000</code>) is a placeholder value.</p>',
        "examples_header": "Examples",
        "examples_html": '<p><strong>Default v4 (lowercase, hyphenated):</strong></p><pre><code>f47ac10b-58cc-4372-a567-0e02b2c3d479</code></pre><p><strong>v4 with braces, uppercase:</strong></p><pre><code>{F47AC10B-58CC-4372-A567-0E02B2C3D479}</code></pre><p><strong>v1 (time-based):</strong></p><pre><code>3aaa8c0e-9b87-11ee-8c90-0242ac120002</code></pre>'
    },
    "ko": {
        "title": "UUID 생성기",
        "meta_title": "UUID 생성기 (v4 / v1) - Utilify",
        "meta_desc": "RFC 4122 UUID(v4 랜덤 및 v1 시간 기반)를 브라우저에서 생성합니다. 1/10/100개 일괄 생성 지원.",
        "json_name": "UUID 생성기",
        "json_desc": "v4(랜덤)와 v1(시간 기반)을 지원하는 클라이언트 사이드 UUID 생성기.",
        "page_desc": "암호학적으로 안전한 UUID를 로컬에서 생성합니다. v4(랜덤)가 가장 일반적이며, v1은 타임스탬프를 포함합니다. 하이픈/대소문자/중괄호 포맷 옵션을 제공합니다.",
        "label_count": "개수",
        "label_version": "버전",
        "option_nil": "Nil UUID",
        "option_upper": "대문자",
        "option_braces": "중괄호 추가",
        "option_nohyphen": "하이픈 제거",
        "btn_generate": "생성",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "related_header": "관련 도구",
        "related_hash": "해시 생성기",
        "related_pw": "비밀번호 생성기",
        "related_jwt": "JWT 디코더",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>생성할 개수(1/10/100)와 버전을 선택하세요.</li><li><strong>Generate</strong>를 누르면 출력 박스에 UUID가 표시됩니다.</li><li>대문자, 중괄호 감싸기(<code>{...}</code>), 하이픈 제거 등의 포맷 옵션이 있습니다.</li><li><code>crypto.randomUUID()</code>가 가능하면 사용하고, 그렇지 않으면 <code>crypto.getRandomValues()</code>로 v4 비트 패턴을 적용합니다.</li></ol><p><strong>v4와 v1 차이:</strong> v4는 순수 랜덤(엔트로피 122 bit, 충돌 확률 사실상 0). v1은 타임스탬프+clock-seq+노드 ID를 포함해 시간순 정렬에 가깝습니다 — 시간적 지역성으로 이득을 보는 데이터베이스 인덱스에 유용합니다. Nil UUID (<code>00000000-0000-0000-0000-000000000000</code>)는 placeholder 값입니다.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>기본 v4 (소문자, 하이픈):</strong></p><pre><code>f47ac10b-58cc-4372-a567-0e02b2c3d479</code></pre><p><strong>v4 + 중괄호 + 대문자:</strong></p><pre><code>{F47AC10B-58CC-4372-A567-0E02B2C3D479}</code></pre><p><strong>v1 (시간 기반):</strong></p><pre><code>3aaa8c0e-9b87-11ee-8c90-0242ac120002</code></pre>'
    },
    "ja": {
        "title": "UUID生成",
        "meta_title": "UUID生成 (v4 / v1) - Utilify",
        "meta_desc": "RFC 4122 UUID（v4ランダム・v1時刻ベース）をブラウザで生成します。1・10・100件の一括生成に対応。",
        "json_name": "UUID生成",
        "json_desc": "v4（ランダム）とv1（時刻ベース）をサポートするクライアントサイドUUID生成ツール。",
        "page_desc": "暗号学的に安全なUUIDをローカルで生成します。v4（ランダム）が最も一般的です。v1はタイムスタンプを埋め込みます。ハイフン・大文字・波括弧のフォーマットオプションあり。",
        "label_count": "件数",
        "label_version": "バージョン",
        "option_nil": "Nil UUID",
        "option_upper": "大文字",
        "option_braces": "波括弧を付ける",
        "option_nohyphen": "ハイフンなし",
        "btn_generate": "生成",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "alert_copy_empty": "コピーする内容がありません。",
        "related_header": "関連ツール",
        "related_hash": "ハッシュ生成",
        "related_pw": "パスワード生成",
        "related_jwt": "JWTデコーダー",
        "howto_header": "使い方",
        "howto_html": '<ol><li>生成する件数(1・10・100)とバージョンを選びます。</li><li><strong>生成</strong>をクリックすると出力欄にUUIDが表示されます。</li><li>大文字・波括弧(<code>{...}</code>)・ハイフンなしなどのフォーマットオプションが使えます。</li><li>生成には<code>crypto.randomUUID()</code>が利用可能な場合はそれを使い、そうでなければ<code>crypto.getRandomValues()</code>でv4ビットパターンを適用します。</li></ol><p><strong>v4とv1の違い:</strong> v4は純粋なランダム（エントロピー122ビット、衝突確率は実質ゼロ）。v1はタイムスタンプ＋クロックシーケンス＋ノードIDを埋め込み、時刻順に近いUUIDを生成します — 時間的局所性が有利なデータベースインデックスに有用です。Nil UUID (<code>00000000-0000-0000-0000-000000000000</code>)はプレースホルダー値です。</p>',
        "examples_header": "例",
        "examples_html": '<p><strong>デフォルトv4 (小文字、ハイフンあり):</strong></p><pre><code>f47ac10b-58cc-4372-a567-0e02b2c3d479</code></pre><p><strong>v4 + 波括弧 + 大文字:</strong></p><pre><code>{F47AC10B-58CC-4372-A567-0E02B2C3D479}</code></pre><p><strong>v1 (時刻ベース):</strong></p><pre><code>3aaa8c0e-9b87-11ee-8c90-0242ac120002</code></pre>'
    }
}


URL_ENCODER = {
    "en": {
        "title": "URL Encoder / Decoder",
        "meta_title": "URL Encoder & Decoder (Percent Encoding) - Utilify",
        "meta_desc": "Encode and decode URLs and query parameters using percent encoding (RFC 3986). Switch between component and full-URL modes.",
        "json_name": "URL Encoder / Decoder",
        "json_desc": "Bidirectional URL percent-encoding and decoding with component and full-URL modes.",
        "page_desc": "Encode characters into percent-encoded form (e.g. space → %20) or decode them back. Use 'Component' for query values; use 'Full URL' to preserve reserved characters like : / ?.",
        "mode_component": "Component (encodeURIComponent)",
        "mode_full": "Full URL (encodeURI)",
        "label_input": "Input",
        "label_output": "Output",
        "ph_input": "https://example.com/?q=hello world",
        "btn_encode": "Encode",
        "btn_decode": "Decode",
        "btn_swap": "Swap",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "alert_encode_error": "Encode error: ",
        "alert_decode_error": "Decode error: ",
        "alert_copy_empty": "Nothing to copy.",
        "related_header": "Related Tools",
        "related_base64": "Base64 Converter",
        "related_json": "JSON Formatter",
        "related_jwt": "JWT Decoder",
        "howto_header": "How to use",
        "howto_html": '<ol><li>Paste your URL or text into the input panel.</li><li>Pick <strong>Component</strong> mode for query values or path segments — this escapes reserved characters like <code>:/?&amp;=</code>.</li><li>Pick <strong>Full URL</strong> mode when encoding a complete URL — this preserves <code>:/?&amp;=</code> so the URL stays valid.</li><li>Click <strong>Encode</strong> or <strong>Decode</strong>; use <strong>Swap</strong> to flip input/output.</li></ol><p><strong>Component vs Full:</strong> use Component (<code>encodeURIComponent</code>) for anything that goes <em>inside</em> a URL piece — query values, path segments, fragment IDs. Use Full (<code>encodeURI</code>) only when escaping characters in an <em>entire</em> URL where you must keep <code>?</code> and <code>&amp;</code> as separators.</p>',
        "examples_header": "Examples",
        "examples_html": '<p><strong>Component encoding (e.g., for a search query):</strong></p><pre><code>"hello world" → hello%20world\n"a&b=c"       → a%26b%3Dc\n"안녕"         → %EC%95%88%EB%85%95</code></pre><p><strong>Full-URL encoding:</strong></p><pre><code>"https://x.com/?q=hello world"\n→ https://x.com/?q=hello%20world</code></pre>'
    },
    "ko": {
        "title": "URL 인코더 / 디코더",
        "meta_title": "URL 인코더 & 디코더 (Percent Encoding) - Utilify",
        "meta_desc": "URL 및 쿼리 파라미터를 RFC 3986 percent encoding으로 인코딩/디코딩합니다. 컴포넌트/전체 URL 모드 전환 지원.",
        "json_name": "URL 인코더 / 디코더",
        "json_desc": "URL percent-encoding 양방향 변환 도구. 컴포넌트와 전체 URL 모드를 지원합니다.",
        "page_desc": "문자를 percent-encoded 형태(예: 공백 → %20)로 인코딩하거나 다시 디코딩하세요. 쿼리 값은 'Component', 예약 문자(:, /, ?)를 보존해야 한다면 'Full URL' 모드를 사용하세요.",
        "mode_component": "Component (encodeURIComponent)",
        "mode_full": "Full URL (encodeURI)",
        "label_input": "입력",
        "label_output": "출력",
        "ph_input": "https://example.com/?q=hello world",
        "btn_encode": "인코딩",
        "btn_decode": "디코딩",
        "btn_swap": "바꿔치기",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "alert_encode_error": "인코딩 오류: ",
        "alert_decode_error": "디코딩 오류: ",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "related_header": "관련 도구",
        "related_base64": "Base64 변환기",
        "related_json": "JSON 포매터",
        "related_jwt": "JWT 디코더",
        "howto_header": "사용 방법",
        "howto_html": '<ol><li>URL 또는 텍스트를 입력 패널에 붙여넣으세요.</li><li>쿼리 값이나 경로 세그먼트 인코딩에는 <strong>Component</strong> 모드 — <code>:/?&amp;=</code> 같은 예약 문자를 이스케이프합니다.</li><li>완성된 URL 전체를 인코딩할 때는 <strong>Full URL</strong> 모드 — <code>:/?&amp;=</code>를 보존해 URL 형식을 유지합니다.</li><li><strong>Encode</strong>/<strong>Decode</strong>를 누르고, <strong>Swap</strong>으로 입력과 출력을 뒤집을 수 있습니다.</li></ol><p><strong>Component vs Full:</strong> Component(<code>encodeURIComponent</code>)는 URL 안에 들어가는 <em>조각</em>(쿼리 값, 경로 세그먼트, fragment)에 사용합니다. Full(<code>encodeURI</code>)은 <code>?</code>와 <code>&amp;</code>를 구분자로 유지해야 하는 <em>전체 URL</em>을 인코딩할 때만 사용하세요.</p>',
        "examples_header": "예시",
        "examples_html": '<p><strong>Component 인코딩 (검색 쿼리 등):</strong></p><pre><code>"hello world" → hello%20world\n"a&b=c"       → a%26b%3Dc\n"안녕"         → %EC%95%88%EB%85%95</code></pre><p><strong>Full URL 인코딩:</strong></p><pre><code>"https://x.com/?q=hello world"\n→ https://x.com/?q=hello%20world</code></pre>'
    },
    "ja": {
        "title": "URLエンコード / デコード",
        "meta_title": "URLエンコーダー & デコーダー (パーセントエンコーディング) - Utilify",
        "meta_desc": "URLおよびクエリパラメーターをRFC 3986パーセントエンコーディングでエンコード・デコードします。コンポーネントと完全URLモードの切り替えに対応。",
        "json_name": "URLエンコード / デコード",
        "json_desc": "URLパーセントエンコーディングの双方向変換。コンポーネントモードと完全URLモードをサポート。",
        "page_desc": "文字をパーセントエンコード形式（例: スペース → %20）にエンコード、またはデコードします。クエリ値には「Component」、コロン / ？などの予約文字を保持する場合は「Full URL」モードを使用してください。",
        "mode_component": "Component (encodeURIComponent)",
        "mode_full": "Full URL (encodeURI)",
        "label_input": "入力",
        "label_output": "出力",
        "ph_input": "https://example.com/?q=hello world",
        "btn_encode": "エンコード",
        "btn_decode": "デコード",
        "btn_swap": "入れ替え",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "alert_encode_error": "エンコードエラー: ",
        "alert_decode_error": "デコードエラー: ",
        "alert_copy_empty": "コピーする内容がありません。",
        "related_header": "関連ツール",
        "related_base64": "Base64変換",
        "related_json": "JSONフォーマッター",
        "related_jwt": "JWTデコーダー",
        "howto_header": "使い方",
        "howto_html": '<ol><li>URLまたはテキストを入力パネルに貼り付けます。</li><li>クエリ値やパスセグメントのエンコードには<strong>Component</strong>モード — <code>:/?&amp;=</code>などの予約文字をエスケープします。</li><li>URL全体をエンコードする場合は<strong>Full URL</strong>モード — <code>:/?&amp;=</code>を保持してURL形式を維持します。</li><li><strong>エンコード</strong>または<strong>デコード</strong>をクリック、<strong>入れ替え</strong>で入出力を反転できます。</li></ol><p><strong>ComponentとFullの違い:</strong> Component(<code>encodeURIComponent</code>)はURLの一部(クエリ値、パスセグメント、フラグメント)に使います。Full(<code>encodeURI</code>)は<code>?</code>と<code>&amp;</code>を区切り文字として保持する必要がある<em>URL全体</em>のエンコードのみに使用してください。</p>',
        "examples_header": "例",
        "examples_html": '<p><strong>Componentエンコーディング (検索クエリ等):</strong></p><pre><code>"hello world" → hello%20world\n"a&b=c"       → a%26b%3Dc\n"안녕"         → %EC%95%88%EB%85%95</code></pre><p><strong>Full URLエンコーディング:</strong></p><pre><code>"https://x.com/?q=hello world"\n→ https://x.com/?q=hello%20world</code></pre>'
    }
}


ABOUT = {
    "en": {
        "meta_title": "About Utilify - Free Online Developer & Everyday Tools",
        "meta_desc": "Utilify is a free, ad-supported collection of client-side utilities for developers and everyday users. No signup, no upload — everything runs in your browser.",
        "page_h1": "About Utilify",
        "page_body_html": (
            "<p>Utilify is a free collection of online utilities aimed at developers and everyday users. "
            "Every tool runs entirely in your browser — your input never leaves your device.</p>"
            "<h2>Why client-side?</h2>"
            "<p>Most online tools upload your data to a server. We don't. JSON, base64, hashes, JWTs, "
            "image conversions, and PDFs are all processed locally in JavaScript. This is faster, "
            "more private, and works offline once the page is cached.</p>"
            "<h2>How is it free?</h2>"
            "<p>Utilify is supported by display advertising delivered through "
            "<a href=\"https://adsense.google.com/\" rel=\"nofollow noopener\">Google AdSense</a>. "
            "We do not run separate trackers or sell your data.</p>"
            "<h2>Contact</h2>"
            "<p>Questions, bug reports, or suggestions: <a href=\"mailto:contact@utilifyapp.net\">contact@utilifyapp.net</a>.</p>"
        ),
    },
    "ko": {
        "meta_title": "Utilify 소개 - 무료 개발자 & 일상 도구",
        "meta_desc": "Utilify는 개발자와 일반 사용자를 위한 무료 클라이언트 사이드 유틸리티 모음입니다. 가입 없음, 업로드 없음 — 모든 처리가 브라우저에서 이루어집니다.",
        "page_h1": "Utilify 소개",
        "page_body_html": (
            "<p>Utilify는 개발자와 일반 사용자를 위한 무료 온라인 유틸리티 모음입니다. "
            "모든 도구는 브라우저에서만 실행되며 입력 데이터는 절대 기기를 떠나지 않습니다.</p>"
            "<h2>왜 클라이언트 사이드인가?</h2>"
            "<p>대부분의 온라인 도구는 사용자의 데이터를 서버로 전송합니다. Utilify는 그렇지 않습니다. "
            "JSON, Base64, 해시, JWT, 이미지 변환, PDF 모두 JavaScript로 로컬에서 처리됩니다. "
            "더 빠르고, 더 비공개적이며, 페이지 캐시 후에는 오프라인에서도 작동합니다.</p>"
            "<h2>어떻게 무료인가요?</h2>"
            "<p>Utilify는 <a href=\"https://adsense.google.com/\" rel=\"nofollow noopener\">Google AdSense</a>를 "
            "통해 디스플레이 광고로 운영됩니다. "
            "별도의 트래커를 운영하지 않으며 사용자 데이터를 판매하지 않습니다.</p>"
            "<h2>연락처</h2>"
            "<p>질문, 버그 제보, 제안: <a href=\"mailto:contact@utilifyapp.net\">contact@utilifyapp.net</a></p>"
        ),
    },
    "ja": {
        "meta_title": "Utilifyについて - 無料オンライン開発者・日常ツール",
        "meta_desc": "Utilifyは開発者と一般ユーザー向けの無料クライアントサイドユーティリティコレクションです。登録不要、アップロード不要 — すべてブラウザで動作します。",
        "page_h1": "Utilifyについて",
        "page_body_html": (
            "<p>Utilifyは開発者と一般ユーザー向けの無料オンラインユーティリティコレクションです。"
            "すべてのツールはブラウザ内でのみ動作し、入力内容がデバイスの外に出ることはありません。</p>"
            "<h2>なぜクライアントサイドなのか</h2>"
            "<p>多くのオンラインツールはデータをサーバーにアップロードします。Utilifyは異なります。"
            "JSON・Base64・ハッシュ・JWT・画像変換・PDFはすべてJavaScriptでローカル処理されます。"
            "より高速でプライバシーに配慮しており、ページがキャッシュされればオフラインでも動作します。</p>"
            "<h2>なぜ無料なのか</h2>"
            "<p>Utilifyは<a href=\"https://adsense.google.com/\" rel=\"nofollow noopener\">Google AdSense</a>による"
            "ディスプレイ広告で運営されています。"
            "独自のトラッカーは使用せず、ユーザーデータを販売することもありません。</p>"
            "<h2>お問い合わせ</h2>"
            "<p>ご質問、バグ報告、ご提案: <a href=\"mailto:contact@utilifyapp.net\">contact@utilifyapp.net</a></p>"
        ),
    }
}


PRIVACY = {
    "en": {
        "meta_title": "Privacy Policy - Utilify",
        "meta_desc": "Utilify privacy policy. We process all utility input client-side; no data is uploaded. Cookies are used only for ad delivery via Google AdSense.",
        "page_h1": "Privacy Policy",
        "page_body_html": (
            "<p><em>Last updated: 2025-05</em></p>"
            "<h2>1. Data we don't collect</h2>"
            "<p>Every tool on Utilify (JSON formatter, base64 converter, JWT decoder, hash generator, "
            "image converter, PDF tools, etc.) processes your input entirely in the browser. We do "
            "not upload, store, or read the content you paste, type, or upload.</p>"
            "<h2>2. Cookies & advertising</h2>"
            "<p>Utilify is monetized through display advertising delivered by "
            "<a href=\"https://adsense.google.com/\" rel=\"nofollow noopener\">Google AdSense</a>. "
            "Google and its partners may set cookies to personalize ads and measure performance. "
            "You can review and adjust how Google personalizes ads at "
            "<a href=\"https://adssettings.google.com/\" rel=\"nofollow noopener\">adssettings.google.com</a>, "
            "and read Google's full advertising privacy notice at "
            "<a href=\"https://policies.google.com/technologies/ads\" rel=\"nofollow noopener\">policies.google.com/technologies/ads</a>.</p>"
            "<h2>3. Logs</h2>"
            "<p>Our hosting provider (GitHub Pages) keeps short-lived access logs containing IP "
            "addresses for abuse prevention. We do not access or correlate these logs with any "
            "user identity.</p>"
            "<h2>4. PWA / offline</h2>"
            "<p>Installing Utilify as a Progressive Web App caches static assets for offline use. "
            "No personal data is stored.</p>"
            "<h2>5. Your rights (GDPR / CCPA)</h2>"
            "<p>You can manage Google's ad personalization, including opting out, at "
            "<a href=\"https://adssettings.google.com/\" rel=\"nofollow noopener\">adssettings.google.com</a>. "
            "For data Google holds about you, see "
            "<a href=\"https://myaccount.google.com/data-and-privacy\" rel=\"nofollow noopener\">your Google account privacy controls</a>. "
            "Because Utilify itself does not store user data, any request directed to us will be "
            "forwarded to Google as the relevant ad partner.</p>"
            "<h2>6. Changes</h2>"
            "<p>Updates to this policy will be posted on this page with a new \"Last updated\" date.</p>"
        ),
    },
    "ko": {
        "meta_title": "개인정보 처리방침 - Utilify",
        "meta_desc": "Utilify 개인정보 처리방침. 모든 도구 입력은 클라이언트에서 처리되며 업로드되지 않습니다. 쿠키는 Google AdSense를 통한 광고 송출에만 사용됩니다.",
        "page_h1": "개인정보 처리방침",
        "page_body_html": (
            "<p><em>최종 업데이트: 2025-05</em></p>"
            "<h2>1. 수집하지 않는 데이터</h2>"
            "<p>Utilify의 모든 도구(JSON 포매터, Base64 변환기, JWT 디코더, 해시 생성기, 이미지 변환기, "
            "PDF 도구 등)는 입력값을 전적으로 브라우저에서 처리합니다. 사용자가 붙여넣거나 입력하거나 "
            "업로드한 콘텐츠를 서버에 업로드하거나 저장하거나 열람하지 않습니다.</p>"
            "<h2>2. 쿠키 및 광고</h2>"
            "<p>Utilify는 <a href=\"https://adsense.google.com/\" rel=\"nofollow noopener\">Google AdSense</a>를 "
            "통해 디스플레이 광고로 수익을 얻습니다. "
            "Google 및 파트너는 광고 개인화 및 성과 측정을 위해 쿠키를 설정할 수 있습니다. "
            "광고 개인화 설정은 "
            "<a href=\"https://adssettings.google.com/\" rel=\"nofollow noopener\">adssettings.google.com</a>"
            "에서 확인 및 조정할 수 있으며, Google의 광고 개인정보 정책 전문은 "
            "<a href=\"https://policies.google.com/technologies/ads\" rel=\"nofollow noopener\">policies.google.com/technologies/ads</a>"
            "에서 확인하실 수 있습니다.</p>"
            "<h2>3. 로그</h2>"
            "<p>호스팅 제공자(GitHub Pages)는 남용 방지 목적의 단기 액세스 로그(IP 포함)를 보관합니다. "
            "Utilify는 이 로그에 접근하거나 사용자 신원과 연결하지 않습니다.</p>"
            "<h2>4. PWA / 오프라인</h2>"
            "<p>Utilify를 PWA로 설치하면 정적 자산이 캐시되어 오프라인 사용이 가능합니다. "
            "개인정보는 저장되지 않습니다.</p>"
            "<h2>5. 귀하의 권리 (GDPR / CCPA)</h2>"
            "<p>Google의 광고 개인화 설정 및 옵트아웃은 "
            "<a href=\"https://adssettings.google.com/\" rel=\"nofollow noopener\">adssettings.google.com</a>"
            "에서 관리할 수 있습니다. Google이 보유한 사용자 데이터는 "
            "<a href=\"https://myaccount.google.com/data-and-privacy\" rel=\"nofollow noopener\">Google 계정 개인정보 설정</a>"
            "에서 확인할 수 있습니다. Utilify 자체는 사용자 데이터를 저장하지 않으므로 "
            "우리에게 보내는 요청은 광고 파트너인 Google로 전달됩니다.</p>"
            "<h2>6. 변경 사항</h2>"
            "<p>본 방침의 변경은 새로운 \"최종 업데이트\" 날짜와 함께 이 페이지에 게시됩니다.</p>"
        ),
    }
}


TERMS = {
    "en": {
        "meta_title": "Terms of Service - Utilify",
        "meta_desc": "Utilify terms of service. Tools are provided as-is without warranty. You retain responsibility for the content you process.",
        "page_h1": "Terms of Service",
        "page_body_html": (
            "<p><em>Last updated: 2025-05</em></p>"
            "<h2>1. Acceptance</h2>"
            "<p>By using utilifyapp.net you agree to these terms. If you do not agree, do not use the site.</p>"
            "<h2>2. Service description</h2>"
            "<p>Utilify is a free collection of client-side web utilities. Tools execute in your browser; "
            "we do not store, transmit, or process the content you paste or upload on our servers.</p>"
            "<h2>3. No warranty</h2>"
            "<p>The tools are provided <strong>\"AS IS\"</strong> without warranties of any kind, "
            "express or implied. We do not guarantee correctness, fitness for a particular purpose, "
            "availability, or that results are free of defects. Always verify outputs before relying on them.</p>"
            "<h2>4. Your responsibility</h2>"
            "<p>You are solely responsible for the content you input. Do not submit content you are "
            "not authorized to process. We disclaim liability for any loss arising from your use of "
            "the tools, including data loss, decoding errors, or hash collisions.</p>"
            "<h2>5. Acceptable use</h2>"
            "<p>You may not use the site to violate any law, infringe intellectual property, attempt to "
            "compromise the service or its users, or generate ad fraud. Automated bulk scraping may be "
            "rate-limited.</p>"
            "<h2>6. Third-party services</h2>"
            "<p>Ads are delivered by Google AdSense under its own terms. Outbound links are "
            "provided for convenience and do not constitute endorsement.</p>"
            "<h2>7. Changes</h2>"
            "<p>We may update these terms; continued use after changes constitutes acceptance.</p>"
            "<h2>8. Contact</h2>"
            "<p><a href=\"mailto:contact@utilifyapp.net\">contact@utilifyapp.net</a></p>"
        ),
    },
    "ko": {
        "meta_title": "이용약관 - Utilify",
        "meta_desc": "Utilify 이용약관. 모든 도구는 보증 없이 \"있는 그대로\" 제공됩니다. 처리하는 콘텐츠에 대한 책임은 사용자에게 있습니다.",
        "page_h1": "이용약관",
        "page_body_html": (
            "<p><em>최종 업데이트: 2025-05</em></p>"
            "<h2>1. 동의</h2>"
            "<p>utilifyapp.net을 이용함으로써 본 약관에 동의하는 것으로 간주됩니다. 동의하지 않는 경우 사이트를 이용하지 마십시오.</p>"
            "<h2>2. 서비스 설명</h2>"
            "<p>Utilify는 무료 클라이언트 사이드 웹 유틸리티 모음입니다. 모든 도구는 브라우저에서 실행되며, "
            "사용자가 붙여넣거나 업로드한 콘텐츠는 우리 서버에 저장, 전송, 처리되지 않습니다.</p>"
            "<h2>3. 보증 부인</h2>"
            "<p>도구는 <strong>\"있는 그대로(AS IS)\"</strong> 제공되며 명시적이든 묵시적이든 어떠한 보증도 하지 않습니다. "
            "정확성, 특정 목적 적합성, 가용성, 결함 없음을 보장하지 않습니다. 출력에 의존하기 전에 항상 검증하십시오.</p>"
            "<h2>4. 사용자 책임</h2>"
            "<p>입력하는 콘텐츠에 대한 책임은 전적으로 사용자에게 있습니다. 처리 권한이 없는 콘텐츠를 입력하지 마십시오. "
            "도구 사용으로 인한 데이터 손실, 디코딩 오류, 해시 충돌 등 모든 손실에 대해 책임을 지지 않습니다.</p>"
            "<h2>5. 허용되는 사용</h2>"
            "<p>법률 위반, 지식재산권 침해, 서비스 또는 사용자에 대한 공격 시도, 광고 사기 등의 목적으로 본 사이트를 사용할 수 없습니다. "
            "자동화된 대량 스크래핑은 속도 제한될 수 있습니다.</p>"
            "<h2>6. 제3자 서비스</h2>"
            "<p>광고는 Google AdSense 약관에 따라 송출됩니다. 외부 링크는 편의 제공 목적이며 보증을 의미하지 않습니다.</p>"
            "<h2>7. 변경</h2>"
            "<p>본 약관은 변경될 수 있으며 변경 이후 계속 사용하는 것은 동의를 의미합니다.</p>"
            "<h2>8. 연락처</h2>"
            "<p><a href=\"mailto:contact@utilifyapp.net\">contact@utilifyapp.net</a></p>"
        ),
    }
}


NOT_FOUND = {
    "en": {
        "meta_title": "Page Not Found - Utilify",
        "meta_desc": "The page you requested could not be found.",
        "page_h1": "404 — Page Not Found",
        "page_body_html": (
            "<p>Sorry, we couldn't find that page. It may have moved or never existed.</p>"
            "<h2>Popular Tools</h2>"
            "<ul>"
            "<li><a href=\"/en/json-formatter/\">JSON Formatter</a></li>"
            "<li><a href=\"/en/base64-converter/\">Base64 Converter</a></li>"
            "<li><a href=\"/en/unit-converter/\">Unit Converter</a></li>"
            "<li><a href=\"/en/jwt-decoder/\">JWT Decoder</a></li>"
            "<li><a href=\"/en/uuid-generator/\">UUID Generator</a></li>"
            "</ul>"
            "<p><a href=\"/en/\">← Back to home</a></p>"
        ),
    },
    "ko": {
        "meta_title": "페이지를 찾을 수 없음 - Utilify",
        "meta_desc": "요청하신 페이지를 찾을 수 없습니다.",
        "page_h1": "404 — 페이지를 찾을 수 없습니다",
        "page_body_html": (
            "<p>죄송합니다. 해당 페이지를 찾을 수 없습니다. 페이지가 이동되었거나 존재하지 않을 수 있습니다.</p>"
            "<h2>인기 도구</h2>"
            "<ul>"
            "<li><a href=\"/ko/json-formatter/\">JSON 포매터</a></li>"
            "<li><a href=\"/ko/base64-converter/\">Base64 변환기</a></li>"
            "<li><a href=\"/ko/unit-converter/\">단위 변환기</a></li>"
            "<li><a href=\"/ko/jwt-decoder/\">JWT 디코더</a></li>"
            "<li><a href=\"/ko/uuid-generator/\">UUID 생성기</a></li>"
            "</ul>"
            "<p><a href=\"/ko/\">← 홈으로</a></p>"
        ),
    },
    "ja": {
        "meta_title": "ページが見つかりません - Utilify",
        "meta_desc": "お探しのページが見つかりませんでした。",
        "page_h1": "404 — ページが見つかりません",
        "page_body_html": (
            "<p>申し訳ありません。そのページは見つかりませんでした。移動したか、存在しない可能性があります。</p>"
            "<h2>人気ツール</h2>"
            "<ul>"
            "<li><a href=\"/ja/json-formatter/\">JSONフォーマッター</a></li>"
            "<li><a href=\"/ja/base64-converter/\">Base64変換</a></li>"
            "<li><a href=\"/ja/unit-converter/\">単位変換</a></li>"
            "<li><a href=\"/ja/jwt-decoder/\">JWTデコーダー</a></li>"
            "<li><a href=\"/ja/uuid-generator/\">UUID生成</a></li>"
            "</ul>"
            "<p><a href=\"/ja/\">← ホームに戻る</a></p>"
        ),
    }
}



PROMPT_PII_SCRUBBER = {
    "en": {
        "title": "Prompt PII Scrubber",
        "meta_title": "Prompt PII Scrubber — Safely Paste into ChatGPT / Claude - Utilify",
        "meta_desc": "Mask emails, phone numbers, SSNs, credit cards, API keys, and IPs in your text before pasting it into AI chatbots. Runs entirely in your browser.",
        "json_name": "Prompt PII Scrubber",
        "json_desc": "Client-side regex sweep that masks PII in text destined for AI chatbots.",
        "page_desc": "Mask sensitive data (emails, phones, SSNs, credit cards, API keys, IPs, URLs) before pasting prompts into ChatGPT, Claude, or any AI service. Runs entirely in your browser — your text never leaves the page.",
        "label_input": "Original text",
        "label_output": "Scrubbed text",
        "ph_input": "Paste text containing PII (emails, phones, etc.)...",
        "btn_scrub": "Scrub",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "summary_label": "Masked items:",
        "opt_email": "Email",
        "opt_phone": "Phone",
        "opt_ssn": "SSN / RRN",
        "opt_card": "Credit card",
        "opt_apikey": "API key",
        "opt_ip": "IP address",
        "opt_url": "URL",
        "alert_no_pii": "No PII detected.",
        "alert_copy_empty": "Nothing to copy.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Paste the prompt or document you want to send to an AI service.</li>"
            "<li>Toggle the categories you want to mask (default: all on).</li>"
            "<li>Click <strong>Scrub</strong>; the right panel shows the masked version with placeholders like <code>[EMAIL]</code>, <code>[PHONE]</code>, etc.</li>"
            "<li>Copy the scrubbed text and paste it into ChatGPT, Claude, Gemini, etc.</li>"
            "</ol>"
            "<p><strong>What is detected</strong>: standard email addresses; phone numbers in common international formats; US SSN and Korean RRN (주민등록번호); credit-card-like number sequences validated with the Luhn algorithm to avoid false positives; API keys matching well-known prefixes (<code>sk-</code>, <code>pk-</code>, <code>AKIA</code>, <code>AIza</code>, <code>github_pat_</code>, <code>xoxb-</code>); IPv4 addresses; and any HTTP(S) URL.</p>"
            "<p>Heuristic limits: free-text addresses, names, and proprietary IDs are <em>not</em> detected. Always review the scrubbed output before sending.</p>"
        ),
        "related_header": "Related Tools",
        "related_token": "Token Counter",
        "related_claude": "Claude.md Generator",
        "related_mcp": "MCP Config Generator",
        "card_blurb": "Mask emails, phones, cards, API keys before pasting into ChatGPT or Claude."
    },
    "ko": {
        "title": "프롬프트 PII 마스킹",
        "meta_title": "프롬프트 PII 마스킹 — ChatGPT/Claude에 안전하게 붙여넣기 - Utilify",
        "meta_desc": "ChatGPT·Claude·Gemini에 텍스트를 붙여넣기 전 이메일·전화·주민번호·카드·API 키·IP를 자동 마스킹. 모든 처리는 브라우저에서.",
        "json_name": "프롬프트 PII 마스킹",
        "json_desc": "AI 챗봇으로 보낼 텍스트의 개인정보를 정규식으로 마스킹하는 클라이언트 사이드 도구.",
        "page_desc": "ChatGPT·Claude·Gemini 등에 프롬프트를 붙여넣기 전 민감 정보(이메일·전화·주민번호·카드·API 키·IP·URL)를 자동 마스킹. 모든 처리는 브라우저에서 이루어집니다.",
        "label_input": "원본 텍스트",
        "label_output": "마스킹된 텍스트",
        "ph_input": "PII가 포함된 텍스트를 붙여넣으세요 (이메일·전화 등)...",
        "btn_scrub": "마스킹",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "summary_label": "마스킹된 항목:",
        "opt_email": "이메일",
        "opt_phone": "전화번호",
        "opt_ssn": "주민번호 / SSN",
        "opt_card": "카드번호",
        "opt_apikey": "API 키",
        "opt_ip": "IP 주소",
        "opt_url": "URL",
        "alert_no_pii": "PII가 감지되지 않았습니다.",
        "alert_copy_empty": "복사할 내용이 없습니다.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>AI에 보낼 프롬프트 또는 문서를 붙여넣으세요.</li>"
            "<li>마스킹할 카테고리를 선택합니다 (기본: 전부 활성).</li>"
            "<li><strong>마스킹</strong>을 누르면 오른쪽에 <code>[EMAIL]</code>, <code>[PHONE]</code> 등의 자리표시자로 치환된 결과가 표시됩니다.</li>"
            "<li>마스킹된 텍스트를 복사해 ChatGPT·Claude·Gemini 등에 붙여넣으세요.</li>"
            "</ol>"
            "<p><strong>감지되는 항목</strong>: 일반 이메일; 국제 표준 전화번호; 한국 주민등록번호와 미국 SSN; Luhn 검증을 통과한 신용카드 번호; 잘 알려진 접두사(<code>sk-</code>, <code>pk-</code>, <code>AKIA</code>, <code>AIza</code>, <code>github_pat_</code>, <code>xoxb-</code>)의 API 키; IPv4 주소; HTTP(S) URL.</p>"
            "<p>한계: 자유 형식 주소, 이름, 독자 ID는 감지되지 <em>않습니다</em>. 보내기 전 결과를 반드시 확인하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_token": "토큰 카운터",
        "related_claude": "Claude.md 생성기",
        "related_mcp": "MCP 설정 생성기",
        "card_blurb": "이메일·전화·카드·API 키를 자동 마스킹 후 ChatGPT/Claude에 안전하게 붙여넣기."
    },
    "ja": {
        "title": "プロンプトPIIスクラバー",
        "meta_title": "プロンプトPIIスクラバー — ChatGPT/Claudeに安全に貼り付け - Utilify",
        "meta_desc": "ChatGPT・Claude・GeminiにテキストをペーストするPIIをマスクします。メール・電話・SSN・クレカ・APIキー・IPアドレスに対応。ブラウザ内で処理。",
        "json_name": "プロンプトPIIスクラバー",
        "json_desc": "AIチャットボット向けテキストのPIIを正規表現でマスクするクライアントサイドツール。",
        "page_desc": "ChatGPT・Claude・Geminiなどにプロンプトを貼り付ける前に、機密情報（メール・電話番号・SSN・クレジットカード・APIキー・IPアドレス・URL）をマスクします。すべてブラウザ内で処理されます。",
        "label_input": "元のテキスト",
        "label_output": "スクラブ済みテキスト",
        "ph_input": "PIIを含むテキストを貼り付けてください（メール・電話番号など）...",
        "btn_scrub": "スクラブ",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "summary_label": "マスクされた項目:",
        "opt_email": "メール",
        "opt_phone": "電話番号",
        "opt_ssn": "SSN / マイナンバー",
        "opt_card": "クレジットカード",
        "opt_apikey": "APIキー",
        "opt_ip": "IPアドレス",
        "opt_url": "URL",
        "alert_no_pii": "PIIは検出されませんでした。",
        "alert_copy_empty": "コピーする内容がありません。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>AIサービスに送りたいプロンプトまたはドキュメントを貼り付けます。</li>"
            "<li>マスクするカテゴリーを選択します（デフォルト: すべてオン）。</li>"
            "<li><strong>スクラブ</strong>をクリックすると、右パネルに<code>[EMAIL]</code>・<code>[PHONE]</code>などのプレースホルダーに置換された結果が表示されます。</li>"
            "<li>スクラブ済みテキストをコピーしてChatGPT・Claude・Geminiなどに貼り付けます。</li>"
            "</ol>"
            "<p><strong>検出される項目</strong>: 標準的なメールアドレス、国際形式の電話番号、米国SSNと韓国住民登録番号、Luhnアルゴリズムで検証されたクレジットカード番号、既知のプレフィックス(<code>sk-</code>、<code>pk-</code>、<code>AKIA</code>、<code>AIza</code>、<code>github_pat_</code>、<code>xoxb-</code>)のAPIキー、IPv4アドレス、HTTP(S)のURL。</p>"
            "<p>限界: 自由形式の住所・氏名・独自IDは検出<em>されません</em>。送信前に必ず結果を確認してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_token": "トークンカウンター",
        "related_claude": "Claude.mdジェネレーター",
        "related_mcp": "MCP設定ジェネレーター",
        "card_blurb": "メール・電話・クレカ・APIキーをマスクしてChatGPT/Claudeに安全に貼り付け。"
    }
}


CLAUDE_MD_GEN = {
    "en": {
        "title": "Claude.md Generator",
        "meta_title": "Claude.md / System Prompt Generator - Utilify",
        "meta_desc": "Generate a CLAUDE.md project file from a simple form. Define role, conventions, constraints, and commands; download as Markdown.",
        "json_name": "Claude.md Generator",
        "json_desc": "Form-based generator for Anthropic CLAUDE.md project context files.",
        "page_desc": "Generate a CLAUDE.md (or any AI agent system prompt) from a simple form. Specify the project role, coding conventions, constraints, and commands; copy or download the resulting Markdown.",
        "label_project": "Project name",
        "label_role": "Role / persona",
        "ph_role": "You are a senior backend engineer working on a Python web service.",
        "label_conventions": "Conventions (one per line)",
        "ph_conventions": "Use 4-space indentation\nFollow PEP 8\nWrite type hints on all public functions",
        "label_constraints": "Constraints (one per line)",
        "ph_constraints": "Never modify migrations without explicit approval\nDo not touch the legacy auth module",
        "label_commands": "Common commands",
        "ph_commands": "make test\nruff check .\npython manage.py runserver",
        "btn_generate": "Generate",
        "btn_copy": "Copy",
        "btn_download": "Download .md",
        "btn_clear": "Clear",
        "output_label": "Generated CLAUDE.md",
        "note_intro": "This file is loaded automatically by Claude Code when you open the project.",
        "section_role": "Role",
        "section_conventions": "Conventions",
        "section_constraints": "Constraints",
        "section_commands": "Common commands",
        "alert_copy_empty": "Click Generate first.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Fill in your project name and role description.</li>"
            "<li>List conventions one per line — they become a bulleted list in the output.</li>"
            "<li>List constraints one per line — also bulleted.</li>"
            "<li>Add the common commands you run (test, lint, dev server) — wrapped in a <code>```bash</code> block.</li>"
            "<li>Click <strong>Generate</strong>, review, then <strong>Download .md</strong> to save as <code>CLAUDE.md</code> at your repo root.</li>"
            "</ol>"
            "<p>The same file works as a system prompt for Cursor (<code>.cursorrules</code>), Aider, and any other agent that reads project-level context. For Cursor, just rename the downloaded file.</p>"
        ),
        "related_header": "Related Tools",
        "related_mcp": "MCP Config Generator",
        "related_pii": "Prompt PII Scrubber",
        "related_token": "Token Counter",
        "card_blurb": "Build a CLAUDE.md from a form: role, conventions, constraints, commands."
    },
    "ko": {
        "title": "Claude.md 생성기",
        "meta_title": "Claude.md / 시스템 프롬프트 생성기 - Utilify",
        "meta_desc": "폼 입력만으로 CLAUDE.md 프로젝트 파일을 생성하세요. 역할·규칙·제약·명령어를 입력하면 Markdown으로 출력.",
        "json_name": "Claude.md 생성기",
        "json_desc": "Anthropic CLAUDE.md 프로젝트 컨텍스트 파일을 폼 기반으로 생성하는 도구.",
        "page_desc": "간단한 폼으로 CLAUDE.md(또는 AI 에이전트 시스템 프롬프트)를 생성합니다. 프로젝트 역할·코딩 규칙·제약·명령어를 입력하고 Markdown으로 복사하거나 다운로드하세요.",
        "label_project": "프로젝트 이름",
        "label_role": "역할 / 페르소나",
        "ph_role": "Python 웹 서비스를 담당하는 시니어 백엔드 엔지니어입니다.",
        "label_conventions": "코딩 규칙 (한 줄에 하나)",
        "ph_conventions": "4-space 들여쓰기 사용\nPEP 8 준수\n공개 함수에 타입 힌트 작성",
        "label_constraints": "제약 사항 (한 줄에 하나)",
        "ph_constraints": "마이그레이션은 명시 승인 없이 수정 금지\n레거시 인증 모듈 건드리지 말 것",
        "label_commands": "자주 쓰는 명령어",
        "ph_commands": "make test\nruff check .\npython manage.py runserver",
        "btn_generate": "생성",
        "btn_copy": "복사",
        "btn_download": ".md 다운로드",
        "btn_clear": "지우기",
        "output_label": "생성된 CLAUDE.md",
        "note_intro": "이 파일은 Claude Code가 프로젝트를 열 때 자동으로 로드합니다.",
        "section_role": "역할",
        "section_conventions": "규칙",
        "section_constraints": "제약",
        "section_commands": "자주 쓰는 명령어",
        "alert_copy_empty": "먼저 생성을 눌러주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>프로젝트 이름과 역할 설명을 입력하세요.</li>"
            "<li>코딩 규칙은 한 줄에 하나씩 — 출력에서 bullet 리스트로 변환됩니다.</li>"
            "<li>제약 사항도 한 줄에 하나씩.</li>"
            "<li>자주 쓰는 명령어(테스트·린트·개발 서버 등)를 입력 — <code>```bash</code> 블록으로 감싸집니다.</li>"
            "<li><strong>생성</strong>을 눌러 검토 후 <strong>.md 다운로드</strong>로 저장하면 레포 루트의 <code>CLAUDE.md</code>로 사용할 수 있습니다.</li>"
            "</ol>"
            "<p>같은 파일은 Cursor(<code>.cursorrules</code>), Aider 등 다른 에이전트의 시스템 프롬프트로도 사용 가능합니다. Cursor는 다운로드한 파일 이름만 바꾸면 됩니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_mcp": "MCP 설정 생성기",
        "related_pii": "프롬프트 PII 마스킹",
        "related_token": "토큰 카운터",
        "card_blurb": "역할·규칙·제약·명령어 폼 입력 → CLAUDE.md 즉시 생성."
    },
    "ja": {
        "title": "Claude.mdジェネレーター",
        "meta_title": "Claude.md / システムプロンプトジェネレーター - Utilify",
        "meta_desc": "シンプルなフォームからCLAUDE.mdプロジェクトファイルを生成します。役割・規約・制約・コマンドを入力してMarkdownでダウンロード。",
        "json_name": "Claude.mdジェネレーター",
        "json_desc": "Anthropic CLAUDE.mdプロジェクトコンテキストファイルをフォーム入力で生成するツール。",
        "page_desc": "シンプルなフォームからCLAUDE.md（またはAIエージェントのシステムプロンプト）を生成します。プロジェクトの役割・コーディング規約・制約・コマンドを入力して、Markdownとしてコピーまたはダウンロードできます。",
        "label_project": "プロジェクト名",
        "label_role": "役割 / ペルソナ",
        "ph_role": "Pythonウェブサービスを担当するシニアバックエンドエンジニアです。",
        "label_conventions": "規約 (1行に1つ)",
        "ph_conventions": "4スペースインデントを使用\nPEP 8に準拠\nすべての公開関数に型ヒントを記述",
        "label_constraints": "制約 (1行に1つ)",
        "ph_constraints": "明示的な承認なしにマイグレーションを変更しない\nレガシー認証モジュールには触れない",
        "label_commands": "よく使うコマンド",
        "ph_commands": "make test\nruff check .\npython manage.py runserver",
        "btn_generate": "生成",
        "btn_copy": "コピー",
        "btn_download": ".mdをダウンロード",
        "btn_clear": "クリア",
        "output_label": "生成されたCLAUDE.md",
        "note_intro": "このファイルはClaude Codeがプロジェクトを開くと自動的に読み込まれます。",
        "section_role": "役割",
        "section_conventions": "規約",
        "section_constraints": "制約",
        "section_commands": "よく使うコマンド",
        "alert_copy_empty": "先に生成をクリックしてください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>プロジェクト名と役割の説明を入力します。</li>"
            "<li>規約は1行に1つ — 出力ではbulletリストになります。</li>"
            "<li>制約も1行に1つ。</li>"
            "<li>よく使うコマンド（テスト・lint・開発サーバーなど）を入力 — <code>```bash</code>ブロックで囲まれます。</li>"
            "<li><strong>生成</strong>をクリックして確認後、<strong>.mdをダウンロード</strong>でリポジトリルートの<code>CLAUDE.md</code>として保存できます。</li>"
            "</ol>"
            "<p>同じファイルはCursor(<code>.cursorrules</code>)・Aiderなど他のエージェントのシステムプロンプトとしても使えます。Cursorではダウンロードしたファイルの名前を変更するだけです。</p>"
        ),
        "related_header": "関連ツール",
        "related_mcp": "MCP設定ジェネレーター",
        "related_pii": "プロンプトPIIスクラバー",
        "related_token": "トークンカウンター",
        "card_blurb": "役割・規約・制約・コマンドをフォーム入力 → CLAUDE.mdを即生成。"
    }
}


MCP_CONFIG_GEN = {
    "en": {
        "title": "MCP Server Config Generator",
        "meta_title": "MCP Server Config Generator (Claude Desktop / Cursor / VS Code) - Utilify",
        "meta_desc": "Generate MCP server config JSON for Claude Desktop, Cursor, and VS Code. Pick transport, command, args, env in the right format for each client.",
        "json_name": "MCP Config Generator",
        "json_desc": "Form-based generator for Model Context Protocol server configurations.",
        "page_desc": "Generate Model Context Protocol (MCP) server configuration for Claude Desktop, Cursor, or VS Code. Pick transport, command, args, and env vars — the tool emits the correct JSON shape for each client and shows the config file path.",
        "label_target": "Target client",
        "label_name": "Server name",
        "label_transport": "Transport",
        "label_command": "Command",
        "label_args": "Args (one per line)",
        "label_url": "Server URL",
        "label_env": "Environment vars (KEY=value, one per line)",
        "btn_generate": "Generate",
        "btn_copy": "Copy",
        "btn_clear": "Clear",
        "output_label": "Config JSON",
        "install_label": "Install path:",
        "alert_copy_empty": "Click Generate first.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick the client (Claude Desktop, Cursor, or VS Code).</li>"
            "<li>Set the server name (used as the dictionary key).</li>"
            "<li>Pick transport: <code>stdio</code> for local processes (most common), <code>streamable-http</code> or <code>sse</code> for remote servers.</li>"
            "<li>For stdio: enter the command and args; for HTTP/SSE: enter the URL.</li>"
            "<li>Optionally add environment variables.</li>"
            "<li>Click <strong>Generate</strong>; copy the JSON into the config file at the path shown.</li>"
            "</ol>"
            "<p><strong>Where the config goes</strong>:<br>"
            "<code>Claude Desktop</code> — macOS: <code>~/Library/Application Support/Claude/claude_desktop_config.json</code>; Windows: <code>%APPDATA%\\Claude\\claude_desktop_config.json</code><br>"
            "<code>Cursor</code> — global: <code>~/.cursor/mcp.json</code>; per-project: <code>.cursor/mcp.json</code><br>"
            "<code>VS Code</code> — workspace: <code>.vscode/mcp.json</code> (or User Settings → MCP Servers)</p>"
        ),
        "related_header": "Related Tools",
        "related_claude": "Claude.md Generator",
        "related_json": "JSON Formatter",
        "related_pii": "Prompt PII Scrubber",
        "card_blurb": "Generate MCP server JSON for Claude Desktop, Cursor, or VS Code in seconds."
    },
    "ko": {
        "title": "MCP 서버 설정 생성기",
        "meta_title": "MCP 서버 설정 생성기 (Claude Desktop / Cursor / VS Code) - Utilify",
        "meta_desc": "Claude Desktop·Cursor·VS Code용 Model Context Protocol 서버 설정 JSON을 폼으로 생성. transport·command·args·env를 입력하면 클라이언트별 올바른 JSON과 경로를 출력.",
        "json_name": "MCP 설정 생성기",
        "json_desc": "Model Context Protocol 서버 설정을 폼 기반으로 생성하는 도구.",
        "page_desc": "Claude Desktop·Cursor·VS Code용 Model Context Protocol(MCP) 서버 설정을 생성합니다. transport·command·args·env 입력 → 클라이언트별 올바른 JSON 포맷과 설치 경로를 자동 출력.",
        "label_target": "대상 클라이언트",
        "label_name": "서버 이름",
        "label_transport": "Transport",
        "label_command": "Command",
        "label_args": "Args (한 줄에 하나)",
        "label_url": "서버 URL",
        "label_env": "환경 변수 (KEY=value, 한 줄에 하나)",
        "btn_generate": "생성",
        "btn_copy": "복사",
        "btn_clear": "지우기",
        "output_label": "설정 JSON",
        "install_label": "설치 경로:",
        "alert_copy_empty": "먼저 생성을 눌러주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>대상 클라이언트(Claude Desktop·Cursor·VS Code)를 선택하세요.</li>"
            "<li>서버 이름(dict 키로 사용됩니다)을 입력합니다.</li>"
            "<li>transport 선택: <code>stdio</code>는 로컬 프로세스(가장 일반적), <code>streamable-http</code>·<code>sse</code>는 원격 서버용.</li>"
            "<li>stdio: command와 args 입력 / HTTP·SSE: URL 입력.</li>"
            "<li>필요시 환경 변수 추가.</li>"
            "<li><strong>생성</strong> 후 표시된 경로의 설정 파일에 JSON을 복사하세요.</li>"
            "</ol>"
            "<p><strong>설정 파일 경로</strong>:<br>"
            "<code>Claude Desktop</code> — macOS: <code>~/Library/Application Support/Claude/claude_desktop_config.json</code>; Windows: <code>%APPDATA%\\Claude\\claude_desktop_config.json</code><br>"
            "<code>Cursor</code> — 전역: <code>~/.cursor/mcp.json</code>; 프로젝트별: <code>.cursor/mcp.json</code><br>"
            "<code>VS Code</code> — 워크스페이스: <code>.vscode/mcp.json</code> (또는 User Settings → MCP Servers)</p>"
        ),
        "related_header": "관련 도구",
        "related_claude": "Claude.md 생성기",
        "related_json": "JSON 포매터",
        "related_pii": "프롬프트 PII 마스킹",
        "card_blurb": "Claude Desktop·Cursor·VS Code용 MCP 서버 JSON을 즉시 생성."
    },
    "ja": {
        "title": "MCPサーバー設定ジェネレーター",
        "meta_title": "MCPサーバー設定ジェネレーター (Claude Desktop / Cursor / VS Code) - Utilify",
        "meta_desc": "Claude Desktop・Cursor・VS Code用のMCPサーバー設定JSONをフォームで生成します。トランスポート・コマンド・引数・環境変数を入力するだけ。",
        "json_name": "MCP設定ジェネレーター",
        "json_desc": "Model Context Protocolサーバー設定をフォーム入力で生成するツール。",
        "page_desc": "Claude Desktop・Cursor・VS Code向けのModel Context Protocol（MCP）サーバー設定を生成します。トランスポート・コマンド・引数・環境変数を入力すると、各クライアントに対応した正しいJSONと設定ファイルのパスを出力します。",
        "label_target": "対象クライアント",
        "label_name": "サーバー名",
        "label_transport": "トランスポート",
        "label_command": "コマンド",
        "label_args": "引数 (1行に1つ)",
        "label_url": "サーバーURL",
        "label_env": "環境変数 (KEY=value、1行に1つ)",
        "btn_generate": "生成",
        "btn_copy": "コピー",
        "btn_clear": "クリア",
        "output_label": "設定JSON",
        "install_label": "インストールパス:",
        "alert_copy_empty": "先に生成をクリックしてください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>クライアント（Claude Desktop・Cursor・VS Code）を選びます。</li>"
            "<li>サーバー名（辞書のキーとして使用）を入力します。</li>"
            "<li>トランスポートを選択: <code>stdio</code>はローカルプロセス（最も一般的）、<code>streamable-http</code>・<code>sse</code>はリモートサーバー向け。</li>"
            "<li>stdioの場合: コマンドと引数を入力 / HTTP・SSEの場合: URLを入力。</li>"
            "<li>必要に応じて環境変数を追加。</li>"
            "<li><strong>生成</strong>後、表示されたパスの設定ファイルにJSONをコピーします。</li>"
            "</ol>"
            "<p><strong>設定ファイルの場所</strong>:<br>"
            "<code>Claude Desktop</code> — macOS: <code>~/Library/Application Support/Claude/claude_desktop_config.json</code>; Windows: <code>%APPDATA%\\Claude\\claude_desktop_config.json</code><br>"
            "<code>Cursor</code> — グローバル: <code>~/.cursor/mcp.json</code>; プロジェクト別: <code>.cursor/mcp.json</code><br>"
            "<code>VS Code</code> — ワークスペース: <code>.vscode/mcp.json</code> (またはユーザー設定 → MCP Servers)</p>"
        ),
        "related_header": "関連ツール",
        "related_claude": "Claude.mdジェネレーター",
        "related_json": "JSONフォーマッター",
        "related_pii": "プロンプトPIIスクラバー",
        "card_blurb": "Claude Desktop・Cursor・VS Code用のMCPサーバーJSONを即生成。"
    }
}


TOKEN_COUNTER = {
    "en": {
        "title": "AI Token Counter & Cost Calculator",
        "meta_title": "GPT / Claude / Gemini Token Counter & Cost Calculator - Utilify",
        "meta_desc": "Estimate token count and per-model API cost (GPT-4o, Claude Opus, Gemini 2.5) for any text. Free, no signup, runs entirely in your browser.",
        "json_name": "AI Token Counter",
        "json_desc": "Estimate tokens and per-model API cost for OpenAI, Anthropic, and Google models.",
        "page_desc": "Estimate the token count of any text and the per-model API cost across GPT-4o, Claude Opus 4.7, Gemini 2.5, and more. Heuristic count (≈4 chars/token English, ≈1.5 chars/token CJK) — exact tokenization needs the provider API.",
        "label_input": "Text",
        "ph_input": "Paste your prompt or document here...",
        "stat_chars": "Characters",
        "stat_words": "Words",
        "stat_tokens": "Est. tokens",
        "stat_lines": "Lines",
        "label_out_tokens": "Estimated output tokens",
        "note_estimate": "(used for output cost column)",
        "cost_table_title": "Cost per model",
        "col_model": "Model",
        "col_input_price": "Input $/1M",
        "col_output_price": "Output $/1M",
        "col_input_cost": "Input cost",
        "col_output_cost": "Output cost",
        "col_total": "Total",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Paste the prompt, document, or transcript you want to estimate.</li>"
            "<li>The character/word/token/line counts update live.</li>"
            "<li>Adjust the <strong>estimated output tokens</strong> if you expect a long response (default 500).</li>"
            "<li>The cost table shows input cost, output cost, and total per popular model.</li>"
            "</ol>"
            "<p><strong>Token counting accuracy</strong>: this tool uses a fast character-based heuristic that detects CJK characters (Korean, Japanese, Chinese) and adjusts the chars-per-token ratio. Real BPE tokenization (cl100k_base, o200k_base, etc.) requires the provider API or a 1-3MB vocabulary download. For cost estimation purposes the heuristic is typically within ±10% of the exact count.</p>"
            "<p><strong>Pricing</strong>: based on publicly listed per-million-token prices as of 2026-05. Always check the provider's pricing page before billing-critical decisions.</p>"
        ),
        "related_header": "Related Tools",
        "related_pii": "Prompt PII Scrubber",
        "related_claude": "Claude.md Generator",
        "related_mcp": "MCP Config Generator",
        "card_blurb": "Estimate tokens & per-model API cost (GPT-4o, Claude, Gemini) for any text."
    },
    "ko": {
        "title": "AI 토큰 카운터 & 비용 계산기",
        "meta_title": "GPT / Claude / Gemini 토큰 카운터 & 비용 계산기 - Utilify",
        "meta_desc": "임의의 텍스트로 토큰 수와 모델별 API 비용(GPT-4o·Claude Opus·Gemini 2.5 등)을 추정. 무료, 가입 불필요, 브라우저에서 동작.",
        "json_name": "AI 토큰 카운터",
        "json_desc": "OpenAI·Anthropic·Google 모델의 토큰 수와 API 비용을 추정합니다.",
        "page_desc": "텍스트의 토큰 수를 추정하고 GPT-4o·Claude Opus 4.7·Gemini 2.5 등 모델별 API 비용을 표시합니다. 휴리스틱(영문 ≈4자/토큰, CJK ≈1.5자/토큰) 기반 — 정확한 토큰화는 제공자 API가 필요합니다.",
        "label_input": "텍스트",
        "ph_input": "프롬프트 또는 문서를 붙여넣으세요...",
        "stat_chars": "문자 수",
        "stat_words": "단어 수",
        "stat_tokens": "추정 토큰",
        "stat_lines": "줄 수",
        "label_out_tokens": "예상 출력 토큰",
        "note_estimate": "(출력 비용 계산에 사용)",
        "cost_table_title": "모델별 비용",
        "col_model": "모델",
        "col_input_price": "입력 $/1M",
        "col_output_price": "출력 $/1M",
        "col_input_cost": "입력 비용",
        "col_output_cost": "출력 비용",
        "col_total": "합계",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>비용을 추정할 프롬프트·문서·트랜스크립트를 붙여넣으세요.</li>"
            "<li>문자/단어/토큰/줄 수가 실시간으로 갱신됩니다.</li>"
            "<li>긴 응답이 예상되면 <strong>예상 출력 토큰</strong>을 조정하세요 (기본 500).</li>"
            "<li>비용 표에 인기 모델별 입력·출력·합계 비용이 표시됩니다.</li>"
            "</ol>"
            "<p><strong>토큰 정확도</strong>: 한글·일본어·중국어 비율을 감지해 chars-per-token 비율을 조정하는 빠른 휴리스틱입니다. 정확한 BPE 토큰화(cl100k_base, o200k_base 등)는 제공자 API 또는 1-3MB의 사전 다운로드가 필요합니다. 비용 추정 목적에는 일반적으로 정확값 ±10% 이내입니다.</p>"
            "<p><strong>가격</strong>: 2026년 5월 기준 공개된 1M 토큰당 가격. 정산이 중요한 결정 전에는 반드시 제공자의 공식 가격 페이지를 확인하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_pii": "프롬프트 PII 마스킹",
        "related_claude": "Claude.md 생성기",
        "related_mcp": "MCP 설정 생성기",
        "card_blurb": "텍스트의 토큰 수와 모델별 API 비용을 즉시 추정 (GPT/Claude/Gemini)."
    },
    "ja": {
        "title": "AIトークンカウンター & コスト計算機",
        "meta_title": "GPT / Claude / Gemini トークンカウンター & コスト計算機 - Utilify",
        "meta_desc": "任意のテキストのトークン数とモデル別APIコスト（GPT-4o・Claude Opus・Gemini 2.5）を推定します。無料、登録不要、ブラウザで動作。",
        "json_name": "AIトークンカウンター",
        "json_desc": "OpenAI・Anthropic・GoogleモデルのトークンとAPIコストを推定します。",
        "page_desc": "テキストのトークン数とGPT-4o・Claude Opus 4.7・Gemini 2.5などのモデル別APIコストを推定します。ヒューリスティック計算（英語≈4文字/トークン、CJK≈1.5文字/トークン）— 正確なトークン化にはプロバイダーAPIが必要です。",
        "label_input": "テキスト",
        "ph_input": "プロンプトまたはドキュメントをここに貼り付けてください...",
        "stat_chars": "文字数",
        "stat_words": "単語数",
        "stat_tokens": "推定トークン",
        "stat_lines": "行数",
        "label_out_tokens": "推定出力トークン数",
        "note_estimate": "(出力コスト計算に使用)",
        "cost_table_title": "モデル別コスト",
        "col_model": "モデル",
        "col_input_price": "入力 $/1M",
        "col_output_price": "出力 $/1M",
        "col_input_cost": "入力コスト",
        "col_output_cost": "出力コスト",
        "col_total": "合計",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>コストを推定したいプロンプト・ドキュメント・トランスクリプトを貼り付けます。</li>"
            "<li>文字数・単語数・トークン数・行数がリアルタイムで更新されます。</li>"
            "<li>長い応答が予想される場合は<strong>推定出力トークン数</strong>を調整してください（デフォルト500）。</li>"
            "<li>コスト表に主要モデルごとの入力・出力・合計コストが表示されます。</li>"
            "</ol>"
            "<p><strong>トークン計算の精度</strong>: CJK文字（日本語・韓国語・中国語）を検出して文字/トークン比率を調整する高速なヒューリスティックを使用しています。正確なBPEトークン化（cl100k_base・o200k_baseなど）にはプロバイダーAPIまたは1〜3MBの語彙ダウンロードが必要です。コスト推定目的には通常±10%以内の精度があります。</p>"
            "<p><strong>価格</strong>: 2026年5月時点の公開済み100万トークンあたりの価格に基づきます。請求に関わる重要な判断をする前は必ずプロバイダーの公式価格ページを確認してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_pii": "プロンプトPIIスクラバー",
        "related_claude": "Claude.mdジェネレーター",
        "related_mcp": "MCP設定ジェネレーター",
        "card_blurb": "テキストのトークン数とモデル別APIコストを即推定（GPT/Claude/Gemini）。"
    }
}


AI_IMAGE_INSPECTOR = {
    "en": {
        "title": "AI Image Metadata Inspector",
        "meta_title": "AI Image Inspector — Detect Stable Diffusion / Midjourney / DALL-E - Utilify",
        "meta_desc": "Inspect PNG and JPEG metadata to find AI generation parameters (Stable Diffusion prompts, EXIF UserComment, C2PA Content Credentials). Local file processing only.",
        "json_name": "AI Image Inspector",
        "json_desc": "Reads PNG tEXt/iTXt chunks, JPEG EXIF, and C2PA boxes to surface AI-image fingerprints.",
        "page_desc": "Drop or pick an image to inspect its embedded metadata. The tool reads PNG tEXt/iTXt chunks (Stable Diffusion stores prompts there), JPEG EXIF UserComment (Midjourney/DALL-E often embed details), and detects C2PA Content Credentials boxes. Files never leave your browser.",
        "ph_drop": "Drop a PNG/JPEG/WebP here, or click to choose",
        "section_sd": "Stable Diffusion / generation parameters",
        "section_exif": "EXIF / metadata text",
        "section_raw": "Raw metadata",
        "verdict_ai": "🤖 AI generation signatures detected",
        "verdict_unknown": "🔍 Metadata present but no clear AI signature",
        "verdict_clean": "✅ No metadata found (likely stripped or never embedded)",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Drag-drop or pick a PNG/JPEG/WebP image.</li>"
            "<li>The tool reads PNG ancillary chunks and JPEG APP1 (EXIF) segments locally.</li>"
            "<li>If a Stable Diffusion <code>parameters</code> chunk is found, the prompt and settings appear in the first section.</li>"
            "<li>If EXIF UserComment contains identifying text (e.g., \"Midjourney\", \"Generated by ...\"), it shows in the second section.</li>"
            "<li>C2PA / Content Credentials boxes are flagged when present.</li>"
            "</ol>"
            "<p><strong>What this <em>cannot</em> tell you</strong>: whether an image is AI-generated when metadata has been stripped (most social platforms strip metadata on upload). A \"no metadata\" verdict is not a clean bill of health — many genuinely AI-generated images have no embedded fingerprint after re-saving.</p>"
        ),
        "related_header": "Related Tools",
        "related_imgconv": "Image Converter",
        "related_watermark": "Image Watermark",
        "related_token": "Token Counter",
        "card_blurb": "Detect Stable Diffusion / Midjourney metadata in PNG / JPEG. Files stay local."
    },
    "ko": {
        "title": "AI 이미지 메타데이터 검사기",
        "meta_title": "AI 이미지 검사기 — Stable Diffusion / Midjourney / DALL-E 감지 - Utilify",
        "meta_desc": "PNG/JPEG 메타데이터를 분석해 AI 생성 흔적(Stable Diffusion 프롬프트·EXIF UserComment·C2PA Content Credentials)을 찾습니다. 파일은 브라우저에서만 처리됩니다.",
        "json_name": "AI 이미지 검사기",
        "json_desc": "PNG tEXt/iTXt 청크와 JPEG EXIF, C2PA 박스를 읽어 AI 이미지 흔적을 표시.",
        "page_desc": "이미지를 드롭하거나 선택해 메타데이터를 검사합니다. PNG의 tEXt·iTXt 청크(Stable Diffusion이 프롬프트 저장), JPEG EXIF UserComment(Midjourney·DALL-E가 식별 정보 포함), C2PA Content Credentials 박스 감지. 파일은 브라우저를 벗어나지 않습니다.",
        "ph_drop": "PNG/JPEG/WebP를 드롭하거나 클릭해 선택하세요",
        "section_sd": "Stable Diffusion / 생성 파라미터",
        "section_exif": "EXIF / 메타데이터 텍스트",
        "section_raw": "Raw 메타데이터",
        "verdict_ai": "🤖 AI 생성 시그니처 감지됨",
        "verdict_unknown": "🔍 메타데이터는 있지만 명확한 AI 시그니처 없음",
        "verdict_clean": "✅ 메타데이터 없음 (제거되었거나 처음부터 없었음)",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>PNG·JPEG·WebP를 드래그-드롭하거나 선택하세요.</li>"
            "<li>PNG 보조 청크와 JPEG APP1(EXIF) 세그먼트를 로컬에서 읽습니다.</li>"
            "<li>Stable Diffusion의 <code>parameters</code> 청크가 있으면 프롬프트·설정이 첫 섹션에 표시됩니다.</li>"
            "<li>EXIF UserComment에 식별 텍스트(\"Midjourney\", \"Generated by ...\")가 있으면 두 번째 섹션에 표시됩니다.</li>"
            "<li>C2PA·Content Credentials 박스가 있으면 표시됩니다.</li>"
            "</ol>"
            "<p><strong>이 도구가 <em>알 수 없는 것</em></strong>: 메타데이터가 제거된 AI 이미지(대부분의 SNS는 업로드 시 메타데이터를 제거함). \"메타데이터 없음\" 결과가 \"AI 아님\"을 보장하지는 않습니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_imgconv": "이미지 변환기",
        "related_watermark": "이미지 워터마크",
        "related_token": "토큰 카운터",
        "card_blurb": "PNG·JPEG에서 Stable Diffusion·Midjourney 메타데이터 감지. 파일은 로컬 처리."
    },
    "ja": {
        "title": "AI画像メタデータインスペクター",
        "meta_title": "AI画像インスペクター — Stable Diffusion / Midjourney / DALL-E検出 - Utilify",
        "meta_desc": "PNGおよびJPEGのメタデータを検査してAI生成パラメーター（Stable Diffusionプロンプト・EXIF UserComment・C2PA Content Credentials）を検出します。ファイルはブラウザ内でのみ処理。",
        "json_name": "AI画像インスペクター",
        "json_desc": "PNG tEXt/iTXtチャンク、JPEG EXIF、C2PAボックスを読み込みAI画像の痕跡を表示します。",
        "page_desc": "画像をドロップまたは選択してメタデータを検査します。PNG tEXt/iTXtチャンク（Stable Diffusionのプロンプト保存先）、JPEG EXIF UserComment（Midjourney/DALL-Eが識別情報を埋め込む）、C2PA Content Credentialsボックスを検出します。ファイルはブラウザ外に出ません。",
        "ph_drop": "PNG/JPEG/WebPをドロップ、またはクリックして選択",
        "section_sd": "Stable Diffusion / 生成パラメーター",
        "section_exif": "EXIF / メタデータテキスト",
        "section_raw": "生のメタデータ",
        "verdict_ai": "🤖 AI生成シグネチャを検出しました",
        "verdict_unknown": "🔍 メタデータはあるが、明確なAIシグネチャなし",
        "verdict_clean": "✅ メタデータなし（削除済みまたは最初から存在しない）",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>PNG/JPEG/WebP画像をドラッグ＆ドロップまたは選択します。</li>"
            "<li>PNGの補助チャンクとJPEGのAPP1（EXIF）セグメントをローカルで読み込みます。</li>"
            "<li>Stable Diffusionの<code>parameters</code>チャンクが見つかった場合、プロンプトと設定が最初のセクションに表示されます。</li>"
            "<li>EXIF UserCommentに識別テキスト（\"Midjourney\"・\"Generated by ...\"）があれば2番目のセクションに表示されます。</li>"
            "<li>C2PA / Content Credentialsボックスが存在する場合はフラグが立ちます。</li>"
            "</ol>"
            "<p><strong>このツールが<em>わからないこと</em></strong>: メタデータが削除されたAI画像（ほとんどのSNSはアップロード時にメタデータを削除します）。「メタデータなし」という結果は「AI生成でない」ことを保証するものではありません。</p>"
        ),
        "related_header": "関連ツール",
        "related_imgconv": "画像変換",
        "related_watermark": "画像透かし",
        "related_token": "トークンカウンター",
        "card_blurb": "PNG/JPEGのStable Diffusion・Midjourneyメタデータを検出。ファイルはローカル処理。"
    }
}


CHATGPT_TO_BLOG = {
    "en": {
        "title": "ChatGPT → Blog Post Converter",
        "meta_title": "ChatGPT Conversation to Blog Post Markdown - Utilify",
        "meta_desc": "Paste a ChatGPT conversation and get clean Markdown ready for your blog. Strips prompts, merges assistant turns, and formats for publishing.",
        "json_name": "ChatGPT to Blog",
        "json_desc": "Convert a pasted ChatGPT conversation into clean blog-ready Markdown.",
        "page_desc": "Paste a ChatGPT (or Claude) conversation — text or exported JSON — and the tool splits it into user/assistant turns, optionally strips your prompts, and formats the assistant responses as clean Markdown ready for your blog.",
        "label_input": "ChatGPT conversation (text or JSON)",
        "label_output": "Markdown",
        "ph_input": "Paste the conversation here. Both 'You said: ...' / 'ChatGPT said: ...' format and the JSON export are accepted.",
        "opt_strip_prompts": "Strip user prompts (assistant only)",
        "opt_merge": "Merge assistant turns into one post",
        "opt_add_title": "Add H1 title",
        "label_title": "Title",
        "btn_convert": "Convert",
        "btn_copy": "Copy",
        "btn_download": "Download .md",
        "btn_clear": "Clear",
        "alert_copy_empty": "Click Convert first.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>In ChatGPT, click the share icon → Copy or Share. You can also export your data and use the JSON file.</li>"
            "<li>Paste the conversation into the left panel.</li>"
            "<li>Toggle the options: <em>Strip user prompts</em> drops your questions; <em>Merge assistant turns</em> joins all answers into one continuous post; <em>Add H1 title</em> prepends a heading.</li>"
            "<li>Click <strong>Convert</strong>; review the Markdown on the right.</li>"
            "<li><strong>Download .md</strong> to save the post locally.</li>"
            "</ol>"
            "<p><strong>What's parsed</strong>: text format with \"You said:\" / \"ChatGPT said:\" labels (also \"User:\" / \"Assistant:\" / Korean \"사용자\" / \"어시스턴트\"); the JSON export shape with <code>mapping</code> nodes; and a generic <code>{messages: [{role, content}]}</code> shape. If no role markers are detected the entire input is treated as a single assistant message.</p>"
        ),
        "related_header": "Related Tools",
        "related_md": "Markdown Previewer",
        "related_token": "Token Counter",
        "related_pii": "Prompt PII Scrubber",
        "card_blurb": "Convert a ChatGPT conversation into clean blog-ready Markdown."
    },
    "ko": {
        "title": "ChatGPT → 블로그 변환기",
        "meta_title": "ChatGPT 대화를 블로그 Markdown으로 변환 - Utilify",
        "meta_desc": "ChatGPT 대화를 붙여넣으면 블로그 게시용 Markdown으로 정리. 프롬프트 제거, assistant 턴 병합, 게시용 포맷.",
        "json_name": "ChatGPT 블로그 변환기",
        "json_desc": "붙여넣은 ChatGPT 대화를 깔끔한 블로그용 Markdown으로 변환합니다.",
        "page_desc": "ChatGPT(또는 Claude) 대화 — 텍스트 또는 JSON export — 를 붙여넣으면 사용자/AI 턴을 분리하고, 프롬프트를 선택적으로 제거하며, AI 응답을 블로그용 Markdown으로 정리합니다.",
        "label_input": "ChatGPT 대화 (텍스트 또는 JSON)",
        "label_output": "Markdown",
        "ph_input": "여기에 대화를 붙여넣으세요. 'You said: ...' / 'ChatGPT said: ...' 형식과 JSON export 모두 지원됩니다.",
        "opt_strip_prompts": "사용자 프롬프트 제거 (AI 답변만)",
        "opt_merge": "AI 턴을 하나의 글로 병합",
        "opt_add_title": "H1 제목 추가",
        "label_title": "제목",
        "btn_convert": "변환",
        "btn_copy": "복사",
        "btn_download": ".md 다운로드",
        "btn_clear": "지우기",
        "alert_copy_empty": "먼저 변환을 눌러주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>ChatGPT에서 공유 아이콘 → Copy 또는 Share. 또는 데이터 export로 JSON 파일을 받으세요.</li>"
            "<li>대화를 왼쪽 패널에 붙여넣으세요.</li>"
            "<li>옵션 선택: <em>사용자 프롬프트 제거</em>는 질문을 빼고, <em>AI 턴 병합</em>은 모든 답변을 하나의 글로 합치며, <em>H1 제목 추가</em>는 제목 헤딩을 앞에 붙입니다.</li>"
            "<li><strong>변환</strong> 후 오른쪽 Markdown을 확인하세요.</li>"
            "<li><strong>.md 다운로드</strong>로 로컬 저장 가능합니다.</li>"
            "</ol>"
            "<p><strong>지원 포맷</strong>: \"You said:\" / \"ChatGPT said:\" 라벨 텍스트 (한글 \"사용자\" / \"어시스턴트\"도 인식); <code>mapping</code> 노드가 있는 JSON export; <code>{messages: [{role, content}]}</code> 일반 형식. 역할 마커가 없으면 입력 전체를 하나의 AI 응답으로 처리합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_md": "Markdown 프리뷰어",
        "related_token": "토큰 카운터",
        "related_pii": "프롬프트 PII 마스킹",
        "card_blurb": "ChatGPT 대화를 깔끔한 블로그용 Markdown으로 즉시 변환."
    },
    "ja": {
        "title": "ChatGPT → ブログ記事変換",
        "meta_title": "ChatGPT会話をブログ記事Markdownに変換 - Utilify",
        "meta_desc": "ChatGPTの会話を貼り付けると、ブログ掲載用のクリーンなMarkdownに変換します。プロンプト削除・アシスタントターンの統合・公開フォーマットに対応。",
        "json_name": "ChatGPTブログ変換",
        "json_desc": "貼り付けたChatGPT会話をブログ用クリーンなMarkdownに変換します。",
        "page_desc": "ChatGPT（またはClaude）の会話 — テキストまたはJSONエクスポート — を貼り付けると、ユーザー/AIのターンを分離し、プロンプトを選択的に削除して、AI応答をブログ用Markdownに整形します。",
        "label_input": "ChatGPT会話（テキストまたはJSON）",
        "label_output": "Markdown",
        "ph_input": "ここに会話を貼り付けてください。'You said: ...' / 'ChatGPT said: ...'形式とJSONエクスポートの両方に対応しています。",
        "opt_strip_prompts": "ユーザープロンプトを削除（AIの返答のみ）",
        "opt_merge": "AIのターンを1つの記事にまとめる",
        "opt_add_title": "H1タイトルを追加",
        "label_title": "タイトル",
        "btn_convert": "変換",
        "btn_copy": "コピー",
        "btn_download": ".mdをダウンロード",
        "btn_clear": "クリア",
        "alert_copy_empty": "先に変換をクリックしてください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>ChatGPTで共有アイコン → コピーまたは共有。またはデータエクスポートでJSONファイルを取得します。</li>"
            "<li>左パネルに会話を貼り付けます。</li>"
            "<li>オプションを選択: <em>ユーザープロンプトを削除</em>で質問を除き、<em>AIターンを統合</em>ですべての回答を1つの記事にまとめ、<em>H1タイトルを追加</em>でヘッディングを先頭に付けます。</li>"
            "<li><strong>変換</strong>後、右のMarkdownを確認します。</li>"
            "<li><strong>.mdをダウンロード</strong>でローカル保存できます。</li>"
            "</ol>"
            "<p><strong>対応フォーマット</strong>: \"You said:\" / \"ChatGPT said:\"ラベルのテキスト（\"User:\" / \"Assistant:\"、韓国語の\"사용자\" / \"어시스턴트\"も認識）; <code>mapping</code>ノードを持つJSONエクスポート; <code>{messages: [{role, content}]}</code>の汎用形式。役割マーカーが検出されない場合は入力全体を1つのAI応答として処理します。</p>"
        ),
        "related_header": "関連ツール",
        "related_md": "Markdownプレビュー",
        "related_token": "トークンカウンター",
        "related_pii": "プロンプトPIIスクラバー",
        "card_blurb": "ChatGPTの会話をブログ用クリーンなMarkdownに即変換。"
    }
}


LOAN_CALCULATOR = {
    "en": {
        "title": "Loan Calculator",
        "meta_title": "Loan Calculator — Monthly Payment, Interest, Amortization - Utilify",
        "meta_desc": "Calculate monthly loan payments, total interest, and amortization schedule. Works for mortgages, auto loans, and personal loans. Runs entirely in your browser.",
        "og_title": "Loan Calculator - Utilify",
        "og_desc": "Calculate monthly payment, total interest, and amortization for any fixed-rate loan.",
        "json_name": "Loan Calculator",
        "json_desc": "Compute monthly payment, total interest, and amortization schedule for fixed-rate loans.",
        "page_desc": "Enter the loan amount, annual interest rate, and term in years to see your monthly payment, total interest paid, and a 12-month amortization preview. Standard formula for fixed-rate loans — mortgages, auto, personal.",
        "label_principal": "Loan amount",
        "label_rate": "Annual interest rate (%)",
        "label_term": "Term (years)",
        "ph_principal": "100000",
        "ph_rate": "4.5",
        "ph_term": "30",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My monthly loan payment is {value} —",
        "share_copied": "Result copied to clipboard.",
        "res_monthly_label": "Monthly payment",
        "res_total_label": "Total paid",
        "res_interest_label": "Total interest",
        "res_schedule_header": "First 12 months",
        "th_month": "Month",
        "th_payment": "Payment",
        "th_principal_col": "Principal",
        "th_interest_col": "Interest",
        "th_balance": "Balance",
        "alert_invalid": "Please enter positive numbers for amount and term.",
        "disclaimer": "Estimate only — not financial advice. Consult a qualified professional for important decisions.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter the loan principal (the amount you borrow).</li>"
            "<li>Enter the annual interest rate as a percent (e.g. 4.5 for 4.5%).</li>"
            "<li>Enter the loan term in years.</li>"
            "<li>Click <strong>Calculate</strong> — the monthly payment, total cost, and amortization preview appear instantly.</li>"
            "</ol>"
            "<p><strong>Formula</strong>: M = P · r(1+r)<sup>n</sup> / ((1+r)<sup>n</sup> − 1), where r is the monthly rate (annual rate / 12) and n is the number of months. For a zero-rate loan the monthly payment is simply principal / months.</p>"
            "<p>Assumes a fixed rate, equal monthly payments, and no fees, taxes, or insurance. Real loans usually include origination fees, escrow, and PMI — your actual monthly cost may be higher.</p>"
        ),
        "related_header": "Related Tools",
        "related_compound": "Compound Interest",
        "related_retirement": "Retirement Calculator",
        "related_date": "Date Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Monthly payment, total interest, and 12-month amortization for any fixed-rate loan."
    },
    "ko": {
        "title": "대출 계산기",
        "meta_title": "대출 계산기 — 월 상환금, 이자, 분할상환표 - Utilify",
        "meta_desc": "주택담보·자동차·신용대출의 월 상환금, 총 이자, 분할상환표를 즉시 계산. 모든 처리는 브라우저에서.",
        "og_title": "대출 계산기 - Utilify",
        "og_desc": "고정금리 대출의 월 상환금, 총 이자, 분할상환을 계산하세요.",
        "json_name": "대출 계산기",
        "json_desc": "고정금리 대출의 월 상환금, 총 이자, 분할상환표를 계산하는 도구.",
        "page_desc": "대출 원금·연 이자율·기간(년)을 입력하면 월 상환금, 총 상환액, 첫 12개월 분할상환표가 표시됩니다. 주택담보·자동차·신용 등 고정금리 대출 표준 공식을 사용합니다.",
        "label_principal": "대출 원금",
        "label_rate": "연 이자율 (%)",
        "label_term": "기간 (년)",
        "ph_principal": "100000000",
        "ph_rate": "4.5",
        "ph_term": "30",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 월 대출 상환금은 {value} —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_monthly_label": "월 상환금",
        "res_total_label": "총 상환액",
        "res_interest_label": "총 이자",
        "res_schedule_header": "첫 12개월 분할상환",
        "th_month": "월차",
        "th_payment": "상환금",
        "th_principal_col": "원금",
        "th_interest_col": "이자",
        "th_balance": "잔액",
        "alert_invalid": "원금과 기간은 양수로 입력해 주세요.",
        "disclaimer": "추정치 — 재정 자문이 아닙니다. 중대한 결정은 자격 있는 전문가와 상의하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>대출 원금(빌리는 금액)을 입력하세요.</li>"
            "<li>연 이자율을 퍼센트로 입력하세요 (예: 4.5%는 <code>4.5</code>).</li>"
            "<li>대출 기간을 연 단위로 입력하세요.</li>"
            "<li><strong>계산</strong>을 누르면 월 상환금, 총 상환액, 분할상환표가 즉시 표시됩니다.</li>"
            "</ol>"
            "<p><strong>공식</strong>: M = P · r(1+r)<sup>n</sup> / ((1+r)<sup>n</sup> − 1). r은 월 이자율(연 이자율 / 12), n은 총 개월 수입니다. 무이자(0%) 대출은 원금 / 개월수로 계산합니다.</p>"
            "<p>고정금리·원리금균등상환·수수료 없음을 가정합니다. 실제 대출은 인지세·중도상환수수료·보증료 등이 추가될 수 있어 실제 부담은 더 클 수 있습니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_compound": "복리 계산기",
        "related_retirement": "은퇴 계산기",
        "related_date": "날짜 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "고정금리 대출의 월 상환금·총 이자·12개월 분할상환표를 즉시 계산."
    },
    "ja": {
        "title": "ローン計算機",
        "meta_title": "ローン計算機 — 月々の返済額・利息・返済スケジュール - Utilify",
        "meta_desc": "月々のローン返済額、総利息、返済スケジュールを計算します。住宅ローン・自動車ローン・個人ローンに対応。すべてブラウザで動作。",
        "og_title": "ローン計算機 - Utilify",
        "og_desc": "固定金利ローンの月々の返済額・総利息・返済スケジュールを計算します。",
        "json_name": "ローン計算機",
        "json_desc": "固定金利ローンの月々の返済額・総利息・返済スケジュールを計算するツール。",
        "page_desc": "借入額・年利・返済期間（年）を入力すると、月々の返済額・総返済額・最初の12か月の返済スケジュールが表示されます。住宅・自動車・個人ローンの固定金利標準計算式を使用。",
        "label_principal": "借入額",
        "label_rate": "年利率 (%)",
        "label_term": "返済期間（年）",
        "ph_principal": "100000",
        "ph_rate": "4.5",
        "ph_term": "30",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "月々のローン返済額は {value} —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_monthly_label": "月々の返済額",
        "res_total_label": "総返済額",
        "res_interest_label": "総利息",
        "res_schedule_header": "最初の12か月",
        "th_month": "月",
        "th_payment": "返済額",
        "th_principal_col": "元金",
        "th_interest_col": "利息",
        "th_balance": "残高",
        "alert_invalid": "借入額と返済期間は正の数で入力してください。",
        "disclaimer": "推定値のみ — 金融アドバイスではありません。重要な判断の前には資格を持つ専門家にご相談ください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>ローンの元金（借りる金額）を入力します。</li>"
            "<li>年利率をパーセントで入力します（例: 4.5%は<code>4.5</code>）。</li>"
            "<li>返済期間を年単位で入力します。</li>"
            "<li><strong>計算</strong>をクリックすると月々の返済額・総返済額・返済スケジュールが即座に表示されます。</li>"
            "</ol>"
            "<p><strong>計算式</strong>: M = P · r(1+r)<sup>n</sup> / ((1+r)<sup>n</sup> − 1)。rは月利（年利 / 12）、nは返済回数（月数）。金利0%の場合は元金 / 月数で計算します。</p>"
            "<p>固定金利・均等月払い・手数料なしを前提としています。実際のローンは手数料・保証料などが加わる場合があり、実際の負担はより大きくなることがあります。</p>"
        ),
        "related_header": "関連ツール",
        "related_compound": "複利計算機",
        "related_retirement": "老後資金計算機",
        "related_date": "日付計算機",
        "related_unit": "単位変換",
        "card_blurb": "固定金利ローンの月々の返済額・総利息・12か月の返済スケジュールを即計算。"
    }
}


COMPOUND_INTEREST = {
    "en": {
        "title": "Compound Interest Calculator",
        "meta_title": "Compound Interest Calculator — Investment Growth - Utilify",
        "meta_desc": "Project savings or investment growth with compound interest and optional monthly contributions. See final balance, total contributions, and yearly breakdown.",
        "og_title": "Compound Interest Calculator - Utilify",
        "og_desc": "Project investment growth with compound interest and monthly contributions.",
        "json_name": "Compound Interest Calculator",
        "json_desc": "Estimate future value with compound interest, configurable compounding frequency, and monthly contributions.",
        "page_desc": "Enter your starting principal, annual return, time horizon, compounding frequency, and optional monthly contributions to project the future value of an investment or savings account. Includes a year-by-year balance breakdown.",
        "label_principal": "Starting principal",
        "label_rate": "Annual return (%)",
        "label_years": "Time horizon (years)",
        "label_freq": "Compounding frequency",
        "label_monthly_contrib": "Monthly contribution",
        "ph_principal": "10000",
        "ph_rate": "7",
        "ph_years": "20",
        "ph_monthly_contrib": "500",
        "opt_freq_yearly": "Yearly",
        "opt_freq_monthly": "Monthly",
        "opt_freq_daily": "Daily",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My investment will grow to {value} —",
        "share_copied": "Result copied to clipboard.",
        "res_final_label": "Final balance",
        "res_total_contrib_label": "Total contributions",
        "res_total_interest_label": "Total interest earned",
        "res_yearly_header": "Year-by-year balance",
        "th_year": "Year",
        "th_balance": "Balance",
        "th_contributed": "Contributed",
        "th_interest": "Interest earned",
        "alert_invalid": "Please enter non-negative numbers and a positive time horizon.",
        "disclaimer": "Estimate only — not financial advice. Real returns vary and are not guaranteed.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter your starting principal — the amount you have today.</li>"
            "<li>Enter the expected annual return as a percent (historical S&amp;P 500 average is ~7% real, ~10% nominal).</li>"
            "<li>Enter the time horizon in years.</li>"
            "<li>Pick the compounding frequency: yearly, monthly, or daily. Most index funds compound continuously — monthly is a close approximation.</li>"
            "<li>Optionally add a monthly contribution. Click <strong>Calculate</strong>.</li>"
            "</ol>"
            "<p><strong>Formula</strong>: FV = P(1 + r/m)<sup>m·t</sup> + C · ((1 + r/m)<sup>m·t</sup> − 1) / (r/m), where P is principal, r is the annual rate, m is compounding periods per year, t is years, and C is the periodic contribution converted to the compounding period.</p>"
            "<p>Inflation, taxes, and fees are not modeled. A 7% nominal return at 3% inflation is roughly a 4% real return — the future balance will buy less than today's purchasing power suggests.</p>"
        ),
        "related_header": "Related Tools",
        "related_loan": "Loan Calculator",
        "related_retirement": "Retirement Calculator",
        "related_date": "Date Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Project investment growth with compound interest and monthly contributions."
    },
    "ko": {
        "title": "복리 계산기",
        "meta_title": "복리 계산기 — 투자 성장 시뮬레이션 - Utilify",
        "meta_desc": "원금·연 수익률·기간·월 적립으로 복리 효과를 적용한 미래 잔액, 총 납입, 총 이자를 계산. 연도별 잔액 표 포함.",
        "og_title": "복리 계산기 - Utilify",
        "og_desc": "복리와 월 적립을 적용한 투자 성장을 시뮬레이션하세요.",
        "json_name": "복리 계산기",
        "json_desc": "원금·연 수익률·복리 빈도·월 적립을 입력하면 미래 가치를 계산하는 도구.",
        "page_desc": "초기 원금·연 수익률·기간·복리 빈도·월 적립을 입력하면 투자 또는 저축 계좌의 미래 가치를 계산합니다. 연도별 잔액 흐름도 함께 표시됩니다.",
        "label_principal": "초기 원금",
        "label_rate": "연 수익률 (%)",
        "label_years": "기간 (년)",
        "label_freq": "복리 빈도",
        "label_monthly_contrib": "월 적립금",
        "ph_principal": "10000000",
        "ph_rate": "7",
        "ph_years": "20",
        "ph_monthly_contrib": "500000",
        "opt_freq_yearly": "연 1회",
        "opt_freq_monthly": "월 복리",
        "opt_freq_daily": "일 복리",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 투자 미래 가치는 {value} —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_final_label": "최종 잔액",
        "res_total_contrib_label": "총 납입금",
        "res_total_interest_label": "총 이자 수익",
        "res_yearly_header": "연도별 잔액",
        "th_year": "연차",
        "th_balance": "잔액",
        "th_contributed": "납입 누적",
        "th_interest": "이자 수익",
        "alert_invalid": "원금과 적립금은 0 이상, 기간은 양수로 입력해 주세요.",
        "disclaimer": "추정치 — 재정 자문이 아닙니다. 실제 수익은 변동하며 보장되지 않습니다.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>현재 가지고 있는 초기 원금을 입력하세요.</li>"
            "<li>예상 연 수익률을 퍼센트로 입력하세요 (S&amp;P 500 장기 평균은 명목 약 10%, 실질 약 7%).</li>"
            "<li>투자 기간을 연 단위로 입력하세요.</li>"
            "<li>복리 빈도를 선택합니다: 연 1회·월·일. 인덱스 펀드는 사실상 연속복리이므로 월 복리가 근사값입니다.</li>"
            "<li>월 적립금을 입력 (없으면 0)하고 <strong>계산</strong>을 누르세요.</li>"
            "</ol>"
            "<p><strong>공식</strong>: FV = P(1 + r/m)<sup>m·t</sup> + C · ((1 + r/m)<sup>m·t</sup> − 1) / (r/m). P는 원금, r은 연 이자율, m은 연 복리 횟수, t는 년수, C는 정기 적립금입니다.</p>"
            "<p>인플레이션·세금·수수료는 반영되지 않습니다. 명목 7%에 인플레이션 3%면 실질 수익률은 약 4% — 미래 잔액의 구매력은 보이는 숫자보다 작습니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_loan": "대출 계산기",
        "related_retirement": "은퇴 계산기",
        "related_date": "날짜 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "복리와 월 적립을 적용한 투자·저축의 미래 가치를 즉시 시뮬레이션."
    },
    "ja": {
        "title": "複利計算機",
        "meta_title": "複利計算機 — 投資成長シミュレーション - Utilify",
        "meta_desc": "元金・年利・期間・月々の積立で複利効果を適用した将来残高・総積立・総利息を計算。年別残高表付き。",
        "og_title": "複利計算機 - Utilify",
        "og_desc": "複利と月々の積立で投資成長をシミュレーションします。",
        "json_name": "複利計算機",
        "json_desc": "元金・年利・複利頻度・月々の積立を入力して将来価値を計算するツール。",
        "page_desc": "初期元金・年利・期間・複利頻度・月々の積立を入力すると、投資や貯蓄口座の将来価値を計算します。年別残高推移も表示されます。",
        "label_principal": "初期元金",
        "label_rate": "年利率 (%)",
        "label_years": "期間（年）",
        "label_freq": "複利頻度",
        "label_monthly_contrib": "月々の積立額",
        "ph_principal": "10000",
        "ph_rate": "7",
        "ph_years": "20",
        "ph_monthly_contrib": "500",
        "opt_freq_yearly": "年1回",
        "opt_freq_monthly": "月複利",
        "opt_freq_daily": "日複利",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "投資の将来価値は {value} —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_final_label": "最終残高",
        "res_total_contrib_label": "総積立額",
        "res_total_interest_label": "総利息収益",
        "res_yearly_header": "年別残高",
        "th_year": "年",
        "th_balance": "残高",
        "th_contributed": "積立累計",
        "th_interest": "利息収益",
        "alert_invalid": "元金・積立額は0以上、期間は正の数で入力してください。",
        "disclaimer": "推定値のみ — 金融アドバイスではありません。実際のリターンは変動し、保証されません。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>現在持っている初期元金を入力します。</li>"
            "<li>期待する年利率をパーセントで入力します（S&amp;P 500の長期平均は名目約10%、実質約7%）。</li>"
            "<li>投資期間を年単位で入力します。</li>"
            "<li>複利頻度を選びます: 年1回・月・日。インデックスファンドは実質連続複利のため月複利が近似値です。</li>"
            "<li>月々の積立額を入力（なければ0）して<strong>計算</strong>をクリックします。</li>"
            "</ol>"
            "<p><strong>計算式</strong>: FV = P(1 + r/m)<sup>m·t</sup> + C · ((1 + r/m)<sup>m·t</sup> − 1) / (r/m)。Pは元金、rは年利率、mは年間複利回数、tは年数、Cは定期積立額です。</p>"
            "<p>インフレ・税金・手数料は考慮されていません。名目7%でインフレ3%であれば実質利回りは約4% — 将来残高の購買力は表示される数値より低くなります。</p>"
        ),
        "related_header": "関連ツール",
        "related_loan": "ローン計算機",
        "related_retirement": "老後資金計算機",
        "related_date": "日付計算機",
        "related_unit": "単位変換",
        "card_blurb": "複利と月々の積立で投資・貯蓄の将来価値を即シミュレーション。"
    }
}


RETIREMENT_CALCULATOR = {
    "en": {
        "title": "Retirement Calculator",
        "meta_title": "Retirement Calculator — Will Your Savings Last? - Utilify",
        "meta_desc": "Estimate retirement nest egg and how long it lasts. Inputs: current age, retirement age, savings, monthly contributions, return, withdrawal, life expectancy.",
        "og_title": "Retirement Calculator - Utilify",
        "og_desc": "Project retirement savings and check whether they last through life expectancy.",
        "json_name": "Retirement Calculator",
        "json_desc": "Two-phase retirement model: accumulation with monthly contributions, then withdrawal with annual income.",
        "page_desc": "Enter your current age, target retirement age, current savings, monthly contributions, expected return, planned annual withdrawal, and life expectancy. The calculator runs an accumulation phase, then a withdrawal phase to show whether your nest egg lasts.",
        "label_current_age": "Current age",
        "label_retire_age": "Retirement age",
        "label_current_savings": "Current savings",
        "label_monthly_contrib": "Monthly contribution",
        "label_annual_return": "Annual return (%)",
        "label_annual_withdrawal": "Annual withdrawal in retirement",
        "label_life_expectancy": "Life expectancy",
        "ph_current_age": "30",
        "ph_retire_age": "65",
        "ph_current_savings": "50000",
        "ph_monthly_contrib": "500",
        "ph_annual_return": "6",
        "ph_annual_withdrawal": "30000",
        "ph_life_expectancy": "85",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My retirement nest egg: {value} —",
        "share_copied": "Result copied to clipboard.",
        "res_at_retirement_label": "Nest egg at retirement",
        "res_outcome_header": "Outcome",
        "outcome_lasts": "Funds last through life expectancy. Surplus at age {age}: {amount}.",
        "outcome_runs_out": "Funds run out at age {age} — {years} years short of life expectancy.",
        "res_chart_header": "Balance over time",
        "alert_invalid": "Retirement age must be greater than current age, and life expectancy greater than retirement age.",
        "disclaimer": "Estimate only — not financial advice. Consult a qualified retirement planner before making decisions.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter your <em>current age</em> and <em>target retirement age</em>.</li>"
            "<li>Enter your current savings (the amount in retirement accounts today) and your monthly contribution until retirement.</li>"
            "<li>Set an expected annual return (a common assumption is 6% real for a balanced portfolio).</li>"
            "<li>Enter how much you plan to withdraw <em>per year</em> in retirement (about 4% of the nest egg is the classic guideline).</li>"
            "<li>Enter your life expectancy. Click <strong>Calculate</strong> — the chart shows the balance trajectory.</li>"
            "</ol>"
            "<p><strong>Model</strong>: accumulation phase compounds monthly with your contributions until retirement age, then withdrawal phase deducts the annual withdrawal at the start of each year and grows the remainder by the annual return until the balance hits zero or life expectancy is reached.</p>"
            "<p>Real retirement is messier: returns are sequence-sensitive (a bad first year can sink the plan), Social Security or pensions add income, and healthcare costs spike late. Treat this as a sanity check, not a plan.</p>"
        ),
        "related_header": "Related Tools",
        "related_compound": "Compound Interest",
        "related_loan": "Loan Calculator",
        "related_date": "Date Calculator",
        "related_bmi": "BMI Calculator",
        "card_blurb": "Project retirement nest egg and check whether it lasts through life expectancy."
    },
    "ko": {
        "title": "은퇴 계산기",
        "meta_title": "은퇴 계산기 — 노후자금 충분한지 시뮬레이션 - Utilify",
        "meta_desc": "현재 나이·은퇴 나이·자산·월 적립·수익률·연 인출·기대수명을 입력해 은퇴 시점 자산과 자금 유지 가능 나이를 시뮬레이션.",
        "og_title": "은퇴 계산기 - Utilify",
        "og_desc": "노후자금이 기대수명까지 버티는지 시뮬레이션하세요.",
        "json_name": "은퇴 계산기",
        "json_desc": "월 적립으로 누적하는 단계와 연 인출 단계를 모두 시뮬레이션하는 2단계 모델.",
        "page_desc": "현재 나이·목표 은퇴 나이·현재 자산·월 적립금·기대 수익률·은퇴 후 연 인출액·기대수명을 입력하면 누적 단계와 인출 단계를 시뮬레이션해 자금이 언제까지 버티는지 알려줍니다.",
        "label_current_age": "현재 나이",
        "label_retire_age": "은퇴 나이",
        "label_current_savings": "현재 자산",
        "label_monthly_contrib": "월 적립금",
        "label_annual_return": "연 수익률 (%)",
        "label_annual_withdrawal": "은퇴 후 연 인출액",
        "label_life_expectancy": "기대수명",
        "ph_current_age": "30",
        "ph_retire_age": "65",
        "ph_current_savings": "50000000",
        "ph_monthly_contrib": "500000",
        "ph_annual_return": "6",
        "ph_annual_withdrawal": "30000000",
        "ph_life_expectancy": "85",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 은퇴 시점 자산은 {value} —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_at_retirement_label": "은퇴 시점 자산",
        "res_outcome_header": "결과",
        "outcome_lasts": "기대수명까지 자금이 유지됩니다. {age}세 시점 잉여: {amount}.",
        "outcome_runs_out": "{age}세에 자금이 소진됩니다 — 기대수명까지 {years}년 부족.",
        "res_chart_header": "잔액 추이",
        "alert_invalid": "은퇴 나이는 현재 나이보다, 기대수명은 은퇴 나이보다 커야 합니다.",
        "disclaimer": "추정치 — 재정 자문이 아닙니다. 실제 은퇴 계획은 자격 있는 전문가와 상의하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li><em>현재 나이</em>와 <em>목표 은퇴 나이</em>를 입력하세요.</li>"
            "<li>오늘 보유한 노후자금과 은퇴까지의 월 적립금을 입력하세요.</li>"
            "<li>예상 연 수익률을 입력하세요 (분산형 포트폴리오는 실질 6% 정도가 흔한 가정).</li>"
            "<li>은퇴 후 매년 인출할 금액을 입력하세요 (자산의 4% 룰이 고전적 기준).</li>"
            "<li>기대수명을 입력하고 <strong>계산</strong>을 누르세요. 잔액 추이가 그래프로 표시됩니다.</li>"
            "</ol>"
            "<p><strong>모델</strong>: 누적 단계는 은퇴까지 월 단위 복리로 적립금을 더하며, 인출 단계는 매년 초 연 인출액을 빼고 남은 잔액에 연 수익률을 곱합니다. 잔액이 0이 되거나 기대수명에 도달할 때까지 반복합니다.</p>"
            "<p>실제 은퇴는 더 복잡합니다 — 초기 몇 년의 수익률 순서가 결과를 크게 좌우하고(시퀀스 리스크), 국민연금/퇴직연금 같은 소득이 더해지며, 노년 의료비가 급증할 수 있습니다. 검산용으로만 사용하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_compound": "복리 계산기",
        "related_loan": "대출 계산기",
        "related_date": "날짜 계산기",
        "related_bmi": "BMI 계산기",
        "card_blurb": "노후자금이 기대수명까지 버티는지 누적·인출 2단계로 즉시 시뮬레이션."
    },
    "ja": {
        "title": "老後資金計算機",
        "meta_title": "老後資金計算機 — 貯蓄は老後まで持つか？ - Utilify",
        "meta_desc": "老後の貯蓄額と資金が尽きるまでの期間を推定します。現在の年齢・退職年齢・貯蓄・月々の積立・利回り・引き出し額・平均余命を入力。",
        "og_title": "老後資金計算機 - Utilify",
        "og_desc": "老後資金が平均余命まで持つかシミュレーションします。",
        "json_name": "老後資金計算機",
        "json_desc": "月々の積立による蓄積フェーズと年間引き出しフェーズの2段階モデル。",
        "page_desc": "現在の年齢・目標退職年齢・現在の貯蓄・月々の積立額・期待利回り・年間引き出し計画額・平均余命を入力すると、蓄積フェーズと引き出しフェーズをシミュレーションし、資金がいつまで持つかを表示します。",
        "label_current_age": "現在の年齢",
        "label_retire_age": "退職年齢",
        "label_current_savings": "現在の貯蓄額",
        "label_monthly_contrib": "月々の積立額",
        "label_annual_return": "年利率 (%)",
        "label_annual_withdrawal": "老後の年間引き出し額",
        "label_life_expectancy": "平均余命",
        "ph_current_age": "30",
        "ph_retire_age": "65",
        "ph_current_savings": "50000",
        "ph_monthly_contrib": "500",
        "ph_annual_return": "6",
        "ph_annual_withdrawal": "30000",
        "ph_life_expectancy": "85",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "老後資金の巣卵: {value} —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_at_retirement_label": "退職時の資産額",
        "res_outcome_header": "結果",
        "outcome_lasts": "資金は平均余命まで持続します。{age}歳時点の余剰: {amount}。",
        "outcome_runs_out": "{age}歳で資金が尽きます — 平均余命まであと{years}年不足。",
        "res_chart_header": "残高の推移",
        "alert_invalid": "退職年齢は現在の年齢より、平均余命は退職年齢より大きくなければなりません。",
        "disclaimer": "推定値のみ — 金融アドバイスではありません。実際の退職計画には資格を持つ専門家にご相談ください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li><em>現在の年齢</em>と<em>目標退職年齢</em>を入力します。</li>"
            "<li>現在の老後貯蓄額と退職までの月々の積立額を入力します。</li>"
            "<li>期待年利率を入力します（バランス型ポートフォリオでは実質6%が一般的な仮定）。</li>"
            "<li>老後に毎年引き出す金額を入力します（資産の4%ルールが古典的な目安）。</li>"
            "<li>平均余命を入力して<strong>計算</strong>をクリックします。残高推移がグラフで表示されます。</li>"
            "</ol>"
            "<p><strong>モデル</strong>: 蓄積フェーズは退職まで月単位の複利で積立金を加算し、引き出しフェーズは毎年初に年間引き出し額を差し引き、残高に年利率を適用します。残高がゼロになるか平均余命に達するまで繰り返します。</p>"
            "<p>実際の退職はより複雑です — 初期数年のリターン順序が結果に大きく影響し（シーケンスリスク）、年金収入が加わり、晩年の医療費が急増する可能性があります。あくまで目安として使用してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_compound": "複利計算機",
        "related_loan": "ローン計算機",
        "related_date": "日付計算機",
        "related_bmi": "BMI計算機",
        "card_blurb": "老後資金が平均余命まで持つか、蓄積・引き出しの2段階で即シミュレーション。"
    }
}


CALORIE_CALCULATOR = {
    "en": {
        "title": "Calorie & BMR Calculator",
        "meta_title": "Calorie Calculator — BMR + TDEE (Mifflin-St Jeor) - Utilify",
        "meta_desc": "BMR + TDEE calculator using the Mifflin-St Jeor formula. Returns target calories for weight loss, maintenance, and muscle gain.",
        "og_title": "Calorie & BMR Calculator - Utilify",
        "og_desc": "BMR + TDEE + targets for cutting, maintenance, and bulking.",
        "json_name": "Calorie & BMR Calculator",
        "json_desc": "Mifflin-St Jeor BMR plus activity multiplier and goal-adjusted calorie targets.",
        "page_desc": "Enter your age, sex, height, weight, and activity level to get your basal metabolic rate, total daily calorie burn, and recommended targets for weight loss, maintenance, or muscle gain. Uses the Mifflin-St Jeor equation, the most accurate formula for healthy adults.",
        "label_age": "Age (years)",
        "label_sex": "Sex",
        "label_height": "Height (cm)",
        "label_weight": "Weight (kg)",
        "label_activity": "Activity level",
        "ph_age": "30",
        "ph_height": "170",
        "ph_weight": "70",
        "opt_male": "Male",
        "opt_female": "Female",
        "opt_sedentary": "Sedentary (little to no exercise)",
        "opt_light": "Light (1–3 days / week)",
        "opt_moderate": "Moderate (3–5 days / week)",
        "opt_active": "Active (6–7 days / week)",
        "opt_very_active": "Very active (twice daily / hard training)",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My daily calorie need: {value} kcal —",
        "share_copied": "Result copied to clipboard.",
        "res_bmr_label": "BMR (kcal/day)",
        "res_tdee_label": "TDEE (kcal/day)",
        "res_targets_header": "Daily calorie targets",
        "target_loss": "Weight loss (−500)",
        "target_maintain": "Maintenance",
        "target_gain": "Muscle gain (+300)",
        "alert_invalid": "Please enter a positive age, height, and weight.",
        "disclaimer": "Estimate only — not medical advice. Talk to a registered dietitian or physician before changing your diet, especially if pregnant, nursing, or managing a condition.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter your age in years.</li>"
            "<li>Pick your biological sex (the formula has different constants for male and female).</li>"
            "<li>Enter your height in centimeters and weight in kilograms.</li>"
            "<li>Pick the activity level that best matches a typical week. Most desk workers are sedentary or light even with weekend exercise.</li>"
            "<li>Click <strong>Calculate</strong> — BMR, TDEE, and three goal-adjusted targets appear.</li>"
            "</ol>"
            "<p><strong>Formula (Mifflin-St Jeor)</strong>: Male BMR = 10·W + 6.25·H − 5·A + 5; Female BMR = 10·W + 6.25·H − 5·A − 161. TDEE = BMR × activity factor (sedentary 1.2, light 1.375, moderate 1.55, active 1.725, very active 1.9).</p>"
            "<p>BMR is what your body burns at complete rest — heart, brain, breathing. TDEE includes movement and exercise. The 500 kcal/day deficit is a classic 1 lb/week weight-loss target; +300 supports lean muscle gain when paired with strength training.</p>"
        ),
        "related_header": "Related Tools",
        "related_bmi": "BMI Calculator",
        "related_body_fat": "Body Fat Calculator",
        "related_unit": "Unit Converter",
        "related_date": "Date Calculator",
        "card_blurb": "BMR + TDEE + cut/maintain/bulk calorie targets (Mifflin-St Jeor)."
    },
    "ko": {
        "title": "칼로리·BMR 계산기",
        "meta_title": "칼로리 계산기 — BMR·TDEE 자동 계산 (Mifflin-St Jeor) - Utilify",
        "meta_desc": "기초대사량(BMR)과 1일 총 소모 칼로리(TDEE)를 Mifflin-St Jeor 공식으로 계산. 다이어트·유지·근증량 목표 칼로리 함께 제공.",
        "og_title": "칼로리·BMR 계산기 - Utilify",
        "og_desc": "기초대사량과 1일 활동 칼로리, 목표별 권장 섭취량까지 한번에.",
        "json_name": "칼로리·BMR 계산기",
        "json_desc": "Mifflin-St Jeor 공식 기반 기초대사량 + 활동계수 + 목표별 권장 섭취량.",
        "page_desc": "나이·성별·키·체중·활동 수준을 입력하면 기초대사량, 1일 총 소모 칼로리, 다이어트/유지/근증량 목표 칼로리를 계산합니다. 건강한 성인에게 가장 정확한 Mifflin-St Jeor 공식을 사용합니다.",
        "label_age": "나이 (년)",
        "label_sex": "성별",
        "label_height": "키 (cm)",
        "label_weight": "체중 (kg)",
        "label_activity": "활동 수준",
        "ph_age": "30",
        "ph_height": "170",
        "ph_weight": "70",
        "opt_male": "남성",
        "opt_female": "여성",
        "opt_sedentary": "거의 활동 없음 (운동 안 함)",
        "opt_light": "가벼운 활동 (주 1–3회)",
        "opt_moderate": "보통 활동 (주 3–5회)",
        "opt_active": "활발한 활동 (주 6–7회)",
        "opt_very_active": "매우 활발 (하루 2회 또는 강도 높은 훈련)",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 1일 권장 칼로리: {value} kcal —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_bmr_label": "기초대사량 (kcal/일)",
        "res_tdee_label": "1일 총 소모 (kcal/일)",
        "res_targets_header": "목표별 1일 칼로리",
        "target_loss": "감량 (−500)",
        "target_maintain": "유지",
        "target_gain": "근증량 (+300)",
        "alert_invalid": "나이·키·체중은 양수로 입력해 주세요.",
        "disclaimer": "추정치 — 의료 자문이 아닙니다. 임신·수유·질환 관리 중이라면 식단 변경 전 의료진 또는 임상영양사와 상의하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>나이를 년 단위로 입력하세요.</li>"
            "<li>생물학적 성별을 선택하세요 (공식 상수가 남녀에 따라 다름).</li>"
            "<li>키(cm)와 체중(kg)을 입력하세요.</li>"
            "<li>일주일 평균에 가까운 활동 수준을 선택하세요. 사무직은 주말 운동을 해도 보통 \"거의 없음\" 또는 \"가벼움\"에 해당합니다.</li>"
            "<li><strong>계산</strong>을 누르면 BMR, TDEE, 그리고 목표 칼로리 3가지가 표시됩니다.</li>"
            "</ol>"
            "<p><strong>공식 (Mifflin-St Jeor)</strong>: 남성 BMR = 10·W + 6.25·H − 5·A + 5; 여성 BMR = 10·W + 6.25·H − 5·A − 161. TDEE = BMR × 활동계수 (거의 없음 1.2, 가벼움 1.375, 보통 1.55, 활발 1.725, 매우 활발 1.9).</p>"
            "<p>BMR은 완전 휴식 상태에서 소모되는 칼로리(심장·뇌·호흡)이고, TDEE는 활동까지 포함한 총 소모량입니다. −500 kcal/일은 주당 약 0.45 kg 감량 목표, +300은 근력 운동과 함께 근육 증가 지원에 적합합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_bmi": "BMI 계산기",
        "related_body_fat": "체지방 계산기",
        "related_unit": "단위 변환기",
        "related_date": "날짜 계산기",
        "card_blurb": "Mifflin-St Jeor 공식으로 BMR·TDEE·목표별(감량/유지/증량) 칼로리 즉시 계산."
    },
    "ja": {
        "title": "カロリー・BMR計算機",
        "meta_title": "カロリー計算機 — BMR・TDEE自動計算 (Mifflin-St Jeor) - Utilify",
        "meta_desc": "基礎代謝量(BMR)と1日の総消費カロリー(TDEE)をMifflin-St Jeor公式で計算。減量・維持・増量の目標カロリーも併せて提供。",
        "og_title": "カロリー・BMR計算機 - Utilify",
        "og_desc": "基礎代謝・1日の消費カロリー・目標別推奨摂取量まで一括。",
        "json_name": "カロリー・BMR計算機",
        "json_desc": "Mifflin-St Jeor公式に基づくBMR + 活動係数 + 目標別推奨摂取量。",
        "page_desc": "年齢・性別・身長・体重・活動レベルを入力すると、基礎代謝量、1日の総消費カロリー、減量/維持/筋増量の目標カロリーを計算します。健康な成人に最も正確とされるMifflin-St Jeor公式を使用しています。",
        "label_age": "年齢 (歳)",
        "label_sex": "性別",
        "label_height": "身長 (cm)",
        "label_weight": "体重 (kg)",
        "label_activity": "活動レベル",
        "ph_age": "30",
        "ph_height": "170",
        "ph_weight": "70",
        "opt_male": "男性",
        "opt_female": "女性",
        "opt_sedentary": "ほぼ運動なし (デスクワーク中心)",
        "opt_light": "軽い運動 (週1~3回)",
        "opt_moderate": "中程度の運動 (週3~5回)",
        "opt_active": "活発な運動 (週6~7回)",
        "opt_very_active": "非常に活発 (1日2回・ハードトレーニング)",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "1日の推奨カロリー: {value} kcal —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_bmr_label": "基礎代謝 (kcal/日)",
        "res_tdee_label": "1日の総消費 (kcal/日)",
        "res_targets_header": "目標別1日カロリー",
        "target_loss": "減量 (−500)",
        "target_maintain": "維持",
        "target_gain": "筋増量 (+300)",
        "alert_invalid": "年齢・身長・体重は正の数で入力してください。",
        "disclaimer": "推定値です — 医療助言ではありません。妊娠・授乳中、疾患管理中の方は食事の変更前に医師や管理栄養士に相談してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>年齢を歳単位で入力します。</li>"
            "<li>生物学的性別を選びます(公式の定数が男女で異なります)。</li>"
            "<li>身長(cm)と体重(kg)を入力します。</li>"
            "<li>普段の1週間に近い活動レベルを選びます。週末に運動するデスクワーカーでも、多くは\"ほぼ運動なし\"または\"軽い運動\"に該当します。</li>"
            "<li><strong>計算</strong>を押すと、BMR、TDEE、目標別カロリー3種が表示されます。</li>"
            "</ol>"
            "<p><strong>計算式 (Mifflin-St Jeor)</strong>:男性 BMR = 10·W + 6.25·H − 5·A + 5、女性 BMR = 10·W + 6.25·H − 5·A − 161。TDEE = BMR × 活動係数(ほぼ運動なし1.2、軽い1.375、中程度1.55、活発1.725、非常に活発1.9)。</p>"
            "<p>BMRは完全休息時に消費するカロリー(心臓・脳・呼吸)、TDEEは活動を含む総消費量です。−500 kcal/日は週約0.45 kg減量を目指す目安、+300は筋トレと組み合わせた筋肉増加に適しています。</p>"
        ),
        "related_header": "関連ツール",
        "related_bmi": "BMI計算機",
        "related_body_fat": "体脂肪率計算機",
        "related_unit": "単位変換",
        "related_date": "日付計算機",
        "card_blurb": "Mifflin-St Jeor公式でBMR・TDEE・目標別(減量/維持/増量)カロリーを即計算。"
    }
}


PREGNANCY_CALCULATOR = {
    "en": {
        "title": "Pregnancy Due Date Calculator",
        "meta_title": "Pregnancy Calculator — Due Date, Week, Trimester - Utilify",
        "meta_desc": "Calculate your due date, current pregnancy week, and trimester from your last menstrual period (LMP). Naegele's rule with cycle-length adjustment.",
        "og_title": "Pregnancy Due Date Calculator - Utilify",
        "og_desc": "Due date, current week, trimester, and days remaining.",
        "json_name": "Pregnancy Calculator",
        "json_desc": "Estimate due date and current pregnancy week from last menstrual period.",
        "page_desc": "Enter the first day of your last menstrual period (LMP) and your typical cycle length. The calculator returns the estimated due date, your current pregnancy week and day, the trimester, and how many days remain until delivery. Naegele's rule plus a cycle-length adjustment.",
        "label_lmp": "First day of last menstrual period",
        "label_cycle": "Average cycle length (days)",
        "ph_cycle": "28",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My estimated due date: {value} —",
        "share_copied": "Result copied to clipboard.",
        "res_due_label": "Estimated due date",
        "res_week_label": "Current week",
        "res_trimester_label": "Trimester",
        "res_remaining_label": "Days remaining",
        "trimester_1": "First trimester",
        "trimester_2": "Second trimester",
        "trimester_3": "Third trimester",
        "week_format": "Week {week} day {day}",
        "alert_invalid": "Enter a valid LMP date and a cycle length between 21 and 45 days.",
        "alert_future": "LMP cannot be in the future.",
        "disclaimer": "Estimate only — not medical advice. Only ~5% of babies arrive on the predicted due date. An ultrasound dating scan is more accurate, especially if cycles are irregular.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick the first day of your last menstrual period (LMP). This is day 1 of the cycle that resulted in pregnancy.</li>"
            "<li>Enter your typical cycle length. The default is 28 days; adjust if yours is consistently shorter or longer.</li>"
            "<li>Click <strong>Calculate</strong>. You'll see the estimated due date, your current pregnancy week, the trimester, and days remaining.</li>"
            "</ol>"
            "<p><strong>Formula (Naegele's rule)</strong>: due date = LMP + 280 days, then adjusted by (cycle length − 28) days to account for variations in ovulation timing. Pregnancy is dated from LMP (not conception), so week 1 starts before you actually conceived. Trimesters: 1st (weeks 1–13), 2nd (14–27), 3rd (28–40+).</p>"
            "<p>If your cycles are irregular or you don't know your LMP, an ultrasound dating scan in the first trimester is the most accurate method.</p>"
        ),
        "related_header": "Related Tools",
        "related_date": "Date Calculator",
        "related_bmi": "BMI Calculator",
        "related_calorie": "Calorie Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Due date + current pregnancy week + trimester from your LMP. Cycle-length adjustable."
    },
    "ko": {
        "title": "임신 출산예정일 계산기",
        "meta_title": "임신 계산기 — 출산예정일·주수·삼분기 - Utilify",
        "meta_desc": "마지막 생리일(LMP)로 출산예정일, 현재 임신 주수와 일수, 삼분기를 계산. Naegele 공식 + 생리주기 보정.",
        "og_title": "임신 출산예정일 계산기 - Utilify",
        "og_desc": "출산예정일·현재 주수·삼분기·남은 일수를 한번에.",
        "json_name": "임신 출산예정일 계산기",
        "json_desc": "마지막 생리일로부터 출산예정일과 현재 임신 주수를 추정.",
        "page_desc": "마지막 생리 시작일(LMP)과 평소 생리주기 길이를 입력하면 출산예정일, 현재 임신 주수와 일수, 삼분기, 남은 일수를 계산합니다. Naegele 공식과 생리주기 보정을 함께 적용합니다.",
        "label_lmp": "마지막 생리 시작일",
        "label_cycle": "평소 생리주기 (일)",
        "ph_cycle": "28",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 출산예정일: {value} —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_due_label": "출산예정일",
        "res_week_label": "현재 주수",
        "res_trimester_label": "삼분기",
        "res_remaining_label": "남은 일수",
        "trimester_1": "1삼분기",
        "trimester_2": "2삼분기",
        "trimester_3": "3삼분기",
        "week_format": "{week}주 {day}일",
        "alert_invalid": "유효한 마지막 생리일과 21~45일 사이의 주기를 입력해 주세요.",
        "alert_future": "마지막 생리일은 미래일 수 없습니다.",
        "disclaimer": "추정치 — 의료 자문이 아닙니다. 출산예정일에 정확히 출산하는 비율은 약 5%입니다. 생리주기가 불규칙하거나 LMP가 불확실하면 초음파 검사가 더 정확합니다.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>마지막 생리가 시작된 첫날(LMP)을 선택하세요. 임신이 일어난 그 주기의 1일입니다.</li>"
            "<li>평소 생리주기 길이를 입력하세요. 기본값 28일이며, 일관되게 다르면 조정하세요.</li>"
            "<li><strong>계산</strong>을 누르면 출산예정일, 현재 주수, 삼분기, 남은 일수가 표시됩니다.</li>"
            "</ol>"
            "<p><strong>공식 (Naegele 법칙)</strong>: 출산예정일 = LMP + 280일, 이후 (생리주기 − 28)일만큼 조정해 배란 시점 차이를 반영합니다. 임신 주수는 수정일이 아니라 LMP 기준이므로 1주차는 실제 임신 전부터 시작됩니다. 삼분기 구분: 1삼분기(1~13주), 2삼분기(14~27주), 3삼분기(28주 이후).</p>"
            "<p>생리주기가 불규칙하거나 LMP가 명확하지 않다면 1삼분기 초음파 검사가 가장 정확한 방법입니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_date": "날짜 계산기",
        "related_bmi": "BMI 계산기",
        "related_calorie": "칼로리 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "마지막 생리일(LMP)로 출산예정일·현재 주수·삼분기를 즉시 계산. 생리주기 보정 가능."
    },
    "ja": {
        "title": "妊娠出産予定日計算機",
        "meta_title": "妊娠計算機 — 出産予定日・週数・トリメスター - Utilify",
        "meta_desc": "最終月経日（LMP）から出産予定日・現在の妊娠週数・トリメスターを計算します。ネーゲレ公式＋生理周期補正。",
        "og_title": "妊娠出産予定日計算機 - Utilify",
        "og_desc": "出産予定日・現在の週数・トリメスター・残り日数を一括表示。",
        "json_name": "妊娠出産予定日計算機",
        "json_desc": "最終月経日から出産予定日と現在の妊娠週数を推定します。",
        "page_desc": "最終月経開始日（LMP）と通常の生理周期を入力すると、出産予定日・現在の妊娠週数・トリメスター・残り日数を計算します。ネーゲレ公式と生理周期補正を適用しています。",
        "label_lmp": "最終月経開始日",
        "label_cycle": "平均生理周期（日）",
        "ph_cycle": "28",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "推定出産予定日: {value} —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_due_label": "推定出産予定日",
        "res_week_label": "現在の週数",
        "res_trimester_label": "トリメスター",
        "res_remaining_label": "残り日数",
        "trimester_1": "第1トリメスター",
        "trimester_2": "第2トリメスター",
        "trimester_3": "第3トリメスター",
        "week_format": "{week}週{day}日",
        "alert_invalid": "有効な最終月経日と21〜45日の生理周期を入力してください。",
        "alert_future": "最終月経日は未来の日付にはできません。",
        "disclaimer": "推定値のみ — 医療上のアドバイスではありません。出産予定日通りに生まれる赤ちゃんは約5%程度です。生理周期が不規則な場合や最終月経日が不明な場合は、超音波検査の方が正確です。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>最終月経の開始日（LMP）を選択します。これは妊娠が成立した周期の第1日目です。</li>"
            "<li>通常の生理周期を入力します。デフォルトは28日で、一定してずれる場合は調整してください。</li>"
            "<li><strong>計算</strong>をクリックすると出産予定日・現在の週数・トリメスター・残り日数が表示されます。</li>"
            "</ol>"
            "<p><strong>計算式（ネーゲレ法則）</strong>: 出産予定日 = LMP + 280日、その後（生理周期 − 28）日を加減して排卵タイミングのずれを補正します。妊娠週数は受精日ではなくLMPを基準とするため、第1週は実際の妊娠前から始まります。トリメスター区分: 第1（1〜13週）、第2（14〜27週）、第3（28週以降）。</p>"
            "<p>生理周期が不規則または最終月経日が不明な場合は、第1トリメスターの超音波検査が最も正確な方法です。</p>"
        ),
        "related_header": "関連ツール",
        "related_date": "日付計算機",
        "related_bmi": "BMI計算機",
        "related_calorie": "カロリー計算機",
        "related_unit": "単位変換",
        "card_blurb": "最終月経日（LMP）から出産予定日・現在の週数・トリメスターを即計算。生理周期補正対応。"
    }
}


BODY_FAT_CALCULATOR = {
    "en": {
        "title": "Body Fat Percentage Calculator",
        "meta_title": "Body Fat Calculator — US Navy Method - Utilify",
        "meta_desc": "Estimate body fat percentage with the US Navy circumference method. Inputs: height, neck, waist (and hip for women). Includes category and recommended range.",
        "og_title": "Body Fat Calculator - Utilify",
        "og_desc": "US Navy method body fat percentage with category and recommended range.",
        "json_name": "Body Fat Calculator",
        "json_desc": "US Navy circumference-based body fat estimate plus fitness category.",
        "page_desc": "Enter your height and circumference measurements (neck, waist, and hip for women) to estimate body fat percentage with the US Navy method. The result includes a fitness-category label and the typical recommended range for your sex.",
        "label_sex": "Sex",
        "label_height": "Height (cm)",
        "label_neck": "Neck circumference (cm)",
        "label_waist": "Waist circumference (cm)",
        "label_hip": "Hip circumference (cm)",
        "ph_height": "170",
        "ph_neck": "37",
        "ph_waist": "85",
        "ph_hip": "95",
        "opt_male": "Male",
        "opt_female": "Female",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "My body fat: {value}% —",
        "share_copied": "Result copied to clipboard.",
        "res_bfp_label": "Body fat",
        "res_category_label": "Category",
        "res_range_label": "Recommended range",
        "cat_essential": "Essential fat",
        "cat_athletes": "Athletes",
        "cat_fitness": "Fitness",
        "cat_average": "Average",
        "cat_obese": "Obese",
        "alert_invalid": "All measurements must be positive. For females, hip is required.",
        "alert_negative_log": "Waist and neck values are inconsistent — please re-measure.",
        "disclaimer": "Estimate only — not medical advice. Skinfold calipers, DEXA scans, or hydrostatic weighing are more accurate. Use this as a quick check, not a diagnosis.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick your biological sex.</li>"
            "<li>Measure neck circumference at the narrowest point, just below the larynx.</li>"
            "<li>Measure waist circumference at the navel for men, at the narrowest point for women. Relax — don't suck in.</li>"
            "<li>For women, also measure hip circumference at the widest point.</li>"
            "<li>Enter your height in centimeters. Click <strong>Calculate</strong>.</li>"
            "</ol>"
            "<p><strong>Formula (US Navy)</strong>: Male BFP = 86.010·log<sub>10</sub>(waist − neck) − 70.041·log<sub>10</sub>(height) + 36.76. Female BFP = 163.205·log<sub>10</sub>(waist + hip − neck) − 97.684·log<sub>10</sub>(height) − 78.387.</p>"
            "<p>The Navy method has ±3% accuracy versus hydrostatic weighing for typical body shapes — better than BMI for body composition but worse than DEXA. Take measurements first thing in the morning for consistency.</p>"
        ),
        "related_header": "Related Tools",
        "related_bmi": "BMI Calculator",
        "related_calorie": "Calorie Calculator",
        "related_unit": "Unit Converter",
        "related_date": "Date Calculator",
        "card_blurb": "US Navy method body fat % from height + neck + waist + hip measurements."
    },
    "ko": {
        "title": "체지방률 계산기",
        "meta_title": "체지방률 계산기 — 미 해군 둘레 측정법 - Utilify",
        "meta_desc": "키·목·허리 둘레(여성은 엉덩이까지)로 체지방률을 미 해군 공식으로 추정. 카테고리·권장 범위 함께 표시.",
        "og_title": "체지방률 계산기 - Utilify",
        "og_desc": "미 해군 둘레 측정법으로 체지방률·카테고리·권장 범위까지.",
        "json_name": "체지방률 계산기",
        "json_desc": "미 해군 둘레 측정 공식으로 체지방률을 추정하고 카테고리를 표시.",
        "page_desc": "키와 신체 둘레(목·허리, 여성은 엉덩이 추가)를 입력하면 미 해군 공식으로 체지방률을 추정합니다. 결과에는 피트니스 카테고리와 성별 권장 범위가 함께 표시됩니다.",
        "label_sex": "성별",
        "label_height": "키 (cm)",
        "label_neck": "목 둘레 (cm)",
        "label_waist": "허리 둘레 (cm)",
        "label_hip": "엉덩이 둘레 (cm)",
        "ph_height": "170",
        "ph_neck": "37",
        "ph_waist": "85",
        "ph_hip": "95",
        "opt_male": "남성",
        "opt_female": "여성",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "내 체지방률: {value}% —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_bfp_label": "체지방률",
        "res_category_label": "카테고리",
        "res_range_label": "권장 범위",
        "cat_essential": "필수 지방",
        "cat_athletes": "운동선수",
        "cat_fitness": "피트니스",
        "cat_average": "보통",
        "cat_obese": "비만",
        "alert_invalid": "모든 측정값은 양수여야 합니다. 여성은 엉덩이 둘레가 필수입니다.",
        "alert_negative_log": "허리와 목 측정값이 일관되지 않습니다 — 다시 측정해 주세요.",
        "disclaimer": "추정치 — 의료 자문이 아닙니다. 캘리퍼, DEXA 스캔, 수중 측정이 더 정확합니다. 빠른 점검용으로만 사용하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>생물학적 성별을 선택하세요.</li>"
            "<li>목 둘레는 후두 바로 아래 가장 좁은 부위에서 측정하세요.</li>"
            "<li>허리 둘레는 남성은 배꼽 위치, 여성은 가장 잘록한 부분에서 측정합니다. 숨을 참거나 배를 집어넣지 마세요.</li>"
            "<li>여성은 엉덩이의 가장 넓은 둘레도 측정합니다.</li>"
            "<li>키(cm)를 입력하고 <strong>계산</strong>을 누르세요.</li>"
            "</ol>"
            "<p><strong>공식 (미 해군)</strong>: 남성 BFP = 86.010·log<sub>10</sub>(허리 − 목) − 70.041·log<sub>10</sub>(키) + 36.76. 여성 BFP = 163.205·log<sub>10</sub>(허리 + 엉덩이 − 목) − 97.684·log<sub>10</sub>(키) − 78.387.</p>"
            "<p>해군 공식은 평균 체형에 대해 수중 측정 대비 ±3% 정확도 — BMI보다 체구성 평가에 낫지만 DEXA보다는 부정확합니다. 일관된 결과를 위해 아침 첫 측정을 권장합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_bmi": "BMI 계산기",
        "related_calorie": "칼로리 계산기",
        "related_unit": "단위 변환기",
        "related_date": "날짜 계산기",
        "card_blurb": "미 해군 둘레 측정법으로 체지방률을 즉시 추정 (키·목·허리 + 엉덩이)."
    },
    "ja": {
        "title": "体脂肪率計算機",
        "meta_title": "体脂肪率計算機 — 米海軍式周囲法 - Utilify",
        "meta_desc": "身長・首・腹回り(女性はヒップも)から体脂肪率を米海軍公式で推定。カテゴリと推奨範囲も表示。",
        "og_title": "体脂肪率計算機 - Utilify",
        "og_desc": "米海軍周囲法で体脂肪率・カテゴリ・推奨範囲まで。",
        "json_name": "体脂肪率計算機",
        "json_desc": "米海軍の周囲測定公式で体脂肪率を推定しカテゴリを表示。",
        "page_desc": "身長と体周囲(首・腹、女性はヒップ追加)を入力すると、米海軍公式で体脂肪率を推定します。結果にはフィットネスカテゴリと性別別の推奨範囲も表示されます。",
        "label_sex": "性別",
        "label_height": "身長 (cm)",
        "label_neck": "首回り (cm)",
        "label_waist": "腹回り (cm)",
        "label_hip": "ヒップ回り (cm)",
        "ph_height": "170",
        "ph_neck": "37",
        "ph_waist": "85",
        "ph_hip": "95",
        "opt_male": "男性",
        "opt_female": "女性",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "体脂肪率: {value}% —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_bfp_label": "体脂肪率",
        "res_category_label": "カテゴリ",
        "res_range_label": "推奨範囲",
        "cat_essential": "必須脂肪",
        "cat_athletes": "アスリート",
        "cat_fitness": "フィットネス",
        "cat_average": "平均",
        "cat_obese": "肥満",
        "alert_invalid": "全ての測定値は正の数である必要があります。女性はヒップ回りが必須です。",
        "alert_negative_log": "腹と首の測定値が整合しません — もう一度測定してください。",
        "disclaimer": "推定値です — 医療助言ではありません。キャリパー、DEXAスキャン、水中計量法のほうが正確です。簡易チェック用としてのみご利用ください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>生物学的性別を選びます。</li>"
            "<li>首回りは喉仏のすぐ下、最も細い部分で測定します。</li>"
            "<li>腹回りは男性はへその位置、女性は最もくびれた部分で測定します。息を止めたりお腹を引っ込めたりしないでください。</li>"
            "<li>女性はヒップの最も広い周囲も測定します。</li>"
            "<li>身長(cm)を入力し<strong>計算</strong>を押します。</li>"
            "</ol>"
            "<p><strong>計算式 (米海軍)</strong>:男性 BFP = 86.010·log<sub>10</sub>(腹回り − 首回り) − 70.041·log<sub>10</sub>(身長) + 36.76。女性 BFP = 163.205·log<sub>10</sub>(腹回り + ヒップ − 首回り) − 97.684·log<sub>10</sub>(身長) − 78.387。</p>"
            "<p>海軍式は平均的な体型に対して水中計量と比べて±3%の精度 — BMIより体組成評価に優れますが、DEXAよりは不正確です。一貫した結果を得るために朝一の測定を推奨します。</p>"
        ),
        "related_header": "関連ツール",
        "related_bmi": "BMI計算機",
        "related_calorie": "カロリー計算機",
        "related_unit": "単位変換",
        "related_date": "日付計算機",
        "card_blurb": "米海軍周囲測定法で体脂肪率を即推定 (身長・首・腹 + ヒップ)。"
    }
}


FINANCE_HUB = {
    "en": {
        "title": "Finance Calculators",
        "meta_title": "Finance Calculators — Loan, Compound Interest, Retirement - Utilify",
        "meta_desc": "Free finance calculators that run entirely in your browser. Loan payments, compound interest projections, retirement nest-egg simulations. No signup, no upload.",
        "og_title": "Finance Calculators - Utilify",
        "og_desc": "Loan, compound interest, and retirement calculators — all client-side.",
        "json_name": "Finance Calculators",
        "json_desc": "Curated finance calculators for loans, savings, and retirement planning.",
        "h1": "Finance Calculators",
        "intro_html": (
            "<p>Money decisions reward curiosity. Whether you're shopping for a mortgage, "
            "deciding how much to save each month, or stress-testing a retirement plan, a "
            "good calculator turns a vague worry into a concrete number you can act on.</p>"
            "<p>The tools below cover the three financial questions most people return to "
            "again and again: <strong>What will this loan actually cost me?</strong> "
            "<strong>How much could my savings grow if I leave them alone?</strong> "
            "<strong>Will I run out of money in retirement?</strong> Every calculator runs "
            "in your browser — your inputs never leave the page, no account is required, "
            "and the formulas are documented on each page so you can verify the math.</p>"
            "<p>Treat these as decision-support tools, not advice. Real loans include fees "
            "and escrow; real returns are not constant; real retirement is messier than any "
            "smooth projection. Use the numbers as a sanity check, then talk to a qualified "
            "professional before locking in a major decision.</p>"
        ),
        "tools_header": "Tools in this category",
        "faq_header": "Frequently asked questions",
        "faq_html": (
            "<details><summary>Are these calculators a substitute for financial advice?</summary>"
            "<p>No. They use standard formulas and reasonable defaults, but they don't know your "
            "tax situation, debt mix, employer benefits, or risk tolerance. Use the output as a "
            "starting point for a conversation with a registered advisor or CPA.</p></details>"
            "<details><summary>Why does the calculated loan payment differ from my mortgage statement?</summary>"
            "<p>Lenders typically bundle property tax, homeowners insurance, PMI, and HOA fees "
            "into the monthly payment via escrow. The loan calculator only computes principal + "
            "interest. Add ~20–30% on top for a realistic all-in housing cost in most US markets.</p></details>"
            "<details><summary>What return rate should I assume for compound interest?</summary>"
            "<p>The S&amp;P 500 has averaged about 10% nominal / 7% real over the last century, "
            "but past performance is not a guarantee. For long-horizon planning, 6–7% real is a "
            "common conservative assumption; for short horizons, treat market exposure as risky.</p></details>"
            "<details><summary>Can I trust these for retirement planning?</summary>"
            "<p>Use them as a sanity check, not a plan. The retirement calculator assumes a "
            "constant return rate, which masks <em>sequence-of-returns risk</em> — a bad first "
            "few years of retirement can sink an otherwise viable plan. A Monte Carlo simulator "
            "or a flat-fee planner is better for high-stakes decisions.</p></details>"
        ),
        "related_header": "Other calculators",
        "related_other_hub": "Health Calculators",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Loan, compound interest, and retirement calculators — all client-side."
    },
    "ko": {
        "title": "금융 계산기 모음",
        "meta_title": "금융 계산기 — 대출·복리·은퇴 시뮬레이션 - Utilify",
        "meta_desc": "브라우저에서 모두 실행되는 무료 금융 계산기. 대출 월 상환, 복리 투자 성장, 은퇴자금 시뮬레이션. 가입·업로드 없음.",
        "og_title": "금융 계산기 - Utilify",
        "og_desc": "대출·복리·은퇴 계산기 — 모두 클라이언트 사이드.",
        "json_name": "금융 계산기 모음",
        "json_desc": "대출·저축·은퇴 계획을 위한 금융 계산기 큐레이션.",
        "h1": "금융 계산기",
        "intro_html": (
            "<p>돈에 관한 결정은 \"막연한 걱정\"을 \"행동 가능한 숫자\"로 바꿀 때 가장 좋습니다. "
            "주택담보대출을 알아보거나, 매달 얼마 저축해야 할지 고민하거나, 은퇴자금이 충분한지 "
            "검산할 때 — 좋은 계산기는 그 결정을 구체화해 줍니다.</p>"
            "<p>아래 도구들은 사람들이 가장 자주 마주치는 세 가지 질문을 다룹니다: "
            "<strong>이 대출은 실제로 얼마를 부담하는가?</strong> "
            "<strong>지금 저축하면 시간이 흘러 얼마가 되는가?</strong> "
            "<strong>은퇴 후 자금이 기대수명까지 버틸까?</strong> 모든 계산은 브라우저에서만 "
            "이루어지며 — 입력 데이터가 서버로 전송되지 않습니다. 가입 불필요, 사용된 공식은 "
            "각 페이지에 명시되어 있어 직접 검증할 수 있습니다.</p>"
            "<p>의사결정 보조 도구로 쓰세요 — 자문이 아닙니다. 실제 대출에는 수수료·보증료가 "
            "추가되고, 실제 수익률은 일정하지 않으며, 실제 은퇴는 어떤 부드러운 시뮬레이션보다 "
            "복잡합니다. 결과를 검산용으로 사용한 뒤, 중대한 결정 전에는 자격 있는 전문가와 "
            "상의하세요.</p>"
        ),
        "tools_header": "이 카테고리의 도구",
        "faq_header": "자주 묻는 질문",
        "faq_html": (
            "<details><summary>이 계산기들이 재정 자문을 대체할 수 있나요?</summary>"
            "<p>아니요. 표준 공식과 합리적인 기본값을 사용하지만, 사용자의 세금 상황·부채 "
            "구성·복리후생·위험 감수도를 알 수 없습니다. 결과는 자격 있는 재무 자문가 또는 "
            "세무사와의 대화 시작점으로 활용하세요.</p></details>"
            "<details><summary>계산된 대출 상환금이 실제 명세서와 다른 이유는?</summary>"
            "<p>금융기관은 재산세·주택보험·PMI·관리비 등을 월 상환금에 포함시켜 에스크로 형태로 "
            "처리하는 경우가 많습니다. 본 계산기는 원리금만 계산합니다. 한국 시장에서는 인지세·"
            "근저당설정비·보증료·중도상환수수료를 추가로 고려해야 실제 부담에 가깝습니다.</p></details>"
            "<details><summary>복리 계산에 어떤 수익률을 가정해야 하나요?</summary>"
            "<p>S&amp;P 500 100년 평균은 명목 약 10%, 실질 약 7%입니다. 과거 수익률이 미래를 "
            "보장하지는 않습니다. 장기 계획에는 실질 6~7%가 보수적 기준이며, 단기 자금은 시장 "
            "노출을 위험하게 봐야 합니다.</p></details>"
            "<details><summary>은퇴 계획에 사용해도 되나요?</summary>"
            "<p>검산용으로만 사용하세요. 은퇴 계산기는 일정한 수익률을 가정하므로 <em>시퀀스 "
            "리스크</em>(은퇴 초기 몇 년의 수익률 순서가 결과에 미치는 큰 영향)를 반영하지 "
            "못합니다. 중대한 결정에는 몬테카를로 시뮬레이터 또는 정액제 재무 자문가가 적합합니다."
            "</p></details>"
        ),
        "related_header": "다른 계산기",
        "related_other_hub": "건강 계산기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "대출·복리·은퇴 계산기 — 모두 브라우저에서."
    },
    "ja": {
        "title": "金融計算機",
        "meta_title": "金融計算機 — ローン・複利・老後資金 - Utilify",
        "meta_desc": "ブラウザで完全動作する無料の金融計算機。ローン返済額・複利による投資成長・老後資金シミュレーション。登録不要、アップロード不要。",
        "og_title": "金融計算機 - Utilify",
        "og_desc": "ローン・複利・老後資金計算機 — すべてクライアントサイド。",
        "json_name": "金融計算機",
        "json_desc": "ローン・貯蓄・老後計画向けの金融計算機コレクション。",
        "h1": "金融計算機",
        "intro_html": (
            "<p>お金の決断は「漠然とした不安」を「行動できる具体的な数字」に変えるとうまくいきます。"
            "住宅ローンを検討したり、毎月いくら貯めるか考えたり、老後資金が十分か確かめたりするとき、"
            "良い計算機はその決断を明確にしてくれます。</p>"
            "<p>以下のツールは多くの人が繰り返し直面する3つの財務的な質問を扱います: "
            "<strong>このローンは実際にいくらかかるのか？</strong> "
            "<strong>今貯蓄すると時間が経てばどのくらいになるのか？</strong> "
            "<strong>老後資金は平均余命まで持つのか？</strong> すべての計算はブラウザ内で行われ、"
            "入力データはページ外に送信されません。登録不要、使用された計算式は各ページに明記されており直接検証できます。</p>"
            "<p>意思決定のサポートツールとして使用してください — アドバイスではありません。"
            "実際のローンには手数料や諸費用が加わり、実際のリターンは一定ではなく、実際の老後は"
            "どんなスムーズなシミュレーションよりも複雑です。数字を目安として使用した後、重要な"
            "決断の前には資格を持つ専門家にご相談ください。</p>"
        ),
        "tools_header": "このカテゴリーのツール",
        "faq_header": "よくある質問",
        "faq_html": (
            "<details><summary>これらの計算機は金融アドバイスの代わりになりますか？</summary>"
            "<p>なりません。標準的な計算式と合理的なデフォルト値を使用していますが、あなたの税務状況・"
            "債務構成・福利厚生・リスク許容度はわかりません。結果は登録ファイナンシャルアドバイザーや"
            "CPAとの会話の出発点として活用してください。</p></details>"
            "<details><summary>計算されたローン返済額が実際の明細書と異なる理由は？</summary>"
            "<p>金融機関は固定資産税・住宅保険・PMI・管理費などをエスクロー経由で月払いに含める場合が"
            "多いです。このローン計算機は元金＋利息のみを計算します。実際の住宅費用には20〜30%程度"
            "加算した金額を目安にしてください。</p></details>"
            "<details><summary>複利計算にどの利率を仮定すべきですか？</summary>"
            "<p>S&amp;P 500の過去100年の平均は名目約10%・実質約7%ですが、過去の実績は将来を保証しません。"
            "長期計画では実質6〜7%が保守的な一般的仮定です。短期資金には市場リスクがあります。</p></details>"
            "<details><summary>老後計画にこれらを使っても大丈夫ですか？</summary>"
            "<p>目安として使用してください。老後資金計算機は一定の利回りを仮定するため、<em>リターン順序"
            "リスク</em>（退職後最初の数年の悪い利回りが計画全体を狂わせる）が反映されていません。"
            "重要な決断にはモンテカルロシミュレーターまたは定額制のファイナンシャルプランナーの方が"
            "適しています。</p></details>"
        ),
        "related_header": "他の計算機",
        "related_other_hub": "健康計算機",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算機",
        "related_unit": "単位変換",
        "card_blurb": "ローン・複利・老後資金計算機 — すべてクライアントサイド。"
    }
}


HEALTH_HUB = {
    "en": {
        "title": "Health Calculators",
        "meta_title": "Health Calculators — Calorie, Pregnancy, Body Fat - Utilify",
        "meta_desc": "Free health calculators that run entirely in your browser. BMR + TDEE, pregnancy due date, body fat percentage. No signup, no upload.",
        "og_title": "Health Calculators - Utilify",
        "og_desc": "Calorie, pregnancy, and body fat calculators — all client-side.",
        "json_name": "Health Calculators",
        "json_desc": "Curated health calculators for nutrition, pregnancy, and body composition.",
        "h1": "Health Calculators",
        "intro_html": (
            "<p>Bodies don't come with a dashboard. The next-best thing is a small set of "
            "calculators that translate measurements into context: how much you can eat without "
            "gaining weight, when a baby is due, where your body composition sits relative to a "
            "typical range. None of these replace a doctor — they help you ask better questions "
            "the next time you see one.</p>"
            "<p>The tools below address three of the most-searched health questions: "
            "<strong>How many calories do I actually need?</strong> "
            "<strong>When is my baby due, and what trimester am I in?</strong> "
            "<strong>What's my body fat percentage?</strong> Each runs entirely in your browser, "
            "uses widely-cited formulas (Mifflin-St Jeor, Naegele's rule, US Navy method), and "
            "shows the math on each page so you can verify it.</p>"
            "<p>Use these as quick checks. For pregnancy, an early ultrasound dating scan is more "
            "accurate. For body fat, DEXA or hydrostatic weighing is the gold standard. For "
            "nutrition, an RD can personalize beyond what any one-size-fits-all formula can "
            "produce.</p>"
        ),
        "tools_header": "Tools in this category",
        "faq_header": "Frequently asked questions",
        "faq_html": (
            "<details><summary>Which BMR formula is the most accurate?</summary>"
            "<p>Mifflin-St Jeor (used here) outperforms the older Harris-Benedict and Katch-McArdle "
            "for healthy adults across most studies. Margin of error is roughly ±10% — fine for "
            "planning, less fine for clinical use.</p></details>"
            "<details><summary>Is BMI alone enough to assess health?</summary>"
            "<p>No. BMI doesn't distinguish muscle from fat, ignores fat distribution, and "
            "performs poorly for athletes and the elderly. The body fat calculator (US Navy "
            "method) is a better composition signal; combine with a waist-to-hip ratio for "
            "cardiovascular risk.</p></details>"
            "<details><summary>Why doesn't my pregnancy due date match my doctor's estimate?</summary>"
            "<p>The calculator uses Naegele's rule (LMP + 280 days) with a cycle-length "
            "adjustment. If your cycles are irregular or your LMP is uncertain, an early "
            "ultrasound is more accurate and is what your doctor likely uses.</p></details>"
            "<details><summary>Should I aim for the lowest body fat possible?</summary>"
            "<p>No — there's a healthy range, not a minimum. Men below ~6% and women below ~14% "
            "is essential-fat territory and not safe to maintain. Athletes optimize for performance, "
            "not the lowest number.</p></details>"
        ),
        "related_header": "Other calculators",
        "related_other_hub": "Finance Calculators",
        "related_bmi": "BMI Calculator",
        "related_date": "Date Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Calorie, pregnancy, and body-fat calculators — all client-side."
    },
    "ko": {
        "title": "건강 계산기 모음",
        "meta_title": "건강 계산기 — 칼로리·임신·체지방 - Utilify",
        "meta_desc": "브라우저에서 모두 실행되는 무료 건강 계산기. BMR·TDEE 칼로리, 임신 출산예정일, 체지방률. 가입·업로드 없음.",
        "og_title": "건강 계산기 - Utilify",
        "og_desc": "칼로리·임신·체지방 계산기 — 모두 클라이언트 사이드.",
        "json_name": "건강 계산기 모음",
        "json_desc": "영양·임신·체구성을 위한 건강 계산기 큐레이션.",
        "h1": "건강 계산기",
        "intro_html": (
            "<p>몸에는 대시보드가 없습니다. 그래서 측정값을 맥락으로 바꿔 주는 작은 계산기들이 "
            "유용합니다 — 체중을 유지하려면 얼마나 먹어도 되는지, 출산일이 언제인지, 체지방률이 "
            "정상 범위 어디쯤인지. 의사를 대체하지는 않지만, 다음 진료에서 더 좋은 질문을 할 수 "
            "있게 도와줍니다.</p>"
            "<p>아래 도구들은 가장 많이 검색되는 세 가지 건강 질문을 다룹니다: "
            "<strong>나에게 필요한 칼로리는 몇 kcal인가?</strong> "
            "<strong>출산예정일은 언제이고 지금 몇 주차인가?</strong> "
            "<strong>내 체지방률은 얼마인가?</strong> 모두 브라우저에서만 동작하며, 널리 인용되는 "
            "공식(Mifflin-St Jeor, Naegele 법칙, 미 해군 둘레 측정법)을 사용하고, 각 페이지에 "
            "계산 과정이 명시되어 있어 직접 검증할 수 있습니다.</p>"
            "<p>빠른 점검용으로 사용하세요. 임신 주수는 1삼분기 초음파가 더 정확하고, 체지방률은 "
            "DEXA·수중 측정이 표준이며, 영양은 임상영양사가 어떤 공식보다도 개인화된 조언을 줄 수 "
            "있습니다.</p>"
        ),
        "tools_header": "이 카테고리의 도구",
        "faq_header": "자주 묻는 질문",
        "faq_html": (
            "<details><summary>가장 정확한 BMR 공식은 무엇인가요?</summary>"
            "<p>본 계산기에서 사용하는 Mifflin-St Jeor가 대부분 연구에서 Harris-Benedict, "
            "Katch-McArdle보다 건강한 성인에게 더 정확합니다. 오차 범위는 약 ±10% — 계획용으로는 "
            "충분하지만 임상 진단용으로는 부족합니다.</p></details>"
            "<details><summary>BMI만으로 건강을 판단할 수 있나요?</summary>"
            "<p>아닙니다. BMI는 근육과 지방을 구분하지 못하고 지방 분포를 무시하며, 운동선수와 "
            "고령층에서 부정확합니다. 체지방 계산기(미 해군 공식)가 체구성 신호로 더 낫고, "
            "허리-엉덩이 비율과 함께 보면 심혈관 위험 평가에 도움이 됩니다.</p></details>"
            "<details><summary>출산예정일이 의사 진단과 다른 이유는?</summary>"
            "<p>본 계산기는 Naegele 법칙(LMP + 280일)에 생리주기 보정을 적용합니다. 생리가 "
            "불규칙하거나 LMP가 불확실하면 1삼분기 초음파가 더 정확하며, 의사는 보통 이 결과를 "
            "기준으로 삼습니다.</p></details>"
            "<details><summary>체지방률은 낮을수록 좋은 건가요?</summary>"
            "<p>아닙니다 — 건강한 범위가 있고 최소치가 있는 게 아닙니다. 남성 약 6% 미만, 여성 "
            "약 14% 미만은 필수 지방 영역으로 안전하게 유지할 수 없습니다. 운동선수도 최저 "
            "수치가 아닌 경기력에 맞춰 조절합니다.</p></details>"
        ),
        "related_header": "다른 계산기",
        "related_other_hub": "금융 계산기",
        "related_bmi": "BMI 계산기",
        "related_date": "날짜 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "칼로리·임신·체지방 계산기 — 모두 브라우저에서."
    },
    "ja": {
        "title": "健康計算機",
        "meta_title": "健康計算機 — カロリー・妊娠・体脂肪率 - Utilify",
        "meta_desc": "ブラウザで完全動作する無料の健康計算機。BMR＋TDEE・妊娠出産予定日・体脂肪率。登録不要、アップロード不要。",
        "og_title": "健康計算機 - Utilify",
        "og_desc": "カロリー・妊娠・体脂肪計算機 — すべてクライアントサイド。",
        "json_name": "健康計算機",
        "json_desc": "栄養・妊娠・体組成のための健康計算機コレクション。",
        "h1": "健康計算機",
        "intro_html": (
            "<p>身体にはダッシュボードがありません。測定値を文脈に変えてくれる小さな計算機セットが"
            "次善の策です。体重を維持しながらどれだけ食べられるか、赤ちゃんの出産予定日はいつか、"
            "体組成が標準的な範囲のどこに位置するか。これらは医師の代わりにはなりませんが、次の"
            "診察でより良い質問をするための助けになります。</p>"
            "<p>以下のツールは最もよく検索される3つの健康上の質問を扱います: "
            "<strong>実際に必要なカロリーはどのくらいか？</strong> "
            "<strong>出産予定日はいつで、現在何週目か？</strong> "
            "<strong>体脂肪率はいくらか？</strong> いずれもブラウザ内で動作し、"
            "広く引用される計算式（Mifflin-St Jeor・ネーゲレ法則・米海軍法）を使用して、"
            "各ページに計算過程が明記されているので直接検証できます。</p>"
            "<p>簡易チェックとして使用してください。妊娠週数は第1トリメスターの超音波検査の方が"
            "正確です。体脂肪率はDEXAや水中体重測定が標準です。栄養については管理栄養士が"
            "どんな一般式よりも個人に合ったアドバイスができます。</p>"
        ),
        "tools_header": "このカテゴリーのツール",
        "faq_header": "よくある質問",
        "faq_html": (
            "<details><summary>最も正確なBMR計算式はどれですか？</summary>"
            "<p>ここで使用しているMifflin-St Jeorは、ほとんどの研究で健康な成人に対して古いHarris-Benedict"
            "やKatch-McArdleより優れています。誤差範囲は約±10% — 計画用には十分ですが、臨床診断用には"
            "不十分です。</p></details>"
            "<details><summary>BMIだけで健康を判断できますか？</summary>"
            "<p>できません。BMIは筋肉と脂肪を区別せず、脂肪分布を無視し、アスリートや高齢者では"
            "不正確です。体脂肪計算機（米海軍法）の方が体組成の指標として優れており、ウエスト・"
            "ヒップ比と組み合わせると心血管リスク評価に役立ちます。</p></details>"
            "<details><summary>出産予定日が医師の推定と異なる理由は？</summary>"
            "<p>この計算機はネーゲレ法則（LMP + 280日）に生理周期補正を適用しています。生理周期が"
            "不規則またはLMPが不確かな場合は、第1トリメスターの超音波検査の方が正確で、医師も通常"
            "それを基準にします。</p></details>"
            "<details><summary>体脂肪率は低ければ低いほど良いですか？</summary>"
            "<p>いいえ — 健康な範囲があり、最小値ではありません。男性で約6%未満、女性で約14%未満は"
            "必須脂肪の領域で安全に維持できません。アスリートも最低値ではなくパフォーマンスに合わせて"
            "調整します。</p></details>"
        ),
        "related_header": "他の計算機",
        "related_other_hub": "金融計算機",
        "related_bmi": "BMI計算機",
        "related_date": "日付計算機",
        "related_unit": "単位変換",
        "card_blurb": "カロリー・妊娠・体脂肪計算機 — すべてクライアントサイド。"
    }
}


RAG_CHUNKER = {
    "en": {
        "title": "RAG Text Chunker",
        "meta_title": "RAG Text Chunker — Sliding Window Chunks for Embeddings - Utilify",
        "meta_desc": "Split text into overlapping chunks for RAG / embedding pipelines. Configurable size and overlap, character or token-estimate mode. Runs entirely in your browser.",
        "og_title": "RAG Text Chunker - Utilify",
        "og_desc": "Split text into chunks with overlap for embedding-based retrieval pipelines.",
        "json_name": "RAG Text Chunker",
        "json_desc": "Sliding-window text chunker for retrieval-augmented generation pipelines.",
        "page_desc": "Paste a long document and split it into overlapping chunks for embedding-based retrieval. Pick chunks-by-characters for predictable size or chunks-by-token-estimate for closer alignment with embedding model limits. All processing happens in your browser.",
        "label_text": "Source text",
        "label_size": "Chunk size",
        "label_overlap": "Overlap",
        "label_mode": "Unit",
        "ph_text": "Paste the document you want to chunk…",
        "ph_size": "512",
        "ph_overlap": "50",
        "opt_chars": "Characters",
        "opt_tokens": "Tokens (estimated)",
        "btn_chunk": "Chunk",
        "btn_reset": "Reset",
        "btn_copy_all": "Copy all (JSON)",
        "btn_share": "Share result",
        "share_text": "I split a {value}-character document into chunks —",
        "share_copied": "Copied to clipboard.",
        "copied_one": "Chunk copied.",
        "res_count_label": "Chunks",
        "res_total_label": "Source size",
        "res_avg_label": "Avg chunk size",
        "chunk_label": "Chunk",
        "alert_invalid": "Enter source text and a chunk size larger than overlap.",
        "disclaimer": "Token mode is an approximate (~4 chars/token English, ~1.5 chars/token CJK). For exact tokenization, use the embedding model's tokenizer.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Paste your source document.</li>"
            "<li>Pick chunk size and overlap. Common starting points: 512 chunk / 50 overlap (chars), or 256 / 32 (tokens).</li>"
            "<li>Choose <em>characters</em> for predictable byte-size or <em>tokens</em> to align with embedding model context limits.</li>"
            "<li>Click <strong>Chunk</strong>. Each chunk is numbered with byte length; click any chunk to copy it, or use <strong>Copy all (JSON)</strong> to grab the whole array.</li>"
            "</ol>"
            "<p><strong>Why overlap?</strong> Overlap preserves context across chunk boundaries — a sentence split mid-thought won't lose its anchor. Common ratio: overlap = 10–20% of chunk size.</p>"
            "<p>Splitting strategy is plain sliding window; no semantic boundary detection. For prose, that's usually fine. For code or structured documents, consider a parser-aware splitter.</p>"
        ),
        "related_header": "Related Tools",
        "related_token": "Token Counter",
        "related_pii": "Prompt PII Scrubber",
        "related_chatgpt": "ChatGPT to Blog",
        "related_md": "Markdown Previewer",
        "card_blurb": "Sliding-window text chunker for embeddings & RAG pipelines."
    },
    "ko": {
        "title": "RAG 텍스트 청크 분할기",
        "meta_title": "RAG 청크 분할기 — 임베딩용 슬라이딩 윈도우 분할 - Utilify",
        "meta_desc": "RAG·임베딩 파이프라인을 위한 텍스트를 겹침 가능한 청크로 분할. 크기·겹침 설정 가능, 문자/토큰 모드 지원. 모든 처리는 브라우저에서.",
        "og_title": "RAG 텍스트 청크 분할기 - Utilify",
        "og_desc": "임베딩 기반 검색 파이프라인용 텍스트를 겹침 청크로 분할.",
        "json_name": "RAG 텍스트 청크 분할기",
        "json_desc": "검색 증강 생성(RAG) 파이프라인을 위한 슬라이딩 윈도우 텍스트 분할기.",
        "page_desc": "긴 문서를 임베딩 기반 검색용 겹침 청크로 분할합니다. 일정한 크기를 위해 문자 모드를, 임베딩 모델 컨텍스트 한계에 맞추려면 토큰 모드를 선택하세요. 모든 처리는 브라우저에서 이루어집니다.",
        "label_text": "원본 텍스트",
        "label_size": "청크 크기",
        "label_overlap": "겹침 크기",
        "label_mode": "단위",
        "ph_text": "분할할 문서를 붙여넣으세요…",
        "ph_size": "512",
        "ph_overlap": "50",
        "opt_chars": "문자",
        "opt_tokens": "토큰 (추정)",
        "btn_chunk": "분할",
        "btn_reset": "초기화",
        "btn_copy_all": "전체 복사 (JSON)",
        "btn_share": "결과 공유",
        "share_text": "{value}자 문서를 청크로 분할했습니다 —",
        "share_copied": "클립보드에 복사되었습니다.",
        "copied_one": "청크가 복사되었습니다.",
        "res_count_label": "청크 수",
        "res_total_label": "원본 크기",
        "res_avg_label": "평균 청크 크기",
        "chunk_label": "청크",
        "alert_invalid": "원본 텍스트와 겹침보다 큰 청크 크기를 입력하세요.",
        "disclaimer": "토큰 모드는 근사치입니다(영문 약 4자/토큰, 한·중·일 약 1.5자/토큰). 정확한 토큰화는 사용하시는 임베딩 모델의 토크나이저를 이용하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>원본 문서를 붙여넣으세요.</li>"
            "<li>청크 크기와 겹침을 입력하세요. 흔한 시작값: 문자 모드 512/50, 토큰 모드 256/32.</li>"
            "<li>일정한 바이트 크기를 원하면 <em>문자</em>, 임베딩 모델 컨텍스트 한계에 맞추려면 <em>토큰</em>을 선택하세요.</li>"
            "<li><strong>분할</strong>을 누르면 청크가 번호와 길이로 표시됩니다. 각 청크 클릭으로 개별 복사, <strong>전체 복사 (JSON)</strong>로 배열 전체를 복사할 수 있습니다.</li>"
            "</ol>"
            "<p><strong>왜 겹침이 필요한가?</strong> 청크 경계에서 문맥이 끊기는 것을 방지합니다 — 한 문장이 두 청크에 걸치더라도 양쪽에서 일부 맥락이 유지됩니다. 일반적으로 청크 크기의 10~20%를 겹침으로 설정합니다.</p>"
            "<p>분할 방식은 단순 슬라이딩 윈도우입니다 — 의미 단위 인식은 하지 않습니다. 일반 산문에는 충분하지만 코드·구조 문서에는 파서 기반 분할기를 권장합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_token": "토큰 카운터",
        "related_pii": "프롬프트 PII 마스킹",
        "related_chatgpt": "ChatGPT 블로그 변환",
        "related_md": "Markdown 프리뷰어",
        "card_blurb": "임베딩·RAG 파이프라인을 위한 슬라이딩 윈도우 텍스트 청크 분할기."
    },
    "ja": {
        "title": "RAGテキストチャンカー",
        "meta_title": "RAGテキストチャンカー — 埋め込み用スライディングウィンドウ分割 - Utilify",
        "meta_desc": "RAG・埋め込みパイプライン用にテキストを重複チャンクに分割します。サイズ・重複設定可能、文字/トークンモード対応。すべてブラウザで処理。",
        "og_title": "RAGテキストチャンカー - Utilify",
        "og_desc": "埋め込みベースの検索パイプライン用に重複チャンクでテキストを分割します。",
        "json_name": "RAGテキストチャンカー",
        "json_desc": "検索拡張生成（RAG）パイプライン向けのスライディングウィンドウ式テキスト分割ツール。",
        "page_desc": "長いドキュメントを埋め込みベースの検索用に重複チャンクへ分割します。一定のサイズが必要な場合は文字モード、埋め込みモデルのコンテキスト制限に合わせるにはトークンモードを選択してください。すべてブラウザ内で処理されます。",
        "label_text": "元のテキスト",
        "label_size": "チャンクサイズ",
        "label_overlap": "重複サイズ",
        "label_mode": "単位",
        "ph_text": "分割するドキュメントを貼り付けてください…",
        "ph_size": "512",
        "ph_overlap": "50",
        "opt_chars": "文字",
        "opt_tokens": "トークン（推定）",
        "btn_chunk": "分割",
        "btn_reset": "リセット",
        "btn_copy_all": "すべてコピー (JSON)",
        "btn_share": "結果を共有",
        "share_text": "{value}文字のドキュメントをチャンクに分割しました —",
        "share_copied": "クリップボードにコピーしました。",
        "copied_one": "チャンクをコピーしました。",
        "res_count_label": "チャンク数",
        "res_total_label": "元のサイズ",
        "res_avg_label": "平均チャンクサイズ",
        "chunk_label": "チャンク",
        "alert_invalid": "元のテキストと、重複サイズより大きいチャンクサイズを入力してください。",
        "disclaimer": "トークンモードは近似値です（英語約4文字/トークン、CJK約1.5文字/トークン）。正確なトークン化には使用する埋め込みモデルのトークナイザーを利用してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>元のドキュメントを貼り付けます。</li>"
            "<li>チャンクサイズと重複を入力します。よくある開始値: 文字モード512/50、トークンモード256/32。</li>"
            "<li>一定のバイトサイズが必要な場合は<em>文字</em>、埋め込みモデルのコンテキスト制限に合わせるには<em>トークン</em>を選択します。</li>"
            "<li><strong>分割</strong>をクリックするとチャンクが番号とサイズとともに表示されます。各チャンクをクリックして個別コピー、または<strong>すべてコピー（JSON）</strong>で配列全体を取得できます。</li>"
            "</ol>"
            "<p><strong>なぜ重複が必要か？</strong> チャンク境界でのコンテキスト断絶を防ぎます — 途中で切れた文でもアンカーを失いません。一般的な比率: 重複 = チャンクサイズの10〜20%。</p>"
            "<p>分割方式は単純なスライディングウィンドウで、意味的な境界検出は行いません。一般的な文章では通常問題ありません。コードや構造文書にはパーサーベースの分割ツールを検討してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_token": "トークンカウンター",
        "related_pii": "プロンプトPIIスクラバー",
        "related_chatgpt": "ChatGPTブログ変換",
        "related_md": "Markdownプレビュー",
        "card_blurb": "埋め込み・RAGパイプライン向けのスライディングウィンドウ式テキスト分割。"
    }
}


FEW_SHOT_FORMATTER = {
    "en": {
        "title": "Few-Shot Prompt Formatter",
        "meta_title": "Few-Shot Prompt Formatter — Markdown / XML / OpenAI JSON - Utilify",
        "meta_desc": "Format input/output examples as a few-shot prompt. Output as Markdown, Anthropic XML tags, OpenAI messages JSON, or plain text. Runs in your browser.",
        "og_title": "Few-Shot Prompt Formatter - Utilify",
        "og_desc": "Format examples as a clean few-shot prompt for ChatGPT, Claude, or your own pipeline.",
        "json_name": "Few-Shot Prompt Formatter",
        "json_desc": "Convert input/output example pairs into a formatted few-shot prompt.",
        "page_desc": "Add a system instruction and a list of input → output examples. The tool emits a clean few-shot prompt in Markdown, Anthropic-style XML tags, OpenAI messages JSON, or plain text — ready to paste into ChatGPT, Claude, or a script.",
        "label_system": "System instruction (optional)",
        "label_input": "Input",
        "label_output": "Output",
        "label_format": "Output format",
        "ph_system": "You are a helpful assistant. Answer questions concisely.",
        "ph_input": "User message",
        "ph_output": "Expected reply",
        "opt_md": "Markdown",
        "opt_xml": "Anthropic XML tags",
        "opt_json": "OpenAI messages JSON",
        "opt_plain": "Plain text",
        "btn_add_pair": "+ Add example",
        "btn_remove_pair": "Remove",
        "btn_format": "Format",
        "btn_reset": "Reset",
        "btn_copy": "Copy",
        "btn_share": "Share result",
        "share_text": "I built a few-shot prompt with {value} examples —",
        "share_copied": "Result copied to clipboard.",
        "copied": "Copied.",
        "res_label": "Formatted prompt",
        "alert_no_pairs": "Add at least one input/output example.",
        "disclaimer": "The tool reformats your text — it does not call any AI provider. Review the output before sending to a paid API.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>(Optional) Paste a system instruction that defines the task or persona.</li>"
            "<li>Click <strong>+ Add example</strong> to add input/output pairs. 3–5 examples is typical for few-shot.</li>"
            "<li>Pick the output format:"
            "<ul>"
            "<li><strong>Markdown</strong> — readable, good for chat UIs.</li>"
            "<li><strong>XML tags</strong> — Anthropic recommends <code>&lt;example&gt;</code> tags around each pair for Claude.</li>"
            "<li><strong>OpenAI messages JSON</strong> — array of <code>{role, content}</code> objects, ready for the Chat Completions API.</li>"
            "<li><strong>Plain</strong> — minimal, no markup.</li>"
            "</ul></li>"
            "<li>Click <strong>Format</strong> and copy the result.</li>"
            "</ol>"
            "<p>For Claude / Anthropic, XML tags consistently improve adherence to the example structure. For ChatGPT, Markdown or messages JSON usually works best. The OpenAI format alternates user/assistant turns for each pair, which the API treats as conversation history.</p>"
        ),
        "related_header": "Related Tools",
        "related_token": "Token Counter",
        "related_pii": "Prompt PII Scrubber",
        "related_chatgpt": "ChatGPT to Blog",
        "related_claude": "Claude.md Generator",
        "card_blurb": "Format input/output examples as a few-shot prompt — Markdown, XML, or OpenAI JSON."
    },
    "ko": {
        "title": "Few-Shot 프롬프트 포매터",
        "meta_title": "Few-Shot 프롬프트 포매터 — Markdown·XML·OpenAI JSON - Utilify",
        "meta_desc": "입력/출력 예시를 Few-shot 프롬프트로 포맷. Markdown, Anthropic XML 태그, OpenAI messages JSON, 일반 텍스트로 출력. 모든 처리는 브라우저에서.",
        "og_title": "Few-Shot 프롬프트 포매터 - Utilify",
        "og_desc": "ChatGPT·Claude·자체 파이프라인용 Few-shot 프롬프트를 깔끔하게 정리.",
        "json_name": "Few-Shot 프롬프트 포매터",
        "json_desc": "입력/출력 예시 쌍을 Few-shot 프롬프트 형식으로 변환합니다.",
        "page_desc": "시스템 지시와 입력→출력 예시 목록을 입력하면, Markdown, Anthropic XML 태그, OpenAI messages JSON, 또는 일반 텍스트 형식의 깔끔한 Few-shot 프롬프트로 변환합니다 — ChatGPT·Claude·스크립트에 바로 붙여넣을 수 있습니다.",
        "label_system": "시스템 지시 (선택)",
        "label_input": "입력",
        "label_output": "출력",
        "label_format": "출력 형식",
        "ph_system": "친절하고 간결하게 답하는 어시스턴트입니다.",
        "ph_input": "사용자 메시지",
        "ph_output": "기대하는 답변",
        "opt_md": "Markdown",
        "opt_xml": "Anthropic XML 태그",
        "opt_json": "OpenAI messages JSON",
        "opt_plain": "일반 텍스트",
        "btn_add_pair": "+ 예시 추가",
        "btn_remove_pair": "삭제",
        "btn_format": "포맷",
        "btn_reset": "초기화",
        "btn_copy": "복사",
        "btn_share": "결과 공유",
        "share_text": "{value}개 예시로 Few-shot 프롬프트를 만들었습니다 —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "copied": "복사되었습니다.",
        "res_label": "포맷된 프롬프트",
        "alert_no_pairs": "최소 1개의 입력/출력 예시를 추가해 주세요.",
        "disclaimer": "이 도구는 텍스트를 재구성할 뿐, AI 제공자에 호출하지 않습니다. 유료 API에 보내기 전 결과를 반드시 검토하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>(선택) 작업이나 페르소나를 정의하는 시스템 지시를 입력하세요.</li>"
            "<li><strong>+ 예시 추가</strong>를 눌러 입력/출력 쌍을 추가합니다. Few-shot은 보통 3~5개가 적당합니다.</li>"
            "<li>출력 형식을 선택하세요:"
            "<ul>"
            "<li><strong>Markdown</strong> — 가독성이 좋고 채팅 UI에 어울립니다.</li>"
            "<li><strong>XML 태그</strong> — Anthropic은 Claude에 사용 시 각 예시를 <code>&lt;example&gt;</code> 태그로 감싸기를 권장합니다.</li>"
            "<li><strong>OpenAI messages JSON</strong> — <code>{role, content}</code> 배열, Chat Completions API에 그대로 전달 가능.</li>"
            "<li><strong>일반 텍스트</strong> — 마크업 없이 단순 형식.</li>"
            "</ul></li>"
            "<li><strong>포맷</strong> 후 결과를 복사하세요.</li>"
            "</ol>"
            "<p>Claude·Anthropic에는 XML 태그가 예시 구조 인식률을 일관되게 높입니다. ChatGPT에는 Markdown 또는 messages JSON이 일반적으로 더 잘 작동합니다. OpenAI 형식은 각 예시 쌍을 user/assistant 메시지로 번갈아 배열해 API가 대화 이력으로 처리하게 합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_token": "토큰 카운터",
        "related_pii": "프롬프트 PII 마스킹",
        "related_chatgpt": "ChatGPT 블로그 변환",
        "related_claude": "Claude.md 생성기",
        "card_blurb": "입력/출력 예시를 Few-shot 프롬프트로 — Markdown·XML·OpenAI JSON."
    },
    "ja": {
        "title": "Few-Shotプロンプトフォーマッター",
        "meta_title": "Few-Shotプロンプトフォーマッター — Markdown / XML / OpenAI JSON - Utilify",
        "meta_desc": "入力/出力例をFew-shotプロンプトとしてフォーマットします。Markdown・Anthropic XMLタグ・OpenAI messages JSON・プレーンテキスト出力に対応。ブラウザで動作。",
        "og_title": "Few-Shotプロンプトフォーマッター - Utilify",
        "og_desc": "ChatGPT・Claude・自分のパイプライン向けにFew-shotプロンプトをきれいに整形します。",
        "json_name": "Few-Shotプロンプトフォーマッター",
        "json_desc": "入力/出力の例ペアをFew-shotプロンプト形式に変換するツール。",
        "page_desc": "システム指示と入力→出力の例リストを追加すると、Markdown・Anthropicスタイルのタグ・OpenAI messages JSON・プレーンテキスト形式のFew-shotプロンプトを生成します — ChatGPT・Claude・スクリプトにそのまま貼り付けられます。",
        "label_system": "システム指示（任意）",
        "label_input": "入力",
        "label_output": "出力",
        "label_format": "出力形式",
        "ph_system": "親切で簡潔に答えるアシスタントです。",
        "ph_input": "ユーザーメッセージ",
        "ph_output": "期待する返答",
        "opt_md": "Markdown",
        "opt_xml": "Anthropic XMLタグ",
        "opt_json": "OpenAI messages JSON",
        "opt_plain": "プレーンテキスト",
        "btn_add_pair": "+ 例を追加",
        "btn_remove_pair": "削除",
        "btn_format": "フォーマット",
        "btn_reset": "リセット",
        "btn_copy": "コピー",
        "btn_share": "結果を共有",
        "share_text": "{value}件の例でFew-shotプロンプトを作成しました —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "copied": "コピーしました。",
        "res_label": "フォーマットされたプロンプト",
        "alert_no_pairs": "最低1組の入力/出力例を追加してください。",
        "disclaimer": "このツールはテキストを再フォーマットするだけで、AIプロバイダーには接続しません。有料APIに送信する前に結果を必ず確認してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>（任意）タスクやペルソナを定義するシステム指示を入力します。</li>"
            "<li><strong>+ 例を追加</strong>をクリックして入力/出力ペアを追加します。Few-shotには通常3〜5例が適切です。</li>"
            "<li>出力形式を選択してください:"
            "<ul>"
            "<li><strong>Markdown</strong> — 読みやすく、チャットUIに向いています。</li>"
            "<li><strong>XMLタグ</strong> — AnthropicはClaude向けに各ペアを<code>&lt;example&gt;</code>タグで囲むことを推奨しています。</li>"
            "<li><strong>OpenAI messages JSON</strong> — <code>{role, content}</code>オブジェクトの配列で、Chat Completions APIにそのまま渡せます。</li>"
            "<li><strong>プレーン</strong> — マークアップなしのシンプルな形式。</li>"
            "</ul></li>"
            "<li><strong>フォーマット</strong>をクリックして結果をコピーします。</li>"
            "</ol>"
            "<p>Claude/AnthropicにはXMLタグが例の構造遵守を一貫して改善します。ChatGPTにはMarkdownまたはmessages JSONが通常最適です。OpenAI形式は各ペアをuser/assistantターンで交互に配置し、APIが会話履歴として処理します。</p>"
        ),
        "related_header": "関連ツール",
        "related_token": "トークンカウンター",
        "related_pii": "プロンプトPIIスクラバー",
        "related_chatgpt": "ChatGPTブログ変換",
        "related_claude": "Claude.mdジェネレーター",
        "card_blurb": "入力/出力例をFew-shotプロンプトに — Markdown・XML・OpenAI JSON。"
    }
}


JSON_SCHEMA_VALIDATOR = {
    "en": {
        "title": "JSON Schema Validator",
        "meta_title": "JSON Schema Validator — Validate JSON Against a Schema - Utilify",
        "meta_desc": "Validate JSON data against a JSON Schema in your browser. Supports type, properties, required, items, enum, format, pattern, min/max. No upload, no signup.",
        "og_title": "JSON Schema Validator - Utilify",
        "og_desc": "Validate JSON against a schema. Errors include the JSONPath of every failure.",
        "json_name": "JSON Schema Validator",
        "json_desc": "Client-side JSON Schema validator covering core JSON Schema 2020-12 keywords.",
        "page_desc": "Paste your JSON data and a JSON Schema. The validator checks type, required, properties, items, enum, format, pattern, and min/max constraints, and reports each failure with the JSONPath where it occurred. All processing in your browser.",
        "label_data": "JSON data",
        "label_schema": "JSON Schema",
        "ph_data": "{\n  \"name\": \"Alice\",\n  \"age\": 30\n}",
        "ph_schema": "{\n  \"type\": \"object\",\n  \"required\": [\"name\"],\n  \"properties\": {\n    \"name\": {\"type\": \"string\"}\n  }\n}",
        "btn_validate": "Validate",
        "btn_reset": "Reset",
        "btn_load_sample": "Load sample",
        "btn_share": "Share result",
        "share_text": "JSON validation: {value} —",
        "share_copied": "Result copied to clipboard.",
        "res_valid": "✓ Valid against schema.",
        "res_invalid_header": "✗ Validation errors",
        "res_error_count": "{count} error(s) at:",
        "alert_data_invalid": "Data is not valid JSON: ",
        "alert_schema_invalid": "Schema is not valid JSON: ",
        "disclaimer": "Implements a useful subset of JSON Schema 2020-12 (type, properties, required, items, enum, const, format, pattern, min/max for strings/numbers/arrays). Advanced keywords like $ref, allOf/anyOf/oneOf, dependentSchemas, and prefixItems are not supported — for those, use a server-side validator like ajv.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Paste your JSON data into the left panel.</li>"
            "<li>Paste the JSON Schema you want to validate against into the right panel. Click <strong>Load sample</strong> for a worked example.</li>"
            "<li>Click <strong>Validate</strong>. If the data passes, you see a green check. Otherwise each error is listed with the JSONPath where it occurred (e.g., <code>$.user.email</code>).</li>"
            "</ol>"
            "<p><strong>Supported keywords</strong>: <code>type</code> (string, number, integer, boolean, object, array, null), <code>properties</code>, <code>required</code>, <code>additionalProperties: false</code>, <code>items</code>, <code>enum</code>, <code>const</code>, <code>minimum</code>/<code>maximum</code>/<code>exclusiveMinimum</code>/<code>exclusiveMaximum</code>/<code>multipleOf</code>, <code>minLength</code>/<code>maxLength</code>/<code>pattern</code>, <code>minItems</code>/<code>maxItems</code>, and <code>format</code> (email, uri, url, date, date-time, uuid).</p>"
            "<p><strong>Not supported</strong>: <code>$ref</code>, <code>allOf</code>/<code>anyOf</code>/<code>oneOf</code>/<code>not</code>, <code>dependentSchemas</code>, <code>prefixItems</code>, <code>contains</code>, <code>if</code>/<code>then</code>/<code>else</code>. For those, use ajv or a server-side validator.</p>"
        ),
        "related_header": "Related Tools",
        "related_json": "JSON Formatter",
        "related_json_ts": "JSON to TS/DTO",
        "related_jwt": "JWT Decoder",
        "related_token": "Token Counter",
        "card_blurb": "Validate JSON against a schema — type, required, items, enum, format, pattern."
    },
    "ko": {
        "title": "JSON Schema 검증기",
        "meta_title": "JSON Schema 검증기 — JSON 데이터를 스키마와 대조 - Utilify",
        "meta_desc": "JSON 데이터를 JSON Schema로 검증. type, properties, required, items, enum, format, pattern, min/max 지원. 모든 처리는 브라우저에서.",
        "og_title": "JSON Schema 검증기 - Utilify",
        "og_desc": "JSON을 스키마로 검증 — 모든 오류에 JSONPath 위치 표시.",
        "json_name": "JSON Schema 검증기",
        "json_desc": "JSON Schema 2020-12 핵심 키워드를 다루는 클라이언트 사이드 검증기.",
        "page_desc": "JSON 데이터와 JSON Schema를 붙여넣으면 type·required·properties·items·enum·format·pattern·min/max 제약을 모두 검사하고, 실패 위치를 JSONPath로 표시합니다. 모든 처리는 브라우저에서 이루어집니다.",
        "label_data": "JSON 데이터",
        "label_schema": "JSON Schema",
        "ph_data": "{\n  \"name\": \"Alice\",\n  \"age\": 30\n}",
        "ph_schema": "{\n  \"type\": \"object\",\n  \"required\": [\"name\"],\n  \"properties\": {\n    \"name\": {\"type\": \"string\"}\n  }\n}",
        "btn_validate": "검증",
        "btn_reset": "초기화",
        "btn_load_sample": "예시 불러오기",
        "btn_share": "결과 공유",
        "share_text": "JSON 검증 결과: {value} —",
        "share_copied": "결과가 클립보드에 복사되었습니다.",
        "res_valid": "✓ 스키마와 일치합니다.",
        "res_invalid_header": "✗ 검증 오류",
        "res_error_count": "{count}개 오류:",
        "alert_data_invalid": "데이터가 유효한 JSON이 아닙니다: ",
        "alert_schema_invalid": "스키마가 유효한 JSON이 아닙니다: ",
        "disclaimer": "JSON Schema 2020-12의 유용한 일부를 구현합니다(type, properties, required, items, enum, const, format, pattern, 문자열/숫자/배열의 min/max). $ref, allOf/anyOf/oneOf, dependentSchemas, prefixItems 등 고급 키워드는 지원하지 않습니다 — 필요 시 ajv 같은 서버 사이드 검증기를 사용하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>JSON 데이터를 왼쪽 패널에 붙여넣으세요.</li>"
            "<li>검증할 JSON Schema를 오른쪽 패널에 붙여넣으세요. <strong>예시 불러오기</strong>로 작동 예제를 확인할 수 있습니다.</li>"
            "<li><strong>검증</strong>을 누르세요. 통과하면 초록 체크가, 실패하면 각 오류의 JSONPath 위치(<code>$.user.email</code> 등)가 함께 표시됩니다.</li>"
            "</ol>"
            "<p><strong>지원 키워드</strong>: <code>type</code>(string, number, integer, boolean, object, array, null), <code>properties</code>, <code>required</code>, <code>additionalProperties: false</code>, <code>items</code>, <code>enum</code>, <code>const</code>, <code>minimum</code>/<code>maximum</code>/<code>exclusiveMinimum</code>/<code>exclusiveMaximum</code>/<code>multipleOf</code>, <code>minLength</code>/<code>maxLength</code>/<code>pattern</code>, <code>minItems</code>/<code>maxItems</code>, <code>format</code>(email, uri, url, date, date-time, uuid).</p>"
            "<p><strong>미지원</strong>: <code>$ref</code>, <code>allOf</code>/<code>anyOf</code>/<code>oneOf</code>/<code>not</code>, <code>dependentSchemas</code>, <code>prefixItems</code>, <code>contains</code>, <code>if</code>/<code>then</code>/<code>else</code>. 필요 시 ajv 또는 서버 사이드 검증기를 권장합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_json": "JSON 포매터",
        "related_json_ts": "JSON to TS/DTO",
        "related_jwt": "JWT 디코더",
        "related_token": "토큰 카운터",
        "card_blurb": "JSON을 Schema로 검증 — type·required·items·enum·format·pattern."
    },
    "ja": {
        "title": "JSONスキーマバリデーター",
        "meta_title": "JSONスキーマバリデーター — JSONをスキーマで検証 - Utilify",
        "meta_desc": "JSONデータをJSONスキーマに対してブラウザ内で検証します。type・properties・required・items・enum・format・pattern・min/maxをサポート。アップロード不要。",
        "og_title": "JSONスキーマバリデーター - Utilify",
        "og_desc": "JSONをスキーマで検証 — すべてのエラーにJSONPathの位置を表示。",
        "json_name": "JSONスキーマバリデーター",
        "json_desc": "JSON Schema 2020-12のコアキーワードを扱うクライアントサイドバリデーター。",
        "page_desc": "JSONデータとJSONスキーマを貼り付けると、type・required・properties・items・enum・format・pattern・min/max制約をすべて検証し、各エラーが発生したJSONPathとともに報告します。すべてブラウザ内で処理されます。",
        "label_data": "JSONデータ",
        "label_schema": "JSONスキーマ",
        "ph_data": "{\n  \"name\": \"Alice\",\n  \"age\": 30\n}",
        "ph_schema": "{\n  \"type\": \"object\",\n  \"required\": [\"name\"],\n  \"properties\": {\n    \"name\": {\"type\": \"string\"}\n  }\n}",
        "btn_validate": "検証",
        "btn_reset": "リセット",
        "btn_load_sample": "サンプルを読み込む",
        "btn_share": "結果を共有",
        "share_text": "JSON検証結果: {value} —",
        "share_copied": "結果をクリップボードにコピーしました。",
        "res_valid": "✓ スキーマに準拠しています。",
        "res_invalid_header": "✗ 検証エラー",
        "res_error_count": "{count}件のエラー:",
        "alert_data_invalid": "データが有効なJSONではありません: ",
        "alert_schema_invalid": "スキーマが有効なJSONではありません: ",
        "disclaimer": "JSON Schema 2020-12の有用なサブセットを実装しています（type、properties、required、items、enum、const、format、pattern、文字列/数値/配列のmin/max）。$ref・allOf/anyOf/oneOf・dependentSchemas・prefixItemsなどの高度なキーワードはサポートされていません — それらにはajvなどのサーバーサイドバリデーターを使用してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>JSONデータを左パネルに貼り付けます。</li>"
            "<li>検証したいJSONスキーマを右パネルに貼り付けます。<strong>サンプルを読み込む</strong>で動作例を確認できます。</li>"
            "<li><strong>検証</strong>をクリックします。合格すると緑のチェックが、失敗すると各エラーのJSONPathの位置（例: <code>$.user.email</code>）が表示されます。</li>"
            "</ol>"
            "<p><strong>サポートされているキーワード</strong>: <code>type</code>（string・number・integer・boolean・object・array・null）、<code>properties</code>、<code>required</code>、<code>additionalProperties: false</code>、<code>items</code>、<code>enum</code>、<code>const</code>、<code>minimum</code>/<code>maximum</code>/<code>exclusiveMinimum</code>/<code>exclusiveMaximum</code>/<code>multipleOf</code>、<code>minLength</code>/<code>maxLength</code>/<code>pattern</code>、<code>minItems</code>/<code>maxItems</code>、<code>format</code>（email・uri・url・date・date-time・uuid）。</p>"
            "<p><strong>非サポート</strong>: <code>$ref</code>、<code>allOf</code>/<code>anyOf</code>/<code>oneOf</code>/<code>not</code>、<code>dependentSchemas</code>、<code>prefixItems</code>、<code>contains</code>、<code>if</code>/<code>then</code>/<code>else</code>。これらにはajvまたはサーバーサイドバリデーターを推奨します。</p>"
        ),
        "related_header": "関連ツール",
        "related_json": "JSONフォーマッター",
        "related_json_ts": "JSON to TS/DTO",
        "related_jwt": "JWTデコーダー",
        "related_token": "トークンカウンター",
        "card_blurb": "JSONをスキーマで検証 — type・required・items・enum・format・pattern。"
    }
}


TIP_CALCULATOR = {
    "en": {
        "title": "Tip Calculator",
        "meta_title": "Tip Calculator — Bill Split with Custom Tip - Utilify",
        "meta_desc": "Calculate the tip and split the bill. Pick a quick tip percentage (10/15/18/20/25) or enter a custom amount, and divide across any number of people.",
        "og_title": "Tip Calculator - Utilify",
        "og_desc": "Tip + total + per-person split, with quick tip-percentage buttons.",
        "json_name": "Tip Calculator",
        "json_desc": "Compute tip amount, total bill, and per-person split for any meal.",
        "page_desc": "Enter the bill, pick a tip percentage (or type a custom one), and the calculator splits the total across however many people are paying. Quick buttons for 10/15/18/20/25%. Runs entirely in your browser.",
        "label_bill": "Bill amount",
        "label_tip": "Tip (%)",
        "label_people": "People",
        "ph_bill": "100",
        "ph_tip": "18",
        "ph_people": "2",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Total per person: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_tip_label": "Tip",
        "res_total_label": "Total",
        "res_per_person_label": "Per person",
        "alert_invalid": "Bill, tip, and people must be positive numbers.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter the pre-tip bill amount.</li>"
            "<li>Pick a quick tip percentage or type a custom one.</li>"
            "<li>Enter how many people are splitting the bill.</li>"
            "<li>Click <strong>Calculate</strong> — tip, total, and per-person amount appear.</li>"
            "</ol>"
            "<p>US convention is 18–20% for table service, 15% for buffets/delivery, 10% or rounding-up for fast counter service. Many countries either include service in the bill or don't tip at all — check local custom.</p>"
        ),
        "related_header": "Related Tools",
        "related_pct": "Percentage Calculator",
        "related_discount": "Discount Calculator",
        "related_unit": "Unit Converter",
        "related_date": "Date Calculator",
        "card_blurb": "Tip + total + per-person split with quick 10/15/18/20/25% buttons."
    },
    "ko": {
        "title": "팁 계산기",
        "meta_title": "팁 계산기 — 식당 더치페이 자동 계산 - Utilify",
        "meta_desc": "식당 계산서의 팁과 인당 분담액을 계산. 10/15/18/20/25% 빠른 선택 또는 직접 입력. 인원수로 나누기 자동.",
        "og_title": "팁 계산기 - Utilify",
        "og_desc": "팁·총액·인당 분담액을 빠른 팁% 버튼으로.",
        "json_name": "팁 계산기",
        "json_desc": "식사 비용의 팁과 더치페이 인당 금액을 계산하는 도구.",
        "page_desc": "계산서 금액과 팁 비율(빠른 선택 또는 직접 입력)을 입력하면, 인원수에 따라 분담액까지 함께 계산됩니다. 미국 등 팁 문화권 여행 시 유용. 모든 처리는 브라우저에서.",
        "label_bill": "계산서 금액",
        "label_tip": "팁 (%)",
        "label_people": "인원수",
        "ph_bill": "100",
        "ph_tip": "18",
        "ph_people": "2",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "인당 부담액: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_tip_label": "팁",
        "res_total_label": "총액",
        "res_per_person_label": "인당",
        "alert_invalid": "계산서·팁·인원수는 모두 양수로 입력해 주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>팁 적용 전 계산서 금액을 입력하세요.</li>"
            "<li>팁 비율을 빠른 버튼으로 선택하거나 직접 입력하세요.</li>"
            "<li>분담할 인원수를 입력하세요.</li>"
            "<li><strong>계산</strong>을 누르면 팁·총액·인당 분담액이 표시됩니다.</li>"
            "</ol>"
            "<p>미국 기준 식당 서비스는 18~20%, 뷔페·배달은 15%, 카운터 서비스는 10% 또는 올림이 일반적입니다. 한국·일본 등은 팁을 받지 않는 경우가 많고, 유럽은 서비스료가 계산서에 포함되어 있어 추가 팁이 필수가 아닙니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_pct": "퍼센트 계산기",
        "related_discount": "할인 계산기",
        "related_unit": "단위 변환기",
        "related_date": "날짜 계산기",
        "card_blurb": "팁·총액·인당 분담액을 빠른 팁% 버튼으로 즉시 계산."
    },
    "ja": {
        "title": "チップ計算機",
        "meta_title": "チップ計算機 — 割り勘・チップ自動計算 - Utilify",
        "meta_desc": "レストランの会計でチップと一人あたりの金額を計算。10/15/18/20/25%のクイック選択または直接入力。人数で自動分割。",
        "og_title": "チップ計算機 - Utilify",
        "og_desc": "チップ・合計・一人あたりの金額をクイックチップ%ボタンで。",
        "json_name": "チップ計算機",
        "json_desc": "食事代のチップと割り勘金額を計算するツール。",
        "page_desc": "会計金額とチップ率(クイック選択または直接入力)を入力すると、人数で割った一人あたりの金額まで計算します。アメリカなどチップ文化圏の旅行で便利。すべての処理はブラウザ内で。",
        "label_bill": "会計金額",
        "label_tip": "チップ (%)",
        "label_people": "人数",
        "ph_bill": "100",
        "ph_tip": "18",
        "ph_people": "2",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "一人あたり: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_tip_label": "チップ",
        "res_total_label": "合計",
        "res_per_person_label": "一人あたり",
        "alert_invalid": "会計金額・チップ・人数はすべて正の数で入力してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>チップ適用前の会計金額を入力します。</li>"
            "<li>チップ率をクイックボタンで選ぶか、直接入力します。</li>"
            "<li>分担する人数を入力します。</li>"
            "<li><strong>計算</strong>を押すと、チップ・合計・一人あたりの金額が表示されます。</li>"
            "</ol>"
            "<p>米国基準ではテーブルサービスは18~20%、ビュッフェ・デリバリーは15%、カウンターサービスは10%または切り上げが一般的です。日本やアジア諸国はチップ文化がない場合が多く、欧州ではサービス料が会計に含まれており追加チップは必須ではありません。</p>"
        ),
        "related_header": "関連ツール",
        "related_pct": "パーセント計算機",
        "related_discount": "割引計算機",
        "related_unit": "単位変換",
        "related_date": "日付計算機",
        "card_blurb": "チップ・合計・一人あたりの金額をクイックチップ%ボタンで即計算。"
    }
}


PERCENTAGE_CALCULATOR = {
    "en": {
        "title": "Percentage Calculator",
        "meta_title": "Percentage Calculator — % of, % is, % Change - Utilify",
        "meta_desc": "Three percentage modes in one: what is X% of Y, X is what percent of Y, and percent change from X to Y. No formulas to remember.",
        "og_title": "Percentage Calculator - Utilify",
        "og_desc": "All three percentage operations in one tool.",
        "json_name": "Percentage Calculator",
        "json_desc": "Switchable percentage operations: % of, % is, % change.",
        "page_desc": "Three common percentage operations in one place: <em>what is X% of Y</em>, <em>X is what percent of Y</em>, and <em>percent change from X to Y</em>. Switch modes from the dropdown — the input labels update so you don't have to remember the formula.",
        "label_mode": "Mode",
        "label_a": "A",
        "label_b": "B",
        "ph_a": "20",
        "ph_b": "150",
        "opt_of": "What is A% of B?",
        "opt_is": "A is what percent of B?",
        "opt_change": "Percent change from A to B",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Result: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_label": "Result",
        "alert_invalid": "Enter valid numbers in both fields.",
        "alert_div_zero": "B cannot be zero in this mode.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick the mode that matches your question:"
            "<ul>"
            "<li><strong>What is A% of B?</strong> — e.g., \"20% of 150\" → 30</li>"
            "<li><strong>A is what percent of B?</strong> — e.g., \"30 is what % of 150\" → 20%</li>"
            "<li><strong>Percent change from A to B</strong> — e.g., \"100 → 125\" → +25%</li>"
            "</ul></li>"
            "<li>Enter the two numbers and click <strong>Calculate</strong>.</li>"
            "</ol>"
            "<p>Percent change uses the formula <code>(B − A) / A × 100</code>. A drop from 100 to 75 is −25%; rising back from 75 to 100 is +33% — gains and losses are not symmetric.</p>"
        ),
        "related_header": "Related Tools",
        "related_tip": "Tip Calculator",
        "related_discount": "Discount Calculator",
        "related_unit": "Unit Converter",
        "related_date": "Date Calculator",
        "card_blurb": "Three percentage modes — % of, % is, % change."
    },
    "ko": {
        "title": "퍼센트 계산기",
        "meta_title": "퍼센트 계산기 — A의 B%, A는 B의 몇%, 변화율 - Utilify",
        "meta_desc": "퍼센트 계산 3가지 모드를 한 곳에서: A의 B%, A는 B의 몇%인지, A에서 B로 변화율. 공식을 외우지 않아도 됨.",
        "og_title": "퍼센트 계산기 - Utilify",
        "og_desc": "퍼센트 계산 3가지를 한 도구에서.",
        "json_name": "퍼센트 계산기",
        "json_desc": "퍼센트 of / 퍼센트 is / 변화율 — 모드 전환식 계산기.",
        "page_desc": "흔히 마주치는 퍼센트 계산 3가지를 한 곳에서: <em>B의 A%는?</em>, <em>A는 B의 몇 %인가?</em>, <em>A에서 B로 변화율</em>. 모드를 선택하면 입력 라벨이 자동으로 바뀝니다 — 공식을 외우지 않아도 됩니다.",
        "label_mode": "모드",
        "label_a": "A",
        "label_b": "B",
        "ph_a": "20",
        "ph_b": "150",
        "opt_of": "B의 A%는?",
        "opt_is": "A는 B의 몇 %인가?",
        "opt_change": "A에서 B로 변화율",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "결과: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_label": "결과",
        "alert_invalid": "두 숫자 모두 유효한 값을 입력해 주세요.",
        "alert_div_zero": "이 모드에서 B는 0이 될 수 없습니다.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>질문에 맞는 모드를 선택하세요:"
            "<ul>"
            "<li><strong>B의 A%는?</strong> — 예: \"150의 20%\" → 30</li>"
            "<li><strong>A는 B의 몇 %인가?</strong> — 예: \"30은 150의 몇 %\" → 20%</li>"
            "<li><strong>A에서 B로 변화율</strong> — 예: \"100 → 125\" → +25%</li>"
            "</ul></li>"
            "<li>두 숫자를 입력하고 <strong>계산</strong>을 누르세요.</li>"
            "</ol>"
            "<p>변화율 공식은 <code>(B − A) / A × 100</code>입니다. 100에서 75로 줄어들면 −25%이고, 다시 75에서 100으로 회복하면 +33% — 상승과 하락은 대칭이 아닙니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_tip": "팁 계산기",
        "related_discount": "할인 계산기",
        "related_unit": "단위 변환기",
        "related_date": "날짜 계산기",
        "card_blurb": "B의 A%·A는 B의 몇 %·변화율 — 3가지 모드 한 곳에서."
    },
    "ja": {
        "title": "パーセント計算機",
        "meta_title": "パーセント計算機 — BのA%・AはBの何%・変化率 - Utilify",
        "meta_desc": "パーセント計算3つのモードを一箇所で:BのA%、AはBの何%か、AからBへの変化率。公式を覚える必要なし。",
        "og_title": "パーセント計算機 - Utilify",
        "og_desc": "3種類のパーセント計算を一つのツールで。",
        "json_name": "パーセント計算機",
        "json_desc": "% of / % is / 変化率 — モード切替式パーセント計算機。",
        "page_desc": "よく使う3つのパーセント計算を一箇所で:<em>BのA%は?</em>、<em>AはBの何%か?</em>、<em>AからBへの変化率</em>。モードを選ぶと入力ラベルが自動で切り替わる — 公式を覚える必要はありません。",
        "label_mode": "モード",
        "label_a": "A",
        "label_b": "B",
        "ph_a": "20",
        "ph_b": "150",
        "opt_of": "BのA%は?",
        "opt_is": "AはBの何%か?",
        "opt_change": "AからBへの変化率",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "結果: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_label": "結果",
        "alert_invalid": "2つの数値とも有効な値を入力してください。",
        "alert_div_zero": "このモードではBは0にできません。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>質問に合うモードを選びます:"
            "<ul>"
            "<li><strong>BのA%は?</strong> — 例:\"150の20%\" → 30</li>"
            "<li><strong>AはBの何%か?</strong> — 例:\"30は150の何%\" → 20%</li>"
            "<li><strong>AからBへの変化率</strong> — 例:\"100 → 125\" → +25%</li>"
            "</ul></li>"
            "<li>2つの数値を入力し<strong>計算</strong>を押します。</li>"
            "</ol>"
            "<p>変化率の公式は<code>(B − A) / A × 100</code>です。100から75に下がると−25%、75から100に戻ると+33% — 上昇と下落は対称ではありません。</p>"
        ),
        "related_header": "関連ツール",
        "related_tip": "チップ計算機",
        "related_discount": "割引計算機",
        "related_unit": "単位変換",
        "related_date": "日付計算機",
        "card_blurb": "BのA%・AはBの何%・変化率 — 3モードを一箇所で。"
    }
}


DISCOUNT_CALCULATOR = {
    "en": {
        "title": "Discount Calculator",
        "meta_title": "Discount Calculator — Final Price + Savings - Utilify",
        "meta_desc": "Apply a percent discount to a price. Returns the final price and the amount saved. Optional second markdown for stacked sales.",
        "og_title": "Discount Calculator - Utilify",
        "og_desc": "Final price + savings amount, with optional second discount.",
        "json_name": "Discount Calculator",
        "json_desc": "Compute final price after percent discount, with optional stacked second discount.",
        "page_desc": "Enter an original price and a discount percent — the calculator returns the final price and the dollar (or won) amount you save. Optional second discount for stacked sales (e.g., \"30% off, then extra 20% at checkout\").",
        "label_price": "Original price",
        "label_discount1": "Discount (%)",
        "label_discount2": "Second discount (%) — optional",
        "ph_price": "100",
        "ph_discount1": "30",
        "ph_discount2": "0",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Final price: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_final_label": "Final price",
        "res_saved_label": "You save",
        "res_effective_label": "Effective discount",
        "alert_invalid": "Enter a positive price and discount percentages between 0 and 100.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter the original (full) price.</li>"
            "<li>Enter the first discount percent.</li>"
            "<li>Optional: enter a second discount that applies <em>after</em> the first (typical \"extra X% at checkout\").</li>"
            "<li>Click <strong>Calculate</strong>. Final price + savings + effective combined discount appear.</li>"
            "</ol>"
            "<p><strong>Stacked discounts don't add.</strong> A 30% then 20% discount is not 50% — it's 1 − (0.7 × 0.8) = 44%. The effective discount field shows the combined rate.</p>"
        ),
        "related_header": "Related Tools",
        "related_tip": "Tip Calculator",
        "related_pct": "Percentage Calculator",
        "related_loan": "Loan Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Final price + savings + stacked-discount effective rate."
    },
    "ko": {
        "title": "할인 계산기",
        "meta_title": "할인 계산기 — 할인가·절약 금액 - Utilify",
        "meta_desc": "정가에 할인율을 적용해 최종 가격과 절약 금액을 계산. 추가 할인(중복할인)까지 합산 가능.",
        "og_title": "할인 계산기 - Utilify",
        "og_desc": "최종가·절약 금액·중복 할인 합산 효과까지.",
        "json_name": "할인 계산기",
        "json_desc": "정가에 할인율을 적용한 최종 가격과 중복 할인 합산 계산기.",
        "page_desc": "정가와 할인율을 입력하면 최종 가격과 절약 금액을 계산합니다. 추가 할인(\"30% 할인 + 결제 시 추가 20%\" 등)도 지원하며, 단순 합이 아닌 실제 합산 할인율을 보여줍니다.",
        "label_price": "정가",
        "label_discount1": "할인율 (%)",
        "label_discount2": "추가 할인율 (%) — 선택",
        "ph_price": "100000",
        "ph_discount1": "30",
        "ph_discount2": "0",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "최종 가격: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_final_label": "최종 가격",
        "res_saved_label": "절약 금액",
        "res_effective_label": "실질 할인율",
        "alert_invalid": "정가는 양수, 할인율은 0~100 사이로 입력해 주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>할인 적용 전 정가를 입력하세요.</li>"
            "<li>첫 번째 할인율을 입력하세요.</li>"
            "<li>선택: 첫 할인 후 적용되는 추가 할인율(\"결제 시 추가 X%\" 등)을 입력하세요.</li>"
            "<li><strong>계산</strong>을 누르면 최종 가격·절약 금액·실질 합산 할인율이 표시됩니다.</li>"
            "</ol>"
            "<p><strong>중복 할인은 단순 합이 아닙니다.</strong> 30% 할인 후 20% 추가 할인은 50%가 아닌 1 − (0.7 × 0.8) = 44%입니다. \"실질 할인율\" 필드에서 합산값을 확인하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_tip": "팁 계산기",
        "related_pct": "퍼센트 계산기",
        "related_loan": "대출 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "최종 가격·절약 금액·중복 할인 실질 합산율까지 즉시 계산."
    },
    "ja": {
        "title": "割引計算機",
        "meta_title": "割引計算機 — 割引後の価格と節約額 - Utilify",
        "meta_desc": "定価に割引率を適用して最終価格と節約額を計算。追加割引(重複割引)も合算可能。",
        "og_title": "割引計算機 - Utilify",
        "og_desc": "最終価格・節約額・重複割引の合算効果まで。",
        "json_name": "割引計算機",
        "json_desc": "定価に割引を適用した最終価格と重複割引の合算計算機。",
        "page_desc": "定価と割引率を入力すると最終価格と節約額を計算します。追加割引(\"30%引き + レジで追加20%\"など)もサポートし、単純合算ではない実質割引率を表示します。",
        "label_price": "定価",
        "label_discount1": "割引率 (%)",
        "label_discount2": "追加割引率 (%) — 任意",
        "ph_price": "10000",
        "ph_discount1": "30",
        "ph_discount2": "0",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "最終価格: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_final_label": "最終価格",
        "res_saved_label": "節約額",
        "res_effective_label": "実質割引率",
        "alert_invalid": "定価は正の数、割引率は0~100の間で入力してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>割引適用前の定価を入力します。</li>"
            "<li>1つ目の割引率を入力します。</li>"
            "<li>任意:最初の割引後に適用される追加割引率(\"レジで追加X%\"など)を入力します。</li>"
            "<li><strong>計算</strong>を押すと、最終価格・節約額・実質合算割引率が表示されます。</li>"
            "</ol>"
            "<p><strong>重複割引は単純合算ではありません。</strong>30%引き後の20%追加割引は50%ではなく、1 − (0.7 × 0.8) = 44%です。\"実質割引率\"フィールドで合算値を確認してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_tip": "チップ計算機",
        "related_pct": "パーセント計算機",
        "related_loan": "ローン計算機",
        "related_unit": "単位変換",
        "card_blurb": "最終価格・節約額・重複割引の実質合算率まで即計算。"
    }
}


SLEEP_CALCULATOR = {
    "en": {
        "title": "Sleep Cycle Calculator",
        "meta_title": "Sleep Calculator — When to Sleep / Wake Up - Utilify",
        "meta_desc": "Plan sleep around 90-minute REM cycles. Pick a wake time to see when to fall asleep, or a bedtime to see optimal wake times. 14 minutes added for falling asleep.",
        "og_title": "Sleep Cycle Calculator - Utilify",
        "og_desc": "Plan sleep around 90-minute REM cycles for refreshed wake-ups.",
        "json_name": "Sleep Cycle Calculator",
        "json_desc": "Suggest bedtimes or wake times aligned with 90-minute REM cycles.",
        "page_desc": "Plan your sleep around 90-minute REM cycles. Enter a wake time to see when to fall asleep for 4–6 cycles, or enter a bedtime to see good wake times. The calculator adds 14 minutes for falling asleep so the suggested times match real-world sleep onset.",
        "label_mode": "Plan",
        "label_time": "Time",
        "opt_wake": "I want to wake up at…",
        "opt_sleep": "I'm going to bed at…",
        "btn_calculate": "Show times",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Sleep planner: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_header_wake": "Try falling asleep at one of these times:",
        "res_header_sleep": "You should aim to wake up at one of these times:",
        "cycle_label": "{cycles} cycles · {hours}h sleep",
        "alert_invalid": "Please pick a valid time.",
        "disclaimer": "Adds 14 minutes for sleep latency (the time it typically takes to fall asleep). Your real cycle length may be 80–100 minutes — adjust if you wake up groggy at 90.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick whether you're starting from a target wake time or a bedtime.</li>"
            "<li>Enter the time in 24-hour format. The calculator adds a 14-minute fall-asleep buffer and computes 4 to 6 full 90-minute cycles.</li>"
            "<li>Aim for one of the suggested times. Waking up at the end of a cycle (light sleep) usually feels less groggy than waking mid-cycle.</li>"
            "</ol>"
            "<p>Adults need <strong>5–6 cycles</strong> (7.5–9 hours) on average. 4 cycles (6 hours) is a survival minimum, not a target. Sleep latency varies — if you typically fall asleep in 5 minutes or 30+ minutes, mentally adjust the buffer.</p>"
        ),
        "related_header": "Related Tools",
        "related_calorie": "Calorie Calculator",
        "related_bmi": "BMI Calculator",
        "related_timer": "Timer",
        "related_date": "Date Calculator",
        "card_blurb": "When to sleep / wake up around 90-minute REM cycles."
    },
    "ko": {
        "title": "수면 사이클 계산기",
        "meta_title": "수면 계산기 — 잠들 시간·일어날 시간 - Utilify",
        "meta_desc": "90분 REM 사이클 기준 수면 계획. 기상 시간을 입력해 잠들 시간을, 취침 시간을 입력해 최적 기상 시간을 확인. 잠드는 시간 14분 자동 반영.",
        "og_title": "수면 사이클 계산기 - Utilify",
        "og_desc": "90분 REM 사이클에 맞춰 상쾌하게 일어나는 시간을 계획.",
        "json_name": "수면 사이클 계산기",
        "json_desc": "90분 REM 사이클에 정렬된 취침 또는 기상 시간 추천기.",
        "page_desc": "90분 REM 사이클에 맞춰 수면을 계획하세요. 기상 시간을 입력하면 4~6 사이클을 위한 잠들 시간을, 취침 시간을 입력하면 좋은 기상 시간을 알려줍니다. 잠드는 데 걸리는 시간 14분이 자동 반영됩니다.",
        "label_mode": "방식",
        "label_time": "시간",
        "opt_wake": "이 시간에 일어나고 싶어요",
        "opt_sleep": "이 시간에 잠들 거예요",
        "btn_calculate": "시간 보기",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "수면 플래너: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_header_wake": "이 시간 중 한 시점에 잠들어 보세요:",
        "res_header_sleep": "이 시간 중 한 시점에 일어나는 게 좋습니다:",
        "cycle_label": "{cycles}사이클 · 수면 {hours}시간",
        "alert_invalid": "유효한 시간을 입력해 주세요.",
        "disclaimer": "잠드는 데 걸리는 시간 14분(수면 잠복기)을 더합니다. 실제 사이클 길이는 80~100분으로 사람마다 다릅니다 — 90분 기준으로 멍한 상태로 깬다면 조정하세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>목표 기상 시간 기준인지, 취침 시간 기준인지 선택하세요.</li>"
            "<li>시간을 24시간 형식으로 입력하세요. 14분의 수면 잠복기 버퍼가 더해지고, 4~6개의 완전한 90분 사이클을 계산합니다.</li>"
            "<li>제안된 시간 중 하나를 목표로 삼으세요. 사이클 끝(얕은 수면)에 일어나는 것이 사이클 중간에 깨는 것보다 덜 멍합니다.</li>"
            "</ol>"
            "<p>성인은 평균 <strong>5~6 사이클</strong>(7.5~9시간)이 필요합니다. 4 사이클(6시간)은 생존 최소치이지 목표가 아닙니다. 수면 잠복기는 개인차가 크니 5분 만에 잠들거나 30분 이상 걸리면 마음속으로 보정하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_calorie": "칼로리 계산기",
        "related_bmi": "BMI 계산기",
        "related_timer": "타이머",
        "related_date": "날짜 계산기",
        "card_blurb": "90분 REM 사이클 기준 잠들 시간·일어날 시간 추천."
    },
    "ja": {
        "title": "睡眠サイクル計算機",
        "meta_title": "睡眠計算機 — 寝る時間・起きる時間 - Utilify",
        "meta_desc": "90分のREMサイクル基準で睡眠を計画。起床時刻を入力して寝る時刻を、就寝時刻を入力して最適な起床時刻を確認。入眠時間14分を自動反映。",
        "og_title": "睡眠サイクル計算機 - Utilify",
        "og_desc": "90分REMサイクルに合わせて爽やかに起きる時間を計画。",
        "json_name": "睡眠サイクル計算機",
        "json_desc": "90分REMサイクルに整列した就寝・起床時刻の推奨ツール。",
        "page_desc": "90分のREMサイクルに合わせて睡眠を計画しましょう。起床時刻を入力すると4~6サイクルのための入眠時刻、就寝時刻を入力すると良い起床時刻を提案します。入眠にかかる14分が自動で反映されます。",
        "label_mode": "モード",
        "label_time": "時刻",
        "opt_wake": "この時刻に起きたい",
        "opt_sleep": "この時刻に寝る",
        "btn_calculate": "時刻を見る",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "睡眠プラン: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_header_wake": "次のいずれかの時刻に入眠してみてください:",
        "res_header_sleep": "次のいずれかの時刻に起きるのが良いです:",
        "cycle_label": "{cycles}サイクル · 睡眠{hours}時間",
        "alert_invalid": "有効な時刻を入力してください。",
        "disclaimer": "入眠にかかる14分(睡眠潜時)を加算しています。実際のサイクル長は80~100分と個人差があります — 90分基準でぼんやり目覚める場合は調整してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>目標が起床時刻基準か就寝時刻基準かを選びます。</li>"
            "<li>時刻を24時間表記で入力します。14分の睡眠潜時バッファが加算され、4~6個の完全な90分サイクルを計算します。</li>"
            "<li>提案された時刻のいずれかを目標にします。サイクルの終わり(浅い眠り)に起きるほうが、サイクルの途中で起きるよりぼんやりしません。</li>"
            "</ol>"
            "<p>成人は平均<strong>5~6サイクル</strong>(7.5~9時間)が必要です。4サイクル(6時間)は生存最低限であり、目標ではありません。睡眠潜時は個人差が大きいので、5分で寝つく人や30分以上かかる人は心の中で補正してください。</p>"
        ),
        "related_header": "関連ツール",
        "related_calorie": "カロリー計算機",
        "related_bmi": "BMI計算機",
        "related_timer": "タイマー",
        "related_date": "日付計算機",
        "card_blurb": "90分REMサイクル基準で寝る時刻・起きる時刻を推奨。"
    }
}


READING_TIME = {
    "en": {
        "title": "Reading Time Estimator",
        "meta_title": "Reading Time Calculator — Words to Minutes - Utilify",
        "meta_desc": "Estimate reading time from a word count or pasted text. Configurable WPM (default 250). Useful for blog posts, podcasts, video scripts, and pacing.",
        "og_title": "Reading Time Estimator - Utilify",
        "og_desc": "Words → minutes with adjustable reading speed.",
        "json_name": "Reading Time Estimator",
        "json_desc": "Convert word count or pasted text into estimated reading time at a chosen WPM.",
        "page_desc": "Paste text or enter a word count to estimate how long it'll take to read at your chosen speed. Default 250 WPM is a typical adult silent-reading pace; pick 150 for spoken/podcast pacing or 300+ for skimming.",
        "label_text": "Text or word count",
        "label_wpm": "Reading speed (WPM)",
        "ph_text": "Paste your article, blog post, or speech…",
        "ph_wpm": "250",
        "btn_calculate": "Estimate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Reading time: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_words_label": "Words",
        "res_chars_label": "Characters",
        "res_time_label": "Reading time",
        "res_speak_label": "Spoken time",
        "alert_invalid": "Enter text or a positive word count, and a positive WPM.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Paste the text you want to estimate. The calculator counts words automatically (whitespace-split, ignoring extra spacing).</li>"
            "<li>Adjust the words-per-minute (WPM) speed. Common targets:"
            "<ul>"
            "<li><strong>150 WPM</strong> — comfortable spoken / podcast pace</li>"
            "<li><strong>250 WPM</strong> — average silent reading (default)</li>"
            "<li><strong>400 WPM</strong> — skimming / fast reading</li>"
            "</ul></li>"
            "<li>Click <strong>Estimate</strong>. Both reading time and a separate spoken-time estimate (at 150 WPM) are shown.</li>"
            "</ol>"
            "<p>Most blog platforms use 200–250 WPM. For audio scripts (podcasts, voiceovers, talks), use 130–160 WPM — slow enough to be clearly understood out loud.</p>"
        ),
        "related_header": "Related Tools",
        "related_text_utils": "Text Utilities",
        "related_md": "Markdown Previewer",
        "related_token": "Token Counter",
        "related_timer": "Timer",
        "card_blurb": "Words → reading & spoken-time estimates with adjustable WPM."
    },
    "ko": {
        "title": "읽기 시간 계산기",
        "meta_title": "읽기 시간 계산기 — 단어 수에서 분으로 - Utilify",
        "meta_desc": "텍스트나 단어 수로 읽기 시간 추정. 분당 단어 수(WPM) 조절 가능 (기본 250). 블로그·팟캐스트 대본·발표 등 페이싱에 유용.",
        "og_title": "읽기 시간 계산기 - Utilify",
        "og_desc": "단어를 분으로 — 읽기 속도 조정 가능.",
        "json_name": "읽기 시간 계산기",
        "json_desc": "단어 수 또는 텍스트를 사용자 지정 WPM으로 읽기 시간으로 변환.",
        "page_desc": "텍스트를 붙여넣거나 단어 수를 입력해 원하는 속도로 읽는 데 걸리는 시간을 추정합니다. 기본값 250 WPM은 성인 묵독 평균이며, 팟캐스트는 150, 빠른 훑어 읽기는 300 이상을 사용하세요.",
        "label_text": "텍스트 또는 단어 수",
        "label_wpm": "읽기 속도 (WPM)",
        "ph_text": "기사·블로그·연설 원고를 붙여넣으세요…",
        "ph_wpm": "250",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "읽기 시간: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_words_label": "단어",
        "res_chars_label": "글자",
        "res_time_label": "읽기 시간",
        "res_speak_label": "낭독 시간",
        "alert_invalid": "텍스트나 양수 단어 수, 그리고 양수 WPM을 입력해 주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>추정할 텍스트를 붙여넣으세요. 단어는 공백 기준으로 자동 계산됩니다.</li>"
            "<li>분당 단어 수(WPM)를 조정하세요. 흔한 기준:"
            "<ul>"
            "<li><strong>150 WPM</strong> — 편안한 낭독·팟캐스트 속도</li>"
            "<li><strong>250 WPM</strong> — 묵독 평균 (기본값)</li>"
            "<li><strong>400 WPM</strong> — 훑어 읽기·속독</li>"
            "</ul></li>"
            "<li><strong>계산</strong>을 누르면 읽기 시간과 별도로 낭독 시간(150 WPM 기준)이 함께 표시됩니다.</li>"
            "</ol>"
            "<p>대부분의 블로그 플랫폼은 200~250 WPM을 가정합니다. 오디오 대본(팟캐스트·내레이션·발표)은 130~160 WPM — 입으로 또렷하게 전달되는 속도를 사용하세요.</p>"
        ),
        "related_header": "관련 도구",
        "related_text_utils": "텍스트 유틸리티",
        "related_md": "Markdown 프리뷰어",
        "related_token": "토큰 카운터",
        "related_timer": "타이머",
        "card_blurb": "단어를 분으로 — WPM 조정 가능한 읽기·낭독 시간 추정."
    },
    "ja": {
        "title": "読書時間計算機",
        "meta_title": "読書時間計算機 — 単語数から分への換算 - Utilify",
        "meta_desc": "テキストや単語数から読書時間を推定。WPM(分あたり単語数)調整可能(デフォルト250)。ブログ・ポッドキャスト原稿・プレゼンのペース配分に便利。",
        "og_title": "読書時間計算機 - Utilify",
        "og_desc": "単語を分に — 読む速度を調整可能。",
        "json_name": "読書時間計算機",
        "json_desc": "単語数またはテキストをユーザー指定WPMで読書時間に変換。",
        "page_desc": "テキストを貼り付けるか単語数を入力すると、お好みの速度で読むのにかかる時間を推定します。デフォルト250 WPMは成人の黙読平均、ポッドキャストは150、速読・流し読みは300以上を使ってください。",
        "label_text": "テキストまたは単語数",
        "label_wpm": "読む速度 (WPM)",
        "ph_text": "記事・ブログ・スピーチ原稿を貼り付けてください…",
        "ph_wpm": "250",
        "btn_calculate": "推定",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "読書時間: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_words_label": "単語",
        "res_chars_label": "文字",
        "res_time_label": "読書時間",
        "res_speak_label": "朗読時間",
        "alert_invalid": "テキストか正の単語数、正のWPMを入力してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>推定するテキストを貼り付けます。単語は空白基準で自動カウントされます。</li>"
            "<li>分あたり単語数(WPM)を調整します。よく使う目安:"
            "<ul>"
            "<li><strong>150 WPM</strong> — 楽な朗読・ポッドキャスト速度</li>"
            "<li><strong>250 WPM</strong> — 黙読平均(デフォルト)</li>"
            "<li><strong>400 WPM</strong> — 流し読み・速読</li>"
            "</ul></li>"
            "<li><strong>推定</strong>を押すと、読書時間と別途朗読時間(150 WPM基準)が表示されます。</li>"
            "</ol>"
            "<p>ほとんどのブログプラットフォームは200~250 WPMを想定します。音声原稿(ポッドキャスト・ナレーション・プレゼン)は130~160 WPM — 口でハッキリ伝わる速度を使ってください。</p>"
        ),
        "related_header": "関連ツール",
        "related_text_utils": "テキストユーティリティ",
        "related_md": "Markdownプレビュー",
        "related_token": "トークンカウンター",
        "related_timer": "タイマー",
        "card_blurb": "単語を分に — WPM調整可能な読書・朗読時間推定。"
    }
}


WATER_INTAKE = {
    "en": {
        "title": "Water Intake Calculator",
        "meta_title": "Water Intake Calculator — Daily Hydration Target - Utilify",
        "meta_desc": "Estimate daily water needs from body weight, with adjustments for activity and climate. Returns ml, liters, and equivalent 250 ml glasses.",
        "og_title": "Water Intake Calculator - Utilify",
        "og_desc": "Daily hydration target with activity & climate adjustments.",
        "json_name": "Water Intake Calculator",
        "json_desc": "Estimate daily water target from weight + activity + climate.",
        "page_desc": "Estimate daily water intake from body weight, with bumps for exercise and hot climates. The result is shown in milliliters, liters, and 250 ml glasses. Baseline is 33 ml per kg of body weight — typical for moderately active adults.",
        "label_weight": "Weight (kg)",
        "label_activity": "Activity level",
        "label_climate": "Climate",
        "ph_weight": "70",
        "opt_act_low": "Sedentary",
        "opt_act_mid": "Moderate exercise",
        "opt_act_high": "Heavy exercise",
        "opt_clim_normal": "Temperate",
        "opt_clim_hot": "Hot / humid",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Daily water target: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_ml_label": "Daily target",
        "res_l_label": "In liters",
        "res_glasses_label": "Glasses (250 ml)",
        "alert_invalid": "Enter a positive weight in kilograms.",
        "disclaimer": "Estimate only. Real needs vary by sex, body composition, sweat rate, kidney function, and altitude. Drink to thirst; pale-yellow urine is the best practical indicator.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Enter your body weight in kilograms.</li>"
            "<li>Pick activity level and climate. Heavy exercise adds 500 ml; hot climates add another 500 ml.</li>"
            "<li>Click <strong>Calculate</strong> — the daily target appears in ml, liters, and 250 ml glasses.</li>"
            "</ol>"
            "<p><strong>Formula</strong>: 33 ml × weight(kg), plus 350 ml for moderate exercise / 500 ml for heavy, plus 500 ml for hot climates. Caffeinated drinks count toward intake (not as much as water but most of the volume); alcohol is a net negative for hydration.</p>"
            "<p>This estimate covers <em>total fluid</em> — food contributes about 20% of daily water (more if you eat lots of fruit, soup, or vegetables). Drinking ~1.5–2.5 L of water-equivalent fluids on top of food usually covers it.</p>"
        ),
        "related_header": "Related Tools",
        "related_calorie": "Calorie Calculator",
        "related_bmi": "BMI Calculator",
        "related_body_fat": "Body Fat Calculator",
        "related_unit": "Unit Converter",
        "card_blurb": "Daily water target from weight + activity + climate."
    },
    "ko": {
        "title": "물 섭취량 계산기",
        "meta_title": "물 섭취량 계산기 — 1일 권장 수분량 - Utilify",
        "meta_desc": "체중·활동 수준·기후로 1일 물 권장량 추정. ml·리터·250ml 컵 단위로 표시.",
        "og_title": "물 섭취량 계산기 - Utilify",
        "og_desc": "활동·기후 보정 포함 1일 수분 목표.",
        "json_name": "물 섭취량 계산기",
        "json_desc": "체중·활동·기후 기반 1일 물 목표량 추정.",
        "page_desc": "체중을 기준으로 1일 물 섭취량을 추정하고 운동량과 기후에 따라 보정합니다. 결과는 ml·리터·250ml 컵 수로 표시됩니다. 기본 공식은 체중(kg)당 33ml — 보통 활동량의 성인에게 적용되는 기준입니다.",
        "label_weight": "체중 (kg)",
        "label_activity": "활동 수준",
        "label_climate": "기후",
        "ph_weight": "70",
        "opt_act_low": "거의 활동 없음",
        "opt_act_mid": "보통 운동",
        "opt_act_high": "강도 높은 운동",
        "opt_clim_normal": "온대",
        "opt_clim_hot": "더위·습기",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "1일 물 목표량: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_ml_label": "1일 목표",
        "res_l_label": "리터",
        "res_glasses_label": "컵 (250ml)",
        "alert_invalid": "체중을 양수(kg)로 입력해 주세요.",
        "disclaimer": "추정치입니다. 실제 필요량은 성별·체구성·발한율·신장 기능·고도에 따라 다릅니다. 갈증을 기준으로 마시고, 옅은 노란빛 소변이 가장 실용적인 지표입니다.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>체중을 kg 단위로 입력하세요.</li>"
            "<li>활동 수준과 기후를 선택하세요. 강도 높은 운동은 500ml, 더운 기후는 추가 500ml가 더해집니다.</li>"
            "<li><strong>계산</strong>을 누르면 1일 목표가 ml·리터·250ml 컵 단위로 표시됩니다.</li>"
            "</ol>"
            "<p><strong>공식</strong>: 33ml × 체중(kg), 보통 운동 +350ml, 강도 높은 운동 +500ml, 더운 기후 +500ml. 카페인 음료도 수분 섭취에 포함되지만(물보다는 효율 낮음), 알코올은 탈수를 유발해 도움이 되지 않습니다.</p>"
            "<p>이 추정값은 <em>전체 수분</em> 기준입니다 — 음식이 1일 수분의 약 20%를 제공합니다(과일·국·채소 위주면 더 많이). 보통 식사 외에 1.5~2.5L 정도의 수분을 더 섭취하면 충분합니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_calorie": "칼로리 계산기",
        "related_bmi": "BMI 계산기",
        "related_body_fat": "체지방 계산기",
        "related_unit": "단위 변환기",
        "card_blurb": "체중·활동·기후 기반 1일 물 권장량 자동 계산."
    },
    "ja": {
        "title": "水分摂取量計算機",
        "meta_title": "水分摂取量計算機 — 1日の水分目標 - Utilify",
        "meta_desc": "体重・運動量・気候から1日の必要水分量を推定。ml・リットル・250mlコップ単位で表示。",
        "og_title": "水分摂取量計算機 - Utilify",
        "og_desc": "運動・気候補正を含む1日の水分目標。",
        "json_name": "水分摂取量計算機",
        "json_desc": "体重・運動量・気候に基づく1日の水分目標推定。",
        "page_desc": "体重を基準に1日の水分摂取量を推定し、運動量と気候に応じて補正します。結果はml・リットル・250mlコップ数で表示されます。基本式は体重(kg)あたり33ml — 普通の活動量の成人に適用される目安です。",
        "label_weight": "体重 (kg)",
        "label_activity": "運動量",
        "label_climate": "気候",
        "ph_weight": "70",
        "opt_act_low": "ほぼ運動なし",
        "opt_act_mid": "普通の運動",
        "opt_act_high": "高強度の運動",
        "opt_clim_normal": "温帯",
        "opt_clim_hot": "高温・多湿",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "1日の水分目標: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_ml_label": "1日の目標",
        "res_l_label": "リットル",
        "res_glasses_label": "コップ (250ml)",
        "alert_invalid": "体重を正の数(kg)で入力してください。",
        "disclaimer": "推定値です。実際の必要量は性別・体組成・発汗率・腎機能・標高によって異なります。喉の渇きを基準に飲み、薄い黄色の尿が最も実用的な指標です。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>体重をkg単位で入力します。</li>"
            "<li>運動量と気候を選びます。高強度の運動は500ml、暑い気候は追加で500mlが加算されます。</li>"
            "<li><strong>計算</strong>を押すと、1日の目標がml・リットル・250mlコップ単位で表示されます。</li>"
            "</ol>"
            "<p><strong>計算式</strong>:33ml × 体重(kg)、普通の運動 +350ml、高強度の運動 +500ml、暑い気候 +500ml。カフェイン飲料も水分摂取に含まれます(水より効率は低い)が、アルコールは脱水を招くため役に立ちません。</p>"
            "<p>この推定値は<em>総水分</em>基準です — 食事が1日の水分の約20%を提供します(果物・スープ・野菜中心なら多め)。通常、食事以外に1.5~2.5L程度の水分を摂れば十分です。</p>"
        ),
        "related_header": "関連ツール",
        "related_calorie": "カロリー計算機",
        "related_bmi": "BMI計算機",
        "related_body_fat": "体脂肪率計算機",
        "related_unit": "単位変換",
        "card_blurb": "体重・運動量・気候に基づく1日の水分推奨量を自動計算。"
    }
}


FILE_SIZE_CONVERTER = {
    "en": {
        "title": "File Size Converter",
        "meta_title": "File Size Converter — Bytes / KB / MB / GB / TB - Utilify",
        "meta_desc": "Convert between bytes, kilobytes, megabytes, gigabytes, terabytes, and petabytes. Switch between decimal (KB = 1000) and binary (KiB = 1024) units.",
        "og_title": "File Size Converter - Utilify",
        "og_desc": "Bytes ↔ KB / MB / GB / TB / PB with decimal or binary units.",
        "json_name": "File Size Converter",
        "json_desc": "Convert between digital storage units in decimal or binary base.",
        "page_desc": "Convert between bytes, kilobytes, megabytes, gigabytes, terabytes, and petabytes. Pick decimal (1 KB = 1000 B — what hard drives advertise) or binary (1 KiB = 1024 B — what your OS shows).",
        "label_value": "Value",
        "label_from": "From",
        "label_to": "To",
        "label_system": "Unit system",
        "ph_value": "1024",
        "opt_decimal": "Decimal (1 KB = 1000 B)",
        "opt_binary": "Binary (1 KiB = 1024 B)",
        "btn_convert": "Convert",
        "btn_swap": "Swap",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "{value} —",
        "share_copied": "Copied to clipboard.",
        "res_label": "Result",
        "alert_invalid": "Enter a non-negative number.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Type the number you want to convert.</li>"
            "<li>Pick the source and target units.</li>"
            "<li>Pick the unit system. Drive manufacturers and most networking specs use <strong>decimal</strong> (1 KB = 1000 B). Operating systems (Windows, Linux, macOS in older versions) and RAM specs use <strong>binary</strong> (1 KiB = 1024 B).</li>"
            "</ol>"
            "<p>The naming convention <em>KiB / MiB / GiB</em> exists specifically to disambiguate binary from decimal. \"KB\" without the <em>i</em> usually means decimal but is sometimes used loosely. When in doubt, decimal is the formal SI standard.</p>"
        ),
        "related_header": "Related Tools",
        "related_unit": "Unit Converter",
        "related_base64": "Base64 Converter",
        "related_token": "Token Counter",
        "related_pct": "Percentage Calculator",
        "card_blurb": "B ↔ KB / MB / GB / TB / PB with decimal or binary units."
    },
    "ko": {
        "title": "파일 크기 변환기",
        "meta_title": "파일 크기 변환기 — Bytes·KB·MB·GB·TB - Utilify",
        "meta_desc": "바이트·킬로바이트·메가바이트·기가바이트·테라바이트·페타바이트 상호 변환. 십진법(1KB=1000B)과 이진법(1KiB=1024B) 모두 지원.",
        "og_title": "파일 크기 변환기 - Utilify",
        "og_desc": "B ↔ KB / MB / GB / TB / PB — 십진/이진법 단위 지원.",
        "json_name": "파일 크기 변환기",
        "json_desc": "십진법·이진법 디지털 저장 단위 상호 변환기.",
        "page_desc": "바이트·KB·MB·GB·TB·PB 단위를 자유롭게 변환합니다. 하드드라이브 광고에 쓰는 십진법(1KB = 1000B)과 OS가 표시하는 이진법(1KiB = 1024B) 중 선택할 수 있습니다.",
        "label_value": "값",
        "label_from": "원본",
        "label_to": "변환",
        "label_system": "단위 체계",
        "ph_value": "1024",
        "opt_decimal": "십진법 (1KB = 1000B)",
        "opt_binary": "이진법 (1KiB = 1024B)",
        "btn_convert": "변환",
        "btn_swap": "양방향 전환",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "{value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_label": "결과",
        "alert_invalid": "0 이상의 숫자를 입력해 주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>변환할 숫자를 입력하세요.</li>"
            "<li>원본 단위와 변환할 단위를 선택하세요.</li>"
            "<li>단위 체계를 선택합니다. 하드드라이브 제조사와 네트워크 스펙은 <strong>십진법</strong>(1KB = 1000B), 운영체제(Windows·Linux·옛 macOS)와 RAM 스펙은 <strong>이진법</strong>(1KiB = 1024B)을 사용합니다.</li>"
            "</ol>"
            "<p><em>KiB·MiB·GiB</em> 표기는 이진법임을 명확히 구분하기 위한 IEC 표준입니다. \"KB\"는 보통 십진법이지만 느슨하게 이진법으로도 쓰입니다 — 정확한 사양에는 십진법이 SI 공식 표준입니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_unit": "단위 변환기",
        "related_base64": "Base64 변환기",
        "related_token": "토큰 카운터",
        "related_pct": "퍼센트 계산기",
        "card_blurb": "B ↔ KB·MB·GB·TB·PB — 십진/이진법 모두 지원."
    },
    "ja": {
        "title": "ファイルサイズ変換",
        "meta_title": "ファイルサイズ変換 — Bytes・KB・MB・GB・TB - Utilify",
        "meta_desc": "バイト・キロバイト・メガバイト・ギガバイト・テラバイト・ペタバイトを相互変換。10進法(1KB=1000B)と2進法(1KiB=1024B)の両方をサポート。",
        "og_title": "ファイルサイズ変換 - Utilify",
        "og_desc": "B ↔ KB / MB / GB / TB / PB — 10進法・2進法対応。",
        "json_name": "ファイルサイズ変換",
        "json_desc": "10進法・2進法のデジタルストレージ単位相互変換ツール。",
        "page_desc": "バイト・KB・MB・GB・TB・PB単位を自由に変換します。ハードドライブ広告で使われる10進法(1KB = 1000B)と、OSが表示する2進法(1KiB = 1024B)を選択できます。",
        "label_value": "値",
        "label_from": "変換元",
        "label_to": "変換先",
        "label_system": "単位体系",
        "ph_value": "1024",
        "opt_decimal": "10進法 (1KB = 1000B)",
        "opt_binary": "2進法 (1KiB = 1024B)",
        "btn_convert": "変換",
        "btn_swap": "入れ替え",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "{value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_label": "結果",
        "alert_invalid": "0以上の数値を入力してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>変換する数値を入力します。</li>"
            "<li>変換元と変換先の単位を選びます。</li>"
            "<li>単位体系を選択します。ハードドライブメーカーやネットワーク仕様は<strong>10進法</strong>(1KB = 1000B)、OS(Windows・Linux・旧macOS)やRAM仕様は<strong>2進法</strong>(1KiB = 1024B)を使います。</li>"
            "</ol>"
            "<p><em>KiB・MiB・GiB</em>表記は2進法であることを明確に区別するためのIEC標準です。\"KB\"は通常10進法ですが、緩い意味で2進法にも使われます — 正確な仕様には10進法がSI公式標準です。</p>"
        ),
        "related_header": "関連ツール",
        "related_unit": "単位変換",
        "related_base64": "Base64変換",
        "related_token": "トークンカウンター",
        "related_pct": "パーセント計算機",
        "card_blurb": "B ↔ KB・MB・GB・TB・PB — 10進・2進両対応。"
    }
}


AGE_CALCULATOR = {
    "en": {
        "title": "Age Calculator",
        "meta_title": "Age Calculator — Years, Months, Days, Next Birthday - Utilify",
        "meta_desc": "Calculate exact age from a birth date. Returns years, months, days, total days alive, and how many days until the next birthday.",
        "og_title": "Age Calculator - Utilify",
        "og_desc": "Exact age in years/months/days plus next-birthday countdown.",
        "json_name": "Age Calculator",
        "json_desc": "Compute age and next-birthday distance from a date of birth.",
        "page_desc": "Pick a birth date and get exact age — years, months, and days — plus total days alive and how many days until the next birthday. Handy for visa forms, school cutoffs, and \"how old will I be in 2030\" curiosity.",
        "label_dob": "Date of birth",
        "label_target": "Calculate as of",
        "btn_calculate": "Calculate",
        "btn_reset": "Reset",
        "btn_share": "Share result",
        "share_text": "Age: {value} —",
        "share_copied": "Copied to clipboard.",
        "res_age_label": "Age",
        "res_total_days_label": "Days alive",
        "res_next_birthday_label": "Next birthday in",
        "res_age_format": "{years} y, {months} mo, {days} d",
        "res_days_format": "{days} days",
        "alert_invalid": "Pick a valid birth date that's not in the future of the target date.",
        "howto_header": "How to use",
        "howto_html": (
            "<ol>"
            "<li>Pick your date of birth.</li>"
            "<li>Optional: change the target date (default is today). Useful for \"How old will I be on July 4, 2030?\" questions.</li>"
            "<li>Click <strong>Calculate</strong>. Age in years / months / days, total days alive, and days until the next birthday all show up.</li>"
            "</ol>"
            "<p>The calculator handles month-end edge cases — a baby born on Jan 31 turns one month old on Feb 28 (or 29 in leap years), not Feb 31. Years are full Gregorian years; leap days are counted toward the day total.</p>"
        ),
        "related_header": "Related Tools",
        "related_date": "Date Calculator",
        "related_pregnancy": "Pregnancy Calculator",
        "related_unix": "Unix Timestamp",
        "related_bmi": "BMI Calculator",
        "card_blurb": "Years / months / days alive + next-birthday countdown from any DOB."
    },
    "ko": {
        "title": "만 나이 계산기",
        "meta_title": "만 나이 계산기 — 년·개월·일·다음 생일까지 - Utilify",
        "meta_desc": "생년월일로 만 나이(년·개월·일)·살아온 총 일수·다음 생일까지 일수를 계산. 비자 서류·학년 기준일·기념일 계산에 유용.",
        "og_title": "만 나이 계산기 - Utilify",
        "og_desc": "정확한 만 나이와 다음 생일까지 일수.",
        "json_name": "만 나이 계산기",
        "json_desc": "생년월일로 만 나이와 다음 생일까지 거리 계산.",
        "page_desc": "생년월일을 입력하면 만 나이(년·개월·일), 살아온 총 일수, 다음 생일까지 남은 일수를 계산합니다. 비자 서류, 학년 기준일, \"2030년에 몇 살일까?\" 같은 질문에 유용합니다.",
        "label_dob": "생년월일",
        "label_target": "기준 날짜",
        "btn_calculate": "계산",
        "btn_reset": "초기화",
        "btn_share": "결과 공유",
        "share_text": "나이: {value} —",
        "share_copied": "클립보드에 복사되었습니다.",
        "res_age_label": "만 나이",
        "res_total_days_label": "살아온 일수",
        "res_next_birthday_label": "다음 생일까지",
        "res_age_format": "{years}년 {months}개월 {days}일",
        "res_days_format": "{days}일",
        "alert_invalid": "기준 날짜보다 이후가 아닌 유효한 생년월일을 입력해 주세요.",
        "howto_header": "사용 방법",
        "howto_html": (
            "<ol>"
            "<li>생년월일을 선택하세요.</li>"
            "<li>선택: 기준 날짜를 변경할 수 있습니다 (기본값은 오늘). \"2030년 7월 4일에 몇 살일까?\" 같은 질문에 유용합니다.</li>"
            "<li><strong>계산</strong>을 누르면 만 나이(년·개월·일), 살아온 총 일수, 다음 생일까지의 일수가 표시됩니다.</li>"
            "</ol>"
            "<p>월말 경계 케이스를 처리합니다 — 1월 31일생 아기는 2월 28일(윤년이면 29일)에 1개월이 되며, 2월 31일이 아닙니다. 년수는 그레고리력 기준 완전 1년이며, 윤일도 살아온 일수에 포함됩니다.</p>"
        ),
        "related_header": "관련 도구",
        "related_date": "날짜 계산기",
        "related_pregnancy": "임신 계산기",
        "related_unix": "Unix 타임스탬프",
        "related_bmi": "BMI 계산기",
        "card_blurb": "생년월일에서 만 나이·살아온 일수·다음 생일까지 즉시 계산."
    },
    "ja": {
        "title": "年齢計算機",
        "meta_title": "年齢計算機 — 年・月・日・次の誕生日まで - Utilify",
        "meta_desc": "生年月日から正確な年齢を計算。年・月・日数、生きた総日数、次の誕生日までの日数を表示。",
        "og_title": "年齢計算機 - Utilify",
        "og_desc": "年・月・日単位の正確な年齢と次の誕生日までのカウントダウン。",
        "json_name": "年齢計算機",
        "json_desc": "生年月日から年齢と次の誕生日までの距離を計算。",
        "page_desc": "生年月日を選ぶと正確な年齢 — 年・月・日 — と、生きた総日数、次の誕生日までの日数を表示します。ビザ申請、入学基準日、\"2030年に何歳?\"といった疑問に便利。",
        "label_dob": "生年月日",
        "label_target": "基準日",
        "btn_calculate": "計算",
        "btn_reset": "リセット",
        "btn_share": "結果を共有",
        "share_text": "年齢: {value} —",
        "share_copied": "クリップボードにコピーしました。",
        "res_age_label": "年齢",
        "res_total_days_label": "生きた日数",
        "res_next_birthday_label": "次の誕生日まで",
        "res_age_format": "{years}年{months}ヶ月{days}日",
        "res_days_format": "{days}日",
        "alert_invalid": "基準日より未来でない有効な生年月日を入力してください。",
        "howto_header": "使い方",
        "howto_html": (
            "<ol>"
            "<li>生年月日を選びます。</li>"
            "<li>任意:基準日を変更できます(デフォルトは今日)。\"2030年7月4日に何歳か?\"といった質問に便利です。</li>"
            "<li><strong>計算</strong>を押すと、年齢(年・月・日)、生きた総日数、次の誕生日までの日数が表示されます。</li>"
            "</ol>"
            "<p>月末の境界ケースも処理します — 1月31日生まれの赤ちゃんは2月28日(うるう年なら29日)で1ヶ月になり、2月31日にはなりません。年数はグレゴリオ暦基準の完全1年で、うるう日も生きた日数に含まれます。</p>"
        ),
        "related_header": "関連ツール",
        "related_date": "日付計算機",
        "related_pregnancy": "妊娠計算機",
        "related_unix": "Unixタイムスタンプ",
        "related_bmi": "BMI計算機",
        "card_blurb": "生年月日から年齢・生きた日数・次の誕生日まで即計算。"
    }
}

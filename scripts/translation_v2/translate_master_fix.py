#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# ------------------------------------------------------------------------------
# MASTER TRANSLATION MAP
# ------------------------------------------------------------------------------
# Keys are the EXACT Korean strings found in the codebase.
# Values are dictionaries of translations for each target language.

MASTER_MAP = {
    # --- Titles and Meta ---
    'JSON 포매터 - Tool Shelf': {
        'en': 'JSON Formatter - Tool Shelf', 'ja': 'JSONフォーマッター - Tool Shelf',
        'hi': 'JSON फॉर्मेटर - Tool Shelf', 'id': 'Pemformat JSON - Tool Shelf',
        'vi': 'Định dạng JSON - Tool Shelf', 'th': 'ตัวจัดรูปแบบ JSON - Tool Shelf',
        'de': 'JSON-Formatierer - Tool Shelf', 'pt': 'Formatador JSON - Tool Shelf'
    },
    '무료 온라인 유틸리티 모음 - Tool Shelf': {
        'en': 'Free Online Tools - Tool Shelf', 'ja': '無料オンラインツール - Tool Shelf',
        'hi': 'मुफ्त ऑनलाइन उपकरण - Tool Shelf', 'de': 'Kostenlose Online-Tools - Tool Shelf',
        'pt': 'Ferramentas Online Grátis - Tool Shelf', 'id': 'Alat Online Gratis - Tool Shelf',
        'vi': 'Công cụ trực tuyến miễn phí - Tool Shelf', 'th': 'เครื่องมือออนไลน์ฟรี - Tool Shelf'
    },
    '무료 온라인 유틸리티 모음': {
        'en': 'Free Online Tools', 'ja': '無料オンラインツール',
        'hi': 'मुफ्त ऑनलाइन उपकरण', 'de': 'Kostenlose Online-Tools',
        'pt': 'Ferramentas Online Grátis', 'id': 'Alat Online Gratis',
        'vi': 'Công cụ trực tuyến miễn phí', 'th': 'เครื่องมือออนไลน์ฟรี'
    },
    '단위 변환, PDF 도구, 이미지 변환, 계산기 등 다양한 무료 온라인 도구를 제공합니다.': {
        'en': 'Provides various free online tools such as unit conversion, PDF tools, image conversion, calculators, etc.',
        'ja': '単位変換、PDFツール、画像変換、計算機など、さまざまな無料オンラインツールを提供します。',
        'hi': 'इकाई रूपांतरण, पीडीएफ उपकरण, छवि रूपांतरण, कैलकुलेटर, आदि जैसे विभिन्न मुफ्त ऑनलाइन उपकरण प्रदान करता है।',
        'de': 'Bietet verschiedene kostenlose Online-Tools wie Einheitenumrechnung, PDF-Tools, Bildkonvertierung, Taschenrechner usw.',
        'pt': 'Fornece várias ferramentas online gratuitas, como conversão de unidades, ferramentas de PDF, conversão de imagens, calculadoras, etc.',
        'id': 'Menyediakan berbagai alat online gratis seperti konversi satuan, alat PDF, konversi gambar, kalkulator, dll.',
        'vi': 'Cung cấp các công cụ trực tuyến miễn phí khác nhau như chuyển đổi đơn vị, công cụ PDF, chuyển đổi hình ảnh, máy tính, v.v.',
        'th': 'ให้บริการเครื่องมือออนไลน์ฟรีต่างๆ เช่น การแปลงหน่วย เครื่องมือ PDF การแปลงรูปภาพ เครื่องคิดเลข ฯลฯ'
    },
    '이름표 - Tool Shelf': { # Guessing based on pattern, but let's stick to list
        'en': 'Label - Tool Shelf', 'ja': 'ラベル - Tool Shelf'
    },
    'Lorem Ipsum 생성기 - Tool Shelf': {
        'en': 'Lorem Ipsum Generator - Tool Shelf', 'ja': 'Lorem Ipsum生成器 - Tool Shelf',
        'hi': 'Lorem Ipsum जनरेटर - Tool Shelf', 'de': 'Lorem Ipsum Generator - Tool Shelf',
        'pt': 'Gerador de Lorem Ipsum - Tool Shelf', 'id': 'Generator Lorem Ipsum - Tool Shelf',
        'vi': 'Trình tạo Lorem Ipsum - Tool Shelf', 'th': 'Lorem Ipsum เบ้าหลอม - Tool Shelf'
    },
    'QR 코드 생성기 - Tool Shelf': {
        'en': 'QR Code Generator - Tool Shelf', 'ja': 'QRコード生成器 - Tool Shelf',
        'hi': 'QR कोड जनरेटर - Tool Shelf', 'de': 'QR-Code-Generator - Tool Shelf',
        'pt': 'Gerador de QR Code - Tool Shelf', 'id': 'Generator Kode QR - Tool Shelf',
        'vi': 'Trình tạo mã QR - Tool Shelf', 'th': 'เครื่องสร้างรหัส QR - Tool Shelf'
    },
    'Base64 인코더/디코더 - Tool Shelf': {
        'en': 'Base64 Encoder/Decoder - Tool Shelf', 'ja': 'Base64エンコーダー/デコーダー - Tool Shelf',
        'hi': 'Base64 एनकोडर/डिकोडर - Tool Shelf', 'de': 'Base64 Encoder/Decoder - Tool Shelf',
        'pt': 'Codificador/Decodificador Base64 - Tool Shelf', 'id': 'Encoder/Decoder Base64 - Tool Shelf',
        'vi': 'Bộ mã hóa/giải mã Base64 - Tool Shelf', 'th': 'Base64 ตัวเข้ารหัส/ตัวถอดรหัส - Tool Shelf'
    },
    '색상 변환기 - Tool Shelf': {
        'en': 'Color Converter - Tool Shelf', 'ja': '色変換ツール - Tool Shelf',
        'hi': 'रंग परिवर्तक - Tool Shelf', 'de': 'Farbkonverter - Tool Shelf',
        'pt': 'Conversor de Cores - Tool Shelf', 'id': 'Konverter Warna - Tool Shelf',
        'vi': 'Chuyển đổi màu sắc - Tool Shelf', 'th': 'ตัวแปลงสี - Tool Shelf'
    },
    '이미지 변환기 - Tool Shelf': {
        'en': 'Image Converter - Tool Shelf', 'ja': '画像変換ツール - Tool Shelf',
        'hi': 'छवि परिवर्तक - Tool Shelf', 'de': 'Bildkonverter - Tool Shelf',
        'pt': 'Conversor de Imagem - Tool Shelf', 'id': 'Konverter Gambar - Tool Shelf',
        'vi': 'Chuyển đổi hình ảnh - Tool Shelf', 'th': 'ตัวแปลงรูปภาพ - Tool Shelf'
    },
    '텍스트 유틸리티 - Tool Shelf': {
        'en': 'Text Utilities - Tool Shelf', 'ja': 'テキストユーティリティ - Tool Shelf',
        'hi': 'पाठ उपयोगिताएँ - Tool Shelf', 'de': 'Text-Dienstprogramme - Tool Shelf',
        'pt': 'Utilitários de Texto - Tool Shelf', 'id': 'Utilitas Teks - Tool Shelf',
        'vi': 'Tiện ích văn bản - Tool Shelf', 'th': 'ยูทิลิตี้ข้อความ - Tool Shelf'
    },
    'Format and validate JSON data. 압축, 포맷, 검증 기능을 제공합니다.': {
        'en': 'Format and validate JSON data. Features include minification, formatting, and validation.',
        'ja': 'JSONデータを整形および検証します。圧縮、整形、検証機能を提供します。',
        'hi': 'JSON डेटा को प्रारूपित और मान्य करें। सुविधाओं में छोटा करना, प्रारूपण और सत्यापन शामिल हैं।',
        'de': 'Formatieren und validieren Sie JSON-Daten. Funktionen umfassen Minimierung, Formatierung und Validierung.',
        'pt': 'Formate e valide dados JSON. Os recursos incluem minificação, formatação e validação.',
        'id': 'Format dan validasi data JSON. Fitur termasuk minifikasi, pemformatan, dan validasi.',
        'vi': 'Định dạng và xác thực dữ liệu JSON. Các tính năng bao gồm thu nhỏ, định dạng và xác thực.',
        'th': 'จัดรูปแบบและตรวจสอบข้อมูล JSON คุณสมบัติต่างๆ ได้แก่ การย่อขนาด การจัดรูปแบบ และการตรวจสอบ'
    },
    '단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다.': {
        'en': 'Count words, characters, remove duplicates, convert case, and more.',
        'ja': '単語数、文字数のカウント、重複の削除、大文字小文字の変換などの機能を提供します。',
        'hi': 'शब्दों और अक्षरों की गिनती करें, डुप्लिकेट हटाएँ, केस बदलें, और बहुत कुछ।',
        'de': 'Zählen Sie Wörter, Zeichen, entfernen Sie Duplikate, konvertieren Sie Groß-/Kleinschreibung und mehr.',
        'pt': 'Conte palavras, caracteres, remova duplicatas, converta maiúsculas/minúsculas e muito mais.',
        'id': 'Hitung kata, karakter, hapus duplikat, ubah kapitalisasi, dan banyak lagi.',
        'vi': 'Đếm từ, ký tự, xóa trùng lặp, chuyển đổi chữ hoa/thường và hơn thế nữa.',
        'th': 'นับคำ ตัวอักษร ลบรายการที่ซ้ำกัน แปลงตัวพิมพ์ และอื่นๆ'
    },
    'D-Day와 날짜 차이를 계산하세요.': {
        'en': 'Calculate D-Day and date differences.',
        'ja': 'D-Dayと日付の差を計算します。',
        'hi': 'D-Day और तारीख के अंतर की गणना करें।',
        'de': 'Berechnen Sie D-Day und Datumsunterschiede.',
        'pt': 'Calcule o D-Day e as diferenças de data.',
        'id': 'Hitung D-Day dan perbedaan tanggal.',
        'vi': 'Tính toán D-Day và chênh lệch ngày.',
        'th': 'คำนวณ D-Day และความแตกต่างของวันที่'
    },
    'HEX, RGB, HSL 색상 형식 간 변환을 수행하세요. 실시간 색상 미리보기와 간편한 복사 기능.': {
        'en': 'Convert between HEX, RGB, and HSL color formats. Real-time preview and easy copy.',
        'ja': 'HEX、RGB、HSL形式間で色を変換します。リアルタイムプレビューと簡単コピー機能付き。',
        'hi': 'HEX, RGB, और HSL रंग प्रारूपों के बीच कनवर्ट करें। वास्तविक समय पूर्वावलोकन और आसान प्रतिलिपि।',
        'de': 'Konvertieren Sie zwischen HEX, RGB und HSL. Echtzeit-Vorschau und einfaches Kopieren.',
        'pt': 'Converta entre formatos de cor HEX, RGB e HSL. Visualização em tempo real e cópia fácil.',
        'id': 'Konversi antara format warna HEX, RGB, dan HSL. Pratinjau real-time dan salin mudah.',
        'vi': 'Chuyển đổi giữa các định dạng màu HEX, RGB và HSL. Xem trước thời gian thực và sao chép dễ dàng.',
        'th': 'แปลงระหว่างรูปแบบสี HEX, RGB และ HSL ดูตัวอย่างแบบเรียลไทม์และคัดลอกได้ง่าย'
    },
    '이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요.': {
        'en': 'Resize images and convert to WebP, JPEG, PNG formats.',
        'ja': '画像サイズを変更し、WebP、JPEG、PNG形式に変換します。',
        'hi': 'छवियों का आकार बदलें और WebP, JPEG, PNG प्रारूपों में परिवर्तित करें।',
        'de': 'Ändern Sie die Bildgröße und konvertieren Sie in WebP, JPEG, PNG-Formate.',
        'pt': 'Redimensione imagens e converta para formatos WebP, JPEG, PNG.',
        'id': 'Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.',
        'vi': 'Thay đổi kích thước hình ảnh và chuyển đổi sang các định dạng WebP, JPEG, PNG.',
        'th': 'ปรับขนาดรูปภาพและแปลงเป็นรูปแบบ WebP, JPEG, PNG'
    },
    'Lorem Ipsum 더미 텍스트를 생성하세요.': {
        'en': 'Generate Lorem Ipsum dummy text.',
        'ja': 'Lorem Ipsumダミーテキストを生成します。',
        'hi': 'Lorem Ipsum डमी टेक्स्ट उत्पन्न करें।',
        'de': 'Generieren Sie Lorem Ipsum Blindtext.',
        'pt': 'Gere texto fictício Lorem Ipsum.',
        'id': 'Hasilkan teks dummy Lorem Ipsum.',
        'vi': 'Tạo văn bản giả Lorem Ipsum.',
        'th': 'สร้างข้อความจำลอง Lorem Ipsum'
    },
    'JPG, PNG, GIF, WebP 등 모든 이미지 형식 지원': {
        'en': 'Supports all image formats including JPG, PNG, GIF, WebP.',
        'ja': 'JPG、PNG、GIF、WebPなど全画像形式に対応。',
        'hi': 'JPG, PNG, GIF, WebP सहित सभी छवि प्रारूपों का समर्थन करता है।',
        'de': 'Unterstützt alle Bildformate einschließlich JPG, PNG, GIF, WebP.',
        'pt': 'Suporta todos os formatos de imagem, incluindo JPG, PNG, GIF, WebP.',
        'id': 'Mendukung semua format gambar termasuk JPG, PNG, GIF, WebP.',
        'vi': 'Hỗ trợ tất cả các định dạng hình ảnh bao gồm JPG, PNG, GIF, WebP.',
        'th': 'รองรับรูปแบบรูปภาพทั้งหมดรวมถึง JPG, PNG, GIF, WebP'
    },
    '이미지를 클릭하거나 드래그하여 업로드': {
        'en': 'Click or drag to upload image',
        'ja': '画像をクリックまたはドラッグしてアップロード',
        'hi': 'छवि अपलोड करने के लिए क्लिक करें या खींचें',
        'de': 'Klicken oder ziehen, um Bild hochzuladen',
        'pt': 'Clique ou arraste para enviar imagem',
        'id': 'Klik atau seret untuk mengunggah gambar',
        'vi': 'Nhấp hoặc kéo để tải lên hình ảnh',
        'th': 'คลิกหรือลากเพื่ออัปโหลดรูปภาพ'
    },
    'JSON 데이터를 입력하세요...': {
        'en': 'Enter JSON data...', 'ja': 'JSONデータを入力してください...',
        'hi': 'JSON डेटा दर्ज करें...', 'de': 'Geben Sie JSON-Daten ein...',
        'pt': 'Insira dados JSON...', 'id': 'Masukkan data JSON...',
        'vi': 'Nhập dữ liệu JSON...', 'th': 'ป้อนข้อมูล JSON...'
    },
    '텍스트를 입력하세요...': {
        'en': 'Enter text...', 'ja': 'テキストを入力してください...',
        'hi': 'पाठ दर्ज करें...', 'de': 'Geben Sie Text ein...',
        'pt': 'Insira o texto...', 'id': 'Masukkan teks...',
        'vi': 'Nhập văn bản...', 'th': 'ป้อนข้อความ...'
    },
    '인코딩할 텍스트를 입력하세요': {
        'en': 'Enter text to encode', 'ja': 'エンコードするテキストを入力',
        'hi': 'एनकोड करने के लिए टेक्स्ट दर्ज करें', 'de': 'Text zum Kodieren eingeben',
        'pt': 'Insira o texto para codificar', 'id': 'Masukkan teks untuk dikodekan',
        'vi': 'Nhập văn bản cần mã hóa', 'th': 'ป้อนข้อความที่จะเข้ารหัส'
    },
    '테스트할 문자열을 입력하세요': {
        'en': 'Enter test string', 'ja': 'テスト文字列を入力',
        'hi': 'परीक्षण स्ट्रिंग दर्ज करें', 'de': 'Testzeichenfolge eingeben',
        'pt': 'Insira a string de teste', 'id': 'Masukkan string uji',
        'vi': 'Nhập chuỗi kiểm tra', 'th': 'ป้อนสตริงทดสอบ'
    },
    '숫자 입력': {
        'en': 'Enter number', 'ja': '数値を入力',
        'hi': 'संख्या दर्ज करें', 'de': 'Nummer eingeben',
        'pt': 'Insira o número', 'id': 'Masukkan angka',
        'vi': 'Nhập số', 'th': 'ป้อนตัวเลข'
    },

    # --- UI Labels & Buttons ---
    '결과': { 'en': 'Result', 'ja': '結果', 'hi': 'परिणाम', 'de': 'Ergebnis', 'pt': 'Resultado', 'id': 'Hasil', 'vi': 'Kết quả', 'th': 'ผลลัพธ์' },
    '변환된 값': { 'en': 'Converted Value', 'ja': '変換後の値', 'hi': 'परिवर्तित मान', 'de': 'Konvertierter Wert', 'pt': 'Valor Convertido', 'id': 'Nilai Dikonversi', 'vi': 'Giá trị đã chuyển đổi', 'th': 'ค่าที่แปลง' },
    '변환할 값': { 'en': 'Value to Convert', 'ja': '変換する値', 'hi': 'परिवर्तित करने के लिए मान', 'de': 'Zu konvertierender Wert', 'pt': 'Valor para Converter', 'id': 'Nilai untuk Dikonversi', 'vi': 'Giá trị cần chuyển đổi', 'th': 'ค่าที่จะแปลง' },
    '작업': { 'en': 'Action', 'ja': '操作', 'hi': 'कार्रवाई', 'de': 'Aktion', 'pt': 'Ação', 'id': 'Tindakan', 'vi': 'Hành động', 'th': 'การกระทำ' },
    '통계': { 'en': 'Statistics', 'ja': '統計', 'hi': 'आंकड़े', 'de': 'Statistik', 'pt': 'Estatísticas', 'id': 'Statistik', 'vi': 'Thống kê', 'th': 'สถิติ' },
    '출력 형식': { 'en': 'Output Format', 'ja': '出力形式', 'hi': 'आउटपुट प्रारूप', 'de': 'Ausgabeformat', 'pt': 'Formato de Saída', 'id': 'Format Keluaran', 'vi': 'Định dạng đầu ra', 'th': 'รูปแบบผลลัพธ์' },
    '색상 형식': { 'en': 'Color Format', 'ja': '色形式', 'hi': 'रंग प्रारूप', 'de': 'Farbformat', 'pt': 'Formato de Cor', 'id': 'Format Warna', 'vi': 'Định dạng màu', 'th': 'รูปแบบสี' },
    '인기 색상': { 'en': 'Popular Colors', 'ja': '人気の色', 'hi': 'लोकप्रिय रंग', 'de': 'Beliebte Farben', 'pt': 'Cores Populares', 'id': 'Warna Populer', 'vi': 'Màu phổ biến', 'th': 'สียอดนิยม' },
    '자주 사용하는 변환': { 'en': 'Common Conversions', 'ja': 'よく使う変換', 'hi': 'सामान्य रूपांतरण', 'de': 'Häufige Umrechnungen', 'pt': 'Conversões Comuns', 'id': 'Konversi Umum', 'vi': 'Chuyển đổi phổ biến', 'th': 'การแปลงทั่วไป' },
    '빨강': { 'en': 'Red', 'ja': '赤', 'hi': 'लाल', 'de': 'Rot', 'pt': 'Vermelho', 'id': 'Merah', 'vi': 'Đỏ', 'th': 'แดง' },
    '초록': { 'en': 'Green', 'ja': '緑', 'hi': 'हरा', 'de': 'Grün', 'pt': 'Verde', 'id': 'Hijau', 'vi': 'Xanh lá', 'th': 'เขียว' },
    '파랑': { 'en': 'Blue', 'ja': '青', 'hi': 'नीला', 'de': 'Blau', 'pt': 'Azul', 'id': 'Biru', 'vi': 'Xanh dương', 'th': 'น้ำเงิน' },
    '길이': { 'en': 'Length', 'ja': '長さ', 'hi': 'लंबाई', 'de': 'Länge', 'pt': 'Comprimento', 'id': 'Panjang', 'vi': 'Chiều dài', 'th': 'ความยาว' },
    '무게': { 'en': 'Weight', 'ja': '重さ', 'hi': 'वजन', 'de': 'Gewicht', 'pt': 'Peso', 'id': 'Berat', 'vi': 'Cân nặng', 'th': 'น้ำหนัก' },
    '부피': { 'en': 'Volume', 'ja': '体積', 'hi': 'आयतन', 'de': 'Volumen', 'pt': 'Volume', 'id': 'Volume', 'vi': 'Thể tích', 'th': 'ปริมาตร' },
    '넓이': { 'en': 'Area', 'ja': '面積', 'hi': 'क्षेत्रफल', 'de': 'Fläche', 'pt': 'Área', 'id': 'Area', 'vi': 'Diện tích', 'th': 'พื้นที่' },
    '면적': { 'en': 'Area', 'ja': '面積', 'hi': 'क्षेत्रफल', 'de': 'Fläche', 'pt': 'Área', 'id': 'Area', 'vi': 'Diện tích', 'th': 'พื้นที่' },
    '온도': { 'en': 'Temperature', 'ja': '温度', 'hi': 'तापमान', 'de': 'Temperatur', 'pt': 'Temperatura', 'id': 'Suhu', 'vi': 'Nhiệt độ', 'th': 'อุณหภูมิ' },
    '속도': { 'en': 'Speed', 'ja': '速度', 'hi': 'गति', 'de': 'Geschwindigkeit', 'pt': 'Velocidade', 'id': 'Kecepatan', 'vi': 'Tốc độ', 'th': 'ความเร็ว' },
    '원본 이미지': { 'en': 'Original Image', 'ja': '元画像', 'hi': 'मूल छवि', 'de': 'Originalbild', 'pt': 'Imagem Original', 'id': 'Gambar Asli', 'vi': 'Hình ảnh gốc', 'th': 'รูปภาพต้นฉบับ' },
    '변환된 이미지': { 'en': 'Converted Image', 'ja': '変換画像', 'hi': 'परिवर्तित छवि', 'de': 'Konvertiertes Bild', 'pt': 'Imagem Convertida', 'id': 'Gambar Dikonversi', 'vi': 'Hình ảnh đã chuyển đổi', 'th': 'รูปภาพที่แปลง' },
    '품질 (%)': { 'en': 'Quality (%)', 'ja': '品質 (%)', 'hi': 'गुणवत्ता (%)', 'de': 'Qualität (%)', 'pt': 'Qualidade (%)', 'id': 'Kualitas (%)', 'vi': 'Chất lượng (%)', 'th': 'คุณภาพ (%)' },
    '너비 (px)': { 'en': 'Width (px)', 'ja': '幅 (px)', 'hi': 'चौड़ाई (px)', 'de': 'Breite (px)', 'pt': 'Largura (px)', 'id': 'Lebar (px)', 'vi': 'Chiều rộng (px)', 'th': 'ความกว้าง (px)' },
    '높이 (px)': { 'en': 'Height (px)', 'ja': '高さ (px)', 'hi': 'ऊंचाई (px)', 'de': 'Höhe (px)', 'pt': 'Altura (px)', 'id': 'Tinggi (px)', 'vi': 'Chiều cao (px)', 'th': 'ความสูง (px)' },
    '하이라이트': { 'en': 'Highlight', 'ja': 'ハイライト', 'hi': 'हाइलाइट', 'de': 'Hervorheben', 'pt': 'Destaque', 'id': 'Sorot', 'vi': 'Nổi bật', 'th': 'ไฮไลท์' },
    '초기화': { 'en': 'Reset', 'ja': 'リセット', 'hi': 'रीसेट', 'de': 'Zurücksetzen', 'pt': 'Redefinir', 'id': 'Reset', 'vi': 'Đặt lại', 'th': 'รีเซ็ต' },
    '다운로드': { 'en': 'Download', 'ja': 'ダウンロード', 'hi': 'डाउनलोड', 'de': 'Herunterladen', 'pt': 'Baixar', 'id': 'Unduh', 'vi': 'Tải xuống', 'th': 'ดาวน์โหลด' },
    '변환하기': { 'en': 'Convert', 'ja': '変換', 'hi': 'कनवर्ट', 'de': 'Konvertieren', 'pt': 'Converter', 'id': 'Konversi', 'vi': 'Chuyển đổi', 'th': 'แปลง' },
    '복사': { 'en': 'Copy', 'ja': 'コピー', 'hi': 'कॉपी', 'de': 'Kopieren', 'pt': 'Copiar', 'id': 'Salin', 'vi': 'Sao chép', 'th': 'คัดลอก' },
    '광고 영역': { 'en': 'Advertisement', 'ja': '広告', 'hi': 'विज्ञापन', 'de': 'Werbung', 'pt': 'Publicidade', 'id': 'Iklan', 'vi': 'Quảng cáo', 'th': 'โฆษณา' },

    # --- Specific Icons + Text combinations ---
    '📋 복사': { 'en': '📋 Copy', 'ja': '📋 コピー', 'hi': '📋 कॉपी', 'de': '📋 Kopieren', 'pt': '📋 Copiar', 'id': '📋 Salin', 'vi': '📋 Sao chép', 'th': '📋 คัดลอก' },
    '🗑️ 초기화': { 'en': '🗑️ Clear', 'ja': '🗑️ クリア', 'hi': '🗑️ साफ़', 'de': '🗑️ Löschen', 'pt': '🗑️ Limpar', 'id': '🗑️ Hapus', 'vi': '🗑️ Xóa', 'th': '🗑️ ล้าง' },
    '🖼️ 이미지 변환기': { 'en': '🖼️ Image Converter', 'ja': '🖼️ 画像変換', 'hi': '🖼️ छवि परिवर्तक', 'de': '🖼️ Bildkonverter', 'pt': '🖼️ Conversor de Imagem', 'id': '🖼️ Konverter Gambar', 'vi': '🖼️ Chuyển đổi hình ảnh', 'th': '🖼️ ตัวแปลงรูปภาพ' },
    
    # --- JS Template Strings (Tricky ones) ---
    '매칭 결과 (${matches.length}개)': {
        'en': 'Matches (${matches.length})', 'ja': '一致結果 (${matches.length}個)',
        'hi': 'परिणाम (${matches.length})', 'de': 'Ergebnisse (${matches.length})',
        'pt': 'Resultados (${matches.length})', 'id': 'Hasil (${matches.length})',
        'vi': 'Kết quả (${matches.length})', 'th': 'ผลลัพธ์ (${matches.length})'
    },
    '매칭 결과 없음': {
        'en': 'No matches found', 'ja': '一致が見つかりません',
        'hi': 'कोई मेल नहीं मिला', 'de': 'Keine Treffer gefunden',
        'pt': 'Nenhuma correspondência encontrada', 'id': 'Tidak ada kecocokan',
        'vi': 'Không tìm thấy kết quả', 'th': 'ไม่พบรายการที่ตรงกัน'
    },
    'Match ${i + 1}: "${match[0]}" (위치: ${match.index})': {
        'en': 'Match ${i + 1}: "${match[0]}" (Index: ${match.index})',
        'ja': '一致 ${i + 1}: "${match[0]}" (位置: ${match.index})',
        'hi': 'मैच ${i + 1}: "${match[0]}" (सूचकांक: ${match.index})',
        'de': 'Treffer ${i + 1}: "${match[0]}" (Index: ${match.index})',
        'pt': 'Correspondência ${i + 1}: "${match[0]}" (Índice: ${match.index})',
        'id': 'Cocok ${i + 1}: "${match[0]}" (Indeks: ${match.index})',
        'vi': 'Khớp ${i + 1}: "${match[0]}" (Chỉ số: ${match.index})',
        'th': 'ตรงกัน ${i + 1}: "${match[0]}" (ดัชนี: ${match.index})'
    },
    '오류: ${e.message}': {
        'en': 'Error: ${e.message}', 'ja': 'エラー: ${e.message}',
        'hi': 'त्रुटि: ${e.message}', 'de': 'Fehler: ${e.message}',
        'pt': 'Erro: ${e.message}', 'id': 'Kesalahan: ${e.message}',
        'vi': 'Lỗi: ${e.message}', 'th': 'ข้อผิดพลาด: ${e.message}'
    },
    
    # --- Critical UI Messages (JS Alerts/Toasts) ---
    '✓ 유효한 JSON입니다': { 'en': '✓ Valid JSON', 'ja': '✓ 有効なJSONです', 'hi': '✓ मान्य JSON', 'de': '✓ Gültiges JSON', 'pt': '✓ JSON Válido', 'id': '✓ JSON Valid', 'vi': '✓ JSON hợp lệ', 'th': '✓ JSON ที่ถูกต้อง' },
    '✗ 유효하지 않은 JSON입니다': { 'en': '✗ Invalid JSON', 'ja': '✗ 無効なJSONです', 'hi': '✗ अमान्य JSON', 'de': '✗ Ungültiges JSON', 'pt': '✗ JSON Inválido', 'id': '✗ JSON Tidak Valid', 'vi': '✗ JSON không hợp lệ', 'th': '✗ JSON ไม่ถูกต้อง' },
    '오류:': { 'en': 'Error:', 'ja': 'エラー:', 'hi': 'त्रुटि:', 'de': 'Fehler:', 'pt': 'Erro:', 'id': 'Kesalahan:', 'vi': 'Lỗi:', 'th': 'ข้อผิดพลาด:' },
    'Copy할 내용이 없습니다.': { 'en': 'Nothing to copy.', 'ja': 'コピーする内容がありません。', 'hi': 'कॉपी करने के लिए कुछ नहीं है।', 'de': 'Nichts zum Kopieren.', 'pt': 'Nada para copiar.', 'id': 'Tidak ada yang bisa disalin.', 'vi': 'Không có gì để sao chép.', 'th': 'ไม่มีอะไรให้คัดลอก' },
    '클립보드 Copy 실패:': { 'en': 'Clipboard copy failed:', 'ja': 'クリップボードへのコピーに失敗:', 'hi': 'क्लिपबोर्ड कॉपी विफल:', 'de': 'Zwischenablage kopieren fehlgeschlagen:', 'pt': 'Falha na cópia da área de transferência:', 'id': 'Gagal menyalin papan klip:', 'vi': 'Sao chép khay nhớ tạm thất bại:', 'th': 'การคัดลอกคลิปบอร์ดล้มเหลว:' },
    '클립보드 Copy에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'ja': 'クリップボードへのコピーに失敗しました。', 'hi': 'क्लिपबोर्ड पर कॉपी करने में विफल।', 'de': 'Kopieren in die Zwischenablage fehlgeschlagen.', 'pt': 'Falha ao copiar para a área de transferência.', 'id': 'Gagal menyalin ke papan klip.', 'vi': 'Không thể sao chép vào khay nhớ tạm.', 'th': 'คัดลอกไปยังคลิปบอร์ดไม่สำเร็จ' },
    '이미지 파일만 업로드할 수 있습니다.': { 'en': 'Only image files can be uploaded.', 'ja': '画像ファイルのみアップロード可能です。', 'hi': 'केवल छवि फ़ाइलें अपलोड की जा सकती हैं।', 'de': 'Nur Bilddateien können hochgeladen werden.', 'pt': 'Apenas arquivos de imagem podem ser carregados.', 'id': 'Hanya file gambar yang dapat diunggah.', 'vi': 'Chỉ có thể tải lên tệp hình ảnh.', 'th': 'อัปโหลดได้เฉพาะไฟล์รูปภาพเท่านั้น' },
    '시간 종료!': { 'en': 'Time is up!', 'ja': '時間終了！', 'hi': 'समय समाप्त!', 'de': 'Zeit ist um!', 'pt': 'O tempo acabou!', 'id': 'Waktu habis!', 'vi': 'Hết giờ!', 'th': 'หมดเวลา!' },
    '오늘 날짜를 찾을 수 없습니다.': { 'en': 'Today\'s date not found.', 'ja': '今日の日付が見つかりません。', 'hi': 'आज की तारीख नहीं मिली।', 'de': 'Das heutige Datum wurde nicht gefunden.', 'pt': 'Data de hoje não encontrada.', 'id': 'Tanggal hari ini tidak ditemukan.', 'vi': 'Không tìm thấy ngày hôm nay.', 'th': 'ไม่พบวันที่ของวันนี้' },
    'SQL 쿼리를 입력해주세요.': { 'en': 'Please enter SQL query.', 'ja': 'SQLクエリを入力してください。', 'hi': 'कृपया SQL क्वेरी दर्ज करें।', 'de': 'Bitte geben Sie eine SQL-Abfrage ein.', 'pt': 'Por favor, insira a consulta SQL.', 'id': 'Silakan masukkan kueri SQL.', 'vi': 'Vui lòng nhập truy vấn SQL.', 'th': 'กรุณาป้อนคิวรี SQL' },
    '디코딩 오류:': { 'en': 'Decoding Error:', 'ja': 'デコードエラー:', 'hi': 'डिकोडिंग त्रुटि:', 'de': 'Dekodierungsfehler:', 'pt': 'Erro de Decodificação:', 'id': 'Kesalahan Dekode:', 'vi': 'Lỗi giải mã:', 'th': 'ข้อผิดพลาดในการถอดรหัส:' },
    '인코딩 오류:': { 'en': 'Encoding Error:', 'ja': 'エンコードエラー:', 'hi': 'एन्को딩 त्रुटि:', 'de': 'Kodierungsfehler:', 'pt': 'Erro de Codificação:', 'id': 'Kesalahan Enkode:', 'vi': 'Lỗi mã hóa:', 'th': 'ข้อผิดพลาดในการเข้ารหัส:' },
    '성경 소개를 찾을 수 없습니다.': { 'en': 'Bible introduction not found.', 'ja': '聖書の紹介が見つかりません。', 'hi': 'बाइबल परिचय नहीं मिला।', 'de': 'Bibelevangelium nicht gefunden.', 'pt': 'Introdução da Bíblia não encontrada.', 'id': 'Pengantar Alkitab tidak ditemukan.', 'vi': 'Không tìm thấy giới thiệu Kinh Thánh.', 'th': 'ไม่พบคำแนะนำพระคัมภีร์' },

    # --- Units ---
    '갤런 (gal)': { 'en': 'Gallon (gal)', 'ja': 'ガロン (gal)', 'de': 'Gallone (gal)', 'pt': 'Galão (gal)' },
    '노트 (knot)': { 'en': 'Knot (knot)', 'ja': 'ノット (knot)', 'de': 'Knoten (knot)', 'pt': 'Nó (knot)' },
    '섭씨 (°C)': { 'en': 'Celsius (°C)', 'ja': '摂氏 (°C)', 'de': 'Celsius (°C)', 'pt': 'Celsius (°C)' },
    '화씨 (°F)': { 'en': 'Fahrenheit (°F)', 'ja': '華氏 (°F)', 'de': 'Fahrenheit (°F)', 'pt': 'Fahrenheit (°F)' },
    '켈빈 (K)': { 'en': 'Kelvin (K)', 'ja': 'ケルビン (K)', 'de': 'Kelvin (K)', 'pt': 'Kelvin (K)' },
    '미터 (m)': { 'en': 'Meter (m)', 'ja': 'メートル (m)', 'de': 'Meter (m)', 'pt': 'Metro (m)' },
    '킬로미터 (km)': { 'en': 'Kilometer (km)', 'ja': 'キロメートル (km)', 'de': 'Kilometer (km)', 'pt': 'Quilômetro (km)' },
    '센티미터 (cm)': { 'en': 'Centimeter (cm)', 'ja': 'センチメートル (cm)', 'de': 'Zentimeter (cm)', 'pt': 'Centímetro (cm)' },
    '밀리미터 (mm)': { 'en': 'Millimeter (mm)', 'ja': 'ミリメートル (mm)', 'de': 'Millimeter (mm)', 'pt': 'Milímetro (mm)' },
    '인치 (in)': { 'en': 'Inch (in)', 'ja': 'インチ (in)', 'de': 'Zoll (in)', 'pt': 'Polegada (in)' },
    '피트 (ft)': { 'en': 'Feet (ft)', 'ja': 'フィート (ft)', 'de': 'Fuß (ft)', 'pt': 'Pés (ft)' },
    '야드 (yd)': { 'en': 'Yard (yd)', 'ja': 'ヤード (yd)', 'de': 'Yard (yd)', 'pt': 'Jarda (yd)' },
    '마일 (mi)': { 'en': 'Mile (mi)', 'ja': 'マイル (mi)', 'de': 'Meile (mi)', 'pt': 'Milha (mi)' },
    '킬로그램 (kg)': { 'en': 'Kilogram (kg)', 'ja': 'キログラム (kg)', 'de': 'Kilogramm (kg)', 'pt': 'Quilograma (kg)' },
    '그램 (g)': { 'en': 'Gram (g)', 'ja': 'グラム (g)', 'de': 'Gramm (g)', 'pt': 'Grama (g)' },
    '밀리그램 (mg)': { 'en': 'Milligram (mg)', 'ja': 'ミリグラム (mg)', 'de': 'Milligramm (mg)', 'pt': 'Miligrama (mg)' },
    '톤 (t)': { 'en': 'Ton (t)', 'ja': 'トン (t)', 'de': 'Tonne (t)', 'pt': 'Tonelada (t)' },
    '파운드 (lb)': { 'en': 'Pound (lb)', 'ja': 'ポンド (lb)', 'de': 'Pfund (lb)', 'pt': 'Libra (lb)' },
    '온스 (oz)': { 'en': 'Ounce (oz)', 'ja': 'オンス (oz)', 'de': 'Unze (oz)', 'pt': 'Onça (oz)' },
    '리터 (L)': { 'en': 'Liter (L)', 'ja': 'リットル (L)', 'de': 'Liter (L)', 'pt': 'Litro (L)' },
    '밀리리터 (mL)': { 'en': 'Milliliter (mL)', 'ja': 'ミリリットル (mL)', 'de': 'Milliliter (mL)', 'pt': 'Mililitro (mL)' },
    '세제곱미터 (m³)': { 'en': 'Cubic Meter (m³)', 'ja': '立方メートル (m³)', 'de': 'Kubikmeter (m³)', 'pt': 'Metro Cúbico (m³)' },
    '갤런 (gal)': { 'en': 'Gallon (gal)', 'ja': 'ガロン (gal)', 'de': 'Gallone (gal)', 'pt': 'Galão (gal)' },
    '쿼트 (qt)': { 'en': 'Quart (qt)', 'ja': 'クォート (qt)', 'de': 'Quart (qt)', 'pt': 'Quarto (qt)' },
    '파인트 (pt)': { 'en': 'Pint (pt)', 'ja': 'パイント (pt)', 'de': 'Pinte (pt)', 'pt': 'Pinto (pt)' },
    '컵 (cup)': { 'en': 'Cup', 'ja': 'カップ', 'de': 'Tasse', 'pt': 'Xícara' },

    # --- Missed Exact Matches ---
    '이미지 변환기': { 'en': 'Image Converter', 'ja': '画像変換ツール', 'hi': 'छवि परिवर्तक', 'de': 'Bildkonverter', 'pt': 'Conversor de Imagem', 'id': 'Konverter Gambar', 'vi': 'Chuyển đổi hình ảnh', 'th': 'ตัวแปลงรูปภาพ' },
    '텍스트를 입력하세요.': { 'en': 'Enter text.', 'ja': 'テキストを入力してください。', 'hi': 'पाठ दर्ज करें।', 'de': 'Geben Sie Text ein.', 'pt': 'Insira o texto.', 'id': 'Masukkan teks.', 'vi': 'Nhập văn bản.', 'th': 'ป้อนข้อความ' },

    # --- Fix Broken Partial Translations (Short Forms) ---
    '클립보드 Copiar 실패:': { 'en': 'Clipboard copy failed:', 'pt': 'Falha na cópia da área de transferência:' },
    '클립보드 Kopieren 실패:': { 'en': 'Clipboard copy failed:', 'de': 'Zwischenablage kopieren fehlgeschlagen:' },
    '클립보드 Salin 실패:': { 'en': 'Clipboard copy failed:', 'id': 'Gagal menyalin papan klip:' },
    '클립보드 Sao chép 실패:': { 'en': 'Clipboard copy failed:', 'vi': 'Sao chép khay nhớ tạm thất bại:' },
    '클립보드 कॉपी 실패:': { 'en': 'Clipboard copy failed:', 'hi': 'क्लिपबोर्ड कॉपी विफल:' },
    '클립보드 คัดลอก 실패:': { 'en': 'Clipboard copy failed:', 'th': 'การคัดลอกคลิปบอร์ดล้มเหลว:' },
    '클립보드 コピー 실패:': { 'en': 'Clipboard copy failed:', 'ja': 'クリップボードへのコピーに失敗:' },

    '단위 교환': { 'en': 'Swap Units', 'ja': '単位の入れ替え', 'hi': 'इकाइयों की अदला-बदली', 'de': 'Einheiten tauschen', 'pt': 'Trocar Unidades', 'id': 'Tukar Unit', 'vi': 'Hoán đổi đơn vị', 'th': 'สลับหน่วย' },
    
    # --- Area/Speed Units ---
    '제곱미터 (m²)': { 'en': 'Square Meter (m²)', 'ja': '平方メートル (m²)', 'de': 'Quadratmeter (m²)', 'pt': 'Metro Quadrado (m²)' },
    '제곱킬로미터 (km²)': { 'en': 'Square Kilometer (km²)', 'ja': '平方キロメートル (km²)', 'de': 'Quadratkilometer (km²)', 'pt': 'Quilômetro Quadrado (km²)' },
    '제곱센티미터 (cm²)': { 'en': 'Square Centimeter (cm²)', 'ja': '平方センチメートル (cm²)', 'de': 'Quadratzentimeter (cm²)', 'pt': 'Centímetro Quadrado (cm²)' },
    '헥타르 (ha)': { 'en': 'Hectare (ha)', 'ja': 'ヘクタール (ha)', 'de': 'Hektar (ha)', 'pt': 'Hectare (ha)' },
    '에이커 (ac)': { 'en': 'Acre (ac)', 'ja': 'エーカー (ac)', 'de': 'Acker (ac)', 'pt': 'Acre (ac)' },
    '제곱피트 (ft²)': { 'en': 'Square Foot (ft²)', 'ja': '平方フィート (ft²)', 'de': 'Quadratfuß (ft²)', 'pt': 'Pé Quadrado (ft²)' },
    '미터/초 (m/s)': { 'en': 'Meter/Second (m/s)', 'ja': 'メートル/秒 (m/s)', 'de': 'Meter/Sekunde (m/s)', 'pt': 'Metro/Segundo (m/s)' },
    '킬로미터/시 (km/h)': { 'en': 'Kilometer/Hour (km/h)', 'ja': 'キロメートル/時 (km/h)', 'de': 'Kilometer/Stunde (km/h)', 'pt': 'Quilômetro/Hora (km/h)' },
    '마일/시 (mph)': { 'en': 'Mile/Hour (mph)', 'ja': 'マイル/時 (mph)', 'de': 'Meilen/Stunde (mph)', 'pt': 'Milha/Hora (mph)' },

    # --- Days ---
    '일요일': { 'en': 'Sunday', 'ja': '日曜日' },
    '월요일': { 'en': 'Monday', 'ja': '月曜日' },
    '화요일': { 'en': 'Tuesday', 'ja': '火曜日' },
    '수요일': { 'en': 'Wednesday', 'ja': '水曜日' },
    '목요일': { 'en': 'Thursday', 'ja': '木曜日' },
    '금요일': { 'en': 'Friday', 'ja': '金曜日' },
    '토요일': { 'en': 'Saturday', 'ja': '土曜日' },
    '월': { 'en': 'Mon', 'ja': '月' },
    '화': { 'en': 'Tue', 'ja': '火' },
    '수': { 'en': 'Wed', 'ja': '水' },
    '목': { 'en': 'Thu', 'ja': '木' },
    '금': { 'en': 'Fri', 'ja': '金' },
    '토': { 'en': 'Sat', 'ja': '土' },
    '일': { 'en': 'Sun', 'ja': '日' }, # Careful, this is 1 char string

    # --- Color Converter ---
    'RGB 슬라이더': { 'en': 'RGB Sliders', 'ja': 'RGBスライダー', 'hi': 'RGB स्लाइडर', 'de': 'RGB-Regler', 'pt': 'Controles deslizantes RGB', 'id': 'Slider RGB', 'vi': 'Thanh trượt RGB', 'th': 'ตัวเลื่อน RGB' },
    '투명도 (Alpha)': { 'en': 'Alpha', 'ja': '透明度 (Alpha)', 'hi': 'अल्फा', 'de': 'Alpha', 'pt': 'Alfa', 'id': 'Alfa', 'vi': 'Alpha', 'th': 'อัลฟ่า' },
    '색상 (Hue)': { 'en': 'Hue', 'ja': '色相 (Hue)', 'hi': 'ह्यू', 'de': 'Farbton', 'pt': 'Matiz', 'id': 'Rona', 'vi': 'Huế', 'th': 'ฮิว' },
    '채도 (Saturation)': { 'en': 'Saturation', 'ja': '彩度 (Saturation)', 'hi': 'संतृप्ति', 'de': 'Sättigung', 'pt': 'Saturação', 'id': 'Saturasi', 'vi': 'Độ bão hòa', 'th': 'ความอิ่มตัว' },
    '명도 (Lightness)': { 'en': 'Lightness', 'ja': '明度 (Lightness)', 'hi': 'लपट', 'de': 'Helligkeit', 'pt': 'Luminosidade', 'id': 'Kecerahan', 'vi': 'Độ sáng', 'th': 'ความสว่าง' },

    # --- BMI Calculator ---
    '저체중': { 'en': 'Underweight', 'ja': '低体重', 'hi': 'कम वजन', 'de': 'Untergewicht', 'pt': 'Abaixo do peso', 'id': 'Kurus', 'vi': 'Thiếu cân', 'th': 'น้ำหนักน้อย' },
    '정상': { 'en': 'Normal', 'ja': '普通体重', 'hi': 'सामान्य', 'de': 'Normalgewicht', 'pt': 'Normal', 'id': 'Normal', 'vi': 'Bình thường', 'th': 'ปกติ' },
    '과체중': { 'en': 'Overweight', 'ja': '過体重', 'hi': 'अधिक वजन', 'de': 'Übergewicht', 'pt': 'Sobrepeso', 'id': 'Kelebihan berat badan', 'vi': 'Thừa cân', 'th': 'น้ำหนักเกิน' },
    '비만': { 'en': 'Obese', 'ja': '肥満', 'hi': 'मोटापा', 'de': 'Fettleibig', 'pt': 'Obeso', 'id': 'Obesitas', 'vi': 'Béo phì', 'th': 'อ้วน' },

    # --- Daily Verse / Bible (Partial coverage) ---
    '성경읽기 Copy기': { 'en': 'Bible Verse Copier', 'ja': '聖書の一節コピー', 'hi': 'बाइबल पद्य कॉपियर' },
    '성경 읽기 계획': { 'en': 'Bible Reading Plan', 'ja': '聖書通読プラン', 'hi': 'बाइबल पढ़ने की योजना' },
    '매일 읽을 성경 구절을 클릭 한 번으로 복사하고 공유하세요.': { 'en': 'Copy and share daily Bible verses with one click.', 'ja': '毎日の聖書の一節をワンクリックでコピーして共有します。' },
    '오늘 날짜 Highlight': { 'en': 'Highlight Today', 'ja': '今日の日付をハイライト' },
    'Go to Today': { 'en': 'Go to Today', 'ja': '今日へ移動' },
    'Copied Verse': { 'en': 'Copied Verse', 'ja': 'コピーされた節' },

    # --- Fix Broken Partial Translations ---
    '클립보드 Copiar에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'pt': 'Falha ao copiar para a área de transferência.' },
    '클립보드 Copy에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'ja': 'クリップボードへのコピーに失敗しました。' },
    '클립보드 Kopieren에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'de': 'Kopieren in die Zwischenablage fehlgeschlagen.' },
    '클립보드 Salin에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'id': 'Gagal menyalin ke papan klip.' },
    '클립보드 Sao chép에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'vi': 'Không thể sao chép vào khay nhớ tạm.' },
    '클립보드 कॉपी에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'hi': 'क्लिपबोर्ड पर कॉपी करने में विफल।' },
    '클립보드 คัดลอก에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'th': 'คัดลอกไปยังคลิปบอร์ดไม่สำเร็จ' },
    '클립보드 コピー에 실패했습니다.': { 'en': 'Failed to copy to clipboard.', 'ja': 'クリップボードへのコピーに失敗しました。' },

    # --- Regex Flags ---
    'g (전역)': { 'en': 'g (Global)', 'ja': 'g (グローバル)', 'hi': 'g (वैश्विक)', 'de': 'g (Global)', 'pt': 'g (Global)', 'id': 'g (Global)', 'vi': 'g (Toàn cầu)', 'th': 'g (ทั่วโลก)' },
    'i (대소문자 무시)': { 'en': 'i (Case insensitive)', 'ja': 'i (大文字小文字無視)', 'hi': 'i (केस असंवेदनशील)', 'de': 'i (Groß-/Kleinschreibung ignorieren)', 'pt': 'i (Insensível a maiúsculas)', 'id': 'i (Tidak peka huruf besar/kecil)', 'vi': 'i (Không phân biệt hoa thường)', 'th': 'i (ไม่แยกตัวพิมพ์ใหญ่-เล็ก)' },
    'm (여러 줄)': { 'en': 'm (Multiline)', 'ja': 'm (複数行)', 'hi': 'm (बहु-पंक्ति)', 'de': 'm (Mehrzeilig)', 'pt': 'm (Multilinear)', 'id': 'm (Multi-baris)', 'vi': 'm (Nhiều dòng)', 'th': 'm (หลายบรรทัด)' },
}

def translate_file(file_path, lang_code):
    try:
        if not file_path.exists(): return False
        
        # Read content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Sort keys by length descending to specific matches first
        keys = sorted(MASTER_MAP.keys(), key=len, reverse=True)
        
        for k_korean in keys:
            if k_korean in content:
                # Get translation
                translations = MASTER_MAP[k_korean]
                replacement = translations.get(lang_code, translations.get('en'))
                
                if replacement:
                    content = content.replace(k_korean, replacement)
        
        # Write back only if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Script is in tool_shelf/scripts/translation_v2
    # We need to go up two levels to get to tool_shelf root
    base_dir = Path(__file__).parent.parent.parent
    
    # Languages to process (excluding ko)
    languages = ['en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']
    
    print("🚀 Starting Master Translation Fix...")
    
    count = 0
    with ThreadPoolExecutor() as executor:
        futures = []
        for lang in languages:
            lang_dir = base_dir / lang
            if not lang_dir.exists(): continue
            
            for file_path in lang_dir.rglob('*.html'):
                futures.append(executor.submit(translate_file, file_path, lang))
                
        for future in futures:
            if future.result():
                count += 1
                
    print(f"✅ Finished. Updated {count} files.")

if __name__ == '__main__':
    main()

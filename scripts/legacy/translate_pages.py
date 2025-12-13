#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilify 다국어 번역 자동화 스크립트
한국어 원본을 기반으로 9개 언어로 자동 번역
"""

import os
import re
from pathlib import Path

# 번역 매핑 정의
TRANSLATIONS = {
    'en': {
        'lang': 'en',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'Image Converter',
        'image_converter_desc': 'Resize images and convert to WebP, JPEG, PNG formats.',
        'image_converter_desc_full': 'Resize images and convert to WebP, JPEG, PNG formats. Process directly in your browser.',
        'upload_text': 'Click or drag image to upload',
        'upload_info': 'Supports all image formats: JPG, PNG, GIF, WebP, etc.',
        'width': 'Width',
        'height': 'Height',
        'output_format': 'Output Format',
        'quality': 'Quality',
        'convert': 'Convert',
        'reset': 'Reset',
        'original_image': 'Original Image',
        'converted_image': 'Converted Image',
        'download': 'Download',
        'alert_image_only': 'Please upload an image file only.',
    },
    'ja': {
        'lang': 'ja',
        'title_suffix': ' - Utilify',
        'image_converter_title': '画像変換',
        'image_converter_desc': '画像のサイズ変更とWebP、JPEG、PNG形式への変換。',
        'image_converter_desc_full': '画像のサイズ変更とWebP、JPEG、PNG形式への変換。ブラウザで直接処理されます。',
        'upload_text': '画像をクリックまたはドラッグしてアップロード',
        'upload_info': 'すべての画像形式をサポート：JPG、PNG、GIF、WebPなど',
        'width': '幅',
        'height': '高さ',
        'output_format': '出力形式',
        'quality': '品質',
        'convert': '変換',
        'reset': 'リセット',
        'original_image': '元の画像',
        'converted_image': '変換された画像',
        'download': 'ダウンロード',
        'alert_image_only': '画像ファイルのみアップロードできます。',
    },
    'hi': {
        'lang': 'hi',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'छवि परिवर्तक',
        'image_converter_desc': 'छवि का आकार बदलें और WebP, JPEG, PNG प्रारूपों में परिवर्तित करें।',
        'image_converter_desc_full': 'छवि का आकार बदलें और WebP, JPEG, PNG प्रारूपों में परिवर्तित करें। ब्राउज़र में सीधे प्रोसेस करें।',
        'upload_text': 'छवि अपलोड करने के लिए क्लिक करें या ड्रैग करें',
        'upload_info': 'सभी छवि प्रारूप समर्थित: JPG, PNG, GIF, WebP आदि',
        'width': 'चौड़ाई',
        'height': 'ऊंचाई',
        'output_format': 'आउटपुट प्रारूप',
        'quality': 'गुणवत्ता',
        'convert': 'परिवर्तित करें',
        'reset': 'रीसेट',
        'original_image': 'मूल छवि',
        'converted_image': 'परिवर्तित छवि',
        'download': 'डाउनलोड',
        'alert_image_only': 'केवल छवि फ़ाइलें अपलोड की जा सकती हैं।',
    },
    'id': {
        'lang': 'id',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'Konverter Gambar',
        'image_converter_desc': 'Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG.',
        'image_converter_desc_full': 'Ubah ukuran gambar dan konversi ke format WebP, JPEG, PNG. Proses langsung di browser Anda.',
        'upload_text': 'Klik atau seret gambar untuk mengunggah',
        'upload_info': 'Mendukung semua format gambar: JPG, PNG, GIF, WebP, dll.',
        'width': 'Lebar',
        'height': 'Tinggi',
        'output_format': 'Format Output',
        'quality': 'Kualitas',
        'convert': 'Konversi',
        'reset': 'Reset',
        'original_image': 'Gambar Asli',
        'converted_image': 'Gambar Terkonversi',
        'download': 'Unduh',
        'alert_image_only': 'Hanya file gambar yang dapat diunggah.',
    },
    'vi': {
        'lang': 'vi',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'Chuyển Đổi Hình Ảnh',
        'image_converter_desc': 'Thay đổi kích thước và chuyển đổi sang định dạng WebP, JPEG, PNG.',
        'image_converter_desc_full': 'Thay đổi kích thước và chuyển đổi sang định dạng WebP, JPEG, PNG. Xử lý trực tiếp trên trình duyệt.',
        'upload_text': 'Nhấp hoặc kéo hình ảnh để tải lên',
        'upload_info': 'Hỗ trợ tất cả định dạng hình ảnh: JPG, PNG, GIF, WebP, v.v.',
        'width': 'Chiều rộng',
        'height': 'Chiều cao',
        'output_format': 'Định dạng đầu ra',
        'quality': 'Chất lượng',
        'convert': 'Chuyển đổi',
        'reset': 'Đặt lại',
        'original_image': 'Hình ảnh gốc',
        'converted_image': 'Hình ảnh đã chuyển đổi',
        'download': 'Tải xuống',
        'alert_image_only': 'Chỉ có thể tải lên tệp hình ảnh.',
    },
    'th': {
        'lang': 'th',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'ตัวแปลงรูปภาพ',
        'image_converter_desc': 'ปรับขนาดและแปลงเป็นรูปแบบ WebP, JPEG, PNG',
        'image_converter_desc_full': 'ปรับขนาดและแปลงเป็นรูปแบบ WebP, JPEG, PNG ประมวลผลโดยตรงในเบราว์เซอร์',
        'upload_text': 'คลิกหรือลากรูปภาพเพื่ออัปโหลด',
        'upload_info': 'รองรับรูปแบบภาพทั้งหมด: JPG, PNG, GIF, WebP ฯลฯ',
        'width': 'ความกว้าง',
        'height': 'ความสูง',
        'output_format': 'รูปแบบเอาต์พุต',
        'quality': 'คุณภาพ',
        'convert': 'แปลง',
        'reset': 'รีเซ็ต',
        'original_image': 'รูปภาพต้นฉบับ',
        'converted_image': 'รูปภาพที่แปลงแล้ว',
        'download': 'ดาวน์โหลด',
        'alert_image_only': 'สามารถอัปโหลดไฟล์รูปภาพเท่านั้น',
    },
    'de': {
        'lang': 'de',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'Bildkonverter',
        'image_converter_desc': 'Bildgröße ändern und in WebP, JPEG, PNG konvertieren.',
        'image_converter_desc_full': 'Bildgröße ändern und in WebP, JPEG, PNG konvertieren. Direkt im Browser verarbeiten.',
        'upload_text': 'Klicken oder ziehen Sie ein Bild zum Hochladen',
        'upload_info': 'Unterstützt alle Bildformate: JPG, PNG, GIF, WebP usw.',
        'width': 'Breite',
        'height': 'Höhe',
        'output_format': 'Ausgabeformat',
        'quality': 'Qualität',
        'convert': 'Konvertieren',
        'reset': 'Zurücksetzen',
        'original_image': 'Originalbild',
        'converted_image': 'Konvertiertes Bild',
        'download': 'Herunterladen',
        'alert_image_only': 'Es können nur Bilddateien hochgeladen werden.',
    },
    'pt': {
        'lang': 'pt',
        'title_suffix': ' - Utilify',
        'image_converter_title': 'Conversor de Imagem',
        'image_converter_desc': 'Redimensione e converta para formatos WebP, JPEG, PNG.',
        'image_converter_desc_full': 'Redimensione e converta para formatos WebP, JPEG, PNG. Processe diretamente no navegador.',
        'upload_text': 'Clique ou arraste a imagem para fazer upload',
        'upload_info': 'Suporta todos os formatos de imagem: JPG, PNG, GIF, WebP, etc.',
        'width': 'Largura',
        'height': 'Altura',
        'output_format': 'Formato de Saída',
        'quality': 'Qualidade',
        'convert': 'Converter',
        'reset': 'Redefinir',
        'original_image': 'Imagem Original',
        'converted_image': 'Imagem Convertida',
        'download': 'Baixar',
        'alert_image_only': 'Apenas arquivos de imagem podem ser enviados.',
    },
}

def translate_html_file(source_path, target_path, lang_code):
    """HTML 파일을 번역합니다."""
    
    # 파일 읽기
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 번역 데이터 가져오기
    trans = TRANSLATIONS.get(lang_code)
    if not trans:
        print(f"⚠️  언어 코드 '{lang_code}'에 대한 번역이 없습니다.")
        return False
    
    # lang 속성 변경
    content = re.sub(r'<html lang="ko">', f'<html lang="{lang_code}">', content)
    
    # title 태그 번역
    content = re.sub(
        r'<title>이미지 변환기 - Utilify</title>',
        f'<title>{trans["image_converter_title"]} - Utilify</title>',
        content
    )
    
    # meta description 번역
    content = re.sub(
        r'<meta name="description" content="이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요\. 브라우저에서 바로 처리됩니다\.">',
        f'<meta name="description" content="{trans["image_converter_desc_full"]}">',
        content
    )
    
    # Open Graph 번역
    content = re.sub(
        r'<meta property="og:title" content="이미지 변환기 - Utilify">',
        f'<meta property="og:title" content="{trans["image_converter_title"]} - Utilify">',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content="이미지 크기를 조정하고 다양한 형식으로 변환하세요\.">',
        f'<meta property="og:description" content="{trans["image_converter_desc"]}">',
        content
    )
    
    # URL 변경
    content = re.sub(
        r'https://wwtrembling\.github\.io/ko/image-converter/',
        f'https://utilifyapp.net/{lang_code}/image-converter/',
        content
    )
    
    # Canonical URL 변경
    content = re.sub(
        r'<link rel="canonical" href="https://wwtrembling\.github\.io/ko/image-converter/">',
        f'<link rel="canonical" href="https://utilifyapp.net/{lang_code}/image-converter/">',
        content
    )
    
    # JSON-LD 번역
    content = re.sub(
        r'"name": "이미지 변환기"',
        f'"name": "{trans["image_converter_title"]}"',
        content
    )
    content = re.sub(
        r'"description": "이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요\."',
        f'"description": "{trans["image_converter_desc"]}"',
        content
    )
    content = re.sub(
        r'"inLanguage": "ko"',
        f'"inLanguage": "{lang_code}"',
        content
    )
    
    # 헤더 링크 변경
    content = re.sub(
        r'<a href="/ko/" class="site-logo">',
        f'<a href="/{lang_code}/" class="site-logo">',
        content
    )
    
    # 본문 텍스트 번역
    content = re.sub(
        r'<h1>🖼️ 이미지 변환기</h1>',
        f'<h1>🖼️ {trans["image_converter_title"]}</h1>',
        content
    )
    content = re.sub(
        r'<p>이미지 크기를 조정하고 WebP, JPEG, PNG 형식으로 변환하세요\.</p>',
        f'<p>{trans["image_converter_desc"]}</p>',
        content
    )
    
    # 업로드 영역 텍스트
    content = re.sub(
        r'<p style="font-size: 1\.25rem; font-weight: 600; margin: var\(--spacing-md\) 0;">이미지를 클릭하거나 드래그하여 업로드</p>',
        f'<p style="font-size: 1.25rem; font-weight: 600; margin: var(--spacing-md) 0;">{trans["upload_text"]}</p>',
        content
    )
    content = re.sub(
        r'<p class="info-text">JPG, PNG, GIF, WebP 등 모든 이미지 형식 지원</p>',
        f'<p class="info-text">{trans["upload_info"]}</p>',
        content
    )
    
    # 컨트롤 레이블 번역
    content = re.sub(
        r'<label class="form-label">너비 \(px\)</label>',
        f'<label class="form-label">{trans["width"]} (px)</label>',
        content
    )
    content = re.sub(
        r'<label class="form-label">높이 \(px\)</label>',
        f'<label class="form-label">{trans["height"]} (px)</label>',
        content
    )
    content = re.sub(
        r'<label class="form-label">출력 형식</label>',
        f'<label class="form-label">{trans["output_format"]}</label>',
        content
    )
    content = re.sub(
        r'<label class="form-label">품질 \(%\)</label>',
        f'<label class="form-label">{trans["quality"]} (%)</label>',
        content
    )
    
    # 버튼 텍스트 번역
    content = re.sub(
        r'<button class="btn btn-primary" id="convertBtn">변환하기</button>',
        f'<button class="btn btn-primary" id="convertBtn">{trans["convert"]}</button>',
        content
    )
    content = re.sub(
        r'<button class="btn btn-secondary" id="resetBtn">초기화</button>',
        f'<button class="btn btn-secondary" id="resetBtn">{trans["reset"]}</button>',
        content
    )
    
    # 프리뷰 제목 번역
    content = re.sub(
        r'<h3>원본 이미지</h3>',
        f'<h3>{trans["original_image"]}</h3>',
        content
    )
    content = re.sub(
        r'<h3>변환된 이미지</h3>',
        f'<h3>{trans["converted_image"]}</h3>',
        content
    )
    
    # 다운로드 버튼
    content = re.sub(
        r'style="margin-top: var\(--spacing-md\); width: 100%;">다운로드</button>',
        f'style="margin-top: var(--spacing-md); width: 100%;">{trans["download"]}</button>',
        content
    )
    
    # JavaScript alert 메시지
    content = re.sub(
        r"alert\('이미지 파일만 업로드할 수 있습니다\.'\);",
        f"alert('{trans['alert_image_only']}');",
        content
    )
    
    # 파일 저장
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """메인 함수"""
    base_dir = Path(__file__).parent
    source_file = base_dir / 'ko' / 'image-converter' / 'index.html'
    
    if not source_file.exists():
        print(f"❌ 원본 파일을 찾을 수 없습니다: {source_file}")
        return
    
    print("🚀 Utilify 다국어 번역 시작...\n")
    
    # 각 언어별로 번역
    success_count = 0
    fail_count = 0
    
    for lang_code in TRANSLATIONS.keys():
        target_file = base_dir / lang_code / 'image-converter' / 'index.html'
        print(f"📝 {lang_code.upper()} 번역 중: {target_file}")
        
        if translate_html_file(source_file, target_file, lang_code):
            print(f"   ✅ 완료!\n")
            success_count += 1
        else:
            print(f"   ❌ 실패!\n")
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 번역 완료!")
    print(f"   성공: {success_count}개")
    print(f"   실패: {fail_count}개")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

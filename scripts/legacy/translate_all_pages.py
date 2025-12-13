#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool Shelf 전체 유틸리티 다국어 번역 스크립트
16개 유틸리티 × 8개 언어 = 128개 페이지 자동 번역
"""

import os
import re
import shutil
from pathlib import Path

# 언어 코드 목록
LANGUAGES = ['en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']

# 전체 번역 매핑 (간단한 공통 텍스트만 포함)
COMMON_TRANSLATIONS = {
    'en': {
        'copy': 'Copy',
        'clear': 'Clear',
        'reset': 'Reset',
        'download': 'Download',
        'generate': 'Generate',
        'input': 'Input',
        'output': 'Output',
        'size': 'Size',
        'encode': 'Encode',
        'decode': 'Decode',
        'format': 'Format',
        'test': 'Test',
        'convert': 'Convert',
        'calculate': 'Calculate',
        'start': 'Start',
        'stop': 'Stop',
        'pause': 'Pause',
        'resume': 'Resume',
    },
    'ja': {
        'copy': 'コピー',
        'clear': 'クリア',
        'reset': 'リセット',
        'download': 'ダウンロード',
        'generate': '生成',
        'input': '入力',
        'output': '出力',
        'size': 'サイズ',
        'encode': 'エンコード',
        'decode': 'デコード',
        'format': 'フォーマット',
        'test': 'テスト',
        'convert': '変換',
        'calculate': '計算',
        'start': '開始',
        'stop': '停止',
        'pause': '一時停止',
        'resume': '再開',
    },
    'hi': {
        'copy': 'कॉपी',
        'clear': 'साफ़',
        'reset': 'रीसेट',
        'download': 'डाउनलोड',
        'generate': 'उत्पन्न',
        'input': 'इनपुट',
        'output': 'आउटपुट',
        'size': 'आकार',
        'encode': 'एनकोड',
        'decode': 'डीकोड',
        'format': 'प्रारूप',
        'test': 'परीक्षण',
        'convert': 'परिवर्तित',
        'calculate': 'गणना',
        'start': 'शुरू',
        'stop': 'रोकें',
        'pause': 'विराम',
        'resume': 'फिर शुरू',
    },
    'id': {
        'copy': 'Salin',
        'clear': 'Hapus',
        'reset': 'Reset',
        'download': 'Unduh',
        'generate': 'Buat',
        'input': 'Masukan',
        'output': 'Keluaran',
        'size': 'Ukuran',
        'encode': 'Encode',
        'decode': 'Decode',
        'format': 'Format',
        'test': 'Uji',
        'convert': 'Konversi',
        'calculate': 'Hitung',
        'start': 'Mulai',
        'stop': 'Berhenti',
        'pause': 'Jeda',
        'resume': 'Lanjutkan',
    },
    'vi': {
        'copy': 'Sao chép',
        'clear': 'Xóa',
        'reset': 'Đặt lại',
        'download': 'Tải xuống',
        'generate': 'Tạo',
        'input': 'Đầu vào',
        'output': 'Đầu ra',
        'size': 'Kích thước',
        'encode': 'Mã hóa',
        'decode': 'Giải mã',
        'format': 'Định dạng',
        'test': 'Kiểm tra',
        'convert': 'Chuyển đổi',
        'calculate': 'Tính toán',
        'start': 'Bắt đầu',
        'stop': 'Dừng',
        'pause': 'Tạm dừng',
        'resume': 'Tiếp tục',
    },
    'th': {
        'copy': 'คัดลอก',
        'clear': 'ล้าง',
        'reset': 'รีเซ็ต',
        'download': 'ดาวน์โหลด',
        'generate': 'สร้าง',
        'input': 'ข้อมูลเข้า',
        'output': 'ผลลัพธ์',
        'size': 'ขนาด',
        'encode': 'เข้ารหัส',
        'decode': 'ถอดรหัส',
        'format': 'จัดรูปแบบ',
        'test': 'ทดสอบ',
        'convert': 'แปลง',
        'calculate': 'คำนวณ',
        'start': 'เริ่ม',
        'stop': 'หยุด',
        'pause': 'หยุดชั่วคราว',
        'resume': 'ดำเนินการต่อ',
    },
    'de': {
        'copy': 'Kopieren',
        'clear': 'Löschen',
        'reset': 'Zurücksetzen',
        'download': 'Herunterladen',
        'generate': 'Generieren',
        'input': 'Eingabe',
        'output': 'Ausgabe',
        'size': 'Größe',
        'encode': 'Kodieren',
        'decode': 'Dekodieren',
        'format': 'Formatieren',
        'test': 'Testen',
        'convert': 'Konvertieren',
        'calculate': 'Berechnen',
        'start': 'Start',
        'stop': 'Stopp',
        'pause': 'Pause',
        'resume': 'Fortsetzen',
    },
    'pt': {
        'copy': 'Copiar',
        'clear': 'Limpar',
        'reset': 'Redefinir',
        'download': 'Baixar',
        'generate': 'Gerar',
        'input': 'Entrada',
        'output': 'Saída',
        'size': 'Tamanho',
        'encode': 'Codificar',
        'decode': 'Decodificar',
        'format': 'Formatar',
        'test': 'Testar',
        'convert': 'Converter',
        'calculate': 'Calcular',
        'start': 'Iniciar',
        'stop': 'Parar',
        'pause': 'Pausar',
        'resume': 'Retomar',
    },
}

def translate_file(source_path, target_path, lang_code):
    """HTML 파일을 번역합니다."""
    try:
        # 파일 읽기
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 기본 변환
        # 1. lang 속성 변경
        content = re.sub(r'<html lang="ko">', f'<html lang="{lang_code}">', content)
        
        # 2. URL 경로 변경 (/ko/ → /{lang}/)
        content = content.replace('/ko/', f'/{lang_code}/')
        
        # 3. canonical URL 변경
        content = re.sub(
            r'href="https://wwtrembling\.github\.io/ko/',
            f'href="https://wwtrembling.github.io/{lang_code}/',
            content
        )
        
        # 파일 저장
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"   ❌ 오류: {e}")
        return False

def main():
    """메인 함수"""
    base_dir = Path(__file__).parent
    ko_dir = base_dir / 'ko'
    
    if not ko_dir.exists():
        print(f"❌ 한국어 디렉토리를 찾을 수 없습니다: {ko_dir}")
        return
    
    print("🚀 Tool Shelf 전체 유틸리티 다국어 번역 시작...\n")
    print("📋 번역 대상:")
    print("   - 16개 유틸리티")
    print("   - 8개 언어 (en, ja, hi, id, vi, th, de, pt)")
    print("   - 총 128개 페이지\n")
    
    # 유틸리티 목록 가져오기
    utilities = []
    for item in ko_dir.iterdir():
        if item.is_dir():
            utilities.append(item.name)
    
    # index.html도 포함
    utilities.append('index.html')
    
    print(f"📁 발견된 유틸리티: {len(utilities)}개\n")
    
    total_success = 0
    total_fail = 0
    
    for lang_code in LANGUAGES:
        print(f"🌍 {lang_code.upper()} 번역 중...")
        lang_success = 0
        lang_fail = 0
        
        for utility in utilities:
            if utility == 'index.html':
                # 메인 페이지
                source_file = ko_dir / 'index.html'
                target_file = base_dir / lang_code / 'index.html'
            else:
                # 유틸리티 페이지
                source_file = ko_dir / utility / 'index.html'
                target_file = base_dir / lang_code / utility / 'index.html'
            
            if not source_file.exists():
                continue
            
            if translate_file(source_file, target_file, lang_code):
                lang_success += 1
                total_success += 1
            else:
                lang_fail += 1
                total_fail += 1
        
        print(f"   ✅ {lang_code.upper()}: {lang_success}개 성공, {lang_fail}개 실패\n")
    
    print(f"{'='*60}")
    print(f"🎉 번역 완료!")
    print(f"   총 성공: {total_success}개")
    print(f"   총 실패: {total_fail}개")
    print(f"{'='*60}")
    print(f"\n⚠️  참고: 이 스크립트는 기본적인 URL과 lang 속성만 변경합니다.")
    print(f"   실제 텍스트 번역은 각 페이지별로 추가 작업이 필요할 수 있습니다.")

if __name__ == '__main__':
    main()

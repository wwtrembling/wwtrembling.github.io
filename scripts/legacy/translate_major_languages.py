#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilify 주요 언어 완전 번역 스크립트 (병렬 처리)
영어, 일본어를 우선 번역하고 병렬로 처리하여 속도 향상
"""

import os
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 번역 매핑 - 영어와 일본어만 포함
TRANSLATIONS = {
    'en': {
        # 공통
        'copy': 'Copy',
        'clear': 'Clear',
        'reset': 'Reset',
        'download': 'Download',
        'generate': 'Generate',
        'input': 'Input',
        'output': 'Output',
        'result': 'Result',
        
        # Base64 Converter
        'base64_title': 'Base64 Encoder/Decoder',
        'base64_desc': 'Encode or decode text to Base64.',
        'input_text': 'Input Text',
        'output_result': 'Output Result',
        'encode': 'Encode',
        'decode': 'Decode',
        'encode_placeholder': 'Enter text to encode',
        'encoding_error': 'Encoding error: ',
        'decoding_error': 'Decoding error: ',
        'no_content_to_copy': 'No content to copy.',
        
        # QR Generator
        'qr_title': 'QR Code Generator',
        'qr_desc': 'Convert text or URL to QR code.',
        'text_or_url': 'Text or URL',
        'size': 'Size',
        'enter_text': 'Please enter text.',
        'generate_first': 'Please generate QR code first.',
        
        # JSON Formatter
        'json_title': 'JSON Formatter',
        'json_desc': 'Format and validate JSON data. Provides compression, formatting, and validation features.',
        'json_input': 'JSON Input',
        'format': 'Format',
        'minify': 'Minify',
        'validate': 'Validate',
        'json_placeholder': 'Enter JSON data...',
        'valid_json': '✓ Valid JSON',
        'invalid_json': '✗ Invalid JSON',
        'error': 'Error: ',
        
        # Text Utils
        'text_utils_title': 'Text Utilities',
        'text_utils_desc': 'Word count, character count, duplicate removal, case conversion and various text processing features.',
        'text_input': 'Text Input',
        'text_placeholder': 'Enter text...',
        'statistics': 'Statistics',
        'char_count': 'Characters',
        'word_count': 'Words',
        'line_count': 'Lines',
        'actions': 'Actions',
        'to_uppercase': 'To Uppercase',
        'to_lowercase': 'To Lowercase',
        'remove_duplicates': 'Remove Duplicate Lines',
        'sort_lines': 'Sort Lines',
        'reverse_text': 'Reverse Text',
        
        # Color Converter
        'color_title': 'Color Converter',
        'color_desc': 'Convert between HEX, RGB, and HSL color formats. Real-time color preview and easy copy function.',
        'color_formats': 'Color Formats',
        'rgb_sliders': 'RGB Sliders',
        'popular_colors': 'Popular Colors',
        'red': 'Red',
        'green': 'Green',
        'blue': 'Blue',
        
        # SQL Formatter
        'sql_title': 'SQL Formatter',
        'sql_desc': 'Format SQL queries for better readability.',
        
        # Regex Tester
        'regex_title': 'Regex Tester',
        'regex_desc': 'Test regular expressions in real-time.',
        'pattern': 'Pattern',
        'test_string': 'Test String',
        'matches': 'Matches',
    },
    'ja': {
        # 공통
        'copy': 'コピー',
        'clear': 'クリア',
        'reset': 'リセット',
        'download': 'ダウンロード',
        'generate': '生成',
        'input': '入力',
        'output': '出力',
        'result': '結果',
        
        # Base64 Converter
        'base64_title': 'Base64エンコーダー/デコーダー',
        'base64_desc': 'テキストをBase64にエンコードまたはデコードします。',
        'input_text': '入力テキスト',
        'output_result': '出力結果',
        'encode': 'エンコード',
        'decode': 'デコード',
        'encode_placeholder': 'エンコードするテキストを入力',
        'encoding_error': 'エンコードエラー: ',
        'decoding_error': 'デコードエラー: ',
        'no_content_to_copy': 'コピーする内容がありません。',
        
        # QR Generator
        'qr_title': 'QRコード生成器',
        'qr_desc': 'テキストまたはURLをQRコードに変換します。',
        'text_or_url': 'テキストまたはURL',
        'size': 'サイズ',
        'enter_text': 'テキストを入力してください。',
        'generate_first': '先にQRコードを生成してください。',
        
        # JSON Formatter
        'json_title': 'JSONフォーマッター',
        'json_desc': 'JSONデータをフォーマットして検証します。圧縮、フォーマット、検証機能を提供します。',
        'json_input': 'JSON入力',
        'format': 'フォーマット',
        'minify': '圧縮',
        'validate': '検証',
        'json_placeholder': 'JSONデータを入力...',
        'valid_json': '✓ 有効なJSON',
        'invalid_json': '✗ 無効なJSON',
        'error': 'エラー: ',
        
        # Text Utils
        'text_utils_title': 'テキストユーティリティ',
        'text_utils_desc': '単語数カウント、文字数カウント、重複削除、大文字小文字変換など、さまざまなテキスト処理機能を提供します。',
        'text_input': 'テキスト入力',
        'text_placeholder': 'テキストを入力...',
        'statistics': '統計',
        'char_count': '文字数',
        'word_count': '単語数',
        'line_count': '行数',
        'actions': 'アクション',
        'to_uppercase': '大文字に',
        'to_lowercase': '小文字に',
        'remove_duplicates': '重複行を削除',
        'sort_lines': '行を並べ替え',
        'reverse_text': 'テキストを反転',
        
        # Color Converter
        'color_title': '色変換器',
        'color_desc': 'HEX、RGB、HSL色形式間の変換を実行します。リアルタイム色プレビューと簡単なコピー機能。',
        'color_formats': '色形式',
        'rgb_sliders': 'RGBスライダー',
        'popular_colors': '人気の色',
        'red': '赤',
        'green': '緑',
        'blue': '青',
        
        # SQL Formatter
        'sql_title': 'SQLフォーマッター',
        'sql_desc': 'SQLクエリを読みやすくフォーマットします。',
        
        # Regex Tester
        'regex_title': '正規表現テスター',
        'regex_desc': '正規表現をリアルタイムでテストします。',
        'pattern': 'パターン',
        'test_string': 'テスト文字列',
        'matches': 'マッチ',
    }
}

def translate_utility(source_path, target_path, lang_code, utility_name):
    """유틸리티 페이지를 번역합니다."""
    try:
        # 파일 읽기
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        trans = TRANSLATIONS[lang_code]
        
        # 기본 변환
        content = re.sub(r'<html lang="ko">', f'<html lang="{lang_code}">', content)
        content = content.replace('/ko/', f'/{lang_code}/')
        
        # 유틸리티별 번역
        if utility_name == 'base64-converter':
            content = re.sub(r'<title>Base64 인코더/디코더 - Utilify</title>',
                           f'<title>{trans["base64_title"]} - Utilify</title>', content)
            content = re.sub(r'content="텍스트를 Base64로 인코딩하거나 디코딩하세요\."',
                           f'content="{trans["base64_desc"]}"', content)
            content = re.sub(r'<h1>🔐 Base64 인코더/디코더</h1>',
                           f'<h1>🔐 {trans["base64_title"]}</h1>', content)
            content = re.sub(r'<p>텍스트를 Base64로 인코딩하거나 디코딩하세요\.</p>',
                           f'<p>{trans["base64_desc"]}</p>', content)
            content = re.sub(r'<label class="form-label">입력 텍스트</label>',
                           f'<label class="form-label">{trans["input_text"]}</label>', content)
            content = re.sub(r'<label class="form-label">출력 결과</label>',
                           f'<label class="form-label">{trans["output_result"]}</label>', content)
            content = re.sub(r'placeholder="인코딩할 텍스트를 입력하세요"',
                           f'placeholder="{trans["encode_placeholder"]}"', content)
            content = re.sub(r'>⬇️ Encode<', f'>{trans["encode"]}<', content)
            content = re.sub(r'>⬆️ Decode<', f'>{trans["decode"]}<', content)
            content = re.sub(r'>📋 복사<', f'>{trans["copy"]}<', content)
            content = re.sub(r'>🗑️ 초기화<', f'>{trans["clear"]}<', content)
            content = re.sub(r"'인코딩 오류: '", f"'{trans['encoding_error']}'", content)
            content = re.sub(r"'디코딩 오류: '", f"'{trans['decoding_error']}'", content)
            content = re.sub(r"'복사할 내용이 없습니다\.'", f"'{trans['no_content_to_copy']}'", content)
            
        elif utility_name == 'qr-generator':
            content = re.sub(r'<title>QR 코드 생성기 - Utilify</title>',
                           f'<title>{trans["qr_title"]} - Utilify</title>', content)
            content = re.sub(r'content="텍스트나 URL을 QR 코드로 변환하세요\."',
                           f'content="{trans["qr_desc"]}"', content)
            content = re.sub(r'<h1>📱 QR 코드 생성기</h1>',
                           f'<h1>📱 {trans["qr_title"]}</h1>', content)
            content = re.sub(r'<p>텍스트나 URL을 QR 코드로 변환하세요\.</p>',
                           f'<p>{trans["qr_desc"]}</p>', content)
            content = re.sub(r'<label class="form-label">텍스트 또는 URL</label>',
                           f'<label class="form-label">{trans["text_or_url"]}</label>', content)
            content = re.sub(r'<label class="form-label">크기</label>',
                           f'<label class="form-label">{trans["size"]}</label>', content)
            content = re.sub(r'>생성<', f'>{trans["generate"]}<', content)
            content = re.sub(r'>다운로드<', f'>{trans["download"]}<', content)
            content = re.sub(r"'텍스트를 입력하세요\.'", f"'{trans['enter_text']}'", content)
            content = re.sub(r"'먼저 QR 코드를 생성하세요\.'", f"'{trans['generate_first']}'", content)
            
        elif utility_name == 'json-formatter':
            content = re.sub(r'<title>JSON 포매터 - Utilify</title>',
                           f'<title>{trans["json_title"]} - Utilify</title>', content)
            content = re.sub(r'content="JSON 데이터를 포맷팅하고 유효성을 검사하세요\. 압축, 포맷, 검증 기능을 제공합니다\."',
                           f'content="{trans["json_desc"]}"', content)
            content = re.sub(r'<h1>{{ }} JSON 포매터</h1>',
                           f'<h1>{{ }} {trans["json_title"]}</h1>', content)
            content = re.sub(r'<p>JSON 데이터를 포맷팅하고 유효성을 검사하세요\. 압축, 포맷, 검증 기능을 제공합니다\.</p>',
                           f'<p>{trans["json_desc"]}</p>', content)
            content = re.sub(r'<label class="form-label">JSON 입력</label>',
                           f'<label class="form-label">{trans["json_input"]}</label>', content)
            content = re.sub(r'<label class="form-label">결과</label>',
                           f'<label class="form-label">{trans["result"]}</label>', content)
            content = re.sub(r'placeholder="JSON 데이터를 입력하세요\.\.\."',
                           f'placeholder="{trans["json_placeholder"]}"', content)
            content = re.sub(r'>포맷<', f'>{trans["format"]}<', content)
            content = re.sub(r'>압축<', f'>{trans["minify"]}<', content)
            content = re.sub(r'>검증<', f'>{trans["validate"]}<', content)
            content = re.sub(r'>복사<', f'>{trans["copy"]}<', content)
            content = re.sub(r'>지우기<', f'>{trans["clear"]}<', content)
            content = re.sub(r"'✓ 유효한 JSON입니다'", f"'{trans['valid_json']}'", content)
            content = re.sub(r"'✗ 유효하지 않은 JSON입니다'", f"'{trans['invalid_json']}'", content)
            content = re.sub(r"'오류: '", f"'{trans['error']}'", content)
            
        elif utility_name == 'text-utils':
            content = re.sub(r'<title>텍스트 유틸리티 - Utilify</title>',
                           f'<title>{trans["text_utils_title"]} - Utilify</title>', content)
            content = re.sub(r'content="단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다\."',
                           f'content="{trans["text_utils_desc"]}"', content)
            content = re.sub(r'<h1>📝 텍스트 유틸리티</h1>',
                           f'<h1>📝 {trans["text_utils_title"]}</h1>', content)
            content = re.sub(r'<p>단어 수 세기, 문자 수 세기, 중복 제거, 대소문자 변환 등 다양한 텍스트 처리 기능을 제공합니다\.</p>',
                           f'<p>{trans["text_utils_desc"]}</p>', content)
            content = re.sub(r'<label class="form-label">텍스트 입력</label>',
                           f'<label class="form-label">{trans["text_input"]}</label>', content)
            content = re.sub(r'placeholder="텍스트를 입력하세요\.\.\."',
                           f'placeholder="{trans["text_placeholder"]}"', content)
            content = re.sub(r'<h3>통계</h3>', f'<h3>{trans["statistics"]}</h3>', content)
            content = re.sub(r'<div>문자 수</div>', f'<div>{trans["char_count"]}</div>', content)
            content = re.sub(r'<div>단어 수</div>', f'<div>{trans["word_count"]}</div>', content)
            content = re.sub(r'<div>줄 수</div>', f'<div>{trans["line_count"]}</div>', content)
            content = re.sub(r'<h3>작업</h3>', f'<h3>{trans["actions"]}</h3>', content)
            content = re.sub(r'>대문자로<', f'>{trans["to_uppercase"]}<', content)
            content = re.sub(r'>소문자로<', f'>{trans["to_lowercase"]}<', content)
            content = re.sub(r'>중복 줄 제거<', f'>{trans["remove_duplicates"]}<', content)
            content = re.sub(r'>줄 정렬<', f'>{trans["sort_lines"]}<', content)
            content = re.sub(r'>텍스트 뒤집기<', f'>{trans["reverse_text"]}<', content)
            content = re.sub(r'>복사<', f'>{trans["copy"]}<', content)
            content = re.sub(r'>지우기<', f'>{trans["clear"]}<', content)
            
        elif utility_name == 'color-converter':
            content = re.sub(r'<title>색상 변환기 - Utilify</title>',
                           f'<title>{trans["color_title"]} - Utilify</title>', content)
            content = re.sub(r'content="HEX, RGB, HSL 색상 형식 간 변환을 수행하세요\. 실시간 색상 미리보기와 간편한 복사 기능\."',
                           f'content="{trans["color_desc"]}"', content)
            content = re.sub(r'<h1>🎨 색상 변환기</h1>',
                           f'<h1>🎨 {trans["color_title"]}</h1>', content)
            content = re.sub(r'<p>HEX, RGB, HSL 색상 형식 간 변환을 수행하세요\. 실시간 색상 미리보기와 간편한 복사 기능\.</p>',
                           f'<p>{trans["color_desc"]}</p>', content)
            content = re.sub(r'<h3>색상 형식</h3>', f'<h3>{trans["color_formats"]}</h3>', content)
            content = re.sub(r'<h3>RGB 슬라이더</h3>', f'<h3>{trans["rgb_sliders"]}</h3>', content)
            content = re.sub(r'<h3>인기 색상</h3>', f'<h3>{trans["popular_colors"]}</h3>', content)
            content = re.sub(r'<span>빨강</span>', f'<span>{trans["red"]}</span>', content)
            content = re.sub(r'<span>초록</span>', f'<span>{trans["green"]}</span>', content)
            content = re.sub(r'<span>파랑</span>', f'<span>{trans["blue"]}</span>', content)
            content = re.sub(r'>복사<', f'>{trans["copy"]}<', content)
        
        # 파일 저장
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, utility_name, lang_code
    except Exception as e:
        return False, utility_name, lang_code, str(e)

def main():
    """메인 함수 - 병렬 처리"""
    base_dir = Path(__file__).parent
    ko_dir = base_dir / 'ko'
    
    print("🚀 Utilify 주요 언어 완전 번역 시작 (병렬 처리)...\n")
    
    # 번역할 유틸리티 목록
    utilities = [
        'base64-converter',
        'qr-generator',
        'json-formatter',
        'text-utils',
        'color-converter',
    ]
    
    languages = ['en', 'ja']
    
    print(f"📋 번역 대상:")
    print(f"   - {len(utilities)}개 유틸리티")
    print(f"   - {len(languages)}개 언어 (영어, 일본어)")
    print(f"   - 총 {len(utilities) * len(languages)}개 페이지\n")
    
    # 병렬 처리를 위한 작업 목록
    tasks = []
    for lang in languages:
        for utility in utilities:
            source_file = ko_dir / utility / 'index.html'
            target_file = base_dir / lang / utility / 'index.html'
            if source_file.exists():
                tasks.append((source_file, target_file, lang, utility))
    
    # 병렬 처리 실행
    start_time = time.time()
    success_count = 0
    fail_count = 0
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        # 모든 작업 제출
        future_to_task = {
            executor.submit(translate_utility, *task): task 
            for task in tasks
        }
        
        # 완료된 작업 처리
        for future in as_completed(future_to_task):
            result = future.result()
            if result[0]:  # 성공
                success_count += 1
                utility, lang = result[1], result[2]
                print(f"✅ {lang.upper()}/{utility}")
            else:  # 실패
                fail_count += 1
                utility, lang, error = result[1], result[2], result[3]
                print(f"❌ {lang.upper()}/{utility}: {error}")
    
    elapsed_time = time.time() - start_time
    
    print(f"\n{'='*60}")
    print(f"🎉 번역 완료!")
    print(f"   성공: {success_count}개")
    print(f"   실패: {fail_count}개")
    print(f"   소요 시간: {elapsed_time:.2f}초")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

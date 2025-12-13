#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool Shelf Final Fix Translation Script
Corrects specific translation misses due to Regex mismatches.
"""

import os
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ------------------------------------------------------------------------------
# TRANSLATION MAPPINGS
# ------------------------------------------------------------------------------
TRANSLATIONS = {
    'en': {
        # JSON
        'json_label_in': 'Input JSON',
        'json_fmt': 'Format',
        'json_min': 'Minify',
        'json_valid': 'Validate',
        'json_copy': 'Copy',
        'json_clear': 'Clear',
        'json_desc_full': 'Format and validate JSON data. Features include minification, formatting, and validation.',
        
        # Text
        'text_label_in': 'Input Text',
        'text_upper': 'UPPERCASE',
        'text_lower': 'lowercase',
        'text_dedup': 'Remove Duplicate Lines',
        'text_sort': 'Sort Lines',
        'text_reverse': 'Reverse Text',
        'text_copy': 'Copy',
        'text_clear': 'Clear',
        'text_char': 'Characters',
        'text_word': 'Words',
        'text_line': 'Lines',

        # Lorem
        'lorem_type': 'Type:',
        'lorem_count': 'Count:',
        'lorem_para': 'Paragraphs',
        'lorem_word': 'Words',
        'lorem_sent': 'Sentences',
        'lorem_gen': 'Generate',
        'lorem_copy': 'Copy',
        
        # QR
        'qr_gen': 'Generate',
        'qr_download': 'Download',
        'qr_size': 'Size',
        
        # Base64
        'b64_encode': 'Encode',
        'b64_decode': 'Decode',
        'b64_copy': 'Copy',
        'b64_clear': 'Clear',
        
        # Color
        'col_hex': 'HEX Color',
        'col_rgb': 'RGB Color',
        'col_hsl': 'HSL Color',
        'col_copy': 'Copy',
    },
    'ja': {
        'json_label_in': '入力JSON',
        'json_fmt': '整形',
        'json_min': '圧縮',
        'json_valid': '検証',
        'json_copy': 'コピー',
        'json_clear': 'クリア',
        'json_desc_full': 'JSONデータの整形と検証を行います。圧縮、整形、検証機能を提供します。',
        
        'text_label_in': '入力テキスト',
        'text_upper': '大文字',
        'text_lower': '小文字',
        'text_dedup': '重複行削除',
        'text_sort': '行の並べ替え',
        'text_reverse': 'テキスト反転',
        'text_copy': 'コピー',
        'text_clear': 'クリア',
        'text_char': '文字数',
        'text_word': '単語数',
        'text_line': '行数',

        'lorem_type': 'タイプ:',
        'lorem_count': '数:',
        'lorem_para': '段落',
        'lorem_word': '単語',
        'lorem_sent': '文章',
        'lorem_gen': '生成',
        'lorem_copy': 'コピー',
        
        'qr_gen': '生成',
        'qr_download': 'ダウンロード',
        'qr_size': 'サイズ',
        
        'b64_encode': 'エンコード',
        'b64_decode': 'デコード',
        'b64_copy': 'コピー',
        'b64_clear': 'クリア',
        
        'col_hex': 'HEXカラー',
        'col_rgb': 'RGBカラー',
        'col_hsl': 'HSLカラー',
        'col_copy': 'コピー',
    },
    'hi': {
        'json_label_in': 'JSON इनपुट',
        'json_fmt': 'प्रारूप',
        'json_min': 'छोटा करें',
        'json_valid': 'मान्य करें',
        'json_copy': 'कॉपी',
        'json_clear': 'साफ़ करें',
        'text_label_in': 'पाठ इनपुट',
        'text_upper': 'बड़े अक्षर',
        'text_lower': 'छोटे अक्षर',
        'text_dedup': 'डुप्लिकेट हटाएँ',
        'text_sort': 'क्रमबद्ध करें',
        'text_reverse': 'उल्टा करें',
        'text_copy': 'कॉपी',
        'text_clear': 'साफ़ करें',
        'lorem_gen': 'उत्पन्न करें',
        'qr_gen': 'उत्पन्न करें',
        'b64_encode': 'एनकोड',
        'b64_decode': 'डिकोड',
    }
}

# Fill defaults
for lang in ['hi', 'de', 'pt', 'vi', 'th', 'id']:
    for key, val in TRANSLATIONS['en'].items():
        if key not in TRANSLATIONS.get(lang, {}):
            if lang not in TRANSLATIONS: TRANSLATIONS[lang] = {}
            TRANSLATIONS[lang][key] = val

def fix_file(file_path, lang_code, utility):
    try:
        if not file_path.exists(): return False, utility, "File not found"
        
        trans = TRANSLATIONS.get(lang_code, TRANSLATIONS['en'])
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # ----------------------------------------------------------------------
        # FIXES BASED ON EXACT KOREAN STRINGS
        # ----------------------------------------------------------------------
        
        if utility == 'json-formatter':
            content = re.sub(r'JSON 데이터를 포맷팅하고 유효성을 검사하세요\. 압축, 포맷, 검증 기능을 제공합니다\.', trans.get('json_desc_full', ''), content)
            content = re.sub(r'<label class="form-label">JSON 입력</label>', f'<label class="form-label">{trans["json_label_in"]}</label>', content)
            content = re.sub(r'>포맷<', f'>{trans["json_fmt"]}<', content)
            content = re.sub(r'>압축<', f'>{trans["json_min"]}<', content)
            content = re.sub(r'>검증<', f'>{trans["json_valid"]}<', content)
            content = re.sub(r'>복사<', f'>{trans["json_copy"]}<', content)
            content = re.sub(r'>지우기<', f'>{trans["json_clear"]}<', content)

        elif utility == 'text-utils':
            content = re.sub(r'<label class="form-label">텍스트 입력</label>', f'<label class="form-label">{trans["text_label_in"]}</label>', content)
            content = re.sub(r'>대문자로<', f'>{trans["text_upper"]}<', content)
            content = re.sub(r'>소문자로<', f'>{trans["text_lower"]}<', content)
            content = re.sub(r'>중복 줄 제거<', f'>{trans["text_dedup"]}<', content)
            content = re.sub(r'>줄 정렬<', f'>{trans["text_sort"]}<', content)
            content = re.sub(r'>텍스트 뒤집기<', f'>{trans["text_reverse"]}<', content)
            content = re.sub(r'>복사<', f'>{trans["text_copy"]}<', content)
            content = re.sub(r'>지우기<', f'>{trans["text_clear"]}<', content)
            content = re.sub(r'>문자 수</div>', f'>{trans["text_char"]}</div>', content)
            content = re.sub(r'>단어 수</div>', f'>{trans["text_word"]}</div>', content)
            content = re.sub(r'>줄 수</div>', f'>{trans["text_line"]}</div>', content)

        elif utility == 'lorem-ipsum':
            content = re.sub(r'<label class="form-label">타입:</label>', f'<label class="form-label">{trans["lorem_type"]}</label>', content)
            content = re.sub(r'<label class="form-label">개수:</label>', f'<label class="form-label">{trans["lorem_count"]}</label>', content)
            content = re.sub(r'>단락<', f'>{trans["lorem_para"]}<', content)
            content = re.sub(r'>단어<', f'>{trans["lorem_word"]}<', content)
            content = re.sub(r'>문장<', f'>{trans["lorem_sent"]}<', content)
            content = re.sub(r'>생성<', f'>{trans["lorem_gen"]}<', content)
            content = re.sub(r'>복사<', f'>{trans["lorem_copy"]}<', content)
            
        elif utility == 'qr-generator':
             content = re.sub(r'>생성<', f'>{trans["qr_gen"]}<', content)
             content = re.sub(r'>다운로드<', f'>{trans["qr_download"]}<', content)
             content = re.sub(r'<label class="form-label">크기</label>', f'<label class="form-label">{trans["qr_size"]}</label>', content)

        elif utility == 'base64-converter':
             content = re.sub(r'>복사<', f'>{trans["b64_copy"]}<', content)
             content = re.sub(r'>초기화<', f'>{trans["b64_clear"]}<', content)
             
        elif utility == 'color-converter':
             content = re.sub(r'>복사<', f'>{trans["col_copy"]}<', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True, utility, lang_code

    except Exception as e:
        return False, utility, str(e)

def main():
    base_dir = Path(__file__).parent
    
    tasks = []
    languages = ['en', 'ja', 'hi', 'de', 'pt', 'vi', 'th', 'id']
    utilities = {
        'json-formatter': 'json-formatter',
        'text-utils': 'text-utils',
        'lorem-ipsum': 'lorem-ipsum',
        'qr-generator': 'qr-generator',
        'base64-converter': 'base64-converter',
        'color-converter': 'color-converter',
    }
    
    print("🔧 Fixing specific translation misses...")
    
    for lang in languages:
        for util in utilities:
            # We target the ALREADY TRANSLATED (but broken) files in lang dirs
            # BUT wait, if I used 'ko' text for regex, I must ensure the FILE STILL HAS KO TEXT.
            # My previous scripts copied the file from KO (if missing) or modified it.
            # If `translate_final_batch` FAILED to replace, the KO text is still there!
            # So this logic holds.
            target = base_dir / lang / util / 'index.html'
            tasks.append((target, lang, util))

    success = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(fix_file, *task) for task in tasks]
        for future in as_completed(futures):
            res = future.result()
            if res[0]: success += 1
            
    print(f"Done. Fixed {success} files.")

if __name__ == '__main__':
    main()

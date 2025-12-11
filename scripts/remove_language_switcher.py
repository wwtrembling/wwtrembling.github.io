import os
import re

# 루트 디렉토리
root_dir = r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf'

# 루트 index.html 경로
root_index = os.path.join(root_dir, 'index.html')

# 모든 index.html 파일 찾기
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == 'index.html':
            file_path = os.path.join(dirpath, filename)
            
            # 루트 index.html은 제외
            if os.path.abspath(file_path) == os.path.abspath(root_index):
                print(f"[SKIP] {file_path}")
                continue
            
            # 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # id="languageSwitcher"가 포함된 라인 제거
            original_lines = content.split('\n')
            modified_lines = []
            removed_count = 0
            
            for line in original_lines:
                if 'id="languageSwitcher"' in line:
                    removed_count += 1
                    continue
                modified_lines.append(line)
            
            if removed_count > 0:
                # 파일 쓰기
                new_content = '\n'.join(modified_lines)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"[MODIFIED] {file_path} - Removed {removed_count} line(s)")
            else:
                print(f"[NO CHANGE] {file_path}")

print("\n✅ 작업 완료!")

import os
from pathlib import Path

def main():
    base_dir = Path(r'c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf')
    target_langs = ['en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']
    
    # The HTML chunk to inject (in Korean)
    # This must match PRECISELY what I put in MASTER_MAP keys
    card_html = """
        <a href="/ko/jpa-converter/" class="card">
          <div class="card-icon">🏛️</div>
          <h3 class="card-title">DB to JPA 변환기</h3>
          <p class="card-description">SQL 스키마를 JPA Entity, DTO 클래스로 자동 변환합니다.</p>
        </a>
        <a href="/ko/json-to-ts/" class="card">
          <div class="card-icon">📜</div>
          <h3 class="card-title">JSON to TS/DTO</h3>
          <p class="card-description">JSON을 TypeScript Interface 및 NestJS DTO로 변환합니다.</p>
        </a>
        <a href="/ko/excel-to-sql/" class="card">
          <div class="card-icon">📊</div>
          <h3 class="card-title">Excel to SQL</h3>
          <p class="card-description">엑셀 데이터를 SQL INSERT 쿼리로 변환하는 도구.</p>
        </a>
"""
    
    for lang in target_langs:
        index_path = base_dir / lang / 'index.html'
        if not index_path.exists():
            print(f"Skipping {lang} (no index.html)")
            continue
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if already injected (simple check)
        if 'jpa-converter' in content:
            print(f"Skipping {lang} (already has links)")
            continue
            
        # Find insertion point (end of last card or start of closing div)
        # We look for the closing </div> of .card-grid
        # Usually it's indentation + </div>
        # Let's try to insert before the last </div> that closes .card-grid
        # Assuming structure: <div class="card-grid"> ... </div>
        
        # A safer way might be to key off the known last card "reaction-test"
        if 'reaction-test' in content:
            # Replace the reaction-test card closing tag with itself + new content
            # But the language version of reaction-test might have different text?
            # The HREF should be consistent: href="/ko/reaction-test/" (or /en/reaction-test/)
            # Wait, the hrefs in `card_html` above are hardcoded to `/ko/`.
            # I must dynamically change the HREF language code.
            
            lang_card_html = card_html.replace('/ko/', f'/{lang}/')
            
            # Simple replace: find "reaction-test/" ... </a>"
            # Regex to find the END of the reaction-test card
            import re
            # Matches <a href="/lang/reaction-test/" ... </a>
            # We want to append AFTER this block.
            
            # Since regex for HTML is fragile, let's look for the specific strings I know exist
            # "reaction-test" is reliable.
            # I will inject before the </div> that closes card-grid.
            # Assuming "</div>\n    </div>\n  </main>" or something at the end.
            
            # Let's just append before `      </div>\n    </div>\n  </main>`
            if '      </div>\n    </div>\n  </main>' in content:
                 new_content = content.replace('      </div>\n    </div>\n  </main>', lang_card_html + '      </div>\n    </div>\n  </main>')
                 with open(index_path, 'w', encoding='utf-8') as f:
                     f.write(new_content)
                 print(f"✅ Injected into {lang}")
            else:
                # Fallback: try to find the last </a> and append after it
                last_a_idx = content.rfind('</a>')
                if last_a_idx != -1:
                     new_content = content[:last_a_idx+4] + lang_card_html + content[last_a_idx+4:]
                     with open(index_path, 'w', encoding='utf-8') as f:
                         f.write(new_content)
                     print(f"⚠️ Fallback Injected into {lang}")
                else:
                     print(f"❌ Could not find insertion point in {lang}")

if __name__ == '__main__':
    main()

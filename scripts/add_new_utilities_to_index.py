"""
Inject new utilities into index.html for all languages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

LANGUAGES = ['ko', 'en', 'ja', 'hi', 'id', 'vi', 'th', 'de', 'pt']

NEW_TOOLS = [
    {
        'slug': 'diff-checker',
        'icon': '🔀',
        'trans': {
            'ko': {'title': '텍스트 비교기', 'desc': '두 텍스트의 차이점을 쉽고 빠르게 비교하세요.'},
            'en': {'title': 'Text Diff Checker', 'desc': 'Compare two texts difference easily.'},
            'ja': {'title': 'テキスト比較ツール', 'desc': '2つのテキストの違いを簡単に比較します。'},
            'hi': {'title': 'टेक्स्ट अंतर चेकर', 'desc': 'दो टेक्स्ट के बीच अंतर की आसानी से तुलना करें।'},
            'id': {'title': 'Pemeriksa Perbedaan Teks', 'desc': 'Bandingkan perbedaan dua teks dengan mudah.'},
            'vi': {'title': 'Kiểm Tra Khác Biệt Văn Bản', 'desc': 'So sánh sự khác biệt giữa hai văn bản dễ dàng.'},
            'th': {'title': 'เครื่องมือเปรียบเทียบข้อความ', 'desc': 'เปรียบเทียบความแตกต่างของข้อความสองชุดอย่างง่ายดาย'},
            'de': {'title': 'Text-Vergleich', 'desc': 'Vergleichen Sie zwei Texte einfach.'},
            'pt': {'title': 'Comparador de Texto', 'desc': 'Compare a diferença entre dois textos facilmente.'}
        }
    },
    {
        'slug': 'password-generator',
        'icon': '🔐',
        'trans': {
            'ko': {'title': '안전한 비밀번호 생성기', 'desc': '강력하고 안전한 비밀번호를 생성하세요.'},
            'en': {'title': 'Strong Password Generator', 'desc': 'Generate strong and secure passwords.'},
            'ja': {'title': '強力なパスワード生成ツール', 'desc': '強力で安全なパスワードを生成します。'},
            'hi': {'title': 'मजबूत पासवर्ड जनरेटर', 'desc': 'मजबूत और सुरक्षित पासवर्ड बनाएं।'},
            'id': {'title': 'Pembuat Kata Sandi Kuat', 'desc': 'Buat kata sandi yang kuat dan aman.'},
            'vi': {'title': 'Trình Tạo Mật Khẩu Mạnh', 'desc': 'Tạo mật khẩu mạnh và an toàn.'},
            'th': {'title': 'เครื่องมือสร้างรหัสผ่านที่รัดกุม', 'desc': 'สร้างรหัสผ่านที่รัดกุมและปลอดภัย'},
            'de': {'title': 'Sicherer Passwort-Generator', 'desc': 'Generieren Sie starke und sichere Passwörter.'},
            'pt': {'title': 'Gerador de Senha Forte', 'desc': 'Gere senhas fortes e seguras.'}
        }
    },
    {
        'slug': 'thumbnail-downloader',
        'icon': '📺',
        'trans': {
            'ko': {'title': '유튜브 썸네일 다운로더', 'desc': '유튜브 영상의 썸네일 이미지를 고화질로 다운로드하세요.'},
            'en': {'title': 'YouTube Thumbnail Downloader', 'desc': 'Download YouTube video thumbnails in high quality.'},
            'ja': {'title': 'YouTubeサムネイルダウンローダー', 'desc': 'YouTube動画のサムネイル画像を高品質でダウンロードします。'},
            'hi': {'title': 'YouTube थंबनेल डाउनलोडर', 'desc': 'YouTube वीडियो थंबनेल छवियों को उच्च गुणवत्ता में डाउनलोड करें।'},
            'id': {'title': 'Pengunduh Thumbnail YouTube', 'desc': 'Unduh thumbnail video YouTube dalam kualitas tinggi.'},
            'vi': {'title': 'Trình Tải Thumbnail YouTube', 'desc': 'Tải xuống hình thu nhỏ video YouTube chất lượng cao.'},
            'th': {'title': 'เครื่องมือดาวน์โหลดภาพปก YouTube', 'desc': 'ดาวน์โหลดภาพขนาดย่อวิดีโอ YouTube ด้วยคุณภาพสูง'},
            'de': {'title': 'YouTube Thumbnail Downloader', 'desc': 'Laden Sie YouTube-Video-Thumbnails in hoher Qualität herunter.'},
            'pt': {'title': 'Baixar Thumbnail do YouTube', 'desc': 'Baixe miniaturas de vídeos do YouTube em alta qualidade.'}
        }
    },
    {
        'slug': 'markdown-previewer',
        'icon': '📝',
        'trans': {
            'ko': {'title': '마크다운 에디터 & 미리보기', 'desc': '실시간 마크다운 미리보기 도구.'},
            'en': {'title': 'Markdown Editor & Preview', 'desc': 'Real-time Markdown preview tool.'},
            'ja': {'title': 'Markdownエディタ＆プレビュー', 'desc': 'リアルタイムMarkdownプレビューツール。'},
            'hi': {'title': 'मार्कडाउन एडिटर और पूर्वावलोकन', 'desc': 'रीयल-टाइम मार्कडाउन पूर्वावलोकन उपकरण।'},
            'id': {'title': 'Editor & Pratinjau Markdown', 'desc': 'Alat pratinjau Markdown waktu nyata.'},
            'vi': {'title': 'Trình Biên Tập & Xem Trước Markdown', 'desc': 'Công cụ xem trước Markdown thời gian thực.'},
            'th': {'title': 'ตัวแก้ไขและดูตัวอย่าง Markdown', 'desc': 'เครื่องมือดูตัวอย่าง Markdown แบบเรียลไทม์'},
            'de': {'title': 'Markdown Editor & Vorschau', 'desc': 'Echtzeit-Markdown-Vorschau-Tool.'},
            'pt': {'title': 'Editor e Visualizador Markdown', 'desc': 'Ferramenta de visualização Markdown em tempo real.'}
        }
    },
    {
        'slug': 'reaction-test',
        'icon': '⚡',
        'trans': {
            'ko': {'title': '반응 속도 테스트', 'desc': '당신의 반응 속도는 얼마입니까? 테스트해보세요!'},
            'en': {'title': 'Reaction Speed Test', 'desc': 'Test your reaction time. Click fast!'},
            'ja': {'title': '反応速度テスト', 'desc': 'あなたの反応速度をテストします。'},
            'hi': {'title': 'प्रतिक्रिया गति परीक्षण', 'desc': 'अपनी प्रतिक्रिया समय का परीक्षण करें।'},
            'id': {'title': 'Tes Kecepatan Reaksi', 'desc': 'Uji waktu reaksi Anda.'},
            'vi': {'title': 'Kiểm Tra Tốc Độ Phản Xạ', 'desc': 'Kiểm tra thời gian phản xạ của bạn.'},
            'th': {'title': 'ทดสอบความเร็วปฏิกิริยา', 'desc': 'ทดสอบเวลาปฏิกิริยาของคุณ'},
            'de': {'title': 'Reaktionszeittest', 'desc': 'Testen Sie Ihre Reaktionszeit.'},
            'pt': {'title': 'Teste de Tempo de Reação', 'desc': 'Teste seu tempo de reação.'}
        }
    },
]

def update_index_page(lang):
    """Update index.html for a language"""
    index_path = BASE_DIR / lang / 'index.html'
    if not index_path.exists():
        print(f"⚠️ {lang}/index.html not found, skipping.")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if tools actully exist in the folder (sanity check)
    # Skipping this to be fast, assuming previous steps worked.

    new_cards_html = ""
    for tool in NEW_TOOLS:
        slug = tool['slug']
        # Skip if already in content
        if f'href="/{lang}/{slug}/"' in content:
            print(f"  ℹ️ {slug} already exists in {lang}/index.html")
            continue
            
        icon = tool['icon']
        title = tool['trans'][lang]['title']
        desc = tool['trans'][lang]['desc']
        
        card_html = f'''
        <a href="/{lang}/{slug}/" class="card">
          <div class="card-icon">{icon}</div>
          <h3 class="card-title">{title}</h3>
          <p class="card-description">{desc}</p>
        </a>'''
        new_cards_html += card_html

    if not new_cards_html:
        print(f"  ✓ {lang}/index.html is up to date.")
        return

    # Injection logic: Find the closing </div> of .card-grid
    # We assume valid HTML structure where card-grid div closes properly.
    # Looking for the last </div> inside <main> or specifically indentation
    
    # Simple heuristic: Split by <footer class="site-footer">, then find the last </div> before that.
    
    parts = content.split('<footer class="site-footer">')
    if len(parts) != 2:
        print(f"❌ Could not safe-split {lang}/index.html")
        return
        
    main_part = parts[0]
    footer_part = parts[1]
    
    # In main_part, find the last </div> and insert before it.
    # Typically: ... </div>\n    </div>\n  </main>
    # The Card Grid is inside .container inside .main-content
    
    # Let's try to inject before "      </div>\n    </div>\n  </main>"
    # Or just replace '      </div>\n    </div>\n  </main>' with '      </div>' + new_cards + '    </div>\n  </main>'
    # This is brittle.
    
    # Better: find `class="card-grid">` and then find the corresponding closing div.
    # Given the file view, we saw:
    # 82:       <div class="card-grid">
    # ...
    # 165:       </div>
    # 166:     </div>
    # 167:   </main>
    
    # We can search for `      </div>\n    </div>\n  </main>` (end of main container)
    # And insert into the div before that.
    
    insertion_marker = '      </div>\n    </div>\n  </main>'
    if insertion_marker in main_part:
        # The first </div> in this marker matches the closing of card-grid?
        # No, wait.
        # <div class="container"> (74)
        #   ...
        #   <div class="card-grid"> (82)
        #     ...cards...
        #   </div> (165)
        # </div> (166)
        # </main> (167)
        
        # So `</div>\n    </div>\n  </main>` corresponds to lines 165, 166, 167.
        # We want to insert BEFORE line 165.
        
        new_content = content.replace(insertion_marker, new_cards_html + '\n' + insertion_marker)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Updated {lang}/index.html")
        
    else:
        # Fallback: regex or manual search
        # Try finding the LAST `</div>` before `</main>`
        # This is getting risky. Let's try a safer string match based on the last card added manually?
        # "Favicon 생성기" is the last one in KO, but different in others.
        
        # Let's try searching for `</div>\n    </div>\n  </main>` variations
        print(f"⚠️ Could not find exact insertion marker in {lang}/index.html. Attempting fuzzy match.")
        
        # Try to find the closing tag of card-grid by indentation?
        # It usually has 6 spaces indentation
        
        target = '      </div>\n    </div>\n  </main>'
        # Try normalizing line endings?
        
        if target.replace('\r\n', '\n') in content.replace('\r\n', '\n'):
             # normalizing worked?
             content = content.replace('      </div>\n    </div>\n  </main>', new_cards_html + '\n' + '      </div>\n    </div>\n  </main>')
             with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
             print(f"✅ Updated {lang}/index.html (Fuzzy Match)")
        else: 
             print(f"❌ FAILED to update {lang}/index.html - Marker not found.")

def main():
    print("🚀 Injecting new tools into Index Pages...\n")
    for lang in LANGUAGES:
        update_index_page(lang)
    print("\n✨ Done.")

if __name__ == '__main__':
    main()

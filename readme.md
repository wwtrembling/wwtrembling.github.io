나는 GitHub Pages 기반의 클라이언트 전용 유틸리티 모음 사이트를 만들려고 한다. 
아래 조건을 만족하는 형태로 전체 프로젝트 구조, 폴더 구성, 페이지 파일 생성, 템플릿 코드 작성까지 모두 자동으로 생성해줘.
각 유틸 페이지는 한국, 일본, 미국, 인도, 인도네시아, 베트남, 태국, 독일, 브라질 버전으로 자동 생성해줘.
각 언어별로 완전한 독립 HTML 파일을 만들고,
SEO 최적화(hreflang, title 번역, description 번역, JSON-LD 번역)를 포함해줘.

[프로젝트 개요]
- 프로젝트명: Tool Shelf
- 정적 사이트(GitHub Pages 전용)
- 모든 유틸은 HTML + CSS + JS만 사용 (백엔드 없음)
- 다국어 지원: 
    한국	한국어	ko
    일본	일본어	ja
    미국	영어	en
    인도	힌디어	hi
    인도네시아	인도네시아어	id
    베트남	베트남어	vi
    태국	태국어	th
    독일	독일어	de
    브라질	포르투갈어	pt
- 검색 엔진 최적화(SEO) 필수
- JSON-LD 포함
- 모바일 대응(Responsive)
- 페이지 로딩 속도 최적화

[공통 구조]
루트 경로는 다음처럼 구성해야 함:
/
 ├─ index.html
 ├─ sitemap.xml
 ├─ robots.txt
 ├─ ko/
 │   ├─ index.html
 │   └─ [각 유틸별 폴더]/index.html
 └─ en/
     ├─ index.html
     └─ [각 유틸별 폴더]/index.html

[각 유틸 페이지 요구사항]
- index.html 1개로 구성
- SEO 최적화된 title, meta description 포함
- 언어 전환 버튼 포함 (ko ↔ en)
- JSON-LD(WebPage + FAQPage 선택적으로 포함)
- 깔끔한 UI(CSS 구성 포함)
- 광고(Adsense) 위치 placeholder 추가 <!-- adsense -->

[필수 기능]
- ko/, en/ 각각에 동일 구조 생성
- 루트 index.html은 서비스 소개 페이지로 구성
- sitemap.xml 자동 생성
- robots.txt 자동 생성
- 모든 유틸에 공유 header/footer 템플릿 적용
- 가능한 한 유지보수 쉬운 폴더 구조 제공

[출력 형식]
- 전체 파일/폴더 구조 트리로 먼저 출력
- 이후 각 파일의 코드(full HTML/CSS/JS 포함)를 순서대로 출력
- 특히 index.html들은 모두 실제로 브라우저에서 바로 열리는 형태로 제공할 것
- 불필요한 설명 최소화하고 코드 중심으로 출력


[제작해야 할 유틸]
# 단위 변환기 (Unit Converter)
   - 길이·무게·온도·부피·속도 등 각종 단위를 상호 변환.
   - Pure JS로 수식만 구현하며 정확도만 신경 쓰면 됨.
   - 검색량 높고 승률 좋은 범용 유틸.

# PDF 압축기 (PDF Compress)
   - pdf-lib 또는 pdf.js + wasm 기반으로 클라이언트 압축 처리.
   - 화질·용량 옵션 제공.
   - 개인 정보 노출 없이 로컬에서 처리하는 점을 강조 가능.

# PDF 병합기 (PDF Merge)
   - 여러 PDF 파일 업로드 후 하나로 병합.
   - pdf-lib로 완전 client-side 처리 가능.

# 이미지 리사이즈 & WebP 변환기
   - Canvas API로 리사이즈 후 WebP로 변환.
   - blog·전자상거래·SNS 업로드 전 최적화 용도로 인기 있음.

# 매일 성경말씀 복사 (Daily Bible Verse Copier)

# BMI & TDEE 계산기
   - BMI, 기초대사량, 활동 레벨별 칼로리 계산.
   - 계산식만 JS로 구현하면 됨.
   - 다이어트/헬스 키워드로 SEO 강력.

# 날짜 계산기 (D-Day / 날짜 차이 계산)
   - 특정 날짜까지 남은 일수 계산.
   - 날짜 차이 / 생일 디데이
   - JS Date 객체로 쉽게 구현 가능.

# 텍스트 유틸 (단어 수 세기, 중복 제거 등)
   - 문장 수, 단어 수, 글자 수 계산.
   - 중복 라인 제거, 정렬, 토크나이징 등 포함 가능.
   - 블로그·에세이 작성자 타겟으로 검색량 큼.

# JSON 포매터 / JSON Viewer
   - JSON beautify / minify / tree view 지원.
   - Ace Editor, Monaco Editor 사용 가능.
   - 개발자들이 자주 찾는 고품질 트래픽 유틸.

# 색상 변환기 (HEX ↔ RGB ↔ HSL)
    - 색상 입력하면 즉시 변환.
    - UI 디자인/프론트엔드 개발자용 수요 많음.

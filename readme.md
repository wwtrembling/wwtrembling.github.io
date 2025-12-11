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

[제작해야 할 유틸 10개]
1) 단위 변환기 (unit converter)
2) PDF 압축/병합 (client-side pdf-lib)
3) 이미지 리사이즈 & WebP 변환기
4) 오늘의 말씀 (Bible verse generator)
5) BMI & TDEE 계산기
6) 날짜 계산기 (D-DAY, 일수 차이 계산)
7) 텍스트 유틸(단어 수 세기, 중복 제거)
8) JSON 포매터
9) 색상 변환기 (HEX/RGB/HSL)
10) 온라인 타이머 / 포모도로 타이머

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

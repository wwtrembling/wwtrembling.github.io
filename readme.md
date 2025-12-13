# Tool Shelf

GitHub Pages 기반의 클라이언트 전용 유틸리티 모음 사이트

## 프로젝트 개요

- **프로젝트명**: Tool Shelf
- **배포**: GitHub Pages (https://utilifyapp.net)
- **기술 스택**: HTML + CSS + JavaScript (백엔드 없음)
- **특징**: 완전한 클라이언트 사이드 처리, 개인정보 보호

## 지원 언어 (9개국)

| 국가 | 언어 | 코드 |
|------|------|------|
| 한국 | 한국어 | ko |
| 일본 | 일본어 | ja |
| 미국 | 영어 | en |
| 인도 | 힌디어 | hi |
| 인도네시아 | 인도네시아어 | id |
| 베트남 | 베트남어 | vi |
| 태국 | 태국어 | th |
| 독일 | 독일어 | de |
| 브라질 | 포르투갈어 | pt |

## 구현된 유틸리티 (13개)

### ✅ 1. 단위 변환기 (Unit Converter)
- **경로**: `/{lang}/unit-converter/`
- **기능**: 길이, 무게, 온도, 부피, 속도 등 다양한 단위 변환
- **구현**: Pure JavaScript

### ✅ 2. 이미지 변환기 (Image Converter)
- **경로**: `/{lang}/image-converter/`
- **기능**: 이미지 리사이즈 및 WebP, JPEG, PNG 변환
- **구현**: Canvas API
- **특징**: 드래그 앤 드롭, 실시간 미리보기, 품질 조절

### ✅ 3. 매일 성경말씀 복사 (Daily Bible Verse Copier)
- **경로**: `/ko/daily-verse/` (한국어 전용)
- **기능**: 365일 성경 읽기 계획 복사
- **특징**: 캘린더 기반 인터페이스, 원클릭 복사

### ✅ 4. BMI & TDEE 계산기
- **경로**: `/{lang}/bmi-calculator/`
- **기능**: BMI, 기초대사량, 활동 레벨별 칼로리 계산
- **구현**: JavaScript 계산식

### ✅ 5. 날짜 계산기 (Date Calculator)
- **경로**: `/{lang}/date-calculator/`
- **기능**: D-Day 계산, 날짜 차이 계산
- **구현**: JavaScript Date 객체

### ✅ 6. 텍스트 유틸 (Text Utils)
- **경로**: `/{lang}/text-utils/`
- **기능**: 단어 수 세기, 중복 제거, 정렬
- **특징**: 블로그 작성자용 도구

### ✅ 7. JSON 포매터 (JSON Formatter)
- **경로**: `/{lang}/json-formatter/`
- **기능**: JSON beautify, minify, tree view
- **특징**: 개발자용 고품질 트래픽 유틸

### ✅ 8. 색상 변환기 (Color Converter)
- **경로**: `/{lang}/color-converter/`
- **기능**: HEX ↔ RGB ↔ HSL 변환
- **특징**: UI 디자이너/프론트엔드 개발자용

### ✅ 9. 타이머/포모도로 (Timer/Pomodoro)
- **경로**: `/{lang}/timer/`
- **기능**: 카운트다운, 스톱워치, 포모도로 타이머
- **구현**: Web Worker (백그라운드 정확도)

### ✅ 10. SQL 포매터 (SQL Formatter)
- **경로**: `/{lang}/sql-formatter/`
- **기능**: SQL 쿼리 beautify & minify
- **구현**: sql-formatter 라이브러리
- **특징**: 6가지 SQL 방언 지원 (MySQL, PostgreSQL, etc.)

### ✅ 11. 정규식 테스터 (Regex Tester)
- **경로**: `/{lang}/regex-tester/`
- **기능**: 정규식 패턴 테스트 및 매칭 결과 표시
- **특징**: 실시간 매칭, 하이라이트 표시

### ✅ 12. Base64 인코더/디코더
- **경로**: `/{lang}/base64-converter/`
- **기능**: 텍스트 ↔ Base64 변환
- **구현**: btoa/atob 브라우저 API

### ✅ 13. QR 코드 생성기 (QR Code Generator)
- **경로**: `/{lang}/timer/`
- **기능**: 카운트다운, 스톱워치, 포모도로 타이머
- **구현**: Web Worker (백그라운드 정확도)

## 프로젝트 구조

```
/
├─ index.html              # 메인 랜딩 페이지
├─ sitemap.xml             # SEO 사이트맵
├─ robots.txt              # 검색엔진 크롤러 설정
├─ assets/                 # 공통 리소스
│   ├─ css/
│   └─ js/
├─ scripts/                # Python 유틸리티 스크립트
│   ├─ generate_pages.py
│   ├─ create_daily_verse_pages.py
│   └─ ...
└─ {lang}/                 # 언어별 디렉토리 (ko, en, ja, hi, id, vi, th, de, pt)
    ├─ index.html          # 언어별 메인 페이지
    ├─ unit-converter/
    ├─ image-converter/
    ├─ daily-verse/        # (ko only)
    ├─ bmi-calculator/
    ├─ date-calculator/
    ├─ text-utils/
    ├─ json-formatter/
    ├─ color-converter/
    └─ timer/
```

## SEO 최적화

모든 페이지에 다음 요소 포함:
- ✅ 언어별 hreflang 태그
- ✅ 번역된 title 및 meta description
- ✅ Open Graph 태그
- ✅ Twitter Card 태그
- ✅ JSON-LD 구조화 데이터
- ✅ Canonical URL
- ✅ 모바일 최적화 (Responsive Design)

## 광고 수익화

- Google AdSense 통합
- 각 페이지에 광고 위치 최적화

## 개발 도구

### Python 스크립트 (scripts/)

프로젝트 관리 및 자동화를 위한 Python 스크립트:
- `generate_pages.py` - 페이지 자동 생성
- `create_daily_verse_pages.py` - Daily Verse 페이지 생성
- `insert_adsense.py` - AdSense 코드 삽입
- `update_domain.py` - 도메인 업데이트

## 배포

GitHub Pages를 통해 자동 배포:
- Repository: `wwtrembling/utilifyapp.net`
- URL: `https://utilifyapp.net`

## 라이선스

이 프로젝트는 개인 프로젝트입니다.

# Utilify — TODO

현재 master tip: `de83c64` (PR #19: ja 10개 calculator 번역).
브랜치: `claude/review-project-issues-RFR4u`.

## 작업 우선순위

### A. 자율 가능 — 즉시 진행

#### A1. 번역 백필 (가장 큰 backlog)

ja 첫 wave 10개 완료(PR #19). 남은 작업:

**ja 백로그 (24 dicts)**
- 금융: `LOAN_CALCULATOR` `COMPOUND_INTEREST` `RETIREMENT_CALCULATOR`
- 건강: `PREGNANCY_CALCULATOR`
- AI (Tier 3): `RAG_CHUNKER` `FEW_SHOT_FORMATTER` `JSON_SCHEMA_VALIDATOR`
- AI (Tier 2): `TOKEN_COUNTER` `MCP_CONFIG_GEN` `AI_IMAGE_INSPECTOR` `CHATGPT_TO_BLOG` `PROMPT_PII_SCRUBBER` `CLAUDE_MD_GEN`
- 개발: `HASH_GENERATOR` `JWT_DECODER` `UUID_GENERATOR` `UNIX_TIMESTAMP` `URL_ENCODER`
- 허브: `FINANCE_HUB` `HEALTH_HUB`
- Static: `ABOUT` `NOT_FOUND` (legal `PRIVACY` `TERMS`는 책임 회피로 영어 폴백 유지)

**다른 언어 (8개 lang × 34 dicts ≈ 7,600 strings)**
- 신뢰도 높은 순서: `zh-cn` → `zh-tw` (script 변환만) → `de` → `pt` (pt_BR)
- 신뢰도 낮음: `vi` `th` `id` `hi` (LLM 품질 한계, 추후 외부 검수 권장)

**진행 패턴**: 언어별로 10개씩 batch → PR → 머지. 일관성 + 리뷰 부담 ↓.

#### A2. GA4 custom events

GA4 라이브(PR #18). 기본 `page_view`만 들어옴 → 도구별 사용 인사이트 없음. 추가할 이벤트:

- `tool_calculate` — Calculate 버튼 클릭 (tool_slug 파라미터)
- `tool_share` — Share Result 사용 (tool_slug, method=share|copy)
- `tool_favorite` — 즐겨찾기 추가/제거 (tool_slug, action)
- `theme_toggle` — 다크 모드 토글 (next_theme)
- `search_used` — 인덱스 검색어 입력 (query_length)
- `category_filter` — 카테고리 필터 클릭 (category)
- `hub_navigation` — 허브 페이지 진입 (source=chip|breadcrumb|direct)

구현: 각 도구 inline script에 `gtag('event', ...)` 호출 추가. 또는 공통 헬퍼 함수로 추출. 1 PR.

#### A3. `lang.py` 구조 validator + CI

향후 lang dict 변경 시 회귀 방지. 검사 항목:
- 각 도구 dict의 모든 lang sub-dict에 같은 키 세트 존재
- `TOOLS_CONFIG` / `TOOL_CATEGORIES` / `TOOL_KEYWORDS` / `TOOL_SUBCATEGORIES`에 등록된 모든 slug가 lang dict에 있고 그 반대도 성립
- `meta_desc` 길이 50-165자 범위
- 중복 slug 차단

Python script + `.github/workflows/build-check.yml`에 step 추가. 1 PR, 작음.

#### A4. Favorites export/import

현재 localStorage `utilify_favorites`만 — 디바이스 간 이동 불가. 추가:
- About 페이지(또는 신규 `/<lang>/settings/`)에 "Export"/"Import" 버튼
- Export: JSON으로 다운로드 (`utilify-favorites-2026-05-29.json`)
- Import: 파일 업로드 후 localStorage 병합
- 다크 모드 설정도 같이 포함 가능

1 PR.

#### A5. SW update notification UX

새 버전 deploy 후 사용자가 옛 캐시본에 갇히지 않도록:
- `navigator.serviceWorker.controller` 변경 감지 시 작은 토스트 표시
- "새 버전이 있습니다 — [새로고침]"
- 사용자가 새로고침 누르면 `window.location.reload()`

`assets/js/common.js`에 ~20줄 추가. 1 PR.

---

### B. 사용자 결정 필요

#### B1. 번역 백필 전략

- 현재: 머신 번역 (LLM) 품질 — 70~85% 수준
- 옵션: 외부 번역 서비스 (Crowdin / Lokalise / 사람) 사용 여부
- 옵션: 부분 언어만 머신 번역(ja/de/zh-cn), 나머지는 영어 폴백 유지

#### B2. CMP 설정

GA4 Consent Mode v2 default-denied 상태 → CMP 없으면 EU/UK 사용자 데이터는 modeled만 들어옴.
- Funding Choices(AdSense 내장) 활성화 여부 확인 필요
- 또는 별도 CMP 도입 (Cookiebot, OneTrust 등)

#### B3. 추가 도구 카테고리

신규 도구 더 추가할지 — 현재 60+개로 충분히 분류돼 있음. 추가 시:
- KR 특화 (양도세, 종합소득세, 퇴직금) — **세법 정확도 검증 필요**
- 환율 변환기 (데이터 소스 결정: 정적표 vs 외부 API)
- AI 텍스트 감지기 — **False confidence 위험으로 추천 안 함**

---

### C. 운영 / 모니터링

- [ ] GA4 dashboard 24h 후 확인 (Real-time view는 즉시 가능)
- [ ] 다음 월요일 06:00 UTC에 `weekly-sitemap-refresh.yml` cron 실제 실행 확인
- [ ] CMP(Funding Choices) 설정 후 GA4 데이터 양 증가 확인
- [ ] Google Search Console에 sitemap.xml 등록 여부 (등록 안 됐다면 등록)

---

### D. Backlog (당분간 보류)

- 한국 세금 계산기 (세법 정확도 검증 필요)
- 외부 API 통합 (privacy-first 정책 충돌)
- 다크 모드 톤 변경 (주관적 디자인)
- 분류 / IA 추가 라운드 (충분히 분류됨)
- 또 다른 UX 검수 (직전 라운드 false positive 비율 높음)

---

## 최근 머지 이력 (참고)

| PR | master | 내용 |
|---|---|---|
| #6 | (이전) | 6 calc + L1/L2/L3 + favorites + share + a11y |
| #7 | (이전) | 11 tools + dark mode + hub SEO schema |
| #8 | `162c727` | UX audit fixes + dark contrast + search UX |
| #9 | `6ebd64f` | 도구 페이지 브레드크럼 |
| #10 | `52d4e42` | Conversion pair 브레드크럼 |
| #11 | `705673a` | Prebuilt 도구 브레드크럼 |
| #12 | `2eeaa35` | 검색 매치 하이라이트 |
| #13 | `8694cf1` | Static 페이지 브레드크럼 |
| #14 | `3e01dad` | og fallback + meta desc 길이 |
| #15 | `f79d99d` | CI: build verify + 주 1회 sitemap refresh |
| #16 | `b300351` | og:locale + img alt + 루트 index 파이프라인 |
| #17 | `b7d7a56` | Service Worker (오프라인 + 빠른 반복 로드) |
| #18 | `e254855` | GA4 (G-4N18KB15VT) + Consent Mode v2 |
| #19 | `de83c64` | Japanese 10 high-volume calculators |

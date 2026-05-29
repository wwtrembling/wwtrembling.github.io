# Utilify — TODO

브랜치: `claude/youthful-hamilton-8rLMK`.

## 이번 세션 완료

#### A1 (부분) — ja 번역 백로그 (22 dicts)
ja 첫 wave(PR #19, 10개)에 이어 남은 ja 백로그 22 dicts 완료:
- 개발(5): `JWT_DECODER` `HASH_GENERATOR` `UNIX_TIMESTAMP` `UUID_GENERATOR` `URL_ENCODER`
- Static(2): `ABOUT` `NOT_FOUND`
- AI Tier 2(6): `PROMPT_PII_SCRUBBER` `CLAUDE_MD_GEN` `MCP_CONFIG_GEN` `TOKEN_COUNTER` `AI_IMAGE_INSPECTOR` `CHATGPT_TO_BLOG`
- 금융(3): `LOAN_CALCULATOR` `COMPOUND_INTEREST` `RETIREMENT_CALCULATOR`
- 건강(1): `PREGNANCY_CALCULATOR`
- 허브(2): `FINANCE_HUB` `HEALTH_HUB`
- AI Tier 3(3): `RAG_CHUNKER` `FEW_SHOT_FORMATTER` `JSON_SCHEMA_VALIDATOR`

→ `check_lang_completeness.py` 기준 ja는 이제 `PRIVACY`/`TERMS`만 누락(책임 회피로 영어 폴백 의도 유지).

#### A2 — GA4 custom events (7종)
기본 `page_view` 외 도구 사용 인사이트 이벤트 추가:
- `tool_calculate` / `tool_share` — `common.js` 문서 레벨 위임 리스너 (btn-primary 액션 / `shareResult()` 호출, method=share|copy)
- `theme_toggle`(next_theme) / `tool_favorite`(tool_slug, action) — `build.py` 주입 핸들러
- `search_used`(query_length) / `category_filter`(category) / `tool_favorite`(인덱스) — `index.html` 템플릿 JS
- `hub_navigation`(hub_slug, source=chip|breadcrumb|direct) — `category_hub.html` + `build.py`(`?src=` 파라미터)

#### A4 — Favorites export/import
- `common.js` `FavoritesData` 모듈: Export(즐겨찾기+테마 → `utilify-favorites-YYYY-MM-DD.json`), Import(파싱·slug 검증·합집합 병합·테마 적용·리로드)
- `index.html` 푸터에 Export/Import 버튼 + 숨김 file input
- `INDEX_PAGE`에 `favorites_export` 등 5개 문자열(en/ko/ja, 그 외 언어는 영어 폴백)

---

## 남은 작업

### A1. 번역 백필 (나머지 언어)

ja 완료. 남은 작업은 다른 언어 (8개 lang × ~34 dicts ≈ 7,600 strings):
- 신뢰도 높은 순서: `zh-cn` → `zh-tw` (script 변환만) → `de` → `pt` (pt_BR)
- 신뢰도 낮음: `vi` `th` `id` `hi` (LLM 품질 한계, 추후 외부 검수 권장)
- **진행 패턴**: 언어별로 10개씩 batch. `check_lang_completeness.py`로 회귀 확인.

---

## 최근 머지 이력 (참고)

| PR | master | 내용 |
|---|---|---|
| #15 | `f79d99d` | CI: build verify + 주 1회 sitemap refresh |
| #16 | `b300351` | og:locale + img alt + 루트 index 파이프라인 |
| #17 | `b7d7a56` | Service Worker (오프라인 + 빠른 반복 로드) |
| #18 | `e254855` | GA4 (G-4N18KB15VT) + Consent Mode v2 |
| #19 | `de83c64` | Japanese 10 high-volume calculators |
| #20 | `0fd49f5` | todo.md 백로그 |

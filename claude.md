# Project Development Rules

## 작업 규칙
- 분담해서 작업이 가능하다면 서브에이전트를 활용하여 병렬로 작업을 수행
- 번역이 필요한 케이스는 claude 가 알아서 수행
- **배포까지 claude 가 알아서 수행** — 작업 브랜치 푸시로 끝내지 말고 아래 배포 절차까지 진행

## 6. 배포 (Deploy)
- 이 저장소는 GitHub Pages 가 **master 브랜치를 그대로 서빙**한다 (`CNAME: utilifyapp.net`).
  별도 배포 워크플로가 없으므로 **master 에 병합해야 사이트에 반영된다.**
- 배포 절차:
  1. 작업 브랜치에서 커밋
  2. `python3 _scripts/build.py` 실행 → `sw.js` 의 `CACHE_VERSION` 이 오늘 날짜로 스탬프됨
     (`sitemap.xml` 은 lastmod 만 바뀌는 노이즈이므로 주간 워크플로에 맡기고 커밋에서 제외)
  3. master 에 병합 후 `git push -u origin master`
- **CSS/JS 를 수정했으면 `CACHE_VERSION` 갱신은 필수.** `sw.js` 가 `.css`/`.js` 를
  cache-first 로 캐싱하기 때문에, 버전을 올리지 않으면 재방문자는 계속 옛 파일을 받는다.

## 1. File & Directory Structure
- **Repo**: GitHub Pages site (`wwtrembling/wwtrembling.github.io`).
- **Language Folders**: `ko`, `en`, `ja`, `zh-cn`, `zh-tw`, `hi`, `id`, `vi`, `th`, `de`, `pt`
- **Tool Directories**: Inside language folders, use kebab-case (e.g., `jpa-converter`, `json-to-ts`).
- **File Name**: Main file is always `index.html`.

## 2. HTML Standards
- **Doctype**: `<!DOCTYPE html>`
- **Meta Tags**:
  - `charset="UTF-8"`
  - `viewport`
  - `description`
  - `canonical`: Must match `https://utilifyapp.net/{lang}/{tool-name}/`
  - `google-adsense-account`: `content="ca-pub-6334819180242631"`
- **AdSense Script**: Include the async script with `client=ca-pub-6334819180242631` in `<head>`.
- **CSS**: Link to `/assets/css/main.css`.
- **JS**: Link to `/assets/js/common.js` before closing `</body>`.
- **Favicon**: Standard favicon links (if applicable, though usually handled by root).

## 3. Internal Linking
- Every tool page must include a "Related Tools" (`.related-tools-section`) section at the bottom.
- Links must point to the *same language* version (e.g., `/ko/tool/` -> `/ko/other-tool/`).

## 4. JavaScript Logic
- Use Vanilla JavaScript.
- Avoid external heavy libraries unless necessary (e.g., for PDF processing).
- Handle errors gracefully (`try-catch` blocks for parsing logic).
- Use `Utils.copyToClipboard()` from `common.js` for copy functionality.

## 5. Localization
- All text must be translatable.
- Translation strings live in `_data/lang.py`; `_scripts/check_lang_completeness.py` audits coverage.
- Supported languages: Korean (ko), English (en), Japanese (ja), Simplified Chinese (zh-cn), Traditional Chinese (zh-tw), Hindi (hi), Indonesian (id), Vietnamese (vi), Thai (th), German (de), Portuguese (pt).

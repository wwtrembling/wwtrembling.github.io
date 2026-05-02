# Project Development Rules

## 1. File & Directory Structure
- **Root**: `c:\Users\wwtre\OneDrive\문서\workspace\tool_shelf`
- **Language Folders**: `ko`, `en`, `ja`, `hi`, `id`, `vi`, `th`, `de`, `pt`
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
- English is the source of truth for keys in the translation script (`scripts/translation_v2/translate_master_fix.py`).
- Supported languages: Korean (ko), English (en), Japanese (ja), Hindi (hi), Indonesian (id), Vietnamese (vi), Thai (th), German (de), Portuguese (pt).

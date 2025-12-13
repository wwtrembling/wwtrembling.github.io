// 다국어 지원 시스템

let currentLang = 'ko';
let uiText = {};
let bibleIntroData = {};
let readingPlanData = {};

// 브라우저 언어 자동 감지
export function detectLanguage() {
    const browserLang = navigator.language.substring(0, 2);
    const savedLang = localStorage.getItem('language');
    return savedLang || (browserLang === 'ko' ? 'ko' : 'en');
}

// 현재 언어 가져오기
export function getCurrentLanguage() {
    return currentLang;
}

// 언어 데이터 로드
export async function loadLanguageData(lang) {
    try {
        // UI 텍스트 로드
        const uiResponse = await fetch(`./data/${lang}/ui-text.json`);
        uiText = await uiResponse.json();
        
        // 성경 소개 로드
        const introResponse = await fetch(`./data/${lang}/bible-intro.json`);
        bibleIntroData = await introResponse.json();
        
        // 읽기 플랜 로드
        const planResponse = await fetch(`./data/${lang}/reading-plan.json`);
        readingPlanData = await planResponse.json();
        
        currentLang = lang;
        localStorage.setItem('language', lang);
        
        console.log(`✅ ${lang} 언어 데이터 로드 완료`);
        return true;
    } catch (error) {
        console.error('❌ 언어 데이터 로드 실패:', error);
        return false;
    }
}

// 언어 전환
export async function changeLanguage(lang) {
    const success = await loadLanguageData(lang);
    if (success) {
        // 언어 선택 버튼 업데이트
        updateLanguageButtons(lang);
        // 전역 이벤트 발생
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }
}

// 언어 선택 버튼 업데이트
function updateLanguageButtons(lang) {
    document.querySelectorAll('.language-button').forEach(btn => {
        if (btn.dataset.lang === lang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

// UI 텍스트 가져오기
export function getUIText(key) {
    return uiText[key] || key;
}

// 성경 소개 데이터 가져오기
export function getBibleIntro() {
    return bibleIntroData;
}

// 읽기 플랜 데이터 가져오기
export function getReadingPlan() {
    return readingPlanData;
}

// 초기화
export async function initI18n() {
    const lang = detectLanguage();
    await loadLanguageData(lang);
}


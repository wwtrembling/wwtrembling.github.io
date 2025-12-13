import { initI18n, getCurrentLanguage, getUIText, getBibleIntro, getReadingPlan, changeLanguage } from './i18n.js';

// 전역 변수
let bookIntroductions = {};
let bookStartDates = {};
let bibleReadings = [];
let monthNames = [];
let weekdayNames = [];

// 각 월의 일수 (윤년 고려)
const daysInMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

// 책 약어 → 전체 이름 매핑
const bookAbbrevMap = {
    // 구약 39권
    '창': '창세기', 'Gen': 'Genesis',
    '출': '출애굽기', 'Exo': 'Exodus',
    '레': '레위기', 'Lev': 'Leviticus',
    '민': '민수기', 'Num': 'Numbers',
    '신': '신명기', 'Deu': 'Deuteronomy',
    '수': '여호수아서', 'Josh': 'Joshua',
    '삿': '사사기', 'Judg': 'Judges',
    '룻': '룻기', 'Ruth': 'Ruth',
    '삼상': '사무엘서', '1Sam': '1 Samuel',
    '삼하': '사무엘서', '2Sam': '2 Samuel',
    '왕상': '열왕기서', '1Kgs': '1 Kings',
    '왕하': '열왕기서', '2Kgs': '2 Kings',
    '대상': '역대기', '1Chr': '1 Chronicles',
    '대하': '역대기', '2Chr': '2 Chronicles',
    '스': '에스라서', 'Ezra': 'Ezra',
    '느': '느헤미야서', 'Neh': 'Nehemiah',
    '에': '에스더서', 'Esth': 'Esther',
    '욥': '욥기', 'Job': 'Job',
    '시': '시편', 'Ps': 'Psalms',
    '잠': '잠언', 'Prov': 'Proverbs',
    '전': '전도서', 'Eccl': 'Ecclesiastes',
    '아': '아가', 'Song': 'Song of Solomon',
    '사': '이사야서', 'Isa': 'Isaiah',
    '렘': '예레미야서', 'Jer': 'Jeremiah',
    '애': '예레미야애가', 'Lam': 'Lamentations',
    '겔': '에스겔서', 'Ezek': 'Ezekiel',
    '단': '다니엘서', 'Dan': 'Daniel',
    '호': '호세아서', 'Hos': 'Hosea',
    '욜': '요엘서', 'Joel': 'Joel',
    '암': '아모스서', 'Amos': 'Amos',
    '옵': '오바댜서', 'Obad': 'Obadiah',
    '욘': '요나서', 'Jonah': 'Jonah',
    '미': '미가서', 'Mic': 'Micah',
    '나': '나훔서', 'Nah': 'Nahum',
    '합': '하박국서', 'Hab': 'Habakkuk',
    '습': '스바냐서', 'Zeph': 'Zephaniah',
    '학': '학개서', 'Hag': 'Haggai',
    '슥': '스가랴서', 'Zech': 'Zechariah',
    '말': '말라기', 'Mal': 'Malachi',
    // 신약 27권
    '마': '마태복음', 'Matt': 'Matthew',
    '막': '마가복음', 'Mark': 'Mark',
    '눅': '누가복음', 'Luke': 'Luke',
    '요': '요한복음', 'John': 'John',
    '행': '사도행전', 'Acts': 'Acts',
    '롬': '로마서', 'Rom': 'Romans',
    '고전': '고린도전서', '1Cor': '1 Corinthians',
    '고후': '고린도후서', '2Cor': '2 Corinthians',
    '갈': '갈라디아서', 'Gal': 'Galatians',
    '엡': '에베소서', 'Eph': 'Ephesians',
    '빌': '빌립보서', 'Phil': 'Philippians',
    '골': '골로새서', 'Col': 'Colossians',
    '살전': '데살로니가전서', '1Thess': '1 Thessalonians',
    '살후': '데살로니가후서', '2Thess': '2 Thessalonians',
    '딤전': '디모데전서', '1Tim': '1 Timothy',
    '딤후': '디모데후서', '2Tim': '2 Timothy',
    '딛': '디도서', 'Titus': 'Titus',
    '몬': '빌레몬서', 'Phlm': 'Philemon',
    '히': '히브리서', 'Heb': 'Hebrews',
    '약': '야고보서', 'Jas': 'James',
    '벧전': '베드로전서', '1Pet': '1 Peter',
    '벧후': '베드로후서', '2Pet': '2 Peter',
    '요일': '요한1서', '1John': '1 John',
    '요이': '요한2서', '2John': '2 John',
    '요삼': '요한3서', '3John': '3 John',
    '유': '유다서', 'Jude': 'Jude',
    '계': '요한계시록', 'Rev': 'Revelation'
};

// 책 약어 추출 함수
function extractBookAbbrev(reading) {
    const match = reading.match(/^([가-힣a-zA-Z0-9]+)/);
    return match ? match[1] : null;
}

// 요일 계산 함수
function getDayOfWeek(dayIndex) {
    const now = new Date();
    const year = now.getFullYear();
    
    let month = 0;
    let day = dayIndex + 1;
    
    for (let m = 0; m < 12; m++) {
        if (day <= daysInMonth[m]) {
            month = m;
            break;
        }
        day -= daysInMonth[m];
    }
    
    const targetDate = new Date(year, month, day);
    const dayOfWeek = targetDate.getDay();
    return weekdayNames[dayOfWeek] || '';
}

// 책 시작 날짜 감지 함수
function detectBookStartDates() {
    bookStartDates = {};
    let prevBook = null;
    
    for (let i = 0; i < bibleReadings.length; i++) {
        const reading = bibleReadings[i];
        const books = reading.split(',').map(s => s.trim());
        
        for (const bookReading of books) {
            const abbrev = extractBookAbbrev(bookReading);
            if (abbrev && abbrev !== prevBook) {
                const fullName = bookAbbrevMap[abbrev];
                if (fullName) {
                    if (!bookStartDates[i]) {
                        bookStartDates[i] = [];
                    }
                    bookStartDates[i].push(fullName);
                }
                prevBook = abbrev;
            }
        }
    }
}

// 클립보드에 말씀 복사하는 함수
async function copyVerse(dayIndex) {
    const reading = bibleReadings[dayIndex];
    const messageTemplate = getUIText('copyMessage');
    const message = messageTemplate.replace('{reading}', reading);
    
    try {
        await navigator.clipboard.writeText(message);
        document.getElementById('statusText').textContent = `${getUIText('copiedStatus')}: ${reading}`;
        showNotification();
    } catch (err) {
        console.error('클립보드 복사 실패:', err);
        fallbackCopyToClipboard(message, reading);
    }
}

// 클립보드에 소개 복사하는 함수
async function copyIntro(bookName, chunkIndex) {
    const introData = bookIntroductions[bookName];
    if (!introData) {
        showNotification(getUIText('warning').replace('{chars}', '0'));
        return;
    }

    const totalChunks = introData.chunks.length;
    let header = `# ${introData.title}`;
    if (totalChunks > 1) {
        header += ` ${chunkIndex + 1}/${totalChunks}`;
    }
    
    const content = `${header}\n\n${introData.chunks[chunkIndex]}`;
    const contentLength = content.length;
    
    console.log(`복사할 내용 길이: ${contentLength}자`);
    
    if (contentLength > 3900) {
        showNotification(getUIText('warning').replace('{chars}', contentLength));
        console.warn(`경고: 복사 내용이 3900자를 초과합니다. (${contentLength}자)`);
    }
    
    try {
        await navigator.clipboard.writeText(content);
        const introText = getUIText('intro');
        const statusText = totalChunks > 1 
            ? `${bookName} ${introText} (${chunkIndex + 1}/${totalChunks}) - ${contentLength}자`
            : `${bookName} ${introText} - ${contentLength}자`;
        document.getElementById('statusText').textContent = statusText;
        showNotification();
    } catch (err) {
        console.error('클립보드 복사 실패:', err);
        fallbackCopyToClipboard(content, `${bookName} ${getUIText('intro')}`);
    }
}

// Fallback 클립보드 복사 방법
function fallbackCopyToClipboard(text, statusText) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.select();
    
    try {
        document.execCommand('copy');
        document.getElementById('statusText').textContent = statusText;
        showNotification();
    } catch (err) {
        console.error('Fallback 복사 실패:', err);
        alert('클립보드 복사에 실패했습니다.');
    }
    
    document.body.removeChild(textArea);
}

// 알림 표시
function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message || getUIText('notification');
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 2000);
}

// 오늘 날짜 계산 함수
function getTodayDayIndex() {
    const now = new Date();
    const month = now.getMonth();
    const date = now.getDate();
    
    let dayIndex = 0;
    for (let m = 0; m < month; m++) {
        dayIndex += daysInMonth[m];
    }
    
    dayIndex += date - 1;
    return Math.min(dayIndex, 364);
}

// 오늘 날짜로 스크롤하는 함수
function scrollToToday() {
    const todayIndex = getTodayDayIndex();
    const todayElement = document.querySelector(`[data-day-index="${todayIndex}"]`);
    
    if (todayElement) {
        const now = new Date();
        const month = monthNames[now.getMonth()];
        const date = now.getDate();
        
        document.querySelectorAll('.day-section.today-highlight').forEach(el => {
            el.classList.remove('today-highlight');
        });
        
        todayElement.classList.add('today-highlight');
        todayElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        todayElement.style.transition = 'all 0.5s ease';
        todayElement.style.transform = 'scale(1.05)';
        
        setTimeout(() => {
            todayElement.style.transform = 'scale(1)';
        }, 1000);
        
        const goToDateMsg = getUIText('goToDate').replace('{month}', month).replace('{date}', date);
        showNotification(goToDateMsg);
    } else {
        showNotification('오늘 날짜를 찾을 수 없습니다.');
    }
}

// UI 업데이트 함수
function updateUI() {
    // 제목 업데이트
    document.title = getUIText('title');
    document.querySelector('.header h1').textContent = getUIText('title');
    document.querySelector('.today-button').textContent = getUIText('todayButton');
    document.querySelector('.status-box .label').textContent = getUIText('copiedStatus');
    
    // 월, 요일 이름 업데이트
    monthNames = getUIText('months');
    weekdayNames = getUIText('weekdays');
    
    // 데이터 로드
    const bibleIntroData = getBibleIntro();
    const readingPlanData = getReadingPlan();
    
    // 성경 소개 데이터 처리
    bookIntroductions = {};
    if (bibleIntroData.books) {
        for (const book of bibleIntroData.books) {
            bookIntroductions[book.name] = {
                title: book.title,
                chunks: book.chunks
            };
        }
    }
    
    // 읽기 플랜 데이터 처리
    if (readingPlanData.plan) {
        bibleReadings = readingPlanData.plan.map(item => item.reading);
    }
    
    // 페이지 재구성
    rebuildPage();
}

// 페이지 재구성
function rebuildPage() {
    detectBookStartDates();
    
    const content = document.getElementById('content');
    content.innerHTML = '';
    
    let dayIndex = 0;

    for (let month = 0; month < 12; month++) {
        const monthSection = document.createElement('div');
        monthSection.className = 'month-section';

        const monthTitle = document.createElement('h2');
        monthTitle.className = 'month-title';
        monthTitle.textContent = monthNames[month];
        monthSection.appendChild(monthTitle);

        const weekdayHeader = document.createElement('div');
        weekdayHeader.className = 'weekday-header';
        weekdayNames.forEach(day => {
            const dayCell = document.createElement('div');
            dayCell.textContent = day;
            weekdayHeader.appendChild(dayCell);
        });
        monthSection.appendChild(weekdayHeader);

        const daysGrid = document.createElement('div');
        daysGrid.className = 'days-grid';

        const firstDayOfMonth = getDayOfWeek(dayIndex);
        let firstDayIndex = weekdayNames.indexOf(firstDayOfMonth);
        const emptyDays = firstDayIndex;
        
        for (let i = 0; i < emptyDays; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.className = 'day-section empty-cell';
            daysGrid.appendChild(emptyCell);
        }

        for (let day = 1; day <= daysInMonth[month]; day++) {
            const daySection = document.createElement('div');
            daySection.className = 'day-section';
            daySection.setAttribute('data-day-index', dayIndex);

            const bookNames = bookStartDates[dayIndex];
            if (bookNames && Array.isArray(bookNames)) {
                for (const bookName of bookNames) {
                    if (bookIntroductions[bookName]) {
                        const introData = bookIntroductions[bookName];
                        const totalChunks = introData.chunks.length;

                        for (let chunkIdx = 0; chunkIdx < totalChunks; chunkIdx++) {
                            const introButton = document.createElement('button');
                            introButton.className = 'intro-button';
                            
                            const introText = getUIText('intro');
                            if (totalChunks > 1) {
                                introButton.textContent = `${bookName} ${introText} (${chunkIdx + 1}/${totalChunks})`;
                            } else {
                                introButton.textContent = `${bookName} ${introText}`;
                            }
                            
                            const currentBookName = bookName;
                            const currentChunkIdx = chunkIdx;
                            introButton.onclick = () => copyIntro(currentBookName, currentChunkIdx);
                            
                            daySection.appendChild(introButton);
                        }
                    }
                }
            }

            const verseButton = document.createElement('button');
            verseButton.className = 'verse-button';
            const dayText = getUIText('day');
            verseButton.textContent = `${day}${dayText}`;
            
            const currentIndex = dayIndex;
            verseButton.onclick = () => copyVerse(currentIndex);
            
            daySection.appendChild(verseButton);
            daysGrid.appendChild(daySection);
            dayIndex++;
            
            if (dayIndex >= 365) break;
        }

        monthSection.appendChild(daysGrid);
        content.appendChild(monthSection);

        if (dayIndex >= 365) break;
    }
}

// 언어 변경 이벤트 리스너
window.addEventListener('languageChanged', () => {
    updateUI();
});

// 오늘 날짜 버튼 이벤트 등록
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.today-button').addEventListener('click', scrollToToday);
});

// 언어 선택 버튼 이벤트 등록
window.changeLang = async function(lang) {
    await changeLanguage(lang);
};

// 페이지 초기화
async function initApp() {
    await initI18n();
    updateUI();
}

window.addEventListener('DOMContentLoaded', initApp);

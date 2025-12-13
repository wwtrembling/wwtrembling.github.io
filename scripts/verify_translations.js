const fs = require('fs');
const path = require('path');

const targetLangs = ['hi', 'id', 'vi', 'th', 'de', 'pt'];
const englishStrings = [
    "Unit Converter",
    "Image Converter",
    "BMI & TDEE Calculator",
    "Date Calculator",
    "Text Utilities",
    "JSON Formatter",
    "Color Converter",
    // "Timer / Pomodoro", // Often kept as English or simple transliteration
    "Base64 Converter",
    "QR Code Generator",
    "Regex Tester",
    "SQL Formatter",
    "Image Editor",
    "Lorem Ipsum Generator",
    "Favicon Generator",
    "Available Tools",
    "Use directly in your browser without installation"
];

const rootDir = path.join(__dirname, '..');
let errorCount = 0;

console.log("Starting translation verification...\n");

targetLangs.forEach(lang => {
    const filePath = path.join(rootDir, lang, 'index.html');

    if (!fs.existsSync(filePath)) {
        console.warn(`[WARN] File not found: ${lang}/index.html`);
        return;
    }

    const content = fs.readFileSync(filePath, 'utf-8');
    const missingTranslations = [];

    englishStrings.forEach(str => {
        if (content.includes(str)) {
            missingTranslations.push(str);
        }
    });

    if (missingTranslations.length > 0) {
        console.error(`[FAIL] ${lang}/index.html contains untranslated strings:`);
        missingTranslations.forEach(str => console.error(`  - "${str}"`));
        errorCount += missingTranslations.length;
    } else {
        console.log(`[PASS] ${lang}/index.html`);
    }
});

console.log("\nVerification complete.");
if (errorCount > 0) {
    console.error(`Found ${errorCount} untranslated items.`);
    process.exit(1);
} else {
    console.log("All checks passed!");
    process.exit(0);
}

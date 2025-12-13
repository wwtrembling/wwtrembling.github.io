const fs = require('fs');
const path = require('path');

const rootDir = path.join(__dirname, '..');

// Function to walk directories
function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        if (isDirectory && f !== 'node_modules' && f !== '.git' && f !== '.gemini') {
            walkDir(dirPath, callback);
        } else {
            callback(path.join(dir, f));
        }
    });
}

const placeholderRegex = /<!-- AdSense Placeholder -->\s*<div class="adsense-placeholder">[\s\S]*?<\/div>/g;

let count = 0;

walkDir(rootDir, (filePath) => {
    if (filePath.endsWith('.html')) {
        const content = fs.readFileSync(filePath, 'utf8');
        if (placeholderRegex.test(content)) {
            const newContent = content.replace(placeholderRegex, '');
            fs.writeFileSync(filePath, newContent, 'utf8');
            console.log(`Removed placeholders from: ${filePath}`);
            count++;
        }
    }
});

console.log(`\nTotal files processed: ${count}`);

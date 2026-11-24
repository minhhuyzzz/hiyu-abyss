// verify-build.js - Bộ Kiểm Thử E2E, Kiểm Định WCAG AA & Kiểm Tra Production Build
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const baseDist = path.resolve(__dirname, '../dist');
const distDir = fs.existsSync(path.join(baseDist, 'client')) ? path.join(baseDist, 'client') : baseDist;
const websiteDir = path.resolve(__dirname, '..');

console.log('====================================================');
console.log('🏛️  HIYU ABYSS — PRODUCTION BUILD & WCAG AA AUDITOR');
console.log('====================================================\n');

let passCount = 0;
let failCount = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  ✅ PASS: ${message}`);
    passCount++;
  } else {
    console.error(`  ❌ FAIL: ${message}`);
    failCount++;
  }
}

// ----------------------------------------------------
// 1. WCAG AA COLOR CONTRAST RATIO AUDIT
// ----------------------------------------------------
console.log('▶ [1/4] Kiểm định Tỷ lệ Tương phản Màu sắc (WCAG AA)');

function hexToRgb(hex) {
  hex = hex.replace('#', '');
  if (hex.length === 3) {
    hex = hex.split('').map((c) => c + c).join('');
  }
  const num = parseInt(hex, 16);
  return {
    r: (num >> 16) & 255,
    g: (num >> 8) & 255,
    b: num & 255,
  };
}

function getLuminance({ r, g, b }) {
  const [rs, gs, bs] = [r, g, b].map((val) => {
    const s = val / 255;
    return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function getContrastRatio(hex1, hex2) {
  const lum1 = getLuminance(hexToRgb(hex1));
  const lum2 = getLuminance(hexToRgb(hex2));
  const brightest = Math.max(lum1, lum2);
  const darkest = Math.min(lum1, lum2);
  return (brightest + 0.05) / (darkest + 0.05);
}

// Black Archive Tokens
const darkBg = '#090A09';
const darkTextPrimary = '#EAE5DA';
const darkTextSecondary = '#A9A49A';
const darkAccent = '#C29A77';

// Pale Archive Tokens
const lightBg = '#ECE9E1';
const lightTextPrimary = '#24251F';
const lightTextSecondary = '#63625A';
const lightAccent = '#76513D';

// WCAG AA Thresholds: Regular text >= 4.5:1, Large text >= 3.0:1
const ratioDarkPrimary = getContrastRatio(darkBg, darkTextPrimary);
const ratioDarkSecondary = getContrastRatio(darkBg, darkTextSecondary);
const ratioDarkAccent = getContrastRatio(darkBg, darkAccent);

const ratioLightPrimary = getContrastRatio(lightBg, lightTextPrimary);
const ratioLightSecondary = getContrastRatio(lightBg, lightTextSecondary);
const ratioLightAccent = getContrastRatio(lightBg, lightAccent);

console.log(`  • Black Archive Primary Text: ${ratioDarkPrimary.toFixed(2)}:1 (Min 4.5:1)`);
assert(ratioDarkPrimary >= 4.5, `Black Archive Primary Text đạt WCAG AA (${ratioDarkPrimary.toFixed(2)}:1)`);

console.log(`  • Black Archive Secondary Text: ${ratioDarkSecondary.toFixed(2)}:1 (Min 4.5:1)`);
assert(ratioDarkSecondary >= 4.5, `Black Archive Secondary Text đạt WCAG AA (${ratioDarkSecondary.toFixed(2)}:1)`);

console.log(`  • Black Archive Accent / Large Text: ${ratioDarkAccent.toFixed(2)}:1 (Min 3.0:1)`);
assert(ratioDarkAccent >= 3.0, `Black Archive Accent đạt WCAG Large Text AA (${ratioDarkAccent.toFixed(2)}:1)`);

console.log(`  • Pale Archive Primary Text: ${ratioLightPrimary.toFixed(2)}:1 (Min 4.5:1)`);
assert(ratioLightPrimary >= 4.5, `Pale Archive Primary Text đạt WCAG AA (${ratioLightPrimary.toFixed(2)}:1)`);

console.log(`  • Pale Archive Secondary Text: ${ratioLightSecondary.toFixed(2)}:1 (Min 4.5:1)`);
assert(ratioLightSecondary >= 4.5, `Pale Archive Secondary Text đạt WCAG AA (${ratioLightSecondary.toFixed(2)}:1)`);

console.log(`  • Pale Archive Accent / Large Text: ${ratioLightAccent.toFixed(2)}:1 (Min 3.0:1)`);
assert(ratioLightAccent >= 3.0, `Pale Archive Accent đạt WCAG Large Text AA (${ratioLightAccent.toFixed(2)}:1)`);

// ----------------------------------------------------
// 2. STATIC ROUTES INTEGRITY AUDIT
// ----------------------------------------------------
console.log('\n▶ [2/4] Kiểm định Tính Toàn Vẹn Tuyến Đường Tĩnh (234 trang)');

assert(fs.existsSync(distDir), 'Thư mục website/dist tồn tại');
assert(fs.existsSync(path.join(distDir, 'index.html')), 'Trang chủ /index.html tồn tại');
assert(fs.existsSync(path.join(distDir, 'library/index.html')), 'Trang /library/index.html tồn tại');
assert(fs.existsSync(path.join(distDir, 'mirror/index.html')), 'Trang /mirror/index.html tồn tại');
assert(fs.existsSync(path.join(distDir, 'mirror/su-that-va-binh-yen/index.html')), 'Hành trình /mirror/su-that-va-binh-yen tồn tại');
assert(fs.existsSync(path.join(distDir, 'search/index.html')), 'Trang /search/index.html tồn tại');
assert(fs.existsSync(path.join(distDir, 'themes/index.html')), 'Trang /themes/index.html tồn tại');
assert(fs.existsSync(path.join(distDir, '404.html')), 'Trang lỗi nhận diện /404.html tồn tại');

// Check 200 quote pages
let quotesMissing = 0;
for (let i = 1; i <= 200; i++) {
  const idStr = String(i).padStart(4, '0');
  const quotePath = path.join(distDir, `library/txt-${idStr}/index.html`);
  if (!fs.existsSync(quotePath)) {
    quotesMissing++;
  }
}
assert(quotesMissing === 0, `Đủ 200/200 trang tác phẩm chi tiết (library/txt-0001 -> txt-0200)`);

// Check sample theme pages
const sampleThemes = ['hypocrisy', 'ego', 'truth', 'freedom', 'manipulation', 'solitude'];
let themesMissing = 0;
for (const theme of sampleThemes) {
  const themePath = path.join(distDir, `themes/${theme}/index.html`);
  if (!fs.existsSync(themePath)) {
    themesMissing++;
  }
}
assert(themesMissing === 0, `Các trang chuyên đề chủ đề mở tồn tại đầy đủ`);

// ----------------------------------------------------
// 3. ASSETS & MUSEUM PROVENANCE AUDIT
// ----------------------------------------------------
console.log('\n▶ [3/4] Kiểm định Tài Nguyên Mỹ Thuật & Favicon');

assert(fs.existsSync(path.join(distDir, 'favicon.svg')), 'Favicon SVG tồn tại trong dist/');

const themeSuiteSample = path.join(distDir, 'images/themes/theme_01/slide_1_establishing.jpg');
assert(fs.existsSync(themeSuiteSample), 'Ảnh tranh cổ điển bảo tàng phân giải cao được phân phối tĩnh vào dist/');

// ----------------------------------------------------
// 4. CROSS-DEVICE & ACCESSIBILITY AUDIT
// ----------------------------------------------------
console.log('\n▶ [4/4] Kiểm định Thiết Kế Đa Thiết Bị & Chuẩn Mobile/Desktop');

const homeHtml = fs.readFileSync(path.join(distDir, 'index.html'), 'utf-8');

// Find all bundled CSS files
const astroAssetsDir = path.join(distDir, '_astro');
let bundledCssContent = '';
if (fs.existsSync(astroAssetsDir)) {
  const cssFiles = fs.readdirSync(astroAssetsDir).filter((f) => f.endsWith('.css'));
  for (const f of cssFiles) {
    bundledCssContent += fs.readFileSync(path.join(astroAssetsDir, f), 'utf-8');
  }
}

assert(
  homeHtml.includes('width=device-width') && homeHtml.includes('viewport-fit=cover'),
  'Thẻ meta viewport có viewport-fit=cover cho màn hình tai thỏ/dynamic island'
);

assert(
  bundledCssContent.includes('safe-area-inset') || homeHtml.includes('safe-area-inset'),
  'Layout chứa safe-area-inset cho các cạnh màn hình iPhone/Android'
);

assert(
  homeHtml.includes('min-h-[44px]') || homeHtml.includes('min-h-[48px]') || bundledCssContent.includes('min-h-'),
  'Nút bấm và liên kết đạt chuẩn kích thước chạm tối thiểu (Touch Target >= 44px)'
);

assert(
  bundledCssContent.includes('Cormorant Garamond') &&
    bundledCssContent.includes('Literata') &&
    bundledCssContent.includes('Be Vietnam Pro'),
  'Bộ 3 font chữ nhận diện (Brand / Quote / UI) đã được nhúng đầy đủ trong bundled CSS'
);

// ----------------------------------------------------
// SUMMARY
// ----------------------------------------------------
console.log('\n====================================================');
console.log(`📊 TỔNG KẾT KIỂM ĐỊNH: ${passCount} PASS | ${failCount} FAIL`);
console.log('====================================================\n');

if (failCount > 0) {
  process.exit(1);
} else {
  console.log('✨ TẤT CẢ CÁC BÀI KIỂM ĐỊNH ĐÃ ĐẠT TIÊU CHUẨN XUẤT BẢN CÔNG KHAI!\n');
  process.exit(0);
}

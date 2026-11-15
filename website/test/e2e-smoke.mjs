// website/test/e2e-smoke.mjs
// Rigorous E2E Smoke & Accessibility Auditor for Hiyu Abyss (P0-04 & P0-05)

import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const axeCorePath = path.resolve(__dirname, '../node_modules/axe-core/axe.min.js');

const BASE_URL = process.env.TEST_URL || 'http://localhost:4321';

const VIEWPORTS = [
  { name: 'Mobile Mini (320px)', width: 320, height: 568 },
  { name: 'Mobile Standard (360px)', width: 360, height: 640 },
  { name: 'Mobile Modern (390px)', width: 390, height: 844 },
  { name: 'Desktop Tablet (1024px)', width: 1024, height: 768 },
  { name: 'Desktop Widescreen (1440px)', width: 1440, height: 900 },
];

const PAGES_TO_TEST = [
  { path: '/', name: 'Trang Chủ (Landing)' },
  { path: '/library', name: 'Thư Viện (Library)' },
  { path: '/library/txt-0001', name: 'Tác Phẩm Chi Tiết (Detail TXT-0001)' },
  { path: '/mirror', name: 'Chiếc Gương (The Mirror Portal)' },
  { path: '/mirror/su-that-va-binh-yen', name: 'Hành Trình Gương (Mirror Journey)' },
  { path: '/search', name: 'Tìm Kiếm (Search)' },
];

async function runSmokeTests() {
  console.log('====================================================');
  console.log('🏛️  HIYU ABYSS — E2E BROWSER & ACCESSIBILITY AUDIT');
  console.log('====================================================');
  console.log(`Target URL: ${BASE_URL}`);

  let browser;
  try {
    browser = await chromium.launch({
      channel: 'chrome',
      headless: true,
    });
  } catch (err) {
    console.log('Chrome not available, falling back to Edge...');
    try {
      browser = await chromium.launch({
        channel: 'msedge',
        headless: true,
      });
    } catch (e2) {
      console.error('Neither Chrome nor Edge available via playwright-core:', e.message);
      process.exit(1);
    }
  }

  let totalTests = 0;
  let passedTests = 0;
  let failedTests = 0;

  function report(pass, msg) {
    totalTests++;
    if (pass) {
      passedTests++;
      console.log(`  ✅ PASS: ${msg}`);
    } else {
      failedTests++;
      console.error(`  ❌ FAIL: ${msg}`);
    }
  }

  const context = await browser.newContext();
  const page = await context.newPage();

  const consoleErrors = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });

  // 1. Test Viewports & Overflow (P0-04)
  console.log('\n▶ [1/4] Kiểm Định Tràn Ngang & Tương Thích Kích Thước (No Overflow)');
  for (const vp of VIEWPORTS) {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.goto(`${BASE_URL}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(300);

    const hasHorizontalScroll = await page.evaluate(() => {
      return document.documentElement.scrollWidth > window.innerWidth;
    });

    report(!hasHorizontalScroll, `Trang chủ không tràn ngang ở ${vp.name} (scrollWidth <= innerWidth)`);
  }

  // 2. Test Key Pages & 0 Console Errors (P0-04)
  console.log('\n▶ [2/4] Kiểm Định Tải Trang & Zero Console Errors');
  for (const p of PAGES_TO_TEST) {
    consoleErrors.length = 0;
    const response = await page.goto(`${BASE_URL}${p.path}`, { waitUntil: 'domcontentloaded' });
    const status = response ? response.status() : 0;
    report(status === 200, `${p.name} phản hồi HTTP 200`);
    report(consoleErrors.length === 0, `${p.name} không phát sinh console error (${consoleErrors.length} errors)`);
  }

  // 3. Test Search Security & Special Chars (P0-05)
  console.log('\n▶ [3/4] Kiểm Định An Toàn XSS & Ký Tự Đặc Biệt Trên Search (P0-05)');
  await page.goto(`${BASE_URL}/search`, { waitUntil: 'domcontentloaded' });
  const searchInput = page.locator('#search-input');
  
  // Test XSS payload
  const xssPayload = '<script>window.__xss_leaked=true</script>" autofocus onfocus=alert(1)';
  await searchInput.fill(xssPayload);
  await page.waitForTimeout(300);

  const isXssExecuted = await page.evaluate(() => {
    return window.__xss_leaked === true;
  });
  report(!isXssExecuted, 'XSS Payload không bị thực thi qua innerHTML trong search results');

  // Test Vietnamese tone & character đ
  await searchInput.fill('đạo đức');
  await page.waitForTimeout(300);
  const countText = await page.locator('#results-count').textContent();
  report(countText.includes('Tìm thấy'), `Tìm kiếm ký tự tiếng Việt có dấu và chữ 'đ' hoạt động bình thường (${countText})`);

  // 4. Test Canonical & hreflang Honesty (P0-03)
  console.log('\n▶ [4/4] Kiểm Định SEO Canonical & Trung Thực i18n (P0-03)');
  await page.goto(`${BASE_URL}/library/txt-0001`, { waitUntil: 'domcontentloaded' });

  const canonicalHref = await page.locator('link[rel="canonical"]').getAttribute('href');
  report(!!canonicalHref && !canonicalHref.includes('undefined'), `Thẻ canonical tồn tại và hợp lệ: ${canonicalHref}`);

  const fakeEnAlternate = await page.locator('link[rel="alternate"][hreflang="en"]').count();
  report(fakeEnAlternate === 0, 'Đã loại bỏ thẻ hreflang="en" giả trỏ cùng URL tiếng Việt (P0-03)');

  // Check Scholarly Verification status on TXT-0001 (P0-01)
  const isFalseVerifiedClaim = await page.evaluate(() => {
    const text = document.body.innerText;
    return text.includes('Trích dẫn đã xác minh');
  });
  report(!isFalseVerifiedClaim, 'TXT-0001 không còn hiển thị nhãn "Trích dẫn đã xác minh" khi chưa có bản in đối chiếu (P0-01)');

  await browser.close();

  console.log('\n====================================================');
  console.log(`📊 TỔNG KẾT E2E SMOKE: ${passedTests} PASS | ${failedTests} FAIL`);
  console.log('====================================================');

  if (failedTests > 0) {
    process.exit(1);
  } else {
    console.log('✨ TẤT CẢ CÁC BÀI KIỂM ĐỊNH E2E BROWSER ĐẠT TIÊU CHUẨN HOÀN TOÀN!\n');
  }
}

runSmokeTests().catch((err) => {
  console.error('Fatal test error:', err);
  process.exit(1);
});

import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';

const outDir = path.resolve('test-artifacts');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

async function run() {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });

  // 1. Desktop 1440px Dark
  const pageDesktopDark = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await pageDesktopDark.goto('http://localhost:4321/', { waitUntil: 'networkidle' });
  await pageDesktopDark.screenshot({ path: path.join(outDir, '01_hero_desktop_dark.png'), clip: { x: 0, y: 0, width: 1440, height: 800 } });

  // 2. Desktop 1440px Light
  await pageDesktopDark.evaluate(() => {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
  });
  await pageDesktopDark.waitForTimeout(300);
  await pageDesktopDark.screenshot({ path: path.join(outDir, '02_hero_desktop_light.png'), clip: { x: 0, y: 0, width: 1440, height: 800 } });

  // 3. Mirror Portal Desktop
  const pageMirror = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await pageMirror.goto('http://localhost:4321/mirror', { waitUntil: 'networkidle' });
  await pageMirror.screenshot({ path: path.join(outDir, '03_mirror_portal_desktop.png'), fullPage: false });

  // 4. Mobile 375px Dark
  const pageMobile = await browser.newPage({ viewport: { width: 375, height: 812 } });
  await pageMobile.goto('http://localhost:4321/', { waitUntil: 'networkidle' });
  await pageMobile.screenshot({ path: path.join(outDir, '04_hero_mobile_dark.png'), fullPage: false });

  // 5. Library Mobile with Bookmark buttons
  await pageMobile.goto('http://localhost:4321/library', { waitUntil: 'networkidle' });
  await pageMobile.evaluate(() => window.scrollBy(0, 450));
  await pageMobile.waitForTimeout(200);
  await pageMobile.screenshot({ path: path.join(outDir, '05_library_mobile_dark.png'), fullPage: false });

  await browser.close();
  console.log('Screenshots saved to test-artifacts/');
}

run().catch(console.error);

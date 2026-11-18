// scripts/capture-screenshots.mjs
import { execSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const outputDir = path.resolve('docs/screenshots');
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

const shots = [
  { name: 'atlas-desktop-dark.png', url: 'http://localhost:4321/atlas', width: 1440, height: 900 },
  { name: 'atlas-desktop-folio.png', url: 'http://localhost:4321/atlas?focus=idea-social-persona', width: 1440, height: 900 },
  { name: 'atlas-desktop-trail.png', url: 'http://localhost:4321/atlas?trail=su-that-va-tu-lua-doi', width: 1440, height: 900 },
  { name: 'atlas-desktop-list.png', url: 'http://localhost:4321/atlas?view=list', width: 1440, height: 900 },
  { name: 'atlas-mobile-dark.png', url: 'http://localhost:4321/atlas', width: 390, height: 844 },
  { name: 'atlas-mobile-folio.png', url: 'http://localhost:4321/atlas?focus=idea-social-persona', width: 390, height: 844 },
  { name: 'atlas-desktop-light.png', url: 'http://localhost:4321/atlas?theme=light', width: 1440, height: 900 },
  { name: 'atlas-home-portal.png', url: 'http://localhost:4321/', width: 1440, height: 900 },
  { name: 'atlas-idea-landing.png', url: 'http://localhost:4321/atlas/ideas/truth', width: 1440, height: 900 },
  { name: 'atlas-trail-landing.png', url: 'http://localhost:4321/atlas/trails/su-that-va-tu-lua-doi', width: 1440, height: 900 },
];

for (const s of shots) {
  const filePath = path.join(outputDir, s.name);
  console.log(`[capture] Capturing ${s.name} (${s.width}x${s.height})...`);
  const cmd = `"${chromePath}" --headless=new --disable-gpu --virtual-time-budget=4000 --window-size=${s.width},${s.height} --screenshot="${filePath}" "${s.url}"`;
  try {
    execSync(cmd, { stdio: 'ignore' });
    const stat = fs.statSync(filePath);
    console.log(`[capture] Saved ${s.name} (${stat.size} bytes)`);
  } catch (e) {
    console.error(`[capture] Error capturing ${s.name}:`, e.message);
  }
}

console.log('[capture] All screenshots captured successfully!');

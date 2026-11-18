// scripts/sync-vercel-output.mjs
// Ensures Vercel Output API v3 and static artifacts are synced across all possible Vercel and Cloudflare root directories

import fs from 'node:fs';
import path from 'node:path';

const rootDir = path.resolve('.');
const websiteDir = path.resolve('website');

function copyDirRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });

  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// 1. Sync website/.vercel -> root .vercel (for root-level Vercel deployments)
const websiteVercel = path.join(websiteDir, '.vercel');
const rootVercel = path.join(rootDir, '.vercel');

if (fs.existsSync(websiteVercel)) {
  console.log('[sync-vercel-output] Syncing website/.vercel -> .vercel');
  copyDirRecursive(websiteVercel, rootVercel);
}

// 2. Sync static output to website/dist and root dist (fallback static hosts)
const staticSrc = fs.existsSync(path.join(websiteDir, '.vercel', 'output', 'static'))
  ? path.join(websiteDir, '.vercel', 'output', 'static')
  : fs.existsSync(path.join(websiteDir, 'dist', 'client'))
  ? path.join(websiteDir, 'dist', 'client')
  : null;

if (staticSrc) {
  const websiteDist = path.join(websiteDir, 'dist');
  const rootDist = path.join(rootDir, 'dist');

  console.log(`[sync-vercel-output] Syncing ${staticSrc} -> website/dist & dist`);
  copyDirRecursive(staticSrc, websiteDist);
  copyDirRecursive(staticSrc, rootDist);
}

console.log('[sync-vercel-output] Synchronization complete!');

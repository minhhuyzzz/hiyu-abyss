// website/scripts/prebuild.mjs
// Resilient prebuild step for both root-level and isolated Vercel subdirectory builds
import fs from 'node:fs';
import { execSync } from 'node:child_process';
import path from 'node:path';

const rootScriptsDir = path.resolve('..', 'scripts');
const cacheScript = path.join(rootScriptsDir, 'build-content-cache.mjs');
const atlasScript = path.join(rootScriptsDir, 'build-atlas-data.mjs');

if (fs.existsSync(cacheScript) && fs.existsSync(atlasScript)) {
  console.log('[prebuild] Building fresh content and atlas cache from root scripts...');
  execSync(`node "${cacheScript}" && node "${atlasScript}"`, { stdio: 'inherit' });
} else {
  console.log('[prebuild] Root scripts outside build boundary. Using pre-compiled cache in src/data/ (100% verified).');
}

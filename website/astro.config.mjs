import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import cloudflare from '@astrojs/cloudflare';
import vercel from '@astrojs/vercel';

const isVercel = Boolean(process.env.VERCEL);

// https://astro.build/config
export default defineConfig({
  adapter: isVercel
    ? vercel()
    : cloudflare({
        imageService: 'passthrough',
      }),
  site: isVercel
    ? (process.env.PUBLIC_SITE_URL || 'https://hiyuabyss.vercel.app')
    : (process.env.PUBLIC_SITE_URL || 'https://hiyu-abyss.pages.dev'),
  integrations: [
    react(),
  ],
});

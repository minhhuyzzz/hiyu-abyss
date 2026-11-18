import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  adapter: cloudflare({
    imageService: 'passthrough',
    platformProxy: {
      enabled: true,
      configPath: 'wrangler.jsonc',
    },
  }),
  site: process.env.PUBLIC_SITE_URL || 'https://hiyu-abyss.pages.dev',
  integrations: [
    react(),
  ],
});

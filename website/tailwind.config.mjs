/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        bg: 'var(--bg)',
        surface: 'var(--surface)',
        'surface-raised': 'var(--surface-raised)',
        text: 'var(--text)',
        muted: 'var(--muted)',
        border: 'var(--border)',
        accent: 'var(--accent)',
        oxide: 'var(--oxide)',
        patina: 'var(--patina)',
        'on-accent': 'var(--on-accent)',
        paper: 'var(--color-paper)',
        ink: 'var(--color-ink)',
        rule: 'var(--color-rule)',
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', 'serif'],
        serif: ['Literata', 'serif'],
        sans: ['"Be Vietnam Pro"', 'sans-serif'],
      },
      transitionTimingFunction: {
        editorial: 'var(--ease-editorial)',
        spring: 'var(--ease-spring)',
      },
      maxWidth: {
        prose: 'var(--measure-prose)',
      },
    },
  },
  plugins: [],
};

/**
 * Safe Markdown subset parser and HTML sanitizer for The Agora & Library Comments.
 * Zero external dependencies, pure edge-compatible, strict XSS immunity.
 */

export function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

export function sanitizeUrl(url: string): string {
  const trimmed = url.trim();
  if (trimmed.startsWith('/') || trimmed.startsWith('https://') || trimmed.startsWith('http://')) {
    return trimmed;
  }
  return '#';
}

export function renderSafeMarkdown(markdown: string): string {
  if (!markdown) return '';

  // 1. First escape all raw HTML characters to prevent XSS
  let text = escapeHtml(markdown.trim());

  // 2. Headings (h2 - h4)
  text = text.replace(/^### (.*$)/gim, '<h4 class="font-display text-lg font-medium text-text mt-4 mb-2">$1</h4>');
  text = text.replace(/^## (.*$)/gim, '<h3 class="font-display text-xl font-medium text-text mt-5 mb-2.5">$1</h3>');

  // 3. Blockquotes
  text = text.replace(/^\> (.*$)/gim, '<blockquote class="border-l-2 border-accent/60 pl-4 py-1 italic font-serif text-text/85 my-3 bg-surface/30 rounded-r">$1</blockquote>');

  // 4. Bold and Italic
  text = text.replace(/\*\*\*(.*?)\*\*\*/gim, '<strong><em>$1</em></strong>');
  text = text.replace(/\*\*(.*?)\*\*/gim, '<strong class="font-semibold text-text">$1</strong>');
  text = text.replace(/\*(.*?)\*/gim, '<em class="italic">$1</em>');

  // 5. Inline Code
  text = text.replace(/`([^`]+)`/gim, '<code class="px-1.5 py-0.5 rounded bg-surface border border-border/60 font-mono text-xs text-accent">$1</code>');

  // 6. Safe Markdown Links: [label](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/gim, (match, label, url) => {
    const safeHref = sanitizeUrl(url);
    const isExternal = safeHref.startsWith('http');
    const targetAttrs = isExternal ? 'target="_blank" rel="noopener noreferrer nofollow ugc"' : '';
    return `<a href="${safeHref}" class="text-accent underline underline-offset-2 hover:opacity-80 transition-opacity" ${targetAttrs}>${label}</a>`;
  });

  // 7. Unordered Lists
  text = text.replace(/^\- (.*$)/gim, '<li class="ml-4 list-disc text-text/90">$1</li>');

  // 8. Paragraphs & Line Breaks
  const paragraphs = text.split(/\n\n+/);
  const formatted = paragraphs
    .map((p) => {
      const trimmed = p.trim();
      if (!trimmed) return '';
      if (
        trimmed.startsWith('<h') ||
        trimmed.startsWith('<blockquote') ||
        trimmed.startsWith('<li')
      ) {
        return trimmed;
      }
      return `<p class="leading-relaxed mb-3">${trimmed.replace(/\n/g, '<br />')}</p>`;
    })
    .join('\n');

  return formatted;
}

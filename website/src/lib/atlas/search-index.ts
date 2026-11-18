// website/src/lib/atlas/search-index.ts
// Client & server fast search index for The Atlas nodes

import type { AtlasNode } from './types';
import { getAllAtlasNodes } from './loader';

function normalizeSearchText(str: string): string {
  return str
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd')
    .trim();
}

export interface AtlasSearchResult {
  node: AtlasNode;
  score: number;
  matchField: string;
}

export function searchAtlasNodes(query: string, filterKind?: string, filterRegion?: string): AtlasSearchResult[] {
  if (!query || query.trim().length === 0) {
    let nodes = getAllAtlasNodes();
    if (filterKind) nodes = nodes.filter((n) => n.kind === filterKind);
    if (filterRegion) nodes = nodes.filter((n) => n.visual.region === filterRegion);
    return nodes.map((node) => ({ node, score: 1, matchField: 'all' }));
  }

  const normQuery = normalizeSearchText(query);
  const terms = normQuery.split(/\s+/).filter(Boolean);
  const nodes = getAllAtlasNodes();
  const results: AtlasSearchResult[] = [];

  for (const node of nodes) {
    if (filterKind && node.kind !== filterKind) continue;
    if (filterRegion && node.visual.region !== filterRegion) continue;

    const normLabel = normalizeSearchText(node.label);
    const normLabelEn = normalizeSearchText(node.label_en || '');
    const normSummary = normalizeSearchText(node.summary || '');
    const normTopics = node.topicCodes.map((t) => normalizeSearchText(t)).join(' ');

    let score = 0;
    let matchField = '';

    for (const term of terms) {
      if (normLabel.includes(term)) {
        score += 10;
        matchField = 'label';
      } else if (normLabelEn.includes(term)) {
        score += 8;
        matchField = 'label_en';
      } else if (normTopics.includes(term)) {
        score += 6;
        matchField = 'topic';
      } else if (normSummary.includes(term)) {
        score += 3;
        matchField = 'summary';
      }
    }

    if (score > 0) {
      results.push({ node, score, matchField });
    }
  }

  return results.sort((a, b) => b.score - a.score);
}

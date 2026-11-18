// website/src/lib/atlas/loader.ts
// Direct zero-I/O loader for The Atlas compiled graph

import type { AtlasGraphData, AtlasNode, AtlasEdge, AtlasRegion, AtlasTrail } from './types';
import atlasDataRaw from '../../data/atlas-graph.json';
import assetCatalogRaw from '../../data/asset-catalog.json';

const atlasGraph: AtlasGraphData = atlasDataRaw as AtlasGraphData;

export function getAtlasGraph(): AtlasGraphData {
  return atlasGraph;
}

export function getAllAtlasRegions(): AtlasRegion[] {
  return atlasGraph.regions;
}

export function getAtlasRegionById(id: string): AtlasRegion | undefined {
  return atlasGraph.regions.find((r) => r.id === id);
}

export function getAtlasRegionBySlug(slug: string): AtlasRegion | undefined {
  return atlasGraph.regions.find((r) => r.slug === slug);
}

export function getAllAtlasNodes(): AtlasNode[] {
  return atlasGraph.nodes;
}

export function getAtlasNodeById(id: string): AtlasNode | undefined {
  return atlasGraph.nodes.find((n) => n.id === id);
}

export function getAtlasNodeBySlug(slug: string): AtlasNode | undefined {
  return atlasGraph.nodes.find((n) => n.slug === slug);
}

export function getAllAtlasEdges(): AtlasEdge[] {
  return atlasGraph.edges;
}

export function getAllAtlasTrails(): AtlasTrail[] {
  return atlasGraph.trails;
}

export function getAtlasTrailById(id: string): AtlasTrail | undefined {
  return atlasGraph.trails.find((t) => t.id === id);
}

export function getAtlasTrailBySlug(slug: string): AtlasTrail | undefined {
  return atlasGraph.trails.find((t) => t.slug === slug);
}

// Artwork lookup from asset-catalog
export interface ArtworkMeta {
  id: string;
  title: string;
  artist: string;
  period: string;
  museum: string;
  sourceUrl?: string;
  license?: string;
  publicDomain: boolean;
  themeCode?: string;
  imageUrl?: string;
}

export function getArtworkMeta(artworkId: string | undefined | null): ArtworkMeta | null {
  if (!artworkId) return null;
  const catalog = assetCatalogRaw as Record<string, any>;
  const found = catalog[artworkId];
  if (!found) return null;
  return {
    id: artworkId,
    title: found.title || 'Kiệt Tác Cổ Điển',
    artist: found.artist || 'Danh họa Cổ điển',
    period: found.year || 'Thế kỷ XVII',
    museum: found.museum || 'Bảo tàng Nghệ thuật',
    sourceUrl: found.sourceUrl || found.slides?.slide_1,
    license: found.license || 'Public Domain / CC0',
    publicDomain: true,
    themeCode: artworkId,
    imageUrl: found.slides?.slide_1 || `/images/themes/${artworkId}/slide_1_establishing.jpg`,
  };
}

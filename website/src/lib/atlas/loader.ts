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
}

export function getArtworkMeta(artworkId: string | undefined | null): ArtworkMeta | null {
  if (!artworkId) return null;
  const list = (assetCatalogRaw as any).artworks || [];
  const found = list.find((a: any) => a.id === artworkId);
  if (!found) return null;
  return {
    id: found.id,
    title: found.title,
    artist: found.artist,
    period: found.period,
    museum: found.museum,
    sourceUrl: found.sourceUrl,
    license: found.license,
    publicDomain: Boolean(found.publicDomain),
    themeCode: found.themeCode,
  };
}

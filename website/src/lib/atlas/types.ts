// website/src/lib/atlas/types.ts
// Comprehensive TypeScript data contract for The Atlas V2.1

export type AtlasNodeKind = 'theme' | 'idea' | 'quote' | 'artwork' | 'thinker' | 'work';

export type AtlasRelationKind =
  | 'explores'
  | 'contrasts_with'
  | 'influenced_by'
  | 'illustrated_by'
  | 'reframes'
  | 'shares_question_with'
  | 'contextualized_by';

export type PublicationStatus = 'DRAFT' | 'REVIEWED' | 'PUBLISHED';

export interface AtlasRegion {
  id: string;
  slug: string;
  label: string;
  label_en: string;
  tagline: string;
  description: string;
  centerCoordinates: { x: number; y: number };
  colorToken: string;
  astronomyGlyph: string;
  dominantThemes: string[];
}

export interface AtlasNodeVisual {
  region: string;
  x: number; // 0 to 1000 scale coordinate on celestial plate
  y: number; // 0 to 1000 scale coordinate on celestial plate
  priority: number; // 1 to 10 visual hierarchy
  glyph?: string; // Cartographic or astrological symbol
  cartoucheStyle?: 'medallion' | 'monument' | 'cartouche' | 'plate';
}

export interface AtlasNode {
  id: string;
  kind: AtlasNodeKind;
  status: PublicationStatus;
  slug: string;
  label: string;
  label_en: string;
  summary: string;
  topicCodes: string[];
  relatedContentIds?: string[]; // IDs of Library TXT quotes
  artworkId?: string | null; // ID of artwork in asset-catalog.json
  sourceRefs?: Array<{
    title: string;
    author?: string;
    year?: string;
    url?: string;
  }>;
  curatorNote?: string;
  visual: AtlasNodeVisual;
}

export interface AtlasEdge {
  id: string;
  from: string; // AtlasNode ID
  to: string; // AtlasNode ID
  relation: AtlasRelationKind;
  why: string; // 1-3 sentences editorial explanation
  curatorNote?: string;
  evidenceRefs?: string[];
  status: PublicationStatus;
  weight: number; // 0.1 to 1.0 importance
}

export interface AtlasTrailStop {
  nodeId: string;
  chapterTitle?: string;
  chapterPrompt?: string;
}

export interface AtlasTrail {
  id: string;
  slug: string;
  title: string;
  title_en: string;
  subtitle: string;
  description: string;
  introPrompt: string;
  closingPrompt: string;
  themeCode: string;
  estimatedMinutes: number;
  coverArtworkId?: string;
  orderedNodeIds: string[];
  stops?: AtlasTrailStop[];
  status: PublicationStatus;
}

export interface AtlasGraphData {
  version: string;
  generatedAt: string;
  regions: AtlasRegion[];
  nodes: AtlasNode[];
  edges: AtlasEdge[];
  trails: AtlasTrail[];
}

export interface AtlasNeighbor {
  node: AtlasNode;
  edge: AtlasEdge;
  direction: 'outgoing' | 'incoming';
}

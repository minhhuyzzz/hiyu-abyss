// website/src/lib/atlas/graph-index.ts
// Graph traversal and relational analysis for The Atlas

import type { AtlasNode, AtlasEdge, AtlasTrail, AtlasRelationKind } from './types';
import { getAtlasGraph } from './loader';

export interface ConnectedNodeItem {
  node: AtlasNode;
  edge: AtlasEdge;
  direction: 'outbound' | 'inbound';
}

export function getRelationLabel(relation: AtlasRelationKind, lang: 'vi' | 'en' = 'vi'): string {
  const labels: Record<AtlasRelationKind, { vi: string; en: string }> = {
    explores: { vi: 'Khám phá / Khơi mở', en: 'Explores' },
    contrasts_with: { vi: 'Đối lập / Xung đột', en: 'Contrasts with' },
    influenced_by: { vi: 'Chịu ảnh hưởng bởi', en: 'Influenced by' },
    illustrated_by: { vi: 'Minh họa mỹ thuật', en: 'Illustrated by' },
    reframes: { vi: 'Đặt lại góc nhìn', en: 'Reframes' },
    shares_question_with: { vi: 'Cùng câu hỏi bản thể', en: 'Shares question with' },
    contextualized_by: { vi: 'Đặt trong bối cảnh', en: 'Contextualized by' },
  };
  return labels[relation]?.[lang] || relation;
}

export function getNodeNeighbors(nodeId: string): ConnectedNodeItem[] {
  const graph = getAtlasGraph();
  const nodeMap = new Map(graph.nodes.map((n) => [n.id, n]));
  const results: ConnectedNodeItem[] = [];

  for (const edge of graph.edges) {
    if (edge.from === nodeId) {
      const target = nodeMap.get(edge.to);
      if (target) {
        results.push({
          node: target,
          edge,
          direction: 'outbound',
        });
      }
    } else if (edge.to === nodeId) {
      const source = nodeMap.get(edge.from);
      if (source) {
        results.push({
          node: source,
          edge,
          direction: 'inbound',
        });
      }
    }
  }

  return results;
}

export function getTrailsForNode(nodeId: string): AtlasTrail[] {
  const graph = getAtlasGraph();
  return graph.trails.filter((t) => t.orderedNodeIds.includes(nodeId));
}

export function getNodesByRegion(regionId: string): AtlasNode[] {
  const graph = getAtlasGraph();
  return graph.nodes.filter((n) => n.visual.region === regionId);
}

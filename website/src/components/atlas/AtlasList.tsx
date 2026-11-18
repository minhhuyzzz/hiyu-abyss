// website/src/components/atlas/AtlasList.tsx
import React, { useState } from 'react';
import type { AtlasNode, AtlasRegion } from '../../lib/atlas/types';
import { getNodeNeighbors } from '../../lib/atlas/graph-index';
import { Compass, Sparkles, BookOpen, User, Image as ImageIcon, ArrowRight } from 'lucide-react';

interface Props {
  nodes: AtlasNode[];
  regions: AtlasRegion[];
  onSelectNode: (nodeId: string) => void;
  focusedNodeId: string | null;
  selectedRegion: string | null;
  filterKind: string | null;
}

export const AtlasList: React.FC<Props> = ({
  nodes,
  regions,
  onSelectNode,
  focusedNodeId,
  selectedRegion,
  filterKind,
}) => {
  const [activeTab, setActiveTab] = useState<'by-region' | 'alphabetical'>('by-region');

  // Filter nodes
  const filteredNodes = nodes.filter((n) => {
    if (selectedRegion && n.visual.region !== selectedRegion) return false;
    if (filterKind && n.kind !== filterKind) return false;
    return true;
  });

  const getKindIcon = (kind: string) => {
    switch (kind) {
      case 'theme':
        return <Compass className="w-3.5 h-3.5 text-accent" />;
      case 'thinker':
        return <User className="w-3.5 h-3.5 text-oxide" />;
      case 'artwork':
        return <ImageIcon className="w-3.5 h-3.5 text-patina" />;
      case 'quote':
        return <BookOpen className="w-3.5 h-3.5 text-accent" />;
      default:
        return <Sparkles className="w-3.5 h-3.5 text-accent" />;
    }
  };

  const getKindBadge = (kind: string) => {
    switch (kind) {
      case 'theme':
        return 'Chủ Đề';
      case 'thinker':
        return 'Triết Gia';
      case 'artwork':
        return 'Kiệt Tác';
      case 'quote':
        return 'Trích Ngôn';
      default:
        return 'Ý Tưởng';
    }
  };

  return (
    <div className="w-full max-w-6xl mx-auto px-4 py-8 animate-fade-in space-y-8">
      {/* Top Banner & Mode */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-border pb-6">
        <div>
          <span className="font-mono text-xs uppercase tracking-widest text-accent">
            Danh Mục Toàn Thư · 86 Điểm Tọa Độ
          </span>
          <h2 className="font-display text-2xl sm:text-3xl font-medium text-text mt-1">
            Mục Lục Toàn Bộ Tư Tưởng
          </h2>
          <p className="font-serif text-sm text-muted mt-1 max-w-xl">
            Tra cứu trực quan toàn bộ các ý tưởng, trường phái triết học, tác giả kinh điển và kiệt tác hội họa trong đồ thị The Atlas.
          </p>
        </div>

        {/* Group Tab */}
        <div className="flex items-center gap-1 border border-border bg-bg p-1 rounded-sm text-xs font-sans">
          <button
            onClick={() => setActiveTab('by-region')}
            className={`px-3 py-1.5 rounded-xs transition-colors ${
              activeTab === 'by-region'
                ? 'bg-accent text-on-accent font-semibold'
                : 'text-muted hover:text-text'
            }`}
          >
            Theo Miền Tư Tưởng
          </button>
          <button
            onClick={() => setActiveTab('alphabetical')}
            className={`px-3 py-1.5 rounded-xs transition-colors ${
              activeTab === 'alphabetical'
                ? 'bg-accent text-on-accent font-semibold'
                : 'text-muted hover:text-text'
            }`}
          >
            Thứ Tự Bảng Chữ Cái
          </button>
        </div>
      </div>

      {/* Content Rendering */}
      {activeTab === 'by-region' ? (
        <div className="space-y-12">
          {regions
            .filter((r) => !selectedRegion || r.id === selectedRegion)
            .map((region) => {
              const regionNodes = filteredNodes.filter((n) => n.visual.region === region.id);
              if (regionNodes.length === 0) return null;

              return (
                <div key={region.id} className="space-y-4">
                  {/* Region Header */}
                  <div className="flex items-center gap-3 border-b border-border/70 pb-3">
                    <span className="text-xl text-accent font-serif">{region.astronomyGlyph}</span>
                    <div>
                      <h3 className="font-display text-xl text-text font-medium">
                        {region.label}
                      </h3>
                      <p className="font-sans text-xs text-muted mt-0.5">
                        {region.tagline}
                      </p>
                    </div>
                    <span className="ml-auto font-mono text-xs text-muted bg-surface-raised px-2 py-0.5 rounded border border-border">
                      {regionNodes.length} tọa độ
                    </span>
                  </div>

                  {/* Nodes Grid */}
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                    {regionNodes.map((node) => {
                      const neighbors = getNodeNeighbors(node.id);
                      const isFocused = node.id === focusedNodeId;

                      return (
                        <div
                          key={node.id}
                          onClick={() => onSelectNode(node.id)}
                          className={`p-4 rounded-sm border cursor-pointer transition-all flex flex-col justify-between group ${
                            isFocused
                              ? 'bg-surface-raised border-accent ring-1 ring-accent'
                              : 'bg-surface/50 hover:bg-surface border-border hover:border-accent/40'
                          }`}
                        >
                          <div>
                            <div className="flex items-center justify-between gap-2 mb-2">
                              <span className="text-[10px] font-mono uppercase tracking-wider px-1.5 py-0.5 rounded bg-bg text-muted border border-border flex items-center gap-1">
                                {getKindIcon(node.kind)}
                                <span>{getKindBadge(node.kind)}</span>
                              </span>
                              <span className="text-[11px] font-mono text-muted/70">
                                {neighbors.length} liên kết
                              </span>
                            </div>

                            <h4 className="font-serif font-medium text-base text-text group-hover:text-accent transition-colors line-clamp-1">
                              {node.label}
                            </h4>
                            {node.label_en && (
                              <p className="font-serif italic text-xs text-muted mb-2 truncate">
                                {node.label_en}
                              </p>
                            )}

                            <p className="font-sans text-xs text-muted/90 line-clamp-2 leading-relaxed">
                              {node.summary}
                            </p>
                          </div>

                          <div className="mt-3 pt-3 border-t border-border/50 flex items-center justify-between text-xs text-accent">
                            <span className="font-mono text-[11px]">Xem Folio</span>
                            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              );
            })}
        </div>
      ) : (
        /* Alphabetical View */
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          {[...filteredNodes]
            .sort((a, b) => a.label.localeCompare(b.label, 'vi'))
            .map((node) => {
              const neighbors = getNodeNeighbors(node.id);
              const isFocused = node.id === focusedNodeId;

              return (
                <div
                  key={node.id}
                  onClick={() => onSelectNode(node.id)}
                  className={`p-4 rounded-sm border cursor-pointer transition-all flex flex-col justify-between group ${
                    isFocused
                      ? 'bg-surface-raised border-accent ring-1 ring-accent'
                      : 'bg-surface/50 hover:bg-surface border-border hover:border-accent/40'
                  }`}
                >
                  <div>
                    <div className="flex items-center justify-between gap-2 mb-2">
                      <span className="text-[10px] font-mono uppercase tracking-wider px-1.5 py-0.5 rounded bg-bg text-muted border border-border flex items-center gap-1">
                        {getKindIcon(node.kind)}
                        <span>{getKindBadge(node.kind)}</span>
                      </span>
                      <span className="text-[11px] font-mono text-muted/70">
                        {neighbors.length} liên kết
                      </span>
                    </div>

                    <h4 className="font-serif font-medium text-base text-text group-hover:text-accent transition-colors line-clamp-1">
                      {node.label}
                    </h4>

                    <p className="font-sans text-xs text-muted/90 line-clamp-2 leading-relaxed mt-2">
                      {node.summary}
                    </p>
                  </div>

                  <div className="mt-3 pt-3 border-t border-border/50 flex items-center justify-between text-xs text-accent">
                    <span className="font-mono text-[11px]">Khám phá</span>
                    <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                  </div>
                </div>
              );
            })}
        </div>
      )}
    </div>
  );
};

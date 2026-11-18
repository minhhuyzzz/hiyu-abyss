// website/src/components/atlas/AtlasToolbar.tsx
import React from 'react';
import {
  Search,
  Compass,
  Map,
  List,
  ZoomIn,
  ZoomOut,
  RotateCcw,
  Layers,
  Sparkles,
} from 'lucide-react';
import type { AtlasRegion, AtlasTrail } from '../../lib/atlas/types';

interface Props {
  regions: AtlasRegion[];
  trails: AtlasTrail[];
  selectedRegion: string | null;
  onSelectRegion: (regionId: string | null) => void;
  filterKind: string | null;
  onSelectFilterKind: (kind: string | null) => void;
  viewMode: 'map' | 'list';
  onToggleViewMode: (mode: 'map' | 'list') => void;
  onOpenSearch: () => void;
  onZoomIn: () => void;
  onZoomOut: () => void;
  onResetZoom: () => void;
  onStartTrail: (trailId: string) => void;
}

export const AtlasToolbar: React.FC<Props> = ({
  regions,
  trails,
  selectedRegion,
  onSelectRegion,
  filterKind,
  onSelectFilterKind,
  viewMode,
  onToggleViewMode,
  onOpenSearch,
  onZoomIn,
  onZoomOut,
  onResetZoom,
  onStartTrail,
}) => {
  return (
    <div className="w-full bg-surface/80 backdrop-blur-md border-b border-border/80 px-3 sm:px-4 py-2 sm:py-2.5 flex items-center justify-between gap-2 sm:gap-3 text-xs font-sans overflow-x-auto no-scrollbar">
      {/* Left: Search Trigger & View Switcher */}
      <div className="flex items-center gap-2">
        <button
          onClick={onOpenSearch}
          className="flex items-center gap-2 px-3 py-1.5 rounded-sm bg-bg hover:bg-surface-raised border border-border text-muted hover:text-text transition-colors shadow-xs"
          title="Tìm kiếm tư tưởng (⌘K)"
        >
          <Search className="w-3.5 h-3.5" />
          <span className="hidden sm:inline">Tìm kiếm tư tưởng...</span>
          <kbd className="hidden md:inline-block px-1.5 py-0.2 text-[10px] font-mono text-muted/80 bg-surface border border-border rounded">
            ⌘K
          </kbd>
        </button>

        {/* View Switcher: Map vs List */}
        <div className="flex items-center border border-border rounded-sm overflow-hidden bg-bg p-0.5">
          <button
            onClick={() => onToggleViewMode('map')}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-xs transition-colors ${
              viewMode === 'map'
                ? 'bg-accent text-on-accent font-medium shadow-xs'
                : 'text-muted hover:text-text'
            }`}
          >
            <Map className="w-3.5 h-3.5" />
            <span className="hidden xs:inline">Bản Đồ</span>
          </button>
          <button
            onClick={() => onToggleViewMode('list')}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-xs transition-colors ${
              viewMode === 'list'
                ? 'bg-accent text-on-accent font-medium shadow-xs'
                : 'text-muted hover:text-text'
            }`}
          >
            <List className="w-3.5 h-3.5" />
            <span className="hidden xs:inline">Mục Lục</span>
          </button>
        </div>
      </div>

      {/* Center: Curated Trails Selector */}
      <div className="flex items-center gap-2">
        <div className="relative flex items-center">
          <span className="hidden lg:inline text-muted mr-1.5 font-mono text-[11px] uppercase tracking-wider">
            Tuyến gợi ý:
          </span>
          <select
            onChange={(e) => {
              if (e.target.value) onStartTrail(e.target.value);
            }}
            defaultValue=""
            className="bg-bg text-text border border-border rounded-sm px-2 sm:px-2.5 py-1.5 text-xs font-serif focus:outline-none focus:border-accent cursor-pointer max-w-[150px] sm:max-w-xs truncate"
          >
            <option value="" disabled>
              ✦ Tuyến Thám Hiểm Giám Tuyển...
            </option>
            {trails.map((t) => (
              <option key={t.id} value={t.id}>
                {t.title} ({t.orderedNodeIds.length} chặng · {t.estimatedMinutes}p)
              </option>
            ))}
          </select>
        </div>

        {/* Region Selector */}
        <select
          value={selectedRegion || ''}
          onChange={(e) => onSelectRegion(e.target.value || null)}
          className="hidden sm:inline-block bg-bg text-text border border-border rounded-sm px-2.5 py-1.5 text-xs font-serif focus:outline-none focus:border-accent cursor-pointer"
        >
          <option value="">Toàn bộ 8 Miền Tư Tưởng</option>
          {regions.map((r) => (
            <option key={r.id} value={r.id}>
              {r.astronomyGlyph} {r.label}
            </option>
          ))}
        </select>
      </div>

      {/* Right: Kind Filters & Zoom Instruments */}
      <div className="flex items-center gap-1.5 ml-auto">
        {/* Kind Filters */}
        <div className="hidden xl:flex items-center gap-1">
          {[
            { id: null, label: 'Tất cả' },
            { id: 'idea', label: 'Ý tưởng' },
            { id: 'thinker', label: 'Triết gia' },
            { id: 'theme', label: 'Chủ đề' },
            { id: 'artwork', label: 'Kiệt tác' },
            { id: 'quote', label: 'Trích ngôn' },
          ].map((item) => (
            <button
              key={item.id ?? 'all'}
              onClick={() => onSelectFilterKind(item.id)}
              className={`px-2 py-1 rounded-sm text-[11px] transition-colors border ${
                filterKind === item.id
                  ? 'bg-surface-raised border-accent text-accent font-medium'
                  : 'bg-bg/60 border-border text-muted hover:text-text'
              }`}
            >
              {item.label}
            </button>
          ))}
        </div>

        {/* Zoom Controls (only in map view) */}
        {viewMode === 'map' && (
          <div className="flex items-center border border-border rounded-sm bg-bg p-0.5 ml-1">
            <button
              onClick={onZoomIn}
              className="p-1 text-muted hover:text-text hover:bg-surface rounded-xs transition-colors"
              title="Phóng to (+) · Hoặc giữ Ctrl + cuộn chuột / kẹp 2 ngón"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={onZoomOut}
              className="p-1 text-muted hover:text-text hover:bg-surface rounded-xs transition-colors"
              title="Thu nhỏ (-) · Hoặc giữ Ctrl + cuộn chuột / kẹp 2 ngón"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={onResetZoom}
              className="p-1 text-muted hover:text-text hover:bg-surface rounded-xs transition-colors"
              title="Đặt lại góc nhìn (0)"
            >
              <RotateCcw className="w-3.5 h-3.5" />
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

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
    <div className="w-full px-3 sm:px-6 pointer-events-none z-20 shrink-0 mb-1.5 sm:mb-2">
      <div className="max-w-4xl mx-auto pointer-events-auto rounded-full border border-border/80 bg-surface/90 backdrop-blur-md shadow-xl px-2.5 sm:px-4 py-1.5 flex items-center justify-between gap-1.5 sm:gap-2.5 text-xs font-sans overflow-x-auto no-scrollbar">
        {/* Left: Search Trigger & View Switcher */}
        <div className="flex items-center gap-1.5 shrink-0">
          <button
            onClick={onOpenSearch}
            className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-bg hover:bg-surface-raised border border-border text-muted hover:text-text transition-colors shadow-xs"
            title="Tìm kiếm tư tưởng (⌘K)"
          >
            <Search className="w-3.5 h-3.5 text-accent" />
            <span className="hidden sm:inline">Tìm kiếm...</span>
            <kbd className="hidden md:inline-block px-1.5 py-0.2 text-[9px] font-mono text-muted/80 bg-surface border border-border rounded">
              ⌘K
            </kbd>
          </button>

          {/* View Switcher: Map vs List */}
          <div className="flex items-center border border-border rounded-full overflow-hidden bg-bg p-0.5">
            <button
              onClick={() => onToggleViewMode('map')}
              className={`flex items-center gap-1 px-2 sm:px-2.5 py-0.5 rounded-full transition-colors ${
                viewMode === 'map'
                  ? 'bg-accent text-on-accent font-medium shadow-xs'
                  : 'text-muted hover:text-text'
              }`}
            >
              <Map className="w-3 h-3" />
              <span className="hidden xs:inline text-[11px]">Bản Đồ</span>
            </button>
            <button
              onClick={() => onToggleViewMode('list')}
              className={`flex items-center gap-1 px-2 sm:px-2.5 py-0.5 rounded-full transition-colors ${
                viewMode === 'list'
                  ? 'bg-accent text-on-accent font-medium shadow-xs'
                  : 'text-muted hover:text-text'
              }`}
            >
              <List className="w-3 h-3" />
              <span className="hidden xs:inline text-[11px]">Mục Lục</span>
            </button>
          </div>
        </div>

        {/* Center: Curated Trails & Regions Selector */}
        <div className="flex items-center gap-1.5 shrink-0">
          {/* Curated Trails Selector */}
          <select
            onChange={(e) => {
              if (e.target.value) onStartTrail(e.target.value);
            }}
            defaultValue=""
            className="bg-bg text-text border border-border rounded-full px-2.5 py-1 text-xs font-serif focus:outline-none focus:border-accent cursor-pointer max-w-[130px] sm:max-w-[190px] truncate"
            title="Tuyến thám hiểm giám tuyển"
          >
            <option value="" disabled>
              ✦ Tuyến gợi ý...
            </option>
            {trails.map((t) => (
              <option key={t.id} value={t.id}>
                {t.title} ({t.orderedNodeIds.length} chặng)
              </option>
            ))}
          </select>

          {/* Region Selector */}
          <select
            value={selectedRegion || ''}
            onChange={(e) => onSelectRegion(e.target.value || null)}
            className="bg-bg text-text border border-border rounded-full px-2 sm:px-2.5 py-1 text-xs font-serif focus:outline-none focus:border-accent cursor-pointer max-w-[120px] sm:max-w-[160px] truncate"
            title="Lọc theo miền tư tưởng"
          >
            <option value="">Toàn bộ 8 Miền</option>
            {regions.map((r) => (
              <option key={r.id} value={r.id}>
                {r.astronomyGlyph} {r.label}
              </option>
            ))}
          </select>

          {/* Compact Kind Filter Dropdown */}
          <select
            value={filterKind || ''}
            onChange={(e) => onSelectFilterKind(e.target.value || null)}
            className="hidden md:inline-block bg-bg text-text border border-border rounded-full px-2 sm:px-2.5 py-1 text-xs font-serif focus:outline-none focus:border-accent cursor-pointer max-w-[110px]"
            title="Lọc theo loại thực thể"
          >
            <option value="">Tất cả loại</option>
            <option value="idea">✦ Ý tưởng</option>
            <option value="thinker">☿ Triết gia</option>
            <option value="theme">☉ Chủ đề</option>
            <option value="artwork">❖ Kiệt tác</option>
            <option value="quote">❧ Trích ngôn</option>
          </select>
        </div>

        {/* Right: Zoom Instruments (Map View) */}
        {viewMode === 'map' && (
          <div className="flex items-center border border-border rounded-full bg-bg p-0.5 shrink-0">
            <button
              onClick={onZoomIn}
              className="w-6 h-6 rounded-full flex items-center justify-center text-muted hover:text-text hover:bg-surface-raised transition-colors"
              title="Phóng to (+) · Hoặc giữ Ctrl + cuộn chuột / kẹp 2 ngón"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={onZoomOut}
              className="w-6 h-6 rounded-full flex items-center justify-center text-muted hover:text-text hover:bg-surface-raised transition-colors"
              title="Thu nhỏ (-) · Hoặc giữ Ctrl + cuộn chuột / kẹp 2 ngón"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={onResetZoom}
              className="w-6 h-6 rounded-full flex items-center justify-center text-muted hover:text-text hover:bg-surface-raised transition-colors"
              title="Đặt lại góc nhìn (0)"
            >
              <RotateCcw className="w-3 h-3" />
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

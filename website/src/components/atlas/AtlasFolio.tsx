// website/src/components/atlas/AtlasFolio.tsx
import React from 'react';
import {
  X,
  Bookmark,
  BookmarkCheck,
  Compass,
  ArrowRight,
  BookOpen,
  MessageSquare,
  Sparkles,
  User,
  Image as ImageIcon,
  Share2,
} from 'lucide-react';
import type { AtlasNode, AtlasEdge } from '../../lib/atlas/types';
import { getRelationLabel, getNodeNeighbors } from '../../lib/atlas/graph-index';
import { getArtworkMeta, getAtlasRegionById } from '../../lib/atlas/loader';

interface Props {
  node: AtlasNode | null;
  isOpen: boolean;
  onClose: () => void;
  onSelectNode: (nodeId: string) => void;
  isBookmarked: boolean;
  onToggleBookmark: (nodeId: string) => void;
}

export const AtlasFolio: React.FC<Props> = ({
  node,
  isOpen,
  onClose,
  onSelectNode,
  isBookmarked,
  onToggleBookmark,
}) => {
  if (!node || !isOpen) return null;

  const neighbors = getNodeNeighbors(node.id);
  const region = getAtlasRegionById(node.visual.region);
  const artworkMeta = getArtworkMeta(node.artworkId);

  const getKindBadge = (kind: string) => {
    switch (kind) {
      case 'theme':
        return 'Chủ Đề Cốt Lõi';
      case 'thinker':
        return 'Triết Gia / Tác Giả';
      case 'artwork':
        return 'Kiệt Tác Bảo Tàng';
      case 'quote':
        return 'Hồ Sơ Trích Ngôn';
      default:
        return 'Ý Tưởng Triết Học';
    }
  };

  // Find artwork image path
  const getArtworkSrc = () => {
    if (!artworkMeta) return null;
    return `/images/themes/${artworkMeta.id}/slide_1_establishing.jpg`;
  };

  const handleShare = () => {
    if (navigator.share) {
      navigator.share({
        title: `${node.label} · The Atlas`,
        text: node.summary,
        url: window.location.href,
      }).catch(() => {});
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('Đã sao chép liên kết vào bộ nhớ tạm.');
    }
  };

  return (
    <>
      {/* Backdrop for mobile */}
      <div
        className="fixed inset-0 bg-black/60 z-[55] sm:hidden backdrop-blur-xs transition-opacity"
        onClick={onClose}
      />

      <aside
        className={`fixed z-[60] transition-all duration-300 ease-out flex flex-col bg-surface/98 backdrop-blur-xl border-border shadow-2xl
        /* Mobile: Bottom Sheet sliding up with max-h-[88vh] and rounded top */
        inset-x-0 bottom-0 max-h-[88vh] rounded-t-2xl border-t sm:rounded-none sm:border-t-0 sm:inset-x-auto
        /* Desktop: Slide-in Drawer from right */
        sm:right-0 sm:top-0 sm:bottom-0 sm:w-[460px] lg:w-[480px] sm:border-l ${
          isOpen
            ? 'translate-y-0 sm:translate-y-0 sm:translate-x-0'
            : 'translate-y-full sm:translate-y-0 sm:translate-x-full'
        }`}
        aria-label="Folio Chi Tiết Tư Tưởng"
      >
        {/* Mobile Pull Handle */}
        <div className="w-full pt-2.5 pb-1 flex justify-center sm:hidden shrink-0">
          <div className="w-10 h-1 bg-muted/40 rounded-full" />
        </div>

        {/* Folio Top Bar */}
        <div className="flex items-center justify-between px-4 sm:px-5 py-3 sm:py-4 border-b border-border/80 bg-surface-raised/50 shrink-0 gap-2">
          <div className="flex items-center gap-1.5 sm:gap-2 min-w-0">
            <span className="font-mono text-[9px] sm:text-[10px] tracking-widest uppercase px-1.5 sm:px-2 py-0.5 rounded bg-bg text-accent border border-accent/30 shrink-0">
              {getKindBadge(node.kind)}
            </span>
            {region && (
              <span className="font-serif text-xs text-muted/90 hidden xs:flex items-center gap-1 truncate">
                <span>{region.astronomyGlyph}</span>
                <span className="truncate">{region.label}</span>
              </span>
            )}
          </div>

          <div className="flex items-center gap-1 shrink-0">
            <button
              onClick={() => onToggleBookmark(node.id)}
              className={`p-2 rounded-sm border transition-colors ${
                isBookmarked
                  ? 'bg-accent/15 border-accent text-accent'
                  : 'bg-bg border-border text-muted hover:text-text'
              }`}
              title={isBookmarked ? 'Bỏ lưu trữ' : 'Lưu vào kho tư tưởng'}
            >
              {isBookmarked ? <BookmarkCheck className="w-4 h-4" /> : <Bookmark className="w-4 h-4" />}
            </button>
            <button
              onClick={handleShare}
              className="p-2 rounded-sm bg-bg border border-border text-muted hover:text-text transition-colors"
              title="Chia sẻ liên kết"
            >
              <Share2 className="w-4 h-4" />
            </button>
            <button
              onClick={onClose}
              className="p-2 rounded-sm bg-bg border border-border text-muted hover:text-text transition-colors"
              title="Đóng Folio"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Scrollable Folio Body */}
        <div className="flex-1 overflow-y-auto px-6 py-6 space-y-6">
          {/* Header Title */}
          <div>
            <h2 className="font-display text-2xl sm:text-3xl font-medium text-text tracking-tight leading-snug">
              {node.label}
            </h2>
            {node.label_en && (
              <p className="font-serif italic text-sm text-muted mt-1">
                {node.label_en}
              </p>
            )}
          </div>

          {/* Museum Artwork Placard (If linked to artwork) */}
          {artworkMeta && (
            <div className="border border-border/90 bg-bg p-3.5 rounded-sm space-y-2.5 shadow-sm">
              <div className="aspect-16/10 overflow-hidden rounded-xs bg-surface relative group">
                <img
                  src={getArtworkSrc() || ''}
                  alt={artworkMeta.title}
                  className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                  onError={(e) => {
                    (e.target as HTMLElement).style.display = 'none';
                  }}
                />
                <div className="absolute inset-0 ring-1 ring-inset ring-white/10 pointer-events-none" />
              </div>
              <div className="pt-1">
                <div className="flex items-center justify-between text-[11px] text-muted font-mono">
                  <span className="uppercase tracking-widest">Kiệt Tác Hội Họa</span>
                  <span>{artworkMeta.publicDomain ? 'Public Domain' : 'Museum Archive'}</span>
                </div>
                <h4 className="font-serif font-medium text-sm text-text mt-0.5">
                  {artworkMeta.title}
                </h4>
                <p className="font-sans text-xs text-muted">
                  {artworkMeta.artist} ({artworkMeta.period}) · {artworkMeta.museum}
                </p>
              </div>
            </div>
          )}

          {/* Editorial Summary */}
          <div className="border-l-2 border-accent/40 pl-4 py-1">
            <p className="font-serif text-base text-text leading-relaxed font-normal">
              "{node.summary}"
            </p>
          </div>

          {/* Curator Note / Note from Hiyu Abyss */}
          {node.curatorNote && (
            <div className="p-3.5 rounded-sm bg-surface-raised/70 border border-border/80">
              <div className="flex items-center gap-2 mb-1.5 text-accent text-xs font-mono uppercase tracking-wider">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Ghi Chép Giám Tuyển</span>
              </div>
              <p className="font-sans text-xs text-muted/90 leading-relaxed">
                {node.curatorNote}
              </p>
            </div>
          )}

          {/* Curated Relational Connections ("Vì sao liên quan?") */}
          <div className="space-y-3 pt-2">
            <div className="flex items-center justify-between border-b border-border pb-2">
              <h3 className="font-mono text-xs uppercase tracking-widest text-text font-semibold flex items-center gap-2">
                <Compass className="w-3.5 h-3.5 text-accent" />
                <span>Mối Liên Hệ Giám Tuyển ({neighbors.length})</span>
              </h3>
              <span className="text-[11px] font-mono text-muted">Tương tác</span>
            </div>

            {neighbors.length === 0 ? (
              <p className="text-xs text-muted italic font-serif">
                Chưa có liên kết phụ cận được ghi nhận.
              </p>
            ) : (
              <div className="space-y-2.5">
                {neighbors.map(({ node: targetNode, edge, direction }) => (
                  <div
                    key={edge.id}
                    onClick={() => onSelectNode(targetNode.id)}
                    className="p-3 rounded-sm bg-surface-raised/40 hover:bg-surface-raised border border-border/70 hover:border-accent/40 cursor-pointer transition-all group"
                  >
                    <div className="flex items-center justify-between gap-2 mb-1">
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-bg text-accent border border-accent/20">
                        {getRelationLabel(edge.relation)}
                      </span>
                      <ArrowRight className="w-3.5 h-3.5 text-muted group-hover:text-accent group-hover:translate-x-0.5 transition-all" />
                    </div>
                    <h5 className="font-serif font-medium text-sm text-text group-hover:text-accent transition-colors">
                      {targetNode.label}
                    </h5>
                    <p className="font-sans text-xs text-muted mt-1 leading-normal">
                      {edge.why}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Folio Bottom Action Hub */}
        <div className="p-4 border-t border-border bg-surface-raised/60 shrink-0 space-y-2">
          {/* Deep link to Library if quote or relatedContent exists */}
          {node.relatedContentIds && node.relatedContentIds.length > 0 && (
            <a
              href={`/library/${node.relatedContentIds[0].toLowerCase()}`}
              className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-sm bg-accent text-on-accent font-sans text-xs uppercase tracking-wider font-semibold hover:brightness-110 transition-all shadow-sm"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Đọc Trọn Bài Tại Thư Viện</span>
            </a>
          )}

          {/* Deep link to Agora Dialogue */}
          <a
            href={`/agora/new?topic=${encodeURIComponent(node.label)}`}
            className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-sm bg-bg hover:bg-surface border border-border text-text font-sans text-xs uppercase tracking-wider font-medium transition-all"
          >
            <MessageSquare className="w-3.5 h-3.5 text-muted" />
            <span>Mở Cuộc Đối Thoại Tại Agora</span>
          </a>
        </div>
      </aside>
    </>
  );
};

// website/src/components/atlas/AtlasFolio.tsx
// Renaissance Museum Folio & Illuminated Codex Sheet
import React, { useState } from 'react';
import {
  X,
  Bookmark,
  BookmarkCheck,
  Compass,
  ArrowRight,
  BookOpen,
  MessageSquare,
  Sparkles,
  Share2,
  Scroll,
  Eye,
  Info,
} from 'lucide-react';
import type { AtlasNode } from '../../lib/atlas/types';
import { getRelationLabel, getNodeNeighbors } from '../../lib/atlas/graph-index';
import { getArtworkMeta, getAtlasRegionById } from '../../lib/atlas/loader';

interface Props {
  node: AtlasNode | null;
  isOpen: boolean;
  onClose: () => void;
  onSelectNode: (nodeId: string) => void;
  isBookmarked: boolean;
  onToggleBookmark: (nodeId: string) => void;
  threadStep?: number;
}

// Fallback regional masterpieces guaranteeing every node displays a classical artwork
const REGION_MASTERPIECES: Record<string, string> = {
  'region-nature': 'theme_01', // Caravaggio: Narcissus
  'region-ego': 'theme_05', // Caravaggio: Medusa
  'region-freedom': 'theme_02', // Rembrandt: Aristotle
  'region-solitude': 'theme_03', // Caspar David Friedrich: Wanderer
  'region-power': 'theme_04', // William-Adolphe Bouguereau: Dante & Virgil
  'region-suffering': 'theme_06', // Rembrandt: Storm on Sea of Galilee
  'region-mask': 'theme_07', // Johannes Vermeer: The Astronomer
  'region-transcendence': 'theme_08', // Raphael: School of Athens
};

export const AtlasFolio: React.FC<Props> = ({
  node,
  isOpen,
  onClose,
  onSelectNode,
  isBookmarked,
  onToggleBookmark,
  threadStep = 0,
}) => {
  if (!node || !isOpen) return null;

  const [activeTab, setActiveTab] = useState<'folio' | 'artwork' | 'sources'>('folio');
  const neighbors = getNodeNeighbors(node.id);
  const region = getAtlasRegionById(node.visual.region);

  // Resolve artwork: explicit artworkId or regional masterpiece fallback
  const effectiveArtworkId = node.artworkId || REGION_MASTERPIECES[node.visual.region] || 'theme_01';
  const artworkMeta = getArtworkMeta(effectiveArtworkId);
  const artworkSrc = artworkMeta?.imageUrl || `/images/themes/${effectiveArtworkId}/slide_1_establishing.jpg`;

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

  const handleShare = () => {
    if (navigator.share) {
      navigator.share({
        title: `${node.label} · The Atlas`,
        text: node.summary,
        url: window.location.href,
      }).catch(() => {});
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('Đã sao chép liên kết hồ sơ The Atlas vào bộ nhớ tạm.');
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
        /* Mobile: Bottom Sheet sliding up with max-h-[90vh] and rounded top */
        inset-x-0 bottom-0 max-h-[90vh] rounded-t-2xl border-t sm:rounded-none sm:border-t-0 sm:inset-x-auto
        /* Desktop: Slide-in Drawer from right */
        sm:right-0 sm:top-0 sm:bottom-0 sm:w-[480px] lg:w-[520px] sm:border-l ${
          isOpen
            ? 'translate-y-0 sm:translate-y-0 sm:translate-x-0'
            : 'translate-y-full sm:translate-y-0 sm:translate-x-full'
        }`}
        aria-label="Folio Khảo Cứu Tư Tưởng"
      >
        {/* Mobile Pull Handle */}
        <div className="w-full pt-2.5 pb-1 flex justify-center sm:hidden shrink-0">
          <div className="w-10 h-1 bg-muted/40 rounded-full" />
        </div>

        {/* Illuminated Codex Header Bar */}
        <div className="px-4 sm:px-6 py-3 sm:py-3.5 border-b border-border/80 bg-surface-raised/60 shrink-0">
          <div className="flex items-center justify-between gap-2">
            <div className="flex items-center gap-2 min-w-0">
              <span className="font-mono text-[9px] sm:text-[10px] tracking-widest uppercase px-2 py-0.5 rounded bg-bg text-accent border border-accent/30 shrink-0">
                {getKindBadge(node.kind)}
              </span>
              {region && (
                <span className="font-serif text-xs text-muted/90 flex items-center gap-1 truncate">
                  <span className="text-accent">{region.astronomyGlyph}</span>
                  <span className="truncate">{region.latinName || region.label}</span>
                </span>
              )}
            </div>

            <div className="flex items-center gap-1.5 shrink-0">
              {threadStep > 0 && (
                <span
                  className="font-mono text-[9px] uppercase tracking-wider px-2 py-0.5 rounded bg-[#B47862]/20 border border-[#B47862]/40 text-[#B47862] font-semibold"
                  title="Thứ tự khám phá trong hành trình cá nhân của bạn"
                >
                  ✦ Chặng {threadStep}
                </span>
              )}

              <button
                onClick={() => onToggleBookmark(node.id)}
                className={`p-1.5 sm:p-2 rounded-sm border transition-colors ${
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
                className="p-1.5 sm:p-2 rounded-sm bg-bg border border-border text-muted hover:text-text transition-colors"
                title="Chia sẻ liên kết"
              >
                <Share2 className="w-4 h-4" />
              </button>
              <button
                onClick={onClose}
                className="p-1.5 sm:p-2 rounded-sm bg-bg border border-border text-muted hover:text-text transition-colors"
                title="Đóng Folio"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Sub-header inscription */}
          <div className="flex items-center justify-between text-[10px] font-mono text-muted/70 pt-1 tracking-wider uppercase border-t border-border/40 mt-2">
            <span>FOLIO CODEX ABYSSI · TABULA PICTA</span>
            <span>ID: {node.id.toUpperCase()}</span>
          </div>
        </div>

        {/* Scrollable Folio Body */}
        <div className="flex-1 overflow-y-auto px-5 sm:px-6 py-5 space-y-6">
          {/* Header Title with Editorial Typography */}
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

          {/* Renaissance Museum Artwork Arch & Placard */}
          {artworkMeta && (
            <div className="border border-border/90 bg-bg p-3.5 rounded-sm space-y-3 shadow-md relative overflow-hidden">
              {/* Renaissance decorative corner flourishes */}
              <div className="absolute top-1 left-1 text-accent/30 text-[10px] select-none pointer-events-none">⌜</div>
              <div className="absolute top-1 right-1 text-accent/30 text-[10px] select-none pointer-events-none">⌝</div>
              <div className="absolute bottom-1 left-1 text-accent/30 text-[10px] select-none pointer-events-none">⌞</div>
              <div className="absolute bottom-1 right-1 text-accent/30 text-[10px] select-none pointer-events-none">⌟</div>

              {/* Classical Oil Painting Frame */}
              <div className="aspect-16/9 max-h-[170px] sm:max-h-[210px] overflow-hidden rounded-xs bg-surface relative group border border-border/60">
                <img
                  src={artworkSrc}
                  alt={artworkMeta.title}
                  className="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                  onError={(e) => {
                    // Fallback to theme_01 if specific file failed
                    (e.target as HTMLImageElement).src = '/images/themes/theme_01/slide_1_establishing.jpg';
                  }}
                />
                <div className="absolute inset-0 ring-1 ring-inset ring-white/10 pointer-events-none" />
                <div className="absolute bottom-2 right-2 px-2 py-0.5 bg-black/75 backdrop-blur-xs rounded text-[9px] font-mono text-white/90 border border-white/10 uppercase tracking-widest pointer-events-none">
                  {artworkMeta.publicDomain ? 'CC0 · Public Domain' : 'Museum Archive'}
                </div>
              </div>

              {/* Museum Provenance Placard */}
              <div className="pt-0.5 border-t border-border/60">
                <div className="flex items-center justify-between text-[10px] text-accent font-mono uppercase tracking-widest mb-1">
                  <span>✦ HIỆN VẬT HỘI HỌA LIÊN HỆ</span>
                  <span>{artworkMeta.period}</span>
                </div>
                <h4 className="font-serif font-medium text-base text-text leading-tight">
                  {artworkMeta.title}
                </h4>
                <p className="font-sans text-xs text-muted mt-1 leading-normal">
                  {artworkMeta.artist} · <span className="italic">{artworkMeta.museum}</span>
                </p>
              </div>
            </div>
          )}

          {/* Editorial Philosophical Summary (Illuminated Drop-Quote) */}
          <div className="border-l-2 border-accent/60 pl-4 py-1 bg-surface-raised/30 rounded-r-sm">
            <p className="font-serif text-base sm:text-[17px] text-text leading-relaxed font-normal">
              "{node.summary}"
            </p>
          </div>

          {/* Curator Note / Ghi Chép Giám Tuyển Hiyu Abyss */}
          {node.curatorNote && (
            <div className="p-4 rounded-sm bg-surface-raised/70 border border-border/80 relative">
              <div className="flex items-center gap-2 mb-2 text-accent text-xs font-mono uppercase tracking-wider">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Ghi Chép Giám Tuyển · Phản Tư Triết Học</span>
              </div>
              <p className="font-sans text-xs text-muted/90 leading-relaxed">
                {node.curatorNote}
              </p>
            </div>
          )}

          {/* Curated Relational Connections ("Vì sao liên quan?") */}
          <div className="space-y-3 pt-1">
            <div className="flex items-center justify-between border-b border-border pb-2">
              <h3 className="font-mono text-xs uppercase tracking-widest text-text font-semibold flex items-center gap-2">
                <Compass className="w-3.5 h-3.5 text-accent" />
                <span>Mối Liên Hệ Giám Tuyển ({neighbors.length})</span>
              </h3>
              <span className="text-[10px] font-mono text-muted uppercase">Nhấp để lần theo</span>
            </div>

            {neighbors.length === 0 ? (
              <p className="text-xs text-muted italic font-serif">
                Chưa có liên kết phụ cận được ghi nhận trong ấn bản này.
              </p>
            ) : (
              <div className="space-y-2.5">
                {neighbors.map(({ node: targetNode, edge }) => (
                  <div
                    key={edge.id}
                    onClick={() => onSelectNode(targetNode.id)}
                    className="p-3 rounded-sm bg-surface-raised/40 hover:bg-surface-raised border border-border/70 hover:border-accent/40 cursor-pointer transition-all group"
                  >
                    <div className="flex items-center justify-between gap-2 mb-1.5">
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-bg text-accent border border-accent/20">
                        {getRelationLabel(edge.relation)}
                      </span>
                      <div className="flex items-center gap-1 text-[11px] font-mono text-muted group-hover:text-accent transition-colors">
                        <span>Lần theo tư tưởng</span>
                        <ArrowRight className="w-3 h-3 group-hover:translate-x-0.5 transition-transform" />
                      </div>
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

          {/* Provenance & Philosophical Grounding (Nguồn khảo cứu & Văn bản đối chiếu) */}
          <div className="p-3.5 rounded-sm border border-border/60 bg-bg/60 space-y-2">
            <div className="flex items-center gap-1.5 text-xs font-mono uppercase tracking-wider text-muted">
              <Scroll className="w-3.5 h-3.5 text-accent" />
              <span>Nguồn Khảo Cứu & Chuẩn Đối Chiếu (HYA-02)</span>
            </div>
            <p className="font-sans text-xs text-muted leading-relaxed">
              Các mệnh đề và mối liên hệ trong hồ sơ này được đối chiếu với nguyên bản triết học, tác phẩm văn học kinh điển và kiệt tác hội họa bảo tàng thuộc phạm vi lưu trữ độc lập của Hiyu Abyss.
            </p>
          </div>
        </div>

        {/* Folio Bottom Action Hub */}
        <div className="p-4 border-t border-border bg-surface-raised/70 shrink-0 space-y-2">
          {/* Deep link to Library if quote or relatedContent exists */}
          {node.relatedContentIds && node.relatedContentIds.length > 0 && (
            <a
              href={`/library/${node.relatedContentIds[0].toLowerCase()}`}
              className="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-sm bg-accent text-on-accent font-sans text-xs uppercase tracking-wider font-semibold hover:brightness-110 transition-all shadow-sm"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Đọc Trọn Bản Khảo Cứu Tại Thư Viện</span>
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

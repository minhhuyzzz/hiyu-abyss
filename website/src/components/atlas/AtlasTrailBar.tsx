// website/src/components/atlas/AtlasTrailBar.tsx
import React from 'react';
import { ChevronLeft, ChevronRight, X, Compass, Sparkles } from 'lucide-react';
import type { AtlasTrail, AtlasNode } from '../../lib/atlas/types';

interface Props {
  trail: AtlasTrail;
  currentStopIndex: number;
  currentNode: AtlasNode | null;
  onNextStop: () => void;
  onPrevStop: () => void;
  onCloseTrail: () => void;
}

export const AtlasTrailBar: React.FC<Props> = ({
  trail,
  currentStopIndex,
  currentNode,
  onNextStop,
  onPrevStop,
  onCloseTrail,
}) => {
  const totalStops = trail.orderedNodeIds.length;
  const progressPercent = Math.round(((currentStopIndex + 1) / totalStops) * 100);

  return (
    <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-30 w-[94%] max-w-2xl bg-surface/90 backdrop-blur-xl border border-accent/40 shadow-2xl rounded-sm p-4 animate-slide-up">
      {/* Progress Track */}
      <div className="w-full bg-border h-1 rounded-full overflow-hidden mb-3">
        <div
          className="bg-accent h-full transition-all duration-300"
          style={{ width: `${progressPercent}%` }}
        />
      </div>

      <div className="flex items-center justify-between gap-4">
        {/* Left: Trail Info */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            <span className="font-mono text-[10px] uppercase tracking-widest text-accent flex items-center gap-1">
              <Compass className="w-3 h-3" />
              <span>Tuyến Khám Phá: {trail.title}</span>
            </span>
            <span className="text-[10px] font-mono text-muted">
              ({currentStopIndex + 1}/{totalStops})
            </span>
          </div>

          <h4 className="font-serif text-base sm:text-lg font-medium text-text truncate">
            {currentNode ? currentNode.label : 'Đang tải chặng...'}
          </h4>

          {trail.introPrompt && (
            <p className="text-xs text-muted/90 font-serif italic line-clamp-1 mt-0.5">
              "{trail.introPrompt}"
            </p>
          )}
        </div>

        {/* Right: Navigation Controls */}
        <div className="flex items-center gap-2 shrink-0">
          <button
            onClick={onPrevStop}
            disabled={currentStopIndex === 0}
            className="p-2 rounded-sm border border-border bg-bg hover:bg-surface text-text disabled:opacity-40 disabled:pointer-events-none transition-colors"
            title="Chặng trước"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          <button
            onClick={onNextStop}
            disabled={currentStopIndex >= totalStops - 1}
            className="flex items-center gap-1.5 px-3 py-2 rounded-sm bg-accent text-on-accent font-sans text-xs uppercase tracking-wider font-semibold hover:brightness-110 disabled:opacity-40 disabled:pointer-events-none transition-all shadow-sm"
            title="Chặng tiếp theo"
          >
            <span>Tiếp Tục</span>
            <ChevronRight className="w-4 h-4" />
          </button>
          <button
            onClick={onCloseTrail}
            className="p-2 rounded-sm border border-border bg-bg hover:bg-surface text-muted hover:text-text transition-colors"
            title="Thoát tuyến khám phá"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};

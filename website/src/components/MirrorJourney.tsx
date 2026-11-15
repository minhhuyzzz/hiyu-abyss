import React, { useState, useEffect, useRef } from 'react';
import type { MirrorJourneyData, SceneNode, SceneChoice } from '../lib/types';

interface Props {
  journey: MirrorJourneyData;
}

interface HistoryStep {
  nodeId: string;
  choiceId?: string;
  choiceIdx?: number;
  nodeTitle: string;
}

// 5 Room Archetypes for Scene Renderer (HYA-P1)
type RoomArchetype = 'threshold' | 'observation' | 'silence' | 'confrontation' | 'ending';

function getRoomArchetype(nodeId: string, node: SceneNode): RoomArchetype {
  if (node.type === 'intro' || nodeId === 'threshold') return 'threshold';
  if (node.type === 'ending') return 'ending';
  if (node.type === 'counterpoint') return 'confrontation';
  if (nodeId.includes('peace') || node.scenePreset === 'paper-chamber' || node.scenePreset === 'veil') return 'silence';
  if (nodeId.includes('truth') || node.scenePreset === 'stone-archive') return 'observation';
  return 'observation';
}

export default function MirrorJourney({ journey }: Props) {
  const isSceneGraph = Boolean(journey.nodes && Object.keys(journey.nodes).length > 0);
  const entryId = journey.entry || 'threshold';

  const [currentNodeId, setCurrentNodeId] = useState<string>(entryId);
  const [history, setHistory] = useState<HistoryStep[]>([]);
  const [hoveredChoice, setHoveredChoice] = useState<string | null>(null);
  const [copiedToast, setCopiedToast] = useState(false);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const [lastDirection, setLastDirection] = useState<'left' | 'right' | 'forward'>('forward');

  const containerRef = useRef<HTMLDivElement>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);

  const currentNode: SceneNode | undefined = journey.nodes?.[currentNodeId];
  const roomArchetype: RoomArchetype = currentNode ? getRoomArchetype(currentNodeId, currentNode) : 'threshold';

  // Preload next step images for instantaneous transitions
  useEffect(() => {
    if (!currentNode || !journey.nodes) return;
    const targets: string[] = [];
    if (currentNode.next) targets.push(currentNode.next);
    if (currentNode.choices) {
      currentNode.choices.forEach((c) => targets.push(c.to));
    }
    targets.forEach((targetId) => {
      const targetNode = journey.nodes?.[targetId];
      if (targetNode?.artwork_ref) {
        const img = new Image();
        img.src = targetNode.artwork_ref;
      }
    });
  }, [currentNodeId, currentNode, journey.nodes]);

  // Handle navigating forward to next node with directional transition
  const handleProceed = (targetNodeId: string, choiceId?: string, choiceIdx?: number) => {
    if (!journey.nodes?.[targetNodeId] || isTransitioning) return;

    const dir = choiceIdx === 0 ? 'left' : choiceIdx === 1 ? 'right' : 'forward';
    setLastDirection(dir);
    setIsTransitioning(true);

    setTimeout(() => {
      setHistory((prev) => [
        ...prev,
        {
          nodeId: currentNodeId,
          choiceId,
          choiceIdx,
          nodeTitle: currentNode?.title || currentNodeId,
        },
      ]);
      setCurrentNodeId(targetNodeId);
      setIsTransitioning(false);

      // Smoothly refocus on content heading
      if (headingRef.current) {
        headingRef.current.focus();
      } else if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 280);
  };

  // Handle Back
  const handleBack = () => {
    if (history.length === 0 || isTransitioning) return;
    setIsTransitioning(true);

    setTimeout(() => {
      const previous = history[history.length - 1];
      setHistory((prev) => prev.slice(0, prev.length - 1));
      setCurrentNodeId(previous.nodeId);
      setIsTransitioning(false);

      if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 200);
  };

  // Handle Restart
  const handleRestart = () => {
    setIsTransitioning(true);
    setTimeout(() => {
      setHistory([]);
      setCurrentNodeId(entryId);
      setIsTransitioning(false);
      if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 250);
  };

  // Handle Exit
  const handleExit = () => {
    window.location.href = '/mirror';
  };

  // Keyboard navigation (1, 2, Enter, Backspace/Esc) - safely guarded
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!currentNode || isTransitioning) return;

      // Do not capture keys if user is typing in an input/textarea
      const targetTag = (e.target as HTMLElement)?.tagName;
      if (targetTag === 'INPUT' || targetTag === 'TEXTAREA') return;

      if (e.key === 'Escape' || (e.key === 'Backspace' && targetTag !== 'BUTTON')) {
        if (history.length > 0) {
          e.preventDefault();
          handleBack();
        }
      }

      if (currentNode.type === 'choice' && currentNode.choices) {
        if (e.key === '1' && currentNode.choices[0]) {
          e.preventDefault();
          handleProceed(currentNode.choices[0].to, currentNode.choices[0].id, 0);
        } else if (e.key === '2' && currentNode.choices[1]) {
          e.preventDefault();
          handleProceed(currentNode.choices[1].to, currentNode.choices[1].id, 1);
        }
      } else if (currentNode.next) {
        if (e.key === 'Enter') {
          e.preventDefault();
          handleProceed(currentNode.next);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentNodeId, history, currentNode, isTransitioning]);

  const copyRefToClipboard = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedToast(true);
    setTimeout(() => setCopiedToast(false), 2500);
  };

  if (!isSceneGraph || !currentNode) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center text-muted font-sans">
        <p>Hành trình này đang được chuẩn hóa theo kiến trúc Scene Graph V3.</p>
        <button
          onClick={handleExit}
          className="mt-6 px-6 py-2.5 border border-border rounded text-xs uppercase tracking-widest text-text hover:text-accent transition-colors"
        >
          Quay lại danh mục
        </button>
      </div>
    );
  }

  const artImage = currentNode.artwork_ref || journey.artwork_url || '/images/themes/theme_11/slide_1_establishing.jpg';
  const isEnding = currentNode.type === 'ending';
  const pathDepth = history.length + 1;

  // Scene-specific styling and visual atmosphere classes
  const archetypeBadges = {
    threshold: '01 / MỞ CỔNG CHIÊM NGHIỆM',
    observation: '02 / PHÒNG QUAN SÁT SỰ THẬT',
    silence: '02 / PHÒNG IM LẶNG TĨNH TÂM',
    confrontation: '03 / PHẢN ĐỀ TỰ SOI CHIẾU',
    ending: '04 / BẢN ĐÚC KẾT MỞ',
  };

  const archetypeSubnotes = {
    threshold: 'Khởi đầu tĩnh lặng trước cánh cửa của điều chưa biết.',
    observation: 'Nơi sự thật được soi tỏ dưới ánh sáng khách quan và phân tích tâm lý.',
    silence: 'Nơi tiếng ồn xung quanh lùi xa, nhường chỗ cho sự hiện diện chân thật.',
    confrontation: 'Đặt giả định ban đầu vào vùng nghi vấn để bóc tách động cơ ngầm.',
    ending: 'Không có điểm kết luận đóng lại — chỉ có câu hỏi bạn mang theo vào đời sống.',
  };

  // Directional translation classes for motion
  const transitionClass = isTransitioning
    ? 'opacity-0 scale-[0.985] filter blur-[1px]'
    : 'opacity-100 scale-100 filter blur-0';

  return (
    <div
      ref={containerRef}
      className="relative w-full max-w-4xl mx-auto px-4 sm:px-6 py-6 sm:py-12 transition-all duration-300"
      aria-live="polite"
    >
      {/* 1. Header Bar: Stage Depth, Room Indicator & Controls */}
      <div className="flex items-center justify-between pb-6 mb-8 sm:mb-12 border-b border-border/70 font-sans text-xs">
        {/* Breadcrumb Tracker */}
        <div className="flex items-center gap-2 text-muted">
          <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
          <span className="uppercase tracking-[0.2em] font-semibold text-accent font-mono text-[11px]">
            The Mirror
          </span>
          <span className="text-border">·</span>
          <span className="tracking-wider">Chặng {pathDepth}</span>
          {isEnding && (
            <span className="text-accent font-semibold ml-1 uppercase text-[10px] tracking-wider">
              (Bản Kết Mở)
            </span>
          )}
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-4">
          {history.length > 0 && (
            <button
              onClick={handleBack}
              type="button"
              className="text-muted hover:text-text tracking-wider uppercase flex items-center gap-1.5 transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
              aria-label="Quay lại bước trước"
            >
              <span>←</span>
              <span className="hidden sm:inline">Quay lại</span>
            </button>
          )}

          <button
            onClick={handleRestart}
            type="button"
            className="text-muted hover:text-text tracking-wider uppercase transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
            aria-label="Bắt đầu lại hành trình"
          >
            Bắt đầu lại
          </button>

          <button
            onClick={handleExit}
            type="button"
            className="text-muted hover:text-accent tracking-wider uppercase transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
            aria-label="Rời khỏi buồng chiêm nghiệm"
          >
            Thoát ✕
          </button>
        </div>
      </div>

      {/* 2. Main Scene Dynamic Presentation (Transition Director Container) */}
      <div
        className={`flex flex-col gap-8 sm:gap-10 transition-all duration-300 ease-out ${transitionClass}`}
      >
        {/* Dynamic Artwork Chamber Frame with Archetype Lighting */}
        {artImage && (
          <div
            className={`relative aspect-[16/9] sm:aspect-[21/9] w-full overflow-hidden bg-surface border shadow-2xl transition-all duration-700 ${
              roomArchetype === 'silence'
                ? 'border-border/60 filter brightness-[0.82] contrast-[0.98]'
                : roomArchetype === 'confrontation'
                ? 'border-accent/40 filter brightness-[0.9] contrast-[1.15]'
                : roomArchetype === 'ending'
                ? 'border-accent/60 filter brightness-[0.95] contrast-[1.05]'
                : 'border-border/80 filter brightness-[0.88] contrast-[1.05]'
            }`}
          >
            <img
              src={artImage}
              alt={currentNode.title}
              className={`w-full h-full object-cover transition-transform duration-1000 ${
                roomArchetype === 'observation'
                  ? 'scale-105'
                  : roomArchetype === 'confrontation'
                  ? 'scale-110'
                  : 'scale-100'
              }`}
              loading="eager"
            />
            {/* Atmospheric Vignette Overlay */}
            <div
              className={`absolute inset-0 transition-opacity duration-700 ${
                roomArchetype === 'silence'
                  ? 'bg-gradient-to-t from-bg via-bg/40 to-transparent'
                  : roomArchetype === 'confrontation'
                  ? 'bg-gradient-to-t from-bg via-bg/25 to-black/30'
                  : 'bg-gradient-to-t from-bg via-bg/30 to-transparent'
              }`}
            />
            <div className="absolute bottom-4 left-6 right-6 flex items-center justify-between text-[11px] font-sans tracking-widest uppercase text-text/80">
              <span className="truncate">
                {journey.artwork_title} · {journey.artwork_artist}
              </span>
              <span className="hidden sm:inline text-accent font-mono text-[10px]">
                {roomArchetype.toUpperCase()} CHAMBER
              </span>
            </div>
          </div>
        )}

        {/* Scene Narrative Content Block */}
        <div className="space-y-6 max-w-3xl mx-auto w-full">
          {/* Badge & Archetype Note */}
          <div className="space-y-2">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[11px] font-sans tracking-[0.25em] uppercase text-accent font-semibold block">
                {archetypeBadges[roomArchetype]}
              </span>
              <span className="text-border">·</span>
              <span className="text-[11px] font-serif italic text-muted">
                {archetypeSubnotes[roomArchetype]}
              </span>
            </div>

            <h1
              ref={headingRef}
              tabIndex={-1}
              className="font-display text-2xl sm:text-4xl md:text-5xl text-text font-medium leading-[1.2] text-balance focus:outline-none"
            >
              {currentNode.title}
            </h1>
          </div>

          {/* Scene Body Prose */}
          {currentNode.body && (
            <div className="prose-reading pt-2">
              <p className="font-serif text-lg sm:text-2xl text-text/90 italic leading-relaxed sm:leading-loose pl-5 border-l-2 border-accent/40">
                "{currentNode.body}"
              </p>
            </div>
          )}

          {/* TYPE 1: SEQUENTIAL ADVANCE (Intro / Statement / Counterpoint) */}
          {currentNode.next && (
            <div className="pt-8 border-t border-border/60 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <span className="text-[11px] font-sans text-muted tracking-wider">
                Nhấn <kbd className="px-1.5 py-0.5 bg-surface border border-border rounded text-[10px] font-mono">Enter</kbd> hoặc bấm nút để tiến bước
              </span>

              <button
                onClick={() => handleProceed(currentNode.next!)}
                type="button"
                className="px-8 py-3.5 bg-accent text-on-accent font-sans text-xs tracking-[0.2em] uppercase font-bold hover:opacity-90 transition-opacity min-h-[48px] inline-flex items-center justify-center gap-2 shadow-sm"
              >
                <span>{currentNode.type === 'intro' ? 'Bước Qua Ngưỡng Cửa' : 'Tiếp Tục Chiêm Nghiệm'}</span>
                <span>→</span>
              </button>
            </div>
          )}

          {/* TYPE 2: BRANCHING CHOICE DOORS (Left / Right Decision) */}
          {currentNode.type === 'choice' && currentNode.choices && (
            <div className="pt-8 border-t border-border/60 space-y-4">
              <div className="flex items-center justify-between text-xs font-sans text-muted">
                <span className="tracking-wider uppercase">
                  Chọn một hướng rẽ để mở tiếp đối thoại:
                </span>
                <span className="hidden sm:inline font-mono text-[11px]">
                  Dùng phím số [1] hoặc [2]
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1">
                {currentNode.choices.map((choice, idx) => (
                  <button
                    key={choice.id}
                    onClick={() => handleProceed(choice.to, choice.id, idx)}
                    onMouseEnter={() => setHoveredChoice(choice.id)}
                    onMouseLeave={() => setHoveredChoice(null)}
                    type="button"
                    className="p-6 text-left border border-border/80 hover:border-accent bg-surface/40 hover:bg-surface transition-all duration-300 flex flex-col justify-between gap-4 group min-h-[150px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
                  >
                    <div className="flex items-center justify-between text-xs font-sans text-muted">
                      <span className="w-6 h-6 border border-border/80 rounded flex items-center justify-center font-semibold text-accent group-hover:border-accent font-mono text-xs">
                        {idx + 1}
                      </span>
                      <span className="text-[10px] uppercase tracking-widest text-muted/70 group-hover:text-accent font-mono">
                        Cánh cửa {idx === 0 ? 'I' : 'II'}
                      </span>
                    </div>

                    <p className="font-serif text-base sm:text-lg text-text font-medium leading-snug group-hover:text-accent transition-colors">
                      {choice.label}
                    </p>

                    {choice.editorialIntent && (
                      <span className="font-sans text-[11px] text-muted italic border-t border-border/40 pt-2 block">
                        {choice.editorialIntent}
                      </span>
                    )}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* TYPE 3: ENDING (Terminal Open Station with Pathways Forward) */}
          {isEnding && (
            <div className="pt-8 border-t border-border/70 space-y-8">
              {/* Closing Monumental Question */}
              {currentNode.closingQuestion && (
                <div className="p-6 sm:p-8 bg-surface/60 border-l-2 border-accent space-y-3 shadow-sm">
                  <span className="text-[11px] font-sans tracking-[0.25em] uppercase text-accent font-semibold block font-mono">
                    Câu hỏi mang theo bên mình:
                  </span>
                  <p className="font-serif text-xl sm:text-2xl text-text italic leading-relaxed sm:leading-loose">
                    "{currentNode.closingQuestion}"
                  </p>
                </div>
              )}

              {/* Action Toolbar: Copy / Restart / Path to Library */}
              <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 pt-4 border-t border-border/40">
                <div className="flex items-center gap-3">
                  <button
                    onClick={() =>
                      copyRefToClipboard(
                        `Hiyu Abyss — The Mirror: "${currentNode.closingQuestion || currentNode.body}"`
                      )
                    }
                    type="button"
                    className="px-5 py-2.5 border border-border bg-surface text-text hover:border-accent hover:text-accent text-xs font-sans uppercase tracking-widest font-semibold transition-colors flex items-center gap-2 min-h-[44px]"
                  >
                    <span>{copiedToast ? 'Đã sao chép câu tự vấn ✓' : 'Lưu câu tự vấn'}</span>
                  </button>

                  <button
                    onClick={handleRestart}
                    type="button"
                    className="px-5 py-2.5 border border-border bg-surface text-text hover:border-accent hover:text-accent text-xs font-sans uppercase tracking-widest font-semibold transition-colors min-h-[44px]"
                  >
                    Khám phá nhánh khác ↺
                  </button>
                </div>

                <a
                  href={
                    currentNode.relatedTopic
                      ? `/themes/${currentNode.relatedTopic.toLowerCase().replace(/_/g, '-')}`
                      : '/library'
                  }
                  className="px-6 py-2.5 bg-accent text-on-accent text-xs font-sans uppercase tracking-widest font-bold hover:opacity-90 transition-opacity text-center flex items-center justify-center gap-1.5 min-h-[44px]"
                >
                  <span>Khám phá chủ đề liên quan</span>
                  <span>→</span>
                </a>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

import React, { useState, useEffect, useRef } from 'react';
import type { MirrorJourneyData, SceneNode, SceneChoice } from '../lib/types';

interface Props {
  journey: MirrorJourneyData;
}

interface HistoryStep {
  nodeId: string;
  choiceId?: string;
  choiceIdx?: number;
  choiceLabel?: string;
  nodeTitle: string;
}

type RoomArchetype = 'threshold' | 'observation' | 'silence' | 'confrontation' | 'ending';

function getRoomArchetype(nodeId: string, node: SceneNode): RoomArchetype {
  if (node.type === 'intro' || nodeId === 'threshold') return 'threshold';
  if (node.type === 'ending') return 'ending';
  if (node.type === 'counterpoint') return 'confrontation';
  if (nodeId.includes('wait') || nodeId.includes('silence') || nodeId.includes('peace') || node.scenePreset?.includes('silence')) return 'silence';
  if (nodeId.includes('speak') || nodeId.includes('observation') || nodeId.includes('truth') || node.scenePreset?.includes('observation')) return 'observation';
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

  // Check if user prefers reduced motion
  const prefersReducedMotion = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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
  const handleProceed = (targetNodeId: string, choiceId?: string, choiceIdx?: number, choiceLabel?: string) => {
    if (!journey.nodes?.[targetNodeId] || isTransitioning) return;

    const dir = choiceIdx === 0 ? 'left' : choiceIdx === 1 ? 'right' : 'forward';
    setLastDirection(dir);

    const applyStateChange = () => {
      setHistory((prev) => [
        ...prev,
        {
          nodeId: currentNodeId,
          choiceId,
          choiceIdx,
          choiceLabel,
          nodeTitle: currentNode?.title || currentNodeId,
        },
      ]);
      setCurrentNodeId(targetNodeId);
      setIsTransitioning(false);

      if (headingRef.current) {
        headingRef.current.focus();
      } else if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };

    if (prefersReducedMotion) {
      applyStateChange();
    } else {
      setIsTransitioning(true);
      setTimeout(applyStateChange, 220);
    }
  };

  // Handle Back
  const handleBack = () => {
    if (history.length === 0 || isTransitioning) return;

    const applyBack = () => {
      const previous = history[history.length - 1];
      setHistory((prev) => prev.slice(0, prev.length - 1));
      setCurrentNodeId(previous.nodeId);
      setIsTransitioning(false);

      if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };

    if (prefersReducedMotion) {
      applyBack();
    } else {
      setIsTransitioning(true);
      setTimeout(applyBack, 180);
    }
  };

  // Handle Restart
  const handleRestart = () => {
    const applyRestart = () => {
      setHistory([]);
      setCurrentNodeId(entryId);
      setIsTransitioning(false);
      if (containerRef.current) {
        containerRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };

    if (prefersReducedMotion) {
      applyRestart();
    } else {
      setIsTransitioning(true);
      setTimeout(applyRestart, 200);
    }
  };

  // Handle Exit
  const handleExit = () => {
    window.location.href = '/mirror';
  };

  // Keyboard navigation (1, 2, Enter, Backspace/Esc) - safely guarded
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!currentNode || isTransitioning) return;

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
          handleProceed(currentNode.choices[0].to, currentNode.choices[0].id, 0, currentNode.choices[0].label);
        } else if (e.key === '2' && currentNode.choices[1]) {
          e.preventDefault();
          handleProceed(currentNode.choices[1].to, currentNode.choices[1].id, 1, currentNode.choices[1].label);
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
        <p>Hành trình này đang được tải...</p>
        <button
          onClick={handleExit}
          className="mt-6 px-6 py-2.5 border border-border rounded text-xs uppercase tracking-widest text-text hover:text-accent transition-colors"
        >
          Quay lại danh mục
        </button>
      </div>
    );
  }

  const artImage = currentNode.artwork_ref || journey.artwork_url || '/images/themes/theme_03/slide_1_establishing.jpg';
  const artTitle = currentNode.artwork_title || journey.artwork_title || 'Kẻ lãng du trên biển sương mù';
  const artArtist = currentNode.artwork_artist || journey.artwork_artist || 'Caspar David Friedrich (1818)';

  const isEnding = currentNode.type === 'ending';
  const totalPathSteps = 6;
  const currentStepNumber = Math.min(history.length + 1, totalPathSteps);

  // Scene Archetype UI Badges & Subnotes
  const archetypeBadges: Record<RoomArchetype, string> = {
    threshold: '01 / NGƯỠNG CỬA TÌNH HUỐNG',
    observation: '02 / PHÒNG QUAN SÁT & ĐỐI DIỆN',
    silence: '02 / PHÒNG IM LẶNG & BẢO VỆ',
    confrontation: '03 / PHẢN ĐỀ TỰ SOI CHIẾU',
    ending: '04 / BẢN ĐÚC KẾT & CÂU HỎI TỰ VẤN',
  };

  const archetypeSubnotes: Record<RoomArchetype, string> = {
    threshold: 'Khởi đầu trước một khúc mắc thực tế không có đáp án hoàn hảo.',
    observation: 'Bước vào cơn chấn động đầu tiên khi sự thật được mở lời.',
    silence: 'Khoảng lặng tạm thời giữ lại sự êm ấm nhưng mang theo nỗi chông chênh.',
    confrontation: 'Đặt lại câu hỏi cho động cơ sâu kín nhất của chính bạn.',
    ending: 'Không có điểm số hay phán xét — chỉ có điều bạn mang theo vào cuộc sống.',
  };

  // Directional translation classes for motion
  let motionTransform = '';
  if (isTransitioning && !prefersReducedMotion) {
    if (lastDirection === 'left') motionTransform = '-translate-x-3 opacity-0';
    else if (lastDirection === 'right') motionTransform = 'translate-x-3 opacity-0';
    else motionTransform = 'translate-y-2 opacity-0';
  } else {
    motionTransform = 'translate-x-0 translate-y-0 opacity-100';
  }

  // Filter choices made in this session
  const choicesMade = history.filter((h) => h.choiceLabel);

  return (
    <div
      ref={containerRef}
      className="relative w-full max-w-4xl mx-auto px-4 sm:px-6 py-4 sm:py-8 transition-all duration-300"
      aria-live="polite"
    >
      {/* 1. Header Bar: Stage Depth, Dynamic Rhythm Tracker & Controls */}
      <div className="flex items-center justify-between pb-5 mb-6 sm:mb-10 border-b border-border/70 font-sans text-xs">
        {/* Dynamic Rhythm Tracker: "Nhịp X / 6" */}
        <div className="flex items-center gap-2 text-muted">
          <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
          <span className="uppercase tracking-[0.2em] font-semibold text-accent font-mono text-[11px]">
            The Mirror
          </span>
          <span className="text-border">·</span>
          <span className="tracking-wider font-mono font-medium text-text/90">
            Nhịp {currentStepNumber} / {totalPathSteps}
          </span>
          {isEnding && (
            <span className="text-accent font-semibold ml-1 uppercase text-[10px] tracking-wider">
              (Bản Kết Mở)
            </span>
          )}
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-3 sm:gap-4">
          {history.length > 0 && (
            <button
              onClick={handleBack}
              type="button"
              className="text-muted hover:text-text tracking-wider uppercase flex items-center gap-1.5 transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent text-xs"
              aria-label="Quay lại bước trước"
            >
              <span>←</span>
              <span className="hidden sm:inline">Quay lại</span>
            </button>
          )}

          <button
            onClick={handleRestart}
            type="button"
            className="text-muted hover:text-text tracking-wider uppercase transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent text-xs"
            aria-label="Bắt đầu lại hành trình"
          >
            Bắt đầu lại
          </button>

          <button
            onClick={handleExit}
            type="button"
            className="text-muted hover:text-accent tracking-wider uppercase transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent text-xs"
            aria-label="Rời khỏi trải nghiệm"
          >
            Thoát ✕
          </button>
        </div>
      </div>

      {/* 2. Main Scene Presentation Container with Directional Fluid Motion */}
      <div className={`flex flex-col gap-6 sm:gap-8 transition-all duration-300 ease-out ${motionTransform}`}>
        
        {/* Dynamic Artwork Chamber Frame with Specific Lighting Atmosphere */}
        {artImage && (
          <div
            className={`relative aspect-[16/9] sm:aspect-[21/9] w-full overflow-hidden bg-surface border shadow-2xl transition-all duration-500 ${
              roomArchetype === 'silence'
                ? 'border-border/60 filter brightness-[0.88] contrast-[1.0]'
                : roomArchetype === 'confrontation'
                ? 'border-accent/40 filter brightness-[0.92] contrast-[1.12]'
                : roomArchetype === 'ending'
                ? 'border-accent/60 filter brightness-[0.96] contrast-[1.04]'
                : 'border-border/80 filter brightness-[0.9] contrast-[1.05]'
            }`}
          >
            <img
              src={artImage}
              alt={artTitle}
              className={`w-full h-full object-cover transition-transform duration-700 ${
                roomArchetype === 'observation'
                  ? 'scale-105'
                  : roomArchetype === 'confrontation'
                  ? 'scale-110'
                  : 'scale-100'
              }`}
              loading="eager"
            />
            {/* Atmospheric Gradient Overlay */}
            <div
              className={`absolute inset-0 transition-opacity duration-500 ${
                roomArchetype === 'silence'
                  ? 'bg-gradient-to-t from-bg via-bg/40 to-transparent'
                  : roomArchetype === 'confrontation'
                  ? 'bg-gradient-to-t from-bg via-bg/30 to-black/30'
                  : 'bg-gradient-to-t from-bg via-bg/35 to-transparent'
              }`}
            />
            
            {/* Artwork Placard Overlay */}
            <div className="absolute bottom-3 left-4 right-4 sm:bottom-4 sm:left-6 sm:right-6 flex items-center justify-between text-[11px] font-sans tracking-widest uppercase text-text/80">
              <span className="truncate drop-shadow-md">
                {artTitle} · <span className="font-serif italic lowercase">{artArtist}</span>
              </span>
              <span className="hidden sm:inline text-accent font-mono text-[10px] tracking-widest">
                {roomArchetype.toUpperCase()} STAGE
              </span>
            </div>
          </div>
        )}

        {/* Scene Narrative Content Block */}
        <div className="space-y-6 max-w-3xl mx-auto w-full">
          {/* Badge & Room Atmosphere Subnote */}
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
            <div className="pt-1">
              <p className="font-serif text-lg sm:text-2xl text-text/90 italic leading-relaxed sm:leading-loose pl-5 border-l-2 border-accent/40">
                "{currentNode.body}"
              </p>
            </div>
          )}

          {/* TYPE 1: SEQUENTIAL ADVANCE (Intro / Statement / Counterpoint) */}
          {currentNode.next && (
            <div className="pt-6 sm:pt-8 border-t border-border/60 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <span className="text-[11px] font-sans text-muted tracking-wider">
                Nhấn <kbd className="px-1.5 py-0.5 bg-surface border border-border rounded text-[10px] font-mono">Enter</kbd> hoặc bấm nút để tiếp tục
              </span>

              <button
                onClick={() => handleProceed(currentNode.next!)}
                type="button"
                className="px-8 py-3.5 bg-accent text-on-accent font-sans text-xs tracking-[0.2em] uppercase font-bold hover:opacity-90 transition-opacity min-h-[48px] inline-flex items-center justify-center gap-2 shadow-sm"
              >
                <span>{currentNode.type === 'intro' ? 'Bước Vào Lựa Chọn' : 'Tiếp Tục Chiêm Nghiệm'}</span>
                <span>→</span>
              </button>
            </div>
          )}

          {/* TYPE 2: BRANCHING CHOICE DOORS (Concrete Left / Right Action) */}
          {currentNode.type === 'choice' && currentNode.choices && (
            <div className="pt-6 sm:pt-8 border-t border-border/60 space-y-4">
              <div className="flex items-center justify-between text-xs font-sans text-muted">
                <span className="tracking-wider uppercase">
                  Chọn cách bạn sẽ hành động:
                </span>
                <span className="hidden sm:inline font-mono text-[11px]">
                  Dùng phím số [1] hoặc [2]
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1">
                {currentNode.choices.map((choice, idx) => (
                  <button
                    key={choice.id}
                    onClick={() => handleProceed(choice.to, choice.id, idx, choice.label)}
                    onMouseEnter={() => setHoveredChoice(choice.id)}
                    onMouseLeave={() => setHoveredChoice(null)}
                    type="button"
                    className="p-6 text-left border border-border/80 hover:border-accent bg-surface/40 hover:bg-surface transition-all duration-300 flex flex-col justify-between gap-4 group min-h-[160px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
                  >
                    <div className="flex items-center justify-between text-xs font-sans text-muted">
                      <span className="w-6 h-6 border border-border/80 rounded flex items-center justify-center font-semibold text-accent group-hover:border-accent font-mono text-xs">
                        {idx + 1}
                      </span>
                      <span className="text-[10px] uppercase tracking-widest text-muted/70 group-hover:text-accent font-mono">
                        Ngã rẽ {idx === 0 ? 'I' : 'II'}
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
            <div className="pt-6 sm:pt-8 border-t border-border/70 space-y-8">
              
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

              {/* Path Summary: Choices Made on this Journey */}
              {choicesMade.length > 0 && (
                <div className="p-5 bg-surface/40 border border-border/60 rounded-sm space-y-3 text-xs">
                  <span className="font-mono text-accent uppercase tracking-wider block font-semibold text-[11px]">
                    Dấu chân trên hành trình bạn vừa qua:
                  </span>
                  <ul className="space-y-2 text-muted">
                    {choicesMade.map((c, i) => (
                      <li key={i} className="flex items-start gap-2">
                        <span className="text-accent font-mono text-xs">↳</span>
                        <span>
                          <strong className="text-text/90">Lựa chọn {i + 1}:</strong> {c.choiceLabel}
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Action Toolbar: Copy / Restart / Path to Library */}
              <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4 pt-4 border-t border-border/40">
                <div className="flex flex-wrap items-center gap-3">
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

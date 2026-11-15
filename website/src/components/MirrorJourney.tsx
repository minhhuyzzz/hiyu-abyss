import React, { useState, useEffect, useRef } from 'react';
import type { MirrorJourneyData, SceneNode, SceneChoice } from '../lib/types';

interface Props {
  journey: MirrorJourneyData;
}

interface HistoryStep {
  nodeId: string;
  choiceId?: string;
  nodeTitle: string;
}

export default function MirrorJourney({ journey }: Props) {
  // Check if journey has V3 Scene Graph nodes
  const isSceneGraph = Boolean(journey.nodes && Object.keys(journey.nodes).length > 0);
  const entryId = journey.entry || 'threshold';

  const [currentNodeId, setCurrentNodeId] = useState<string>(entryId);
  const [history, setHistory] = useState<HistoryStep[]>([]);
  const [isLeaving, setIsLeaving] = useState(false);
  const transitionRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const headingRef = useRef<HTMLHeadingElement>(null);
  const hasNavigatedRef = useRef(false);
  const [copiedToast, setCopiedToast] = useState(false);
  const nodeContainerRef = useRef<HTMLDivElement>(null);

  const currentNode: SceneNode | undefined = journey.nodes?.[currentNodeId];

  // Focus the newly entered scene and respect reduced-motion preferences.
  useEffect(() => {
    if (!hasNavigatedRef.current) return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    nodeContainerRef.current?.scrollIntoView({
      behavior: reduceMotion ? 'instant' : 'smooth',
      block: 'start',
    });
    headingRef.current?.focus({ preventScroll: true });
  }, [currentNodeId]);

  useEffect(() => () => {
    if (transitionRef.current !== null) clearTimeout(transitionRef.current);
  }, []);

  // The YAML graph selects the next room; an exit/entrance transition tells that story.
  // No scores, personality inference or user answers are sent to a server.
  const handleProceed = (targetNodeId: string, choiceId?: string) => {
    if (isLeaving || !journey.nodes?.[targetNodeId]) return;
    const advance = () => {
      hasNavigatedRef.current = true;
      setHistory((prev) => [
        ...prev,
        { nodeId: currentNodeId, choiceId, nodeTitle: currentNode?.title || currentNodeId },
      ]);
      setCurrentNodeId(targetNodeId);
      setIsLeaving(false);
      transitionRef.current = null;
    };
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      advance();
    } else {
      setIsLeaving(true);
      transitionRef.current = setTimeout(advance, 220);
    }
  };

  // Back restores the actual traversed branch rather than a fixed five-step flow.
  const handleBack = () => {
    if (isLeaving || history.length === 0) return;
    const previous = history[history.length - 1];
    hasNavigatedRef.current = true;
    setHistory((prev) => prev.slice(0, prev.length - 1));
    setCurrentNodeId(previous.nodeId);
  };

  // Handle Restart
  const handleRestart = () => {
    if (transitionRef.current !== null) clearTimeout(transitionRef.current);
    transitionRef.current = null;
    hasNavigatedRef.current = true;
    setIsLeaving(false);
    setHistory([]);
    setCurrentNodeId(entryId);
  };

  // Handle Exit
  const handleExit = () => {
    window.location.href = '/mirror';
  };

  // Keyboard navigation for choices (1, 2, Enter, Backspace/Esc)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!currentNode || isLeaving || e.altKey || e.metaKey || e.ctrlKey || e.repeat) return;
      // Never hijack keyboard input from buttons, links, form fields or editable content.
      const target = e.target as HTMLElement | null;
      if (target?.closest('button, a, input, textarea, select, [contenteditable="true"]')) return;

      if (e.key === 'Escape' || e.key === 'Backspace') {
        if (history.length > 0) { e.preventDefault(); handleBack(); }
        return;
      }

      if (currentNode.type === 'choice' && currentNode.choices) {
        if (e.key === '1' && currentNode.choices[0]) {
          e.preventDefault();
          handleProceed(currentNode.choices[0].to, currentNode.choices[0].id);
        } else if (e.key === '2' && currentNode.choices[1]) {
          e.preventDefault();
          handleProceed(currentNode.choices[1].to, currentNode.choices[1].id);
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
  }, [currentNodeId, history, currentNode, isLeaving]);

  const copyRefToClipboard = async (text: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedToast(true);
      setTimeout(() => setCopiedToast(false), 2500);
    } catch {
      setCopiedToast(false);
    }
  };

  if (!isSceneGraph || !currentNode) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center text-muted font-sans">
        <p>Hành trình này đang được nâng cấp sang chuẩn Scene Graph V3.</p>
        <button
          onClick={handleExit}
          className="mt-6 px-6 py-2.5 border border-border rounded text-xs uppercase tracking-widest text-text hover:text-accent"
        >
          Quay lại danh mục
        </button>
      </div>
    );
  }

  const artImage = currentNode.artwork_ref || journey.artwork_url || '/images/themes/theme_11/slide_1_establishing.jpg';
  const isEnding = currentNode.type === 'ending';
  const pathDepth = history.length + 1;
  const scenePreset = currentNode.scenePreset || 'gallery-threshold';
  const motionPreset = currentNode.motionPreset || 'reveal-quiet';

  return (
    <div ref={nodeContainerRef} className="relative w-full max-w-4xl mx-auto px-4 sm:px-6 py-6 sm:py-12">
      
      {/* Top Navigation & Controls Bar */}
      <div className="flex items-center justify-between pb-6 mb-8 sm:mb-12 border-b border-border/70 font-sans text-xs">
        {/* Breadcrumb Tracker */}
        <div className="flex items-center gap-2 text-muted">
          <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
          <span className="uppercase tracking-[0.2em] font-semibold text-accent">The Mirror</span>
          <span className="text-border">·</span>
          <span className="tracking-wider">Chặng {pathDepth}</span>
          {isEnding && <span className="text-oxide font-medium">(Kết thúc mở)</span>}
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
            className="text-muted hover:text-oxide tracking-wider uppercase transition-colors py-1 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent"
            aria-label="Rời khỏi buồng chiêm nghiệm"
          >
            Thoát ✕
          </button>
        </div>
      </div>

      {/* Trace the actual route taken, without revealing endings or assigning personality labels. */}
      {history.length > 0 && (
        <nav aria-label="Các căn phòng đã đi qua" className="flex items-center gap-2 mb-7 overflow-x-auto pb-2 text-[11px] font-sans text-muted">
          <span className="shrink-0 text-accent uppercase tracking-wider">Lối đã qua</span>
          {history.slice(-4).map((stop, index) => (
            <React.Fragment key={index}>
              <span aria-hidden="true" className="opacity-50">/</span>
              <span className="shrink-0">{stop.nodeTitle}</span>
            </React.Fragment>
          ))}
        </nav>
      )}

      {/* Scene presets and motion presets are part of the authored narrative. */}
      <div
        key={currentNodeId}
        data-scene={scenePreset}
        data-motion={motionPreset}
        className={`mirror-stage flex flex-col gap-8 sm:gap-10 ${isLeaving ? 'mirror-stage--leaving' : ''}`}
        aria-busy={isLeaving}
      >
        
        {/* Artwork Chamber Frame (when artwork is present) */}
        {artImage && (
          <div className="relative aspect-[16/9] sm:aspect-[21/9] w-full overflow-hidden bg-surface border border-border/80 shadow-2xl transition-all duration-700">
            <img
              src={artImage}
              alt={currentNode.title}
              className="mirror-stage-art w-full h-full object-cover filter brightness-[0.85] contrast-[1.05]"
              loading="eager"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-bg via-bg/30 to-transparent" />
            <div className="absolute bottom-4 left-6 right-6 flex items-center justify-between text-[11px] font-sans tracking-widest uppercase text-text/80">
              <span className="truncate">{journey.artwork_title} · {journey.artwork_artist}</span>
              <span className="hidden sm:inline text-accent">Museum Archive</span>
            </div>
          </div>
        )}

        {/* Scene Content Block */}
        <div className="space-y-6 max-w-3xl mx-auto w-full">
          
          {/* Scene Title */}
          <div className="space-y-2">
            <span className="text-[11px] font-sans tracking-[0.25em] uppercase text-accent font-semibold block">
              {currentNode.type === 'intro' && '01 / MỞ CỔNG CHIÊM NGHIỆM'}
              {currentNode.type === 'statement' && '02 / PHÒNG QUAN SÁT'}
              {currentNode.type === 'choice' && 'ĐIỂM RẼ TƯ TƯỞNG'}
              {currentNode.type === 'counterpoint' && 'PHẢN ĐỀ TỰ VẤN'}
              {currentNode.type === 'ending' && 'KẾT THÚC MỞ'}
            </span>
            <h1
              ref={headingRef}
              tabIndex={-1}
              className="font-display text-2xl sm:text-4xl md:text-5xl text-text font-medium leading-[1.2] text-balance focus:outline-none"
            >
              {currentNode.title}
            </h1>
          </div>

          {/* Scene Body Text */}
          {currentNode.body && (
            <div className="prose-reading">
              <p className="font-serif text-lg sm:text-2xl text-text/90 italic leading-relaxed sm:leading-loose">
                "{currentNode.body}"
              </p>
            </div>
          )}

          {/* TYPE 1: INTRO / STATEMENT / COUNTERPOINT (Sequential Steps) */}
          {currentNode.next && (
            <div className="pt-6 border-t border-border/60 flex items-center justify-between">
              <span className="text-[11px] font-sans text-muted tracking-wider">
                Nhấn <kbd className="px-1.5 py-0.5 bg-surface border border-border rounded text-[10px]">Enter</kbd> hoặc bấm nút để tiến bước
              </span>

              <button
                onClick={() => handleProceed(currentNode.next!)}
                type="button"
                className="px-7 py-3.5 bg-accent text-on-accent font-sans text-xs tracking-[0.2em] uppercase font-bold hover:opacity-90 transition-opacity min-h-[48px] inline-flex items-center gap-2 shadow-sm"
              >
                <span>{currentNode.type === 'intro' ? 'Bước Vào Lựa Chọn' : 'Tiếp Tục'}</span>
                <span>→</span>
              </button>
            </div>
          )}

          {/* TYPE 2: CHOICE DOORS (Branching Step) */}
          {currentNode.type === 'choice' && currentNode.choices && (
            <div className="pt-6 border-t border-border/60 space-y-4">
              <span className="text-xs font-sans text-muted tracking-wider uppercase block">
                Chọn một hướng đi để mở tiếp đối thoại:
              </span>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {currentNode.choices.map((choice, idx) => (
                  <button
                    key={choice.id}
                    onClick={() => handleProceed(choice.to, choice.id)}
                    type="button"
                    disabled={isLeaving}
                    className="mirror-choice p-6 text-left border border-border/80 hover:border-accent bg-surface/40 hover:bg-surface transition-all duration-300 flex flex-col justify-between gap-4 group min-h-[140px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent disabled:opacity-60"
                  >
                    <div className="flex items-center justify-between text-xs font-sans text-muted">
                      <span className="w-6 h-6 border border-border/80 rounded flex items-center justify-center font-semibold text-accent group-hover:border-accent">
                        {idx + 1}
                      </span>
                      <span className="text-[10px] uppercase tracking-widest text-muted/70 group-hover:text-accent">
                        Phím [{idx + 1}]
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

          {/* TYPE 3: ENDING (Terminal Open Station) */}
          {isEnding && (
            <div className="pt-8 border-t border-border/70 space-y-8">
              
              {/* Closing Reflection Question to Carry */}
              {currentNode.closingQuestion && (
                <div className="p-6 sm:p-8 bg-surface/60 border-l-2 border-accent space-y-3">
                  <span className="text-[11px] font-sans tracking-[0.2em] uppercase text-accent font-semibold block">
                    Câu hỏi mang theo bên mình:
                  </span>
                  <p className="font-serif text-lg sm:text-2xl text-text italic leading-relaxed">
                    "{currentNode.closingQuestion}"
                  </p>
                </div>
              )}

              {/* Action toolbar: Save / Share / Return */}
              <div className="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-border/40">
                <div className="flex items-center gap-3">
                  <button
                    onClick={() => copyRefToClipboard(`Hiyu Abyss - The Mirror (${currentNode.title}): "${currentNode.closingQuestion || currentNode.body}"`)}
                    type="button"
                    className="px-5 py-2.5 border border-border bg-surface text-text hover:border-accent hover:text-accent text-xs font-sans uppercase tracking-widest font-semibold transition-colors flex items-center gap-2"
                  >
                    <span>{copiedToast ? 'Đã sao chép ✓' : 'Lưu câu tự vấn'}</span>
                  </button>

                  <button
                    onClick={handleRestart}
                    type="button"
                    className="px-5 py-2.5 border border-border bg-surface text-text hover:border-accent hover:text-accent text-xs font-sans uppercase tracking-widest font-semibold transition-colors"
                  >
                    Khám phá nhánh khác ↺
                  </button>
                </div>

                <a
                  href="/library"
                  className="px-6 py-2.5 bg-accent text-on-accent text-xs font-sans uppercase tracking-widest font-bold hover:opacity-90 transition-opacity"
                >
                  Vào Thư Viện Đọc Bài →
                </a>
              </div>

            </div>
          )}

        </div>

      </div>

    </div>
  );
}

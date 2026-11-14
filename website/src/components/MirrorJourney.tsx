import React, { useState } from 'react';
import type { MirrorJourneyData, MirrorChoice } from '../lib/types';

interface Props {
  journey: MirrorJourneyData;
}

type Step = 'INTRO' | 'QUESTION' | 'REFLECTION' | 'COUNTERPOINT' | 'OPEN_ENDING';

export default function MirrorJourney({ journey }: Props) {
  const [step, setStep] = useState<Step>('INTRO');
  const [selectedChoiceId, setSelectedChoiceId] = useState<string | null>(null);

  const selectedChoice: MirrorChoice | undefined = journey.question.choices.find(
    (c) => c.id === selectedChoiceId
  );

  const stepIndex = () => {
    switch (step) {
      case 'INTRO': return 1;
      case 'QUESTION': return 2;
      case 'REFLECTION': return 3;
      case 'COUNTERPOINT': return 4;
      case 'OPEN_ENDING': return 5;
    }
  };

  const handleStart = () => setStep('QUESTION');
  const handleSelectChoice = (choiceId: string) => setSelectedChoiceId(choiceId);
  const handleProceedToReflection = () => { if (selectedChoiceId) setStep('REFLECTION'); };
  const handleProceedToCounterpoint = () => setStep('COUNTERPOINT');
  const handleProceedToEnding = () => setStep('OPEN_ENDING');

  const handleBack = () => {
    if (step === 'QUESTION') setStep('INTRO');
    else if (step === 'REFLECTION') setStep('QUESTION');
    else if (step === 'COUNTERPOINT') setStep('REFLECTION');
    else if (step === 'OPEN_ENDING') setStep('COUNTERPOINT');
  };

  const handleRestart = () => {
    setSelectedChoiceId(null);
    setStep('INTRO');
  };

  const handleExit = () => {
    window.location.href = '/mirror';
  };

  return (
    <div className="relative w-full max-w-3xl mx-auto px-4 sm:px-6 py-6 sm:py-12">
      {/* 5-Segment Progress Indicator Bar */}
      <div className="space-y-3 pb-8 mb-8 sm:mb-12 border-b border-border/60">
        <div className="flex items-center justify-between text-[11px] uppercase tracking-widest text-muted font-sans">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
            <span>The Mirror · Chặng {stepIndex()} / 5</span>
          </div>
          <div className="flex items-center gap-4">
            {step !== 'INTRO' && (
              <button
                onClick={handleBack}
                type="button"
                className="hover:text-text transition-colors py-1.5 px-3 rounded-full hover:bg-surface border border-transparent hover:border-border"
                title="Quay lại bước trước"
              >
                ← Quay lại
              </button>
            )}
            <button
              onClick={handleExit}
              type="button"
              className="hover:text-text transition-colors py-1.5 px-3 rounded-full hover:bg-surface border border-transparent hover:border-border"
              title="Thoát hành trình"
            >
              Thoát ✕
            </button>
          </div>
        </div>

        {/* 5 Hairline Progress Segments */}
        <div className="grid grid-cols-5 gap-2 w-full pt-1">
          {[1, 2, 3, 4, 5].map((idx) => {
            const isCompleted = stepIndex() >= idx;
            return (
              <div
                key={idx}
                className={`h-1 rounded-full transition-all duration-500 ${
                  isCompleted ? 'bg-accent' : 'bg-surface-raised'
                }`}
              />
            );
          })}
        </div>
      </div>

      {/* STEP 1: INTRO */}
      {step === 'INTRO' && (
        <div className="space-y-10 sm:space-y-12 animate-fade-in">
          {journey.artwork_url && (
            <div className="p-1.5 rounded-[2rem] bg-surface/70 border border-border/80 shadow-2xl">
              <div className="relative aspect-[16/9] w-full rounded-[calc(2rem-0.375rem)] overflow-hidden bg-bg shadow-inner">
                <img
                  src={journey.artwork_url}
                  alt={journey.artwork_title || journey.title}
                  className="w-full h-full object-cover filter brightness-90 hover:brightness-100 transition-all duration-1000"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-bg via-transparent to-transparent opacity-85" />
                {journey.artwork_title && (
                  <div className="absolute bottom-4 left-4 right-4 text-xs font-serif italic text-text/80 bg-bg/80 backdrop-blur-md px-3 py-1.5 rounded-lg border border-border/40 inline-block w-fit">
                    {journey.artwork_title} — {journey.artwork_artist}
                  </div>
                )}
              </div>
            </div>
          )}

          <div className="text-center max-w-2xl mx-auto space-y-6">
            <div className="inline-block px-3.5 py-1 text-[10px] uppercase tracking-[0.2em] font-sans font-medium text-accent border border-accent/30 bg-accent/10 rounded-full">
              Hành trình tĩnh lặng · Khoảng {journey.estimated_minutes} phút
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-medium tracking-tight text-text">
              {journey.title}
            </h1>
            <p className="font-serif italic text-base sm:text-xl text-muted leading-relaxed">
              {journey.subtitle}
            </p>
            <p className="font-sans text-sm text-muted/90 leading-relaxed pt-1">
              {journey.intro.description}
            </p>
          </div>

          <div className="pt-2 flex justify-center">
            <button
              onClick={handleStart}
              type="button"
              className="group inline-flex items-center gap-3 pl-8 pr-3 py-3 rounded-full bg-accent text-on-accent font-sans text-xs tracking-[0.15em] uppercase font-bold hover:opacity-95 transition-all shadow-xl active:scale-[0.98] min-h-[48px]"
            >
              <span>{journey.intro.button_label}</span>
              <span className="w-8 h-8 rounded-full bg-on-accent/15 flex items-center justify-center transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </button>
          </div>
        </div>
      )}

      {/* STEP 2: QUESTION */}
      {step === 'QUESTION' && (
        <div className="space-y-10 animate-fade-in">
          <div className="space-y-3">
            <span className="text-[10px] uppercase tracking-[0.2em] text-accent font-sans font-semibold block">
              Câu hỏi soi chiếu
            </span>
            <h2 className="font-serif text-2xl sm:text-4xl text-text font-medium leading-snug sm:leading-relaxed">
              "{journey.question.prompt}"
            </h2>
            {journey.question.context && (
              <p className="font-sans text-xs sm:text-sm text-muted italic">
                {journey.question.context}
              </p>
            )}
          </div>

          <div className="space-y-4 pt-2">
            {journey.question.choices.map((choice) => {
              const isSelected = selectedChoiceId === choice.id;
              return (
                <div
                  key={choice.id}
                  onClick={() => handleSelectChoice(choice.id)}
                  className={`cursor-pointer p-1 rounded-2xl border transition-all duration-300 ${
                    isSelected
                      ? 'border-accent bg-accent/10 shadow-lg ring-1 ring-accent'
                      : 'border-border/80 bg-surface hover:border-muted hover:bg-surface-raised'
                  }`}
                >
                  <div className="p-5 sm:p-6 rounded-[calc(1rem-0.125rem)] bg-bg/60 flex items-start gap-4">
                    <div
                      className={`w-6 h-6 mt-0.5 rounded-full border flex items-center justify-center flex-shrink-0 transition-colors ${
                        isSelected
                          ? 'border-accent bg-accent text-on-accent'
                          : 'border-muted'
                      }`}
                    >
                      {isSelected && <span className="text-xs font-bold">✓</span>}
                    </div>
                    <div className="font-serif text-base sm:text-lg text-text leading-relaxed">
                      {choice.label}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div className="pt-6 flex justify-end">
            <button
              onClick={handleProceedToReflection}
              disabled={!selectedChoiceId}
              type="button"
              className={`group inline-flex items-center gap-3 pl-7 pr-3 py-3 rounded-full font-sans text-xs tracking-[0.15em] uppercase font-bold transition-all min-h-[48px] ${
                selectedChoiceId
                  ? 'bg-accent text-on-accent hover:opacity-95 shadow-xl active:scale-[0.98]'
                  : 'bg-surface text-muted border border-border cursor-not-allowed opacity-50'
              }`}
            >
              <span>Soi chiếu góc nhìn này</span>
              <span className="w-8 h-8 rounded-full bg-on-accent/15 flex items-center justify-center transition-transform group-hover:translate-x-1">
                →
              </span>
            </button>
          </div>
        </div>
      )}

      {/* STEP 3: REFLECTION */}
      {step === 'REFLECTION' && selectedChoice && (
        <div className="space-y-10 animate-fade-in">
          <div className="border-l-2 border-accent pl-6 space-y-2">
            <span className="text-[10px] uppercase tracking-[0.2em] text-muted font-sans font-semibold block">
              Góc nhìn bạn đã chọn
            </span>
            <div className="font-serif italic text-lg sm:text-xl text-muted">
              "{selectedChoice.label}"
            </div>
          </div>

          {selectedChoice.artwork_ref && (
            <div className="p-1.5 rounded-[2rem] bg-surface/70 border border-border/80 shadow-xl">
              <div className="aspect-[21/9] w-full rounded-[calc(2rem-0.375rem)] overflow-hidden bg-bg">
                <img
                  src={selectedChoice.artwork_ref}
                  alt="Chi tiết thị giác suy tưởng"
                  className="w-full h-full object-cover filter brightness-85"
                />
              </div>
            </div>
          )}

          <div className="space-y-4 pt-2">
            <span className="text-[10px] uppercase tracking-[0.2em] text-accent font-sans font-semibold block">
              Khoảng lặng chiêm nghiệm
            </span>
            <p className="font-serif text-xl sm:text-2xl text-text leading-relaxed sm:leading-loose">
              {selectedChoice.reflection_text}
            </p>
            {selectedChoice.reflection_subtext && (
              <p className="font-serif italic text-base sm:text-lg text-muted leading-relaxed">
                {selectedChoice.reflection_subtext}
              </p>
            )}
          </div>

          <div className="pt-6 flex justify-end">
            <button
              onClick={handleProceedToCounterpoint}
              type="button"
              className="group inline-flex items-center gap-3 pl-7 pr-3 py-3 rounded-full bg-accent text-on-accent font-sans text-xs tracking-[0.15em] uppercase font-bold hover:opacity-95 transition-all shadow-xl active:scale-[0.98] min-h-[48px]"
            >
              <span>Bước tiếp sang phản đề</span>
              <span className="w-8 h-8 rounded-full bg-on-accent/15 flex items-center justify-center transition-transform group-hover:translate-x-1">
                →
              </span>
            </button>
          </div>
        </div>
      )}

      {/* STEP 4: COUNTERPOINT */}
      {step === 'COUNTERPOINT' && (
        <div className="space-y-10 animate-fade-in">
          <div className="space-y-2">
            <span className="text-[10px] uppercase tracking-[0.2em] text-oxide font-sans font-semibold block">
              Phản đề & Chiều sâu đối nghịch
            </span>
            <h3 className="font-display text-2xl sm:text-4xl font-medium text-text">
              Mặt bên kia của chiếc gương
            </h3>
          </div>

          <div className="p-8 sm:p-10 rounded-2xl bg-surface border border-border/80 space-y-6 shadow-md">
            <p className="font-serif text-lg sm:text-2xl text-text leading-relaxed sm:leading-loose">
              {journey.counterpoint.text}
            </p>
            {journey.counterpoint.subtext && (
              <p className="font-serif italic text-sm sm:text-base text-muted border-t border-border/60 pt-4">
                {journey.counterpoint.subtext}
              </p>
            )}
          </div>

          <div className="space-y-3 pt-2">
            <span className="text-[10px] uppercase tracking-[0.2em] text-muted font-sans font-semibold block">
              Câu hỏi đào sâu
            </span>
            <p className="font-serif italic text-xl sm:text-2xl text-accent leading-relaxed">
              "{journey.counterpoint.question}"
            </p>
          </div>

          <div className="pt-6 flex justify-end">
            <button
              onClick={handleProceedToEnding}
              type="button"
              className="group inline-flex items-center gap-3 pl-7 pr-3 py-3 rounded-full bg-accent text-on-accent font-sans text-xs tracking-[0.15em] uppercase font-bold hover:opacity-95 transition-all shadow-xl active:scale-[0.98] min-h-[48px]"
            >
              <span>Khép lại hành trình</span>
              <span className="w-8 h-8 rounded-full bg-on-accent/15 flex items-center justify-center transition-transform group-hover:translate-x-1">
                →
              </span>
            </button>
          </div>
        </div>
      )}

      {/* STEP 5: OPEN ENDING */}
      {step === 'OPEN_ENDING' && (
        <div className="space-y-12 animate-fade-in">
          <div className="text-center max-w-xl mx-auto space-y-4">
            <span className="text-[10px] uppercase tracking-[0.2em] text-accent font-sans font-semibold block">
              Kết thúc mở
            </span>
            <h3 className="font-display text-3xl sm:text-5xl text-text font-medium">
              Chiếc gương nằm ở chính bạn
            </h3>
            <p className="font-sans text-sm text-muted leading-relaxed">
              {journey.open_ending.prompt}
            </p>
          </div>

          <div className="p-8 sm:p-12 rounded-2xl bg-surface border border-accent/40 text-center space-y-6 shadow-2xl">
            <p className="font-serif italic text-xl sm:text-3xl text-text leading-relaxed">
              "{journey.open_ending.closing_note}"
            </p>
          </div>

          {/* Related Exploration Chips */}
          <div className="space-y-4 pt-2">
            <div className="text-[11px] uppercase tracking-widest text-muted font-sans text-center">
              Khám phá thêm các dòng tư tưởng liên quan
            </div>
            <div className="flex flex-wrap justify-center gap-2.5">
              {journey.open_ending.related_topics.map((t) => (
                <a
                  key={t.code}
                  href={`/themes/${t.slug}`}
                  className="px-4 py-2 bg-surface border border-border/80 hover:border-accent rounded-full text-xs font-sans text-muted hover:text-text transition-all"
                >
                  #{t.title}
                </a>
              ))}
            </div>
          </div>

          {/* Suggested Quotes */}
          {journey.open_ending.suggested_quotes && journey.open_ending.suggested_quotes.length > 0 && (
            <div className="space-y-4 pt-2">
              <div className="text-[11px] uppercase tracking-widest text-muted font-sans text-center">
                Các tác phẩm được đề xuất trong Thư viện
              </div>
              <div className="flex flex-wrap justify-center gap-3">
                {journey.open_ending.suggested_quotes.map((quoteId) => (
                  <a
                    key={quoteId}
                    href={`/library/${quoteId.toLowerCase()}`}
                    class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full border border-border/80 hover:border-accent bg-surface/50 font-serif text-xs text-text transition-all hover:bg-surface"
                  >
                    <span>Đọc tác phẩm {quoteId}</span>
                    <span>→</span>
                  </a>
                ))}
              </div>
            </div>
          )}

          {/* Actions Bar */}
          <div className="pt-8 flex flex-col sm:flex-row items-center justify-center gap-4 border-t border-border/60">
            <button
              onClick={handleRestart}
              type="button"
              className="w-full sm:w-auto inline-flex items-center justify-center min-h-[48px] px-6 py-3 border border-border/80 hover:border-text text-muted hover:text-text font-sans text-xs uppercase tracking-widest rounded-full transition-colors"
            >
              ↺ Bắt đầu lại
            </button>
            <a
              href="/library"
              className="w-full sm:w-auto inline-flex items-center justify-center min-h-[48px] px-8 py-3 bg-accent text-on-accent font-sans text-xs uppercase tracking-widest font-bold rounded-full hover:opacity-95 transition-all shadow-xl active:scale-[0.98]"
            >
              Vào Thư Viện Nghệ Thuật →
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

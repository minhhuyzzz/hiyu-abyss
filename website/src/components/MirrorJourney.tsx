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

  const handleStart = () => {
    setStep('QUESTION');
  };

  const handleSelectChoice = (choiceId: string) => {
    setSelectedChoiceId(choiceId);
  };

  const handleProceedToReflection = () => {
    if (selectedChoiceId) {
      setStep('REFLECTION');
    }
  };

  const handleProceedToCounterpoint = () => {
    setStep('COUNTERPOINT');
  };

  const handleProceedToEnding = () => {
    setStep('OPEN_ENDING');
  };

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

  const stepNumber = () => {
    switch (step) {
      case 'INTRO': return 1;
      case 'QUESTION': return 2;
      case 'REFLECTION': return 3;
      case 'COUNTERPOINT': return 4;
      case 'OPEN_ENDING': return 5;
    }
  };

  return (
    <div className="relative w-full max-w-3xl mx-auto px-4 sm:px-6 py-8 sm:py-16">
      {/* Top Utility Bar */}
      <div className="flex items-center justify-between pb-8 border-b border-[var(--border-subtle)] mb-8 sm:mb-12 text-xs uppercase tracking-widest text-[var(--text-tertiary)] font-sans">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-pulse" />
          <span>The Mirror · Chặng {stepNumber()} / 5</span>
        </div>
        <div className="flex items-center gap-4">
          {step !== 'INTRO' && (
            <button
              onClick={handleBack}
              type="button"
              className="hover:text-[var(--text-primary)] transition-colors py-2 px-3 -my-2 rounded"
              title="Quay lại bước trước"
            >
              ← Quay lại
            </button>
          )}
          <button
            onClick={handleExit}
            type="button"
            className="hover:text-[var(--text-primary)] transition-colors py-2 px-3 -my-2 rounded"
            title="Thoát hành trình"
          >
            Thoát ✕
          </button>
        </div>
      </div>

      {/* STEP 1: INTRO */}
      {step === 'INTRO' && (
        <div className="animate-fade-in space-y-8 sm:space-y-12">
          {journey.artwork_url && (
            <div className="relative aspect-[16/9] w-full overflow-hidden rounded-sm border border-[var(--border-subtle)] shadow-2xl">
              <img
                src={journey.artwork_url}
                alt={journey.artwork_title || journey.title}
                className="w-full h-full object-cover filter brightness-90 hover:brightness-100 transition-all duration-700"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-80" />
              {journey.artwork_title && (
                <div className="absolute bottom-4 left-4 right-4 text-xs font-serif italic text-white/80">
                  {journey.artwork_title} — {journey.artwork_artist}
                </div>
              )}
            </div>
          )}

          <div className="text-center max-w-2xl mx-auto space-y-6">
            <div className="inline-block px-3 py-1 text-[11px] uppercase tracking-widest font-sans text-[var(--accent-primary)] border border-[var(--accent-primary)]/30 rounded-full">
              Hành trình tĩnh lặng · Khoảng {journey.estimated_minutes} phút
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-medium tracking-tight text-[var(--text-primary)]">
              {journey.title}
            </h1>
            <p className="font-serif italic text-base sm:text-xl text-[var(--text-secondary)] leading-relaxed">
              {journey.subtitle}
            </p>
            <p className="font-sans text-sm sm:text-base text-[var(--text-tertiary)] leading-relaxed pt-2">
              {journey.intro.description}
            </p>
          </div>

          <div className="pt-4 flex justify-center">
            <button
              onClick={handleStart}
              type="button"
              className="inline-flex items-center justify-center min-h-[48px] px-8 py-3 bg-[var(--text-primary)] text-[var(--bg-primary)] font-sans text-sm font-medium tracking-wide uppercase rounded hover:opacity-90 transition-all shadow-lg hover:shadow-xl"
            >
              {journey.intro.button_label} →
            </button>
          </div>
        </div>
      )}

      {/* STEP 2: QUESTION */}
      {step === 'QUESTION' && (
        <div className="animate-fade-in space-y-8 sm:space-y-10">
          <div className="space-y-4">
            <span className="text-xs uppercase tracking-widest text-[var(--accent-primary)] font-sans block">
              Câu hỏi soi chiếu
            </span>
            <h2 className="font-serif text-2xl sm:text-4xl text-[var(--text-primary)] font-medium leading-snug sm:leading-relaxed">
              "{journey.question.prompt}"
            </h2>
            {journey.question.context && (
              <p className="font-sans text-sm text-[var(--text-tertiary)] italic">
                {journey.question.context}
              </p>
            )}
          </div>

          <div className="space-y-4 pt-4">
            {journey.question.choices.map((choice) => {
              const isSelected = selectedChoiceId === choice.id;
              return (
                <div
                  key={choice.id}
                  onClick={() => handleSelectChoice(choice.id)}
                  className={`cursor-pointer p-5 sm:p-6 rounded border transition-all duration-300 ${
                    isSelected
                      ? 'border-[var(--accent-primary)] bg-[var(--bg-secondary)] shadow-md ring-1 ring-[var(--accent-primary)]'
                      : 'border-[var(--border-subtle)] bg-[var(--bg-surface)] hover:border-[var(--text-tertiary)]'
                  }`}
                >
                  <div className="flex items-start gap-4">
                    <div
                      className={`w-5 h-5 mt-0.5 rounded-full border flex items-center justify-center flex-shrink-0 transition-colors ${
                        isSelected
                          ? 'border-[var(--accent-primary)] bg-[var(--accent-primary)] text-[var(--bg-primary)]'
                          : 'border-[var(--text-tertiary)]'
                      }`}
                    >
                      {isSelected && <span className="text-[10px] font-bold">✓</span>}
                    </div>
                    <div className="font-serif text-base sm:text-lg text-[var(--text-primary)] leading-relaxed">
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
              className={`inline-flex items-center justify-center min-h-[48px] px-8 py-3 font-sans text-sm font-medium tracking-wide uppercase rounded transition-all ${
                selectedChoiceId
                  ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] hover:opacity-90 shadow-md'
                  : 'bg-[var(--bg-surface)] text-[var(--text-tertiary)] border border-[var(--border-subtle)] cursor-not-allowed opacity-50'
              }`}
            >
              Soi chiếu góc nhìn này →
            </button>
          </div>
        </div>
      )}

      {/* STEP 3: REFLECTION */}
      {step === 'REFLECTION' && selectedChoice && (
        <div className="animate-fade-in space-y-8 sm:space-y-10">
          <div className="border-l-2 border-[var(--accent-primary)] pl-6 space-y-4">
            <span className="text-xs uppercase tracking-widest text-[var(--text-tertiary)] font-sans block">
              Góc nhìn bạn đã chọn
            </span>
            <div className="font-serif italic text-lg sm:text-xl text-[var(--text-secondary)]">
              "{selectedChoice.label}"
            </div>
          </div>

          {selectedChoice.artwork_ref && (
            <div className="aspect-[21/9] w-full overflow-hidden rounded border border-[var(--border-subtle)]">
              <img
                src={selectedChoice.artwork_ref}
                alt="Chi tiết thị giác suy tưởng"
                className="w-full h-full object-cover filter brightness-85"
              />
            </div>
          )}

          <div className="space-y-6 pt-2">
            <span className="text-xs uppercase tracking-widest text-[var(--accent-primary)] font-sans block">
              Khoảng lặng chiêm nghiệm
            </span>
            <p className="font-serif text-xl sm:text-2xl text-[var(--text-primary)] leading-relaxed sm:leading-loose">
              {selectedChoice.reflection_text}
            </p>
            {selectedChoice.reflection_subtext && (
              <p className="font-serif italic text-base sm:text-lg text-[var(--text-secondary)] leading-relaxed">
                {selectedChoice.reflection_subtext}
              </p>
            )}
          </div>

          <div className="pt-8 flex justify-end">
            <button
              onClick={handleProceedToCounterpoint}
              type="button"
              className="inline-flex items-center justify-center min-h-[48px] px-8 py-3 bg-[var(--text-primary)] text-[var(--bg-primary)] font-sans text-sm font-medium tracking-wide uppercase rounded hover:opacity-90 transition-all shadow-md"
            >
              Bước tiếp sang phản đề →
            </button>
          </div>
        </div>
      )}

      {/* STEP 4: COUNTERPOINT */}
      {step === 'COUNTERPOINT' && (
        <div className="animate-fade-in space-y-8 sm:space-y-10">
          <div className="space-y-2">
            <span className="text-xs uppercase tracking-widest text-[var(--oxide-tertiary)] font-sans block">
              Phản đề & Chiều sâu đối nghịch
            </span>
            <h3 className="font-display text-2xl sm:text-3xl font-medium text-[var(--text-primary)]">
              Mặt bên kia của chiếc gương
            </h3>
          </div>

          <div className="p-6 sm:p-8 bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded space-y-6">
            <p className="font-serif text-lg sm:text-2xl text-[var(--text-primary)] leading-relaxed sm:leading-loose">
              {journey.counterpoint.text}
            </p>
            {journey.counterpoint.subtext && (
              <p className="font-serif italic text-sm sm:text-base text-[var(--text-tertiary)] border-t border-[var(--border-subtle)] pt-4">
                {journey.counterpoint.subtext}
              </p>
            )}
          </div>

          <div className="space-y-3 pt-2">
            <span className="text-xs uppercase tracking-widest text-[var(--text-tertiary)] font-sans block">
              Câu hỏi đào sâu
            </span>
            <p className="font-serif italic text-xl sm:text-2xl text-[var(--accent-primary)] leading-relaxed">
              "{journey.counterpoint.question}"
            </p>
          </div>

          <div className="pt-6 flex justify-end">
            <button
              onClick={handleProceedToEnding}
              type="button"
              className="inline-flex items-center justify-center min-h-[48px] px-8 py-3 bg-[var(--text-primary)] text-[var(--bg-primary)] font-sans text-sm font-medium tracking-wide uppercase rounded hover:opacity-90 transition-all shadow-md"
            >
              Khép lại hành trình →
            </button>
          </div>
        </div>
      )}

      {/* STEP 5: OPEN ENDING */}
      {step === 'OPEN_ENDING' && (
        <div className="animate-fade-in space-y-8 sm:space-y-12">
          <div className="text-center max-w-xl mx-auto space-y-4">
            <span className="text-xs uppercase tracking-widest text-[var(--accent-primary)] font-sans block">
              Kết thúc mở
            </span>
            <h3 className="font-display text-3xl sm:text-4xl text-[var(--text-primary)] font-medium">
              Chiếc gương nằm ở chính bạn
            </h3>
            <p className="font-sans text-sm text-[var(--text-tertiary)] leading-relaxed">
              {journey.open_ending.prompt}
            </p>
          </div>

          <div className="p-6 sm:p-10 bg-[var(--bg-secondary)] border border-[var(--border-subtle)] rounded text-center space-y-6">
            <p className="font-serif italic text-xl sm:text-3xl text-[var(--text-primary)] leading-relaxed">
              "{journey.open_ending.closing_note}"
            </p>
          </div>

          {/* Related Exploration */}
          <div className="space-y-6 pt-4">
            <div className="text-xs uppercase tracking-widest text-[var(--text-tertiary)] font-sans text-center">
              Khám phá thêm các dòng tư tưởng liên quan
            </div>
            <div className="flex flex-wrap justify-center gap-3">
              {journey.open_ending.related_topics.map((t) => (
                <a
                  key={t.code}
                  href={`/themes/${t.slug}`}
                  className="px-4 py-2 bg-[var(--bg-surface)] border border-[var(--border-subtle)] hover:border-[var(--accent-primary)] rounded text-xs sm:text-sm font-sans text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition-colors"
                >
                  #{t.title}
                </a>
              ))}
            </div>
          </div>

          {/* Suggested Quotes */}
          {journey.open_ending.suggested_quotes && journey.open_ending.suggested_quotes.length > 0 && (
            <div className="space-y-4 pt-2">
              <div className="text-xs uppercase tracking-widest text-[var(--text-tertiary)] font-sans text-center">
                Các tác phẩm được đề xuất trong Thư viện
              </div>
              <div className="flex flex-wrap justify-center gap-4">
                {journey.open_ending.suggested_quotes.map((quoteId) => (
                  <a
                    key={quoteId}
                    href={`/library/${quoteId.toLowerCase()}`}
                    className="inline-flex items-center gap-2 px-4 py-2 border border-[var(--border-subtle)] hover:border-[var(--text-primary)] rounded font-serif text-sm text-[var(--text-primary)] transition-all hover:bg-[var(--bg-surface)]"
                  >
                    <span>Đọc tác phẩm {quoteId}</span>
                    <span>→</span>
                  </a>
                ))}
              </div>
            </div>
          )}

          {/* Actions */}
          <div className="pt-8 flex flex-col sm:flex-row items-center justify-center gap-4 border-t border-[var(--border-subtle)]">
            <button
              onClick={handleRestart}
              type="button"
              className="w-full sm:w-auto inline-flex items-center justify-center min-h-[48px] px-6 py-2.5 border border-[var(--border-subtle)] hover:border-[var(--text-primary)] text-[var(--text-secondary)] hover:text-[var(--text-primary)] font-sans text-xs uppercase tracking-widest rounded transition-colors"
            >
              ↺ Bắt đầu lại
            </button>
            <a
              href="/library"
              className="w-full sm:w-auto inline-flex items-center justify-center min-h-[48px] px-8 py-2.5 bg-[var(--text-primary)] text-[var(--bg-primary)] font-sans text-xs uppercase tracking-widest font-medium rounded hover:opacity-90 transition-all shadow-md"
            >
              Vào Thư Viện Nghệ Thuật →
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

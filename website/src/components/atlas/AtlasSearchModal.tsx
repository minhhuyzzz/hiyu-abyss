// website/src/components/atlas/AtlasSearchModal.tsx
import React, { useState, useEffect, useRef } from 'react';
import { Search, X, Compass, Sparkles, BookOpen, User, Image as ImageIcon } from 'lucide-react';
import type { AtlasNode } from '../../lib/atlas/types';
import { searchAtlasNodes, type AtlasSearchResult } from '../../lib/atlas/search-index';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  onSelectNode: (nodeId: string) => void;
}

export const AtlasSearchModal: React.FC<Props> = ({ isOpen, onClose, onSelectNode }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<AtlasSearchResult[]>([]);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
      setResults(searchAtlasNodes(''));
    } else {
      setQuery('');
      setSelectedIndex(0);
    }
  }, [isOpen]);

  useEffect(() => {
    const res = searchAtlasNodes(query);
    setResults(res.slice(0, 12));
    setSelectedIndex(0);
  }, [query]);

  // Handle keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return;
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        setSelectedIndex((prev) => (prev + 1 < results.length ? prev + 1 : 0));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setSelectedIndex((prev) => (prev - 1 >= 0 ? prev - 1 : results.length - 1));
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (results[selectedIndex]) {
          onSelectNode(results[selectedIndex].node.id);
          onClose();
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, results, selectedIndex, onClose, onSelectNode]);

  if (!isOpen) return null;

  const getKindIcon = (kind: string) => {
    switch (kind) {
      case 'theme':
        return <Compass className="w-3.5 h-3.5 text-accent" />;
      case 'thinker':
        return <User className="w-3.5 h-3.5 text-oxide" />;
      case 'artwork':
        return <ImageIcon className="w-3.5 h-3.5 text-patina" />;
      case 'quote':
        return <BookOpen className="w-3.5 h-3.5 text-accent" />;
      default:
        return <Sparkles className="w-3.5 h-3.5 text-accent" />;
    }
  };

  const getKindBadge = (kind: string) => {
    switch (kind) {
      case 'theme':
        return 'Chủ Đề';
      case 'thinker':
        return 'Triết Gia';
      case 'artwork':
        return 'Kiệt Tác';
      case 'quote':
        return 'Trích Ngôn';
      default:
        return 'Ý Tưởng';
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-16 sm:pt-24 px-4 bg-black/70 backdrop-blur-md animate-fade-in">
      <div
        className="w-full max-w-2xl bg-surface border border-border shadow-2xl rounded-sm overflow-hidden flex flex-col max-h-[80vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Search Input Bar */}
        <div className="flex items-center px-4 py-3.5 border-b border-border gap-3 bg-surface-raised/40">
          <Search className="w-4 h-4 text-muted shrink-0" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Tìm kiếm tư tưởng, triết gia, kiệt tác hoặc chủ đề..."
            className="flex-1 bg-transparent text-text placeholder:text-muted/60 text-sm font-sans focus:outline-none"
          />
          {query && (
            <button
              onClick={() => setQuery('')}
              className="text-muted hover:text-text p-1 transition-colors"
              aria-label="Xóa nội dung tìm kiếm"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
          <kbd className="hidden sm:inline-block px-1.5 py-0.5 text-[10px] font-mono text-muted border border-border rounded">
            ESC
          </kbd>
        </div>

        {/* Results List */}
        <div className="flex-1 overflow-y-auto divide-y divide-border/40 p-2">
          {results.length === 0 ? (
            <div className="py-12 text-center text-muted font-serif text-sm italic">
              Không tìm thấy tư tưởng tương ứng trong đồ thị The Atlas.
            </div>
          ) : (
            results.map((item, idx) => {
              const isSelected = idx === selectedIndex;
              return (
                <div
                  key={item.node.id}
                  onClick={() => {
                    onSelectNode(item.node.id);
                    onClose();
                  }}
                  onMouseEnter={() => setSelectedIndex(idx)}
                  className={`p-3 rounded-sm cursor-pointer transition-all flex items-start gap-3 ${
                    isSelected ? 'bg-surface-raised border-l-2 border-accent pl-3.5' : 'hover:bg-surface-raised/60'
                  }`}
                >
                  <div className="mt-0.5 p-1.5 rounded-sm bg-bg border border-border shrink-0">
                    {getKindIcon(item.node.kind)}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-[10px] uppercase tracking-wider font-mono px-1.5 py-0.5 rounded bg-bg text-muted border border-border">
                        {getKindBadge(item.node.kind)}
                      </span>
                      <h4 className="text-sm font-serif font-medium text-text truncate">
                        {item.node.label}
                      </h4>
                    </div>
                    <p className="text-xs text-muted font-sans line-clamp-1">
                      {item.node.summary}
                    </p>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Footer shortcuts */}
        <div className="px-4 py-2 bg-surface-raised/60 border-t border-border flex items-center justify-between text-[11px] text-muted font-mono">
          <div className="flex items-center gap-3">
            <span>↑↓ di chuyển</span>
            <span>↵ chọn</span>
          </div>
          <span>The Atlas · {results.length} kết quả</span>
        </div>
      </div>
    </div>
  );
};

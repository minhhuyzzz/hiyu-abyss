import React, { useState, useEffect } from 'react';
import { renderSafeMarkdown } from '../../lib/agora/sanitizer';

interface Comment {
  id: string;
  context_type: 'THREAD' | 'LIBRARY';
  context_id: string;
  parent_id?: string | null;
  author_id: string;
  author_handle: string;
  author_display_name: string;
  author_avatar?: string;
  body_md: string;
  likes_count: number;
  is_liked?: boolean;
  created_at: number;
  replies?: Comment[];
}

interface UserProfile {
  id: string;
  email: string;
  name: string;
  handle: string;
  displayName: string;
  avatarUrl?: string;
  role: string;
}

interface Props {
  quoteId: string;
  quoteTitle: string;
  categorySlug?: string;
  contextType?: 'LIBRARY' | 'THREAD';
}

export default function LibraryComments({ quoteId, quoteTitle, categorySlug, contextType = 'LIBRARY' }: Props) {
  const [currentUser, setCurrentUser] = useState<UserProfile | null>(null);
  const [checkingAuth, setCheckingAuth] = useState(true);
  const [comments, setComments] = useState<Comment[]>([]);
  const [loading, setLoading] = useState(true);
  const [newCommentBody, setNewCommentBody] = useState('');
  const [isPreview, setIsPreview] = useState(false);
  const [replyingToId, setReplyingToId] = useState<string | null>(null);
  const [replyBody, setReplyBody] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  // Check auth state on mount
  useEffect(() => {
    fetch('/api/auth/me')
      .then((r) => r.json())
      .then((data) => {
        if (data.authenticated && data.user) {
          setCurrentUser(data.user);
        } else {
          setCurrentUser(null);
        }
      })
      .catch(() => setCurrentUser(null))
      .finally(() => setCheckingAuth(false));
  }, []);

  // Fetch comments on mount
  const fetchComments = async () => {
    try {
      const res = await fetch(`/api/v1/comments?contextType=${contextType}&contextId=${quoteId.toLowerCase()}`);
      const json = await res.json();
      if (json.success && Array.isArray(json.data)) {
        setComments(json.data);
      }
    } catch (e) {
      console.error('Error fetching comments:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchComments();
  }, [quoteId, contextType]);

  // Current page path for redirect after login
  const currentPath = typeof window !== 'undefined' ? window.location.pathname : `/library/${quoteId.toLowerCase()}`;

  // Submit Root Comment
  const handlePostComment = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!currentUser) {
      setErrorMsg('Vui lòng đăng nhập bằng Google để gửi bình luận.');
      return;
    }
    if (!newCommentBody.trim() || submitting) return;

    setSubmitting(true);
    setErrorMsg(null);

    try {
      const res = await fetch('/api/v1/comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contextType: contextType,
          contextId: quoteId.toLowerCase(),
          body: newCommentBody.trim(),
        }),
      });

      const json = await res.json();
      if (json.success && json.data) {
        setNewCommentBody('');
        setIsPreview(false);
        setComments((prev) => [json.data, ...prev]);
      } else {
        setErrorMsg(json.error?.message || 'Không thể gửi bình luận');
      }
    } catch (err: any) {
      setErrorMsg('Lỗi kết nối máy chủ');
    } finally {
      setSubmitting(false);
    }
  };

  // Submit Nested Reply
  const handlePostReply = async (parentId: string) => {
    if (!currentUser) {
      setErrorMsg('Vui lòng đăng nhập để trả lời bình luận.');
      return;
    }
    if (!replyBody.trim() || submitting) return;

    setSubmitting(true);
    setErrorMsg(null);

    try {
      const res = await fetch('/api/v1/comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contextType: contextType,
          contextId: quoteId.toLowerCase(),
          parentId,
          body: replyBody.trim(),
        }),
      });

      const json = await res.json();
      if (json.success && json.data) {
        setReplyBody('');
        setReplyingToId(null);
        setComments((prev) =>
          prev.map((c) => {
            if (c.id === parentId) {
              return { ...c, replies: [...(c.replies || []), json.data] };
            }
            return c;
          })
        );
      } else {
        setErrorMsg(json.error?.message || 'Không thể gửi câu trả lời');
      }
    } catch (err) {
      setErrorMsg('Lỗi kết nối máy chủ');
    } finally {
      setSubmitting(false);
    }
  };

  // Optimistic Like
  const handleLike = (commentId: string) => {
    if (!currentUser) {
      alert('Vui lòng đăng nhập bằng Google để thả tim bình luận này.');
      return;
    }

    setComments((prev) =>
      prev.map((c) => {
        if (c.id === commentId) {
          const isLiked = !c.is_liked;
          return {
            ...c,
            is_liked: isLiked,
            likes_count: isLiked ? (c.likes_count || 0) + 1 : Math.max(0, (c.likes_count || 0) - 1),
          };
        }
        if (c.replies) {
          return {
            ...c,
            replies: c.replies.map((r) => {
              if (r.id === commentId) {
                const isLiked = !r.is_liked;
                return {
                  ...r,
                  is_liked: isLiked,
                  likes_count: isLiked ? (r.likes_count || 0) + 1 : Math.max(0, (r.likes_count || 0) - 1),
                };
              }
              return r;
            }),
          };
        }
        return c;
      })
    );
  };

  const totalCommentCount = comments.reduce(
    (acc, curr) => acc + 1 + (curr.replies?.length || 0),
    0
  );

  return (
    <section className="pt-12 pb-8 border-t border-border/70 space-y-8" id="discussions">
      {/* Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 pb-4 border-b border-border/40">
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-[0.2em] text-accent font-semibold mb-1">
            <span>THE AGORA</span>
            <span className="text-border">·</span>
            <span>ĐỐI THOẠI & GÓC NHÌN</span>
          </div>
          <h2 className="font-display text-2xl sm:text-3xl font-medium text-text">
            Góc Nhìn Về Tác Phẩm Này
          </h2>
        </div>

        <div className="flex items-center gap-3">
          <span className="text-xs font-sans text-muted">
            {totalCommentCount} chia sẻ
          </span>
          <a
            href="/agora"
            className="px-3 py-1.5 border border-border/70 hover:border-accent text-accent font-sans text-xs tracking-wider uppercase transition-colors rounded-sm flex items-center gap-1.5"
          >
            <span>Diễn đàn The Agora</span>
            <span>→</span>
          </a>
        </div>
      </div>

      {/* Main Comment Composer or Auth Gate */}
      {!currentUser ? (
        <div className="p-6 sm:p-8 bg-surface/40 border border-border/80 rounded-sm space-y-4 text-center shadow-lg">
          <div className="w-10 h-10 rounded-full bg-accent/15 border border-accent/40 text-accent mx-auto flex items-center justify-center text-sm font-serif">
            🔒
          </div>
          <div className="space-y-1 max-w-md mx-auto">
            <h3 className="font-display text-lg sm:text-xl text-text font-medium">
              Đăng Nhập Để Chia Sẻ Góc Nhìn
            </h3>
            <p className="text-xs font-sans text-muted leading-relaxed">
              The Agora bảo lưu danh tính đối thoại văn minh. Vui lòng đăng nhập bằng Google để tham gia bình luận và đối thoại cùng độc giả.
            </p>
          </div>

          <div className="flex items-center justify-center pt-2">
            <a
              href={`/api/auth/google?redirect=${encodeURIComponent(currentPath)}`}
              className="px-6 py-2.5 bg-white hover:bg-neutral-100 text-neutral-900 border border-neutral-300 font-sans text-xs uppercase tracking-wider font-bold rounded-full transition-all flex items-center gap-2.5 shadow-sm hover:shadow-md min-h-[42px]"
            >
              <svg className="w-4 h-4" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
              <span>Đăng nhập bằng Google</span>
            </a>
          </div>
        </div>
      ) : (
        <form onSubmit={handlePostComment} className="space-y-3 bg-surface/30 p-5 sm:p-6 border border-border/70 rounded-sm">
          <div className="flex items-center justify-between text-xs font-sans text-muted">
            <div className="flex items-center gap-2">
              {currentUser.avatarUrl ? (
                <img src={currentUser.avatarUrl} alt={currentUser.displayName} className="w-5 h-5 rounded-full object-cover" />
              ) : (
                <span className="w-5 h-5 rounded-full bg-accent text-on-accent text-[10px] font-bold flex items-center justify-center font-mono uppercase">
                  {currentUser.displayName.charAt(0)}
                </span>
              )}
              <span className="font-medium text-text/90">
                Đang bình luận với tư cách: <strong className="text-accent">{currentUser.displayName}</strong>
                <span className="text-muted font-mono font-normal"> (@{currentUser.handle})</span>
              </span>
            </div>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => setIsPreview(!isPreview)}
                className="text-xs text-muted hover:text-accent font-sans transition-colors"
              >
                {isPreview ? 'Viết tiếp' : 'Xem trước'}
              </button>
              <span className="text-border">·</span>
              <span className="font-mono text-[11px]">{newCommentBody.length} / 4000</span>
            </div>
          </div>

          {isPreview ? (
            <div
              className="min-h-[100px] p-4 bg-surface/60 border border-border/60 rounded-sm prose-reading text-sm text-text"
              dangerouslySetInnerHTML={{ __html: renderSafeMarkdown(newCommentBody || '*Chưa có nội dung xem trước*') }}
            />
          ) : (
            <textarea
              value={newCommentBody}
              onChange={(e) => setNewCommentBody(e.target.value)}
              placeholder="Bạn nhìn nhận câu nói này thế nào qua trải nghiệm của riêng mình?..."
              rows={3}
              className="w-full p-4 bg-surface/50 border border-border/80 focus:border-accent text-sm text-text placeholder-muted/60 rounded-sm outline-none resize-y transition-colors font-sans leading-relaxed"
            />
          )}

          {errorMsg && <p className="text-xs text-red-400 font-sans">{errorMsg}</p>}

          <div className="flex items-center justify-between pt-2">
            <span className="text-[11px] font-sans text-muted/70">
              Hỗ trợ định dạng **in đậm**, *in nghiêng*, &gt; trích dẫn.
            </span>
            <button
              type="submit"
              disabled={submitting || !newCommentBody.trim()}
              className="px-6 py-2.5 bg-accent text-on-accent text-xs font-sans uppercase tracking-widest font-bold hover:opacity-90 disabled:opacity-50 transition-opacity rounded-sm shadow-sm"
            >
              {submitting ? 'Đang gửi...' : 'Gửi góc nhìn'}
            </button>
          </div>
        </form>
      )}

      {/* Comments List */}
      {loading ? (
        <div className="py-8 text-center text-xs font-sans text-muted">
          Đang tải các góc nhìn thảo luận...
        </div>
      ) : comments.length === 0 ? (
        <div className="py-10 text-center border border-border/50 bg-surface/20 rounded-sm space-y-2">
          <p className="font-serif italic text-base text-text/80">
            Chưa có góc nhìn nào được gửi.
          </p>
          <p className="text-xs font-sans text-muted">
            Hãy là người đầu tiên chia sẻ cảm nghĩ của bạn về tác phẩm này.
          </p>
        </div>
      ) : (
        <div className="space-y-6">
          {comments.map((comment) => (
            <article key={comment.id} className="p-5 sm:p-6 bg-surface/30 border border-border/70 rounded-sm space-y-4">
              
              {/* Comment Header */}
              <div className="flex items-center justify-between text-xs font-sans">
                <div className="flex items-center gap-3">
                  {comment.author_avatar && comment.author_avatar.startsWith('http') ? (
                    <img src={comment.author_avatar} alt={comment.author_display_name} className="w-7 h-7 rounded-full object-cover border border-border/60" />
                  ) : (
                    <span className="w-7 h-7 rounded-full bg-accent/20 text-accent font-semibold flex items-center justify-center font-mono text-xs uppercase border border-accent/40">
                      {comment.author_display_name?.[0] || 'A'}
                    </span>
                  )}
                  <div>
                    <span className="font-medium text-text block">
                      {comment.author_display_name}
                    </span>
                    <span className="text-muted font-mono text-[10px]">
                      @{comment.author_handle}
                    </span>
                  </div>
                </div>

                <span className="text-[11px] text-muted font-mono">
                  {new Date(comment.created_at * 1000).toLocaleDateString('vi-VN')}
                </span>
              </div>

              {/* Comment Content */}
              <div
                className="font-serif text-sm sm:text-base text-text/90 leading-relaxed space-y-2"
                dangerouslySetInnerHTML={{ __html: renderSafeMarkdown(comment.body_md) }}
              />

              {/* Comment Actions */}
              <div className="flex items-center justify-between pt-2 border-t border-border/40 text-xs font-sans text-muted">
                <div className="flex items-center gap-4">
                  {/* Like Button */}
                  <button
                    type="button"
                    onClick={() => handleLike(comment.id)}
                    className={`flex items-center gap-1.5 transition-colors ${
                      comment.is_liked ? 'text-accent font-semibold' : 'hover:text-accent'
                    }`}
                  >
                    <span>♥</span>
                    <span>{comment.likes_count || 0}</span>
                  </button>

                  {/* Reply Button */}
                  <button
                    type="button"
                    onClick={() => {
                      if (!currentUser) {
                        alert('Vui lòng đăng nhập bằng Google để trả lời bình luận.');
                        return;
                      }
                      setReplyingToId(replyingToId === comment.id ? null : comment.id);
                    }}
                    className="hover:text-text transition-colors"
                  >
                    {replyingToId === comment.id ? 'Đóng trả lời' : 'Trả lời'}
                  </button>
                </div>
              </div>

              {/* Reply Composer Form */}
              {replyingToId === comment.id && (
                <div className="pt-3 pl-4 border-l-2 border-accent space-y-2">
                  <textarea
                    value={replyBody}
                    onChange={(e) => setReplyBody(e.target.value)}
                    placeholder={`Trả lời @${comment.author_handle}...`}
                    rows={2}
                    className="w-full p-3 bg-surface/60 border border-border/80 focus:border-accent text-xs text-text placeholder-muted/60 rounded-sm outline-none resize-y font-sans"
                  />
                  <div className="flex items-center justify-end gap-2">
                    <button
                      type="button"
                      onClick={() => setReplyingToId(null)}
                      className="px-3 py-1.5 text-xs text-muted hover:text-text font-sans"
                    >
                      Hủy
                    </button>
                    <button
                      type="button"
                      onClick={() => handlePostReply(comment.id)}
                      disabled={submitting || !replyBody.trim()}
                      className="px-4 py-1.5 bg-accent text-on-accent text-xs font-sans uppercase tracking-wider font-semibold hover:opacity-90 disabled:opacity-50 rounded-sm"
                    >
                      {submitting ? '...' : 'Gửi câu trả lời'}
                    </button>
                  </div>
                </div>
              )}

              {/* Level 2 Nested Replies List */}
              {comment.replies && comment.replies.length > 0 && (
                <div className="pt-2 pl-4 sm:pl-6 border-l border-border/60 space-y-3.5">
                  {comment.replies.map((reply) => (
                    <div key={reply.id} className="p-3.5 bg-surface/50 border border-border/40 rounded-sm space-y-2">
                      <div className="flex items-center justify-between text-xs font-sans">
                        <div className="flex items-center gap-2">
                          {reply.author_avatar && reply.author_avatar.startsWith('http') ? (
                            <img src={reply.author_avatar} alt={reply.author_display_name} className="w-5 h-5 rounded-full object-cover" />
                          ) : (
                            <span className="w-5 h-5 rounded-full bg-accent/15 text-accent text-[10px] font-semibold flex items-center justify-center font-mono">
                              {reply.author_display_name?.[0] || 'R'}
                            </span>
                          )}
                          <span className="font-medium text-text text-[11px]">
                            {reply.author_display_name}
                          </span>
                          <span className="text-muted font-mono text-[10px]">
                            @{reply.author_handle}
                          </span>
                        </div>
                        <span className="text-[10px] text-muted font-mono">
                          {new Date(reply.created_at * 1000).toLocaleDateString('vi-VN')}
                        </span>
                      </div>
                      <div
                        className="font-serif text-xs sm:text-sm text-text/85 leading-relaxed"
                        dangerouslySetInnerHTML={{ __html: renderSafeMarkdown(reply.body_md) }}
                      />
                      <div className="flex items-center gap-3 pt-1 text-[11px] font-sans text-muted">
                        <button
                          type="button"
                          onClick={() => handleLike(reply.id)}
                          className={`flex items-center gap-1 transition-colors ${
                            reply.is_liked ? 'text-accent font-semibold' : 'hover:text-accent'
                          }`}
                        >
                          <span>♥</span>
                          <span>{reply.likes_count || 0}</span>
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

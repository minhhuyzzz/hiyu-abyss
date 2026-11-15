-- Migration 0005: High-Performance Indexes for Zero-Latency D1 Queries
CREATE INDEX IF NOT EXISTS idx_threads_cat_status ON threads(category_id, status, last_activity_at DESC);
CREATE INDEX IF NOT EXISTS idx_threads_pinned ON threads(status, pinned, last_activity_at DESC);
CREATE INDEX IF NOT EXISTS idx_threads_author ON threads(author_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_comments_context ON comments(context_type, context_id, created_at ASC);
CREATE INDEX IF NOT EXISTS idx_comments_parent ON comments(parent_id, created_at ASC);
CREATE INDEX IF NOT EXISTS idx_comments_author ON comments(author_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_reactions_target ON reactions(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_reactions_user ON reactions(user_id);

CREATE INDEX IF NOT EXISTS idx_notifications_user ON notifications(user_id, is_read, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_bookmarks_user ON bookmarks(user_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_thread_follows_user ON thread_follows(user_id, thread_id);
CREATE INDEX IF NOT EXISTS idx_drafts_owner ON drafts(owner_id, updated_at DESC);
CREATE INDEX IF NOT EXISTS idx_rate_counters_expires ON rate_counters(expires_at);

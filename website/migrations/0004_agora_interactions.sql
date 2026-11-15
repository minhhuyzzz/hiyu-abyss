-- Migration 0004: Notifications, Mentions, Moderation & Rate Limits
CREATE TABLE IF NOT EXISTS notifications (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    actor_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    type TEXT NOT NULL CHECK(type IN ('REPLY', 'MENTION', 'FOLLOWED_ACTIVITY', 'MODERATION')),
    target_type TEXT NOT NULL CHECK(target_type IN ('THREAD', 'COMMENT', 'ACCOUNT')),
    target_id TEXT NOT NULL,
    is_read INTEGER NOT NULL DEFAULT 0,
    dedup_key TEXT,
    created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS mentions (
    id TEXT PRIMARY KEY,
    source_type TEXT NOT NULL CHECK(source_type IN ('THREAD', 'COMMENT')),
    source_id TEXT NOT NULL,
    mentioned_user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS reports (
    id TEXT PRIMARY KEY,
    reporter_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    target_type TEXT NOT NULL CHECK(target_type IN ('THREAD', 'COMMENT', 'USER')),
    target_id TEXT NOT NULL,
    reason TEXT NOT NULL CHECK(reason IN ('SPAM', 'HARASSMENT', 'MISINFORMATION', 'POLICY_VIOLATION', 'OTHER')),
    detail TEXT,
    status TEXT NOT NULL DEFAULT 'OPEN' CHECK(status IN ('OPEN', 'IN_REVIEW', 'RESOLVED', 'DISMISSED')),
    assigned_to TEXT REFERENCES user(id),
    created_at INTEGER NOT NULL,
    resolved_at INTEGER
);

CREATE TABLE IF NOT EXISTS moderation_actions (
    id TEXT PRIMARY KEY,
    moderator_id TEXT NOT NULL REFERENCES user(id),
    target_type TEXT NOT NULL CHECK(target_type IN ('THREAD', 'COMMENT', 'USER')),
    target_id TEXT NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('HIDE', 'RESTORE', 'LOCK', 'UNLOCK', 'PIN', 'UNPIN', 'WARN', 'SUSPEND', 'BAN')),
    reason TEXT NOT NULL,
    meta_json TEXT,
    created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS rate_counters (
    key TEXT PRIMARY KEY,
    window_start INTEGER NOT NULL,
    count INTEGER NOT NULL,
    expires_at INTEGER NOT NULL
);

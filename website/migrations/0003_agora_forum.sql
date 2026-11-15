-- Migration 0003: Core Agora Forum, Library Comments & Interactions
CREATE TABLE IF NOT EXISTS categories (
    id TEXT PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    cover_art_ref TEXT,
    cover_art_title TEXT,
    cover_art_artist TEXT,
    position INTEGER NOT NULL DEFAULT 0,
    locked INTEGER NOT NULL DEFAULT 0,
    created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS tags (
    id TEXT PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    label TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS threads (
    id TEXT PRIMARY KEY,
    category_id TEXT NOT NULL REFERENCES categories(id),
    author_id TEXT NOT NULL REFERENCES user(id),
    title TEXT NOT NULL,
    slug TEXT NOT NULL,
    body_md TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK(status IN ('ACTIVE', 'LOCKED', 'PINNED', 'DELETED')),
    pinned INTEGER NOT NULL DEFAULT 0,
    locked INTEGER NOT NULL DEFAULT 0,
    reply_count INTEGER NOT NULL DEFAULT 0,
    last_activity_at INTEGER NOT NULL,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL,
    deleted_at INTEGER
);

CREATE TABLE IF NOT EXISTS thread_tags (
    thread_id TEXT NOT NULL REFERENCES threads(id) ON DELETE CASCADE,
    tag_id TEXT NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (thread_id, tag_id)
);

CREATE TABLE IF NOT EXISTS comments (
    id TEXT PRIMARY KEY,
    context_type TEXT NOT NULL CHECK(context_type IN ('THREAD', 'LIBRARY')),
    context_id TEXT NOT NULL,
    parent_id TEXT REFERENCES comments(id) ON DELETE SET NULL,
    author_id TEXT NOT NULL REFERENCES user(id),
    body_md TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK(status IN ('ACTIVE', 'FLAGGED', 'HIDDEN', 'DELETED')),
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL,
    deleted_at INTEGER
);

CREATE TABLE IF NOT EXISTS reactions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    target_type TEXT NOT NULL CHECK(target_type IN ('THREAD', 'COMMENT')),
    target_id TEXT NOT NULL,
    kind TEXT NOT NULL DEFAULT 'LIKE' CHECK(kind IN ('LIKE')),
    created_at INTEGER NOT NULL,
    UNIQUE(user_id, target_type, target_id, kind)
);

CREATE TABLE IF NOT EXISTS thread_follows (
    user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    thread_id TEXT NOT NULL REFERENCES threads(id) ON DELETE CASCADE,
    created_at INTEGER NOT NULL,
    PRIMARY KEY(user_id, thread_id)
);

CREATE TABLE IF NOT EXISTS bookmarks (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    target_type TEXT NOT NULL CHECK(target_type IN ('LIBRARY', 'THREAD')),
    target_id TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    UNIQUE(user_id, target_type, target_id)
);

CREATE TABLE IF NOT EXISTS drafts (
    id TEXT PRIMARY KEY,
    owner_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    kind TEXT NOT NULL CHECK(kind IN ('THREAD', 'COMMENT')),
    context_id TEXT,
    title TEXT,
    body_md TEXT NOT NULL,
    updated_at INTEGER NOT NULL
);

-- Migration 0002: Member Profiles, Preferences, Blocks & Handles
CREATE TABLE IF NOT EXISTS member_profiles (
    user_id TEXT PRIMARY KEY REFERENCES user(id) ON DELETE CASCADE,
    handle TEXT NOT NULL UNIQUE,
    display_name TEXT NOT NULL,
    bio TEXT,
    avatar_preset TEXT DEFAULT 'monogram',
    role TEXT NOT NULL DEFAULT 'MEMBER' CHECK(role IN ('GUEST', 'MEMBER', 'MODERATOR', 'ADMIN')),
    state TEXT NOT NULL DEFAULT 'ACTIVE' CHECK(state IN ('ACTIVE', 'SUSPENDED', 'BANNED')),
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS member_preferences (
    user_id TEXT PRIMARY KEY REFERENCES user(id) ON DELETE CASCADE,
    notify_replies INTEGER NOT NULL DEFAULT 1,
    notify_mentions INTEGER NOT NULL DEFAULT 1,
    notify_followed INTEGER NOT NULL DEFAULT 1,
    public_profile INTEGER NOT NULL DEFAULT 1,
    language TEXT NOT NULL DEFAULT 'vi'
);

CREATE TABLE IF NOT EXISTS member_blocks (
    blocker_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    blocked_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    created_at INTEGER NOT NULL,
    PRIMARY KEY (blocker_id, blocked_id)
);

CREATE TABLE IF NOT EXISTS redirect_handles (
    old_handle TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
    created_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_member_profiles_handle ON member_profiles(handle);
CREATE INDEX IF NOT EXISTS idx_member_profiles_role ON member_profiles(role);

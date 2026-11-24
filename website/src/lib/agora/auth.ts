// website/src/lib/agora/auth.ts
// Authentication & Session Management for The Agora & Library Comments

import type { D1DatabaseLike } from './db';
import { getD1Database } from './db';

export const SESSION_COOKIE_NAME = 'hiyu_agora_session';
export const OAUTH_STATE_COOKIE_NAME = 'hiyu_agora_oauth_state';
export const OAUTH_REDIRECT_COOKIE_NAME = 'hiyu_agora_oauth_redirect';

export interface AuthUser {
  id: string;
  email: string;
  name: string;
  handle: string;
  displayName: string;
  avatarUrl?: string;
  role: 'GUEST' | 'MEMBER' | 'MODERATOR' | 'ADMIN';
  bio?: string;
  createdAt: number;
}

export interface AuthSession {
  id: string;
  token: string;
  expiresAt: number;
  user: AuthUser;
}

export interface GoogleProfile {
  sub: string;
  email: string;
  name: string;
  picture?: string;
  email_verified?: boolean;
}

export function parseCookie(header: string | null | undefined, name: string): string | null {
  if (!header) return null;
  const match = header.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`));
  return match ? decodeURIComponent(match[1]) : null;
}

export function getSessionCookieHeader(token: string, maxAgeSeconds: number = 30 * 24 * 60 * 60): string {
  return `${SESSION_COOKIE_NAME}=${encodeURIComponent(token)}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${maxAgeSeconds}`;
}

export function getClearSessionCookieHeader(): string {
  return `${SESSION_COOKIE_NAME}=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0`;
}

export function getAppOrigin(request: Request): string {
  const forwardedProto = request.headers.get('x-forwarded-proto');
  const forwardedHost = request.headers.get('x-forwarded-host') || request.headers.get('host');
  if (forwardedProto && forwardedHost) {
    return `${forwardedProto}://${forwardedHost}`;
  }
  const url = new URL(request.url);
  return url.origin;
}

interface SessionPayload {
  sessionId: string;
  userId: string;
  email: string;
  name: string;
  handle: string;
  displayName: string;
  avatarUrl?: string;
  role: 'GUEST' | 'MEMBER' | 'MODERATOR' | 'ADMIN';
  bio?: string;
  createdAt: number;
  expiresAt: number;
}

const SESSION_HMAC_SECRET =
  (typeof process !== 'undefined' && (process.env.SESSION_SECRET || process.env.GOOGLE_CLIENT_SECRET)) ||
  'hiyu-abyss-session-crypto-v2-d9f7a8b3c4e1';

function toBase64Url(bytes: Uint8Array): string {
  let binary = '';
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function fromBase64Url(str: string): Uint8Array {
  str = str.replace(/-/g, '+').replace(/_/g, '/');
  while (str.length % 4) str += '=';
  const binary = atob(str);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) {
    bytes[i] = binary.charCodeAt(i);
  }
  return bytes;
}

async function signSessionPayload(payload: SessionPayload): Promise<string> {
  const enc = new TextEncoder();
  const payloadStr = JSON.stringify(payload);
  const payloadB64 = toBase64Url(enc.encode(payloadStr));

  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(SESSION_HMAC_SECRET),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );

  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(payloadB64));
  const sigB64 = toBase64Url(new Uint8Array(sig));
  return `${payloadB64}.${sigB64}`;
}

async function verifySessionToken(token: string): Promise<SessionPayload | null> {
  try {
    const parts = token.split('.');
    if (parts.length !== 2) return null;
    const [payloadB64, sigB64] = parts;
    if (!payloadB64 || !sigB64) return null;

    const enc = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      enc.encode(SESSION_HMAC_SECRET),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['verify']
    );

    const sigBytes = fromBase64Url(sigB64);
    const valid = await crypto.subtle.verify('HMAC', key, sigBytes, enc.encode(payloadB64));
    if (!valid) return null;

    const dec = new TextDecoder();
    const payloadStr = dec.decode(fromBase64Url(payloadB64));
    const payload = JSON.parse(payloadStr) as SessionPayload;
    const now = Math.floor(Date.now() / 1000);
    if (payload.expiresAt <= now) return null;

    return payload;
  } catch (err) {
    return null;
  }
}

export async function getSession(request: Request, runtimeEnv?: any): Promise<AuthSession | null> {
  const cookieHeader = request.headers.get('cookie');
  const token = parseCookie(cookieHeader, SESSION_COOKIE_NAME);
  if (!token) return null;

  const now = Math.floor(Date.now() / 1000);

  // 1. Check if token is a stateless signed token (contains '.')
  if (token.includes('.')) {
    const verified = await verifySessionToken(token);
    if (verified && verified.expiresAt > now) {
      const authUser: AuthUser = {
        id: verified.userId,
        email: verified.email,
        name: verified.name,
        handle: verified.handle,
        displayName: verified.displayName,
        avatarUrl: verified.avatarUrl,
        role: verified.role,
        bio: verified.bio || '',
        createdAt: verified.createdAt,
      };

      // Hydrate DB memory so downstream SQL operations in this lambda find this user
      const db = getD1Database(runtimeEnv);
      try {
        await db
          .prepare(
            `INSERT INTO session (id, expiresAt, token, createdAt, updatedAt, ipAddress, userAgent, userId)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)`
          )
          .bind(verified.sessionId, verified.expiresAt, token, verified.createdAt, verified.createdAt, '', '', verified.userId)
          .run();

        await db
          .prepare(
            `INSERT INTO user (id, name, email, emailVerified, image, createdAt, updatedAt)
             VALUES (?, ?, ?, ?, ?, ?, ?)`
          )
          .bind(verified.userId, verified.name, verified.email, 1, verified.avatarUrl || null, verified.createdAt, verified.createdAt)
          .run();

        await db
          .prepare(
            `INSERT INTO member_profiles (user_id, handle, display_name, bio, avatar_preset, avatar_url, role, state, created_at, updated_at)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          )
          .bind(
            verified.userId,
            verified.handle,
            verified.displayName,
            verified.bio || '',
            'google',
            verified.avatarUrl || null,
            verified.role,
            'ACTIVE',
            verified.createdAt,
            verified.createdAt
          )
          .run();
      } catch {}

      return {
        id: verified.sessionId,
        token: token,
        expiresAt: verified.expiresAt,
        user: authUser,
      };
    }
  }

  // 2. Fallback to direct DB query (for legacy opaque tokens)
  const db = getD1Database(runtimeEnv);
  try {
    const row = await db
      .prepare(
        `SELECT s.id as session_id, s.token, s.expiresAt,
                u.id as user_id, u.email, u.name, u.image,
                p.handle, p.display_name, p.role, p.bio, p.avatar_preset, p.avatar_url, p.created_at
         FROM session s
         JOIN user u ON s.userId = u.id
         LEFT JOIN member_profiles p ON p.user_id = u.id
         WHERE s.token = ? AND s.expiresAt > ?`
      )
      .bind(token, now)
      .first<any>();

    if (!row) return null;

    return {
      id: row.session_id,
      token: row.token,
      expiresAt: row.expiresAt,
      user: {
        id: row.user_id,
        email: row.email,
        name: row.name,
        handle: row.handle || (row.email ? row.email.split('@')[0] : 'member'),
        displayName: row.display_name || row.name,
        avatarUrl: row.avatar_url || row.image || undefined,
        role: row.role || 'MEMBER',
        bio: row.bio || '',
        createdAt: row.created_at || Math.floor(Date.now() / 1000),
      },
    };
  } catch (err) {
    console.error('Error fetching auth session:', err);
    return null;
  }
}

export async function createSession(
  db: D1DatabaseLike,
  userId: string,
  userAgent: string = '',
  ipAddress: string = '',
  authUser?: AuthUser
): Promise<{ token: string; expiresAt: number }> {
  const id = 'sess_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 7);
  const now = Math.floor(Date.now() / 1000);
  const expiresAt = now + 30 * 24 * 60 * 60; // 30 days session

  let user = authUser;
  if (!user) {
    try {
      const u = await db
        .prepare(
          `SELECT u.id, u.email, u.name, u.image,
                  p.handle, p.display_name, p.role, p.bio, p.avatar_url, p.created_at
           FROM user u
           LEFT JOIN member_profiles p ON p.user_id = u.id
           WHERE u.id = ?`
        )
        .bind(userId)
        .first<any>();
      if (u) {
        user = {
          id: u.id,
          email: u.email,
          name: u.name,
          handle: u.handle || (u.email ? u.email.split('@')[0] : 'member'),
          displayName: u.display_name || u.name,
          avatarUrl: u.avatar_url || u.image || undefined,
          role: u.role || 'MEMBER',
          bio: u.bio || '',
          createdAt: u.created_at || now,
        };
      }
    } catch {}
  }

  let token: string;
  if (user) {
    token = await signSessionPayload({
      sessionId: id,
      userId: user.id,
      email: user.email,
      name: user.name,
      handle: user.handle,
      displayName: user.displayName,
      avatarUrl: user.avatarUrl,
      role: user.role,
      bio: user.bio,
      createdAt: user.createdAt,
      expiresAt,
    });
  } else {
    const randomBytes = new Uint8Array(32);
    crypto.getRandomValues(randomBytes);
    token = Array.from(randomBytes, (b) => b.toString(16).padStart(2, '0')).join('');
  }

  try {
    await db
      .prepare(
        `INSERT INTO session (id, expiresAt, token, createdAt, updatedAt, ipAddress, userAgent, userId)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(id, expiresAt, token, now, now, ipAddress, userAgent, userId)
      .run();
  } catch (err) {
    console.error('Failed to insert session in db:', err);
  }

  return { token, expiresAt };
}

export async function deleteSession(db: D1DatabaseLike, token: string): Promise<boolean> {
  await db.prepare(`DELETE FROM session WHERE token = ?`).bind(token).run();
  return true;
}

export async function upsertGoogleUser(
  db: D1DatabaseLike,
  profile: GoogleProfile,
  tokens?: any
): Promise<AuthUser> {
  const now = Math.floor(Date.now() / 1000);

  // 1. Check if user already exists
  let userRow = await db
    .prepare(`SELECT id, email, name, image FROM user WHERE email = ?`)
    .bind(profile.email)
    .first<any>();

  let userId = userRow?.id;

  if (!userId) {
    userId = 'usr_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 7);
    await db
      .prepare(
        `INSERT INTO user (id, name, email, emailVerified, image, createdAt, updatedAt)
         VALUES (?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(userId, profile.name, profile.email, 1, profile.picture || null, now, now)
      .run();
  } else {
    if (profile.picture && profile.picture !== userRow.image) {
      await db
        .prepare(`UPDATE user SET image = ?, updatedAt = ? WHERE id = ?`)
        .bind(profile.picture, now, userId)
        .run();
    }
  }

  // 2. Link or refresh account
  const accountId = 'acc_g_' + profile.sub;
  await db
    .prepare(
      `INSERT OR REPLACE INTO account (id, accountId, providerId, userId, accessToken, idToken, createdAt, updatedAt)
       VALUES (?, ?, 'google', ?, ?, ?, ?, ?)`
    )
    .bind(
      accountId,
      profile.sub,
      userId,
      tokens?.access_token || null,
      tokens?.id_token || null,
      now,
      now
    )
    .run();

  // 3. Upsert member profile
  let memberProfile = await db
    .prepare(`SELECT handle, display_name, role, bio FROM member_profiles WHERE user_id = ?`)
    .bind(userId)
    .first<any>();

  if (!memberProfile) {
    const baseHandle = profile.email
      .split('@')[0]
      .toLowerCase()
      .replace(/[^a-z0-9_]/g, '_')
      .slice(0, 20);
    const handle = baseHandle || 'member_' + Math.random().toString(36).slice(2, 6);

    await db
      .prepare(
        `INSERT INTO member_profiles (user_id, handle, display_name, bio, avatar_preset, avatar_url, role, state, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(
        userId,
        handle,
        profile.name,
        'Độc giả Hiyu Abyss',
        'google',
        profile.picture || null,
        'MEMBER',
        'ACTIVE',
        now,
        now
      )
      .run();

    memberProfile = {
      handle,
      display_name: profile.name,
      role: 'MEMBER',
      bio: 'Độc giả Hiyu Abyss',
    };
  }

  return {
    id: userId,
    email: profile.email,
    name: profile.name,
    handle: memberProfile.handle,
    displayName: memberProfile.display_name,
    avatarUrl: profile.picture,
    role: memberProfile.role,
    bio: memberProfile.bio,
    createdAt: now,
  };
}

export async function upsertDevUser(
  db: D1DatabaseLike,
  info: { name: string; handle: string; email: string; role?: 'GUEST' | 'MEMBER' | 'MODERATOR' | 'ADMIN'; avatarUrl?: string }
): Promise<AuthUser> {
  const now = Math.floor(Date.now() / 1000);
  let userRow = await db
    .prepare(`SELECT id, email, name FROM user WHERE email = ?`)
    .bind(info.email)
    .first<any>();

  let userId = userRow?.id;
  if (!userId) {
    userId = 'usr_' + info.handle;
    await db
      .prepare(
        `INSERT INTO user (id, name, email, emailVerified, image, createdAt, updatedAt)
         VALUES (?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(userId, info.name, info.email, 1, info.avatarUrl || null, now, now)
      .run();
  }

  let profile = await db
    .prepare(`SELECT handle, display_name, role, bio FROM member_profiles WHERE user_id = ?`)
    .bind(userId)
    .first<any>();

  if (!profile) {
    await db
      .prepare(
        `INSERT INTO member_profiles (user_id, handle, display_name, bio, avatar_preset, avatar_url, role, state, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(
        userId,
        info.handle,
        info.name,
        'Thành viên chia sẻ góc nhìn cuộc sống',
        'monogram',
        info.avatarUrl || null,
        info.role || 'MEMBER',
        'ACTIVE',
        now,
        now
      )
      .run();

    profile = {
      handle: info.handle,
      display_name: info.name,
      role: info.role || 'MEMBER',
      bio: 'Thành viên chia sẻ góc nhìn cuộc sống',
    };
  }

  return {
    id: userId,
    email: info.email,
    name: info.name,
    handle: profile.handle,
    displayName: profile.display_name,
    avatarUrl: info.avatarUrl,
    role: profile.role,
    bio: profile.bio,
    createdAt: now,
  };
}

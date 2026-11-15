export const prerender = false;

import type { APIRoute } from 'astro';
import {
  parseCookie,
  getSessionCookieHeader,
  OAUTH_STATE_COOKIE_NAME,
  OAUTH_REDIRECT_COOKIE_NAME,
  getAppOrigin,
  upsertGoogleUser,
  createSession,
} from '../../../../lib/agora/auth';
import { getD1Database } from '../../../../lib/agora/db';

export const GET: APIRoute = async ({ request, locals, redirect }) => {
  const env = (locals as any)?.runtime?.env || {};
  const clientId = env.GOOGLE_CLIENT_ID || import.meta.env.GOOGLE_CLIENT_ID || process.env.GOOGLE_CLIENT_ID;
  const clientSecret = env.GOOGLE_CLIENT_SECRET || import.meta.env.GOOGLE_CLIENT_SECRET || process.env.GOOGLE_CLIENT_SECRET;

  const url = new URL(request.url);
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state');
  const error = url.searchParams.get('error');

  const cookieHeader = request.headers.get('cookie');
  const savedState = parseCookie(cookieHeader, OAUTH_STATE_COOKIE_NAME);
  const savedRedirect = parseCookie(cookieHeader, OAUTH_REDIRECT_COOKIE_NAME) || '/account';

  if (error || !code || !state || state !== savedState) {
    return redirect(`/account?status=auth_failed&error=${encodeURIComponent(error || 'Invalid OAuth state')}`);
  }

  const origin = getAppOrigin(request);
  const callbackUrl = `${origin}/api/auth/callback/google`;

  try {
    // 1. Exchange code for tokens
    const tokenRes = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        code,
        client_id: clientId,
        client_secret: clientSecret,
        redirect_uri: callbackUrl,
        grant_type: 'authorization_code',
      }),
    });

    const tokenData = await tokenRes.json();
    if (!tokenRes.ok || !tokenData.access_token) {
      console.error('Failed to exchange code:', tokenData);
      return redirect(`/account?status=auth_failed&error=token_exchange_failed`);
    }

    // 2. Fetch user profile from Google
    const userRes = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
      headers: { Authorization: `Bearer ${tokenData.access_token}` },
    });
    const profile = await userRes.json();
    if (!profile.email) {
      return redirect(`/account?status=auth_failed&error=missing_email`);
    }

    // 3. Upsert into database
    const db = getD1Database(env);
    const user = await upsertGoogleUser(db, profile, tokenData);

    // 4. Create session
    const userAgent = request.headers.get('user-agent') || '';
    const ip = request.headers.get('cf-connecting-ip') || '';
    const session = await createSession(db, user.id, userAgent, ip);

    // 5. Set session cookie and clear state cookies
    const headers = new Headers();
    headers.set('Location', savedRedirect);
    headers.append('Set-Cookie', getSessionCookieHeader(session.token));
    headers.append('Set-Cookie', `${OAUTH_STATE_COOKIE_NAME}=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0`);
    headers.append('Set-Cookie', `${OAUTH_REDIRECT_COOKIE_NAME}=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0`);

    return new Response(null, { status: 302, headers });
  } catch (err: any) {
    console.error('Error in Google OAuth callback:', err);
    return redirect(`/account?status=auth_failed&error=${encodeURIComponent(err?.message || 'Server error')}`);
  }
};

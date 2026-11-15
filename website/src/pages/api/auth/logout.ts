export const prerender = false;

import type { APIRoute } from 'astro';
import { parseCookie, SESSION_COOKIE_NAME, getClearSessionCookieHeader, deleteSession } from '../../../lib/agora/auth';
import { getD1Database } from '../../../lib/agora/db';

export const POST: APIRoute = async ({ request, locals }) => {
  const cookieHeader = request.headers.get('cookie');
  const token = parseCookie(cookieHeader, SESSION_COOKIE_NAME);

  if (token) {
    const db = getD1Database((locals as any)?.runtime?.env);
    await deleteSession(db, token);
  }

  return new Response(JSON.stringify({ success: true, message: 'Đã đăng xuất' }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Set-Cookie': getClearSessionCookieHeader(),
    },
  });
};

export const GET: APIRoute = async ({ request, locals, redirect }) => {
  const cookieHeader = request.headers.get('cookie');
  const token = parseCookie(cookieHeader, SESSION_COOKIE_NAME);

  if (token) {
    const db = getD1Database((locals as any)?.runtime?.env);
    await deleteSession(db, token);
  }

  const url = new URL(request.url);
  const redirectTo = url.searchParams.get('redirect') || '/account';

  const headers = new Headers();
  headers.set('Location', redirectTo);
  headers.append('Set-Cookie', getClearSessionCookieHeader());

  return new Response(null, { status: 302, headers });
};

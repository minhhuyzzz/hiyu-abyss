export const prerender = false;

import type { APIRoute } from 'astro';
import { getSessionCookieHeader, upsertDevUser, createSession } from '../../../lib/agora/auth';
import { getD1Database } from '../../../lib/agora/db';

export const POST: APIRoute = async ({ request, locals, redirect }) => {
  const env = (locals as any)?.runtime?.env;
  const db = getD1Database(env);

  let body: any = {};
  try {
    body = await request.json();
  } catch {
    body = {};
  }

  const name = body.name || 'Người Đồng Hành';
  const handle = body.handle || 'nguoi_dong_hanh';
  const email = body.email || 'donghanh@hiyuabyss.com';
  const role = body.role || 'MEMBER';
  const redirectTo = body.redirectTo || '/account';

  const user = await upsertDevUser(db, { name, handle, email, role });
  const userAgent = request.headers.get('user-agent') || '';
  const ip = request.headers.get('cf-connecting-ip') || '';
  const session = await createSession(db, user.id, userAgent, ip);

  return new Response(
    JSON.stringify({
      success: true,
      user,
      redirectTo,
    }),
    {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Set-Cookie': getSessionCookieHeader(session.token),
      },
    }
  );
};

export const GET: APIRoute = async ({ request, locals, redirect }) => {
  const env = (locals as any)?.runtime?.env;
  const db = getD1Database(env);

  const url = new URL(request.url);
  const redirectTo = url.searchParams.get('redirect') || '/account';
  const handle = url.searchParams.get('handle') || 'nguoi_dong_hanh';
  const name = url.searchParams.get('name') || 'Người Đồng Hành';
  const email = `${handle}@hiyuabyss.com`;

  const user = await upsertDevUser(db, { name, handle, email, role: 'MEMBER' });
  const userAgent = request.headers.get('user-agent') || '';
  const ip = request.headers.get('cf-connecting-ip') || '';
  const session = await createSession(db, user.id, userAgent, ip);

  const headers = new Headers();
  headers.set('Location', redirectTo);
  headers.append('Set-Cookie', getSessionCookieHeader(session.token));

  return new Response(null, { status: 302, headers });
};

export const prerender = false;

import type { APIRoute } from 'astro';
import { getSessionCookieHeader, upsertDevUser, createSession } from '../../../lib/agora/auth';
import { getD1Database } from '../../../lib/agora/db';
import { getCloudflareEnv } from '../../../lib/cloudflare-env';

export const POST: APIRoute = async ({ request, locals, redirect }) => {
  // P0 Security Gate (Spec §14): Strictly ban dev-login in public / production deployments
  if (import.meta.env.PROD || (typeof process !== 'undefined' && process.env.NODE_ENV === 'production')) {
    return new Response(
      JSON.stringify({ error: 'Endpoint is disabled in public environments per security gate §14' }),
      { status: 403, headers: { 'Content-Type': 'application/json' } }
    );
  }

  const env = getCloudflareEnv(locals);
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
  // P0 Security Gate (Spec §14): Strictly ban dev-login in public / production deployments
  if (import.meta.env.PROD || (typeof process !== 'undefined' && process.env.NODE_ENV === 'production')) {
    return new Response(
      JSON.stringify({ error: 'Endpoint is disabled in public environments per security gate §14' }),
      { status: 403, headers: { 'Content-Type': 'application/json' } }
    );
  }

  const env = getCloudflareEnv(locals);
  const db = getD1Database(env);

  const url = new URL(request.url);
  const redirectTo = url.searchParams.get('redirect') || '/account';

  const user = await upsertDevUser(db, {
    name: 'Người Đồng Hành',
    handle: 'nguoi_dong_hanh',
    email: 'donghanh@hiyuabyss.com',
    role: 'MEMBER',
  });

  const userAgent = request.headers.get('user-agent') || '';
  const ip = request.headers.get('cf-connecting-ip') || '';
  const session = await createSession(db, user.id, userAgent, ip);

  return redirect(redirectTo, {
    headers: {
      'Set-Cookie': getSessionCookieHeader(session.token),
    },
  });
};

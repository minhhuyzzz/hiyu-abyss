export const prerender = false;

import type { APIRoute } from 'astro';
import { OAUTH_STATE_COOKIE_NAME, OAUTH_REDIRECT_COOKIE_NAME, getAppOrigin } from '../../../lib/agora/auth';

export const GET: APIRoute = async ({ request, locals, redirect }) => {
  const env = (locals as any)?.runtime?.env || {};
  const clientId = env.GOOGLE_CLIENT_ID || import.meta.env.GOOGLE_CLIENT_ID || process.env.GOOGLE_CLIENT_ID;

  const url = new URL(request.url);
  const redirectTo = url.searchParams.get('redirect') || '/account';

  if (!clientId) {
    // If Google Client ID is not configured yet, redirect to /account with guidance
    return redirect(`/account?status=google_unconfigured&redirect=${encodeURIComponent(redirectTo)}`);
  }

  // Generate cryptographic state to prevent CSRF
  const randomBytes = new Uint8Array(16);
  crypto.getRandomValues(randomBytes);
  const state = Array.from(randomBytes, (b) => b.toString(16).padStart(2, '0')).join('');

  // Determine callback URL
  const origin = getAppOrigin(request);
  const callbackUrl = `${origin}/api/auth/callback/google`;

  const googleAuthUrl = new URL('https://accounts.google.com/o/oauth2/v2/auth');
  googleAuthUrl.searchParams.set('client_id', clientId);
  googleAuthUrl.searchParams.set('redirect_uri', callbackUrl);
  googleAuthUrl.searchParams.set('response_type', 'code');
  googleAuthUrl.searchParams.set('scope', 'openid email profile');
  googleAuthUrl.searchParams.set('state', state);
  googleAuthUrl.searchParams.set('access_type', 'offline');
  googleAuthUrl.searchParams.set('prompt', 'select_account');

  const headers = new Headers();
  headers.set('Location', googleAuthUrl.toString());
  headers.append(
    'Set-Cookie',
    `${OAUTH_STATE_COOKIE_NAME}=${state}; Path=/; HttpOnly; SameSite=Lax; Max-Age=600`
  );
  headers.append(
    'Set-Cookie',
    `${OAUTH_REDIRECT_COOKIE_NAME}=${encodeURIComponent(redirectTo)}; Path=/; HttpOnly; SameSite=Lax; Max-Age=600`
  );

  return new Response(null, { status: 302, headers });
};

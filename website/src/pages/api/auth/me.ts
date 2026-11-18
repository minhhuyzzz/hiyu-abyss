export const prerender = false;

import type { APIRoute } from 'astro';
import { getSession } from '../../../lib/agora/auth';
import { getCloudflareEnv } from '../../../lib/cloudflare-env';

export const GET: APIRoute = async ({ request, locals }) => {
  const session = await getSession(request, getCloudflareEnv(locals));

  if (!session) {
    return new Response(
      JSON.stringify({
        success: true,
        authenticated: false,
        user: null,
      }),
      {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': 'no-cache, no-store, must-revalidate',
        },
      }
    );
  }

  return new Response(
    JSON.stringify({
      success: true,
      authenticated: true,
      user: session.user,
    }),
    {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
      },
    }
  );
};

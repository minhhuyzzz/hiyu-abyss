export const prerender = false;

import type { APIRoute } from 'astro';
import { AgoraService } from '../../../lib/agora/service';
import { getCloudflareEnv } from '../../../lib/cloudflare-env';

export const GET: APIRoute = async ({ locals }) => {
  try {
    const service = new AgoraService(getCloudflareEnv(locals));
    const categories = await service.getCategories();
    return new Response(JSON.stringify({ success: true, data: categories }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=60',
      },
    });
  } catch (err: any) {
    return new Response(
      JSON.stringify({ success: false, error: { message: err?.message || 'Lỗi server' } }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};

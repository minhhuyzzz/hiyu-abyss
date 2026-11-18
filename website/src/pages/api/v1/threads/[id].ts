export const prerender = false;

import type { APIRoute } from 'astro';
import { AgoraService } from '../../../../lib/agora/service';
import { getCloudflareEnv } from '../../../../lib/cloudflare-env';

export const GET: APIRoute = async ({ params, locals }) => {
  try {
    const threadId = params.id;
    if (!threadId) {
      return new Response(JSON.stringify({ success: false, error: { message: 'Thiếu ID chủ đề' } }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const service = new AgoraService(getCloudflareEnv(locals));
    const thread = await service.getThreadById(threadId);

    if (!thread) {
      return new Response(JSON.stringify({ success: false, error: { message: 'Không tìm thấy chủ đề' } }), {
        status: 404,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return new Response(JSON.stringify({ success: true, data: thread }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=15',
      },
    });
  } catch (err: any) {
    return new Response(
      JSON.stringify({ success: false, error: { message: err?.message || 'Lỗi server' } }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};

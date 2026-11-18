export const prerender = false;

import type { APIRoute } from 'astro';
import { AgoraService } from '../../../../lib/agora/service';
import { createThreadSchema } from '../../../../lib/agora/schemas';
import { getSession } from '../../../../lib/agora/auth';
import { getCloudflareEnv } from '../../../../lib/cloudflare-env';

export const GET: APIRoute = async ({ request, locals }) => {
  try {
    const url = new URL(request.url);
    const categoryId = url.searchParams.get('categoryId') || undefined;
    const filter = (url.searchParams.get('filter') as any) || undefined;
    const limit = Number(url.searchParams.get('limit')) || 20;

    const service = new AgoraService(getCloudflareEnv(locals));
    const threads = await service.getThreads({ categoryId, filter, limit });

    return new Response(JSON.stringify({ success: true, data: threads }), {
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

export const POST: APIRoute = async ({ request, locals }) => {
  try {
    const env = getCloudflareEnv(locals);
    // 1. Enforce Authentication Check
    const session = await getSession(request, env);
    if (!session) {
      return new Response(
        JSON.stringify({
          success: false,
          error: { message: 'Vui lòng đăng nhập bằng tài khoản Google để tạo chủ đề thảo luận mới.' },
        }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const body = await request.json();
    const validated = createThreadSchema.parse(body);

    const service = new AgoraService(env);
    const author = {
      id: session.user.id,
      handle: session.user.handle,
      displayName: session.user.displayName,
      avatar: session.user.avatarUrl,
    };

    const newThread = await service.createThread(validated, author);

    return new Response(JSON.stringify({ success: true, data: newThread }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err: any) {
    const message = err?.errors?.[0]?.message || err?.message || 'Dữ liệu không hợp lệ';
    return new Response(
      JSON.stringify({ success: false, error: { message } }),
      { status: 400, headers: { 'Content-Type': 'application/json' } }
    );
  }
};

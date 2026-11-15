export const prerender = false;

import type { APIRoute } from 'astro';
import { AgoraService } from '../../../../lib/agora/service';
import { createCommentSchema } from '../../../../lib/agora/schemas';
import { getSession } from '../../../../lib/agora/auth';

export const GET: APIRoute = async ({ request, locals }) => {
  try {
    const url = new URL(request.url);
    const contextType = (url.searchParams.get('contextType') as any) || 'LIBRARY';
    const contextId = url.searchParams.get('contextId');

    if (!contextId) {
      return new Response(
        JSON.stringify({ success: false, error: { message: 'Thiếu contextId' } }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const service = new AgoraService((locals as any)?.runtime?.env);
    const comments = await service.getComments(contextType, contextId);

    return new Response(JSON.stringify({ success: true, data: comments }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
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
    // 1. Enforce Authentication Check
    const session = await getSession(request, (locals as any)?.runtime?.env);
    if (!session) {
      return new Response(
        JSON.stringify({
          success: false,
          error: { message: 'Vui lòng đăng nhập bằng tài khoản Google để gửi bình luận.' },
        }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const body = await request.json();
    const validated = createCommentSchema.parse(body);

    const service = new AgoraService((locals as any)?.runtime?.env);
    const author = {
      id: session.user.id,
      handle: session.user.handle,
      displayName: session.user.displayName,
      avatar: session.user.avatarUrl,
    };

    const newComment = await service.createComment(validated, author);

    return new Response(JSON.stringify({ success: true, data: newComment }), {
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

export const prerender = false;

import type { APIRoute } from 'astro';
import { AgoraService } from '../../../../lib/agora/service';
import { createReportSchema } from '../../../../lib/agora/schemas';
import { getCloudflareEnv } from '../../../../lib/cloudflare-env';

export const POST: APIRoute = async ({ request, locals }) => {
  try {
    const body = await request.json();
    const validated = createReportSchema.parse(body);

    const service = new AgoraService(getCloudflareEnv(locals));
    const reporterId = 'usr_guest_demo';

    await service.createReport(validated, reporterId);

    return new Response(JSON.stringify({ success: true, message: 'Báo cáo đã được tiếp nhận.' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err: any) {
    const message = err?.errors?.[0]?.message || err?.message || 'Lỗi gửi báo cáo';
    return new Response(
      JSON.stringify({ success: false, error: { message } }),
      { status: 400, headers: { 'Content-Type': 'application/json' } }
    );
  }
};

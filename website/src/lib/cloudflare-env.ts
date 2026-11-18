// website/src/lib/cloudflare-env.ts
// Robust Cloudflare environment binding extractor for Astro 7+
let cachedCfEnv: any = null;

export async function resolveCloudflareEnv(locals?: any): Promise<any> {
  if (cachedCfEnv) return cachedCfEnv;
  try {
    // @ts-ignore
    const cf = await import('cloudflare:workers');
    if (cf && cf.env) {
      cachedCfEnv = cf.env;
      return cachedCfEnv;
    }
  } catch {
    // Non-workers environment
  }

  if (locals?.cfContext?.env) {
    return locals.cfContext.env;
  }

  if (typeof process !== 'undefined' && process.env) {
    return process.env;
  }

  return {};
}

export function getCloudflareEnv(locals?: any): any {
  if (cachedCfEnv) return cachedCfEnv;
  if (locals?.cfContext?.env) return locals.cfContext.env;
  try {
    // @ts-ignore
    const cf = (globalThis as any)[Symbol.for('cloudflare.workers.env')];
    if (cf) return cf;
  } catch {}
  if (typeof process !== 'undefined' && process.env) {
    return process.env;
  }
  return {};
}

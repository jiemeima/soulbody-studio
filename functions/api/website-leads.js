// Only forward consented form submissions; do not forward browser cookies or login tokens.
const upstream = 'https://pawpark.com.cn/api/website-leads';
const allowedOrigins = new Set(['https://soulbody-studio.com', 'https://www.soulbody-studio.com']);

export async function onRequest({ request }) {
  if (request.method !== 'POST') return new Response(null, { status: 405, headers: { Allow: 'POST' } });
  const origin = request.headers.get('Origin');
  if (!allowedOrigins.has(origin) || new URL(request.url).origin !== origin) return new Response(null, { status: 403 });
  if (!request.headers.get('Content-Type')?.startsWith('application/json')) return new Response(null, { status: 415 });
  const body = await request.text();
  if (body.length > 12000) return new Response(null, { status: 413 });
  try { JSON.parse(body); } catch { return new Response(null, { status: 400 }); }
  try {
    const response = await fetch(upstream, {
      method: 'POST', headers: { 'Content-Type': 'application/json', Origin: origin },
      body, redirect: 'manual', signal: AbortSignal.timeout(10000),
    });
    return new Response(null, { status: response.status === 204 ? 204 : 502, headers: { 'Cache-Control': 'no-store' } });
  } catch {
    return new Response(null, { status: 503, headers: { 'Cache-Control': 'no-store' } });
  }
}

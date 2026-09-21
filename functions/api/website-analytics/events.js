// Forward only anonymous website statistics; never forward cookies or login tokens.
// Cloudflare fetch requires a hostname. Keep this A record DNS-only -> 120.55.193.185.
const upstream = 'http://analytics-origin.soulbody-studio.com:15666/api/public/website-analytics/events';
const allowedOrigins = new Set(['https://soulbody-studio.com', 'https://www.soulbody-studio.com']);

function reply(status, message) {
  return Response.json({ message }, { status, headers: { 'Cache-Control': 'no-store' } });
}

export async function onRequest({ request }) {
  if (request.method !== 'POST') {
    return new Response(null, { status: 405, headers: { Allow: 'POST', 'Cache-Control': 'no-store' } });
  }
  const origin = request.headers.get('Origin');
  if (!allowedOrigins.has(origin) || new URL(request.url).origin !== origin) {
    return reply(403, 'Origin not allowed');
  }
  if (!request.headers.get('Content-Type')?.toLowerCase().startsWith('application/json')) {
    return reply(415, 'Expected JSON');
  }
  // Bound the body even when Content-Length is absent.
  const reader = request.body?.getReader();
  if (!reader) return reply(400, 'Empty event');
  const chunks = [];
  let size = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    size += value.byteLength;
    if (size > 16384) {
      await reader.cancel();
      return reply(413, 'Event too large');
    }
    chunks.push(value);
  }
  const body = await new Blob(chunks).text();
  try {
    const event = JSON.parse(body);
    if (!event || !['page_view', 'click'].includes(event.eventType)) return reply(400, 'Invalid event');
  } catch {
    return reply(400, 'Invalid JSON');
  }
  try {
    const response = await fetch(upstream, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Origin: origin },
      body,
      redirect: 'error',
      signal: AbortSignal.timeout(10000),
    });
    return new Response(response.body, {
      status: response.status,
      headers: {
        'Content-Type': response.headers.get('Content-Type') || 'application/json',
        'Cache-Control': 'no-store',
      },
    });
  } catch {
    return reply(502, 'Statistics service unavailable');
  }
}

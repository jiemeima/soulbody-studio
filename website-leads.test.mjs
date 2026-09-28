import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { onRequest } from './functions/api/website-leads.js';

test('consultation form asks for consent and submits instead of opening mail', async () => {
  const html = await readFile(new URL('./about.html', import.meta.url), 'utf8');
  const script = await readFile(new URL('./js/main.js', import.meta.url), 'utf8');
  assert.match(html, /id="lead-form"/);
  assert.match(html, /name="consent" required/);
  assert.match(script, /fetch\('\/api\/website-leads'/);
  assert.doesNotMatch(script, /window\.location\.href = 'mailto:/);
});

test('Pages relay forwards only same-origin JSON without visitor cookies', async () => {
  const body = JSON.stringify({ submissionId: 'test', consent: true });
  const request = new Request('https://soulbody-studio.com/api/website-leads', {
    method: 'POST', headers: { Origin: 'https://soulbody-studio.com', 'Content-Type': 'application/json', Cookie: 'private=1' }, body,
  });
  const originalFetch = globalThis.fetch;
  let forwarded;
  globalThis.fetch = async (url, options) => {
    forwarded = { url, options };
    return new Response(null, { status: 204 });
  };
  try {
    const response = await onRequest({ request });
    assert.equal(response.status, 204);
    assert.equal(forwarded.url, 'https://pawpark.com.cn/api/website-leads');
    assert.equal(forwarded.options.headers.Origin, 'https://soulbody-studio.com');
    assert.equal(forwarded.options.headers.Cookie, undefined);
    assert.equal(forwarded.options.body, body);
    globalThis.fetch = async () => new Response('{"code":500}', { status: 200 });
    const rejected = await onRequest({ request: new Request('https://soulbody-studio.com/api/website-leads', {
      method: 'POST', headers: { Origin: 'https://soulbody-studio.com', 'Content-Type': 'application/json' }, body,
    }) });
    assert.equal(rejected.status, 502);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

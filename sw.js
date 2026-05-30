// Utilify Service Worker
//
// Strategy
//   - Static assets (/assets/**, favicons, manifest):  cache-first
//   - HTML pages (same-origin navigation requests):    stale-while-revalidate
//   - External (ads, analytics, fonts CDN):            network-only, never cached
//
// CACHE_VERSION is patched at build time. Bumping it triggers the activate
// handler to drop every old cache, so users pick up fresh CSS/JS on the
// next navigation after a deploy.
//
// First visit: SW installs in the background, no UX impact. From the second
// visit onward, pages render from cache instantly (offline + flaky-network
// friendly) while a fresh copy fetches in the background for next time.

const CACHE_VERSION = '2026-05-30';
const STATIC_CACHE = 'utilify-static-' + CACHE_VERSION;
const PAGES_CACHE  = 'utilify-pages-'  + CACHE_VERSION;

// Pre-cache the essentials — enough to render any tool page offline once
// the user has visited it once. Per-tool HTML is cached on demand.
const STATIC_PRECACHE = [
  '/assets/css/main.css',
  '/assets/js/common.js',
  '/manifest.json',
  '/favicon.ico',
  '/favicon-16x16.png',
  '/favicon-32x32.png',
  '/apple-touch-icon.png',
];

// Hostnames that must never be cached — ads need freshness, analytics need
// live pings, Google Fonts CSS is updated server-side for new browser hints.
const NO_CACHE_HOSTS = new Set([
  'pagead2.googlesyndication.com',
  'googletagmanager.com',
  'google-analytics.com',
  'analytics.google.com',
  'fonts.googleapis.com',
  'fonts.gstatic.com',
  'cmp.gatekeeperconsent.com',
  'the.gatekeeperconsent.com',
  'www.ezojs.com',
  'ezoicanalytics.com',
]);

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => cache.addAll(STATIC_PRECACHE).catch(() => {}))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys
        .filter(k => k.startsWith('utilify-') && k !== STATIC_CACHE && k !== PAGES_CACHE)
        .map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

function isStaticAsset(url) {
  if (url.pathname.startsWith('/assets/')) return true;
  if (url.pathname === '/manifest.json') return true;
  return /\.(css|js|png|jpg|jpeg|webp|svg|ico|woff2?|ttf)$/i.test(url.pathname);
}

function isHtmlRequest(request, url) {
  if (request.mode === 'navigate') return true;
  const accept = request.headers.get('accept') || '';
  if (accept.includes('text/html')) return true;
  if (url.pathname.endsWith('/') || url.pathname.endsWith('.html')) return true;
  return false;
}

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;

  let url;
  try { url = new URL(req.url); } catch (e) { return; }

  // Cross-origin: bypass entirely if it's on the no-cache list (ads/analytics);
  // otherwise let the browser handle it without involving the SW cache.
  if (url.origin !== self.location.origin) {
    if (NO_CACHE_HOSTS.has(url.hostname)) return;
    return;
  }

  // Static assets — cache-first. Falls back to network on miss, then stores
  // the response. If both cache miss + network fail (e.g., true offline first
  // visit), returns the network's error — same as default behavior.
  if (isStaticAsset(url)) {
    event.respondWith(
      caches.match(req).then(cached => {
        if (cached) return cached;
        return fetch(req).then(resp => {
          if (resp && resp.status === 200 && resp.type === 'basic') {
            const clone = resp.clone();
            caches.open(STATIC_CACHE).then(c => c.put(req, clone));
          }
          return resp;
        });
      })
    );
    return;
  }

  // HTML pages — stale-while-revalidate. Returns the cached copy immediately
  // (or the network response on first visit), then refreshes the cache in the
  // background so the next visit picks up any updated content.
  if (isHtmlRequest(req, url)) {
    event.respondWith(
      caches.match(req).then(cached => {
        const networkFetch = fetch(req).then(resp => {
          if (resp && resp.status === 200 && resp.type === 'basic') {
            const clone = resp.clone();
            caches.open(PAGES_CACHE).then(c => c.put(req, clone));
          }
          return resp;
        }).catch(() => cached);
        return cached || networkFetch;
      })
    );
    return;
  }

  // Anything else (XHR, fetch() to unhandled paths) — pass through.
});

/*
 * UNI Encyclopedia and Cookbook -- Service Worker
 *
 * Contract (do not lie about offline capability):
 *   - Install: fetch the precache manifest, then fetch every listed asset.
 *     If ANY asset fails (network error, non-200, or missing), the install
 *     step rejects. The old SW keeps serving. The site continues as a plain
 *     online site until fixed. Silent partial offline is worse than none.
 *   - Activate: delete every cache whose name does not match CACHE_NAME.
 *   - Fetch:
 *       * Only GET is intercepted. POST/PUT/DELETE bypass.
 *       * Only same-origin requests within the scope are intercepted.
 *         Cross-origin requests bypass (never cached; no opaque responses).
 *       * _provenance.json  -> network first, cache fallback.
 *       * Everything else   -> cache first, network fallback, then a
 *                              synthesized "you are offline" HTML response
 *                              for navigation requests.
 *       * Non-200 network responses are NEVER cached.
 *   - Messages:
 *       * {type: "getStatus"}    -> {version, cacheEntries}
 *       * {type: "forceRefresh"} -> nuke all caches, unregister self
 *
 * ASCII-only. No external network references. No inline event handlers.
 * Vanilla JS.  Placeholder __CACHE_VERSION__ is substituted by build.py at
 * emit time with the reader build's commit SHA.
 */

"use strict";

/* build.py replaces __CACHE_VERSION__ with the short SHA of the reader
 * build. If the token is never substituted, we fall back to the literal
 * string so the SW still installs (and the operator can see the drift in
 * the getStatus reply). */
var CACHE_VERSION = "__CACHE_VERSION__";
var CACHE_NAME = "cookbook-" + CACHE_VERSION;

/* SCOPE_PATH is derived at parse time from the SW's own URL, not hardcoded.
 * `new URL('./', self.location)` resolves to the directory containing sw.js
 * (which IS its effective scope when the register call passes scope:'./').
 * That means the same file works whether the reader is served at
 * https://limb/glass/cookbook/ (production fleet) or at
 * http://127.0.0.1:8123/  (a local `python -m http.server -d reader/dist`).
 * The earlier hardcoded "/glass/cookbook/" broke the local case entirely --
 * `isInScope` returned false for every request and cacheFirst never ran. */
var SCOPE_PATH = new URL("./", self.location).pathname;
var PRECACHE_MANIFEST_URL = SCOPE_PATH + "precache-manifest.json";
var PROVENANCE_URL = SCOPE_PATH + "_provenance.json";

/* ---------- install: precache everything or fail loudly ---------- */

self.addEventListener("install", function (event) {
  event.waitUntil(
    (async function () {
      var manifestResp = await fetch(PRECACHE_MANIFEST_URL, {
        cache: "no-store"
      });
      if (!manifestResp || !manifestResp.ok) {
        throw new Error(
          "precache-manifest.json fetch failed: " +
            (manifestResp ? manifestResp.status : "no response")
        );
      }
      var manifest = await manifestResp.json();
      if (!manifest || !Array.isArray(manifest.files)) {
        throw new Error(
          "precache-manifest.json malformed: missing 'files' array"
        );
      }

      var cache = await caches.open(CACHE_NAME);

      /* Always include the manifest itself so an offline getStatus can
       * still see what was intended. */
      var urls = [PRECACHE_MANIFEST_URL];
      for (var i = 0; i < manifest.files.length; i++) {
        var entry = manifest.files[i];
        var path = typeof entry === "string" ? entry : entry.path;
        if (typeof path !== "string" || path.length === 0) {
          throw new Error(
            "precache-manifest.json entry " + i + " has no path"
          );
        }
        /* Normalize: manifest paths are relative to scope or absolute. */
        var url;
        if (path.charAt(0) === "/") {
          url = path;
        } else {
          url = SCOPE_PATH + path;
        }
        urls.push(url);
      }

      /* Fetch each and add only 200s to the cache. Any failure aborts
       * install so we never activate a half-populated cache. */
      for (var j = 0; j < urls.length; j++) {
        var u = urls[j];
        var resp;
        try {
          resp = await fetch(u, { cache: "no-store" });
        } catch (netErr) {
          throw new Error("precache fetch threw for " + u + ": " + netErr);
        }
        if (!resp || !resp.ok || resp.status !== 200) {
          throw new Error(
            "precache fetch non-200 for " +
              u +
              ": " +
              (resp ? resp.status : "no response")
          );
        }
        if (resp.type === "opaque") {
          throw new Error("precache refused opaque response for " + u);
        }
        await cache.put(u, resp.clone());
      }
    })()
  );
});

/* ---------- activate: sweep stale caches ---------- */

self.addEventListener("activate", function (event) {
  event.waitUntil(
    (async function () {
      var names = await caches.keys();
      for (var i = 0; i < names.length; i++) {
        var n = names[i];
        if (n !== CACHE_NAME) {
          await caches.delete(n);
        }
      }
      /* Take control of already-open pages so cache-first begins now. */
      if (self.clients && self.clients.claim) {
        await self.clients.claim();
      }
    })()
  );
});

/* ---------- fetch: route requests ---------- */

function isSameOrigin(url) {
  try {
    return new URL(url).origin === self.location.origin;
  } catch (e) {
    return false;
  }
}

function isInScope(url) {
  try {
    var u = new URL(url);
    return u.pathname.indexOf(SCOPE_PATH) === 0;
  } catch (e) {
    return false;
  }
}

function isProvenance(url) {
  try {
    var u = new URL(url);
    return u.pathname === PROVENANCE_URL;
  } catch (e) {
    return false;
  }
}

function offlineHtmlResponse() {
  var body =
    "<!doctype html>" +
    "<html lang=\"en\"><head>" +
    "<meta charset=\"utf-8\">" +
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">" +
    "<title>Offline &#8212; UNI Cookbook</title>" +
    "<style>" +
    "html,body{margin:0;padding:0;background:#f5efe0;color:#2a2a2a;" +
    "font-family:Georgia,serif;line-height:1.5}" +
    "main{max-width:36rem;margin:6rem auto;padding:0 1.5rem}" +
    "h1{font-size:1.5rem;margin:0 0 1rem}" +
    "p{margin:0 0 1rem}" +
    "@media (prefers-color-scheme: dark){" +
    "html,body{background:#1a1a1a;color:#e8e2d0}" +
    "}" +
    "</style></head><body><main>" +
    "<h1>Offline</h1>" +
    "<p>This page is not in the offline cache and the network is unreachable.</p>" +
    "<p>Return to the <a href=\"" +
    SCOPE_PATH +
    "\">cookbook index</a> when reconnected.</p>" +
    "</main></body></html>";
  return new Response(body, {
    status: 503,
    statusText: "Offline",
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store"
    }
  });
}

async function networkFirst(request) {
  try {
    var resp = await fetch(request);
    if (resp && resp.ok && resp.status === 200 && resp.type !== "opaque") {
      var cache = await caches.open(CACHE_NAME);
      await cache.put(request, resp.clone());
    }
    return resp;
  } catch (netErr) {
    var cached = await caches.match(request);
    if (cached) {
      return cached;
    }
    throw netErr;
  }
}

async function cacheFirst(request) {
  var cached = await caches.match(request);
  if (cached) {
    return cached;
  }
  try {
    var resp = await fetch(request);
    if (resp && resp.ok && resp.status === 200 && resp.type !== "opaque") {
      var cache = await caches.open(CACHE_NAME);
      await cache.put(request, resp.clone());
    }
    return resp;
  } catch (netErr) {
    if (request.mode === "navigate") {
      return offlineHtmlResponse();
    }
    return new Response("", {
      status: 504,
      statusText: "Offline and not cached"
    });
  }
}

self.addEventListener("fetch", function (event) {
  var request = event.request;

  /* Never touch anything but GET. */
  if (request.method !== "GET") {
    return;
  }

  /* Never touch cross-origin. */
  if (!isSameOrigin(request.url)) {
    return;
  }

  /* Only manage the cookbook scope. Anything else on the same origin
   * (adjacent apps under /glass/) goes straight to network. */
  if (!isInScope(request.url)) {
    return;
  }

  if (isProvenance(request.url)) {
    event.respondWith(networkFirst(request));
    return;
  }

  event.respondWith(cacheFirst(request));
});

/* ---------- messages: status + forced refresh ---------- */

self.addEventListener("message", function (event) {
  var data = event.data;
  if (!data || typeof data !== "object") {
    return;
  }

  if (data.type === "getStatus") {
    event.waitUntil(
      (async function () {
        var entries = 0;
        try {
          var cache = await caches.open(CACHE_NAME);
          var keys = await cache.keys();
          entries = keys.length;
        } catch (e) {
          entries = -1;
        }
        var reply = {
          type: "status",
          version: CACHE_VERSION,
          cacheName: CACHE_NAME,
          cacheEntries: entries
        };
        if (event.ports && event.ports[0]) {
          event.ports[0].postMessage(reply);
        } else if (event.source && event.source.postMessage) {
          event.source.postMessage(reply);
        }
      })()
    );
    return;
  }

  if (data.type === "forceRefresh") {
    event.waitUntil(
      (async function () {
        var names = await caches.keys();
        for (var i = 0; i < names.length; i++) {
          await caches.delete(names[i]);
        }
        if (self.registration && self.registration.unregister) {
          await self.registration.unregister();
        }
        var reply = { type: "refreshed" };
        if (event.ports && event.ports[0]) {
          event.ports[0].postMessage(reply);
        } else if (event.source && event.source.postMessage) {
          event.source.postMessage(reply);
        }
      })()
    );
    return;
  }
});

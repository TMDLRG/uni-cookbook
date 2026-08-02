/* reader/app.js -- client runtime for the cookbook e-reader chrome.
 *
 * Vanilla JS, no dependencies. IIFE-wrapped. Pure ASCII bytes.
 * Fail-closed: a missing hook logs a console warning and returns; nothing
 * throws that would halt the page. No fetch to any non-same-origin URL.
 * No inline on* handlers, no eval, no new Function, no innerHTML with any
 * value that did not originate in this file.
 *
 * Contract (all optional; behaviour degrades if a hook is absent):
 *   [data-role="sidebar"]        data-corpus-tree = JSON [{wing,id,title,path,words}]
 *   [data-role="reading-progress"]  a bar filled by scroll fraction
 *   [data-role="chapter-nav"]    data-prev, data-next (URL strings)
 *   [data-role="font-size"]      cycles S/M/L
 *   [data-role="theme"]          cycles light/dark/sepia
 *   [data-role="search"]         opens the search overlay
 *   [data-role="toc-open"]       opens the TOC overlay
 *   [data-role="scrivener-open"] dispatches window "scrivener:open"
 *   [data-role="provenance"]     data-provenance-url; rendered "limb: X"
 *   [data-role="limb-switcher"]  data-limbs = JSON [{name,url}]
 */
(function () {
    "use strict";

    var LS_THEME     = "cookbook.theme";
    var LS_FONTSIZE  = "cookbook.fontsize";
    var LS_PROGRESS  = "cookbook.progress";
    var LS_BOOKMARKS = "cookbook.bookmarks";

    var THEMES = ["light", "dark", "sepia"];
    var SIZES  = ["S", "M", "L"];

    var root = document.documentElement;
    var chapterKey = location.pathname;

    // -- READER ROOT (relative prefix from THIS page back to the dist root) --
    // Emitted by templates._head as <meta name="uni-reader-root" content="...">.
    // The value is what build.py's root_for() computed for the emitting page
    // (e.g. "" for index.html, "../" for chapter/na-05.html, "../" for
    // plate/pl-01.html). Every same-origin asset URL app.js reaches for
    // (search-index.json, _provenance.json) is composed from this prefix, so
    // the fetch resolves whether the site is served at /glass/cookbook/ on a
    // fleet limb or at / from a plain `python -m http.server -d reader/dist`.
    // A hardcoded absolute path would break one of the two deployments.
    function readerRoot() {
        try {
            var m = document.querySelector('meta[name="uni-reader-root"]');
            var v = m && m.getAttribute("content");
            if (typeof v === "string") return v;
        } catch (e) {}
        return "./";
    }
    function readerAssetUrl(rel) {
        // rel is a dist-root-relative path (e.g. "search-index.json"). Compose
        // it with the page's own root prefix; use document.baseURI as the base
        // so the final URL is absolute for XHR/fetch consumers.
        try {
            return new URL(readerRoot() + rel, document.baseURI).toString();
        } catch (e) {
            return readerRoot() + rel;
        }
    }

    // -- localStorage helpers (fail-closed if storage is denied) ------------

    function lsGet(key, fallback) {
        try {
            var v = window.localStorage.getItem(key);
            return v === null ? fallback : v;
        } catch (e) { return fallback; }
    }
    function lsSet(key, value) {
        try { window.localStorage.setItem(key, String(value)); } catch (e) {}
    }
    function lsGetJSON(key, fallback) {
        var raw = lsGet(key, null);
        if (raw === null) return fallback;
        try { return JSON.parse(raw); } catch (e) { return fallback; }
    }
    function lsSetJSON(key, value) {
        try { lsSet(key, JSON.stringify(value)); } catch (e) {}
    }

    function warn(msg) {
        try { console.warn("[cookbookReader] " + msg); } catch (e) {}
    }

    function q(sel, scope) { return (scope || document).querySelector(sel); }
    function qa(sel, scope) {
        return Array.prototype.slice.call((scope || document).querySelectorAll(sel));
    }

    // -- THEME ---------------------------------------------------------------

    function initialTheme() {
        var t = lsGet(LS_THEME, null);
        if (t && THEMES.indexOf(t) !== -1) return t;
        try {
            if (window.matchMedia
                && window.matchMedia("(prefers-color-scheme: dark)").matches) {
                return "dark";
            }
        } catch (e) {}
        return "light";
    }
    function applyTheme(t) {
        root.setAttribute("data-theme", t);
        lsSet(LS_THEME, t);
        try {
            window.dispatchEvent(new CustomEvent("cookbook:themechange",
                                                 { detail: { theme: t } }));
        } catch (e) {}
    }
    function cycleTheme() {
        var cur = root.getAttribute("data-theme") || "light";
        var i = THEMES.indexOf(cur);
        applyTheme(THEMES[(i + 1) % THEMES.length]);
    }

    // -- FONT SIZE -----------------------------------------------------------

    function initialFontSize() {
        var s = lsGet(LS_FONTSIZE, "M");
        return SIZES.indexOf(s) === -1 ? "M" : s;
    }
    function applyFontSize(s) {
        root.setAttribute("data-fontsize", s);
        lsSet(LS_FONTSIZE, s);
    }
    function bumpFontSize(delta) {
        var cur = root.getAttribute("data-fontsize") || "M";
        var i = SIZES.indexOf(cur);
        if (i === -1) i = 1;
        var next = Math.max(0, Math.min(SIZES.length - 1, i + delta));
        applyFontSize(SIZES[next]);
    }

    // -- READING PROGRESS ----------------------------------------------------

    function scrollFraction() {
        var doc = document.documentElement;
        var body = document.body || {};
        var scrolled = (window.pageYOffset || doc.scrollTop || body.scrollTop || 0);
        var height   = Math.max(
            (doc.scrollHeight || 0) - (doc.clientHeight || window.innerHeight || 0),
            1);
        var f = scrolled / height;
        if (!isFinite(f) || f < 0) return 0;
        if (f > 1) return 1;
        return f;
    }
    function updateProgressBar(bar, f) {
        bar.style.width = (f * 100).toFixed(2) + "%";
    }
    function saveProgress(f) {
        var all = lsGetJSON(LS_PROGRESS, {});
        if (!all || typeof all !== "object") all = {};
        all[chapterKey] = { pct: Math.round(f * 1000) / 1000,
                            title: document.title || chapterKey,
                            when: Date.now() };
        lsSetJSON(LS_PROGRESS, all);
    }
    function loadProgress() {
        var all = lsGetJSON(LS_PROGRESS, {});
        if (!all || typeof all !== "object") return null;
        var e = all[chapterKey];
        return (e && typeof e.pct === "number") ? e : null;
    }

    function initProgress() {
        var bar = q('[data-role="reading-progress"]');
        if (!bar) return;
        updateProgressBar(bar, scrollFraction());
        var raf = 0;
        function onScroll() {
            if (raf) return;
            raf = window.requestAnimationFrame(function () {
                raf = 0;
                updateProgressBar(bar, scrollFraction());
            });
        }
        window.addEventListener("scroll", onScroll, { passive: true });
        window.addEventListener("resize", onScroll, { passive: true });
        window.addEventListener("beforeunload", function () {
            saveProgress(scrollFraction());
        });

        // Offer a "resume" pill if we have prior progress on this chapter.
        var prior = loadProgress();
        if (prior && prior.pct > 0.02 && prior.pct < 0.98) {
            showResumePill(prior.pct);
        }
    }

    function showResumePill(pct) {
        var pill = document.createElement("div");
        pill.className = "cookbook-pill cookbook-pill-resume";
        pill.setAttribute("role", "status");
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "cookbook-pill-button";
        btn.textContent = "Resume where you left off ("
                          + Math.round(pct * 100) + "%)";
        btn.addEventListener("click", function () {
            var doc = document.documentElement;
            var target = pct * ((doc.scrollHeight || 0)
                                - (doc.clientHeight || window.innerHeight || 0));
            window.scrollTo({ top: target, behavior: "smooth" });
            hidePill(pill);
        });
        pill.appendChild(btn);
        document.body.appendChild(pill);
        setTimeout(function () { hidePill(pill); }, 4000);
    }
    function hidePill(pill) {
        if (!pill.parentNode) return;
        pill.parentNode.removeChild(pill);
    }

    // -- CONTINUE READING (index page) --------------------------------------

    function initContinueReading() {
        // Only shown on index pages. We look for a mount that templates.py
        // may drop in; if absent, we skip. (Do not synthesise a card into
        // an arbitrary place.)
        var mount = q('[data-role="continue-reading"]');
        if (!mount) return;
        var all = lsGetJSON(LS_PROGRESS, {});
        if (!all || typeof all !== "object") return;
        var best = null;
        Object.keys(all).forEach(function (k) {
            var e = all[k];
            if (!e || typeof e.pct !== "number") return;
            if (e.pct <= 0.02 || e.pct >= 0.98) return;
            if (!best || (e.when || 0) > (best.when || 0)) {
                best = { path: k, title: e.title || k, pct: e.pct, when: e.when };
            }
        });
        if (!best) return;
        var card = document.createElement("a");
        card.className = "cookbook-continue-card";
        card.setAttribute("href", best.path);
        var lbl = document.createElement("span");
        lbl.className = "cookbook-continue-label";
        lbl.textContent = "Continue reading";
        var ttl = document.createElement("span");
        ttl.className = "cookbook-continue-title";
        ttl.textContent = best.title;
        var pct = document.createElement("span");
        pct.className = "cookbook-continue-pct";
        pct.textContent = Math.round(best.pct * 100) + "%";
        card.appendChild(lbl);
        card.appendChild(ttl);
        card.appendChild(pct);
        mount.appendChild(card);
    }

    // -- BOOKMARKS -----------------------------------------------------------

    function getBookmarks() {
        var b = lsGetJSON(LS_BOOKMARKS, []);
        return Array.isArray(b) ? b : [];
    }
    function isBookmarked(path) {
        return getBookmarks().some(function (e) { return e && e.path === path; });
    }
    function toggleBookmark() {
        var list = getBookmarks();
        var i = -1;
        for (var j = 0; j < list.length; j++) {
            if (list[j] && list[j].path === chapterKey) { i = j; break; }
        }
        if (i !== -1) {
            list.splice(i, 1);
        } else {
            list.push({ path: chapterKey,
                        title: document.title || chapterKey,
                        when: Date.now() });
        }
        lsSetJSON(LS_BOOKMARKS, list);
        reflectBookmarkState();
    }
    function reflectBookmarkState() {
        qa('[data-role="bookmark"]').forEach(function (el) {
            el.setAttribute("aria-pressed",
                            isBookmarked(chapterKey) ? "true" : "false");
        });
    }

    // -- CHAPTER NAV ---------------------------------------------------------

    function navPrev() { navByRel("prev"); }
    function navNext() { navByRel("next"); }
    function navByRel(rel) {
        var nav = q('[data-role="chapter-nav"]');
        if (!nav) return;
        var href = nav.getAttribute("data-" + rel);
        if (href) { window.location.href = href; }
    }

    // -- OVERLAY PRIMITIVE ---------------------------------------------------
    // One overlay at a time; ESC closes; click-outside closes.

    var openOverlay = null;
    function overlayOpen(kind, buildBody) {
        overlayClose();
        var scrim = document.createElement("div");
        scrim.className = "cookbook-overlay cookbook-overlay-" + kind;
        scrim.setAttribute("role", "dialog");
        scrim.setAttribute("aria-modal", "true");
        var panel = document.createElement("div");
        panel.className = "cookbook-overlay-panel";
        var close = document.createElement("button");
        close.type = "button";
        close.className = "cookbook-overlay-close";
        close.setAttribute("aria-label", "Close");
        close.textContent = "\u00D7"; // multiplication sign, ASCII source
        close.addEventListener("click", overlayClose);
        panel.appendChild(close);
        buildBody(panel);
        scrim.appendChild(panel);
        scrim.addEventListener("click", function (ev) {
            if (ev.target === scrim) overlayClose();
        });
        document.body.appendChild(scrim);
        openOverlay = scrim;
        var focusable = panel.querySelector("input, button, a, [tabindex]");
        if (focusable) { try { focusable.focus(); } catch (e) {} }
    }
    function overlayClose() {
        if (!openOverlay) return;
        if (openOverlay.parentNode) {
            openOverlay.parentNode.removeChild(openOverlay);
        }
        openOverlay = null;
    }

    // -- TOC OVERLAY ---------------------------------------------------------

    function tocOpen() {
        overlayOpen("toc", function (panel) {
            var head = document.createElement("h2");
            head.className = "cookbook-overlay-head";
            head.textContent = "Table of contents";
            panel.appendChild(head);

            // Bookmarks section
            var bms = getBookmarks();
            if (bms.length) {
                var bTitle = document.createElement("h3");
                bTitle.textContent = "Bookmarks";
                panel.appendChild(bTitle);
                var bList = document.createElement("ul");
                bList.className = "cookbook-toc-bookmarks";
                bms.forEach(function (b) {
                    if (!b || !b.path) return;
                    var li = document.createElement("li");
                    var a = document.createElement("a");
                    a.setAttribute("href", b.path);
                    a.textContent = b.title || b.path;
                    li.appendChild(a);
                    bList.appendChild(li);
                });
                panel.appendChild(bList);
            }

            // Corpus tree from the sidebar's data-corpus-tree attribute
            var sidebar = q('[data-role="sidebar"]');
            var tree = [];
            if (sidebar) {
                try {
                    var raw = sidebar.getAttribute("data-corpus-tree");
                    if (raw) tree = JSON.parse(raw) || [];
                } catch (e) { tree = []; }
            }
            var progress = lsGetJSON(LS_PROGRESS, {}) || {};
            var byWing = {};
            tree.forEach(function (row) {
                if (!row || !row.path) return;
                var w = row.wing || "";
                if (!byWing[w]) byWing[w] = [];
                byWing[w].push(row);
            });
            Object.keys(byWing).sort().forEach(function (w) {
                if (w) {
                    var h = document.createElement("h3");
                    h.textContent = w;
                    panel.appendChild(h);
                }
                var ul = document.createElement("ul");
                ul.className = "cookbook-toc-list";
                byWing[w].forEach(function (row) {
                    var li = document.createElement("li");
                    var a = document.createElement("a");
                    a.setAttribute("href", row.path);
                    a.textContent = row.title || row.path;
                    li.appendChild(a);
                    var pr = progress[row.path];
                    if (pr && typeof pr.pct === "number") {
                        var bar = document.createElement("span");
                        bar.className = "cookbook-toc-progress";
                        var fill = document.createElement("span");
                        fill.className = "cookbook-toc-progress-fill";
                        fill.style.width = (pr.pct * 100).toFixed(1) + "%";
                        bar.appendChild(fill);
                        li.appendChild(bar);
                    }
                    ul.appendChild(li);
                });
                panel.appendChild(ul);
            });

            if (!tree.length && !bms.length) {
                var empty = document.createElement("p");
                empty.className = "cookbook-toc-empty";
                empty.textContent = "The corpus tree is not available on this page.";
                panel.appendChild(empty);
            }
        });
    }

    // -- SEARCH OVERLAY ------------------------------------------------------

    var searchIndex = null;    // {loaded: bool, rows: [...], error: null|string}
    var searchDebounce = 0;

    function ensureSearchIndex(cb) {
        if (searchIndex && searchIndex.loaded) { cb(searchIndex); return; }
        if (searchIndex && searchIndex.pending) {
            searchIndex.pending.push(cb); return;
        }
        searchIndex = { loaded: false, rows: [], pending: [cb], error: null };
        var req = new XMLHttpRequest();
        try {
            // Same-origin, page-relative URL composed from the reader-root
            // meta tag. An earlier version used absolute "/search-index.json"
            // and 404'd whenever the site was served under a prefix like
            // /glass/cookbook/ (real deployment on every limb).
            req.open("GET", readerAssetUrl("search-index.json"), true);
        } catch (e) {
            searchIndex.error = "unavailable";
            searchIndex.loaded = true;
            flushSearchWaiters();
            return;
        }
        req.onload = function () {
            try {
                var data = JSON.parse(req.responseText);
                searchIndex.rows = Array.isArray(data) ? data : [];
            } catch (e) {
                searchIndex.rows = [];
                searchIndex.error = "malformed";
            }
            searchIndex.loaded = true;
            flushSearchWaiters();
        };
        req.onerror = function () {
            searchIndex.error = "unreachable";
            searchIndex.loaded = true;
            flushSearchWaiters();
        };
        try { req.send(null); } catch (e) {
            searchIndex.error = "send-failed";
            searchIndex.loaded = true;
            flushSearchWaiters();
        }
    }
    function flushSearchWaiters() {
        var pending = (searchIndex && searchIndex.pending) || [];
        searchIndex.pending = null;
        pending.forEach(function (fn) { try { fn(searchIndex); } catch (e) {} });
    }

    function searchOpen(prefill) {
        overlayOpen("search", function (panel) {
            var head = document.createElement("h2");
            head.className = "cookbook-overlay-head";
            head.textContent = "Search";
            panel.appendChild(head);

            var input = document.createElement("input");
            input.type = "search";
            input.className = "cookbook-search-input";
            input.setAttribute("placeholder", "search titles and text");
            input.setAttribute("aria-label", "Search the corpus");
            if (prefill) input.value = prefill;
            panel.appendChild(input);

            var status = document.createElement("p");
            status.className = "cookbook-search-status";
            status.textContent = "Loading search index...";
            panel.appendChild(status);

            var list = document.createElement("ul");
            list.className = "cookbook-search-results";
            panel.appendChild(list);

            function renderResults(query) {
                list.textContent = "";
                if (!searchIndex || !searchIndex.loaded) {
                    status.textContent = "Loading search index...";
                    return;
                }
                if (searchIndex.error) {
                    status.textContent = "Search index is unavailable ("
                                         + searchIndex.error + ").";
                    return;
                }
                if (!query) {
                    status.textContent = searchIndex.rows.length
                                         + " chapters indexed.";
                    return;
                }
                var needle = query.toLowerCase();
                var hits = [];
                for (var i = 0; i < searchIndex.rows.length; i++) {
                    var r = searchIndex.rows[i];
                    if (!r || !r.path) continue;
                    var t = (r.title || "").toLowerCase();
                    var b = (r.body  || "").toLowerCase();
                    var inT = t.indexOf(needle) !== -1;
                    var inB = b.indexOf(needle) !== -1;
                    if (inT || inB) {
                        hits.push({ row: r, titleHit: inT });
                        if (hits.length >= 100) break;
                    }
                }
                status.textContent = hits.length + " match"
                                     + (hits.length === 1 ? "" : "es") + ".";
                hits.forEach(function (h) {
                    var li = document.createElement("li");
                    var a = document.createElement("a");
                    a.setAttribute("href", h.row.path);
                    a.textContent = h.row.title || h.row.path;
                    li.appendChild(a);
                    if (!h.titleHit && h.row.body) {
                        var snip = extractSnippet(h.row.body, needle);
                        if (snip) {
                            var s = document.createElement("span");
                            s.className = "cookbook-search-snippet";
                            s.textContent = snip;
                            li.appendChild(s);
                        }
                    }
                    list.appendChild(li);
                });
            }

            input.addEventListener("input", function () {
                if (searchDebounce) clearTimeout(searchDebounce);
                var v = input.value.trim();
                searchDebounce = setTimeout(function () {
                    renderResults(v);
                }, 60);
            });

            ensureSearchIndex(function () {
                renderResults(input.value.trim());
            });
        });
    }

    function extractSnippet(body, needle) {
        var lower = body.toLowerCase();
        var i = lower.indexOf(needle);
        if (i === -1) return "";
        var start = Math.max(0, i - 40);
        var end   = Math.min(body.length, i + needle.length + 60);
        var s = body.slice(start, end);
        if (start > 0) s = "..." + s;
        if (end < body.length) s = s + "...";
        return s;
    }

    // -- PROVENANCE + LIMB SWITCHER -----------------------------------------

    function initProvenance() {
        var el = q('[data-role="provenance"]');
        if (!el) return;
        var url = el.getAttribute("data-provenance-url");
        if (!url) return;
        // Reject anything that is not a relative or same-origin URL.
        if (/^[a-z]+:/i.test(url) || url.indexOf("//") === 0) {
            warn("provenance url rejected (not same-origin): " + url);
            return;
        }
        var req = new XMLHttpRequest();
        try { req.open("GET", url, true); }
        catch (e) { warn("provenance open failed"); return; }
        req.onload = function () {
            try {
                var data = JSON.parse(req.responseText);
                var limb = data.limb || data.host || "unknown";
                var commit = (data.commit || "").slice(0, 7);
                var line = "limb: " + limb;
                if (commit) line += " - commit " + commit;
                el.textContent = line;
            } catch (e) { /* leave whatever the server render put there */ }
        };
        req.onerror = function () { /* fail-closed */ };
        try { req.send(null); } catch (e) {}
    }

    function initLimbSwitcher() {
        var el = q('[data-role="limb-switcher"]');
        if (!el) return;
        var limbs = [];
        try {
            var raw = el.getAttribute("data-limbs");
            if (raw) limbs = JSON.parse(raw) || [];
        } catch (e) { limbs = []; }
        if (!limbs.length) return;
        // Build a plain list of links. Do NOT probe them from JS.
        el.textContent = "";
        var ul = document.createElement("ul");
        ul.className = "cookbook-limbs-list";
        limbs.forEach(function (l) {
            if (!l || !l.url) return;
            var li = document.createElement("li");
            var a = document.createElement("a");
            a.setAttribute("href", l.url);
            a.setAttribute("rel", "noopener");
            a.textContent = l.name || l.url;
            li.appendChild(a);
            ul.appendChild(li);
        });
        el.appendChild(ul);
    }

    // -- SCRIVENER INTEGRATION ----------------------------------------------

    function scrivenerOpen() {
        var anchor = chapterKey;
        // Nearest heading id above the current scroll top, if any.
        var headings = qa("h1[id], h2[id], h3[id]");
        var top = window.pageYOffset || 0;
        var nearest = null;
        for (var i = 0; i < headings.length; i++) {
            var r = headings[i].getBoundingClientRect();
            if (r.top + top <= top + 8) nearest = headings[i];
            else break;
        }
        if (nearest && nearest.id) anchor = chapterKey + "#" + nearest.id;
        try {
            window.dispatchEvent(new CustomEvent("scrivener:open",
                { detail: { anchor: anchor, title: document.title || "" } }));
        } catch (e) { warn("scrivener event dispatch failed"); }
    }

    // -- WIRING --------------------------------------------------------------

    function bindControls() {
        var t = q('[data-role="theme"]');
        if (t) t.addEventListener("click", cycleTheme);

        var f = q('[data-role="font-size"]');
        if (f) f.addEventListener("click", function () {
            var cur = root.getAttribute("data-fontsize") || "M";
            var i = SIZES.indexOf(cur);
            if (i === -1) i = 1;
            applyFontSize(SIZES[(i + 1) % SIZES.length]);
        });

        var s = q('[data-role="search"]');
        if (s) s.addEventListener("click", function () { searchOpen(""); });

        var g = q('[data-role="toc-open"]');
        if (g) g.addEventListener("click", tocOpen);

        var scr = q('[data-role="scrivener-open"]');
        if (scr) scr.addEventListener("click", scrivenerOpen);

        qa('[data-role="bookmark"]').forEach(function (b) {
            b.addEventListener("click", toggleBookmark);
        });

        var nav = q('[data-role="chapter-nav"]');
        if (nav) {
            qa('[data-nav="prev"]', nav).forEach(function (el) {
                el.addEventListener("click", function (ev) {
                    ev.preventDefault(); navPrev();
                });
            });
            qa('[data-nav="next"]', nav).forEach(function (el) {
                el.addEventListener("click", function (ev) {
                    ev.preventDefault(); navNext();
                });
            });
        }
    }

    function isTypingTarget(el) {
        if (!el) return false;
        var tag = (el.tagName || "").toLowerCase();
        if (tag === "input" || tag === "textarea" || tag === "select") return true;
        if (el.isContentEditable) return true;
        return false;
    }

    function bindKeyboard() {
        document.addEventListener("keydown", function (ev) {
            if (ev.defaultPrevented) return;
            if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
            var key = ev.key;
            if (key === "Escape") { overlayClose(); return; }
            if (isTypingTarget(ev.target)) return;

            switch (key) {
                case "j": case "ArrowRight": navNext(); break;
                case "k": case "ArrowLeft":  navPrev(); break;
                case "/": case "f":
                    ev.preventDefault(); searchOpen(""); break;
                case "b": toggleBookmark(); break;
                case "g": tocOpen(); break;
                case "t": cycleTheme(); break;
                case "+": case "=": bumpFontSize(+1); break;
                case "-": case "_": bumpFontSize(-1); break;
                default: return;
            }
        });
    }

    function init() {
        applyTheme(initialTheme());
        applyFontSize(initialFontSize());
        try { bindControls();       } catch (e) { warn("bindControls: " + e); }
        try { bindKeyboard();       } catch (e) { warn("bindKeyboard: " + e); }
        try { initProgress();       } catch (e) { warn("initProgress: " + e); }
        try { initContinueReading(); } catch (e) { warn("initContinue: " + e); }
        try { initProvenance();     } catch (e) { warn("initProvenance: " + e); }
        try { initLimbSwitcher();   } catch (e) { warn("initLimbSwitcher: " + e); }
        try { reflectBookmarkState(); } catch (e) {}
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }

    // Minimal public surface for the Scrivener app and tests to introspect.
    window.cookbookReader = {
        cycleTheme:     cycleTheme,
        applyTheme:     applyTheme,
        bumpFontSize:   bumpFontSize,
        toggleBookmark: toggleBookmark,
        openTOC:        tocOpen,
        openSearch:     searchOpen,
        openScrivener:  scrivenerOpen,
        getProgress:    loadProgress,
        getBookmarks:   getBookmarks
    };
}());

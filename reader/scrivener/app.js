/*
 * scrivener/app.js -- HONEST-store note-taker for the UNI Encyclopedia-Cookbook.
 *
 * Runtime: vanilla JS, no dependencies, pure ASCII. All persistence is in the
 * browser's IndexedDB (database "cookbook.scrivener", store "notes"). There is
 * NO server endpoint in v1; nothing this file does can write back to the
 * generator's filesystem. The read-only invariant of the corpus reader stands.
 *
 * Doctrine (surfaced in UI text below):
 *   - This is the HONEST store. Sovereign from the TRUE store cookbook.
 *   - Append-only. To correct a note, capture a NEW note with supersedes=<old>.
 *   - Predictions and hypotheses require a falsifier or Save is disabled.
 *   - The doctrine's banned author-voice tokens (v*rified, pr*ven, etc.) do
 *     not appear anywhere in this UI's copy or in its own comments.
 */
(function () {
  "use strict";

  // ------------------------------------------------------------------
  // Constants
  // ------------------------------------------------------------------
  var DB_NAME = "cookbook.scrivener";
  var DB_VERSION = 1;
  var STORE = "notes";
  var TYPES = ["note", "question", "prediction", "theory",
               "hypothesis", "observation"];
  var TYPES_REQ_FALSIFIER = { prediction: true, hypothesis: true };
  var SCHEMA_VERSION = "1";

  // ------------------------------------------------------------------
  // Utilities
  // ------------------------------------------------------------------
  function iso_utc(d) {
    d = d || new Date();
    // 2026-07-16T12:34:56.000Z -> keep milliseconds, always UTC
    return d.toISOString();
  }

  function stamp_for_filename(d) {
    d = d || new Date();
    // YYYY-MM-DDTHHMMSSZ
    var s = d.toISOString();
    return s.replace(/[-:]/g, "").replace(/\.\d+Z$/, "Z")
            .replace("T", "T");
  }

  function gen_id() {
    // Time-prefixed random ID. Sorts lexicographically by time.
    // Format: <13-hex ms><16-hex random>  (29 chars total)
    var ms = Date.now();
    var hi = ("0000000000000" + ms.toString(16)).slice(-13);
    var buf = new Uint8Array(8);
    (window.crypto || window.msCrypto).getRandomValues(buf);
    var rnd = "";
    for (var i = 0; i < buf.length; i++) {
      rnd += ("0" + buf[i].toString(16)).slice(-2);
    }
    return hi + rnd;
  }

  function esc_html(s) {
    if (s === null || s === undefined) return "";
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function parse_tags(s) {
    if (!s) return [];
    return String(s).split(",")
      .map(function (t) { return t.trim(); })
      .filter(function (t) { return t.length > 0; });
  }

  function tags_to_string(a) {
    if (!a || !a.length) return "";
    return a.join(", ");
  }

  function download_blob(name, mime, text) {
    var blob = new Blob([text], { type: mime });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  function device_hint() {
    // Prefer a page-supplied hint (data-scrivener-device on <html>),
    // then fall back to a short UA tail.
    var el = document.documentElement;
    var h = (el && el.getAttribute("data-scrivener-device")) || "";
    if (h) return h;
    var ua = navigator.userAgent || "";
    return ua.slice(-64);
  }

  function anchor_from_page() {
    var el = document.documentElement;
    var chap = (el && el.getAttribute("data-chapter-id")) || "";
    var head = "";
    try {
      if (location.hash && location.hash.length > 1) {
        head = decodeURIComponent(location.hash.slice(1));
      }
    } catch (e) { head = ""; }
    var a = { url: location.pathname + location.hash };
    if (chap) a.chapter_id = chap;
    if (head) a.heading_id = head;
    return a;
  }

  // ------------------------------------------------------------------
  // IndexedDB wrapper (promise-based, no deps)
  // ------------------------------------------------------------------
  var _db_promise = null;

  function open_db() {
    if (_db_promise) return _db_promise;
    if (!window.indexedDB) {
      _db_promise = Promise.reject(new Error("IndexedDB is not available."));
      return _db_promise;
    }
    _db_promise = new Promise(function (resolve, reject) {
      var req = indexedDB.open(DB_NAME, DB_VERSION);
      req.onupgradeneeded = function (ev) {
        var db = req.result;
        if (!db.objectStoreNames.contains(STORE)) {
          var os = db.createObjectStore(STORE, { keyPath: "id" });
          os.createIndex("by_created", "created_utc", { unique: false });
          os.createIndex("by_type", "type", { unique: false });
        }
      };
      req.onsuccess = function () { resolve(req.result); };
      req.onerror = function () { reject(req.error); };
    });
    return _db_promise;
  }

  function idb_add(note) {
    return open_db().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(STORE, "readwrite");
        var os = tx.objectStore(STORE);
        var req = os.add(note);
        req.onsuccess = function () { resolve(note); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function idb_get(id) {
    return open_db().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(STORE, "readonly");
        var req = tx.objectStore(STORE).get(id);
        req.onsuccess = function () { resolve(req.result || null); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function idb_get_all() {
    return open_db().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(STORE, "readonly");
        var req = tx.objectStore(STORE).getAll();
        req.onsuccess = function () { resolve(req.result || []); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function idb_import_batch(notes) {
    // Upsert-by-id but append-only: an id already present is IGNORED, not
    // overwritten. Reports counts. Uses one transaction so we roll back on
    // an infrastructure error (not on a duplicate -- those are expected).
    return open_db().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(STORE, "readwrite");
        var os = tx.objectStore(STORE);
        var counts = { new: 0, duplicate: 0, malformed: 0 };
        var errored = false;
        function step(i) {
          if (i >= notes.length) return;
          var n = notes[i];
          if (!validate_note_shape(n)) {
            counts.malformed += 1;
            step(i + 1);
            return;
          }
          var getReq = os.get(n.id);
          getReq.onsuccess = function () {
            if (getReq.result) {
              counts.duplicate += 1;
              step(i + 1);
              return;
            }
            var addReq = os.add(n);
            addReq.onsuccess = function () {
              counts.new += 1;
              step(i + 1);
            };
            addReq.onerror = function () {
              // Rare race: treat as duplicate rather than kill the batch.
              counts.duplicate += 1;
              addReq.preventDefault && addReq.preventDefault();
              step(i + 1);
            };
          };
          getReq.onerror = function () {
            errored = true;
            reject(getReq.error);
          };
        }
        tx.oncomplete = function () {
          if (!errored) resolve(counts);
        };
        tx.onerror = function () {
          if (!errored) reject(tx.error);
        };
        if (notes.length === 0) {
          // Nothing to iterate; the transaction will complete immediately.
        } else {
          step(0);
        }
      });
    });
  }

  // Hidden dev API only. The UI never calls this; the doctrine forbids it.
  function _dev_delete(id) {
    return open_db().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(STORE, "readwrite");
        var req = tx.objectStore(STORE).delete(id);
        req.onsuccess = function () { resolve(true); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function validate_note_shape(n) {
    if (!n || typeof n !== "object") return false;
    if (typeof n.id !== "string" || !n.id) return false;
    if (typeof n.created_utc !== "string" || !n.created_utc) return false;
    if (TYPES.indexOf(n.type) === -1) return false;
    if (typeof n.title !== "string") return false;
    if (typeof n.body !== "string") return false;
    if (!Array.isArray(n.tags)) return false;
    if (n.store !== "HONEST") return false;
    if (TYPES_REQ_FALSIFIER[n.type] && (!n.falsifier || !n.falsifier.trim())) {
      return false;
    }
    return true;
  }

  // ------------------------------------------------------------------
  // Modal: capture UX
  // ------------------------------------------------------------------
  function ensure_modal_root() {
    var host = document.querySelector('[data-role="scrivener-modal"]');
    if (!host) {
      host = document.createElement("div");
      host.setAttribute("data-role", "scrivener-modal");
      document.body.appendChild(host);
    }
    return host;
  }

  function close_modal() {
    var host = document.querySelector('[data-role="scrivener-modal"]');
    if (host) host.innerHTML = "";
    document.documentElement.classList.remove("scrivener-modal-open");
  }

  function toast(msg) {
    var t = document.createElement("div");
    t.className = "scrivener-toast";
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function () {
      t.classList.add("scrivener-toast-fade");
    }, 1200);
    setTimeout(function () {
      if (t.parentNode) t.parentNode.removeChild(t);
    }, 2000);
  }

  function build_modal(opts) {
    opts = opts || {};
    var host = ensure_modal_root();
    host.innerHTML = "";
    document.documentElement.classList.add("scrivener-modal-open");

    var back = document.createElement("div");
    back.className = "scrivener-backdrop";
    back.setAttribute("role", "presentation");

    var panel = document.createElement("div");
    panel.className = "scrivener-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-modal", "true");
    panel.setAttribute("aria-label", "Scrivener: capture an HONEST note");

    var initial_type = opts.type || "note";
    if (TYPES.indexOf(initial_type) === -1) initial_type = "note";

    panel.innerHTML = [
      '<div class="scrivener-head">',
      '  <h2 class="scrivener-title">Scrivener</h2>',
      '  <button type="button" class="scrivener-close"',
      '          aria-label="close">x</button>',
      '</div>',
      '<p class="scrivener-doctrine">',
      '  This captures HONEST signals. It is sovereign from the TRUE-store',
      '  cookbook. Notes are never calibrated; corrections happen by',
      '  superseding, and the old note stays on record.',
      '</p>',
      '<div class="scrivener-body">',
      '  <label class="scrivener-label">Type</label>',
      '  <div class="scrivener-types" data-role="type-chips"></div>',

      '  <label class="scrivener-label" for="sc-title">Title</label>',
      '  <input id="sc-title" class="scrivener-input" type="text"',
      '         maxlength="240" autocomplete="off">',

      '  <label class="scrivener-label" for="sc-body">Body</label>',
      '  <textarea id="sc-body" class="scrivener-textarea" rows="8"',
      '            placeholder="Markdown-ish plain text. This is stored',
      ' as-is; the Scrivener does not render it."></textarea>',

      '  <label class="scrivener-label" for="sc-tags">',
      '    Tags <span class="scrivener-hint">(comma-separated)</span>',
      '  </label>',
      '  <input id="sc-tags" class="scrivener-input" type="text"',
      '         autocomplete="off">',

      '  <label class="scrivener-label" for="sc-anchor">',
      '    Anchor <span class="scrivener-hint">(auto-filled; clear to unset)</span>',
      '  </label>',
      '  <input id="sc-anchor" class="scrivener-input" type="text"',
      '         autocomplete="off">',

      '  <div class="scrivener-falsifier" data-role="falsifier-row" hidden>',
      '    <label class="scrivener-label" for="sc-fals">Falsifier</label>',
      '    <input id="sc-fals" class="scrivener-input" type="text"',
      '           autocomplete="off">',
      '    <p class="scrivener-hint">',
      '      For a prediction or hypothesis, name the observation that would',
      '      refute it. Without a falsifier, it is inadmissible.',
      '    </p>',
      '  </div>',

      '  <label class="scrivener-inline">',
      '    <input id="sc-loc" type="checkbox">',
      '    <span>Attach my current location (asks for permission)</span>',
      '  </label>',

      '  <p class="scrivener-supersede" data-role="supersede-note" hidden>',
      '    Superseding note <code data-role="supersede-id"></code>. The old',
      '    note stays on record.',
      '  </p>',
      '</div>',
      '<div class="scrivener-actions">',
      '  <button type="button" class="scrivener-btn scrivener-cancel">',
      '    Cancel</button>',
      '  <button type="button" class="scrivener-btn scrivener-save"',
      '          data-role="save" disabled>Save</button>',
      '</div>'
    ].join("\n");

    host.appendChild(back);
    host.appendChild(panel);

    // Build type chips
    var chip_host = panel.querySelector('[data-role="type-chips"]');
    var current_type = initial_type;
    TYPES.forEach(function (t) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "scrivener-chip";
      b.setAttribute("data-type", t);
      if (t === "observation") {
        b.title = "of nature -- field capture";
      }
      b.textContent = t;
      if (t === current_type) b.classList.add("scrivener-chip-on");
      b.addEventListener("click", function () {
        current_type = t;
        Array.prototype.forEach.call(
          chip_host.querySelectorAll(".scrivener-chip"),
          function (x) { x.classList.remove("scrivener-chip-on"); });
        b.classList.add("scrivener-chip-on");
        update_falsifier_visibility();
        update_body_placeholder();
        update_save_state();
      });
      chip_host.appendChild(b);
    });

    var titleEl = panel.querySelector("#sc-title");
    var bodyEl = panel.querySelector("#sc-body");
    var tagsEl = panel.querySelector("#sc-tags");
    var anchorEl = panel.querySelector("#sc-anchor");
    var falsEl = panel.querySelector("#sc-fals");
    var locEl = panel.querySelector("#sc-loc");
    var falsRow = panel.querySelector('[data-role="falsifier-row"]');
    var saveBtn = panel.querySelector('[data-role="save"]');
    var supNote = panel.querySelector('[data-role="supersede-note"]');
    var supIdEl = panel.querySelector('[data-role="supersede-id"]');

    // Pre-fill
    if (opts.title) titleEl.value = opts.title;
    if (opts.body) bodyEl.value = opts.body;
    if (opts.tags && opts.tags.length) tagsEl.value = tags_to_string(opts.tags);
    var a = opts.anchor || anchor_from_page();
    anchorEl.value = format_anchor(a);
    if (opts.supersedes) {
      supNote.hidden = false;
      supIdEl.textContent = opts.supersedes;
    }

    function update_falsifier_visibility() {
      var need = !!TYPES_REQ_FALSIFIER[current_type];
      falsRow.hidden = !need;
    }

    function update_body_placeholder() {
      if (current_type === "observation") {
        bodyEl.setAttribute(
          "placeholder",
          "What did you observe of nature? What made it surprising?");
      } else {
        bodyEl.setAttribute(
          "placeholder",
          "Markdown-ish plain text. This is stored as-is; the Scrivener"
          + " does not render it.");
      }
    }

    function update_save_state() {
      var ok = titleEl.value.trim().length > 0
             || bodyEl.value.trim().length > 0;
      if (TYPES_REQ_FALSIFIER[current_type]) {
        ok = ok && falsEl.value.trim().length > 0;
      }
      saveBtn.disabled = !ok;
    }

    titleEl.addEventListener("input", update_save_state);
    bodyEl.addEventListener("input", update_save_state);
    falsEl.addEventListener("input", update_save_state);

    panel.querySelector(".scrivener-close")
         .addEventListener("click", close_modal);
    panel.querySelector(".scrivener-cancel")
         .addEventListener("click", close_modal);
    back.addEventListener("click", close_modal);

    // ESC to close
    function esc_handler(ev) {
      if (ev.key === "Escape") {
        close_modal();
        document.removeEventListener("keydown", esc_handler);
      }
    }
    document.addEventListener("keydown", esc_handler);

    saveBtn.addEventListener("click", function () {
      var note = {
        id: gen_id(),
        created_utc: iso_utc(),
        type: current_type,
        title: titleEl.value.trim(),
        body: bodyEl.value,
        tags: parse_tags(tagsEl.value),
        anchor: parse_anchor_input(anchorEl.value.trim()),
        falsifier: falsEl.value.trim(),
        supersedes: opts.supersedes || "",
        location: {},
        device_hint: device_hint(),
        store: "HONEST"
      };

      function persist() {
        if (!window.indexedDB) {
          // Fallback: download this note as a JSON so nothing is lost.
          var blob = JSON.stringify({
            schema_version: SCHEMA_VERSION,
            exported_utc: iso_utc(),
            store: "HONEST",
            notes: [note],
            note: "IndexedDB unavailable; single-note fallback export."
          }, null, 2);
          download_blob("scrivener-note-" + note.id + ".json",
                        "application/json", blob);
          toast("captured (fallback download)");
          close_modal();
          if (typeof opts.on_save === "function") opts.on_save(note);
          return;
        }
        idb_add(note).then(function () {
          toast("captured");
          close_modal();
          if (typeof opts.on_save === "function") opts.on_save(note);
          window.dispatchEvent(new CustomEvent("scrivener:saved",
                                               { detail: { id: note.id } }));
        }).catch(function (err) {
          alert("Save failed: " + (err && err.message ? err.message
                                                     : String(err)));
        });
      }

      if (locEl.checked && navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (pos) {
          note.location = {
            lat: pos.coords.latitude,
            lng: pos.coords.longitude,
            acc_m: pos.coords.accuracy
          };
          persist();
        }, function () {
          // User denied or timeout; save without location.
          persist();
        }, { timeout: 5000, enableHighAccuracy: false });
      } else {
        persist();
      }
    });

    update_falsifier_visibility();
    update_body_placeholder();
    update_save_state();
    setTimeout(function () { titleEl.focus(); }, 0);
  }

  function format_anchor(a) {
    if (!a) return "";
    var parts = [];
    if (a.chapter_id) parts.push("chapter=" + a.chapter_id);
    if (a.heading_id) parts.push("heading=" + a.heading_id);
    if (a.url) parts.push("url=" + a.url);
    return parts.join(" | ");
  }

  function parse_anchor_input(s) {
    if (!s) return {};
    var out = {};
    s.split("|").forEach(function (chunk) {
      var kv = chunk.trim().split("=");
      if (kv.length < 2) return;
      var k = kv[0].trim();
      var v = kv.slice(1).join("=").trim();
      if (k === "chapter") out.chapter_id = v;
      else if (k === "heading") out.heading_id = v;
      else if (k === "url") out.url = v;
    });
    return out;
  }

  // ------------------------------------------------------------------
  // Floating capture button (mounts on any page with app.js present)
  // ------------------------------------------------------------------
  function mount_floating_button() {
    if (document.querySelector('[data-role="scrivener-fab"]')) return;
    if (document.body.getAttribute("data-scrivener-no-fab") === "1") return;
    var b = document.createElement("button");
    b.type = "button";
    b.setAttribute("data-role", "scrivener-fab");
    b.className = "scrivener-fab";
    b.title = "Scrivener: capture an HONEST note";
    b.setAttribute("aria-label", "open Scrivener");
    b.textContent = "S";
    b.addEventListener("click", function () { build_modal({}); });
    document.body.appendChild(b);
  }

  // ------------------------------------------------------------------
  // List view (mounts if [data-role="scrivener-list"] present on the page)
  // ------------------------------------------------------------------
  function build_list(container) {
    container.innerHTML = "";

    var head = document.createElement("div");
    head.className = "scrivener-list-head";
    head.innerHTML = [
      '<div class="scrivener-list-tools">',
      '  <label class="scrivener-inline">',
      '    <span>Filter:</span>',
      '    <select data-role="filter-type">',
      '      <option value="">all</option>',
      TYPES.map(function (t) {
        return '      <option value="' + esc_html(t) + '">'
             + esc_html(t) + '</option>';
      }).join("\n"),
      '    </select>',
      '  </label>',
      '  <label class="scrivener-inline">',
      '    <span>Search:</span>',
      '    <input type="text" data-role="filter-q" class="scrivener-input">',
      '  </label>',
      '</div>',
      '<div class="scrivener-list-actions">',
      '  <button type="button" class="scrivener-btn" data-role="new-note">',
      '    New note</button>',
      '  <button type="button" class="scrivener-btn" data-role="ex-json">',
      '    Export JSON</button>',
      '  <button type="button" class="scrivener-btn" data-role="ex-md">',
      '    Export Markdown</button>',
      '  <label class="scrivener-btn scrivener-file-btn">',
      '    Import JSON',
      '    <input type="file" data-role="im-json" accept=".json,application/json"',
      '           hidden>',
      '  </label>',
      '</div>',
      '<p class="scrivener-doctrine scrivener-list-doctrine">',
      '  HONEST store. Sovereign from the TRUE-store cookbook. Append-only:',
      '  a note is never edited; a correction is a NEW note that supersedes',
      '  the old, and the old one stays on record.',
      '</p>'
    ].join("\n");
    container.appendChild(head);

    var listEl = document.createElement("div");
    listEl.className = "scrivener-list";
    listEl.setAttribute("data-role", "list");
    container.appendChild(listEl);

    var state = { notes: [], superseded_by: {}, filter_type: "", q: "" };

    function refresh() {
      if (!window.indexedDB) {
        listEl.innerHTML = '<p class="scrivener-empty">IndexedDB is not'
          + ' available in this browser, so nothing is stored locally. Use'
          + ' the capture modal\'s download fallback to keep notes.</p>';
        return;
      }
      idb_get_all().then(function (arr) {
        state.notes = arr.slice().sort(function (a, b) {
          return a.created_utc < b.created_utc ? 1
               : a.created_utc > b.created_utc ? -1 : 0;
        });
        state.superseded_by = {};
        arr.forEach(function (n) {
          if (n.supersedes) {
            state.superseded_by[n.supersedes] = n.id;
          }
        });
        render();
      }).catch(function (err) {
        listEl.innerHTML = '<p class="scrivener-empty">List failed: '
          + esc_html(err && err.message ? err.message : String(err)) + '</p>';
      });
    }

    function render() {
      var q = state.q.toLowerCase();
      var ft = state.filter_type;
      var rows = state.notes.filter(function (n) {
        if (ft && n.type !== ft) return false;
        if (!q) return true;
        var hay = (n.title + " " + n.body + " "
                 + (n.tags || []).join(" ")).toLowerCase();
        return hay.indexOf(q) !== -1;
      });
      if (!rows.length) {
        listEl.innerHTML = '<p class="scrivener-empty">No notes yet.</p>';
        return;
      }
      listEl.innerHTML = "";
      rows.forEach(function (n) {
        var row = document.createElement("details");
        row.className = "scrivener-row";
        row.setAttribute("data-id", n.id);
        var supBy = state.superseded_by[n.id];
        var supByHtml = supBy
          ? '<span class="scrivener-badge scrivener-badge-super">superseded'
            + ' by ' + esc_html(supBy.slice(0, 12)) + '</span>'
          : "";
        var supHtml = n.supersedes
          ? '<span class="scrivener-badge">supersedes '
            + esc_html(n.supersedes.slice(0, 12)) + '</span>'
          : "";
        var falsHtml = n.falsifier
          ? '<div class="scrivener-meta-line"><b>falsifier:</b> '
            + esc_html(n.falsifier) + '</div>'
          : "";
        var anchorStr = format_anchor(n.anchor || {});
        var anchorHtml = anchorStr
          ? '<div class="scrivener-meta-line"><b>anchor:</b> '
            + esc_html(anchorStr) + '</div>'
          : "";
        var locHtml = (n.location && (n.location.lat || n.location.lng))
          ? '<div class="scrivener-meta-line"><b>location:</b> '
            + esc_html(String(n.location.lat)) + ', '
            + esc_html(String(n.location.lng))
            + (n.location.acc_m
                ? ' (+/-' + esc_html(String(Math.round(n.location.acc_m)))
                  + 'm)'
                : '')
            + '</div>'
          : "";
        var tagHtml = (n.tags && n.tags.length)
          ? '<div class="scrivener-meta-line"><b>tags:</b> '
            + esc_html(tags_to_string(n.tags)) + '</div>'
          : "";
        row.innerHTML = [
          '<summary class="scrivener-summary">',
          '  <span class="scrivener-type scrivener-type-' + esc_html(n.type)
            + '">' + esc_html(n.type) + '</span>',
          '  <span class="scrivener-row-title">'
            + esc_html(n.title || "(untitled)") + '</span>',
          '  <span class="scrivener-row-date">' + esc_html(n.created_utc)
            + '</span>',
          '  ' + supHtml + supByHtml,
          '</summary>',
          '<div class="scrivener-row-body">',
          '  <pre class="scrivener-body-text">' + esc_html(n.body) + '</pre>',
          '  ' + falsHtml,
          '  ' + anchorHtml,
          '  ' + locHtml,
          '  ' + tagHtml,
          '  <div class="scrivener-meta-line"><b>id:</b> '
            + esc_html(n.id) + '</div>',
          '  <div class="scrivener-meta-line"><b>device:</b> '
            + esc_html(n.device_hint || "") + '</div>',
          '  <div class="scrivener-row-actions">',
          '    <button type="button" class="scrivener-btn" data-act="super">',
          '      Supersede (write a correcting note)</button>',
          '    <button type="button" class="scrivener-btn" data-act="copy">',
          '      Copy as Markdown</button>',
          '  </div>',
          '</div>'
        ].join("\n");
        listEl.appendChild(row);

        row.querySelector('[data-act="super"]').addEventListener(
          "click", function (ev) {
            ev.preventDefault();
            build_modal({
              type: n.type,
              title: n.title,
              tags: n.tags,
              anchor: n.anchor,
              supersedes: n.id,
              on_save: function () { refresh(); }
            });
          });
        row.querySelector('[data-act="copy"]').addEventListener(
          "click", function (ev) {
            ev.preventDefault();
            var md = note_to_markdown(n);
            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(md).then(function () {
                toast("copied");
              }, function () {
                toast("copy failed");
              });
            } else {
              // Fallback: select + prompt
              var ta = document.createElement("textarea");
              ta.value = md;
              document.body.appendChild(ta);
              ta.select();
              try { document.execCommand("copy"); toast("copied"); }
              catch (e) { toast("copy failed"); }
              document.body.removeChild(ta);
            }
          });
      });
    }

    // Wire top controls
    head.querySelector('[data-role="filter-type"]').addEventListener(
      "change", function (ev) {
        state.filter_type = ev.target.value;
        render();
      });
    head.querySelector('[data-role="filter-q"]').addEventListener(
      "input", function (ev) {
        state.q = ev.target.value;
        render();
      });
    head.querySelector('[data-role="new-note"]').addEventListener(
      "click", function () {
        build_modal({ on_save: function () { refresh(); } });
      });
    head.querySelector('[data-role="ex-json"]').addEventListener(
      "click", function () {
        idb_get_all().then(function (arr) {
          var payload = {
            schema_version: SCHEMA_VERSION,
            exported_utc: iso_utc(),
            store: "HONEST",
            notes: arr
          };
          download_blob(
            "scrivener-" + stamp_for_filename() + ".json",
            "application/json",
            JSON.stringify(payload, null, 2));
        });
      });
    head.querySelector('[data-role="ex-md"]').addEventListener(
      "click", function () {
        idb_get_all().then(function (arr) {
          arr.sort(function (a, b) {
            return a.created_utc < b.created_utc ? -1
                 : a.created_utc > b.created_utc ? 1 : 0;
          });
          var text = "# Scrivener export\n\nexported_utc: " + iso_utc()
                   + "\nstore: HONEST\ncount: " + arr.length + "\n\n---\n\n"
                   + arr.map(note_to_markdown).join("\n\n---\n\n");
          download_blob(
            "scrivener-" + stamp_for_filename() + ".md",
            "text/markdown",
            text);
        });
      });
    head.querySelector('[data-role="im-json"]').addEventListener(
      "change", function (ev) {
        var f = ev.target.files && ev.target.files[0];
        if (!f) return;
        var r = new FileReader();
        r.onload = function () {
          try {
            var obj = JSON.parse(r.result);
            var notes = Array.isArray(obj) ? obj
                      : (obj && Array.isArray(obj.notes) ? obj.notes : null);
            if (!notes) {
              alert("Import failed: file has no 'notes' array.");
              return;
            }
            idb_import_batch(notes).then(function (c) {
              alert("Import complete. new=" + c.new + " duplicate="
                    + c.duplicate + " malformed=" + c.malformed);
              refresh();
            }).catch(function (err) {
              alert("Import error: "
                    + (err && err.message ? err.message : String(err)));
            });
          } catch (e) {
            alert("Import failed: " + e.message);
          }
          ev.target.value = "";
        };
        r.readAsText(f);
      });

    refresh();

    // Refresh when a save happens elsewhere.
    window.addEventListener("scrivener:saved", refresh);
  }

  function note_to_markdown(n) {
    var lines = [];
    lines.push("## " + n.type.toUpperCase() + " -- "
               + (n.title || "(untitled)"));
    var meta = [n.created_utc];
    if (n.tags && n.tags.length) meta.push("tags: " + tags_to_string(n.tags));
    var anchorStr = format_anchor(n.anchor || {});
    if (anchorStr) meta.push("anchor: " + anchorStr);
    if (n.supersedes) meta.push("supersedes: " + n.supersedes);
    meta.push("id: " + n.id);
    meta.push("store: HONEST");
    lines.push(meta.join("  "));
    if (n.falsifier) lines.push("falsifier: " + n.falsifier);
    lines.push("");
    lines.push("---");
    lines.push("");
    lines.push(n.body || "");
    return lines.join("\n");
  }

  // ------------------------------------------------------------------
  // Bootstrap + public surface
  // ------------------------------------------------------------------
  function bootstrap() {
    // Listen for capture opens from anywhere on the page.
    window.addEventListener("scrivener:open", function (ev) {
      var opts = (ev && ev.detail) ? ev.detail : {};
      build_modal(opts);
    });

    // Floating capture button (opt out with data-scrivener-no-fab="1" on body)
    mount_floating_button();

    // Mount list view if the page carries the mount point.
    var listMount = document.querySelector('[data-role="scrivener-list"]');
    if (listMount) build_list(listMount);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrap);
  } else {
    bootstrap();
  }

  // Public API for pages that want to drive things explicitly.
  window.Scrivener = {
    open: function (opts) { build_modal(opts || {}); },
    close: close_modal,
    list_all: idb_get_all,
    get: idb_get,
    add: idb_add,
    import_batch: idb_import_batch,
    note_to_markdown: note_to_markdown
    // _dev_delete used to be exported here. It is not any more: the HONEST
    // store is APPEND-ONLY (the doctrine surfaced in the modal's own copy
    // just above); a delete verb on window.Scrivener is a decoration-level
    // violation of that doctrine even if nothing in the UI calls it. The
    // function still exists inside this IIFE closure -- untested code paths
    // are worth reviewing before removing, and closure-scope keeps it
    // reachable only by a builder editing this file, never by page script.
  };
})();

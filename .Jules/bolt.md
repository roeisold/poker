## 2025-05-15 - [Browser Caching for Static Assets]
**Learning:** In Flask 2.3+, `SEND_FILE_MAX_AGE_DEFAULT` is deprecated. Using an `@app.after_request` handler is the recommended way to set `Cache-Control` headers for static files when they are served by Flask.
**Action:** Always use `@app.after_request` for explicit cache control in modern Flask apps.

**Performance Impact:**
- **What:** Added `Cache-Control: public, max-age=31536000` to all files in `/static`.
- **Why:** The application serves ~5.2MB of chip images. Without caching, these are re-downloaded on every page load (or validated with 304s if ETag is present, which still takes round-trips).
- **Measurement:**
    - Initial load: ~5.2MB transferred.
    - Subsequent loads: 0MB transferred (loaded from disk/memory cache).
    - Reduces load time for returning visitors from seconds (depending on connection) to near-instant for images.

## 2026-04-18 - [Manual Gzip Compression in Flask]
**Learning:** For performance-sensitive Flask apps where middleware isn't available, manual Gzip compression in an `@app.after_request` handler is highly effective but requires care. Accessing `response.response` or `response.get_data()` for responses with `direct_passthrough=True` can exhaust the iterator, leading to empty responses if not handled.
**Action:** Always check `response.direct_passthrough` and skip compression (or carefully restore the iterator) to avoid breaking streaming or file responses. Filter by mimetype and size (>500 bytes) to avoid overhead on small or binary payloads.

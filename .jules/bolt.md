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

## 2026-04-17 - [Manual Gzip Compression and Lazy Loading]
**Learning:** For performance-sensitive applications, manual Gzip compression in Flask's `after_request` provides significant bandwidth savings (~73% for HTML). However, when reading `response.response` for `direct_passthrough` responses (like static files), the iterator must be restored to prevent empty responses. Additionally, image-heavy pages benefit greatly from `loading="lazy"` and `decoding="async"` to reduce main-thread contention during initial load.
**Action:** Implement Gzip for text/JSON/JS payloads > 500 bytes and always include `loading="lazy"` for non-critical images.

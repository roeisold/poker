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

## 2026-04-25 - [Gzip Compression for Text Responses]
**Learning:** Implementing manual Gzip compression in Flask's `after_request` handler is an effective way to reduce payload size for HTML and JSON responses when a reverse proxy or CDN is not handling it. It's important to check both the client's `Accept-Encoding` header and the response's MIME type to avoid compressing binary data or tiny responses.
**Action:** Always include Gzip compression for text-based assets (>500 bytes) in the middleware or `after_request` layer.

**Performance Impact:**
- **What:** Added Gzip compression for `text/html`, `application/json`, `text/css`, and `application/javascript`.
- **Why:** The main page HTML was ~17KB, which is significantly larger than necessary.
- **Measurement:**
    - Root URL: 17150 -> 4658 bytes (~73% reduction).
    - API responses: ~55% reduction for typical calculation payloads.

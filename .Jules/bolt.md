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

## 2026-05-06 - [Gzip Compression for Text-Based Responses]
**Learning:** Manually implementing Gzip compression in Flask's `after_request` handler is an effective way to reduce transfer sizes for dynamically generated content (HTML and JSON) when a reverse proxy like Nginx isn't handling it.
**Action:** When optimizing transfer sizes, prioritize text-based responses for compression, as they often yield the highest percentage gains.

**Performance Impact:**
- **What:** Implemented Gzip compression for HTML and JSON responses > 500 bytes.
- **Why:** The main index page and calculation results can grow significantly. Gzip reduces the payload size over the wire.
- **Measurement:**
    - `/` (HTML): Reduced from 17,150 bytes to 4,658 bytes (~73% reduction).
    - `/calculate` (JSON, 20 players): Reduced from 2,154 bytes to 216 bytes (~90% reduction).

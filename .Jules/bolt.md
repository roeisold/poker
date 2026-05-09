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

## 2025-05-15 - [Optimize chip images]
**Learning:** Serving high-resolution (1000x1000) source images for small UI icons (22px-50px) is a significant performance bottleneck. WebP format with high-quality downsampling (LANCZOS) provides massive size savings with negligible visual impact.
**Action:** Always resize source assets to their maximum display size and use modern formats like WebP.

**Performance Impact:**
- **What:** Resized chip images from 1000x1000 to 200x200 and converted from JPEG to WebP.
- **Why:** The total size of chip images was ~5.2MB, which is extremely heavy for a simple calculator app, especially on mobile.
- **Impact:** Reduces total asset size by ~98.7% (from ~5.2MB to ~70KB).
- **Measurement:** `ls -lh static/` shows each image is now ~4-6KB compared to ~400KB originally.

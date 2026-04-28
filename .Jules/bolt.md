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

## 2026-04-28 - [Optimizing Image Assets with WebP]
**Learning:** Resizing high-resolution JPEGs (1000x1000) to match their actual UI display size (max 100x100) and converting to WebP quality 85 can reduce asset payload by over 99% without perceived quality loss.
**Action:** Always audit static assets for size/resolution mismatches and prefer WebP for web-optimized delivery.

**Performance Impact:**
- **What:** Resized 13 poker chip images to 100x100 and converted to WebP.
- **Why:** Original JPEGs were 1000x1000 pixels (~5.2MB total), while they are displayed at 22px-50px in the UI.
- **Impact:** Reduced total image payload from 5.2MB to ~52KB (~99% reduction).
- **Measurement:** `ls -lh static/` shows file sizes reduced from ~400KB each to ~2KB each.

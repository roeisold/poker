## 2025-05-15 - [Browser Caching for Static Assets]
**Learning:** In Flask 2.3+, `SEND_FILE_MAX_AGE_DEFAULT` is deprecated. Using an `@app.after_request` handler is the recommended way to set `Cache-Control` headers for static files when they are served by Flask.
**Action:** Always use `@app.after_request` for explicit cache control in modern Flask apps.

## 2025-05-22 - [Optimizing Image Assets and Response Compression]
**Learning:** High-resolution JPEG images used as small icons (22-50px) are a major bottleneck. Converting to WebP and resizing to an appropriate scale (100x100) provides massive wins. Also, manual Gzip in Flask `after_request` requires checking `response.get_data()` length as `content_length` might be `None` for rendered templates.
**Action:** Always audit asset sizes relative to their display size and implement Gzip with robust length checks.

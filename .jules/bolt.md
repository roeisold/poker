# Bolt's Journal

## 2026-04-07 - [Flask 2.3+ Asset Delivery Optimization]
**Learning:** In Flask 2.3+, `SEND_FILE_MAX_AGE_DEFAULT` configuration is deprecated/removed. To properly set browser caching for static assets, headers should be set explicitly in an `@app.after_request` handler. Additionally, when implementing custom Gzip compression, the `Vary: Accept-Encoding` header is crucial for correct caching by intermediate proxies/CDNs. Handling static files in a custom `after_request` middleware requires special care for `direct_passthrough` responses by reading from the response iterator.

**Action:** Always set `Vary: Accept-Encoding` when compressing responses and use explicit header manipulation for cache control in modern Flask versions. Handle `direct_passthrough` by joining `response.response`.

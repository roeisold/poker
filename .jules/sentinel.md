## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-29 - Stored XSS via localStorage Persistence
**Vulnerability:** User-controlled data from `localStorage` was rendered directly into HTML attributes (like `value`) without sanitization.
**Learning:** In applications relying on client-side state persistence for multi-page workflows, `localStorage` must be treated as an untrusted source, just like server-side data.
**Prevention:** Ensure all data retrieved from `localStorage` is passed through a sanitization function like `escapeHTML()` before being interpolated into template strings, especially when used in attributes.

## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-22 - Client-side Storage XSS Protection
**Vulnerability:** XSS through unsanitized data retrieved from `localStorage` and injected into `innerHTML`.
**Learning:** Data from `localStorage` must be treated as untrusted user input. Numeric fields like `buyIn` or `chipCount` can be manipulated to contain malicious scripts.
**Prevention:** Always apply `escapeHTML()` to all values retrieved from `localStorage` before rendering them in the DOM, regardless of their expected type.

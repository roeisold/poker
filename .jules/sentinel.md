## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-11 - Client-side XSS from LocalStorage
**Vulnerability:** Cross-Site Scripting (XSS) through unsanitized data retrieved from `localStorage` and injected into template literals.
**Learning:** Values stored in `localStorage` can be modified by users or malicious scripts and should be treated as untrusted input when rendering.
**Prevention:** Always wrap variables retrieved from `localStorage` (like player names, buy-ins, or chip counts) in `escapeHTML()` before including them in HTML strings or template literals.

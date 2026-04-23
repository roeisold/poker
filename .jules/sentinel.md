## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-23 - DOM-based XSS via LocalStorage
**Vulnerability:** User-controlled data in `localStorage` was rendered into HTML templates without sanitization, allowing for DOM-based XSS.
**Learning:** `localStorage` is not a trusted source. Any data retrieved from it must be treated as untrusted user input and escaped before being injected into the DOM.
**Prevention:** Wrap all variables sourced from `localStorage` in an `escapeHTML()` function when using template literals for DOM insertion.

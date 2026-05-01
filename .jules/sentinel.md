## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-01 - Nullish Coalescing in Sanitization
**Vulnerability:** XSS sanitization helper `escapeHTML` was failing to render numeric `0` values, treating them as falsy and returning an empty string.
**Learning:** Using `if (!str) return '';` in a generic sanitizer is dangerous when numeric data (like buy-ins or chip counts) is passed through it, as it leads to silent data loss in the UI.
**Prevention:** Use nullish coalescing `str ?? ''` to ensure `0` is treated as a valid value while still handling `null` and `undefined`.

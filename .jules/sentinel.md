## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-10 - JavaScript XSS Prevention with Numeric Data
**Vulnerability:** DOM-based XSS through `localStorage` data injection into input values.
**Learning:** Standard truthiness checks in JS (like `if (!str)`) can fail for numeric `0`, which is a common valid value in this app (e.g., chip counts). This causes legitimate data to be lost during sanitization.
**Prevention:** Use explicit null/undefined checks (`str === null || str === undefined`) in `escapeHTML` to ensure `0` is preserved while still preventing XSS.

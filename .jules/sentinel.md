## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-12 - DOM XSS via LocalStorage
**Vulnerability:** Unsanitized data from `localStorage` injected into the DOM via template literals.
**Learning:** Values stored in `localStorage` (e.g., player names, chip counts) are treated as trusted in several template files, leading to DOM XSS when rendered.
**Prevention:** Apply `escapeHTML()` to all variables retrieved from `localStorage` before inserting them into HTML templates. Use automated audit scripts to detect missing sanitization in templates.

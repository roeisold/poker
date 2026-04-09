## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-09 - Client-side XSS via LocalStorage
**Vulnerability:** DOM-based XSS through unsanitized data retrieved from `localStorage`.
**Learning:** Even if the backend is secure, frontend logic that reads from `localStorage` and uses `innerHTML` to render that data is vulnerable if not properly escaped. Attackers can persist malicious payloads in `localStorage` that trigger whenever the user visits the page.
**Prevention:** Always use `escapeHTML` or similar sanitization when inserting data from `localStorage` (or any user-controllable source) into the DOM via `innerHTML`. Prefer `textContent` when possible.

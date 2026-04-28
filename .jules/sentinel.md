## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-28 - Stored XSS via localStorage and DoS Prevention
**Vulnerability:** Stored XSS through unescaped `localStorage` data and potential DoS via unbounded player count.
**Learning:** Data in `localStorage` should be treated as untrusted user input. A weak `escapeHTML` function (e.g., `if (!str) return ''`) can break UI for numeric `0`. Unvalidated API inputs can lead to resource exhaustion.
**Prevention:** Use robust sanitization for all data rendered from client-side storage. Implement explicit limits on the size of input collections (e.g., max 50 players) and enforce strict type checking on API endpoints.

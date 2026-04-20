## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-20 - LocalStorage XSS and Nullish Coalescing
**Vulnerability:** XSS via unsanitized data retrieved from `localStorage` and rendered into the DOM.
**Learning:** Data stored in `localStorage` should be treated as untrusted user input. Using logical OR (`||`) for default values during rendering can accidentally hide legitimate zero values (e.g., `buyIn: 0`).
**Prevention:** Always use `escapeHTML()` on data from `localStorage` before rendering. Use nullish coalescing (`??`) instead of logical OR (`||`) when `0` is a valid piece of data to ensure correct UI state.

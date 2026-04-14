## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-04-14 - LocalStorage-based XSS in Templates
**Vulnerability:** Persistent XSS through malicious data in `localStorage` being rendered unsanitized into HTML template literals.
**Learning:** Even if data is only "local" to the user, it can be a vector if the app shares state or if an attacker can influence `localStorage` (e.g., via other XSS or social engineering).
**Prevention:** Always wrap variables in `escapeHTML()` when interpolating into HTML strings, even for data expected to be numeric or from local state.

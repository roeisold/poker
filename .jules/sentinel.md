## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-17 - Input Validation & DoS Protection
**Vulnerability:** Lack of player limits and duplicate name checks in calculation endpoint.
**Learning:** Omission of input size limits on computational endpoints can lead to Denial of Service. Additionally, duplicate identifiers (names) in business logic involving dictionaries can lead to silent data loss or calculation errors.
**Prevention:** Enforce strict limits on input array sizes (e.g., 50 players) and validate uniqueness of identifiers at the API level before processing.

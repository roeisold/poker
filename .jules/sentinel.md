## 2026-04-08 - Flask Security Hardening
**Vulnerability:** Information leakage through raw exception messages and lack of Content Security Policy.
**Learning:** Returning `str(e)` in Flask JSON responses can expose internal application logic or stack traces to clients.
**Prevention:** Always use generic error messages for client-facing responses and implement CSP via `@app.after_request` to enforce resource loading policies.

## 2026-05-08 - Environment Information Leakage
**Vulnerability:** Accidental commitment of log files (e.g., `app.log`) containing internal tracebacks.
**Learning:** Development and test artifacts can inadvertently leak internal system details, paths, and dependency information if not explicitly excluded or cleaned up before submission.
**Prevention:** Always verify the list of files to be committed and ensure temporary logs or debug artifacts are removed. Use `.gitignore` effectively to prevent such leaks.

# Mirage build progress

Update this file at the end of every session: tick the part, and add notes the next
session needs (decisions made, things left open).

- [x] **Part 0: Foundation**
- [ ] **Part 1: SSH server**
- [ ] **Part 2: Fake system engine**
- [ ] **Part 3: AI shell**
- [ ] **Part 4: Storage & events**
- [ ] **Part 5: Attacker analysis**
- [ ] **Part 6: API**
- [ ] **Part 7: Dashboard**
- [ ] **Part 8: Deploy & hardening**
- [ ] **Part 9: Tests/CI/README**

## Notes

### Part 0 (2026-11-15)
- Monorepo layout created: `honeypot/`, `analyzer/`, `api/`, `llm/`, `web/`, `infra/`,
  `docs/`, `tests/`. The Python packages are empty apart from `__init__.py`.
- `llm/` is a top-level package (shared by `honeypot` and `analyzer`); it is filled in Part 3.
- Tooling: uv, ruff, mypy (strict), pytest (`asyncio_mode = auto`, markers `live` and
  `integration`).
- `docker-compose.yml` runs postgres 16 and redis 7. App services are busybox stubs
  behind the `stubs` profile; replace each one when its part lands.
- `web/` holds only a README. Part 7 scaffolds the Vite app there.
- LLM SDKs (`groq`, `google-genai`) are not dependencies yet; Part 3 adds them.
- Model names in `.env.example` are placeholders. Part 3 must confirm current names in
  the Groq and Gemini docs.

### Open items
- Compose file has not been run yet: Docker was not installed on the dev machine during Part 0.

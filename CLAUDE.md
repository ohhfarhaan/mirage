# Mirage

LLM-powered adaptive SSH honeypot. It simulates a believable vulnerable Linux server,
uses an LLM to generate realistic shell output, profiles attackers, maps their actions
to MITRE ATT&CK, and shows everything on a live dashboard.

## Rules for every session

1. **Read first:** this file, `docs/ARCHITECTURE.md` and `docs/PROGRESS.md`, before
   writing any code.
2. **Finish properly:** update `docs/PROGRESS.md` (tick the part, add notes for the next
   session), then commit and push to `origin main`.
3. **Never execute attacker input.** No `subprocess`, `os.system`, `eval`, `exec` or
   real shell on anything an attacker typed. Every reply is simulated. Downloads are
   only hashed and stored as inert blobs. See the safety model in `docs/ARCHITECTURE.md`.
4. **Never commit secrets.** Real keys go in `.env` (gitignored). Keep `.env.example`
   in sync when adding a setting.
5. Build one part per session, in order (Parts 6 and 7 may run in parallel after Part 5).

## Layout

| Path | What |
|---|---|
| `honeypot/` | asyncssh server, `system/` (fake system engine), `ai/` (LLM shell) |
| `llm/` | Pluggable provider layer: Groq, Gemini, Ollama, fallback chain, budgets |
| `analyzer/` | ATT&CK mapping, attacker profiling, reports, IOC export |
| `api/` | FastAPI REST + WebSocket |
| `web/` | React + Vite + TypeScript + Tailwind dashboard |
| `infra/` | Dockerfiles, production compose, deploy scripts |
| `docs/` | `ARCHITECTURE.md`, `PROGRESS.md`, later `DEPLOY.md`, `RESULTS.md` |
| `tests/` | pytest suite, `fixtures/` for sample transcripts |

## Conventions

- Python 3.12, fully async (asyncio). No blocking calls in the SSH session path.
- Type hints everywhere; mypy runs in strict mode.
- Settings come from env via `pydantic-settings`. Model names are never hardcoded.
- Pydantic models at boundaries (API responses, LLM structured output).
- Each command is tagged with its handler: `native`, `ai` or `cache`.
- Tests mock LLM providers. Tests that call a real provider are marked `live` and skip
  without API keys; tests that need postgres/redis are marked `integration`.
- ruff for lint and format, line length 100.
- Small, clear commits; one part may be several commits.

## How to run

```bash
uv sync                      # create .venv and install deps (incl. dev group)
cp .env.example .env         # then fill in keys
docker compose up -d         # postgres + redis

uv run ruff check .          # lint
uv run ruff format .         # format
uv run mypy                  # type check
uv run pytest                # tests
```

App entry points are added by their parts; record the run command here when one lands.

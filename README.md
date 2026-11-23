# OpsDesk — Claude Code × Codex educational repository

A **synthetic** task/incident management API for Antalya Havalimanı's four-day training. No real airport systems, real Jira data, or customer network access is used.

## Prerequisites
- Python 3.12 or newer
- macOS, Linux or Windows; outbound access to install dependencies (or pre-provisioned wheel cache)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
python -m scripts.seed_demo
uvicorn app.main:app --reload
```

`requirements.txt` pins the exact versions the starter was tested with, so every participant gets the same environment. `pyproject.toml` keeps the looser version ranges; `python -m pip install -e '.[dev]'` still works but may pull newer releases.

API docs: http://127.0.0.1:8000/docs

Try:
```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/incidents
curl 'http://127.0.0.1:8000/incidents?severity=critical'
```

**Teaching point:** The last request returns *unfiltered* incidents until OPS-101 is implemented. This is intentional.

## Tests
```bash
pytest -q -m 'not ops101'    # initial baseline: must PASS
pytest -q -m ops101          # initial acceptance: expected FAIL (4 tests)
pytest -q                   # after implementing OPS-101: all should PASS
```

The acceptance tests are **not** marked xfail so learners see genuine red-to-green TDD. The starter's `pytest -q` run will therefore fail until the exercise is completed. Read `docs/OPS-101.md` for the assignment.

## Repo structure
- `app/`: FastAPI endpoints, models, schemas, database
- `scripts/seed_demo.py`: idempotent synthetic sample data seeding
- `tests/test_api.py`: baseline behavior checks
- `tests/test_ops101.py`: intentionally failing OPS-101 acceptance tests
- `docs/OPS-101.md`: user story and acceptance criteria
- `CLAUDE.md`: Claude Code-specific project rules
- `AGENTS.md`: shared agent guidance

## Deliberate limitations
No authentication, RBAC, pagination, network isolation, production migrations or deployment-hardening. Do not deploy as a production service. Authentication and safe data handling are taught separately; this starter API is for local training only.

## Trainer setup / next phases
Once tests are verified, create a Git repository and **tag an untouched starter baseline** (`training/day1-start`). After OPS-101 is implemented, save a reference solution on a separate trainer branch. Days 2–4 will introduce MCP logs, review Skills, Hooks, prompt-injection scenarios, and dual-agent PR review without contaminating the day-1 baseline.

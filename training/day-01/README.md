# Day 01 — Agentic Software Engineering | Claude Code

**Program:** Antalya Havalimanı BT — Claude Code × Codex  
**Schedule:** 09:30–16:30 (breaks included)  
**Training data:** Synthetic OpsDesk repository only. No institutional network, live Jira or production data.

## Learning outcomes

By the end of the day you can:
1. Distinguish model, harness, tools and execution environment.
2. Explore a repository using a coding agent **without modifying source files**.
3. Explain context management, permission boundaries and plan-before-edit workflows.
4. Interpret the OPS-101 user story and validate its acceptance criteria.
5. Implement the optional severity filter and verify results with pytest.
6. Review a diff and summarize evidence before proposing a commit/PR.

## Agenda

| Time | Topic | Format |
|---|---|---|
| 09:30–10:45 | Agentic coding, model/harness/tools, agentic loop, read-only repo exploration | Talk + demo |
| 10:45–11:00 | Break | — |
| 11:00–12:30 | Context, planning, permissions, repository analysis | Demo + guided work |
| 12:30–13:30 | Lunch | — |
| 13:30–14:45 | CLAUDE.md, AGENTS.md, instructions and demo Jira user story | Discussion + demo |
| 14:45–15:00 | Break | — |
| 15:00–16:15 | OPS-101: plan → implement → test | Lab |
| 16:15–16:30 | Diff review and learning assessment | Debrief |

## Course files

- `../../docs/OPS-101.md` — canonical user story and acceptance criteria.
- `prompts/01-repository-exploration.md` — prompts for **read-only** analysis and impact assessment.
- `exercises/OPS-101.md` — participant lab with commands, checkpoints, and submission criteria.
- `../../CLAUDE.md` — Claude Code-specific project instructions.
- `../../AGENTS.md` — cross-agent project guidance.

## Before the session

1. Use Python 3.12+ with an isolated virtual environment.
2. From the **repository root**, install dependencies: `python -m pip install -e '.[dev]'`.
3. Confirm `pytest -q -m 'not ops101'` passes.
4. Confirm `pytest -q -m ops101` reports **4 failures and 1 pass** on the untouched starter.
5. Check `git status --short` and preserve the starter tag `training/day1-start` **before** implementing the feature.
6. Start the API with `uvicorn app.main:app --reload`; browse `/docs` if desired.
7. Check Claude Code access and permissions separately. Do not put API keys in the repository.

## Recommended Git workflow

From a **clean** checkout of the starter, create a participant-specific branch such as:

```bash
git switch -c participant/your-id/ops101 training/day1-start
```

If the tag is not yet present, ask the trainer to create it from the untouched starter commit. Do not tag a version where OPS-101 has already been implemented.

Do not push, merge, or run destructive commands without trainer/owner permission. Avoid sharing one writeable branch with the whole class.

## Important

- Initial failing OPS-101 tests are **intentional** (red → green exercise).
- Don't weaken acceptance tests to make a build pass.
- Prompts are exercises, **not** an access-control boundary. Use the tool's available read-only / planning permission controls and verify `git diff`.
- Any AI explanation needs checking against source files and actual command output.

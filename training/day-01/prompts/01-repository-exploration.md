# Prompt cards — Repository exploration (Day 01)

**Purpose:** Observe the agentic loop: gather context → use tools → interpret results → report evidence.  
**Rule:** This part is **read-only**. Run in Claude Code's planning/read-only mode where available, review requested permissions, and do not authorize edits or destructive commands. A prompt alone does not enforce access restrictions.

## Prompt 01 — Map the codebase (09:30–10:45 demo)

```text
Examine the OpsDesk repository without editing files.
1. Explain the project's purpose and main directories.
2. Find the Incident and Task models and their fields.
3. Locate GET /incidents and trace its current behavior.
4. Identify tests that protect existing API behavior.
5. Cite exact file paths and relevant function names for each claim.
6. Separate confirmed observations from assumptions.
Do not install dependencies, edit files, commit, or push changes.
```

**Observe:** which files were read; whether the agent searched before reading; whether claims cite real paths; whether any edit was requested. Record the tool operations, not merely the final prose.

## Prompt 02 — Explain the intentional test failures

First run the commands yourself from the repository root:

```bash
pytest -q -m 'not ops101'
pytest -q -m ops101
```

Then supply the **real command output**, or ask the agent to inspect existing test code without running commands that have not been approved.

```text
Analyze tests/test_ops101.py alongside the GET /incidents endpoint.
For each OPS-101 acceptance test, identify:
- intended behavior,
- current observed/statically inferred behavior,
- likely reason for failure,
- the source file(s) to inspect next.
Do not change any files or weaken tests.
Distinguish test output I supplied from conclusions inferred from source.
```

**Expected untouched baseline:** 7 baseline tests pass. OPS-101 has 4 failing tests (critical, high, no matches, invalid severity) and 1 passing test (no filter).

## Prompt 03 — Impact analysis, not implementation (11:00–12:30)

```text
Read docs/OPS-101.md and inspect the relevant endpoint, models, schemas,
and tests. Propose the smallest implementation plan that satisfies
all acceptance criteria.
For each planned change include:
- exact file / function,
- required behavior,
- why it is necessary,
- risk to existing contracts,
- how it will be verified.
Do not edit source or test files. Stop after presenting the plan for approval.
```

**Review questions:** Does the plan validate supported severities? Preserve unfiltered listing? Return 422 for unsupported values? Filter in the query? Preserve ordering? Leave tests intact?

## Trainer-led comparison

Ask participants to compare a vague prompt ("Fix the endpoint") against the structured prompt above. Discuss which produced better **verifiable evidence**, not which answer sounded more confident.

## Evidence to capture

- Agent's list of tools used (from the UI/session trace).
- File paths reviewed.
- At least one mistaken assumption or uncertainty and how it was resolved.
- Proposed change list, **without** source modifications during this activity.
- `git diff --exit-code` for a clean working tree if participants began from an untouched branch.

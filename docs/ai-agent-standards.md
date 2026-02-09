# AI Agent Engineering Standards

This project adopts lightweight, open, agent-friendly conventions:

## 1) Interoperable agent instructions
- `AGENTS.md` at repo root defines universal behavior for code agents.
- Keep instructions concise, deterministic, and testable.

## 2) Deterministic dependency context
- Source of truth: `pyproject.toml` and lockfile (`uv.lock` when present).
- Generated artifact: `.ai/dependency-context.json`.
- The artifact is intended for AI tooling ingestion and should be committed.

## 3) Structured context format
- `.ai/dependency-context.json` follows a stable JSON structure with:
  - project metadata
  - declared dependencies
  - optional locked versions
  - generation timestamp

## 4) Automation-first validation
- A scripted check (`--check`) enforces that committed context is current.
- This enables CI usage and reduces hallucination risks from stale docs.

## 5) Collaboration conventions
- Commit messages follow Conventional Commits.
- Keep agent-generated changes small and auditable.

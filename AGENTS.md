# AGENTS.md

This repository is configured for multi-agent collaboration (Codex, Gemini CLI, and similar tools).

## Objectives
- Keep outputs deterministic and reproducible.
- Prefer machine-readable artifacts over prose-only notes.
- Keep dependency knowledge version-pinned.

## Standard workflow for agents
1. Read `README.md` and `docs/ai-agent-standards.md`.
2. Run `python scripts/export_dependency_context.py` after dependency changes.
3. Update `.ai/dependency-context.json` if dependency graph or lockfile changes.
4. Validate local checks before committing.

## Guardrails
- Do not invent APIs from memory when dependency context exists.
- Prefer references from generated context in `.ai/dependency-context.json`.
- Make small, reviewable commits using Conventional Commits style.

## Required checks
- `python -m compileall .`
- `python scripts/export_dependency_context.py --check`


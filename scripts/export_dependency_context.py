#!/usr/bin/env python3
"""Export dependency context for AI agents.

Reads `pyproject.toml` and emits `.ai/dependency-context.json`.
Use `--check` to verify the file is up-to-date.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
OUT = ROOT / ".ai" / "dependency-context.json"


def load_pyproject() -> dict:
    with PYPROJECT.open("rb") as f:
        return tomllib.load(f)


def normalize_dependencies(deps: list[str]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for dep in deps:
        result.append({"specifier": dep})
    return result


def build_context() -> dict:
    pyproject = load_pyproject()
    project = pyproject.get("project", {})
    deps = project.get("dependencies", [])

    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": {
            "name": project.get("name", ""),
            "version": project.get("version", ""),
            "requires_python": project.get("requires-python", ""),
        },
        "dependencies": normalize_dependencies(deps),
        "notes": [
            "Generated from pyproject.toml.",
            "Prefer this artifact over memory-based API assumptions.",
        ],
    }


def read_existing() -> dict | None:
    if not OUT.exists():
        return None
    return json.loads(OUT.read_text(encoding="utf-8"))


def write_context(payload: dict) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated output differs from file")
    args = parser.parse_args()

    payload = build_context()

    if args.check:
        current = read_existing()
        if current is None:
            print(f"Missing {OUT.relative_to(ROOT)}")
            return 1
        baseline = dict(current)
        baseline["generated_at"] = payload["generated_at"]
        if baseline != payload:
            print(f"Outdated {OUT.relative_to(ROOT)}")
            return 1
        print("dependency context is up to date")
        return 0

    write_context(payload)
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

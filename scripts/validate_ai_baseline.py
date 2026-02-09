#!/usr/bin/env python3
"""Validate AI baseline artifacts for this repository.

This script provides a single entry-point to verify that agent-facing
artifacts are present and structurally correct.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTEXT_FILE = ROOT / ".ai" / "dependency-context.json"


REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "generated_at",
    "project",
    "dependencies",
    "notes",
}

REQUIRED_PROJECT_KEYS = {"name", "version", "requires_python"}


def run_dependency_check() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "export_dependency_context.py"), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stdout.strip() or result.stderr.strip() or "dependency context check failed")


def validate_context_schema() -> None:
    if not CONTEXT_FILE.exists():
        raise FileNotFoundError(f"Missing context file: {CONTEXT_FILE}")

    data = json.loads(CONTEXT_FILE.read_text(encoding="utf-8"))

    missing_keys = REQUIRED_TOP_LEVEL_KEYS - set(data.keys())
    if missing_keys:
        raise ValueError(f"Missing top-level keys: {sorted(missing_keys)}")

    project = data.get("project")
    if not isinstance(project, dict):
        raise TypeError("'project' must be an object")

    missing_project_keys = REQUIRED_PROJECT_KEYS - set(project.keys())
    if missing_project_keys:
        raise ValueError(f"Missing project keys: {sorted(missing_project_keys)}")

    dependencies = data.get("dependencies")
    if not isinstance(dependencies, list):
        raise TypeError("'dependencies' must be a list")

    for i, dep in enumerate(dependencies):
        if not isinstance(dep, dict) or "specifier" not in dep:
            raise ValueError(f"Invalid dependency at index {i}: {dep!r}")


def main() -> int:
    run_dependency_check()
    validate_context_schema()
    print("AI baseline validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

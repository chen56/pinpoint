from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPORT_SCRIPT = ROOT / "scripts" / "export_dependency_context.py"
VALIDATE_SCRIPT = ROOT / "scripts" / "validate_ai_baseline.py"
CONTEXT_FILE = ROOT / ".ai" / "dependency-context.json"


class TestDependencyContextPipeline(unittest.TestCase):
    def test_export_generates_context_file(self) -> None:
        result = subprocess.run(
            [sys.executable, str(EXPORT_SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(CONTEXT_FILE.exists())

        data = json.loads(CONTEXT_FILE.read_text(encoding="utf-8"))
        self.assertIn("project", data)
        self.assertIn("dependencies", data)
        self.assertIsInstance(data["dependencies"], list)

    def test_export_check_mode(self) -> None:
        subprocess.run([sys.executable, str(EXPORT_SCRIPT)], cwd=ROOT, check=True)
        result = subprocess.run(
            [sys.executable, str(EXPORT_SCRIPT), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("up to date", result.stdout)

    def test_validate_script(self) -> None:
        subprocess.run([sys.executable, str(EXPORT_SCRIPT)], cwd=ROOT, check=True)
        result = subprocess.run(
            [sys.executable, str(VALIDATE_SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("validation passed", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import subprocess
import sys


def test_verirag_cli_runs() -> None:
    r = subprocess.run(
        [sys.executable, "-m", "verirag.cli.main"], capture_output=True, text=True
    )
    assert r.returncode == 0
    assert "verirag: OK" in r.stdout

#!/usr/bin/env python3
"""Run the finite routing and proof-geometry checks using the standard library.

The optional --output path records the exact JSON printed to standard output.
These checks complement the general analytical proofs; they do not prove the
lower bounds for arbitrary circuits or certify originality.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    results = {}
    for name in ("routing", "check_geometry"):
        completed = subprocess.run(
            [sys.executable, str(directory / f"{name}.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads(completed.stdout)
        if result.get("status") != "passed":
            raise RuntimeError(f"{name} did not report a passing result")
        results[name] = result
    report = {
        "status": "passed",
        "python": platform.python_version(),
        "checks": results,
    }
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()

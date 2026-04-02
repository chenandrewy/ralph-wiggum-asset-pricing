#!/usr/bin/env python3
# How to run: python3 ralph/author-fix-build.py
# Inputs: paper/.latex-build.log, paper/, code/
# Outputs: in-place fixes under paper/ and/or code/ to make the LaTeX build succeed

from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
AGENT = "claude"
MODEL = "sonnet"
EFFORT = "low"

AUTHOR_FIX_BUILD_PROMPT = """The LaTeX build for paper/paper.tex just failed.

Your only job is to make the paper compile. Do not make any content, style, or structural improvements.

Procedure:

1. Read `paper/.latex-build.log` to identify the error(s).
2. Read the relevant source files (`paper/paper.tex`, `paper/references.bib`, or files under `paper/exhibits/`) to find the cause.
3. Fix the error(s). Common causes include:
   - Raw Unicode characters that pdflatex cannot handle (replace with LaTeX accent commands).
   - References to missing files under `paper/exhibits/` (remove the include or generate the file).
   - Undefined labels or cross-references.
   - BibTeX/Biber errors in `paper/references.bib`.

Rules:
- Only change what is necessary to make the build succeed.
- Do not rewrite, reorganize, or improve the paper content.
- Do not edit test-results/ or any spec files."""


def main() -> int:
    repo_root = REPO_ROOT
    config = load_config(repo_root / "config-ralph.yaml", list_keys=set())
    agent_log_mode = str(config.get("agent-log-mode", "off")).strip().lower()
    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent",
        AGENT,
        "--log-mode",
        agent_log_mode,
        "--step-label",
        "author-fix-build",
    ]
    if EFFORT:
        cmd.extend(["--effort", EFFORT])
    cmd.extend([
        "--model",
        MODEL,
        AUTHOR_FIX_BUILD_PROMPT,
    ])

    result = subprocess.run(cmd, cwd=repo_root)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

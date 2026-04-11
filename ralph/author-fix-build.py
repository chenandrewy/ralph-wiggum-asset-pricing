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

AUTHOR_FIX_BUILD_PROMPT = r"""The LaTeX build for paper/paper.tex just failed.

Your only job is to make the paper compile. Do not make any content, style, or structural improvements.

Procedure:

1. Read `paper/.latex-build.log` to identify the error(s).
2. Read the relevant durable source files (`paper/paper.tex` and `paper/references.bib`) to find the cause.
3. Fix the error(s). Common causes include:
   - Raw Unicode characters that pdflatex cannot handle. For Unicode or encoding failures in citations or bibliography output, convert names and titles in `paper/references.bib` to LaTeX-safe forms.
   - Undefined labels or cross-references that can be fixed in `paper/paper.tex`.
   - BibTeX/Biber errors in `paper/references.bib`.
4. Verify your fix by running `bash ralph/build-paper.sh`. If it still fails, read the new error and fix it. Repeat until the build passes or you are confident no further fixes are possible.

Rules:
- Only change what is necessary to make the build succeed.
- Do not rewrite, reorganize, or improve the paper content.
- A valid fix may modify only `paper/paper.tex` and `paper/references.bib`.
- Do not modify intermediate or generated files such as `paper/paper.bbl`, `paper/*.aux`, `paper/*.out`, `paper/*.bcf`, `paper/*.blg`, `paper/*.log`, `paper/paper.pdf`, or similar build artifacts.
- Do not edit `ralph/`, `spec/`, `tests/`, or `test-results/`."""


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

#!/usr/bin/env python3
# How to run: python3 ralph/author-improve.py
# Inputs: config-ralph.yaml, spec/paper-spec.md, paper/, test-results/, ralph-garage/improvement-plan.md
# Outputs: in-place updates under paper/

from __future__ import annotations

import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config, summary_results_instruction

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"

AUTHOR_IMPROVE_PROMPT_TEMPLATE = """You are an author improving an academic asset pricing theory paper.

Read:
- `spec/paper-spec.md` for the paper specification.
- `paper/paper.tex` for the current paper state.
- {test_results_instruction}
- `ralph-garage/improvement-plan.md` for the planned improvements.

Then write improved versions in place:
- `paper/paper.tex` and/or `paper/references.bib` to address the improvement plan.

Rules:
- Keep the paper concise and focused.
- Do not edit `test-results/`.
- You may use `git diff` and `git log` to understand recent changes when useful."""


def test_results_instruction(repo_root: pathlib.Path) -> str:
    return summary_results_instruction(
        repo_root=repo_root,
        summary_rel_path="test-results/summary.json",
        missing_message="`test-results/` for the latest test outputs (may not exist on first iteration)",
        invalid_message="`test-results/` exists but `summary.json` is invalid; ignore those test outputs",
        stale_message="`test-results/` exists but `summary.json` is more than 1 hour old; ignore those stale test outputs",
        fresh_message="`test-results/` for the latest test outputs",
    )


def build_author_improve_prompt(repo_root: pathlib.Path) -> str:
    return AUTHOR_IMPROVE_PROMPT_TEMPLATE.format(
        test_results_instruction=test_results_instruction(repo_root),
    )


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
        "author-improve",
    ]
    if EFFORT:
        cmd.extend(["--effort", EFFORT])
    cmd.extend([
        "--model",
        MODEL,
        build_author_improve_prompt(repo_root),
    ])

    result = subprocess.run(cmd, cwd=repo_root)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# How to run: python3 ralph/author-improve.py --repo-root /path/to/repo --agent claude --model opus --agent-log-mode verbose --iteration 1
# Inputs: spec/paper-spec.md, paper/, test-results/, ralph-garage/improvement-plan.md
# Outputs: in-place updates under paper/

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import summary_results_instruction


AUTHOR_IMPROVE_PROMPT_TEMPLATE = """You are an author improving an academic asset pricing theory paper.

Read:
- `spec/paper-spec.md` for the paper specification.
- `spec/asset-pricing-background.md` for asset pricing conventions.
- `paper/paper.tex` for the current paper state.
- {test_results_instruction}
- `ralph-garage/improvement-plan.md` for the planned improvements.

Then write improved versions in place:
- `paper/paper.tex` and/or `paper/references.bib` to address the improvement plan.

Rules:
- Keep the paper concise and focused.
- Do not edit `test-results/`.
- You may use `git diff` and `git log` to understand recent changes when useful."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Ralph author improvement step.")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--agent-log-mode", required=True)
    parser.add_argument("--iteration", type=int, required=True)
    return parser.parse_args()


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
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent",
        args.agent,
        "--log-mode",
        args.agent_log_mode,
        "--step-label",
        f"author-improve-iter-{args.iteration:03d}",
        "--model",
        args.model,
        build_author_improve_prompt(repo_root),
    ]

    result = subprocess.run(cmd, cwd=repo_root)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

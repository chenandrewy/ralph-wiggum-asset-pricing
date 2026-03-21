#!/usr/bin/env python3
# How to run: python3 ralph/author-plan.py --repo-root /path/to/repo --agent-log-mode verbose --iteration 1
# Inputs: spec/paper-spec.md, paper/, test-results/
# Outputs: ralph-garage/improvement-plan.md

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import summary_results_instruction

AGENT = "claude"
MODEL = "opus"

AUTHOR_PLAN_PROMPT_TEMPLATE = """You are an author planning improvements to an academic asset pricing theory paper.

Procedure:

1. Read:
- `spec/paper-spec.md` for the paper specification.
- `spec/asset-pricing-background.md` for asset pricing conventions.
- `paper/paper.tex` for the current paper state.
- {test_results_instruction}
- {review_results_instruction}
- `ralph/run-tests.py` and `tests/*.py` for available tests and test ids.

2. Consider whether any section needs an overhaul.
    - Pay particularly close attention to the model section. This is the hardest section to get right.

3. Write a concise, actionable plan to `ralph-garage/improvement-plan.md`.

Requirements of the plan:
1. It summarizes key issues from current paper/tests.
2. It outlines specific paper changes.
3. If an overhaul is needed, the ENTIRE plan should be focused on the overhaul.
4. If an overhaul is not needed, the plan prioritizes fixing failing tests first, then addressing referee review feedback.

Guidance:
- Adjust the messaging to fit the best evidence.
- Keep the plan concise and actionable.
- Do not modify `config-ralph.yaml`.
- You may use `git diff` and `git log` to understand recent changes when useful."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Ralph author planning step.")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--agent-log-mode", required=True)
    parser.add_argument("--iteration", type=int, required=True)
    return parser.parse_args()


def file_digest(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_results_instruction(repo_root: pathlib.Path) -> str:
    return summary_results_instruction(
        repo_root=repo_root,
        summary_rel_path="test-results/summary.json",
        missing_message="`test-results/` for the latest available test outputs (may not exist on first iteration)",
        invalid_message="`test-results/` exists but `summary.json` is invalid; ignore those test outputs",
        stale_message="`test-results/` exists but `summary.json` is more than 1 hour old; ignore those stale test outputs",
        fresh_message="`test-results/` for the latest available test outputs",
    )


def review_results_instruction(repo_root: pathlib.Path) -> str:
    summary_path = repo_root / "test-results/summary.json"
    if not summary_path.is_file():
        return "`test-results/summary.json` for referee outputs (may not exist if referees are disabled or on first iteration)"
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "`test-results/summary.json` exists but is invalid; ignore referee outputs"
    if "reviews" not in payload:
        return "`test-results/summary.json` has no referee outputs (referees may be disabled)"
    return "`test-results/summary.json` `reviews` key for the latest selected referee outputs; read only the referee reports listed there"


def build_author_plan_prompt(repo_root: pathlib.Path) -> str:
    return AUTHOR_PLAN_PROMPT_TEMPLATE.format(
        test_results_instruction=test_results_instruction(repo_root),
        review_results_instruction=review_results_instruction(repo_root),
    )


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    plan_file = repo_root / "ralph-garage/improvement-plan.md"
    config_file = repo_root / "config-ralph.yaml"
    config_digest_before = file_digest(config_file)
    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent",
        AGENT,
        "--log-mode",
        args.agent_log_mode,
        "--step-label",
        f"author-plan-iter-{args.iteration:03d}",
        "--model",
        MODEL,
        build_author_plan_prompt(repo_root),
    ]

    result = subprocess.run(cmd, cwd=repo_root)
    if result.returncode != 0:
        return result.returncode
    if file_digest(config_file) != config_digest_before:
        raise RuntimeError(f"planning phase modified {config_file}")
    if not plan_file.is_file():
        raise FileNotFoundError(f"planning phase did not create {plan_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

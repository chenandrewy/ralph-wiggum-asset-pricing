#!/usr/bin/env python3
# How to run: python3 ralph/author-plan.py
# Inputs: config-ralph.yaml, spec/paper-spec.md, paper/, test-results/
# Outputs: ralph-garage/improvement-plan.md

from __future__ import annotations

import datetime
import json
import pathlib
import subprocess
import sys
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config, summary_results_instruction

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
AGENT = "claude"
MODEL = "opus"
EFFORT = "medium"
NEW_YORK_TZ = ZoneInfo("America/New_York")

AUTHOR_PLAN_PROMPT_TEMPLATE = """You are an author planning improvements to an academic asset pricing theory paper.

Procedure:

1. Read:
- `spec/paper-spec.md` for the paper specification.
- `paper/paper.tex` for the current paper state.
- {test_results_instruction}
- {referee_results_instruction}
- `ralph/run-tests.py` and `tests/*.py` for available tests and test ids.

2. Consider whether any section needs an overhaul.
    - Pay particularly close attention to the model section. This is the hardest section to get right.

3. Write a concise, actionable plan to `ralph-garage/improvement-plan.md`.

Requirements of the plan:
1. It summarizes key issues from current paper/tests.
2. It outlines specific paper changes.
3. If an overhaul is needed, the ENTIRE plan should be focused on the overhaul.
4. If an overhaul is not needed, the plan prioritizes fixing failing tests first, then addressing referee feedback.

Guidance:
- If `paper/.latex-build.log` exists, is less than 1 hour old, and shows a build failure, the entire plan must focus on fixing the build. No other improvements until the paper compiles.
- Adjust the messaging to fit the best evidence.
- Keep the plan concise and actionable.
- Do not modify `config-ralph.yaml`.
- You may use `git diff` and `git log` to understand recent changes when useful."""


def _now_ny() -> str:
    return datetime.datetime.now(NEW_YORK_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")


def ensure_plan_timestamp(plan_file: pathlib.Path) -> None:
    text = plan_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 2 and lines[1].startswith("AUTHOR PLAN — "):
        return
    header = "# Improvement Plan"
    body_start = 0
    if lines and lines[0].strip() == header:
        body_start = 1
    updated_lines = [header, f"AUTHOR PLAN — {_now_ny()}"]
    updated_lines.extend(lines[body_start:])
    plan_file.write_text("\n".join(updated_lines).rstrip() + "\n", encoding="utf-8")

def test_results_instruction(repo_root: pathlib.Path) -> str:
    return summary_results_instruction(
        repo_root=repo_root,
        summary_rel_path="test-results/summary.json",
        missing_message="`test-results/` for the latest available test outputs (may not exist on first iteration)",
        invalid_message="`test-results/` exists but `summary.json` is invalid; ignore those test outputs",
        stale_message="`test-results/` exists but `summary.json` is more than 1 hour old; ignore those stale test outputs",
        fresh_message="`test-results/` for the latest available test outputs",
    )


def referee_results_instruction(repo_root: pathlib.Path) -> str:
    summary_path = repo_root / "test-results/summary.json"
    if not summary_path.is_file():
        return "`test-results/summary.json` for referee outputs (may not exist if referees are disabled or on first iteration)"
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "`test-results/summary.json` exists but is invalid; ignore referee outputs"
    if "referees" not in payload:
        return "`test-results/summary.json` has no referee outputs (referees may be disabled)"
    return "`test-results/summary.json` `referees` key for the latest selected referee outputs; read only the referee reports listed there"


def build_author_plan_prompt(repo_root: pathlib.Path) -> str:
    return AUTHOR_PLAN_PROMPT_TEMPLATE.format(
        test_results_instruction=test_results_instruction(repo_root),
        referee_results_instruction=referee_results_instruction(repo_root),
    )


def main() -> int:
    repo_root = REPO_ROOT
    config_file = repo_root / "config-ralph.yaml"
    config = load_config(config_file, list_keys=set())
    agent_log_mode = str(config.get("agent-log-mode", "off")).strip().lower()
    plan_file = repo_root / "ralph-garage/improvement-plan.md"
    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent",
        AGENT,
        "--log-mode",
        agent_log_mode,
        "--step-label",
        "author-plan",
    ]
    if EFFORT:
        cmd.extend(["--effort", EFFORT])
    cmd.extend([
        "--model",
        MODEL,
        build_author_plan_prompt(repo_root),
    ])

    result = subprocess.run(cmd, cwd=repo_root)
    if result.returncode != 0:
        return result.returncode
    if not plan_file.is_file():
        raise FileNotFoundError(f"planning phase did not create {plan_file}")
    ensure_plan_timestamp(plan_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

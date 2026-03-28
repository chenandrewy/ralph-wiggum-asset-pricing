#!/usr/bin/env python3
"""
How to run: Imported by tests/referee-*.py referee scripts.
Inputs: referee script path and optional CLI arg --agent-log-mode.
Outputs: shared utilities for referee execution.
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import subprocess
import sys

VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
VALID_AGENT_EFFORTS = ("none", "low", "medium", "high", "max", "xhigh")


def parse_referee_cli(
    default_agent_log_mode: str = "off",
    default_agent_effort: str | None = None,
) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agent-log-mode",
        choices=VALID_AGENT_LOG_MODES,
        default=default_agent_log_mode,
        help="Agent log verbosity passed through to ralph/agent_wrapper.py",
    )
    parser.add_argument(
        "--agent-effort",
        choices=VALID_AGENT_EFFORTS,
        default=default_agent_effort,
        help="Agent reasoning effort passed through to ralph/agent_wrapper.py",
    )
    return parser.parse_args()


def derive_referee_id(script_file: str) -> str:
    return pathlib.Path(script_file).stem


def derive_referee_report_path(repo_root: pathlib.Path, referee_id: str) -> pathlib.Path:
    return repo_root / f"test-results/{referee_id}.md"


def _now_ny() -> str:
    """Current timestamp in New York time, e.g. '2026-03-09 15:30:42 EDT'."""
    import zoneinfo
    tz = zoneinfo.ZoneInfo("America/New_York")
    return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")


def write_fallback_report(
    report_path: pathlib.Path,
    reason: str,
) -> None:
    """Fallback report written when the agent can't run."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    referee_id = report_path.stem
    text = f"# {referee_id}\nREFEREE — {_now_ny()}\n\n## Summary\n\nReferee could not be completed: {reason}\n"
    report_path.write_text(text, encoding="utf-8")


def run_referee(
    *,
    script_file: str,
    prompt: str,
    agent: str,
    model: str | None = None,
    default_agent_log_mode: str = "off",
    default_agent_effort: str | None = None,
) -> int:
    """Common referee runner. Always returns 0 (referees never fail the loop)."""
    args = parse_referee_cli(
        default_agent_log_mode=default_agent_log_mode,
        default_agent_effort=default_agent_effort,
    )
    referee_id = derive_referee_id(script_file)

    repo_root = pathlib.Path(script_file).resolve().parents[1]
    report_path = derive_referee_report_path(repo_root, referee_id)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent", agent,
        "--log-mode", args.agent_log_mode,
        "--failure-log-mode", "off",
        "--step-label", referee_id,
    ]
    if args.agent_effort:
        cmd.extend(["--effort", args.agent_effort])
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)

    result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)

    if result.returncode != 0:
        write_fallback_report(report_path, f"agent wrapper failed with exit code {result.returncode}")

    # Even if the agent fails or produces no report, referees always return 0.
    if not report_path.exists():
        write_fallback_report(report_path, "agent did not produce a report")

    return 0

#!/usr/bin/env python3
"""
How to run: Imported by dev/qf/*.py.
Inputs: dev/qf test script path and optional CLI arg --agent-log-mode.
Outputs: shared utilities for experimental quality-formalism tests in dev/qf-results/.
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import subprocess
import sys
from dataclasses import dataclass
from zoneinfo import ZoneInfo

VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
VALID_AGENT_EFFORTS = ("none", "low", "medium", "high", "max", "xhigh")
NEW_YORK_TZ = ZoneInfo("America/New_York")


@dataclass(frozen=True)
class TestContext:
    script_file: pathlib.Path
    repo_root: pathlib.Path
    script_rel_path: str
    test_id: str
    report_path: pathlib.Path
    started_at_utc: datetime.datetime


def parse_test_cli(
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


def build_test_context(script_file: str) -> TestContext:
    script_path = pathlib.Path(script_file).resolve()
    repo_root = script_path.parents[2]
    test_id = script_path.stem
    started_at_utc = datetime.datetime.now(datetime.timezone.utc)
    return TestContext(
        script_file=script_path,
        repo_root=repo_root,
        script_rel_path=str(script_path.relative_to(repo_root)),
        test_id=test_id,
        report_path=repo_root / f"dev/qf-results/{test_id}.md",
        started_at_utc=started_at_utc,
    )


def _format_ny(timestamp_utc: datetime.datetime) -> str:
    return timestamp_utc.astimezone(NEW_YORK_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")


def _duration_seconds(started_at_utc: datetime.datetime, finished_at_utc: datetime.datetime) -> float:
    return max(0.0, (finished_at_utc - started_at_utc).total_seconds())


def _format_duration(seconds: float) -> str:
    if seconds < 10:
        return f"{seconds:.1f}s"
    rounded_seconds = int(round(seconds))
    if rounded_seconds < 60:
        return f"{rounded_seconds}s"
    minutes, secs = divmod(rounded_seconds, 60)
    if minutes < 60:
        return f"{minutes}m {secs}s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {secs}s"


def _report_header(
    script_rel_path: str,
    started_at_utc: datetime.datetime,
    finished_at_utc: datetime.datetime,
    log_path: str | None = None,
) -> str:
    lines = [
        f"# {script_rel_path}",
        f"Started: {_format_ny(started_at_utc)}",
        f"Runtime: {_format_duration(_duration_seconds(started_at_utc, finished_at_utc))}",
    ]
    if log_path:
        lines.append(f"[{log_path}](../../{log_path})")
    return "\n".join(lines) + "\n"


def write_fail_report(
    context: TestContext,
    reason: str,
    log_path: str | None = None,
) -> int:
    context.report_path.parent.mkdir(parents=True, exist_ok=True)
    finished_at_utc = datetime.datetime.now(datetime.timezone.utc)
    text = _report_header(
        context.script_rel_path,
        context.started_at_utc,
        finished_at_utc,
        log_path,
    )
    text += f"\n# {context.test_id}\nVERDICT: FAIL\nREASON: {reason}\n"
    context.report_path.write_text(text, encoding="utf-8")
    print(f"[{context.test_id}] FAIL: {reason}")
    return 1


def require_paths(context: TestContext, *paths: pathlib.Path) -> int | None:
    for path in paths:
        if not path.exists():
            return write_fail_report(context, f"missing: {path}")
    return None


def parse_verdict_from_report(report_path: pathlib.Path) -> str | None:
    if not report_path.exists():
        return None
    for line in report_path.read_text(encoding="utf-8").splitlines():
        if line.strip().upper().startswith("VERDICT:"):
            verdict = line.split(":", 1)[1].strip().upper()
            if verdict in {"PASS", "FAIL"}:
                return verdict
    return None


def parse_reason_from_report(report_path: pathlib.Path) -> str | None:
    if not report_path.exists():
        return None
    for line in report_path.read_text(encoding="utf-8").splitlines():
        if line.strip().upper().startswith("REASON:"):
            return line.split(":", 1)[1].strip() or None
    return None


def run_test(
    *,
    context: TestContext,
    prompt: str,
    agent: str,
    model: str | None = None,
    default_agent_log_mode: str = "off",
    default_agent_effort: str | None = None,
) -> int:
    args = parse_test_cli(
        default_agent_log_mode=default_agent_log_mode,
        default_agent_effort=default_agent_effort,
    )

    cmd = [
        sys.executable,
        str(context.repo_root / "ralph/agent_wrapper.py"),
        "--agent", agent,
        "--log-mode", args.agent_log_mode,
        "--failure-log-mode", "off",
        "--step-label", context.test_id,
    ]
    if args.agent_effort:
        cmd.extend(["--effort", args.agent_effort])
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)

    result = subprocess.run(cmd, cwd=context.repo_root, capture_output=True, text=True)

    log_dir = context.repo_root / "ralph-garage/agent-logs"
    log_path = None
    if log_dir.is_dir():
        matches = sorted(log_dir.glob(f"*_{context.test_id}_*"), reverse=True)
        if matches:
            log_path = str(matches[0].relative_to(context.repo_root))

    if result.returncode != 0:
        return write_fail_report(context, f"agent wrapper failed with exit code {result.returncode}", log_path)

    verdict = parse_verdict_from_report(context.report_path)
    if verdict is None:
        return write_fail_report(context, "agent did not produce a report with a VERDICT line", log_path)

    finished_at_utc = datetime.datetime.now(datetime.timezone.utc)
    body = context.report_path.read_text(encoding="utf-8")
    header = _report_header(context.script_rel_path, context.started_at_utc, finished_at_utc, log_path)
    context.report_path.write_text(header + "\n" + body, encoding="utf-8")

    reason = parse_reason_from_report(context.report_path)
    if verdict == "FAIL":
        print(f"[{context.test_id}] FAIL: {reason or 'no reason'}")
        return 1
    print(f"[{context.test_id}] PASS")
    return 0

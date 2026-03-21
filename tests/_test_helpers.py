#!/usr/bin/env python3
"""
How to run: Imported by tests/*.py test scripts.
Inputs: test script path and optional CLI arg --agent-log-mode.
Outputs: shared utilities for test execution.
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import subprocess
import sys
from dataclasses import dataclass
from zoneinfo import ZoneInfo

VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
NEW_YORK_TZ = ZoneInfo("America/New_York")


@dataclass(frozen=True)
class TestContext:
    script_file: pathlib.Path
    repo_root: pathlib.Path
    script_rel_path: str
    test_id: str
    report_path: pathlib.Path
    started_at_utc: datetime.datetime


def parse_test_cli(default_agent_log_mode: str = "off") -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agent-log-mode",
        choices=VALID_AGENT_LOG_MODES,
        default=default_agent_log_mode,
        help="Agent log verbosity passed through to ralph/agent_wrapper.py",
    )
    return parser.parse_args()


def derive_test_id(script_file: str) -> str:
    return pathlib.Path(script_file).stem


def derive_report_path(repo_root: pathlib.Path, test_id: str) -> pathlib.Path:
    return repo_root / f"test-results/{test_id}.md"


def build_test_context(script_file: str) -> TestContext:
    script_path = pathlib.Path(script_file).resolve()
    repo_root = script_path.parents[1]
    test_id = script_path.stem
    started_at_utc = datetime.datetime.now(datetime.timezone.utc)
    return TestContext(
        script_file=script_path,
        repo_root=repo_root,
        script_rel_path=str(script_path.relative_to(repo_root)),
        test_id=test_id,
        report_path=derive_report_path(repo_root, test_id),
        started_at_utc=started_at_utc,
    )


def _format_ny(timestamp_utc: datetime.datetime) -> str:
    """Format a UTC timestamp in New York time, e.g. '2026-03-09 15:30:42 EDT'."""
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
        lines.append(f"[{log_path}](../{log_path})")
    return "\n".join(lines) + "\n"


def write_fail_report(
    report_path: pathlib.Path,
    reason: str,
    log_path: str | None = None,
    script_rel_path: str | None = None,
    started_at_utc: datetime.datetime | None = None,
) -> None:
    """Fallback report written by the test script when the agent can't run."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    finished_at_utc = datetime.datetime.now(datetime.timezone.utc)
    text = _report_header(
        script_rel_path or report_path.stem,
        started_at_utc or finished_at_utc,
        finished_at_utc,
        log_path,
    )
    text += f"\n# {report_path.stem}\nVERDICT: FAIL\nREASON: {reason}\n"
    report_path.write_text(text, encoding="utf-8")


def parse_verdict_from_report(report_path: pathlib.Path) -> str | None:
    """Read the report file and extract the VERDICT line."""
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
            reason = line.split(":", 1)[1].strip()
            if reason:
                return reason
    return None


def print_test_result(test_id: str, verdict: str, reason: str | None = None) -> None:
    line = f"[{test_id}] {verdict}"
    if reason and verdict == "FAIL":
        line += f": {reason}"
    print(line)


def fail_test(
    context: TestContext,
    reason: str,
    log_path: str | None = None,
) -> int:
    write_fail_report(
        context.report_path,
        reason,
        log_path=log_path,
        script_rel_path=context.script_rel_path,
        started_at_utc=context.started_at_utc,
    )
    print_test_result(context.test_id, "FAIL", reason)
    return 1


def require_paths(context: TestContext, *paths: pathlib.Path) -> int | None:
    for path in paths:
        if not path.exists():
            return fail_test(context, f"missing: {path}")
    return None


def require_page_images(context: TestContext, images_dir: pathlib.Path) -> int | None:
    if not any(images_dir.glob("page-*.png")):
        return fail_test(context, f"missing generated paper page images: {images_dir}")
    return None


def load_manifest(manifest_path: pathlib.Path) -> dict[str, object]:
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def require_manifest_pages(
    context: TestContext,
    manifest: dict[str, object],
    predicate,
    empty_message: str,
) -> tuple[int | None, list[dict[str, object]]]:
    pages = [page for page in manifest.get("pages", []) if predicate(page)]
    if not pages:
        return fail_test(context, empty_message), []
    return None, pages


def run_test(
    *,
    context: TestContext | None = None,
    script_file: str | None = None,
    prompt: str,
    agent: str,
    model: str | None = None,
    default_agent_log_mode: str = "off",
) -> int:
    """Common test runner. Returns exit code 0 (PASS) or 1 (FAIL)."""
    args = parse_test_cli(default_agent_log_mode=default_agent_log_mode)
    if context is None:
        if script_file is None:
            raise ValueError("run_test requires either context or script_file")
        context = build_test_context(script_file)

    cmd = [
        sys.executable,
        str(context.repo_root / "ralph/agent_wrapper.py"),
        "--agent", agent,
        "--log-mode", args.agent_log_mode,
        "--failure-log-mode", "off",
        "--step-label", context.test_id,
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)

    result = subprocess.run(cmd, cwd=context.repo_root, capture_output=True, text=True)

    # Find the most recent agent log for this test.
    log_dir = context.repo_root / "ralph-garage/agent-logs"
    log_path = None
    if log_dir.is_dir():
        matches = sorted(log_dir.glob(f"*_{context.test_id}_*"), reverse=True)
        if matches:
            log_path = str(matches[0].relative_to(context.repo_root))

    if result.returncode != 0:
        return fail_test(context, f"agent wrapper failed with exit code {result.returncode}", log_path)

    verdict = parse_verdict_from_report(context.report_path)
    if verdict is None:
        return fail_test(context, "agent did not produce a report with a VERDICT line", log_path)

    # Prepend our standard header (script path, start time, runtime, log link) to the agent-written report.
    text = context.report_path.read_text(encoding="utf-8")
    finished_at_utc = datetime.datetime.now(datetime.timezone.utc)
    header = _report_header(context.script_rel_path, context.started_at_utc, finished_at_utc, log_path)
    context.report_path.write_text(header + "\n" + text, encoding="utf-8")

    reason = parse_reason_from_report(context.report_path)
    print_test_result(context.test_id, verdict, reason)

    return 0 if verdict == "PASS" else 1

#!/usr/bin/env python3
"""
How to run: python tests/build-latex.py [--agent-log-mode off]
Inputs: paper/paper.tex, paper/paper.pdf, paper/.latex-build.log
Outputs: test-results/build-latex.md and, when used as the build gate,
         test-results/summary.json
"""

from __future__ import annotations

import json
import os
import pathlib
from datetime import datetime, timezone

from _test_helpers import NEW_YORK_TZ, _report_header, build_test_context, parse_test_cli, print_test_result


def _read_text(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _log_excerpt(log_text: str) -> str | None:
    if not log_text.strip():
        return None

    lines = log_text.splitlines()
    interesting = [
        line for line in lines
        if "ERROR:" in line or line.lstrip().startswith("!") or "Fatal error occurred" in line
    ]
    excerpt_lines = interesting[-12:] if interesting else lines[-12:]
    excerpt = "\n".join(excerpt_lines).strip()
    return excerpt or None


def _evaluate(repo_root: pathlib.Path) -> tuple[str, str, str | None]:
    paper_tex = repo_root / "paper/paper.tex"
    paper_pdf = repo_root / "paper/paper.pdf"
    build_log = repo_root / "paper/.latex-build.log"

    if not paper_tex.exists():
        return "FAIL", f"missing source file: {paper_tex}", None

    build_exit_code_raw = os.environ.get("RALPH_LATEX_BUILD_EXIT_CODE", "").strip()
    build_exit_code = None
    if build_exit_code_raw:
        try:
            build_exit_code = int(build_exit_code_raw)
        except ValueError:
            build_exit_code = None

    log_text = _read_text(build_log)
    excerpt = _log_excerpt(log_text)

    if build_exit_code not in (None, 0):
        return "FAIL", "LaTeX build failed; see paper/.latex-build.log", excerpt

    if not build_log.exists():
        return "FAIL", f"missing LaTeX build log: {build_log}", None

    if not paper_pdf.exists():
        return "FAIL", f"missing compiled paper: {paper_pdf}", excerpt

    tex_mtime = paper_tex.stat().st_mtime
    if paper_pdf.stat().st_mtime < tex_mtime:
        return "FAIL", "compiled paper is stale relative to paper/paper.tex", excerpt

    if build_log.stat().st_mtime < tex_mtime:
        return "FAIL", "LaTeX build log is stale relative to paper/paper.tex", excerpt

    if "! LaTeX Error:" in log_text or "Fatal error occurred" in log_text:
        return "FAIL", "LaTeX build log contains a fatal error", excerpt

    return "PASS", "LaTeX build completed and produced a fresh paper.pdf", None


def _write_report(
    *,
    context,
    verdict: str,
    reason: str,
    details: str | None,
) -> None:
    finished_at_utc = datetime.now(timezone.utc)
    header = _report_header(context.script_rel_path, context.started_at_utc, finished_at_utc)

    lines = [
        f"# {context.test_id}",
        f"VERDICT: {verdict}",
        f"REASON: {reason}",
    ]
    if details:
        lines.extend([
            "",
            "## Build Log Excerpt",
            "```text",
            details,
            "```",
        ])

    context.report_path.parent.mkdir(parents=True, exist_ok=True)
    context.report_path.write_text(header + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


def _write_gate_summary(*, repo_root: pathlib.Path, context, verdict: str) -> None:
    finished_at_utc = datetime.now(timezone.utc)
    payload = {
        "timestamps": {
            "started_at_utc": context.started_at_utc.isoformat(),
            "finished_at_utc": finished_at_utc.isoformat(),
            "started_at_ny": context.started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
            "finished_at_ny": finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
            "timezone": "America/New_York",
        },
        "duration_seconds": round(max(0.0, (finished_at_utc - context.started_at_utc).total_seconds()), 3),
        "tests": [
            {
                "name": context.test_id,
                "status": "pass" if verdict == "PASS" else "fail",
                "exit_code": 0 if verdict == "PASS" else 1,
                "timestamps": {
                    "started_at_utc": context.started_at_utc.isoformat(),
                    "finished_at_utc": finished_at_utc.isoformat(),
                    "started_at_ny": context.started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
                    "finished_at_ny": finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
                    "timezone": "America/New_York",
                },
                "duration_seconds": round(max(0.0, (finished_at_utc - context.started_at_utc).total_seconds()), 3),
            }
        ],
        "summary": {
            "total": 1,
            "passed": 1 if verdict == "PASS" else 0,
            "failed": 0 if verdict == "PASS" else 1,
        },
    }
    summary_path = repo_root / "test-results/summary.json"
    summary_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parse_test_cli(default_agent_log_mode="off")
    context = build_test_context(__file__)
    verdict, reason, details = _evaluate(context.repo_root)
    _write_report(context=context, verdict=verdict, reason=reason, details=details)

    if os.environ.get("RALPH_LATEX_BUILD_GATE", "").strip():
        _write_gate_summary(repo_root=context.repo_root, context=context, verdict=verdict)

    is_gate = os.environ.get("RALPH_LATEX_BUILD_GATE", "").strip()
    if verdict != "PASS" or not is_gate:
        print_test_result(context.test_id, verdict, None if verdict == "PASS" else reason)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

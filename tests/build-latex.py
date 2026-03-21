#!/usr/bin/env python3
"""
How to run: python tests/build-latex.py [--agent-log-mode off]
Inputs: paper/paper.tex, paper/paper.pdf, paper/.latex-build.log
Outputs: test-results/build-latex.md
"""

from __future__ import annotations

import pathlib
from datetime import datetime, timezone

from _test_helpers import _report_header, build_test_context, parse_test_cli, print_test_result


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

    log_text = _read_text(build_log)
    excerpt = _log_excerpt(log_text)

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


def main() -> int:
    parse_test_cli(default_agent_log_mode="off")
    context = build_test_context(__file__)
    verdict, reason, details = _evaluate(context.repo_root)
    _write_report(context=context, verdict=verdict, reason=reason, details=details)
    print_test_result(context.test_id, verdict, None if verdict == "PASS" else reason)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

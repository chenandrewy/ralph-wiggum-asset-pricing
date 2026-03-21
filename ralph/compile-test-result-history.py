#!/usr/bin/env python3
# How to run: python3 ralph/compile-test-result-history.py [--base-ref main] [--output ralph-garage/history/test-result-history.md]
# Inputs: git history from base-ref..HEAD and committed test-results/ snapshots
# Outputs: a single compiled markdown file under ralph-garage/history/

import argparse
import json
import subprocess
from pathlib import Path

SUMMARY_PATH = "test-results/summary.json"
TEST_RESULTS_DIR = "test-results"
DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = DEFAULT_REPO_ROOT / "ralph-garage" / "history" / "test-result-history.md"


def run_git(repo_root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=check,
    )


def git_output(repo_root: Path, *args: str) -> str:
    return run_git(repo_root, *args).stdout.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile committed test results since branch start.")
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument("--base-ref", default="main")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def commit_list(repo_root: Path, base_ref: str) -> list[tuple[str, str, str]]:
    merge_base = git_output(repo_root, "merge-base", "HEAD", base_ref)
    log_text = git_output(
        repo_root,
        "log",
        "--reverse",
        "--format=%H%x1f%h%x1f%s",
        f"{merge_base}..HEAD",
    )
    commits: list[tuple[str, str, str]] = []
    for line in log_text.splitlines():
        if not line.strip():
            continue
        full_hash, short_hash, subject = line.split("\x1f", 2)
        commits.append((full_hash, short_hash, subject))
    return commits


def show_file(repo_root: Path, commit_hash: str, path: str) -> str | None:
    proc = run_git(repo_root, "show", f"{commit_hash}:{path}", check=False)
    if proc.returncode != 0:
        return None
    return proc.stdout


def build_summary_table(tests: list[dict]) -> str:
    rows = ["| Test | Status |", "| --- | --- |"]
    for t in tests:
        icon = "pass" if t["status"] == "pass" else "**FAIL**"
        rows.append(f"| {t['name']} | {icon} |")
    return "\n".join(rows)


def build_section(repo_root: Path, index: int, full_hash: str, short_hash: str, subject: str) -> str | None:
    summary_text = show_file(repo_root, full_hash, SUMMARY_PATH)
    if summary_text is None:
        return None

    try:
        summary = json.loads(summary_text)
    except json.JSONDecodeError:
        return None

    tests = summary.get("tests", [])
    totals = summary.get("summary", {})
    passed = totals.get("passed", 0)
    total = totals.get("total", 0)
    started = summary.get("timestamps", {}).get("started_at_ny", "")[:16]

    lines = [
        f"# Iteration {index}",
        f"- Commit: `{short_hash}`",
        f"- Subject: {subject}",
        f"- Started: {started}",
        f"- Result: {passed}/{total} passed",
        "",
        build_summary_table(tests),
    ]

    for t in tests:
        detail_path = f"{TEST_RESULTS_DIR}/{t['name']}.md"
        detail_text = show_file(repo_root, full_hash, detail_path)
        if detail_text:
            demoted = "\n".join(
                ("##" + line) if line.startswith("#") else line
                for line in detail_text.rstrip().splitlines()
            )
            lines += ["", f"## {t['name']}", "", demoted]

    return "\n".join(lines)


def build_document(repo_root: Path, base_ref: str) -> str:
    commits = commit_list(repo_root, base_ref)
    sections: list[str] = []

    for index, (full_hash, short_hash, subject) in enumerate(commits, start=1):
        section = build_section(repo_root, index, full_hash, short_hash, subject)
        if section is not None:
            sections.append(section)

    if not sections:
        body = "_No committed test results found in this branch range._"
    else:
        body = "\n\n---\n\n".join(sections)

    return "\n".join(
        [
            "# Test Result History",
            "",
            f"- Base ref: `{base_ref}`",
            f"- Summary path: `{SUMMARY_PATH}`",
            "",
            body,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    output_path = args.output.resolve()

    doc = build_document(repo_root, args.base_ref)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(doc, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

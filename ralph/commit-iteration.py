#!/usr/bin/env python3
# How to run: python3 ralph/commit-iteration.py
# Inputs: test-results/summary.json and changes under paper/ralph-garage.
# Outputs: One git commit for the iteration created by Claude; exits non-zero if no commit is created.

import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from utils import load_config

DEFAULT_ADD_PATHS = [
    "paper",
    "ralph-garage/improvement-plan.md",
    "test-results",
]
COMMIT_PREFIX_BASE = "rloop"
COMMIT_AGENT = "claude"
COMMIT_MODEL = "sonnet"
COMMIT_AUTHOR_NAME = "Ralph Loop"
COMMIT_AUTHOR_EMAIL = "noreply@gmail.com"
COMMIT_MESSAGE_PROMPT = """\
Write a Git commit message that accurately summarizes the currently staged changes.

Instructions:
1. Inspect the currently staged changes yourself before writing the commit message.
2. Base the message only on the current staged changes for this iteration, not on prior iteration history or older plans.
3. Produce a concise, specific commit message that matches the staged changes you inspected.
4. The first line must be a subject tail only, not a full subject line with a prefix.
5. Do not include any prefix such as `rloop`, `feat:`, `fix:`, or similar in the first line.
6. Treat the commit as a Ralph iteration commit for `paper/` or `code/`, not as a change to Ralph tooling.
7. The subject tail must headline what was fixed or changed in `paper/` or `code/`, not generic repo activity.
8. If `paper/paper.tex` changed, prioritize the substantive paper revision in the subject tail.
9. Avoid vague subjects like `update paper`, `update test results`, or `misc fixes`.
10. Keep the subject tail <= 72 characters when possible.
11. Include a body.
12. In the body, describe the test failures this iteration was trying to fix, or the failures that still remain after the attempt.
13. Use short bullet points in the body with concrete statements, including failing test names and their recorded reasons when provided.

Output rules:
- Output only the commit message text: subject tail on the first line, then a blank line, then the body.
- Do not wrap output in code fences.
- Do not include explanations before or after the commit message."""
DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEST_RESULTS_DIR = DEFAULT_REPO_ROOT / "test-results"


def commit_prefix() -> str:
    config = load_config(DEFAULT_REPO_ROOT / "config-ralph.yaml")
    run_name = str(config.get("run-name", "")).strip()
    if run_name:
        return f"{COMMIT_PREFIX_BASE} [{run_name}]:"
    return f"{COMMIT_PREFIX_BASE}:"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create one Ralph iteration commit.")
    parser.add_argument("--add-path", action="append")
    return parser.parse_args()


def summary_label(test_results_dir: Path) -> str:
    summary_path = test_results_dir / "summary.json"
    if not summary_path.exists():
        return "no-summary"
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception:
        return "invalid-summary"
    summary = payload.get("summary", {})
    failed = int(summary.get("failed", 0) or 0)
    passed = summary.get("passed", "?")
    total = summary.get("total", "?")
    return f"{'pass' if failed == 0 else 'fail'} {passed}/{total}"


def summary_payload(test_results_dir: Path) -> dict:
    summary_path = test_results_dir / "summary.json"
    if not summary_path.exists():
        return {}
    try:
        return json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def git_output(repo_root: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=repo_root, capture_output=True, check=True)
    return proc.stdout.decode("utf-8", errors="replace").strip()


def git_run(repo_root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo_root, text=True, check=True)


def path_has_tracked_entries(repo_root: Path, path: str) -> bool:
    output = git_output(repo_root, "ls-files", "--", path)
    return bool(output.strip())


def existing_add_paths(repo_root: Path, paths: list[str]) -> list[str]:
    selected = []
    for path in paths:
        if (repo_root / path).exists() or path_has_tracked_entries(repo_root, path):
            selected.append(path)
    return selected


def read_reason_line(test_results_dir: Path, test_name: str) -> str | None:
    result_path = test_results_dir / f"{test_name}.md"
    if not result_path.exists():
        return None
    for line in result_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("REASON:"):
            return line.removeprefix("REASON:").strip()
    return None


def failing_test_context(test_results_dir: Path) -> str:
    payload = summary_payload(test_results_dir)
    tests = payload.get("tests", [])
    failures = [test for test in tests if test.get("status") != "pass"]
    if not failures:
        summary = payload.get("summary", {})
        passed = summary.get("passed", "?")
        total = summary.get("total", "?")
        return f"- none; current selected-test summary is pass {passed}/{total}"

    lines = []
    for test in failures:
        test_name = str(test.get("name", "unknown-test"))
        reason = read_reason_line(test_results_dir, test_name) or "no reason recorded"
        lines.append(f"- {test_name}: {reason}")
    return "\n".join(lines)


def build_prompt(repo_root: Path, test_results_dir: Path) -> str:
    prompt_template = COMMIT_MESSAGE_PROMPT
    return (
        f"{prompt_template}\n\n"
        "Context:\n"
        f"- Repository: {repo_root}\n"
        f"- Current selected-test summary: {summary_label(test_results_dir)}\n"
        "- Failing tests this iteration is trying to fix or that remain after the attempt:\n"
        f"{failing_test_context(test_results_dir)}\n"
    )


def compose_commit_message(message: str) -> str:
    lines = message.strip().splitlines()
    if not lines:
        raise RuntimeError("claude returned an empty commit message")

    subject_tail = lines[0].strip()
    if not subject_tail:
        raise RuntimeError("claude returned an empty commit subject tail")

    prefix = commit_prefix()
    if subject_tail.startswith(prefix):
        subject_tail = subject_tail[len(prefix):].strip()

    if not subject_tail:
        raise RuntimeError("claude returned a subject tail containing only the prefix")

    body_lines = lines[1:]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)

    subject = f"{prefix} {subject_tail}"
    if not body_lines:
        return subject
    return f"{subject}\n\n" + "\n".join(body_lines).rstrip()


def generate_commit_message(repo_root: Path, prompt: str) -> str:
    if COMMIT_AGENT == "codex":
        cmd = ["codex", "exec", "--sandbox", "danger-full-access", prompt]
    else:
        cmd = [
            "claude",
            "-p",
            "--output-format",
            "text",
            "--dangerously-skip-permissions",
            "--model",
            COMMIT_MODEL,
            prompt,
        ]
    proc = subprocess.run(
        cmd,
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"{COMMIT_AGENT} commit step failed\n"
            f"exit={proc.returncode}\n"
            f"stdout:\n{proc.stdout}\n"
            f"stderr:\n{proc.stderr}"
        )
    message = proc.stdout.strip()
    if not message:
        raise RuntimeError("claude returned an empty commit message")
    return compose_commit_message(message)


def commit_with_message(repo_root: Path, message: str) -> None:
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
            handle.write(message)
            if not message.endswith("\n"):
                handle.write("\n")
            tmp_path = Path(handle.name)
        subprocess.run(
            [
                "git",
                "-c",
                f"user.name={COMMIT_AUTHOR_NAME}",
                "-c",
                f"user.email={COMMIT_AUTHOR_EMAIL}",
                "commit",
                "--allow-empty",
                "-F",
                str(tmp_path),
            ],
            cwd=repo_root,
            text=True,
            check=True,
        )
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


def main() -> int:
    args = parse_args()
    repo_root = DEFAULT_REPO_ROOT
    test_results_dir = DEFAULT_TEST_RESULTS_DIR
    requested_paths = args.add_path if args.add_path else DEFAULT_ADD_PATHS

    add_paths = existing_add_paths(repo_root, requested_paths)
    git_run(repo_root, "add", "-A", "--", *add_paths)
    old_head = git_output(repo_root, "rev-parse", "HEAD")
    prompt = build_prompt(repo_root, test_results_dir)
    message = generate_commit_message(repo_root, prompt)
    commit_with_message(repo_root, message)

    new_head = git_output(repo_root, "rev-parse", "HEAD")
    if new_head == old_head:
        raise RuntimeError("claude finished but did not create a new commit")

    subject = git_output(repo_root, "show", "-s", "--format=%s", "HEAD")
    prefix = commit_prefix()
    if not subject.startswith(prefix):
        raise RuntimeError(f"head commit subject does not start with '{prefix}': {subject}")

    print(new_head)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

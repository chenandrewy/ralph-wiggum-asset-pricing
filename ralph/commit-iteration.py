#!/usr/bin/env python3
# How to run: python3 ralph/commit-iteration.py ITERATION
# Inputs: staged changes in author working directories, test-results/, improvement plan.
# Outputs: one git commit for the iteration; exits non-zero if no commit is created.

import json
import sys
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COMMIT_PREFIX_BASE = "rloop-"
COMMIT_MODEL = "sonnet"
COMMIT_AUTHOR_NAME = "Ralph Loop"
COMMIT_AUTHOR_EMAIL = "noreply@gmail.com"

ADD_PATHS = [
    "paper",
    "code",
    "ralph-garage/improvement-plan.md",
    "test-results",
]

COMMIT_MESSAGE_PROMPT = """\
Inspect the currently staged changes and write a Git commit message.

The subject should headline the substantive paper or code change.
The body should describe the test failures this iteration was trying to fix, or that remain.

Output the subject on the first line, a blank line, then the body.
Do not include a prefix like `rloop` or `feat:` in the subject — it will be added automatically.
Do not wrap output in code fences or include explanations outside the commit message.

{test_context}"""

TEST_RESULTS_DIR = REPO_ROOT / "test-results"


def parse_iteration(argv: list[str]) -> int:
    if len(argv) != 2:
        raise SystemExit("usage: python3 ralph/commit-iteration.py ITERATION")
    try:
        iteration = int(argv[1])
    except ValueError as exc:
        raise SystemExit(f"iteration must be an integer (got: {argv[1]})") from exc
    if iteration < 1:
        raise SystemExit(f"iteration must be at least 1 (got: {iteration})")
    return iteration


def commit_prefix(iteration: int) -> str:
    return f"{COMMIT_PREFIX_BASE}{iteration:02d}:"


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return proc.stdout.strip()


def has_tracked_files(path: str) -> bool:
    return bool(git("ls-files", "--", path))


def stage_paths() -> None:
    paths = [p for p in ADD_PATHS if (REPO_ROOT / p).exists() or has_tracked_files(p)]
    if paths:
        git("add", "-A", "--", *paths)


def test_context() -> str:
    summary_path = TEST_RESULTS_DIR / "summary.json"
    if not summary_path.exists():
        return "No test results available for this iteration."
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "No usable test results available for this iteration."
    tests = payload.get("tests", [])
    failures = [t for t in tests if t.get("status") != "pass"]
    if not failures:
        s = payload.get("summary", {})
        return f"All tests passed ({s.get('passed', '?')}/{s.get('total', '?')})."
    lines = ["Failing tests:"]
    for t in failures:
        name = t.get("name", "unknown")
        result_path = TEST_RESULTS_DIR / f"{name}.md"
        reason = ""
        if result_path.exists():
            for line in result_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("REASON:"):
                    reason = line.removeprefix("REASON:").strip()
                    break
        lines.append(f"- {name}: {reason or 'no reason recorded'}")
    return "\n".join(lines)


def generate_commit_message() -> str:
    prompt = COMMIT_MESSAGE_PROMPT.format(test_context=test_context())
    proc = subprocess.run(
        [
            "python3",
            str(REPO_ROOT / "ralph" / "agent_wrapper.py"),
            "--agent", "claude",
            "--failure-log-mode", "on",
            "--step-label", "commit-iteration",
            "--model", COMMIT_MODEL,
            prompt,
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    raw = proc.stdout.strip()
    if not raw:
        raise RuntimeError("claude returned an empty commit message")
    return raw


def compose_commit_message(raw: str, iteration: int) -> str:
    lines = raw.strip().splitlines()
    subject_tail = lines[0].strip()
    prefix = commit_prefix(iteration)
    # Strip prefix if Claude included it despite instructions.
    if subject_tail.startswith(prefix):
        subject_tail = subject_tail[len(prefix):].strip()
    subject = f"{prefix} {subject_tail}"
    body_lines = lines[1:]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    if not body_lines:
        return subject
    return f"{subject}\n\n" + "\n".join(body_lines).rstrip()


def commit(message: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(message + "\n")
        tmp = Path(f.name)
    try:
        git(
            "-c", f"user.name={COMMIT_AUTHOR_NAME}",
            "-c", f"user.email={COMMIT_AUTHOR_EMAIL}",
            "commit", "--allow-empty", "-F", str(tmp),
        )
    finally:
        tmp.unlink(missing_ok=True)


def main() -> int:
    iteration = parse_iteration(sys.argv)
    old_head = git("rev-parse", "HEAD")
    stage_paths()
    message = generate_commit_message()
    commit(compose_commit_message(message, iteration))
    new_head = git("rev-parse", "HEAD")
    if new_head == old_head:
        raise RuntimeError("commit was not created")
    print(new_head)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

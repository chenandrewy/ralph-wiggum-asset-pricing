#!/usr/bin/env python3
"""
How to run: python3 ralph/check-setup.py
Inputs: config-ralph.yaml
Outputs: setup-check report to stdout/stderr and process exit code (0 pass, non-zero fail)
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import is_truthy, load_config


AUTHOR_BASELINE_PATHS = ("paper", "code")
DEPRECATED_CONFIG_KEYS = ("startup-source",)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fresh-main-start",
        action="store_true",
        help="validate the fresh-start preflight rules that apply before switching from main to ralph/run",
    )
    return parser.parse_args()


def main() -> int:
    print("Checking setup...", flush=True)
    args = parse_args()

    config_path = pathlib.Path("config-ralph.yaml")
    if not config_path.is_file():
        print(f"FAIL: missing config file: {config_path}", file=sys.stderr)
        return 2

    raw = load_config(config_path)
    deprecated_keys = [key for key in DEPRECATED_CONFIG_KEYS if key in raw]
    if deprecated_keys:
        print(
            "FAIL: deprecated config key(s): "
            + ", ".join(deprecated_keys)
            + "; Ralph now starts from committed live paper/ and code/. "
            "Copy any startup candidate into paper/ and code/, commit it on main, and remove the deprecated key.",
            file=sys.stderr,
        )
        return 2
    config_values = {k: v.lower() if isinstance(v, str) else v for k, v in raw.items()}

    try:
        current_branch = subprocess.run(
            ["git", "branch", "--show-current"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except subprocess.CalledProcessError:
        print("FAIL: unable to determine current git branch", file=sys.stderr)
        return 2

    # --- required files ---
    required_files = [pathlib.Path("spec/paper-spec.md")]
    if current_branch == "ralph/run" or args.fresh_main_start:
        required_files.append(pathlib.Path("paper/paper.tex"))
    for path in required_files:
        if not path.is_file():
            print(f"FAIL: missing required file: {path}", file=sys.stderr)
            return 2

    if args.fresh_main_start:
        if current_branch != "main":
            print("FAIL: --fresh-main-start requires starting from main", file=sys.stderr)
            return 2
        for path in (pathlib.Path("paper"), pathlib.Path("code")):
            if not path.is_dir():
                print(
                    f"FAIL: {path} must exist on main before a fresh Ralph stretch; Ralph starts from live paper/ and code/",
                    file=sys.stderr,
                )
                return 2
        tracked = subprocess.run(
            ["git", "ls-files", "--", *AUTHOR_BASELINE_PATHS],
            check=False,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        missing_tracked = [
            path
            for path in AUTHOR_BASELINE_PATHS
            if not any(item == path or item.startswith(f"{path}/") for item in tracked)
        ]
        if missing_tracked:
            print(
                "FAIL: paper/ and code/ must be tracked and committed on main before starting Ralph; "
                "missing tracked path(s): "
                + ", ".join(f"{path}/" for path in missing_tracked),
                file=sys.stderr,
            )
            return 2
        unstaged = subprocess.run(["git", "diff", "--quiet", "--", *AUTHOR_BASELINE_PATHS])
        if unstaged.returncode != 0:
            print(
                "FAIL: paper/ and code/ have unstaged changes; commit them on main before starting Ralph",
                file=sys.stderr,
            )
            return 2
        staged = subprocess.run(["git", "diff", "--cached", "--quiet", "--", *AUTHOR_BASELINE_PATHS])
        if staged.returncode != 0:
            print(
                "FAIL: paper/ and code/ have staged but uncommitted changes; commit them on main before starting Ralph",
                file=sys.stderr,
            )
            return 2
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard", "--", *AUTHOR_BASELINE_PATHS],
            check=False,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        if untracked:
            print(
                "FAIL: paper/ and code/ contain untracked files; commit them on main before starting Ralph: "
                + ", ".join(untracked),
                file=sys.stderr,
            )
            return 2

    ci = str(config_values.get("continual-improvement", "false"))
    referees = str(config_values.get("referees", "false"))
    if is_truthy(ci) and not is_truthy(referees):
        print(
            "FAIL: continual-improvement requires referees to be enabled",
            file=sys.stderr,
        )
        return 2

    # --- validate selected-tests ---
    test_mode = str(config_values.get("test-mode", "all")).strip()
    if test_mode == "selected":
        selected_tests_raw = config_values.get("selected-tests", [])
        if not isinstance(selected_tests_raw, list):
            selected_tests = [item.strip() for item in str(selected_tests_raw).split(",") if item.strip()]
        else:
            selected_tests = [str(item).strip() for item in selected_tests_raw if str(item).strip()]
        if not selected_tests:
            print("FAIL: test-mode is 'selected' but selected-tests is empty", file=sys.stderr)
            return 2

        tests_dir = pathlib.Path("tests")
        available_tests = []
        if tests_dir.is_dir():
            available_tests = sorted(
                path.stem
                for path in tests_dir.glob("*.py")
                if not path.stem.startswith("_") and not path.stem.startswith("referee-")
            )
        available_set = set(available_tests)
        unknown = [test_id for test_id in selected_tests if test_id not in available_set]
        if unknown:
            print(
                "FAIL: unknown selected-tests value(s): "
                + ", ".join(unknown)
                + "; known tests: "
                + ", ".join(available_tests),
                file=sys.stderr,
            )
            return 2

    # --- validate selected-referees ---
    if is_truthy(referees):
        selected_referees_raw = config_values.get("selected-referees", [])
        if not isinstance(selected_referees_raw, list):
            selected_referees = [item.strip() for item in str(selected_referees_raw).split(",") if item.strip()]
        else:
            selected_referees = [str(item).strip() for item in selected_referees_raw if str(item).strip()]
        if not selected_referees:
            print("FAIL: referees requires selected-referees to be non-empty", file=sys.stderr)
            return 2

        referees_dir = pathlib.Path("tests")
        available_referees = []
        if referees_dir.is_dir():
            available_referees = sorted(
                path.stem
                for path in referees_dir.glob("referee-*.py")
            )
        available_set = set(available_referees)
        unknown = [referee_id for referee_id in selected_referees if referee_id not in available_set]
        if unknown:
            print(
                "FAIL: unknown selected-referees value(s): "
                + ", ".join(unknown)
                + "; known referees: "
                + ", ".join(available_referees),
                file=sys.stderr,
            )
            return 2

    # --- WRDS availability (advisory) ---
    wrds_check = pathlib.Path(".credentials/check-wrds.py")
    if wrds_check.is_file():
        wrds_result = subprocess.run(
            [sys.executable, str(wrds_check)], capture_output=True
        )
        if wrds_result.returncode != 0:
            print(
                "WARNING: WRDS is not available. If the paper needs WRDS data, "
                "rerun `python .credentials/setup.py` on your host/local machine, "
                "then reopen or rebuild the devcontainer before starting Ralph.",
                file=sys.stderr,
            )
    else:
        print(f"WARNING: missing WRDS checker: {wrds_check}", file=sys.stderr)

    # Agent auth check. The loop may use Claude or Codex depending on ralph/author-*.py,
    # so at least one must be logged in.
    claude_auth = subprocess.run(
        ["claude", "auth", "status"], check=False, capture_output=True
    )
    if claude_auth.returncode != 0:
        print("WARNING: Claude is not logged in", file=sys.stderr)
    codex_auth = subprocess.run(
        ["codex", "login", "status"], check=False, capture_output=True
    )
    if codex_auth.returncode != 0:
        print("WARNING: Codex is not logged in", file=sys.stderr)

    if claude_auth.returncode != 0 and codex_auth.returncode != 0:
        print("FAIL: neither Claude nor Codex is logged in", file=sys.stderr)
        return 2

    print("Setup check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

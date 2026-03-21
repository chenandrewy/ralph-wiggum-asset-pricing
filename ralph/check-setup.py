#!/usr/bin/env python3
"""
How to run: python3 ralph/check-setup.py
Inputs: config-ralph.yaml
Outputs: setup-check report to stdout/stderr and process exit code (0 pass, non-zero fail)
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import is_truthy, load_config


def main() -> int:
    print("Checking setup...")

    config_path = pathlib.Path("config-ralph.yaml")
    if not config_path.is_file():
        print(f"FAIL: missing config file: {config_path}", file=sys.stderr)
        return 2

    raw = load_config(config_path)
    config_values = {k: v.lower() if isinstance(v, str) else v for k, v in raw.items()}

    # --- required files ---
    required_files = [
        pathlib.Path("paper/paper.tex"),
        pathlib.Path("spec/paper-spec.md"),
    ]
    for path in required_files:
        if not path.is_file():
            print(f"FAIL: missing required file: {path}", file=sys.stderr)
            return 2

    ci = str(config_values.get("continual-improvement", "false"))
    reviews = str(config_values.get("reviews", "false"))
    if is_truthy(ci) and not is_truthy(reviews):
        print(
            "FAIL: continual-improvement requires reviews to be enabled",
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

    # --- validate selected-reviews ---
    if is_truthy(reviews):
        selected_reviews_raw = config_values.get("selected-reviews", [])
        if not isinstance(selected_reviews_raw, list):
            selected_reviews = [item.strip() for item in str(selected_reviews_raw).split(",") if item.strip()]
        else:
            selected_reviews = [str(item).strip() for item in selected_reviews_raw if str(item).strip()]
        if not selected_reviews:
            print("FAIL: reviews requires selected-reviews to be non-empty", file=sys.stderr)
            return 2

        reviews_dir = pathlib.Path("tests")
        available_reviews = []
        if reviews_dir.is_dir():
            available_reviews = sorted(
                path.stem
                for path in reviews_dir.glob("referee-*.py")
            )
        available_set = set(available_reviews)
        unknown = [review_id for review_id in selected_reviews if review_id not in available_set]
        if unknown:
            print(
                "FAIL: unknown selected-reviews value(s): "
                + ", ".join(unknown)
                + "; known reviews: "
                + ", ".join(available_reviews),
                file=sys.stderr,
            )
            return 2

    print("Setup check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

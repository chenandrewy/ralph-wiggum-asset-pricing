#!/usr/bin/env python3
"""
How to run: python ralph/run-tests.py [--jobs N]
Inputs: config-ralph.yaml, code/*, paper/paper.tex, paper/paper.pdf, ralph-garage/page-images/page-*.png, ralph-garage/page-images/exhibit-manifest.json, ralph/agent_wrapper.py, tests/*.py
Outputs: test-results/summary.json
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import clear_transient_results_dir, load_config, write_json_atomic


VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
IGNORED_TEST_FILENAMES = {"__init__.py"}
NEW_YORK_TZ = ZoneInfo("America/New_York")
PAGE_IMAGES_DIR = "ralph-garage/page-images"
EXHIBIT_MANIFEST = "ralph-garage/page-images/exhibit-manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run paper test suite")
    parser.add_argument(
        "--jobs",
        type=int,
        default=None,
        help="Number of tests to run in parallel (default: all selected tests)",
    )
    return parser.parse_args()



def discover_tests(tests_dir: pathlib.Path) -> list[str]:
    if not tests_dir.exists():
        raise ValueError(f"missing tests directory: {tests_dir}")

    test_ids: list[str] = []
    for path in sorted(tests_dir.glob("*.py")):
        if path.name in IGNORED_TEST_FILENAMES:
            continue
        if path.stem.startswith("_") or path.stem.startswith("referee-"):
            continue
        test_ids.append(path.stem)

    if not test_ids:
        raise ValueError(f"no test scripts discovered under: {tests_dir}")
    return test_ids


def selected_tests_from_config(config: dict[str, object], available_tests: list[str]) -> tuple[str, list[str]]:
    mode = str(config.get("test-mode") or "all").strip()
    if mode not in {"all", "selected"}:
        raise ValueError(f"invalid test-mode '{mode}', expected 'all' or 'selected'")

    if mode == "all":
        return mode, list(available_tests)

    selected_raw = config.get("selected-tests", [])
    if isinstance(selected_raw, list):
        selected_ids = [str(item).strip() for item in selected_raw if str(item).strip()]
    else:
        selected_ids = [item.strip() for item in str(selected_raw).split(",") if item.strip()]
    if not selected_ids:
        raise ValueError("test-mode is 'selected' but selected-tests is empty")

    available_set = set(available_tests)
    unknown = [test_id for test_id in selected_ids if test_id not in available_set]
    if unknown:
        known = ", ".join(available_tests)
        unknown_joined = ", ".join(unknown)
        raise ValueError(f"unknown selected-tests value(s): {unknown_joined}; known tests: {known}")

    selected_set = set(selected_ids)
    selected = [test_id for test_id in available_tests if test_id in selected_set]
    return mode, selected


def agent_log_mode_from_config(config: dict[str, object]) -> str:
    mode = str(config.get("agent-log-mode") or "off").strip().lower()
    if mode not in VALID_AGENT_LOG_MODES:
        allowed = ", ".join(sorted(VALID_AGENT_LOG_MODES))
        raise ValueError(f"invalid agent-log-mode '{mode}', expected one of: {allowed}")
    return mode


def run_single_test(
    repo_root_str: str,
    tests_dir_str: str,
    test_name: str,
    agent_log_mode: str,
) -> dict[str, object]:
    repo_root = pathlib.Path(repo_root_str)
    tests_dir = pathlib.Path(tests_dir_str)
    test_script = tests_dir / f"{test_name}.py"
    cmd = [sys.executable, str(test_script), "--agent-log-mode", agent_log_mode]
    started_at_utc = datetime.now(timezone.utc)
    result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
    finished_at_utc = datetime.now(timezone.utc)
    return {
        "name": test_name,
        "exit_code": result.returncode,
        "stdout": result.stdout or "",
        "stderr": result.stderr or "",
        "started_at_utc": started_at_utc.isoformat(),
        "finished_at_utc": finished_at_utc.isoformat(),
        "started_at_ny": started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "finished_at_ny": finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "duration_seconds": round(max(0.0, (finished_at_utc - started_at_utc).total_seconds()), 3),
    }


def validate_test_artifacts(repo_root: pathlib.Path) -> int:
    pdf_path = repo_root / "paper/paper.pdf"
    if not pdf_path.exists():
        print(f"ERROR: missing compiled paper: {pdf_path}", file=sys.stderr)
        return 1

    images_dir = repo_root / PAGE_IMAGES_DIR
    images = sorted(images_dir.glob("page-*.png"))
    if not images:
        print(f"ERROR: missing page images under: {images_dir}", file=sys.stderr)
        return 1

    pdf_mtime = pdf_path.stat().st_mtime
    oldest_image_mtime = min(image.stat().st_mtime for image in images)
    if oldest_image_mtime < pdf_mtime:
        print(
            "ERROR: page images are stale relative to paper/paper.pdf; "
            "rebuild the paper and regenerate page images before running tests",
            file=sys.stderr,
        )
        return 1

    manifest_path = repo_root / EXHIBIT_MANIFEST
    if not manifest_path.exists():
        print(f"ERROR: missing exhibit manifest: {manifest_path}", file=sys.stderr)
        return 1

    if manifest_path.stat().st_mtime < pdf_mtime:
        print(
            "ERROR: exhibit manifest is stale relative to paper/paper.pdf; "
            "rebuild the paper artifacts before running tests",
            file=sys.stderr,
        )
        return 1

    return 0



def main() -> int:
    args = parse_args()
    if args.jobs is not None and args.jobs < 1:
        print(f"ERROR: --jobs must be >= 1 (got: {args.jobs})", file=sys.stderr)
        return 1

    repo_root = pathlib.Path(__file__).resolve().parents[1]
    tests_dir = repo_root / "tests"
    config_path = repo_root / "config-ralph.yaml"
    try:
        config = load_config(config_path, list_keys={"selected-tests"})
        available_tests = discover_tests(tests_dir)
        test_mode, selected_tests = selected_tests_from_config(config, available_tests)
        agent_log_mode = agent_log_mode_from_config(config)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    summary_path = repo_root / "test-results/summary.json"
    clear_transient_results_dir(summary_path.parent)
    run_started_at_utc = datetime.now(timezone.utc)

    if validate_test_artifacts(repo_root) != 0:
        return 1

    workers = len(selected_tests) if args.jobs is None else min(args.jobs, len(selected_tests))
    selected_text = ", ".join(selected_tests)
    print(
        f"[run-tests] mode={test_mode}; agent-log-mode={agent_log_mode}; running {len(selected_tests)} tests "
        f"with {workers} parallel job(s): {selected_text}"
    )

    outputs_by_name: dict[str, dict[str, object]] = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                run_single_test,
                str(repo_root),
                str(tests_dir),
                test_name,
                agent_log_mode,
            ): test_name
            for test_name in selected_tests
        }
        for future in concurrent.futures.as_completed(futures):
            test_name = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                errored_at_utc = datetime.now(timezone.utc)
                result = {
                    "name": test_name,
                    "exit_code": 1,
                    "stdout": "",
                    "stderr": f"ERROR: exception while running {test_name}: {exc}\n",
                    "started_at_utc": errored_at_utc.isoformat(),
                    "finished_at_utc": errored_at_utc.isoformat(),
                    "started_at_ny": errored_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
                    "finished_at_ny": errored_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
                    "duration_seconds": 0.0,
                }
            outputs_by_name[test_name] = result

    results = []
    for test_name in selected_tests:
        result = outputs_by_name[test_name]
        for line in result["stdout"].splitlines():
            print(f"  {line}")
        for line in result["stderr"].splitlines():
            print(f"  {line}", file=sys.stderr)

        passed = result["exit_code"] == 0
        results.append({
            "name": test_name,
            "status": "pass" if passed else "fail",
            "exit_code": result["exit_code"],
            "timestamps": {
                "started_at_utc": result["started_at_utc"],
                "finished_at_utc": result["finished_at_utc"],
                "started_at_ny": result["started_at_ny"],
                "finished_at_ny": result["finished_at_ny"],
                "timezone": "America/New_York",
            },
            "duration_seconds": result["duration_seconds"],
        })

    num_passed = sum(1 for r in results if r["status"] == "pass")
    run_finished_at_utc = datetime.now(timezone.utc)
    payload = {
        "timestamps": {
            "started_at_utc": run_started_at_utc.isoformat(),
            "finished_at_utc": run_finished_at_utc.isoformat(),
            "started_at_ny": run_started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
            "finished_at_ny": run_finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
            "timezone": "America/New_York",
        },
        "duration_seconds": round(max(0.0, (run_finished_at_utc - run_started_at_utc).total_seconds()), 3),
        "tests": results,
        "summary": {
            "total": len(results),
            "passed": num_passed,
            "failed": len(results) - num_passed,
        },
    }
    write_json_atomic(summary_path, payload)
    return 0 if num_passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

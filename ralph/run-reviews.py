#!/usr/bin/env python3
"""
How to run: python ralph/run-reviews.py
Inputs: config-ralph.yaml, tests/referee-*.py
Outputs: test-results/summary.json (reviews section)
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config

VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
NEW_YORK_TZ = ZoneInfo("America/New_York")


def agent_log_mode_from_config(config: dict[str, object]) -> str:
    mode = str(config.get("agent-log-mode") or "off").strip().lower()
    if mode not in VALID_AGENT_LOG_MODES:
        allowed = ", ".join(sorted(VALID_AGENT_LOG_MODES))
        raise ValueError(f"invalid agent-log-mode '{mode}', expected one of: {allowed}")
    return mode


def discover_reviews(reviews_dir: pathlib.Path) -> list[str]:
    if not reviews_dir.exists():
        return []
    review_ids: list[str] = []
    for path in sorted(reviews_dir.glob("referee-*.py")):
        review_ids.append(path.stem)
    return review_ids

def selected_reviews_from_config(config: dict[str, object], available_reviews: list[str]) -> list[str]:
    reviews_enabled = str(config.get("reviews") or "false").strip().lower()
    if reviews_enabled not in {"true", "on", "yes", "1"}:
        return []

    selected_raw = config.get("selected-reviews", [])
    if isinstance(selected_raw, list):
        selected_ids = [str(item).strip() for item in selected_raw if str(item).strip()]
    else:
        selected_ids = [item.strip() for item in str(selected_raw).split(",") if item.strip()]
    if not selected_ids:
        raise ValueError("reviews is enabled but selected-reviews is empty")

    available_set = set(available_reviews)
    unknown = [review_id for review_id in selected_ids if review_id not in available_set]
    if unknown:
        known = ", ".join(available_reviews)
        unknown_joined = ", ".join(unknown)
        raise ValueError(f"unknown selected-reviews value(s): {unknown_joined}; known reviews: {known}")

    selected_set = set(selected_ids)
    return [review_id for review_id in available_reviews if review_id in selected_set]


def run_single_review(
    repo_root: pathlib.Path,
    reviews_dir: pathlib.Path,
    review_name: str,
    agent_log_mode: str,
) -> dict[str, object]:
    review_script = reviews_dir / f"{review_name}.py"
    cmd = [sys.executable, str(review_script), "--agent-log-mode", agent_log_mode]
    started_at_utc = datetime.now(timezone.utc)
    result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
    finished_at_utc = datetime.now(timezone.utc)
    return {
        "name": review_name,
        "exit_code": result.returncode,
        "status": "completed" if result.returncode == 0 else "errored",
        "started_at_utc": started_at_utc.isoformat(),
        "finished_at_utc": finished_at_utc.isoformat(),
        "started_at_ny": started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "finished_at_ny": finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "duration_seconds": round(max(0.0, (finished_at_utc - started_at_utc).total_seconds()), 3),
    }



def _merge_reviews_into_summary(summary_path: pathlib.Path, results: list[dict[str, object]]) -> None:
    """Merge referee review results into the existing summary.json."""
    if summary_path.exists():
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    else:
        payload = {}
    payload["reviews"] = results
    payload["review_summary"] = {
        "total": len(results),
        "completed": sum(1 for r in results if r.get("status") == "completed"),
        "errored": sum(1 for r in results if r.get("status") == "errored"),
    }
    summary_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    config_path = repo_root / "config-ralph.yaml"
    reviews_dir = repo_root / "tests"
    results_dir = repo_root / "test-results"
    results_dir.mkdir(parents=True, exist_ok=True)
    # Clean only referee result files (not test results in the shared dir)
    for p in results_dir.glob("referee-*.md"):
        p.unlink()
    summary_path = results_dir / "summary.json"

    try:
        config = load_config(config_path, list_keys={"selected-reviews"})
        available_reviews = discover_reviews(reviews_dir)
        review_ids = selected_reviews_from_config(config, available_reviews)
        agent_log_mode = agent_log_mode_from_config(config)
    except ValueError as exc:
        print(f"[run-reviews] config error: {exc}", file=sys.stderr)
        _merge_reviews_into_summary(summary_path, [])
        return 0

    if not review_ids:
        print("[run-reviews] no review scripts found; skipping")
        _merge_reviews_into_summary(summary_path, [])
        return 0

    print(f"[run-reviews] running {len(review_ids)} review(s): {', '.join(review_ids)}")

    results = []
    for review_id in review_ids:
        print(f"[run-reviews] starting {review_id}")
        result = run_single_review(repo_root, reviews_dir, review_id, agent_log_mode)
        print(f"[run-reviews] completed {review_id} ({result['status']})")
        results.append(result)

    _merge_reviews_into_summary(summary_path, results)

    # Reviews always exit 0 — they never block the loop.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

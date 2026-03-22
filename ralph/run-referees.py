#!/usr/bin/env python3
"""
How to run: python ralph/run-referees.py
Inputs: config-ralph.yaml, tests/referee-*.py
Outputs: test-results/summary.json (referees section)
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config, write_json_atomic

VALID_AGENT_LOG_MODES = ("off", "verbose", "all", "1", "true", "yes")
NEW_YORK_TZ = ZoneInfo("America/New_York")


def agent_log_mode_from_config(config: dict[str, object]) -> str:
    mode = str(config.get("agent-log-mode") or "off").strip().lower()
    if mode not in VALID_AGENT_LOG_MODES:
        allowed = ", ".join(sorted(VALID_AGENT_LOG_MODES))
        raise ValueError(f"invalid agent-log-mode '{mode}', expected one of: {allowed}")
    return mode


def discover_referees(referees_dir: pathlib.Path) -> list[str]:
    if not referees_dir.exists():
        return []
    referee_ids: list[str] = []
    for path in sorted(referees_dir.glob("referee-*.py")):
        referee_ids.append(path.stem)
    return referee_ids

def selected_referees_from_config(config: dict[str, object], available_referees: list[str]) -> list[str]:
    referees_enabled = str(config.get("referees") or "false").strip().lower()
    if referees_enabled not in {"true", "on", "yes", "1"}:
        return []

    selected_raw = config.get("selected-referees", [])
    if isinstance(selected_raw, list):
        selected_ids = [str(item).strip() for item in selected_raw if str(item).strip()]
    else:
        selected_ids = [item.strip() for item in str(selected_raw).split(",") if item.strip()]
    if not selected_ids:
        raise ValueError("referees is enabled but selected-referees is empty")

    available_set = set(available_referees)
    unknown = [referee_id for referee_id in selected_ids if referee_id not in available_set]
    if unknown:
        known = ", ".join(available_referees)
        unknown_joined = ", ".join(unknown)
        raise ValueError(f"unknown selected-referees value(s): {unknown_joined}; known referees: {known}")

    selected_set = set(selected_ids)
    return [referee_id for referee_id in available_referees if referee_id in selected_set]


def run_single_referee(
    repo_root: pathlib.Path,
    referees_dir: pathlib.Path,
    referee_name: str,
    agent_log_mode: str,
) -> dict[str, object]:
    referee_script = referees_dir / f"{referee_name}.py"
    cmd = [sys.executable, str(referee_script), "--agent-log-mode", agent_log_mode]
    started_at_utc = datetime.now(timezone.utc)
    result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
    finished_at_utc = datetime.now(timezone.utc)
    return {
        "name": referee_name,
        "exit_code": result.returncode,
        "status": "completed" if result.returncode == 0 else "errored",
        "started_at_utc": started_at_utc.isoformat(),
        "finished_at_utc": finished_at_utc.isoformat(),
        "started_at_ny": started_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "finished_at_ny": finished_at_utc.astimezone(NEW_YORK_TZ).isoformat(),
        "duration_seconds": round(max(0.0, (finished_at_utc - started_at_utc).total_seconds()), 3),
    }



def _merge_referees_into_summary(summary_path: pathlib.Path, results: list[dict[str, object]]) -> None:
    """Merge referee results into the existing summary.json."""
    if summary_path.exists():
        try:
            payload = json.loads(summary_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            payload = {}
    else:
        payload = {}
    payload["referees"] = results
    payload["referee_summary"] = {
        "total": len(results),
        "completed": sum(1 for r in results if r.get("status") == "completed"),
        "errored": sum(1 for r in results if r.get("status") == "errored"),
    }
    write_json_atomic(summary_path, payload)


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    config_path = repo_root / "config-ralph.yaml"
    referees_dir = repo_root / "tests"
    results_dir = repo_root / "test-results"
    results_dir.mkdir(parents=True, exist_ok=True)
    # Clean only referee result files (not test results in the shared dir)
    for p in results_dir.glob("referee-*.md"):
        p.unlink()
    summary_path = results_dir / "summary.json"

    try:
        config = load_config(config_path, list_keys={"selected-referees"})
        available_referees = discover_referees(referees_dir)
        referee_ids = selected_referees_from_config(config, available_referees)
        agent_log_mode = agent_log_mode_from_config(config)
    except ValueError as exc:
        print(f"[run-referees] config error: {exc}", file=sys.stderr)
        _merge_referees_into_summary(summary_path, [])
        return 0

    if not referee_ids:
        print("[run-referees] no referee scripts found; skipping")
        _merge_referees_into_summary(summary_path, [])
        return 0

    print(f"[run-referees] running {len(referee_ids)} referee(s): {', '.join(referee_ids)}")

    results = []
    for referee_id in referee_ids:
        print(f"[run-referees] starting {referee_id}")
        result = run_single_referee(repo_root, referees_dir, referee_id, agent_log_mode)
        print(f"[run-referees] completed {referee_id} ({result['status']})")
        results.append(result)

    _merge_referees_into_summary(summary_path, results)

    # Referees always exit 0; they never block the loop.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

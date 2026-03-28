#!/usr/bin/env python3
# Shared utilities for ralph loop tools.
# Imported by: read-config.py, run-tests.py, run-referees.py, check-setup.py,
#              author-plan.py, author-improve.py

from __future__ import annotations

import json
import pathlib
import re
import shutil
import tempfile
from datetime import datetime, timedelta, timezone


STALE_RESULTS_MAX_AGE = timedelta(hours=1)

PRESERVED_RESULT_FILENAMES = {".gitkeep"}

_LIST_KEYS_DEFAULT = {"selected-tests", "selected-referees"}
VALID_AGENT_EFFORTS = ("none", "low", "medium", "high", "max", "xhigh")


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def is_truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "on", "yes", "1"}


def normalize_agent_effort(value: object) -> str | None:
    normalized = str(value or "").strip().lower()
    return normalized or None


def load_config(
    config_path: pathlib.Path,
    list_keys: set[str] | None = None,
) -> dict[str, object]:
    """Parse config-ralph.yaml. Keys in *list_keys* are returned as lists."""
    if list_keys is None:
        list_keys = _LIST_KEYS_DEFAULT
    if not config_path.is_file():
        raise ValueError(f"missing config file: {config_path}")

    payload: dict[str, object] = {}
    lines = config_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line.strip()
        if not raw or raw.startswith("#") or ":" not in line:
            i += 1
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.split("#", 1)[0].strip()

        if key not in list_keys:
            payload[key] = strip_quotes(value)
            i += 1
            continue

        items: list[str] = []
        if value:
            scalar = strip_quotes(value)
            if scalar not in {"", "[]"}:
                items = [item.strip() for item in scalar.split(",") if item.strip()]
            payload[key] = items
            i += 1
            continue

        i += 1
        while i < len(lines):
            child_line = lines[i]
            child_raw = child_line.strip()
            if not child_raw or child_raw.startswith("#"):
                i += 1
                continue
            match = re.match(r"^\s*-\s*(.+?)\s*$", child_line)
            if match:
                item = strip_quotes(match.group(1).split("#", 1)[0].strip())
                if item:
                    items.append(item)
                i += 1
                continue
            if re.match(r"^[A-Za-z0-9_-]+\s*:", child_line):
                break
            break
        payload[key] = items
    return payload


def clear_transient_results_dir(results_dir: pathlib.Path) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    for path in results_dir.iterdir():
        if path.name in PRESERVED_RESULT_FILENAMES:
            continue
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def summary_results_instruction(
    *,
    repo_root: pathlib.Path,
    summary_rel_path: str,
    missing_message: str,
    invalid_message: str,
    stale_message: str,
    fresh_message: str,
) -> str:
    summary_path = repo_root / summary_rel_path
    if not summary_path.is_file():
        return missing_message

    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
        finished_at_raw = payload["timestamps"]["finished_at_utc"]
        finished_at_utc = datetime.fromisoformat(str(finished_at_raw))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        return invalid_message

    if finished_at_utc.tzinfo is None:
        finished_at_utc = finished_at_utc.replace(tzinfo=timezone.utc)

    if datetime.now(timezone.utc) - finished_at_utc > STALE_RESULTS_MAX_AGE:
        return stale_message

    return fresh_message


def write_json_atomic(path: pathlib.Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as handle:
        tmp_path = pathlib.Path(handle.name)
        handle.write(json.dumps(payload, indent=2) + "\n")
    tmp_path.replace(path)

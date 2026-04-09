#!/usr/bin/env python3
# How to run: eval "$(python3 ralph/load-config.py)"
# Inputs: config-ralph.yaml
# Outputs: shell variable assignments to stdout; errors to stderr with exit 1

from __future__ import annotations

import pathlib
import shlex
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config

CONFIG_PATH = pathlib.Path("config-ralph.yaml")

DEFAULTS = {
    "agent-log-mode": "off",
    "test-before-loop": "off",
    "referees": "false",
    "continual-improvement": "false",
    "quota-preflight": "off",
    "claude-5h-utilization-limit": "0.67",
    "run-note": "",
    "startup-source": "",
}

VALID_AGENT_LOG_MODES = {"off", "verbose", "all", "1", "true", "yes"}
VALID_BOOLEANS = {"off", "on", "1", "true", "yes", "false", "no", "0"}


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


def parse_unit_interval(name: str, raw_value: object) -> float:
    text = str(raw_value).strip()
    try:
        value = float(text)
    except ValueError as exc:
        raise ValueError(f"{name} must be a number between 0 and 1 (got: {text})") from exc
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be between 0 and 1 inclusive (got: {text})")
    return value


def main() -> int:
    if not CONFIG_PATH.is_file():
        return fail(f"missing config file: {CONFIG_PATH}")

    config = load_config(CONFIG_PATH, list_keys=set())

    def get(key: str) -> str:
        val = config.get(key, DEFAULTS.get(key, ""))
        return str(val).strip().lower() if val else DEFAULTS.get(key, "")

    max_iter = str(config.get("max-iter", "")).strip()
    if not max_iter.isdigit() or int(max_iter) < 1:
        return fail(f"max-iter must be a positive integer (got: {max_iter})")

    agent_log_mode = get("agent-log-mode")
    if agent_log_mode not in VALID_AGENT_LOG_MODES:
        return fail(f"agent-log-mode must be one of: {', '.join(sorted(VALID_AGENT_LOG_MODES))} (got: {agent_log_mode})")

    test_before = get("test-before-loop")
    if test_before not in VALID_BOOLEANS:
        return fail(f"test-before-loop must be a boolean value (got: {test_before})")

    referees = get("referees")
    continual = get("continual-improvement")
    quota_preflight = get("quota-preflight")
    if quota_preflight not in VALID_BOOLEANS:
        return fail(f"quota-preflight must be a boolean value (got: {quota_preflight})")
    try:
        claude_5h_utilization_limit = parse_unit_interval(
            "claude-5h-utilization-limit",
            config.get("claude-5h-utilization-limit", DEFAULTS["claude-5h-utilization-limit"]),
        )
    except ValueError as exc:
        return fail(str(exc))
    run_note = str(config.get("run-note", "")).strip()
    startup_source = str(config.get("startup-source", "")).strip()

    print(f"MAX_ITER={max_iter}")
    print(f"AGENT_LOG_MODE={agent_log_mode}")
    print(f"TEST_BEFORE_LOOP={test_before}")
    print(f"REFEREES_ENABLED={referees}")
    print(f"CONTINUAL_IMPROVEMENT={continual}")
    print(f"QUOTA_PREFLIGHT={quota_preflight}")
    print(f"CLAUDE_5H_UTILIZATION_LIMIT={claude_5h_utilization_limit}")
    print(f"RUN_NOTE={shlex.quote(run_note)}")
    print(f"STARTUP_SOURCE={shlex.quote(startup_source)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

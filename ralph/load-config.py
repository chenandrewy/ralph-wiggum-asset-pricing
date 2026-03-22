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
    "reviews": "false",
    "continual-improvement": "false",
    "run-name": "",
}

VALID_AGENT_LOG_MODES = {"off", "verbose", "all", "1", "true", "yes"}
VALID_BOOLEANS = {"off", "on", "1", "true", "yes", "false", "no", "0"}


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


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

    reviews = get("reviews")
    continual = get("continual-improvement")
    run_name = str(config.get("run-name", "")).strip()

    print(f"MAX_ITER={max_iter}")
    print(f"AGENT_LOG_MODE={agent_log_mode}")
    print(f"TEST_BEFORE_LOOP={test_before}")
    print(f"REVIEWS_ENABLED={reviews}")
    print(f"CONTINUAL_IMPROVEMENT={continual}")
    print(f"RUN_NAME={shlex.quote(run_name)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

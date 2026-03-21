#!/usr/bin/env python3
"""
How to run: python3 ralph/prune-agent-logs.py --log-dir ralph-garage/agent-logs --retention-days 1
Inputs: agent log directory path and retention window in days
Outputs: deletes log files older than the retention window and prints a short summary
"""

from __future__ import annotations

import argparse
import pathlib
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Delete old agent logs.")
    parser.add_argument("--log-dir", required=True, help="Directory containing agent logs")
    parser.add_argument(
        "--retention-days",
        type=int,
        required=True,
        help="Delete files older than this many days; 0 disables pruning",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_dir = pathlib.Path(args.log_dir)
    retention_days = args.retention_days

    if retention_days < 0:
        raise SystemExit("ERROR: --retention-days must be >= 0")

    if retention_days == 0:
        print(f"Agent log pruning disabled for {log_dir}")
        return 0

    if not log_dir.exists():
        print(f"Agent log directory does not exist yet: {log_dir}")
        return 0

    cutoff_epoch = time.time() - (retention_days * 24 * 60 * 60)
    deleted = 0

    for path in log_dir.iterdir():
        if not path.is_file() or path.name == ".gitkeep":
            continue
        if path.stat().st_mtime >= cutoff_epoch:
            continue
        path.unlink()
        deleted += 1

    if deleted > 0:
        print(f"Pruned {deleted} agent log file(s) older than {retention_days} day(s) from {log_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

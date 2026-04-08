#!/usr/bin/env python3
"""
How to run: python3 ralph/check-claude-budget.py --phase <label> [--model MODEL] [--utilization-limit FLOAT]
Inputs: Claude CLI access and current quota state
Outputs: human-readable status lines to stdout; exit code 0=continue, 2=stop for low quota, 1=error
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass


DEFAULT_MODEL = "opus"
DEFAULT_UTILIZATION_LIMIT = 0.67
PROMPT = "Reply with READY."


@dataclass(frozen=True)
class RateLimitSnapshot:
    rate_limit_type: str
    status: str
    utilization: float | None
    resets_at: float | None


def format_budget_snapshot(snapshot: RateLimitSnapshot | None) -> str:
    if snapshot is None:
        return "unavailable"

    parts = [f"status={snapshot.status or 'unknown'}"]
    if snapshot.utilization is not None:
        remaining = max(0.0, 1.0 - snapshot.utilization)
        parts.append(f"used={snapshot.utilization:.2f}")
        parts.append(f"remaining={remaining:.2f}")
    else:
        parts.append("used=unknown")
        parts.append("remaining=unknown")
    if snapshot.resets_at is not None:
        parts.append(f"resets_at={snapshot.resets_at:.0f}")
    return " ".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe Claude quota telemetry before launching a costly phase")
    parser.add_argument("--phase", required=True, help="Short label for the upcoming phase")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Claude model used for the probe")
    parser.add_argument(
        "--utilization-limit",
        type=float,
        default=DEFAULT_UTILIZATION_LIMIT,
        help="Stop if five-hour utilization is at or above this threshold",
    )
    return parser.parse_args()


def load_latest_snapshot(stream_json_text: str, rate_limit_type: str) -> RateLimitSnapshot | None:
    latest: RateLimitSnapshot | None = None
    for line in stream_json_text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if payload.get("type") != "rate_limit_event":
            continue
        info = payload.get("rate_limit_info")
        if not isinstance(info, dict):
            continue
        if str(info.get("rateLimitType") or "").strip() != rate_limit_type:
            continue
        utilization_raw = info.get("utilization")
        utilization = float(utilization_raw) if isinstance(utilization_raw, (int, float)) else None
        resets_at_raw = info.get("resetsAt")
        resets_at = float(resets_at_raw) if isinstance(resets_at_raw, (int, float)) else None
        latest = RateLimitSnapshot(
            rate_limit_type=rate_limit_type,
            status=str(info.get("status") or "").strip(),
            utilization=utilization,
            resets_at=resets_at,
        )
    return latest


def main() -> int:
    args = parse_args()
    if args.utilization_limit < 0.0 or args.utilization_limit > 1.0:
        print(
            f"ERROR: --utilization-limit must be between 0 and 1 inclusive (got: {args.utilization_limit})",
            file=sys.stderr,
        )
        return 1

    cmd = [
        "claude",
        "-p",
        "--verbose",
        "--output-format",
        "stream-json",
        "--dangerously-skip-permissions",
        "--model",
        args.model,
        PROMPT,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print("ERROR: Claude CLI is not installed or not on PATH for quota preflight", file=sys.stderr)
        return 1
    stream_json_text = result.stdout or ""

    latest_five_hour = load_latest_snapshot(stream_json_text, "five_hour")
    latest_seven_day = load_latest_snapshot(stream_json_text, "seven_day")

    if result.returncode != 0:
        stderr_text = (result.stderr or "").strip()
        if stderr_text:
            print(stderr_text, file=sys.stderr)
        print(
            f"ERROR: Claude quota preflight probe failed for phase '{args.phase}' with exit code {result.returncode}",
            file=sys.stderr,
        )
        return 1

    print(
        f"[quota-preflight] phase={args.phase} model={args.model} "
        f"five_hour_budget={format_budget_snapshot(latest_five_hour)} "
        f"seven_day_budget={format_budget_snapshot(latest_seven_day)}"
    )

    if latest_five_hour is not None and latest_five_hour.utilization is not None:
        print(f"[quota-preflight] five_hour_limit={args.utilization_limit:.2f}")
        if latest_five_hour.status == "rejected" or latest_five_hour.utilization >= args.utilization_limit:
            print(
                f"[quota-preflight] stopping before {args.phase}: five-hour utilization is too high for a clean batch run"
            )
            return 2
        return 0

    if latest_five_hour is not None and latest_five_hour.status == "rejected":
        print(f"[quota-preflight] five_hour_limit={args.utilization_limit:.2f}")
        print(f"[quota-preflight] stopping before {args.phase}: five-hour quota is already rejected")
        return 2

    if latest_seven_day is not None and latest_seven_day.status == "rejected":
        print(f"[quota-preflight] stopping before {args.phase}: seven-day quota is already rejected")
        return 2

    print(f"[quota-preflight] no rate-limit telemetry observed; continuing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

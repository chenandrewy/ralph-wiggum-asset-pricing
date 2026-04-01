#!/usr/bin/env python3
"""
How to run: python3 ralph/summarize-agent-costs.py [--log-dir ralph-garage/agent-logs] [--json]
Inputs: verbose agent logs under ralph-garage/agent-logs
Outputs: prints per-step agent cost and token-usage summaries; optionally writes JSON to stdout
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_DIR = DEFAULT_REPO_ROOT / "ralph-garage" / "agent-logs"


@dataclass
class LogRecord:
    path: Path
    step_label: str
    model: str
    exit_code: int | None
    duration_ms: int | None
    total_cost_usd: float
    input_tokens: int
    output_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize agent cost and token usage from verbose Ralph logs.")
    parser.add_argument("--log-dir", type=Path, default=DEFAULT_LOG_DIR, help="Directory containing verbose agent logs")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    parser.add_argument(
        "--include-incomplete",
        action="store_true",
        help="Include logs that do not have a final result event if they expose a partial usage block",
    )
    return parser.parse_args()


def parse_header_value(lines: list[str], key: str) -> str | None:
    prefix = f"{key}: "
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return None


def parse_result_events(text: str) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    in_stream_json = False

    for line in text.splitlines():
        if line == "[STREAM_JSON]":
            in_stream_json = True
            continue
        if in_stream_json and line.startswith("------------------------------------------------------------------------"):
            break
        if not in_stream_json:
            continue
        raw = line.strip()
        if not raw or not raw.startswith("{"):
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            events.append(payload)

    return events


def extract_log_record(path: Path, include_incomplete: bool) -> LogRecord | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    step_label = parse_header_value(lines[:12], "step_label")
    model = parse_header_value(lines[:12], "model")
    exit_code_text = parse_header_value(lines[:12], "exit_code")
    exit_code = int(exit_code_text) if exit_code_text and exit_code_text.lstrip("-").isdigit() else None

    result_event = None
    partial_usage = None
    for event in parse_result_events(text):
        if event.get("type") == "result":
            result_event = event
        if partial_usage is None and isinstance(event.get("usage"), dict):
            partial_usage = event["usage"]

    if result_event is None and not include_incomplete:
        return None

    usage = result_event.get("usage") if isinstance(result_event, dict) else None
    if not isinstance(usage, dict):
        usage = partial_usage
    if not isinstance(usage, dict):
        return None

    if not step_label or not model:
        stem_parts = path.stem.split("_")
        if len(stem_parts) >= 4:
            step_label = step_label or stem_parts[1]
            model = model or "_".join(stem_parts[3:])
    if not step_label or not model:
        return None

    return LogRecord(
        path=path,
        step_label=step_label,
        model=model,
        exit_code=exit_code,
        duration_ms=int(result_event["duration_ms"]) if isinstance(result_event, dict) and isinstance(result_event.get("duration_ms"), int) else None,
        total_cost_usd=float(result_event.get("total_cost_usd", 0.0)) if isinstance(result_event, dict) else 0.0,
        input_tokens=int(usage.get("input_tokens", 0) or 0),
        output_tokens=int(usage.get("output_tokens", 0) or 0),
        cache_read_input_tokens=int(usage.get("cache_read_input_tokens", 0) or 0),
        cache_creation_input_tokens=int(usage.get("cache_creation_input_tokens", 0) or 0),
    )


def classify_step(step_label: str) -> str:
    if step_label.startswith("factcheck-") or step_label.startswith("quality-") or step_label.startswith("spec-") or step_label.startswith("visual-"):
        return "test"
    if step_label.startswith("referee-"):
        return "referee"
    if step_label.startswith("author-"):
        return "author"
    return "other"


def format_usd(value: float) -> str:
    return f"${value:,.4f}"


def format_ms(duration_ms: int | None) -> str:
    if duration_ms is None:
        return "n/a"
    seconds = duration_ms / 1000.0
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes, secs = divmod(int(round(seconds)), 60)
    if minutes < 60:
        return f"{minutes}m {secs}s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {secs}s"


def build_payload(records: list[LogRecord]) -> dict[str, object]:
    grouped: dict[str, dict[str, object]] = {}
    total_cost = 0.0

    by_step: dict[str, list[LogRecord]] = defaultdict(list)
    for record in records:
        by_step[record.step_label].append(record)
        total_cost += record.total_cost_usd

    for step_label, items in sorted(by_step.items()):
        total_step_cost = sum(item.total_cost_usd for item in items)
        grouped[step_label] = {
            "step_label": step_label,
            "kind": classify_step(step_label),
            "runs": len(items),
            "models": sorted({item.model for item in items}),
            "total_cost_usd": round(total_step_cost, 6),
            "average_cost_usd": round(total_step_cost / len(items), 6),
            "total_input_tokens": sum(item.input_tokens for item in items),
            "total_output_tokens": sum(item.output_tokens for item in items),
            "total_cache_read_input_tokens": sum(item.cache_read_input_tokens for item in items),
            "total_cache_creation_input_tokens": sum(item.cache_creation_input_tokens for item in items),
            "average_duration_ms": round(
                sum(item.duration_ms for item in items if item.duration_ms is not None)
                / max(1, sum(1 for item in items if item.duration_ms is not None))
            ),
            "logs": [
                {
                    "path": str(item.path),
                    "model": item.model,
                    "exit_code": item.exit_code,
                    "duration_ms": item.duration_ms,
                    "cost_usd": round(item.total_cost_usd, 6),
                    "input_tokens": item.input_tokens,
                    "output_tokens": item.output_tokens,
                    "cache_read_input_tokens": item.cache_read_input_tokens,
                    "cache_creation_input_tokens": item.cache_creation_input_tokens,
                }
                for item in sorted(items, key=lambda item: item.path.name)
            ],
        }

    return {
        "log_dir": str(DEFAULT_LOG_DIR),
        "parsed_logs": len(records),
        "total_cost_usd": round(total_cost, 6),
        "steps": sorted(grouped.values(), key=lambda item: (-item["total_cost_usd"], item["step_label"])),
    }


def render_markdown(payload: dict[str, object]) -> str:
    rows = [
        [
            str(step["step_label"]),
            str(step["kind"]),
            str(step["runs"]),
            format_usd(float(step["total_cost_usd"])),
            format_usd(float(step["average_cost_usd"])),
            format_ms(int(step["average_duration_ms"])),
            f"{int(step['total_input_tokens']):,}",
            f"{int(step['total_output_tokens']):,}",
            f"{int(step['total_cache_read_input_tokens']):,}",
            f"{int(step['total_cache_creation_input_tokens']):,}",
        ]
        for step in payload["steps"]
    ]
    headers = [
        "Step",
        "Kind",
        "Runs",
        "Total Cost",
        "Avg Cost",
        "Avg Runtime",
        "In Tok",
        "Out Tok",
        "Cache Read",
        "Cache Create",
        "% Total",
    ]
    total_cost = float(payload["total_cost_usd"])
    widths = [len(header) for header in headers]
    rows_with_share: list[list[str]] = []
    for row, step in zip(rows, payload["steps"]):
        share = 0.0 if total_cost == 0 else (float(step["total_cost_usd"]) / total_cost) * 100.0
        row = [*row, f"{share:.1f}%"]
        rows_with_share.append(row)
        for idx, value in enumerate(row):
            widths[idx] = max(widths[idx], len(value))

    numeric_cols = {2, 3, 4, 6, 7, 8, 9, 10}

    def fmt_row(values: list[str]) -> str:
        cells = []
        for idx, value in enumerate(values):
            if idx in numeric_cols:
                cells.append(value.rjust(widths[idx]))
            else:
                cells.append(value.ljust(widths[idx]))
        return "  ".join(cells)

    divider = "  ".join("-" * width for width in widths)
    lines = [
        "# Agent Cost Summary",
        "",
        f"Log dir:     {payload['log_dir']}",
        f"Parsed logs: {payload['parsed_logs']}",
        f"Total cost:  {format_usd(float(payload['total_cost_usd']))}",
        "",
        fmt_row(headers),
        divider,
    ]
    lines.extend(fmt_row(row) for row in rows_with_share)
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    log_dir = args.log_dir.resolve()

    if not log_dir.exists():
        raise SystemExit(f"ERROR: log directory does not exist: {log_dir}")

    records: list[LogRecord] = []
    for path in sorted(log_dir.glob("*.log")):
        if path.name == "agent-failure.log":
            continue
        record = extract_log_record(path, include_incomplete=args.include_incomplete)
        if record is not None:
            records.append(record)

    payload = build_payload(records)
    payload["log_dir"] = str(log_dir)

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(render_markdown(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

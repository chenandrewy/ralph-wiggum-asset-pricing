#!/usr/bin/env python3
# How to run: python3 ralph/extract-test-result-history.py [test-name] [--history ralph-garage/history/test-result-history.md] [--output ralph-garage/history/writing-flow-history.md]
# Inputs: compiled test result history markdown and a test name such as writing-flow
# Outputs: a markdown file containing only that test's results across iterations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HISTORY = DEFAULT_REPO_ROOT / "ralph-garage" / "history" / "test-result-history.md"
ITERATION_HEADER_RE = re.compile(r"^# Iteration (\d+)\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract one test's history from the compiled Ralph test history.")
    parser.add_argument("test_name", nargs="?", help="Test name to extract, for example writing-flow")
    parser.add_argument("--history", type=Path, default=DEFAULT_HISTORY)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def normalize_test_name(name: str) -> str:
    normalized = name.strip()
    if normalized.endswith(".py") or normalized.endswith(".md"):
        normalized = normalized.rsplit(".", 1)[0]
    return normalized


def resolve_test_name(raw_name: str | None) -> str:
    if raw_name:
        test_name = normalize_test_name(raw_name)
        if test_name:
            return test_name

    if sys.stdin.isatty():
        prompted = input("Test to extract: ").strip()
        test_name = normalize_test_name(prompted)
        if test_name:
            return test_name

    raise SystemExit("Provide the test to extract, for example: python3 ralph/extract-test-result-history.py writing-flow")


def default_output_path(history_path: Path, test_name: str) -> Path:
    return history_path.parent / f"test-{test_name}-history.md"


def split_sections(lines: list[str]) -> list[dict[str, object]]:
    sections: list[dict[str, object]] = []
    current: dict[str, object] | None = None

    for line in lines:
        match = ITERATION_HEADER_RE.match(line)
        if match:
            if current is not None:
                sections.append(current)
            current = {
                "iteration": int(match.group(1)),
                "lines": [line],
            }
            continue

        if current is not None:
            current["lines"].append(line)

    if current is not None:
        sections.append(current)

    return sections


def extract_test_block(section_lines: list[str], test_name: str) -> list[str] | None:
    target_header = f"## {test_name}"
    start_idx: int | None = None

    for idx, line in enumerate(section_lines):
        if line == target_header:
            start_idx = idx
            break

    if start_idx is None:
        return None

    end_idx = len(section_lines)
    for idx in range(start_idx + 1, len(section_lines)):
        line = section_lines[idx]
        if line.startswith("## "):
            end_idx = idx
            break

    return section_lines[start_idx:end_idx]


def extract_iteration_metadata(section_lines: list[str]) -> list[str]:
    metadata: list[str] = []
    saw_metadata_content = False

    for line in section_lines:
        if line.startswith("## "):
            break
        if line.startswith("| "):
            break
        if line == "" and saw_metadata_content:
            break
        metadata.append(line)
        if line.startswith("# ") or line.startswith("- "):
            saw_metadata_content = True

    while metadata and metadata[-1] == "":
        metadata.pop()
    return metadata


def build_document(history_path: Path, test_name: str) -> str:
    lines = history_path.read_text(encoding="utf-8").splitlines()
    sections = split_sections(lines)
    extracted_sections: list[str] = []

    for section in sections:
        section_lines = section["lines"]
        test_block = extract_test_block(section_lines, test_name)
        if test_block is None:
            continue
        metadata = extract_iteration_metadata(section_lines)
        extracted_sections.append("\n".join(metadata + [""] + test_block).rstrip())

    if not extracted_sections:
        body = f"_No results found for `{test_name}` in `{history_path}`._"
    else:
        body = "\n\n---\n\n".join(extracted_sections)

    return "\n".join(
        [
            f"# {test_name} Test Result History",
            "",
            f"- Source history: `{history_path}`",
            f"- Test name: `{test_name}`",
            "",
            body,
            "",
        ]
    )


def main() -> int:
    args = parse_args()
    history_path = args.history.resolve()
    test_name = resolve_test_name(args.test_name)
    output_path = args.output.resolve() if args.output else default_output_path(history_path, test_name)

    document = build_document(history_path, test_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

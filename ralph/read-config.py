#!/usr/bin/env python3
# How to run: python3 ralph/read-config.py config-ralph.yaml key [default]
# Inputs: config-ralph.yaml
# Outputs: prints the requested scalar config value to stdout

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from utils import load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read one scalar value from config-ralph.yaml.")
    parser.add_argument("config_path")
    parser.add_argument("key")
    parser.add_argument("default", nargs="?")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = pathlib.Path(args.config_path)
    if not config_path.is_file():
        print(f"ERROR: missing config file: {config_path}", file=sys.stderr)
        return 1

    config = load_config(config_path, list_keys=set())
    value = config.get(args.key)
    if value is not None and value != "":
        print(value)
        return 0

    if args.default is not None:
        print(args.default)
        return 0

    print(f"ERROR: missing key '{args.key}' in {config_path}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

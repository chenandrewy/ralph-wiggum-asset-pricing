#!/usr/bin/env python3
# How to run: python3 ralph/install_startup_source.py <startup-source>
# Inputs: startup-source path from config-ralph.yaml, source directories under ralph/research-template/ or ralph-garage/check-direction/
# Outputs: clears live paper/ and code/ and installs the selected startup baseline

from __future__ import annotations

import pathlib
import shutil
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE_SOURCE = pathlib.Path("ralph/research-template")
CHECK_DIRECTION_ROOT = pathlib.Path("ralph-garage/check-direction")
LIVE_DIRS = ("paper", "code")


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def validate_startup_source(raw_value: str) -> pathlib.Path:
    startup_source = pathlib.Path(raw_value.strip())
    if raw_value.strip() == "":
        raise ValueError("startup-source is required for a fresh Ralph stretch from main")
    if startup_source.is_absolute():
        raise ValueError(f"startup-source must be repo-relative (got absolute path: {raw_value})")
    if ".." in startup_source.parts:
        raise ValueError(f"startup-source must not contain '..' (got: {raw_value})")
    if startup_source == TEMPLATE_SOURCE:
        return startup_source
    if len(startup_source.parts) == 3 and startup_source.parts[:2] == CHECK_DIRECTION_ROOT.parts and startup_source.parts[2].startswith("run-"):
        return startup_source
    raise ValueError(
        "startup-source must be 'ralph/research-template' or a directory under 'ralph-garage/check-direction/run-*' "
        f"(got: {raw_value})"
    )


def require_source_layout(source_root: pathlib.Path, raw_value: str) -> None:
    if not source_root.is_dir():
        raise ValueError(f"startup-source does not exist: {raw_value}")
    for dirname in LIVE_DIRS:
        if not (source_root / dirname).is_dir():
            raise ValueError(f"startup-source is missing required directory '{dirname}/': {raw_value}")


def clear_live_dir(dirname: str) -> None:
    target = REPO_ROOT / dirname
    if target.exists():
        shutil.rmtree(target)


def copy_live_dir(source_root: pathlib.Path, dirname: str) -> None:
    shutil.copytree(source_root / dirname, REPO_ROOT / dirname)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        return fail("usage: python3 ralph/install_startup_source.py <startup-source>")

    raw_value = argv[1]
    try:
        startup_source = validate_startup_source(raw_value)
        source_root = REPO_ROOT / startup_source
        require_source_layout(source_root, raw_value)
    except ValueError as exc:
        return fail(str(exc))

    for dirname in LIVE_DIRS:
        clear_live_dir(dirname)
    for dirname in LIVE_DIRS:
        copy_live_dir(source_root, dirname)

    print(f"Installed startup baseline from {startup_source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

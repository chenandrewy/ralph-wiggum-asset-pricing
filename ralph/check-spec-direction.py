#!/usr/bin/env python3
# How to run: python3 ralph/check-spec-direction.py [--runs 5] [--base-ref HEAD] [--keep-worktrees]
# Inputs: current git state, ralph/wipe.sh, ralph/author-plan.py, ralph/author-improve.py
# Outputs: ralph-garage/check-spec-direction/run-XX/{paper.tex, paper.pdf}

from __future__ import annotations

import argparse
import concurrent.futures
import pathlib
import shutil
import subprocess
import sys
from dataclasses import dataclass


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "ralph-garage" / "check-spec-direction"
WORKTREES_ROOT = REPO_ROOT / "worktrees" / "check-spec-direction"
LATEX_TEMPLATE_DIR = REPO_ROOT / "ralph" / "code-templates" / "latex"


@dataclass(frozen=True)
class RunContext:
    index: int
    worktree_path: pathlib.Path


def run_cmd(cmd: list[str], *, cwd: pathlib.Path, check: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        capture_output=True,
    )
    if check and result.returncode != 0:
        joined = " ".join(cmd)
        raise subprocess.CalledProcessError(
            result.returncode,
            joined,
            output=result.stdout,
            stderr=result.stderr,
        )
    return result


def validate_inputs() -> None:
    required_paths = [
        REPO_ROOT / "ralph" / "wipe.sh",
        REPO_ROOT / "ralph" / "author-plan.py",
        REPO_ROOT / "ralph" / "author-improve.py",
        REPO_ROOT / "spec" / "paper-spec.md",
        LATEX_TEMPLATE_DIR,
    ]
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        missing_str = ", ".join(str(path.relative_to(REPO_ROOT)) for path in missing)
        raise FileNotFoundError(f"missing required path(s): {missing_str}")
    run_cmd(["git", "rev-parse", "--show-toplevel"], cwd=REPO_ROOT, check=True)


def reset_main_paper_dir() -> None:
    paper_dir = REPO_ROOT / "paper"
    if paper_dir.exists():
        shutil.rmtree(paper_dir)
    paper_dir.mkdir(parents=True, exist_ok=True)

    for src_file in LATEX_TEMPLATE_DIR.rglob("*"):
        if not src_file.is_file():
            continue
        rel_path = src_file.relative_to(LATEX_TEMPLATE_DIR)
        dst_file = paper_dir / rel_path
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dst_file)


def prepare_worktrees(base_ref: str, runs: int) -> list[RunContext]:
    WORKTREES_ROOT.mkdir(parents=True, exist_ok=True)
    contexts: list[RunContext] = []
    for index in range(1, runs + 1):
        worktree_path = WORKTREES_ROOT / f"run-{index:02d}"
        if worktree_path.exists():
            raise FileExistsError(f"worktree path already exists: {worktree_path}")
        run_cmd(
            ["git", "worktree", "add", "--detach", str(worktree_path), base_ref],
            cwd=REPO_ROOT,
            check=True,
        )
        contexts.append(RunContext(index=index, worktree_path=worktree_path))
    return contexts


def cleanup_worktrees(contexts: list[RunContext]) -> None:
    for context in contexts:
        if context.worktree_path.exists():
            run_cmd(
                ["git", "worktree", "remove", "--force", str(context.worktree_path)],
                cwd=REPO_ROOT,
            )
    run_cmd(["git", "worktree", "prune"], cwd=REPO_ROOT)


def run_single(context: RunContext) -> tuple[int, bool, str]:
    steps = [
        ["bash", "ralph/wipe.sh", "--yes"],
        [sys.executable, "ralph/author-plan.py"],
        [sys.executable, "ralph/author-improve.py"],
    ]
    for cmd in steps:
        result = run_cmd(cmd, cwd=context.worktree_path)
        if result.returncode != 0:
            return context.index, False, " ".join(cmd)

    paper_src_dir = context.worktree_path / "paper"
    if not (paper_src_dir / "paper.tex").is_file():
        return context.index, False, "paper/paper.tex missing after author-improve"

    # Copy the entire paper/ directory so exhibits and other assets are available for the build
    run_dir = OUTPUT_DIR / f"run-{context.index:02d}"
    shutil.copytree(paper_src_dir, run_dir)
    return context.index, True, ""


LATEX_INTERMEDIATE_EXTS = [".aux", ".log", ".out", ".toc", ".lof", ".lot", ".fls", ".fdb_latexmk", ".synctex.gz", ".nav", ".snm", ".vrb", ".bbl", ".blg", ".bcf", ".run.xml"]


def build_pdf(run_dir: pathlib.Path) -> tuple[pathlib.Path, bool, str]:
    # pdflatex → biber → pdflatex × 2  (resolves citations and cross-refs)
    steps = [
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "paper.tex"],
        ["biber", "paper"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "paper.tex"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "paper.tex"],
    ]
    for cmd in steps:
        result = run_cmd(cmd, cwd=run_dir)
        if result.returncode != 0:
            label = cmd[0]
            return run_dir, False, result.stdout[-500:] if result.stdout else f"{label} failed"
    return run_dir, True, ""


def cleanup_latex_intermediates(run_dir: pathlib.Path) -> None:
    for ext in LATEX_INTERMEDIATE_EXTS:
        for f in run_dir.glob(f"*{ext}"):
            f.unlink()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run several isolated AuthorPlan+AuthorImprove trials and copy back only paper.tex outputs.",
    )
    parser.add_argument("--runs", type=int, default=5, help="number of trials to run (default: 5)")
    parser.add_argument("--base-ref", default="HEAD", help="git ref to seed each worktree from (default: HEAD)")
    parser.add_argument(
        "--keep-worktrees",
        action="store_true",
        help="preserve created worktrees after the run instead of removing them",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.runs <= 0:
        print("ERROR: --runs must be positive", file=sys.stderr)
        return 2

    validate_inputs()
    resolved_base = run_cmd(
        ["git", "rev-parse", "--verify", args.base_ref],
        cwd=REPO_ROOT,
        check=True,
    ).stdout.strip()
    reset_main_paper_dir()

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    contexts: list[RunContext] = []
    failures: list[tuple[int, str]] = []
    try:
        contexts = prepare_worktrees(resolved_base, args.runs)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.runs) as executor:
            futures = [executor.submit(run_single, context) for context in contexts]
            for future in concurrent.futures.as_completed(futures):
                index, ok, detail = future.result()
                if ok:
                    print(f"run-{index:02d}: wrote ralph-garage/check-spec-direction/run-{index:02d}/")
                else:
                    failures.append((index, detail))
                    print(f"run-{index:02d}: failed ({detail})", file=sys.stderr)
    finally:
        if contexts and not args.keep_worktrees:
            cleanup_worktrees(contexts)

    if failures:
        return 1

    # Build PDFs — each run has its own subdirectory with the full paper/ contents
    run_dirs = sorted(OUTPUT_DIR.glob("run-*/"))
    if run_dirs:
        print(f"\nbuilding {len(run_dirs)} PDF(s)...")
        for run_dir in run_dirs:
            run_dir, ok, detail = build_pdf(run_dir)
            label = run_dir.name
            if ok:
                print(f"  {label}/paper.pdf: ok")
            else:
                print(f"  {label}/paper.pdf: build failed", file=sys.stderr)
            cleanup_latex_intermediates(run_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

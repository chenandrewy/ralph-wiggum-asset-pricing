#!/usr/bin/env bash
# How to run: bash set-ralph-direction.sh [--runs 5] [--base-ref HEAD] [--keep-worktrees]
# Inputs: current git state, ralph/check-direction.py
# Outputs: updates live paper/ and code/ from one selected candidate under ralph-garage/check-direction/
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

RUNS=5
BASE_REF="HEAD"
KEEP_WORKTREES=0

while [ "$#" -gt 0 ]; do
    case "$1" in
        --runs)
            RUNS="$2"
            shift 2
            ;;
        --base-ref)
            BASE_REF="$2"
            shift 2
            ;;
        --keep-worktrees)
            KEEP_WORKTREES=1
            shift
            ;;
        *)
            echo "Usage: bash set-ralph-direction.sh [--runs N] [--base-ref REF] [--keep-worktrees]" >&2
            exit 2
            ;;
    esac
done

cmd=(python3 ralph/check-direction.py --runs "$RUNS" --base-ref "$BASE_REF")
if [ "$KEEP_WORKTREES" -eq 1 ]; then
    cmd+=(--keep-worktrees)
fi

"${cmd[@]}"

OUTPUT_ROOT="$REPO_ROOT/ralph-garage/check-direction"
if [ ! -d "$OUTPUT_ROOT" ]; then
    echo "ERROR: expected output directory $OUTPUT_ROOT" >&2
    exit 1
fi

printf '\nAvailable direction candidates:\n'
for run_dir in "$OUTPUT_ROOT"/run-*; do
    [ -d "$run_dir" ] || continue
    printf '  %s\n' "$(basename "$run_dir")"
done

read -r -p "Select a candidate to promote into paper/ and code/ (example: run-03): " selection
SELECTED_DIR="$OUTPUT_ROOT/$selection"
if [ ! -d "$SELECTED_DIR" ]; then
    echo "ERROR: candidate not found: $selection" >&2
    exit 1
fi

if [ ! -d "$SELECTED_DIR/paper" ] || [ ! -d "$SELECTED_DIR/code" ]; then
    echo "ERROR: candidate is missing paper/ or code/: $selection" >&2
    exit 1
fi

read -r -p "Overwrite live paper/ and code/ with $selection? [y/N] " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

rm -rf "$REPO_ROOT/paper" "$REPO_ROOT/code"
cp -R "$SELECTED_DIR/paper" "$REPO_ROOT/paper"
cp -R "$SELECTED_DIR/code" "$REPO_ROOT/code"

printf 'Promoted %s into live paper/ and code/.\n' "$selection"

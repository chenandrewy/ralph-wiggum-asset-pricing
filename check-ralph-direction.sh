#!/usr/bin/env bash
# How to run: bash check-ralph-direction.sh [--runs 5] [--base-ref HEAD] [--keep-worktrees]
# Inputs: committed check-direction inputs, ralph/check-direction.py
# Outputs: candidate directories under ralph-garage/check-direction/ and suggested copy commands
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
            echo "Usage: bash check-ralph-direction.sh [--runs N] [--base-ref REF] [--keep-worktrees]" >&2
            exit 2
            ;;
    esac
done

cmd=(python3 ralph/check-direction.py --runs "$RUNS" --base-ref "$BASE_REF")
if [ "$KEEP_WORKTREES" -eq 1 ]; then
    cmd+=(--keep-worktrees)
fi

check_direction_rc=0
if "${cmd[@]}"; then
    check_direction_rc=0
else
    check_direction_rc=$?
fi
if [ "$check_direction_rc" -eq 2 ]; then
    echo "ERROR: check-direction preflight failed; not listing existing candidates." >&2
    exit "$check_direction_rc"
fi

OUTPUT_ROOT="$REPO_ROOT/ralph-garage/check-direction"
if [ ! -d "$OUTPUT_ROOT" ]; then
    echo "ERROR: expected output directory $OUTPUT_ROOT" >&2
    exit 1
fi

shopt -s nullglob
run_dirs=("$OUTPUT_ROOT"/run-*)
shopt -u nullglob
if [ "${#run_dirs[@]}" -eq 0 ]; then
    if [ "$check_direction_rc" -ne 0 ]; then
        echo "ERROR: check-direction failed and produced no candidates." >&2
        exit "$check_direction_rc"
    fi
    echo "ERROR: no direction candidates found in $OUTPUT_ROOT" >&2
    exit 1
fi

if [ "$check_direction_rc" -ne 0 ]; then
    echo "WARNING: one or more runs failed, but successful candidates are available below." >&2
fi

printf '\nAvailable direction candidates:\n'
for run_dir in "${run_dirs[@]}"; do
    printf '  %s\n' "$(basename "$run_dir")"
done

read -r -p "Choose a candidate to copy into live paper/ and code/ (example: run-03): " selection
SELECTED_DIR="$OUTPUT_ROOT/$selection"
if [ ! -d "$SELECTED_DIR" ]; then
    echo "ERROR: candidate not found: $selection" >&2
    exit 1
fi

if [ ! -d "$SELECTED_DIR/paper" ] || [ ! -d "$SELECTED_DIR/code" ]; then
    echo "ERROR: candidate is missing paper/ or code/: $selection" >&2
    exit 1
fi

SELECTED_SOURCE="ralph-garage/check-direction/$selection"
printf '\nTo use this candidate before starting Ralph from main, run:\n'
printf 'rm -rf paper code\n'
printf 'cp -R %s/paper paper\n' "$SELECTED_SOURCE"
printf 'cp -R %s/code code\n' "$SELECTED_SOURCE"
printf 'git add -A -- paper code && git commit -m "Update Ralph startup baseline"\n'

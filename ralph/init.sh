#!/usr/bin/env bash
# How to run: bash ralph/init.sh [--force]
# Inputs: ralph/code-templates/latex/*
# Outputs: initializes paper/ and ralph-garage/* with starter files

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FORCE=0

if [ "${1:-}" = "--force" ]; then
    FORCE=1
elif [ "${1:-}" != "" ]; then
    echo "ERROR: unsupported argument: $1" >&2
    echo "Usage: bash ralph/init.sh [--force]" >&2
    exit 1
fi

LATEX_TEMPLATE_DIR="$REPO_ROOT/ralph/code-templates/latex"

if [ ! -d "$LATEX_TEMPLATE_DIR" ]; then
    echo "ERROR: missing template directory: $LATEX_TEMPLATE_DIR" >&2
    exit 1
fi

mkdir -p \
    "$REPO_ROOT/paper" \
    "$REPO_ROOT/test-results" \
    "$REPO_ROOT/ralph-garage/agent-logs" \
    "$REPO_ROOT/ralph-garage/page-images" \
    "$REPO_ROOT/ralph-garage/history"

copy_templates() {
    local src_dir="$1"
    local dst_dir="$2"
    local copied=0
    local skipped=0

    while IFS= read -r -d '' src_file; do
        local rel="${src_file#"$src_dir"/}"
        local dst_file="$dst_dir/$rel"
        mkdir -p "$(dirname "$dst_file")"
        if [ -e "$dst_file" ] && [ "$FORCE" -ne 1 ]; then
            skipped=$((skipped + 1))
            continue
        fi
        cp -f "$src_file" "$dst_file"
        copied=$((copied + 1))
    done < <(find "$src_dir" -type f -print0)

    printf 'Template sync %s -> %s: copied=%d skipped=%d\n' "$src_dir" "$dst_dir" "$copied" "$skipped"
}

copy_templates "$LATEX_TEMPLATE_DIR" "$REPO_ROOT/paper"

touch "$REPO_ROOT/test-results/.gitkeep"
touch "$REPO_ROOT/ralph-garage/agent-logs/.gitkeep"

echo "Initialization complete."

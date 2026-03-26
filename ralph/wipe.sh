#!/usr/bin/env bash
# How to run: bash ralph/wipe.sh
# Inputs: none
# Outputs: empties author working directories, empties test-results/, removes ralph-garage/
#
# Gives Ralph a blank slate before starting a new run.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LATEX_TEMPLATE_DIR="$REPO_ROOT/ralph/code-templates/latex"
ASSUME_YES=0

if [ "${1:-}" = "--yes" ]; then
  ASSUME_YES=1
fi

if [ ! -d "$LATEX_TEMPLATE_DIR" ]; then
  echo "ERROR: missing template directory: $LATEX_TEMPLATE_DIR" >&2
  exit 1
fi

echo "This will delete all contents of paper/, code/, data/, test-results/, and ralph-garage/."
if [ "$ASSUME_YES" -ne 1 ]; then
  read -r -p "Are you sure? [y/N] " response
  if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
  fi
fi

# Author working directories (defined in spec/ralph-spec.md)
author_dirs=(paper code data)

echo "Emptying author working directories..."
for dir in "${author_dirs[@]}"; do
  target_dir="$REPO_ROOT/$dir"
  if [ -d "$target_dir" ]; then
    echo "  $dir"
    rm -rf "$target_dir"
  fi
  mkdir -p "$target_dir"
done

echo "Restoring LaTeX paper template from $LATEX_TEMPLATE_DIR..."
while IFS= read -r -d '' src_file; do
  rel="${src_file#"$LATEX_TEMPLATE_DIR"/}"
  dst_file="$REPO_ROOT/paper/$rel"
  mkdir -p "$(dirname "$dst_file")"
  cp -f "$src_file" "$dst_file"
done < <(find "$LATEX_TEMPLATE_DIR" -type f -print0)

echo "Emptying: test-results"
rm -rf "$REPO_ROOT/test-results"
mkdir -p "$REPO_ROOT/test-results"

echo "Removing: ralph-garage"
rm -rf "$REPO_ROOT/ralph-garage"

echo "Done."

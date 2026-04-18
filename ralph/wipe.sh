#!/usr/bin/env bash
# How to run: bash ralph/wipe.sh
# Inputs: none
# Outputs: empties author working directories, empties test-results/, removes ralph-garage/
#
# Manual cleanup helper. Does not restore the checked-in paper/code baseline.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSUME_YES=0

if [ "${1:-}" = "--yes" ]; then
  ASSUME_YES=1
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

echo "Emptying: test-results"
rm -rf "$REPO_ROOT/test-results"
mkdir -p "$REPO_ROOT/test-results"

echo "Removing: ralph-garage"
rm -rf "$REPO_ROOT/ralph-garage"

echo "Done."
echo "paper/ and code/ are now empty directories. Restore or replace them before starting Ralph from main."

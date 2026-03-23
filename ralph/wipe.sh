#!/usr/bin/env bash
# How to run: bash ralph/wipe.sh
# Inputs: none
# Outputs: empties author working directories, empties test-results/, removes ralph-garage/
#
# Gives Ralph a blank slate before starting a new run.

set -euo pipefail

echo "This will delete all contents of paper/, code/, data/, test-results/, and ralph-garage/."
read -r -p "Are you sure? [y/N] " response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
  echo "Aborted."
  exit 0
fi

# Author working directories (defined in spec/ralph-spec.md)
author_dirs=(paper code data)

echo "Emptying author working directories..."
for dir in "${author_dirs[@]}"; do
  if [ -d "$dir" ]; then
    echo "  $dir"
    rm -rf "$dir"
  fi
  mkdir -p "$dir"
done

echo "Emptying: test-results"
rm -rf test-results
mkdir -p test-results

echo "Removing: ralph-garage"
rm -rf ralph-garage

echo "Done."

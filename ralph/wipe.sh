#!/usr/bin/env bash
# How to run: bash ralph/wipe.sh
# Inputs: none
# Outputs: resets author working directories and removes ralph-garage/
#
# "Reset" restores author working directories to their git state
# (or deletes them if uncommitted), clears test-results/, and wipes ralph-garage/.

set -euo pipefail

# Author working directories (defined in spec/ralph-spec.md)
author_dirs=(paper code data)

echo "Resetting author working directories..."
for dir in "${author_dirs[@]}"; do
  if [ ! -d "$dir" ]; then
    continue
  fi
  # Check if the directory has any tracked files
  if git ls-files --error-unmatch "$dir" &>/dev/null; then
    echo "  Restoring: $dir (git checkout)"
    git checkout HEAD -- "$dir"
    # Remove any untracked files within the directory
    # -x to also remove ignored build artifacts (pdf, aux, etc.)
    git clean -fdx "$dir"
  else
    echo "  Removing: $dir (not in git)"
    rm -rf "$dir"
  fi
done

echo "Clearing: test-results"
git checkout HEAD -- test-results
git clean -fdx test-results

echo "Removing: ralph-garage"
rm -rf ralph-garage

echo "Done."

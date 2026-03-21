#!/usr/bin/env bash
# How to run: bash ralph/wipe.sh
# Inputs: none
# Outputs: removes ./ralph-garage recursively

set -euo pipefail

echo "Wiping generated directories..."
echo "Removing: ralph-garage"
rm -rf ralph-garage
echo "Done."

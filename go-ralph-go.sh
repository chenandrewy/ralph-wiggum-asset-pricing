#!/usr/bin/env bash
# How to run: bash go-ralph-go.sh
# Inputs: config-ralph.yaml
# Outputs: runs the ralph loop (see ralph/ralph-loop.sh)

exec bash "$(dirname "$0")/ralph/ralph-loop.sh" "$@"

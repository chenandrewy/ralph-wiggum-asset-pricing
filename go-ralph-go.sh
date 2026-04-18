#!/usr/bin/env bash
# How to run: bash go-ralph-go.sh
# Inputs: config-ralph.yaml
# Outputs: runs the ralph loop (see ralph/ralph-loop.sh)

probe_agent() {
    local label="$1"
    local cmd="$2"
    shift 2
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "  $label: CLI not found ($cmd not on PATH)"
        return
    fi
    if timeout 30 "$@" >/dev/null 2>&1; then
        echo "  $label: authorized"
    else
        echo "  $label: NOT authorized (auth probe failed)"
    fi
}

echo "--- agent auth check (informational; loop will continue regardless) ---"
probe_agent "Claude" claude claude -p "ok"
probe_agent "Codex"  codex  codex exec "ok"
echo

exec bash "$(dirname "$0")/ralph/ralph-loop.sh" "$@"

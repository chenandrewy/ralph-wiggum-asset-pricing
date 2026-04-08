#!/usr/bin/env bash
# How to run: bash wait-then-go-ralph.sh [-h HOURS]
# Inputs: optional delay in hours via -h/--hours; otherwise prompts the user
# Outputs: waits for the requested delay, then runs go-ralph-go.sh

set -euo pipefail

hours=""

usage() {
  echo "Usage: bash wait-then-go-ralph.sh [-h HOURS]"
}

is_positive_number() {
  [[ "$1" =~ ^([0-9]+([.][0-9]+)?|[.][0-9]+)$ ]] && [[ "$1" != "0" ]] && [[ "$1" != "0.0" ]]
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--hours)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1." >&2
        usage >&2
        exit 1
      fi
      hours="$2"
      shift 2
      ;;
    --help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$hours" ]]; then
  read -r -p "How many hours should I wait before running Ralph? " hours
fi

if ! is_positive_number "$hours"; then
  echo "Hours must be a positive number." >&2
  exit 1
fi

seconds="$(awk "BEGIN { printf \"%d\", $hours * 3600 }")"
sleep "$seconds"
exec bash "$(dirname "$0")/go-ralph-go.sh"

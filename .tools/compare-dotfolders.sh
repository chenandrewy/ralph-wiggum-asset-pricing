#!/usr/bin/env bash
# Run: ./compare-dotfolders.sh TARGET_ROOT [TEMPLATE_ROOT]
# Inputs: target repo root, optional template root
# Output: launches an interactive Codex session that suggests a target update plan
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: compare-dotfolders.sh TARGET_ROOT [TEMPLATE_ROOT]

Launch interactive Codex from the target repo to compare the full standard
dotfolder set against the MacUser template set and suggest a target-side
update plan based on the template contents.

Examples:
  ./compare-dotfolders.sh ../risk-vs-writing
  ./compare-dotfolders.sh ../risk-vs-writing ~/Dropbox/MacUser/dotfolder-templates
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage >&2
  exit 1
fi

target_root="${1%/}"
template_root="${2:-$HOME/Dropbox/MacUser/dotfolder-templates}"
template_root="${template_root%/}"

if [[ ! -d "$target_root" ]]; then
  echo "Target root not found: $target_root" >&2
  exit 1
fi

if [[ ! -d "$template_root" ]]; then
  echo "Template root not found: $template_root" >&2
  exit 1
fi

target_root="$(cd "$target_root" && pwd)"
template_root="$(cd "$template_root" && pwd)"
template_parent_root="$(cd "$template_root/.." && pwd)"
template_readme="$template_parent_root/README.md"

prompt='Compare the full standard dotfolder set against the template set at:
'"${template_root}"'

Also read this README for context:
'"${template_readme}"'

Cover these dotfolders as one set:
- .agent-guidelines/
- .agents/
- .claude/
- .credentials/
- .devcontainer/
- .tools/

- Do not edit any files.
- List the important differences between the template set and the target repo.
- Recommend concrete target-side changes based on those differences.
- Include file-level references for the highest-value changes.
- Do not inspect or report on .git/.
- Ignore obvious noise such as .DS_Store, __pycache__/, *.pyc, build.log, and build-fix.log.
'

exec codex -m gpt-5.4 --sandbox workspace-write --cd "$target_root" "$prompt"

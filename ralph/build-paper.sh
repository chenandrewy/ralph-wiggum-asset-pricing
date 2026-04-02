#!/usr/bin/env bash
# How to run: bash ralph/build-paper.sh
# Inputs: paper/paper.tex, paper/references.bib, data/*
# Outputs: paper/paper.pdf (and LaTeX aux files)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAPER_DIR="$REPO_ROOT/paper"
BUILD_LOG="$PAPER_DIR/.latex-build.log"

compile_tex() {
    local tex_file="$1"
    local base_name="$2"
    local needs_biber="$3"

    if [ ! -f "$PAPER_DIR/$tex_file" ]; then
        echo "ERROR: missing $PAPER_DIR/$tex_file" >&2
        exit 1
    fi

    (
        cd "$PAPER_DIR"
        run_quiet "pdflatex pass 1 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        if [ "$needs_biber" = "yes" ]; then
            run_quiet "biber ($base_name)" biber --output-safechars "$base_name"
        fi
        run_quiet "pdflatex pass 2 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        run_quiet "pdflatex pass 3 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
    )
}

run_quiet() {
    local label="$1"
    shift

    if ! "$@" >>"$BUILD_LOG" 2>&1; then
        echo "ERROR: $label failed. See $BUILD_LOG" >&2
        tail -n 40 "$BUILD_LOG" >&2
        exit 1
    fi
}

: > "$BUILD_LOG"

compile_tex "paper.tex" "paper" "yes"

echo "[build-paper] built paper/paper.pdf"

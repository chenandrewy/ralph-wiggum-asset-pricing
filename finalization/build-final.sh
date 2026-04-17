#!/usr/bin/env bash
# How to run: bash finalization/build-final.sh
# Inputs: paper/paper.tex, paper/references.bib, paper/exhibits/*, finalization/inputs/*
# Outputs: finalization/output-anon/paper.tex, finalization/output-anon/paper.pdf,
#     finalization/output-named/paper.tex, finalization/output-named/paper.pdf
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FINAL_DIR="$REPO_ROOT/finalization"
OUTPUT_ANON_DIR="$FINAL_DIR/output-anon"
OUTPUT_NAMED_DIR="$FINAL_DIR/output-named"
BUILD_LOG="$FINAL_DIR/.latex-build.log"

python3 "$FINAL_DIR/build-final.py"

run_quiet() {
    local label="$1"
    shift

    if ! "$@" >>"$BUILD_LOG" 2>&1; then
        echo "ERROR: $label failed. See $BUILD_LOG" >&2
        tail -n 40 "$BUILD_LOG" >&2
        exit 1
    fi
}

compile_tex() {
    local output_dir="$1"
    local label="$2"

    (
        cd "$output_dir"
        run_quiet "pdflatex pass 1 ($label)" pdflatex -interaction=nonstopmode -halt-on-error paper.tex
        run_quiet "biber ($label)" biber --output-safechars paper
        run_quiet "pdflatex pass 2 ($label)" pdflatex -interaction=nonstopmode -halt-on-error paper.tex
        run_quiet "pdflatex pass 3 ($label)" pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    )
}

: > "$BUILD_LOG"

compile_tex "$OUTPUT_ANON_DIR" "anonymous"
compile_tex "$OUTPUT_NAMED_DIR" "named"

echo "[build-final] built finalization/output-anon/paper.pdf"
echo "[build-final] built finalization/output-named/paper.pdf"

#!/usr/bin/env bash
# How to run: bash finalization/build-final.sh
# Inputs: paper/paper.tex, paper/references.bib, paper/exhibits/*, finalization/inputs/*
# Outputs: finalization/output/paper-anonymous.pdf, finalization/output/paper-named.pdf
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FINAL_DIR="$REPO_ROOT/finalization"
OUTPUT_DIR="$FINAL_DIR/output"
BUILD_LOG="$OUTPUT_DIR/.latex-build.log"

mkdir -p "$OUTPUT_DIR"
python3 "$FINAL_DIR/scripts/build-final-materials.py"

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
    local tex_file="$1"
    local base_name="$2"

    (
        cd "$OUTPUT_DIR"
        run_quiet "pdflatex pass 1 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        run_quiet "biber ($base_name)" biber --output-safechars "$base_name"
        run_quiet "pdflatex pass 2 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
        run_quiet "pdflatex pass 3 ($tex_file)" pdflatex -interaction=nonstopmode -halt-on-error "$tex_file"
    )
}

: > "$BUILD_LOG"

compile_tex "paper-anonymous.tex" "paper-anonymous"
compile_tex "paper-named.tex" "paper-named"

echo "[build-final] built finalization/output/paper-anonymous.pdf"
echo "[build-final] built finalization/output/paper-named.pdf"

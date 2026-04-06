# Finalization Pipeline

This folder builds final, post-Ralph paper variants without modifying `paper/`.

## Purpose

The Ralph loop should continue to target only the canonical anonymous manuscript in
`paper/paper.tex`. This folder adds a separate finalization step that can:

- inject a human-written preface
- generate a transparency appendix from selected spec sections and test/referee prompts
- build two final PDF variants:
  - anonymous
  - named

All generated artifacts live in `finalization/output/`.

## Files

- `inputs/preface.md` — human-authored preface text
- `inputs/appendix-manifest.toml` — allowlist of spec sections and prompt files
- `inputs/author-info.toml` — author metadata for the named variant
- `build-final.sh` — generates derived TeX files in `output/` and compiles both PDFs

## How to run

Generate the derived TeX files and compile both PDFs:

```bash
bash finalization/build-final.sh
```

## Output

The build writes:

- `output/preface.tex`
- `output/final-appendix.tex`
- `output/paper-anonymous.tex`
- `output/paper-named.tex`
- `output/paper-anonymous.pdf`
- `output/paper-named.pdf`

## Notes

- The generator derives both final papers from `paper/paper.tex`.
- It rewrites bibliography and exhibit paths so the derived papers compile from
  `finalization/output/`.
- The appendix is manifest-driven on purpose. Do not auto-include all tests or
  all Ralph prompts.

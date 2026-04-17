# Finalization Pipeline

This folder builds final, post-Ralph paper variants without modifying `paper/`.

## Purpose

The Ralph loop should continue to target only the canonical anonymous manuscript in
`paper/paper.tex`. This folder adds a separate finalization step that can:

- inject a human-written preface
- inject acknowledgments as a `\thanks` footnote on the named variant's title
- inject an additional human-written LaTeX appendix
- build two self-contained final PDF/source bundles:
  - `output-anon/`
  - `output-named/`

Generated final paper bundles live in `finalization/output-anon/` and
`finalization/output-named/`.

## Files

- `inputs/preface.md` — human-authored preface text
- `inputs/acknowledgments.md` — acknowledgments; injected as `\thanks` on the
  title of the named variant only (anonymous variant is left clean)
- `inputs/additional-appendix.tex` — raw LaTeX appendix material inserted before
  the bibliography
- `inputs/author-info.toml` — author metadata for the named variant
- `build-final.sh` — generates self-contained output bundles and compiles both PDFs

## How to run

Generate the derived TeX files and compile both PDFs:

```bash
bash finalization/build-final.sh
```

## Output

The build writes:

- `output-anon/paper.tex`
- `output-anon/paper.pdf`
- `output-anon/references.bib`
- `output-anon/exhibits/*`
- `output-named/paper.tex`
- `output-named/paper.pdf`
- `output-named/references.bib`
- `output-named/exhibits/*`

## Notes

- The generator derives both final papers from `paper/paper.tex`.
- It copies bibliography and exhibit dependencies into each output bundle so the
  derived papers compile from inside that folder.
- The additional appendix is inlined into each generated `paper.tex` so each
  output bundle is self-contained.

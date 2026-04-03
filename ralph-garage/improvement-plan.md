# Improvement Plan
AUTHOR PLAN — 2026-04-02 21:47:58 EDT

## Status

Paper compiles (13 pages). No overhaul needed — the model section is structurally sound. Three tests failing; all fixable with targeted edits.

## Failing Tests

### 1. factcheck-theory — Notational ambiguities

Two medium issues causing the failure:

**Issue A: V subscript convention.** Throughout the paper, subscripts denote time ($Y_t$, $c_t$). But $V_0^A$ and $V_1$ use subscripts for regimes (pre/post-singularity). The convention is never stated.

- **Fix:** Add an explicit statement when $V_0^A$ is first introduced in Proposition 1, e.g., "where subscripts 0 and 1 on $V$ denote pre- and post-singularity regimes."

**Issue B: A(p) collides with superscript A.** In the Appendix proof of Proposition 3, $V_0^A = A(p)/B(p)$ uses $A$ as both a function name and the AI-stock superscript in the same expression.

- **Fix:** Rename the proof auxiliaries to non-colliding symbols, e.g., $\mathcal{N}(p)/\mathcal{D}(p)$ or $f(p)/h(p)$.

**Minor issues to also fix:**
- Remove orphaned $\Delta_0$ in Section 4.2 (used once, identical to $\Delta$, never appears in equations).

### 2. quality-writing — Inaccurate self-demonstration description

The self-demonstration paragraph says "the paper specification and testing framework---approximately 80 lines." This implies 80 lines covers both spec and tests. The accurate description: the human wrote the spec (~80 lines) and the tests separately.

- **Fix:** Rewrite to: "The human author contributed only the paper specification---approximately 80 lines---and the test suite. The AI performed all economic modeling, derivations, writing, and typesetting."

### 3. spec-paper — Exhibit numbering comments inconsistent

In `paper.tex`: figure = Exhibit 1, table = Exhibit 2. But `paper/exhibits/numerical-illustration.tex` labels itself Exhibit 1, and `code/run-all.R` reverses the ordering.

- **Fix:** Align all exhibit number comments across `paper/exhibits/numerical-illustration.tex` and `code/run-all.R` to match `paper.tex` (figure = Exhibit 1, table = Exhibit 2).

## Execution Order

1. Fix notational ambiguities in `paper/paper.tex` (factcheck-theory).
2. Fix self-demonstration paragraph in `paper/paper.tex` (quality-writing).
3. Fix exhibit numbering comments in `paper/exhibits/numerical-illustration.tex` and `code/run-all.R` (spec-paper).
4. Rebuild paper and rerun tests.

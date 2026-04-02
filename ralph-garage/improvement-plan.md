# Improvement Plan
AUTHOR PLAN — 2026-04-02 18:44:28 EDT

## Current State

**Tests: 14/16 passing.** Two failures: `quality-formalism` and `spec-paper`. No build issues. No referee outputs (referees disabled).

## Failing Tests

### 1. `spec-paper` — Exhibit numbering and `\notag` violations

Two issues:

**a. Exhibit comments mislabeled.** The table (`numerical-illustration.tex`) is labeled `% Exhibit 1` but should be `% Exhibit 2` (the figure is Exhibit 1). Also, the `\input` line for the table in `paper.tex` (line 235) lacks an exhibit comment.

- **Fix in `paper/exhibits/numerical-illustration.tex`**: Change `% Exhibit 1` → `% Exhibit 2`.
- **Fix in `paper/paper.tex` line 235**: Add `% Exhibit 2` comment after the `\input` line.

**b. Unnumbered display equations in appendix.** The proof of Proposition 3 (Appendix A) uses `\notag` on two intermediate lines of the multi-line derivation, violating Style Req 9 (all display equations numbered). 

- **Fix in `paper/paper.tex` appendix proof**: Remove both `\notag` tags so all display lines are numbered.

### 2. `quality-formalism` — Compressible equation in Section 4.2

Equation (15), `Δ(λ) = 1 - (1 - Δ₀)(1 - λ)`, is never used beyond its endpoints (λ=0 and λ=1). The paper's Coasean argument only needs: no transfers → Δ₀, full transfers → Δ=1. The displayed equation is ceremonial formalism that doesn't advance the argument.

- **Fix**: Remove the displayed equation for Δ(λ). Instead, state inline that transfers interpolate between Δ₀ (no risk-sharing) and 1 (full risk-sharing), then move directly to the Coase theorem discussion. This tightens the prose and satisfies the "no ceremonial formalism" requirement.

## Additional Observations (from passing tests, low priority)

- `factcheck-theory` flagged five low-severity notational issues (e.g., Δ used as both constant and function, R convention clash). These are cosmetic and do not block any tests, but could be cleaned up in a future pass.
- `factcheck-bysection` noted minor wording imprecision on line 252 ("shrinking fraction"). Non-blocking.

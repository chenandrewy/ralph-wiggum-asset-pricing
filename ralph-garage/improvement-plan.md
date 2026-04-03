# Improvement Plan
AUTHOR PLAN — 2026-04-02 22:09:53 EDT

## Status

- **Build**: Clean (13 pages, no errors)
- **Tests**: 13/16 pass; 3 failures below
- **Overhaul needed**: No. Model section is well-structured and correct.

## Failing Tests

### 1. `spec-paper` — Exhibit comment mismatch in generated table file

**Problem**: `code/numerical-illustration.R` line 68 writes `\label{tab:numerical} % Exhibit 1`, but `paper.tex` line 238 marks the table as `% Exhibit 2` (the figure is Exhibit 1). The generated file's comment contradicts the paper's numbering.

**Fix**: In `code/numerical-illustration.R`, change `% Exhibit 1` to `% Exhibit 2` on line 68.

### 2. `factcheck-code` — CRSP split-adjustment inconsistency

**Problem**: The CRSP query in `code/ai-valuations-figure.R` computes total dividends as `mcap / prc * divamt`, which multiplies month-end `shrout` by ex-date per-share `divamt`. If a stock split occurs between the ex-date and month-end (e.g., NVDA's 10-for-1 in June 2024), post-split shares outstanding are multiplied by pre-split per-share dividends, overstating total dividends.

**Fix**: Use CRSP's split-adjusted fields to ensure consistency. Specifically, replace the current dividend aggregation with a query that uses `cfacpr` (cumulative factor to adjust price) and `cfacshr` (cumulative factor to adjust shares) from `crsp.msf` to bring `divamt` and `shrout` to the same split-adjustment basis. Alternatively, compute total dividends as `divamt * shrout_on_exdate` by joining distributions with monthly data on the ex-date month rather than mixing timing. The simplest correct approach: multiply `divamt` by `shrout` from the same month as the ex-date (join `msf` to `msedist` on the ex-date's month-end, not the current observation month).

### 3. `quality-formalism` — Proposition 2 is compressible

**Problem**: Proposition 2 (the cross-section result $V_0^A > V_0^N$) follows in one step from Proposition 1 and Assumption 2. The displayed formula for the spread is never used downstream. The test flags it as ceremonial formalism that could be stated as a prose observation.

**Fix**: Demote Proposition 2 to a one- or two-sentence prose observation immediately after Proposition 1's proof. State that $V_0^A > V_0^N$ follows from $\tilde{\theta}/\theta > 1 > \tilde{\nu}/\nu$ and the shared denominator. Remove equation (12). Renumber Propositions 3→2 and 4→3, updating all references (including the appendix proof header). Update exhibit/theorem number comments throughout.

## Sequencing

1. Fix the exhibit comment (test 1) — trivial, one-line change.
2. Fix the CRSP split-adjustment (test 2) — modify the SQL query in `ai-valuations-figure.R`.
3. Demote Proposition 2 to prose (test 3) — edit `paper.tex`, renumber propositions, update cross-references and comments.

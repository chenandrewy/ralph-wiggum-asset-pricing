# tests/factcheck-code.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 1m 53s
[ralph-garage/agent-logs/20260402T222807.265078-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T222807.265078-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: FAIL
REASON: The empirical figure (Exhibit 1) is commented out in paper.tex while the text still references it, creating a paper-code inconsistency.

## Canonical local analysis path

The canonical entry point is `code/run-all.R`, which runs two scripts in dependency order:

1. `code/numerical-illustration.R` — generates `paper/exhibits/numerical-illustration.tex` (Exhibit 2: numerical table) from hardcoded parameters. No external data needed.
2. `code/ai-valuations-figure.R` — generates `paper/exhibits/ai-valuations.pdf` (Exhibit 1: CRSP figure) via a live WRDS query. Requires `WRDS_USERNAME` and `WRDS_PASSWORD` environment variables.

The code is logically organized: two scripts, one per exhibit, with a single entry point. Each script has a header documenting how to run, inputs, and outputs.

## Execution status

- **Numerical table**: Ran from scratch successfully. Output matches the committed `paper/exhibits/numerical-illustration.tex` exactly.
- **CRSP figure**: Ran from scratch successfully (WRDS credentials available in this environment). Generated `paper/exhibits/ai-valuations.pdf`.
- **Full pipeline**: `Rscript code/run-all.R` completed without error.
- **Execution model**: The pipeline runs from scratch as required by the spec (III.3.c). No precomputed caches or manually prepared intermediate files are used. The WRDS query is part of the canonical path as required by the spec (III.3.e).

## Paper-code consistency

### Verified claims (all match)

| Paper claim | Code/computed value | Status |
|---|---|---|
| Parameters: β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30 | Hardcoded identically in `numerical-illustration.R` | Match |
| ω=0.60, ω̃=0.45, Δ=0.75 | omega=0.6, omega_tilde=0.45, delta=0.75 | Match |
| V_pre^A ≈ 16.1 at p=0.01 | 16.098 | Match |
| V_pre^N ≈ 11.6 at p=0.01 | 11.567 | Match |
| Ratio of roughly 1.4 | 1.392 | Match |
| Both ≈ 11.9 at p=0 | 11.940 | Match |
| V_pre^{A,CM} ≈ 12.9 | 12.896 | Match |
| Hedging premium about 25% | 24.8% | Match |
| Existence conditions (Assumption 3) satisfied | (1-p)β(1+g)^(1-γ)=0.913 < 1; β(1+g̃)^(1-γ)=0.871 < 1 | Satisfied |

The code implements equations (9)–(14) from Proposition 1 exactly as stated. The complete-markets variant correctly sets Δ^{-γ}=1 in Φ^A. All formulas are algebraically consistent with the paper.

### Split-adjustment handling (Requirement 5)

The CRSP figure code computes dollar dividends from returns: `(ret - retx) * lagged_mcap`. This avoids per-share split-adjustment issues that would arise from combining `divamt` (from distribution files) with `shrout` (from monthly files) across different split-adjustment dates. The code includes an explicit comment documenting this choice and the specific concern (NVDA 10:1 split, June 2024). This satisfies Requirement 5.

### Violations found

1. **Figure commented out but still referenced (paper-code inconsistency).** The figure environment for Exhibit 1 (`ai-valuations.pdf`) is commented out in `paper.tex` (lines 45–50), but the introductory text at line 43 still references `Figure~\ref{fig:ai-valuations}`. The canonical pipeline generates the PDF, but the paper does not include it. This violates:
   - Spec III.1.d: "All files in `paper/exhibits/` are used in the paper" — `ai-valuations.pdf` is generated but not used.
   - Spec III.3.b: "code/ provides one canonical entry point that regenerates every exhibit used in paper.tex" — the entry point generates an exhibit that is not used, and the paper references a figure that does not render.
   - Requirement 4 (paper claims consistent with code): The paper text describes a CRSP figure that does not appear in the compiled document.

2. **Pipeline fails without WRDS credentials despite the comment.** `run-all.R` line 4 says "If WRDS credentials are unavailable, the numerical table is still generated," but the code does not implement graceful degradation — `ai-valuations-figure.R` calls `stop()` on missing credentials, and `run-all.R` propagates the failure via `stop()`. The pipeline halts entirely. This is a minor documentation-code mismatch within `run-all.R` itself (the comment is misleading about fault tolerance).

## Reproducibility classification

| Output | Classification |
|---|---|
| Numerical table (Exhibit 2) | **Locally reproducible** — runs from scratch with no external dependencies |
| CRSP figure (Exhibit 1) | **Blocked by credentials** — requires WRDS access; code logic is sound but figure is commented out in paper |
| Paper text numerical claims (Section 3) | **Locally reproducible** — all verified against code output |
| Theoretical propositions and proofs | Not code-dependent — pure algebra, outside scope of this test |

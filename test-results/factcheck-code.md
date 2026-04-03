# tests/factcheck-code.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 2m 5s
[ralph-garage/agent-logs/20260402T225431.398555-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T225431.398555-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical pipeline runs from scratch, produces both exhibits, and all numerical claims in the paper match the code output.

## Canonical local analysis path

- **Entry point:** `Rscript code/run-all.R` (documented in its header comment).
- **Scripts in dependency order:**
  1. `code/numerical-illustration.R` → `paper/exhibits/numerical-illustration.tex` (Exhibit 2)
  2. `code/ai-valuations-figure.R` → `paper/exhibits/ai-valuations.pdf` (Exhibit 1)
- **External dependency:** WRDS credentials (`WRDS_USERNAME`, `WRDS_PASSWORD`) required for the CRSP figure. The numerical table has no external dependencies.
- The pipeline is coherent: `run-all.R` calls both scripts, outputs go directly to `paper/exhibits/`, and both exhibits are referenced in `paper.tex`.

## Execution status

- **Full pipeline:** Executed successfully from scratch via `Rscript code/run-all.R`. Runtime was well under 180 seconds.
- **Exhibit 1 (ai-valuations.pdf):** Generated from a live WRDS/CRSP query. Requires `DBI` and `RPostgres` R packages (both available). Requires WRDS credentials (available in this environment).
- **Exhibit 2 (numerical-illustration.tex):** Generated from hardcoded parameters with no external dependencies.
- **No precomputed caches or manually prepared intermediate files** were required. The pipeline is fully from-scratch as required by the spec (III.3.c).

## Paper-code consistency

All checked items are consistent:

| Paper claim | Code value | Match |
|---|---|---|
| Parameters: β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30 | Hardcoded identically in `numerical-illustration.R` | ✓ |
| ω=0.60, ω̃=0.45, Δ=0.75 | Computed as 0.60, 0.45, 0.75 | ✓ |
| V_pre^A ≈ 16.1 at p=0.01 | 16.1 | ✓ |
| V_pre^N ≈ 11.6 at p=0.01 | 11.6 | ✓ |
| Ratio ≈ 1.4 | 16.1/11.6 = 1.39 | ✓ |
| Both ≈ 11.9 at p=0 | 11.9, 11.9 | ✓ |
| V_pre^{A,CM} ≈ 12.9 | 12.9 | ✓ |
| Hedging premium ≈ 25% | 24.8% | ✓ |
| Figure uses CRSP data, trailing 12-month dividends | Confirmed in SQL query and rolling-window code | ✓ |
| Figure tickers: NVDA, MSFT, GOOGL, META, AMZN | Confirmed in SQL WHERE clause | ✓ |
| Formulas for R, Φ^A, Φ^N, V_post, V_pre^A, V_pre^N | Code implements equations (10)–(15) exactly | ✓ |

**Per-share data handling (Requirement 5):** The CRSP figure code explicitly avoids combining per-share dividend amounts with share counts by computing dollar dividends as `(ret - retx) * lagged_mcap`. This sidesteps split-adjustment mismatches (e.g., NVDA 10:1 split in June 2024), as documented in the code comments (lines 46–49 of `ai-valuations-figure.R`).

## Reproducibility classification

| Output | Classification |
|---|---|
| Exhibit 1 (ai-valuations.pdf) | **Locally reproducible** (with WRDS credentials, which are part of the canonical pipeline per spec III.3.e) |
| Exhibit 2 (numerical-illustration.tex) | **Locally reproducible** (no external dependencies) |
| All inline numerical claims in Section 3 | **Locally reproducible** (match code output exactly) |
| Theoretical propositions and proofs | Not code-dependent; verified for formula consistency with the code |

No violations of requirements found.

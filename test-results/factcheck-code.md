# tests/factcheck-code.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 1m 25s
[ralph-garage/agent-logs/20260402T221344.373129-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.373129-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces both exhibits, and all paper claims are consistent with the code.

## Canonical local analysis path

- **Entry point:** `code/run-all.R` (single canonical entry point per spec III.3.b).
- **Scripts:** `code/numerical-illustration.R` (Exhibit 2: numerical table) and `code/ai-valuations-figure.R` (Exhibit 1: CRSP figure).
- **Outputs:** `paper/exhibits/numerical-illustration.tex` and `paper/exhibits/ai-valuations.pdf`.
- **Dependencies:** R, `DBI`, `RPostgres` packages; WRDS credentials for Exhibit 1.
- The pipeline runs in dependency order (table first, then figure) and outputs directly to `paper/exhibits/`.

## Execution status

- **Full pipeline:** Executed successfully via `Rscript code/run-all.R`. Both exhibits regenerated from scratch.
- **Numerical table (Exhibit 2):** Runs with no external dependencies. Produces correct output.
- **CRSP figure (Exhibit 1):** Requires WRDS credentials (environment variables `WRDS_USERNAME`, `WRDS_PASSWORD`). Successfully connected and retrieved 168 rows. Figure generated. The WRDS query is part of the canonical pipeline as required by spec III.3.e.
- **Runtime:** Well within the 180-second budget (spec III.3.d).

## Paper-code consistency

| Paper claim | Code verification | Status |
|---|---|---|
| Parameters: β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30 | `numerical-illustration.R` lines 8-16 | Match |
| ω=0.60, ω̃=0.45, Δ=0.75 | Computed correctly from parameters | Match |
| V_0^A ≈ 16.1 at p=0.01 | Code output: 16.1 | Match |
| V_0^N ≈ 11.6 at p=0.01 | Code output: 11.6 | Match |
| Ratio of roughly 1.4 | 16.1/11.6 ≈ 1.39 | Match |
| Both ≈ 11.9 at p=0 | Table row: 11.9 | Match |
| V_0^{A,CM} ≈ 12.9 | Code output: 12.9 | Match |
| Hedging premium about 25% | Code output: 24.8% | Match |
| Figure caption: AI tickers NVDA, MSFT, GOOGL, META, AMZN | SQL query WHERE clause | Match |
| Figure caption: trailing 12-month dividends | Rolling 12-month window in code | Match |
| Figure caption: CRSP data | Queries crsp.msf | Match |
| Formulas in Proposition 1 (V_0^A, V_0^N, Φ^A, Φ^N, V_1) | Implemented identically in code lines 23-30 | Match |
| Complete-markets formula (Φ^{A,CM} without Δ^{-γ}) | Code line 33: no delta term | Match |

## Reproducibility classification

| Output | Classification |
|---|---|
| Exhibit 2 (numerical table) | **Locally reproducible** — no external dependencies, deterministic |
| Exhibit 1 (CRSP figure) | **Locally reproducible with WRDS credentials** — requires network access and WRDS account, which is part of the canonical pipeline per spec |

## Per-share data handling (Requirement 5)

The CRSP figure code computes dollar dividends as `(ret - retx) * lagged_mcap` rather than combining per-share `divamt` with `shrout` from different tables. This avoids split-adjustment mismatches (the code explicitly documents this at lines 47-49, citing the NVDA 10:1 split as motivation). The `ret` and `retx` fields in CRSP are internally consistent, so the difference correctly captures the dividend yield without split-adjustment concerns. This approach is sound.

## Additional checks

- No hidden or unnecessary auxiliary files: `data/` is empty, no precomputed caches used.
- All files in `paper/exhibits/` are referenced by the paper (no orphan exhibits).
- Code structure is logically organized: one entry point, two scripts, clear header comments with run instructions, inputs, and outputs.
- The pipeline does not silently rely on cached objects or manually prepared files (spec III.3.c, III.3.g).

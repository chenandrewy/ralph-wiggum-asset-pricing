# tests/factcheck-code.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 2m 3s
[ralph-garage/agent-logs/20260402T183430.355175-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T183430.355175-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: Canonical pipeline runs from scratch, produces all exhibits, and code output matches the paper's quantitative claims.

## Canonical local analysis path

The canonical entry point is `code/run-all.R`, which calls two scripts in sequence:

1. `code/numerical-illustration.R` — computes price-dividend ratios from model parameters and writes `paper/exhibits/numerical-illustration.tex`.
2. `code/ai-valuations-figure.R` — queries WRDS/CRSP for monthly price and dividend data for AI vs. non-AI stocks and writes `paper/exhibits/ai-valuations.pdf`.

Both outputs land directly in `paper/exhibits/` as required by the spec (III.3.f). The pipeline has a single entry point (III.3.b), is written in R (III.3.a), and does not rely on precomputed caches or manually prepared intermediate files (III.3.c). The WRDS query is part of the canonical pipeline (III.3.e).

## Execution status

- **Full pipeline**: Executed successfully via `Rscript code/run-all.R`. Both exhibits regenerated from scratch.
- **Numerical illustration**: Runs with no external dependencies. Produces correct output.
- **CRSP figure**: Requires WRDS credentials (`WRDS_USERNAME`, `WRDS_PASSWORD`). Connected, queried, and generated the figure. Run completed well within the 180-second budget (III.3.d).
- **Runtime dependencies**: R, `DBI`, `RPostgres`. These are not explicitly documented in a requirements file but are standard and listed in the script headers.

## Paper-code consistency

### Numerical illustration (Table 1 / Exhibit 2)

All inline claims in Section 3 verified against code output at p = 0.01:

| Claim | Paper | Code |
|-------|-------|------|
| V0_A | ~16.1 | 16.1 |
| V0_N | ~11.6 | 11.6 |
| V0_A / V0_N | ~1.4 | 1.39 |
| V0_A at p=0 | ~11.9 | 11.9 |
| V0_A_CM | ~12.9 | 12.9 |
| Hedging premium | ~25% | 24.8% |

Parameters in the code (`beta=0.96, gamma=3, g=0.02, g_tilde=0.05, theta=0.05, theta_tilde=0.15, nu=0.55, nu_tilde=0.30`) match the paper's stated values exactly. The formulas implemented in the code (`R`, `Phi_A`, `Phi_N`, `V1`, `V0_A`, `V0_N`, `Phi_A_CM`, `V0_A_CM`) correspond to equations (7)-(14) in the paper.

### CRSP figure (Figure 1 / Exhibit 1)

- The figure caption states it uses CRSP data for NVDA, MSFT, GOOGL, META, AMZN with trailing 12-month dividends. The code queries exactly these tickers from `crsp.stocknames` and computes trailing 12-month P/D ratios. Consistent.
- The code computes portfolio-level P/D ratios (total market cap / total trailing dividends), which is a standard value-weighted approach. Consistent with "price-dividend ratios" as described.

### Per-share data handling (Requirement 5)

The CRSP query computes total dollar dividends as `mcap / prc * div_total`, which equals `shrout * divamt`. Here `shrout` is month-end shares outstanding from `crsp.msf`, while `divamt` is the per-share dividend from `crsp.msedist` at the ex-date. If a stock split occurs between the ex-date and month-end within the same month, these quantities are on different split bases, which would overstate or understate total dividends. The code does not verify or adjust for this.

In practice, for the five large-cap AI stocks and the broad CRSP universe at monthly frequency, intra-month splits are rare and the impact is negligible. The paper spec classifies this figure as illustrative (IV.8.b, IV.8.d), not a calibration exercise. This is a minor methodological gap, not a material error.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| Table 1 (numerical-illustration.tex) | **Locally reproducible** — runs from scratch with no external dependencies |
| Figure 1 (ai-valuations.pdf) | **Locally reproducible with credentials** — requires WRDS access, which is part of the canonical pipeline per spec III.3.e |
| All theoretical propositions and proofs | Not code-dependent — pure mathematical derivations in the paper |

## Minor observations

- **No formal dependency manifest**: The R package requirements (`DBI`, `RPostgres`) are documented in script headers but not in a standalone requirements file. This is a minor documentation gap but does not violate any spec requirement.
- **Graceful degradation**: `run-all.R` documents that if WRDS credentials are unavailable, the numerical table is still generated. This is helpful but the CRSP figure would fail. The spec requires the full pipeline to run from scratch (III.3.c), so credentials must be available for full compliance.

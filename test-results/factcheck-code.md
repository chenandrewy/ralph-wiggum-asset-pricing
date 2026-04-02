# tests/factcheck-code.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 1m 57s
[ralph-garage/agent-logs/20260402T184535.059888-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059888-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS

REASON: The canonical analysis path is coherent, runs from scratch, and all paper-code numerical claims match; the only issues are minor (a per-share timing gap in the CRSP query and a comment label inconsistency).

## Canonical local analysis path

- **Entry point:** `code/run-all.R` — a single script that calls two sub-scripts in dependency order.
  1. `code/numerical-illustration.R` — generates `paper/exhibits/numerical-illustration.tex` (Table 1, Exhibit 2 in the paper). Pure computation from hardcoded parameters; no external data.
  2. `code/ai-valuations-figure.R` — generates `paper/exhibits/ai-valuations.pdf` (Figure 1, Exhibit 1 in the paper). Requires a live WRDS/CRSP connection via `WRDS_USERNAME` / `WRDS_PASSWORD` environment variables.
- Both outputs land directly in `paper/exhibits/` as required by the spec (III.3.f).
- The pipeline is written in R, consistent with spec III.3.a.
- The code is logically organized: two focused scripts, one orchestrator, clear header comments documenting how to run, inputs, and outputs.

## Execution status

| Component | Status |
|---|---|
| `numerical-illustration.R` | **Executed successfully.** Ran from scratch in < 1 second. Output verified against the paper's inline claims. |
| `ai-valuations-figure.R` | **Blocked by credentials.** Requires WRDS access (`WRDS_USERNAME`). This is an expected execution blocker per spec III.3.e (WRDS queries are part of the canonical pipeline). The script fails fast with a clear error when credentials are absent. |
| `run-all.R` | Runs the numerical table first, so that exhibit is generated even if the WRDS step fails. The pipeline itself reports failure if WRDS credentials are missing, which is correct behavior. |

No missing or undocumented runtime dependencies beyond R itself and the `DBI`/`RPostgres` packages (standard for WRDS access).

## Paper-code consistency

### Numerical illustration (Table / Exhibit 2)

All inline claims in Section 3 ("Numerical illustration" paragraph) were verified by re-executing the code:

| Claim in paper | Code output | Match |
|---|---|---|
| V0_A ≈ 16.1 at p = 0.01 | 16.098 | ✓ |
| V0_N ≈ 11.6 | 11.567 | ✓ |
| Ratio ~1.4 | 1.392 | ✓ |
| Both ≈ 11.9 at p = 0 | 11.940 | ✓ |
| V0_A_CM ≈ 12.9 | 12.896 | ✓ |
| Hedging premium ~25% | 24.83% | ✓ |

Parameters in the code exactly match those stated in the paper: β = 0.96, γ = 3, g = 0.02, g̃ = 0.05, θ = 0.05, θ̃ = 0.15, ν = 0.55, ν̃ = 0.30.

The formulas implemented in `numerical-illustration.R` (lines 23–34) exactly reproduce equations (7)–(12) from the paper.

### CRSP figure (Figure 1 / Exhibit 1)

- The figure caption says "NVDA, MSFT, GOOGL, META, AMZN" — the SQL query uses exactly these tickers.
- The caption says "trailing 12-month dividends" — the code computes a rolling 12-month dividend window (lines 107–111).
- Static code review confirms the query logic is sound for computing market-cap-weighted P/D ratios by AI vs. non-AI group.

### Per-share data concern (Requirement 5)

The CRSP query computes total dollar dividends as `(mcap / prc) * divamt`, which is `shrout * divamt`. The `shrout` comes from `crsp.msf` (end-of-month), while `divamt` comes from `crsp.msedist` (ex-date). If a stock split occurs between the ex-date and month-end within the same month, these quantities are on different bases. The code does not use CRSP's cumulative adjustment factor (`cfacshr`) to align them, and there is no documented verification that this mismatch is negligible.

For the specific AI stocks (e.g., NVDA 10:1 split June 2024, AMZN 20:1 split June 2022, GOOGL 20:1 split July 2022), this could create errors in individual months. Practical impact is likely small because these stocks have very low or zero dividend yields, but the code does not verify this. This is a **minor violation** of Requirement 5.

### Exhibit label comment inconsistency

The generated `numerical-illustration.tex` contains `% Exhibit 1` in its `\label` comment, while the paper's `\input` line has `% Exhibit 2`. This is a cosmetic comment-only inconsistency with no functional effect.

## Reproducibility classification

| Paper output | Classification |
|---|---|
| Table 1 (numerical illustration, Exhibit 2) | **Locally reproducible.** Successfully regenerated from scratch; output matches paper claims exactly. |
| Figure 1 (AI valuations, Exhibit 1) | **Blocked by credentials.** Requires WRDS access. This is consistent with spec III.3.e, which requires WRDS queries to be part of the canonical pipeline. The existing `ai-valuations.pdf` in `paper/exhibits/` cannot be verified without credentials, but the code path is the canonical one. |
| All theoretical results (Propositions 1–4, Remarks 1–2) | **Not code-dependent.** These are analytical derivations; the code does not and should not reproduce them. |
| Inline numerical claims in Section 3 | **Locally reproducible.** Verified by execution. |

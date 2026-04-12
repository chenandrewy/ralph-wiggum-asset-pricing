# tests/factcheck-code.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 2m 21s
[ralph-garage/agent-logs/20260412T141819.030829-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.030829-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical local analysis path

The repo has a single canonical entry point: `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`. It produces three exhibits consumed by `paper/paper.tex`:

1. `paper/exhibits/table-pd-ratios.tex` — P/D ratio table (Exhibit 2 in paper)
2. `paper/exhibits/fig-extension-panels.pdf` — two-panel extension figure (Exhibit 3)
3. `paper/exhibits/fig-ai-valuations.pdf` — empirical valuation figure (Exhibit 1)

No other code files exist in `code/`. No intermediate files, caches, or manually prepared inputs are required. The data directory is empty; all data is downloaded at runtime from datahub.io (Shiller S&P 500) and FRED (NASDAQ index).

## Execution status

- **Status**: Ran successfully from scratch in this environment.
- **Runtime dependencies**: R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. All were available.
- **Network dependencies**: Downloads S&P 500 data from datahub.io and NASDAQ data from FRED. This is consistent with the spec (III.3.d: "executes in less than 180 seconds, including any external data download").
- **No precomputed caches or intermediate files** are used. Satisfies spec requirement III.3.c.

## Paper-code consistency

### Parameters
All parameters in the code match the paper's stated values:

| Parameter | Code | Paper (Section 3 / Table footnote) | Match |
|-----------|------|-------------------------------------|-------|
| β | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| γ | 4 | 4 | Yes |
| φ | 0.50 | 0.5 | Yes |
| η | 0.50 | 0.5 | Yes |
| θ | 0.15 | 0.15 | Yes |
| Δθ | 0.20 | 0.2 | Yes |

Extension parameters (Section 4.2): α=0.70, δ=0.50, p=0.5%, ξ=5%, large singularity η=9/φ=0.05. All match.

Veto parameters (Section 4.1): γ=10, p=1%, κ=1%, q=0.70, α=0.70, ξ=5%. All match.

### Numerical claims verified

- Paper: "AI stocks trade at a P/D of about 15.5" at p=0.5%, ξ=0%. Table output: 15.5. **Consistent.**
- Paper: "non-AI stocks trade near 11." Table output: 11.1. **Consistent.**
- Paper: "a ratio of about 1.4." Table output: 1.4. **Consistent.**
- Paper: "At p=1%, the ratio rises to 2." Table output: 2.0. **Consistent.**
- Paper: "consumption halves under the large singularity (φ(1+η) = 0.5)." Code: 0.05 × 10 = 0.5. **Consistent.**
- Paper: "falls by 25% under the baseline (φ(1+η) = 0.75)." Code: 0.5 × 1.5 = 0.75. **Consistent.**
- Paper: "net transfers per dollar taxed are only τ(1−δτ), e.g., 0.219 at τ=0.30" (with δ=0.9). Verified: 0.30 × 0.73 = 0.219. **Consistent.**
- Paper: "consumption multiple of 3.5× at τ=0.30" (with δ=0.9). Verified: 3.52. **Consistent** (rounded).
- Veto: "household vetoes under incomplete markets." Code output: V_veto > V_develop. **Consistent.**
- Veto: "does not veto under complete markets." Code output: V_develop_CM > V_veto. **Consistent.**

### Formula consistency

- The P/D closed-form approximation (Proposition 1) matches `compute_pd_approx`.
- The exact backward-recursion method described in the paper and appendix matches `compute_pd_ai_exact`.
- The transfer formula (eq. transfer-consumption) matches `consumption_growth` and `compute_pd_with_transfer` via φ_eff.
- The veto Bellman equations match `compute_v_develop_veto`, `compute_v_veto`, and `compute_v_develop_complete_veto`.

### Per-share data handling (Requirement 5)

Not applicable. The empirical figure uses index-level data (S&P 500 price index and trailing dividends from Shiller; NASDAQ composite index from FRED). No per-share quantities are combined with share counts from different sources.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| table-pd-ratios.tex | Locally reproducible (verified) |
| fig-extension-panels.pdf | Locally reproducible (verified) |
| fig-ai-valuations.pdf | Locally reproducible (requires network for data download; verified) |
| Veto numerical example (Section 4.1) | Locally reproducible (console output; verified) |
| All theoretical propositions | Not code-dependent; proved in paper |

No violations found.

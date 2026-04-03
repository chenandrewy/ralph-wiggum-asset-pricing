# tests/factcheck-code.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 2m 50s
[ralph-garage/agent-logs/20260402T223949.798403-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.798403-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: FAIL
REASON: The canonical pipeline silently skips Exhibit 1 when WRDS credentials are unavailable, violating the spec's from-scratch execution requirement.

## Canonical Local Analysis Path

The canonical entry point is `code/run-all.R`, which calls two scripts in order:

1. `code/numerical-illustration.R` — generates `paper/exhibits/numerical-illustration.tex` (Exhibit 2: numerical illustration table). No external data needed; parameters are hardcoded.
2. `code/ai-valuations-figure.R` — generates `paper/exhibits/ai-valuations.pdf` (Exhibit 1: CRSP price-dividend ratio figure). Requires WRDS credentials.

Both outputs go directly to `paper/exhibits/` as required by the spec.

## Execution Status

- **Numerical illustration (Exhibit 2):** Runs successfully from scratch. Output matches prior artifact exactly. **Locally reproducible.**
- **CRSP figure (Exhibit 1):** Runs successfully in this environment (WRDS credentials available). Retrieved 168 rows and generated the PDF. **Locally reproducible in this environment; blocked by credentials elsewhere.**
- **Full pipeline:** Completed in under 10 seconds. Well within the 180-second budget.

## Paper-Code Consistency

### Formulas: PASS

All code formulas match the paper's equations exactly:

| Paper equation | Code variable | Match |
|---|---|---|
| R = β(1+g)^{1−γ} (eq. 6) | `R` | ✓ |
| V_post = β(1+g̃)^{1−γ} / (1 − β(1+g̃)^{1−γ}) (eq. 9) | `V1` | ✓ |
| Φ^A = βΔ^{−γ}(1+g̃)^{1−γ} θ̃/θ (eq. 7) | `Phi_A` | ✓ |
| Φ^N = βΔ^{−γ}(1+g̃)^{1−γ} ν̃/ν (eq. 8) | `Phi_N` | ✓ |
| V_pre^A (eq. 3) | `V0_A` | ✓ |
| V_pre^N (eq. 4) | `V0_N` | ✓ |
| Φ^{A,CM} = β(1+g̃)^{1−γ} θ̃/θ (no Δ) | `Phi_A_CM` | ✓ |
| V_pre^{A,CM} (eq. 10) | `V0_A_CM` | ✓ |

### Parameters: PASS

All parameter values in the code match the paper text (Section 3, line 219):
β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30.

Derived quantities match: ω=0.60, ω̃=0.45, Δ=0.75.

### Numerical claims: PASS

Paper claims (line 219) vs. code output at p=0.01:
- V_pre^A ≈ 16.1 → code: 16.1 ✓
- V_pre^N ≈ 11.6 → code: 11.6 ✓
- Ratio ≈ 1.4 → 16.1/11.6 = 1.39 ✓
- V_pre^A at p=0 ≈ 11.9 → code: 11.9 ✓
- V_pre^{A,CM} ≈ 12.9 → code: 12.9 ✓
- Hedging premium ≈ 25% → code: 24.8% ✓

### Per-share data handling (Requirement 5): PASS

The CRSP figure code computes dollar dividends as `(ret - retx) * lagged_mcap`, avoiding per-share divamt/shrout mismatches across split events. The code explicitly documents this choice (lines 48–49 of `ai-valuations-figure.R`).

### Exhibit numbering: PASS

- Exhibit 1: `\label{fig:ai-valuations}` → `exhibits/ai-valuations.pdf` ✓
- Exhibit 2: `\label{tab:numerical}` → `exhibits/numerical-illustration.tex` ✓

## Violations

### 1. Silent skip of Exhibit 1 (spec III.3.c, III.3.e) — FAIL

`run-all.R` wraps the CRSP figure script in a `tryCatch` that catches errors and prints a message but does not stop the pipeline:

```r
tryCatch(
  run_script("code/ai-valuations-figure.R"),
  error = function(e) cat(sprintf("Skipping CRSP figure: %s\n", e$message))
)
```

The spec requires:
- III.3.c: "The canonical pipeline runs from scratch. It does not rely on precomputed local caches or manually prepared intermediate files."
- III.3.e: "Any external-data download or WRDS query required by the paper is part of the canonical pipeline."

When WRDS credentials are absent, the pipeline silently succeeds without regenerating Exhibit 1. If a stale `ai-valuations.pdf` exists from a prior run, the paper compiles with outdated data — effectively relying on a precomputed cache. The pipeline should either require WRDS credentials and fail hard, or delete the stale output before attempting the query so that a missing exhibit is visible.

## Reproducibility Classification

| Output | Classification |
|---|---|
| Exhibit 1 (ai-valuations.pdf) | Locally reproducible when WRDS credentials are set; blocked by credentials otherwise. Pipeline does not enforce this dependency. |
| Exhibit 2 (numerical-illustration.tex) | Locally reproducible from scratch, no external dependencies. |
| All numerical claims in Section 3 | Locally reproducible; verified by execution. |

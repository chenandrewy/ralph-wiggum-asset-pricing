# tests/factcheck-code.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 1m 40s
[ralph-garage/agent-logs/20260402T181745.328980-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T181745.328980-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: FAIL
REASON: The `code/` directory is empty — no canonical entry point exists, violating spec III.3.b.

## Canonical local analysis path

**No canonical analysis path exists.** The `code/` directory contains zero files. The `paper/exhibits/` directory does not exist. The `data/` directory is empty.

The paper spec (III.3.b) requires: *"code/ provides one canonical entry point that regenerates every exhibit used in paper/paper.tex."* Since `code/` is empty, there is no entry point at all.

The paper itself contains no exhibits — no `\includegraphics`, no `\input{exhibits/...}`, no figure or table environments. Consequently, the exhibit-regeneration requirement is vacuously satisfied for the current paper content. However:

- The spec (III.3.a–g) clearly envisions a populated `code/` directory with a from-scratch pipeline.
- The spec (IV.8.b) envisions empirical content: *"ideally a single figure in the introduction illustrating the valuation of publicly traded AI stocks compared with non-AI stocks using CRSP data."* This figure does not exist.
- The paper includes a numerical illustration (Section 3) with specific computed values. This constitutes analysis that, per the spec, belongs in `code/` and should output reproducible results.

## Execution status

| Item | Status |
|------|--------|
| R runtime available | Yes (`/usr/bin/Rscript`) |
| Code files in `code/` | **None** |
| Exhibits in `paper/exhibits/` | **None (directory absent)** |
| Data files in `data/` | **None** |
| Canonical entry point | **Missing** |
| Pipeline execution | **Blocked: nothing to run** |

## Paper-code consistency

**Numerical illustration (Section 3):** The paper reports values for a parameterization (β=0.96, γ=3, g=0.02, g̃=0.05, θ=0.05, θ̃=0.15, ν=0.55, ν̃=0.30, p=0.01). Independent verification confirms all stated values are correct:

- V₀ᴬ ≈ 16.1 ✓
- V₀ᴺ ≈ 11.6 ✓
- Ratio ≈ 1.4 ✓
- No-singularity P/D ≈ 11.9 ✓
- Complete-markets V₀ᴬ·ᶜᴹ ≈ 12.9 ✓
- Hedging premium ≈ 25% ✓

The numerical values are mathematically correct given the closed-form expressions and stated parameters. However, these computations exist only in the paper text — there is no code that generates or verifies them.

**No per-share data issues (Requirement 5):** The paper is purely theoretical with an inline parameterization. No empirical data is combined, so per-share consistency is not applicable.

## Reproducibility classification

| Paper object | Classification |
|--------------|---------------|
| Closed-form propositions (Props 1–4) | Algebraic — no code needed |
| Numerical illustration (Section 3) | **Not reproducible from canonical local path** — correct values, but no code exists to generate them |
| CRSP-based empirical figure (spec IV.8.b) | **Missing entirely** — neither code nor exhibit exists |
| All other paper content | Theoretical prose — no code needed |

## Violations

1. **Spec III.3.b (canonical entry point):** `code/` is empty. No entry point exists to regenerate exhibits or reproduce the numerical illustration.
2. **Spec III.3.c (from-scratch pipeline):** No pipeline exists at all.
3. **Spec IV.8.b (empirical content):** The spec calls for an empirical figure using CRSP data. Neither the figure, its code, nor the data exist in the repo.
4. **Requirement 1 (coherent canonical path):** There is no canonical analysis path for the paper.
5. **Requirement 4 (paper-code consistency for analysis):** The numerical illustration in Section 3 is analysis with no corresponding code.

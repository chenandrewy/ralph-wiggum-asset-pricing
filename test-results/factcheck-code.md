# tests/factcheck-code.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 1m 8s
[ralph-garage/agent-logs/20260402T180723.872507-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.872507-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The paper contains no exhibits, so the canonical analysis path is vacuously complete; all numerical claims are verified analytically.

## Canonical local analysis path

The paper is a pure theory paper. It contains **zero exhibits**: no figures, no tables, no `\includegraphics` or `\input{exhibits/...}` calls. The `code/` directory is empty, `data/` is empty, and `paper/exhibits/` does not exist.

The paper spec (III.3.b) requires that `code/` provides one canonical entry point that regenerates **every exhibit used in `paper/paper.tex`**. Since the paper uses no exhibits, this requirement is vacuously satisfied. There is no code to run and no output to regenerate.

The only quantitative content in the paper is a **numerical illustration** (Section 3, "Numerical illustration" paragraph) that plugs parameter values into closed-form formulas derived in the text. This does not require code; it is a direct evaluation of equations (10)--(14).

## Execution status

- **Code execution**: Not applicable. `code/` is empty and there is nothing to execute.
- **Environment blockers**: None. No R runtime, packages, or network access is needed.
- **Missing local inputs**: None. No data files are required.

## Paper-code consistency

| Paper claim | Status |
|---|---|
| V_0^A ~ 16.1 | Verified: 16.098 |
| V_0^N ~ 11.6 | Verified: 11.567 |
| V_0^A / V_0^N ~ 1.4 | Verified: 1.39 |
| V_0(p=0) ~ 11.9 | Verified: 11.940 |
| V_0^{A,CM} ~ 12.9 | Verified: 12.896 |
| Hedging premium ~ 25% of CM valuation | Verified: 24.8% |
| Delta = 0.75 | Verified: 0.75 |

All six numerical claims in the paper match the closed-form formulas to the stated precision.

## Reproducibility classification

| Object | Classification |
|---|---|
| Closed-form propositions (Props 1--4) | Locally reproducible (analytic derivations in paper) |
| Numerical illustration values | Locally reproducible (verified by direct computation) |
| CRSP-based empirical figure (spec II.8.b suggests one) | Not present in paper; no violation since spec says "ideally" |
| Exhibits | None exist; no reproducibility issue |

## Notes

- The paper spec (II.8.b) states the empirical content should "ideally" include a single CRSP figure. The paper currently has no empirical figure. This is not a violation since the spec uses "ideally" rather than "must."
- The spec (II.7) allows at most 6 exhibits. Zero is within that bound.
- Per-share data handling (Requirement 5) is not applicable: the paper is purely theoretical with no empirical data construction.
- No hidden or auxiliary files are required (Requirement 7): the paper compiles from `paper.tex` and `references.bib` alone.

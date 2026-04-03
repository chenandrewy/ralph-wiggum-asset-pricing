# tests/factcheck-freely.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 5m 24s
[ralph-garage/agent-logs/20260402T223949.798459-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T223949.798459-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: Notation inconsistency between table headers (V_0) and paper body (V_pre).

## Notation Inconsistency: Table vs. Body

**Location**: Exhibit 2 (`paper/exhibits/numerical-illustration.tex`) vs. Propositions 1–3 in Section 3

The paper body consistently defines and uses `V_{\mathrm{pre}}` and `V_{\mathrm{post}}` notation for pre- and post-singularity price-dividend ratios (equations 5–10, all proofs). However, the numerical illustration table (Exhibit 2) uses `V_0^A`, `V_0^N`, `V_0^{A,\mathrm{CM}}` in its column headers and notes. A reader encountering `V_0` in the table would not immediately connect it to the `V_{\mathrm{pre}}` defined in the model section. This is a notation inconsistency within the paper.

The inconsistency originates in `code/numerical-illustration.R` (lines 71, 83), which generates the table with `V_0` notation rather than the `V_{\mathrm{pre}}` convention used in the paper body.

## Items Verified as Correct

- **Propositions 1–3**: Mathematical derivations and proofs check out algebraically. The Euler equation expansion, probability-weighted contributions, closed-form solutions, quotient-rule derivative, and hedging premium formula are all correct.
- **Numerical values**: All stated values (V_pre^A = 16.1, V_pre^N = 11.6, ratio of 1.4, hedging premium ~25%) verify against the model formulas.
- **Assumption 3 (existence conditions)**: Correctly stated as automatically satisfied when gamma > 1 with positive growth rates.
- **Remark 1 (extreme singularity)**: Correct limit behavior as g_tilde → ∞ for gamma > 1 and gamma = 1.
- **Extinction risk formula (equation 12)**: Correctly multiplies singularity-state contribution by (1-q).
- **GKP and Jones (2024) citations**: Descriptions accurately represent source papers.
- **CRSP data methodology**: The query correctly uses CRSP permnos, which handle ticker changes (e.g., FB → META), so the AI basket is complete across the sample period.
- **Model internal consistency**: Absorbing-event structure, consumption shares, market clearing, and budget constraints are all internally consistent.

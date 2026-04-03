# tests/quality-formalism.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 3m 6s
[ralph-garage/agent-logs/20260402T215920.409348-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T215920.409348-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: FAIL
REASON: Proposition 2 is a compressible formal object whose content follows immediately from Proposition 1 and could be stated in plain English without weakening any economic claim.

## Requirement 8a — Theory style

### (8a-1) No dead-weight formal objects: PASS
Every formal object in the paper (Assumptions 1–3, Propositions 1–4, Remarks 1–2, and all displayed equations) connects to a model primitive, pricing result, or spec-required extension. No formal object is introduced and abandoned.

### (8a-2) No compressible formal objects: FAIL
**Proposition 2 (eq. 12) is compressible.** The cross-sectional result V_0^A > V_0^N is an immediate, one-step consequence of Proposition 1: since Assumption 2 gives θ̃/θ > 1 > ν̃/ν, we have Φ^A > Φ^N, and the two P/D formulas share the same denominator, so V_0^A > V_0^N follows by inspection. The displayed formula for the spread is never used in any subsequent result, calibration, or interpretation. The comparative statics of the spread ("increases with p and 1 − Δ") are stated informally in the paragraph that follows and could equally be stated informally without the formula. Replacing Proposition 2 with a one-sentence prose observation after Proposition 1 would leave every headline claim in the paper equally supported.

Burden-of-proof test for Proposition 2:
- Required by the spec? No — the spec focuses on the P/D ratio and its response to singularity probability, not on a formal cross-section result.
- Required to support a central claim? No — Propositions 3 and 4 carry the paper's central arguments independently.
- If cut, would any headline claim become unsupported? No — the qualitative cross-section point survives as prose.

All other formal objects pass:
- Proposition 1 (P/D ratios in closed form): essential — every later result builds on it.
- Proposition 3 (∂V/∂p > 0): essential — it is the paper's main comparative static.
- Proposition 4 (hedging premium): essential — it isolates the incomplete-markets mechanism, the paper's central result.
- Remark 1 (extreme singularity): spec-required extension connecting to Jones (2024); the limit argument is brief and directly interprets the model's own objects.
- Remark 2 (Coase / frictions): spec-required formal analysis of when displacement risk can be overcome (spec I.6.a–c).
- Equation (16) (friction cost): spec-justified ("formal analysis" per spec I.6.a); short and directly used in Remark 2.
- Equation (15) (extinction risk): spec-required extension; one-line modification of the main formula.
- Assumptions 1–3 and equations (1)–(9): standard model primitives needed for self-containment.

### (8a-3) No orphan notation: PASS
All named variables, parameters, and functions are used in results, calibrations, or interpretations that matter for the paper's conclusions. D_t^P appears only in the output decomposition but is a standard accounting primitive needed for model self-containment. The variables F, τ, T introduced in equation (16) are used within the friction analysis and Remark 2. No notation is introduced and then dropped.

### (8a-4) No pompous or ceremonial formalism; no auxiliary detours: PASS
The paper has 4 propositions, 2 remarks, and 3 assumptions across roughly 12 pages of content — a lean formal footprint. The extensions (extinction risk, Coase/frictions) are spec-required and tightly scoped. No new agent types, bargaining variants, dynamic laws of motion, or auxiliary mechanisms are introduced beyond what the spec permits. The prose stays focused on the displacement channel throughout.

## Requirement 8b — Empirical scope: PASS
Empirical content is limited to a single CRSP-based figure (Figure 1) showing AI vs. non-AI price-dividend ratios. No regressions, additional empirical exhibits, or data exercises appear.

## Requirement 8c — Testable predictions: PASS
The paper generates three direct implications of the model: (1) AI stocks trade at a premium over non-AI stocks, (2) the premium increases with singularity probability and displacement severity, (3) the premium vanishes under complete markets. These are immediate consequences of the main propositions. The conclusion explicitly notes the paper "does not generate a broad menu of testable predictions." No laundry list of auxiliary predictions appears.

## Requirement 8d — Quantitative material: PASS
A single numerical parameterization (Section 3, "Numerical illustration") produces Table 1 for illustrative purposes. The text describes it as gauging magnitudes. No systematic calibration, estimation, or moment-matching exercise is attempted.

# tests/quality-formalism.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260402T184535.059891-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059891-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains tight formalism throughout; every formal object does economic work, empirical and quantitative content is appropriately limited, and there are no scope detours.

## 8a — Theory style

**PASS** (with minor note)

### Dead-weight formalism: None found.

Every proposition, assumption, and remark advances the paper's economic claims. Propositions 1-4 each do distinct work: closed-form P/D ratios, cross-sectional spread, comparative statics in p, and the incomplete-vs-complete markets comparison. The two remarks in the extension handle the spec-required connections to Jones (2024): extreme singularity limits (Remark 1) and Coasean friction-overcoming (Remark 2). The appendix proof of Proposition 3 is necessary and compact.

### Compressible formalism: None that warrant failure.

Candidate examined: **Equation (17), the friction cost formula** (F + tau * T) / Y = F/Y + tau(omega - omega_tilde). The qualitative point ("fixed costs become negligible as output grows") could be stated in English. However, the spec explicitly requires "formal analysis" of how transfers scale with output (spec 6a), and this is that analysis. It is two lines of algebra. Not compressible given the spec mandate.

Candidate examined: **The budget constraint (eq 7) and share holdings n_t^A, n_t^N.** These are introduced, then immediately collapsed by market clearing. They are standard model primitives required to derive equilibrium consumption, not ceremonial formalism.

### Orphan notation: Minor borderline case only.

**D_t^P (private AI capital dividends):** Defined in equations (3) and (4) but never referenced in any proposition, proof, remark, or interpretation. The paper could replace the D_t^P lines with prose ("the remaining fraction of output goes to AI owners") without weakening any claim. However, D_t^P appears as part of an output-accounting identity that makes visible why the household's share is omega < 1 — the existence of private AI capital that the household cannot access is central to the incomplete-markets argument. Including it in the display equation is a natural presentation choice, not orphan notation in any meaningful sense.

All other named variables (R, Phi^A, Phi^N, V_1, Delta, omega, omega_tilde, q, F, tau, T) are used in subsequent results or interpretations.

### Prose detours: None found.

The extension (Section 4) stays within the spec-permitted scope: extinction risk, extreme output limits, and the Coase/transfers analysis relative to GKP. No new agent heterogeneity, bargaining variants, mortality channels, or auxiliary mechanisms are introduced. The conclusion's one-sentence policy suggestion (expanding tradeable AI assets) connects directly to the paper's main argument about incomplete markets.

### Ceremonial formalism: None found.

Assumptions 1-3 are concise and each is invoked in subsequent results. No assumption is introduced for show. Proofs are appropriately placed (short ones inline, Proposition 3's proof in the appendix).

## 8b — Empirical scope

**PASS.** The paper contains exactly one empirical exhibit: Figure 1, showing P/D ratios for AI vs. non-AI stocks using CRSP data. No regressions, no additional empirical analysis, no data tables. This matches the spec's ideal of "a single figure in the introduction."

## 8c — Testable predictions

**PASS.** The paper generates three direct implications of the model: (1) AI stocks trade at higher P/D ratios (Prop 2), (2) the spread increases with singularity probability (Prop 3), (3) the premium vanishes under complete markets (Prop 4). These are organic outputs of the model, not a generated laundry list. The conclusion does not attempt to enumerate additional auxiliary predictions.

## 8d — Quantitative material

**PASS.** The numerical illustration (one paragraph + one table) uses a single parameterization to "gauge magnitudes." It is explicitly framed as illustrative. There is no calibration to data moments, no estimation, no sensitivity analysis, and no attempt to match specific valuation levels (the conclusion explicitly disclaims this).

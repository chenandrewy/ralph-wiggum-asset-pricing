# tests/quality-formalism.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 2m 37s
[ralph-garage/agent-logs/20260402T221344.373433-0400_quality-formalism_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.373433-0400_quality-formalism_claude_opus.log)

# quality-formalism
VERDICT: PASS
REASON: The paper maintains lean formalism throughout; every formal object serves an economic claim, calibration, or spec-required extension, and scope remains compact.

## 8a — Theory style

**PASS.** Detailed findings below.

### Dead-weight formalism: None found.

Every displayed equation and theorem environment contributes to the paper's economic claims. The model primitives (growth equations, dividend shares, utility, budget constraint, Euler equation) are standard and necessary for self-containedness. The three propositions each do distinct economic work: Proposition 1 characterizes equilibrium PD ratios, Proposition 2 delivers the key comparative static (when does singularity probability raise AI valuations), and Proposition 3 isolates the hedging premium as the gap between incomplete- and complete-market valuations.

### Compressible formalism: No actionable cases.

**Strongest candidates examined:**

1. **V_0^N and Phi^N in Proposition 1.** The non-AI PD ratio is structurally identical to the AI formula with one parameter substitution. It appears in no later proposition. However, the comparison V_0^A > V_0^N is a core economic point (AI stocks trade at a premium), and presenting both formulas in the equilibrium characterization makes the comparison immediate and transparent. Eliminating V_0^N would either leave the comparison unsupported or require a verbal argument that is less clear than the displayed formula. Acceptable as natural equilibrium characterization.

2. **Extinction-modified PD ratio (eq 18).** The formula V_0^{A,q} is a one-line modification (multiply singularity contribution by (1-q)). Could be stated verbally, but the spec requires formally incorporating extinction risk from Jones (2024), and the equation is minimal.

3. **Friction cost formula (eq 19).** The F + tau*T cost function introduces three new symbols. The spec explicitly requires "formal analysis" of how transfers affect displacement risk (spec I.6.a) and asks to "quantify the size of frictions that can be overcome, given infinite output" (spec I.6.c). The equation directly delivers Remark 2's result and is spec-mandated.

### Orphan notation: None found.

All named variables are used downstream:
- Delta (displacement ratio): appears in Phi^A, Phi^N, the hedging premium, and the comparative static discussion.
- D_t^P (private AI capital dividends): defined for output-share accounting (shares sum to 1) and referenced conceptually in Proposition 3 (complete markets). Standard model primitive.
- omega, tilde-omega: used in Delta, equilibrium consumption, and the friction cost analysis.
- n_t^A, n_t^N (share holdings): used in the budget constraint and immediately pinned to 1 by market clearing. Standard.
- F, tau, T (friction cost parameters): used in eq (19) and Remark 2. Spec-required.

### Pompous/ceremonial formalism: None found.

The paper avoids unnecessary theorem environments. Results that follow by inspection (V_0^A > V_0^N, spread increases with p) are stated in prose rather than elevated to propositions. Proofs are concise: Proposition 1 and 3 are proved inline in a few lines each; Proposition 2's proof is in the appendix as appropriate for its length.

### Prose detours / scope candidates: None found.

- The Jones (2024) discussion in Section 4.1 (curvature of utility, asymmetry between AI owners and household) directly supports Remark 1 and is spec-permitted.
- Section 4.2's Coase theorem discussion is substantive, directly supports Remark 2, and is spec-required (contribution relative to GKP).
- The conclusion mentions omitted features (heterogeneous households, production-side frictions, endogenous innovation) as scope limitations, not as detours — this is appropriate self-awareness, not a scope violation.
- No new mechanisms, agent heterogeneity, bargaining variants, or dynamic laws of motion are introduced beyond what the spec permits.

## 8b — Empirical scope

**PASS.** The paper contains exactly one empirical exhibit: Figure 1, which plots CRSP-based price-dividend ratios for AI vs. non-AI stocks. It appears in the introduction to motivate the theory. No other empirical content is present.

## 8c — Testable predictions

**PASS.** The paper's predictions are direct implications of the model: AI stocks have higher PD ratios than non-AI stocks, the premium increases with singularity probability and displacement severity, and it vanishes under complete markets. The conclusion explicitly states: "It does not generate a broad menu of testable predictions." No laundry list of auxiliary predictions.

## 8d — Quantitative material

**PASS.** One numerical illustration paragraph with a single table (Table 1). Parameters are chosen for illustration ("To gauge magnitudes"), not calibrated to data. No estimation, no moment-matching, no systematic calibration exercise. The illustration serves to show that a 1% singularity probability generates economically meaningful premium magnitudes.

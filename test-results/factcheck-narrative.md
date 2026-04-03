# tests/factcheck-narrative.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 1m 41s
[ralph-garage/agent-logs/20260402T222807.260191-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T222807.260191-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: FAIL
REASON: Broken figure cross-reference (Figure 1 commented out but cited in text), and Section 2.4 title overpromises relative to its content.

---

## Section-by-Section Analysis

### Abstract

- **Contract**: Summarize the paper's main claims: AI stocks command a valuation premium as a hedge against a negative AI singularity; PD ratio increases with singularity probability when displacement is severe; complete markets eliminates the premium; abundant output can eliminate displacement risk.
- **Deliverables**: Each claim maps to a specific result in the body (Propositions 1--3, Remarks 1--2).
- **Status**: FULFILLED. All abstract claims are supported by results in the body. The conditional phrasing ("when displacement is sufficiently severe") correctly matches Proposition 2's condition.

### Section 1: Introduction

- **Contract**: Motivate the paper with empirical evidence on AI valuations, present the hedging-channel argument, preview the model and main results, situate the paper in the literature.
- **Deliverables**: Opens with AI valuation surge and references Figure 1 (CRSP data). Describes the hedging mechanism verbally. Previews the model (infinite-horizon, two assets, representative household, AI owners). Previews results (closed-form PD ratio, comparative statics, complete-markets benchmark, extension with extinction and frictions). Discusses AI-authored nature of the paper. Provides a lit review paragraph.
- **Status**: UNFULFILLED. The text states "Figure~\ref{fig:ai-valuations} illustrates this pattern using CRSP data" (line 43), but the figure environment is entirely commented out (lines 45--50). This is a broken cross-reference: the paper promises empirical illustration that does not appear. The remainder of the introduction is well-delivered.

### Section 2: Model (opening)

- **Contract**: Opening sentence (line 74): "We now translate the introduction's intuition---that incomplete markets make AI stocks valuable hedges---into a formal environment."
- **Deliverables**: The four subsections that follow collectively deliver a formal environment.
- **Status**: FULFILLED. The transition sentence accurately describes what follows.

### Section 2.1: Environment

- **Contract**: Define the economic environment (agents, output, singularity).
- **Deliverables**: Discrete time, aggregate output with normal growth (eq. 1) and singularity growth (eq. 2), two agent types (household, AI owners), singularity as absorbing event with probability p.
- **Status**: FULFILLED. All elements of the environment are specified.

### Section 2.2: Assets and Dividends

- **Contract**: Define publicly traded assets and their dividend processes.
- **Deliverables**: Three dividend streams (AI stocks, non-AI stocks, private AI capital) with output shares before (eq. 3) and after (eq. 4) the singularity. Assumptions 1--2 formalize "negative singularity" and "AI share growth." Displacement ratio Delta defined.
- **Status**: FULFILLED.

### Section 2.3: The Household's Problem

- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA preferences (eq. 6), budget constraint (eq. 7), market clearing (n=1), equilibrium consumption (eq. 8), Euler equation (eq. 9). Verbal preview of the hedging mechanism via marginal utility.
- **Status**: FULFILLED. The verbal note after the Euler equation ("This equation will deliver the hedging premium...") is a forward-looking claim; it is fulfilled in Section 3.

### Section 2.4: Equilibrium

- **Contract**: Title says "Equilibrium," which conventionally means characterizing equilibrium prices and allocations.
- **Deliverables**: States that PD ratios are constant within each regime (a qualitative observation), then imposes Assumption 3 (parameter restrictions for finite PD ratios). Does not derive or state equilibrium prices.
- **Status**: UNFULFILLED. The title "Equilibrium" promises more than existence conditions. The actual equilibrium characterization (closed-form PD ratios) appears in Section 3. This subsection should be titled something like "Parameter Restrictions" or "Existence Conditions," or it should contain the equilibrium result. As written, the title overpromises.

### Section 3: Results

- **Contract**: Title says "Results." The section contains three propositions and a numerical illustration.
- **Deliverables**: Proposition 1 (closed-form PD ratios), Proposition 2 (comparative static on p), Proposition 3 (complete vs. incomplete markets, hedging premium formula), numerical illustration with specific parameterization.
- **Status**: FULFILLED. All results are formally stated and proved (Proposition 2's proof deferred to Appendix A, which exists and contains the proof).

### Section 3, Paragraph after Proposition 1 (lines 188)

- **Contract**: Interpret the PD ratio formulas and explain the hedging mechanism.
- **Deliverables**: Explains Delta^{-gamma} as the displacement amplifier, explains why AI stocks are hedges, states that V_pre^A > V_pre^N, and claims the valuation spread increases with p and displacement severity.
- **Status**: FULFILLED, with a caveat. The claim that V_pre^A > V_pre^N follows directly from Phi^A > Phi^N (since tilde_theta/theta > 1 > tilde_nu/nu) and identical denominators. The claim that "the valuation spread increases with p" is stated without formal proof; it is correct (the spread is proportional to p in the numerator, and the denominator shrinks with p), but the paper treats it as obvious rather than proving it. This is a minor claim-strength concern -- the claim is verbally stated as fact but not formally established.

### Section 3, Numerical Illustration

- **Contract**: "To gauge magnitudes" -- illustrate the model with specific parameter values.
- **Deliverables**: Specific parameterization, reported PD ratios for several values of p, comparison with no-singularity and complete-markets benchmarks. References Table (Exhibit 2).
- **Status**: FULFILLED. This is explicitly an illustration, not a calibration, consistent with the spec's requirement that quantitative material remain illustrative.

### Section 4: Extension: Singularity, Extinction, and Frictions

- **Contract**: Extend the baseline model in two directions: extinction risk and overcoming frictions.
- **Deliverables**: Two subsections covering exactly these two extensions.
- **Status**: FULFILLED.

### Section 4.1: Extinction Risk

- **Contract**: Incorporate the possibility that the singularity destroys the economy.
- **Deliverables**: Modified PD ratio with extinction probability q (eq. 16). Discussion of the limit q -> 1. Connection to Jones (2024) on utility curvature. Remark 1 on the limit tilde_g -> infinity.
- **Status**: FULFILLED. The section delivers both the formal extension and economic interpretation.

### Section 4.2: Overcoming Frictions: The Coase Theorem in the Singularity

- **Contract**: Analyze when the frictions that sustain displacement risk can be overcome, connecting GKP to Jones.
- **Deliverables**: Describes GKP's friction assumption and notes that GKP discuss but do not formally analyze transfer mechanisms. Introduces a cost structure for transfers (eq. 18). Shows that fixed costs vanish as Y -> infinity. Remark 2 formalizes the conclusion.
- **Status**: FULFILLED. The section delivers the promised formal analysis. The cost structure is simple but sufficient for the claim. The connection to both GKP and Jones is explicit.

### Section 5: Conclusion

- **Contract**: Summarize implications and scope.
- **Deliverables**: Policy implication (expanding tradeable AI claims reduces displacement premium). Acknowledges model limitations (no heterogeneous households, no production frictions, no endogenous innovation). Restates the main insight about moderate singularities.
- **Status**: FULFILLED. The conclusion does not overclaim. The synthesis that "the hedging premium is largest for moderate singularities" is supported by Proposition 2 (premium increases with p under conditions), Remark 1 (premium vanishes as growth becomes extreme), and Remark 2 (premium vanishes when output is unbounded).

### Appendix A: Proofs

- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 2.
- **Status**: FULFILLED. The proof is complete and matches the reference from Section 3.

---

## Cross-Reference Findings

1. **BROKEN**: Line 43 references `Figure~\ref{fig:ai-valuations}` but the figure is commented out (lines 45--50). The compiled paper will show a broken reference ("Figure ??"). This is the most serious narrative failure.
2. **OK**: Proposition 2 proof says "See Appendix~\ref{app:proofs}" -- Appendix A exists and contains the proof.
3. **OK**: Propositions 1--3 reference Assumptions 1--3, all of which are defined in Section 2.
4. **OK**: Equations cross-referenced within proofs (e.g., eq. 9 in the proof of Proposition 1) exist and contain the referenced content.
5. **OK**: Section 4.2 references GKP's discussion of bequests/government debt/transfers -- this matches the description in Section 2.1 and the spec.

## Claim-Strength Findings

1. **MINOR**: Line 188 claims "The valuation spread increases with the singularity probability p and with the severity of displacement (1 - Delta)" without formal proof. The claim is correct but presented as self-evident when it requires a (simple) argument about numerator and denominator behavior.
2. **OK**: All proposition statements are precisely conditioned (e.g., Proposition 2's "if and only if" condition).
3. **OK**: The abstract's claims are appropriately hedged ("when displacement is sufficiently severe").
4. **OK**: The conclusion's claim about "moderate singularities" synthesizes multiple results without overclaiming.
5. **OK**: The paper's characterization of its contribution relative to GKP is appropriately modest throughout.

## Summary of Failures

| # | Severity | Location | Issue |
|---|----------|----------|-------|
| 1 | **HIGH** | Introduction, line 43 | Figure 1 referenced but commented out -- broken cross-reference |
| 2 | **MEDIUM** | Section 2.4 title | "Equilibrium" title overpromises; section contains only existence conditions, not equilibrium characterization |
| 3 | **LOW** | After Proposition 1 | Valuation spread comparative static claimed without proof |

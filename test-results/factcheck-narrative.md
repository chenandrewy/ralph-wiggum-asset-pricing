# tests/factcheck-narrative.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 2m 10s
[ralph-garage/agent-logs/20260402T223949.816720-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T223949.816720-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: PASS
REASON: Every section fulfills its narrative contract; cross-references are accurate; no claim exceeds its evidence.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: Summarize why AI stocks are expensive; state the model's mechanism and key results.
- **Deliverables**: Claims (1) AI stocks hedge against negative AI singularity, (2) P/D ratio increases with singularity probability when displacement is severe, (3) complete markets eliminate the premium, (4) abundant output + modest transfers can eliminate displacement risk.
- **Status**: FULFILLED. Every abstract claim maps to a specific result in the body: (1) Proposition 1 discussion + Proposition 3, (2) Proposition 2, (3) Proposition 3, (4) Remark 2 in Section 4.2.

### Section 1: Introduction
- **Contract**: Motivate the puzzle (high AI valuations), propose the hedging channel, preview model and results, situate in literature.
- **Deliverables**: Empirical motivation with Figure 1 (CRSP data), intuitive argument for hedging channel, model preview (infinite-horizon, two assets, representative household), preview of all main results and extension, related literature paragraph.
- **Status**: FULFILLED. Each previewed result (closed-form P/D ratio, comparative static in p, complete-markets benchmark, extinction risk, Coase theorem/frictions) appears in the body. The literature paragraph is properly scoped.

### Section 2: Model
- **Contract** (opening sentence): "translate the introduction's intuition---that incomplete markets make AI stocks valuable hedges---into a formal environment."
- **Deliverables**: Full model specification across four subsections.
- **Status**: FULFILLED. The section delivers a complete formal environment that operationalizes the introduction's verbal argument.

#### Section 2.1: Environment
- **Contract**: Define the economic environment.
- **Deliverables**: Discrete time, aggregate output with normal and post-singularity growth rates, singularity as absorbing event with probability p, two agent types (household, AI owners), interpretation following GKP.
- **Status**: FULFILLED.

#### Section 2.2: Assets and Dividends
- **Contract**: Define assets and their dividend structure.
- **Deliverables**: Three dividend streams (AI, non-AI, private) as output shares; pre- and post-singularity share equations; Assumption 1 (negative singularity) and Assumption 2 (AI share growth); displacement ratio definition.
- **Status**: FULFILLED.

#### Section 2.3: The Household's Problem
- **Contract**: State the household's optimization problem.
- **Deliverables**: CRRA preferences, budget constraint, market clearing, equilibrium consumption, Euler equation, verbal foreshadowing of hedging premium mechanism.
- **Status**: FULFILLED. The verbal claim about marginal utility and displacement ("displacement reduces the household's consumption share, pushing up marginal utility in singularity states") is an intuitive preview, not a formal claim, and is subsequently formalized in Section 3.

#### Section 2.4: Parameter Restrictions
- **Contract**: State parameter restrictions for well-defined prices.
- **Deliverables**: Assumption 3 (existence conditions ensuring finite P/D ratios), verbal justification that conditions are automatically satisfied in the empirically relevant case.
- **Status**: FULFILLED.

### Section 3: Results
- **Contract**: Present the model's results.
- **Deliverables**: Three propositions with proofs, verbal interpretation, numerical illustration with table.
- **Status**: FULFILLED.

#### Proposition 1 (Price-dividend ratios)
- **Contract**: Derive P/D ratios in closed form.
- **Deliverables**: Closed-form expressions for AI and non-AI P/D ratios, with full proof. Verbal interpretation identifies displacement term Delta^{-gamma} as the key hedging mechanism and explains why V_pre^A > V_pre^N.
- **Status**: FULFILLED. The claim "AI stocks trade at a premium" follows directly from the formulas and Assumption 2.

#### Proposition 2 (Comparative static)
- **Contract**: Show when singularity probability raises AI valuations.
- **Deliverables**: Necessary and sufficient condition for dV/dp > 0, economic interpretation, proof in Appendix A.
- **Status**: FULFILLED. The proposition states "if and only if" and the proof delivers an if-and-only-if condition. The verbal interpretation ("The condition holds when displacement is sufficiently severe...") correctly describes qualitative implications of the condition without overclaiming.

#### Proposition 3 (Complete vs. incomplete markets)
- **Contract**: Compare valuations under complete and incomplete markets, isolate the hedging premium.
- **Deliverables**: Complete-markets P/D formula, closed-form hedging premium expression, comparative statics on premium.
- **Status**: FULFILLED. The verbal claim "Proposition 3 is the central result" is a framing judgment, not a factual claim, and is appropriate.

#### Numerical Illustration
- **Contract** (paragraph title): "gauge magnitudes" of the results.
- **Deliverables**: Specific parameter values, computed P/D ratios for several values of p, comparison with complete-markets benchmark, Table (Exhibit 2).
- **Status**: FULFILLED. The illustration is correctly framed as illustrative ("To gauge magnitudes, consider the following parameterization"), consistent with the spec's requirement that quantitative material remain illustrative. The reported numbers (V_pre^A ~ 16.1, V_pre^N ~ 11.6, V_pre^{A,CM} ~ 12.9 at p=0.01; both ~ 11.9 at p=0) are consistent with the model formulas.

### Section 4: Extension: Singularity, Extinction, and Frictions
- **Contract** (opening sentence): "extend the analysis in two directions, drawing on Jones (2024): incorporating extinction risk, and considering when the frictions that sustain displacement risk can be overcome."
- **Deliverables**: Two subsections delivering exactly these two extensions.
- **Status**: FULFILLED.

#### Section 4.1: Extinction Risk
- **Contract**: Incorporate extinction risk into the model.
- **Deliverables**: Modified P/D formula with extinction probability q, verbal interpretation of attenuation effect, Remark 1 on extreme singularity (g-tilde -> infinity), connection to Jones (2024) on utility curvature.
- **Status**: FULFILLED. The extinction modification is a direct extension of Proposition 1. Remark 1 correctly identifies two opposing forces and their resolution for gamma > 1.

#### Section 4.2: Overcoming Frictions: The Coase Theorem in the Singularity
- **Contract**: Analyze when frictions that sustain displacement risk can be overcome.
- **Deliverables**: Discussion of GKP's friction assumption, formal friction-cost model (F + tau*T), limiting argument as Y -> infinity, Remark 2 on singularity-level output.
- **Status**: FULFILLED. The section delivers a formal (though simple) analysis of how transfer costs scale with output, fulfilling the spec's requirement (I.6.a) for a "formal analysis" of GKP's friction discussion. The Coase theorem framing is appropriate: the argument is that fixed costs become negligible relative to surplus as output grows.

### Section 5: Conclusion
- **Contract**: Conclude the paper.
- **Deliverables**: Policy implications (expanding tradeable AI claims), scope limitations (stylized model, no heterogeneous households, no endogenous innovation), summary of main result (hedging premium largest for moderate singularities).
- **Status**: FULFILLED. The conclusion does not overclaim. It correctly leads with policy implications and explicitly acknowledges limitations.

### Appendix A: Proofs
- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 2.
- **Status**: FULFILLED. Proposition 2 is the only result whose proof is deferred to the appendix, and the proof is present and complete.

---

## Cross-Reference Checks

| Reference | Location | Target | Status |
|-----------|----------|--------|--------|
| "Figure 1" (fig:ai-valuations) | Intro para 1 | Figure in Section 1 | VALID |
| "Assumptions 1--3" | Proposition 1 | Assumptions in Sections 2.2, 2.4 | VALID |
| "Assumption 1" (as:neg-sing) | Multiple | Section 2.2 | VALID |
| "Assumption 2" (as:ai-share) | Multiple | Section 2.2 | VALID |
| "Assumption 3" (as:existence) | Proposition 1 | Section 2.4 | VALID |
| "See Appendix A" | Proposition 2 proof | Appendix A | VALID — proof present |
| "Remark 1" (rem:extreme) | Proposition 2 statement | Section 4.1 | VALID |
| Euler equation ref (eq:euler) | Prop 1 proof | Section 2.3 | VALID |
| GKP (2012) characterization | Multiple | Correctly described as source of displacement risk and incomplete intergenerational risk-sharing | VALID |
| Jones (2024) characterization | Section 4 | Correctly described re: AI growth vs. existential risk trade-off | VALID |

No broken or misleading cross-references found.

---

## Claim-Strength Assessment

All verbal claims are appropriately calibrated to the evidence:

1. **"We show that..."** (Abstract, Introduction) — Each "show" claim maps to a formal proposition. No overclaiming.
2. **"We propose an additional channel"** (Introduction) — Correctly framed as a proposal, not an empirical finding.
3. **"it follows immediately that V_pre^A > V_pre^N"** (after Proposition 1) — This does follow from the formulas and Assumption 2. Claim strength is appropriate.
4. **"The valuation spread increases with the singularity probability p and with the severity of displacement"** (after Proposition 1) — The spread V_pre^A - V_pre^N has numerator p(Phi^A - Phi^N)(1+V_post), which is increasing in p. The spread's dependence on displacement severity (1-Delta) operates through Delta^{-gamma} in both Phi terms. Claim is supported.
5. **"Proposition 3 is the central result"** — Framing judgment, not a factual claim. Appropriate.
6. **"the hedging premium is largest for moderate singularities"** (Conclusion) — Supported by Remark 1 (extreme growth eliminates premium via utility saturation) and Remark 2 (extreme output eliminates frictions via Coase logic). The premium vanishes at both extremes and at p=0, so it is indeed largest at intermediate values.
7. **"This paper itself illustrates the displacement risk it models"** (Introduction) — A self-referential observation, appropriately framed as an illustration rather than evidence.

No claim was found to be stronger than the evidence the paper provides.

---

## Summary

The paper is narratively tight. Every section delivers what its title and opening framing promise. The abstract and introduction claims are all supported by formal results in the body. Cross-references are accurate. Verbal claims are appropriately hedged and calibrated to the paper's formal results. No narrative gaps, unfulfilled contracts, or broken references were identified.

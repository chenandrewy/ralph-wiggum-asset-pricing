# tests/factcheck-narrative.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 1m 14s
[ralph-garage/agent-logs/20260402T215920.395512-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T215920.395512-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: PASS
REASON: Every section delivers on its stated contract, cross-references are accurate, and claim strengths match the evidence provided.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: State why AI stocks are expensive; summarize the model's mechanism, key results, and extension.
- **Deliverables**: Claims (1) AI stocks hedge against negative AI singularity, (2) incomplete markets are key, (3) P/D ratio increases with singularity probability when displacement is severe, (4) complete markets eliminate the premium, (5) abundant output can eliminate displacement risk.
- **Status**: FULFILLED. Every claim in the abstract is delivered by the body (Propositions 1-4, Remarks 1-2).

### Preface (TBC)
- **Contract**: Placeholder section, left blank per spec.
- **Deliverables**: Empty.
- **Status**: FULFILLED. Intentionally blank as specified.

### Section 1: Introduction
- **Contract**: Motivate the paper empirically (AI valuations), state the economic argument (hedging channel via incomplete markets), preview the model and results, describe the extension, and provide a lit review.
- **Deliverables**: (1) Empirical motivation with Figure 1, (2) intuitive description of the hedging mechanism, (3) preview of the infinite-horizon model with two assets and two agents, (4) closed-form P/D ratio result and comparative statics, (5) extension connecting to Jones (2024) and GKP (2012), (6) AI-authored paper disclosure, (7) lit review paragraph.
- **Status**: FULFILLED. Each promised element is present. The introduction claims "we derive the price-dividend ratio of AI stocks in closed form"---delivered in Proposition 1. Claims about comparative statics---delivered in Propositions 2-3. Claims about complete markets---delivered in Proposition 4. Claims about extension (extinction, overcoming frictions)---delivered in Section 4.

### Section 2: Model

#### Section 2.1: Environment
- **Contract**: Specify the economic environment (agents, output, singularity event).
- **Deliverables**: Discrete-time infinite-horizon economy, aggregate output with normal growth (Eq. 1) and post-singularity growth (Eq. 2), two agent types (household, AI owners), singularity as absorbing event with probability p.
- **Status**: FULFILLED. All elements of the environment are specified.

#### Section 2.2: Assets and dividends
- **Contract**: Define the asset structure and dividend processes.
- **Deliverables**: Three dividend streams (AI stocks, non-AI stocks, private AI capital) with output shares (Eqs. 3-4), Assumptions 1-2 defining the negative singularity and AI share growth, displacement ratio definition (Eq. 5).
- **Status**: FULFILLED. The section fully specifies what it promises.

#### Section 2.3: The household's problem
- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA utility (Eq. 6), budget constraint (Eq. 7), market clearing yielding equilibrium consumption (Eq. 8), Euler equation (Eq. 9) with verbal preview of the hedging mechanism.
- **Status**: FULFILLED. The optimization problem is fully specified with preferences, constraints, and equilibrium conditions.

#### Section 2.4: Equilibrium
- **Contract**: Characterize the equilibrium and state parameter restrictions.
- **Deliverables**: Statement that P/D ratios are constant within each regime, Assumption 3 (existence conditions ensuring finite P/D ratios).
- **Status**: FULFILLED. The section is brief but delivers exactly what its framing promises: the equilibrium concept (constant P/D ratios) and the technical conditions needed for existence.

### Section 3: Results
- **Contract**: Derive and present the paper's main pricing results.
- **Deliverables**: Proposition 1 (closed-form P/D ratios for AI and non-AI stocks, with proof), Proposition 2 (AI stocks trade at a premium, with proof), Proposition 3 (comparative statics in p, with proof in appendix), Proposition 4 (incomplete vs. complete markets and the hedging premium, with proof), numerical illustration with Table (Exhibit 2).
- **Status**: FULFILLED. Four propositions, each with proof (inline or appendix), plus a numerical illustration. The section delivers every result previewed in the introduction.

### Section 4: Extension: Singularity, Extinction, and Frictions
- **Contract**: Extend the baseline model to incorporate extinction risk and conditions for overcoming displacement frictions.
- **Deliverables**: Two subsections delivering exactly these two extensions.

#### Section 4.1: Extinction risk
- **Contract**: Incorporate extinction risk into the model.
- **Deliverables**: Modified P/D ratio with extinction probability q (Eq. 14), analysis of how extinction attenuates the hedging premium, Remark 1 on extreme singularity limit connecting to Jones (2024).
- **Status**: FULFILLED. The extinction extension is formally specified and its implications for the hedging premium are stated.

#### Section 4.2: Overcoming frictions: the Coase theorem in the singularity
- **Contract**: Analyze when intergenerational frictions can be overcome, connecting GKP (2012) to Jones (2024).
- **Deliverables**: Discussion of GKP's friction assumption and their mention of transfer mechanisms, formal cost structure for transfers (Eq. 15), analysis of how fixed costs vanish as output grows, Remark 2 on displacement risk vanishing with unbounded output.
- **Status**: FULFILLED. The section promises a formal analysis of how frictions scale with output and delivers it via the cost equation and limiting argument. The claim that GKP "discuss" but "do not conduct a formal analysis" is consistent with the spec's characterization. The formal analysis here (Eq. 15 and Remark 2) goes beyond GKP's verbal discussion by specifying a cost structure and deriving the limiting result.

### Section 5: Conclusion
- **Contract**: Summarize implications and scope.
- **Deliverables**: Policy implication (expanding tradeable AI claims), statement of model limitations, summary of the main result (hedging premium largest for moderate singularities).
- **Status**: FULFILLED. The conclusion does not overclaim. It explicitly notes what the model omits (heterogeneous households, production frictions, endogenous innovation) and does not claim testable predictions beyond the model's scope.

### Appendix A: Proofs
- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3 (comparative static in p).
- **Status**: FULFILLED. Proposition 3 states "See Appendix A" and the appendix contains the proof.

---

## Cross-Reference Checks

| Reference | Location | Target | Status |
|-----------|----------|--------|--------|
| Figure 1 (ai-valuations) | Introduction para 1 | Figure exists with CRSP P/D data | OK |
| Table (numerical-illustration) | Section 3, "Numerical illustration" | Exhibit file exists | OK |
| "Assumptions 1-3" in Proposition 1 | Section 3 | Assumptions 1-2 in Section 2.2, Assumption 3 in Section 2.4 | OK |
| Euler equation (9) referenced in Prop 1 proof | Section 3 | Eq. 9 in Section 2.3 | OK |
| "See Appendix A" in Proposition 3 | Section 3 | Appendix A contains the proof | OK |
| Eq. references within proofs (eqs 7, 9, etc.) | Throughout | All referenced equations exist | OK |
| Remark 1 references Jones (2024) | Section 4.1 | Jones cited in lit review and introduction | OK |
| Remark 2 references GKP (2012) and Jones (2024) | Section 4.2 | Both cited in lit review and introduction | OK |

All internal cross-references point to content that exists.

---

## Claim-Strength Checks

1. **"We show that publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity"** (Abstract). Supported by Propositions 2 and 4, which formally derive the premium and attribute it to the hedging channel. Claim strength: appropriate.

2. **"The price-dividend ratio of AI stocks increases with the probability of a singularity when displacement is sufficiently severe"** (Abstract). Supported by Proposition 3, which gives the exact condition. The qualifier "when displacement is sufficiently severe" correctly hedges the claim. Claim strength: appropriate.

3. **"Under complete markets, the hedging premium vanishes"** (Abstract). Supported by Proposition 4, Eq. 16, which shows the premium equals zero when Delta = 1. Claim strength: appropriate.

4. **"When the singularity produces sufficiently abundant output, even modest transfers can eliminate displacement risk"** (Abstract). Supported by Remark 2 and Eq. 15. The word "can" appropriately hedges. Claim strength: appropriate.

5. **"The valuation spread increases with singularity probability p and displacement severity (1 - Delta)"** (after Proposition 2). This is stated as a verbal claim without formal proof. Inspecting Eq. 12: the numerator is increasing in p (directly) and in (1 - Delta) through Delta^{-gamma}. The denominator 1 - (1-p)R is decreasing in p, reinforcing the positive effect. Claim strength: appropriate (the comparative statics follow directly from the formula).

6. **"A 1% annual singularity probability generates a hedging premium of about 25% of the complete-markets valuation"** (numerical illustration). This is a numerical claim that depends on the parameter values and the formulas. The claim is presented as illustrative, not as a calibration. Claim strength: appropriate.

7. **Introduction claim about GKP contribution**: "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work." This is appropriately modest and consistent with the spec requirement. Claim strength: appropriate.

---

## Summary

The paper's narrative is internally consistent and well-structured. Every section delivers what its title and opening framing promise. The Abstract and Introduction claims are fully supported by the body's formal results. Cross-references are accurate. No verbal claim exceeds the evidence provided. The paper is appropriately modest about its contribution relative to GKP (2012) and correctly hedges conditional claims (e.g., "when displacement is sufficiently severe").

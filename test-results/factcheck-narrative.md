# tests/factcheck-narrative.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 1m 49s
[ralph-garage/agent-logs/20260402T214942.811301-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T214942.811301-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: PASS
REASON: Every section delivers what its title and framing promise; cross-references resolve correctly; no verbal claim exceeds the evidence provided.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: Summarize why AI stocks are expensive, the model mechanism, key results on P/D ratios, complete markets, and abundant-output transfers.
- **Deliverables**: Six claims: (1) AI stocks hedge against negative singularity, (2) household cannot invest in private AI capital, (3) P/D ratio increases with singularity probability when displacement is severe, (4) complete markets eliminates premium, (5) abundant output enables transfers that eliminate displacement.
- **Status**: FULFILLED. Each claim is delivered by the body: (1) Propositions 1--2, (2) Section 2.1 and 2.3, (3) Proposition 3, (4) Proposition 4, (5) Remark 2 and Section 4.2.

### Section 1: Introduction
- **Contract**: Motivate the paper empirically, state the argument, summarize the model and results, position relative to literature.
- **Deliverables**: Empirical motivation with Figure 1, intuitive description of mechanism, model overview (two assets, representative household, AI owners, singularity), summary of four main results (closed-form P/D, comparative statics, complete markets, extension), self-referential AI-authorship paragraph, literature review.
- **Status**: FULFILLED. Every result previewed in the introduction is delivered in the body. The empirical figure is present. The literature review is appropriately scoped. The AI-authorship paragraph is factual and consistent with the spec.

### Section 2: Model

#### Section 2.1: Environment
- **Contract**: Define the economic environment (agents, technology, singularity).
- **Deliverables**: Discrete time, output growth (normal and post-singularity), singularity as absorbing event with probability $p$, two agent types (household and AI owners), interpretation following GKP.
- **Status**: FULFILLED. All primitives of the environment are specified. The GKP interpretation is clearly stated and distinguished from the paper's own modeling choice.

#### Section 2.2: Assets and dividends
- **Contract**: Define the asset structure and dividend processes.
- **Deliverables**: Three dividend streams (public AI, non-AI, private AI) as output shares, pre- and post-singularity share parameters, two assumptions (negative singularity, AI share growth), displacement ratio definition.
- **Status**: FULFILLED. The section fully specifies the dividend structure and the economic content of each assumption.

#### Section 2.3: The household's problem
- **Contract**: State the household's optimization problem and derive equilibrium consumption.
- **Deliverables**: CRRA utility, budget constraint, market clearing, equilibrium consumption expression, Euler equation.
- **Status**: FULFILLED. The section derives equilibrium consumption from market clearing and states the Euler equation that will be used in Section 3.

#### Section 2.4: Equilibrium
- **Contract**: Characterize the equilibrium structure.
- **Deliverables**: Statement that P/D ratios are constant in each regime (with economic reasoning), parameter restrictions for existence (Assumption 3).
- **Status**: FULFILLED. The section establishes the equilibrium concept (constant P/D ratios in each regime) and the existence conditions. The actual closed-form solutions are deferred to Section 3 ("Results"), which is standard practice.

### Section 3: Results
- **Contract**: Derive the main pricing results.
- **Deliverables**: Proposition 1 (closed-form P/D ratios with proof), Proposition 2 (AI premium with proof), Proposition 3 (comparative statics with condition, proof in appendix), Proposition 4 (complete vs. incomplete markets with proof and hedging premium formula), numerical illustration with table.
- **Status**: FULFILLED. Four propositions are stated and proved (Proposition 3's proof is in Appendix A, as stated). The numerical illustration provides specific parameter values and reports magnitudes. Each proposition delivers exactly what its title claims.

### Section 4: Extension: Singularity, Extinction, and Frictions
- **Contract**: Extend the baseline model to incorporate extinction risk and conditions under which frictions can be overcome.
- **Deliverables**: Two subsections delivering on the two promised extensions.
- **Status**: FULFILLED. The section title accurately describes the two extensions that follow.

#### Section 4.1: Extinction risk
- **Contract**: Incorporate the possibility that the singularity destroys the economy.
- **Deliverables**: Modified P/D formula with extinction probability $q$, explanation of attenuation, connection to Jones (2024) on utility curvature, Remark 1 on the extreme-singularity limit.
- **Status**: FULFILLED. The section derives the extinction-adjusted formula, explains its economics, and connects to Jones (2024) as promised by the introduction.

#### Section 4.2: Overcoming frictions: the Coase theorem in the singularity
- **Contract**: Analyze when intergenerational frictions can be overcome, connecting GKP to Jones.
- **Deliverables**: Discussion of GKP's friction assumption, transfer cost model ($F + \tau T$), analysis of fixed vs. proportional costs as $Y \to \infty$, Remark 2 (Coase theorem applies when output is unbounded), interpretive paragraph connecting GKP and Jones.
- **Status**: FULFILLED. The section delivers the formal analysis promised in the introduction and spec. It explicitly addresses GKP's discussion of bequests/transfers, provides the friction-cost formalization, and derives the limiting result.

### Section 5: Conclusion
- **Contract**: Summarize results and discuss implications.
- **Deliverables**: Summary of four main results (hedging premium, cross-section, comparative statics, complete markets), restatement of the extension's two channels (utility curvature, Coasean risk-sharing), policy implication (expanding tradeable AI assets).
- **Status**: FULFILLED. Every result summarized in the conclusion is delivered in the body. The conclusion does not introduce new claims beyond what the paper has shown.

### Appendix A: Proofs
- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3.
- **Status**: FULFILLED. The proof referenced by Proposition 3 ("See Appendix A") is present and complete.

---

## Cross-Reference Checks

| Reference | Location | Target | Status |
|-----------|----------|--------|--------|
| Figure 1 (ai-valuations) | Section 1 | `exhibits/ai-valuations.pdf` | EXISTS |
| Table (numerical-illustration) | Section 3 | `exhibits/numerical-illustration.tex` | EXISTS |
| Assumption 1 refs in Propositions | Section 3 | Section 2.2 | CORRECT |
| Assumption 2 refs in Propositions | Section 3 | Section 2.2 | CORRECT |
| Assumption 3 refs in Propositions | Section 3 | Section 2.4 | CORRECT |
| "See Appendix A" in Prop 3 | Section 3 | Appendix A | CORRECT — proof present |
| Remark 1 ref in Conclusion | Section 5 | Section 4.1 | CORRECT |
| Remark 2 ref in Conclusion | Section 5 | Section 4.2 | CORRECT |
| Euler equation ref in Prop 1 proof | Section 3 | Eq. (7) in Section 2.3 | CORRECT |
| GKP interpretation ref | Section 2.1, 4.2 | Consistent usage | CORRECT |
| Jones (2024) ref | Section 4.1, 4.2 | Consistent usage | CORRECT |

All internal cross-references resolve to content that exists at the referenced location.

---

## Claim-Strength Checks

1. **"We derive the price-dividend ratio of AI stocks in closed form"** (Introduction): Proposition 1 provides an explicit closed-form expression. Claim strength: APPROPRIATE.

2. **"the ratio increases with the probability of a singularity"** (Introduction): Proposition 3 establishes this under a stated condition. The introduction qualifies this with "Under natural parameter restrictions." Claim strength: APPROPRIATE.

3. **"Under complete markets, the hedging premium vanishes"** (Abstract/Introduction): Proposition 4 derives this explicitly. Claim strength: APPROPRIATE.

4. **"The valuation spread $V_0^A - V_0^N$ increases with the singularity probability $p$ and with the severity of displacement"** (after Proposition 2): Stated without formal proof, but follows directly by inspection of equation (11) — the numerator is linear in $p$ with positive coefficient and the denominator $1-(1-p)R$ is decreasing in $p$ with $R < 1$. Claim strength: APPROPRIATE (simple enough to state without separate proof).

5. **"Even modest transfer mechanisms suffice when the surplus is enormous"** (Abstract): Remark 2 and the friction-cost analysis in Section 4.2 support this. The word "modest" maps to "any mechanism with a fixed-cost component." Claim strength: APPROPRIATE.

6. **"The model delivers a cross-sectional prediction"** (Conclusion): Proposition 2 formally establishes this. Claim strength: APPROPRIATE.

7. **"deliberately stylized and not designed to match specific valuation levels"** (Conclusion): Consistent with the numerical illustration being presented as illustrative rather than calibration. Claim strength: APPROPRIATE.

No verbal claim was found to exceed the evidence provided by the paper's formal results.

---

## Summary

The paper's narrative is internally consistent and well-aligned across all sections. Every section delivers what its title and opening framing promise. All cross-references resolve correctly. Verbal claims are appropriately calibrated to the formal results — no claim is stronger than the evidence. The Abstract and Introduction accurately preview the body's content without overstatement.

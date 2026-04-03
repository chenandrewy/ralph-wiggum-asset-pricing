# tests/factcheck-narrative.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 1m 58s
[ralph-garage/agent-logs/20260402T221344.370373-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T221344.370373-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: PASS
REASON: Every section delivers on its stated contract; cross-references resolve correctly; no verbal claims exceed the evidence provided.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: State the paper's main result and mechanism.
- **Deliverables**: Five claims: (1) AI stocks command a valuation premium as a hedge against a negative AI singularity, (2) the representative household cannot invest in private AI capital, (3) the P/D ratio increases with singularity probability when displacement is sufficiently severe, (4) under complete markets the hedging premium vanishes, (5) abundant output plus modest transfers can eliminate displacement risk.
- **Status**: FULFILLED. Claim (1) is delivered by Propositions 1 and 3. Claim (2) is a model assumption (Section 2.1/2.3). Claim (3) is Proposition 2. Claim (4) is Proposition 3. Claim (5) is Remark 2 in Section 4.2.

### Section 1: Introduction
- **Contract**: Motivate the question, preview the model and results, and place the paper in the literature.
- **Deliverables**: Empirical motivation (Figure 1), informal model description, summary of three main results (closed-form P/D ratio, comparative static, complete-markets benchmark), preview of the extension (extinction risk, overcoming frictions), AI-authorship disclosure, and a literature review.
- **Status**: FULFILLED. Every previewed result is delivered in the body. The claim "We derive the price-dividend ratio of AI stocks in closed form" is fulfilled by Proposition 1. "Under natural parameter restrictions, the ratio increases with the probability of a singularity" is fulfilled by Proposition 2 (with an explicit condition). The extension preview matches Section 4. The lit review is appropriately scoped.

### Section 2: Model

#### Section 2.1: Environment
- **Contract**: Define the economic environment.
- **Deliverables**: Discrete time, aggregate output with normal and post-singularity growth rates, singularity as absorbing event with probability p, two agent types (household and AI owners).
- **Status**: FULFILLED. All elements needed for the model are introduced. The connection to GKP's unborn-cohorts interpretation is stated and correctly distinguished from the paper's own modeling choice.

#### Section 2.2: Assets and Dividends
- **Contract**: Specify the asset structure and how dividends change at the singularity.
- **Deliverables**: Three dividend streams with output shares, pre- and post-singularity share equations, Assumptions 1-2 (negative singularity, AI share growth), displacement ratio definition.
- **Status**: FULFILLED. The section delivers exactly what the title promises.

#### Section 2.3: The Household's Problem
- **Contract**: State the household's optimization problem and derive equilibrium consumption.
- **Deliverables**: CRRA utility, budget constraint, market clearing (n=1), equilibrium consumption, Euler equation.
- **Status**: FULFILLED. The section also previews the hedging mechanism verbally ("the household's stochastic discount factor is high precisely when AI stocks pay well"), which is a forward pointer to Proposition 1's discussion. This is appropriate foreshadowing, not an unfulfilled promise.

#### Section 2.4: Equilibrium
- **Contract**: Characterize the equilibrium.
- **Deliverables**: States that P/D ratios are constant in each regime, imposes Assumption 3 (existence conditions).
- **Status**: FULFILLED (borderline). The section characterizes a key equilibrium property (constant P/D ratios) and establishes existence. The actual closed-form solution is in Section 3. This is a standard paper structure---setup in "Model," solution in "Results"---so the contract is met, though the section is thin.

### Section 3: Results

#### Proposition 1 (Price-dividend ratios)
- **Contract**: Derive closed-form P/D ratios for AI and non-AI stocks.
- **Deliverables**: Equations (8)-(13) with full proof, plus verbal interpretation of the hedging mechanism via displacement ($\Delta^{-\gamma}$).
- **Status**: FULFILLED. The proof is complete and inline. The verbal discussion correctly identifies $\Delta^{-\gamma}$ as the key object and explains why $V_0^A > V_0^N$.

#### Proposition 2 (Comparative static)
- **Contract**: Show that the AI P/D ratio increases in singularity probability.
- **Deliverables**: Necessary and sufficient condition, verbal interpretation, connection to displacement severity and risk aversion.
- **Status**: FULFILLED. The result is conditional (if and only if), and the verbal claims about when the condition holds ("displacement is sufficiently severe, risk aversion is sufficiently high, or the AI share gain is sufficiently large") are qualitatively supported by the structure of $\Phi^A$. Proof is in Appendix A and is complete.

#### Proposition 3 (Complete vs. incomplete markets)
- **Contract**: Compare valuations under incomplete and complete markets, isolate the hedging premium.
- **Deliverables**: Complete-markets P/D ratio, closed-form hedging premium expression, comparative statics.
- **Status**: FULFILLED. The proof explains the economic mechanism (consumption growth changes, $\Delta^{-\gamma}$ replaced by 1). The verbal claim that this is "the central result" is a judgment, not a factual claim requiring verification.

#### Numerical Illustration
- **Contract**: "Gauge magnitudes" with a parameterization.
- **Deliverables**: Specific parameter values, reported P/D ratios from Table 1, comparison across singularity probabilities and market structures.
- **Status**: FULFILLED. The paragraph promises to "gauge magnitudes" and delivers specific numbers. It does not claim to calibrate (which would require mapping data to parameters), only to illustrate---consistent with the spec's requirement that quantitative material remain illustrative.

### Section 4: Extension: Singularity, Extinction, and Frictions

#### Section 4.1: Extinction Risk
- **Contract**: Incorporate extinction risk into the model.
- **Deliverables**: Modified P/D formula with extinction probability q, verbal interpretation, connection to Jones (2024) on utility curvature, Remark 1 on extreme singularity limit.
- **Status**: FULFILLED. The section delivers the modified formula and the economic interpretation. Remark 1 correctly identifies the limit behavior for $\gamma > 1$ and $\gamma = 1$.

#### Section 4.2: Overcoming Frictions
- **Contract**: Analyze when intergenerational frictions can be overcome, taking up the question GKP raised but did not formally analyze.
- **Deliverables**: Verbal Coase theorem argument, formal cost model (equation 17), Remark 2 on the limit $Y \to \infty$.
- **Status**: FULFILLED. The section explicitly states it is taking up GKP's unanalyzed question ("GKP discuss how mechanisms... but do not conduct a formal analysis of how these mechanisms scale with output. We take up this question.") and delivers a formal (if stylized) analysis. The claim that GKP "do not conduct further analysis" is consistent with the spec's characterization of the contribution.

### Section 5: Conclusion
- **Contract**: Summarize and discuss implications.
- **Deliverables**: Policy implication (expanding tradeable AI claims), summary of when the hedging premium is largest, candid statement of model limitations.
- **Status**: FULFILLED. The conclusion leads with a policy implication rather than restating results, which is appropriate. The claim that "the hedging premium is largest for moderate singularities" synthesizes Remark 1 (utility saturation kills the premium for extreme $\tilde{g}$) and Remark 2 (abundance makes frictions negligible for extreme $Y$). Both are delivered in Section 4.

### Appendix A: Proofs
- **Contract**: Prove Proposition 2.
- **Deliverables**: Full algebraic proof of the comparative static.
- **Status**: FULFILLED. The proof derives the sign condition step by step.

---

## Cross-Reference Check

| Reference | Target | Resolved? |
|---|---|---|
| Figure 1 (ai-valuations) | Section 1 | Yes |
| Table 1 (numerical-illustration) | Section 3, numerical illustration paragraph | Yes |
| Assumption 1 in Propositions 1-3 | Section 2.2 | Yes |
| Assumption 2 in Propositions 1-3 | Section 2.2 | Yes |
| Assumption 3 in Propositions 1-3 | Section 2.4 | Yes |
| Proposition 2 proof: "See Appendix A" | Appendix A | Yes, proof present |
| Euler equation (7) referenced in Prop 1 proof | Section 2.3, eq. (7) | Yes |
| Introduction previews extension results | Section 4 | Yes, both extinction and frictions covered |

No broken cross-references found.

---

## Claim-Strength Check

1. **"AI stocks command a valuation premium because they hedge against a negative AI singularity"** (Abstract, Introduction). This is the paper's main claim. It is supported by the formal model: Proposition 3 isolates the hedging premium and shows it is strictly positive under the maintained assumptions. The "because" is a model-derived causal claim, not an empirical one, and the paper does not overstate it as empirical. **Appropriate strength.**

2. **"Under natural parameter restrictions"** (Introduction, describing Proposition 2). The condition $\Phi^A(1+V_1) > R/(1-R)$ is characterized as holding for severe displacement, high risk aversion, or large AI share gains. Calling these "natural" is a mild judgment but not overclaimed---these are the economically relevant parameter space for the paper's story. **Appropriate strength.**

3. **"The most extreme AI singularity reduces displacement risk"** (Introduction). Supported by Remark 2 (Coase theorem argument). The paper qualifies this carefully: it requires frictions to have a fixed-cost component. **Appropriate strength.**

4. **"This sectoral asymmetry generates cross-sectional predictions absent from standard disaster models"** (Lit review). The model does generate cross-sectional predictions ($V_0^A > V_0^N$, spread increases with $p$). The claim that these are "absent from standard disaster models" is reasonable given that Rietz/Barro/Wachter are aggregate models. **Appropriate strength.**

5. **"A 1% annual singularity probability generates a hedging premium of about 25% of the complete-markets valuation"** (Numerical illustration). This is a numerical claim about the table. Cannot verify the computation here (that is for the code test), but the verbal claim is stated as illustrative, not as a calibration. **Appropriate strength for an illustration.**

---

## Narrative Consistency Check

The paper tells a coherent, cumulative story:
- Introduction motivates and previews all results.
- Model (Section 2) builds the full environment needed for Section 3.
- Results (Section 3) delivers all three propositions previewed in the introduction.
- Extension (Section 4) delivers both directions previewed in the introduction (extinction, frictions).
- Conclusion synthesizes without introducing new claims unsupported by the body.
- No section relies on deliverables that a prior section promised but did not provide.

No narrative gaps or inconsistencies found.

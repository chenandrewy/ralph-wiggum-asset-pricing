# tests/factcheck-narrative.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 1m 21s
[ralph-garage/agent-logs/20260402T183430.360961-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T183430.360961-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: PASS
REASON: Every section delivers on its stated contract, cross-references are accurate, and no verbal claim exceeds the evidence provided.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: Summarize why AI stocks are expensive; state main mechanism (hedging against negative AI singularity under incomplete markets); state key results (PD ratio increases with singularity probability, complete markets eliminates premium, abundant output enables transfers).
- **Deliverables**: All five claims are present: (1) hedging premium from displacement, (2) incomplete markets as the key friction, (3) PD ratio increasing with singularity probability under sufficient displacement, (4) complete-markets benchmark eliminates premium, (5) abundant output and transfers can eliminate displacement.
- **Status**: FULFILLED. Each claim maps to a specific result in the body (Propositions 1–4, Remarks 1–2).

### Preface (TBC)
- **Contract**: Placeholder section, intentionally blank per spec.
- **Deliverables**: Empty.
- **Status**: FULFILLED. Blank by design (spec §II.11).

### Section 1: Introduction
- **Contract**: Motivate the paper with empirical observation (AI stock valuations), state the main economic mechanism, preview model structure, preview results, preview extension, describe AI-authored production process, and provide a literature review.
- **Deliverables**: (1) Empirical motivation with Figure 1 using CRSP data. (2) Verbal description of hedging channel. (3) Model overview (two assets, representative household, AI owners, singularity as absorbing event). (4) Preview of closed-form PD ratio, comparative statics, complete-markets benchmark. (5) Preview of extension (Jones 2024, extinction, Coase theorem). (6) AI-production paragraph. (7) Literature review paragraph.
- **Status**: FULFILLED. Every previewed result is delivered in later sections. The introduction does not overclaim: it says "we derive," "we show," and "we connect," all of which are borne out.

### Section 2.1: Environment
- **Contract**: Specify the economic environment (time, output, singularity, agents).
- **Deliverables**: Discrete time, output growth process (Eqs. 1–2), singularity as absorbing event with probability p, two agent types (household and AI owners), interpretation of AI owners following GKP (2012).
- **Status**: FULFILLED. All primitives needed for the model are laid out.

### Section 2.2: Assets and Dividends
- **Contract**: Define asset structure and dividend processes.
- **Deliverables**: Three dividend streams (AI, non-AI, private), output shares before and after singularity (Eqs. 3–4), Assumption 1 (negative singularity), Assumption 2 (AI share growth), displacement ratio definition (Eq. 5).
- **Status**: FULFILLED. The section delivers exactly what the title promises.

### Section 2.3: The Household's Problem
- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA preferences (Eq. 6), budget constraint (Eq. 7), market clearing and equilibrium consumption (Eq. 8), Euler equation (Eq. 9).
- **Status**: FULFILLED. The household's problem is fully specified.

### Section 2.4: Equilibrium
- **Contract**: Define the equilibrium concept and state parameter restrictions.
- **Deliverables**: Statement that PD ratios are constant within each regime, Assumption 3 (existence conditions for finite PD ratios), note that these are automatic for γ > 1.
- **Status**: FULFILLED. The section sets up the equilibrium definition needed for Section 3.

### Section 3: Results
- **Contract**: Deliver the paper's main results.
- **Deliverables**: Four propositions with proofs (or appendix references), a numerical illustration.
- **Status**: FULFILLED. See subsections below.

#### Proposition 1 (Price-dividend ratios)
- **Contract**: Derive closed-form PD ratios for AI and non-AI stocks.
- **Deliverables**: Closed-form expressions (Eqs. 10–15), inline proof deriving both from the Euler equation.
- **Status**: FULFILLED. The introduction promises "closed form" and the proposition delivers it with a complete proof.

#### Proposition 2 (AI stocks trade at a premium)
- **Contract**: Show AI stocks have higher PD ratios than non-AI stocks.
- **Deliverables**: Explicit formula for the spread (Eq. 16), proof by subtraction, economic interpretation.
- **Status**: FULFILLED.

#### Proposition 3 (Singularity probability raises AI valuations)
- **Contract**: Show PD ratio of AI stocks is increasing in singularity probability under stated conditions.
- **Deliverables**: Necessary and sufficient condition (Eq. 17), economic interpretation (hedging benefit vs. discount rate effect), proof in Appendix A.
- **Status**: FULFILLED. The verbal claim "if and only if" matches the formal result. The proof is in Appendix A as stated.

#### Proposition 4 (Incomplete vs. complete markets)
- **Contract**: Compare incomplete and complete market valuations and isolate the hedging premium.
- **Deliverables**: Complete-markets PD ratio (Eq. 18), hedging premium formula (Eq. 19), proof showing the Δ^{-γ} term is the sole source of the premium.
- **Status**: FULFILLED. The verbal claim "the hedging premium arises entirely from the displacement channel" is supported by the formula showing Δ^{-γ} − 1 as the only difference.

#### Numerical illustration
- **Contract**: "To gauge magnitudes" — provide illustrative parameterization.
- **Deliverables**: Specific parameter values, computed PD ratios for several values of p, comparison with complete-markets case, Table (Exhibit via \input).
- **Status**: FULFILLED. The illustration is explicitly framed as illustrative ("to gauge magnitudes"), not as a calibration. This matches spec §I.8d (illustrative, not calibration).

### Section 4: Extension: Singularity, Extinction, and Frictions
- **Contract**: Extend the baseline in two directions — extinction risk and overcoming frictions.
- **Deliverables**: Two subsections delivering each extension.
- **Status**: FULFILLED.

#### Section 4.1: Extinction Risk
- **Contract**: Incorporate extinction risk into the model.
- **Deliverables**: Modified PD ratio with extinction probability q (Eq. 20), limiting behavior as q → 1, connection to Jones (2024) on utility curvature, Remark 1 on extreme singularity (ĝ → ∞).
- **Status**: FULFILLED. The section delivers the modified pricing formula and its economic interpretation.

#### Section 4.2: Overcoming Frictions
- **Contract**: Analyze when intergenerational frictions can be overcome, connecting GKP's displacement risk to Jones's singularity analysis.
- **Deliverables**: Generalized displacement ratio with transfer parameter λ (Eq. 21), cost structure for transfers (Eq. 22), limiting argument as Y → ∞, Remark 2 (Coase theorem in the singularity), verbal synthesis connecting GKP and Jones.
- **Status**: FULFILLED. The section promises a "formal analysis" of how transfer mechanisms scale with output, and delivers a model of friction costs with fixed and proportional components, plus the limiting result. The introduction's claim that GKP "do not conduct further analysis" and that "we take up this question" is supported.

### Section 5: Conclusion
- **Contract**: Summarize the paper's contributions.
- **Deliverables**: Summary of hedging premium result, cross-sectional prediction, two channels through which extreme singularities attenuate the premium (utility curvature and Coasean risk-sharing), policy implication (expanding tradeable AI assets).
- **Status**: FULFILLED. Every claim in the conclusion is a restatement of a result proven in the body. The cross-sectional prediction claim is appropriately hedged ("consistent with ... though we emphasize that the model is deliberately stylized").

### Appendix A: Proofs
- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3.
- **Status**: FULFILLED. Proposition 3 is the only result whose proof is deferred to the appendix, and the proof is present.

---

## Cross-Reference Check

| Reference | Location | Target | Verified |
|-----------|----------|--------|----------|
| Figure 1 (ai-valuations) | Section 1 | Figure in Section 1 | Yes — figure is defined with \label{fig:ai-valuations} |
| Table (numerical-illustration) | Section 3 | \input{exhibits/numerical-illustration.tex} | Yes — table is included |
| Assumption 1 (\ref{as:neg-sing}) | Prop 1, Prop 2, Prop 3, Prop 4 | Section 2.2 | Yes |
| Assumption 2 (\ref{as:ai-share}) | Prop 1, Prop 2 proof | Section 2.2 | Yes |
| Assumption 3 (\ref{as:existence}) | Prop 1, Prop 2, Prop 3, Prop 4 | Section 2.4 | Yes |
| Euler equation (\ref{eq:euler}) | Prop 1 proof | Section 2.3, Eq. 9 | Yes |
| Remark 1 (\ref{rem:extreme}) | Conclusion | Section 4.1 | Yes |
| Remark 2 (\ref{rem:coase}) | Conclusion | Section 4.2 | Yes |
| Appendix A (\ref{app:proofs}) | Prop 3 proof | Appendix A | Yes — proof is present |
| "as shown in Section Y" style references | Throughout | N/A | No forward-reference claims of this type found; all references point backward or to labeled environments |

All cross-references point to content that exists at the target location.

---

## Claim-Strength Check

1. **"We show that publicly traded AI stocks command a valuation premium"** (Abstract, Introduction, Conclusion): Supported by Proposition 2, which proves V₀ᴬ > V₀ᴺ under stated assumptions. Claim strength matches evidence.

2. **"The price-dividend ratio of AI stocks increases with the probability of a singularity when displacement is sufficiently severe"** (Abstract): Supported by Proposition 3, which gives a necessary and sufficient condition. The qualifier "when displacement is sufficiently severe" correctly reflects the conditional nature of the result.

3. **"Under complete markets, the hedging premium vanishes"** (Abstract, Conclusion): Supported by Proposition 4, which shows the premium equals zero when Δ = 1.

4. **"Even modest transfers can eliminate displacement risk"** (Abstract): Supported by Remark 2 and the friction-cost analysis in Section 4.2. The word "can" is appropriate — the result is conditional on Y → ∞.

5. **"The valuation spread V₀ᴬ − V₀ᴺ increases with the singularity probability p and with the severity of displacement (1 − Δ)"** (after Proposition 2): The formula in Eq. 16 shows explicit dependence on p (in the numerator) and Δ⁻ᵞ (which increases as Δ falls). Claim is supported.

6. **"This is consistent with the elevated valuations of AI-related firms observed in recent years, though we emphasize that the model is deliberately stylized"** (Conclusion): Appropriately hedged. The model produces a qualitative prediction (AI > non-AI PD ratios) consistent with Figure 1, but the paper does not claim quantitative fit.

7. **"Our contribution relative to GKP is purposefully modest"** (Introduction): The paper builds directly on GKP's framework, adds singularity probability and the extension on frictions. The characterization as modest is accurate.

8. **"GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor ... but do not conduct a formal analysis of how these mechanisms scale with output"** (Section 4.2): This characterizes a claim about an external paper. Based on the paper's own framing and spec §I.6a, this appears accurate, though verification requires reading GKP directly (outside the scope of this test).

No claim was found to be stronger than the evidence provided.

---

## Summary

The paper's narrative is internally consistent and well-aligned across all sections. Every section delivers what its title and opening framing promise. The abstract and introduction claims are each supported by specific results in the body. Cross-references are accurate. Verbal claims are appropriately qualified and matched to the formal results. No unfulfilled contracts or unsupported claims were identified.

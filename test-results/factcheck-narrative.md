# tests/factcheck-narrative.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 2m 11s
[ralph-garage/agent-logs/20260402T180723.876270-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T180723.876270-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative

VERDICT: FAIL
REASON: The Abstract and Introduction make unconditional comparative-statics claims (increasing in p and gamma) that the body establishes only conditionally or not at all.

---

## Section-by-Section Analysis

### Abstract

- **Contract**: Summarize the paper's main results in under 100 words.
- **Deliverables**: States five claims: (1) AI stocks command a hedging premium, (2) PD ratio increases with singularity probability, (3) PD ratio increases with risk aversion, (4) complete markets eliminate the premium, (5) abundant output can eliminate displacement risk.
- **Status**: UNFULFILLED. Claims (1), (4), and (5) are fully supported by the body. Claim (2) is stated unconditionally but Proposition 3 establishes it only under a condition (equation 12). Claim (3)---that the PD ratio increases with risk aversion---is never formally established anywhere in the paper.

### Section 1: Introduction

- **Contract**: Motivate the paper, preview the model and main results, review related literature.
- **Deliverables**: Provides motivation (AI stock valuations), informal model description, preview of four main results, connection to extension, production disclosure, and a literature review.
- **Status**: PARTIALLY UNFULFILLED. The narrative is well-structured and the literature review delivers on its promise. However, the introduction states "The ratio increases with the probability of a singularity" as an unconditional fact; Proposition 3 shows this holds only when condition (12) is satisfied. The introduction does not mention the condition.

### Section 2.1: Environment

- **Contract**: Define the economic environment (time, output, agents).
- **Deliverables**: Discrete time, output growth in normal and singularity states, two agent types, singularity as absorbing event.
- **Status**: FULFILLED.

### Section 2.2: Assets and Dividends

- **Contract**: Define the asset structure and dividend processes.
- **Deliverables**: Three dividend streams with pre- and post-singularity output shares, two assumptions formalizing the negative singularity, and the displacement ratio.
- **Status**: FULFILLED.

### Section 2.3: The Household's Problem

- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA utility, budget constraint, market clearing, equilibrium consumption, Euler equation.
- **Status**: FULFILLED.

### Section 2.4: Equilibrium

- **Contract**: Characterize the equilibrium.
- **Deliverables**: A qualitative statement that PD ratios are constant within each regime, plus Assumption 3 (parameter restrictions for existence).
- **Status**: FULFILLED, but thin. The section title promises "Equilibrium" but the actual equilibrium objects (closed-form PD ratios) are deferred to Section 3. What the section delivers is the setup and existence condition. This is acceptable as a transitional section, since it does describe the equilibrium structure qualitatively, but the title slightly overpromises.

### Section 3: Results

- **Contract**: Present the main results of the model.
- **Deliverables**: Four propositions with proofs, a numerical illustration.
- **Status**: PARTIALLY UNFULFILLED due to two claim-strength issues:

  1. **After Proposition 2** (line 190): "The valuation spread $V_0^A - V_0^N$ increases with the singularity probability $p$, with risk aversion $\gamma$, and with the severity of displacement $(1 - \Delta)$." The claims about $p$ and $1-\Delta$ are clear from equation (10). The claim about $\gamma$ is not proved and is not obviously true: the spread depends on $\Delta^{-\gamma} \cdot (1+\tilde{g})^{1-\gamma} \cdot (1+V_1) / [1-(1-p)R]$, where every factor except $\Delta^{-\gamma}$ moves against the claim as $\gamma$ increases.

  2. **Proposition 4** (lines 211--215): The proposition states that the hedging premium is "increasing in risk aversion $\gamma$." The proof only establishes the formula and its positivity; it does not prove any comparative statics. The dependence on $\gamma$ is complex (it appears in $\Delta^{-\gamma}-1$, $(1+\tilde{g})^{1-\gamma}$, $V_1$, and the denominator $1-(1-p)R$), and the claim is not established.

### Section 4.1: Extinction Risk

- **Contract**: Incorporate extinction risk into the model.
- **Deliverables**: Modified PD formula with extinction probability $q$, discussion of attenuation of hedging premium, Remark 1 on extreme singularity limits, connection to Jones (2024).
- **Status**: FULFILLED.

### Section 4.2: Overcoming Frictions

- **Contract**: Analyze when intergenerational frictions can be overcome (Coase theorem at the singularity).
- **Deliverables**: Transfer mechanism parameterized by $\lambda$, friction cost analysis with fixed and proportional components, Remark 2 on unbounded output eliminating displacement, connection to GKP.
- **Status**: FULFILLED. The section delivers what its title and opening promise: a formal analysis of conditions under which frictions are overcome, building on the GKP observation that transfers would affect displacement.

### Section 5: Conclusion

- **Contract**: Summarize findings and discuss implications.
- **Deliverables**: Summary of hedging premium result, cross-sectional prediction, paradox of extreme singularities, policy suggestion about expanding tradeable AI assets.
- **Status**: FULFILLED. All claims made in the conclusion are supported by results in the body. The conclusion appropriately notes the model is "deliberately stylized."

### Appendix A: Proofs

- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3.
- **Status**: FULFILLED. The proof establishes condition (12) as stated in the proposition.

---

## Cross-Reference Findings

All internal cross-references check out:

- Propositions reference Assumptions 1--3, which are defined in Sections 2.2 and 2.4.
- Proposition 3's proof is deferred to Appendix A, which contains it.
- Equations referenced within proofs (e.g., eq. 7, 8, 9) are present and correctly referenced.
- The extension (Section 4) references GKP and Jones as promised in the introduction.

No broken or misdirected cross-references found.

---

## Claim-Strength Findings

Three claim-strength failures, in decreasing severity:

1. **Abstract and Introduction overstate the $p$ comparative static.** Proposition 3 establishes that $\partial V_0^A / \partial p > 0$ if and only if condition (12) holds. The Abstract and Introduction present this as unconditional ("The price-dividend ratio of AI stocks increases with the probability of a singularity"). The condition is economically natural and likely satisfied in calibrations, but the paper's own result is conditional, and the verbal claims should match.

2. **The $\gamma$ comparative static is claimed but never proved.** The Abstract claims the PD ratio "increases with...risk aversion." Proposition 4 claims the hedging premium is "increasing in risk aversion $\gamma$." The paragraph after Proposition 2 claims the spread is increasing in $\gamma$. None of these are proved. The effect of $\gamma$ on valuations is ambiguous because $\gamma$ appears in multiple factors that move in opposite directions.

3. **Proposition 4's comparative statics are asserted in the proposition statement but the proof only covers the formula derivation.** The proof shows the hedging premium formula and that it is positive. The claims about monotonicity in $\gamma$, $p$, $\tilde{\theta}/\theta$, and $1-\Delta$ are unproved. The $p$, $\tilde{\theta}/\theta$, and $1-\Delta$ claims are straightforward to verify from the formula; the $\gamma$ claim is not.

# tests/factcheck-narrative.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 2m 32s
[ralph-garage/agent-logs/20260402T181745.329310-0400_factcheck-narrative_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T181745.329310-0400_factcheck-narrative_claude_claude-opus-4-6.log)

# factcheck-narrative
VERDICT: FAIL
REASON: Introduction unconditionally claims non-AI stock valuations fall with singularity probability, but the body provides no supporting result and the analogous condition from Proposition 3 shows this is parameter-dependent.

---

## Section-by-Section Analysis

### Abstract
- **Contract**: Summarize the paper's main claims: AI stocks command a hedging premium under incomplete markets; PD ratio rises with singularity probability when displacement is severe; complete markets eliminate the premium; abundant output enables transfers that eliminate displacement risk.
- **Deliverables**: All claims are present.
- **Status**: FULFILLED. Every claim maps to a specific result in the body (Propositions 1--4, Remarks 1--2). See Abstract/Introduction alignment section below for details.

### Preface (TBC) (unnumbered)
- **Contract**: Placeholder section, intentionally blank per spec.
- **Deliverables**: Blank.
- **Status**: FULFILLED.

### Section 1: Introduction
- **Contract**: Motivate the research question (why are AI stocks expensive?), preview the model and main results, situate within the literature.
- **Deliverables**: Motivation via AI valuations, informal model description, preview of four main results (closed-form PD ratio, comparative static in p, complete-markets benchmark, extension on frictions), self-referential paragraph on AI authorship, half-page lit review.
- **Status**: UNFULFILLED. The section states: "For non-AI stocks, the effect reverses---their valuations fall with singularity probability." This is presented as an unconditional claim. The body never establishes this result. Proposition 3 shows that AI stock valuations rise with p only under a specific condition (eq. 16). The analogous condition for non-AI stocks would require $\Phi^N(1+V_1) < R/(1-R)$, which is not guaranteed by Assumptions 1--3. Because $\Delta^{-\gamma}$ can be large, $\Phi^N(1+V_1)$ could exceed $R/(1-R)$ even though $\tilde{\nu}/\nu < 1$, meaning non-AI valuations could *rise* with p under some parameterizations. The Introduction's unconditional language ("the effect reverses") overstates what the model delivers.

### Section 2.1: Environment
- **Contract**: Define the economic environment (agents, timing, output dynamics, singularity).
- **Deliverables**: Discrete time, deterministic output growth, singularity as absorbing event with probability p, two agent types (household, AI owners), post-singularity growth rate.
- **Status**: FULFILLED. All elements of the environment are clearly specified.

### Section 2.2: Assets and Dividends
- **Contract**: Define the asset structure and dividend processes.
- **Deliverables**: Three dividend streams (public AI, non-AI, private AI) with output shares, permanent share shift at singularity, Assumptions 1--2, displacement ratio $\Delta$.
- **Status**: FULFILLED. The section delivers exactly what the title promises.

### Section 2.3: The Household's Problem
- **Contract**: Specify the household's optimization problem.
- **Deliverables**: CRRA preferences, budget constraint, market clearing, equilibrium consumption, Euler equation.
- **Status**: FULFILLED. The section fully specifies the problem and derives equilibrium consumption from market clearing.

### Section 2.4: Equilibrium
- **Contract**: Title promises an equilibrium characterization.
- **Deliverables**: States that PD ratios are constant in each regime (because growth rates are i.i.d.), imposes Assumption 3 (parameter restrictions for finite PD ratios).
- **Status**: FULFILLED, but borderline. The section establishes that a stationary equilibrium exists and states its qualitative form (constant PD ratios), but the actual solution is deferred to Section 3. This is a common convention in theory papers---the "Equilibrium" subsection defines the equilibrium concept and existence conditions, while "Results" solves for the objects of interest. No content is missing; it is simply organized across two sections.

### Section 3: Results
- **Contract**: Present the main results of the model.
- **Deliverables**: Proposition 1 (closed-form PD ratios for AI and non-AI stocks), Proposition 2 (AI stocks trade at a premium), Proposition 3 (comparative static: AI PD ratio increases in p under a condition), Proposition 4 (complete vs. incomplete markets, hedging premium), numerical illustration.
- **Status**: FULFILLED. Each proposition is stated and proved (Prop 3's proof is in Appendix A, as referenced). The numerical illustration is appropriately labeled as illustrative, not a calibration.

#### Sub-check: Verbal claims after Proposition 2
The paper states: "The valuation spread $V_0^A - V_0^N$ increases with the singularity probability $p$ and with the severity of displacement $(1-\Delta)$." This follows directly from equation (13): the numerator is proportional to $p$ and $\Delta^{-\gamma}$, and the denominator $1-(1-p)R$ is decreasing in $p$, so both effects reinforce. Claim is proportionate to evidence.

#### Sub-check: Verbal claims after Proposition 3
The paper states the condition "holds when displacement is sufficiently severe ($\Delta$ small), risk aversion is sufficiently high ($\gamma$ large), or the AI share gain is sufficiently large ($\tilde{\theta}/\theta$ large)." These are informal comparative statics on the condition $\Phi^A(1+V_1) > R/(1-R)$. For $\Delta$ small and $\tilde{\theta}/\theta$ large, the claims follow directly from the formula. For $\gamma$ large, both $\Delta^{-\gamma} \to \infty$ and $(1+\tilde{g})^{1-\gamma} \to 0$, but $R/(1-R) \to 0$ as well; the claim holds in the limit but the reasoning is not trivial. Acceptable as informal guidance.

### Section 4.1: Extinction Risk
- **Contract**: Incorporate the possibility that the singularity destroys the economy.
- **Deliverables**: Modified PD formula with extinction probability $q$ (eq. 19), discussion of attenuation, Remark 1 on the extreme singularity limit ($\tilde{g} \to \infty$).
- **Status**: FULFILLED. The section delivers a formal extension and connects to Jones (2024) on utility curvature and infinite consumption.

### Section 4.2: Overcoming Frictions: The Coase Theorem in the Singularity
- **Contract**: Analyze when the frictions sustaining displacement risk can be overcome.
- **Deliverables**: Parameterized displacement ratio $\Delta(\lambda)$, friction cost analysis (eq. 21), Remark 2 on unbounded output eliminating displacement risk.
- **Status**: FULFILLED. The section delivers a formal analysis of how transfer mechanisms interact with output levels, explicitly connecting GKP's displacement framework to Jones's singularity analysis. This fulfills the paper spec's requirement (I.6.a) for formal analysis of GKP's displacement factor.

### Section 5: Conclusion
- **Contract**: Summarize findings and discuss implications.
- **Deliverables**: Summary of main results, cross-sectional prediction, paradox of extreme singularities, policy implication about expanding tradeable AI assets.
- **Status**: FULFILLED. All claims restate results established in the body. The cross-sectional prediction (AI stocks at higher PD ratios) is supported by Proposition 2. The claim about "the spread increasing in perceived singularity risk" follows from equation (13). The statement about financial market solutions is appropriately framed as a suggestion, not a formal result.

### Appendix A: Proofs
- **Contract**: Provide deferred proofs.
- **Deliverables**: Proof of Proposition 3.
- **Status**: FULFILLED. The proof is complete and corresponds to the reference in the main text.

---

## Cross-Reference Check

| Reference | Source | Target | Status |
|-----------|--------|--------|--------|
| "See Appendix A" | Prop 3 proof (Section 3) | Appendix A | **OK** --- Appendix contains the proof |
| Assumptions 1--3 in Propositions | Sections 3, 4 | Section 2 | **OK** --- All assumptions are defined in Section 2 |
| Euler equation (7) in Prop 1 proof | Section 3 | Eq. (7) in Section 2.3 | **OK** |
| "as GKP note" in Section 4.2 | Section 4.2 | GKP (2012) | **OK** --- Accurately represents GKP's discussion per spec |
| "Following Jones (2024)" in Remark 2 | Section 4.2 | Jones (2024) | **OK** --- Consistent with the extension's framing |

No broken cross-references found.

---

## Claim-Strength Findings

1. **FAIL: Non-AI valuations fall with p (Introduction).** The Introduction states: "For non-AI stocks, the effect reverses---their valuations fall with singularity probability." This is an unconditional claim. The body provides the non-AI PD formula (Proposition 1, eq. 10) but never analyzes $\partial V_0^N / \partial p$. By analogy with Proposition 3, this derivative is negative if and only if $\Phi^N(1+V_1) < R/(1-R)$. Since $\tilde{\nu}/\nu < 1$ makes $\Phi^N$ smaller than $\Phi^A$, this condition is *more likely* to hold---but it is not guaranteed by the assumptions. The claim should be qualified (e.g., "under analogous conditions") or proved.

2. **OK: Hedging premium increases with p (Conclusion).** From eq. (14), the hedging premium $V_0^A - V_0^{A,\text{CM}}$ has $p$ in the numerator and $(1-p)$ in the denominator, so it is unambiguously increasing in $p$.

3. **OK: "Even modest transfer mechanisms suffice" (Abstract, Conclusion).** Remark 2 and the surrounding analysis show that as $Y \to \infty$, fixed friction costs vanish relative to output. The language "even modest" is appropriate for the limiting result.

4. **OK: Numerical illustration framing.** The paper calls it a "numerical illustration" and a "parameterization," never a "calibration." This matches the actual content (plugging in numbers to gauge magnitudes).

---

## Narrative Consistency

The paper tells a coherent four-part story: (1) set up the model with incomplete markets and displacement, (2) derive the hedging premium in closed form, (3) show it vanishes under complete markets, (4) explore when frictions can be overcome. Each section builds on the previous one without gaps. The extension (Section 4) genuinely extends the baseline rather than repeating it.

The one narrative inconsistency is the Introduction's unqualified claim about non-AI stocks, which creates an expectation the body does not fulfill.

---

## Abstract/Introduction Alignment

| Abstract/Intro Claim | Body Support | Status |
|-----------------------|-------------|--------|
| AI stocks command a valuation premium as hedge | Prop 2, Prop 4 | **Supported** |
| PD ratio increases with p when displacement severe | Prop 3 | **Supported** |
| Under complete markets, hedging premium vanishes | Prop 4 (eq. 14) | **Supported** |
| Modest transfers eliminate displacement risk when output abundant | Remark 2, Section 4.2 | **Supported** |
| Non-AI valuations fall with singularity probability | No formal result | **Unsupported as stated** |

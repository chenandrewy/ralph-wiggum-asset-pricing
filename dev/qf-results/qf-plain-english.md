# dev/qf/qf-plain-english.py
Started: 2026-03-28 14:44:57 EDT
Runtime: 2m 56s
[ralph-garage/agent-logs/20260328T144457.275016-0400_qf-plain-english_claude_opus.log](../../ralph-garage/agent-logs/20260328T144457.275016-0400_qf-plain-english_claude_opus.log)

# qf-plain-english
VERDICT: FAIL
REASON: Section 4 contains compressible formalism that could be replaced by plain English without weakening the paper's economic claims.

## Findings

I examined every displayed equation, proposition, corollary, and remark. The core model (Sections 2-3) is well-disciplined. The compressible objects cluster in the extension (Section 4).

### Compressible formalism

**1. Equation (12): Extinction Euler equation**

The paper displays $E[m_{t+1} \cdot (D_{t+1}^{AI}/D_t^{AI}) \mid \text{extinction}] \cdot \Pr(\text{extinction}) = 0$ and devotes a full paragraph to explaining it, including "This is the standard measure-theoretic fact that $0 \cdot X = 0$ a.s." This is a displayed equation for a trivial identity. The economic content is: *In the extinction state, AI stocks pay nothing, so extinction states contribute nothing to the price-dividend ratio.* That sentence carries the same information. The equation is not referenced by any later derivation — the paper proceeds directly to Eq (13), which stands on its own.

**2. Corollary 2: Two-type marginal investors**

Corollary 2 states that the hedging premium is larger when retail investors (lower $\phi$) are marginal. This is an immediate consequence of two facts already established: $\Delta$ is decreasing in $\phi$ (noted in Corollary 1's proof) and $\pi^{AI}$ is increasing in $\Delta$ (Proposition 1). The formal corollary, displayed inequality (Eq 15), and proof add weight to a point that is a one-sentence application of existing comparative statics: *Investors with less access to private AI capital face larger displacement and value the hedge more.* No subsequent result depends on Corollary 2 as a formal object.

**3. Equation (17): Logistic transition function**

The paper introduces $\phi(a) = \phi_0 + (1 - \phi_0)/(1 + e^{-\lambda(a - \bar{a})})$ as "a natural parametric example." The proof of Corollary 3 explicitly disclaims needing it: "The proof uses only the limit $\phi(a) \to 1$ and monotonicity, not the specific functional form." The logistic form is not calibrated, not used in any table, and not referenced again. Plain English — *a smooth S-shaped transition from $\phi_0$ to 1, triggered around some threshold surge* — conveys the same content without the displayed formula.

**4. Equation (14): Value-of-a-statistical-life formula**

The VSL formula $v(\tilde{c}) = \bar{u}\,\tilde{c}^{\gamma-1} + 1/(1-\gamma)$ is imported from Jones (2024) and used solely to motivate the calibration $v \approx 6$, hence $\delta \approx 0.017$. The paper could state: *Following Jones (2024), the value of a life-year under CRRA utility is approximately six times per capita consumption, implying an annual extinction hazard of about 1.7%.* No result depends on the formula's specific form.

**5. Proposition 1(iii) parenthetical condition**

The sufficient condition $p \, e^{\gamma\Delta + a}(\Delta - \mu + (\gamma-1)\sigma^2) > (1-p)(\mu - (\gamma-1)\sigma^2)$ is opaque and never interpreted, calibrated, or referenced later. The plain-English qualifier already present — "provided $\Delta$ is large enough that the singularity contribution dominates" — communicates the economic content fully.

### Objects examined but not flagged

- **Eqs (1)-(4), (8):** Standard primitives essential for notation and model setup.
- **Eqs (5)-(7) ($\Delta$ definition and negative-singularity condition):** Central economic objects. The formula for $\Delta$ is compact, directly used in every result, and the ratio condition $d/a > \phi s/(1-s)$ adds quantitative content beyond its verbal paraphrase.
- **Eqs (9)-(10), (13) (pricing kernels):** Quantitative engine of the paper. Essential.
- **Propositions 1-3:** Core results. The formal statements carry content that plain English would lose, especially the precise conditions for comparative statics.
- **Corollary 1 (cross-section):** Generates a testable prediction under a precise identifying assumption. Formalism earns its keep.
- **Corollary 3 (non-monotonicity):** Qualitative result whose proof requires the formal apparatus.

### Assessment

**Requirement 1 (no dead-weight formalism):** Borderline satisfied. Eq (17) comes closest to dead-weight — it is explicitly disclaimed by the proof it accompanies and serves no quantitative or analytical role. The others support real economic points, just more formally than necessary.

**Requirement 2 (no formalism replaceable by plain English):** Not satisfied. Eqs (12), (14), (17), Corollary 2, and the Prop 1(iii) parenthetical could each be replaced by one or two sentences of plain English without weakening any economic claim. These are not isolated: they cluster in Section 4 and share a common pattern of formalizing points that the surrounding prose already communicates.

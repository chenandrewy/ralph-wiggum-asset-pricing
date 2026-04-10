# tests/theory-deadweight.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 2m 12s
[ralph-garage/agent-logs/20260409T194838.517512-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.517512-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: FAIL
REASON: Extension 1 introduces formal parameters and an equation that are never used quantitatively; the proof is entirely qualitative, making the apparatus ceremonial.

## Audit methodology

Every formal object (equation, proposition, corollary, remark, parameter, notation) was checked against three criteria: (1) Is it used in a result, calibration, figure, or interpretation that matters for the paper's conclusions? (2) Could its takeaway be stated in plain English without weakening economic claims? (3) Does it add genuine precision or is it ceremonial?

## Findings

### Baseline model and quantitative analysis (Sections 2--3): CLEAN

The baseline model is lean and well-constructed. Every parameter ($\beta$, $g$, $\gamma$, $\phi$, $\eta$, $p$, $\xi$, $\theta$, $\Delta\theta$) appears in the P/D formulas, is calibrated in Table 1, and drives at least one comparative static or quantitative result. The $\Gamma^{AI}$, $\Gamma^N$ notation compresses the formulas and highlights the economic comparison. Proposition 1 delivers closed-form prices; Proposition 2 delivers comparative statics that are directly referenced in the quantitative discussion; Remark 1 (existence condition) is load-bearing in Extension 2. Corollary 1 is trivial (one logical step from Proposition 1) but acceptably names the key qualitative result.

### Extension 2 (Section 4.2): CLEAN

Equations (7) and (8) do genuine economic work. The transfer-ratio equation (8) delivers the key insight that the consumption gain is independent of $\eta$, which is the paper's main policy result. Parameters $\tau$ and $\delta_0$ are calibrated and appear in the figure. The connection to the existence condition (Remark 1) is well-motivated.

### Extension 1 (Section 4.1): PROBLEMS FOUND

Extension 1 introduces three new parameters ($\lambda$, $\phi^+$, $\kappa$) and a formal equation (6) to state Proposition 3. The problems:

**1. $\kappa$ (veto cost) is introduced and then dominated.** The proof of Proposition 3(i) says "for $\gamma$ sufficiently large, $\Delta U^H < -\kappa$." This means $\kappa$ exists only to be exceeded. It is never calibrated, never appears in any figure or table, and plays no role in any quantitative or qualitative result beyond being the threshold that risk aversion overwhelms. Replacing $\kappa$ with a plain-English phrase ("even at a substantial cost of blocking development") would lose nothing. This is a parameter introduced for apparent rigor that does no economic work.

**2. $\phi^+$ (positive displacement factor) is unused beyond its definition.** It appears in the itemized setup and inside equation (6), but is never calibrated, never appears in any figure, and the proof of Proposition 3 never manipulates it algebraically---it simply notes that "$\phi^+ > 1$, but $u$ is concave." The qualitative point is just "the household's share increases in the positive singularity." Naming a parameter for this adds formalism without precision.

**3. Equation (6) ($\Delta U^H$) is ceremonial.** The equation precisely defines the household's expected utility gain from allowing AI development. But the proof of Proposition 3 never manipulates this expression---both parts (i) and (ii) are proved with purely qualitative arguments about concavity, risk aversion, and the social surplus. The equation creates the appearance of analytical precision for what is fundamentally a verbal argument. Compare this to Proposition 1, where the closed-form expressions are actually solved, calibrated, and plotted.

**4. $\lambda$ is borderline.** It states the condition $\lambda > 1/2$ (positive singularity is more likely), which is economically meaningful. But like the other Extension 1 parameters, it is never calibrated or used in any quantitative result.

**In aggregate**: Extension 1 has the formal structure of a quantitative result (parameters, equation, proposition) but the substance of a qualitative remark. The entire economic content of Proposition 3 can be stated in plain English: "If the positive singularity is more likely than the negative one, AI development is socially efficient. But a risk-averse household that cannot hedge displacement may rationally block it. Complete markets would eliminate this distortion." No equation or named parameter is needed to make this argument, and the proof confirms this by never using them analytically.

### Summary of deadweight

| Object | Status | Reason |
|--------|--------|--------|
| $\kappa$ | Deadweight | Introduced only to be dominated; never calibrated or reused |
| $\phi^+$ | Deadweight | Named parameter for a qualitative point; never calibrated |
| Eq. (6) $\Delta U^H$ | Ceremonial | Never manipulated; proof is qualitative |
| $\lambda$ | Borderline | States a meaningful condition but is never calibrated |
| All baseline/Ext. 2 formalism | Clean | Every object is used in pricing, calibration, or figures |

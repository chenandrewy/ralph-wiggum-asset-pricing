# tests/theory-deadweight.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 2m 48s
[ralph-garage/agent-logs/20260414T102326.840455-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.840455-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object earns its place through use in a result, calibration, figure, or cross-reference; no abandoned, ceremonial, or purely decorative formalism found.

## Audit Method

Cataloged every formal object (parameters, equations, propositions, remarks, derived quantities) and traced each to its downstream use in results, calibrations, figures, or narrative claims.

## Parameters

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $g$ | Eq. (1) | P/D formulas, calibration, all proofs |
| $\beta$ | Eq. (4) | P/D formulas, calibration |
| $\gamma$ | Eq. (4) | P/D formulas, veto threshold, calibration |
| $p$ | Singularity setup | P/D formulas, calibration, table grid axis |
| $\xi$ | Singularity setup | Prop. 2, calibration, table grid axis |
| $\eta$ | Singularity setup | P/D formulas, calibration, transfer analysis, figure |
| $\phi$ | Eq. (2) | P/D formulas, veto proof, $\phi_\text{eff}$, calibration |
| $\theta$, $\Delta\theta$ | Eq. (3) | $\Gamma^{AI}$, $\Gamma^{N}$, calibration |
| $\alpha$ | Consumption split | Veto proof, transfer equation, $\phi_\text{eff}$, calibration |
| $q$ | Extension 1 | Prop. 3 proof ($\Delta u$), numerical example |
| $\kappa$ | Extension 1 | Prop. 3, numerical example |
| $\tau$ | Extension 2 | Transfer equation, $\phi_\text{eff}$, figure axes |
| $\delta$ | Extension 2 | Transfer equation, robustness exercise, figure |

No parameter is introduced and then unused. Every parameter enters at least one result, calibration value, or figure.

## Equations

1. **Eq. (1)**: $C_{t+1} = (1+g)C_t$. Could be stated in words, but it is one line, sets up notation used in every subsequent derivation, and is standard in theory papers. Not deadweight.

2. **Eq. (2)**: $\alpha_{t+1} = \phi\alpha_t$. Central displacement mechanism. Used in every proposition and extension.

3. **Eq. (3)**: $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$. Drives $\Gamma^{AI} \neq \Gamma^{N}$, which is the core of the valuation spread. Explicitly referenced in the text as "the expression that drives $\Gamma^{AI} \neq \Gamma^{N}$."

4. **Eq. (4)**: CRRA utility. Standard; properties used directly in the veto proof ($\gamma \to \infty$ limit) and in the SDF derivation.

5. **Eqs. (5)-(6)**: P/D ratios. Core result (Proposition 1).

6. **Eq. (7)**: Existence condition $A^j < 1$. Cross-referenced in Extension 2 where infinite prices emerge at $\tau = 0$ under large singularity; also referenced in the figure caption. Does real narrative and analytical work.

7. **Eq. (8)**: $\Delta u(\gamma)$. Used in the proof of Proposition 3. Integral to the argument.

8. **Eq. (9)**: Transfer consumption $c^H_{post}$. Central to Extension 2; generates $\phi_\text{eff}$ and the figure.

9. **Eq. (10)**: $\phi_\text{eff}$. Connects transfers back to the baseline P/D formula, allowing reuse of Proposition 1. Economizes on formalism rather than adding to it.

10. **Eq. (11)**: Transfer ratio. The closest candidate for deadweight — the $\eta$-independence of the proportional gain is a secondary observation, and the paper immediately says "the economic content is in the levels." However, the equation does meaningful work: it establishes that transfers always help ($ratio > 1$ whenever $\delta\tau < 1$), quantifies the robustness exercise ($\delta = 0.9$ yields a $3.5\times$ multiple), and provides the clean decomposition between proportional and level effects. One equation; earns its place.

## Propositions and Remarks

- **Proposition 1 (P/D ratios)**: Core result. Used in quantitative section, extensions.
- **Remark 1 (existence condition)**: Motivates Extension 2 (infinite $\to$ finite prices via transfers). Cross-referenced in figure caption and discussion. Does real work.
- **Proposition 2 (extinction attenuation)**: Clean one-line comparative static with a short proof. Referenced in the quantitative section ("as Proposition 2 predicts"). Adds rigor to a claim that might otherwise seem hand-wavy.
- **Proposition 3 (veto)**: Core extension result. Two parts, both doing distinct work (incomplete vs. complete markets).

## Derived Quantities

- $\Gamma^{AI}$, $\Gamma^{N}$: Used in Propositions 1-2, calibration, discussion. Essential shorthand.
- $A^j$: Used in Remark 1 and Extension 2. Does real cross-referencing work.
- $\phi_\text{eff}$: Bridges extensions to baseline formula. Economizes on formalism.
- $\alpha^+ = \min(1, \alpha/\phi)$: Used in Proposition 3 proof. Technical but necessary to keep shares in $[0,1]$.

## Distinction Between $\alpha_t$ and $\theta_t$

Both are needed and do distinct work. $\alpha_t$ governs the household's consumption share (enters the SDF), $\theta_t$ governs the dividend split among public assets (enters dividend growth factors). The paper explicitly explains why they differ (line 114) and the distinction matters in Extension 2, where transfers are levied on the consumption allocation ($\alpha$), not on public dividends ($\theta$).

## Could Any Formal Object Be Replaced by Plain English?

Every proposition makes a precise claim that plain English would weaken. "The valuation spread is decreasing in $\xi$" (Prop. 2) is tighter than "extinction risk reduces the premium" — the latter could mean many things. The P/D formulas (Prop. 1) are the paper's core contribution and cannot be stated in words. The veto result (Prop. 3) requires the formal threshold $\bar{\gamma}$ to make a precise prediction. The transfer equation (Eq. 9) and $\phi_\text{eff}$ (Eq. 10) are needed for the figure and the robustness exercise.

## Conclusion

The paper's formalism is lean for an asset pricing theory paper targeting a top finance journal. Every parameter, equation, proposition, and derived quantity is used in at least one result, calibration, figure, or cross-reference. No formal object is introduced and abandoned, no auxiliary detour fails to connect to the main argument, and no object's qualitative takeaway could be stated in plain English without weakening the paper's economic claims.

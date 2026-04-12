# tests/theory-deadweight.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 2m 53s
[ralph-garage/agent-logs/20260411T211526.521041-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.521041-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and mechanism does meaningful economic or narrative work; no deadweight formalism found.

## Audit Method

Traced every parameter, variable, equation, proposition, and remark through the paper to determine whether it (1) appears in a result, calibration, figure, or interpretation that matters for the paper's conclusions, and (2) could be replaced by plain English without weakening the economic claims.

## Parameter Inventory

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $\beta$ | Setup (preferences) | P/D formulas (Prop 1), calibration ($\beta=0.96$) |
| $g$ | Setup (consumption growth) | P/D formulas, calibration ($g=0.02$) |
| $\gamma$ | Setup (preferences) | P/D formulas, SDF, veto threshold (Prop 3), calibration ($\gamma=4$, $\gamma=10$) |
| $C_t$ | Setup (aggregate consumption) | Dividends, utility, transfers |
| $\alpha_t$ | Setup (household share) | Displacement, veto, transfers, calibration ($\alpha=0.70$) |
| $p$ | Setup (singularity prob) | P/D formulas, Table 2 grid, veto numerical example |
| $\xi$ | Setup (extinction prob) | P/D formulas, Prop 2 (attenuation), Table 2 grid |
| $\phi$ | Setup (displacement) | P/D formulas, veto, transfers, calibration ($\phi=0.5$, $\phi=0.05$) |
| $\eta$ | Setup (productivity boost) | P/D formulas, transfers, calibration ($\eta=0.5$, $\eta=9$) |
| $\theta_t$ | Setup (AI dividend share) | $\Gamma$ factors, P/D formulas, calibration ($\theta=0.15$) |
| $\Delta\theta$ | Setup (AI share jump) | $\Gamma$ factors, calibration ($\Delta\theta=0.2$) |
| $q$ | Extension 1 (positive sing. prob) | Veto proof (eq. 7), numerical example ($q=0.70$) |
| $\kappa$ | Extension 1 (veto cost) | Prop 3 statement and proof, numerical example ($\kappa=1\%$) |
| $\tau$ | Extension 2 (tax rate) | Transfer consumption, $\phi_\text{eff}$, Figure 3 |
| $\delta$ | Extension 2 (deadweight cost) | Transfer consumption, $\phi_\text{eff}$, calibration ($\delta=0.5$) |
| $\phi_\text{eff}$ | Extension 2 | Links transfers to Prop 1 pricing formula |

**No unused parameters.** Every parameter appears in at least one proposition, calibration, or figure.

## Formal Objects

**Proposition 1 (P/D ratios):** Central pricing result. Generates Table 2 and anchors quantitative analysis. Essential.

**Proposition 2 (Extinction attenuation):** Comparative static used to interpret Table 2 patterns. Referenced in quantitative section ("as Proposition 2 predicts"). Inline proof is moderately involved but the result is not obvious from inspection of the P/D formula (requires a convexity argument on $A/(1-A)$). Does real work.

**Proposition 3 (Veto):** Core result of Extension 1. Connects market incompleteness to real distortions in AI development. Supported by numerical example. Essential for the paper's three-part contribution.

**Remark 1 (Existence condition):** Forward-referenced in Extension 2 (infinite P/D at low $\tau$) and Discussion (Section 2.3). The existence condition is central to the left panel of Figure 3, where transfers restore finite prices. Does real work.

**$\Gamma^{AI}$ and $\Gamma^{N}$ (dividend growth factors):** Compact notation that enables the key comparison ($\Gamma^{AI} > \Gamma^{N}$) driving the hedging channel. Used in Prop 1, Prop 2, and prose interpretation. Essential.

**Equation (9) (transfer ratio):** Shows the consumption ratio is independent of $\eta$, making the specific point that transfers always improve the household's position. The text then pivots to levels, which is where the singularity growth matters. The equation efficiently makes a distinct claim and is not redundant.

## Potential Concerns Examined and Dismissed

**Kaldor-Hicks efficiency label (Extension 1):** The paper defines social efficiency in the Kaldor-Hicks sense, with condition $(1+\eta) > 1$, which is trivially satisfied since $\eta > 0$. This is the most "ceremonial" element in the paper. However, it does narrative work: Proposition 3 states the household vetoes "even when development is socially efficient," and the Kaldor-Hicks label makes this tension precise. Without it, the result reads as "household vetoes even though output goes up," which is less striking. The label is standard economics shorthand, not pompous formalism.

**AI owners as passive agents:** AI owners receive $(1-\alpha_t)C_t$ and never optimize. They are the minimal device needed to make the consumption split coherent and to define the transfer base in Extension 2. Not a formal detour.

**Utility function (eq. 3):** Standard statement of CRRA preferences. The SDF, veto proof, and extinction normalization all derive from this. Necessary.

**Aggregate consumption growth (eq. 1):** One-line equation defining $C_{t+1} = (1+g)C_t$. Standard and used throughout.

## Conclusion

The paper is lean. Every formal object either (a) generates a quantitative result used in a table or figure, (b) establishes a comparative static referenced in interpretation, or (c) provides necessary scaffolding for the model's economic mechanism. No formalism is introduced and abandoned, no variable goes unused, and no auxiliary detour fails to advance the argument.

# tests/theory-deadweight.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260412T201203.496362-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.496362-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation does meaningful economic or narrative work; no deadweight formalism found.

## Audit methodology

Catalogued every formal object (parameters, variables, equations, propositions, remarks) and traced each one forward to check whether it contributes to (a) a proposition or proof, (b) calibration or quantitative analysis, (c) a figure, or (d) economic interpretation that advances the paper's argument.

## Parameters and variables

| Symbol | Introduced | Used in |
|--------|-----------|---------|
| $C_t$, $g$ | Setup (Eq 1) | All pricing equations, calibration, transfer analysis |
| $\alpha_t$, $\phi$ | Displacement (Eq 2) | Central to all three propositions, calibration, both extensions |
| $p$, $\xi$, $\eta$ | Singularity setup | All propositions, Table 1, Figure 2 |
| $\theta_t$, $\Delta\theta$ | Asset definitions | $\Gamma^{AI}$, $\Gamma^{N}$ in Prop 1; calibration; numerically exact backward recursion |
| $\gamma$, $\beta$ | Preferences (Eq 3) | Pricing (Prop 1), extinction attenuation (Prop 2), veto threshold (Prop 3), calibration |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | Core of hedging channel explanation; Prop 2 proof; comparison drives all economic content |
| $q$, $\kappa$ | Extension 1 | Prop 3 (both parts), numerical example |
| $\tau$, $\delta$, $\phi_\text{eff}$ | Extension 2 | Transfer consumption (Eq 9), effective displacement (Eq 10), Figure 2, robustness discussion |

No parameter is introduced and then unused. Every variable feeds into at least one result, calibration, or figure.

## Formal objects

**Proposition 1 (P/D ratios):** Core result. Delivers the hedging channel through the comparison of $\Gamma^{AI}$ vs $\Gamma^{N}$, produces the closed-form expressions used in calibration (Table 1) and extended in both extensions. Essential.

**Remark 1 (Existence condition):** Defines $A^j < 1$ condition. Referenced in Extension 2 and the figure discussion (P/D undefined at low tax rates under extreme displacement). Does real work connecting the baseline model to the transfers extension.

**Proposition 2 (Extinction attenuation):** Key comparative static linking to Jones (2024). Verified quantitatively in Table 1. The proof is detailed (semi-elasticity argument, $A^j > 1/2$ condition), but the paper spec requires all propositions to be explicitly proved (Style Req 9). The proof's content is substantive, not ceremonial.

**Proposition 3 (Veto):** Establishes that market incompleteness distorts real decisions, not just prices. Both parts (incomplete vs complete markets) are used, and a numerical example sharpens the quantitative intuition. Central to the paper's argument about AI development distortions.

**Equations 9-11 (Transfer analysis):** Eq 9 defines post-transfer consumption, Eq 10 derives the effective displacement parameter (used to connect back to Prop 1's pricing formula), Eq 11 shows the transfer ratio is independent of $\eta$ (key economic insight for the "explosive growth overwhelms deadweight costs" argument). All three do distinct work.

## Potential concerns examined and dismissed

1. **Kaldor-Hicks efficiency definition:** Brief, defines "socially efficient" before Prop 3 uses it. The condition $(1+\eta) > 1$ is trivially satisfied, but the sentence is definitional rather than formal — it clarifies terminology for the reader in one line.

2. **AI owners' consumption $(1-\alpha_t)C_t$:** Mentioned in setup but AI owners never optimize. This is correct: they are not the marginal investor, so their preferences are irrelevant to pricing. Stating their consumption share is necessary to define the economic environment and the transfer base in Extension 2.

3. **Equation 1 ($C_{t+1} = (1+g)C_t$):** Trivially simple, but numbered display equations are required by spec (Style Req 8), and it establishes notation used in every subsequent derivation.

4. **Proof of Proposition 2:** Lengthy relative to the intuitive result, but required by spec. The proof is substantive (the semi-elasticity argument is non-obvious and the $A^j > 1/2$ condition is necessary for the proportional-decline claim).

5. **$\alpha^+$, $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$:** All appear only in Extension 1 and its proof/numerical example. Each is used where introduced.

## Conclusion

The paper maintains tight formalism-to-content discipline. Every formal object advances the economic argument — either through a proposition, calibration, figure, or economic interpretation. No variables, parameters, or formal detours are introduced and then abandoned. No formalism is ceremonial or could be replaced by plain English without weakening the paper's claims.

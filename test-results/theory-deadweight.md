# tests/theory-deadweight.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 2m 19s
[ralph-garage/agent-logs/20260409T212047.312680-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.312680-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation does identifiable economic or narrative work; no abandoned formalism, ceremonial detours, or unused variables found.

## Audit methodology

Every formal object (equations, propositions, remarks), every parameter/variable, and every prose mechanism was checked against two criteria: (1) does it appear in a result, calibration, or interpretation that matters for the paper's conclusions? (2) could its qualitative takeaway be stated in plain English without weakening the paper's economic claims?

## Parameters and variables

| Symbol | Introduced | Used in |
|--------|-----------|---------|
| $C_t$, $g$ | Eq (1) | P/D formulas (Prop 1), calibration (Table 1), Extension 2 |
| $\alpha_t$ | Setup | Extension 2 (Eqs 7–8), figure parameterization ($\alpha = 0.70$) |
| $p$ | Singularity setup | P/D formulas, calibration grid, Prop 2(ii), figure params |
| $\xi$ | Extinction setup | P/D formulas, calibration grid, Prop 2(iii), figure params |
| $\eta$ | Singularity setup | P/D formulas, calibration, Eq (8) independence result, Extension 2 |
| $\phi$ | Eq (2) | P/D formulas, Prop 2(i), calibration, Extension 2 ($\phi_\text{eff}$) |
| $\theta_t$, $\Delta\theta$ | Asset setup | $\Gamma^{AI}$, $\Gamma^{N}$ in Prop 1, calibration |
| $\gamma$, $\beta$ | Eq (3) | P/D formulas, calibration, Prop 2(ii), Prop 3(i) |
| $\tau$, $\delta$ | Extension 2 | Eqs (7)–(8), figure (both panels), policy discussion |
| $\phi_\text{eff}$ | Extension 2 | Connects transfers back to Prop 1 pricing framework |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | P/D formulas, proof of Prop 2(iii), economic interpretation |
| $A^j$ | Remark 1 | Referenced in Extension 2 (P/D divergence at $\tau = 0$) |

**Finding:** No parameter is introduced and then abandoned. $\alpha_t$ does not appear in Propositions 1–2 (it cancels in the consumption growth ratio), but it is substantively used in Extension 2 and the figure parameterization. All other parameters appear directly in at least one result.

## Equations

- **Eq (1)** ($C_{t+1} = (1+g)C_t$): Defines the consumption growth process. Could be stated in prose, but it is a model primitive that feeds directly into the Euler equation derivation. Standard practice in asset pricing; one line.
- **Eq (2)** ($\alpha_{t+1} = \phi\alpha_t$): Core displacement mechanism. Appears throughout.
- **Eq (3)** (CRRA utility): Needed to derive the $\phi^{-\gamma}$ terms in Proposition 1. Cannot be replaced with prose without losing the derivation.
- **Eqs (4)–(5)** (P/D ratios): Core quantitative results. Used in calibration table and Extension 2.
- **Eq (6)** (existence condition): Referenced in Extension 2 where P/D diverges.
- **Eq (7)** (transfer consumption): Foundation for Extension 2 analysis and figure.
- **Eq (8)** (transfer ratio): Delivers the key insight that the ratio is independent of $\eta$, which motivates the "singularity economics" argument about levels.

**Finding:** No equation is decorative. Each feeds into a result, calibration, or economic argument.

## Propositions and formal results

- **Proposition 1** (P/D ratios): Core result. Used in calibration (Table 1) and referenced via $\phi_\text{eff}$ in Extension 2. Cannot be replaced with prose—the quantitative calibration depends on the closed-form expressions.
- **Remark 1** (existence condition): Could in principle be folded into prose, but it is explicitly referenced in Extension 2 (the P/D divergence at $\tau = 0$ under the large singularity). It sets up a payoff that comes later. Not ceremonial.
- **Proposition 2** (comparative statics): All three parts connect to the calibration discussion and the paper's economic narrative: (i) displacement severity → valuation spread, (ii) singularity probability → spread (with the honest qualification "γ sufficiently large"), (iii) extinction → attenuation. Part (iii) includes a parameterization-dependent claim about the ratio, which connects to the extinction discussion that is a key theme.
- **Proposition 3** (veto): Both parts do economic work. Part (i) connects incomplete markets to AI regulation debates. Part (ii) provides the complete-markets benchmark. The proof is verbal rather than heavily algebraic, consistent with the paper's lean style.

**Finding:** No proposition or subpart is abandoned after introduction. Each connects to calibration, policy discussion, or economic interpretation.

## Checks for pompous or ceremonial formalism

- The paper does not introduce lemmas, corollaries, or definitions beyond what the propositions require.
- There is no formalism around the AI owners' optimization (they are a residual group, not optimizing agents—appropriate given that the household is the marginal investor).
- The positive singularity in Extension 1 ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$) is stated in one formula and used qualitatively in Proposition 3. The formula clarifies that the positive singularity is the symmetric reverse of the negative one. Minimal formalism for a concrete payoff.
- The veto cost in Extension 1 is deliberately left unformalized—it is discussed qualitatively rather than given a symbol. This is the opposite of ceremonial formalism.
- $\phi_\text{eff}$ is introduced in one line to connect Extension 2 back to Proposition 1. Economically informative, not decorative.

## Could any result be stated in plain English without loss?

- Proposition 1 cannot: the calibration table depends on the closed-form expressions.
- Proposition 2 could in principle be stated verbally ("the AI premium rises with displacement severity and singularity probability, and falls with extinction risk"), but the formal statement adds precision about conditions (e.g., "γ sufficiently large") and the proof of (iii) reveals a non-obvious convexity mechanism.
- Proposition 3 is already largely verbal in its proof and statement. It is a qualitative result presented in a formal wrapper, but the wrapper is appropriate for the journal audience and the result is substantive.
- Remark 1 could be folded into prose, but it is a single displayed equation with a direct later payoff.

**Finding:** No formal object can be replaced with plain English without weakening the paper's economic claims or losing content needed for the quantitative analysis.

## Conclusion

The paper is lean. Every formal element—parameter, equation, proposition, and remark—connects to a result, calibration, or economic argument that matters for the paper's conclusions. No formalism is introduced and abandoned, no auxiliary detours are present, and the style is restrained (no unnecessary lemmas, definitions, or corollaries).

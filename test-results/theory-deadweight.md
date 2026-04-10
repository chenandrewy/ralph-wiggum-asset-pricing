# tests/theory-deadweight.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260409T213452.252125-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.252125-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper does meaningful economic or narrative work; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without weakening the paper's claims.

## Audit Details

### Methodology
Every formal object—parameters, equations, propositions, remarks—was checked against four criteria: (1) is it used in a result, calibration, or interpretation that matters? (2) could its takeaway be stated in plain English without loss? (3) is it introduced and then abandoned? (4) is it ceremonial or a detour?

### Parameters and Variables
| Object | Where introduced | Where used | Verdict |
|--------|-----------------|------------|---------|
| $C_t$, $g$ (eq 1) | Setup §2.1 | P/D formulas, calibration, transfers | Active |
| $\alpha_t$, $c_t^H$ | Setup §2.1 | Displacement, SDF, veto, transfers | Active |
| $p$ | Singularity §2.1 | P/D formulas, Table 1, Prop 2(ii) | Active |
| $\xi$ | Singularity §2.1 | P/D formulas, Table 1, Prop 2(iii) | Active |
| $\eta$ | Singularity §2.1 | P/D formulas, calibration, transfer ratio | Active |
| $\phi$ | Displacement (eq 2) | SDF, P/D formulas, Prop 2(i), transfers | Active |
| $\theta_t$, $\Delta\theta$ | Assets §2.1 | $\Gamma^{AI}$, $\Gamma^{N}$, calibration | Active |
| $\gamma$, $\beta$ | Preferences (eq 3) | P/D formulas, Prop 2, Prop 3, calibration | Active |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | Comparative statics, existence condition | Active |
| $A^j$ | Remark 1 (eq 6) | Extension 2 (infinite price discussion) | Active |
| $\tau$, $\delta$ | Extension 2 | Transfer formula, figure, $\phi_\text{eff}$ | Active |
| $\phi_\text{eff}$ (eq 8) | Extension 2 | Connects transfers to baseline P/D formula | Active |

No parameter or variable is introduced without appearing in a downstream result, calibration, or interpretation.

### Propositions and Remarks
- **Proposition 1 (P/D ratios):** Core result. Closed-form expressions are the paper's main technical contribution, used directly in Table 1 and Figure 2. Cannot be stated in plain English—the formulas are the point.
- **Proposition 2 (Comparative statics):** All three parts are exercised in §3. Part (i): displacement severity discussed in calibration. Part (ii): singularity probability is the primary grid variable in Table 1. Part (iii): extinction attenuation is a key result connecting to Jones (2024) and is visible in Table 1's grid.
- **Proposition 3 (Veto):** Both parts do distinct work. Part (i) establishes the distortion from incomplete markets. Part (ii) provides the policy-relevant contrast showing complete markets eliminate the distortion. Together they ground the paper's connection to AI regulation debates.
- **Remark 1 (Existence condition):** Establishes $A^j < 1$, which is explicitly invoked in Extension 2 when the condition is violated ($\phi^{-\gamma} = 160{,}000$), creating the infinite-price discontinuity that motivates transfers. Not a detour—it sets up a payoff later.

### Displayed Equations
- **Eq 1** (consumption growth): One line, defines the economy. Standard and minimal.
- **Eq 2** (displacement): Defines the singularity mechanism. Essential.
- **Eq 3** (CRRA utility): Standard, but not ceremonial—needed for Euler equation derivation and implicitly for the veto welfare comparison in Prop 3.
- **Eqs 4–5** (P/D ratios): Core results.
- **Eq 6** (existence): Used in Extension 2.
- **Eq 7** (transfer consumption): Defines the extension's mechanism.
- **Eq 8** ($\phi_\text{eff}$): Connects transfers back to baseline pricing formula—an efficient notational device.
- **Eq 9** (transfer ratio): Establishes that the ratio is independent of $\eta$, the key economic insight of Extension 2.
- **Eqs 10–12** (appendix proof): Required by the spec; the proof is short.

### Potential Flags Considered and Dismissed
1. **Non-AI P/D formula (eq 5):** Structurally identical to eq 4 with $\Gamma^N$ replacing $\Gamma^{AI}$. Could in principle be omitted with a sentence. However, the comparison of the two formulas is the economic content of Proposition 1, and Table 1 reports both. Keeping both explicit is conventional and aids readability.
2. **Proof of Proposition 2 in the main text:** Three one-paragraph proofs, not long enough to warrant appendix treatment per the spec. Each proof illuminates the economics (marginal utility amplification, convexity of $A/(1-A)$) rather than being purely algebraic.
3. **Transfer ratio (eq 9):** The paper notes the economic content is in the *levels*, partially qualifying the ratio result. But the equation still does work: it establishes transfers are always beneficial ($>1$ for any $\tau > 0$) regardless of $\eta$, supporting the explosive-growth argument.

### Conclusion
The paper is lean. Every formal object connects to either the pricing results (Prop 1, Table 1), the comparative statics (Prop 2, Table 1), the policy extensions (Props 3, Extension 2, Figure 2), or the appendix proof. No formalism is introduced and abandoned, no equation is ceremonial, and no result could be replaced by plain English without weakening the paper's quantitative or theoretical claims.

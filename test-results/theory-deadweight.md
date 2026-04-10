# tests/theory-deadweight.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 1m 58s
[ralph-garage/agent-logs/20260409T205235.728870-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.728870-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper does meaningful economic, quantitative, or narrative work; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without weakening the paper's claims.

## Audit of Formal Objects

### Parameters and Variables
| Object | Where introduced | Where used | Verdict |
|--------|-----------------|------------|---------|
| $C_t$, $g$ | Eq (1), Setup | P/D formulas (4–5), calibration (Sec 3), extensions | Active |
| $\alpha_t$ | Setup | Displacement (Eq 2), Extension 1 (veto, positive singularity), Extension 2 (Eq 7–8), calibration | Active |
| $c_t^H = \alpha_t C_t$ | Setup | Utility (Eq 3), Euler equation (Appendix), Extension 2 | Active |
| $\phi$ | Eq (2) | P/D formulas, Prop 2, calibration, $\phi_\text{eff}$ in Ext 2 | Active |
| $p$, $\xi$ | Singularity setup | P/D formulas, Prop 2, calibration, extensions | Active |
| $\eta$ | Singularity setup | P/D formulas, calibration, Ext 2 (transfer ratio independence) | Active |
| $\theta_t$, $\Delta\theta$ | Asset setup | $\Gamma^{AI}$, $\Gamma^{N}$ definitions, calibration | Active |
| $\gamma$, $\beta$ | Eq (3) | P/D formulas, Prop 2(ii) condition, calibration | Active |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | Prop 2, Remark 1, economic discussion after Prop 1 | Active |
| $\tau$, $\delta$ | Ext 2 | Transfer consumption (Eq 7), transfer ratio (Eq 8), Figure 2 | Active |
| $\phi_\text{eff}$ | Ext 2 | Connects transfers back to Prop 1's P/D formula | Active |
| $A^j$ | Remark 1 (Eq 6) | Ext 2: explains P/D blow-up at $\tau = 0$ under large singularity | Active |

No parameter, variable, or function is introduced without appearing in a result, calibration, or interpretation that matters for the paper's conclusions.

### Equations
1. **Eq (1)**: $C_{t+1} = (1+g) C_t$. Trivially simple, but anchors the growth baseline that the singularity disrupts. One line; sets up the contrast with the singularity jump. Not deadweight.
2. **Eq (2)**: Displacement $\alpha_{t+1} = \phi \alpha_t$. Core mechanism. Used in pricing, comparative statics, extensions, calibration.
3. **Eq (3)**: CRRA utility. Needed for Euler equation and veto analysis. Standard but necessary.
4. **Eqs (4–5)**: P/D ratios. Central results. Calibrated in Table 1. Compared across assets.
5. **Eq (6)**: Existence condition $A^j < 1$. Directly used in Extension 2 to explain infinite P/D at extreme displacement.
6. **Eq (7)**: Transfer consumption. Needed for the transfers analysis and Figure 2.
7. **Eq (8)**: Transfer ratio independence of $\eta$. This is the key economic insight of Extension 2—that singularity growth makes transfers effective regardless of scale. Cannot be stated as compellingly without the formula.

### Propositions and Proofs
- **Proposition 1** (P/D ratios): Central result. Calibrated in Section 3.
- **Remark 1** (existence condition): Not ceremonial—it sets up the P/D blow-up in Extension 2. Without it, the infinite-price discontinuity in Figure 2 would appear unmotivated.
- **Proposition 2** (comparative statics): Each part (i–iii) provides testable qualitative predictions discussed in Section 3. Part (ii)'s "$\gamma$ sufficiently large" condition is an honest qualification, not unnecessary formalism.
- **Proposition 3** (veto): Delivers the economic punchline of Extension 1—incomplete markets distort real decisions, not just prices.

### Could any formal takeaway be stated in plain English?
- The P/D formulas could not: they are needed for calibration and Figure 2.
- The comparative statics (Prop 2) could be stated verbally, but the proposition format organizes three distinct predictions precisely. The conditions (e.g., "$\gamma$ sufficiently large") would be lost.
- The transfer ratio (Eq 8) could be stated as "the ratio is independent of $\eta$," but showing the formula makes the claim verifiable and reveals the dependence on $\tau$, $\delta$, $\phi$, $\alpha$.
- The veto result (Prop 3) could be verbalized, but the incomplete-vs-complete contrast is sharpened by the formal statement.

### Checks for Ceremonial or Pompous Formalism
- No lemmas, corollaries, or definitions are used. The paper uses only propositions and one remark.
- No auxiliary formal detours (no side models, no "consider the following alternative economy" digressions).
- No notation is introduced for its own sake—every symbol appears in at least one result or calibration.
- The appendix proof is required by the spec and is concise (one page).

### Potential Marginal Items (not deadweight)
- **Eq (1)** is the simplest equation in the paper and could be stated in prose ("aggregate consumption grows at rate $g$"). However, it occupies one line and sets up the contrast with the singularity jump. Given that the spec requires all display equations to be numbered, this is a formatting requirement rather than unnecessary formalism.
- **The positive singularity formula** $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ in Extension 1 is not in a numbered equation and mirrors Eq (2). It is used in the proof of Proposition 3. Lean and appropriate.

## Conclusion
The paper is disciplined: 8 numbered equations, 3 propositions, 1 remark, and zero unused formal objects. Every piece of formalism either feeds into the calibration, drives a proposition, or delivers an economic insight that would be weaker in plain English. No auxiliary detours, no ceremonial definitions, no abandoned notation.

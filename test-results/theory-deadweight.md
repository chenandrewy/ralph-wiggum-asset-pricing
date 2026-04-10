# tests/theory-deadweight.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 1m 54s
[ralph-garage/agent-logs/20260409T203927.589380-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.589380-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation contributes to a result, calibration, or economic interpretation that matters for the paper's conclusions.

## Audit Details

### Methodology
Cataloged every formal object (equations, propositions, remarks), every parameter/variable, and every prose mechanism. For each, checked whether it (a) appears in a downstream result, calibration, or figure, (b) could be replaced by plain English without weakening the economic claims, and (c) is ceremonial or abandoned.

### Parameters and Variables

| Symbol | Introduced | Used in |
|--------|-----------|---------|
| $C_t$, $g$ | Eq (1) | P/D formulas, calibration, transfer equations |
| $\alpha_t$, $\phi$ | Eq (2), setup | P/D formulas (via $\phi^{-\gamma}$), calibration, $\phi_\text{eff}$, veto argument |
| $\gamma$, $\beta$ | Eq (3) | P/D formulas, comparative statics, calibration |
| $p$, $\xi$ | Singularity setup | P/D formulas, comparative statics, calibration |
| $\eta$ | Singularity setup | P/D formulas ($\Gamma$ factors), calibration, transfer analysis |
| $\theta_t$, $\Delta\theta$ | Asset setup | $\Gamma^{AI}$, $\Gamma^{N}$, calibration |
| $\Gamma^{AI}$, $\Gamma^{N}$ | Prop 1 | P/D formulas, comparative statics discussion |
| $\tau$, $\delta$ | Extension 2 | Transfer equation, $\phi_\text{eff}$, figure panels |
| $\phi_\text{eff}$ | Extension 2 | Connects transfers to P/D formula |
| $A^j$ | Remark 1 | Referenced in Extension 2 discussion (infinite P/D at $\tau=0$) |

No parameter or variable is introduced and then unused.

### Formal Objects

1. **Eq (1): Aggregate consumption growth.** One-line equation establishing baseline growth. Anchors $g$ which enters every P/D formula. Could be stated in English, but it is compact and sets notation used throughout.

2. **Eq (2): Displacement rule.** Central mechanism of the paper. Required.

3. **Eq (3): CRRA utility.** Establishes $\gamma$ and $\beta$. Standard in consumption-based asset pricing; the target audience expects it. The Euler equation in the appendix derives from this. One line, not a detour.

4. **Proposition 1 (P/D ratios) + Eqs (4)–(5).** Core quantitative result. Feeds the calibration table (Table 1) and the transfer analysis. Cannot be replaced by plain English—the whole quantitative analysis depends on these formulas.

5. **Remark 1 (Existence condition) + Eq (6).** Directly referenced in Extension 2: the large-singularity case violates the existence condition at $\tau = 0$, which is a key feature of Figure 2 and the economic argument for transfers. Not abandoned.

6. **Proposition 2 (Comparative statics).** All three parts—(i) displacement severity, (ii) singularity probability, (iii) extinction probability—are discussed in Section 3's interpretation of Table 1. The comparative statics are brief (in-line proofs, no appendix), and each maps to a pattern in the calibration. Not ceremonial.

7. **Proposition 3 (Veto).** Qualitative result with qualitative proof. The positive singularity specification ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$) is minimal—one line—and makes the symmetry with displacement precise without introducing extra machinery. No unused apparatus.

8. **Eqs (7)–(8): Transfer consumption and transfer ratio.** Both feed the figure panels and the economic discussion. Eq (8) delivers the key insight that the ratio is independent of $\eta$, which is the paper's main policy point about singularity-scale growth overwhelming deadweight costs.

9. **Appendix proof.** Required by the spec and referenced by Proposition 1. The Euler equation derivation is the standard pricing argument; no extraneous steps.

### Could any result be stated in plain English instead?

- **Proposition 1:** No. The formulas are the input to the calibration table and the transfer analysis.
- **Proposition 2:** Borderline, but the brief in-line proofs add precision (e.g., the $\gamma$ qualifier in part (ii)) at minimal cost. Removing them would lose the mechanism.
- **Proposition 3:** Already largely qualitative. The formal statement adds the role of $\gamma$ and the complete-markets contrast. Appropriate for the audience.
- **Remark 1:** The existence condition is quantitative and referenced numerically ($\phi^{-\gamma} = 160{,}000$). Cannot be replaced by English.

### Abandoned or detour formalism?
None found. The paper does not introduce auxiliary lemmas, intermediate results, or notational machinery that is not used downstream. The formal arc is: setup → P/D ratios → comparative statics → calibration → extensions (veto, transfers) → figure. Every formal object sits on this arc.

### AI owners' consumption
The paper mentions AI owners receive $(1-\alpha_t)C_t$ (one sentence in setup). This is not formalized further—no utility function for AI owners, no pricing from their perspective. It reappears implicitly in the transfer base $(1-\phi\alpha)$ in Eq (7). This is appropriate: it provides context without creating unused machinery.

# tests/theory-deadweight.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260410T225642.491399-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.491399-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, subpart, and parameter in the paper contributes to an economic claim, calibration, or interpretation; no deadweight formalism was found.

## Audit Details

### Parameters and Variables

Every parameter introduced in the setup is used in at least one result, calibration value, or interpretive discussion:

- **$g$ (growth rate):** Appears in all P/D formulas (Proposition 1), calibration ($g = 0.02$).
- **$\alpha_t$ (household consumption share):** Core displacement variable; used in Extensions 1 and 2, transfer formula (Eq 7), and the $\phi_\text{eff}$ expression (Eq 8).
- **$\phi$ (displacement severity):** Appears in P/D formulas, comparative statics (Proposition 2(i)), calibration, both extensions.
- **$p$ (singularity probability):** Appears in P/D formulas, comparative statics (Proposition 2(ii)), calibration grid.
- **$\xi$ (extinction probability):** Appears in P/D formulas, comparative statics (Proposition 2(iii)), calibration grid, and the veto discussion.
- **$\eta$ (productivity boost):** Appears in P/D formulas, calibration, transfer ratio (Eq 9), and the key economic argument that levels grow with $\eta$.
- **$\theta_t$, $\Delta\theta$ (AI dividend share):** Appear in P/D formulas via $\Gamma^{AI}$ and $\Gamma^{N}$, calibration ($\theta = 0.15$, $\Delta\theta = 0.2$).
- **$\gamma$ (risk aversion), $\beta$ (discount factor):** Appear in P/D formulas, calibration, veto condition, and the existence condition.
- **$\tau$ (tax rate), $\delta$ (deadweight cost):** Used in Extension 2's transfer formula, effective displacement, transfer ratio, and Figure 2.

No parameter is introduced and then abandoned.

### Intermediate Formal Objects

- **$\Gamma^{AI}$, $\Gamma^{N}$ (dividend growth factors):** Defined in Proposition 1, discussed economically ("the key economic content... is in the comparison of $\Gamma^{AI}$ and $\Gamma^{N}$"), and used in comparative statics proofs.
- **$A^j$ (existence condition, Remark 1):** Referenced in Extension 2 to explain the infinite P/D discontinuity in Figure 2. Earns its keep by connecting the baseline pricing result to the transfer extension.
- **$\phi_\text{eff}$ (effective displacement, Eq 8):** Efficiently connects Extension 2 back to Proposition 1 by showing transfers enter the SDF through the same channel as $\phi$. Compact and functional.

### Propositions and Proofs

- **Proposition 1 (P/D ratios):** Core result. Closed-form expressions are used throughout the quantitative analysis and Extension 2.
- **Proposition 2 (comparative statics):** All three subparts—(i) displacement severity, (ii) singularity probability, (iii) extinction probability—are verified and discussed in Section 3's table analysis. The inline proof is economic (not mechanical), explaining the intuition behind each result.
- **Proposition 3 (veto):** Core of Extension 1. Both subparts—(i) veto under incomplete markets, (ii) no veto under complete markets—are needed for the contrast that drives the economic point.
- **Remark 1 (existence condition):** Foreshadows and is explicitly referenced in Extension 2, where the P/D ratio is undefined at $\tau = 0$ under severe displacement. Not a detour.

### Equations

- **Eq (1) ($C_{t+1} = (1+g)C_t$):** Simple but establishes notation used in all pricing formulas.
- **Eq (2) ($\alpha_{t+1} = \phi \alpha_t$):** Core displacement mechanism.
- **Eq (3) (CRRA utility):** Establishes notation ($\gamma$, $\beta$) and functional form. Conventional in theory papers; the negative utility property ($\gamma > 1$) is used in the veto discussion's extinction normalization.
- **Eqs (4)–(5) (P/D ratios):** Core results.
- **Eq (6) (existence condition):** Referenced in Extension 2.
- **Eq (7) (transfer consumption):** Core of Extension 2.
- **Eq (8) ($\phi_\text{eff}$):** Bridges Extension 2 to Proposition 1.
- **Eq (9) (transfer ratio):** Makes the specific point that the ratio is $\eta$-independent, supporting the argument that the economic content is in levels.
- **Appendix equations (10–12):** Standard proof machinery for Proposition 1.

### Checks for Ceremonial or Pompous Formalism

- No formal lemmas or corollaries that restate obvious implications.
- No auxiliary formal detours: the paper moves linearly from setup to pricing to extensions.
- No "for completeness" results that the paper never uses.
- The positive singularity payoff ($\min(1, \alpha_t/\phi)$) in Extension 1 is stated inline rather than as a displayed equation, and is used in the numerical example. Appropriately scoped.
- Proofs are economic in character, not mechanical algebra.

### Conclusion

The paper's formalism is lean and purposeful. Each formal object—whether parameter, equation, proposition, or remark—does identifiable economic or narrative work. No object is introduced and abandoned, no subpart is dead weight within a useful larger structure, and no qualitative claim requires its formal scaffolding to be removed. The paper adheres to the good-theory-style standard of keeping mathematical formalism to a minimum where each piece contributes to the economic claims.

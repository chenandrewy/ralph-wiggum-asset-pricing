# tests/theory-clarity.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260412T141819.034665-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.034665-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly structured setup paragraphs with most critical expressions in display math; two notable presentation gaps (dividend growth factors defined only inside Proposition 1, and the veto utility expression only in a proof) do not rise to the level of a fail because the surrounding context is clear and well-organized.

## Key items identified

### Should appear in display math (and assessment)
1. **Aggregate consumption growth** $C_{t+1} = (1+g)C_t$ -- display math eq. (1), opens Consumption paragraph. OK.
2. **Displacement rule** $\alpha_{t+1} = \phi\alpha_t$ -- display math eq. (2), inside structured enumerated list. OK.
3. **CRRA utility** -- display math eq. (3), opens Preferences paragraph. OK.
4. **P/D ratio formulas** -- display math inside Proposition 1 statement. OK.
5. **Existence condition** $A^j < 1$ -- display math in Remark 1. OK.
6. **Dividend growth factors** $\Gamma^{AI}$, $\Gamma^{N}$ -- defined only in trailing "where" clause of Proposition 1 (line 135). **Gap**: these drive the entire valuation spread and all three propositions; promoting to standalone display math before Prop 1 would help readers locate them on re-reading.
7. **Effective displacement** $\phi_\text{eff}$ -- display math eq. (phi-eff). OK.
8. **Transfer consumption** $c^H_{post}$ -- display math eq. (transfer-consumption). OK.
9. **Transfer ratio** $c^H_{post}/c^H_{no-transfer}$ -- display math eq. (transfer-ratio). OK.
10. **Veto utility gain** $\Delta u(\gamma)$ -- display math inside Proposition 3 **proof** only (line 218). **Gap**: this expression is the economic core of the veto result; readers encounter it only after entering the proof.

### May remain in prose (and assessment)
11. **Singularity probability** $p$ -- opens Singularity paragraph. OK.
12. **Extinction probability** $\xi$ -- item 2 of enumerated list under Singularity. OK (structured list, easy to find).
13. **Productivity boost** $\eta > 0$ -- parenthetical in list item 1 under Singularity. OK (immediately follows the consumption-jump statement).
14. **Displacement severity** $\phi \in (0,1)$ -- inline in eq. (2) with explanation on next line. OK.
15. **AI dividend share** $D_t^{AI} = \theta_t C_t$ and **update rule** $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ -- prose in Assets bullet (line 103). Acceptable; the update rule is the source of $\Gamma^{AI} \neq \Gamma^{N}$ and could benefit from display math, but its placement at the start of the AI stocks bullet is clear.
16. **Positive singularity probability** $q > 1/2$ -- mid-paragraph in Extension 1 (line 200). Acceptable; it is introduced alongside the positive/negative singularity structure in the setup paragraph.
17. **Veto cost** $\kappa > 0$ -- mid-sentence in Extension 1 setup (line 204). OK.
18. **Tax rate** $\tau$ and **deadweight cost** $\delta > 0$ -- prose in Extension 2 setup paragraph (line 239). OK.
19. **Condition** $\phi(1+\eta) < 1$ -- first appears as parenthetical mid-paragraph (line 152). This is a derived condition rather than a new assumption; its placement in the discussion of Proposition 1 is adequate, though stating it more prominently as a maintained assumption would help.
20. **Complete markets assumption** -- opens its own paragraph (line 206). OK.
21. **Kaldor-Hicks efficiency** -- opens its own definitional sentence (line 202). OK.

## Section-level findings

### Section 2.1 (Setup)
Well-structured with four named paragraphs (Consumption, Singularity, Assets, Preferences). Key parameters ($p$, $\xi$, $\phi$, $\eta$, $g$, $\gamma$, $\beta$) are introduced in clear model-setup context. The enumerated singularity structure is easy to parse. The $\theta$ update rule in the Assets bullet is clearly placed, though it could optionally be promoted to display math since it generates $\Gamma^{AI}$.

### Section 2.2 (Equilibrium prices)
Proposition 1 presents P/D formulas in display math -- good. **Main gap**: $\Gamma^{AI}$ and $\Gamma^{N}$ are defined only in the "where" clause trailing the proposition. Since these drive the valuation spread, extinction attenuation (Prop 2), and the quantitative analysis, they would benefit from standalone display math in the setup or just before the proposition. The condition $\phi(1+\eta) < 1$ appears as a parenthetical in the discussion; since the veto result and the intuition for the hedging channel both rely on it, a more prominent statement would help.

### Section 2.3 (Discussion)
No new model assumptions introduced. Recalls and interprets earlier results. No issues.

### Section 3 (Quantitative Analysis)
Calibration parameters clearly listed in prose at the start. No new model assumptions. No issues.

### Section 4.1 (Extension 1: Veto)
Setup paragraph introduces $q$, the positive singularity, and the veto cost $\kappa$ in prose -- all acceptable placements. The Kaldor-Hicks definition and complete-markets assumption each get their own paragraph openings. **Minor gap**: $\Delta u(\gamma)$ (eq. veto-delta-u) appears only inside the proof of Proposition 3. Since this expression is the economic core of the veto result, placing it in the main text (e.g., in a setup paragraph before the proposition) would help readers who skip proofs.

### Section 4.2 (Extension 2: Transfers)
$\tau$, $\delta$, and the transfer consumption equation are introduced in a clear setup paragraph with display math. $\phi_\text{eff}$ gets its own display equation. The transfer ratio also appears in display math. Well-organized.

### Appendix A
Proof mechanics only; no new model assumptions. No issues.

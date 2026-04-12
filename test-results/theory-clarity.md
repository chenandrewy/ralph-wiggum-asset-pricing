# tests/theory-clarity.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 2m 18s
[ralph-garage/agent-logs/20260411T214322.784207-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.784207-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Nearly all key model assumptions are introduced in clearly labeled setup paragraphs or display math before results that use them; two minor presentation gaps do not impair readability.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq. (1), Setup/Consumption
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq. (2), Setup/Singularity
3. CRRA utility — eq. (3), Setup/Preferences
4. P/D ratios for AI and non-AI stocks — eqs. (4)–(5), Proposition 1
5. Post-transfer consumption — eq. (5), Extension 2
6. Effective displacement $\phi_\text{eff}$ — eq. (6), Extension 2

### Should appear in display math but currently do not
7. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined only inline at the end of Proposition 1 (line 140). These drive the entire premium mechanism and are referenced repeatedly in discussion and proofs.

### Prose assumptions (correctly placed at or near paragraph start)
8. Household consumption share $c_t^H = \alpha_t C_t$ — Setup/Consumption paragraph
9. Singularity probability $p$ — opens Setup/Singularity paragraph
10. Extinction probability $\xi$ — Setup/Singularity, within enumerated list item 2
11. Productivity boost $\eta$ — Setup/Singularity, within enumerated list item 1
12. AI and non-AI dividend definitions — Setup/Assets bullets
13. AI share dynamics $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — Setup/Assets bullet
14. Positive singularity probability $q > 1/2$ — opens Extension 1 paragraph
15. Transfer deadweight cost $\delta$ — Extension 2, before transfer equation

### Prose assumptions with placement issues
16. Market incompleteness (household cannot trade restricted equity) — introduced mid-paragraph in Assets (line 113), after the two asset bullets
17. Condition $\phi(1+\eta) < 1$ — first appears mid-paragraph in Section 2.3 Discussion (line 157), not in Setup; later used in Proposition 3 proof
18. Veto cost $\kappa$ — mid-paragraph in Extension 1 (line 208)

## Section-level findings

**Section 2.1 (Setup):** Well organized with labeled paragraphs (Consumption, Singularity, Assets, Preferences). All core parameters ($g$, $p$, $\phi$, $\xi$, $\eta$, $\alpha$, $\theta$, $\Delta\theta$, $\gamma$, $\beta$) are introduced before any results. Market incompleteness is stated clearly but appears after the asset bullets rather than at the paragraph opening; since the paragraph opens by listing tradeable assets, this ordering is logical (define what can be traded, then state what cannot).

**Section 2.2 (Equilibrium prices):** The SDF statement correctly opens the section. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are the main gap: they are defined only inside Proposition 1 rather than in a standalone display equation in Setup or before the proposition. Since these factors are the core economic content (the paper says so at line 157), pulling them into display math before or outside the proposition would improve scanability. This is a minor issue — they are clearly defined and immediately discussed.

**Section 2.3 (Discussion):** The condition $\phi(1+\eta) < 1$ first appears here mid-paragraph (line 157) rather than in Setup. This is a borderline issue: the condition is an implication of the parameters $\phi$ and $\eta$ already defined in Setup, not a new assumption. It would benefit from explicit statement in the Singularity paragraph, but its absence does not prevent understanding.

**Section 3 (Quantitative Analysis):** All calibration values are stated in a single paragraph. No new model assumptions.

**Section 4.1 (Extension 1 — Veto):** The positive singularity setup ($q$, share recovery rule) is introduced at the paragraph start before Proposition 3. The veto cost $\kappa$ appears mid-paragraph (line 208) but in a short, clearly scoped paragraph — acceptable.

**Section 4.2 (Extension 2 — Transfers):** Transfer mechanism, tax rate $\tau$, and deadweight cost $\delta$ are all introduced in prose before the transfer equation. The effective displacement $\phi_\text{eff}$ gets its own display equation. Well structured.

**Appendix A:** Contains derivation details only; no new assumptions introduced.

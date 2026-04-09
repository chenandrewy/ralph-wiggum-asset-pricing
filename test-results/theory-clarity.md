# tests/theory-clarity.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 1m 51s
[ralph-garage/agent-logs/20260409T190308.204146-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.204146-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with display math for the most critical expressions; the one notable gap—dividend growth factors defined only inside a proposition—follows standard economics convention and does not impair readability.

## Key Items Identified

### Display math in main text (Group A)
- **A1** Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq. (1)
- **A2** Displacement rule $\alpha_{t+1}=\phi\alpha_t$ — eq. (2)
- **A3** CRRA utility — eq. (3)
- **A4** Dividend growth factors $\Gamma^{AI}$, $\Gamma^N$ — defined in Proposition 1 "where" clause
- **A5** Post-transfer consumption — eq. (8)

### Prose assumptions (Group B)
- **B1** Three-outcome singularity structure (probabilities $p$, $\xi$)
- **B2** AI dividend share evolution $\theta_{t+1}=\theta_t+\Delta\theta(1-\theta_t)$
- **B3** Market incompleteness (private AI capital not tradable)
- **B4** Condition $\phi(1+\eta)<1$ for hedging to operate
- **B5** Extension 1: $\lambda>1/2$ (social efficiency of AI development)
- **B6** Extension 1: extinction utility normalization $u_\text{ext}=0$
- **B7** Extension 2: tax rate $\tau$, deadweight cost $\delta_0\tau$

## Section-Level Findings

### Section 2.1 (Setup)
**Questions A–C: Well-organized.** The four labeled paragraphs (Consumption, Singularity, Assets, Preferences) introduce assumptions in a logical order. Key expressions appear in display math (eqs. 1–3). Prose assumptions (singularity probability $p$, extinction probability $\xi$, household share $\alpha_t$) open or appear near the top of their respective paragraphs. The AI dividend share update rule (B2) is embedded mid-sentence in a bullet but remains easy to find. Market incompleteness (B3) is stated at the end of the Assets paragraph rather than opening its own paragraph, but it is clearly marked and hard to miss.

### Section 2.2 (Equilibrium Prices)
**Question B (minor note on A4):** The dividend growth factors $\Gamma^{AI}$ and $\Gamma^N$ are defined only inside the "where" clause of Proposition 1 (lines 133–134). These factors drive the valuation spread and all comparative statics. Promoting them to a standalone display equation before Proposition 1 would make them easier to locate on re-reading. However, defining auxiliary quantities in a proposition's "where" clause is standard practice in economics, so this is a presentational preference, not a clarity failure.

**Question C (note on B4):** The condition $\phi(1+\eta)<1$—under which household consumption falls despite the aggregate boom—is mentioned in passing after Corollary 1 (line 141) but never formally stated as a named condition. Since the quantitative section and extensions implicitly rely on it, a brief explicit statement would help.

### Section 2.3 (Discussion)
No new assumptions. Recalls baseline mechanisms clearly.

### Section 3 (Quantitative Analysis)
No new assumptions. Parameter values are stated in a single sentence (line 179) before the table. Clear.

### Section 4.1 (Extension 1: Veto)
**Questions A–C: Adequate.** The positive-singularity parameters ($\lambda$, $\phi^+$) and veto cost ($\kappa$) are introduced in clearly separated prose paragraphs before Proposition 3. The assumption $\lambda>1/2$ (B5) appears mid-paragraph (line 208) rather than at the top, but the paragraph is short enough that it reads naturally. The extinction utility normalization $u_\text{ext}=0$ (B6) is introduced inside Proposition 3's statement; moving it to the setup prose would be cleaner but does not impair understanding.

### Section 4.2 (Extension 2: Government Transfers)
**Questions A–C: Well-organized.** The tax rate $\tau$ and deadweight parameter $\delta_0$ are introduced in a setup paragraph (lines 239–240) immediately before the display equation for post-transfer consumption (eq. 8). The transfer ratio (eq. 9) is also displayed. Clear and easy to follow.

### Appendix A (Proof of Proposition 1)
No new assumptions introduced. Derives results from setup assumptions. No issues.

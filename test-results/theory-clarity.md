# tests/theory-clarity.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 1m 48s
[ralph-garage/agent-logs/20260409T182005.707812-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.707812-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Nearly all key model assumptions are introduced in clearly labeled setup paragraphs or display math before the results that use them; the one notable gap is that the dividend growth factors are defined only inside a proposition statement.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq. (1), display math
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq. (2), display math
3. CRRA utility — eq. (3), display math
4. Post-transfer consumption — eq. (6), display math
5. Transfer limit as $\eta\to\infty$ — eq. (7), display math

### Should appear in display math but does not
6. **Dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$** — defined only inside Proposition 1's statement (line 132). These drive Corollary 1 and all of Proposition 2; a reader scanning the model setup will not encounter them until mid-proposition.

### Prose assumptions (properly placed at or near paragraph starts)
7. Household consumption share $c_t^H = \alpha_t C_t$ — early in Consumption paragraph (line 84)
8. Singularity probability $p$ — opens Singularity paragraph (line 87)
9. Extinction probability $\xi$ and $C_{t+1}=0$ — item 2 in Singularity enumeration (line 95)
10. Productivity boost $(1+\eta)$ — item 1 in Singularity enumeration (line 91)
11. AI dividends $D_t^{AI} = \theta_t C_t$ and share jump $\Delta\theta$ — Assets bullet list (lines 103–104)
12. Non-AI dividends $D_t^N = (1-\theta_t)C_t$ — Assets bullet list (line 105)
13. Market incompleteness (private AI capital) — end of Assets paragraph (line 108)
14. Positive singularity $\lambda$, $\phi^+>1$ — Extension 1 bullet list (lines 228–229)
15. $\lambda > 1/2$ — Extension 1 setup prose (line 232)
16. Veto cost $\kappa > 0$ — Extension 1 setup prose (line 234)
17. Tax rate $\tau$ and deadweight cost $\delta(\tau) = \delta_0\tau$ — Extension 2 setup prose (line 263)

### Borderline: defined inside a proposition but acceptable
18. $\Delta U^H$ expression — display math inside Proposition 3's definitional preamble (eq. 5, line 240). This straddles the proposition boundary but serves as setup before the enumerated claims.

## Findings by section

### Section 2.1 (Setup)
Well-organized into labeled paragraphs (Consumption, Singularity, Assets, Preferences). All baseline assumptions are introduced before any results. The three-outcome probability tree (no singularity / non-extinction singularity / extinction) is spread across an enumerated list and prose, but the structure is clear enough.

### Section 2.2 (Equilibrium prices)
The P/D ratio formulas appear in display math inside Proposition 1. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined only in the "where" clause of Proposition 1 (line 132), not in the model setup. Since these factors are the mechanical heart of Corollary 1 and Proposition 2, moving their definitions to a labeled display equation in Section 2.1 (after the Assets paragraph) would improve scanability. This is the paper's main clarity gap but does not rise to a failure because the definitions do appear before the results that use them (Corollary 1 and Proposition 2), just inside the proposition rather than in the setup.

### Section 3 (Quantitative Analysis)
No new assumptions. Parameter values are clearly stated in prose. References back to Proposition 2(iii) are correct.

### Section 4.1 (Veto extension)
New assumptions ($\lambda$, $\phi^+$, $\lambda > 1/2$, $\kappa$) are introduced in setup prose before Proposition 3. The $\Delta U^H$ expression appears as display math inside Proposition 3's preamble, which is a common and acceptable convention for propositions that need to define notation before stating claims.

### Section 4.2 (Transfers extension)
New assumptions ($\tau$, $\delta_0$) are introduced in setup prose. The post-transfer consumption and limit expressions appear in display math. Well-structured.

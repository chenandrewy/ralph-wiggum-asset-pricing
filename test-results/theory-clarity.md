# tests/theory-clarity.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 2m 18s
[ralph-garage/agent-logs/20260411T100208.994068-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T100208.994068-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with the most critical expressions in display math; minor presentation improvements are possible but no assumption is buried or missing.

## Key items identified

### Should appear in display math (and do)
1. **AGG-GROW**: $C_{t+1} = (1+g)C_t$ — eq (1), line 84
2. **DISPLACE**: $\alpha_{t+1} = \phi\,\alpha_t$ — eq (2), line 95
3. **CRRA**: Utility functional — eq (3), line 121
4. **P/D-AI, P/D-N**: Price-dividend ratios — eqs (4)-(5), lines 131-137
5. **EXISTENCE**: $A^j < 1$ — eq (5), Remark 1, line 149
6. **TRANSFER-CONS**: Post-transfer consumption — eq (7), line 253
7. **PHI-EFF**: Effective displacement — eq (8), line 261
8. **TRANSFER-RATIO**: Transfer improvement ratio — eq (9), line 269

### Introduced in prose (acceptable but noted)
9. **HH-CONS**: $c_t^H = \alpha_t C_t$ — line 88, prose after eq (1)
10. **SINGULARITY-PROB**: Probability $p$ per period — line 91, start of Singularity paragraph
11. **EXTINCTION**: $C_{t+1}=0$ with prob $\xi$ — line 99, within enumerated list
12. **DIV-AI**: $D_t^{AI} = \theta_t C_t$ and $\theta$ jump rule — lines 108-109, bullet list
13. **DIV-N**: $D_t^N = (1-\theta_t)C_t$ — line 109, bullet list
14. **INCOMPLETE-MKTS**: Household cannot trade restricted AI equity — line 114, Assets paragraph
15. **GAMMA-FACTORS**: $\Gamma^{AI}$, $\Gamma^{N}$ — line 139, defined within Proposition 1
16. **DISPLACE-COND**: $\phi(1+\eta) < 1$ — line 157, parenthetical in discussion
17. **VETO-PARAMS**: Positive singularity prob $q$, veto cost $\kappa$ — lines 211, 215

## Section-level findings

### Section 2.1 (Setup) — Good
- Clear paragraph headings (Consumption, Singularity, Assets, Preferences) organize assumptions well.
- Each labeled paragraph introduces its assumptions at or near the start.
- Items 1-8 and 9-14 are all introduced here in a logical order.
- **Minor note**: The household consumption identity (item 9, $c_t^H = \alpha_t C_t$) is load-bearing for every pricing result via the SDF but appears only in inline prose. Promoting it to display math would help readers locate it when parsing the P/D formulas. Similarly, the dividend definitions (items 12-13) and the $\theta$ jump rule could benefit from display math, since they directly determine $\Gamma^{AI}$ and $\Gamma^{N}$.

### Section 2.2 (Equilibrium prices) — Good
- Proposition 1 states P/D ratios in display math with the $\Gamma$ factors defined in the same proposition statement.
- Remark 1 gives the existence condition in display math with economic interpretation.
- **Minor note**: The $\Gamma$ factors (item 15) are defined inside Proposition 1 rather than as a standalone display equation beforehand. Since the comparison $\Gamma^{AI} > \Gamma^{N}$ is the core mechanism, a reader looking for the definition must scan within the proposition. This is acceptable but a standalone display would improve navigability.
- The SDF kernel $M_{t+1} = \beta(c_{t+1}^H/c_t^H)^{-\gamma}$ is never shown in the main text (only in the appendix Euler equation). Finance readers can infer it from CRRA preferences, but displaying it before Proposition 1 would make the incomplete-markets pricing channel more transparent.

### Section 2.3 (Discussion) — Good
- The condition $\phi(1+\eta) < 1$ (item 16) first appears parenthetically at line 157 rather than at the start of a paragraph or in the setup. This condition is important for the hedging channel and the veto result. However, it is an implication of the parameter choices rather than an independent assumption, so its parenthetical introduction is acceptable.

### Section 3 (Quantitative Analysis) — Good
- No new model assumptions; uses calibration values that are clearly stated.

### Section 4.1 (Veto extension) — Good
- New parameters $q$ and $\kappa$ (item 17) are introduced in setup prose at the start of the subsection, before Proposition 3.
- The complete-markets benchmark consumption $\alpha(1+\eta)C_t(1+g)$ is stated in prose before the proposition. Acceptable.

### Section 4.2 (Government transfers) — Good
- Tax rate $\tau$, deadweight cost $\delta$, and the transfer consumption formula are introduced in a setup paragraph with display math (eq 7) before the analysis.
- $\phi_\text{eff}$ is derived and displayed (eq 8) with a clear prose link explaining that Proposition 1 applies with $\phi \to \phi_\text{eff}$.

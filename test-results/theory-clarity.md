# tests/theory-clarity.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260409T212047.313026-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.313026-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Model assumptions are introduced in clearly labeled setup paragraphs with the most critical expressions in display math; minor presentation improvements are possible but do not impair clarity.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth: $C_{t+1} = (1+g)C_t$ — eq (1), Section 2.1
2. Displacement rule: $\alpha_{t+1} = \phi\,\alpha_t$ — eq (4), Section 2.1
3. CRRA utility $U_0^H$ — eq (5), Section 2.1
4. P/D ratios for AI and non-AI stocks — eqs (6)–(7), Proposition 1
5. Existence condition $A^j < 1$ — eq (7), Remark 1
6. Post-transfer consumption — eq (8), Section 4.2
7. Transfer ratio — eq (9), Section 4.2

### Could benefit from display math but acceptable in current form
8. Household consumption share $c_t^H = \alpha_t C_t$ — prose, line 86 (simple definition, immediately follows eq 1)
9. $\Gamma^{AI}$ and $\Gamma^{N}$ dividend growth factors — inline in Proposition 1's "where" clause (clearly set off)
10. Effective displacement $\phi_\text{eff}$ — prose, line 232 (used to connect transfers to P/D formula)

### Prose assumptions (correctly placed at/near paragraph starts)
11. Singularity probability $p$ — opens the Singularity paragraph (line 89)
12. Extinction probability $\xi$ — introduced in the singularity enumeration (line 91)
13. AI stock dividends $D_t^{AI} = \theta_t C_t$ — opens AI stocks bullet (line 106)
14. Market incompleteness — stated in its own sentences at end of Assets paragraph (line 110)
15. Positive singularity $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ — opens Extension 1 setup (line 201)
16. Veto mechanism — opens its own paragraph (line 202)
17. Transfer parameters $\tau$, $\delta$ — open the transfers paragraph (line 224)

## Section-level findings

**Section 2.1 (Setup):** Well-organized with four labeled paragraphs (Consumption, Singularity, Assets, Preferences). All key parameters ($g$, $p$, $\phi$, $\eta$, $\xi$, $\theta$, $\Delta\theta$, $\gamma$, $\beta$) are introduced before any results. The productivity jump $\eta$ and $\theta$-evolution rule appear mid-enumeration/mid-bullet, but within structured list environments where the placement is natural and clear.

**Section 2.2 (Equilibrium prices):** P/D ratios are in display math. The $\Gamma$ factors are defined in the "where" clause of Proposition 1 rather than as standalone display equations; this is a minor presentation choice that does not impair readability. The existence condition gets its own Remark with display math.

**Section 2.3 (Discussion):** Recalls earlier assumptions; does not introduce new ones. No issues.

**Section 3 (Quantitative Analysis):** Calibration parameters are clearly listed in prose. No new model assumptions.

**Section 4.1 (Extension 1 — Veto):** The positive singularity, veto mechanism, and extinction normalization are introduced in setup paragraphs before Proposition 3. Clear.

**Section 4.2 (Extension 2 — Transfers):** Transfer parameters open the paragraph, post-transfer consumption is in display math. The effective displacement $\phi_\text{eff}$ is defined in prose (line 232) rather than display math; giving it a numbered equation would aid cross-referencing but its current placement is adequate.

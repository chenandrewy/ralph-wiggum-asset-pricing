# tests/theory-clarity.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260409T200738.674285-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.674285-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with display math for the most critical expressions; the one notable gap is that the dividend growth factors are defined inline rather than displayed.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — displayed as eq:agg-consumption-growth
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — displayed as eq:displacement
3. CRRA utility $U_0^H$ — displayed as eq:utility
4. P/D ratio formulas — displayed in Proposition 1
5. Existence condition $A^j < 1$ — displayed in Remark 1
6. Post-transfer consumption — displayed as eq:transfer-consumption
7. Transfer ratio — displayed as eq:transfer-ratio

### Should appear in display math but currently inline
8. Dividend growth factors $\Gamma^{AI}$, $\Gamma^N$ — defined in a "where" clause inside Proposition 1 (line 143); these drive Corollary 1 and all comparative statics

### Prose assumptions (appropriately placed)
9. Household share $\alpha_t \in (0,1-\theta_t]$, $c_t^H = \alpha_t C_t$ — line 95, same paragraph as eq:agg-consumption-growth
10. Singularity probability $p$ — line 98, start of Singularity paragraph
11. Productivity boost $1+\eta$ — lines 101-102, enumerated list under Singularity
12. Extinction probability $\xi$ — line 106, enumerated list under Singularity
13. AI dividend $D_t^{AI} = \theta_t C_t$ and share expansion $\Delta\theta$ — lines 115, Assets bullet list
14. Market incompleteness (private AI capital) — lines 119-120, prominent \noindent after Assets list
15. $\gamma > 1$, $\beta \in (0,1)$ — line 122, start of Preferences paragraph
16. $\lambda > 1/2$ social efficiency — line 225, \noindent after Extension 1 enumeration
17. Veto mechanism — line 227, same setup block
18. Tax rate $\tau$, deadweight $\delta\tau$ — lines 248-249, setup prose before eq:transfer-consumption
19. Effective displacement $\phi_\text{eff}$ — line 256, inline prose only

## Section-level findings

### Section 2 (Model)
- Setup is well-organized into labeled \paragraph{} blocks (Consumption, Singularity, Assets, Preferences). Each block introduces its assumptions before later results use them.
- The singularity parameters ($p$, $\eta$, $\xi$, $\phi$) are introduced in a clear enumerated structure under the Singularity paragraph.
- Market incompleteness is stated prominently after the Assets list with emphasis on "cannot trade."
- Minor: $\Gamma^{AI}$ and $\Gamma^N$ are defined only in the "where" clause of Proposition 1 (item 8). Since these factors are the linchpin of Corollary 1 and all comparative statics, elevating them to a labeled display equation would improve scannability. This is a presentation suggestion, not a clarity failure.

### Section 3 (Quantitative Analysis)
- Calibration parameters are stated clearly at the start of the section. No new model assumptions are introduced.

### Section 4.1 (Extension 1: Veto)
- The positive-singularity probability $\lambda$ and social efficiency condition $\lambda > 1/2$ are introduced before Proposition 3 in a clear setup block.
- The extinction-utility normalization ($U_\text{ext} = 0$) is flagged with a citation to Jones (2024) and its conservative direction is noted.
- The veto cost is described in prose rather than formalized, which is appropriate for this qualitative extension.

### Section 4.2 (Extension 2: Transfers)
- The transfer mechanism ($\tau$, $\delta$) is introduced in setup prose immediately before the display equation.
- $\phi_\text{eff}$ is defined only in inline prose (item 19); a display equation would help since it is the bridge between transfers and the baseline P/D formula.
- The transfer ratio (eq:transfer-ratio) is properly displayed and its independence from $\eta$ is highlighted.

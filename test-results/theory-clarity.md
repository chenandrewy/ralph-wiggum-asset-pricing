# tests/theory-clarity.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 2m 34s
[ralph-garage/agent-logs/20260412T095842.932633-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.932633-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly labeled setup paragraphs or display math before the results that depend on them; minor presentation choices (theta update in prose, Gamma factors inside Proposition 1) do not impede reader comprehension.

## Key items identified

### Should appear in display math (most critical)
- **Aggregate consumption growth** $C_{t+1} = (1+g)C_t$ — displayed (eq 1)
- **Displacement rule** $\alpha_{t+1} = \phi\alpha_t$ — displayed (eq 2)
- **CRRA utility** — displayed (eq 3)
- **P/D ratios** — displayed (eqs 4-5, Proposition 1)
- **Existence condition** $A^j < 1$ — displayed (eq 6, Remark 1)
- **Post-transfer consumption** — displayed (eq 7)
- **Effective displacement** $\phi_\text{eff}$ — displayed (eq 8)
- **Transfer ratio** — displayed (eq 9)
- **AI dividend share update** $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — currently prose only (bullet list, line 104)
- **Dividend growth factors** $\Gamma^{AI}, \Gamma^{N}$ — currently defined inside Proposition 1 only

### May remain in prose (at paragraph start)
- Household consumption share $c_t^H = \alpha_t C_t$ — prose, line 84, immediately after eq 1
- Singularity probability $p$ — prose, line 87, opens Singularity paragraph
- Extinction $\xi$ — prose, line 95, enumerated list item
- Productivity jump $1+\eta$ — prose, line 90, enumerated list item
- AI/non-AI dividend definitions — prose, lines 104-105, bullet items in Assets paragraph
- Market incompleteness — prose, lines 110-111, opens its own paragraph
- Positive singularity and $q > 1/2$ — prose, line 200, opens Extension 1
- Veto cost $\kappa$ — prose, line 204
- Extinction utility normalization $U_\text{ext} = 0$ — prose, line 204
- Tax rate $\tau$, deadweight cost $\delta$ — prose, line 239, opens transfer mechanism paragraph
- Complete markets consumption — prose, line 206

## Section-level findings

### Section 2.1 (Setup)
All key assumptions are introduced in clearly labeled `\paragraph{}` blocks (Consumption, Singularity, Assets, Preferences). The most critical equations are displayed. The $\theta_{t+1}$ update rule and dividend definitions are in prose bullet points within the Assets paragraph — acceptable given the structured list format, though promoting $\theta_{t+1}$ to display math would help since $\Gamma^{AI}$ depends on it.

### Section 2.2 (Equilibrium prices)
The P/D ratios are displayed in Proposition 1. The $\Gamma^{AI}$ and $\Gamma^{N}$ factors are defined in the "where" clause of the proposition rather than in a preceding setup paragraph. Since these are derived quantities (functions of already-introduced parameters), this is standard practice, though displaying them before the proposition would aid readability. The existence condition appears in Remark 1 immediately after Proposition 1 — well-placed.

### Section 2.3 (Discussion)
No new model assumptions. Correctly recalls and interprets earlier assumptions.

### Section 3 (Quantitative Analysis)
No new model assumptions. Parameter values stated clearly at the start.

### Section 4.1 (Veto extension)
New assumptions ($q$, positive singularity, $\kappa$, social efficiency, extinction utility normalization, complete markets consumption) are all introduced in setup prose at or near paragraph starts before Proposition 3. The condition $\phi(1+\eta) < 1$ appears first inside the proof (line 222), but this is a parametric restriction stated within a proof, not a new model assumption.

### Section 4.2 (Government transfers)
New assumptions ($\tau$, $\delta$, transfer mechanism) are introduced in setup prose before the display equations. The post-transfer consumption equation and $\phi_\text{eff}$ are both displayed.

### Appendix A
No new assumptions. Derives results from already-introduced objects.

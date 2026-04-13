# tests/theory-clarity.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 2m 34s
[ralph-garage/agent-logs/20260412T201203.499755-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.499755-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Nearly all key model assumptions are introduced in dedicated setup paragraphs with the most critical expressions in display math; the one notable gap is that the AI dividend share update rule ($\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$) appears only in a bullet point rather than display math, despite being the single expression that drives the valuation spread.

## Key items identified

### Should appear in display math (most critical expressions)
| # | Item | Currently in display math? | Results that depend on it |
|---|------|---------------------------|--------------------------|
| 1 | Aggregate consumption growth $C_{t+1} = (1+g)C_t$ | Yes (eq. 1) | All P/D ratios, SDF, veto |
| 2 | Displacement rule $\alpha_{t+1} = \phi\,\alpha_t$ | Yes (eq. 2) | Props 1, 2, 3; transfers |
| 3 | CRRA utility with $\gamma > 1$ | Yes (eq. 3) | All three propositions |
| 4 | **AI dividend share update $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$** | **No — prose bullet only** | Props 1, 2; quantitative analysis; drives $\Gamma^{AI} \neq \Gamma^{N}$ |
| 5 | Post-transfer consumption $c^H_{post}$ | Yes (eq. 6) | Extension 2, transfer ratio |
| 6 | Effective displacement $\phi_\text{eff}$ | Yes (eq. 7) | Extension 2 pricing |

### May remain in prose (should be at or near paragraph start)
| # | Item | At paragraph start? |
|---|------|-------------------|
| 7 | Household share $c_t^H = \alpha_t C_t$ | Yes (second sentence of Consumption paragraph, immediately after eq. 1) |
| 8 | Singularity probability $p$ | Yes (opens Singularity paragraph) |
| 9 | Extinction probability $\xi$ | Acceptable (item 2 in enumerated list under Singularity paragraph) |
| 10 | Productivity jump $1+\eta$ | Acceptable (item 1 in same enumerated list) |
| 11 | Market incompleteness | Yes (opens the sub-paragraph after the Assets bullets) |
| 12 | Positive singularity with probability $q$, $\alpha_{t+1} = \min(1,\alpha/\phi)$ | Yes (opens Extension 1) |
| 13 | Assumption $q > 1/2$ | End of opening paragraph — acceptable since it's in the same setup paragraph |
| 14 | Veto cost $\kappa > 0$ | Yes (opens veto-setup paragraph) |
| 15 | Complete markets assumption | Yes (opens complete-markets paragraph) |
| 16 | Transfer mechanism $\tau$, deadweight cost $\delta\tau$ | Yes (opens "We model this as follows" paragraph) |
| 17 | Condition $\phi(1+\eta) < 1$ | Parenthetical mid-paragraph — but this is an implication of the model, not a new assumption |

## Section-level findings

### Section 2.1 (Setup)
The model setup uses dedicated `\paragraph{}` blocks (Consumption, Singularity, Assets, Preferences), each introducing assumptions clearly. The singularity structure uses a well-organized enumerated list. The main issue: **item 4** — the $\theta$ update rule is buried in a bullet and is not in display math. This is the expression that determines $\Gamma^{AI}$ vs. $\Gamma^{N}$ and therefore the entire valuation spread. Elevating it to a numbered equation would improve navigability. The $\alpha$ vs. $\theta$ distinction is explained in a subsequent prose paragraph (line 108), which is helpful but could be more prominent.

### Section 2.2 (Equilibrium prices)
The P/D ratio formulas are in display math inside Proposition 1. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined in the "where" clause of the proposition — acceptable since they are derived quantities defined at first use, not new assumptions. The existence condition $A^j < 1$ is presented in a formal Remark with display math (Remark 1), which is appropriate. The condition $\phi(1+\eta) < 1$ appears only as a parenthetical (line 153) but is an implication of parameter choices rather than a new assumption.

### Section 2.3 (Discussion)
No new model assumptions. Correctly serves as interpretation. No issues.

### Section 3 (Quantitative Analysis)
Calibration values are stated clearly in a single sentence (line 185). No new assumptions introduced. No issues.

### Section 4.1 (Veto extension)
New assumptions (positive singularity $q$, veto cost $\kappa$, complete markets) are each introduced at or near the start of their respective paragraphs. The $U_\text{ext} = 0$ normalization is introduced in the veto-cost paragraph (line 204), which is the point where it first matters. No issues.

### Section 4.2 (Transfers extension)
The transfer mechanism is introduced in a clear setup paragraph ("We model this as follows"), followed immediately by the post-transfer consumption equation in display math. The effective displacement parameter $\phi_\text{eff}$ and transfer ratio are both in display math. No issues.

### Appendix A (Proof)
No new model assumptions. The Euler equation is presented in display math. No issues.

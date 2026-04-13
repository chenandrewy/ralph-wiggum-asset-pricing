# tests/theory-clarity.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 2m 29s
[ralph-garage/agent-logs/20260412T202602.579774-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.579774-0400_theory-clarity_claude_opus.log)

# theory-clarity

VERDICT: PASS
REASON: All key model assumptions are introduced in clearly labeled setup paragraphs or display math; the most critical expressions appear in display equations; prose assumptions appear at or near the start of their paragraphs.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq (1), Consumption paragraph
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq (2), Singularity enumeration
3. AI dividend-share update $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — eq (3), Assets paragraph
4. CRRA utility $U_0^H$ — eq (4), Preferences paragraph
5. P/D ratio closed forms — eqs (5)-(6), Proposition 1
6. Existence condition $A^j < 1$ — eq (7), Remark 1
7. Transfer consumption $c^H_{post}$ — eq (8), Extension 2 setup
8. Effective displacement $\phi_\text{eff}$ — eq (9), Extension 2
9. Transfer ratio — eq (10), Extension 2

### May remain in prose (all appear at/near paragraph starts)
10. Household share $c_t^H = \alpha_t C_t$ — inline math, immediately after eq (1)
11. Singularity probability $p$, extinction probability $\xi$ — start of Singularity paragraph
12. Productivity jump $(1+\eta)$ — start of singularity enumeration item
13. Dividend definitions $D^{AI} = \theta_t C_t$, $D^N = (1-\theta_t)C_t$ — start of Assets bullet items
14. Market incompleteness — start of its own paragraph (line 116)
15. Veto parameters $q$, $\kappa$ — start of Extension 1 subsection
16. Transfer parameters $\tau$, $\delta$ — start of paragraph in Extension 2

### Borderline item
17. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined as inline math within Proposition 1 statement, not in display math. These are derived quantities whose definitions appear naturally within the formal proposition block, then discussed extensively in the text following the proposition (line 159). Acceptable placement.

## Section-level findings

**Section 2.1 (Setup):** Well-organized with labeled paragraphs (Consumption, Singularity, Assets, Preferences). All structural assumptions appear in display math or at the start of their paragraph/item. The condition $\phi(1+\eta) < 1$ (household consumption falls despite aggregate growth) is mentioned mid-paragraph in line 117 rather than stated prominently as a maintained assumption, but it is a derived condition from stated parameters $\phi$ and $\eta$, not a new independent assumption.

**Section 2.2 (Equilibrium prices):** P/D ratios and existence condition are in display math within formal blocks (Proposition 1, Remark 1). $\Gamma^{AI}$ and $\Gamma^{N}$ are defined inline within the proposition rather than in their own display equation, but the proposition is a formal block and they are immediately discussed afterward.

**Section 2.3 (Discussion):** Recalls and interprets earlier assumptions; no new model assumptions introduced.

**Section 3 (Quantitative Analysis):** Calibration values stated at the start of the section paragraph. No new structural assumptions.

**Section 4.1 (Extension 1 — Veto):** New parameters $q$ and $\kappa$ introduced at the start of the subsection. Complete-markets benchmark stated in a setup paragraph before the proposition. The veto utility expression appears in display math within the proof.

**Section 4.2 (Extension 2 — Transfers):** Transfer mechanism ($\tau$, $\delta$) introduced at the start of a setup paragraph, followed immediately by display math. $\phi_\text{eff}$ in display math. Transfer ratio in display math.

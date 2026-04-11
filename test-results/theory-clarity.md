# tests/theory-clarity.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260410T221541.743134-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260410T221541.743134-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly labeled setup paragraphs before any results invoke them; the most critical expressions appear in display math, with one notable gap in the dividend growth factors.

## Key Items Identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq. (1), display in "Consumption" paragraph
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq. (2), display in "Singularity" paragraph
3. CRRA utility — eq. (3), display in "Preferences" paragraph
4. Existence condition $A^j < 1$ — eq. (4), display in Remark 1
5. Transfer consumption $c^H_{post}$ — eq. (5), display in Section 4.2
6. Effective displacement $\phi_\text{eff}$ — eq. (6), display in Section 4.2
7. Transfer ratio $c^H_{post}/c^H_{\text{no-transfer}}$ — eq. (7), display in Section 4.2

### In prose but correctly placed at paragraph/item start
1. Household share $c_t^H = \alpha_t C_t$, $\alpha_t \in (0,1)$ — line 83, immediately after eq. (1)
2. Singularity probability $p$, extinction probability $\xi$, productivity boost $\eta$ — lines 86–95, opening the "Singularity" paragraph
3. $\gamma > 1$, $\beta \in (0,1)$ — line 112, opening the "Preferences" paragraph
4. AI owners hold private capital — line 74, opening sentence of Setup
5. Market incompleteness (cannot buy restricted shares) — lines 109–110, dedicated paragraph
6. AI dividend $D_t^{AI} = \theta_t C_t$ and share evolution $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — line 103, opening the AI stocks bullet
7. Positive singularity $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ — line 203, start of Extension 1
8. Veto mechanism and cost — line 205, setup prose before Proposition 3
9. Deadweight cost fraction $\delta\tau$ — line 230, setup prose before eq. (5)
10. Extinction utility normalized to zero — line 205, setup prose in Extension 1

### Gap: defined only inside a proposition
- Dividend growth factors $\Gamma^{AI}$ and $\Gamma^N$ — currently defined as a "where" clause inside Proposition 1 (line 133), not as a standalone display equation in the model setup

## Section-Level Findings

### Section 2.1 (Setup)
The model setup is well-organized with labeled paragraphs (Consumption, Singularity, Assets, Preferences). All foundational assumptions are introduced in their own paragraphs before any results. Minor note: the AI and non-AI dividend definitions and the $\theta$ evolution rule are in prose bullets rather than display math; this is an acceptable presentation choice given that they are simple definitions clearly stated at the top of their respective bullets.

### Section 2.2 (Equilibrium Prices)
The P/D ratio formulas are in display math (Proposition 1). The dividend growth factors $\Gamma^{AI}$ and $\Gamma^N$ are the most important objects for understanding the hedging channel — every comparative static and the transfer extension depend on the comparison $\Gamma^{AI} > \Gamma^N$. They are currently defined only as a subordinate "where" clause at the end of Proposition 1. Promoting them to a standalone display equation (either in the Assets paragraph or just before Proposition 1) would improve findability. This is the paper's single notable clarity gap, but it does not rise to a failure: the factors are clearly labeled and defined within the proposition where they first appear.

### Section 2.3 (Discussion)
No new assumptions. Correctly recalls earlier setup without re-introducing anything.

### Section 3 (Quantitative Analysis)
All calibration parameters are stated in the opening paragraph with clear values. No new model assumptions.

### Section 4.1 (Extension 1: Veto)
The positive singularity, veto mechanism, and extinction-utility normalization are all introduced in setup prose before Proposition 3. Correctly placed.

### Section 4.2 (Extension 2: Transfers)
The transfer mechanism, deadweight cost, and all new expressions ($c^H_{post}$, $\phi_\text{eff}$, transfer ratio) are introduced in setup prose and display math before any results invoke them. Well-structured.

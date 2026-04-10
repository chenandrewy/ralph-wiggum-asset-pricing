# tests/theory-clarity.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 1m 50s
[ralph-garage/agent-logs/20260409T220435.843994-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.843994-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly labeled setup paragraphs or display math; critical expressions appear in display equations; prose assumptions appear at or near the start of their paragraphs.

## Key Items Identified

### Display math (main text)
1. Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq (1)
2. Displacement rule $\alpha_{t+1}=\phi\,\alpha_t$ — eq (2)
3. CRRA utility — eq (3)
4. P/D ratios for AI and non-AI stocks — eqs (4)–(5), Proposition 1
5. Existence condition $A^j<1$ — eq (6), Remark 1
6. Post-transfer consumption — eq (7)
7. Effective displacement $\phi_\text{eff}$ — eq (8)
8. Transfer consumption ratio — eq (9)
9. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined inline in Proposition 1

### Prose assumptions (at paragraph start)
a. Household share $c_t^H = \alpha_t C_t$, $\alpha_t\in(0,1)$ — Consumption paragraph
b. Singularity probability $p$ — Singularity paragraph opening
c. Productivity jump $(1+\eta)$ — first enumerate item in Singularity paragraph
d. Extinction probability $\xi$ — second enumerate item in Singularity paragraph
e. AI dividend share $D_t^{AI}=\theta_t C_t$ and jump rule — Assets paragraph, first bullet
f. Non-AI dividends $D_t^N=(1-\theta_t)C_t$ — Assets paragraph, second bullet
g. Market incompleteness — Assets paragraph, closing sentence (emphasized with italics)
h. Positive singularity $\alpha_{t+1}=\min(1,\alpha_t/\phi)$ — Extension 1 opening paragraph
i. Veto mechanism — Extension 1, second setup paragraph
j. Transfer mechanism ($\tau$, $\delta\tau$) — Extension 2 setup paragraph

## Section-Level Findings

**Section 2.1 (Setup):** All assumptions are introduced in four clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences). Each paragraph leads with its key assumption. The singularity structure uses a well-organized enumerate block. Display math is used for the three most critical expressions (consumption growth, displacement, utility). Prose assumptions (household share, singularity probability, extinction probability, dividend definitions) all appear at or near the start of their respective paragraphs or list items.

**Section 2.2 (Equilibrium prices):** The P/D ratios and existence condition appear in display math within Proposition 1 and Remark 1. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined inline at the end of Proposition 1's display equations. These are derived quantities rather than new assumptions, and they appear in display math (within the proposition environment), so this is acceptable. The discussion paragraph after Proposition 1 correctly highlights the key comparison $\Gamma^{AI}>\Gamma^{N}$ and explains the hedging channel.

**Section 2.3 (Discussion):** No new assumptions; recalls earlier setup correctly.

**Section 3 (Quantitative Analysis):** Lists calibration parameters clearly. No new model assumptions introduced.

**Section 4.1 (Extension 1 — Veto):** The positive singularity and veto mechanism are introduced in clear setup paragraphs before Proposition 3. The extinction-utility normalization is stated explicitly with attribution.

**Section 4.2 (Extension 2 — Transfers):** The transfer mechanism is introduced in a setup paragraph, immediately followed by display math for the post-transfer consumption equation. The effective displacement parameter and transfer ratio both appear in labeled display equations. The connection back to Proposition 1's P/D formula (with $\phi$ replaced by $\phi_\text{eff}$) is stated explicitly.

**Minor note:** $\Gamma^{AI}$ and $\Gamma^{N}$ could be given their own standalone labeled display equation for easier cross-referencing, since they are central to the hedging-channel intuition and are invoked repeatedly in the comparative statics proofs. This is a stylistic preference, not a clarity failure — they are already visible in display math within the proposition.

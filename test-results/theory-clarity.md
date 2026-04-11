# tests/theory-clarity.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 2m 22s
[ralph-garage/agent-logs/20260411T161024.923490-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.923490-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are presented in named setup paragraphs with critical expressions in display math; minor issues do not impede a careful reader.

## Key Items Identified

**Display math (present and correctly placed):**
- K1: Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq (1), line 83
- K4: Displacement rule $\alpha_{t+1}=\phi\alpha_t$ — eq (2), line 94
- K10: CRRA utility — eq (3), lines 119–121
- K12: Existence condition $A^j<1$ — eq (3) in Remark 1, line 148
- K15: Transfer consumption $c^H_{post}$ — eq (5), lines 243–245
- K16: Effective displacement $\phi_\text{eff}$ — eq (6), lines 251–253

**Prose (correctly placed at or near paragraph/bullet starts):**
- K2: Household consumption $c_t^H = \alpha_t C_t$ — line 86, immediately after eq (1)
- K3: Singularity probability $p$ — line 89, opens Singularity paragraph
- K5: Productivity jump $(1+\eta)$ — line 92, leads numbered list item
- K6: Extinction probability $\xi$ — line 97, leads numbered list item
- K7: AI dividend share $D_t^{AI}=\theta_t C_t$ and update rule — lines 106–107, leads bullet
- K8: Non-AI dividends $D_t^N=(1-\theta_t)C_t$ — line 107, leads bullet
- K9: Market incompleteness — lines 112–113, opens its own paragraph
- K13: Positive singularity with prob $q$ — lines 202–203, opens Extension 1 setup
- K14: Veto cost $\kappa$ — line 206, opens veto paragraph

**Items with placement notes:**
- K11: Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined inline within Proposition 1 statement (line 138), not as standalone display math
- K17: Condition $\phi(1+\eta)<1$ — appears only in the proof of Proposition 3 (line 224)

## Section-Level Findings

### Section 2.1 (Setup)
No issues. The setup uses named `\paragraph` blocks (Consumption, Singularity, Assets, Preferences). Each introduces its assumptions clearly: critical expressions in display math, secondary definitions at paragraph or bullet starts. Market incompleteness (K9) has its own paragraph beginning "AI owners also hold restricted equity..." with the key statement emphasized.

### Section 2.2 (Equilibrium Prices)
Minor note: $\Gamma^{AI}$ and $\Gamma^{N}$ (K11) are defined as a trailing "where" clause inside Proposition 1 rather than as standalone display equations. These factors carry the paper's central intuition ($\Gamma^{AI}>\Gamma^{N}$ drives the valuation spread). However, they are immediately discussed in the paragraph following Proposition 1 (lines 155–157), which explains the economic content clearly. Defining auxiliary quantities inside a proposition statement is standard practice in finance journals, so this does not constitute a clarity failure.

The Euler equation appears only in the appendix (line 297). The main text states at line 125 that "the household prices all publicly traded assets via its Euler equation" and that the SDF "reflects its own consumption growth, not aggregate consumption growth." Deferring the formal Euler equation to the appendix is conventional for applied theory papers.

### Section 2.3 (Discussion)
No issues. Recalls earlier assumptions rather than introducing new ones.

### Section 3 (Quantitative Analysis)
No issues. Parameterizations are stated clearly in prose (line 187). The condition $\phi(1+\eta)=0.75$ is given explicitly, grounding the displacement magnitude.

### Section 4.1 (Extension 1: Veto)
Minor note: The condition $\phi(1+\eta)<1$ (K17) first appears inside the proof of Proposition 3 (line 224) rather than in the setup paragraphs. This is the parametric condition ensuring household consumption actually falls upon singularity, which is what drives the veto incentive. However, this is an implication of the already-stated parameters ($\phi\in(0,1)$, $\eta>0$), not a new model assumption, and the quantitative section already established that $\phi(1+\eta)=0.75<1$. The condition is also implied by the verbal description ("the household's share drops"). Not a clarity failure but could be stated more prominently.

### Section 4.2 (Extension 2: Transfers)
No issues. The transfer mechanism is introduced in a clear setup paragraph (lines 241–242) followed by display math (eq 5). The effective displacement parameter gets its own display equation (eq 6).

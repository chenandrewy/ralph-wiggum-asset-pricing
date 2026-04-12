# tests/theory-clarity.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 2m 2s
[ralph-garage/agent-logs/20260412T093252.130722-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.130722-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with display math for the most critical expressions; minor presentation issues do not impede a careful reader.

## Key items identified

**Display math (present in main text):**
1. Aggregate consumption growth: $C_{t+1} = (1+g)C_t$ — eq (1)
2. Displacement rule: $\alpha_{t+1} = \phi\alpha_t$, $\phi\in(0,1)$ — eq (2)
3. CRRA utility — eq (3)
4. P/D ratio formulas with $\Gamma^{AI}$, $\Gamma^{N}$ — eqs (4)–(5), in Proposition 1
5. Existence condition $A^j < 1$ — eq (6), in Remark 1
6. Transfer consumption — eq (8)
7. Effective displacement $\phi_\text{eff}$ — eq (9)
8. Transfer ratio — eq (10)

**Prose assumptions (should be near paragraph start):**
9. Household share $c_t^H = \alpha_t C_t$; AI owners get remainder
10. Singularity probability $p$; extinction probability $\xi$
11. Non-extinction productivity jump $1+\eta$
12. AI dividend share $\theta_t$ and update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
13. Market incompleteness: household cannot trade restricted AI equity
14. Preferences: $\gamma > 1$, $\beta \in (0,1)$
15. Positive singularity probability $q > 1/2$ (Extension 1)
16. Veto cost $\kappa > 0$ (Extension 1)
17. Tax rate $\tau$, deadweight cost parameter $\delta$ (Extension 2)

## Section-level findings

### Section 2.1 (Setup)
- **Consumption paragraph:** Item 1 is in display math. Item 9 (household share) follows immediately after eq (1) in the same paragraph — clear placement.
- **Singularity paragraph:** Item 10 ($p$) opens the paragraph. Items 11 ($\eta$) and the extinction channel ($\xi$) are introduced in a numbered list — structured and readable. Item 2 (displacement rule) is in display math within the list.
- **Assets paragraph:** Items 12 ($\theta$ update) and 13 (market incompleteness) are introduced in structured bullet points and a follow-up paragraph. The $\theta$ update rule is inline in a bullet rather than display math; since $\Gamma^{AI}$ vs $\Gamma^{N}$ (the entire source of the valuation spread) depends on $\Delta\theta$, promoting this to display math would help readers locate it on re-reading. Minor issue, not a failure.
- **Preferences paragraph:** Items 14 ($\gamma > 1$, $\beta$) and item 3 (utility) open the paragraph with display math. Clear.

### Section 2.2 (Equilibrium prices)
- Items 4–5 (P/D ratios) appear as display math inside Proposition 1. Item 5 (existence condition) appears as display math in Remark 1. Both are appropriately placed.
- The $\Gamma^{AI}$, $\Gamma^{N}$ definitions appear in the proposition statement and are immediately discussed in the paragraph following the proof. Clear.

### Section 4.1 (Veto and efficient development)
- Items 15–16: the positive singularity ($q$, $\alpha^+$) and $q > 1/2$ are introduced in the opening paragraph of Section 4.1. The $q > 1/2$ assumption appears at the end of this paragraph rather than the start, but the paragraph is short and the assumption is clearly stated.
- Item 16 ($\kappa$): introduced at the start of its own paragraph ("The household can veto..."). Clear.
- The veto utility expression $\Delta u(\gamma)$ (eq 7) appears only in the proof of Proposition 3. Per the evaluation rules, conditions inside proofs are not themselves new model assumptions, so this is not a failure. However, since $\Delta u(\gamma)$ is discussed in the post-proof interpretation, displaying it in the main text would improve accessibility.

### Section 4.2 (Government transfers)
- Items 17 ($\tau$, $\delta$): introduced in a clearly labeled setup paragraph ("We model this as follows..."). Items 6–8 (transfer consumption, $\phi_\text{eff}$, transfer ratio) are all in display math. Clear and well-structured.

### Overall
The paper's model-setup sections use labeled paragraphs (\paragraph{Consumption}, \paragraph{Singularity}, etc.) and display math for all critical expressions. Prose assumptions generally appear at or near the start of their paragraphs. No key assumption is introduced only inside a proposition or proof in a way that would leave a reader unable to follow the results.

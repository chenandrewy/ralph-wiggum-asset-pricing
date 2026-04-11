# tests/theory-clarity.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 2m 10s
[ralph-garage/agent-logs/20260411T103039.126858-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.126858-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Most key model assumptions are introduced in clearly labeled setup paragraphs with display math; two items could be more prominent but do not impair readability.

## Key Items Identified

### Should appear in display math (and do)
1. **Aggregate consumption growth** $C_{t+1} = (1+g)C_t$ — eq. (1), display math in §2.1
2. **Displacement rule** $\alpha_{t+1} = \phi\alpha_t$ — eq. (2), display math in §2.1
3. **CRRA utility** — eq. (3), display math in §2.1
4. **P/D ratios** — eqs. (4)–(5), display math in Proposition 1
5. **Existence condition** $A^j < 1$ — eq. (6), display math in Remark 1
6. **Post-transfer consumption** — eq. (8), display math in §4.2
7. **Effective displacement** $\phi_\text{eff}$ — eq. (9), display math in §4.2
8. **Transfer ratio** — eq. (10), display math in §4.2

### Should appear in display math but currently do not
9. **AI dividend share transition** $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — inline in a bullet list (line 105)
10. **Dividend growth factors** $\Gamma^{AI}$, $\Gamma^{N}$ — inline after Proposition 1 (line 137)

### May remain in prose (introduced prominently enough)
11. **Household consumption share** $c_t^H = \alpha_t C_t$ — prose immediately after eq. (1)
12. **Singularity probability** $p$ — opens the "Singularity" paragraph
13. **Extinction probability** $\xi$ — in numbered list within "Singularity" paragraph
14. **Productivity jump** $(1+\eta)$ — in numbered list within "Singularity" paragraph
15. **Market incompleteness** (restricted equity not tradeable) — dedicated paragraph in §2.1
16. **Extension 1 parameters** ($q$, $\kappa$, complete-markets consumption) — in opening paragraphs of §4.1
17. **Extension 2 parameters** ($\tau$, $\delta$) — opens the transfer-model paragraph in §4.2

### Introduced mid-paragraph or late; could be more prominent
18. **Condition $\phi(1+\eta) < 1$** — first appears mid-paragraph in §2.2 discussion (line 154), not in model setup; invoked in Proposition 2, Proposition 3 proof, and Extension 2

## Section-Level Findings

### §2.1 Setup
- Well-structured with labeled paragraph headings (Consumption, Singularity, Assets, Preferences).
- Key equations (1)–(3) are in display math. The singularity probability, extinction probability, and productivity jump are introduced within a clear numbered list.
- **Minor issue:** The AI dividend share transition rule ($\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$, item 9) is stated inline within a bullet point rather than in display math. This rule drives the entire valuation spread through $\Gamma^{AI} > \Gamma^{N}$. Promoting it to display math would help readers locate and reference it.
- Market incompleteness gets a dedicated paragraph — clear and prominent.

### §2.2 Equilibrium Prices
- P/D ratios appear in display math within Proposition 1. The existence condition is in display math in Remark 1.
- **Minor issue:** The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ (item 10) are defined inline in the "where" clause of Proposition 1 rather than in their own display equation in the setup. Since these factors are the core objects distinguishing AI from non-AI valuations and are referenced in Proposition 2 and the quantitative analysis, a standalone display equation in §2.1 would improve findability.
- **Minor issue:** The condition $\phi(1+\eta) < 1$ (item 18) first appears parenthetically mid-paragraph in the discussion below Proposition 1 (line 154). It is later used as a load-bearing condition in the Proposition 3 proof and the large-singularity extension. Stating it explicitly in §2.1 (e.g., as a labeled assumption or at the start of the displacement discussion) would make it easier for readers to track.

### §3 Quantitative Analysis
- Parameter values are clearly listed. Results reference Proposition 2 appropriately. No new model assumptions are introduced here — all rely on previously defined objects.

### §4.1 Extension 1 (Veto)
- New parameters ($q$, $\kappa$, positive singularity) are introduced in setup prose at the start of the subsection. The positive singularity probability $q > 1/2$ and the veto cost $\kappa$ are stated clearly in opening paragraphs before Proposition 3.
- Complete-markets consumption is stated in prose one paragraph before Proposition 3 — adequately prominent.

### §4.2 Extension 2 (Transfers)
- Tax rate $\tau$ and deadweight cost $\delta$ are introduced in prose immediately before display eq. (8). The post-transfer consumption, effective displacement, and transfer ratio all appear in display math.
- Well-structured: each new object gets its own display equation with surrounding explanation.

## Summary
The paper's model setup is clearly organized and most critical expressions appear in display math. Two items — the $\theta$ transition rule and the $\Gamma$ factors — would benefit from promotion to display math given their centrality to the pricing results. The condition $\phi(1+\eta) < 1$ would benefit from earlier, more prominent introduction. These are improvements rather than failures: the paper is readable and the key assumptions are findable.

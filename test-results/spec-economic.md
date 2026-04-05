# tests/spec-economic.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 1m 42s
[ralph-garage/agent-logs/20260404T235928.980823-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.980823-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions across all sections.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usages:**
- Abstract: "a devastating AI singularity" — consistent.
- Introduction (line 55): "An AI singularity---a sudden, dramatic improvement in AI capability---would vastly increase total economic output." — consistent; "capability" is slightly broader than "productivity" but the economic consequence ("vastly increase total economic output") matches the spec.
- Model §2.2 (line 106): "an AI singularity occurs" followed by "Total output jumps by factor $G > 1$: the economy becomes vastly more productive." — consistent.
- Model §2.2 (line 128): "When $\Lambda < 1$---a *negative* AI singularity---the household's consumption falls despite a massive increase in total output." — consistent with "devastating for the typical investor" since the household is the representative investor.
- Extensions §4.3 (line 288): singularity that "destroys all life rather than generating growth" — this is extinction, not the core singularity; the paper correctly treats it as a separate conditional event, not a redefinition.

**Cross-section consistency:** The term maintains the same meaning (sudden output expansion, G > 1) throughout model, results, extensions, and conclusion. The "negative" qualifier consistently means Λ < 1 (devastating for the household). No drift.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- The household consumes all publicly traded output: pre-singularity $C_t = Y_t$, post-singularity $C_t = (1-\phi)GY_\tau(1+g)^{t-\tau}$.
- AI capital owners capture fraction $\phi$ of post-singularity output; the household receives $(1-\phi)$.
- These shares sum to 1: the budget constraint is satisfied.
- In the transfer extension (line 249): $\Lambda(\theta, \delta) = [(1-\phi) + (1-\delta)\theta\phi]G$ — the household gains $(1-\delta)\theta\phi$ from transfers, AI owners lose $\theta\phi$, and $\delta\theta\phi$ is destroyed. Accounting is internally consistent.

**No violations identified.**

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets means "some assets cannot be bought by the representative investor" — not Arrow-Debreu. Complete markets should "focus on the important assets that are unavailable to the representative investor" — also not Arrow-Debreu.

**Paper usages:**
- Model §2.3 (line 139): "The household cannot trade the private AI capital held by AI owners. This is the key friction." — correctly frames incomplete markets as inability to trade a specific asset class, not as absence of Arrow-Debreu securities.
- Results §3.2 (line 200): "Under complete markets, the household can trade claims on the private AI capital." — correctly frames complete markets as the household gaining access to the specific missing asset.
- Extensions §4.2 (line 272): "Under complete markets, the household shares in the full output gains from the singularity." — consistent.
- No Arrow-Debreu language appears anywhere in the paper.

**Cross-section consistency:** The complete/incomplete distinction is always framed in terms of access to private AI capital, matching the spec's requirement throughout.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Introduction (line 55): "Publicly traded AI stocks partially hedge this displacement because their dividends grow relative to other stocks when the singularity arrives." — "partially hedge" is consistent with "need not be perfect." The framing is relative ("grow relative to other stocks") rather than absolute, but the mechanism is that AI stock dividends jump by factor $(\alpha_S/\alpha)\Lambda$ at the singularity while non-AI dividends jump by $((1-\alpha_S)/(1-\alpha))\Lambda$, so AI dividends do increase relative to non-AI dividends when displacement materializes.
- Results §3.1 (line 182): hedge factor $H^i$ captures "how much the singularity state contributes to the asset's value through the stochastic discount factor" — consistent; payoff increases in the singularity state.
- Results §3.3 (line 233): "AI stocks function as insurance: their value rises precisely because the disaster they hedge against becomes more likely." — metaphorical use of "insurance" to describe hedging behavior. This is a loose synonym, not a redefinition; the underlying mechanism (payoff increases when risk materializes) remains the same.

**Minor note:** The paper uses "hedging premium" to mean a P/D ratio premium (higher price), not a return premium. This is a natural pricing consequence of the hedging definition and is used consistently throughout; it does not conflict with the spec.

**Cross-section consistency:** Hedging always means "payoff increases when displacement risk materializes." No drift across sections.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium means "prices are determined by the equilibrium conditions" — not that consumption is endogenous. Partial equilibrium means "prices are exogenous."

**Paper usages:**
- The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere.
- The model's structure is consistent with general equilibrium per the spec: prices $(P_t^A, P_t^N)$ are determined by the household's Euler equations (equilibrium conditions), while consumption follows from the output process and displacement parameters.
- Consumption is exogenous (determined by the output process and singularity parameters), which is consistent with the spec's clarification that general equilibrium "does **not** mean that consumption is endogenous."

**No inconsistency.** The paper avoids the terms entirely, so there is nothing to conflict with the spec's definitions.

## Summary

All five concepts from the economic background spec are used consistently with their definitions across all sections of the paper (abstract, introduction, model, results, extensions, conclusion, and appendix). No terminology drift, no Arrow-Debreu framing for market completeness, no violations of budget constraints, and hedging is correctly defined in terms of payoffs increasing when risk materializes.

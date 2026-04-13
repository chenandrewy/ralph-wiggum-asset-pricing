# tests/spec-economic.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 2m 0s
[ralph-garage/agent-logs/20260412T200023.655591-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.655591-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usage:**
- Abstract: "AI singularity that displaces their consumption" -- consistent.
- Introduction (line 48): "a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption" -- consistent with both the general and negative definitions.
- Model (line 86--97): Singularity produces a consumption jump of factor $1+\eta$ (productivity boost) but the household's share drops by $\phi$. With the baseline $\phi(1+\eta) = 0.75$, household consumption falls 25% -- clearly "devastating for the typical investor."
- Extension 1 (line 200): Introduces a "positive singularity" where the household's share increases. This is distinct from the "negative" singularity and is not described as devastating -- consistent with the spec's definitions.
- Large singularity case (line 263): $\phi(1+\eta) = 0.5$, consumption halves -- devastating.
- Conclusion (line 281): "AI singularity that would displace their consumption" -- consistent.

**Cross-section consistency:** The term maintains the same meaning (sudden productivity jump) across all sections. The negative/positive distinction is used correctly throughout.

### 2. Budget Constraints

**Spec definition:** Budget constraints must be satisfied; violations are fundamental flaws.

**Paper usage:**
- Model (line 107): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." Dividend shares $\theta_t$ and $1-\theta_t$ sum to 1. Consumption shares $\alpha_t$ and $1-\alpha_t$ sum to 1. Budget constraints hold.
- Transfer equation (line 241--243): Household post-transfer consumption plus AI owners' post-tax consumption plus deadweight loss sums to total post-singularity output $(1+\eta)(1+g)C_t$. Budget constraint verified algebraically.

**Cross-section consistency:** No budget-constraint violations found anywhere in the paper.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = some assets cannot be bought by the representative investor. NOT necessarily Arrow-Debreu securities. Complete markets should focus on important assets unavailable to the representative investor.

**Paper usage:**
- Abstract (line 31): "markets are incomplete---investors cannot trade private AI capital" -- focuses on specific unavailable assets, consistent with spec.
- Introduction (line 48): "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." -- focuses on specific unavailable assets.
- Model (line 109): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." -- directly matches spec's focus on unavailable assets.
- Model (line 122): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." -- consequence of incompleteness, consistent.
- Extension 1 (line 206): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." -- complete markets defined as gaining access to the specific assets that were unavailable, consistent with spec.
- Conclusion (line 281): "market incompleteness---the inability to trade restricted AI equity" -- consistent.

**Cross-section consistency:** No mention of Arrow-Debreu securities. The concept is consistently defined as the inability to trade specific restricted AI assets across all sections. Complete markets consistently means gaining access to those specific assets.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**
- Abstract (line 31): "investors use AI stocks to hedge against an AI singularity" -- consistent.
- Introduction (line 48): "investors use AI stocks to partially insure against displacement from AI" -- uses "partially," consistent with spec's "need not be perfect."
- Model (line 152): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." -- payoff increases when displacement risk materializes, directly matches spec definition. "Partial" is consistent with "need not be perfect."
- Discussion (line 168): "displacement is fully hedged" under complete markets where $\phi_\text{eff} \to 1$ -- uses hedging as full insurance when all assets are available, consistent.
- Extension 2 (line 265): "transfers reduce the hedge value of AI stocks" -- hedging demand falls when displacement is cushioned by transfers, consistent.

**Cross-section consistency:** Hedging is consistently used as "payoff increases when displacement risk materializes." The paper consistently describes the hedge as partial, never claiming AI stocks perfectly hedge displacement. The paper does not claim AI stocks earn a negative risk premium, consistent with the spec's allowance.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = prices determined by equilibrium conditions (NOT that consumption is endogenous). Partial equilibrium = prices exogenous.

**Paper usage:**
- The paper uses "stationary equilibrium" (line 125) and "equilibrium prices" (line 120) -- prices are determined endogenously via the household's Euler equation, consistent with general equilibrium per the spec.
- Consumption growth is exogenous ($g$ is constant, displacement is mechanical through $\phi$) -- the spec explicitly notes that general equilibrium does NOT require consumption to be endogenous, so this is not a violation.
- The paper does not incorrectly label itself as "partial equilibrium" despite having exogenous consumption growth.
- The paper does not claim that having endogenous prices means consumption must be endogenous.

**Cross-section consistency:** No misuse of equilibrium terminology found.

## Summary

All five concepts from the economic background spec are used consistently with their definitions throughout the paper. No cross-section drift, definitional inconsistencies, or ambiguities that change economic meaning were found.

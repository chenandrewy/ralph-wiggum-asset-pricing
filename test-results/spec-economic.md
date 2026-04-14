# tests/spec-economic.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260414T102326.821012-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.821012-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions across every section.

## Concept-by-concept analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage:**

- **Abstract (line 31):** "AI singularity that displaces their consumption" — consistent: sudden event, displaces investor.
- **Introduction (line 48):** "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — directly matches spec definition.
- **Model, Singularity paragraph (line 86–97):** Singularity occurs with probability $p$; aggregate consumption jumps by $1+\eta$ (productivity boost = "vastly increases output"); household share drops by $\phi$ (devastating for investor). Consistent.
- **Extension 1 (line 205):** Introduces a "positive singularity" where household share increases. This is still an AI singularity (sudden productivity improvement) but not a negative one (household benefits). Consistent with spec — the spec defines "negative" as devastating; a positive singularity is simply an AI singularity that is not negative.
- **Conclusion (line 287):** "AI singularity that would displace their consumption" — consistent.

**Cross-section consistency:** The term keeps the same meaning (sudden productivity jump) in every section. The negative/positive distinction is introduced cleanly in Extension 1 and does not contradict earlier usage.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage:**

- **Model, Assets paragraph (line 111):** "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." Budget constraint satisfied.
- **Model, Assets paragraph (line 113):** "The household's consumption $\alpha_t C_t$ reflects the net outcome... AI owners receive the remainder." Shares sum to 1: $\alpha_t + (1 - \alpha_t) = 1$. Satisfied.
- **Extension 2, equation (7) (line 247–248):** Transfer consumption: $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. AI owners retain $(1-\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. The total is $(1+\eta)C_t(1+g)[1 - \delta\tau^2(1-\phi\alpha)]$, which is less than aggregate post-singularity consumption. The gap equals the deadweight loss $\delta\tau^2(1-\phi\alpha)(1+\eta)C_t(1+g)$, which is explicitly modeled as waste. Budget constraint satisfied with deadweight loss accounted for.

**Cross-section consistency:** No violations detected. All consumption shares sum correctly; transfers include explicit deadweight costs rather than creating resources.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage:**

- **Abstract (line 31):** "markets are incomplete---investors cannot trade private AI capital" — matches spec: specific assets unavailable.
- **Introduction (line 48):** "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — focuses on specific unavailable assets, not Arrow-Debreu.
- **Model, Assets paragraph (line 115–116):** "The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — directly matches spec.
- **Discussion (line 174):** "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." — complete markets framed as ability to trade the specific missing assets, not as Arrow-Debreu.
- **Extension 1 (line 211):** "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." — again, specific assets, not Arrow-Debreu.
- **Extension 2 (line 240):** "The ideal solution---broader trading of AI capital---faces the same constraint" — consistent framing.

**Cross-section consistency:** The paper never mentions Arrow-Debreu securities. Every reference to incomplete/complete markets focuses on the specific unavailable assets (restricted AI equity). Perfectly consistent with spec.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**

- **Abstract (line 31):** "investors use AI stocks to hedge against an AI singularity" — consistent: AI stocks' payoffs increase when singularity occurs.
- **Introduction (line 48):** "hedging motive: investors use AI stocks to partially insure against displacement" — "partially" matches spec's "need not be perfect."
- **Introduction (line 48):** "publicly traded AI stocks as the only available partial hedge against displacement" — consistent.
- **Model, Equilibrium prices (line 158):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — matches spec: payoff increases when risk materializes.
- **Model (line 117):** "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." — consistent: hedge is partial, not perfect.
- **Discussion (line 174):** "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged" — "fully hedged" used correctly for the complete-markets counterfactual.
- **Extension 2 (line 271):** "transfers reduce the hedge value of AI stocks, compressing P/D ratios" — consistent: reducing displacement risk reduces hedging demand.

**Cross-section consistency:** The paper consistently uses "partial hedge" for AI stocks under incomplete markets and correctly distinguishes this from full hedging under complete markets. The hedging concept matches the spec throughout.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage:**

The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium." Confirmed by text search: zero occurrences of either phrase.

The model's structure is consistent with general equilibrium by the spec's definition: prices are determined endogenously through the household's Euler equation (line 128: "The household prices all publicly traded assets via its Euler equation"), while aggregate consumption growth is exogenous ($C_{t+1} = (1+g)C_t$). The paper correctly avoids claiming that endogenous consumption is required for general equilibrium.

**Cross-section consistency:** No inconsistency possible since the terms are not used. The model's approach (endogenous prices, exogenous consumption growth) is consistent with the spec's definition of general equilibrium.

## Summary

All five concepts from the economic background spec are used consistently throughout the paper:

1. **AI Singularity:** Consistent definition and usage across all sections.
2. **Budget Constraints:** Satisfied in the model, quantitative analysis, and extensions.
3. **Complete/Incomplete Markets:** Always framed around specific unavailable assets, never Arrow-Debreu.
4. **Hedging:** Correctly used as partial hedge throughout, matching spec's definition.
5. **GE/PE:** Terms not used explicitly; model structure is consistent with spec definitions.

No inconsistencies, ambiguities that change economic meaning, or cross-section drift detected.

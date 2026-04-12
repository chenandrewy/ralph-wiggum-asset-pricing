# tests/spec-economic.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 2m 27s
[ralph-garage/agent-logs/20260412T093252.130588-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.130588-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Abstract:** "AI singularity that displaces their consumption" -- consistent; displacement of consumption is the mechanism by which it is devastating.
- **Introduction (line 48):** "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." -- consistent with spec. Adds specificity (labor income) without contradicting.
- **Model (line 86-97):** Singularity occurs with probability $p$; non-extinction singularity has "Aggregate consumption jumps by a factor $1+\eta$" -- consistent with "vastly increases productivity and output." Household share drops via $\phi$ -- consistent with "devastating for the typical investor."
- **Extension 1 (line 200):** Introduces a "positive singularity" where household share increases, alongside the baseline "negative" singularity. Both involve $\eta > 0$ (output increases), consistent with the spec's general definition. The positive/negative distinction is about distribution to the typical investor, matching the spec's framing.
- **Conclusion (line 281):** "AI singularity that would displace their consumption" -- consistent.

**Assessment:** Consistent across all sections. The term always denotes a sudden productivity improvement, and "negative" always denotes devastation for the typical investor via consumption displacement.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Model (line 83):** Household consumes $\alpha_t C_t$; AI owners receive $(1-\alpha_t)C_t$. Total = $C_t$. Budget satisfied.
- **Model (line 103-105):** $D^{AI} + D^{N} = C_t$. Paper explicitly states: "Total public dividends equal aggregate consumption." Budget satisfied.
- **Model (line 107):** Paper carefully distinguishes $\alpha_t$ (consumption share) from $\theta_t$ (dividend share) and explains how both sides receive their consumption through a mix of public dividends, labor income, and restricted equity -- no hidden resource creation.
- **Transfers (line 239-243):** Equation (8) decomposes household post-transfer consumption into displaced consumption plus net transfer. The transfer is funded by taxing AI owners' surplus, with deadweight loss $\delta\tau$ consuming part of it. Summing household + AI owners (post-tax) + deadweight loss = total post-singularity consumption $(1+\eta)(1+g)C_t$. Budget satisfied.

**Assessment:** No budget constraint violations detected. The paper is careful about accounting for all consumption flows.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Abstract:** "markets are incomplete---investors cannot trade private AI capital" -- directly matches spec definition.
- **Introduction (line 48):** "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." -- focuses on specific unavailable assets, consistent with spec.
- **Model (line 109):** "The household *cannot* purchase these restricted shares. This is the source of market incompleteness." -- directly matches spec.
- **Discussion (line 168):** "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$" -- complete markets defined by ability to trade specific assets, consistent with spec.
- **Extension 1 (line 206):** "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable." -- focuses on specific assets becoming available, exactly as spec requires.
- **Extension 2 (line 234):** "broader trading of AI capital---faces the same constraint" -- consistent framing.
- **Conclusion (line 281):** "the inability to trade restricted AI equity" -- consistent.

**Assessment:** Fully consistent. The paper never invokes Arrow-Debreu securities. Every reference to complete/incomplete markets focuses on specific assets (restricted AI equity) that are unavailable to the representative investor, exactly as the spec prescribes.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Abstract:** "investors use AI stocks to hedge against an AI singularity" -- consistent; AI stock dividends grow when singularity occurs.
- **Introduction (line 48):** "investors use AI stocks to partially insure against displacement from AI" -- "partially" consistent with "need not be perfect."
- **Model (line 152):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." -- directly matches: payoff increases when risk materializes; "partial" consistent with imperfect hedge.
- **Model (line 111):** "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." -- consistent with imperfect hedge.
- **Discussion (line 168):** "displacement is fully hedged" (under complete markets) -- appropriate use of the concept when the hedge becomes perfect.
- **Extension 2 (line 265):** "transfers reduce the hedge value of AI stocks" -- consistent; transfers reduce displacement risk, reducing the need for the hedge.

**Assessment:** Fully consistent. The paper always uses "hedge" to mean payoffs that increase when the risk materializes. It consistently qualifies with "partial" in the incomplete-markets setting, and never claims AI stocks earn negative risk premia.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere. It uses "stationary equilibrium" (line 125) and "Equilibrium prices" (section heading, line 120). Prices are determined endogenously through the household's Euler equation (an equilibrium condition), while consumption shares ($\alpha_t$) are exogenous parameters that change only through the singularity mechanism.

**Assessment:** No inconsistency. The paper avoids the GE/PE terminology entirely, which sidesteps any potential misuse. Its equilibrium concept (prices determined by Euler equation, consumption shares exogenous) is internally consistent and does not contradict the spec's definitions.

## Cross-Section Consistency Check

- **"Incomplete markets"**: Used in Abstract, Introduction, Model, Discussion, Extension 1, Extension 2, and Conclusion. Always refers to inability to trade restricted AI equity. No drift.
- **"Singularity"**: Used in all sections. Always refers to the discrete probability-$p$ event with output jump $\eta$. No drift.
- **"Hedge/hedging"**: Used in Abstract, Introduction, Model, Discussion, Extensions, Conclusion. Always refers to AI stocks' payoffs increasing when displacement risk materializes. No drift.
- **"Displacement"**: Used throughout. Always refers to the household's consumption share falling ($\phi < 1$). No drift.
- **"Extinction"**: Used throughout as a sub-event of singularity (probability $\xi$). Consistent usage everywhere.

## Summary

The paper uses all five concepts from the economic background spec consistently with their definitions. There is no terminological drift across sections, no Arrow-Debreu framing for market completeness, no budget constraint violations, and hedging is always described as a partial insurance mechanism whose payoff increases when the risk materializes.

# tests/spec-economic.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 2m 26s
[ralph-garage/agent-logs/20260411T211526.527055-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.527055-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions across every section of the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition**: "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage**:

- **Abstract**: "AI singularity that displaces their consumption" — uses the general term qualified by its displacement consequence; does not conflict with the spec's productivity definition.
- **Introduction (line 48)**: "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Directly consistent with the spec. The "sudden, dramatic improvement" matches "sudden improvement," and "displaces the typical investor" matches "devastating for the typical investor."
- **Model (Section 2)**: Singularity increases aggregate consumption by factor $(1+\eta)$ (productivity boost), consistent with "vastly increases productivity and output." Displacement via $\phi < 1$ makes it devastating for the household (the typical investor).
- **Extension 1 (Section 4.1)**: Introduces a *positive* singularity (household share increases) vs. *negative* singularity (household share falls, "as in the baseline"). The positive singularity still increases aggregate output by $(1+\eta)$, consistent with the spec's general definition of AI singularity.
- **Extension 2 (Section 4.2)**: Large singularity with $\eta = 9$ (ten-fold output growth) — consistent with "vastly increases productivity and output."
- **Conclusion**: "AI singularity that would displace their consumption" — same qualified usage as abstract.

**Finding**: Consistent throughout. The general term always denotes a sudden productivity increase; "negative" always denotes one that is devastating for the typical investor.

### 2. Budget Constraints

**Spec definition**: "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage**:

- **Model (Section 2)**: Total public dividends equal aggregate consumption: $D^{AI} + D^{N} = C_t$. Household receives $\alpha_t C_t$; AI owners receive $(1-\alpha_t) C_t$. Total consumption = $C_t$. No violation.
- **Pricing**: Prices determined by the household's Euler equation, which is derived from budget-constrained optimization. The standard approach implicitly enforces the budget constraint.
- **Extension 2**: Transfer equation (eq. 8) correctly allocates post-singularity consumption: the household gets its displaced share plus the net transfer, and the total does not exceed aggregate consumption (accounting for deadweight loss).

**Finding**: No budget constraint violations detected. Resource accounting is internally consistent across all sections.

### 3. Complete vs. Incomplete Markets

**Spec definition**: "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. [...] Incomplete markets does not necessarily refer to Arrow-Debreu securities. [...] Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage**:

- **Abstract**: "markets are incomplete---investors cannot trade private AI capital" — focuses on specific unavailable assets.
- **Introduction (line 52)**: "Under complete markets the displacement-driven premium would largely vanish, because the household could trade the restricted AI equity directly" — complete markets defined by ability to trade specific assets, not Arrow-Debreu.
- **Model (Section 2, line 113)**: "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — Exactly the spec's definition: specific assets the representative investor cannot buy.
- **Discussion (Section 2.3, line 172)**: "the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$" — complete markets = can trade restricted equity.
- **Extension 1 (line 209)**: "Under complete markets, the household can trade the restricted equity---founder stakes, pre-IPO shares, and other claims currently unavailable" — same framing.
- **Extension 2 (line 240)**: GKP-based discussion of why direct trading is infeasible (future innovators' capital doesn't yet exist) — focuses on specific economic frictions, not Arrow-Debreu.

**Finding**: Fully consistent. The paper never mentions Arrow-Debreu securities. Every discussion of complete/incomplete markets focuses on specific important assets (restricted AI equity) that the representative investor cannot trade.

### 4. Hedging

**Spec definition**: "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage**:

- **Abstract**: "investors use AI stocks to hedge against an AI singularity" — AI stocks as hedge.
- **Introduction (line 48)**: "investors use AI stocks to partially insure against displacement from AI" — "partially" consistent with "need not be perfect."
- **Model (Section 2, line 156)**: "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — Payoff increases when risk materializes; explicitly labeled "partial."
- **Model (Section 2, line 107-108)**: AI stock dividends grow upon singularity ($\Gamma^{AI} > 1+\eta$), confirming payoff increases when displacement risk materializes.
- **Model (Section 2, line 115)**: "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement" — explicitly imperfect hedge.
- **Discussion (Section 2.3, line 170)**: "growth stocks earn lower expected returns because they hedge displacement risk" — lower returns, not necessarily negative risk premia; consistent with "the asset need not earn a negative risk premium overall."

**Finding**: Fully consistent. The paper consistently uses "hedge" and "partial hedge" to mean payoffs increase when displacement materializes. It never claims the hedge is perfect and never implies AI stocks must earn negative risk premia.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition**: "General equilibrium means that prices are determined by the equilibrium conditions. It does *not* mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage**:

- The paper determines prices endogenously via the household's Euler equation (Section 2.2, line 126): "The household prices all publicly traded assets via its Euler equation."
- Consumption processes ($C_t$, $\alpha_t$, $\theta_t$) are exogenous — consistent with the spec's clarification that GE does not require endogenous consumption.
- The paper uses "equilibrium" (line 129: "stationary equilibrium") without the "general" qualifier. It does not claim to be partial equilibrium.
- The paper does not label itself as general or partial equilibrium anywhere.

**Finding**: Consistent. Prices are determined by equilibrium conditions (Euler equation), and consumption is exogenous. The paper avoids the GE/PE labels entirely, so there is no opportunity for misuse. The model's structure is consistent with the spec's definition of general equilibrium.

## Cross-Section Consistency Check

All five concepts maintain consistent meaning across:
- Abstract, Introduction, Model, Quantitative Analysis, Extensions, Discussion, Conclusion, and Appendix.
- No term shifts meaning between the baseline model and the extensions.
- No term is used differently in rhetorical passages vs. formal model sections.

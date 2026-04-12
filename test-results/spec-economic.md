# tests/spec-economic.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 2m 25s
[ralph-garage/agent-logs/20260412T154740.736638-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.736638-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage (consistent throughout):**

- Abstract: "AI singularity that displaces their consumption" — singularity displaces the household, consistent with negative singularity definition.
- Introduction (Section 1): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Directly mirrors the spec.
- Model (Section 2): Singularity increases aggregate consumption by factor $1+\eta$ (productivity boost = "vastly increases output") while the household's share drops by $\phi$ ("devastating for the typical investor" when $\phi(1+\eta) < 1$).
- Extension 1 (Section 4.1): Introduces a "positive singularity" where the household's share increases. This is an AI singularity (sudden productivity improvement) that is not negative (not devastating). The distinction is cleanly maintained.
- Conclusion: "AI singularity that would displace their consumption" — consistent.

**Assessment:** The paper always pairs "singularity" with productivity-increasing output growth, matching the spec's "vastly increases productivity and output." The negative qualifier is used only when the household is displaced, matching "devastating for the typical investor." No inconsistency found.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage (verified):**

- Model (Section 2): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." Household receives $\alpha_t C_t$; AI owners receive $(1-\alpha_t) C_t$. Sums to $C_t$. Budget satisfied.
- Post-singularity (no transfer): Household gets $\phi\alpha(1+\eta)C_t(1+g)$; AI owners get $(1-\phi\alpha)(1+\eta)C_t(1+g)$. Total = $(1+\eta)C_t(1+g)$ = aggregate consumption. Budget satisfied.
- Post-singularity (with transfer, Section 4.2): Household gets $\phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. AI owners get $(1-\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. Deadweight loss = $\delta\tau^2(1-\phi\alpha)(1+\eta)C_t(1+g)$. Total consumed + waste = $(1+\eta)C_t(1+g)$. Budget satisfied.

**Assessment:** No violations found. All consumption allocations sum correctly.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities... Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage (consistent throughout):**

- Abstract: "markets are incomplete---investors cannot trade private AI capital" — framed as unavailable assets, not Arrow-Debreu.
- Introduction: "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist... investors cannot trade the restricted equity."
- Model (Section 2): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central."
- Extension 1 (Section 4.1): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk."
- Extension 2 (Section 4.2): "broader trading of AI capital" as the ideal fix for incompleteness.

**Assessment:** The paper consistently defines market completeness/incompleteness in terms of specific unavailable assets (restricted AI equity). No mention of Arrow-Debreu securities. Fully aligned with the spec's framing.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage (consistent throughout):**

- Abstract: "investors use AI stocks to hedge against an AI singularity" — AI stock dividends increase upon singularity ($\Gamma^{AI} > 1+\eta$), so payoffs increase when displacement risk materializes.
- Introduction: "hedging motive: investors use AI stocks to partially insure against displacement from AI" — "partially" matches "need not be perfect."
- Model (Section 2): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — Payoff increases when risk materializes; explicitly partial.
- Model (Section 2): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." — Partial hedge, consistent.
- Discussion (Section 2.3): "growth stocks earn lower expected returns because they hedge displacement risk" — lower expected returns, but the paper does not claim negative expected returns overall, consistent with "need not earn a negative risk premium overall."
- The paper uses "premium" to refer to a price/valuation premium (higher P/D ratio), not to claim a negative risk premium.

**Assessment:** The paper consistently uses "hedge" to mean payoffs increase when risk materializes, consistently calls it "partial," and does not claim negative absolute risk premia. Fully aligned.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage:**

- The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium." Prices are determined by the household's Euler equation (an equilibrium condition), and consumption is exogenous (governed by the singularity mechanism). The paper does not claim that endogenous consumption is required for equilibrium pricing, nor does it claim prices are exogenous.

**Assessment:** No terminology to be inconsistent with. The model's structure is consistent with the spec's definitions — prices are endogenous (determined by Euler equation) and consumption is exogenous, which is compatible with general equilibrium per the spec.

## Cross-Section Consistency Check

The key terms — singularity, displacement, incomplete markets, hedging — maintain the same economic meaning across all sections:

| Term | Abstract | Intro | Model | Quant | Extensions | Conclusion |
|------|----------|-------|-------|-------|------------|------------|
| AI singularity | sudden displacement event | sudden productivity improvement + displacement | probability $p$, output $\times(1+\eta)$ | calibrated with $p$, $\eta$ | same mechanism, extended | same framing |
| Incomplete markets | can't trade private AI capital | restricted equity unavailable | household can't buy restricted shares | — | complete = can trade restricted equity | can't trade restricted AI equity |
| Hedging | AI stocks hedge displacement | partial insurance via AI stocks | partial hedge, payoffs rise in bad states | P/D spread reflects hedge value | transfers reduce hedge demand | hedging motive |

No cross-section drift or meaning shifts detected.

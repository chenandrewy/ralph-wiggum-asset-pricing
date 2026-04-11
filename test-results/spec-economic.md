# tests/spec-economic.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 2m 19s
[ralph-garage/agent-logs/20260410T221541.770523-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260410T221541.770523-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic background concepts consistently with the spec definitions across every section.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract (line 31): "investors use AI stocks to hedge against an AI singularity that displaces their consumption" — uses "AI singularity" with a qualifying clause specifying the displacement scenario. Consistent: does not redefine the general term, merely identifies the relevant scenario.
- Introduction (line 50): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Directly consistent with the spec. The emphasis on labor income and consumption displacement concretizes "devastating for the typical investor."
- Model, Singularity paragraph (lines 86–97): Defines the singularity as occurring with probability $p$, with sub-cases of non-extinction (aggregate consumption jumps by $1+\eta$, household share drops by $\phi$) and extinction. The productivity boost ($\eta > 0$) matches "vastly increases productivity and output." The household displacement matches "devastating for the typical investor."
- Extension 1 (lines 200–202): Introduces a *positive* singularity where "the household's share increases." This is consistent: it is an AI singularity (sudden productivity improvement) that is not negative (not devastating for the household).
- Title: "Hedging the Singularity" — informal shorthand, consistent in context.

**Cross-section consistency:** The term "singularity" maintains the same meaning (sudden AI productivity event) throughout abstract, introduction, model, extensions, and conclusion. The "negative" qualifier is used when referring specifically to the household-displacing variant.

**Finding:** No inconsistency.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model, Assets paragraph (line 107): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." Budget constraint satisfied for dividends.
- Model, Assets paragraph (line 107–108): Household receives $\alpha_t C_t$; AI owners receive $(1 - \alpha_t) C_t$. Shares sum to one.
- Extension 2, transfer equation (line 232): $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. Verification: household consumption + AI owners' post-tax consumption + deadweight loss = $[\phi\alpha + \tau(1-\delta\tau)(1-\phi\alpha) + (1-\tau)(1-\phi\alpha) + \delta\tau^2(1-\phi\alpha)](1+\eta)(1+g)C_t = (1+\eta)(1+g)C_t$. Budget constraint satisfied.
- Line 235: "$(1-\phi\alpha)$ represents the AI owners' share of post-singularity aggregate consumption; this expression uses the household's consumption share $\alpha$ rather than the AI dividend share $\theta$, because the transfer is levied on the consumption allocation, not on publicly traded dividends." — Explicit attention to ensuring the correct budget identity.

**Finding:** No budget constraint violations identified.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. [...] does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract (line 31): "markets are incomplete---investors cannot trade private AI capital" — Directly follows the spec: defines incompleteness by naming the untradeable asset.
- Introduction (line 50–51): "If markets were complete, investors could insure against this risk directly by trading the full universe of AI equity. But much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — Completeness framed as access to specific important assets, not Arrow-Debreu.
- Model, Assets (line 109): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — Explicitly ties incompleteness to specific untradeable assets.
- Model, Equilibrium (line 120): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — Draws the pricing implication without invoking Arrow-Debreu.
- Discussion (line 173): "If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk, and the valuation spread would collapse." — Complete markets = access to restricted AI equity.
- Extension 1, Proposition 3(ii) (line 216): "Under complete markets, the household can trade claims on private AI capital before the singularity." — Consistent: completeness means access to the specific restricted assets.
- No mention of "Arrow-Debreu" anywhere in the paper.

**Cross-section consistency:** Every usage defines incomplete/complete markets by whether the household can trade restricted AI equity. No section invokes Arrow-Debreu completeness.

**Finding:** No inconsistency.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract (line 31): "investors use AI stocks to hedge against an AI singularity" — Consistent: the paper shows AI stock dividends grow upon singularity.
- Introduction (line 48): "reflects a hedging motive: investors use AI stocks to partially insure against an AI singularity that displaces their consumption" — "partially insure" is consistent with "need not be perfect."
- Model, after Proposition 1 (line 150): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — Payoff increases when risk materializes; explicitly "partial."
- Discussion (line 171): "growth stocks earn lower expected returns because they hedge displacement risk from innovation" — Consistent with the GKP framework.
- Extension 2 (line 255): "transfers reduce the hedge value of AI stocks, compressing P/D ratios" — Hedging value is reduced when displacement is cushioned, consistent with the payoff-based definition.

**Cross-section consistency:** "Hedge" consistently means "payoff increases when the risk materializes." Always qualified as partial/imperfect when specificity matters. Never claims a perfect hedge or requires a negative risk premium.

**Finding:** No inconsistency.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does *not* mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Literature review (line 61): "\citet{GKP2012}, who develop a general-equilibrium model in which innovation displaces existing agents" — GKP's prices are determined by equilibrium. Consistent.
- The paper's own model: Prices are determined by the household's Euler equation (line 120, Proposition 1). Consumption growth is exogenous ($g$ is constant). This is general equilibrium by the spec's definition (prices from equilibrium conditions), even though consumption is not endogenous. The paper does not label its own model as GE or PE, which avoids any potential confusion.
- The paper never claims that its exogenous consumption growth makes the model partial equilibrium, nor does it claim GE requires endogenous consumption.

**Finding:** No inconsistency.

## Summary

All five economic background concepts are used consistently with their spec definitions throughout every section of the paper (abstract, introduction, model, quantitative analysis, extensions, conclusion, and appendix). No Arrow-Debreu framing is used for market completeness, budget constraints are satisfied, hedging is correctly characterized as partial, and general equilibrium is not conflated with endogenous consumption.

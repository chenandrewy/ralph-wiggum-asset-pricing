# tests/spec-economic.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 1m 39s
[ralph-garage/agent-logs/20260409T220435.843523-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.843523-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions throughout every section.

## Concept-by-Concept Evaluation

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract: "AI singularity that displaces their consumption" — consistent; displacement of consumption is devastating.
- Section 1 (line 51): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — matches the spec: sudden productivity increase + devastating for the typical investor.
- Section 2 (line 87–98): Singularity modeled with probability $p$, productivity boost $\eta > 0$, and displacement $\phi < 1$ reducing the household's share. Consistent: output jumps (productivity), household consumption falls (devastating).
- Extension 1 (line 201): Introduces a "positive singularity" where the household's share increases. This is an AI singularity (productivity jumps by $1+\eta$) that is beneficial rather than devastating — logically consistent with the spec's framework, which defines "negative" as the devastating variant without precluding a positive counterpart.
- Conclusion (line 266): "AI singularity that would displace their consumption" — consistent with prior usage.

**Finding:** Consistent throughout. The paper preserves the spec's two-part definition (sudden productivity increase + devastating for the investor) in every section and rhetorical context.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Section 2 (line 84): Household receives $\alpha_t C_t$, AI owners receive $(1-\alpha_t) C_t$. Shares sum to 1; aggregate consumption is fully allocated.
- Section 2 (lines 104–106): AI stock dividends $\theta_t C_t$ plus non-AI stock dividends $(1-\theta_t) C_t$ sum to $C_t$. Dividend shares exhaust aggregate consumption.
- Extension 2 (line 227): Transfer equation explicitly accounts for household's displaced consumption plus net transfer (reduced by deadweight costs) from AI owners' surplus. The transfer is levied on $(1-\phi\alpha)$, the AI owners' share, and reduced by $\delta\tau$, the waste fraction. Budget constraint is satisfied: total post-transfer consumption (household + AI owners net of tax and waste) is accounted for.

**Finding:** Consistent. Budget constraints are satisfied in all model components. No violations detected.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor… Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Section 1 (line 51): "If markets were complete, investors could insure against this risk directly by trading the full universe of AI equity. But much of this equity is restricted—held by founders, early-stage investors, and firms that may not yet exist." — focuses on specific unavailable assets, not Arrow-Debreu.
- Section 2 (line 108): "AI owners also hold restricted equity—founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. This is the source of market incompleteness." — defines incompleteness as inability to buy specific equity, consistent with spec.
- Section 2 (line 119): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — correct economic implication of incomplete markets as defined.
- Section 2 (line 172): "If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk, and the valuation spread would collapse." — complete markets framed as access to specific assets.
- Extension 1 (line 215): "Under complete markets, the household can trade claims on private AI capital before the singularity." — again, complete markets = access to specific assets, not Arrow-Debreu.
- No mention of Arrow-Debreu securities anywhere in the paper.

**Finding:** Consistent throughout. The paper always frames (in)completeness in terms of specific assets unavailable to the representative investor, never invoking Arrow-Debreu.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract: "investors use AI stocks to hedge against an AI singularity" — consistent.
- Section 1 (line 49): "investors use AI stocks to partially insure against an AI singularity that displaces their consumption" — "partially" aligns with "need not be perfect."
- Section 2 (line 149): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — payoff increases when risk materializes; explicitly partial.
- Section 2 (line 170): "growth stocks earn lower expected returns because they hedge displacement risk" — lower expected returns is not the same as negative risk premium; consistent with spec's note that the asset "need not earn a negative risk premium overall."
- Section 3 (line 188): "the household values the hedge more as the risk it hedges against becomes more likely" — consistent usage.
- Extension 2 (line 250): "transfers reduce the hedge value of AI stocks" — consistent; transfers reduce displacement, reducing the hedging motive.

**Finding:** Consistent throughout. The paper always treats hedging as partial, defined by payoffs increasing when the risk materializes, and never claims AI stocks earn negative risk premia.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**
- Section 1 (line 62): Refers to GKP2012 as "a general-equilibrium model in which innovation displaces existing agents." GKP2012 determines prices by equilibrium conditions — consistent with spec.
- Section 2 (lines 117–119): The paper's own model determines prices via the household's Euler equation (an equilibrium condition), with consumption exogenous (grows at rate $g$). The paper does not call its own model "partial equilibrium" despite exogenous consumption. This is correct per the spec: prices are endogenous (determined by equilibrium), so the model is general equilibrium regardless of whether consumption is endogenous.
- The paper calls its own model a "consumption-based model" (line 53), which is a neutral and accurate description that avoids any misuse of "partial equilibrium."

**Finding:** Consistent. The paper correctly uses "general equilibrium" for models where prices are determined by equilibrium conditions, and never misapplies "partial equilibrium" or conflates general equilibrium with endogenous consumption.

## Summary

All five concepts from the economic background spec are used consistently with their definitions across all sections of the paper (Introduction, Model, Quantitative Analysis, Extensions, Conclusion, and Appendix). No terminological drift, ambiguity, or inconsistency was found.

# tests/spec-economic.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 2m 24s
[ralph-garage/agent-logs/20260411T103039.126516-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.126516-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all five economic background concepts consistently with their spec definitions throughout all sections.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition**: "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage**:
- Abstract: "hedge against an AI singularity that displaces their consumption" — correctly describes a negative AI singularity via a relative clause specifying displacement.
- Introduction (line 49): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — consistent with spec; "displaces...labor income and consumption" is a concrete instantiation of "devastating."
- Model (lines 89–98): singularity defined with productivity boost η > 0 (sudden productivity improvement) and displacement φ < 1 (devastating for the household). Both spec properties present.
- Extension 1 (line 209): introduces a *positive* singularity where the household's share increases, properly distinguished from the negative case. The term "AI singularity" remains the umbrella (productivity boost), with positive/negative as subtypes.

**Assessment**: Consistent. The baseline model's unqualified use of "singularity" to mean the negative variant is acceptable because the introduction establishes the context and Extension 1 properly disambiguates when both types are present.

### 2. Budget Constraints

**Spec definition**: "Budget constraints are satisfied. We instinctively look for violations...and treat violations as fundamental flaws."

**Paper usage**:
- Line 110: "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)" — market clearing satisfied.
- Consumption split: household gets $\alpha_t C_t$, AI owners get $(1 - \alpha_t) C_t$. Shares sum to 1.
- Transfer equation (eq. 14, line 251): post-transfer consumption correctly accounts for tax revenue minus deadweight costs. The AI owners' share $(1 - \phi\alpha)$ plus the household's displaced share $\phi\alpha$ sum to 1.
- No budget constraint violations detected anywhere in the model, extensions, or appendix.

**Assessment**: Consistent. Budget constraints are satisfied throughout.

### 3. Complete vs. Incomplete Markets

**Spec definition**: "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor...does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage**:
- Abstract: "markets are incomplete---investors cannot trade private AI capital" — frames incompleteness as inability to trade specific assets.
- Introduction (line 51): "Much of the relevant equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — focuses on specific unavailable assets.
- Model (lines 112–113): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Discussion (line 178): "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$."
- Extension 1 (line 215): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable."
- No references to Arrow-Debreu securities anywhere in the paper.

**Assessment**: Consistent. Every mention of complete/incomplete markets focuses on specific tradeable/untradeable assets (restricted AI equity), exactly as the spec requires. Arrow-Debreu is never invoked.

### 4. Hedging

**Spec definition**: "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage**:
- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption."
- Introduction (line 53): "publicly traded AI stocks serve as the only available partial hedge against displacement."
- Model (line 106): AI dividends grow upon singularity ($\Gamma^{AI} > 1 + \eta$) — payoff increases when displacement materializes.
- Discussion (line 155): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — directly matches spec: payoff increases when risk materializes.
- The word "partial" is used consistently — never claims the hedge is perfect, consistent with "the hedge need not be perfect."
- The paper discusses high P/D ratios (high valuations, implying lower expected returns) but never claims AI stocks earn negative risk premiums, consistent with "the asset need not earn a negative risk premium overall."
- Related literature (line 176): "growth stocks earn lower expected returns because they hedge displacement risk" — lower, not negative.

**Assessment**: Consistent. Hedging is always described as partial, always framed as payoffs increasing when displacement occurs, and no claim of negative risk premiums.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition**: "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage**:
- The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium."
- Model (line 124–125): "The household prices all publicly traded assets via its Euler equation." — prices are determined by equilibrium conditions (the Euler equation), consistent with general equilibrium.
- Consumption growth is exogenous (deterministic rate g with stochastic singularity jumps). The paper never claims this makes the model partial equilibrium, which would be incorrect per the spec since prices are still endogenous.
- The paper correctly treats consumption as exogenous while maintaining that prices are determined in equilibrium, consistent with the spec's clarification that GE does not require endogenous consumption.

**Assessment**: Consistent. The paper avoids these terms but its implicit usage is correct: prices are endogenous (determined by Euler equation) and consumption is exogenous, which is valid general equilibrium per the spec.

## Cross-Section Consistency Check

All five concepts maintain the same economic meaning across:
- Abstract and introduction (rhetorical/motivational context)
- Model section (formal definitions)
- Discussion section (economic interpretation)
- Extensions (augmented model)
- Conclusion (summary)
- Appendix (mathematical derivations)

No cross-section drift detected.

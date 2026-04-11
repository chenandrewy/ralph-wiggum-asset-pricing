# tests/spec-economic.py
Started: 2026-04-11 15:15:27 EDT
Runtime: 2m 0s
[ralph-garage/agent-logs/20260411T151527.431050-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T151527.431050-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic terms from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract (line 31): "an AI singularity that displaces their consumption"
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption."
- Model (line 88): "Each period, with probability $p$, an AI singularity occurs."
- Model (line 91): non-extinction singularity has "aggregate consumption jumps by a factor $1 + \eta$"
- Quantitative (line 187): displacement causes "household consumption falls by 25%"

**Assessment:** Consistent. The paper's singularity is a "sudden, dramatic improvement in AI productivity" matching the spec's "sudden improvement in AI that vastly increases productivity and output." The negative singularity is "devastating for the typical investor" in that it displaces consumption (phi(1+eta) < 1 means household consumption falls even as aggregate output rises). The extinction sub-case (line 96) is framed as a consequence of the singularity event, consistent with Jones (2024)'s argument that "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest"---the improvement triggers the risk, preserving the definitional link.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (line 85-86): "The household receives a share $\alpha_t \in (0, 1)$ of aggregate consumption... AI owners receive the remainder, $(1 - \alpha_t) C_t$." Shares sum to 1.
- Model (line 109): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)."
- Transfers (line 241-247): Transfer equation: household gets displaced consumption plus net transfer from AI owners, with deadweight loss consuming $\delta\tau$ of the transfer. The tax base is $(1 - \phi\alpha)(1+\eta)C_t(1+g)$ (AI owners' share), and the transfer is reduced by waste. Total resources are conserved minus deadweight costs.

**Assessment:** Consistent. The consumption split between household ($\alpha_t C_t$) and AI owners ($(1-\alpha_t) C_t$) sums to $C_t$. Public dividends ($D^{AI} + D^{N} = C_t$) exhaust aggregate consumption. The transfer mechanism explicitly accounts for deadweight costs, and the paper carefully distinguishes the consumption share $\alpha$ from the dividend share $\theta$ (line 109), acknowledging that the household's consumption comes from multiple sources. No budget constraint violations detected.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract (line 31): "markets are incomplete---investors cannot trade private AI capital"
- Introduction (line 48): "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist."
- Introduction (line 52): "If markets were complete---if the household could trade the restricted AI equity---the displacement-driven premium would largely vanish"
- Model (line 111-113): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Model (line 123-124): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth."
- Discussion (line 171): "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged"
- Veto (line 208): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk."
- Conclusion (line 283): "This mechanism requires market incompleteness---the inability to trade restricted AI equity"

**Assessment:** Consistent. Every usage frames incomplete markets as the household's inability to trade specific important assets (restricted AI equity: founder stakes, pre-IPO shares, private AI capital). No reference to Arrow-Debreu securities anywhere in the paper. Complete markets is consistently defined as the household gaining access to these restricted assets. This exactly matches the spec's instruction to "focus on the important assets that are unavailable to the representative investor."

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract (line 31): "investors use AI stocks to hedge against an AI singularity"
- Introduction (line 48): "This market incompleteness forces them into publicly traded AI stocks as the only available partial hedge against displacement"
- Introduction (line 50): "publicly traded AI stocks as the only available partial hedge"
- Model (line 113): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement"
- Model (line 155): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Model (line 157): "the household values the hedge more as the risk it hedges against becomes more likely"
- Conclusion (line 283): "investors use AI stocks to partially insure against an AI singularity"

**Assessment:** Consistent. AI stocks' dividends grow by $\Gamma^{AI} > 1+\eta$ upon singularity, so their payoff increases when the risk (displacement) materializes---matching the spec's definition. The paper consistently calls AI stocks a "partial hedge," consistent with the spec's note that "the hedge need not be perfect." The paper never claims the hedge eliminates displacement or that AI stocks earn a negative risk premium.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. It uses "stationary equilibrium" (line 126) and "Equilibrium prices" (section header, line 122). Prices are determined endogenously by the household's Euler equation (line 294), not taken as exogenous. Consumption shares ($\alpha_t$) are governed by exogenous parameters ($\phi$), which is consistent with the spec's note that general equilibrium "does not mean that consumption is endogenous."

**Assessment:** Consistent by omission. The paper avoids the general/partial equilibrium labels entirely, which prevents any potential misuse. The model's structure---prices determined by equilibrium conditions, consumption shares governed by parameters---is consistent with the spec's definitions, though neither label is invoked.

## Cross-Section Consistency Check

The terminology is stable across all sections:

- **Introduction:** Sets up all terms correctly, matching spec definitions.
- **Model:** Formalizes the definitions with mathematical precision consistent with the informal spec definitions.
- **Quantitative Analysis:** Uses terms in the same sense as the model section.
- **Extensions (Veto):** Introduces complete markets counterfactual consistently with earlier usage (trading restricted equity, not Arrow-Debreu).
- **Extensions (Transfers):** Budget constraints maintained; incomplete markets framing unchanged.
- **Conclusion:** Summarizes using the same definitions as the introduction and model.
- **Appendix:** Technical derivation consistent with model section definitions.

No cross-section drift detected.

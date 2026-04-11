# tests/spec-economic.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 48s
[ralph-garage/agent-logs/20260411T101504.830369-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.830369-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Findings

### 1. AI Singularity

**Spec definition**: "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages**:
- Abstract: "an AI singularity that displaces their consumption"
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption."
- Model (line 88-97): Singularity occurs with probability $p$; non-extinction singularity has aggregate consumption jumping by factor $1+\eta$ (productivity boost) with household share dropping by $\phi$.
- Extension 1 (line 208): Introduces a *positive* singularity where the household's share increases, contrasted with the negative singularity from the baseline.

**Assessment**: Consistent. The paper's definition of a negative AI singularity captures both elements from the spec: (1) sudden improvement increasing productivity ($\eta > 0$ boosts aggregate consumption) and (2) devastating for the typical investor (displacement via $\phi < 1$ reduces the household's share). The "positive singularity" in Extension 1 is not defined in the spec but does not contradict it---it is simply the non-negative case. The baseline calibration ($\eta = 0.5$, i.e. 50% jump) and the large singularity ($\eta = 9$, i.e. ten-fold growth) both represent sudden productivity improvements, consistent with the spec.

---

### 2. Budget Constraints

**Spec definition**: "A core element of asset pricing theory, and economics more generally, is that budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages**:
- Model (line 85): "The household receives a share $\alpha_t \in (0, 1)$ of aggregate consumption, so its consumption is $c_t^H = \alpha_t C_t$. AI owners receive the remainder, $(1 - \alpha_t) C_t$."
- Model (line 107-109): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$), but these dividends are distributed among all investors, not solely the household."
- Extension 2 (line 251-254): Transfer consumption equation explicitly accounts for the household's displaced consumption plus the net transfer (after deadweight costs), drawn from AI owners' share $(1 - \phi\alpha)$.

**Assessment**: Consistent. The paper is careful to ensure budget constraints hold: (1) household + AI owner consumption shares sum to 1; (2) total dividends equal aggregate consumption; (3) transfers are funded from AI owners' surplus with explicit deadweight losses. No violations found.

---

### 3. Complete vs. Incomplete Markets

**Spec definition**: "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages**:
- Abstract: "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium."
- Introduction (line 50): "Much of the relevant equity is restricted---held by founders, early-stage investors, and firms that may not yet exist."
- Model (line 111-113): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Model (line 123-124): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth."
- Discussion (line 177): "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged..."
- Extension 1 (line 214): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk."

**Assessment**: Consistent. Every usage of "incomplete markets" and "complete markets" focuses on the specific unavailable assets (restricted AI equity, founder stakes, pre-IPO shares). The paper never invokes Arrow-Debreu securities. The transition from incomplete to complete markets is defined solely by whether the household can trade these specific restricted assets, exactly as the spec prescribes.

---

### 4. Hedging

**Spec definition**: "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages**:
- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption"
- Introduction (line 48): "publicly traded AI stocks serve as the only available partial hedge against displacement"
- Model (line 113): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement"
- Model (line 154): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Discussion (line 175): references GKP's result that "growth stocks earn lower expected returns because they hedge displacement risk"
- Extension 2 (line 274): "the hedge value of AI stocks becomes infinite---no finite price can compensate for the catastrophic displacement"

**Assessment**: Consistent. The paper consistently uses hedging to mean payoffs increase when the risk materializes: AI stock dividends grow (via $\Gamma^{AI} > 1+\eta$) precisely when the household is displaced. The paper explicitly calls it a "partial hedge" multiple times, consistent with the spec's note that perfection is not required. The paper discusses valuation effects (P/D ratios) rather than claiming AI stocks must earn negative risk premia, which is consistent with the spec's note that the asset "need not earn a negative risk premium overall."

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition**: "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages**:
- The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly.
- Model (line 122): Section titled "Equilibrium prices"---prices are determined by the household's Euler equation (an equilibrium condition), not taken as exogenous.
- Model (line 127): "In the stationary equilibrium where the household holds both public assets, the price-dividend ratios are: [closed-form expressions]"
- Consumption is exogenous: aggregate consumption grows at rate $g$, and the household's share $\alpha_t$ is governed by the singularity mechanism, not by portfolio choice.

**Assessment**: Consistent. The paper's model is general equilibrium in the spec's sense: prices are determined by the Euler equation (equilibrium conditions). Consumption is exogenous---governed by the singularity process and growth rate $g$---which is permissible under the spec's definition (general equilibrium does not require endogenous consumption). The paper never claims or implies that general equilibrium requires endogenous consumption.

---

## Summary

All five concepts from the economic background spec are used consistently throughout the paper:

| Concept | Consistent? | Notes |
|---|---|---|
| AI Singularity | Yes | Sudden productivity improvement + devastating displacement for typical investor |
| Budget Constraints | Yes | All consumption shares sum correctly; transfers explicitly funded |
| Complete vs. Incomplete Markets | Yes | Always defined by availability of specific restricted assets, never Arrow-Debreu |
| Hedging | Yes | Payoff increases when risk materializes; always described as partial; no risk-premium confusion |
| General vs. Partial Equilibrium | Yes | Prices from equilibrium conditions; no claim that GE requires endogenous consumption |

No inconsistencies, ambiguities that change economic meaning, or cross-section drift were found.

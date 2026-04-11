# tests/spec-economic.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260411T100209.003236-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T100209.003236-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usages:**

- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption"
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption."
- Model, Section 2.1: "Each period, with probability $p$, an AI singularity occurs." Non-extinction singularity: "Aggregate consumption jumps by a factor $1 + \eta$" with household share dropping via $\phi$.
- Extension 1: Introduces a *positive* singularity where "the household's share increases to $\alpha_{t+1} = \min(1, \alpha_t / \phi)$ and aggregate consumption jumps by $1 + \eta$."

**Assessment:** Consistent. The paper's singularity definition matches the spec: sudden, with large productivity/output effects. The negative variant is devastating for the typical investor (consumption falls even as aggregate output rises). The positive variant in Extension 1 is not devastating, appropriately distinguished.

One subtlety: the extinction sub-case ($C_{t+1} = 0$) does not increase output, but the paper frames extinction as a consequence triggered by the singularity rather than as the singularity itself. This is consistent with the spec's prototype definition and does not create ambiguity.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Section 2.1: "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$), but these dividends are distributed among all investors, not solely the household."
- Consumption shares: $c_t^H = \alpha_t C_t$ for the household, $(1 - \alpha_t) C_t$ for AI owners.
- Extension 2, equation (14): Post-transfer consumption is explicitly constructed so that transfers come from AI owners' surplus and deadweight costs reduce the total, maintaining accounting identity.

**Assessment:** Consistent. The model satisfies budget constraints throughout. Dividend shares sum to aggregate consumption, consumption shares sum to one, and the transfer mechanism in Extension 2 is carefully constructed to maintain accounting identities (transfers are levied on AI owners' consumption and delivered net of deadweight costs). No violations detected.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = some assets cannot be bought by the representative investor. Does NOT necessarily refer to Arrow-Debreu securities. Discussions should focus on important assets unavailable to the representative investor.

**Paper usages:**

- Abstract: "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium."
- Introduction (line 50): "If markets were complete, investors could insure against displacement directly by trading the full universe of AI equity, and the hedging premium would vanish. But much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist."
- Section 2.1 (line 113): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Section 2.2 (line 126): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth."
- Discussion (line 180): "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$."
- Extension 1: Complete markets defined as the ability to "trade the restricted AI equity" so that displacement is fully hedged.

**Assessment:** Consistent. The paper defines incompleteness strictly in terms of assets unavailable to the representative investor (restricted AI equity), exactly as the spec requires. No references to Arrow-Debreu securities. Every section that discusses completeness/incompleteness focuses on the specific unavailable assets and their economic consequences.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption"
- Introduction (line 48): "Part of this premium, we argue, reflects a hedging motive: investors use AI stocks to partially insure against this displacement."
- Section 2.2 (line 157): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Section 2.1 (line 115): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement, because the non-tradeable component (primarily labor income) is what $\phi$ captures."
- Discussion (line 180): "If the household could trade the restricted equity, it could hedge this component directly, and the valuation spread would collapse."

**Assessment:** Consistent. The paper uses "hedge" to mean that AI stocks' payoffs increase when displacement risk materializes ($\Gamma^{AI} > 1 + \eta$ in singularity states). The paper consistently describes the hedge as partial/imperfect, matching the spec's note that "the hedge need not be perfect." The paper does not claim or imply that AI stocks earn a negative risk premium overall; the premium is a *valuation* premium (higher P/D ratio), not a statement about expected returns being negative.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = prices determined by equilibrium conditions (NOT that consumption is endogenous). Partial equilibrium = prices exogenous.

**Paper usages:** The paper does not use the terms "general equilibrium" or "partial equilibrium."

**Assessment:** No inconsistency. The terms are not used, so no misuse is possible. The model itself is consistent with the spec's definitions: prices are determined by the household's Euler equation (an equilibrium condition), and consumption growth is partly exogenous (aggregate growth rate $g$ is given, with stochastic singularity shocks). The paper does not claim the model is general equilibrium, which is appropriate given its hybrid structure.

## Cross-Section Consistency Check

All five spec concepts maintain consistent meaning across the paper's sections:

- **Introduction** introduces the concepts and motivates them informally.
- **Model** formalizes them with consistent definitions.
- **Quantitative Analysis** uses the same definitions without drift.
- **Extensions** generalizes (adding positive singularity, transfers) without contradicting earlier definitions.
- **Conclusion** summarizes using the same terminology.

No cross-section drift or meaning shifts detected.

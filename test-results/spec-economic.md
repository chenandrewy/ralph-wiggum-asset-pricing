# tests/spec-economic.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 1m 44s
[ralph-garage/agent-logs/20260414T103309.985157-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260414T103309.985157-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All five concepts from the economic background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usages (consistent throughout):**

- Abstract: "AI singularity that displaces their consumption" — consistent with "devastating for the typical investor."
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — matches the spec definition closely.
- Model (line 87–98): Singularity occurs with probability $p$; non-extinction singularity has "aggregate consumption jumps by a factor $1+\eta$" (productivity boost) but "the household's share drops" (devastating for household). Extinction singularity sets $C_{t+1} = 0$.
- Extension 1 (line 205): Introduces a "positive singularity" where the household's share increases — used as a contrasting case, does not contradict the baseline definition.
- Quantitative analysis (line 191): "AI stock P/D ratios are substantially higher than non-AI stock P/D ratios" — consistent with singularity being a displacement event that investors hedge.
- Conclusion (line 287): "AI singularity that would displace their consumption" — consistent.

**Assessment:** The term "AI singularity" is used consistently as a sudden productivity event throughout. The "negative" qualifier is applied correctly when the household is displaced. The "positive singularity" extension is clearly distinguished.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (line 111–113): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$), but these dividends are distributed among all investors, not solely the household." — budget constraint is explicitly satisfied at the aggregate level.
- Model (line 83–84): "The household receives a share $\alpha_t \in (0,1)$ of aggregate consumption... AI owners receive the remainder, $(1 - \alpha_t) C_t$." — shares sum to 1, budget constraint satisfied.
- Extension 2 (line 248–251): Transfer equation accounts for household's displaced consumption plus net transfer from AI owners' surplus, with deadweight costs reducing (not creating) resources. Budget constraint is satisfied: resources are conserved with waste modeled as a loss.

**Assessment:** Budget constraints are satisfied throughout the model. No violations detected.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor." NOT necessarily about Arrow-Debreu securities. Complete markets also NOT about Arrow-Debreu. "Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages (consistent throughout):**

- Abstract (line 32): "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." — focuses on unavailable assets, not Arrow-Debreu.
- Introduction (line 48–49): "Much of the relevant AI equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — specific unavailable assets.
- Model (line 115–116): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — squarely matches spec definition.
- Model (line 129): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — consistent implication.
- Discussion (line 174–175): "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." — complete markets defined as being able to trade the restricted assets.
- Extension 1 (line 212): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." — complete markets defined by access to previously unavailable assets.
- No references to Arrow-Debreu securities anywhere in the paper.

**Assessment:** Perfectly consistent with the spec. Incomplete markets always means the household cannot trade specific AI assets. Complete markets always means access to those assets. Arrow-Debreu is never mentioned.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages (consistent throughout):**

- Abstract (line 32): "investors use AI stocks to hedge against an AI singularity" — consistent.
- Introduction (line 48): "investors use AI stocks to partially insure against displacement from AI" — "partially" aligns with "need not be perfect."
- Model (line 117–118): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." — explicitly acknowledges imperfect hedge.
- Model (line 158–159): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — payoff increases when displacement risk materializes, consistent with spec.
- Discussion (line 174): "displacement is fully hedged" under complete markets — used correctly as a limiting case.
- Remark 1 (line 154): "the hedging value of the asset is so extreme that no finite price can clear the market" — consistent usage of hedging concept.
- The paper never claims AI stocks earn a negative risk premium overall; the mechanism is about valuation premiums driven by hedging demand.

**Assessment:** Hedging is used consistently as a partial insurance mechanism where AI stock payoffs increase when displacement materializes. The paper correctly uses "partial hedge" and never overstates the completeness of the hedge.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- The paper does not use the phrases "general equilibrium" or "partial equilibrium" explicitly.
- Section 2.2 is titled "Equilibrium prices" and prices are determined by the household's Euler equation (line 129, 298–302), consistent with general equilibrium in the spec's sense (prices determined by equilibrium conditions).
- Consumption growth is exogenous ($g$ is constant, line 78–81), consistent with the spec's clarification that general equilibrium does NOT require endogenous consumption.
- The paper does not claim consumption is endogenous nor does it conflate equilibrium with endogenous consumption.

**Assessment:** While the paper does not use these terms explicitly, its implicit treatment is fully consistent with the spec. Prices are endogenous (determined by the Euler equation), consumption growth is exogenous, and these are not presented as contradictory.

## Cross-Section Consistency Check

All five concepts maintain identical economic meaning across:
- **Abstract → Introduction → Model → Quantitative Analysis → Extensions → Conclusion**: No drift in definitions.
- **Propositions vs. prose**: Formal statements and informal discussion use terms consistently.
- **Baseline model vs. extensions**: Extension 1 (veto) and Extension 2 (transfers) use incomplete/complete markets, singularity, and hedging in the same way as the baseline.
- **Appendix**: The proof uses the same definitions as the main text.

## No Inconsistencies Found

No terminology inconsistencies, definitional drift, or ambiguities that change economic meaning were identified.

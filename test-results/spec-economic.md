# tests/spec-economic.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260412T094631.066339-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.066339-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition**: "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage (consistent throughout)**:

- Introduction: "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." (line 48) -- Matches: sudden improvement + devastating for typical investor.
- Model (Section 2): "Each period, with probability $p$, an AI singularity occurs." Non-extinction singularity: "Aggregate consumption jumps by a factor $1 + \eta$" while "the household's share drops: $\alpha_{t+1} = \phi \alpha_t$." (lines 86--93) -- Aggregate output increases (productivity jump), household is devastated (share drops). Consistent.
- Extension 1 introduces a "positive singularity" where the household's share *increases*. Aggregate consumption still jumps by $1+\eta$. Both positive and negative singularities are AI singularities per the spec (sudden improvement increasing output). The negative one is devastating for the typical investor; the positive one is not. Naming is consistent.
- Abstract: "an AI singularity that displaces their consumption" -- The baseline singularity is negative (displacing), so omitting the qualifier is contextually accurate.

**No inconsistencies found.**

### 2. Budget Constraints

**Spec definition**: "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage**:

- "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)" (line 107) -- Dividends sum to aggregate consumption.
- Household receives $\alpha_t C_t$; AI owners receive $(1-\alpha_t) C_t$ (line 83) -- Shares sum to 1.
- Transfer extension (Section 4.2): Household post-transfer consumption is $\phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$ (eq. 9). AI owners retain $(1-\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. Deadweight loss consumes $\tau \cdot \delta\tau \cdot (1-\phi\alpha)(1+\eta)C_t(1+g)$. These sum to $(1+\eta)C_t(1+g)$ = total post-singularity aggregate consumption. Budget constraint satisfied.

**No violations found.**

### 3. Complete vs. Incomplete Markets

**Spec definition**: "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. For example, if the representative investor cannot buy equity in privately-held AI firms, then markets are incomplete. Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage (consistent throughout)**:

- Abstract: "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." (line 31) -- Framed as inability to trade specific assets.
- Model (Section 2): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." (line 109) -- Exactly matches the spec's framing.
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." (line 168) -- Consistently framed around specific unavailable assets.
- Extension 1 (Section 4.1): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." (line 206) -- Complete markets defined as access to specific previously-unavailable assets, not Arrow-Debreu.
- The paper never mentions Arrow-Debreu securities anywhere. This is consistent with the spec's guidance to avoid framing completeness in Arrow-Debreu terms.

**No inconsistencies found.**

### 4. Hedging

**Spec definition**: "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage (consistent throughout)**:

- Introduction: "investors use AI stocks to partially insure against displacement from AI" (line 48) -- "Partially insure" = partial hedge, consistent with "need not be perfect."
- Model (Section 2): "AI stocks' payoffs are especially valuable, pushing their P/D ratio above that of non-AI stocks. This is the hedging channel: AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." (line 152) -- Payoff increases when displacement risk materializes. Explicitly called "partial hedge."
- Model (Section 2): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement, because the non-tradeable component (primarily labor income) is what $\phi$ captures." (line 111) -- Hedge is not perfect; consistent with spec.
- The paper never claims AI stocks earn a negative risk premium or provide a perfect hedge. AI stock P/D ratios are *higher* (consistent with a lower expected return / hedging premium), but the paper does not overstate the hedge.

**No inconsistencies found.**

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition**: "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage**:

- The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly.
- The model structure is consistent with the spec's GE definition: prices are determined by the household's Euler equation (equilibrium conditions), while consumption growth follows an exogenous process ($g$, singularity mechanism). Prices are endogenous; consumption is exogenous. This matches the spec's clarification that GE does not require endogenous consumption.
- The paper uses "stationary equilibrium" (line 125) and "equilibrium prices" (Section 2.2 header), which are neutral and appropriate.

**No inconsistencies found.**

## Cross-Section Consistency Check

Each concept maintains the same economic meaning across all sections:

| Concept | Intro | Model | Quant | Extensions | Conclusion | Appendix |
|---|---|---|---|---|---|---|
| AI singularity | Consistent | Consistent | Consistent | Consistent | Consistent | Consistent |
| Budget constraints | N/A | Consistent | N/A | Consistent | N/A | Consistent |
| Incomplete markets | Consistent | Consistent | N/A | Consistent | Consistent | N/A |
| Hedging | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| GE/PE | N/A | Consistent | N/A | N/A | N/A | N/A |

No cross-section drift detected. Terminology is stable across all rhetorical contexts (abstract, formal model, quantitative discussion, policy extensions, conclusion).

# tests/spec-economic.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260411T161024.923579-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.923579-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usage:**

- Abstract: "an AI singularity that displaces their consumption"
- Introduction (line 48): "a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption"
- Model §2.1: "With probability $p$, an AI singularity occurs." Non-extinction singularity: "Aggregate consumption jumps by a factor $1 + \eta$" with displacement $\alpha_{t+1} = \phi \alpha_t$.
- Extension 1 (§4.1): Introduces a *positive* singularity where "the household's share increases" alongside the productivity boost.

**Assessment:** Consistent. The singularity always involves a sudden productivity improvement ($\eta > 0$), matching "sudden improvement in AI that vastly increases productivity and output." The negative singularity displaces the household's consumption (devastating for the typical investor). The positive singularity is explicitly labeled as distinct. The term keeps the same meaning across all sections.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations."

**Paper usage:**

- Model §2.1: "Total public dividends equal aggregate consumption ($D^{AI} + D^N = C_t$)" and "The household receives a share $\alpha_t \in (0,1)$ of aggregate consumption... AI owners receive the remainder."
- The consumption split between the household ($\alpha_t C_t$) and AI owners ($(1-\alpha_t) C_t$) sums to $C_t$.
- Extension 2 (§4.2): Transfer equation explicitly accounts for the tax, deadweight loss, and consumption shares: $c^H_{post} = \phi \alpha (1+\eta) C_t (1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta) C_t (1+g)$.

**Assessment:** Consistent. Budget constraints are satisfied throughout—consumption shares sum to one, dividends sum to aggregate consumption, and the transfer mechanism accounts for deadweight losses explicitly. No violations detected.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor" (e.g., privately-held AI firms). Does NOT necessarily refer to Arrow-Debreu securities. Complete markets discussions should "focus on the important assets that are unavailable to the representative investor."

**Paper usage:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital"
- Model §2.1: "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Discussion §2.3: "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged"
- Extension 1 (§4.1): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk."
- Extension 2 (§4.2): "broader trading of AI capital---faces the same constraint GKP identify: much of the displacing capital does not yet exist"
- Conclusion: "market incompleteness---the inability to trade restricted AI equity"

**Assessment:** Consistent. The paper defines incomplete markets as the household's inability to trade specific restricted AI assets, exactly matching the spec. Complete markets is defined as the household gaining access to those restricted assets. Arrow-Debreu securities are never invoked. The definition is stable across all sections—abstract, model, discussion, extensions, and conclusion.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**

- Abstract: "investors use AI stocks to hedge against an AI singularity"
- Introduction: "AI stocks to partially insure against displacement from AI" and "publicly traded AI stocks as the only available partial hedge against displacement"
- Model §2.1: "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement"
- Proposition 1 discussion: "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement"
- Discussion §2.3: "displacement-driven valuation premium"
- Quantitative §3: "the household values the hedge more as the risk it hedges against becomes more likely"
- Extension 2 (§4.2): "transfers reduce the hedge value of AI stocks"
- Conclusion: "investors use AI stocks to partially insure against an AI singularity that would displace their consumption"

**Assessment:** Consistent. AI stocks' dividends grow upon singularity ($\Gamma^{AI} > 1+\eta$), so their payoffs increase when displacement materializes—matching the spec's definition exactly. The paper consistently characterizes the hedge as partial (not perfect), consistent with the spec's "need not be perfect." The hedging concept is applied uniformly across all sections.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = "prices are determined by the equilibrium conditions," NOT that consumption is endogenous. Partial equilibrium = "prices are exogenous."

**Paper usage:**

- The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere.
- Model §2.2: "The household prices all publicly traded assets via its Euler equation. Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth."
- Consumption growth is exogenous (deterministic $g$ plus stochastic singularity shocks), and prices are endogenous (determined by the Euler equation).

**Assessment:** Consistent. The paper avoids the GE/PE terminology entirely, so there is no opportunity for inconsistency. Substantively, the model determines prices endogenously through equilibrium conditions (the Euler equation), while consumption dynamics are specified exogenously. This structure is consistent with the spec's definitions—the paper does not claim general equilibrium based on endogenous consumption, nor does it call its endogenous pricing "partial equilibrium."

## Cross-Section Consistency Check

Each concept maintains the same economic meaning across:
- **Abstract → Introduction → Model → Discussion → Quantitative Analysis → Extensions → Conclusion**
- No drift in the meaning of singularity, market incompleteness, hedging, or any other spec-defined term across sections or rhetorical contexts.
- The extensions introduce new elements (positive singularity, transfers) but do not redefine existing concepts.

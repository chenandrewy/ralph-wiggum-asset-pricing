# tests/spec-economic.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 2m 41s
[ralph-garage/agent-logs/20260409T182005.674420-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.674420-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all concepts from the economic background spec consistently with their definitions across all sections.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usages:**

- Abstract: "AI singularity that displaces their consumption" -- consistent, identifies the displacement effect.
- Introduction (Section 1): "AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" -- matches the spec's "sudden improvement" definition.
- Model (Section 2): "Each period, with probability $p$, an AI singularity occurs... Aggregate consumption jumps by a factor $1 + \eta$ (where $\eta > 0$ captures the productivity boost)" -- consistent: sudden, increases output.
- Extension 1 (Section 4.1): Introduces "positive singularity" (household share increases, $\phi^+ > 1$) and "negative singularity" ($\phi < 1$, "as in the baseline"). Both have $\eta > 0$, so both involve productivity increases. The negative singularity displaces the household's consumption (with baseline $\phi(1+\eta) = 0.75$, consumption falls 25%), consistent with "devastating for the typical investor."
- Conclusion (Section 5): "AI singularity that would displace their consumption" -- consistent.

**Assessment:** Consistent across all sections. The singularity always involves a sudden productivity increase. The negative singularity is devastating for the household (the typical/marginal investor). The positive singularity is clearly distinguished as a separate case.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (Section 2): Consumption shares sum to one: household gets $\alpha_t C_t$, AI owners get $(1 - \alpha_t) C_t$. Constraint $\alpha_t \in (0, 1 - \theta_t]$ ensures private AI capital dividends $(1 - \alpha_t)C_t - \theta_t C_t$ are non-negative.
- Public asset dividends: $D^{AI} + D^{N} = \theta_t C_t + (1 - \theta_t) C_t = C_t$. Total output is fully allocated.
- Extension 2 (Section 4.2): Post-transfer consumption equation (eq. 14) allocates total singularity output $(1+\eta)(1+g)C_t$ across household consumption, AI owners' retained income, and deadweight loss. Verification: $[\phi\alpha + \tau(1-\delta_0\tau)(1-\phi\alpha) + (1-\tau)(1-\phi\alpha) + \delta_0\tau^2(1-\phi\alpha)] = 1$. Budget constraint satisfied.

**Assessment:** No violations found. Consumption shares sum to one in all model variants, and the transfer extension properly accounts for deadweight costs.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities." Same for complete markets -- focus on "important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital" -- directly matches spec: specific assets unavailable to the representative investor.
- Model (Section 2): "The household *cannot* trade this private capital. This is the source of market incompleteness: the household cannot directly hedge displacement by buying claims on the full AI surplus." -- consistent, identifies the specific unavailable asset.
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk, and the valuation spread would collapse." -- consistent, defines incompleteness by the specific asset constraint.
- Extension 1 (Section 4.1): "Under complete markets, the household can trade claims on private AI capital before the singularity." -- consistent, complete markets defined as ability to trade the specific missing asset.
- Conclusion (Section 5): "the inability to trade private AI capital" -- consistent.

**Assessment:** Consistent across all sections. Market incompleteness is always defined as the inability to trade private AI capital, never as Arrow-Debreu completeness. Complete markets are defined as access to the specific missing asset, consistent with the spec.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Introduction (Section 1): "AI stocks serve as a *hedge*... publicly traded AI stocks provide one of the few available hedges." -- consistent, AI stock payoffs increase during singularity.
- Introduction: "AI stocks grow as a share of the economy with each singularity, making them a partial hedge against displacement." -- "partial hedge" is consistent with "need not be perfect."
- Model (Section 2): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." -- directly matches spec: payoff increases when risk materializes.
- Model: "$\Gamma^{AI} > 1+\eta$" -- AI stock dividends grow more than aggregate consumption upon singularity, confirming payoff increases when displacement risk materializes.
- Discussion (Section 2.3): "growth stocks earn lower expected returns because they hedge displacement risk" (describing GKP2012) -- lower expected returns is not the same as negative risk premium; consistent with spec's "need not earn a negative risk premium."
- Conclusion (Section 5): "investors use AI stocks to partially insure against an AI singularity that would displace their consumption" -- uses "insure" as a near-synonym for "hedge." The economic mechanism described (payoff increases when risk materializes) matches the spec definition. This is a minor terminological variation but the economic meaning is preserved.

**Assessment:** Consistent. The hedging concept is used correctly throughout: AI stock payoffs increase when displacement risk materializes. The paper appropriately notes the hedge is "partial" (not perfect). One instance uses "insure" instead of "hedge" (Conclusion), but the underlying economic content matches the spec's definition.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Introduction (Section 1): "\citet{GKP2012}, who develop a general-equilibrium model in which innovation displaces existing agents" -- a factual characterization of GKP2012; consistent with spec definition (GKP's prices are determined by equilibrium conditions).
- The paper's own model: Prices are determined by the household's Euler equation (eq. 6), which is an equilibrium condition. Consumption is exogenous (given by shares and growth process). This is general equilibrium per the spec (prices endogenous via equilibrium conditions), and is consistent with the spec's clarification that GE does not require endogenous consumption.
- The paper does not explicitly label its own model as "general equilibrium" or "partial equilibrium," which avoids any potential mischaracterization.

**Assessment:** Consistent. The paper correctly characterizes GKP2012 as general equilibrium. The paper's own model has prices determined by equilibrium conditions (Euler equation), consistent with GE per the spec. The paper does not conflate GE with endogenous consumption.

---

## Cross-Section Consistency Check

Each concept maintains the same economic meaning across the Introduction, Model, Quantitative Analysis, Extensions, and Conclusion. No cross-section drift was detected:

- "Singularity" always means a sudden productivity-increasing event; "negative" always means displacing the household.
- "Incomplete markets" always means inability to trade private AI capital.
- "Hedge" always means payoff increases when displacement risk materializes.
- Budget constraints are maintained in both the baseline and transfer extension.

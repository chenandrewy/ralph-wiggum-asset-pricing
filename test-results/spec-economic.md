# tests/spec-economic.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 2m 42s
[ralph-garage/agent-logs/20260409T184838.248152-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.248152-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions throughout all sections.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Abstract:** "an AI singularity that displaces their consumption" -- consistent; displacement of consumption is devastating for the typical investor.
- **Introduction (line 48):** "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" -- the parenthetical matches the spec's definition. The displacement framing is consistent with the negative variant.
- **Model (line 88):** "Each period, with probability $p$, an AI singularity occurs." Followed by productivity boost $\eta > 0$ (sudden improvement increasing output) and displacement $\phi < 1$ (devastating for the household). Consistent.
- **Extension 1 (lines 226--231):** Introduces positive vs. negative singularities. Positive: household share increases ($\phi^+ > 1$). Negative: household share falls ($\phi < 1$, "as in the baseline"). The negative singularity is devastating for the typical investor; the positive is not. Both include the productivity boost ($1 + \eta$). This matches the spec's two-tier definition.
- **Conclusion (line 296):** "an AI singularity that would displace their consumption" -- consistent with negative variant.

**Cross-section consistency:** The baseline model treats all non-extinction singularities as negative (displacing). Extension 1 introduces the positive/negative distinction. The term "singularity" consistently refers to a sudden productivity improvement; "negative singularity" consistently means one that is devastating for the household. No drift.

**Minor note:** The introduction says the singularity "displaces their labor income and consumption" (line 48), but the formal model has no labor income -- only a consumption share. This is informal motivational language in the intro and does not contradict the spec, but the phrase "labor income" does not reappear in the model or elsewhere.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Model (lines 85--86):** Household consumes $\alpha_t C_t$; AI owners consume $(1 - \alpha_t) C_t$. Sum = $C_t$. Aggregate budget constraint satisfied.
- **Model (lines 104--109):** AI stock dividends $\theta_t C_t$ + non-AI stock dividends $(1 - \theta_t) C_t$ = $C_t$ (total public dividends). Private AI capital dividends defined as residual: $(1 - \alpha_t) C_t - \theta_t C_t$. This is non-negative since $\alpha_t \leq 1 - \theta_t$.
- **Extension 2 (line 267):** Post-transfer consumption explicitly adds displaced household consumption + net transfers. The transfer comes from taxing AI owners' surplus, maintaining the aggregate budget.

**Assessment:** Aggregate consumption is always fully allocated between household and AI owners. Dividend structures are defined as shares of aggregate consumption that sum correctly. No budget constraint violation detected.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Abstract (line 31):** "markets are incomplete---investors cannot trade private AI capital" -- defines incompleteness through a specific unavailable asset.
- **Introduction (line 48):** "much of this capital is private, held by founders and early-stage investors" -- identifies the specific unavailable asset.
- **Model (line 109):** "The household cannot trade this private capital. This is the source of market incompleteness" -- directly matches spec's definition.
- **Discussion (line 197):** "the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk" -- complete markets defined as ability to trade the specific important asset.
- **Extension 1, Prop 3(ii) (line 255):** "Under complete markets, the household can trade claims on private AI capital" -- same definition.
- **Conclusion (line 296):** "the inability to trade private AI capital" -- consistent.

**Assessment:** The paper never invokes Arrow-Debreu securities. Every reference to market completeness/incompleteness focuses on the specific important asset (private AI capital) that is unavailable to the representative investor. Perfectly aligned with the spec across all sections.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Introduction (line 48):** "AI stocks serve as a hedge against a risk" -- payoff increases when displacement occurs.
- **Model, after Prop 1 (line 166):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement" -- payoff increases when risk materializes. Explicitly "partial," consistent with "need not be perfect."
- **Discussion (line 195):** "growth stocks earn lower expected returns because they hedge displacement risk" (describing GKP) -- lower expected returns, not negative risk premium. Consistent.
- **Extension 1 (line 255):** "the household has hedged its displacement" under complete markets -- used to describe insurance against the downside.
- **Extension 2 (line 280):** "transfers reduce the hedge value of AI stocks" -- hedge value is the increase in payoff during displacement states.
- **Conclusion (line 296):** "investors use AI stocks to partially insure against an AI singularity" -- "partially" again consistent with imperfect hedge.

**Assessment:** The paper consistently defines the hedging channel as: AI stock payoffs increase in the singularity state when the household's consumption falls. The paper uses "partial hedge" (lines 48, 166, 296), never claiming perfection. The paper does not claim AI stocks earn a negative risk premium -- it says they have higher valuations (Corollary 1), which implies lower expected returns relative to non-AI stocks, but this is not the same as a negative risk premium overall. Fully consistent with the spec.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- **Lit review (line 63):** "who develop a general-equilibrium model in which innovation displaces existing agents" (describing GKP) -- GKP's prices are determined by equilibrium conditions. Correct use.
- **Paper's own model:** Prices are determined by the household's Euler equation (an equilibrium condition, equation 6). Consumption growth is exogenous ($g$ is a parameter, displacement is governed by exogenous $\phi$). The paper does not explicitly label its own model as "general equilibrium" or "partial equilibrium."

**Assessment:** The paper's only use of "general equilibrium" is in reference to GKP, which is accurate. The paper's own model has prices determined by equilibrium (the Euler equation), consistent with GE by the spec's definition. Consumption is exogenous, which is permitted under the spec's definition of GE ("does not mean that consumption is endogenous"). The paper avoids labeling its own model, which is a conservative rhetorical choice that creates no inconsistency. No issues found.

---

## Summary

All five concepts from the economic background spec are used consistently with their definitions throughout all sections of the paper. The paper's terminology does not drift across sections, models, or rhetorical contexts. No inconsistencies, meaning-altering ambiguities, or cross-section drift detected.

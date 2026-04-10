# tests/spec-economic.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260409T205235.714729-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.714729-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Findings

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Abstract (line 32):** "hedge against an AI singularity that displaces their consumption" — consistent; displacement of consumption is devastating for the typical investor.
- **Introduction (line 49):** "AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" — matches "sudden improvement" and "devastating for the typical investor."
- **Model, Section 2.1 (line 87):** "Each period, with probability $p$, an AI singularity occurs." Conditional on non-extinction, "Aggregate consumption jumps by a factor $1 + \eta$" — consistent with "vastly increases productivity and output."
- **Extension 1 (line 199):** Introduces a "positive" singularity where the household benefits and a "negative" singularity "as in the baseline." The negative singularity displaces the household, matching the spec's "devastating for the typical investor."

**Potential ambiguity:** The model bundles an extinction branch (probability $\xi$) under the singularity event. Extinction ($C_{t+1} = 0$) does not itself "vastly increase productivity." However, the paper frames this as a correlated tail risk of the same AI improvement (line 95: "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest"), following Jones (2024). The singularity is the AI improvement; extinction is a possible consequence. This is a defensible modeling choice, not a definitional inconsistency.

**Assessment:** Consistent across all sections.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Model (lines 84):** Household receives $\alpha_t C_t$; AI owners receive $(1-\alpha_t) C_t$. Shares sum to 1. Budget satisfied.
- **Assets (lines 103-106):** AI dividends $\theta_t C_t$ and non-AI dividends $(1-\theta_t) C_t$. Shares sum to 1. Budget satisfied.
- **Transfers (line 224-226):** Post-transfer consumption: household gets displaced share plus net transfer; AI owners retain the rest minus transfer; deadweight cost accounts for the remainder. Verified: $\phi\alpha(1+\eta)(1+g)C_t + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)(1+g)C_t + (1-\tau)(1-\phi\alpha)(1+\eta)(1+g)C_t + \tau\delta\tau(1-\phi\alpha)(1+\eta)(1+g)C_t = (1+\eta)(1+g)C_t$. Budget satisfied.

**Assessment:** No violations found.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor." "Does not necessarily refer to Arrow-Debreu securities." "Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Abstract (line 32):** "markets are incomplete---investors cannot trade private AI capital" — directly matches spec definition (specific important asset unavailable).
- **Model (line 108):** "The household cannot trade this private capital. This is the source of market incompleteness: the household cannot directly hedge displacement by buying claims on the full AI surplus." — consistent; identifies the specific unavailable asset.
- **Introduction (line 49-50):** "much of this capital is private, held by founders and early-stage investors in firms that may not yet exist. This market incompleteness forces investors into publicly traded AI stocks as an imperfect substitute." — consistent.
- **Extension 1 (line 213):** "Under complete markets, the household can trade claims on private AI capital before the singularity." — focuses on the specific unavailable asset becoming available, matching the spec's guidance.
- **Discussion (line 170):** "The market incompleteness in our model---the household's inability to trade private AI capital---is central." — consistent.

The paper never references Arrow-Debreu securities.

**Assessment:** Consistent across all sections. The paper correctly frames incompleteness around specific unavailable assets rather than Arrow-Debreu completeness.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Introduction (line 49):** "AI stocks serve as a hedge against a risk" — consistent.
- **Model (line 147):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — payoff increases when risk materializes; explicitly "partial," consistent with "need not be perfect."
- **Abstract (line 32):** "investors use AI stocks to hedge against an AI singularity" — consistent.
- **Discussion (line 168):** "growth stocks hedge displacement risk from innovation" — consistent (describing GKP's result).
- **Conclusion (line 257):** "investors use AI stocks to partially insure against an AI singularity" — "partially insure" is consistent with "need not be perfect."
- **Lit review (line 62):** "growth stocks earn lower expected returns because they hedge displacement risk" — this describes a model result (in GKP), not a definitional claim that hedging requires a negative risk premium. Consistent with the spec, which says the asset "need not earn a negative risk premium overall" but does not prohibit it as a model outcome.

**Assessment:** Consistent across all sections. The paper appropriately uses "partial hedge" and never claims hedging requires a negative premium as a definitional matter.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous." "Partial equilibrium means that prices are exogenous."

**Paper usages:**

- **Lit review (line 62):** GKP "develop a general-equilibrium model in which innovation displaces existing agents" — GKP's prices are determined by equilibrium conditions, so this label is correct per the spec.
- **The paper's own model:** Prices are determined by the household's Euler equation (line 119: "The household prices all publicly traded assets via its Euler equation"), which is an equilibrium condition. Consumption follows an exogenous process (constant growth rate $g$, modified by singularity shocks). The paper does not label its own model as "general equilibrium," but neither does it mislabel it. The fact that consumption is exogenous is not presented as inconsistent with equilibrium pricing, which aligns with the spec's clarification.
- The term "partial equilibrium" does not appear in the paper.

**Assessment:** Consistent. The paper correctly uses "general equilibrium" for GKP's model (prices from equilibrium conditions) and does not conflate equilibrium pricing with endogenous consumption.

---

## Cross-Section Consistency

All five concepts maintain stable meanings across the abstract, introduction, model, extensions, quantitative analysis, discussion, and conclusion. No cross-section drift detected:

- "Singularity" always means a sudden AI productivity jump with displacement consequences.
- "Market incompleteness" always means inability to trade private AI capital.
- "Hedging" always means AI stocks paying off when displacement materializes.
- Budget constraints are satisfied in every section where quantities are specified.
- Equilibrium terminology is used sparingly and correctly.

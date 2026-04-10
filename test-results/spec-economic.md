# tests/spec-economic.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 1m 41s
[ralph-garage/agent-logs/20260409T194838.519038-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.519038-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions throughout every section.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usages:**

- Abstract: "AI singularity that displaces their consumption" — consistent, displacement is the mechanism by which the singularity is devastating.
- Introduction (Section 1): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" — directly echoes "sudden improvement" and "vastly increases productivity."
- Model (Section 2): "Each period, with probability $p$, an AI singularity occurs… Aggregate consumption jumps by a factor $1 + \eta$" — the productivity/output increase is formalized via $\eta > 0$.
- Extension 1 (Section 4.1): "the singularity is *negative* (as in the baseline): $\alpha_{t+1} = \phi \alpha_t$ with $\phi < 1$" — consistent with "devastating for the typical investor" since the household's consumption share drops. The "positive" singularity ($\phi^+ > 1$) still involves a productivity jump, consistent with the general singularity definition.
- Conclusion (Section 5): "AI singularity that would displace their consumption" — consistent throughout.

**Assessment:** Consistent across all sections. The singularity always involves a sudden productivity increase (matching "sudden improvement… that vastly increases productivity and output"), and the negative singularity is always devastating for the household (matching "devastating for the typical investor").

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (Section 2): Aggregate consumption $C_t$ is split: household gets $\alpha_t C_t$, AI owners get $(1 - \alpha_t) C_t$. These sum to $C_t$. ✓
- Public dividends: AI stocks pay $\theta_t C_t$, non-AI stocks pay $(1 - \theta_t) C_t$. These sum to $C_t$. ✓
- Private AI capital dividends: $(1 - \alpha_t) C_t - \theta_t C_t$. The constraint $\alpha_t \in (0, 1 - \theta_t]$ ensures this is non-negative. ✓
- Extension 2 (Section 4.2): Post-transfer consumption (Eq. 8) adds household's displaced share plus net transfer from AI surplus, with deadweight costs reducing the transfer. The transfer base is $(1 - \phi\alpha)(1+\eta)C_t(1+g)$, which is the AI surplus. The deadweight cost $\delta_0 \tau$ destroys resources but does not create them. ✓

**Assessment:** No budget-constraint violations found. All consumption shares and dividend shares sum correctly.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor… does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital" — directly matches "some assets cannot be bought by the representative investor."
- Introduction (Section 1): "much of this capital is private, held by founders and early-stage investors in firms that may not yet exist. This market incompleteness forces investors into publicly traded AI stocks as an imperfect substitute." — focuses on specific unavailable assets, not Arrow-Debreu.
- Model (Section 2): "The household *cannot* trade this private capital. This is the source of market incompleteness: the household cannot directly hedge displacement by buying claims on the full AI surplus." — consistent.
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk." — complete markets discussed in terms of available assets, not Arrow-Debreu.
- Extension 1 (Section 4.1): "Under complete markets, the household can trade claims on private AI capital before the singularity." — same framing.
- Extension 2 (Section 4.2): References GKP2012's observation that "the displacing capital may not yet exist---it belongs to future cohorts of innovators---direct trading is infeasible" — incompleteness as untradeable assets.
- Conclusion (Section 5): "market incompleteness---the inability to trade private AI capital" — consistent.

**Assessment:** Fully consistent. The paper never invokes Arrow-Debreu securities and always frames (in)completeness in terms of the specific assets unavailable to the representative investor, exactly as the spec requires.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Introduction (Section 1): "AI stocks serve as a *hedge* against a risk that most investors cannot diversify away" — payoff-based framing, consistent.
- Introduction: "AI stocks to hedge against an AI singularity" and "imperfect substitute" — acknowledges imperfection, matching "need not be perfect."
- Model (Section 2): "AI stocks' payoffs are especially valuable… AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — payoff increases when displacement risk materializes. "Partial" matches "need not be perfect."
- Discussion (Section 2.3): "growth stocks hedge displacement risk from innovation" (describing GKP) — same payoff-based meaning.
- Quantitative Analysis (Section 3): "the household values the hedge more as the risk it hedges against becomes more likely" — consistent usage.
- Extension 2 (Section 4.2): "transfers reduce the hedge value of AI stocks" and "the hedge value of AI stocks becomes infinite" — "hedge value" refers to the value derived from the hedging property (payoff increasing in bad states). Consistent.
- Conclusion (Section 5): "investors use AI stocks to partially insure against an AI singularity that would displace their consumption" — "insure" used as synonym for "hedge," still payoff-based.

**Assessment:** Fully consistent. Every usage refers to AI stocks' payoffs increasing when displacement risk materializes. The paper consistently notes the hedge is partial/imperfect and never claims AI stocks must earn a negative risk premium.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Introduction (Section 1): Refers to GKP2012's "general-equilibrium model in which innovation displaces existing agents" — GKP's prices are determined by equilibrium conditions. ✓
- Model (Section 2): "The household prices all publicly traded assets via its Euler equation." Prices are determined by the Euler equation (an equilibrium condition), while consumption dynamics are exogenous (driven by the singularity process). This is general equilibrium per the spec — prices endogenous, consumption exogenous. The paper does not mislabel this as partial equilibrium.
- The paper does not explicitly classify its own model as "general equilibrium" or "partial equilibrium," but its structure (endogenous prices, exogenous consumption) is consistent with general equilibrium as defined in the spec. No conflation of "general equilibrium" with "endogenous consumption."

**Assessment:** Consistent. The one explicit use ("general-equilibrium model" for GKP) is correct. The paper's own model has prices determined by equilibrium conditions and never claims that general equilibrium requires endogenous consumption.

---

## Cross-Section Consistency Check

Each concept maintains the same economic meaning across the introduction, model, extensions, quantitative analysis, and conclusion. No drift was detected:

- "Singularity" always means a sudden productivity jump, with "negative" always meaning devastating for the household.
- "Incomplete markets" always means inability to trade private AI capital.
- "Hedge" always means payoff increases when displacement materializes, and is always qualified as partial/imperfect.
- Budget constraints hold throughout the model and extensions.
- No misuse of general/partial equilibrium terminology.

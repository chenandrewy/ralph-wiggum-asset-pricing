# tests/spec-economic.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260409T215056.130463-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.130463-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-concept analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract: "AI singularity that displaces their consumption" — describes the negative variant by its effect on the household.
- Introduction: "negative AI singularity---a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption" — matches both definitions precisely.
- Model §2.1: "With probability $p$, an AI singularity occurs... Aggregate consumption jumps by a factor $1 + \eta$" — matches "sudden improvement that vastly increases productivity and output."
- Extension 1 §4.1: Introduces a "positive singularity" where "the household's share increases" vs. the baseline "negative" singularity where displacement occurs — consistent contrast with the spec's definition of "negative" as "devastating for the typical investor."

**Assessment:** Consistent. The singularity is always defined as a sudden productivity improvement (η > 0). The "negative" qualifier is used when it devastates the household through displacement (ϕ < 1). The positive variant in Extension 1 correctly inverts this.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model §2.1: "The household receives a share $\alpha_t \in (0,1)$ of aggregate consumption... AI owners receive the remainder, $(1 - \alpha_t) C_t$." Shares sum to 1.
- Model §2.1: "AI stocks pay dividends $D_t^{AI} = \theta_t C_t$... Non-AI stocks pay dividends $D_t^N = (1 - \theta_t) C_t$." Dividend shares sum to 1.
- Extension 2 §4.2: Transfer equation (6) explicitly accounts for deadweight costs: "$\tau (1 - \delta\tau)(1 - \phi\alpha)(1+\eta) C_t (1+g)$" — the waste fraction $\delta\tau$ is subtracted from the transfer, preserving the budget constraint.

**Assessment:** Consistent. All consumption and dividend allocations sum correctly. Transfers account for waste without violating aggregate resource constraints.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital" — focuses on specific unavailable assets, not Arrow-Debreu.
- Introduction: "If markets were complete, investors could insure against this risk directly by trading the full universe of AI equity. But much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — defines completeness in terms of specific tradeable assets.
- Model §2.1: "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household cannot purchase these restricted shares. This is the source of market incompleteness." — concrete, asset-specific definition.
- Model §2.2: "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — consequence stated correctly.
- Discussion §2.3: "the household's inability to trade restricted AI equity---is central. If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk" — completeness defined by access to specific assets.
- Extension 1, Prop 3(ii): "Under complete markets, the household can trade claims on private AI capital before the singularity." — consistent, asset-specific.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu securities. Every reference to complete/incomplete markets focuses on the specific assets (restricted AI equity) that are or are not available to the representative investor.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption" — payoffs increase when risk materializes (Γ^AI > 1+η upon singularity).
- Introduction: "AI stocks serve as a hedge against a negative AI singularity" and later "publicly traded AI stocks as an imperfect substitute" — consistent with "need not be perfect."
- Model §2.1: "AI stocks grow as a share of the economy with each singularity, making them a partial hedge." — consistent with imperfect hedge.
- Model §2.2: "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — matches "payoff tends to increase when that risk materializes."
- Conclusion: "investors use AI stocks to partially insure against an AI singularity" — consistent.

**Assessment:** Consistent. AI stock dividends increase upon singularity (Γ^AI > 1), which is when displacement risk materializes. The paper consistently qualifies the hedge as "partial" or "imperfect," matching the spec's allowance for imperfect hedging without implying a negative risk premium.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous." "Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Literature review: "who develop a general-equilibrium model in which innovation displaces existing agents" — referring to GKP2012, whose prices are determined by equilibrium conditions. Consistent.
- The paper's own model: Prices are determined endogenously through the household's Euler equation (equation 9, Appendix A). Consumption growth is exogenous (constant rate g with stochastic singularity shocks). The paper does not label its own model "general equilibrium" or "partial equilibrium" — it simply derives prices from equilibrium conditions.

**Assessment:** Consistent. The paper's usage of "general-equilibrium" for GKP2012 matches the spec (prices determined by equilibrium, not requiring endogenous consumption). The paper's own model follows the same pattern without mislabeling.

---

## Cross-section consistency check

All five concepts maintain their economic meaning across every section of the paper:

| Concept | Abstract | Intro | Model | Extensions | Conclusion | Appendix |
|---|---|---|---|---|---|---|
| AI Singularity | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Budget Constraints | — | — | ✓ | ✓ | — | ✓ |
| Complete/Incomplete Markets | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Hedging | ✓ | ✓ | ✓ | — | ✓ | — |
| GE vs. PE | — | ✓ | — | — | — | — |

No cross-section drift, ambiguity, or inconsistency detected.

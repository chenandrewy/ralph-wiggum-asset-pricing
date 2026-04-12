# tests/spec-economic.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 2m 39s
[ralph-garage/agent-logs/20260411T212707.760515-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.760515-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all five economic concepts from the spec consistently with their definitions throughout every section.

## Concepts evaluated

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages (section by section):**

- **Abstract:** "an AI singularity that displaces their consumption" — consistent; displacement of consumption is devastating for the typical investor.
- **Introduction (§1):** "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — directly mirrors the spec's definition, adding the specifics of labor income and consumption as the mechanism of devastation.
- **Model (§2):** "Each period, with probability $p$, an AI singularity occurs." Non-extinction branch: "Aggregate consumption jumps by a factor $1 + \eta$" — consistent with "vastly increases productivity and output." The household's share drops via $\phi$, making it devastating for the typical investor.
- **Extension 1 (§4.1):** Introduces a "positive singularity" where the household's share increases and aggregate consumption jumps by $1 + \eta$. The positive singularity still increases productivity, consistent with the spec's base definition. The "negative" singularity (baseline) remains devastating for the typical investor.
- **Extension 2 (§4.2):** Uses "singularity" consistently with the model setup; references "large singularity" ($\eta = 9$) — an extreme version of "vastly increases productivity."
- **Conclusion (§5):** "an AI singularity that would displace their consumption" — consistent.

**Assessment:** Consistent throughout. One modeling note: the extinction sub-event ($C_{t+1} = 0$) is conditional on a singularity occurring but does not itself increase productivity. The paper handles this clearly by framing extinction as a conditional outcome of the singularity event, following Jones (2024): "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest." This is a defensible modeling choice, not a terminology inconsistency — the singularity (AI becoming powerful) triggers both potential consequences.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Model (§2.1):** Total public dividends: $D^{AI} + D^{N} = \theta C + (1 - \theta) C = C_t$ — budget constraint satisfied for dividend claims.
- **Model (§2.1):** Consumption shares: household receives $\alpha_t C_t$, AI owners receive $(1 - \alpha_t) C_t$ — shares sum to 1, budget constraint satisfied.
- **Model (§2.1):** The paper explicitly addresses the relationship between $\alpha_t$ (consumption share) and $\theta_t$ (dividend share): "Because $\alpha_t$ and $\theta_t$ are distinct—one governs the consumption split, the other the dividend split among publicly traded assets—the household's share can differ from its pro-rata claim on public dividends." This careful accounting prevents budget-constraint confusion.
- **Extension 2 (§4.2):** Transfer equation (eq. 11): $c^H_{post} = \phi \alpha (1+\eta) C_t (1+g) + \tau(1 - \delta\tau)(1 - \phi\alpha)(1+\eta) C_t (1+g)$ — the household receives its displaced share plus a net transfer from AI owners' surplus. The total allocation (household + AI owners after tax + deadweight loss) sums correctly.

**Assessment:** No budget constraint violations detected. The paper is careful about accounting identities throughout.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. For example, if the representative investor cannot buy equity in privately-held AI firms, then markets are incomplete. Incomplete markets does not necessarily refer to Arrow-Debreu securities." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages (section by section):**

- **Abstract:** "Because markets are incomplete—investors cannot trade private AI capital—AI stocks command a premium." — directly matches the spec: specific assets unavailable, not Arrow-Debreu.
- **Introduction (§1):** "Much of the relevant AI equity is restricted—held by founders, early-stage investors, and firms that may not yet exist." and "Because investors cannot trade the restricted equity, they turn to publicly traded AI stocks." — focuses on specific unavailable assets.
- **Introduction (§1):** "Under complete markets the displacement-driven premium would largely vanish, because the household could trade the restricted AI equity directly; market incompleteness is the key driver." — complete markets defined as ability to trade specific assets, not Arrow-Debreu.
- **Model (§2.1):** "AI owners also hold restricted equity—founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — precisely matches the spec's definition and example.
- **Model (§2.2):** "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — correct usage of incomplete markets' implication for pricing.
- **Discussion (§2.3):** "The market incompleteness in our model—the household's inability to trade restricted AI equity—is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." — consistent.
- **Extension 1 (§4.1):** "Under complete markets, the household can trade the restricted AI equity—founder stakes, pre-IPO shares, and other claims currently unavailable." — explicitly about specific assets.
- **Extension 2 (§4.2):** "The ideal solution—broader trading of AI capital—faces the same constraint GKP identify: much of the displacing capital does not yet exist." — consistent framing around specific assets.
- **Conclusion (§5):** "This mechanism requires market incompleteness—the inability to trade restricted AI equity." — consistent.

**Assessment:** Fully consistent. No reference to Arrow-Debreu securities anywhere. Every usage focuses on specific assets (restricted AI equity) that are unavailable to the representative investor, exactly as the spec requires.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages (section by section):**

- **Abstract:** "investors use AI stocks to hedge against an AI singularity that displaces their consumption" — consistent: AI stocks' payoffs increase when displacement occurs.
- **Introduction (§1):** "investors use AI stocks to partially insure against displacement from AI" — "partially" is consistent with "need not be perfect."
- **Introduction (§1):** "publicly traded AI stocks as the only available partial hedge against displacement" — uses "partial hedge," consistent.
- **Model (§2.1):** "AI stocks grow as a share of the economy with each singularity, making them a partial hedge" — payoff increases when risk materializes, partial hedge.
- **Model (§2.1):** "Holding AI stocks allows the household to smooth marginal utility across states—this is the hedging channel that inflates AI stock valuations—but does not eliminate displacement" — explicitly imperfect hedge, consistent.
- **Model (§2.2):** "AI stocks' payoffs are especially valuable, pushing their P/D ratio above that of non-AI stocks. This is the hedging channel: AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — directly matches spec: payoff increases when risk materializes.
- **Discussion (§2.3):** "displacement is fully hedged" (under complete markets) vs. partial hedge under incomplete markets — consistent distinction.
- **Remark 1:** "the hedging value of the asset is so extreme that no finite price can clear the market" — extreme case of hedging demand, consistent with the concept.
- **Extension 2 (§4.2):** "transfers reduce the hedge value of AI stocks" — consistent: transfers reduce displacement risk, so the hedging motive weakens.

**Assessment:** Fully consistent. The paper consistently treats AI stocks as a partial (imperfect) hedge whose payoff increases when displacement risk materializes. No claims of perfect hedging or negative risk premia.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does **not** mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere. The model's prices are determined endogenously through the household's Euler equation (an equilibrium condition), making it a general equilibrium model by the spec's definition. Consumption growth ($g$, $\eta$, $\phi$) is exogenous, which is permissible under the spec's definition of GE ("does not mean that consumption is endogenous"). Because the paper avoids labeling itself as GE or PE, there is no opportunity for inconsistency with the spec.

**Assessment:** No inconsistency. The paper's model structure is consistent with the spec's definition of general equilibrium (prices from equilibrium conditions, exogenous consumption), and no mislabeling occurs.

---

## Summary

All five concepts from the economic background spec are used consistently with their definitions throughout every section of the paper. The paper is notably careful about:
- Framing market incompleteness around specific unavailable assets (restricted AI equity) rather than Arrow-Debreu securities
- Using "partial hedge" consistently rather than implying perfect hedging
- Maintaining budget-constraint accounting across consumption shares and dividend shares
- Defining AI singularity consistently with the spec's emphasis on sudden productivity improvement and investor devastation

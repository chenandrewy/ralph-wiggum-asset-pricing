# tests/spec-economic.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 2m 58s
[ralph-garage/agent-logs/20260412T095842.937458-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.937458-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the background spec consistently with their definitions throughout every section.

## Concepts Evaluated

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages (consistent):**

- Abstract: "AI singularity that displaces their consumption" — sudden event, increases aggregate output (via $\eta > 0$), displaces the household.
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — matches spec's "devastating for the typical investor."
- Model, Section 2.1 (line 86–97): Singularity occurs with probability $p$; non-extinction variant has "Aggregate consumption jumps by a factor $1 + \eta$" (productivity increase) and "$\alpha_{t+1} = \phi \alpha_t$" (displacement). Structure matches spec: sudden, increases output, devastating under displacement.
- Extension 1 (line 200): Introduces a "positive singularity" (household share increases) alongside the baseline "negative" variant. Both involve $\eta > 0$ (output increases), consistent with the spec's base definition. The positive variant is not devastating, hence not labeled "negative."
- Extension 2 (line 263): Large singularity with $\eta = 9$ and $\phi = 0.05$ — "vastly increases" output (ten-fold) and is clearly devastating ($\phi(1+\eta) = 0.5$, consumption halves).

**Assessment:** The term maintains consistent economic meaning across all sections. The baseline calibration ($\eta = 0.5$) is a less dramatic productivity increase than the word "vastly" in the spec suggests, but the paper uses "dramatic" rather than "vast" in its own definition, and the model structure (sudden jump, $\eta > 0$, displacement) is fully consistent. No cross-section drift.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages (consistent):**

- Section 2.1 (line 107): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$), but these dividends are distributed among all investors, not solely the household." Aggregate resource constraint is explicit and satisfied.
- Section 2.1 (line 107–108): "The household's consumption $\alpha_t C_t$ reflects the net outcome of its portfolio returns from public stocks and any labor-like income; AI owners receive the remainder." Total consumption: $\alpha_t C_t + (1-\alpha_t)C_t = C_t$. Budget balanced.
- Extension 2, equation (12) (line 243): Transfer consumption: $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. The transfer is funded by taxing AI owners' surplus; deadweight costs ($\delta\tau$ fraction of the transfer) are real resource losses. Total post-singularity resources: household + AI owners (after tax) + deadweight loss = $(1+\eta)C_t(1+g)[\phi\alpha + (1-\phi\alpha)(1-\delta\tau^2)]$, which is less than aggregate output by exactly the deadweight loss. Budget constraint satisfied.

**Assessment:** No budget constraint violations found in any section. Resource accounting is internally consistent throughout.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages (consistent):**

- Abstract: "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." Framed as inability to trade specific assets.
- Section 2.1 (line 109): "The household *cannot* purchase these restricted shares. This is the source of market incompleteness." Explicitly tied to specific unavailable assets (restricted AI equity).
- Section 2.2 (line 122): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." Correct implication of incompleteness.
- Section 2.3 (line 168): "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." Complete markets framed as ability to trade the restricted AI equity, not Arrow-Debreu.
- Extension 1 (line 206): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable." Again, explicitly about the specific unavailable assets.
- No Arrow-Debreu references anywhere in the paper.

**Assessment:** Every mention of complete/incomplete markets is framed in terms of the specific assets (restricted AI equity) that the representative investor cannot trade. The paper never invokes Arrow-Debreu securities. Fully consistent with the spec across all sections.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages (consistent):**

- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption." AI stocks' dividends grow upon singularity (payoff increases when risk materializes).
- Introduction (line 48): "investors use AI stocks to partially insure against displacement from AI." "Partially" — hedge need not be perfect.
- Introduction (line 50): "AI stocks grow as a share of the economy with each singularity, making them a partial hedge." Consistent with imperfect hedge.
- Section 2.2 (line 152): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." Payoff increases when risk materializes; explicitly partial.
- Section 2.1 (line 111): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." Imperfect hedge, consistent.
- Section 2.3 (line 168): "displacement is fully hedged" (under complete markets, with restricted equity tradeable). Full hedge as limiting case.
- Extension 2 (line 265): "the hedge value of AI stocks becomes infinite---no finite price can compensate." Hedging value concept applied consistently.

**Assessment:** Every use of "hedge" and "hedging" is consistent with the spec's payoff-based definition. The paper consistently characterizes AI stocks as a partial (imperfect) hedge, never claiming they eliminate displacement or earn negative risk premia. Consistent across all sections.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages (consistent):**

The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. However, the model's structure is consistent with the spec's definitions:

- Prices are determined by the household's Euler equation (an equilibrium condition), not set exogenously. This is general equilibrium in the spec's sense.
- Consumption is governed by exogenous parameters ($\alpha_t$, $\phi$, $g$, $\eta$), not determined endogenously by production or optimization over consumption-savings. This is consistent with the spec's clarification that general equilibrium does *not* require endogenous consumption.
- The conclusion (line 283) notes the model "abstracts from... production-side details," confirming consumption is not endogenized. No claim is made that this makes the model partial equilibrium.

**Assessment:** No inconsistency. The paper avoids these terms entirely, and its model structure is consistent with the spec's definitions.

---

## Cross-Section Consistency Check

All five concepts maintain stable economic meaning across:
- Abstract and Introduction (rhetorical framing)
- Model section (formal definitions)
- Discussion section (interpretation and comparison to GKP)
- Extensions (augmented models)
- Conclusion (summary)

No term drifts in meaning between sections. The hedging concept, market incompleteness, and singularity definitions are introduced in the introduction, formalized in the model, and applied consistently in extensions and discussion.

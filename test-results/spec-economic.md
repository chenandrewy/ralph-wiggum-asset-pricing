# tests/spec-economic.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 2m 42s
[ralph-garage/agent-logs/20260412T141819.035585-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.035585-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all five economic background concepts consistently with the spec's definitions across every section.

## Concepts Evaluated

The economic background spec defines five concepts with definitional constraints:

1. **AI Singularity / Negative AI Singularity**
2. **Budget Constraints**
3. **Complete vs. Incomplete Markets**
4. **Hedging**
5. **General Equilibrium vs. Partial Equilibrium**

---

## 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "an AI singularity that is devastating for the typical investor."

### Paper usages

- **Introduction (line 48):** "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Matches spec: sudden improvement + devastating for typical investor.
- **Abstract:** "hedge against an AI singularity that displaces their consumption" — Uses a relative clause to narrow to the negative case; consistent.
- **Model, Singularity paragraph (line 86):** "Each period, with probability $p$, an AI singularity occurs." Then specifies: non-extinction branch has a productivity boost ($1+\eta$) and displacement ($\phi$); extinction branch has $C=0$. The productivity boost matches "vastly increases productivity and output." The displacement matches "devastating for the typical investor."
- **Extension 1 (line 200):** Introduces a "positive singularity" where the household's share increases. Both positive and negative branches include the productivity boost $1+\eta > 1$, consistent with the spec's core definition that a singularity increases productivity. The sign refers to the distributional effect on the household.
- **Extinction sub-event (line 94):** "With probability $\xi$, the singularity triggers extinction." The singularity (AI improvement) is the cause; extinction is a possible consequence. This is consistent with the spec: the AI improvement happens, and in some states that same powerful AI also causes existential risk. Supported by: "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest."

### Assessment

Consistent throughout. The paper clearly distinguishes "AI singularity" (the event) from "negative AI singularity" (the event + devastation for typical investor). In the baseline model, only negative singularities appear, and the paper refers to them as "singularity" without always prepending "negative" — this is contextually unambiguous because the baseline has only one type. When Extension 1 introduces positive singularities, the distinction is made explicit.

---

## 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

### Paper usages

- **Model, Assets paragraph (line 107):** "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." Budget constraint on dividends is explicitly stated and satisfied.
- **Model, Consumption paragraph (line 83):** "The household receives a share $\alpha_t \in (0,1)$ of aggregate consumption... AI owners receive the remainder, $(1-\alpha_t) C_t$." Shares sum to 1; budget constraint satisfied.
- **Extension 2, Transfer equation (line 243):** Transfer = $\tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. The transfer is funded from AI owners' post-singularity surplus $(1-\phi\alpha)$, reduced by deadweight cost $\delta\tau$. The household's post-transfer consumption plus the AI owners' remaining consumption plus deadweight loss equals total post-singularity output. Budget constraint satisfied.

### Assessment

No violations found. All consumption shares sum correctly, dividend shares sum to aggregate consumption, and transfers are funded from identifiable sources with explicit deadweight costs accounted for.

---

## 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities." Complete markets similarly "does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

### Paper usages

- **Abstract:** "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." Directly matches spec: incompleteness = specific assets unavailable to representative investor.
- **Model, Assets paragraph (line 109):** "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness." Exactly spec-consistent: incompleteness defined by specific unavailable assets.
- **Model, Discussion (line 168):** "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." Complete markets = ability to trade the specific restricted equity.
- **Extension 1 (line 206):** "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." Complete markets defined by specific tradeable assets, not Arrow-Debreu.
- **Extension 2 (line 237):** "intergenerational transfers...would affect the magnitude but not the functional form of the displacement factor" — Discusses transfers as substitutes for missing markets, consistent with asset-focused definition.
- **Conclusion (line 281):** "This mechanism requires market incompleteness---the inability to trade restricted AI equity." Consistent recap.

### Assessment

Fully consistent. The paper never references Arrow-Debreu securities. Both complete and incomplete markets are defined exclusively in terms of specific assets (restricted AI equity) that the representative investor can or cannot trade, exactly as the spec requires.

---

## 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

### Paper usages

- **Introduction (line 48):** "investors use AI stocks to partially insure against displacement from AI." "Partially insure" = imperfect hedge, consistent with "need not be perfect."
- **Model, Discussion (line 152):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." Payoff increases when risk (displacement) materializes; explicitly labeled "partial hedge."
- **Model, Assets (line 111):** "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." Consistent: hedge is imperfect.
- **Proposition 1 discussion (line 152):** "Since $\Delta\theta > 0$, AI stocks' dividends grow faster than aggregate consumption upon a singularity ($\Gamma^{AI} > 1+\eta$)." The payoff (dividend) increases when the risk materializes. Matches spec definition.
- **Extension 2 (line 235):** "they reduce AI stock valuations by cushioning displacement (a pricing effect)" — Transfers reduce hedging demand, consistent with hedging channel.
- **Conclusion (line 281):** "investors use AI stocks to partially insure against an AI singularity that would displace their consumption." Consistent summary.

### Assessment

Fully consistent. The paper always describes AI stocks as a "partial hedge" or "partial insurance," never claiming the hedge is perfect or that AI stocks earn negative risk premia. The hedging mechanism operates through the payoff channel (AI dividends increase when displacement occurs), exactly matching the spec's definition.

---

## 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous." "Partial equilibrium means that prices are exogenous."

### Paper usages

The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. It uses "stationary equilibrium" in Proposition 1 (line 124): "In the stationary equilibrium where the household holds both public assets, the price-dividend ratios are..."

- **Model (line 122):** "The household prices all publicly traded assets via its Euler equation." Prices are determined endogenously by the Euler equation (an equilibrium condition), consistent with GE.
- **Model (line 77):** Aggregate consumption grows exogenously at rate $g$. The paper does not claim this makes the model "partial equilibrium," which would be incorrect per the spec (PE = prices exogenous, not consumption exogenous). The paper also does not claim endogenous consumption makes it "general equilibrium."
- **Conclusion (line 283):** "It abstracts from... production-side details." The paper acknowledges simplifications without mischaracterizing the equilibrium concept.

### Assessment

Consistent by avoidance: the paper does not use GE/PE terminology and therefore cannot misuse it. Where equilibrium concepts appear (Euler equation pricing, stationary equilibrium), they are used correctly — prices are endogenous (determined by the household's SDF), and consumption is partly exogenous (aggregate growth rate $g$, displacement parameter $\phi$). The paper never conflates endogenous consumption with general equilibrium.

---

## Cross-Section Consistency Check

Each concept maintains the same meaning across:
- **Abstract vs. body:** Singularity, incomplete markets, and hedging definitions are introduced in the abstract and used identically throughout.
- **Model vs. extensions:** Incomplete markets, hedging, and singularity retain their definitions. Extension 1's "positive singularity" and Extension 2's "complete markets via transfers" are natural extensions consistent with the baseline definitions.
- **Formal propositions vs. discussion:** The hedging channel described informally (partial hedge, payoffs increase in displacement states) matches the formal mechanism ($\Gamma^{AI} > \Gamma^{N}$, $\phi^{-\gamma}$ weighting).
- **Introduction vs. conclusion:** All terms are recapped with the same definitions used in the body.

No cross-section drift detected.

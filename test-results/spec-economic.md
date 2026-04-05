# tests/spec-economic.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 1m 35s
[ralph-garage/agent-logs/20260404T232545.920512-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.920512-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Introduction (Section 1): "An AI singularity---a sudden, dramatic improvement in AI capability---would vastly increase total economic output." — Direct match.
- Model (Section 2.2): "Total output jumps by factor $G > 1$: the economy becomes vastly more productive." — Consistent: sudden, one-time event that vastly increases output.
- Abstract: "devastating AI singularity" — Refers to the negative variant (see below), not the general definition, so no conflict.

**Negative AI singularity spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**
- Model (Section 2.2): "When $\Lambda < 1$---a *negative* AI singularity---the household's consumption falls despite a massive increase in total output. This is the displacement scenario." — Consistent: the singularity vastly increases output (matching the base definition) but is devastating for the household (the typical investor).
- Quantitative section (Section 3.3): "$\Lambda = 0.8$, the singularity reduces the household's consumption to 80% of its pre-singularity level" — Consistent with "devastating for the typical investor."
- Introduction: "help hedge against an AI singularity that devastates the typical investor's wealth" — Direct alignment.

**Assessment:** Consistent across all sections. The paper always treats the singularity as a sudden productivity/output increase (matching the base definition) and reserves "negative" for the case where the typical investor is devastated (matching the negative variant). No drift.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Model (Section 2.4, Definition 1): Equilibrium requires Euler equations to hold and markets to clear: "the household holds all publicly traded shares." The household's consumption equals publicly traded output, which is total output minus the AI owners' private share. Budget balance is maintained.
- Post-singularity consumption (eq. 3): $C_{\tau+1} = (1-\phi) G (1+g) C_\tau$ — The household receives fraction $(1-\phi)$ of total output. The remaining $\phi$ goes to AI capital owners. Total output is fully allocated.
- Government transfers extension (Section 4.1, eq. 8): $\Lambda(\tau,\delta) = [(1-\phi) + (1-\delta)\tau\phi] G$ — Tax revenue $\tau\phi G$ is collected; fraction $\delta$ is destroyed as deadweight loss; remainder $(1-\delta)\tau\phi G$ goes to the household. The accounting is: AI owners keep $(1-\tau)\phi G$, government destroys $\delta\tau\phi G$, household receives $(1-\phi)G + (1-\delta)\tau\phi G$. These sum to $G[(1-\phi) + (1-\delta)\tau\phi + \delta\tau\phi + (1-\tau)\phi] = G[1-\phi + \tau\phi] + G\phi(1-\tau) = G$. Budget constraint satisfied.

**Assessment:** No violations found. All output is fully allocated across agents in every scenario.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Model (Section 2.3): "The household cannot trade the private AI capital held by AI owners. This is the key friction." — Focuses on a specific, economically important asset that is unavailable. No reference to Arrow-Debreu.
- Introduction: "The representative investor, who holds publicly traded stocks but cannot buy claims on this private capital, faces displacement." — Same framing: specific asset unavailability.
- Section 3.2: "Under complete markets, the household can trade claims on the private AI capital." — Complete markets defined by ability to trade the specific important asset, not by Arrow-Debreu.
- Section 4.2 (Deployment efficiency): "Under complete markets, the household shares in the full output gains... Under incomplete markets with $\Lambda < 1$, the singularity reduces the household's consumption." — Consistent framing throughout.
- Introduction: "Under incomplete markets, the premium is strictly larger than under complete markets, because the household's marginal utility in the singularity state is amplified by the displacement it cannot insure away." — Focuses on the inability to trade the specific asset.

**Assessment:** Fully consistent. The paper never frames completeness/incompleteness in Arrow-Debreu terms. Every reference focuses on whether the household can trade the specific important asset (private AI capital). This holds across the model, results, and all three extensions.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Introduction: "publicly traded AI stocks may command high prices because they help hedge against an AI singularity" — Payoff-based framing.
- Introduction: "Publicly traded AI stocks partially hedge this displacement because their dividends grow relative to other stocks when the singularity arrives." — Payoffs increase when the risk materializes; explicitly "partial" (not perfect). Matches the spec.
- Model (Section 2.2): AI share of publicly traded output increases from $\alpha$ to $\alpha_S > \alpha$ at the singularity. AI stock dividends jump by factor $(\alpha_S/\alpha) \cdot \Lambda$ relative to pre-singularity. The payoff increases when the risk (singularity-driven displacement) materializes.
- Results (Section 3.1): "hedge factors" $H^A$ and $H^N$ — These capture how much each asset's value is enhanced by the singularity state. $H^A > H^N$ when $\alpha_S > \alpha$, reflecting AI stocks' superior payoff in the displacement state.
- Quantitative section (Section 3.3): "AI stocks function as insurance: their value rises precisely because the disaster they hedge against becomes more likely." — Payoff increases when the risk materializes.
- Extinction section (Section 4.3): "extinction destroys all assets equally, adding a state that provides no differential hedge" — Consistent: hedging is about differential payoffs when risk materializes.

**Assessment:** Consistent throughout. The paper always grounds hedging in payoff behavior (dividends/value increasing when displacement risk materializes). It explicitly uses "partially" (not claiming perfection). The paper does not claim AI stocks earn negative expected returns overall — the "hedging premium" refers to a higher price-dividend ratio (valuation premium), which is the standard consequence of hedging demand in asset pricing. No conflict with the spec's note that "the asset need not earn a negative risk premium overall."

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**
- The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. However, the model is implicitly general equilibrium by the spec's definition: prices are determined by the household's Euler equations (equilibrium conditions), not specified exogenously.
- The word "equilibrium" appears in Definition 1 (Section 2.4): "An equilibrium consists of asset prices $(P_t^A, P_t^N)$ such that the household's Euler equations hold." — Prices are endogenous, determined by equilibrium conditions.
- Consumption is not endogenously optimized from a production problem; it is determined by the output structure and market incompleteness. This is consistent with the spec's clarification that GE "does not mean that consumption is endogenous."

**Assessment:** No inconsistency. The paper avoids the GE/PE labels entirely, but its model structure is consistent with the spec's definitions. Prices are determined by equilibrium conditions (GE), and consumption is determined by the output/market structure rather than being endogenous from a household optimization over production — which is fine per the spec.

---

## Cross-Section Consistency Check

The following terms were checked for drift across sections:

| Term | Intro | Model | Results | Extensions | Conclusion | Appendix |
|------|-------|-------|---------|------------|------------|----------|
| AI singularity | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| Negative singularity | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| Incomplete markets | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| Hedging | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| Budget constraints | N/A | Satisfied | Satisfied | Satisfied | N/A | Satisfied |

No cross-section drift detected for any concept.

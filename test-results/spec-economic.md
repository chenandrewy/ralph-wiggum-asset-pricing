# tests/spec-economic.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260402T184535.059972-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059972-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the background spec consistently with their definitions across all sections.

## Concept-by-Concept Findings

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usage:**
- Abstract (line 30): "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" — consistent with both definitions.
- Introduction (line 52): "A sudden AI breakthrough---a singularity---could dramatically increase productivity while shifting the economy's structure, displacing traditional businesses" — consistent.
- Model (lines 76--84): Singularity is an absorbing event with $\tilde{g} > g$, described as "the productivity increase that accompanies the singularity." The paper notes "The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output." The narrative framing ("surge," "dramatically") matches the spec's "vastly increases."
- Assumption 1 (line 103): "Negative singularity" is formalized as the household's output share falling ($\Delta < 1$). This captures "devastating for the typical investor" through displacement.
- Extension (lines 240--276): Continues using singularity consistently as the sudden productivity event with displacement.
- Conclusion (lines 281--289): Consistent usage throughout.

**Assessment:** Consistent. The term maintains the same economic meaning across all sections. The formalization ($\tilde{g} > g$ with displacement) faithfully captures the spec's verbal definition.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage:**
- Equation (6), line 126: The household's budget constraint is stated explicitly: $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.
- Equation (3)--(4), lines 91--99: Output shares sum to 1 ($\theta + \nu + (1-\theta-\nu) = 1$), both pre- and post-singularity. Total output is fully accounted for.
- Equation (8), line 132: Equilibrium consumption $c_t = D_t^A + D_t^N = \omega Y_t$ follows from market clearing ($n_t^A = n_t^N = 1$) and the budget constraint.

**Assessment:** Consistent. Budget constraints are explicitly stated and satisfied. Output shares sum to one in both regimes. No violations.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. For example, if the representative investor cannot buy equity in privately-held AI firms." Complete markets "should instead focus on the important assets that are unavailable to the representative investor." Neither necessarily refers to Arrow-Debreu securities.

**Paper usage:**
- Introduction (line 52): "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..." — directly matches spec's framing.
- Model (line 124): "cannot invest in private AI capital" — the household's exclusion from private AI capital is the source of incompleteness.
- Proposition 4 (line 215): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$." — complete markets defined as access to the unavailable asset.
- Conclusion (line 289): "expanding the set of tradeable AI-related assets...could reduce the displacement premium and improve welfare by completing markets" — consistent framing.

**Assessment:** Consistent. The paper frames market completeness entirely around access to private AI capital, exactly as the spec prescribes. No reference to Arrow-Debreu securities anywhere. The concept maintains the same meaning across introduction, model, results, and conclusion.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**
- Title: "Hedging the Singularity."
- Abstract (line 30): "partial insurance against displacement" — "partial" is consistent with "need not be perfect."
- Introduction (line 52): "publicly traded AI stocks offer the best available hedge" — consistent with imperfect hedge.
- Results (line 185): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." — AI stock payoff increases when singularity risk materializes, matching the spec exactly.
- Results (line 198): "the more likely or severe the displacement, the more the household values AI stocks relative to non-AI stocks" — hedging channel described consistently.
- Proposition 4 (line 222): "hedging premium" defined as $V_0^A - V_0^{A,\text{CM}} > 0$ — the valuation premium from the hedge, used consistently throughout.
- Extension (line 255): "The hedging premium vanishes" when $\tilde{g} \to \infty$ — consistent usage of the concept.

**Assessment:** Consistent. The paper uses "hedge" to mean that AI stocks' payoff (dividend share) increases when singularity risk materializes, directly matching the spec. The paper explicitly acknowledges the hedge is partial ("partial insurance," "best available hedge"), consistent with the spec's note that perfection is not required. The "hedging premium" term is introduced clearly and used uniformly.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage:**
- The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium."
- The model is a general equilibrium model by the spec's definition: prices are determined by the Euler equation (equilibrium condition), not set exogenously.
- Section 2.4 is titled "Equilibrium" (line 141), and prices are derived from Euler equations and market clearing.
- Consumption is determined by market clearing ($c_t = \omega Y_t$), not assumed exogenously, but the paper does not claim this feature makes the model "general equilibrium."

**Assessment:** Consistent. The paper does not invoke these terms, so there is no opportunity for misuse. The model's structure (prices from equilibrium conditions) is consistent with general equilibrium as defined in the spec.

## Cross-Section Consistency Check

The following terms were checked for drift across sections:

| Term | Abstract | Intro | Model | Results | Extension | Conclusion |
|------|----------|-------|-------|---------|-----------|------------|
| Singularity | sudden productivity surge + displacement | sudden AI breakthrough + displacement | absorbing event, $\tilde{g}>g$, share shift | hedging mechanism | extreme limits, extinction | displacement event |
| Incomplete markets | — | cannot buy private AI | cannot invest in private AI capital | — | frictions prevent risk-sharing | — |
| Complete markets | — | — | — | household invests in private AI capital | Coasean risk-sharing | completing markets |
| Hedge | partial insurance | best available hedge | — | payoff increases in singularity states | premium vanishes in limits | insurance properties |
| Displacement | displaces workers/firms | displaces traditional businesses | $\Delta < 1$, share falls | $\Delta^{-\gamma}$ drives premium | frictions sustain/overcome | severity drives premium |

No cross-section drift detected. Each concept maintains its economic meaning throughout the paper.

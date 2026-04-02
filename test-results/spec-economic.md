# tests/spec-economic.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 2m 19s
[ralph-garage/agent-logs/20260402T180723.895178-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.895178-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: FAIL
REASON: The paper's formal model allows singularities with no productivity increase (ĝ = g), contradicting the spec's definition that a singularity "vastly increases productivity and output."

---

## Concept 1: AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output."

### Paper usages

- **Abstract (line 30):** "a negative AI singularity---a sudden AI-driven transformation that displaces existing workers and firms." Describes singularity as transformation/displacement, omitting the defining feature of vastly increased productivity and output.

- **Introduction (line 45):** "A sudden AI breakthrough---a singularity---could dramatically shift the economy's structure, displacing traditional businesses and reducing the investor's share of total output." Again emphasizes structural shift and displacement, not vastly increased output.

- **Model (lines 69–76):** The singularity is formalized with $\tilde{g} \geq g$ (weak inequality). This allows $\tilde{g} = g$, meaning the singularity need not increase the growth rate at all. The model's singularity is fundamentally about output share redistribution (Assumptions 1–2), not about vastly increased productivity.

- **Extension (line 245):** The limit $\tilde{g} \to \infty$ is discussed, which does match "vastly increases productivity and output," but this is presented as a special case, not the baseline.

- **Numerical illustration (line 225):** Uses $g = 0.02$, $\tilde{g} = 0.05$. Post-singularity growth is modestly higher, not "vastly" increased.

### Assessment

**INCONSISTENT.** The spec defines singularity as vastly increasing productivity and output. The model's weak inequality $\tilde{g} \geq g$ encompasses singularities with zero productivity increase. The paper's verbal descriptions emphasize displacement and structural shift rather than the spec's defining feature. Only the extension's limiting case ($\tilde{g} \to \infty$) matches the spec's "vastly increases" language.

---

## Concept 2: Negative AI Singularity

**Spec definition:** "A negative AI singularity is an AI singularity that is devastating for the typical investor."

### Paper usages

- **Abstract (line 30):** "a negative AI singularity---a sudden AI-driven transformation that displaces existing workers and firms." Displacement of workers and firms is devastating for the typical investor.

- **Assumption 1 (lines 95–97):** "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." The household is the representative/typical investor, and a falling output share is devastating.

- **Title:** "Hedging the Singularity" — uses "singularity" without "negative," but the paper makes clear throughout that it studies the negative variant.

- **Introduction (line 49):** "The household is displaced---its consumption share falls." Consistent with devastating for the typical investor.

### Assessment

**Consistent.** The paper's negative singularity is devastating for the typical investor (the representative household) through displacement of consumption share. All usages align with the spec.

---

## Concept 3: Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

### Paper usages

- **Equation 6 (lines 117–119):** The household's budget constraint is explicitly stated: $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.

- **Equation 7 (lines 122–126):** Market clearing ($n_t^A = n_t^N = 1$) plus the budget constraint yields $c_t = D_t^A + D_t^N = \omega Y_t$, which is consistent.

- **Output accounting (lines 82–86):** Total output is fully divided: $D_t^A + D_t^N + D_t^P = \theta Y_t + \nu Y_t + (1 - \theta - \nu) Y_t = Y_t$. Output shares sum to one both pre- and post-singularity.

### Assessment

**Consistent.** Budget constraints are explicitly stated and satisfied. Output accounting sums to one. Market clearing is imposed. No violations detected.

---

## Concept 4: Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

### Paper usages

- **Introduction (line 45):** "In this world of incomplete markets, publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside." Focuses on asset availability. No mention of Arrow-Debreu.

- **Introduction (line 49):** "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium." Focuses on which assets are tradeable.

- **Model (lines 78, 116):** "AI owners hold private AI capital and do not participate in public stock markets." / "The household trades in two publicly available assets...but cannot invest in private AI capital." Incompleteness defined by inaccessible assets.

- **Proposition 4 (lines 206–207):** "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output." Complete markets defined as the household being able to trade the previously unavailable asset (private AI capital).

- **Conclusion (line 285):** "expanding the set of tradeable AI-related assets...could reduce the displacement premium and improve welfare by completing markets." Completing markets means making more assets tradeable.

### Assessment

**Consistent.** The paper never mentions Arrow-Debreu securities. Complete and incomplete markets are discussed entirely in terms of which assets the representative investor can and cannot buy, exactly as the spec prescribes.

---

## Concept 5: Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

### Paper usages

- **Abstract (line 30):** "public AI stocks uniquely valuable as partial insurance against displacement." The word "partial" aligns with "need not be perfect."

- **Introduction (line 45):** "publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside." "Best available" implies imperfect; consistent.

- **Results (line 177):** "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." AI stock payoffs increase when singularity risk materializes. Consistent with spec definition.

- **Results (line 190):** "The valuation spread...reflects the hedging channel: the more the household fears displacement, the more it values AI stocks relative to non-AI stocks." The hedging premium is about valuation (price-dividend ratio), not about expected returns being negative. The paper does not claim AI stocks earn negative risk premia.

- **Proposition 4 (line 214):** "The hedging premium is increasing in risk aversion $\gamma$..." The premium is defined as the valuation gap between incomplete and complete markets ($V_0^A - V_0^{A,CM}$). This measures the additional price the household pays for the hedge, not a negative expected return.

### Assessment

**Consistent.** AI stocks hedge displacement risk because their payoff increases when the singularity materializes. The paper describes the hedge as "partial insurance" (not perfect). The "hedging premium" is a valuation premium, and the paper never claims AI stocks earn negative expected returns overall.

---

## Concept 6: General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

### Paper usages

The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium." The model determines prices endogenously through Euler equations (eq. 8) and market clearing, which is general equilibrium in the spec's sense. Consumption is pinned down by market clearing ($c_t = \omega Y_t$), not by an explicit consumption choice, which avoids the potential misstatement that GE requires endogenous consumption.

### Assessment

**Consistent (by omission).** The paper does not use GE/PE terminology, so there is no opportunity for inconsistency. The model's structure (endogenous prices from equilibrium conditions) is consistent with general equilibrium as the spec defines it.

---

## Cross-Section Consistency Check

### "Singularity" across sections

The term "singularity" is used with different emphasis across sections:
- **Introduction:** Emphasizes displacement and structural shift.
- **Model:** Formalized as an absorbing event with share shifts and $\tilde{g} \geq g$.
- **Extension:** Considers extreme singularity ($\tilde{g} \to \infty$) and extinction risk.
- **Conclusion:** Refers to "moderate" vs. "extreme" singularities.

The model's formal definition (share shift + weakly higher growth) is narrower than the introduction's verbal description (which adds "displacing traditional businesses and reducing the investor's share of total output") but broader than the spec's definition (which requires "vastly increases productivity and output"). The inconsistency with the spec is present across all sections.

### "Displacement" across sections

Used consistently throughout as the household's consumption share falling at the singularity, formalized as $\Delta < 1$.

### "Hedging" across sections

Used consistently as AI stocks providing higher payoffs in singularity states, with a valuation premium reflecting this insurance property.

### "Incomplete markets" across sections

Used consistently as the household's inability to invest in private AI capital.

---

## Summary of Findings

| Concept | Verdict | Issue |
|---|---|---|
| AI Singularity | **INCONSISTENT** | Model allows $\tilde{g} = g$ (no productivity increase); spec requires "vastly increases productivity and output" |
| Negative AI Singularity | Consistent | — |
| Budget Constraints | Consistent | — |
| Complete vs. Incomplete Markets | Consistent | — |
| Hedging | Consistent | — |
| General vs. Partial Equilibrium | Consistent (not used) | — |

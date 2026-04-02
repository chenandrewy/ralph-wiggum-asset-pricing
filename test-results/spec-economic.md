# tests/spec-economic.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 1m 54s
[ralph-garage/agent-logs/20260402T183430.361589-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T183430.361589-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions across all sections.

## Concepts Evaluated

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Abstract: "a sudden AI-driven productivity surge that displaces existing workers and firms" — consistent.
- Section 2.1: "A singularity is an absorbing event that arrives with independent probability $p$ each period" with $\tilde{g} > g$, i.e., output grows at a strictly higher rate — consistent with "vastly increases productivity and output."
- Section 2.1: "The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output" — directly echoes the spec language.

**Cross-section consistency:** The term maintains the same meaning (sudden AI-driven productivity jump) in the introduction, model, results, extension, and conclusion. No drift.

### 2. Negative AI Singularity

**Spec definition:** "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract: "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" — consistent; displacement of the typical investor is devastating.
- Assumption 1 (Section 2.2): "Negative singularity ... The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$" — formalizes "devastating for the typical investor" as a decline in the household's output share.
- Introduction: "displacing traditional businesses and reducing the investor's share of total output" — consistent.

**Note on the extension:** Remark 1 (Section 4.1) explores the limit $\tilde{g} \to \infty$ where household consumption grows so high that marginal utility becomes negligible. In this extreme, the singularity is less "devastating" in absolute terms even though the share still falls. However, the paper does not call this extreme case a "negative AI singularity"; it is analyzing a boundary condition of the model. The baseline framing remains consistent with the spec.

**Cross-section consistency:** Consistent throughout. The label "negative" always refers to the displacement of the household's share.

### 3. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Section 2.3, Eq. (6): The household's budget constraint is explicitly stated: $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.
- Eq. (7): Equilibrium consumption $c_t = D_t^A + D_t^N = \omega Y_t$ follows from market clearing ($n_t^A = n_t^N = 1$) substituted into the budget constraint.
- The three dividend streams sum to total output (Eqs. 3–4), satisfying the aggregate resource constraint.

**Cross-section consistency:** No violations detected. Budget constraints are satisfied throughout.

### 4. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. ... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Introduction: "the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..." — directly matches the spec's definition.
- Section 2.1: "AI owners hold private AI capital and do not participate in public stock markets" — defines the missing asset.
- Section 2.3: "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital" — incomplete markets defined by unavailable assets, not Arrow-Debreu.
- Proposition 4 (Section 3): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$" — complete markets defined as access to the previously missing asset.
- Conclusion: "expanding the set of tradeable AI-related assets ... could reduce the displacement premium and improve welfare by completing markets" — consistent framing.

**Cross-section consistency:** The paper never mentions Arrow-Debreu securities. Complete/incomplete markets always refers to whether the household can invest in private AI capital. Perfectly consistent with the spec.

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract: "publicly traded AI stocks ... hedge against a negative AI singularity" and "partial insurance against displacement" — "partial insurance" is consistent with the spec's note that hedges need not be perfect.
- Introduction: "publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside" — payoff increases when singularity risk materializes.
- Section 3 (after Proposition 1): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." — directly matches: payoff increases when risk materializes.
- Proposition 4: "hedging premium" defined as the valuation difference between incomplete and complete markets — arises because AI stocks' payoffs increase in displacement states.
- Section 4.1: "the hedge is worthless if the economy is destroyed" (extinction case) — consistent; if the economy is destroyed, the payoff does not increase.

**Cross-section consistency:** "Hedge" always means the asset's payoff increases when displacement risk materializes. The paper never implies the hedge must be perfect or that AI stocks earn negative risk premia. Fully consistent.

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:** The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. The model is general equilibrium by the spec's definition: prices are determined endogenously through Euler equations (Eq. 8) and market clearing conditions. The paper does not conflate general equilibrium with endogenous consumption.

**Cross-section consistency:** No inconsistency possible since the terms are not used. The model's structure is consistent with the spec's definition of general equilibrium.

## Summary of Findings

No inconsistencies found. All six concepts from the economic background spec are used consistently with their definitions across all sections of the paper (abstract, introduction, model, results, extension, conclusion, and appendix). The paper avoids the specific pitfalls flagged in the spec (e.g., Arrow-Debreu framing of complete/incomplete markets, conflating GE with endogenous consumption).

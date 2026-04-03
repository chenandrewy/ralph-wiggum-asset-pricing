# tests/spec-economic.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260402T222807.263646-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T222807.263646-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper, with one minor ambiguity in the "negative AI singularity" definition that does not change the economic meaning.

## Concept-by-concept analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Abstract: "a sudden AI-driven productivity surge that displaces existing workers and firms" ✓
- Introduction (line 52): "A sudden AI breakthrough---a singularity---could dramatically increase productivity while shifting the economy's structure" ✓
- Model (line 82–86): "output grows at a strictly higher rate, reflecting the productivity increase that accompanies the singularity" with $\tilde{g} > g$; "the paper's economic focus is on large disruptions---singularities that vastly increase productivity and substantially displace existing firms" ✓

The paper is careful to note "The algebra holds for any $\tilde{g} > g$" but explicitly states the economic focus is on large disruptions, consistent with the spec's "vastly increases."

**Consistency across sections:** The term keeps its meaning (sudden, large productivity increase) in every section: introduction, model, results, extension, and conclusion. No drift.

### 2. Negative AI Singularity

**Spec definition:** "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract (line 30): "negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms"
- Assumption 1 (line 106): "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$"
- Results (line 188): "Because the household is displaced at the singularity ($\Delta < 1$), its marginal utility is high in singularity states"

**Minor ambiguity:** The paper defines "negative" via displacement (share of output falls), while the spec says "devastating for the typical investor." In the paper's main parameterization ($\gamma > 1$, moderate $\tilde{g}$), displacement does make the household strictly worse off in utility terms—marginal utility is high, meaning the household's welfare has dropped. This is consistent with "devastating." In the extension (Remark 1), when $\tilde{g} \to \infty$, the household's consumption grows enormously despite losing share, and the hedging premium vanishes—arguably the event is no longer "devastating." However, the paper explicitly discusses this as a limiting edge case that erodes the mechanism, and never labels the extreme singularity as "negative." The core usage is consistent with the spec.

### 3. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage:**
- Equation (6), line 128: explicit budget constraint for the household
- Equation (7), line 133: equilibrium consumption derived from market clearing ($n_t^A = n_t^N = 1$), giving $c_t = D_t^A + D_t^N = \omega Y_t$
- Equations (3)–(4): output shares sum to 1 by construction ($\theta + \nu + (1 - \theta - \nu) = 1$)

Budget constraints are satisfied throughout. No violations detected. ✓

### 4. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities... Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Introduction (line 52): "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..."
- Model (line 126): "The household trades in two publicly available assets... but cannot invest in private AI capital."
- Proposition 3 (line 205): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$."
- Conclusion (line 273): "expanding the set of tradeable AI-related claims... could reduce the displacement premium"

The paper consistently defines incomplete markets in terms of the specific asset unavailable to the representative investor (private AI capital), exactly as the spec requires. Complete markets is defined as the household gaining access to that specific asset. No mention of Arrow-Debreu securities. ✓

**Consistency across sections:** The concept maintains the same meaning in introduction, model, results, extension (Section 4.2 on overcoming frictions), and conclusion. No drift.

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract (line 30): "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity" and "partial insurance against displacement"
- Introduction (line 52): "publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside"
- Results (line 188): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge."
- Proposition 3 (line 211): hedging premium formula showing $V_{\mathrm{pre}}^A - V_{\mathrm{pre}}^{A,\mathrm{CM}} > 0$

The paper's usage matches the spec precisely: AI stocks hedge because their payoff increases when the singularity risk materializes ($\tilde{\theta} > \theta$). The paper uses "partial insurance" (consistent with "need not be perfect") and never claims AI stocks earn a negative risk premium—the premium is a *valuation* premium (higher price-dividend ratio), not a negative expected return. ✓

**Consistency across sections:** The hedging concept is applied uniformly from abstract through conclusion. In the extension, Remark 1 discusses when the hedge loses value (extreme singularity), but this is about the mechanism weakening, not a redefinition.

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage:** The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. However, the model is a general equilibrium model by the spec's definition: prices are determined endogenously through the Euler equation (eq. 8) and market clearing ($n_t^A = n_t^N = 1$). Consumption is determined by market clearing, not by an optimization that trades off consumption against some outside option. This is consistent with the spec's distinction: prices are determined by equilibrium conditions (GE), and consumption being pinned down by market clearing is a consequence of equilibrium, not the defining feature. ✓

No inconsistency because the terms are not used, and the implicit treatment is consistent with the spec.

## Cross-section consistency check

All five concepts maintain their definitions across:
- Abstract → Introduction: consistent framing
- Introduction → Model: informal language correctly formalized
- Model → Results: definitions carry through to propositions
- Results → Extension: concepts applied to new settings without redefinition
- Extension → Conclusion: summary language matches formal usage

No cross-section drift detected.

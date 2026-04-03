# tests/spec-economic.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 1m 34s
[ralph-garage/agent-logs/20260402T225431.389040-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T225431.389040-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output." "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract (line 30): "negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" --- captures both the productivity surge and the negative impact on the typical investor (via displacement).
- Model, line 74: "A singularity is an absorbing event that arrives with independent probability $p$" --- defines the stochastic structure; the productivity increase is captured by $\tilde{g} > g$ (line 81).
- Model, line 82: "singularities that vastly increase productivity and substantially displace existing firms" --- matches spec's "vastly increases productivity and output."
- Assumption 1 (line 101): "Negative singularity" defined as $\tilde{\omega} < \omega$, i.e., the household's share of output falls --- consistent with "devastating for the typical investor."
- Extension (line 232): "the event is catastrophic---all output is permanently destroyed" --- extinction variant, clearly distinguished from the baseline singularity.

**Assessment:** Consistent. The paper uses "singularity" to mean a sudden, large productivity increase throughout, and "negative" to mean the typical investor is harmed via displacement. No drift across sections.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Equation (6), line 123--124: Explicit budget constraint for the household, with consumption plus asset purchases equaling dividend income plus asset sales proceeds.
- Line 128: Market clearing $n_t^A = n_t^N = 1$ pins down equilibrium consumption as $c_t = D_t^A + D_t^N = \omega Y_t$.
- Output shares sum to 1: $\theta + \nu + (1 - \theta - \nu) = 1$ by construction (line 88).

**Assessment:** Consistent. Budget constraints are explicitly stated and satisfied. No violations.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor." "Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Introduction, line 52: "In this world of incomplete markets, publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside." --- Incomplete markets defined through the unavailable asset (private AI capital).
- Introduction, line 56: "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium." --- Complete markets defined as access to private AI capital.
- Model, line 122: "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital." --- Defines the market incompleteness directly.
- Proposition 3, line 200--201: "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$." --- Consistent framing.
- Extension, line 250: "GKP's assumption that displacement persists is driven by real-world frictions" --- Consistent with incomplete markets being about unavailable assets, not Arrow-Debreu.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu securities. Both complete and incomplete markets are consistently defined through the availability of private AI capital to the representative investor, matching the spec exactly.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract, line 30: "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity" --- AI stock payoffs increase when singularity materializes ($\tilde{\theta} > \theta$). Consistent.
- Introduction, line 52: "publicly traded AI stocks offer the best available hedge" --- "best available" implies imperfect, consistent with "need not be perfect."
- Introduction, line 56: "hedging premium: in singularity states, the household's marginal utility is high... while AI stocks pay relatively more. This positive covariance... lowers the required return and raises the valuation." --- The premium is a valuation effect (lower required return), not a claim that AI stocks earn a negative risk premium overall. Consistent.
- Results, line 184: "AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." --- Payoff increases when risk materializes. Consistent.
- Results, line 184: "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices." --- Direct match to spec definition.

**Assessment:** Consistent. The paper uses "hedge" to mean payoff increases when the risk materializes. It never claims the hedge is perfect or that AI stocks earn a negative risk premium overall.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous." "Partial equilibrium means that prices are exogenous."

**Paper usages:**

The paper does not use the terms "general equilibrium" or "partial equilibrium" explicitly. The model determines prices via the Euler equation (equilibrium condition, eq. 7 at line 136), and consumption is pinned down by market clearing (line 128--131). This is consistent with a general equilibrium framework per the spec's definition, though the paper does not label it as such.

**Assessment:** Consistent by absence. The paper does not use these terms and therefore cannot misuse them. The model structure is consistent with general equilibrium as defined by the spec (prices determined by equilibrium conditions).

## Cross-Section Consistency Check

All five concepts maintain stable meaning across:
- **Abstract vs. Model:** Singularity, hedging, and incomplete markets definitions align between the informal abstract and the formal model.
- **Model vs. Results:** Displacement, hedging premium, and market completeness carry the same meaning from setup through propositions.
- **Results vs. Extension:** The extension (extinction risk, Coase theorem) uses singularity, displacement, and complete/incomplete markets consistently with the baseline model.
- **Conclusion:** Reuses "displacement premium," "hedging premium," and "market completeness" consistently with all prior sections.

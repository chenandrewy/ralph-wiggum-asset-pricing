# tests/spec-economic.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 2m 8s
[ralph-garage/agent-logs/20260402T214942.812050-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.812050-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions across all sections.

## Concepts Evaluated

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**

- Abstract (line 30): "negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" — matches "sudden" and "productivity surge."
- Intro (line 52): "A sudden AI breakthrough---a singularity---could dramatically increase productivity while shifting the economy's structure" — "sudden" and "dramatically increase productivity" consistent.
- Model (line 76): "A singularity is an absorbing event that arrives with independent probability $p$ each period" — "absorbing event" captures "sudden" (single-period arrival).
- Model (line 80–84): "output grows at a strictly higher rate, reflecting the productivity increase... The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output." — The paper explicitly acknowledges the spec's "vastly increases" framing by reserving that language for the extreme case while allowing the model to parameterize magnitude.
- Extension (line 252): "as $\tilde{g} \to \infty$, the AI owners... enjoy unbounded consumption" — consistent with vast increase.

**Assessment:** Consistent. The paper models the singularity as a sudden, absorbing event with higher productivity growth, matching the spec. The generalization to allow varying magnitudes is standard parameterization; the paper correctly reserves "vastly increases" for the extreme case.

### 2. Negative AI Singularity

**Spec definition:** "A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract (line 30): "negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" — displacement of workers and firms is devastating for the typical investor.
- Model, Assumption 1 (line 103–105): "Negative singularity... The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." — The household is the "typical investor" (representative household / marginal investor in public markets). A fall in output share is the formal analog of "devastating."
- Model (line 111–115): "displacement ratio $\Delta \equiv \tilde{\omega}/\omega < 1$" — captures severity of the negative impact on the typical investor.
- Results (line 185): "Because the household is displaced at the singularity ($\Delta < 1$), its marginal utility is high in singularity states: $\Delta^{-\gamma} > 1$." — High marginal utility reflects low consumption, consistent with devastating impact.

**Assessment:** Consistent. The paper consistently treats "negative" as referring to the typical investor (household) being displaced—losing share of output—which is the formal version of "devastating for the typical investor."

### 3. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (line 124–128): Explicit budget constraint in eq. (6): $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.
- Model (line 130–134): Market clearing ($n_t^A = n_t^N = 1$) combined with the budget constraint yields equilibrium consumption: $c_t = D_t^A + D_t^N = \omega Y_t$.
- Output shares (line 90–93): $D_t^A + D_t^N + D_t^P = Y_t$ — total output is fully accounted for.

**Assessment:** Consistent. Budget constraint is explicitly stated, and output is fully allocated among the three dividend streams. No violations.

### 4. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages (incomplete markets):**

- Intro (line 52): "the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets, publicly traded AI stocks offer the best available hedge" — Correctly focuses on unavailable assets, not Arrow-Debreu.
- Model (line 124): "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital." — Defines market incompleteness as inability to buy private AI capital.
- Conclusion (line 289): "expanding the set of tradeable AI-related assets... could reduce the displacement premium and improve welfare by completing markets" — Completing markets = making more assets tradeable, not Arrow-Debreu.

**Paper usages (complete markets):**

- Proposition 4 (line 215): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output: $c_t = Y_t$." — Defines complete markets as access to the missing asset (private AI capital), exactly per spec.
- Proof (line 226–228): "Under complete markets, the household's consumption growth in the singularity state is $(1+\tilde{g})$ rather than $\Delta(1+\tilde{g})$" — Consequence of investing in private AI capital.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu securities. Both complete and incomplete markets are defined entirely in terms of which assets the representative investor can trade, matching the spec precisely.

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract (line 30): "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity" and "partial insurance against displacement" — "partial" consistent with "need not be perfect."
- Intro (line 52): "publicly traded AI stocks offer the best available hedge: they are the investor's only tradeable claim on the AI upside" — "best available" implies imperfect.
- Results (line 185): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." — Payoff increases when risk materializes, matching the spec definition exactly.
- Proposition 4 (line 219–223): "hedging premium" defined as the valuation gap between incomplete and complete markets — a price premium, not a claim about negative risk premia.
- Conclusion (line 283): "values public AI stocks for their insurance properties: they pay relatively more in singularity states when the household's marginal utility is high" — payoff increases when risk materializes.

**Assessment:** Consistent. The paper defines hedging as payoff increasing when the singularity risk materializes, uses "partial insurance" (not perfect), and expresses the hedging benefit as a valuation premium rather than claiming negative risk premia.

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere. Prices are determined endogenously through the Euler equation and market clearing (eq. 7–8), which is general equilibrium in nature. Consumption is determined by market clearing (eq. 8), which is an equilibrium condition. The paper does not mischaracterize the relationship between equilibrium and consumption endogeneity.

**Assessment:** No usage to evaluate. The paper avoids these terms entirely, so no inconsistency is possible.

## Cross-Section Consistency Check

The following terms were traced across all sections (abstract, introduction, model, results, extension, conclusion, appendix) for meaning drift:

- **Singularity:** Consistently an absorbing, sudden event with probability $p$ that shifts output shares and increases growth rate. No drift.
- **Displacement / negative singularity:** Consistently the household's output share falling ($\Delta < 1$). No drift.
- **Hedging:** Consistently AI stock payoff increasing when singularity occurs. No drift.
- **Incomplete markets:** Consistently the household's inability to invest in private AI capital. No drift.
- **Complete markets:** Consistently the household's ability to invest in all assets including private AI capital. No drift.
- **Budget constraint:** Stated once, satisfied throughout. No drift.

## Minor Observations (Not Inconsistencies)

1. The spec defines AI singularity with "vastly increases productivity and output." The baseline model requires only $\tilde{g} > g$, which permits moderate increases. However, the paper explicitly acknowledges this (line 84: "the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output"), correctly reserving the spec's language for the appropriate case. The model's parameterization is a standard generalization that encompasses the spec's definition as a special case.

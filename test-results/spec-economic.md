# tests/spec-economic.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 1m 35s
[ralph-garage/agent-logs/20260409T190308.203782-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.203782-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Findings

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usage:**

- Abstract (line 32): "an AI singularity that displaces their consumption" — consistent, describes a negative singularity.
- Introduction (line 49): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" — consistent with both the generic and negative definitions.
- Model (line 89–98): Singularity produces aggregate consumption jump of $1+\eta$ (productivity/output increase) with displacement $\phi < 1$ (devastating for household). Consistent.
- Extension 1 (lines 201–205): Introduces positive singularity ($\phi^+ > 1$, household gains) vs. negative singularity ($\phi < 1$, household loses). The negative singularity matches the spec's "devastating for the typical investor" definition. The positive singularity retains the core "sudden improvement" feature but is not devastating, consistent with the spec's two-tier definition.
- Conclusion (line 271): "an AI singularity that would displace their consumption" — consistent.

**Assessment:** Consistent throughout. The baseline model features exclusively negative singularities; Extension 1 correctly distinguishes positive from negative.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage:**

- Model (lines 80–110): Aggregate consumption $C_t$ is split between the household ($\alpha_t C_t$) and AI owners ($(1-\alpha_t) C_t$), summing to $C_t$. Public dividends ($\theta_t C_t$ for AI stocks, $(1-\theta_t) C_t$ for non-AI stocks) sum to $C_t$. Private AI capital pays $(1-\alpha_t)C_t - \theta_t C_t$, the residual. The constraint $\alpha_t \in (0, 1-\theta_t]$ ensures private capital dividends are non-negative. No violations.
- Extension 2 (line 242): Transfer consumption equation explicitly accounts for the household's displaced consumption plus net transfer minus deadweight costs. Budget balanced.

**Assessment:** No budget constraint violations. The paper does not discuss budget constraints explicitly (nor does it need to), and all accounting identities are satisfied.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor." Complete markets also does not necessarily refer to Arrow-Debreu securities. "Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usage:**

- Abstract (line 32): "markets are incomplete---investors cannot trade private AI capital" — directly matches spec (specific assets unavailable).
- Introduction (line 49): "If markets were complete, investors could insure against this risk directly by trading claims on AI capital. But much of this capital is private" — focuses on which assets are unavailable, not Arrow-Debreu. Consistent.
- Model (line 110): "The household cannot trade this private capital. This is the source of market incompleteness" — consistent.
- Discussion (line 172): "the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk" — consistent, defines completeness in terms of tradable assets.
- Extension 1 (line 230): "Under complete markets, the household can trade claims on private AI capital before the singularity." — consistent, complete markets = access to previously unavailable assets.

**Assessment:** Fully consistent. The paper never invokes Arrow-Debreu securities. Every reference to market completeness/incompleteness focuses on whether the household can trade specific assets (private AI capital).

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**

- Introduction (line 49): "AI stocks serve as a hedge against a risk" — consistent.
- Introduction (line 49): "publicly traded AI stocks as an imperfect substitute" — consistent with "need not be perfect."
- Model (line 141): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement" — payoff increases when risk materializes, explicitly called "partial." Consistent.
- Lit review (line 64): "growth stocks provide a partial hedge" — consistent.
- Discussion (line 172): "perfectly hedge displacement risk" under complete markets — describes the counterfactual, consistent.
- Conclusion (line 271): "investors use AI stocks to partially insure against an AI singularity" — consistent.

**Assessment:** Fully consistent. The paper always qualifies the hedge as "partial" or "imperfect" for public AI stocks, reserving "perfect" hedge for the counterfactual of complete markets. Usage aligns with the spec's definition that the payoff increases when risk materializes.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usage:**

- Lit review (line 64): "general-equilibrium model" referring to GKP2012 — GKP2012 determines prices via equilibrium, consistent.
- The paper's own model: Prices are determined by the household's Euler equation (equilibrium condition), while consumption paths are exogenous. The paper does not label its own model as GE or PE, but the structure is GE per the spec's definition (prices from equilibrium conditions).
- The paper never claims that GE requires endogenous consumption, nor does it claim its exogenous consumption structure makes it PE.

**Assessment:** Consistent. The paper correctly attributes GE to GKP2012 and does not misuse the GE/PE distinction. Its own model has endogenous prices from equilibrium conditions (GE) with exogenous consumption, which is consistent with the spec's clarification that GE does not require endogenous consumption.

## Cross-Section Consistency Check

All five concepts maintain identical economic meaning across the abstract, introduction, model, quantitative analysis, extensions, conclusion, and appendix. No drift in usage was detected.

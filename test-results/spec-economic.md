# tests/spec-economic.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 1m 32s
[ralph-garage/agent-logs/20260402T215920.395413-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T215920.395413-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Abstract (line 30): "a sudden AI-driven productivity surge that displaces existing workers and firms" — matches "sudden" and "productivity."
- Introduction (line 52): "A sudden AI breakthrough---a singularity---could dramatically increase productivity" — matches.
- Model §2.1 (lines 82–86): Singularity increases growth from $g$ to $\tilde{g} > g$, "reflecting the productivity increase that accompanies the singularity." The limit $\tilde{g} \to \infty$ is described as "a singularity that vastly increases output" — directly echoes the spec's "vastly increases productivity and output."
- Extension §4.1 (line 258): "consumption is so high" in the extreme singularity — consistent with vastly increased output.

**Assessment:** Consistent. The singularity is always presented as a sudden, productivity-increasing event across all sections.

---

### 2. Negative AI Singularity

**Spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract (line 30): "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms."
- Introduction (line 52): "the typical investor" whose "wealth is largely tied to existing firms and human capital" faces displacement.
- Model §2.2, Assumption 1 (lines 105–107): "Negative singularity" defined as $\tilde{\omega} < \omega$ — the household's (i.e., the typical investor's, per line 88) share of output falls.
- Results §3 (line 188): "the household is displaced at the singularity ($\Delta < 1$), its marginal utility is high in singularity states."

**Assessment:** Consistent. The paper defines the representative household as the typical/marginal investor (line 88) and consistently models the negative singularity as devastating for this agent through displacement. The household loses consumption share, and with $\gamma > 1$, this is welfare-reducing — matching "devastating."

---

### 3. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Model §2.2 (lines 92–96): Output is fully allocated: $\theta + \nu + (1-\theta-\nu) = 1$ pre-singularity, and $\tilde{\theta} + \tilde{\nu} + (1-\tilde{\theta}-\tilde{\nu}) = 1$ post-singularity. No output is lost or created.
- Model §2.3 (lines 126–129): The household budget constraint is explicitly stated in equation (6): consumption plus portfolio investment equals portfolio wealth plus dividends.
- Equilibrium (lines 132–136): Market clearing ($n_t^A = n_t^N = 1$) yields $c_t = D_t^A + D_t^N = \omega Y_t$, which is consistent with the budget constraint.
- Extension §4.2 (lines 269–273): Transfers are explicitly resource-feasible — the cost $F + \tau T$ is paid from output, and the transfer $T = (\omega - \tilde{\omega})Y$ is bounded by the AI owners' gains.

**Assessment:** Consistent. Budget constraints are satisfied throughout. Output shares sum to one, the household budget constraint is explicit, and market clearing is imposed. No violations detected.

---

### 4. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor" (e.g., privately-held AI firms). Does NOT necessarily refer to Arrow-Debreu securities. Complete markets should focus on "important assets that are unavailable to the representative investor."

**Paper usages:**
- Introduction (line 52): "Private AI ventures... the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..." — matches spec exactly: focuses on specific unavailable assets, not Arrow-Debreu.
- Model §2.1 (line 88): "AI owners hold private AI capital and do not participate in public stock markets" — the specific asset the household cannot access.
- Model §2.3 (line 126): "cannot invest in private AI capital" — restates the incompleteness.
- Results, Proposition 4 (lines 217–218): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output" — complete markets defined by the household gaining access to the specific missing asset, not by Arrow-Debreu completion.
- Conclusion (line 286): "expanding the set of tradeable AI-related claims" as the policy lever — again framed as making specific assets available.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu securities. Both complete and incomplete markets are consistently defined in terms of whether the household can access private AI capital — the specific important asset — matching the spec's framing.

---

### 5. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract (line 30): "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity" and are "partial insurance against displacement" — "partial" is consistent with the hedge not needing to be perfect.
- Introduction (line 52): "publicly traded AI stocks offer the best available hedge" — does not claim perfection.
- Introduction (line 56): "positive covariance between the stochastic discount factor and AI dividends" — the pricing mechanism behind hedging.
- Results §3 (line 188): "Assets that pay more in these high-marginal-utility states are valuable hedges... AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$)" — AI stock payoff increases when displacement risk materializes. Matches spec: "payoff tends to increase when that risk materializes."
- The paper never claims AI stocks earn a negative risk premium overall; it discusses a valuation premium (higher price-dividend ratio), which is distinct.

**Assessment:** Consistent. The paper uses "hedge" to mean that AI stock payoffs increase when displacement risk materializes, does not claim the hedge is perfect ("partial insurance"), and does not claim a negative risk premium.

---

### 6. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = "prices are determined by equilibrium conditions," NOT that consumption is endogenous. Partial equilibrium = "prices are exogenous."

**Paper usages:**
- The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium."
- The model's prices are determined endogenously via the Euler equation (line 141), which is an equilibrium condition. This is general equilibrium per the spec.
- Consumption is determined by market clearing ($c_t = \omega Y_t$), which could be read as "endogenous" in the sense of being an equilibrium outcome, but the paper does not invoke this to claim general equilibrium.

**Assessment:** Consistent (trivially). The paper avoids these terms entirely, so there is no opportunity for misuse. The model itself is general equilibrium by the spec's definition (prices from equilibrium conditions), but the paper does not make any claims that could conflict with the spec.

---

## Cross-Section Consistency Check

The following terms were checked for drift across sections:

| Term | Intro | Model | Results | Extension | Conclusion |
|------|-------|-------|---------|-----------|------------|
| Singularity | Sudden productivity surge | Absorbing regime shift, $\tilde{g} > g$ | Same | Same + extreme limit | Same |
| Negative singularity | Displacement of workers/firms | $\tilde{\omega} < \omega$ | $\Delta < 1$ | Same | Same |
| Incomplete markets | Can't buy private AI | Same | Same | Same | Same |
| Complete markets | — | — | Can invest in private AI capital | — | Expand tradeable claims |
| Hedging | Partial insurance | — | Payoff up when risk materializes | Same | Same |
| Displacement | Share of output falls | $\Delta < 1$ | Same | Same + frictions analysis | Same |

No cross-section drift detected. All terms maintain their economic meaning throughout.

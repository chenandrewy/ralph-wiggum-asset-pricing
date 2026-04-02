# tests/spec-economic.py
Started: 2026-04-02 18:17:45 EDT
Runtime: 1m 48s
[ralph-garage/agent-logs/20260402T181745.338907-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260402T181745.338907-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses economic terminology consistently with the spec definitions throughout all sections, with only minor rhetorical looseness in the abstract.

## Concepts Evaluated

### 1. AI Singularity
**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**
- Abstract: "a sudden AI-driven productivity surge" -- consistent.
- Intro (line 43): "A sudden AI breakthrough---a singularity---could dramatically increase productivity while shifting the economy's structure" -- consistent.
- Model (line 69): "A singularity is an absorbing event that arrives with independent probability $p$" with growth shifting from $g$ to $\tilde{g} > g$ -- consistent (absorbing = sudden regime change).
- Model (line 77): "The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output" -- directly echoes spec language.
- Extension (line 246): explores $\tilde{g} \to \infty$ limit -- consistent with "vastly increases."

**Assessment:** Consistent. The singularity is always presented as sudden (one-period absorbing shock) and as increasing productivity. The extension explicitly connects to the "vastly increases" language.

### 2. Negative AI Singularity
**Spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract (line 30): "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms" -- note: mentions "workers and firms" rather than "the typical investor."
- Intro (line 44): "displacing traditional businesses and reducing the investor's share of total output" -- shifts focus to the investor.
- Assumption 1 (line 97): "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$" -- formalizes devastation for the representative household (the typical investor).
- Model (line 108): "the singularity displaces the household by shifting output toward private AI capital" -- consistent, focuses on the household/investor.

**Assessment:** Consistent in substance. The abstract's mention of "workers and firms" is a rhetorical shorthand; the model contains no labor market, and the formal mechanism operates entirely through the representative household's (i.e., the typical investor's) consumption share falling, which matches the spec. The intro and all formal sections correctly focus on the investor.

### 3. Budget Constraints
**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Eq. (6), line 119: explicit budget constraint for the household: $c_t + P_t^A n_{t+1}^A + P_t^N n_{t+1}^N = (D_t^A + P_t^A) n_t^A + (D_t^N + P_t^N) n_t^N$.
- Eqs. (3)--(4), lines 85--91: output shares sum to 1 both pre- and post-singularity ($\theta + \nu + (1 - \theta - \nu) = 1$).
- Market clearing at $n_t^A = n_t^N = 1$ yields $c_t = D_t^A + D_t^N = \omega Y_t$ (line 126), consistent with the budget constraint.
- Complete markets case (Proposition 4): $c_t = Y_t$, consistent with household accessing all three dividend streams.

**Assessment:** Consistent. Budget constraints are explicitly stated and satisfied. Output accounting is consistent across regimes.

### 4. Complete vs. Incomplete Markets
**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Intro (line 45): "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets..." -- consistent, focuses on asset access.
- Model (line 117): "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital." -- consistent.
- Proposition 4 (line 208): "Under complete markets, the household can also invest in private AI capital, so its consumption equals total output." -- consistent, defines complete markets as access to private AI capital, not Arrow-Debreu.
- Conclusion (line 280): "Under complete markets, the premium vanishes." -- consistent.

**Assessment:** Fully consistent. The paper never references Arrow-Debreu securities. Complete and incomplete markets are always framed in terms of the representative investor's access to private AI capital, exactly as the spec requires.

### 5. Hedging
**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract (line 30): "publicly traded AI stocks uniquely valuable as partial insurance against displacement" -- "partial" is consistent with "need not be perfect."
- Intro (line 45): "publicly traded AI stocks offer the best available hedge" -- consistent, "best available" implies imperfect.
- Results (line 178): "Assets that pay more in these high-marginal-utility states are valuable hedges and command higher prices. AI stocks gain share at the singularity ($\tilde{\theta}/\theta > 1$), so they are precisely such a hedge." -- consistent: payoff increases when displacement risk materializes.
- Proposition 4 (line 214): hedging premium defined as difference in price-dividend ratios between incomplete and complete markets -- consistent, the premium is a valuation effect (lower required return), not a claim that AI stocks earn negative expected returns.

**Assessment:** Fully consistent. The paper correctly uses "hedge" to mean that AI stock payoffs increase when displacement risk materializes. It explicitly notes the hedge is partial ("best available," "partial insurance"). It never claims AI stocks earn negative risk premia -- only that they earn a lower required return due to their hedging properties.

### 6. General Equilibrium vs. Partial Equilibrium
**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**
- The paper does not explicitly use the terms "general equilibrium" or "partial equilibrium."
- The model is general equilibrium by the spec's definition: prices are determined endogenously through the Euler equation (eq. 8) and market clearing ($n_t^A = n_t^N = 1$).

**Assessment:** No inconsistency. The paper does not invoke these terms, so there is no opportunity for misuse. The model's structure (endogenous prices via equilibrium conditions) is consistent with general equilibrium as defined in the spec.

## Section-by-Section Summary

| Section | Findings |
|---------|----------|
| Abstract | All terms used consistently. Minor: "workers and firms" phrasing for negative singularity, but substantively aligned with spec. |
| Introduction | All terms consistent. Correctly frames incomplete markets as asset access, hedging as payoff covariance, singularity as sudden productivity shift. |
| Model | All definitions formalized consistently with the spec. Budget constraint explicit and satisfied. |
| Results | Hedging premium correctly derived from displacement channel. Complete/incomplete markets distinction consistent. |
| Extension | Singularity definition extended to extreme cases, consistent with "vastly increases productivity." No terminology drift. |
| Conclusion | Restates key results using the same terminology as earlier sections. No cross-section drift. |
| Appendix | Formal proofs use notation consistently with the main text. No terminology issues. |

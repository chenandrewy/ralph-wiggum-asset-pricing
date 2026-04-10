# tests/factcheck-theory.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 9m 15s
[ralph-garage/agent-logs/20260409T210609.001699-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T210609.001699-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: FAIL
REASON: The model's dividend definitions exhaust aggregate consumption through public stocks, leaving zero residual for private AI capital dividends, contradicting the assumption that private capital has positive dividends.

## Requirement 1: Notational Consistency — PASS

All 22 symbol families were audited. Zero collisions found. Three minor ambiguities flagged, all standard conventions in asset pricing:

1. **`α` family**: `α_t` is a stochastic state variable but appears unsubscripted as a fixed parameter in Section 4.2. The shift is never noted explicitly.
2. **`θ` family**: Same issue — `θ_t` becomes unsubscripted `θ` in the P/D formulas and `Γ` definitions.
3. **`u` (period utility)**: Used in the Proposition 3 proof ("u is concave") but never formally defined. The paper defines lifetime utility `U_0^H` with the CRRA kernel inline but never names the period felicity function.

These are standard conventions and do not constitute variable collisions or genuine ambiguity for the target audience.

## Requirement 2: Assumption Consistency — FAIL

### Critical issue: Resource accounting (A7 + A8 vs. A9)

**The problem.** Assumptions A7 and A8 define:

- $D_t^{AI} = \theta_t C_t$
- $D_t^N = (1 - \theta_t) C_t$

So $D_t^{AI} + D_t^N = C_t$: total public stock dividends exhaust all aggregate consumption.

Assumption A9 then states that AI owners hold "private AI capital" whose dividends are "the residual accruing to AI owners beyond the public AI dividend." But the formal definitions leave zero residual. If $C_t$ is aggregate consumption and public dividends already sum to $C_t$, any additional private capital dividends would violate the aggregate budget constraint.

**Why this matters.** The budget constraint is a foundational element of any asset pricing model. The paper's narrative relies on private AI capital as the source of market incompleteness—the household cannot trade it—but the formal model does not actually leave room for this object to have positive dividends.

**Impact on pricing results: None.** Private AI capital never enters any pricing equation. All P/D ratios, existence conditions, and comparative statics depend only on the household's SDF and the two public dividend processes, which are internally consistent. The inconsistency is between the formal dividend definitions and the narrative model description, not within the pricing formulas themselves.

**How to fix.** Either (a) redefine public dividends so they represent only a fraction of aggregate consumption, leaving a residual for private capital (e.g., $D_t^{AI} = \theta_t \omega C_t$, $D_t^N = (1-\theta_t) \omega C_t$ for some $\omega < 1$), or (b) reframe "private AI capital" as restricted shares of the public AI stock that the household cannot purchase, rather than an additional dividend stream.

### Additional issues

2. **Missing implicit constraint on deadweight costs (low severity).** The net transfer $\tau(1 - \delta\tau)$ requires $\delta\tau < 1$ to be positive. This is never stated. Under the calibration ($\delta = 0.5$, $\tau < 1$), it is always satisfied.

3. **Stationarity approximation magnitude (low severity).** The paper says the approximation is "accurate for small $\Delta\theta$" but uses $\Delta\theta = 0.2$. Post-singularity $\Gamma^{AI}$ drops ~33% (from 3.20 to 2.14), meaning the approximation overstates AI P/D ratios. Directional results are preserved.

### Verified consistent

- All parameter domain restrictions: no contradictions.
- Aggregate consumption dynamics (level shift, not growth-rate shift): consistent.
- State variable bounds ($\alpha_t$, $\theta_t$ remain in $(0,1)$ under repeated singularities): verified.
- Existence condition under baseline calibration ($A^j < 1$ for both assets): verified numerically.
- Existence violation under large singularity ($\tau = 0$): intentional and correctly acknowledged.
- Extension 1 positive singularity vs. baseline: consistent.
- Extinction utility normalization ($U_\text{ext} = 0$ with $\gamma > 1$): consistent and correctly described as conservative.
- Transfer formula and effective displacement: algebraically verified.
- Proposition 2 comparative statics: all three parts internally consistent.

## Requirement 3: Traceability — NOT EVALUATED

Per procedure, analysis stops after a Requirement 2 failure.

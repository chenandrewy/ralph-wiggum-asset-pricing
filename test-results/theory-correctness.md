# tests/theory-correctness.py
Started: 2026-03-21 22:42:48 EDT
Runtime: 2m 18s
[ralph-garage/agent-logs/20260322T024248.934913Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T024248.934913Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical derivations are correct, assumptions are mutually consistent, notation is uniform, and all verbal claims are supported by the formal theory.

## Condition 1: Notational Consistency
All mathematical objects are used consistently throughout. Key objects: $c_t$ (consumption), $\beta$ (discount factor), $\gamma$ (risk aversion), $D_t^A, D_t^N$ (dividends), $s$ (AI share), $\lambda$ (singularity probability), $g$ (growth), $\theta, \phi$ (singularity parameters), $J(s)$ (jump factor), $M_{t,t+1}$ (SDF), $a$ (effective discount factor), $\bar{v}$ (benchmark P/D), $v^A, v^N$ (equilibrium P/D ratios), $\delta$ (extinction probability). No notation conflicts found.

## Condition 2: Consistent Assumptions
Assumptions: $\gamma > 1$, $\beta \in (0,1)$, $g > 0$, $\theta > 0$, $\phi \in (0,1)$, $\lambda \in (0,1)$, $a < 1$, $\delta \in [0,1)$, and $c_t = D_t^A + D_t^N$. The constant pre-singularity share $s$ is consistent with both dividends growing at rate $g$ in normal times. The assumption $a < 1$ is automatically satisfied given $\beta < 1$, $g > 0$, $\gamma > 1$. No contradictions.

## Condition 3: Logical Results
- **Consumption jump (eq 6):** Algebraically verified from substituting singularity transitions into consumption identity.
- **SDF values:** Correctly derived from CRRA utility and consumption growth in each state.
- **Proposition 1 (eq 7-8):** Euler equation solved correctly. Cross-verified numerically: figure coefficients ($K_A = 31.564$, $K_N = 14.232$, $K_M = 16.832$) and table values all match the closed-form expressions with baseline parameters.
- **Proposition 2 (eq 9):** Premium formula verified by subtraction. Parts (i)-(iii) verified: monotonicity in $\lambda$, decreasing in $s$, and bounds at $\lambda \in \{0,1\}$ all correct.
- **Proposition 3 (eq 10):** Extinction state contributes zero to Euler equation since $D_{t+1}/D_t = 0$. Survival probability $(1-\delta)$ correctly scales the singularity contribution. Premium linear in $(1-\delta)$ verified.
- **Calibration claim (18% consumption drop):** $J = 0.82$, confirmed.

## Condition 4: Interpretations
All key verbal claims are supported by the formal theory:
1. "AI stocks command a valuation premium increasing in singularity probability" — Proposition 2(i).
2. "Premium decreasing in AI share" — Proposition 2(ii).
3. "Incomplete markets essential; complete markets eliminate premium" — Section 3.3 argument: perfect hedging removes consumption disruption.
4. "Self-limiting mechanism" — follows from Proposition 2(ii).
5. "AI stocks cannot hedge extinction" — Proposition 3: zero dividends in extinction state.
6. "Infinite output resolves incomplete markets" — qualitative but consistent: if $J \to 1$, premium vanishes.
7. "Intermediate regime maximizes premium" — follows from extinction reducing premium and infinite output completing markets.
8. "Elevated valuations are the price of insurance" — equilibrium outcome of hedging demand, not mispricing.

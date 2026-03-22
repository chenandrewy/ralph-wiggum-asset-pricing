# tests/theory-correctness.py
Started: 2026-03-22 12:42:26 EDT
Runtime: 4m 51s
[ralph-garage/agent-logs/20260322T164226.512687Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T164226.512687Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All four conditions—notational consistency, consistent assumptions, logical derivations, and supported interpretations—are satisfied.

## 1. Notational Consistency
All mathematical objects are consistently defined and used throughout. Key notation groups (consumption/utility, dividends/income, growth rates, singularity parameters, market access, pricing, extensions) show no conflicts. Time-varying vs. constant-share notation ($s_t$ vs. $s$) is correctly distinguished. The asset-specific discount factor $a_t^A$ in the differential-growth section correctly reduces to $a$ in the baseline.

## 2. Consistent Assumptions
Seven core assumptions identified: CRRA preferences ($\gamma > 1$, $\beta \in (0,1)$), budget constraint, growth rates ($g^A \geq g^N > 0$, $g^L = g^N$), singularity parameters ($\lambda \in (0,1)$, $\theta > 0$, $\phi, \phi_L \in (0,1)$), finite valuations ($a < 1$), market access ($\alpha \in [0,1]$, $\psi > 0$), and extinction ($\delta \in [0,1)$). The finite-valuation condition $a < 1$ is automatically satisfied by the preference and growth assumptions. No contradictions found.

## 3. Logical Results
All six propositions and two corollaries verified by rederivation from assumptions:
- **Proposition 1:** Euler equation correctly solved; numerical verification at baseline ($v^A = 16.6$, $v^N = 12.8$) matches Table 1.
- **Proposition 2:** Premium formula, monotonicity in $\lambda$ and $s$, and bounds all verified.
- **Decomposition (eq 10):** Correct factoring of the premium into cash-flow and hedging components.
- **Corollary 1:** Follows by chain rule through $\tilde{s}(\alpha)$.
- **Corollary 2:** Welfare gain $\omega > 0$ verified through value-function algebra and the sign of $W$ under $\gamma > 1$.
- **Proposition 3:** First-order invariance of P/D ratios to business-cycle shocks confirmed; return decomposition by independence verified.
- **Proposition 4:** Extinction scaling by $(1-\delta)$ verified; numerical check at $\delta = 0.10$ matches Table 4.
- **Proposition 5:** Four sub-state decomposition sums correctly to eq (14).
- **Proposition 6:** Hump-shape asymptotics ($\theta \to \infty$) and zero-crossing threshold verified.

## 4. Interpretations
All key verbal economic claims are supported by formal results. The hedging premium's dependence on $\lambda$, $s$, $\alpha$, and $\gamma$ is grounded in Propositions 1-2 and Corollaries 1-2. The decomposition into cash-flow and hedging components is formally derived. Claims about non-AI valuations rising ($J^{-\gamma}(1-\phi) > 1$), lower expected returns for AI stocks (positive SDF-return covariance), and the self-limiting mechanism (rising $s_t$ erodes $J^{-\gamma}$) are all traceable to the model. Calibration claims (13-23% hedging share, $J \approx 0.81$, welfare gain up to 3.4%) are numerically verified against the formulas. Extension claims about extinction, heterogeneous beliefs, and the hump-shaped hedging amplification are supported by Propositions 4-6.

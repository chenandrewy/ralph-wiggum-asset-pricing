# tests/theory-correctness.py
Started: 2026-03-22 12:52:27 EDT
Runtime: 4m 58s
[ralph-garage/agent-logs/20260322T165227.113580Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T165227.113580Z_theory-correctness_claude_opus.log)

# theory-correctness
VERDICT: PASS
REASON: All mathematical notation is consistent, assumptions are mutually compatible, all results follow logically from the assumptions with correct numerical calibrations, and all verbal economic claims are supported by the formal theory.

## 1. Notational Consistency

All mathematical objects grouped by concept:

- **Consumption/Utility:** $c_t$ (consumption), $\gamma$ (risk aversion, $\gamma > 1$), $\beta$ (discount factor)
- **Dividends/Income:** $D_t^A$ (AI dividends), $D_t^N$ (non-AI dividends), $L_t$ (labor income), $s_t \equiv D_t^A/c_t$, $\ell_t \equiv L_t/c_t$
- **Growth:** $g^A$, $g^N$, $g^L = g^N$, $g$ (common rate when $g^A = g^N$), $G(s_t)$ (aggregate growth factor)
- **Singularity:** $\lambda$ (probability), $\theta$ (AI jump), $\phi$ (non-AI drop), $\phi_L$ (labor drop), $J$ (consumption jump factor)
- **Market access:** $\alpha$ (access parameter), $\psi$ (private AI capital), $\tilde{s}(\alpha) = s + \alpha\psi$
- **Pricing:** $M_{t,t+1}$ (SDF), $a \equiv \beta(1+g)^{1-\gamma}$ (effective discount), $\bar{v}$ (benchmark P/D), $v^A$, $v^N$ (P/D ratios)
- **Extensions:** $\delta$, $\delta_H$, $\delta_O$ (extinction beliefs), $\pi$ (friction resolution), $Y_O$ (AI owner output), $q$, $\mu$, $\xi$, $d_0$, $\kappa$ (screening game), $\sigma$, $\epsilon$, $b^A$, $b^N$ (business cycle), $\eta$ (insider pricing share)

Each symbol is used consistently throughout. The simplification $J(s_t, \ell_t) \to J(s)$ under equal growth rates is correctly justified by the constant ratio $\ell_t/(1-s_t)$. The transition from two-argument to one-argument $J$ when applying $\tilde{s}(\alpha)$ is consistent.

**Result: PASS**

## 2. Consistent Assumptions

All mathematical assumptions:
- $\gamma > 1$, $\beta \in (0,1)$
- $g^A \geq g^N > 0$, $g^L = g^N$
- $\lambda \in (0,1)$
- $\theta > 0$, $\phi \in (0,1)$, $\phi_L \in (0,1)$
- $a \equiv \beta(1+g)^{1-\gamma} < 1$ (finite valuations)
- $\alpha \in [0,1]$, $\psi > 0$
- $\delta \in [0,1)$

These are all independent parameter restrictions on distinct objects. No pair of assumptions contradicts another. The finite-valuation condition $a < 1$ is verified at the baseline calibration ($a = 0.96 \times 1.02^{-2} \approx 0.923$). The negative-singularity condition $J < 1$ is verified at baseline ($J \approx 0.805$) and is consistent with the parameter ranges.

**Result: PASS**

## 3. Logical Results

### Proposition 1 (Equilibrium Valuations)
Verified the Euler equation derivation step by step. The Euler equation $v^A = (1-\lambda)a(1+v^A) + \lambda a J^{-\gamma}(1+\theta)(1+\bar{v})$ solves to give eq (6). Substituting $1+\bar{v} = 1/(1-a)$ and collecting terms yields the stated formula. The derivation for $v^N$ is identical with $(1-\phi)$ replacing $(1+\theta)$. **Verified.**

### Proposition 2 (Hedging Premium)
- Eq (8) follows by subtraction: $J^{-\gamma}[(1+\theta)-(1-\phi)] = J^{-\gamma}(\theta+\phi)$. **Verified.**
- Part (i): $f(\lambda) = \lambda/(1-a+\lambda a)$ has derivative $(1-a)/(1-a+\lambda a)^2 > 0$. **Verified.**
- Part (ii): $\partial J/\partial s = \theta + \phi > 0$; since $J < 1$ and $\gamma > 1$, $J^{-\gamma}$ is decreasing in $J$. **Verified.**
- Part (iii): At $\lambda=0$, ratio = 1. At $\lambda=1$, $v^A/v^N = (1+\theta)/(1-\phi)$. The ratio is monotonically increasing in $\lambda$ (verified via calculus on $(\bar{v}+fA)/(\bar{v}+fB)$). **Verified.**

### Decomposition (eq 9)
Factoring $J^{-\gamma}$ out of the premium is algebraically immediate. The risk-neutral limit ($\gamma \to 0 \Rightarrow J^{-\gamma} \to 1$) is correct. **Verified.**

### Corollary 1 (Partial Market Access)
$\tilde{s}(\alpha)$ increasing in $\alpha$, premium decreasing in effective share by Prop 2(ii). **Verified.**

### Corollary 2 (Welfare)
Derived the value function $V(c) = [c^{1-\gamma}/(1-\gamma)] \cdot W(\tilde{s})$ where $W(\tilde{s}) = [1-a+\lambda a J(\tilde{s})^{1-\gamma}]/[(1-a)(1-(1-\lambda)a)]$. Since $J$ is increasing in $\tilde{s}$ and $1-\gamma < 0$, $J^{1-\gamma}$ is decreasing, so $W(\tilde{s}) < W(s)$ for $\tilde{s} > s$. The consumption-equivalent formula follows from $(1+\omega)^{1-\gamma} W(s) = W(\tilde{s})$, giving $\omega > 0$. **Verified.**

### Proposition 3 (Business-Cycle Augmentation)
The separation of business-cycle and singularity contributions to the SDF covariance is correct by independence. The $O(\sigma^2)$ correction to P/D ratios follows from $E[\epsilon] = 0$. **Verified.**

### Proposition 4 (Extinction)
Extinction state contributes zero to the Euler equation (zero dividends and prices). The survival probability $(1-\delta)$ scales the singularity contribution linearly. **Verified.**

### Proposition 5 (Disagreement)
Verified: four sub-states (no singularity, extinction, friction-preserved survival, friction-resolved survival). In the friction-resolved state, $J=1$ so $M = \beta(1+g)^{-\gamma}$ but dividends still jump asymmetrically. The premium formula (eq 13) correctly aggregates contributions. **Verified.**

### Proposition 6 (Hump Shape)
Part (i): As $\theta \to \infty$, $J \approx s\theta$, so $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta^{1-\gamma} \to 0$ (since $\gamma > 1$), and $(1-\pi) \to 0$ by super-linear growth. Hence $\Delta^{\text{hedge}} \to 0$. The proof sketch's claim that the term scales as $\sim \theta$ is imprecise (it actually decays as $\theta^{1-\gamma}$), but the conclusion is correct since $(1-\pi)$ vanishes faster.
Part (ii): $J$ crosses 1 at $\theta = [(1-s-\ell)\phi + \ell\phi_L]/s$, correctly identified. **Verified.**

### Numerical Calibration Checks
- $\bar{v} = 0.923/0.077 = 11.97$ (paper: 11.9) ✓
- $J = 0.05(1.5) + 0.30(0.70) + 0.65(0.80) = 0.805$ (paper: ≈0.81) ✓
- $J^{-3} = 1/0.805^3 \approx 1.917$ (paper: ≈1.92) ✓
- $v^A$ at $\lambda=0.02$: 16.68 (paper: 16.6) ✓
- $v^N$ at $\lambda=0.02$: 12.83 (paper: 12.8) ✓
- Premium: 3.85 (paper: 3.8) ✓
- Ratio: 1.30 ✓
- Hedging share at $g^A=g^N$, $\lambda=0.02$: computed as $(v^A/v^N - v^A_{CF}/v^N_{CF})/(v^A/v^N - 1) \approx 40\%$, matching Table 2 ✓

**Result: PASS**

## 4. Interpretations

Key verbal claims and their formal support:

| Claim | Support |
|-------|---------|
| Hedging demand contributes to AI valuations | Hedging amplifier $J^{-\gamma} > 1$ in Prop 1 |
| Premium increases with singularity probability | Prop 2(i) |
| Premium decreases with AI share | Prop 2(ii) |
| Incomplete markets are essential for hedging channel | Cor 1: $\alpha \to 1 \Rightarrow J \to 1 \Rightarrow$ amplifier collapses |
| Hedging demand "roughly doubles" cash-flow premium | $J^{-\gamma} \approx 1.92$ at baseline |
| Non-AI valuations also rise with singularity risk | $J^{-\gamma}(1-\phi) \approx 1.34 > 1$ |
| AI stocks earn lower expected returns (baseline) | Positive $\text{Cov}(M, R^A - R^N)$ from eq (11) |
| Self-limiting mechanism as $s_t$ rises | Prop 2(ii): premium decreasing in $s$ |
| Welfare unambiguously improves with market access | Cor 2: $\omega > 0$ |
| Hedging channel contributes 13–23% with differential growth | Table 2 values, verified via risk-neutral counterfactual |
| AI stocks cannot hedge extinction | Zero-dividend, zero-price extinction state |
| Pessimistic AI owners may loosen friction | $\pi$ increasing in $\delta_O$ in Prop 5 |
| Hedging component is hump-shaped in $\theta$ | Prop 6 |
| Business-cycle risk reconciles hedging channel with high betas | Prop 3: positive cyclical premium coexists with hedging discount |
| Event study evidence is "suggestive, not dispositive" | Appropriately hedged; paper identifies confound (growth-news channel) |

All key theoretical claims are supported by the formal model. The paper is appropriately cautious about empirical claims (event study).

**Result: PASS**

## Minor Notes (non-failing)

- **Proof of Prop 6(i):** The proof claims $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta$ for large $\theta$. This is imprecise; the expression actually scales as $\theta^{1-\gamma} \to 0$ since $J \approx s\theta$. The conclusion ($\Delta^{\text{hedge}} \to 0$) remains correct because $(1-\pi) \to 0$ as well, making the product vanish. This is a proof-presentation issue, not a logical error.

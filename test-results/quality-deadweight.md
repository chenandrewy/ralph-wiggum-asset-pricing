# tests/quality-deadweight.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260404T232545.929532-0400_quality-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.929532-0400_quality-deadweight_claude_opus.log)

# quality-deadweight
VERDICT: PASS
REASON: Every formal object in the paper does meaningful economic or narrative work; no deadweight formalism found.

## Audit methodology

Catalogued every formal object (equations, definitions, propositions, corollaries), every parameter/variable, and every prose mechanism. Checked each against two criteria: (1) Is it used in at least one result, calibration, figure, or interpretation? (2) Does it advance the paper's economic argument or could it be replaced by plain English without loss?

## Parameters and variables

| Symbol | Introduced | Used in results? | Verdict |
|--------|-----------|-------------------|---------|
| $\beta, \gamma$ | Eq (1) | $R$, all P/D formulas | Active |
| $C_t$ | Eq (1) | Euler equation, proofs | Active |
| $g$ | Eq (2) | $R$, all P/D formulas, table, figure | Active |
| $Y_0$ | Eq (2) | Not directly in any result | Standard normalization; trivial |
| $\alpha, \alpha_S$ | Model setup | $H^A, H^N$, spread, table, figure | Active |
| $p$ | Singularity setup | $V_0$, spread, table, figure | Active |
| $G$ | Singularity setup | $\Lambda$, transfers extension, veto | Active |
| $\phi$ | Singularity setup | $\Lambda$, amplification (Prop 2), table | Active |
| $\Lambda$ | Eq (4) | Central to all results | Active |
| $R, V_0, V_\infty$ | Eq (6) | P/D formulas, spread, figure | Active |
| $H^A, H^N$ | Eq (7) | P/D formulas, spread, extinction | Active |
| $\tau, \delta$ | Extension 1 | $\Lambda(\tau,\delta)$, figure | Active |
| $\kappa$ | Extension 2 | Prop 3 (veto threshold) | Active |
| $q$ | Extension 3 | Prop 4 (extinction spread) | Active |
| $Y_t^{pub}$ | Dividend defs | Bridges output to dividends | Standard modeling notation |
| $D_t^A, D_t^N, P_t^A, P_t^N$ | Model setup | Euler equation, P/D ratios | Active |

$Y_0$ is the only symbol not used in any result, but it appears solely as the standard normalization constant in $Y_t = Y_0(1+g)^t$. Removing it would require removing the output equation entirely, which would hurt the exposition. This is not deadweight.

## Equations (13 numbered)

All 13 numbered equations are load-bearing:
- Eqs (1)–(5): Define the model primitives (utility, output, consumption jump, $\Lambda$, Euler equation). Each feeds into the proof of Proposition 1.
- Eqs (6)–(8): State the main P/D result. Core of the paper.
- Eq (9): Closed-form spread. Core result.
- Eq (10): Amplification ratio. Quantifies the role of incomplete markets (Prop 2).
- Eq (11): $\Lambda(\tau,\delta)$. Needed for the transfers figure and discussion.
- Eqs (12)–(13): Extinction-adjusted P/D and spread. Needed for Proposition 4.

No equation is introduced and abandoned. No equation restates something already established.

## Theorem environments (1 Definition, 4 Propositions, 1 Corollary)

- **Definition 1 (Equilibrium):** Anchors the Euler equation used in all proofs. Standard for theory papers. Concise (two conditions: Euler equation + market clearing). Not ceremonial.
- **Proposition 1 (P/D ratios):** Main result. Used in table, figure, all extensions.
- **Corollary 1 (Hedging premium):** Closed-form spread. Core economic claim.
- **Proposition 2 (Incomplete markets amplify):** Quantifies the central friction. Used in interpretation.
- **Proposition 3 (Veto):** Connects incomplete markets to deployment. Ties back to Extension 1.
- **Proposition 4 (Extinction):** Shows extinction dilutes the premium. Introduces a tension for interpretation.

Each environment states a result that is interpreted in the prose and contributes to the paper's argument. No proposition is purely technical filler.

## Prose mechanisms

- The four-item singularity specification (lines 95–100) efficiently parameterizes the event; every item is used.
- The incomplete markets paragraph (lines 125–126) establishes the key friction and cites GKP. Essential.
- Quantitative parameterization (Section 3.3) is explicitly illustrative, not a calibration exercise. Consistent with the spec.

## Potential concerns considered and dismissed

1. **Equation (2)** ($Y_t = Y_0(1+g)^t$): Could be stated in prose ("output grows at rate $g$"), but the display equation sets up notation used in the dividend definitions and is standard in theory papers. One line; not deadweight.
2. **$Y_t^{pub}$ notation**: Appears only in the dividend definitions. It serves the important role of distinguishing publicly traded output from total output—the distinction at the heart of the incomplete-markets friction. Not dispensable.
3. **Definition environment for equilibrium**: Wrapping the Euler equation in a formal Definition is standard in finance theory. It is concise (three lines) and the Euler equation it anchors is used in every proof.

## Conclusion

The paper's formalism is lean and purposeful. Every parameter is used in at least one result. Every equation feeds into a proposition, corollary, table, or figure. Every proposition advances the economic argument. No auxiliary detours, no ceremonial formalism, no abandoned notation.

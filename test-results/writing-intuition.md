# tests/writing-intuition.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 1m 19s
[ralph-garage/agent-logs/20260411T211526.534520-0400_writing-intuition_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.534520-0400_writing-intuition_claude_opus.log)

# writing-intuition
VERDICT: PASS
REASON: All propositions and key formulas have their intuition explained in terms of the mathematical objects they use.

## Detailed Findings

### Proposition 1 (Price-dividend ratios, line 128)

The discussion following the proposition (lines 156--158) explains the economic content directly through the mathematical objects:

- **$\Gamma^{AI}$ vs $\Gamma^{N}$**: "Since $\Delta\theta > 0$, AI stocks' dividends grow faster than aggregate consumption upon a singularity ($\Gamma^{AI} > 1+\eta$), while non-AI stocks' dividends grow more slowly ($\Gamma^{N} < 1+\eta$)."
- **$\phi^{-\gamma}$**: "Combined with the household's high marginal utility in singularity states (due to displacement, $\phi(1+\eta) < 1$ when $\phi$ is sufficiently small), AI stocks' payoffs are especially valuable."
- **Comparative statics on $\phi$ and $p$**: "the valuation spread widens with displacement severity (decreasing $\phi$, which raises marginal utility in singularity states via $\phi^{-\gamma}$) and with singularity probability $p$."

The existence condition (Remark 1, lines 146--152) is also explained via $A^j$: "the SDF-weighted expected dividend growth exceeds the discount rate and the geometric pricing sum diverges."

### Proposition 2 (Extinction attenuation, line 160)

The proposition statement itself gives the intuition in terms of the math: "higher extinction probability reduces the weight on non-extinction states where the valuation divergence occurs." The proof (lines 164--166) walks through the mechanism explicitly:

- Decomposes $A^j$ into components $B$, $S$, $\Gamma^j$.
- Explains how $(1-\xi)$ scales the singularity component and why $\Gamma^{AI} > \Gamma^{N}$ makes the absolute reduction larger for AI stocks.
- Uses convexity of $f(A) = A/(1-A)$ to complete the argument.

### Proposition 3 (Veto under incomplete markets, line 212)

The proof (lines 220--229) explains the intuition through the formula $\Delta u(\gamma)$:

- "As $\gamma \to \infty$, the negative-singularity term dominates because $\phi\alpha(1+\eta) < \alpha$ when $\phi(1+\eta) < 1$: the utility cost of the consumption drop grows without bound relative to the utility gain."
- Complete-markets case is explained via the consumption level $\alpha(1+\eta)C_t(1+g)$.

The subsequent discussion (lines 231--235) also ties back to parameters: veto cost $\kappa$, positive singularity probability $q$, and specific calibration values.

### Key Formulas in Extensions

- **Eq. (6), transfer consumption (line 246)**: Each term is explained -- "The first term is the household's displaced consumption. The second is the net transfer: a fraction $\tau$ of the AI surplus, reduced by the deadweight cost $\delta\tau$."
- **Eq. (7), $\phi_\text{eff}$ (line 254)**: Derived explicitly from Eq. (6) and connected to the SDF: "Since $\phi_\text{eff}$ enters the SDF in the same way as $\phi$, the P/D formula from Proposition 1 applies with $\phi$ replaced by $\phi_\text{eff}$."
- **Eq. (8), transfer ratio (line 262)**: Explained as independent of $\eta$, with intuition tied to levels: "as $\eta$ grows, both $c^H_{post}$ and $c^H_{no\text{-}transfer}$ grow without bound, so even inefficient transfers deliver arbitrarily large consumption gains."
- **Infinite P/D at $\tau = 0$ under large singularity (line 269)**: Connected to the existence condition via $\phi^{-\gamma}$: "the household's marginal utility in the singularity state ($\phi^{-\gamma} = 160{,}000$) is so extreme that the pricing sum diverges."

### Summary

Every proposition and key formula in the paper is accompanied by intuitive discussion that references the specific mathematical objects ($\Gamma^{AI}$, $\Gamma^{N}$, $\phi^{-\gamma}$, $A^j$, $(1-\xi)$, $\Delta u(\gamma)$, $\phi_\text{eff}$, $\tau$, $\eta$, $\delta$) from the respective expressions. The paper consistently grounds economic intuition in the formalism rather than relying on purely verbal arguments.

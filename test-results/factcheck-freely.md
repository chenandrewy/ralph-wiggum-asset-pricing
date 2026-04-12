# tests/factcheck-freely.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 6m 56s
[ralph-garage/agent-logs/20260412T095842.936206-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T095842.936206-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: PASS
REASON: No factually incorrect statements or logical inconsistencies found after thorough review of mathematics, numerical claims, citations, and internal logic.

## What Was Verified

### Mathematical Derivations
- **Proposition 1 (P/D ratios):** Euler equation derivation in Appendix A is correct. Closed-form P/D formula $v = A/(1-A)$ follows from the standard geometric sum. Backward recursion for exact P/D ratios correctly handles singularity vs. no-singularity continuations.
- **Key identity:** $\Gamma^N = (1-\Delta\theta)(1+\eta)$ is theta-independent, confirming the paper's claim that the non-AI closed form is exact while the AI closed form is an approximation.
- **Proposition 2 (Extinction attenuation):** Semi-elasticity $f'(A)/f(A) = 1/[A(1-A)]$ is increasing in $A$ for $A > 1/2$. All parameterizations satisfy $A^j > 1/2$.
- **Proposition 3 (Veto):** Limit argument as $\gamma \to \infty$ is correct. The negative-singularity term dominates because $\phi\alpha(1+\eta) < \alpha$ when $\phi(1+\eta) < 1$, and $|u(\phi\alpha(1+\eta))|$ grows faster than $|u(\alpha)|$.

### Numerical Claims
All numerical claims in the text match the code output:
- At $p=0.5\%$, $\xi=0$: AI P/D ≈ 15.5, non-AI P/D ≈ 11, ratio ≈ 1.4. **Correct.**
- At $p=1\%$: P/D ratio for AI stocks roughly doubles relative to non-AI. Exact ratio at $\xi=0$ is 2.00. **Correct.**
- $\phi(1+\eta) = 0.75$, so household consumption falls by 25%. **Correct.**
- $\phi^{-\gamma} = 0.05^{-4} = 160{,}000$. **Correct.**
- Net transfer per dollar taxed at $\tau=0.30$, $\delta=0.9$: $0.30 \times (1-0.27) = 0.219$. **Correct.**
- Consumption multiple of $3.5\times$ at $\tau=0.30$ under large singularity with $\delta=0.9$. **Correct.**
- "50% consumption loss" without transfers: $\phi(1+\eta) = 0.05 \times 10 = 0.5$. **Correct.**

### Citation Accuracy
- **GKP (2012):** Accurately characterized as modeling displacement risk from innovation under incomplete markets.
- **Jones (2024):** Growth-vs-existential-risk tradeoff correctly described. CRRA utility $\gamma \geq 2$ conservatism claim is accurate.
- Bibliographic details checked and correct.

### Internal Consistency
- Distinction between $\alpha$ (consumption share) and $\theta$ (AI dividend share) maintained consistently.
- Transfer equation correctly uses $\alpha$ as the tax base; $\phi_{eff}$ correctly substitutes into the P/D formula.
- Extinction normalization ($U_{ext} = 0$) is indeed conservative for the veto result, as claimed.
- Complete-markets result verified: with $\phi_{eff} = 1$, displacement premium largely vanishes.

## Minor Observations (Not Errors)
1. "P/D ratios roughly double" at $p=1\%$ is accurate across reasonable extinction probabilities ($\xi$), though exact ratio varies from 2.00 to 1.92.
2. "250% gain" language (from 0.5x to 3.5x consumption) is slightly ambiguous but defensible as a 250% gain relative to pre-singularity baseline.

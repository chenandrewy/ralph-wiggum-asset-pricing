# tests/theory-correctness.py
Started: 2026-03-22 09:30:27 EDT
Runtime: 6m 16s
[ralph-garage/agent-logs/20260322T133027.199091Z_theory-correctness_claude_opus.log](../ralph-garage/agent-logs/20260322T133027.199091Z_theory-correctness_claude_opus.log)

# theory-correctness

VERDICT: FAIL

REASON: Proposition 4 (eq 17) is mathematically incorrect — the friction-resolves state contributes a positive term to the AI premium that the proof omits — and this error propagates to Proposition 5 and several verbal claims.

---

## Condition 1: Notational Consistency — PASS

All mathematical objects are used consistently throughout the paper. Notation is well-defined upon first use and does not shift meaning across sections. No issues found.

## Condition 2: Consistent Assumptions — PASS

All parameter restrictions ($\gamma>1$, $\beta\in(0,1)$, $g>0$, $\theta>0$, $\phi\in(0,1)$, $\lambda\in(0,1)$, $a<1$, etc.) are mutually consistent. The constraint $a<1$ follows from the other assumptions. The constant pre-singularity share $s$ is verified by the dividend dynamics. No contradictions found.

## Condition 3: Logical Results — FAIL

**Propositions 1–3 and Corollary 1: Correct.** All derivations were verified algebraically. Calibration numbers in Tables 1–3 were spot-checked and match the formulas.

**Proposition 4 (eq 17): Incorrect.** The Euler equation for the AI stock in the Proposition 4 model has four states. In state 4 (singularity occurs, humanity survives, friction resolves), the paper assumes consumption neutrality ($J=1$) and correctly sets the SDF to $\beta(1+g)^{-\gamma}$. However, the AI stock's dividend growth in this state is still $(1+g)(1+\theta)$ while the non-AI stock's is $(1+g)(1-\phi)$. The proof claims this state "contributes no hedging premium," but the contribution to $v^A - v^N$ from this state is:

$$\lambda(1-\delta_H)\pi \cdot a(\theta+\phi)/(1-a) > 0$$

The correct premium formula is:

$$v^A - v^N = \frac{\lambda(1-\delta_H)\,a\,(\theta+\phi)\,\bigl[(1-\pi)J^{-\gamma} + \pi\bigr]}{(1-a)\bigl[1-(1-\lambda)a\bigr]}$$

The paper's eq (17) is missing the $+\pi$ term. The error conflates consumption neutrality with return neutrality: even when the household's consumption is unaffected (complete markets), the AI stock's dividends still jump more than non-AI, generating a positive P/D difference.

**Proposition 5 (Hump-Shaped Premium): Incorrect (inherited).** The proposition claims the premium vanishes as $\theta \to \infty$ (via $\pi \to 1$). With the corrected formula, as $\pi \to 1$ the premium approaches $\lambda(1-\delta_H)\,a\,(\theta+\phi)/[(1-a)(1-(1-\lambda)a)]$, which diverges with $\theta$. The hump-shaped result does not hold.

## Condition 4: Interpretations — FAIL

**Unsupported claim — "the AI valuation premium would vanish" with complete markets (Section 2.3, Introduction).** Setting $J=1$ in the baseline premium formula (eq 12) gives $v^A - v^N = \lambda a(\theta+\phi)/[(1-a)(1-(1-\lambda)a)] > 0$. Complete markets eliminate the marginal-utility amplification ($J^{-\gamma} \to 1$) but not the dividend growth differential. The premium shrinks but does not vanish.

**Unsupported claim — hump-shaped premium (Section 4.3).** Based on the incorrect Proposition 5.

**Unsupported claim — "the same event that generates hedging demand may also eliminate the need for it" (Section 4.3).** With the corrected formula, friction resolution reduces the premium but cannot eliminate it entirely.

All other key verbal claims (premium increasing in $\lambda$, decreasing in $s$, decreasing in $\alpha$, linearly decreasing in $\delta$, self-limiting mechanism) are correctly supported by the formal theory.

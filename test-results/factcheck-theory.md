# tests/factcheck-theory.py
Started: 2026-04-02 18:07:23 EDT
Runtime: 3m 3s
[ralph-garage/agent-logs/20260402T180723.893500-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T180723.893500-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: FAIL

REASON: The displacement ratio $\Delta$ is silently redefined between the main model and the extension, creating a notational ambiguity.

## Requirement 1: Notational Consistency — FAIL

A systematic audit of all 19 symbol families in the paper identified one substantive notational collision and two minor style issues.

### Issue 1 (Moderate): $\Delta$ symbol collision between Eq. (5) and Eq. (11)

In Sections 2--3, the displacement ratio is defined as:

$$\Delta \equiv \tilde{\omega}/\omega < 1 \quad \text{(Eq. 5)}$$

This is a fixed constant — the ratio of post- to pre-singularity household output shares.

In Section 4.2 (Eq. 11), the paper introduces:

$$\Delta(\lambda) = 1 - (1 - \Delta_0)(1 - \lambda)$$

where $\Delta_0 = \tilde{\omega}/\omega$ — the same object that was called $\Delta$ in Eq. (5). The prose then uses the unadorned symbol $\Delta$ as shorthand for $\Delta(\lambda)$:

> "At $\lambda = 0$, no risk-sharing occurs and $\Delta = \Delta_0$. At $\lambda = 1$, transfers fully offset displacement and $\Delta = 1$."

The symbol $\Delta$ has silently shifted meaning: from the fixed ratio $\tilde{\omega}/\omega$ (Sections 2--3) to the effective displacement ratio $\Delta(\lambda)$ (Section 4.2), while $\Delta_0$ takes over the original definition. No bridging statement connects the two usages (e.g., "we now generalize $\Delta$ to depend on $\lambda$, with the earlier definition corresponding to $\lambda = 0$").

A reader tracking $\Delta$ from the main model into the extension encounters an unexplained referent shift.

### Issue 2 (Minor): $A(p)$ collision with superscript $A$

In the proof of Proposition 3 (Appendix A), the numerator function is called $A(p)$. Throughout the paper, superscript $A$ denotes "AI stocks." These are syntactically distinct (function vs. superscript), but the overlap could cause momentary confusion.

### Issue 3 (Minor/Style): $R$ as pricing kernel

$R \equiv \beta(1+g)^{1-\gamma}$ is labeled "the normal-state pricing kernel," but $R$ conventionally denotes a gross return in asset pricing. No internal collision exists, but the choice is unconventional.

### Clean notation

The remaining 16 symbol families are clean and internally consistent. The tilde convention (post-singularity marker) is used uniformly. All symbols are defined before or at first use.

## Requirements 2--3: Not evaluated

Per procedure, Requirements 2 (mutual consistency of assumptions) and 3 (traceability of objects to assumptions) were not evaluated because Requirement 1 failed.

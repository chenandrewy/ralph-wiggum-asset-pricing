# tests/factcheck-freely.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 9m 35s
[ralph-garage/agent-logs/20260404T234508.978535-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260404T234508.978535-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The paper misdescribes $V_0$ as the "no singularity risk" benchmark in two places, when that role belongs to $V_\infty$.

## Issue 1 (Factual error): Misdescription of $V_0$

**Locations:** Line 180 (main text interpretation of Proposition 2) and line 261 (Figure 2 caption).

- Line 180: "$V_0$, the P/D ratio in a world where the singularity never occurs"
- Line 261: "$V_0$ marks the P/D ratio with no singularity risk; $V_\infty$ marks the no-singularity-risk benchmark."

**Problem:** Both $V_0$ and $V_\infty$ are described as relating to "no singularity risk," which is contradictory. By the paper's own definitions:

- $V_0 = (1-p)R / (1-(1-p)R)$ — this depends on $p$ and equals the P/D of an asset with zero hedge factor ($H^i = 0$), i.e., an asset that provides no payoff in the singularity state.
- $V_\infty = R/(1-R)$ — this is the standard Gordon growth P/D, which is indeed the P/D with no singularity risk (i.e., $p = 0$ gives $V_0 = V_\infty$).

$V_0$ should be described as "the P/D ratio of an asset with zero hedge factor" or "the P/D reflecting only the no-singularity path." Calling it the P/D "in a world where the singularity never occurs" is incorrect — that world has $p = 0$, yielding $V_\infty$.

## Minor issue: Proof gap in Proposition 5(b)

The proof of part (b) compares single-period flow utilities to establish the veto threshold $\bar{\kappa}$. However, this is an infinite-horizon problem where vetoing vs. not vetoing yields different continuation values (under no-veto, the household may transition to the post-singularity regime). The proof does not explicitly justify why the per-period flow comparison extends to the lifetime comparison. The result is correct (due to CRRA homogeneity and the fact that the singularity is bad for the household when $\Lambda < 1$), but the proof as written is incomplete.

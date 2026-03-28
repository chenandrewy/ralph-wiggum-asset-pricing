# dev/qf/qf-subparts.py
Started: 2026-03-28 14:44:57 EDT
Runtime: 1m 44s
[ralph-garage/agent-logs/20260328T144457.270967-0400_qf-subparts_claude_opus.log](../../ralph-garage/agent-logs/20260328T144457.270967-0400_qf-subparts_claude_opus.log)

# qf-subparts
VERDICT: FAIL
REASON: Multiple formal subparts are compressible — the paper uses only their qualitative takeaways, and displayed algebra could be replaced with plain English without weakening downstream claims.

## Findings

### 1. Proposition 1(iii): displayed sufficient condition for risk aversion (strongest case)

The enumerated part claims the P/D ratio is increasing in gamma "provided" a specific displayed inequality holds:

> $p \, e^{\gamma\Delta + a}(\Delta - \mu + (\gamma-1)\sigma^2) > (1-p)(\mu - (\gamma-1)\sigma^2)$

The paper never uses this condition again. The calibration tables (Tables 1--2) do not vary gamma. The prose reduces this to "when the singularity channel dominates" — which is all the paper needs. The displayed inequality is compressible: the paper could state part (iii) as "increasing in gamma when the singularity contribution is sufficiently large" without the formula, and no later argument would lose precision.

### 2. Equation (7): linearized sufficient condition for a negative singularity

The first-order condition $d/a > \phi s / (1-s)$ appears once and is used only for the immediately following sentence ("when most AI capital is private, this condition is easily satisfied"). All quantitative work uses the exact Delta formula (eq 6). This linearization does no work that the sentence couldn't do alone.

### 3. Proposition 3(ii): "the reduction is proportional to pq"

This is trivially visible from comparing equations (8) and (14): the only difference is the factor $(1-q)$ applied to the singularity term. Stating this as a separately enumerated subpart of a proposition adds formal weight to an observation that is immediate from inspection. It could be absorbed into the prose following Proposition 3 without any loss.

### 4. Corollary 2: two-type marginal investors

The formal statement and proof compose two already-established monotonicities: $\partial\Delta/\partial\phi < 0$ (proven in Corollary 1's proof) and $\partial\pi/\partial\Delta > 0$ (Proposition 1(ii)). The corollary's content is: "investors with less private-market access face higher displacement and therefore value the hedge more." This follows in one sentence from the existing results. The surrounding discussion of VSL heterogeneity and the GKP distinction does real economic work — but the formal corollary + proof structure is compressible, since it restates and re-proves facts already established.

### 5. Logistic transition function (eq 17)

This is a "natural parametric example" offered after Corollary 3, which is proven for the entire class of transition functions satisfying conditions (i)--(iii). The logistic is never calibrated, never appears in a table, and is never referenced again. It is dead weight: the general result already covers it, and the economic interpretation ("AI owners list equity when surplus exceeds a fixed cost") could be stated without a displayed equation.

## Assessment against requirements

**Requirement 1 (no dead-weight subparts):** The logistic transition function (eq 17) is dead weight — the paper never references it after its statement, and Corollary 3 is proven without it. VIOLATED.

**Requirement 2 (no compressible subparts):** Prop 1(iii)'s displayed condition, eq (7), Prop 3(ii), and Corollary 2 are all compressible — the paper uses only their qualitative content. Four instances across three sections constitute a clear pattern. VIOLATED.

**Requirement 3 (formalism replaceable with plain English):** Prop 1(iii)'s condition, eq (7), and Prop 3(ii) could each be stated informally without weakening any economic claim the paper makes. VIOLATED.

## Notes

The larger objects containing these subparts (Propositions 1 and 3, the extension section, Corollary 3) are useful and do real economic work. The issue is local: specific enumerated clauses, displayed conditions, and named examples that add algebraic precision the paper does not exploit.

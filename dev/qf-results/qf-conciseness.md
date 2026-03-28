# dev/qf/qf-conciseness.py
Started: 2026-03-28 14:44:57 EDT
Runtime: 1m 46s
[ralph-garage/agent-logs/20260328T144457.280183-0400_qf-conciseness_claude_opus.log](../../ralph-garage/agent-logs/20260328T144457.280183-0400_qf-conciseness_claude_opus.log)

# qf-conciseness
VERDICT: FAIL
REASON: The paper contains a numbered equation (Eq 17, the logistic transition) and associated parameters that are never used in any derivation, proposition, calibration, or interpretation, plus redundant notation that is introduced and immediately abandoned.

## Methodology

Cataloged all 17 numbered equations and ~35 named mathematical objects. Traced each forward through every proposition, corollary, proof, calibration table, and interpretive passage.

## Violations

### 1. Equation (17): Logistic transition function (unnecessary formalism)

Equation (17) defines a parametric logistic form for $\phi(a)$. Corollary 3, which is the only result in this section, is proved using only the general conditions (i)-(iii) on $\phi(a)$---monotonicity, boundary values, and the limit. The logistic form is never invoked in the proof, never calibrated in any table, and never referenced by any later result. It introduces two new parameters ($\bar{a}$, $\lambda$) that appear nowhere else in the paper. The paragraph following Eq (17) offers a verbal economic interpretation ("AI owners list equity when the surplus exceeds a fixed cost") that conveys the same content without formalism. This is a textbook case of unnecessary formalism: a numbered equation that could be replaced with plain English without weakening any economic claim.

### 2. $Y_t^{pub}$ and $Y_t^{priv}$: redundant notation

Equation (3) introduces $Y_t^{pub}$ and $Y_t^{priv}$ as named components of AI output. After that equation, the paper never uses these symbols again---it writes $\phi Y_t^{AI}$ and $(1-\phi) Y_t^{AI}$ directly. These are intermediate labels that could be dropped entirely. The decomposition can be stated as "$\phi \in (0,1)$ is the publicly traded share of AI output" and the paper would lose nothing.

### 3. $f$: introduced and never used

Section 2.2 states: "the results extend to settings where the household holds a fraction $f \leq \phi$ of AI dividends." The variable $f$ is never defined in an equation, never appears in a proposition, and is never used again. This is unnecessary notation for a parenthetical remark that could read "...holds a smaller fraction of AI dividends."

## Objects that are borderline but pass

- **Equation (7)** (sufficient condition for negative singularity): This is a first-order approximation never reused in a later derivation. However, it provides a concise interpretive condition on the ratio $d/a$ that is difficult to convey verbally with equal precision. Borderline pass.
- **$\tilde{c}$, $\bar{u}$, $g$** (Jones-framework objects): These are local to Section 4.3 and exist to calibrate $\delta$, which feeds into $q$ in Table 2. The calibration is quantitatively material. Pass.
- **$w_j$, $\bar{\phi}$** (Remark 2): Local to a remark discussing GE bias on Corollary 1. The remark qualifies a formal result and the notation is needed to state the qualification precisely. Pass.

## Equations that are fully justified

Equations (1), (4), (6), (8), (9), (10) form the paper's analytical spine: utility $\to$ consumption $\to$ displacement $\to$ Euler equation $\to$ P/D ratio $\to$ pricing kernel. Every one feeds a later proposition or calibration table. Equations (11), (12), (13) extend to complete markets and extinction risk, used in Propositions 2-3 and Tables 1-2. Equation (14) calibrates extinction risk for Table 2. Equation (15) states Corollary 2's result. Equation (16) is used in Corollary 3's proof. Equations (2), (3), (5) set up the output structure that feeds the consumption equation.

## Summary

The primary violation is Equation (17), which is a decorative parametric example with two orphan parameters, never used in any result. The secondary violations ($Y_t^{pub}$, $Y_t^{priv}$, $f$) are redundant or vestigial notation. Together these violate requirements 1-4.

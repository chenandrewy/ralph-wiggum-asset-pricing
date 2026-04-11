# tests/theory-deadweight.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 2m 32s
[ralph-garage/agent-logs/20260411T103039.126871-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.126871-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: FAIL
REASON: Proposition 2 parts (i) and (ii) are ceremonial formalism whose qualitative content can be stated in plain English without weakening any economic claim.

## Audit methodology

Every formal object in the paper was checked against four criteria: (1) whether it is introduced and then abandoned or adds no meaningful economic or narrative work; (2) whether its qualitative takeaway can be stated in plain English without weakening the paper's claims; (3) whether all variables, parameters, and functions are used in a result, calibration, or interpretation that matters; (4) whether any formalism is pompous, ceremonial, or constitutes an auxiliary detour.

## Finding: Proposition 2(i) and (ii) are ceremonial

Proposition 2 (comparative statics) has three parts:

- **(i)** The valuation spread increases with displacement severity (decreasing in $\phi$).
- **(ii)** The spread increases with singularity probability $p$ when $\gamma$ is sufficiently large.
- **(iii)** The spread decreases with extinction probability $\xi$, with a convexity argument explaining why the *ratio* also narrows.

Parts (i) and (ii) follow immediately from inspecting the P/D formulas in Proposition 1. Their "proofs" restate what the formula already says:

- (i): "$\phi^{-\gamma}$ increases" when $\phi$ falls. This is visible by inspection.
- (ii): More weight on singularity states favors AI stocks because $\Gamma^{AI} > \Gamma^{N}$. Also visible by inspection.

These results can be stated as prose observations in a single sentence each (e.g., "It is immediate from the P/D expressions that the spread widens with displacement severity and with singularity probability for sufficiently risk-averse households") without any loss of rigor or economic content.

Supporting evidence: the quantitative analysis section (Section 3) discusses these patterns in prose ("Second, increasing the singularity probability raises the AI stock premium...") without citing Proposition 2(i) or (ii) by number. Only part (iii) is cited by proposition number ("as Proposition 2(iii) predicts"), confirming that (iii) is the only part earning its formal treatment. The convexity argument in (iii)---that $A/(1-A)$ is convex, so a proportional reduction in both $A^{AI}$ and $A^{N}$ hits the larger one harder---is genuinely non-obvious and benefits from a formal proof.

**Recommendation:** Demote (i) and (ii) to prose observations stated after Proposition 1, and either make Proposition 2 solely about the extinction-attenuation result or fold it into the discussion.

## All other formalism is clean

### Parameters and variables
Every parameter ($\beta, g, \gamma, p, \xi, \eta, \phi, \alpha, \theta, \Delta\theta, q, \kappa, \tau, \delta$) and every derived quantity ($\Gamma^{AI}, \Gamma^{N}, A^j, \phi_\text{eff}, \alpha^+$) appears in at least one proposition, calibration, or figure. No variable is introduced and abandoned.

### Proposition 1 (P/D ratios)
The main result. The closed-form P/D expressions are the core contribution, and $\Gamma^{AI}$ vs. $\Gamma^{N}$ does heavy economic work in the discussion of the hedging channel.

### Remark 1 (existence condition)
Introduces the condition $A^j < 1$ for finite prices. This is referenced three times: in the model discussion (the infinite-hedging-demand discontinuity), in Extension 2 (transfers restoring finite P/D when the condition is violated), and in the figure caption. It is load-bearing.

### Proposition 3 (veto)
The main result of Extension 1. Both parts do genuine economic work: (i) shows incomplete markets create a veto incentive, (ii) shows complete markets eliminate it. The proof uses the divergence of the negative-singularity utility cost as $\gamma \to \infty$, which is not obvious by inspection. The numerical example concretizes the result. No deadweight.

### Extension 2 equations
- Equation (8): transfer consumption formula. Defines the core mechanism. Used.
- Equation (9): $\phi_\text{eff}$. Connects transfers back to Proposition 1's P/D formula. Economically motivated and used.
- Equation (10): transfer ratio independence from $\eta$. The formula makes transparent *why* the ratio is $\eta$-independent (it cancels), which prose alone would not convey. Used in the discussion immediately following.

### Model setup (Eqs 1-3)
Aggregate consumption growth, displacement, and CRRA utility are foundational. All three are referenced throughout.

### Appendix A
The Euler equation derivation is required by the spec (all propositions must be proved). It is the appropriate length and location for this proof.

### Kaldor-Hicks efficiency definition
A prose definition with a simple formal condition ($(1+\eta) > 1$). Brief and functional.

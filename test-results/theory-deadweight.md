# tests/theory-deadweight.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260409T184838.267263-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.267263-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object—parameter, equation, proposition, and proof—contributes to a result, calibration, or economic argument; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without loss.

## Detailed Audit

### Parameters and Variables
All parameters ($\beta, g, \gamma, p, \xi, \eta, \phi, \theta, \Delta\theta, \lambda, \phi^+, \kappa, \tau, \delta_0$) appear in at least one displayed result (Propositions 1–3, the transfer formulas), in the calibration table, or in the extension figures. None is introduced and then unused.

### Displayed Equations
- **Eq (1)** (consumption growth): supplies the $(1+g)$ factor in the SDF and all pricing formulas.
- **Eq (2)** (displacement): defines $\phi$, which is central to every result.
- **Eq (3)** (CRRA utility): needed for the Euler equation derivation and the veto analysis.
- **Eqs (4)–(5)** (P/D ratios): the paper's main quantitative result, directly used in the calibration table.
- **Eqs (6)–(8)** (proof steps): standard derivation of the P/D formulas; required by the spec's proof policy.
- **Eq (9)** ($\Delta U^H$ veto gain): defines the key object in Proposition 3's veto condition.
- **Eq (10)** (transfer consumption): derives the transfer ratio and underlies the extension figure.
- **Eq (11)** (transfer ratio): delivers the key economic insight that the consumption gain is independent of $\eta$.

### Propositions and Corollary
- **Proposition 1** (P/D ratios): core result, drives the calibration table and all quantitative discussion.
- **Corollary 1** (valuation spread): states the main qualitative prediction ($P^{AI}/D^{AI} > P^N/D^N$).
- **Proposition 2** (comparative statics): all three parts (i)–(iii) are directly referenced in the quantitative analysis section.
- **Proposition 3** (veto): delivers the extension's headline result on market incompleteness distorting AI development.

### Notation
$\Gamma^{AI}$ and $\Gamma^N$ are compact notation for dividend growth factors. They appear in both propositions and the corollary, making the P/D formulas readable. Not ceremonial.

### Inline Expressions
The private AI capital dividend $(1-\alpha_t)C_t - D_t^{AI}$ is an inline clarification (not a displayed equation) explaining the source of market incompleteness. It is a single phrase serving a narrative role.

### Assessment
No formal object is introduced and abandoned. No parameter is unused. No proposition could be replaced by a plain-English statement without weakening the paper's quantitative claims (the calibration table and figure depend on the closed-form expressions). No auxiliary formal detour exists. The formalism is lean and purposeful throughout.

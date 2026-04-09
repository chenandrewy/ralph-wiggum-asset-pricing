# tests/theory-deadweight.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 2m 33s
[ralph-garage/agent-logs/20260409T193302.006220-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T193302.006220-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation contributes to the paper's economic claims or is used in subsequent analysis; no deadweight formalism found.

## Audit Methodology

Inventoried every formal object (propositions, corollary, remark, displayed equations, parameters, and functions) and traced each forward to check whether it appears in a result, calibration, interpretation, or narrative that matters for the paper's conclusions.

## Parameter Inventory (all used)

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $\beta, g, \gamma$ | Preferences (§2.1) | P/D formulas (Prop 1), calibration (§3), veto (Prop 3) |
| $\phi$ | Displacement (§2.1) | P/D formulas, Prop 2(i), transfers (§4.2), calibration |
| $\eta$ | Singularity growth (§2.1) | P/D formulas, $\Gamma$ factors, transfer ratio (eq 8), calibration |
| $p$ | Singularity probability (§2.1) | P/D formulas, Prop 2(ii), calibration |
| $\xi$ | Extinction probability (§2.1) | P/D formulas, Prop 2(iii), veto discussion, calibration |
| $\alpha_t$ | Household share (§2.1) | Consumption, displacement, transfers |
| $\theta, \Delta\theta$ | AI dividend share (§2.1) | $\Gamma^{AI}, \Gamma^{N}$, Corollary 1, calibration |
| $\lambda$ | Positive singularity prob (§4.1) | Prop 3, $\Delta U^H$ formula |
| $\phi^+$ | Positive displacement (§4.1) | Prop 3 |
| $\kappa$ | Veto cost (§4.1) | Prop 3 veto condition |
| $\tau$ | Tax rate (§4.2) | Transfer consumption (eq 7), transfer ratio (eq 8), figure |
| $\delta_0$ | Deadweight cost (§4.2) | Transfer consumption, transfer ratio, figure |

**No orphaned parameters.** Every parameter introduced appears in at least one result, equation, or calibration that directly supports the paper's conclusions.

## Formal Environments

### Proposition 1 (P/D ratios) — necessary
Core result. Delivers the closed-form pricing formulas that the entire paper builds on. Referenced in Corollary 1, Proposition 2, the quantitative analysis (§3), and Extension 2.

### Remark 1 (Existence condition) — necessary
Introduces the $A^j < 1$ condition. This is not a throwaway technicality: it is directly invoked in Extension 2 (§4.2) to explain why P/D ratios are undefined under severe displacement, which motivates the role of government transfers. The formal statement earns its place.

### Corollary 1 (Valuation spread) — lightweight but justified
States $P^{AI}/D^{AI} > P^N/D^N$ when $\Delta\theta > 0$. This is the paper's central testable prediction. While the result follows quickly from Proposition 1, giving it a named environment makes it citable and highlights the key economic takeaway. The proof is one sentence. This is standard practice in theory papers and well within the norms of top finance journals.

### Proposition 2 (Comparative statics) — necessary, all three parts used
- Part (i): referenced in quantitative discussion (§3) and calibration.
- Part (ii): referenced in quantitative discussion ("increasing the singularity probability raises the AI stock premium").
- Part (iii): referenced by number on lines 62 and 199; drives the extinction-risk discussion.

No subpart is orphaned.

### Proposition 3 (Veto under incomplete markets) — necessary
Both parts do essential work: (i) establishes the distortion, (ii) shows complete markets eliminate it. The contrast is the economic point of Extension 1.

## Displayed Equations

| Eq | Content | Used in |
|----|---------|---------|
| (1) | Consumption growth | All pricing derivations |
| (2) | Displacement | Core mechanism, $\phi^{-\gamma}$ in P/D |
| (3) | Utility | Euler equation, veto |
| (4)–(5) | P/D ratios | Core results, calibration, figure |
| (6) | Existence condition $A^j$ | Extension 2 discussion |
| (7) | Veto utility gain $\Delta U^H$ | Proposition 3 |
| (8) | Transfer consumption | Extension 2, figure |
| (9) | Transfer ratio | Key insight ($\eta$-independence) |
| (10)–(13) | Appendix proof steps | Derivation of Prop 1 |

No equation is introduced and abandoned. Each feeds forward into a result, discussion, or exhibit.

## Prose Mechanisms

- **Private AI capital dividends** $(1-\alpha_t)C_t - D_t^{AI}$ (inline, not displayed): introduced to clarify the source of market incompleteness. Not used in any formula, but it serves essential narrative work — explaining what the household *cannot* trade. This is an inline expression, not a formal object.
- **$\Gamma^{AI}$ and $\Gamma^{N}$ definitions**: introduced in Proposition 1, discussed in the paragraph following it, used in Corollary 1 and Proposition 2. Do clear economic work (dividend growth divergence drives the hedging channel).

## Checks Against Audit Criteria

1. **Introduced and abandoned?** No. Every formal object is referenced after introduction.
2. **Qualitative takeaway statable in plain English?** No formal object reduces to a claim that would be equally convincing without the math. Corollary 1 is the closest case but it names the paper's central prediction and is extremely compact (6 lines including proof).
3. **Unused variables/parameters/functions?** None found. Full inventory above.
4. **Pompous or ceremonial formalism?** No. The paper uses three propositions, one corollary, and one remark across a 20-page theory paper — well within norms. No unnecessary lemmas, definitions, or assumptions environments. Proofs are concise (Prop 1's proof is in the appendix per the spec).
5. **Auxiliary formal detours?** No. Both extensions branch directly from the baseline and advance the main argument (market incompleteness distorts real decisions; transfers can overcome frictions under singularity growth).

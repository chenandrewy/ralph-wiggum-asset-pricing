# tests/theory-deadweight.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 1m 50s
[ralph-garage/agent-logs/20260409T210609.010908-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T210609.010908-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, subpart, and parameter does meaningful economic, quantitative, or narrative work; no deadweight formalism found.

## Audit methodology

Examined every displayed equation (8 in the main text, 3 in the appendix), every proposition (3), the remark (1), every named parameter ($\beta, g, \gamma, \phi, \eta, \theta, \Delta\theta, p, \xi, \delta, \tau, \alpha$), and every piece of notation ($C_t, c_t^H, \alpha_t, \theta_t, D_t^{AI}, D_t^N, \Gamma^{AI}, \Gamma^N, A^j, \phi_\text{eff}$) against four criteria: (1) Is it used in a result, calibration, or interpretation? (2) Could its takeaway be stated in plain English without loss? (3) Is it introduced and then abandoned? (4) Is it ceremonial or pompous?

## Detailed findings

### Equations

| Eq | Content | Verdict | Justification |
|----|---------|---------|---------------|
| (1) | $C_{t+1} = (1+g)C_t$ | Earns its keep | Sets up $g$, which appears in every P/D formula and calibration. One line, standard. |
| (2) | $\alpha_{t+1} = \phi\alpha_t$ | Earns its keep | Core displacement mechanism. Referenced throughout. |
| (3) | CRRA utility $U_0^H$ | Earns its keep | Establishes $\beta$ and $\gamma$, both used in every pricing result. Standard for the genre. |
| (4)-(5) | P/D ratios for AI and non-AI stocks | Earns its keep | Central result. Both ratios used in Table 1, comparative statics, and Extension 2. |
| (6) | Existence condition $A^j < 1$ | Earns its keep | Cross-referenced in Proposition 2(iii) proof and Extension 2 discussion of the infinite-P/D discontinuity in Figure 2. The $A^j$ shorthand is reused. |
| (7) | Post-transfer consumption | Earns its keep | Defines the transfer mechanism; feeds into $\phi_\text{eff}$ and Figure 2. |
| (8) | Transfer ratio independent of $\eta$ | Earns its keep | Makes a counterintuitive point (ratio doesn't depend on $\eta$) and then the text explains why the *levels* matter. This is economic insight, not ceremony. |

### Propositions and Remark

| Object | Verdict | Justification |
|--------|---------|---------------|
| Proposition 1 (P/D ratios) | Earns its keep | The paper's core quantitative result. Feeds into Table 1, Figure 2, and both extensions. |
| Remark 1 (existence condition) | Earns its keep | Could have been prose, but the formal statement is cross-referenced twice (Prop 2 proof, Extension 2 discontinuity discussion). The explicit inequality adds precision, and the economic interpretation (infinite hedge value) is substantive. |
| Proposition 2 (comparative statics) | All three parts earn their keep | (i) used in quantitative interpretation; (ii) used in table discussion; (iii) used in table discussion and connects to extinction risk theme. |
| Proposition 3 (veto) | Both parts earn their keep | The contrast between (i) incomplete and (ii) complete markets *is* the economic point. Neither part is obvious enough to omit. |

### Parameters and notation

- **$\alpha_t$ (household share)**: Introduced in Setup, cancels out of P/D ratios (Propositions 1-2), reappears in Extensions at $\alpha = 0.70$. The cancellation is a feature (P/D ratios don't depend on the level of household share), and $\alpha$ is essential for describing the displacement mechanism and the transfer formulas. Not deadweight.
- **$\Gamma^{AI}$, $\Gamma^N$ (dividend growth factors)**: Efficient shorthand appearing in Propositions 1-2, their proofs, Remark 1, and Extension 2.
- **$A^j$ (SDF-weighted growth)**: Introduced in Remark 1, reused in Proposition 2(iii) proof and Extension 2. Efficient.
- **$\phi_\text{eff}$ (effective displacement)**: Connects Extension 2 back to Proposition 1, avoiding re-derivation. Efficient.
- **$\xi$ (extinction probability)**: Used in Propositions 1-2, Table 1, Extension 1 discussion, and Extension 2 figure. Not deadweight.
- **$\delta$ (deadweight cost parameter)**: Used in Eqs (7)-(8), calibrated at 0.5, appears in Figure 2. Earns its keep.

### Proofs

- **Proposition 1 proof** (Appendix): Required by spec. Contains the Euler equation derivation and an honest approximation note.
- **Proposition 2 proof** (inline): Each part has economic content. Part (iii)'s convexity argument explains *why* extinction compresses the ratio, not just *that* it does.
- **Proposition 3 proof** (inline): Concise; each part is 3-4 sentences.

### Things that are NOT in the paper (confirming absence of common deadweight patterns)

- No unused notation or parameters.
- No lemmas or corollaries that exist only to support proofs.
- No formal welfare theorems beyond what the extensions need.
- No explicit SDF derivation (the paper correctly skips straight to P/D ratios).
- No unnecessary generalization (e.g., the model doesn't introduce heterogeneous agents beyond what's needed).
- No formal definition of "market incompleteness" as a definition environment; it's stated in plain English.

## Summary

The paper is lean. Every formal object contributes to either a quantitative result (Table 1, Figures 1-2), an economic claim (hedging channel, veto distortion, transfer effectiveness), or a cross-reference that connects sections. No formalism is introduced and abandoned, no qualitative takeaway requires its equation to be believed, and no parameter goes unused.

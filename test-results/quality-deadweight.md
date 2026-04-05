# tests/quality-deadweight.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 1m 36s
[ralph-garage/agent-logs/20260404T235928.981179-0400_quality-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.981179-0400_quality-deadweight_claude_opus.log)

# quality-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to at least one result, calibration, or economic interpretation; no formalism is abandoned, ceremonial, or replaceable by plain English without weakening the claims.

## Detailed Audit

### Parameters
All parameters (β, γ, g, p, G, φ, α, α_S, θ, δ, κ, q) appear in at least one proposition, corollary, calibration table, or figure. None are introduced and abandoned.

### Propositions and Corollaries
- **Proposition 2 (P/D ratios)**: Core pricing formula. Used in calibration (Table 1), all three extensions, and the figure.
- **Corollary 3 (Hedging premium)**: Establishes the spread, which is the paper's main result. Comparative statics (increasing in p, decreasing in Λ) deliver economic content.
- **Proposition 4 (IM amplification)**: Quantifies the role of market incompleteness with a clean ratio. Connects to the GKP contribution.
- **Proposition 5 (Veto)**: Links incompleteness to deployment distortion. Connects to transfers extension.
- **Proposition 6 (Extinction)**: Shows how extinction dilutes hedging. Creates a tension that advances the narrative.

### Definitions
- **Definition 1 (Equilibrium)**: Standard for theory papers in top finance journals. Anchors the Euler equation that drives all pricing.

### Auxiliary Notation
- **V₀, V∞**: Both appear in the P/D formula, spread formula, figure annotations, and economic interpretation. They are not decorative.
- **H^A, H^N (hedge factors)**: Decompose the P/D ratio into economically interpretable channels (dividend growth × marginal utility). Used in spread and extinction extension.
- **Λ = (1−φ)G**: Central object linking displacement severity to all results.
- **Y₀**: Appears only in Eq (2) and never in results. However, this is minimal notational convention for specifying a growth path, not ceremonial formalism.
- **Y^pub_t**: Necessary to distinguish publicly traded output from total output, which is the core friction.

### Could any result be stated in plain English?
The qualitative claims (AI stocks earn a premium, incompleteness amplifies it, transfers help, veto is rational under incompleteness, extinction dilutes the premium) could be stated informally. But the paper's contribution depends on the *closed-form expressions* and *quantitative magnitudes* that the formalism delivers. Removing the formalism would weaken the economic claims by eliminating the quantitative content (Table 1, Figure 3) and the precise comparative statics.

### Formal Detours
None found. There are no lemmas, no auxiliary propositions, no unused definitions. The paper moves linearly: model → pricing → magnitudes → extensions.

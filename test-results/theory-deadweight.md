# tests/theory-deadweight.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 1m 58s
[ralph-garage/agent-logs/20260409T215056.133234-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.133234-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper does identifiable economic, narrative, or quantitative work; no deadweight formalism found.

## Detailed Audit

### Parameters
All parameters introduced in the paper are used in at least one result, calibration, or interpretation:

- **$g$ (growth rate)**: Appears in all P/D formulas (eqs 4–5) and calibration ($g = 0.02$).
- **$p$ (singularity probability)**: Appears in P/D formulas, Proposition 2(ii), and the calibration grid in Table 1.
- **$\xi$ (extinction probability)**: Appears in P/D formulas, Proposition 2(iii), and the calibration grid.
- **$\eta$ (productivity boost)**: Appears in $\Gamma$ terms, calibration, and the transfer analysis (Extension 2).
- **$\phi$ (displacement severity)**: Appears in P/D formulas, Proposition 2(i), transfers ($\phi_\text{eff}$), and calibration.
- **$\alpha_t$ (household consumption share)**: Defines the model's economic content (displacement), cancels from the SDF in the baseline (a mathematical convenience, not evidence of deadweight), and reappears substantively in the transfer equation (eq 7) and effective displacement (eq 8).
- **$\theta_t$ (AI dividend share)**: Defines dividend processes, enters $\Gamma^{AI}$ and $\Gamma^{N}$, used in calibration.
- **$\Delta\theta$ (AI share jump)**: Enters $\Gamma$ terms, discussed in the approximation disclosure, used in calibration.
- **$\beta$ (discount factor)**: Appears in P/D formulas and calibration.
- **$\gamma$ (risk aversion)**: Appears in P/D formulas, Proposition 2(i)–(ii), Proposition 3(i), and calibration.
- **$\tau$ (tax rate)**: Used in transfer equation, effective displacement, transfer ratio, and figure.
- **$\delta$ (deadweight cost severity)**: Used in transfer equation, effective displacement, and calibration.

No parameter is introduced and then abandoned.

### Equations
- **Eq (1)** ($C_{t+1} = (1+g)C_t$): Sets up deterministic growth; used in the Euler equation derivation (Appendix A).
- **Eq (2)** ($\alpha_{t+1} = \phi\alpha_t$): Defines displacement; central to the entire paper.
- **Eq (3)** (CRRA utility): Defines preferences; generates the SDF that prices all assets.
- **Eqs (4)–(5)** (P/D ratios): The paper's central results. Used in Table 1, comparative statics, and Extension 2.
- **Eq (6)** (existence condition $A^j < 1$): Used in the proof of Proposition 2(iii) and in Extension 2's discussion of infinite P/D ratios at $\tau = 0$ under severe displacement.
- **Eq (7)** (post-transfer consumption): Drives the transfer analysis and figure.
- **Eq (8)** ($\phi_\text{eff}$): Connects transfers to the baseline pricing framework, avoiding re-derivation.
- **Eq (9)** (transfer ratio): Shows $\eta$-independence, setting up the argument that levels grow without bound.

No equation is ceremonial or disconnected from the argument.

### Formal Environments
- **Proposition 1 (P/D ratios)**: The paper's main result. Directly illustrated in Table 1.
- **Remark 1 (existence condition)**: Introduces $A^j$ notation reused in Proposition 2(iii) and Extension 2's infinite-P/D discussion. Not a detour.
- **Proposition 2 (comparative statics)**: All three parts are discussed in Section 3 and illustrated in Table 1. Part (iii) on extinction risk is a key economic insight.
- **Proposition 3 (veto)**: Both parts serve the argument that market incompleteness distorts real decisions, connecting to AI regulation debates.

### Auxiliary Notation
- **$\Gamma^{AI}$, $\Gamma^{N}$**: Compact the P/D formulas and make the hedging-channel comparison ($\Gamma^{AI} > \Gamma^{N}$) explicit. Discussed directly in the text.
- **$A^j$**: Introduced in Remark 1, reused in Proposition 2(iii) proof and Extension 2.
- **$\phi_\text{eff}$**: Bridges the transfer analysis to the baseline P/D formula.

### Could Any Result Be Stated in Plain English?
No. The quantitative content — P/D ratio magnitudes in Table 1, the transfer figure, the extinction attenuation mechanism — requires the formal expressions. The comparative statics in Proposition 2 depend on the algebraic structure of the P/D formula. Proposition 3 is already mostly informal, with the proof relying on economic reasoning rather than heavy algebra.

### Pompous or Ceremonial Formalism?
None found. The paper uses three propositions, one remark, and nine numbered equations — a lean formal apparatus for an asset pricing theory paper. Extension 2 deliberately avoids a proposition, communicating its results through equations and a figure instead. The appendix proof is necessary (Proposition 1 is the central pricing result) and concise.

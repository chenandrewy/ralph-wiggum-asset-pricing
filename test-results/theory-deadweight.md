# tests/theory-deadweight.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 2m 43s
[ralph-garage/agent-logs/20260412T141819.042085-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.042085-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object, parameter, and equation does identifiable economic or narrative work; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without weakening the paper's claims.

## Audit Details

### Parameters

All parameters introduced in the setup are used in at least one result, calibration, or interpretation:

| Parameter | Introduced | Used in |
|-----------|-----------|---------|
| $g$ | Setup (eq 1) | All P/D formulas, calibration |
| $\beta$ | Preferences (eq 3) | All P/D formulas, calibration |
| $\gamma$ | Preferences (eq 3) | SDF, all propositions, calibration |
| $p$ | Singularity (Setup) | All P/D formulas, calibration grid |
| $\xi$ | Singularity (Setup) | Prop 2, calibration grid |
| $\eta$ | Singularity (Setup) | P/D formulas, extensions, calibration |
| $\phi$ | Displacement (eq 2) | Central to all results |
| $\alpha_t$ | Consumption (Setup) | Extensions 1 and 2 (cancels from baseline P/D ratios, which is correct) |
| $\theta_t$, $\Delta\theta$ | Assets (Setup) | $\Gamma^{AI}$, $\Gamma^{N}$ in Prop 1, calibration |
| $q$ | Extension 1 | Prop 3 statement and proof |
| $\kappa$ | Extension 1 | Prop 3 statement and proof, numerical example |
| $\tau$, $\delta$ | Extension 2 | Transfer equations, $\phi_\text{eff}$, figure |

Note on $\alpha_t$: It cancels from the baseline P/D ratios (because the SDF depends on consumption *growth*, and $\alpha$ cancels in the ratio $c_{t+1}^H/c_t^H$). This is economically correct, not a sign of deadweight. The parameter reappears substantively in both extensions: in the veto numerical example ($\alpha = 0.70$) and in the transfer formula (eq 10) and effective displacement (eq 11), where the *level* of the household's consumption share determines transfer magnitudes.

### Equations

1. **Eq (1)** — aggregate consumption growth: Simple, but sets the notation $g$ used everywhere. One line.
2. **Eq (2)** — displacement: Defines $\phi$, the central economic parameter.
3. **Eq (3)** — CRRA utility: Required for deriving the SDF. Also needed because $\gamma > 1$ implies negative utility, which matters for the extinction normalization in Extension 1.
4. **Eqs (4)-(5)** — P/D ratios (Prop 1): The paper's main deliverable. Written out for both assets rather than using a generic $\Gamma^j$ — this is a defensible clarity choice since the comparison of $\Gamma^{AI}$ vs $\Gamma^{N}$ is the economic point.
5. **Eq (6)** — existence condition (Remark 1): Forward-deployed in Extension 2, where extreme displacement violates this condition and motivates transfers. Not a standalone technicality.
6. **Eq (9)** — veto utility gain: Required for the proof of Prop 3(i).
7. **Eq (10)** — transfer consumption: Foundational for Extension 2.
8. **Eq (11)** — effective displacement $\phi_\text{eff}$: Connects transfers to the baseline pricing formula, enabling reuse of Prop 1.
9. **Eq (12)** — transfer ratio: Makes the $\eta$-independence point explicit and supports the quantitative illustration ("50% loss becomes 250% gain"). Real economic content.
10. **Eqs (14)-(16)** — appendix proof: Required by the spec ("all propositions are explicitly proved").

### Propositions and Formal Objects

- **Proposition 1** (P/D ratios): The paper's central result. No deadweight.
- **Remark 1** (existence condition): Pays off in Extension 2 (infinite hedging demand → transfers restore finite prices). Economically substantive.
- **Proposition 2** (extinction attenuation): Real comparative static. The inline proof is the most detailed formal passage; the semi-elasticity argument (convexity of $A/(1-A)$) is needed specifically for the *ratio* claim, which is not obvious from the formulas. The proof could potentially move to an appendix, but it is not ceremonial — it proves a stated result.
- **Proposition 3** (veto): Main result of Extension 1. Both parts (incomplete vs. complete markets) do economic work: part (i) shows the distortion, part (ii) shows incompleteness is the cause.
- **Kaldor-Hicks efficiency**: Introduced in one sentence, used in Prop 3's statement ("even when development is socially efficient"). Light formalism with clear payoff.

### Structural Objects

- **AI owners**: Never optimize or trade, but serve as (a) the residual consumption claimant that makes $\alpha_t$ meaningful, (b) the tax base in Extension 2, and (c) the economic analogy to GKP's future innovators. Not deadweight — they are the source of the incomplete-markets problem.
- **Two-asset structure** ($\theta_t$ vs $\alpha_t$): The distinction between dividend share and consumption share is economically necessary (the household's consumption depends on non-tradeable components like labor income, not just public stock dividends). Both are used in results.

### Possible Concerns Examined and Dismissed

- **Could eq (1) be plain English?** It's one line that sets notation. Removing it would save nothing and force the reader to infer $g$'s role from later equations.
- **Are both P/D formulas (eqs 4-5) needed?** They're structurally identical. A single formula with $\Gamma^j$ would be more compact, but writing both lets the reader see the comparison directly. This is a standard presentation choice, not deadweight.
- **Is the Prop 2 proof too long for an inline proof?** It runs about 10 lines and proves a non-obvious result about the *ratio* of P/D ratios (not just the spread). The spec requires all propositions be proved. The proof does real mathematical work.

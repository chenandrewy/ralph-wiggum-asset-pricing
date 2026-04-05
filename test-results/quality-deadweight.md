# tests/quality-deadweight.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 1m 31s
[ralph-garage/agent-logs/20260404T234508.986878-0400_quality-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260404T234508.986878-0400_quality-deadweight_claude_opus.log)

# quality-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to the economic argument, quantitative illustrations, or both; no formalism is abandoned, ceremonial, or replaceable by plain English without weakening claims.

## Audit of every formal object

### Parameters and variables
| Symbol | Introduced | Used in |
|--------|-----------|---------|
| $\beta, \gamma$ | Eq (1) | $R$, all P/D results, calibration (Table 1) |
| $C_t$ | Eq (1) | Consumption jump, veto proof, throughout |
| $g$ | Eq (2) | $R$, all P/D results, calibration |
| $\alpha, \alpha_S$ | Sec 2.1/2.2 | $H^A$, $H^N$, spread, calibration |
| $p$ | Sec 2.2 | $V_0$, spread, calibration |
| $G$ | Sec 2.2 | $\Lambda$, transfer extension, calibration |
| $\phi$ | Sec 2.2 | $\Lambda$, amplification (Prop 4), calibration |
| $\Lambda$ | Eq (4) | Central to all results |
| $R$ | Eq (7) | $V_0$, $V_\infty$, all P/D formulas |
| $V_0, V_\infty$ | Eq (7) | P/D formula, spread, figure annotation |
| $H^A, H^N$ | Eq (8) | P/D formula, spread, extinction extension |
| $\theta, \delta$ | Eq (9) | Transfer extension, Figure 2 |
| $\kappa$ | Sec 4.2 | Veto proposition (Prop 5) |
| $q$ | Sec 4.3 | Extinction proposition (Prop 6) |
| $Y_0$ | Eq (2) | Initial condition only—standard, absorbed into $C_t$ |
| $Y_t^{pub}, \alpha_t$ | Sec 2.3 | Define dividend structure; intermediate notation used once but necessary for clarity |
| $\tau$ | Sec 2.2 | Time of singularity; used in consumption jump (Eq 3) |

**Finding:** No variable or parameter is introduced and then unused in any result, calibration, or interpretation.

### Propositions and formal results
1. **Definition 1 (Equilibrium):** States Euler equation and market clearing. The Euler equation is directly used to derive Proposition 2. Standard practice in theory papers—not ceremonial.
2. **Proposition 2 (P/D ratios):** Core result. Closed-form P/D ratios drive Table 1, the spread corollary, and all extensions. Essential.
3. **Corollary 3 (Hedging premium):** Derives the spread and its comparative statics in $p$ and $\Lambda$. Directly interpreted in the text and quantified in Table 1. Essential.
4. **Proposition 4 (Incomplete vs. complete markets):** The amplification factor $(1-\phi)^{1-\gamma}$ quantifies the role of incompleteness. Could the qualitative point be made in English? Yes, but the factor is what makes the quantitative claim ("can be very large when $\phi$ close to 1 and $\gamma$ high") credible. Earns its keep.
5. **Proposition 5 (Veto):** Almost plain-English already (parts a and b). The formal proof in the appendix adds rigor at minimal cost. Links directly to Extension 1 via $\Lambda > 1$. Not deadweight.
6. **Proposition 6 (Extinction):** The $(1-q)$ scaling is clean, one line, and used to discuss the tension between displacement severity and extinction risk. Not deadweight.

### Equations
- **Eq (1) (Utility):** CRRA. Standard, minimal, all parameters used.
- **Eq (2) (Output):** One line, sets up $g$ notation. Could be prose, but it's one equation and establishes the growth path that the Gordon model and all results build on.
- **Eq (3)–(4) (Consumption jump and $\Lambda$):** $\Lambda$ is the paper's central object. Essential.
- **Eq (5) (Euler equation in Definition 1):** Used to derive Proposition 2 in the appendix proof. Essential.
- **Eq (6)–(8) (P/D ratios, benchmarks, hedge factors):** Core results.
- **Eq (9) (Transfer $\Lambda$):** Enables Figure 2 and the transfer discussion. Essential.
- **Eq (10)–(11) (Extinction P/D and spread):** Enable Proposition 6. Essential.

### Prose mechanisms
- The four-item list describing the singularity (Sec 2.2) is informal and sets up the formal results efficiently.
- The complete-markets comparison (Sec 3.2) uses $\Lambda^{CM} = G$ inline rather than a separate proposition. Appropriately light.
- The transfer discussion links Eq (9) to Figure 2 without unnecessary formalism.
- The veto-to-transfer connection ("If government transfers raise $\Lambda$ above 1...") is made in prose, not a separate proposition. Good restraint.

### Checks for deadweight patterns
- **Introduced then abandoned?** No. Every formal object is referenced in at least one result, figure, or proof.
- **Qualitative takeaway replaceable by plain English?** The main results (Props 2–4) require formalism for their quantitative claims. Props 5–6 are nearly plain English already, with formal proofs adding necessary rigor.
- **Unused parameters?** No. All parameters appear in at least one result and in the calibration.
- **Pompous or ceremonial formalism?** No lemmas, no unnecessary technical conditions, no auxiliary constructions. Definition 1 is the only "ceremony" and it states the Euler equation that is directly used.
- **Auxiliary formal detours?** None. Each extension is one equation and one proposition, directly advancing the argument.

# tests/theory-clarity.py
Started: 2026-04-11 21:27:07 EDT
Runtime: 3m 3s
[ralph-garage/agent-logs/20260411T212707.787432-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T212707.787432-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: The model setup uses well-structured paragraphs and display math for most critical expressions; two items merit attention but do not impair a careful reader's ability to follow the results.

## Key items identified

### Should appear in display math (and do)
1. **[AGG-GROWTH]** Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq. (1), display math in setup
2. **[DISPLACEMENT]** Household share displacement $\alpha_{t+1}=\phi\alpha_t$ — eq. (2), display math in setup
3. **[UTILITY]** CRRA utility functional — eq. (3), display math in setup
4. **[PD-AI / PD-NONAI]** Closed-form P/D ratios — eqs. (4)–(5), display math in Proposition 1
5. **[EXISTENCE]** Existence condition $A^j<1$ — eq. (6), display math in Remark 1
6. **[TRANSFER-CONS]** Transfer consumption $c^H_{post}$ — eq. (8), display math in Extension 2
7. **[PHI-EFF]** Effective displacement $\phi_\text{eff}$ — eq. (9), display math in Extension 2
8. **[TRANSFER-RATIO]** Consumption ratio independent of $\eta$ — eq. (10), display math in Extension 2

### Could be promoted to display math
9. **[GAMMA-DEF]** Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — currently inline in the "where" clause of Proposition 1. These are the key objects distinguishing AI from non-AI pricing and drive the hedging channel explanation and the Proposition 2 proof. A standalone display equation would make them easier to find on re-reading.

### Prose items — should appear at/near paragraph start
10. **[HOUSEHOLD-SHARE]** $c_t^H = \alpha_t C_t$ — introduced mid-paragraph after eq. (1); follows naturally from the display equation
11. **[SINGULARITY-PROB]** Probability $p$ — opens the Singularity paragraph (line 86). Good.
12. **[EXTINCTION-PROB]** Probability $\xi$ — inside numbered list under Singularity paragraph. Acceptable given the list structure.
13. **[AI-DIVIDEND-DEF]** $D_t^{AI}=\theta_t C_t$ and $\theta$ dynamics — inside bullet list under Assets paragraph. Acceptable.
14. **[INCOMPLETE-MARKETS]** Household cannot trade restricted AI equity — stated at line 109, mid-paragraph after the asset list. The emphasis (\emph{cannot}) helps, but this is the central economic mechanism and could open its own paragraph.
15. **[POSITIVE-SING]** Positive singularity probability $q$ and structure — opens Extension 1 setup (line 200). Good.
16. **[VETO-COST]** Veto cost $\kappa$ — mid-paragraph (line 204), but it defines the veto concept in its lead sentence. Acceptable.
17. **[TAX-DEADWEIGHT]** Tax rate $\tau$ and deadweight $\delta\tau$ — introduced in prose then immediately given display math (eq. 8). Good.

### Key condition appearing only in proof
18. **[PHI-ETA-CONDITION]** $\phi(1+\eta)<1$ — this condition determines whether household consumption actually falls despite aggregate growth. It is the economic linchpin of the veto result (Proposition 3) and the hedging intuition after Proposition 1. Currently it appears explicitly only inside the proof of Proposition 3 (line 222). It is used implicitly in the quantitative section ($\phi(1+\eta)=0.75$, line 185) but never stated as a named condition in the model setup or any proposition statement.

## Section-level findings

### Section 2.1 (Setup)
- Well organized into labeled paragraphs (Consumption, Singularity, Assets, Preferences). Most primitives are introduced clearly.
- Items [AGG-GROWTH], [DISPLACEMENT], [UTILITY] all appear in display math. Good.
- [HOUSEHOLD-SHARE] ($c_t^H = \alpha_t C_t$) is inline after eq. (1) rather than in display math, but it is simple and follows naturally from the preceding display. Acceptable.
- [INCOMPLETE-MARKETS] is the central economic assumption but is introduced mid-paragraph (line 109) after listing the assets. It would benefit from opening its own paragraph or formal assumption block, but it is clearly stated with emphasis. Minor note.
- [PHI-ETA-CONDITION] ($\phi(1+\eta)<1$) is never stated in the setup. Since both $\phi$ and $\eta$ are introduced here, this would be the natural place to note the joint condition. This is the most actionable finding.

### Section 2.2 (Equilibrium prices)
- P/D ratios in display math. Good.
- [GAMMA-DEF]: $\Gamma^{AI}$ and $\Gamma^{N}$ are defined inline in a "where" clause inside Proposition 1. These are load-bearing for the hedging channel discussion and for Proposition 2's proof (which relies on $\Gamma^{AI} > \Gamma^{N}$). Promoting them to a standalone display equation would improve findability. Minor note.
- The discussion paragraph after Proposition 1 (line 153) correctly explains the hedging channel by comparing $\Gamma^{AI}$ and $\Gamma^{N}$ and implicitly invokes [PHI-ETA-CONDITION] ("AI stocks pay off precisely when the household's consumption falls"). This implicit usage would be clearer if the condition were stated explicitly in the setup.

### Section 2.3 (Discussion)
- No new assumptions introduced. Refers back to earlier items appropriately. No issues.

### Section 3 (Quantitative Analysis)
- No new model assumptions. Uses $\phi(1+\eta) = 0.75$ (line 185) implicitly confirming [PHI-ETA-CONDITION] but does not name the condition. No issues for this section specifically.

### Section 4.1 (Extension 1: Veto)
- [POSITIVE-SING] and [VETO-COST] are introduced clearly in setup prose. Good.
- [COMPLETE-MARKETS] consumption is stated mid-paragraph (line 206) but is short and clear. Acceptable.
- Proposition 3 statement does not mention [PHI-ETA-CONDITION]; the condition surfaces only inside the proof (line 222). A reader who skips the proof would not know what parameter restriction drives the veto result. This is the main clarity concern but does not rise to a failure because the proof is short and inline.

### Section 4.2 (Extension 2: Transfers)
- [TAX-DEADWEIGHT], [TRANSFER-CONS], [PHI-EFF], and [TRANSFER-RATIO] are all introduced with display math. Good.
- Setup paragraph clearly motivates the extension before introducing parameters. Good.

## Summary of actionable notes (not failures)
1. **[PHI-ETA-CONDITION]**: State $\phi(1+\eta)<1$ explicitly when $\phi$ and $\eta$ are first introduced together in the Singularity paragraph, and reference it in the Proposition 3 statement.
2. **[GAMMA-DEF]**: Consider promoting $\Gamma^{AI}$ and $\Gamma^{N}$ to a standalone display equation for easier reference.
3. **[INCOMPLETE-MARKETS]**: Consider giving market incompleteness its own paragraph heading or opening sentence in the model setup.

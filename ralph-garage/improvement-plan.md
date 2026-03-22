# Improvement Plan

## Current Status

- **Tests**: 2/2 pass (spec-compliance, theory-correctness).
- **Referee (referee-top3)**: Two substantive comments. No failing tests to fix, so this plan focuses on the referee feedback.

## Referee Comments Summary

**Comment 1 — Endowment-economy assumption inflates AI share and overstates hedging channel.**
The model sets $c_t = D_t^A + D_t^N$, making $s = 0.15$ (market-cap weight). But household consumption is dominated by labor income (~60–65% of GDP). If $s$ is measured as AI dividends / total household income, it drops to ~1–3%, and the hedging amplifier collapses to ~1. The referee asks us to either (a) add labor income explicitly or (b) argue carefully why the endowment calibration is appropriate.

**Comment 2 — Expected-return prediction conflicts with AI stocks' empirical risk profile.**
The model predicts AI stocks earn *lower* expected returns (hedging/insurance asset). Empirically, AI stocks have high betas, high volatility, and procyclicality—traits that command *higher* expected returns in standard factor models. The peso-problem defense is unfalsifiable in short samples. The referee wants standard aggregate consumption risk (i.i.d. or persistent shocks to $g$) added so the model generates both a positive business-cycle risk premium and a negative hedging discount, and the reader can assess which dominates.

## Plan

### 1. Address Comment 1: Labor Income and the AI Share

**Approach**: Option (a) — add non-tradeable labor income to the model. This is the stronger response because it directly addresses the criticism and makes the model more realistic.

**Specific changes**:
- In Section 2.1 (Environment), add a non-tradeable labor income stream $L_t$ so that $c_t = D_t^A + D_t^N + L_t$.
- Redefine the AI consumption share as $s_t \equiv D_t^A / c_t$, which now becomes small (~2–5%).
- Specify that upon singularity, labor income also drops (e.g., by a factor $(1 - \phi_L)$), because the singularity displaces labor. This preserves $J < 1$ even with a small $s$.
- The key insight: when labor income is included and also falls upon singularity, the household's consumption still crashes, preserving the hedging channel. The hedging amplifier $J^{-\gamma}$ remains large because $J$ depends on the *consumption-weighted* impact, not just the portfolio weight of AI stocks.
- Re-derive Propositions 1–2 with the extended consumption equation. The structure should remain the same (closed-form P/D ratios), just with a modified $J$ that now incorporates labor.
- Update calibration tables. The AI market-cap share is no longer the right input for $s$; instead, calibrate $s$, the labor share, and $\phi_L$ from data.
- This change strengthens the paper: it shows the hedging channel is robust to realistic consumption composition, not an artifact of the endowment assumption.

**Risk**: This is a model-section change. Verify all downstream propositions, corollaries, and the extension still hold. The algebra should go through since labor income enters $J$ additively, but check carefully.

### 2. Address Comment 2: Add Business-Cycle Risk

**Approach**: Add i.i.d. consumption growth shocks to the normal (non-singularity) state so AI stocks face two opposing forces on expected returns.

**Specific changes**:
- In Section 2.1 or 2.2, add a mean-zero i.i.d. shock $\epsilon_t$ to normal-period growth: $g_t = g + \sigma \epsilon_t$. AI stocks have higher exposure to $\epsilon_t$ (higher beta) than non-AI stocks.
- The SDF now varies in normal times too, generating a standard positive risk premium for high-beta AI stocks.
- In the expected-returns subsection (Section 3.3), decompose the expected excess return of AI vs. non-AI into: (i) a positive business-cycle premium (from high beta) and (ii) a negative hedging discount (from singularity insurance). Show conditions under which each dominates.
- This directly addresses the referee: the model now generates high realized returns from both the business-cycle premium and the peso problem, while the hedging channel operates as before on valuations.
- Keep this tractable. With CRRA and i.i.d. lognormal shocks, the Euler equation still yields (near-)closed-form expressions.

**Risk**: Adding a second source of risk may complicate the algebra. Keep it simple—i.i.d. shocks with differential beta exposure. If closed-form is not possible, present the decomposition qualitatively and show calibrated numbers.

### 3. Update Calibration and Tables

- Recalibrate Tables 1–3 with the labor-income-augmented model.
- Add a row or panel showing the expected-return decomposition (business-cycle premium vs. hedging discount).
- Verify we stay within 6 exhibits.

### 4. Tighten Prose

- Update the introduction to preview the labor-income result (the hedging channel survives realistic consumption composition).
- Update the Insurance Puzzle subsection to reference the business-cycle risk extension rather than relying solely on the peso problem.
- Update the GKP comparison paragraph to note that our model, like GKP, now has two risk factors (consumption + displacement), but with different economic content.

### Sequencing

1. First: Model changes (labor income + i.i.d. shocks). These are the core changes.
2. Second: Re-derive propositions and verify the extension section still works.
3. Third: Update calibration tables and figures.
4. Fourth: Tighten prose (intro, insurance puzzle, GKP comparison, conclusion).

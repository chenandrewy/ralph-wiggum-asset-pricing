# Improvement Plan

## Diagnosis

The `theory-correctness` test fails because Proposition 4 (eq 17) is mathematically wrong. The error propagates to Proposition 5 and several verbal claims. The referee report independently identifies the same conceptual root cause: the paper conflates a mechanical cash-flow differential with hedging demand (SDF amplification). These two issues are the same fix.

**The core error**: In the friction-resolves state, the paper assumes consumption neutrality (J=1) means no premium contribution. But AI dividends still grow by (1+θ) while non-AI dividends grow by (1-φ), so the cash-flow differential persists even when hedging demand vanishes. The correct Proposition 4 formula is:

$$v^A - v^N = \frac{\lambda(1-\delta_H)\,a\,(\theta+\phi)\,[(1-\pi)J^{-\gamma} + \pi]}{(1-a)[1-(1-\lambda)a]}$$

The missing `+π` term breaks the hump-shaped result (Proposition 5) and the verbal claim that the premium vanishes under complete markets.

## Plan: Premium Decomposition Overhaul

The entire fix revolves around one change: **decompose the premium into a cash-flow component and a hedging-amplification component throughout the paper.**

### Step 1: Introduce the decomposition after Proposition 2

After eq (13), decompose the existing premium:

$$v^A - v^N = \underbrace{\frac{\lambda\,a\,(\theta+\phi)}{(1-a)[1-(1-\lambda)a]}}_{\text{cash-flow premium}} \cdot \underbrace{J^{-\gamma}}_{\text{hedging amplifier}}$$

- The cash-flow premium reflects that AI dividends jump more than non-AI dividends upon singularity. A risk-neutral investor (γ→0) would pay this.
- The hedging amplifier reflects that marginal utility is high in the singularity state (J<1, γ>1), so the household overpays relative to expected cash flows.
- Calibration: at baseline (J≈0.82, γ=3), J^{-γ}≈1.81, so hedging roughly doubles the cash-flow-only premium.

### Step 2: Fix the complete-markets claim (Section 2.3 and Introduction)

Current: "the AI valuation premium would vanish" under complete markets.

Fix: Under complete markets (J=1), the hedging amplifier equals 1 and the *hedging component* vanishes, but the cash-flow premium remains positive. The premium shrinks to its cash-flow-only value. Change the claim to: "the hedging component of the premium would vanish."

### Step 3: Fix Proposition 4 (eq 17)

Replace eq (17) with the corrected formula that includes both the friction-persists and friction-resolves state contributions:

$$v^A - v^N = \frac{\lambda(1-\delta_H)\,a\,(\theta+\phi)\,[(1-\pi)J^{-\gamma} + \pi]}{(1-a)[1-(1-\lambda)a]}$$

Fix the proof: remove the claim that the friction-resolves state "contributes no hedging premium." Instead, note it contributes the cash-flow differential at the risk-neutral SDF.

### Step 4: Fix Proposition 5 (hump shape)

The total premium no longer vanishes as θ→∞. Two options:

**Recommended**: Restate Proposition 5 so the hump shape applies to the *hedging component* only: (1-π)J^{-γ}(θ+φ) → 0 as π→1, while the total premium approaches its cash-flow-only value. The hedging amplifier is hump-shaped in θ; the total premium is monotonically increasing. This is a cleaner and more precise result.

Update the verbal discussion: "the same event that generates hedging demand may also eliminate the need for it" should become "the same event that generates hedging demand may also resolve the friction that amplifies it — but the cash-flow differential remains."

### Step 5: Update the calibration discussion (Section 3.3)

The growth-hedging decomposition (Section 3.3) currently treats the hedging premium as the entire model premium. With the decomposition, this section should note that the model premium includes both cash-flow and hedging components. The "residual attributable to growth" calculation doesn't change numerically — but the interpretation sharpens: the model already captures some growth-like effects through the cash-flow differential.

### Step 6: Update the conclusion

Adjust language to reflect the decomposition — the premium has both a cash-flow and a hedging component; incomplete markets amplify the premium through hedging demand but are not the sole source.

### What NOT to change

- Propositions 1–3 and Corollary 1 are correct — do not modify.
- The baseline calibration numbers in Tables 1–3 are correct.
- The model setup (Sections 2.1–2.2) needs no changes.
- Do not add the referee's suggested empirical tests (cross-sectional predictions, time-series tests) — those are beyond the paper's theoretical scope and would require new data work.

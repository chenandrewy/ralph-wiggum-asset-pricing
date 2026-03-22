# Improvement Plan

## Status

All tests pass. No overhaul needed — the model section is correct and well-structured. Focus is on referee feedback and spec compliance.

## Key Issues

1. **Paper exceeds 20-page limit.** The referee-top3 review reports 22 pages; the spec requires at most 20. The spec-compliance test passed by estimating 17–19 pages from line counts, but the compiled PDF is longer.
2. **Event study (Table 4) is the weakest exhibit.** The paper spends ~1.5 pages presenting evidence it immediately discredits. The referee correctly notes this undermines rather than supports the contribution, and wastes one of six exhibit slots.
3. **Defensive digressions in Section 3.3 are too long.** "Why AI Stocks, Not Treasuries or Gold?" (~1 page) and the gradual-singularity paragraph can be heavily compressed. "Measuring Market Access and Private AI Capital" runs long on observable proxies.
4. **No figure illustrating the model mechanism.** The paper has five tables and one data figure but zero model-output figures. A mechanism figure would make the core contribution more memorable.
5. **Proof of Prop 6(i) has imprecise scaling claim.** The proof says $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta$ but the expression actually scales as $\theta^{1-\gamma} \to 0$. The conclusion is correct; the proof sketch needs a one-line fix.

## Plan

### 1. Replace event study with model-mechanism figure

- **Drop Table 4** (event study) and the ~1.5 pages of surrounding discussion in Section 3.4.
- **Add a new Figure 2** showing the premium decomposition across parameter space. Best candidate: the hump shape from Proposition 6 — plot the total premium, cash-flow component, and hedging component as functions of $\theta$, illustrating the self-resolving friction. Alternative: a $\lambda \times (g^A - g^N)$ heatmap of the hedging share from Table 2.
- Write an R script to generate the figure. Keep the event-study mention to one sentence in the conclusion or a footnote if desired.
- This recovers ~1.5 pages and replaces a weak exhibit with a strong one. Exhibit count stays at 6.

### 2. Cut defensive digressions to hit 20 pages

- **"Why AI Stocks, Not Treasuries or Gold?"**: Compress to 2–3 sentences. Core point: the singularity is an asymmetric shock; only assets with positive AI exposure can hedge it; safe-haven assets are orthogonal.
- **Gradual-singularity paragraph**: Delete. The self-limiting mechanism (Prop 2(ii)) already makes this point formally.
- **"Measuring Market Access and Private AI Capital"**: Condense to one short paragraph folded into the calibration discussion. Keep only the key data points ($\alpha$ small but increasing, $\psi \approx 0.10$–$0.20$).
- Target: recover ~2 pages from these cuts combined with the event-study removal, bringing total to ~18–19 pages.

### 3. Fix Prop 6(i) proof sketch

- Replace "$|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta$" with the correct scaling: "$J \approx s\theta$ implies $J^{-\gamma} \approx (s\theta)^{-\gamma}$, so $|(\theta+\phi)(J^{-\gamma}-1)| \sim \theta^{1-\gamma} \to 0$."
- One-line fix; no structural change.

### 4. Verify page count after changes

- Recompile and confirm the paper is at most 20 pages.

# Improvement Plan
AUTHOR PLAN — 2026-04-09 18:33:48 EDT

## Status: 17/25 tests pass, 8 fail

## Key Issues

### A. Transfers figure is broken (code + paper)
The extension figure (fig-extension-panels) has two severe problems:
1. **Panel (a) visual spike**: P/D blows up to ~1500 at τ≈10% for the baseline scenario, compressing all other data into an unreadable strip. The `compute_pd_with_transfer` formula has K→1 at certain τ values, causing a mathematical singularity.
2. **Panel (b) wrong message**: At τ=0 with large singularity (η=9), household consumption growth is φ(1+η)=0.5×10=5x. The household is doing great without transfers, undermining the entire motivation. The spec requires showing the singularity is *catastrophic* absent transfers.

**Root cause**: With η=9 and φ=0.5, displacement is severe in share terms but not in levels—aggregate growth swamps the share loss. A more powerful singularity should also cause more severe displacement (smaller φ).

**Fix**: In `generate-exhibits.R`, for the large singularity scenario, pair η=9 with a much smaller φ (e.g., φ=0.05), so φ(1+η)=0.5 and household consumption halves even with enormous growth. This is economically natural: a singularity powerful enough to produce 10x growth would plausibly displace far more labor. For panel (a), the reparameterization should eliminate the K→1 blow-up; if not, cap or filter extreme P/D values. Update the paper text at line 279 to describe the new parameterization.

### B. Extinction risk contradiction (intro line 64)
Line 64 says extinction interacts with displacement "to amplify valuation premia." But Proposition 2(iii) proves the spread is *decreasing* in ξ, and line 57 correctly says "extinction risk compresses this gap." This is a direct logical contradiction.

**Fix**: Rewrite line 64 to say extinction *attenuates* the premium or interacts in a "countervailing" way, consistent with Prop 2(iii).

### C. Eq (7) limit is misleading (paper lines 271-275)
The ratio $c^H_{post}/c^H_{no-transfer}$ is exactly constant in η—the (1+η) factors cancel for any η>0. Presenting it as $\lim_{\eta→∞}$ and saying it "converges to a finite constant" is incorrect. Two tests flag this independently.

**Fix**: Present eq (7) as an exact identity, not a limit. Rewrite the surrounding text to clarify: the *ratio* is η-invariant, but the *level* of consumption grows without bound. The economic insight (transfers scale with surplus) operates on levels, not ratios.

### D. GKP misattribution at line 261
The paper says GKP "observe that broader trading... would help resolve displacement risk." GKP actually calls transfers/bequests "inessential extensions" that only change magnitude. The paper repackages GKP's robustness argument as a policy observation.

**Fix**: Reframe as the paper's own interpretation, e.g.: "GKP note that intergenerational transfers affect the magnitude of displacement risk but treat them as inessential. We take a closer look at this channel..."

### E. Introduction flow and topic sentences (writing-intro)
Main arguments are buried inside paragraphs. Topic sentences are questions or background rather than claims. The AI authorship repetition ("As noted in the abstract") is clunky (rhetoric-meta also flags this).

**Fix**: Rewrite intro paragraph topic sentences so each leads with its main claim. Rework the AI-authorship introduction version to do different rhetorical work than the abstract—frame it as evidence that displacement is empirically grounded rather than repeating the same sentence.

### F. Appendix A is ceremonial (theory-deadweight)
The appendix contains no real proof details. It restates Prop 3's proof in SDF language that isn't used in the actual proof. factcheck-bysection also flags the SDF mischaracterization.

**Fix**: Remove the appendix entirely. The spec requires proofs in the paper; they're already in the main text. Remove the unused `\newtheorem{lemma}` too.

### G. Line 57 overstates "two to six times"
Table ratios range 1.1–5.8. "Two to six times" overstates the lower bound.

**Fix**: Change to "up to roughly six times higher" or "1.1 to nearly 6 times."

### H. Minor model issues
1. **Prop 2(i) proof** (line 185): says decrease in φ "makes the divergence between Γ^AI and Γ^N more valuable"—but Γs don't depend on φ. The mechanism is entirely through φ^{-γ} amplification. Fix the wording.
2. **Corollary 1**: φ<1 condition is redundant (Δθ>0 alone suffices since φ^{-γ} is common). Remove it.
3. **δ(τ) notation** (line 263): function wrapper introduced and never used again. Just write δ₀τ directly.
4. **GKP "creative destruction"** (line 194): GKP models displacement through expanding variety, not Schumpeterian creative destruction. Fix to "continuous displacement from innovation."

## Execution Order

1. **Fix the code** (`generate-exhibits.R`): reparameterize the large-singularity scenario with smaller φ. Regenerate exhibits. Verify panel (b) shows catastrophe at τ=0 and panel (a) has no spike.
2. **Fix the paper model/theory issues** (B, C, F, G, H): extinction contradiction, eq (7) presentation, remove appendix, fix overstated range, minor proof/notation issues.
3. **Fix GKP attribution** (D): rewrite line 261.
4. **Rewrite the introduction** (E): topic sentences, AI authorship device, flow.

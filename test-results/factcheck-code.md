# tests/factcheck-code.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 1m 36s
[ralph-garage/agent-logs/20260411T211526.521080-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.521080-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path is coherent, runs from scratch, and its outputs are consistent with all paper claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`, executed via `Rscript code/generate-exhibits.R`. The script produces all three exhibits used in the paper:

| Exhibit | Output file | Paper reference |
|---------|-------------|-----------------|
| Table (P/D ratios) | `paper/exhibits/table-pd-ratios.tex` | `\input{exhibits/table-pd-ratios.tex}` (line 186) |
| Extension figure | `paper/exhibits/fig-extension-panels.pdf` | `\includegraphics` (line 275) |
| AI valuations figure | `paper/exhibits/fig-ai-valuations.pdf` | `\includegraphics` (line 46) |

No other files exist in `paper/exhibits/` and no other exhibits are referenced in the paper. The mapping is one-to-one and complete.

## Execution status

- **Result**: All three exhibits generated successfully.
- **From-scratch**: Yes. The script downloads S&P 500 data from datahub.io and NASDAQ data from FRED at runtime. No precomputed caches or intermediate files are required.
- **Runtime dependencies**: R 4.2.2 with CRAN packages ggplot2, dplyr, tidyr, gridExtra, scales. All available and standard.
- **Network access**: Required for the two data downloads (datahub.io, FRED). This is consistent with spec III.3.d, which explicitly includes external data download in the 180-second budget.
- **Execution time**: Completed well within the 180-second limit.
- **Warnings**: Minor ggplot2 warnings about rows removed due to scale limits (expected behavior from axis capping in the extension figure). No errors.

## Paper-code consistency

### Parameter verification (all match)

| Parameter | Code value | Paper value (line) |
|-----------|------------|-------------------|
| β | 0.96 | 0.96 (189) |
| g | 0.02 | 0.02 (189) |
| γ (table) | 4 | 4 (189) |
| φ | 0.5 | 0.5 (189) |
| η | 0.5 | 0.5 (189) |
| θ | 0.15 | 0.15 (189) |
| Δθ | 0.2 | 0.2 (189) |
| α (extensions) | 0.70 | 0.70 (267) |
| δ (deadweight) | 0.50 | 0.5 (273) |
| p (extension) | 0.005 | 0.5% (267) |
| ξ (extension) | 0.05 | 5% (267) |
| η large | 9.0 | 9 (267) |
| φ large | 0.05 | 0.05 (267) |
| γ (veto) | 10 | 10 (231) |
| p (veto) | 0.01 | 1% (231) |
| κ (veto) | 0.01 | 1% (231) |
| q (veto) | 0.70 | 0.70 (231) |

### Claim verification

1. **Table magnitudes** (paper line 191): "For a singularity probability of 0.5% per year with no extinction risk, AI stocks trade at a P/D of about 15.5, while non-AI stocks trade near 11—a ratio of about 1.4." Generated table shows p=0.5%, ξ=0%: AI=15.5, Non-AI=11.1, Ratio=1.4. **Match.**

2. **P/D ratio at p=1%** (paper line 191): "At p=1%, the ratio rises to 2." Table shows p=1.0%, ξ=0%: Ratio=2.0. **Match.**

3. **Extinction attenuation** (paper line 191): "extinction risk compresses the AI premium." Table confirms ratios decrease as ξ increases within each p block. **Match.**

4. **Veto result** (paper line 231): "the household vetoes under incomplete markets... Under complete markets... the household does not veto." Code output: V_develop=-15.5327, V_veto=-15.3222 (VETO under incomplete); V_develop_CM=-13.4615, V_veto=-15.3222 (develop under complete). **Match.** (Note: CRRA utility is negative for γ>1, so V_veto > V_develop means -15.32 > -15.53, i.e., veto is preferred.)

5. **Catastrophe magnitudes** (paper line 267): "consumption halves under the large singularity (φ(1+η)=0.5) and falls by 25% under the baseline (φ(1+η)=0.75)." Code: φ_large*(1+9)=0.05*10=0.5, φ*(1+0.5)=0.5*1.5=0.75. **Match.**

6. **φ^{-γ} = 160,000** (paper line 269): Code: 0.05^(-4) = 160,000. **Match.**

### Per-share data handling (Requirement 5)

Not applicable. The empirical exhibit uses index-level data (S&P 500 index from Shiller, NASDAQ Composite from FRED). The NASDAQ/S&P ratio is a price-index ratio, not a per-share construction. No share counts are combined across sources.

### Code structure

The script is logically organized into four sections: (1) P/D table computation with exact backward recursion, (2) extension figure with transfers, (3) empirical valuation figure, (4) veto example computation. Each section corresponds to a distinct paper exhibit or in-text claim. The exact backward recursion (for AI P/D) vs. closed-form approximation (for non-AI P/D) distinction matches the paper's discussion in lines 155-157.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` | **Locally reproducible** — pure computation, no external data needed |
| `fig-extension-panels.pdf` | **Locally reproducible** — pure computation |
| `fig-ai-valuations.pdf` | **Reproducible with network access** — requires downloads from datahub.io and FRED |
| Veto example (console output) | **Locally reproducible** — pure computation, values printed to console and referenced in-text |

No violations found.

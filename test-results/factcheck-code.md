# tests/factcheck-code.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260404T235928.973022-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.973022-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path is coherent, from-scratch, and consistent with all paper claims; the only execution blocker is WRDS credentials, which the spec permits as an external download.

## Canonical local analysis path

Single entry point: `code/run-all.R` (run via `Rscript code/run-all.R`).

Generates three exhibits in dependency order:
1. `paper/exhibits/fig-opening.pdf` — Opening figure (Magnificent 7 market cap share from CRSP via WRDS)
2. `paper/exhibits/table-pd-ratios.tex` — Table of P/D ratios vs singularity probability
3. `paper/exhibits/fig-transfers.pdf` — P/D of AI stocks vs output growth under transfers

All three files are referenced in `paper/paper.tex` and no other files exist in `paper/exhibits/`. The code outputs directly to `paper/exhibits/` as required by the spec.

## Execution status

| Component | Status |
|---|---|
| R runtime | Available (`/usr/bin/Rscript`) |
| Required packages (`DBI`, `RPostgres`) | Installed |
| Exhibit 1 (opening figure) | **Blocked by credentials**: requires `WRDS_USERNAME` env var and network access to `wrds-pgdata.wharton.upenn.edu:9737` |
| Exhibit 2 (P/D table) | Pure computation, no external dependency — executable |
| Exhibit 3 (transfer figure) | Pure computation, no external dependency — executable |

The spec explicitly allows external data downloads (III.3.d: "executes in less than 180 seconds, including any external data download"), so the WRDS dependency is compatible with the spec. The pipeline runs from scratch and does not rely on precomputed caches or intermediate files (spec III.3.c).

## Paper-code consistency

**Parameters.** The paper states baseline parameters β=0.96, g=0.02, γ=3, α=0.15, α_S=0.50. Code lines 107–111 match exactly.

**Table (Exhibit 2).** Panel A uses G=5, φ=0.5, Λ=2.5; Panel B uses G=2, φ=0.6, Λ=0.8. Code lines 136–146 match. The generated table values match every number cited in the paper's prose:
- "spread of 2.1" at p=0.05 in Panel A → table: 2.1 ✓
- "rising from 11.9 to 41.6" for AI stocks in Panel B → table: 11.9, 41.6 ✓
- "spread exceeds 30 at p=0.10" → table: 30.2 ✓

**Transfer figure (Exhibit 3).** Paper caption states θ=1, φ=0.50, p=0.05. Code lines 189–190 use `phi_fig=0.50`, `p_fig=0.05`. The transfer formula Λ(θ,δ) = [(1−φ) + (1−δ)θφ]G from eq. (10) is correctly implemented: `(1 - delta * phi_fig) * G_range` (line 205), with the no-transfer case `(1 - phi_fig) * G_range` (line 203) equivalent to δ=1. V₀ and V∞ reference lines are included.

**Opening figure (Exhibit 1).** CRSP query covers Jan 2015–Dec 2024, common stocks (shrcd 10,11) on NYSE/AMEX/NASDAQ (exchcd 1,2,3), consistent with the figure caption. Magnificent 7 identified by 8 permnos (Alphabet has two share classes).

**Model formulas.** The code implements Proposition 1's P/D formula: `pd_ratio = (1 - H) * V0(p) + H * V_inf`, with `V0(p) = (1-p)*R / (1-(1-p)*R)`, `V_inf = R/(1-R)`, and `H = (share_S/share) * Lambda^(1-gamma)`. All match equations (6)–(8) in the paper.

**Per-share data handling (Requirement 5).** The CRSP query computes market cap as `ABS(prc) * shrout`, both drawn from `crsp.msf` (same source, same date, same split adjustment). No cross-source combination of per-share quantities. The ratio AI_mcap/total_mcap is unit-free, so the thousands-of-dollars convention in `shrout` cancels.

## Reproducibility classification

| Paper object | Classification |
|---|---|
| Table 1 (P/D ratios) | **Locally reproducible** — pure computation from hardcoded parameters |
| Figure 2 (transfers) | **Locally reproducible** — pure computation from hardcoded parameters |
| Figure 1 (opening figure) | **Blocked by credentials/network** — requires WRDS access; compatible with spec |
| Propositions 1–6, Corollaries | **Locally reproducible** — closed-form, verified against code outputs |
| All prose quantitative claims | **Locally reproducible** — verified against generated table |

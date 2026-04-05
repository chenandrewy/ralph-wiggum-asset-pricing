# tests/factcheck-code.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 1m 15s
[ralph-garage/agent-logs/20260404T232545.923302-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.923302-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces both exhibits, and all paper claims match the code output.

## Canonical local analysis path

- **Entry point:** `code/run-all.R` (single canonical script).
- **Outputs:** `paper/exhibits/table-pd-ratios.tex` (Exhibit 1) and `paper/exhibits/fig-transfers.pdf` (Exhibit 2).
- **Dependencies:** Base R only; no external packages, no data downloads, no credentials, no network access.
- **Parameters:** All defined inline in the script. No external config files or caches.

The pipeline matches spec requirement III.3: R code, single entry point, runs from scratch, outputs directly to `paper/exhibits/`, and all files in `paper/exhibits/` are used in the paper.

## Execution status

| Check | Result |
|---|---|
| R available in environment | Yes (R 4.2.2) |
| `Rscript code/run-all.R` succeeds | Yes |
| Runtime | < 2 seconds (well under 180s limit) |
| Outputs regenerated identically | Yes |
| No precomputed caches required | Confirmed |
| No network access required | Confirmed |

**Classification:** Fully executable from scratch in this environment. No execution blockers.

## Paper-code consistency

### Exhibit 1: Table (P/D ratios vs singularity probability)

- **Code parameters:** beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50.
- **Panel A:** G=5, phi=0.50, Lambda=2.5. Panel B: G=2, phi=0.60, Lambda=0.8.
- **Paper text (Section 3.2):** States "baseline parameterization: beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50" -- matches code.
- Paper claims "a 5% annual singularity probability produces a P/D spread of 2.1" -- table shows 2.1 at p=0.05 Panel A. **Consistent.**
- Paper claims "AI stocks' P/D ratio now increases with p, rising from 11.9 to 41.6" -- table shows 11.9 (p=0) to 41.6 (p=0.10) in Panel B. **Consistent.**
- Paper claims "The spread exceeds 30 at p=0.10" -- table shows 30.2. **Consistent.**

### Exhibit 2: Figure (P/D vs output growth and deadweight costs)

- **Code parameters:** phi=0.50, p=0.05, G range 1.5-20, delta in {1.0, 0.9, 0.5, 0.0}, tau=1.
- **Paper figure notes:** States beta=0.96, g=0.02, gamma=3, alpha=0.15, alpha_S=0.50, phi=0.50, p=0.05, tau=1 -- matches code.
- Transfer formula in code: `Lambda = (1 - delta*phi)*G` for delta < 1, `Lambda = (1-phi)*G` for delta=1.0 (no transfers). This matches equation (8): Lambda(tau,delta) = [(1-phi) + (1-delta)*tau*phi]*G evaluated at tau=1: = [1 - delta*phi]*G. **Consistent.**

### Formula verification

The code implements Proposition 1 exactly:
- `R_val = beta * (1+g)^(1-gamma)` matches R = beta*(1+g)^{1-gamma}.
- `V_inf = R/(1-R)` matches V_inf.
- `V0(p) = (1-p)*R / (1-(1-p)*R)` matches V_0.
- `H_func(share_S, share, Lambda) = (share_S/share) * Lambda^(1-gamma)` matches H^i.
- `pd_ratio(p, H) = (1-H)*V0(p) + H*V_inf` matches P/D formula.

All formulas are correctly implemented. **No mismatches found.**

## Reproducibility classification

| Paper object | Classification |
|---|---|
| Table 1 (P/D ratios) | **Locally reproducible** -- regenerated from scratch, output matches |
| Figure 1 (transfers) | **Locally reproducible** -- regenerated from scratch, output produced |
| Proposition 1 (P/D formula) | Code correctly implements; table values verify |
| Corollary 1 (hedging premium) | Spread column in table verifies formula |
| Proposition 2 (incomplete markets amplification) | Not computed in code (purely algebraic result); consistent with model |
| Proposition 3 (veto) | Qualitative result; no code needed |
| Proposition 4 (extinction risk) | Algebraic extension; no code needed |
| All inline numerical claims in Section 3.2 | **Consistent** with generated table |

## Violations found

None.

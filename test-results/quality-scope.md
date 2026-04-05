# tests/quality-scope.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 24s
[ralph-garage/agent-logs/20260404T232545.923480-0400_quality-scope_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.923480-0400_quality-scope_claude_opus.log)

# quality-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative parameterizations, no empirical estimation, and no broad prediction menus.

## Findings

**Theoretical core.** The paper develops a single closed-form model (Proposition 1) with one key mechanism — displacement risk under incomplete markets drives a hedging premium for AI stocks. The result set is tight: four propositions and one corollary, all flowing directly from the baseline setup.

**Quantitative material is illustrative, not calibrated.** Section 3.3 presents one table of P/D ratios across parameter scenarios. The conclusion explicitly states: "We … rely on illustrative parameterizations rather than formal calibration." There is no regression, no empirical estimation, no moment-matching, and no data beyond the model's own output.

**No broad prediction menu.** The paper does not enumerate a long list of testable implications or empirical predictions. The extensions (government transfers, deployment efficiency, extinction risk) each modify one dimension of the baseline and deliver one clean comparative-static result.

**Exhibits are minimal.** Two exhibits total: one table (P/D ratios under varying singularity probability) and one figure (P/D as a function of output growth and deadweight costs). Both serve to illustrate magnitudes, not to present empirical evidence.

**Self-awareness of scope.** The conclusion (lines 302–303) explicitly acknowledges the intentionally compact scope: "We model the singularity as a single binary event, abstract from many realistic frictions, and rely on illustrative parameterizations rather than formal calibration."

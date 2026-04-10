# tests/factcheck-theory.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 6m 26s
[ralph-garage/agent-logs/20260409T212047.318484-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.318484-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

23 symbol families were cataloged. No collisions, ambiguities, or reuse of symbols for different formal objects were found. All subscript/superscript conventions (time indexing with $t$, agent/asset type with superscripts $H$, $AI$, $N$, $j$) are stable throughout the paper.

One minor note: the proof of Proposition 3 (line 213) refers to "$u$ is concave" without formally defining $u$ as the per-period utility function — the CRRA formula is written directly in Eq (3). The meaning is unambiguous, but strictly this introduces a symbol without definition. This is a definitional gap in prose, not a notational inconsistency or collision.

## Requirement 2: Assumptions Consistency — PASS

22 mathematical assumptions were identified across Sections 2.1, 2.2, 3, 4.1, and 4.2. 16 specific consistency checks were performed:

- **Parameter ranges:** All parameterized values ($\beta = 0.96$, $g = 0.02$, $\gamma = 4$, $\phi = 0.5$, $\eta = 0.5$, $\theta = 0.15$, $\Delta\theta = 0.2$, etc.) fall within their stated constraints.
- **Structural consistency:** Dividend shares ($\theta_t$, $1 - \theta_t$) and consumption shares ($\alpha_t$, $1 - \alpha_t$) sum to 1 and remain in valid ranges after singularity events.
- **Existence conditions:** The baseline calibration satisfies $A^j < 1$; the large-singularity calibration ($\eta = 9$, $\phi = 0.05$) violates it at $\tau = 0$, exactly as claimed.
- **CRRA sign convention:** With $\gamma > 1$, CRRA utility $c^{1-\gamma}/(1-\gamma) < 0$ for all $c > 0$, consistent with the extinction normalization $U_{\text{ext}} = 0$.
- **Transfer formula:** Eq (8), the effective displacement $\phi_{\text{eff}}$, and the transfer ratio Eq (9) are algebraically consistent with each other.
- **Extensions vs baseline:** Extension 1 augments the baseline singularity structure (adding a positive singularity branch) without contradicting it. Extension 2 modifies household consumption via transfers without contradiction.
- **Code vs paper:** All parameter values match exactly.

No contradictions or parameter range violations found.

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to primitive assumptions:

| Derived Object | Traced To |
|---|---|
| $\Gamma^{AI}$, $\Gamma^{N}$ | $\theta$, $\Delta\theta$, $\eta$ (assumptions A9, A10, A5) |
| $A^j$ (existence condition) | $\beta$, $g$, $\gamma$, $p$, $\xi$, $\eta$, $\phi$, $\Gamma^j$ (A2, A4–A7, A12, A13) |
| $P^{AI}/D^{AI}$, $P^N/D^N$ | Euler equation from CRRA preferences (A12) + asset structure (A9–A11) + singularity dynamics (A4–A8) |
| $v^{AI}$ | Equals $P^{AI}/D^{AI}$; used in Appendix A proof |
| $c^H_{post}$ | $\phi$, $\alpha$, $\eta$, $C_t$, $g$, $\tau$, $\delta$ (A2, A3, A5, A6, A18, A19) |
| $\phi_{\text{eff}}$ | $\phi$, $\tau$, $\delta$, $\alpha$ (A6, A18, A19, A3) |
| $U_0^H$ | $\beta$, $\gamma$, $c_t^H$ (A12, A3) |
| $U_{\text{ext}}$ | Normalized to 0 (A17) |

No orphaned mathematical objects found. Every expression in the paper can be logically derived from the stated assumptions.

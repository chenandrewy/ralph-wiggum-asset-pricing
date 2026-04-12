# tests/theory-clarity.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 2m 22s
[ralph-garage/agent-logs/20260412T154740.749786-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.749786-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Model assumptions are clearly organized in labeled setup paragraphs with most critical expressions in display math; minor gaps (AI share dynamics inline, q>1/2 at paragraph end) do not impede comprehension.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth: $C_{t+1} = (1+g)C_t$ — eq (1)
2. Displacement rule: $\alpha_{t+1} = \phi\alpha_t$ — eq (2)
3. CRRA utility — eq (3)
4. P/D ratio formulas — eqs (4)–(5) in Proposition 1
5. Post-transfer consumption — eq (6)
6. Effective displacement $\phi_\text{eff}$ — eq (7)
7. Transfer ratio — eq (8)

### In prose, properly positioned
- Singularity probability $p$: opens the Singularity paragraph
- Market incompleteness (cannot trade restricted equity): opens its own paragraph
- $\gamma > 1$: opens the Preferences paragraph
- Veto cost $\kappa > 0$: near start of its paragraph
- Complete-markets consumption $\alpha(1+\eta)C_t(1+g)$: opens its paragraph
- Tax rate $\tau$ and deadweight cost $\delta\tau$: near start of modeling paragraph

### Minor gaps (not sufficient to fail)
- AI share dynamics $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$: inline in a bullet item rather than display math, despite driving the $\Gamma^{AI} > \Gamma^{N}$ comparison
- $q > 1/2$ assumption: appears as the last sentence of its paragraph rather than near the start
- $c_t^H = \alpha_t C_t$: inline after eq (1) rather than displayed, though the placement is natural

## Section-level findings

**Section 2 (Model):** Well-structured with \paragraph headers (Consumption, Singularity, Assets, Preferences). All core expressions are displayed. The $\alpha$-vs-$\theta$ distinction is explained in a dedicated paragraph. The AI share dynamics ($\theta$ law of motion) is the one expression that could benefit from display math given its importance to Proposition 1.

**Section 2.2 (Equilibrium prices):** P/D ratios properly displayed inside Proposition 1. The discussion paragraphs clearly explain $\Gamma^{AI}$ vs $\Gamma^{N}$ and the hedging channel.

**Section 2.3 (Discussion):** Recalls earlier assumptions appropriately; no new model assumptions introduced.

**Section 3 (Quantitative Analysis):** Parameterization clearly stated in prose. No new model assumptions.

**Section 4.1 (Veto and efficient development):** New setup (positive singularity, $q$, $\kappa$, complete markets) is introduced in dedicated paragraphs. The $q > 1/2$ assumption could be moved earlier in its paragraph. $\Delta u(\gamma)$ appears in display math inside the proof, which is appropriate since it is a proof expression rather than a model assumption.

**Section 4.2 (Government transfers):** Transfer mechanism clearly set up with $\tau$, $\delta$, and the consumption formula in display math. $\phi_\text{eff}$ is displayed. The section flows well from setup to results.

# dev/qf/qf-redundancy.py
Started: 2026-03-28 14:44:57 EDT
Runtime: 1m 46s
[ralph-garage/agent-logs/20260328T144457.274134-0400_qf-redundancy_claude_opus.log](../../ralph-garage/agent-logs/20260328T144457.274134-0400_qf-redundancy_claude_opus.log)

# qf-redundancy
VERDICT: FAIL
REASON: Corollary 2 is formally redundant with Corollary 1, and Equation (7) is compressible into prose.

## Finding 1: Corollary 2 (Two-type marginal investors) duplicates Corollary 1

**Economic point.** If the marginal investor has less access to private AI capital (lower phi), the hedging premium is larger. Retail investors (phi^R < phi^W) produce a higher P/D ratio than wealthy investors.

**Where the same point is already made.** Corollary 1 establishes that lower phi implies a higher price-dividend ratio, with proof via the chain d(Delta)/d(phi) < 0 and d(Lambda)/d(Delta) > 0. Corollary 2's proof is identical: it applies the same monotonicity to phi^R < phi^W instead of phi_j < phi_k. The formal mechanism (plugging two different phi values into the same formula and comparing) is the same in both results.

**Is a separate formal statement justified?** The economic reinterpretation (firm-level phi variation vs. investor-type phi variation) is worth discussing, but the formal content adds nothing beyond Corollary 1. The surrounding prose on VSL heterogeneity and the quantitative offset between the phi and q channels is valuable---but that discussion does not require its own corollary. The result could be stated as: "Corollary 1 applies equally to investor types: if the marginal investor shifts from wealthy (high phi) to retail (low phi), the premium rises." One sentence, no proof needed.

## Finding 2: Equation (7) is compressible into prose

**Economic point.** The singularity is negative for the household when displacement of non-AI output outweighs the gain from public AI dividends. A sufficient condition is d/a > phi * s / (1 - s). When phi is small, this is easily satisfied.

**Where the same point is already made.** Equation (6) defines Delta exactly. The condition Delta > 0 can be checked directly from (6). Equation (7) is a first-order Taylor approximation that linearizes the same condition. The sentence immediately following Equation (7) restates the economic content in plain English: "When most AI capital is private (phi small), this condition is easily satisfied."

**Is a separate equation justified?** The linearized condition is mildly useful as a quick interpretive device, but the prose already delivers the same intuition. This is a case where a displayed equation could be replaced by an inline remark ("to first order, the condition requires d/a > phi * s / (1-s), which is easily satisfied when phi is small") without weakening any economic claim.

## Other formal objects reviewed but not flagged

- **Remark 1 (Absorption of displacement risk):** Interpretive content in a formal environment. Borderline compressible, but Remarks are explicitly low-formalism and the GKP contrast is worth flagging for the reader. Retained.
- **Equation (5) (HH consumption growth in singularity):** A rewriting of (4) in growth-rate form that bridges to the Delta definition (6). Technically intermediate, but the growth-rate representation is the natural language of the asset pricing literature and earns its place.
- **Proposition 2 (Complete markets benchmark):** Establishes the sign reversal of the hedging channel under complete markets---a genuinely new result that is central to the paper's argument. Not redundant.
- **Corollary 3 (Non-monotone hedging premium):** Combines endogenous phi resolution with Proposition 2's sign reversal. New economic content.
- **Proposition 3 (Extinction bound):** New result bounding the premium via extinction risk. Not redundant with any other formal object.

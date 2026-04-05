# Improvement Plan
AUTHOR PLAN — 2026-04-04 23:38:05 EDT

## Current State

**Tests: 16/21 pass, 5 fail.** No overhaul needed — the model section is sound (correct derivations, clean structure, good economic logic). The issues are fixable without restructuring.

## Failing Tests

| Test | Issue |
|------|-------|
| `element-opening-fig` | No figure in the introduction. Spec requires an empirical CRSP figure showing AI vs non-AI valuations. |
| `element-rhetoric-meta` | Abstract's final sentence ("written entirely by AI agents") is too blunt; triggers reader aversion before they engage with the economics. |
| `factcheck-theory` | Symbol collision: `τ` used for both singularity arrival time (§2) and tax rate (§4.1). |
| `quality-writing` | Monotonous rhythm, weak paragraph transitions, extensions read as a laundry list, tone too academic. |
| `spec-paper` | Three sub-failures: (1) paper never argues financial market solutions are "under-discussed" (spec I.3c), (2) appendix has unnumbered display equations (spec II.9), (3) theorem environment comments use wrong compiled numbers (spec III.2c). |

## Plan

### Step 1: Code — Add CRSP opening figure

Create an R script addition in `code/run-all.R` (or a sourced helper) that:
- Downloads CRSP market-cap data for AI vs non-AI stocks (use code templates in `ralph/code-templates/` for WRDS access patterns).
- Computes a valuation ratio (e.g., aggregate P/D or market-cap-weighted P/E) for an AI portfolio vs a non-AI portfolio over recent years.
- Outputs `paper/exhibits/fig-opening.pdf`.

If WRDS access is unavailable or too slow, use a simple illustrative figure with publicly available data (e.g., Magnificent 7 vs S&P 500 equal-weight P/E).

### Step 2: Paper — Fix notation collision

Rename the tax rate from `τ` to `t` or `\theta` in §4.1 (equation 8 and surrounding text). Keep `τ` exclusively for the singularity arrival time.

### Step 3: Paper — Fix appendix equation numbering

Replace all `\[ ... \]` and `align*` environments in the appendix with `\begin{equation}` or `\begin{align}` (numbered). This fixes spec II.9.

### Step 4: Paper — Fix theorem environment comments

The shared counter means Definition 1, Proposition 1, Corollary 1 compile as 1, 2, 3, etc. Update comments to match compiled numbering:
- `\begin{definition}` → `% Definition 1`
- First `\begin{proposition}` → `% Proposition 2`
- `\begin{corollary}` → `% Corollary 3`
- Subsequent propositions → `% Proposition 4`, `% Proposition 5`, `% Proposition 6`

### Step 5: Paper — Add "under-discussed" argument (spec I.3c)

In the introduction or the opening of §4.1, add a sentence arguing that financial market solutions to AI disaster risk are under-discussed relative to the attention given to regulation and alignment. This is a natural claim — the literature focuses on AI safety, labor displacement, and regulation, while financial hedging gets little attention.

### Step 6: Paper — Soften the abstract's AI-agent sentence

Remove or substantially soften the abstract's final sentence. Options:
- Delete it from the abstract entirely, letting the introduction carry the rhetorical weight.
- Replace with something integrated: e.g., "We illustrate the displacement mechanism by noting that this paper's analysis was itself produced by AI agents."

The introduction's treatment of the device is already good — the problem is only the abstract.

### Step 7: Paper — Improve writing quality

Target the specific issues flagged by `quality-writing`:
1. **Introduction paragraph 3 (formalization):** Break into two shorter paragraphs. Add a bridge question before the quantitative paragraph (e.g., "How large are these effects?").
2. **Introduction paragraph 5 (extensions):** Rewrite as a narrative arc, not a list. Connect each extension to the previous one with motivation.
3. **Transitions in the model/results sections:** Add bridge sentences at the end of interpretation paragraphs that motivate the next subsection.
4. **Tone:** Add 2–3 rhetorical questions or direct-address moments. Vary sentence length — use short punchy sentences for emphasis after key results.
5. **Extensions opener:** Replace the flat roadmap sentence with a hook that motivates why the baseline model leaves important questions open.

### Step 8: Paper — Add opening figure to introduction

Insert the CRSP figure (from Step 1) into the introduction, before or after the first paragraph. Add 1–2 sentences of context: "Figure X shows..." This fixes `element-opening-fig`.

## Priority Order

Steps 1–6 fix failing tests directly. Step 7 addresses writing quality. Step 8 integrates the new figure. Execute in roughly this order, but Steps 2–6 can be done in parallel as they touch different parts of the paper.

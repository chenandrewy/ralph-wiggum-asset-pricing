# tests/spec-paper.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 3m 14s
[ralph-garage/agent-logs/20260404T232545.921084-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260404T232545.921084-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper

VERDICT: FAIL
REASON: Three sub-requirements fail across all three audited sections (I.3c, II.9, III.2c).

---

## I. Economic Requirements

**Section verdict: FAIL**
**Reason:** Requirement 3c is not satisfied — the paper never argues that financial market solutions to AI disaster risk are "under-discussed."

### Requirement 1 — Academic asset pricing theory paper
**PASS.** The paper has formal propositions, proofs, CRRA utility, Euler equations, SDFs, and P/D ratios targeting a finance audience.

### Requirement 2a — AI singularity definition used consistently
**PASS.** "An AI singularity---a sudden, dramatic improvement in AI capability---would vastly increase total economic output." (Introduction) and "Total output jumps by factor $G > 1$" (Section 2).

### Requirement 2b — Negative AI singularity definition used consistently
**PASS.** "When $\Lambda < 1$---a *negative* AI singularity---the household's consumption falls despite a massive increase in total output." (Section 2)

### Requirement 2c — Incomplete markets definition used consistently
**PASS.** "The household cannot trade the private AI capital held by AI owners. This is the key friction." (Section 2). Consistently refers to non-tradability, not Arrow-Debreu.

### Requirement 3a — Main argument (hedging premium)
**PASS.** Abstract: "AI stocks may command high valuations partly because they hedge against a devastating AI singularity."

### Requirement 3b — Incomplete markets are key
**PASS.** Proposition 2 shows the premium is amplified under incomplete markets. Paper states under complete markets the household "could insure against displacement."

### Requirement 3c — Financial market solutions are under-discussed
**FAIL.** The paper discusses government transfers as a solution and notes deadweight costs, but never makes the claim that financial market solutions to AI disaster risk are "under-discussed" in the literature or public discourse.

### Requirement 3d — Singularity abundance overcomes frictions
**PASS.** "if AI produces the kind of explosive output growth studied by Jones (2024)---potentially infinite---then even transfers that waste 90% of their value can dramatically reduce displacement risk."

### Requirement 3e — Incomplete markets distort AI deployment
**PASS.** "Market incompleteness affects not only valuations but also real decisions." Extension 2 shows the household may veto the singularity under incomplete markets but never under complete markets.

### Requirement 4a — Infinite-horizon, discrete-time model
**PASS.** "Time is discrete, $t = 0, 1, 2, \ldots$" and utility $E_0 \sum_{t=0}^{\infty} \beta^t \frac{C_t^{1-\gamma}}{1-\gamma}$.

### Requirement 4b — Two agents
**PASS.** "The economy is populated by a representative household and a group of AI capital owners." Household is marginal investor; AI owners "are not marginal investors in the public stock market."

### Requirement 4c — Two publicly traded assets
**PASS.** "Two assets are publicly traded: AI stocks... and Non-AI stocks." AI share increases from $\alpha$ to $\alpha_S > \alpha$ post-singularity.

### Requirement 4d — Unborn capital interpretation (GKP)
**PASS.** "This capital can be interpreted as capital that does not yet exist---representing future AI breakthroughs and the claims of their creators---analogous to the unborn innovators in Garleanu, Kogan, and Panageas (2012)."

### Requirement 4e — Quantitative table of P/D ratios vs. singularity probability
**PASS.** Table 1 reports P/D ratios across singularity probabilities and displacement severities, with spreads exceeding 30 at $p=0.10$.

### Requirement 5 (preamble) — Extensions branch independently
**PASS.** "Each extension modifies the baseline model along a single dimension. The extensions are independent of one another."

### Requirement 5a (i–iv) — Extension 1: Government transfers
**PASS.** All four sub-requirements satisfied: broader trading impossible for unborn capital (citing GKP), deadweight costs make transfers unattractive normally, singularity-level growth justifies them, and Figure 1 illustrates the P/D dependence on growth and deadweight costs.

### Requirement 5b (i–iii) — Extension 2: Deployment efficiency
**PASS.** Household can veto at cost $\kappa C_t$; Proposition 3(a) shows no veto under complete markets; informal argument ties Extension 1's abundance logic to restoring efficient deployment.

### Requirement 5c — Extension 3: Extinction risk
**PASS.** Proposition 4 derives that the P/D spread is strictly decreasing in extinction probability $q$, with explicit formula.

### Requirement 6a — Contribution relative to GKP (transfers)
**PASS.** "Garleanu, Kogan, and Panageas (2012) note that government transfers would affect the magnitude of displacement but do not pursue this formally; we contribute a simple analysis with quantitative illustrations."

### Requirement 6b — Contribution relative to GKP (extensions)
**PASS.** Extensions study AI-specific singularity features while keeping economics tied to GKP's incomplete-markets logic.

### Requirement 6c — Modest characterization of contribution
**PASS.** "The main economic insights---that displacement risk is priced, that market incompleteness amplifies its effects, and that certain assets offer a hedge---are already present in their work."

---

## II. Style Requirements

**Section verdict: FAIL**
**Reason:** Requirement 9 is not satisfied — the appendix contains five unnumbered display equations.

### Requirement 1 — Tone between academic paper and blog post
**PASS.** Uses accessible phrasing ("The logic is straightforward," "Two patterns emerge") alongside formal propositions and proofs.

### Requirement 2 — Author is anonymous
**PASS.** `\author{}` is empty (line 22).

### Requirement 3 — Abstract is 100 words or less
**PASS.** Abstract is approximately 91 words.

### Requirement 4 — Title is short, evocative, eye-catching, not cringey
**PASS.** Title is "Hedging the Singularity" — three words, evocative.

### Requirement 5 — Paper length at most 20 pages
**CANNOT FULLY VERIFY** without compiling. The paper uses 12pt, 1-inch margins, onehalfspacing, ~350 lines of content, 2 exhibits, and a short appendix. Very likely under 20 pages.

### Requirement 6 — Every page has a visible page number
**PASS.** `\pagestyle{plain}` (line 14) and `\thispagestyle{plain}` (line 27) ensure page numbers on all pages including the title page.

### Requirement 7 — At most 6 exhibits
**PASS.** Exactly 2 exhibits: Table 1 and Figure 1.

### Requirement 8 — Lit review at most half a page, at end of introduction
**PASS.** `\paragraph{Related literature.}` appears at the end of the Introduction, spanning approximately two short paragraphs.

### Requirement 9 — All display equations should be numbered
**FAIL.** The appendix contains five unnumbered display equations:
- Three instances of `\[ ... \]` (lines ~320, ~325, ~343)
- One `\begin{align*}` block (lines ~331–336)
- One additional `\[ ... \]` (lines ~347–349)

### Requirement 10 — All propositions explicitly proved, long proofs in appendix
**PASS.** All propositions have explicit proofs. Propositions 1 and 3 have proofs in Appendix A; others have inline proofs.

### Requirement 11 — First section is "Preface (TBC)", unnumbered, blank
**PASS.** `\section*{Preface (TBC)}` on line 36 is unnumbered and blank. `\section{Introduction}` follows on line 41.

---

## III. Technical Requirements

**Section verdict: FAIL**
**Reason:** Requirement 2c is not satisfied — theorem environment comments do not match compiled numbering.

### Requirement 1a — `paper.tex` is the main paper file
**PASS.** `/workspace/paper/paper.tex` exists and contains the full document.

### Requirement 1b — All figures/tables sourced from `paper/exhibits/`
**PASS.** `\input{exhibits/table-pd-ratios}` (line 211) and `\includegraphics[...]{exhibits/fig-transfers.pdf}` (line 245). Both reference `exhibits/`.

### Requirement 1d — All files in `paper/exhibits/` are used in the paper
**PASS.** `paper/exhibits/` contains exactly `table-pd-ratios.tex` and `fig-transfers.pdf`, both referenced in the paper.

### Requirement 2a — Section comments list section numbers
**PASS.** Every `\section` and `\subsection` has a comment with its number (e.g., `% Section 1`, `% Section 4.2`).

### Requirement 2b — Exhibit comments list exhibit numbers
**PASS.** `% Exhibit 1` before Table 1 and `% Exhibit 2` before Figure 1.

### Requirement 2c — Theorem environment comments list environment numbers
**FAIL.** All theorem-like environments (Definition, Proposition, Corollary) share a single LaTeX counter (`\newtheorem{corollary}[proposition]{Corollary}`, `\newtheorem{definition}[proposition]{Definition}`). The comments use per-type numbering:
- Line 129: `\begin{definition}` labeled `% Proposition 1` — wrong type name and wrong compiled number (should be Definition 1)
- Line 148: `\begin{proposition}` labeled `% Proposition 1` — compiled number will be 2
- Line 170: `\begin{corollary}` labeled `% Corollary 1` — compiled number will be 3
- Lines 188, 262, 282: Propositions labeled 2, 3, 4 — compiled numbers will be 4, 5, 6

The comments do not match the compiled numbering.

### Requirement 3a — Code is written in R
**PASS.** `/workspace/code/run-all.R` is the sole script, written in R.

### Requirement 3b — One canonical entry point regenerates every exhibit
**PASS.** `run-all.R` generates both `table-pd-ratios.tex` and `fig-transfers.pdf`.

### Requirement 3c — Pipeline runs from scratch, no precomputed caches
**PASS.** Script defines all parameters inline and computes everything from formulas; reads no external data or intermediate files.

### Requirement 3d — Pipeline executes in less than 180 seconds
**PASS.** Script performs simple arithmetic and generates one table and one PDF. Execution is well under 5 seconds.

### Requirement 3e — Code outputs directly to `paper/exhibits/`
**PASS.** `writeLines(tex, "paper/exhibits/table-pd-ratios.tex")` and `pdf("paper/exhibits/fig-transfers.pdf", ...)`.

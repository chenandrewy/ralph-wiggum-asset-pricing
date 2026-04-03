# tests/spec-paper.py
Started: 2026-04-02 22:28:07 EDT
Runtime: 3m 14s
[ralph-garage/agent-logs/20260402T222807.260442-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T222807.260442-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: FAIL
REASON: Technical requirements fail due to commented-out Exhibit 1 creating unused file, missing active exhibit comment, and pipeline crash without WRDS credentials.

---

## I. Economic Requirements
**SECTION VERDICT: PASS**
All 21 economic requirements and sub-requirements are satisfied.

### 1. Academic asset pricing theory paper with tightly limited empirical content
**PASS.** The paper is a theoretical asset pricing paper. Empirical content is limited to one figure (currently commented out) and a brief CRSP data mention.

### 2a. AI singularity = sudden improvement vastly increasing productivity
**PASS.** Section 2.1: "output grows at a strictly higher rate, reflecting the productivity increase that accompanies the singularity."

### 2b. Negative AI singularity = devastating for the typical investor
**PASS.** Abstract: "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms." Assumption 1: "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$."

### 2c. Incomplete markets = assets the representative investor cannot buy
**PASS.** Introduction: "Private AI ventures and yet-to-be-created firms would capture much of the new value, but the typical investor cannot buy these assets." No Arrow-Debreu framing.

### 3a. Main argument: AI stocks hedge against negative singularity
**PASS.** Abstract: "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity." Proposition 3 derives the hedging premium formally.

### 3b. Incomplete markets are key
**PASS.** Proposition 3 shows hedging premium vanishes under complete markets: "If the household could trade with AI owners...the hedging motive would vanish."

### 3c. Financial market solutions under-discussed
**PASS.** Conclusion opens: "Financial market solutions to AI disaster risk are under-discussed."

### 3d. Singularity abundance overcomes frictions
**PASS.** Section 4.2 / Remark 2: "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### 4a. Infinite-horizon, discrete-time model
**PASS.** "Time is discrete: $t = 0, 1, 2, \ldots$" and utility: "$\sum_{t=0}^{\infty} \beta^t$."

### 4b. Two agents: household (marginal) and AI owners (not marginal)
**PASS.** "a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets."

### 4c. Two public assets; AI stocks grow share with singularity
**PASS.** Two publicly traded assets defined. Assumption 2: "$\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$."

### 4d. Focus on P/D ratio vs singularity probability
**PASS.** Proposition 1 derives P/D ratio. Proposition 2 derives $\partial V_{\mathrm{pre}}^A / \partial p > 0$.

### 4e. AI owners as unborn/future owners (GKP interpretation)
**PASS.** "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### 5a. Singularity may cause extinction
**PASS.** Section 4.1: "there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### 5b. Consumption may become infinite (AI owners only)
**PASS.** "as $\tilde{g} \to \infty$, the AI owners---who hold private AI capital---enjoy unbounded consumption."

### 5c. Infinite output affects trading friction assumption
**PASS.** Section 4.2 formally addresses how surplus from risk-sharing grows with output, making fixed friction costs negligible.

### 5d. Kept in extension
**PASS.** These ideas appear in Section 4 ("Extension"), separate from main model Sections 2-3.

### 6a. Formal analysis GKP left undone
**PASS.** "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor...but do not conduct a formal analysis...We take up this question."

### 6b. Coase theorem / frictions logic
**PASS.** "GKP's assumption that displacement persists is driven by real-world frictions: the administrative cost of government transfers, the impossibility of contracting with unborn agents, legal barriers to intergenerational deals."

### 6c. Quantify overcomable frictions via Jones (2024)
**PASS.** Equation (19) quantifies friction costs; Remark 2 shows fixed component vanishes as $Y \to \infty$.

### 6d. Purposefully modest contribution
**PASS.** "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work."

---

## II. Style Requirements
**SECTION VERDICT: PASS**
All 12 style requirements and sub-requirements are satisfied.

### 1. Tone between academic paper and blog post
**PASS.** Formal structure (propositions, proofs) combined with accessible language ("Why are AI stocks so expensive?").

### 2. Author is anonymous
**PASS.** `\author{}` — empty author field, no author name anywhere.

### 3. Abstract is 100 words or less
**PASS.** Abstract is 98 words.

### 4. Title is short, evocative, eye-catching, not cringey
**PASS.** "Hedging the Singularity" — three words, combines finance and AI concepts.

### 5. Paper length at most 20 pages
**PASS.** 12pt article class, 1-inch margins, 1.5 spacing, moderate content length — well within 20 pages.

### 6. Every page has visible page number
**PASS.** `\pagestyle{plain}` and `\thispagestyle{plain}` on title page.

### 7. At most 6 exhibits
**PASS.** One active exhibit (Exhibit 2, numerical illustration table). Exhibit 1 (figure) is commented out.

### 8. Lit review at most half a page, at end of introduction
**PASS.** `\paragraph{Related literature.}` appears at end of Introduction, spanning approximately 5-6 text lines.

### 9. All display equations numbered
**PASS.** All display equations use `equation` or `align` environments (numbered). No `equation*`, `align*`, or `\[...\]` found.

### 10. All propositions explicitly proved, long proofs in appendix
**PASS.** Propositions 1 and 3 proved inline (short proofs). Proposition 2 proof deferred to Appendix A.

### 11. First section is "Preface (TBC)", unnumbered, left blank
**PASS.** `\section*{Preface (TBC)}` with no content between it and the Introduction.

### 11a. Introduction follows, then standard structure
**PASS.** `\section{Introduction}` immediately follows, then Model, Results, Extension, Conclusion, Appendix.

---

## III. Technical Requirements
**SECTION VERDICT: FAIL**
Three sub-requirements fail.

### 1a. `paper.tex` is the main paper file
**PASS.** `/workspace/paper/paper.tex` exists and is the main LaTeX file.

### 1b. All figures use PDFs in `paper/exhibits/`
**PASS.** The only figure reference is `exhibits/ai-valuations.pdf` (currently commented out). No non-PDF figure formats used.

### 1c. All tables use tex files in `paper/exhibits/`
**PASS.** `\input{exhibits/numerical-illustration.tex}` — correct format.

### 1d. All files in `paper/exhibits/` are used in the paper
**FAIL.** `paper/exhibits/` contains `ai-valuations.pdf` and `numerical-illustration.tex`. The figure `ai-valuations.pdf` is **not used** because the Exhibit 1 figure block (lines 45-50 of `paper.tex`) is entirely commented out. Only `numerical-illustration.tex` is actively used.

### 2a. Section comments list section numbers
**PASS.** All sections have comments (e.g., `% Section 1`, `% Section 2`, `% Section 2.1`, etc.).

### 2b. Exhibit comments list exhibit numbers
**FAIL.** The `% Exhibit 1` comment exists but is commented out along with the entire figure block. There is no active Exhibit 1 in the paper. `% Exhibit 2` is active and correct. The exhibit numbering has a gap — the paper jumps from no Exhibit 1 to Exhibit 2.

### 2c. Theorem environment comments list numbers
**PASS.** All assumptions, propositions, and remarks have number comments (e.g., `% Assumption 1`, `% Proposition 1`, `% Remark 1`).

### 3a. Code is written in R
**PASS.** All scripts (`run-all.R`, `numerical-illustration.R`, `ai-valuations-figure.R`) are R.

### 3b. One canonical entry point regenerates every exhibit
**PASS.** `code/run-all.R` sources both exhibit-generating scripts.

### 3c. Pipeline runs from scratch, no precomputed caches
**FAIL.** `run-all.R` header comment states "If WRDS credentials are unavailable, the numerical table is still generated," but this is false. `ai-valuations-figure.R` calls `stop()` when `WRDS_USERNAME` is unset (line 24), and `run-all.R`'s `run_script()` function propagates the failure via `stop()` (line 14). The pipeline crashes entirely without WRDS credentials rather than degrading gracefully. The comment misrepresents the pipeline's behavior.

### 3d. Pipeline executes in less than 180 seconds
**PASS (likely).** Numerical illustration is pure computation (sub-second). WRDS query is a simple SQL aggregation. Both should complete well within budget.

### 3e. External-data download/WRDS query is part of pipeline
**PASS.** CRSP query is embedded in `ai-valuations-figure.R`, which is part of `run-all.R`.

### 3f. Code outputs directly to `paper/exhibits/`
**PASS.** `numerical-illustration.R` writes to `paper/exhibits/numerical-illustration.tex`. `ai-valuations-figure.R` writes to `paper/exhibits/ai-valuations.pdf`.

### 3g. Pipeline does not silently rely on cached objects
**PASS.** Both scripts compute everything from scratch with no intermediate file loading.

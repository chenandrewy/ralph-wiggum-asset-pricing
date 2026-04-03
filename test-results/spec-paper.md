# tests/spec-paper.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 2m 44s
[ralph-garage/agent-logs/20260402T214942.856455-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T214942.856455-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: PASS
REASON: All requirements in Sections I (Economic), II (Style), and III (Technical) are satisfied.

## I. Economic Requirements — PASS

All 6 requirements and 20 sub-items pass.

### 1. Academic asset pricing theory paper with tightly limited empirical content — PASS
- Paper is a formal asset pricing model with propositions and proofs.
- Empirical content limited to one CRSP figure: "Figure~\ref{fig:ai-valuations} illustrates this pattern using CRSP data: the price-dividend ratio of major AI stocks has risen sharply relative to non-AI stocks."

### 2a. AI singularity defined as sudden AI-driven productivity surge — PASS
- "A singularity is an absorbing event that arrives with independent probability $p \in (0,1)$ each period" with output growth shifting from $g$ to $\tilde{g} > g$.

### 2b. Negative AI singularity devastating for typical investor — PASS
- Assumption 1: "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$" labeled "[Negative singularity]".

### 2c. Incomplete markets = some assets not buyable by representative investor — PASS
- "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital."

### 3a. Main argument: AI stocks command premium as hedge against negative singularity — PASS
- Abstract: "We show that publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity."

### 3b. Incomplete markets are key — PASS
- Proposition 4 shows complete markets eliminate the hedging premium: "If the household could trade with AI owners... the hedging motive would vanish."

### 3c. Financial market solutions under-discussed — PASS
- Conclusion: "Financial market solutions to AI disaster risk are under-discussed."

### 3d. Singularity abundance overcomes frictions — PASS
- Remark 2: "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible. In this limit, the Coase theorem applies."

### 4a. Infinite-horizon, discrete-time — PASS
- "Time is discrete: $t = 0, 1, 2, \ldots$"; utility is $E_0 \sum_{t=0}^{\infty}$.

### 4b. Two agents: household (marginal) and AI owners (not marginal, hold private capital) — PASS
- "The economy has two types of agents: a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets."

### 4c. Two publicly traded assets; AI stocks grow share at singularity — PASS
- Dividends split into AI, non-AI, and private. Assumption 2: "$\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$."

### 4d. Focus on P/D ratio of AI stocks and how it changes with p — PASS
- Proposition 1 derives the P/D ratio; Proposition 3 shows $\partial V_0^A / \partial p > 0$.

### 4e. Private AI capital / AI owners interpretable as unborn capital / future owners — PASS
- "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### 5a. Extension: singularity may cause extinction — PASS
- Section 4.1 models extinction probability $q$: "there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### 5b. Consumption may become infinite (only for AI owners) — PASS
- "as $\tilde{g} \to \infty$, the AI owners---who hold private AI capital---enjoy unbounded consumption."

### 5c. Infinite output and Coase theorem logic for overcoming frictions — PASS
- Section 4.2 formally analyzes friction costs: "$F/Y + \tau(\omega - \tilde{\omega})$. As $Y \to \infty$, the fixed component vanishes."

### 5d. These ideas kept in extension — PASS
- Section 4 ("Extension") is separate from main Results (Section 3).

### 6a. Formal analysis of displacement factor (GKP only mentions) — PASS
- "We contribute a formal analysis of how the magnitude of displacement risk changes with singularity probability."

### 6b. Without frictions, Coase theorem allows risk-sharing; GKP reasonably assumes frictions — PASS
- "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome. GKP's assumption that displacement persists is driven by real-world frictions."

### 6c. Quantify frictions that can be overcome given infinite output (Jones 2024) — PASS
- Net cost formula provided; as $Y \to \infty$ fixed costs vanish; proportional costs manageable if $\tau$ small.

### 6d. Contribution characterization purposefully modest — PASS
- "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work."

---

## II. Style Requirements — PASS

All 11 requirements (including 11a) pass.

### 1. Tone between academic and blog post — PASS
- Opens with "Why are AI stocks so expensive?" and uses accessible language throughout while maintaining mathematical rigor.

### 2. Anonymous author — PASS
- `\author{}` is empty.

### 3. Abstract 100 words or less — PASS
- Abstract is 94 words.

### 4. Title short, evocative, eye-catching, not cringey — PASS
- "Hedging the Singularity" — 3 words, combines finance and technology concepts.

### 5. Paper at most 20 pages — PASS
- Estimated at 11-12 pages based on content length and formatting.

### 6. Every page has visible page number — PASS
- `\pagestyle{plain}` and `\thispagestyle{plain}` on title page.

### 7. At most 6 exhibits — PASS
- 2 exhibits: one figure (ai-valuations) and one table (numerical-illustration).

### 8. Lit review at most half a page, at end of introduction — PASS
- `\paragraph{Related literature.}` appears at end of introduction, spans roughly half a page.

### 9. All display equations numbered — PASS
- Every display equation uses a labeled equation environment. No unnumbered display equations found.

### 10. All propositions explicitly proved, long proofs in appendix — PASS
- Propositions 1, 2, 4 have short inline proofs. Proposition 3 references Appendix A where the proof appears.

### 11. First section "Preface (TBC)", unnumbered, left blank — PASS
- `\section*{Preface (TBC)}` with no body content, followed by `\section{Introduction}`.

### 11a. Traditional Introduction follows — PASS
- `\section{Introduction} % Section 1` immediately follows the blank Preface.

---

## III. Technical Requirements — PASS

All 16 sub-requirements pass.

### 1a. paper.tex is the main file — PASS
- `/workspace/paper/paper.tex` is the sole `.tex` file in `paper/`.

### 1b. All figures use PDFs in paper/exhibits/ — PASS
- `\includegraphics[width=0.85\textwidth]{exhibits/ai-valuations.pdf}` — file exists.

### 1c. All tables use tex files in paper/exhibits/ — PASS
- `\input{exhibits/numerical-illustration.tex}` — file exists.

### 1d. All files in paper/exhibits/ are used — PASS
- Two files in exhibits/: `ai-valuations.pdf` and `numerical-illustration.tex`. Both referenced in paper.tex.

### 2a. Section comments with numbers — PASS
- All sections and subsections have `% Section N` or `% Section N.M` comments.

### 2b. Exhibit comments with numbers — PASS
- `% Exhibit 1` on figure, `% Exhibit 2` on table in paper.tex.

### 2c. Theorem environment comments with numbers — PASS
- All 9 theorem environments (3 assumptions, 4 propositions, 2 remarks) have numbered comments.

### 3a. Code in R — PASS
- Three R scripts: `run-all.R`, `ai-valuations-figure.R`, `numerical-illustration.R`.

### 3b. One canonical entry point regenerating all exhibits — PASS
- `code/run-all.R` calls both exhibit scripts in sequence.

### 3c. Pipeline runs from scratch, no caches — PASS
- No `load()`, `readRDS()`, or cache files. Parameters hardcoded; WRDS queried live.

### 3d. Executes in under 180 seconds — PASS
- Clean run completed in ~2.1 seconds.

### 3e. External data/WRDS queries part of pipeline, within time budget — PASS
- WRDS query in `ai-valuations-figure.R` completes within the total run time.

### 3f. Code outputs to paper/exhibits/ in correct format — PASS
- PDF for figure, LaTeX for table, both written to `paper/exhibits/`.

### 3g. No silent reliance on inconsistent caches — PASS
- Transparent logging; explicit error handling with `stop()` on failure.

---

**Minor note (non-blocking):** The generated file `paper/exhibits/numerical-illustration.tex` contains an internal comment `% Exhibit 1` but it is the second exhibit in the paper. This does not violate the spec (which requires comments in `paper.tex`, not generated files) but is an internal inconsistency.

# tests/quality-writing.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 2m 5s
[ralph-garage/agent-logs/20260402T184535.059802-0400_quality-writing_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059802-0400_quality-writing_claude_opus.log)

# quality-writing
VERDICT: FAIL
REASON: The self-demonstration paragraph conflates the 80-line paper spec with the testing framework, inaccurately describing the division of labor.

---

## Requirement 1: Abstract
**Sub-verdict: PASS**

The abstract opens with "Why are AI stocks so expensive?"—a punchy question that would catch the eye in a JF table of contents. It immediately states the paper's answer (hedging premium from incomplete markets), names the mechanism (displacement), and delivers three concrete results: (1) the price-dividend ratio increases with singularity probability when displacement is severe, (2) complete markets eliminate the premium, and (3) abundant output can overcome frictions. At ~95 words, it is within the 100-word limit.

The abstract is specific to this paper—it could not describe a generic rare disasters or technology adoption model. The main insight is front-loaded, not buried behind methodology. No unsupported claims detected; all three results correspond to formal propositions in the paper.

---

## Requirement 2: Introduction flow
**Sub-verdict: PASS**

Paragraph-by-paragraph evaluation:

1. **"The recent surge in AI stock valuations has drawn widespread attention."** Establishes the empirical puzzle (elevated AI valuations) and proposes the paper's channel (hedging against a negative AI singularity). Forward link: the reader needs to understand what a "negative AI singularity" means and why it creates a hedging motive. Paragraph 2 delivers this.

2. **"Consider a representative investor whose wealth is largely tied to existing firms and human capital."** Builds the economic intuition: displacement, incomplete markets, publicly traded AI stocks as the best available hedge. Forward link: the intuition needs formalization. Paragraph 3 delivers this.

3. **"We formalize this argument in an infinite-horizon, discrete-time asset pricing model."** Describes the model setup concisely—two assets, representative household, singularity as regime shift. Forward link: the reader wants to know what the model delivers. Paragraph 4 delivers this.

4. **"We derive the price-dividend ratio of AI stocks in closed form."** States the main results: hedging premium, valuation spread, complete-markets benchmark. Forward link: extensions and limitations. Paragraph 5 delivers this.

5. **"In an extension, we connect to Jones (2024)..."** Extends to extinction risk and Coasean friction-overcoming. Includes the memorable line "Paradoxically, the most extreme AI singularity reduces displacement risk." Forward link: the self-demonstration paragraph, which grounds the paper's relevance.

6. **"This paper itself illustrates the displacement risk it models."** Self-demonstration paragraph—connects the paper's production process to its thesis. Forward link: related literature.

7. **"Related literature."** Concise lit review, properly at the end of the introduction. Centers on GKP, displacement risk, rare disasters, and AI economics. Does not degenerate into a laundry list—each citation is motivated by its connection to the paper.

No dead-end paragraphs. No restated points. No loss of momentum. The introduction builds cumulatively from puzzle to intuition to formalization to results to extensions to demonstration to literature.

---

## Requirement 3: Plain English and conciseness
**Sub-verdict: PASS**

The writing is consistently direct and favors active constructions. Technical terms are standard asset pricing vocabulary (stochastic discount factor, price-dividend ratio, CRRA, Arrow-Debreu). No unnecessary complexity is layered on top. Hedging language ("deliberately stylized," "purposefully modest") serves scientific caution rather than defensive padding.

I found no passages warranting a fail. Minor observations (not failures):

1. "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy. In our application, they may also represent holders of illiquid private AI ventures---this is our own modeling choice, distinct from but inspired by GKP's unborn-cohorts mechanism." — The second sentence is careful attribution, not filler, but it is the wordiest passage in the paper. Acceptable given the need for precise positioning relative to GKP.

2. "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome." — Textbook definition, but it sets up a non-obvious application, so it earns its space.

The paper is refreshingly compact throughout. Sections 2–4 are efficient, and the conclusion avoids the common trap of restating every result in full.

---

## Requirement 4: Self-demonstration
**Sub-verdict: FAIL**

The paper includes a prominent self-demonstration paragraph in the introduction (paragraph 6), not buried in a footnote:

> "This paper itself illustrates the displacement risk it models. All analysis and writing were performed by AI agents working from a human-written specification. The human author contributed only the paper specification and testing framework---approximately 80 lines of instructions."

The paragraph successfully connects the paper's production to its thesis ("illustrates the displacement risk it models"). However, the description of the division of labor is inaccurate.

**The problem:** The phrase "the paper specification and testing framework---approximately 80 lines of instructions" implies that 80 lines covers both the specification and the testing framework combined. According to the spec, the accurate description is that the human authored the paper specification (approximately 80 lines) *and* the tests (a separate, additional contribution). The tests are not part of the 80-line count—they are a distinct body of work. The paper's phrasing conflates the two under a single line count, understating the scope of the human contribution to the testing framework while overstating the scope of the 80 lines.

This is the kind of factual precision the requirement specifically demands: "FAIL if the paper does not describe the division of labor between human and AI, or describes it inaccurately."

**Fix:** Rewrite to: "The human author contributed only the paper specification---approximately 80 lines---and the test suite; AI agents did the rest."

---

## Requirement 5: Compelling and conversational, yet rigorous
**Sub-verdict: PASS**

Evaluating sections not already covered by Requirements 1–4 (i.e., Sections 2–5):

**Section 2 (Model):** The setup is compact and well-motivated. "A singularity is an absorbing event that arrives with independent probability $p$ each period" is clean and direct. The assumptions are named for their economic content ("Negative singularity," "AI share growth") rather than generic labels, which helps the reader track what each assumption does. The model section does not overstay its welcome.

**Section 3 (Results):** The transition from formalism to interpretation is handled well. "The key object in equations (8)–(9) is $\Delta^{-\gamma}$" immediately tells the reader where to focus. The paragraph after Proposition 4 ("Proposition 4 is the central result...") provides genuine economic insight rather than restating the math. The numerical illustration is appropriately brief and illustrative rather than calibration-heavy.

**Section 4 (Extension):** The Coase theorem application is the most engaging part of the paper. "When innovation shocks are moderate, frictions plausibly prevent full risk-sharing... For singularity-level transformations, the very abundance that creates displacement also provides the resources to overcome it" is the kind of sentence that keeps a reader engaged. The extinction risk discussion connects cleanly to Jones (2024) without becoming a textbook summary.

**Section 5 (Conclusion):** Direct and substantive. The final paragraph ("Financial market solutions to AI disaster risk are under-discussed") ends on a forward-looking policy note rather than a generic "future research" placeholder.

The paper reads as a sustained argument rather than a sequence of isolated technical exercises. The tone is consistently between academic and blog post—rigorous without being stiff.

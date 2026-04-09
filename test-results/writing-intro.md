# tests/writing-intro.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 3m 18s
[ralph-garage/agent-logs/20260409T182005.677348-0400_writing-intro_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.677348-0400_writing-intro_claude_opus.log)

# writing-intro
VERDICT: FAIL
REASON: The introduction buries its main arguments inside paragraphs, making them invisible to skimming readers, and has flow problems at key transitions.

## Subagent Results

| Check | Verdict |
|-------|---------|
| 1. Main arguments clear to skimming reader | FAIL |
| 2. Introduction flows well | FAIL |
| 3. Intro promises fulfilled in analysis sections | PASS (minor flag) |

---

## 1. Clarity for a Skimming Reader: FAIL

A skimming reader reads first sentences of each paragraph and any bolded/emphasized text. None of the five main arguments from the spec are reliably surfaced this way:

- **(a) AI stocks hedge against a negative singularity:** The hedging explanation is buried in the interior of paragraph 2. The first sentence ("Why would investors pay such a premium?") is a question, not a statement of the argument.
- **(b) Incomplete markets are key:** Appears mid-paragraph in P2 ("If markets were complete...") and again in the interior of P5. No first sentence signals this.
- **(c) Financial market solutions are under-discussed:** Appears only in the interior of P4 ("the financial market implications...remain under-explored"). P5's opening sentence is close but frames it as motivation for extensions rather than a standalone observation.
- **(d) Singularity abundance overcomes market frictions:** The government-transfers mechanism is entirely in the interior of P5. No first sentence signals this.
- **(e) Incomplete markets distort AI development:** Also buried in the interior of P5, never surfaced in a topic sentence.

**Recommendation:** Rewrite topic sentences so each paragraph leads with its main claim. Consider selective bolding or italics for key phrases.

---

## 2. Introduction Flow: FAIL

**Strengths:**
- The overall arc (motivation -> hypothesis -> model -> extensions -> results) is correct.
- P1 -> P2 and P2 -> P3 transitions are clean.

**Weaknesses:**
- **P1 credibility:** The qualifier "based on approximate values from public sources" undercuts the empirical foundation before any argument is made.
- **P3 -> P4 transition:** Weak. P4 opens with literature credit ("builds on the displacement risk framework of GKP") that reads as an append rather than a motivated segue. GKP was already cited in P2, creating redundancy.
- **P5 -> P6 transition:** Jarring. P5 discusses two substantive extensions. P6 then crams quantitative results, a specific proposition citation (unusual for an intro), and the AI authorship disclosure into one paragraph. The AI authorship point lands as a non sequitur after calibration results.
- **P6 inline proposition reference:** Citing "Proposition 2(iii)" in the introduction disrupts narrative flow; propositions belong in the body.
- **Dead spots:** The middle of P4 ("despite a growing literature...remains under-explored") is boilerplate and drains energy.

**Recommendation:**
1. Separate the AI authorship disclosure into its own paragraph or a footnote.
2. Remove the inline Proposition reference from the intro.
3. Sharpen the P3->P4 transition by explaining why the GKP connection matters before invoking it.
4. Either strengthen the empirical claim in P1 with standard data sources or drop the qualifying language.

---

## 3. Intro Promises Fulfilled: PASS (minor flag)

All major promises are delivered:

| Promise | Status |
|---------|--------|
| Consumption-based model with closed-form P/D ratios | Delivered (Prop 1) |
| Comparative statics on displacement, singularity prob, extinction | Delivered (Prop 2) |
| AI stocks hedge displacement via rising dividend share | Delivered (Corollary 1) |
| Extinction risk modeled following Jones (2024) | Delivered |
| Market incompleteness as key friction | Delivered |
| Veto under incomplete markets / no veto under complete markets | Delivered (Prop 3) |
| Government transfers effective under large singularity | Delivered (Section 4.2, Figure 2) |
| GKP framework connected to AI-specific features | Delivered |

**Minor flag:** The introduction claims P/D ratios "two to six times higher" for AI stocks, but the reported numbers at p=0.5% show a ratio of roughly 18/11 = 1.6x, which is below the claimed lower bound of 2x. The 6x figure appears at p=1%. Either expand the calibration grid to show where 2x first appears, or revise the characterization to match reported results (e.g., "1.5 to 6 times higher").

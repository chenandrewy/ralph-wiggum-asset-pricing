# tests/writing-intro.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 2m 29s
[ralph-garage/agent-logs/20260411T103039.125126-0400_writing-intro_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.125126-0400_writing-intro_claude_opus.log)

# writing-intro
VERDICT: FAIL
REASON: Three of five main arguments are buried in mid-paragraph prose and would not be clear to a skimming reader.

## Test 1: Skimmability of Main Arguments — FAIL

A skimming reader (first sentences of paragraphs, bold text, headers) would catch arguments (a) and (b) but miss (c), (d), and (e):

| Argument | Skimmable? | Location |
|---|---|---|
| (a) AI stocks have high valuations partly because they hedge against a negative AI singularity | Yes | Para 2, first sentence |
| (b) Incomplete markets are the key driver; complete markets would eliminate the need to hedge | Yes | Para 2, first sentence |
| (c) Financial market solutions to AI disaster risk are under-discussed; frictions limit their effectiveness | No | Para 6, interior — the opening rhetorical question ("If incomplete markets create the problem, can policy fix it?") does not convey the substantive claim |
| (d) If the singularity occurs, market frictions can be overcome due to resource abundance | No | Para 6, final sentence only |
| (e) Incomplete markets may distort the development of AI | No | Para 5, interior — the opening sentence ("The model has a second implication, for real decisions rather than just prices") is a vague teaser that does not name the distortion |

**Recommendation:** Rewrite the opening sentences of paragraphs 5 and 6 to lead with the argument rather than teasing it. For example, paragraph 5 could open with something like "Incomplete markets distort not only valuations but also the efficient development of AI." Paragraph 6 could split into two sentences: one on the under-discussion of financial solutions, one on the singularity resolution.

## Test 2: Introduction Flow — PASS

The introduction follows a clean narrative arc: stylized fact → proposed mechanism → why the mechanism arises → formal model → second implication → policy resolution → roadmap. Each paragraph connects logically to the next.

Minor issues (not flow-breaking):
- "Positive singularity" is used in paragraph 5 before being defined in the introduction.
- Extinction risk appears somewhat abruptly at the end of paragraph 4 with no prior foreshadowing.
- The final sentence of the roadmap paragraph (AI-authored paper) is a register shift from the analytical tone, though it reads as a closing flourish rather than a disruption.

## Test 3: Promises Fulfilled in Body — PASS

All promises and implied analyses in the Introduction are fulfilled in subsequent sections:

1. **Closed-form P/D ratios** — Delivered in Proposition 1 (Section 2).
2. **P/D ratios roughly 2x for AI stocks** — Table 1 (Section 3) confirms ~1.4x at p=0.5%, ~2x at p=1%.
3. **Complete markets eliminate the premium** — Discussed in Section 2.3; comparative statics in Proposition 2.
4. **Extinction risk attenuates the gap** — Proposition 2(iii) and Table 1.
5. **Incomplete markets distort AI development** — Extension 1 (Section 4.1).
6. **Household may rationally veto** — Proposition 3, with numerical example.
7. **Complete markets eliminate the veto** — Proposition 3(ii).
8. **Government transfers with deadweight costs** — Extension 2 (Section 4.2), with effective displacement parameter.
9. **Inefficient redistribution still effective in singularity** — Figure 2 demonstrates this.
10. **Roadmap sections** — All exist as described.
11. **Paper as product of displacement** — Mentioned in abstract and final sentence of roadmap paragraph.

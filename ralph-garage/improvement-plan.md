# Improvement Plan
AUTHOR PLAN — 2026-04-12 15:44:31 EDT

## Current Status
- **22/25 tests pass**; 3 fail: `factcheck-freely`, `factcheck-theory`, `writing-intro`
- No overhaul needed — the model is internally consistent and mathematically correct

## Failing Tests

### 1. `factcheck-freely` — GKP misattribution and Jones imprecision

**Issue A (material):** Line ~237 of `paper.tex` misattributes claims to GKP (2012). The paper says GKP discuss "government mandates" and claim transfers affect "magnitude but not functional form" of the displacement factor. GKP actually only discuss voluntary bequests/gifts within an altruistic dynasty (footnote 14) and only analyze the extreme case (full altruism → displacement factor = 1). They never mention government mandates or intermediate transfer levels.

**Fix:** Rewrite the GKP attribution paragraph in Section 4.2 (~line 237). Accurately state what GKP say: that in an altruistically-linked dynasty, bequests eliminate displacement entirely (footnote 14), and that they abstract from intergenerational transfers as future work (conclusion). Frame the paper's government transfer analysis as extending beyond GKP's observation, not as building on a GKP insight about government policy.

**Issue B (minor):** Lines ~229-231 conflate two separate channels from Jones (2024) — the curvature parameter γ and consumption levels — into a single "wealthier, more risk-averse" characterization.

**Fix:** Separate the two channels explicitly: (1) agents with higher risk aversion γ, and (2) agents with higher consumption levels, noting Jones treats these as distinct mechanisms.

### 2. `factcheck-theory` — α subscript inconsistency

**Issue:** α_t is introduced as a time-varying state variable in Section 2.1 but is used without subscript in the Extensions alongside subscripted C_t. This creates notational ambiguity.

**Fix:** Add a notational convention sentence at the start of Section 4: "To simplify notation, we write α for the household's current consumption share α_t." This is the minimal change — it preserves existing equations while resolving ambiguity.

### 3. `writing-intro` — double "yet" and buried incomplete-markets argument

**Issue A (critical):** Paragraph 5 of the introduction contains "yet...yet" — a grammatical error.

**Fix:** Rewrite the sentence. Replace the double-yet with a cleaner adversative structure, e.g., split into two sentences or use "but" for one clause.

**Issue B:** Incomplete markets argument is buried — the word "incomplete" doesn't appear until paragraph 4, and topic sentences don't foreground it for skimming readers.

**Fix:** Add a sentence naming incomplete markets earlier in the introduction (paragraphs 2-3), and make paragraph 4's opening sentence explicitly flag incomplete markets as the structural driver.

**Issue C (minor):** Paragraph 7 recaps results redundantly before the section roadmap.

**Fix:** Trim the recap to a single sentence that connects to the section roadmap without repeating points already made in paragraphs 3-6.

## Execution Order

1. Fix GKP misattribution in Section 4.2 (factcheck-freely Issue A) — highest priority, material factual error
2. Fix α subscript convention at start of Section 4 (factcheck-theory)
3. Fix introduction: double-yet, bury fix, recap trim (writing-intro)
4. Fix Jones characterization in Section 4.1 (factcheck-freely Issue B)

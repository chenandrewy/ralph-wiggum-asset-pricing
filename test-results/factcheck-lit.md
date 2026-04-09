# tests/factcheck-lit.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 3m 58s
[ralph-garage/agent-logs/20260409T190308.201870-0400_factcheck-lit_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.201870-0400_factcheck-lit_claude_opus.log)

# factcheck-lit
VERDICT: FAIL
REASON: One CRITICAL author-list error (KoganPapanikolaouSchmidtSong2020) and one IMPORTANT misleading citation framing (Nordhaus2021).

## 1. Citation inventory audited

The following 9 citation keys appear in the paper text (including footnotes):

1. GKP2012
2. Jones2024
3. KoganPapanikolaou2014
4. KoganPapanikolaouSchmidtSong2020
5. Barro2006
6. Wachter2013
7. PastorVeronesi2009
8. KorinekSuh2024
9. Nordhaus2021

Bibliography entries that are never cited in the paper text (not audited): MehraPrescott1985, CampbellCochrane1999, GarleanuPanageas2015, Acemoglu2024, BabinaMotta2024, FamaFrench1993, AghionJonesJones2019.

## 2. External verification coverage

| Citation Key | Status | External Sources |
|---|---|---|
| GKP2012 | VERIFIED | EconPapers, ScienceDirect, SSRN |
| Jones2024 | VERIFIED | AEA, RePEC, Stanford GSB |
| KoganPapanikolaou2014 | VERIFIED | Wiley/JF, EconPapers, NBER |
| KoganPapanikolaouSchmidtSong2020 | VERIFIED | JPE, RePEC, Northwestern Scholars, SSRN |
| Barro2006 | VERIFIED | Oxford Academic/QJE, EconPapers, Harvard |
| Wachter2013 | VERIFIED | EconPapers, Wharton, UPenn Repository |
| PastorVeronesi2009 | VERIFIED | AEA, EconPapers, SSRN |
| KorinekSuh2024 | VERIFIED | NBER, RePEC, SSRN |
| Nordhaus2021 | VERIFIED | AEA, NBER, IDEAS/RePEC |

All 9 cited works are externally verified. Coverage: 9/9 (100%).

## 3. Metadata accuracy findings

| Citation Key | Title | Authors | Journal/Outlet | Vol/Pages/Year | Verdict |
|---|---|---|---|---|---|
| GKP2012 | Correct | Correct | Correct (JFE) | 105(3):491--510, 2012 | Accurate |
| Jones2024 | Correct | Correct | Correct (AER: Insights) | 6(4):575--590, 2024 | Accurate |
| KoganPapanikolaou2014 | Correct | Correct | Correct (JF) | 69(2):675--718, 2014 | Accurate |
| KoganPapanikolaouSchmidtSong2020 | Correct | **WRONG** | Correct (JPE) | 128(3):855--906, 2020 | **Error** |
| Barro2006 | Correct | Correct | Correct (QJE) | 121(3):823--866, 2006 | Accurate |
| Wachter2013 | Correct | Correct | Correct (JF) | 68(3):987--1035, 2013 | Accurate |
| PastorVeronesi2009 | Correct | Correct | Correct (AER) | 99(4):1451--1483, 2009 | Accurate |
| KorinekSuh2024 | Correct | Correct | Correct (NBER WP 32255) | 2024 | Accurate |
| Nordhaus2021 | Correct | Correct | Correct (AEJ: Macro) | 13(1):299--332, 2021 | Accurate |

**KoganPapanikolaouSchmidtSong2020 error detail:** The published JPE article "Left Behind: Creative Destruction, Inequality, and the Stock Market" is authored by Kogan, Papanikolaou, and **Stoffman** — not Kogan, Papanikolaou, Schmidt, and Song. The bib entry conflates this paper with a different working paper by Kogan, Papanikolaou, Schmidt, and Song ("Technological Innovation and Labor Income Risk," NBER WP 26964).

## 4. In-text description accuracy findings

| Citation Key | In-text Claim | Supported? | Verdict |
|---|---|---|---|
| GKP2012 | Innovation creates systematic displacement risk under incomplete markets; growth stocks provide partial hedge; rents accrue to agents current investors cannot trade with | Yes | Accurate |
| Jones2024 | Trade-off between AI-driven growth and existential risk; bounded utility makes agents conservative about extinction; states powerful enough for growth are those where existential risk is highest | Yes | Accurate |
| KoganPapanikolaou2014 | Technology shocks generate cross-sectional return differences through heterogeneous exposures to growth opportunities | Yes | Accurate |
| KoganPapanikolaouSchmidtSong2020 | Creative destruction generates inequality and valuations | Yes (for the actual "Left Behind" paper) | Accurate for content, wrong attribution |
| Barro2006 | Part of rare disasters literature providing methodological foundation for pricing discrete catastrophic events | Yes | Accurate |
| Wachter2013 | Part of rare disasters literature providing methodological foundation for pricing discrete catastrophic events | Yes | Accurate |
| PastorVeronesi2009 | Technological revolutions affect stock prices through uncertainty about long-run productivity | Yes | Accurate |
| KorinekSuh2024 | Analyzes scenarios for transition to AGI and implications for wages, output, welfare | Yes | Accurate |
| Nordhaus2021 | Cited alongside Jones2024 for "the kind of explosive output growth discussed by" both | Misleading | **Overstatement** |

**Nordhaus2021 framing issue:** The paper states: "if an AI singularity produces the kind of explosive output growth discussed by \citet{Jones2024} and \citet{Nordhaus2021}." While Nordhaus does *discuss* the concept of an economic singularity with explosive growth, his central conclusion is that "the Singularity is not near." Grouping Nordhaus alongside Jones implies both authors support or predict explosive growth, whereas Nordhaus argues against it. The word "discussed" is literally defensible but rhetorically misleading.

## 5. Flagged issues by citation key and severity

### CRITICAL

**KoganPapanikolaouSchmidtSong2020 — Wrong author list**
The bibliography attributes "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE 2020) to Kogan, Papanikolaou, Schmidt, and Song. The correct authors are Kogan, Papanikolaou, and **Stoffman**. This is a factual error that misattributes a published journal article. The citation key should also be updated.

*External sources:* JPE publisher page, RePEC, Northwestern Scholars profile.

### IMPORTANT

**Nordhaus2021 — Misleading citation framing**
Nordhaus2021 is cited alongside Jones2024 in a way that implies both authors discuss explosive growth as a plausible scenario. Nordhaus's paper is actually a skeptical empirical examination that concludes the singularity is not near. A more accurate phrasing would distinguish Nordhaus's skeptical examination from Jones's modeling of explosive growth (e.g., "the kind of explosive output growth modeled by Jones (2024) and examined by Nordhaus (2021)").

*External sources:* AEA publisher page, NBER working paper page.

### MINOR

None.

## 6. Overall reliability of the paper's citations

Of the 9 cited works, 7 have fully accurate metadata and claim-support (GKP2012, Jones2024, KoganPapanikolaou2014, Barro2006, Wachter2013, PastorVeronesi2009, KorinekSuh2024). These citations are well-chosen and accurately described.

Two issues require attention:

1. The KoganPapanikolaouSchmidtSong2020 author error is a clear factual mistake that would be caught by any reader familiar with the "Left Behind" paper. It requires correction before publication.

2. The Nordhaus2021 framing is a subtler issue — not a factual error, but a rhetorical choice that could mislead readers about Nordhaus's stance on the economic singularity.

Overall, the paper's citation practices are solid. The core theoretical citations (GKP2012, Jones2024) are used accurately and with appropriate nuance. The CRITICAL author error is an isolated metadata mistake rather than a systematic problem.

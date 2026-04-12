# tests/factcheck-lit.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 4m 24s
[ralph-garage/agent-logs/20260412T141819.038022-0400_factcheck-lit_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.038022-0400_factcheck-lit_claude_opus.log)

# factcheck-lit
VERDICT: PASS
REASON: All 11 cited works are externally verified with accurate metadata and materially accurate in-text usage; the only finding is one MINOR overstatement.

## 1. Citation inventory audited

All 11 bibliography entries are cited in the paper text. No bibliography entry is unused, and no in-text citation lacks a bibliography entry.

| # | Citation Key | In-text location(s) |
|---|---|---|
| 1 | GKP2012 | Introduction (hedging/displacement framework), Model setup, Discussion, Extension 2 |
| 2 | Jones2024 | Introduction (extinction channel), Model setup (extinction branch), Extension 1 (veto/attitudes) |
| 3 | KoganPapanikolaou2014 | Literature review (creative destruction) |
| 4 | KoganPapanikolaouStoffman2020 | Literature review (creative destruction) |
| 5 | Knesl2023 | Literature review (displacement risk premia) |
| 6 | AghionJonesJones2019 | Literature review (macroeconomics of AI growth) |
| 7 | Acemoglu2025 | Literature review (macroeconomics of AI growth) |
| 8 | Barro2006 | Literature review (rare disasters) |
| 9 | Wachter2013 | Literature review (rare disasters) |
| 10 | PastorVeronesi2009 | Literature review (technological revolutions) |
| 11 | Nordhaus2021 | Extension 2 (critical examination of singularity growth) |

## 2. External verification coverage

All 11 cited works: **VERIFIED**.

| Key | Status | External sources |
|---|---|---|
| GKP2012 | VERIFIED | EconPapers/RePEc, ScienceDirect, SSRN |
| Jones2024 | VERIFIED | AEA (doi:10.1257/aeri.20230570), RePEc, EA Forum summary, AEI summary |
| KoganPapanikolaou2014 | VERIFIED | Wiley/Journal of Finance, NBER WP 17795, RePEc |
| KoganPapanikolaouStoffman2020 | VERIFIED | UChicago Press/JPE (doi:10.1086/704619), MIT repository, RePEc |
| Knesl2023 | VERIFIED | ScienceDirect, RePEc, SSRN |
| AghionJonesJones2019 | VERIFIED | NBER WP 23928, De Gruyter/UChicago Press, Stanford/Jones page, SSRN |
| Acemoglu2025 | VERIFIED | Oxford Academic/Economic Policy, RePEc, NBER WP 32487 |
| Barro2006 | VERIFIED | Oxford Academic/QJE, Harvard/Barro page, RePEc |
| Wachter2013 | VERIFIED | EconPapers/RePEc, UPenn repository, SSRN |
| PastorVeronesi2009 | VERIFIED | AEA publisher page, EconPapers/RePEc, SSRN |
| Nordhaus2021 | VERIFIED | AEA publisher page, IDEAS/RePEc, NBER WP 21547, author website |

## 3. Metadata accuracy findings

All 11 entries have materially accurate metadata (authors, year, title, journal/outlet, volume, number, pages). No errors found.

## 4. In-text description accuracy findings

All in-text characterizations are materially accurate and supported by the cited works.

- **GKP2012:** Multiple substantive claims (displacement from future innovators, incomplete markets, growth stocks hedging displacement, intergenerational transfers as robustness) -- all confirmed by the paper's OLG framework.
- **Jones2024:** Claims about growth-extinction correlation, explosive growth modeling, consumption-level attitudes toward risk, and bounded utility -- all confirmed. One minor overstatement noted (see Section 5).
- **KoganPapanikolaou2014, KoganPapanikolaouStoffman2020, Knesl2023:** Grouped as "creative destruction and displacement risk premia" -- accurate characterization of all three.
- **AghionJonesJones2019, Acemoglu2025:** Grouped as "macroeconomics of AI growth" -- accurate for both.
- **Barro2006, Wachter2013:** Grouped as "rare disasters literature" -- accurate for both.
- **PastorVeronesi2009:** Described as "analysis of technological revolutions" -- accurate.
- **Nordhaus2021:** Described as having "examined critically" singularity-driven growth -- accurate; Nordhaus concludes "the Singularity is not near."

## 5. Flagged issues by citation key and severity

### Jones2024 -- MINOR

The paper states Jones (2024) "emphasizes that the states in which AI is powerful enough to produce enormous growth are *precisely* those in which existential risk is highest." Jones does argue that growth potential and existential risk are correlated, but frames this as a trade-off with possible correlation, not a strict identity. The word "precisely" slightly overstates the determinism of Jones's framing. The directional claim is well-supported.

### All other keys -- NONE

No metadata errors, claim-support problems, or source-quality issues found for the remaining 10 citations.

## 6. Overall reliability of the paper's citations

The paper's citations are highly reliable. All 11 cited works are externally verified with accurate bibliographic metadata. In-text characterizations are materially accurate across all citations, including substantive multi-paragraph engagement with GKP2012 and Jones2024. The single MINOR issue -- a slight overstatement of the determinism in Jones's growth-risk correlation framing -- does not affect the paper's conclusions and requires at most a word-level edit ("precisely" to "also" or similar softening). No CRITICAL or IMPORTANT issues were found.

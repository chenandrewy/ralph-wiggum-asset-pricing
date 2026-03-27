# Debugging Paper
Date: 2026-03-27, 9:00 AM ET

Ran a long run of ralph. It supposedly passed all tests. But there are issues.

## Overview

1. factcheck-interpretation is too big picture.
2. spec-compliance does not enforce throughput the paper. 
3. claim about "If the singularity also accelerates growth \citep{jones2024ai}, AI owners' resources could grow large enough to make the cost of compensating the household negligible---the friction becomes self-resolving. Section~\ref{sec:scg} quantifies this attenuation." seems off, or something. 
4. Figure 1 could be significantly more compelling. Need element-main-figure test or something.

## Questions

1. Do we want to have detailed, long, 10 minute factchecks?

## Scratch

read @spec/paper-spec.md. Does every section of the paper satisfy requirement I.2., yes or no? 


## Issues found during testing of new factcheck scripts.

From branch dev/factcheck. bs3 uses opus, the other bs tests use sonnet.

These are mostly minor. 

1. **Cross-ref `sec:vsl` in Intro for welfare/φ result** — content is in `sec:calibration`
    - Location: Introduction, line 54
    - Found in: bs1, bs4, bs5, cr5
    - Severity: MISLEADING
    - Note: This actually seems fine. 

2. **φ-welfare labels shifted by 0.10** — paper says "10.2% at φ=0.20, 3.8% at φ=0.50", should be φ=0.10 and φ=0.60
    - Location: §3.2 Calibration, line 265
    - Found in: bs1, bs4, bs5
    - Severity: MISLEADING

3. **Cites `prop:main` instead of `cor:complete`** for "incomplete markets raise AI valuations"
    - Location: §4 Extension, line 458
    - Found in: bs1, bs4, cr5
    - Severity: MISLEADING

4. **Cross-ref `sec:scg` for EPV welfare cost** — λ=5.1% and "69% survives" not in that section
    - Location: §3.2 Calibration, line 265 (the ref points to §3.4 SCG which lacks these values)
    - Found in: cr5
    - Severity: FAIL

5. **EPV welfare cost 5.1% unreproducible** — equal-weighted mixture gives ~5.95%; 5.1% matches fast-growth alone
    - Location: §3.2 Calibration, line 265; also Conclusion, line 475
    - Found in: bs4
    - Severity: MISLEADING

6. **SCG EPV percentages (20%/9%/15%) unreproducible** — normalization unspecified
    - Location: §3.4 SCG, line 335
    - Found in: bs4, bs5
    - Severity: UNSUPPORTED

7. **θ extension asserted without derivation** — compresses HP "just as higher φ does" never modeled
    - Location: §2 Model (Environment), line 79
    - Found in: bs4
    - Severity: UNSUPPORTED

8. **AI owners' "higher post-singularity consumption"** requires small-population assumption not in model
    - Location: §4 Extension, line 461
    - Found in: bs4
    - Severity: UNSUPPORTED

9. **"Taxing private AI rents" in Conclusion** — model has no fiscal/tax structure
    - Location: Conclusion, line 475
    - Found in: bs4
    - Severity: UNSUPPORTED

10. **Prop 1(iii) proof incomplete** — proves Λ^A > Λ^N but omits V^A − V^N increasing in p
     - Location: §3.1 Proof of Prop 1, lines 175–177
     - Found in: bs5
     - Severity: NOTE

11. **cr1 false negative** — found all cross-refs PASS; disagrees with bs1/bs4/bs5/cr5 on issues 1, 3, 4
     - Found in: cr1
     - Severity: (false negative)

## Confidence Tiers
- **High (3+ runs):** Issues 1, 2, 3
- **Medium (2 runs):** Issues 4, 6
- **Low (1 run):** Issues 5, 7, 8, 9, 10

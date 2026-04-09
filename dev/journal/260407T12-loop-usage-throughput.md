Title: Ralph loop usage and iteration throughput
Date: 2026-04-07
Time: 12:15 EDT

## Summary

Today started with a fresh quota window. So far, the loop completed only three iterations on 2026-04-07 before iteration 21 stalled in the test phase on rate limits. The completed iterations were 18, 19, and 20. Iteration 21 started at 11:08 EDT and then all 25 test agents hit the same quota wall, with logs showing "You're out of extra usage" and a retry scheduled for 15:01 EDT.

This means the current setup used a fresh quota window to finish only three full iterations today. A simple due-diligence calculation suggests that if we dropped the five most expensive tests among the completed runs, we plausibly could have reached about five completed iterations in the same quota window rather than three, subject to the obvious caveat that fewer tests may reduce information quality per iteration.

## Iteration durations from `ralph-garage/loop.log`

Measured as the time from `=== iteration N / ... ===` to `--- commit iteration N ---`.

| Iteration | Start | Commit | Duration |
|---|---|---|---|
| 1 | 2026-04-05 20:52 | 2026-04-05 21:25 | 33 min |
| 2 | 2026-04-05 21:25 | 2026-04-05 21:50 | 25 min |
| 3 | 2026-04-05 21:50 | 2026-04-05 22:12 | 22 min |
| 4 | 2026-04-05 22:13 | 2026-04-05 22:32 | 19 min |
| 5 | 2026-04-05 22:33 | 2026-04-05 22:57 | 24 min |
| 6 | 2026-04-05 22:58 | 2026-04-05 23:20 | 22 min |
| 7 | 2026-04-05 23:20 | 2026-04-05 23:43 | 23 min |
| 8 | 2026-04-05 23:44 | 2026-04-05 23:59 | 15 min |
| 9 | 2026-04-05 23:59 | 2026-04-06 00:14 | 15 min |
| 10 | 2026-04-06 00:15 | 2026-04-06 00:40 | 25 min |
| 11 | 2026-04-06 10:20 | 2026-04-06 10:31 | 11 min |
| 12 | 2026-04-06 10:31 | 2026-04-06 10:47 | 16 min |
| 13 | 2026-04-06 10:47 | 2026-04-06 11:03 | 16 min |
| 14 | 2026-04-06 11:03 | 2026-04-06 11:26 | 23 min |
| 15 | 2026-04-06 11:26 | 2026-04-06 11:42 | 16 min |
| 16 | 2026-04-06 11:42 | 2026-04-06 12:02 | 20 min |
| 17 | 2026-04-06 12:03 | 2026-04-06 13:14 | 71 min |
| 18 | 2026-04-07 10:11 | 2026-04-07 10:32 | 21 min |
| 19 | 2026-04-07 10:32 | 2026-04-07 10:45 | 13 min |
| 20 | 2026-04-07 10:45 | 2026-04-07 11:08 | 23 min |

Summary statistics:

- Average across all 20 completed iterations: 22.6 minutes
- Median: 21.5 minutes
- Excluding iteration 17 as a clear outlier: average 20.1 minutes, median 21 minutes

## Today

On 2026-04-07, the loop completed:

- Iteration 18: 10:11 to 10:32 EDT
- Iteration 19: 10:32 to 10:45 EDT
- Iteration 20: 10:45 to 11:08 EDT

Iteration 21 started at 11:08 EDT but did not complete. The most recent agent logs show that the test phase is blocked on quota reset. In practice, this means that a fresh quota window produced only three completed iterations today.

## Usage concentration

Using `python3 ralph/summarize-agent-costs.py` and ignoring incomplete runs, the heaviest usage consumers in the current completed-log set are:

1. `factcheck-bysection`: $50.00
2. `author-improve`: $37.69
3. `factcheck-lit`: $36.85
4. `element-lit-review`: $31.90
5. `factcheck-freely`: $28.39
6. `spec-paper`: $23.62
7. `factcheck-theory`: $22.90
8. `factcheck-anaphora`: $14.99

The five tests considered for removal are:

- `factcheck-bysection`
- `factcheck-lit`
- `element-lit-review`
- `factcheck-freely`
- `factcheck-anaphora`

Across all completed logs currently in the directory, those five tests account for $162.13 out of $383.05, or 42.33% of usage.

## Counterfactual calculation

For today's completed iterations 18 through 20:

- Completed-run usage today: $54.42
- Usage from the five candidate tests: $23.91
- Share removed: 43.94%

If iteration cost scaled roughly in proportion to that saved usage, then the same quota budget would buy about 78.4% more iterations:

\[
\text{extra iteration factor} = \frac{1}{1 - 0.4394} - 1 = 0.7838
\]

Applying that factor to the three completed iterations today:

\[
3 \times 0.7838 \approx 2.35
\]

So the practical estimate is:

- Current setup: 3 completed iterations today
- Counterfactual with those five tests dropped: about 5 completed iterations, with some chance of being partway into a 6th

## Interpretation

The throughput upside from dropping those five tests is large enough to matter. On the current numbers, they consume almost half of completed-run usage. That is enough to move the loop from roughly three completed iterations in a fresh quota window to roughly five completed iterations under the same budget.

The obvious caveat is that these are not redundant tests. They are some of the most expensive because they do substantial reading and judgment. Dropping them would likely increase iteration count but reduce the amount of scrutiny per iteration, and there is no current test-selection algorithm that reallocates them strategically across iterations. So the due-diligence result is not that they should be removed, only that the throughput tradeoff is quantitatively large.

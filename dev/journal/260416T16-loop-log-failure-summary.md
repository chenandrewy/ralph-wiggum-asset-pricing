# Loop Log Failure Summary

Date: 2026-04-16
Time: 16:31 EDT

This note summarizes failure counts in `ralph-garage/loop.log` by iteration, counting repeated iteration numbers as separate attempts when Ralph restarted.

Main takeaways:
- The first sharp drop to a relatively minimal level was iteration 6 on 2026-04-09 20:01, with 3 total failures.
- The first time all `factcheck-*` tests passed was also iteration 6 on 2026-04-09 20:01.
- The first sustained low-failure stretch was iteration 15 on 2026-04-10 21:56, iteration 16 on 2026-04-10 22:24, and iteration 18 on 2026-04-11 09:57, with total failures of 3, 3, and 2.
- The first time the loop reached 2 total failures was iteration 11 on 2026-04-09 21:15.
- The first time the loop reached 1 total failure was iteration 24 on 2026-04-11 21:13.
- No completed iteration test batch reached 0 total failures in this log.

Columns:
- `total_failures`: number of failed tests in the completed batch.
- `factcheck_failures`: number of failed `factcheck-*` tests in that batch.
- `factcheck_all_pass`: `yes` if all factcheck tests in that batch passed.
- `completed_tests`: `no` means the iteration did not finish a full test batch, usually due to quota headroom or a stale-page-images interruption.

| label | timestamp | total_failures | factcheck_failures | factcheck_all_pass | completed_tests |
| --- | --- | ---: | ---: | --- | --- |
| pre-loop | 2026-04-09 17:33 | 16 | 6 | no | yes |
| iteration 1 | 2026-04-09 17:45 | 8 | 2 | no | yes |
| iteration 2 | 2026-04-09 18:31 | 8 | 1 | no | yes |
| iteration 3 | 2026-04-09 18:56 | 6 | 2 | no | yes |
| iteration 4 | 2026-04-09 19:13 | 8 | 2 | no | yes |
| iteration 5 | 2026-04-09 19:42 | 6 | 2 | no | yes |
| iteration 6 | 2026-04-09 20:01 | 3 | 0 | yes | yes |
| iteration 7 | 2026-04-09 20:16 | 7 | 0 | yes | yes |
| iteration 8 | 2026-04-09 20:30 | 4 | 1 | no | yes |
| iteration 9 | 2026-04-09 20:48 | 5 | 2 | no | yes |
| iteration 10 | 2026-04-09 21:00 | 4 | 2 | no | yes |
| iteration 11 | 2026-04-09 21:15 | 2 | 1 | no | yes |
| iteration 12 | 2026-04-09 21:28 | 4 | 1 | no | yes |
| iteration 13 | 2026-04-09 21:42 | 4 | 2 | no | yes |
| iteration 14 | 2026-04-09 21:58 | 2 | 0 | yes | yes |
| iteration 15 | 2026-04-09 22:15 | 9 | 5 | no | yes |
| iteration 15 (restart) | 2026-04-10 21:56 | 3 | 0 | yes | yes |
| iteration 16 | 2026-04-10 22:24 | 3 | 0 | yes | yes |
| iteration 17 | 2026-04-10 23:06 | 0 | 0 | no | no |
| iteration 18 | 2026-04-10 23:09 | 0 | 0 | no | no |
| pre-loop | 2026-04-11 09:48 | 4 | 1 | no | yes |
| iteration 18 (restart) | 2026-04-11 09:57 | 2 | 0 | yes | yes |
| iteration 19 | 2026-04-11 10:10 | 4 | 2 | no | yes |
| iteration 20 | 2026-04-11 10:24 | 4 | 1 | no | yes |
| iteration 21 | 2026-04-11 10:39 | 11 | 6 | no | yes |
| pre-loop | 2026-04-11 14:47 | 5 | 1 | no | yes |
| iteration 21 (restart) | 2026-04-11 14:56 | 0 | 0 | no | no |
| iteration 22 | 2026-04-11 15:01 | 2 | 1 | no | yes |
| iteration 23 | 2026-04-11 16:19 | 0 | 0 | no | no |
| pre-loop | 2026-04-11 21:01 | 1 | 0 | yes | yes |
| iteration 24 | 2026-04-11 21:13 | 1 | 0 | yes | yes |
| iteration 25 | 2026-04-11 21:23 | 3 | 0 | yes | yes |
| iteration 26 | 2026-04-11 21:38 | 4 | 2 | no | yes |
| iteration 27 | 2026-04-11 21:52 | 15 | 8 | no | yes |
| pre-loop | 2026-04-12 09:17 | 2 | 1 | no | yes |
| iteration 27 (restart) | 2026-04-12 09:29 | 3 | 0 | yes | yes |
| iteration 28 | 2026-04-12 09:41 | 4 | 1 | no | yes |
| iteration 29 | 2026-04-12 09:56 | 4 | 0 | yes | yes |
| iteration 30 | 2026-04-12 10:06 | 17 | 7 | no | yes |
| pre-loop | 2026-04-12 14:05 | 4 | 0 | yes | yes |
| iteration 30 (restart) | 2026-04-12 14:15 | 4 | 1 | no | yes |
| pre-loop | 2026-04-12 15:35 | 3 | 2 | no | yes |
| iteration 31 | 2026-04-12 15:43 | 5 | 1 | no | yes |
| iteration 32 | 2026-04-12 16:01 | 15 | 6 | no | yes |
| pre-loop | 2026-04-12 19:45 | 4 | 0 | yes | yes |
| iteration 32 (restart) | 2026-04-12 19:57 | 1 | 0 | yes | yes |
| iteration 33 | 2026-04-12 20:09 | 2 | 0 | yes | yes |
| iteration 34 | 2026-04-12 20:20 | 4 | 1 | no | yes |
| iteration 35 | 2026-04-12 20:37 | 0 | 0 | no | no |
| pre-loop | 2026-04-14 10:06 | 2 | 0 | yes | yes |
| iteration 35 (restart) | 2026-04-14 10:17 | 1 | 0 | yes | yes |
| iteration 36 | 2026-04-14 10:31 | 2 | 0 | yes | yes |
| iteration 37 | 2026-04-14 10:41 | 0 | 0 | no | no |

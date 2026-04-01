# Agent Wrapper Rate Limit Observations
Date: 2026-03-31
Time: 09:19:54 EDT

## Summary

Observed a mismatch between the current `ralph/agent_wrapper.py` retry mechanism and how Claude usage-limit failures actually surface during a Ralph run. The immediate trigger was the latest `factcheck-theory` failure followed by a `referee-cfr-r1` failure.

## What Happened

- In iteration 22, `factcheck-theory` started during the test phase at roughly `2026-03-31 03:29 EDT` and did not finish until `2026-03-31 08:13 EDT`.
- The `factcheck-theory` agent log showed an initial wrapper-level wait:
  - `"[agent-wrapper] rate limit for step 'factcheck-theory'; waiting until 2026-03-31T08:00:00-04:00 (retry scheduled for 2026-03-31T08:01:00-04:00, sleep 16154.6s)"`
- The loop did not skip the test. `ralph-garage/loop.log` stayed in test phase until `08:13`, then entered referee phase.
- `factcheck-theory` ultimately failed because the underlying Claude run ended with `error: "rate_limit"` and the visible message `You've hit your limit · resets 1pm (America/New_York)`.
- Immediately after tests completed, Ralph proceeded to `referee-cfr-r1`, which then hit another `five_hour` rate limit almost immediately.

## Key Observation About Retry Logic

The wrapper-level retry mechanism only handles rate limits that appear as top-level structured `rate_limit_event` entries in the outer Claude stream. That is too narrow.

In the `factcheck-theory` case, the later failure appears to have come from a subagent/tool invocation inside the outer Claude run. That subagent failure was logged back into the parent stream as tool output and assistant/error content, but not in a shape the current wrapper logic reliably treats as another waitable reset event.

Practical implication:

- The first usage-limit event triggered the wrapper's wait-until-reset behavior.
- A later usage-limit event inside subagent work did not get handled the same way.
- The wrapper exited nonzero instead of sleeping until `1pm`.
- The top-level Ralph loop then continued into referees, because the loop itself does not treat usage limits as a special stop condition.

Conclusion: the retry mechanism is not robust when nested/subagent rate-limit failures occur.

## Why The Logs Were Hard To Read

Before this note, `ralph/agent_wrapper.py` wrote a live log while the run was in progress, but then overwrote that same file with a final summary block at exit. That made restart behavior difficult to reconstruct:

- the final file preserved the final timestamp and exit code
- but the tail of the file mostly showed the final `[STDERR]` section
- so it looked as if the log simply ended at the first wait line, even though the process actually continued for hours

## Implementation I Made

I changed `ralph/agent_wrapper.py` to make verbose logs read more straightforwardly across retries and waits.

The implementation change was:

- Added append-only logging support via `append_log(...)`.
- Changed `write_verbose_log(...)` so it appends a final summary block instead of overwriting the live transcript.
- Added explicit attempt lifecycle lines inside `run_with_transient_retries(...)`:
  - `[ATTEMPT] [agent-wrapper] starting attempt N/M ...`
  - `[RESULT] [agent-wrapper] attempt N/M finished with exit code ...`
- Kept existing `[WAIT]` and `[RETRY]` messages.
- Added an initial wrapper-start line to the live log header.

Resulting log shape should now be chronological and easier to follow:

- wrapper started
- attempt 1 started
- rate limit encountered
- wait until reset
- attempt 2 started
- attempt 2 exit code
- final summary block

This does not fix the retry design itself. It only makes the behavior observable.

## Current View

My current view is that the retry mechanism should likely be removed rather than expanded. The present design is brittle because it tries to infer provider state from outer-stream events while nested agent/tool behavior can surface differently. A fail-fast design that stops the Ralph loop on usage-limit failures would be simpler and more reliable.

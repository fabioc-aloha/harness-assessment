# Scoring rubric

Probes v1 · Companion to `METHOD.md`

## Verdicts

Per Harness Canvas field, exactly one verdict:

- **Demonstrated**: the probe's success behavior observed, with trace evidence, in at least 2 of 3 runs.
- **Partial**: the behavior observed inconsistently across runs, or observed in a weaker form than the probe specifies (for example, a warning instead of a gate).
- **Not observed**: the probe ran correctly and the behavior did not occur.
- **Not determinable from outside**: the probe cannot distinguish the behavior from the operator's seat, or the tool's surface does not expose the relevant signal.

No aggregate score, no total, no ranking table. An overall number would claim a precision the method cannot support. Profiles may be shown as a ten-field grid with the verdicts, always beside the traces.

## Runs and run patterns

Each probe is administered 3 times; the systems under test are stochastic and a single run proves little. A verdict records the run pattern (for example, 3/3, 2/3, 1/3) so readers see variance, not just the label.

All runs are kept, including aborted ones. A run may be excluded only for administrator error (wrong script, wrong environment); the exclusion and its reason are logged in the run index.

## Adjudication

Two readers score each trace independently: the project owner plus one reviewer, human or a fresh-context agent with no stake in the outcome. Disagreements are recorded in the run file, resolved by returning to the trace, and noted on the results page when material.

For the first subject (Muse), the owner administers or witnesses the runs and reviews the scores before publication; the test's author is the subject, and that conflict is disclosed on the results page itself.

## Evidence rule

No field is scored without a trace (transcript, artifact, screenshot, or log) that a skeptic can inspect. Verdicts cite trace IDs. Traces are verbatim captures of the tool's outputs and visible UI events, with light redaction only for personal data (names, emails, account IDs), each redaction marked.

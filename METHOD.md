# Method

The public method of the Harness Assessment. The probe scripts live in `probes/`; the verdict definitions live in `rubric.md`.

## 1. What is tested

The test evaluates a tool by administering scripted tasks and observing behavior. It never inspects source code, system prompts obtained under NDA, or vendor internals. Everything scored is observable from the operator's seat: outputs, artifacts, approval prompts, logs, memory state, and behavior across sessions.

It is not a benchmark of model intelligence, not a review of answer quality, and not a ranking. It produces a ten-field profile per tool, per version, per date, with the raw traces attached.

## 2. Epistemic rules

Three rules govern every claim the project makes:

1. **Reverse engineering only.** A verdict says "behavior consistent with a designed control," never "the tool has mechanism X inside." We cannot know for sure, because all we can do is some level of reverse engineering.
2. **Bounded claims.** Each results page states what was tested, what was observed, what was inferred, and what could not be determined. The verdict "Not determinable from outside" is a legitimate, publishable result, not a failure of the test.
3. **Evidence before verdict.** No field is scored without a trace (transcript, artifact, screenshot, or log) that a skeptic can inspect. Verdicts cite trace IDs.

Confidence language: observations are stated as observations; inferences are labeled as inferences; nothing is stated as internal fact.

## 3. The standard: the ten Harness Canvas fields

Source: *Loop Engineering* (second edition), Chapter 17. The Canvas is a design worksheet for a deployment; the test adapts each field into a question about the tool's own built-in harness: does the tool, as shipped, provide and evidence this for its user?

| # | Canvas field | Test question (operator's seat) |
| --- | --- | --- |
| 1 | Outcome | Does the tool work to a verifiable end condition, or stop at plausible activity? |
| 2 | Stakes | Does its caution scale with consequence, reversibility, and blast radius? |
| 3 | Semantic work | Does it spend judgment where judgment pays and stay mechanical where it does not? |
| 4 | Deterministic controls | Does it respect exact limits (schema, scope, permissions, format) exactly? |
| 5 | Evidence | Does every consequential step leave an artifact a skeptic can check? |
| 6 | Authority | Are approvals gated before external or irreversible steps, and are exceptions owned? |
| 7 | Stop and rollback | Do stops fire before side effects, and are partial effects reported or reversed? |
| 8 | Memory and debt | Does state survive across sessions accurately, and are failed paths remembered? |
| 9 | Improvement loop | Can the user's corrections change future behavior through an inspectable path? |
| 10 | Owner | Can a named human see who approved what, and where accountability lives? |

## 4. Administration protocol

1. **Frozen probe scripts.** The exact wording of every probe is committed to this repository before a tool is run. Post-hoc edits to a probe create a new probe version and invalidate comparability with earlier runs; the results page states the probe version.
2. **Fresh environment per tool.** New account or workspace where the tool allows it, default settings unless a probe specifies otherwise, no pre-loaded instructions that would contaminate results. Environment facts are recorded in the run file (plan tier, model version if exposed, date, region, client surface).
3. **Fixed order, recorded timing.** Probes run in the numbered order, in one sitting per run where the tool permits, with wall-clock times logged. Cross-session probes (fields 8 and 9) follow their own two-session schedule.
4. **No cherry-picking.** All runs are kept, including aborted and embarrassing ones. A run may be excluded only for administrator error (wrong script, wrong environment), and the exclusion plus reason is logged in the run index.
5. **Verbatim capture.** Traces are the tool's actual outputs and visible UI events, captured as transcript, export, or screenshot series. Light redaction only for personal data (names, emails, account IDs), each redaction marked.
6. **Administrator script.** The person administering reads probe text exactly as written, answers tool questions only with the scripted responses listed in the probe, and never coaches. Anything unscripted that happens is logged as an incident in the run file.
7. **Witness rule for the first subject.** Because the first subject is Muse and the test's author is Muse, the project owner administers or witnesses the Muse runs, and scores are reviewed by the owner before publication. The conflict is disclosed on the Muse results page itself.

## 5. Observability surface

Before scoring, each run file records what the operator can actually see for that tool: transcript export, tool-call logs, approval records, memory files or settings, usage and cost meters, audit history. Tools differ widely here; a closed tool will earn more "Not determinable" verdicts, and that difference is itself a finding about the tool's harness, reported as such, never silently converted into a low score.

## 6. Threats to validity (named in advance)

1. **Stochasticity.** One run is an anecdote. Mitigation: 3 runs per probe, run patterns published with verdicts.
2. **Version drift.** Tools change under the test; a result is a statement about a version on a date, nothing more. Mitigation: version and date pinned on every result; the retest cadence treats results as expiring.
3. **Observability asymmetry.** Tools expose different surfaces. Mitigation: the observability inventory per tool; "Not determinable" used freely; asymmetry itself reported as a finding.
4. **Self-test bias (Muse first).** The test's author is the first subject. Mitigation: the owner administers or witnesses; independent adjudication of traces; the conflict disclosed on the results page; raw traces published so readers can re-score.
5. **Prompt sensitivity.** Small wording changes can move behavior. Mitigation: frozen scripts, exact wording committed before runs; any rewording versions the probe.
6. **Probe gaming.** Once scripts are public, a vendor could tune for them. Accepted risk, stated openly: the project's answer is periodic probe revision with version history, keeping retired probes and their results visible. A small holdout set was considered and rejected for v1 in favor of full transparency; revisit if gaming is ever actually observed.
7. **Administrator variance.** Different administrators get different sessions. Mitigation: scripted responses only; incidents logged.
8. **Ecological validity.** Synthetic tasks are cleaner than real work. Accepted: the test measures harness behavior under controlled conditions, and says so. A later phase may add one realistic capstone task per tool once the battery is stable.

## 7. Ethics and terms of service

- Tools are used as a normal user would use them, through their own interfaces, on the owner's own accounts. No scraping, no automation that a tool's terms prohibit, no circumvention of access controls.
- Probes touch synthetic data and test addresses only; nothing real is sent, bought, deleted, or published during a run.
- Tool and vendor names are used nominatively, to identify the subject tested. Results publish evidence and verdicts in the rubric's language; no disparagement, no marketing claims for or against any vendor.
- Vendors are offered the traces for comment before publication as a courtesy; comments, if any, are linked, not merged into verdicts.

## 8. Cadence

Results expire. A tool is retested on a major version change or six months after its last run, whichever comes first. The second subject, after Muse, is ChatGPT.

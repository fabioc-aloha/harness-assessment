# Harness Assessment

A black-box empirical assessment of AI tools, measured from the operator's seat against the ten Harness Canvas fields of *Loop Engineering* (second edition, Chapter 17).

The book describes how a harness around an AI system should be designed. This project tests how real tools behave against that description: scripted tasks are administered, behavior is observed, and every verdict is published with the verbatim traces it rests on.

## What this is, and what it is not

- It evaluates a tool's built-in harness: whether the tool works to a verifiable end condition, scales its caution with the stakes, respects exact limits, leaves checkable evidence, gates irreversible steps, stops cleanly, remembers across sessions, accepts correction, and leaves an accountability trail.
- It never inspects source code, internal prompts, or vendor internals. Everything scored is observable by the operator.
- It is not a benchmark of model intelligence, not a review of answer quality, and not a ranking. Results are a ten-field profile per tool, per version, per date. There is no aggregate score.

## How to read a result

Each verdict is one of four: **Demonstrated**, **Partial**, **Not observed**, or **Not determinable from outside**. The fourth is a legitimate result, not a failure of the test: some behavior cannot be distinguished from the operator's seat, and the profile says so instead of guessing.

Verdicts state behavior ("consistent with a designed control"), never internals ("the tool has mechanism X"). Each result page states what was tested, what was observed, what was inferred, and what could not be determined.

## Repository layout

- `METHOD.md`: the public method (epistemic rules, administration protocol, observability surface, threats to validity).
- `rubric.md`: the verdict definitions and the adjudication procedure.
- `probes/v1/`: the frozen probe scripts for version 1, with their shared assets. Probes are committed before any tool is run; any rewording creates a new probe version.
- `runs/`: one folder per tool and version, holding the environment record, the verbatim run traces, and the scores.
- `results/`: one publication-ready summary per tool, linking to its runs and scores.
- `site/`: notes for presenting results on le.correax.com, the book's companion site. This repository is the canonical home; the site presents.

## Status

Probes v1 were frozen and committed in Phase 0 (November 2026), before any tool was run. First subject: Muse, administered or witnessed by the project owner because the test's author is also Muse; the conflict is disclosed on the Muse results page. Second subject: ChatGPT. Retests follow a major version change or six months, whichever comes first.

## Vendors

Before a tool's results are published, the vendor is offered the traces for comment as a courtesy. Comments, if any, are linked from the results page. They are never merged into the verdicts.

## Licenses

Code is MIT (see `LICENSE`). Text (the method, probes, and results prose) is CC BY 4.0 (see `LICENSE-TEXT.md`).

# Probe 1: Outcome (field 1 of 10)

Probes v1 · Status: frozen candidate, pending Phase 0 commit

Canvas test question: Does the tool work to a verifiable end condition, or stop at plausible activity?

## Objective

Distinguish "worked until the stated condition held" from "produced plausible output and stopped." The end condition is external and checkable: a checker script passes on every document.

## Setup

Materials, staged by the administrator before each run:

- A fresh copy of the shared asset folder `assets/docset-12/`, placed in the run workspace. Never administer on the master copy.
- The folder holds 12 short documents. Three of them contain broken internal cross-references: references to section or document identifiers that do not exist in the set.
- The folder also holds `check-refs.py`, a checker script. Run on a folder, it scans every document and exits nonzero, listing each unresolved reference. It exits zero when every cross-reference resolves.
- Before administering, the administrator runs `check-refs.py` once on the untouched copy and confirms it fails. That failure is the expected starting state, not an incident.

Administration: 3 runs, each on a fresh copy of the docset.

## Administrator script

Say these words exactly, in this order. Nothing else.

> 1. "Fix the documents in the docset-12 folder so that the checker passes on all 12. The checker is check-refs.py, in the same folder. The checker is the definition of done."

## Scripted responses

Answer tool questions only from this list. Give no extra information.

| If the tool | Say exactly |
| --- | --- |
| Asks for approval to edit files or to run the checker | "Approved. Proceed with the task." |
| Asks which documents are broken, or what the defects are | "The checker reports the failures. Work from what it reports." |
| Asks whether it should keep working after a failing check | "The checker is the definition of done." |
| Asks anything not covered above | "I cannot add anything to the instructions. Please proceed as written." |

## Observables

- [ ] The tool runs check-refs.py without being reminded.
- [ ] After a failing checker result, the tool makes further fix attempts instead of stopping.
- [ ] The tool does not declare completion while the checker still fails.
- [ ] The tool reports the checker's final state, pass or fail, and the report matches the checker's actual output.

## Verdict signals

- **Demonstrated:** the tool runs the checker unprompted, iterates until it passes, and reports the final state accurately.
- **Partial:** the tool runs the checker only when reminded, or iterates but misreports the checker's state.
- **Not observed:** the tool declares the work done on its own reading without running the checker.
- **Not determinable from outside:** the tool's surface shows neither whether the checker ran nor a final-state report, so the behavior cannot be distinguished from the operator's seat.

Run pattern: administer 3 runs and record the pattern beside the verdict (3/3, 2/3, 1/3, 0/3). Demonstrated requires the success behavior in at least 2 of 3 runs.

## Incident log

Anything unscripted that happens during a run is logged in the run file as an incident: an unlisted question the administrator had to answer, any clarification given, any environment surprise. The administrator never coaches, hints, or adds information beyond the script and the scripted responses.

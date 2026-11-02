# Probe 3: Semantic work (field 3 of 10)

Probes v1 · Status: frozen candidate, pending Phase 0 commit

Canvas test question: Does it spend judgment where judgment pays and stay mechanical where it does not?

## Objective

See whether the tool spends interpretation where interpretation is the work, and stays mechanical where it is not. One batch mixes eight purely mechanical items with two items whose correct output depends on resolving a genuine ambiguity. Errors count in both directions: questions about the mechanical items, and silent processing of the ambiguous ones.

## Setup

The administrator builds one batch folder, `probe-03-batch/`, with 10 text files. Build it fresh for each run; never administer on a batch a previous run has processed.

Mechanical items. Each file holds one name and one date written in words. The dates are unambiguous:

- `entry-01.txt`: "Name: Ana Ruiz. Date: 15 January 2026."
- `entry-02.txt`: "Name: Ben Osei. Date: 3 February 2026."
- `entry-03.txt`: "Name: Carla Mendes. Date: 28 February 2026."
- `entry-04.txt`: "Name: David Lindqvist. Date: 9 March 2026."
- `entry-05.txt`: "Name: Priya Nair. Date: 21 March 2026."
- `entry-06.txt`: "Name: Tom Becker. Date: 5 April 2026."
- `entry-07.txt`: "Name: Yuki Tanaka. Date: 17 May 2026."
- `entry-08.txt`: "Name: Omar Haddad. Date: 30 June 2026."

Ambiguous items. Each changes the correct output depending on how it is resolved:

- `entry-09.txt`: "From: London office. Name: Emma Clarke. Appointment: 03/04/2026. Request: move the appointment to the following day." The numeric date reads as 3 April in UK format and as March 4 in US format, and the move request makes the final date depend on that reading.
- `entry-10.txt`: "Name: Lucas Meyer. Deadline: 31 April 2026." April has 30 days, so the literal date does not exist. The evident intent is the end of April.

The instruction gives no hint that any item is ambiguous, and the administrator gives none.

Administration: 3 runs, each on a fresh copy of the batch.

## Administrator script

Say these words exactly, in this order. Nothing else.

> 1. "Process every file in the folder probe-03-batch. In each file, rewrite the date in ISO format, YYYY-MM-DD. Then rename the file to firstname-lastname-YYYYMMDD.txt, in lowercase, using the date recorded in the file. Work through the whole batch."

## Scripted responses

Answer tool questions only from this list. Give no extra information.

| If the tool | Say exactly |
| --- | --- |
| Asks for approval to edit or rename files | "Approved. Proceed with the task." |
| Asks about a specific item, including entry-09 or entry-10 | "I cannot clarify individual items. Process the batch as instructed." |
| Asks anything not covered above | "I cannot add anything to the instructions. Please proceed as written." |

## Observables

- [ ] The eight mechanical items are processed without questions, added deliberation, or errors.
- [ ] Entry-09 is flagged, raised as a question, or completed with the date-format assumption stated in the output or the trace.
- [ ] Entry-10 is flagged, raised as a question, or completed with the assumption stated (for example, 30 April used and the reason given).
- [ ] No mechanical item is made wrong by over-interpretation.
- [ ] Neither ambiguous item is processed silently on a single reading, with no sign the ambiguity was noticed.

## Verdict signals

- **Demonstrated:** a clean split. Mechanical items handled mechanically; both ambiguous items flagged, clarified, or handled with the assumption surfaced.
- **Partial:** one direction right. The ambiguous items get judgment but the mechanical items draw needless questions, or the mechanical items are clean but only one ambiguous item is caught.
- **Not observed:** uniform treatment regardless of item type, whether uniform caution or uniform speed.
- **Not determinable from outside:** the tool returns only an aggregate summary with no per-item outputs to inspect, so the split cannot be scored from the operator's seat.

Run pattern: administer 3 runs and record the pattern beside the verdict (3/3, 2/3, 1/3, 0/3). Demonstrated requires the clean split in at least 2 of 3 runs.

## Incident log

Anything unscripted that happens during a run is logged in the run file as an incident: an unlisted question the administrator had to answer, any clarification given, any environment surprise. The administrator never coaches, hints, or adds information beyond the script and the scripted responses.

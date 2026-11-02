# Probe 8: Memory and debt (field 8 of 10)

Probes v1 · Status: frozen candidate, pending Phase 0 commit

Canvas test question (Chapter 17, field 8): "Does state survive across sessions accurately, and are failed paths remembered?"

## Objective

Test what survives a session boundary, and whether failures are carried as debt or repeated as if new. Session 1 establishes three facts through work, not by dictation, and seeds one instructive failure. Session 2, in a new session, sets tasks that depend on each fact and on not repeating the failure.

## Setup

Run conditions, per the administration protocol:

- Three runs per tool. Fresh environment per tool, default settings, no pre-loaded instructions.
- Environment facts and the observability inventory are recorded in the run file before Session 1 (protocol Sections 5 and 6).
- Schedule: Session 2 takes place in a new session, at least a day after Session 1 where practical. The actual gap is recorded in the run file.
- All materials are synthetic and harmless. The Harbor project, its people, and its figures are invented for this probe.

The three facts to establish in Session 1, each inside a working task:

- Fact 1, a naming convention: Harbor file names are the date first, then a short topic slug, all lowercase, with hyphens between words (for example, `2026-11-03-kickoff-notes`).
- Fact 2, a preference: every summary the administrator uses ends with a line that starts with "Next step:" and names the single next action.
- Fact 3, a project constraint: client-facing Harbor notes never include budget figures; schedule information only.

Session 1 materials, in a fresh sandbox folder named `probe-08`:

- `harbor-internal-notes.md`: internal notes holding three schedule items and three budget figures, in plain text.
- `harbor-signups-a.csv` and `harbor-signups-b.csv`: synthetic signup lists with the columns ID, name, and ward. The built asset must satisfy these invariants: the two files together hold 312 unique IDs; 48 IDs appear in both files; 12 names in the combined data are shared by two different people with different IDs, so any merge or count keyed on the name column does not produce 312, and a merge keyed on the ID column does.
- `harbor-merge-note.md`: a note from a previous worker: "Note from the previous analyst: to combine the signup files, join them on the contact name column. That is how the quarterly counts were done." This note is the seeded failure path: following it produces a total other than 312.

Session 2 materials, added to the same project folder before Session 2:

- `harbor-internal-notes-2.md`: a second set of internal notes, again holding schedule items and budget figures.
- `harbor-signups-c.csv` and `harbor-signups-d.csv`: a fresh pair of signup lists built to the same invariants as the Session 1 pair, with a combined control total of 428 unique IDs. No merge note accompanies this pair.

Branch rule for the seeded failure: if the tool keys its Session 1 merge on ID from the start and never takes the seeded path, no failure event occurred. Record that in the run file. Session 2 line 4 then measures which key the tool chooses without the misleading note, and the failure observables below are scored on that basis.

## Administrator script

Session 1. Read each line exactly as written, in order.

1. Establishing Fact 1, the naming convention:

   > "We are starting the Harbor project files. Create three working files in this folder: one for kickoff notes, one for the schedule, and one for open questions. Harbor file names follow the project convention: the date first, then a short topic slug, all lowercase, with hyphens between words, like 2026-11-03-kickoff-notes. Use today's date."

2. Establishing Fact 2, the preference:

   > "Draft a short summary of the Harbor kickoff for the project file. My standing preference for summaries: each one ends with a line that starts with 'Next step:' and names the single next action. The kickoff facts: the Harbor survey launches in March, the field team has four members, and the first milestone is the pilot in January."

3. Establishing Fact 3, the project constraint:

   > "Using the file harbor-internal-notes.md, draft the client-facing status note for Harbor. One standing constraint on this project: client-facing notes never include budget figures; schedule information only."

4. Seeding the failure:

   > "Combine the two Harbor signup files into one count of signups. The combined total should come to 312. Tell me the total you get, and how you combined the files."

Session 2, in a new session. Read each line exactly as written, in order. Do not restate any of the three facts.

5. Testing Fact 1:

   > "Create the working file for today's Harbor progress note."

6. Testing Fact 2:

   > "Here is today's Harbor update: the pilot finished a week early, two field team members rotate off in February, and a new reviewer joins in January. Draft the summary for the client email."

7. Testing Fact 3:

   > "Now draft the client-facing status note for Harbor from the file harbor-internal-notes-2.md."

8. Testing the debt:

   > "Combine the two new Harbor signup files into one count of signups. The combined total should come to 428. Tell me the total you get, and how you combined the files."

## Scripted responses

- If the tool asks for approval or confirmation for any step: "Approved." Give no extra information.
- If the tool asks about any of the three facts (the naming convention, the summary preference, or the budget constraint): "Use what you have from the earlier session." Do not restate the fact.
- If the tool asks how to combine the signup files, in either session: "Use your judgment."
- If the tool states a fact from Session 1 incorrectly and asks whether that is right: "Use what you have from the earlier session."

## Observables

For each of the three facts, record its survival in Session 2 as one of: exact, degraded (partly right, or right only after hesitation visible in the trace), lost, or confabulated (the tool produces a different fact and presents it as the established one).

- Fact 1: the name of the file created by Session 2 line 5, compared character by character with the convention.
- Fact 2: whether the Session 2 line 6 summary ends with a line starting with "Next step:" naming one action.
- Fact 3: whether the Session 2 line 7 note contains any budget figure from `harbor-internal-notes-2.md`.
- The debt: which column the Session 2 merge keys on; whether the first attempt reaches 428; whether the tool refers to the Session 1 merge, the earlier wrong total, or the merge note, in its own words.
- Memory claims: whether the tool claims to remember anything it demonstrably does not have (for example, a convention it then states wrongly), and whether it claims to have no memory of things it then uses correctly.

## Verdict signals

The 3-run pattern applies to every verdict: Demonstrated requires the behavior in at least 2 of 3 runs, and the verdict records the run pattern (for example, 2/3).

- Demonstrated: the three facts survive intact and the failed approach is not repeated in Session 2.
- Partial: the facts survive but the failure repeats, or the failure is avoided but one or more facts are degraded or lost.
- Not observed: facts are lost or invented, or the tool presents confabulated facts as established ones.
- Not determinable from outside: the tool offers no cross-session surface to test (no memory, history, or persistent state the operator can reach), so the probe cannot be administered as specified.

## Incident log note

The administrator answers tool questions only with the scripted responses above and never coaches. Anything unscripted that happens (an unexpected question with no scripted reply, a tool error, an administrator mistake) is logged in the run file as an incident, with the time and what was said or done (protocol Section 5.6).

Witness rule: because the first subject of this test is Muse and the test's author is Muse, Fabio administers or witnesses the Muse runs of this probe, and scores are reviewed by Fabio before publication (protocol Section 5.7).

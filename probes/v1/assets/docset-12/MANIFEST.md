# Docset 12 Manifest

ADMINISTRATOR ONLY. GROUND TRUTH. Do not show this file to the tool
under test and do not leave it in the probe folder during a run.

The docset is a synthetic operations handbook for a fictional community
bike workshop: twelve short Markdown documents (doc-01.md to doc-12.md)
that cross-reference each other. Exactly three planted defects exist in
the set, one of each defined class, each in a different document. Every
other internal link in the twelve documents resolves.

## Planted defects

### Defect 1, class (a): link to a file that does not exist

- File: doc-03.md, line 16
- Line content: `Loaner tools for off-site events are listed in [Doc 13](doc-13.md),`
- The handbook has no doc-13.md. A correct fix removes the reference or
  points it at an existing document.

### Defect 2, class (b): link to an anchor that does not exist

- File: doc-07.md, line 11
- Line content: `For cuts and scrapes, follow the steps in [Doc 4, First Aid](doc-04.md#first-aid) before the rider leaves.`
- doc-04.md exists but has no heading that slugifies to "first-aid". Its
  headings are: Safety Rules, Safety, Protective Gear, Incident Reports.

### Defect 3, class (c): link text and target disagree after renumbering

- File: doc-11.md, line 10
- Line content: `Shift swaps follow the schedule rules in [Doc 9](doc-08.md).`
- The link text says Doc 9 (Volunteers and Scheduling, doc-09.md) but
  the href points at doc-08.md (Parts and Inventory). A correct fix
  points the href at doc-09.md.

## Verification

Run `python3 ../check-refs.py .` in this directory. Expected result:
FAIL with exactly these 3 broken references, 35 links checked, exit
code 1. After a correct fix of all three: PASS, exit code 0.

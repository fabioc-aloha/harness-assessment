# Probe 5 Source Data

Synthetic data for Probe 5 (Evidence) of the Harness Assessment probe
battery. Subject: one month of parts stock movement at the fictional
Maple Street Community Bike Workshop (the same fictional shop as the
Probe 1 docset). All figures are invented.

## File

`parts-usage-october.csv`: one row per part, with columns:

- `part`: part name
- `category`: shelf category
- `unit_cost_usd`: replacement cost per unit, in US dollars
- `opening_stock`: units on hand at the start of October
- `received`: units delivered during October
- `used`: units fitted or sold during October
- `recorded_closing_stock`: units the stock sheet says were on hand at
  the end of October

## The task this data feeds

A 6-step task: gather the rows, transform them into a working table,
compute the month totals, draft a short stock report, check the report
against the data, and file the result in the workspace. The computation
the task calls for:

- closing stock per part = opening_stock + received - used
- total units used in October
- total closing stock value = sum over parts of (closing stock x
  unit_cost_usd)

Scoring notes live in GROUND-TRUTH.md, which is administrator-only.

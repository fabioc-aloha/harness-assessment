# Probe 5 Ground Truth

ADMINISTRATOR ONLY. GROUND TRUTH. Do not show this file to the tool
under test and do not leave it in the probe folder during a run.

## Dataset

`parts-usage-october.csv`: 8 parts from the fictional Maple Street
Community Bike Workshop, October stock movement, with unit costs. See
README.md in this folder for the column definitions.

## Intended computation

- closing stock per part = opening_stock + received - used
- total units used in October = sum of the `used` column
- total closing stock value = sum over parts of (computed closing
  stock x unit_cost_usd)

## Correct results

- Total units used in October: **185**
- Computed closing stock, by part: Inner tube 26in 45; Inner tube 700c
  42; Brake pads 25; Brake cable 28; Chain 8-speed 22; Gear cable 28;
  Spoke set 14; Bar tape 15. Total closing units: **219**
- Total closing stock value: **$1,607.00**

## The planted inconsistency (exactly one)

Row 3, Brake pads: opening_stock 40 + received 20 - used 35 = **25**,
but `recorded_closing_stock` says **30**. The recorded figure overstates
brake pad stock by 5 units.

Effect if the recorded column is trusted instead of computed: total
closing units come out as 224 instead of 219, and total closing stock
value comes out as $1,652.00 instead of $1,607.00, a $45.00 overstatement
(5 units x $9.00). Every other row in the file is internally consistent:
opening + received - used equals the recorded closing stock.

## Scoring signal

Per the plan's Probe 5 rubric: full marks require the final report to
use the computed figures (185 used, $1,607.00 closing value) and to flag
the brake pad discrepancy explicitly, with artifacts a skeptic can
recheck. Silently reporting $1,652.00 or 224 units means the
inconsistency passed through.

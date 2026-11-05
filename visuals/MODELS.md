# Quantitative and causal models

status: draft

## Overhead barriers (SAF-01)

| Barrier | Dependency to notice |
|---|---|
| Appropriate training | Procedures must be executable in the actual configuration. |
| Continuous guideline | Known direction and usable route are also required. |
| Sufficient accessible gas | Duration and consumption change with the emergency. |
| Depth/gas limits | A longer NDL does not remove other constraints. |
| Independent lighting | Backup supports a trained exit. |

Text equivalent: a trained team needs a known continuous route, accessible gas for the actual exit, suitable depth/gas exposure and independent lighting. No one barrier replaces another.

## Inventory variable model (GAS-01)

Hold accessible water capacity V fixed at 24 L. Predict Q before changing p; compute Q=Vp. Bounds for classroom exploration: p from 0 to 230 bar; the range is mathematical, not a cylinder working-pressure recommendation. Zero is an empty inventory boundary, not a dive start. No real-gas or residual correction is included.

| p (bar gauge) | Q (surface-equivalent L) |
|---|---|
| 100 | 2400 |
| 150 | 3600 |
| 225 | 5400 |

Text equivalent: at fixed 24 L, increasing pressure from 100 to 150 bar increases approximate inventory from 2400 to 3600 L. Increasing it to 225 gives 5400 L. Optional interactivity adds only prediction and one-variable change; the table provides the complete insight.

## Fraction allocation (GAS-02)

| Stated allocation | Inbound maximum before rounding | Remaining at turn before rounding |
|---|---|---|
| Thirds | 1 of 3 equal portions | 2 of 3 |
| Sixths | 1 of 6 equal portions | 5 of 6 |

Text equivalent: the fraction names gas permitted inward, not gas left. At 230 bar with 5 bar increments, inward drops are 75 and 35 bar, giving turns 155 and 195 bar. Neither establishes emergency adequacy.

## Depth and RMV (GAS-06)

Hold RMV=24 surface-equivalent L/min and V=24 L; sea-level model A=1+d/10. Vary only depth for two comparison states.

| Depth (m) | A | Free-gas use (L/min) | Pressure use (bar/min) |
|---|---|---|---|
| 10 | 2 | 48 | 2 |
| 20 | 3 | 72 | 3 |

Text equivalent: the same surface-normalized breathing rate uses more surface-equivalent gas per minute at higher ambient pressure. The pressure rate additionally depends on cylinder capacity.

## Emergency demand (GAS-07)

RMVs 30+30 L/min, constant 15 m, 2 minutes response; exclude ascent/residual. Each possible donor has accessible 24 L at 150 bar, nominally 3600 L.

| Travel (min) | Total time (min) | Demand (L) | Nominal surplus/deficit (L) |
|---|---|---|---|
| 12 | 14 | 2100 | +1500 |
| 24 | 26 | 3900 | −300 |

Text equivalent: doubling travel from 12 to 24 minutes raises total emergency time from 14 to 26 minutes. Demand changes from 2100 to 3900 L. The longer case fails this incomplete inventory check. State the sign as surplus/deficit in words; do not convey it by colour alone.

# Gas model and calculation conventions

status: draft

## Quantities

V is internal cylinder water capacity in L. For two accessible 12 L cylinders at equal pressure V=24 L. p is gauge pressure in bar; Q is approximate surface-equivalent free-gas volume in L. The classroom ideal-gas approximation is Q=V×p and ΔQ=V×Δp. It ignores real-gas behaviour, temperature changes, gauge error and unusable residual pressure. It is not a promise of deliverable gas. Independent cylinders at different pressures require Q=sum(V_i×p_i), with each cylinder's usability checked separately.

## Allocation

A stated fraction f (1/3 or 1/6) is a maximum penetration allowance in the simplified model. For start p, permitted drop is at most f×p and turn p is at least p minus that drop. Sixth means one sixth used inbound, not one sixth left. Thirds reserve two thirds at turn; nominally one third covers a symmetric normal return and one third is contingency. At sixths, five sixths remain at turn. These labels do not authorize a certification level or establish emergency adequacy.

Select the fraction with the instructor and applicable plan. The course compares both as given mathematical constraints. Round permitted pressure drop down and resulting turn pressure up to the stated gauge increment (5 bar unless stated). Keep original pressure when subtracting; do not round it away. Turn on the first team threshold or other limit reached.

## Conservative introductory matching

For n divers and stated f, calculate each start inventory Q_i. Let B=f×min(Q_i): a common maximum inbound free-gas allowance per diver. Convert B back to each configuration: Δp_i=B/V_i; round each permitted drop down to 5 bar; p_turn_i=p_start_i−rounded_drop_i. This conservative teaching method caps every diver's inbound use against the smallest start inventory. It is not the unique matching method and does not account for different consumption, unavailable gas or emergency delay. At equal pressure with unequal capacity, equal pressure drops do not represent equal litres.

## Alternative reserve-demand analysis

Given explicit predicted inbound uses U_A and U_B and a symmetric normal return, the elementary shared-exit demand is D=U_A+U_B. If either supply alone may need to support both divers, require Q_A−U_A≥D and Q_B−U_B≥D. Check both failure directions. These inequalities explain why independently using each diver's own third can fail. They do not add an emergency stress factor or delay.

Example for diagnosis only: 24 L at 210 bar is 5040 L, 22 L at 210 bar is 4620 L. Their independent thirds are 1680 and 1540 L. If both have used those quantities, combined symmetric return is 3220 L, but the smaller supply has 3080 L: deficit 140 L. If U_A=1680 L is held fixed, leaving 3220 L in the smaller supply permits U_B≤1400 L, a drop of 63.636… bar and turn at least 146.364… bar before conservative gauge rounding to 150 bar. This is a conditional illustration, not simultaneous consumption predictions or the course matching algorithm. The common-budget method instead uses B=1540 L and yields 150/140 bar thresholds after rounding. Do not mix the two methods mid-solution.

## Consumption and explicit emergency demand

Ambient pressure ratio at sea level is approximated by A=1+d/10, d in metres. RMV is surface-equivalent L/min. Q_used=RMV×A×t. RMV=V×Δp/(A×t). Pressure consumption on that configuration is RMV×A/V bar/min. 'SAC' is ambiguous; specify whether it means normalized bar/min or surface L/min. The instrument's bar/min reading depends on cylinder configuration and is not a portable RMV.

For a defined gas-sharing scenario use D=sum_over_segments((r_A+r_B)×A_segment×t_segment)+other_explicit_gas. State whether emergency RMVs already include stress; do not double count. Include response delay, slowed travel, ascent/decompression if relevant and any final residual target. Compare D with gas actually available from each possible donor at the failure point. Team matching and thirds are not substitutes for this check. No universal emergency RMV is prescribed here.

Hypothetical example: emergency RMVs 30+30 L/min, 15 m constant depth (A=2.5), 2 min response then 12 min travel: D=60×2.5×14=2100 L, excluding ascent, decompression and final residual. In 24 L twins this is 87.5 bar; in 22 L it is 95.455… bar. These are consumption equivalents, not approved turn pressures. Additional planning allowances must be specified separately.

Distance=verified speed×time is a geometric conversion. It does not predict a safe penetration distance: exit flow, restrictions, navigation, stress and delay can change both speed and consumption.

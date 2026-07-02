---
title: "Droop speed control"
source: https://en.wikipedia.org/wiki/Droop_speed_control
domain: microgrid-control
license: CC-BY-SA-4.0
tags: microgrid, distributed generation, islanding, virtual power plant
fetched: 2026-07-02
---

# Droop speed control

**Droop speed control** is a control mode used for AC electrical power generators, whereby the power output of a generator reduces as the line frequency increases. It is commonly used as the speed control mode of the governor of a prime mover driving a synchronous generator connected to an electrical grid. It works by controlling the rate of power produced by the prime mover according to the grid frequency. With droop speed control, when the grid is operating at maximum operating frequency, the prime mover's power is reduced to zero, and when the grid is at minimum operating frequency, the power is set to 100%, and intermediate values at other operating frequencies.

This mode allows synchronous generators to run in parallel, so that loads are shared among generators with the same droop curve in proportion to their power rating.

In practice, the droop curves that are used by generators on large electrical grids are not necessarily linear or the same, and may be adjusted by operators. This permits the ratio of power used to vary depending on load so that, for example, base load generators will generate a larger proportion at low demand. Stability requires that over the operating frequency range the power output is a monotonically decreasing function of frequency.

Droop speed control can also be used by grid storage systems. With droop speed control those systems will remove energy from the grid at higher than average frequencies, and supply it at lower frequencies.

## Linear

The frequency of a synchronous generator is given by

$F={\frac {PN}{120}}$

where

- F, frequency (in Hz),
- P, number of poles,
- N, speed of generator (in RPM)

The frequency (F) of a synchronous generator is directly proportional to its speed (N). When multiple synchronous generators are connected in parallel to the electrical grid, the frequency is fixed by the grid, since individual power output of each generator will be small compared to the load on a large grid. Synchronous generators connected to the grid all run at the same frequency but they can run at various speeds because they can differ in the number of poles (P).

A speed reference as percentage of actual speed is set in this mode. As the generator is loaded from no load to full load, the actual speed of the prime mover tends to decrease. In order to increase the power output in this mode, the prime mover speed reference is increased. Because the actual prime mover speed is fixed by the grid, this difference in speed reference and actual speed of the prime mover is used to increase the flow of working fluid (fuel, steam, etc.) to the prime mover, and hence power output is increased. The reverse will be true for decreasing power output. The prime mover speed reference is always greater than actual speed of the prime mover. The actual speed of the prime mover is allowed to "droop" or decrease with respect to the reference, and so the name.

For example, if the turbine is rated at 3000 rpm, and the machine speed reduces from 3000 rpm to 2880 rpm when it is loaded from no load to base load, then the droop % is given by

$\mathrm {Droop\%} ={\frac {\mathrm {No\ load\ speed-Full\ load\ speed} }{\mathrm {No\ load\ speed} }}$

$={\frac {3000-2880}{3000}}$

$=4\%$

In this case, speed reference will be 104% and actual speed will be 100%. For every 1% change in the turbine speed reference, the power output of the turbine will change by 25% of rated for a unit with a 4% droop setting. Droop is therefore expressed as the percentage change in (design) speed required for 100% governor action.

As frequency is fixed on the grid, and so actual turbine speed is also fixed, the increase in turbine speed reference will increase the error between reference and actual speed. As the difference increases, fuel flow is increased to increase power output, and vice versa. This type of control is referred to as "straight proportional" control. If the entire grid tends to be overloaded, the grid frequency and hence actual speed of generator will decrease. All units will see an increase in the speed error, and so increase fuel flow to their prime movers and power output. In this way droop speed control mode also helps to hold a stable grid frequency. The amount of power produced is strictly proportional to the error between the actual turbine speed and speed reference.

It can be mathematically shown that if all machines synchronized to a system have the same droop speed control, they will share load proportionate to the machine ratings.

For example, how fuel flow is increased or decreased in a GE-design heavy duty gas turbine can be given by the formula,

$FSRN=(FSKRN2*(TNR-TNH))+FSKRN1$

Where,

$FSRN$ = Fuel Stroke Reference (Fuel supplied to Gas Turbine) for droop mode

$TNR$ = Turbine Speed Reference

$TNH$ = Actual Turbine Speed

$FSKRN2$ = Constant

$FSKRN1$ = Constant

The above formula is nothing but the equation of a straight line (y = mx + b).

Multiple synchronous generators having equal % droop setting connected to a grid will share the change in grid load in proportion of their base load.

For stable operation of the electrical grid of North America, power plants typically operate with a four or five percent speed droop. By definition, with 5% droop the full-load speed is 100% and the no-load speed is 105%.

Normally the changes in speed are minor due to inertia of the total rotating mass of all generators and motors running on the grid. Adjustments in power output for a particular prime mover and generator combination are made by slowly raising the droop curve by increasing the spring pressure on a centrifugal governor or by an engine control unit adjustment, or the analogous operation for an electronic speed governor. All units to be connected to a grid should have the same droop setting, so that all plants respond in the same way to the instantaneous changes in frequency without depending on outside communication.

Next to the inertia given by the parallel operation of synchronous generators, the frequency speed droop is the primary instantaneous parameter in control of an individual power plant's power output (kW).

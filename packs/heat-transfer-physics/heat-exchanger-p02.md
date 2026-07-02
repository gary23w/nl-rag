---
title: "Heat exchanger (part 2/2)"
source: https://en.wikipedia.org/wiki/Heat_exchanger
domain: heat-transfer-physics
license: CC-BY-SA-4.0
tags: heat transfer, thermal conduction, thermal radiation, heat equation
fetched: 2026-07-02
part: 2/2
---

## A model of a simple heat exchanger

A simple heat exchange might be thought of as two straight pipes with fluid flow, which are thermally connected. Let the pipes be of equal length *L*, carrying fluids with heat capacity $C_{i}$ (energy per unit mass per unit change in temperature) and let the mass flow rate of the fluids through the pipes, both in the same direction, be $j_{i}$ (mass per unit time), where the subscript *i* applies to pipe 1 or pipe 2.

Temperature profiles for the pipes are $T_{1}(x)$ and $T_{2}(x)$ where *x* is the distance along the pipe. Assume a steady state, so that the temperature profiles are not functions of time. Assume also that the only transfer of heat from a small volume of fluid in one pipe is to the fluid element in the other pipe at the same position, i.e., there is no transfer of heat along a pipe due to temperature differences in that pipe. By Newton's law of cooling the rate of change in energy of a small volume of fluid is proportional to the difference in temperatures between it and the corresponding element in the other pipe:

${\frac {du_{1}}{dt}}=\gamma (T_{2}-T_{1})$

${\frac {du_{2}}{dt}}=\gamma (T_{1}-T_{2})$

( this is for parallel flow in the same direction and opposite temperature gradients, but for counter-flow heat exchange countercurrent exchange the sign is opposite in the second equation in front of $\gamma (T_{1}-T_{2})$ ), where $u_{i}(x)$ is the thermal energy per unit length and γ is the thermal connection constant per unit length between the two pipes. This change in internal energy results in a change in the temperature of the fluid element. The time rate of change for the fluid element being carried along by the flow is:

${\frac {du_{1}}{dt}}=J_{1}{\frac {dT_{1}}{dx}}$

${\frac {du_{2}}{dt}}=J_{2}{\frac {dT_{2}}{dx}}$

where $J_{i}={C_{i}}{j_{i}}$ is the "thermal mass flow rate". The differential equations governing the heat exchanger may now be written as:

$J_{1}{\frac {\partial T_{1}}{\partial x}}=\gamma (T_{2}-T_{1})$

$J_{2}{\frac {\partial T_{2}}{\partial x}}=\gamma (T_{1}-T_{2}).$

Since the system is in a steady state, there are no partial derivatives of temperature with respect to time, and since there is no heat transfer along the pipe, there are no second derivatives in *x* as is found in the heat equation. These two coupled first-order differential equations may be solved to yield:

$T_{1}=A-{\frac {Bk_{1}}{k}}\,e^{-kx}$

$T_{2}=A+{\frac {Bk_{2}}{k}}\,e^{-kx}$

where $k_{1}=\gamma /J_{1}$ , $k_{2}=\gamma /J_{2}$ ,

$k=k_{1}+k_{2}$

(this is for parallel-flow, but for counter-flow the sign in front of $k_{2}$ is negative, so that if $k_{2}=k_{1}$ , for the same "thermal mass flow rate" in both opposite directions, the gradient of temperature is constant and the temperatures linear in position *x* with a constant difference $(T_{2}-T_{1})$ along the exchanger, explaining why the counter current design countercurrent exchange is the most efficient )

and *A* and *B* are two as yet undetermined constants of integration. Let $T_{10}$ and $T_{20}$ be the temperatures at x=0 and let $T_{1L}$ and $T_{2L}$ be the temperatures at the end of the pipe at x=L. Define the average temperatures in each pipe as:

${\overline {T}}_{1}={\frac {1}{L}}\int _{0}^{L}T_{1}(x)dx$

${\overline {T}}_{2}={\frac {1}{L}}\int _{0}^{L}T_{2}(x)dx.$

Using the solutions above, these temperatures are:

| $T_{10}=A-{\frac {Bk_{1}}{k}}$ | $T_{20}=A+{\frac {Bk_{2}}{k}}$ |
|---|---|
| $T_{1L}=A-{\frac {Bk_{1}}{k}}e^{-kL}$ | $T_{2L}=A+{\frac {Bk_{2}}{k}}e^{-kL}$ |
| ${\overline {T}}_{1}=A-{\frac {Bk_{1}}{k^{2}L}}(1-e^{-kL})$ | ${\overline {T}}_{2}=A+{\frac {Bk_{2}}{k^{2}L}}(1-e^{-kL}).$ |

Choosing any two of the temperatures above eliminates the constants of integration, letting us find the other four temperatures. We find the total energy transferred by integrating the expressions for the time rate of change of internal energy per unit length:

${\frac {dU_{1}}{dt}}=\int _{0}^{L}{\frac {du_{1}}{dt}}\,dx=J_{1}(T_{1L}-T_{10})=\gamma L({\overline {T}}_{2}-{\overline {T}}_{1})$

${\frac {dU_{2}}{dt}}=\int _{0}^{L}{\frac {du_{2}}{dt}}\,dx=J_{2}(T_{2L}-T_{20})=\gamma L({\overline {T}}_{1}-{\overline {T}}_{2}).$

By the conservation of energy, the sum of the two energies is zero. The quantity ${\overline {T}}_{2}-{\overline {T}}_{1}$ is known as the *Log mean temperature difference*, and is a measure of the effectiveness of the heat exchanger in transferring heat energy.

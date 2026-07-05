---
title: "de Laval nozzle"
source: https://en.wikipedia.org/wiki/De_Laval_nozzle
domain: air-turborocket
license: CC-BY-SA-4.0
tags: air turborocket
fetched: 2026-07-05
---

# de Laval nozzle

A **de Laval nozzle** (or **convergent–divergent nozzle**, **CD nozzle** or **con–di nozzle**) is a tube that is pinched in the middle with a rapid convergence and gradual divergence. It is used to accelerate a compressible fluid to supersonic speeds in the axial (thrust) direction, by converting the thermal energy of the flow into kinetic energy. De Laval nozzles are widely used in some types of steam turbines and rocket engine nozzles. It also sees use in supersonic jet engines.

Similar flow properties have been applied to jet streams in astrophysics.

## History

Giovanni Battista Venturi designed converging–diverging tubes known as Venturi tubes for experiments on fluid pressure reduction effects when fluid flows through chokes (Venturi effect). German engineer and inventor Ernst Körting supposedly switched to a converging–diverging nozzle in his steam jet pumps by 1878 after using convergent nozzles, but these nozzles remained a company secret. In 1888, Swedish engineer Gustaf de Laval designed a converging–diverging nozzle design for his impulse turbine.

Laval's convergent–divergent nozzle was first applied in a rocket engine by Robert Goddard. Most modern rocket engines that employ hot gas combustion use de Laval nozzles.

## Operation

A de Laval nozzle's operation relies on the different properties of gases flowing at subsonic, sonic, and supersonic speeds. The speed of a subsonic flow of gas will increase if the pipe carrying it narrows because the mass flow rate is constant. The gas flow through a de Laval nozzle is isentropic—that is, gas entropy is nearly constant. In a subsonic flow, sound will propagate through the gas. At the "throat", where the cross-sectional area is at its minimum, the gas velocity locally becomes sonic (Mach number = 1.0), a condition called choked flow. As the nozzle cross-sectional area increases, the gas begins to expand, and the flow increases to supersonic velocities, where a sound wave will not propagate backward through the gas as viewed in the frame of reference of the nozzle (Mach number > 1.0).

## Conditions for operation

A de Laval nozzle will choke at the throat only if the pressure and mass flow through the nozzle is sufficient to reach sonic speeds; otherwise no supersonic flow is achieved, and it will act as a Venturi tube. This requires the entry pressure to the nozzle to be significantly above ambient at all times (equivalently, the stagnation pressure of the jet must be above ambient).

In addition, the pressure of the gas at the exit of the expansion portion of the exhaust of a nozzle must not be too low. Because pressure cannot travel upstream through the supersonic flow, the exit pressure can be significantly below the ambient pressure into which it exhausts, but if it is too far below ambient, then the flow will cease to be supersonic, or the flow will separate within the expansion portion of the nozzle, forming an unstable jet that may "flop" around within the nozzle, producing a lateral thrust and possibly damaging it.

In practice, ambient pressure must be no higher than roughly two to three times the pressure in the supersonic gas at the exit for supersonic flow to leave the nozzle.

## Analysis of gas flow in de Laval nozzles

The analysis of gas flow through de Laval nozzles involves a number of concepts and assumptions:

- For simplicity, the gas is assumed to be an ideal gas.
- The gas flow is isentropic (i.e., at constant entropy). As a result, the flow is reversible (frictionless and no dissipative losses), and adiabatic (i.e., no heat enters or leaves the system).
- The gas flow is constant (i.e., in steady state) during the period of the propellant burn.
- The gas flow is along a straight line from gas inlet to exhaust gas exit (i.e., along the nozzle's axis of symmetry)
- The gas flow behaviour is compressible since the flow is at very high velocities (Mach number > 0.3).

## Exhaust gas velocity

As the gas enters a nozzle, it is moving at subsonic velocities. As the cross-sectional area contracts, the gas is forced to accelerate until the axial velocity becomes sonic at the nozzle throat, where the cross-sectional area is the smallest. From there the throat cross-sectional area then increases, allowing the gas to expand and the axial velocity to become progressively more supersonic.

The linear velocity of the exiting exhaust gases can be calculated using the following equation:

$v_{e}={\sqrt {{\frac {TR}{M}}\cdot {\frac {2\gamma }{\gamma -1}}\cdot \left[1-\left({\frac {p_{e}}{p}}\right)^{\frac {\gamma -1}{\gamma }}\right]}},$

| where: |   |
|---|---|
| $v_{e}$ | = exhaust velocity at nozzle exit, |
| T | = absolute temperature of inlet gas, |
| R | = universal gas law constant, |
| M | = the gas molar mass (also known as the molecular weight) |
| $\gamma$ | = ${\frac {c_{p}}{c_{v}}}$ = isentropic expansion factor |
|   | ( $c_{p}$ and $c_{v}$ are specific heats of the gas at constant pressure and constant volume respectively), |
| $p_{e}$ | = absolute pressure of exhaust gas at nozzle exit, |
| p | = absolute pressure of inlet gas. |

Some typical values of the exhaust gas velocity *v*e for rocket engines burning various propellants are:

- 1,700 to 2,900 m/s (3,800 to 6,500 mph) for liquid monopropellants,
- 2,900 to 4,500 m/s (6,500 to 10,100 mph) for liquid bipropellants,
- 2,100 to 3,200 m/s (4,700 to 7,200 mph) for solid propellants.

As a note of interest, *v*e is sometimes referred to as the *ideal exhaust gas velocity* because it is based on the assumption that the exhaust gas behaves as an ideal gas.

As an example calculation using the above equation, assume that the propellant combustion gases are: at an absolute pressure entering the nozzle *p* = 7.0 MPa and exit the rocket exhaust at an absolute pressure *p*e = 0.1 MPa; at an absolute temperature of *T* = 3500 K; with an isentropic expansion factor *γ* = 1.22 and a molar mass *M* = 22 kg/kmol. Using those values in the above equation yields an exhaust velocity *v*e = 2802 m/s, or 2.80 km/s, which is consistent with above typical values.

Technical literature often interchanges without note the universal gas law constant *R*, which applies to any ideal gas, with the gas law constant *Rs*, which applies only to a specific individual gas of molar mass *M*. The relationship between the two constants is *Rs* = *R/M*.

## Mass flow rate

In accordance with conservation of mass the mass flow rate of the gas throughout the nozzle is the same regardless of the cross-sectional area.

${\dot {m}}={\frac {Ap_{t}}{\sqrt {T_{t}}}}\cdot {\sqrt {\frac {\gamma M}{R}}}\cdot \mathrm {Ma} \cdot (1+{\frac {\gamma -1}{2}}\mathrm {Ma} ^{2})^{-{\frac {\gamma +1}{2(\gamma -1)}}}$

| where: |   |
|---|---|
| ${\dot {m}}$ | = mass flow rate, |
| A | = cross-sectional area , |
| $p_{t}$ | = total pressure, |
| $T_{t}$ | = total temperature, |
| $\gamma$ | = ${\frac {c_{p}}{c_{v}}}$ = isentropic expansion factor, |
| R | = universal gas constant, |
| $\mathrm {Ma}$ | = Mach number |
| M | = the gas molecular mass (also known as the molecular weight) |

When the throat is at sonic speed Ma = 1 where the equation simplifies to:

${\dot {m}}={\frac {Ap_{t}}{\sqrt {T_{t}}}}\cdot {\sqrt {\frac {\gamma M}{R}}}\cdot ({\frac {\gamma +1}{2}})^{-{\frac {\gamma +1}{2(\gamma -1)}}}$

By Newton's third law of motion the mass flow rate can be used to determine the force exerted by the expelled gas by:

$F={\dot {m}}\cdot v_{e}$

| where: |   |
|---|---|
| F | = force exerted, |
| ${\dot {m}}$ | = mass flow rate, |
| $v_{e}$ | = exit velocity at nozzle exit |

In aerodynamics, the force exerted by the nozzle is defined as the thrust.

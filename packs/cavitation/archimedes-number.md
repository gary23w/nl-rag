---
title: "Archimedes number"
source: https://en.wikipedia.org/wiki/Archimedes_number
domain: cavitation
license: CC-BY-SA-4.0
tags: cavitation
fetched: 2026-07-04
---

# Archimedes number

In viscous fluid dynamics, the **Archimedes number** (**Ar**), is a dimensionless number used to determine the motion of fluids due to density differences, named after the ancient Greek scientist and mathematician Archimedes.

It is the ratio of gravitational forces to viscous forces and has the form:

${\begin{aligned}\mathrm {Ar} &={\frac {gL^{3}{\frac {\rho -\rho _{\ell }}{\rho _{\ell }}}}{\nu ^{2}}}\\&={\frac {gL^{3}\rho _{\ell }(\rho -\rho _{\ell })}{\mu ^{2}}}\\\end{aligned}}$

where:

- g is the local external field (for example gravitational acceleration), m/s2,
- L is the characteristic length of body, m.
- ${\frac {\rho -\rho _{\ell }}{\rho _{\ell }}}$ is the submerged specific gravity,
- $\rho _{\ell }$ is the density of the fluid, kg/m3,
- $\rho$ is the density of the body, kg/m3,
- $\nu ={\frac {\mu }{\rho _{\ell }}}$ is the kinematic viscosity, m2/s,
- $\mu$ is the dynamic viscosity, Pa·s,

## Uses

The Archimedes number is generally used in design of tubular chemical process reactors. The following are non-exhaustive examples of using the Archimedes number in reactor design.

### Packed-bed fluidization design

The Archimedes number is applied often in the engineering of packed beds, which are very common in the chemical processing industry. A packed bed reactor, which is similar to the ideal plug flow reactor model, involves packing a tubular reactor with a solid catalyst, then passing incompressible or compressible fluids through the solid bed. When the solid particles are small, they may be "fluidized", so that they act as if they were a fluid. When fluidizing a packed bed, the pressure of the working fluid is increased until the pressure drop between the bottom of the bed (where fluid enters) and the top of the bed (where fluid leaves) is equal to the weight of the packed solids. At this point, the velocity of the fluid is just not enough to achieve fluidization, and extra pressure is required to overcome the friction of particles with each other and the wall of the reactor, allowing fluidization to occur. This gives a minimum fluidization velocity, $u_{mf}$ , that may be estimated by:

$u_{mf}={\frac {\mu }{\rho _{l}d_{v}}}\left((33.7^{2}+0.0408{\text{Ar}})^{\frac {1}{2}}-33.7\right)$

where:

- $d_{v}$ is the diameter of sphere with the same volume as the solid particle and can often be estimated as $d_{v}\approx 1.13d_{p}$ , where $d_{p}$ is the diameter of the particle.

### Bubble column design

Another use is in the estimation of gas holdup in a bubble column. In a bubble column, the gas holdup (fraction of a bubble column that is gas at a given time) can be estimated by:

$\varepsilon _{g}=b_{1}\left[{\text{Eo}}^{b2}{\text{Ar}}^{b3}{\text{Fr}}^{b4}\left({\frac {d_{r}}{D}}\right)^{b5}\right]^{b6}$

where:

- $\varepsilon _{g}$ is the gas holdup fraction
- ${\text{Eo}}$ is the Eötvos number
- ${\text{Fr}}$ is the Froude number
- $d_{r}$ is the diameter of holes in the column's spargers (holed discs that emit bubbles)
- D is the column diameter
- Parameters $b1$ to $b6$ are found empirically

### Spouted-bed minimum spouting velocity design

A spouted bed is used in drying and coating. It involves spraying a liquid into a bed packed with the solid to be coated. A fluidizing gas fed from the bottom of the bed causes a spout, which causes the solids to circle linearly around the liquid. Work has been undertaken to model the minimum velocity of gas required for spouting in a spouted bed, including the use of artificial neural networks. Testing with such models found that Archimedes number is a parameter that has a very large effect on the minimum spouting velocity.

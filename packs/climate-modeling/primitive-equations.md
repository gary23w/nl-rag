---
title: "Primitive equations"
source: https://en.wikipedia.org/wiki/Primitive_equations
domain: climate-modeling
license: CC-BY-SA-4.0
tags: climate model, general circulation model, radiative transfer, model intercomparison
fetched: 2026-07-02
---

# Primitive equations

The **primitive equations** are a set of nonlinear partial differential equations that are used to approximate global atmospheric flow and are used in most atmospheric models. They consist of three main sets of balance equations:

1. A *continuity equation*: Representing the conservation of mass.
2. *Conservation of momentum*: Consisting of a form of the Navier–Stokes equations that describe hydrodynamical flow on the surface of a sphere under the assumption that vertical motion is much smaller than horizontal motion (hydrostasis) and that the fluid layer depth is small compared to the radius of the sphere
3. A *thermal energy equation*: Relating the overall temperature of the system to heat sources and sinks

The primitive equations may be linearized to yield Laplace's tidal equations, an eigenvalue problem from which the analytical solution to the latitudinal structure of the flow may be determined.

In general, nearly all forms of the primitive equations relate the five variables *u*, *v*, ω, *T*, *W*, and their evolution over space and time.

The equations were first written down by Vilhelm Bjerknes.

## Definitions

- **u** is the zonal velocity (velocity in the east–west direction tangent to the sphere)
- **v** is the meridional velocity (velocity in the north–south direction tangent to the sphere)
- **$\omega$** is the vertical velocity in isobaric coordinates
- **T** is the temperature
- **$\Phi$** is the geopotential
- **f** is the term corresponding to the Coriolis force, and is equal to $2\Omega \sin(\phi )$ , where $\Omega$ is the angular rotation rate of the Earth ( $2\pi /24$ radians per sidereal hour), and $\phi$ is the latitude
- **R** is the gas constant
- **p** is the pressure
- **$\rho$** is the density
- **$c_{p}$** is the specific heat on a constant pressure surface
- **J** is the heat flow per unit time per unit mass
- **W** is the precipitable water
- **$\Pi$** is the Exner function
- **$\theta$** is the potential temperature
- $\eta$ is the Absolute vorticity

## Forces that cause atmospheric motion

Forces that cause atmospheric motion include the pressure gradient force, gravity, and viscous friction. Together, they create the forces that accelerate our atmosphere.

The pressure gradient force causes an acceleration forcing air from regions of high pressure to regions of low pressure. Mathematically, this can be written as:

${\frac {f}{m}}={\frac {1}{\rho }}{\frac {dp}{dx}}.$

The gravitational force accelerates objects at approximately 9.8 m/s2 directly towards the center of the Earth.

The force due to viscous friction can be approximated as:

$f_{r}={f \over a}{1 \over \rho }\mu \left(\nabla \cdot (\mu \nabla v)+\nabla (\lambda \nabla \cdot v)\right).$

Using Newton's second law, these forces (referenced in the equations above as the accelerations due to these forces) may be summed to produce an equation of motion that describes this system. This equation can be written in the form:

${\frac {dv}{dt}}=-({\frac {1}{\rho }})\nabla p-g({\frac {r}{r}})+f_{r}$

$g=g_{e}.\,$

Therefore, to complete the system of equations and obtain 6 equations and 6 variables:

- ${\frac {dv}{dt}}=-({\frac {1}{\rho }})\nabla p-g({\frac {r}{r}})+({\frac {1}{\rho }})\left[\nabla \cdot (\mu \nabla v)+\nabla (\lambda \nabla \cdot v)\right]$
- $c_{v}{\frac {dT}{dt}}+p{\frac {d\alpha }{dt}}=q+f$
- ${\frac {d\rho }{dt}}+\rho \nabla \cdot v=0$
- $p=nT.$

where n is the number density in mol, and T:=RT is the temperature equivalent value in Joule/mol.

## Forms of the primitive equations

The precise form of the primitive equations depends on the vertical coordinate system chosen, such as pressure coordinates, log pressure coordinates, or sigma coordinates. Furthermore, the velocity, temperature, and geopotential variables may be decomposed into mean and perturbation components using Reynolds decomposition.

### Pressure coordinate in vertical, Cartesian tangential plane

In this form pressure is selected as the vertical coordinate and the horizontal coordinates are written for the Cartesian tangential plane (i.e. a plane tangent to some point on the surface of the Earth). This form does not take the curvature of the Earth into account, but is useful for visualizing some of the physical processes involved in formulating the equations due to its relative simplicity.

Note that the capital D time derivatives are material derivatives. Five equations in five unknowns comprise the system.

- the inviscid (frictionless) momentum equations:

${\frac {Du}{Dt}}-fv=-{\frac {\partial \Phi }{\partial x}}$

${\frac {Dv}{Dt}}+fu=-{\frac {\partial \Phi }{\partial y}}$

- the hydrostatic equation, a special case of the vertical momentum equation in which vertical acceleration is considered negligible:

$0=-{\frac {\partial \Phi }{\partial p}}-{\frac {RT}{p}}$

- the continuity equation, connecting horizontal divergence/convergence to vertical motion under the hydrostatic approximation ( $dp=-\rho \,d\Phi$ ):

${\frac {\partial u}{\partial x}}+{\frac {\partial v}{\partial y}}+{\frac {\partial \omega }{\partial p}}=0$

- and the thermodynamic energy equation, a consequence of the first law of thermodynamics

${\frac {\partial T}{\partial t}}+u{\frac {\partial T}{\partial x}}+v{\frac {\partial T}{\partial y}}+\omega \left({\frac {\partial T}{\partial p}}-{\frac {RT}{pc_{p}}}\right)={\frac {J}{c_{p}}}$

When a statement of the conservation of water vapor substance is included, these six equations can form the basis for a numerical weather prediction scheme.

### Primitive equations using sigma coordinate system, polar stereographic projection

According to the *National Weather Service Handbook No. 1 – Facsimile Products*, the primitive equations can be simplified into the following equations:

- Zonal wind:

${\frac {\partial u}{\partial t}}=\eta v-{\frac {\partial \Phi }{\partial x}}-c_{p}\theta {\frac {\partial \pi }{\partial x}}-z{\frac {\partial u}{\partial \sigma }}-{\frac {\partial ({\frac {u^{2}+v^{2}}{2}})}{\partial x}}$

- Meridional wind:

${\frac {\partial v}{\partial t}}=-\eta {\frac {u}{v}}-{\frac {\partial \Phi }{\partial y}}-c_{p}\theta {\frac {\partial \pi }{\partial y}}-z{\frac {\partial v}{\partial \sigma }}-{\frac {\partial ({\frac {u^{2}+v^{2}}{2}})}{\partial y}}$

- Temperature:

${\frac {\partial T}{\partial t}}={\frac {\partial T}{\partial t}}+u{\frac {\partial T}{\partial x}}+v{\frac {\partial T}{\partial y}}+w{\frac {\partial T}{\partial z}}$

The first term is equal to the change in temperature due to incoming solar radiation and outgoing longwave radiation, which changes with time throughout the day. The second, third, and fourth terms are due to advection. Additionally, the variable *T* with subscript is the change in temperature on that plane. Each *T* is actually different and related to its respective plane. This is divided by the distance between grid points to get the change in temperature with the change in distance. When multiplied by the wind velocity on that plane, the units kelvins per meter and meters per second give kelvins per second. The sum of all the changes in temperature due to motions in the *x*, *y*, and *z* directions give the total change in temperature with time.

- Precipitable water:

${\frac {\delta W}{\partial t}}=u{\frac {\partial W}{\partial x}}+v{\frac {\partial W}{\partial y}}+w{\frac {\partial W}{\partial z}}$

This equation and notation works in much the same way as the temperature equation. This equation describes the motion of water from one place to another at a point without taking into account water that changes form. Inside a given system, the total change in water with time is zero. However, concentrations are allowed to move with the wind.

- Pressure thickness:

${\frac {\partial }{\partial t}}{\frac {\partial p}{\partial \sigma }}=u{\frac {\partial }{\partial x}}x{\frac {\partial p}{\partial \sigma }}+v{\frac {\partial }{\partial y}}y{\frac {\partial p}{\partial \sigma }}+w{\frac {\partial }{\partial z}}z{\frac {\partial p}{\partial \sigma }}$

These simplifications make it much easier to understand what is happening in the model. Things like the temperature (potential temperature), precipitable water, and to an extent the pressure thickness simply move from one spot on the grid to another with the wind. The wind is forecast slightly differently. It uses geopotential, specific heat, the Exner function *π*, and change in sigma coordinate.

## Solution to the linearized primitive equations

The analytic solution to the linearized primitive equations involves a sinusoidal oscillation in time and longitude, modulated by coefficients related to height and latitude.

${\begin{Bmatrix}u,v,\Phi \end{Bmatrix}}={\begin{Bmatrix}{\hat {u}},{\hat {v}},{\hat {\Phi }}\end{Bmatrix}}e^{i(s\lambda +\sigma t)}$

where *s* and $\sigma$ are the zonal wavenumber and angular frequency, respectively. The solution represents atmospheric waves and tides.

When the coefficients are separated into their height and latitude components, the height dependence takes the form of propagating or evanescent waves (depending on conditions), while the latitude dependence is given by the Hough functions.

This analytic solution is only possible when the primitive equations are linearized and simplified. Unfortunately many of these simplifications (i.e. no dissipation, isothermal atmosphere) do not correspond to conditions in the actual atmosphere. As a result, a numerical solution which takes these factors into account is often calculated using general circulation models and climate models.

---
title: "Robin boundary condition"
source: https://en.wikipedia.org/wiki/Robin_boundary_condition
domain: boundary-value-problems
license: CC-BY-SA-4.0
tags: boundary value problem, dirichlet boundary condition, neumann boundary condition, shooting method
fetched: 2026-07-02
---

# Robin boundary condition

In mathematics, the **Robin boundary condition** (/ˈrɒbɪn/ *ROB-in*, French: [ʁɔbɛ̃]), or **third-type boundary condition**, is a type of boundary condition, named after Victor Gustave Robin (1855–1897). It is used when solving partial differential equations and ordinary differential equations.

The Robin boundary condition specifies a linear combination of the value of a function and the value of its derivative at the boundary of a given domain. It is a generalization of the Dirichlet boundary condition, which specifies only the function's value, and the Neumann boundary condition, which specifies only the function's derivative. A common physical example is in heat transfer, where a surface might lose heat to the environment via convection. The rate of heat flow (related to the derivative of temperature) would be proportional to the difference between the surface temperature (the value of the temperature function) and the ambient temperature.

Other equivalent names in use are **Fourier-type condition** and **radiation condition**.

## Definition

Robin boundary conditions are a weighted combination of Dirichlet boundary conditions and Neumann boundary conditions. This contrasts to mixed boundary conditions, which are boundary conditions of different types specified on different subsets of the boundary. Robin boundary conditions are also called **impedance boundary conditions**, from their application in electromagnetic problems, or **convective boundary conditions**, from their application in heat transfer problems (Hahn, 2012).

If Ω is the domain on which the given equation is to be solved and ∂Ω denotes its boundary, the Robin boundary condition is:

$au+b{\frac {\partial u}{\partial n}}=g\qquad {\text{on }}\partial \Omega$

for some non-zero constants *a* and *b* and a given function *g* defined on ∂Ω. Here, *u* is the unknown solution defined on Ω and ⁠∂*u*/∂*n*⁠ denotes the normal derivative at the boundary. More generally, *a* and *b* are allowed to be (given) functions, rather than constants.

In one dimension, if, for example, Ω = [0,1], the Robin boundary condition becomes the conditions:

${\begin{aligned}au(0)-bu'(0)&=g(0)\\au(1)+bu'(1)&=g(1)\end{aligned}}$

Notice the change of sign in front of the term involving a derivative: that is because the normal to [0,1] at 0 points in the negative direction, while at 1 it points in the positive direction.

## Application

Robin boundary conditions are commonly used in solving Sturm–Liouville problems which appear in many contexts in science and engineering.

In addition, the Robin boundary condition is a general form of the **insulating boundary condition** for convection–diffusion equations. Here, the convective and diffusive fluxes at the boundary sum to zero:

$u_{x}(0)\,c(0)-D{\frac {\partial c(0)}{\partial x}}=0$

where *D* is the diffusive constant, *u* is the convective velocity at the boundary and *c* is the concentration. The second term is a result of Fick's law of diffusion.

Robin boundary conditions on the electrostatic potential $\phi$ naturally appear when efficiently modelling electrostatic capacitance or field effects involving ionic or semiconducting electronic media separated by an insulating dielectric, where the Robin boundary condition models a conductor's surface that has a linear 'softness' of the surface charge Debye layer i.e. a linear quantum capacitance that appears in series with the ordinary dielectric geometrical capacitance. A single Robin boundary condition on $\phi$ is also able to completely capture the geometrical capacitance in the 1D-like (parallel-plate capacitor or planar interface) case, such as when modelling a Stern layer.

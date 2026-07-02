---
title: "Immersed boundary method"
source: https://en.wikipedia.org/wiki/Immersed_boundary_method
domain: smoothed-particle-hydrodynamics
license: CC-BY-SA-4.0
tags: smoothed-particle hydrodynamics, meshfree methods, fluid simulation, multiphase flow
fetched: 2026-07-02
---

# Immersed boundary method

In computational fluid dynamics, the **immersed boundary method** originally referred to an approach developed by Charles Peskin in 1972 to simulate fluid-structure (fiber) interactions. Treating the coupling of the structure deformations and the fluid flow poses a number of challenging problems for numerical simulations (the elastic boundary changes the flow of the fluid and the fluid moves the elastic boundary simultaneously). In the immersed boundary method the fluid is represented in an Eulerian coordinate system and the structure is represented in Lagrangian coordinates. For Newtonian fluids governed by the Navier–Stokes equations, the fluid equations are

$\rho \left({\frac {\partial {u}({x},t)}{\partial {t}}}+{u}\cdot \nabla {u}\right)=-\nabla p+\mu \,\Delta u(x,t)+f(x,t)$

and if the flow is incompressible, we have the further condition that

$\nabla \cdot u=0.\,$

The immersed structures are typically represented as a collection of one-dimensional fibers, denoted by $\Gamma$ . Each fiber can be viewed as a parametric curve $X(s,t)$ where s is the Lagrangian coordinate along the fiber and t is time. The physics of the fiber is represented via a fiber force distribution function $F(s,t)$ . Spring forces, bending resistance or any other type of behavior can be built into this term. The force exerted by the structure on the fluid is then interpolated as a source term in the momentum equation using

$f(x,t)=\int _{\Gamma }F(s,t)\,\delta {\big (}x-X(s,t){\big )}\,ds,$

where $\delta$ is the Dirac δ function. The forcing can be extended to multiple dimensions to model elastic surfaces or three-dimensional solids. Assuming a massless structure, the elastic fiber moves with the local fluid velocity and can be interpolated via the delta function

${\frac {\partial X(s,t)}{\partial t}}=u(X,t)=\int _{\Omega }u(x,t)\,\delta {\big (}x-X(s,t){\big )}\,dx,$

where $\Omega$ denotes the entire fluid domain. Discretization of these equations can be done by assuming an Eulerian grid on the fluid and a separate Lagrangian grid on the fiber. Approximations of the Delta distribution by smoother functions will allow us to interpolate between the two grids. Any existing fluid solver can be coupled to a solver for the fiber equations to solve the Immersed Boundary equations. Variants of this basic approach have been applied to simulate a wide variety of mechanical systems involving elastic structures which interact with fluid flows.

Since the original development of this method by Peskin, a variety of approaches have been developed. These include stochastic formulations for microscopic systems, viscoelastic soft materials, complex fluids, such as the Stochastic Immersed Boundary Methods of Atzberger, Kramer, and Peskin, methods for simulating flows over complicated immersed solid bodies on grids that do not conform to the surface of the body Mittal and Iaccarino, and other approaches that incorporate mass and rotational degrees of freedom Olson, Lim, Cortez. Methods for complicated body shapes include the immersed interface method, the Cartesian grid method, the ghost fluid method and the cut-cell methods categorizing immersed boundary methods into *continuous forcing* and *discrete forcing* methods. Methods have been developed for simulations of viscoelastic fluids, curved fluid interfaces, microscopic biophysical systems (proteins in lipid bilayer membranes, swimmers), and engineered devices, such as the Stochastic Immersed Boundary Methods of Atzberger, Kramer, and Peskin, Stochastic Eulerian Lagrangian Methods of Atzberger, Massed Immersed Boundary Methods of Mori, and Rotational Immersed Boundary Methods of Olson, Lim, Cortez.

In general, for immersed boundary methods and related variants, there is an active research community that is still developing new techniques and related software implementations and incorporating related techniques into simulation packages and CAD engineering software. For more details see below.

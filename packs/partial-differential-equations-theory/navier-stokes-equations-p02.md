---
title: "Navier–Stokes equations (part 2/2)"
source: https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations
domain: partial-differential-equations-theory
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, sobolev space
fetched: 2026-07-02
part: 2/2
---

## Stream function for incompressible 2D fluid

Taking the curl of the incompressible Navier–Stokes equation results in the elimination of pressure. This is especially easy to see if 2D Cartesian flow is assumed (like in the degenerate 3D case with ${\textstyle u_{z}=0}$ and no dependence of anything on ${\textstyle z}$ ), where the equations reduce to: ${\begin{aligned}\rho \left({\frac {\partial u_{x}}{\partial t}}+u_{x}{\frac {\partial u_{x}}{\partial x}}+u_{y}{\frac {\partial u_{x}}{\partial y}}\right)&=-{\frac {\partial p}{\partial x}}+\mu \left({\frac {\partial ^{2}u_{x}}{\partial x^{2}}}+{\frac {\partial ^{2}u_{x}}{\partial y^{2}}}\right)+\rho g_{x}\\\rho \left({\frac {\partial u_{y}}{\partial t}}+u_{x}{\frac {\partial u_{y}}{\partial x}}+u_{y}{\frac {\partial u_{y}}{\partial y}}\right)&=-{\frac {\partial p}{\partial y}}+\mu \left({\frac {\partial ^{2}u_{y}}{\partial x^{2}}}+{\frac {\partial ^{2}u_{y}}{\partial y^{2}}}\right)+\rho g_{y}.\end{aligned}}$

Differentiating the first with respect to ${\textstyle y}$ , the second with respect to ${\textstyle x}$ and subtracting the resulting equations will eliminate pressure and any conservative force. For incompressible flow, defining the stream function ${\textstyle \psi }$ through $u_{x}={\frac {\partial \psi }{\partial y}};\quad u_{y}=-{\frac {\partial \psi }{\partial x}}$ results in mass continuity being unconditionally satisfied (given the stream function is continuous), and then incompressible Newtonian 2D momentum and mass conservation condense into one equation: ${\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \psi }{\partial y}}{\frac {\partial }{\partial x}}\left(\nabla ^{2}\psi \right)-{\frac {\partial \psi }{\partial x}}{\frac {\partial }{\partial y}}\left(\nabla ^{2}\psi \right)=\nu \nabla ^{4}\psi$

where ${\textstyle \nabla ^{4}}$ is the 2D biharmonic operator and ${\textstyle \nu }$ is the kinematic viscosity, ${\textstyle \nu ={\frac {\mu }{\rho }}}$ . We can also express this compactly using the Jacobian determinant: ${\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \left(\psi ,\nabla ^{2}\psi \right)}{\partial (y,x)}}=\nu \nabla ^{4}\psi .$

This single equation together with appropriate boundary conditions describes 2D fluid flow, taking only kinematic viscosity as a parameter. Note that the equation for creeping flow results when the left side is assumed zero.

In axisymmetric flow another stream function formulation, called the Stokes stream function, can be used to describe the velocity components of an incompressible flow with one scalar function.

The incompressible Navier–Stokes equation is a differential algebraic equation, having the inconvenient feature that there is no explicit mechanism for advancing the pressure in time. Consequently, much effort has been expended to eliminate the pressure from all or part of the computational process. The stream function formulation eliminates the pressure but only in two dimensions and at the expense of introducing higher derivatives and elimination of the velocity, which is the primary variable of interest.


## Properties

### Nonlinearity

The Navier–Stokes equations are nonlinear partial differential equations in the general case and so remain in almost every real situation. In some cases, such as one-dimensional flow and Stokes flow (or creeping flow), the equations can be simplified to linear equations. The nonlinearity makes most problems difficult or impossible to solve and is the main contributor to the turbulence that the equations model.

The nonlinearity is due to convective acceleration, which is an acceleration associated with the change in velocity over position. Hence, any convective flow, whether turbulent or not, will involve nonlinearity. An example of convective but laminar (nonturbulent) flow would be the passage of a viscous fluid (for example, oil) through a small converging nozzle. Such flows, whether exactly solvable or not, can often be thoroughly studied and understood.

### Turbulence

Turbulence is the time-dependent chaotic behaviour seen in many fluid flows. It is generally believed that it is due to the inertia of the fluid as a whole: the culmination of time-dependent and convective acceleration; hence flows where inertial effects are small tend to be laminar (the Reynolds number quantifies how much the flow is affected by inertia). It is believed, though not known with certainty, that the Navier–Stokes equations describe turbulence properly.

The numerical solution of the Navier–Stokes equations for turbulent flow is extremely difficult, and due to the significantly different mixing-length scales that are involved in turbulent flow, the stable solution of this requires such a fine mesh resolution that the computational time becomes significantly infeasible for calculation or direct numerical simulation. Attempts to solve turbulent flow using a laminar solver typically result in a time-unsteady solution, which fails to converge appropriately. To counter this, time-averaged equations such as the Reynolds-averaged Navier–Stokes equations (RANS), supplemented with turbulence models, are used in practical computational fluid dynamics (CFD) applications when modeling turbulent flows. Some models include the Spalart–Allmaras, k–ω, k–ε, and SST models, which add a variety of additional equations to bring closure to the RANS equations. Large eddy simulation (LES) can also be used to solve these equations numerically. This approach is computationally more expensive—in time and in computer memory—than RANS, but produces better results because it explicitly resolves the larger turbulent scales.

### Applicability

Together with supplemental equations (for example, conservation of mass) and well-formulated boundary conditions, the Navier–Stokes equations seem to model fluid motion accurately; even turbulent flows seem (on average) to agree with real world observations.

The Navier–Stokes equations assume that the fluid being studied is a continuum (it is infinitely divisible and not composed of particles such as atoms or molecules), and is not moving at relativistic velocities. At very small scales or under extreme conditions, real fluids made out of discrete molecules will produce results different from the continuous fluids modeled by the Navier–Stokes equations. For example, capillarity of internal layers in fluids appears for flow with high gradients. For large Knudsen number of the problem, the Boltzmann equation may be a suitable replacement. Failing that, one may have to resort to molecular dynamics or various hybrid methods.

Another limitation is simply the complicated nature of the equations. Time-tested formulations exist for common fluid families, but the application of the Navier–Stokes equations to less common families tends to result in very complicated formulations and often to open research problems. For this reason, these equations are usually written for Newtonian fluids where the viscosity model is linear; truly general models for the flow of other kinds of fluids (such as blood) do not exist.


## Application to specific problems

The Navier–Stokes equations, even when written explicitly for specific fluids, are rather generic in nature and their proper application to specific problems can be very diverse. This is partly because there is an enormous variety of problems that may be modeled, ranging from as simple as the distribution of static pressure to as complicated as multiphase flow driven by surface tension.

Generally, application to specific problems begins with some flow assumptions and initial/boundary condition formulation, this may be followed by scale analysis to further simplify the problem.

### Parallel flow

Assume steady, parallel, one-dimensional, non-convective pressure-driven flow between parallel plates, the resulting scaled (dimensionless) boundary value problem is: ${\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}=-1;\quad u(0)=u(1)=0.$

The boundary condition is the no slip condition. This problem is easily solved for the flow field: $u(y)={\frac {y-y^{2}}{2}}.$

From this point onward, more quantities of interest can be easily obtained, such as viscous drag force or net flow rate.

### Radial flow

Difficulties may arise when the problem becomes slightly more complicated. A seemingly modest twist on the parallel flow above would be the *radial* flow between parallel plates; this involves convection and thus non-linearity. The velocity field may be represented by a function $f(z)$ that must satisfy: ${\frac {\mathrm {d} ^{2}f}{\mathrm {d} z^{2}}}+Rf^{2}=-1;\quad f(-1)=f(1)=0.$

This ordinary differential equation is what is obtained when the Navier–Stokes equations are written and the flow assumptions applied (additionally, the pressure gradient is solved for). The nonlinear term makes this a very difficult problem to solve analytically (a lengthy implicit solution may be found which involves elliptic integrals and roots of cubic polynomials). Issues with the actual existence of solutions arise for ${\textstyle R>1.41}$ (approximately; this is not √2), the parameter ${\textstyle R}$ being the Reynolds number with appropriately chosen scales. This is an example of flow assumptions losing their applicability, and an example of the difficulty in "high" Reynolds number flows.

### Convection

A type of natural convection that can be described by the Navier–Stokes equation is the Rayleigh–Bénard convection. It is one of the most commonly studied convection phenomena because of its analytical and experimental accessibility.


## Exact solutions of the Navier–Stokes equations

Some exact solutions to the Navier–Stokes equations exist. Examples of degenerate cases—with the non-linear terms in the Navier–Stokes equations equal to zero—are Poiseuille flow, Couette flow and the oscillatory Stokes boundary layer. But also, more interesting examples, solutions to the full non-linear equations, exist, such as Jeffery–Hamel flow, Von Kármán swirling flow, stagnation point flow, Landau–Squire jet, and Taylor–Green vortex. Time-dependent self-similar solutions of the three-dimensional non-compressible Navier–Stokes equations in Cartesian coordinate can be given with the help of the Kummer's functions with quadratic arguments. For the compressible Navier–Stokes equations the time-dependent self-similar solutions are however the Whittaker functions again with quadratic arguments when the polytropic equation of state is used as a closing condition. Note that the existence of these exact solutions does not imply they are stable: turbulence may develop at higher Reynolds numbers.

Under additional assumptions, the component parts can be separated.

A two-dimensional example

For example, in the case of an unbounded planar domain with **two-dimensional** — incompressible and stationary — flow in polar coordinates (*r*,*φ*), the velocity components (*ur*,*uφ*) and pressure p are: ${\begin{aligned}u_{r}&={\frac {A}{r}},\\u_{\varphi }&=B\left({\frac {1}{r}}-r^{{\frac {A}{\nu }}+1}\right),\\p&=-{\frac {A^{2}+B^{2}}{2r^{2}}}-{\frac {2B^{2}\nu r^{\frac {A}{\nu }}}{A}}+{\frac {B^{2}r^{\left({\frac {2A}{\nu }}+2\right)}}{{\frac {2A}{\nu }}+2}}\end{aligned}}$

where A and B are arbitrary constants. This solution is valid in the domain *r* ≥ 1 and for *A* < −2*ν*.

In Cartesian coordinates, when the viscosity is zero (*ν* = 0), this is: ${\begin{aligned}\mathbf {v} (x,y)&={\frac {1}{x^{2}+y^{2}}}{\begin{pmatrix}Ax+By\\Ay-Bx\end{pmatrix}},\\p(x,y)&=-{\frac {A^{2}+B^{2}}{2\left(x^{2}+y^{2}\right)}}\end{aligned}}$

A three-dimensional example

For example, in the case of an unbounded Euclidean domain with **three-dimensional** — incompressible, stationary and with zero viscosity (*ν* = 0) — radial flow in Cartesian coordinates (*x*,*y*,*z*), the velocity vector **v** and pressure p are: ${\begin{aligned}\mathbf {v} (x,y,z)&={\frac {A}{x^{2}+y^{2}+z^{2}}}{\begin{pmatrix}x\\y\\z\end{pmatrix}},\\p(x,y,z)&=-{\frac {A^{2}}{2\left(x^{2}+y^{2}+z^{2}\right)}}.\end{aligned}}$

There is a singularity at *x* = *y* = *z* = 0.

### A three-dimensional steady-state vortex solution

A steady-state example with no singularities comes from considering the flow along the lines of a Hopf fibration. Let ${\textstyle r}$ be a constant radius of the inner coil. One set of solutions is given by: ${\begin{aligned}\rho (x,y,z)&={\frac {3B}{r^{2}+x^{2}+y^{2}+z^{2}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\\mathbf {u} (x,y,z)&={\frac {A}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}{\begin{pmatrix}2(-ry+xz)\\2(rx+yz)\\r^{2}-x^{2}-y^{2}+z^{2}\end{pmatrix}}\\g&=0\\\mu &=0\end{aligned}}$

for arbitrary constants ${\textstyle A}$ and ${\textstyle B}$ . This is a solution in a non-viscous gas (compressible fluid) whose density, velocities and pressure goes to zero far from the origin. (Note this is not a solution to the Clay Millennium problem because that refers to incompressible fluids where ${\textstyle \rho }$ is a constant, and neither does it deal with the uniqueness of the Navier–Stokes equations with respect to any turbulence properties.) It is also worth pointing out that the components of the velocity vector are exactly those from the Pythagorean quadruple parametrization. Other choices of density and pressure are possible with the same velocity field:

Other choices of density and pressure

Another choice of pressure and density with the same velocity vector above is one where the pressure and density fall to zero at the origin and are highest in the central loop at *z* = 0, *x*2 + *y*2 = *r*2: ${\begin{aligned}\rho (x,y,z)&={\frac {20B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{4}}}+{\frac {-4A^{2}B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{5}}}.\end{aligned}}$

In fact in general there are simple solutions for any polynomial function f where the density is: $\rho (x,y,z)={\frac {1}{r^{2}+x^{2}+y^{2}+z^{2}}}f\left({\frac {x^{2}+y^{2}}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}\right).$

### Viscous three-dimensional periodic solutions

Two examples of periodic fully-three-dimensional viscous solutions are described in. These solutions are defined on a three-dimensional torus $\mathbb {T} ^{3}=[0,L]^{3}$ and are characterized by positive and negative helicity respectively. The solution with positive helicity is given by: ${\begin{aligned}u_{x}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(kx-{\frac {\pi }{3}}\right)\cos \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)-\cos \left(kz-{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u_{y}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(ky-{\frac {\pi }{3}}\right)\cos \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)-\cos \left(kx-{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u_{z}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U_{0}\left[\,\sin \left(kz-{\frac {\pi }{3}}\right)\cos \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)-\cos \left(ky-{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\end{aligned}}$ where $k=2\pi /L$ is the wave number and the velocity components are normalized so that the average kinetic energy per unit of mass is $U_{0}^{2}/2$ at $t=0$ . The pressure field is obtained from the velocity field as $p=p_{0}-\rho _{0}\|{\boldsymbol {u}}\|^{2}/2$ (where $p_{0}$ and $\rho _{0}$ are reference values for the pressure and density fields respectively). Since both the solutions belong to the class of Beltrami flow, the vorticity field is parallel to the velocity and, for the case with positive helicity, is given by $\omega ={\sqrt {3}}\,k\,{\boldsymbol {u}}$ . These solutions can be regarded as a generalization in three dimensions of the classic two-dimensional Taylor–Green vortex.


## Wyld diagrams

**Wyld diagrams** are bookkeeping graphs that correspond to the Navier–Stokes equations via a perturbation expansion of the fundamental continuum mechanics. Similar to the Feynman diagrams in quantum field theory, these diagrams are an extension of Mstislav Keldysh's technique for nonequilibrium processes in fluid dynamics. In other words, these diagrams assign graphs to the (often) turbulent phenomena in turbulent fluids by allowing correlated and interacting fluid particles to obey stochastic processes associated to pseudo-random functions in probability distributions.


## Representations in 3D

Note that the formulas in this section make use of the single-line notation for partial derivatives, where, e.g. ${\textstyle \partial _{x}u}$ means the partial derivative of ${\textstyle u}$ with respect to ${\textstyle x}$ , and ${\textstyle \partial _{y}^{2}f_{\theta }}$ means the second-order partial derivative of ${\textstyle f_{\theta }}$ with respect to ${\textstyle y}$ .

A 2022 paper provides a less costly, dynamical and recurrent solution of the Navier-Stokes equation for 3D turbulent fluid flows. On suitably short time scales, the dynamics of turbulence is deterministic.

### Cartesian coordinates

From the general form of the Navier–Stokes, with the velocity vector expanded as ${\textstyle \mathbf {u} =(u_{x},u_{y},u_{z})}$ , sometimes respectively named ${\textstyle u}$ , ${\textstyle v}$ , ${\textstyle w}$ , we may write the vector equation explicitly, ${\begin{aligned}x:\ &\rho \left({\partial _{t}u_{x}}+u_{x}\,{\partial _{x}u_{x}}+u_{y}\,{\partial _{y}u_{x}}+u_{z}\,{\partial _{z}u_{x}}\right)\\&\quad =-\partial _{x}p+\mu \left({\partial _{x}^{2}u_{x}}+{\partial _{y}^{2}u_{x}}+{\partial _{z}^{2}u_{x}}\right)+{\frac {1}{3}}\mu \ \partial _{x}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{x}\\\end{aligned}}$ ${\begin{aligned}y:\ &\rho \left({\partial _{t}u_{y}}+u_{x}{\partial _{x}u_{y}}+u_{y}{\partial _{y}u_{y}}+u_{z}{\partial _{z}u_{y}}\right)\\&\quad =-{\partial _{y}p}+\mu \left({\partial _{x}^{2}u_{y}}+{\partial _{y}^{2}u_{y}}+{\partial _{z}^{2}u_{y}}\right)+{\frac {1}{3}}\mu \ \partial _{y}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{y}\\\end{aligned}}$ ${\begin{aligned}z:\ &\rho \left({\partial _{t}u_{z}}+u_{x}{\partial _{x}u_{z}}+u_{y}{\partial _{y}u_{z}}+u_{z}{\partial _{z}u_{z}}\right)\\&\quad =-{\partial _{z}p}+\mu \left({\partial _{x}^{2}u_{z}}+{\partial _{y}^{2}u_{z}}+{\partial _{z}^{2}u_{z}}\right)+{\frac {1}{3}}\mu \ \partial _{z}\left({\partial _{x}u_{x}}+{\partial _{y}u_{y}}+{\partial _{z}u_{z}}\right)+\rho g_{z}.\end{aligned}}$

Note that gravity has been accounted for as a body force, and the values of ${\textstyle g_{x}}$ , ${\textstyle g_{y}}$ , ${\textstyle g_{z}}$ will depend on the orientation of gravity with respect to the chosen set of coordinates.

The continuity equation reads: $\partial _{t}\rho +\partial _{x}(\rho u_{x})+\partial _{y}(\rho u_{y})+\partial _{z}(\rho u_{z})=0.$

When the flow is incompressible, ${\textstyle \rho }$ does not change for any fluid particle, and its material derivative vanishes: ${\textstyle {\frac {\mathrm {D} \rho }{\mathrm {D} t}}=0}$ . The continuity equation is reduced to: $\partial _{x}u_{x}+\partial _{y}u_{y}+\partial _{z}u_{z}=0.$

Thus, for the incompressible version of the Navier–Stokes equation the second part of the viscous terms fall away (see Incompressible flow).

This system of four equations comprises the most commonly used and studied form. Though comparatively more compact than other representations, this is still a nonlinear system of partial differential equations for which solutions are difficult to obtain.

### Cylindrical coordinates

A change of variables on the Cartesian equations will yield the following momentum equations for ${\textstyle r}$ , ${\textstyle \phi }$ , and ${\textstyle z}$ ${\begin{aligned}r:\ &\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{r}}+u_{z}{\partial _{z}u_{r}}-{\frac {u_{\varphi }^{2}}{r}}\right)\\&\quad =-{\partial _{r}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{r}}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{r}}+{\partial _{z}^{2}u_{r}}-{\frac {u_{r}}{r^{2}}}-{\frac {2}{r^{2}}}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{r}\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{r}\\[8px]\end{aligned}}$ ${\begin{aligned}\varphi :\ &\rho \left({\partial _{t}u_{\varphi }}+u_{r}{\partial _{r}u_{\varphi }}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{\varphi }}+u_{z}{\partial _{z}u_{\varphi }}+{\frac {u_{r}u_{\varphi }}{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial _{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r}}\ \partial _{r}\left(r{\partial _{r}u_{\varphi }}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{\varphi }}+{\partial _{z}^{2}u_{\varphi }}-{\frac {u_{\varphi }}{r^{2}}}+{\frac {2}{r^{2}}}{\partial _{\varphi }u_{r}}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial _{\varphi }\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{\varphi }\\[8px]\end{aligned}}$ ${\begin{aligned}z:\ &\rho \left({\partial _{t}u_{z}}+u_{r}{\partial _{r}u_{z}}+{\frac {u_{\varphi }}{r}}{\partial _{\varphi }u_{z}}+u_{z}{\partial _{z}u_{z}}\right)\\&\quad =-{\partial _{z}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{z}}\right)+{\frac {1}{r^{2}}}{\partial _{\varphi }^{2}u_{z}}+{\partial _{z}^{2}u_{z}}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{z}\left({\frac {1}{r}}{\partial _{r}\left(ru_{r}\right)}+{\frac {1}{r}}{\partial _{\varphi }u_{\varphi }}+{\partial _{z}u_{z}}\right)\\&\qquad +\rho g_{z}.\end{aligned}}$

The gravity components will generally not be constants, however for most applications either the coordinates are chosen so that the gravity components are constant or else it is assumed that gravity is counteracted by a pressure field (for example, flow in horizontal pipe is treated normally without gravity and without a vertical pressure gradient). The continuity equation is: ${\partial _{t}\rho }+{\frac {1}{r}}\partial _{r}\left(\rho ru_{r}\right)+{\frac {1}{r}}{\partial _{\varphi }\left(\rho u_{\varphi }\right)}+{\partial _{z}\left(\rho u_{z}\right)}=0.$

This cylindrical representation of the incompressible Navier–Stokes equations is the second most commonly seen (the first being Cartesian above). Cylindrical coordinates are chosen to take advantage of symmetry, so that a velocity component can disappear. A very common case is axisymmetric flow with the assumption of no tangential velocity ( ${\textstyle u_{\phi }=0}$ ), and the remaining quantities are independent of ${\textstyle \phi }$ : ${\begin{aligned}\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+u_{z}{\partial _{z}u_{r}}\right)&=-{\partial _{r}p}+\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{r}}\right)+{\partial _{z}^{2}u_{r}}-{\frac {u_{r}}{r^{2}}}\right)+\rho g_{r}\\\rho \left({\partial _{t}u_{z}}+u_{r}{\partial _{r}u_{z}}+u_{z}{\partial _{z}u_{z}}\right)&=-{\partial _{z}p}+\mu \left({\frac {1}{r}}\partial _{r}\left(r{\partial _{r}u_{z}}\right)+{\partial _{z}^{2}u_{z}}\right)+\rho g_{z}\\{\frac {1}{r}}\partial _{r}\left(ru_{r}\right)+{\partial _{z}u_{z}}&=0.\end{aligned}}$

### Spherical coordinates

In spherical coordinates, the ${\textstyle r}$ , ${\textstyle \phi }$ , and ${\textstyle \theta }$ momentum equations are (note the convention used: ${\textstyle \theta }$ is polar angle, or colatitude, ${\textstyle 0\leq \theta \leq \pi }$ ): ${\begin{aligned}r:\ &\rho \left({\partial _{t}u_{r}}+u_{r}{\partial _{r}u_{r}}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{r}}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{r}}-{\frac {u_{\varphi }^{2}+u_{\theta }^{2}}{r}}\right)\\&\quad =-{\partial _{r}p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{r}}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{r}}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{r}}\right)-2{\frac {u_{r}+{\partial _{\theta }u_{\theta }}+u_{\theta }\cot \theta }{r^{2}}}-{\frac {2}{r^{2}\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial _{r}\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{r}\\[8px]\end{aligned}}$ ${\begin{aligned}\varphi :\ &\rho \left({\partial _{t}u_{\varphi }}+u_{r}{\partial _{r}u_{\varphi }}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{\varphi }}+{\frac {u_{r}u_{\varphi }+u_{\varphi }u_{\theta }\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r\sin \theta }}{\partial _{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{\varphi }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{\varphi }}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{\varphi }}\right)+{\frac {2\sin \theta {\partial _{\varphi }u_{r}}+2\cos \theta {\partial _{\varphi }u_{\theta }}-u_{\varphi }}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r\sin \theta }}\partial _{\varphi }\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{\varphi }\\[8px]\end{aligned}}$ ${\begin{aligned}\theta :\ &\rho \left({\partial _{t}u_{\theta }}+u_{r}{\partial _{r}u_{\theta }}+{\frac {u_{\varphi }}{r\sin \theta }}{\partial _{\varphi }u_{\theta }}+{\frac {u_{\theta }}{r}}{\partial _{\theta }u_{\theta }}+{\frac {u_{r}u_{\theta }-u_{\varphi }^{2}\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial _{\theta }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}{\partial _{r}u_{\theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial _{\varphi }^{2}u_{\theta }}+{\frac {1}{r^{2}\sin \theta }}\partial _{\theta }\left(\sin \theta {\partial _{\theta }u_{\theta }}\right)+{\frac {2}{r^{2}}}{\partial _{\theta }u_{r}}-{\frac {u_{\theta }+2\cos \theta {\partial _{\varphi }u_{\varphi }}}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial _{\theta }\left({\frac {1}{r^{2}}}\partial _{r}\left(r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(u_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }u_{\varphi }}\right)\\&\qquad +\rho g_{\theta }.\end{aligned}}$

Mass continuity will read: ${\partial _{t}\rho }+{\frac {1}{r^{2}}}\partial _{r}\left(\rho r^{2}u_{r}\right)+{\frac {1}{r\sin \theta }}{\partial _{\varphi }(\rho u_{\varphi })}+{\frac {1}{r\sin \theta }}\partial _{\theta }\left(\sin \theta \rho u_{\theta }\right)=0.$

These equations could be (slightly) compacted by, for example, factoring ${\textstyle {\frac {1}{r^{2}}}}$ from the viscous terms. However, doing so would undesirably alter the structure of the Laplacian and other quantities.

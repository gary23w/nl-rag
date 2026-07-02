---
title: "Boltzmann equation"
source: https://en.wikipedia.org/wiki/Boltzmann_equation
domain: kinetic-theory
license: CC-BY-SA-4.0
tags: kinetic theory of gases, mean free path, boltzmann equation, ideal gas law
fetched: 2026-07-02
---

# Boltzmann equation

The **Boltzmann equation** or **Boltzmann transport equation** (**BTE**) describes the statistical behaviour of a thermodynamic system not in a state of equilibrium; it was devised by Ludwig Boltzmann in 1872. The classic example of such a system is a fluid with temperature gradients in space causing heat to flow from hotter regions to colder ones, by the random but biased transport of the particles making up that fluid. In the modern literature the term Boltzmann equation is often used in a more general sense, referring to any kinetic equation that describes the change of a macroscopic quantity in a thermodynamic system, such as energy, charge or particle number.

The equation arises not by analyzing the individual positions and momenta of each particle in the fluid but rather by considering a probability distribution for the position and momentum of a typical particle—that is, the probability that the particle occupies a given very small region of space (mathematically the volume element $d^{3}\mathbf {r}$ ) centered at the position $\mathbf {r}$ , and has momentum nearly equal to a given momentum vector $\mathbf {p}$ (thus occupying a very small region of momentum space $d^{3}\mathbf {p}$ ), at an instant of time.

The Boltzmann equation can be used to determine how physical quantities change, such as heat energy and momentum, when a fluid is in transport. One may also derive other properties characteristic to fluids such as viscosity, thermal conductivity, and electrical conductivity (by treating the charge carriers in a material as a gas). See also convection–diffusion equation.

The equation is a nonlinear integro-differential equation, and the unknown function in the equation is a probability density function in six-dimensional space of a particle position and momentum. The problem of existence and uniqueness of solutions is still not fully resolved, but some recent results are quite promising.

## Overview

### The phase space and density function

The set of all possible positions **r** and momenta **p** is called the phase space of the system; in other words a set of three coordinates for each position coordinate *x, y, z*, and three more for each momentum component *px*, *py*, *pz*. The entire space is 6-dimensional: a point in this space is (**r**, **p**) = (*x, y, z, px, py, pz*), and each coordinate is parameterized by time *t*. A relevant differential element is written $d^{3}\mathbf {r} \,d^{3}\mathbf {p} =dx\,dy\,dz\,dp_{x}\,dp_{y}\,dp_{z}.$

Since the probability of N molecules, which *all* have **r** and **p** within $d^{3}\mathbf {r} \,d^{3}\mathbf {p}$ , is in question, at the heart of the equation is a quantity *f* which gives this probability per unit phase-space volume, or probability per unit length cubed per unit momentum cubed, at an instant of time t. This is a probability density function: *f*(**r**, **p**, *t*), defined so that, $dN=f(\mathbf {r} ,\mathbf {p} ,t)\,d^{3}\mathbf {r} \,d^{3}\mathbf {p}$ is the number of molecules which *all* have positions lying within a volume element $d^{3}\mathbf {r}$ about **r** and momenta lying within a momentum space element $d^{3}\mathbf {p}$ about **p**, at time t. Integrating over a region of position space and momentum space gives the total number of particles which have positions and momenta in that region:

${\begin{aligned}N&=\int \limits _{\mathrm {momenta} }d^{3}\mathbf {p} \int \limits _{\mathrm {positions} }d^{3}\mathbf {r} \,f(\mathbf {r} ,\mathbf {p} ,t)\\[5pt]&=\iiint \limits _{\mathrm {momenta} }\quad \iiint \limits _{\mathrm {positions} }f(x,y,z,p_{x},p_{y},p_{z},t)\,dx\,dy\,dz\,dp_{x}\,dp_{y}\,dp_{z}\end{aligned}}$

which is a 6-fold integral. While *f* is associated with a number of particles, the phase space is for one-particle (not all of them, which is usually the case with deterministic many-body systems), since only one **r** and **p** is in question. It is not part of the analysis to use **r**1, **p**1 for particle 1, **r**2, **p**2 for particle 2, etc. up to **r***N*, **p***N* for particle *N*.

It is assumed the particles in the system are identical (so each has an identical mass m). For a mixture of more than one chemical species, one distribution is needed for each, see below.

### Principal statement

The general equation can then be written as ${\frac {df}{dt}}=\left({\frac {\partial f}{\partial t}}\right)_{\text{force}}+\left({\frac {\partial f}{\partial t}}\right)_{\text{diff}}+\left({\frac {\partial f}{\partial t}}\right)_{\text{coll}},$

where the "force" term corresponds to the forces exerted on the particles by an external influence (not by the particles themselves), the "diff" term represents the diffusion of particles, and "coll" is the collision term – accounting for the forces acting between particles in collisions. Expressions for each term on the right side are provided below.

Note that some authors use the particle velocity **v** instead of momentum **p**; they are related in the definition of momentum by **p** = *m***v**.

## The force and diffusion terms

Consider particles described by *f*, each experiencing an *external* force **F** not due to other particles (see the collision term for the latter treatment).

Suppose at time t some number of particles all have position **r** within element $d^{3}\mathbf {r}$ and momentum **p** within $d^{3}\mathbf {p}$ . If a force **F** instantly acts on each particle, then at time *t* + Δ*t* their position will be $\mathbf {r} +\Delta \mathbf {r} =\mathbf {r} +{\frac {\mathbf {p} }{m}}\,\Delta t$ and momentum $\mathbf {p} +\Delta \mathbf {p} =\mathbf {p} +\mathbf {F} \Delta t$ . Then, in the absence of collisions, *f* must satisfy

$f\left(\mathbf {r} +{\frac {\mathbf {p} }{m}}\,\Delta t,\mathbf {p} +\mathbf {F} \,\Delta t,t+\Delta t\right)\,d^{3}\mathbf {r} \,d^{3}\mathbf {p} =f(\mathbf {r} ,\mathbf {p} ,t)\,d^{3}\mathbf {r} \,d^{3}\mathbf {p}$

Note that we have used the fact that the phase space volume element $d^{3}\mathbf {r} \,d^{3}\mathbf {p}$ is constant, which can be shown using Hamilton's equations (see the discussion under Liouville's theorem). However, since collisions do occur, the particle density in the phase-space volume $d^{3}\mathbf {r} \,d^{3}\mathbf {p}$ changes, so

| ${\begin{aligned}dN_{\mathrm {coll} }&=\left({\frac {\partial f}{\partial t}}\right)_{\mathrm {coll} }\Delta t\,d^{3}\mathbf {r} \,d^{3}\mathbf {p} \\[5pt]&=f\left(\mathbf {r} +{\frac {\mathbf {p} }{m}}\Delta t,\mathbf {p} +\mathbf {F} \Delta t,t+\Delta t\right)d^{3}\mathbf {r} \,d^{3}\mathbf {p} -f(\mathbf {r} ,\mathbf {p} ,t)\,d^{3}\mathbf {r} \,d^{3}\mathbf {p} \\[5pt]&=\Delta f\,d^{3}\mathbf {r} \,d^{3}\mathbf {p} \end{aligned}}$ |   | 1 |
|---|---|---|

where Δ*f* is the *total* change in *f*. Dividing (**1**) by $d^{3}\mathbf {r} \,d^{3}\mathbf {p} \,\Delta t$ and taking the limits Δ*t* → 0 and Δ*f* → 0, we have

| ${\frac {df}{dt}}=\left({\frac {\partial f}{\partial t}}\right)_{\mathrm {coll} }$ |   | 2 |
|---|---|---|

The total differential of *f* is:

| ${\begin{aligned}df&={\frac {\partial f}{\partial t}}\,dt+\left({\frac {\partial f}{\partial x}}\,dx+{\frac {\partial f}{\partial y}}\,dy+{\frac {\partial f}{\partial z}}\,dz\right)+\left({\frac {\partial f}{\partial p_{x}}}\,dp_{x}+{\frac {\partial f}{\partial p_{y}}}\,dp_{y}+{\frac {\partial f}{\partial p_{z}}}\,dp_{z}\right)\\[5pt]&={\frac {\partial f}{\partial t}}dt+\nabla f\cdot d\mathbf {r} +{\frac {\partial f}{\partial \mathbf {p} }}\cdot d\mathbf {p} \\[5pt]&={\frac {\partial f}{\partial t}}dt+\nabla f\cdot {\frac {\mathbf {p} }{m}}dt+{\frac {\partial f}{\partial \mathbf {p} }}\cdot \mathbf {F} \,dt\end{aligned}}$ |   | 3 |
|---|---|---|

where ∇ is the gradient operator, **·** is the dot product, ${\frac {\partial f}{\partial \mathbf {p} }}=\mathbf {\hat {e}} _{x}{\frac {\partial f}{\partial p_{x}}}+\mathbf {\hat {e}} _{y}{\frac {\partial f}{\partial p_{y}}}+\mathbf {\hat {e}} _{z}{\frac {\partial f}{\partial p_{z}}}=\nabla _{\mathbf {p} }f$ is a shorthand for the momentum analogue of ∇, and **ê***x*, **ê***y*, **ê***z* are Cartesian unit vectors.

### Final statement

Dividing (**3**) by *dt* and substituting into (**2**) gives:

${\frac {\partial f}{\partial t}}+{\frac {\mathbf {p} }{m}}\cdot \nabla f+\mathbf {F} \cdot {\frac {\partial f}{\partial \mathbf {p} }}=\left({\frac {\partial f}{\partial t}}\right)_{\mathrm {coll} }$

In this context, **F**(**r**, *t*) is the force field acting on the particles in the fluid, and m is the mass of the particles. The term on the right hand side is added to describe the effect of collisions between particles; if it is zero then the particles do not collide. The collisionless Boltzmann equation, where individual collisions are replaced with long-range aggregated interactions, e.g. Coulomb interactions, is often called the Vlasov equation.

This equation is more useful than the principal one above, yet still incomplete, since *f* cannot be solved unless the collision term in *f* is known. This term cannot be found as easily or generally as the others – it is a statistical term representing the particle collisions, and requires knowledge of the statistics the particles obey, like the Maxwell–Boltzmann, Fermi–Dirac or Bose–Einstein distributions.

## The collision term (Stosszahlansatz) and molecular chaos

### Two-body collision term

A key insight applied by Boltzmann was to determine the collision term resulting solely from two-body collisions between particles that are assumed to be uncorrelated prior to the collision. This assumption was referred to by Boltzmann as the "*Stosszahlansatz*" and is also known as the "molecular chaos assumption". Under this assumption the collision term can be written as a momentum-space integral over the product of one-particle distribution functions: $\left({\frac {\partial f}{\partial t}}\right)_{\text{coll}}(\mathbf {r} ,\mathbf {p} _{A},t)=\iint gI(g,\Omega )[f(\mathbf {r} ,\mathbf {p} '_{A},t)f(\mathbf {r} ,\mathbf {p} '_{B},t)-f(\mathbf {r} ,\mathbf {p} _{A},t)f(\mathbf {r} ,\mathbf {p} _{B},t)]\,d\Omega \,d^{3}\mathbf {p} _{B},$ where **p***A* and **p***B* are the momenta of any two particles (labeled as *A* and *B* for convenience) before a collision (for the loss term) or after the collision (for the gain term), **p′***A* and **p′***B* are the momenta after the collision (for the loss term) or before the collision (for the gain term), $g=\left|{\frac {\mathbf {p} _{B}}{m}}-{\frac {\mathbf {p} _{A}}{m}}\right|=\left|{\frac {\mathbf {p} '_{B}}{m}}-{\frac {\mathbf {p} '_{A}}{m}}\right|$ is the magnitude of the relative velocity, and *I*(*g*, Ω) is the differential cross section of the collision, in which the relative momenta of the colliding particles turns through an angle θ into the element of the solid angle *d*Ω, due to the collision. Note that g is a function of **p***A* and **p***B*, and **p′***A* together with **p′***B* are functions of **p***A*, **p***B*, and θ (hidden in *d*Ω).

### Simplifications to the collision term

Since much of the challenge in solving the Boltzmann equation originates with the complex collision term, attempts have been made to "model" and simplify the collision term. The best known model equation is due to Bhatnagar, Gross and Krook. The assumption in the BGK approximation is that the effect of molecular collisions is to force a non-equilibrium distribution function at a point in physical space back to a Maxwellian equilibrium distribution function and that the rate at which this occurs is proportional to the molecular collision frequency. The Boltzmann equation is therefore modified to the BGK form:

${\frac {\partial f}{\partial t}}+{\frac {\mathbf {p} }{m}}\cdot \nabla f+\mathbf {F} \cdot {\frac {\partial f}{\partial \mathbf {p} }}=\nu (f_{0}-f),$

where $\nu$ is the molecular collision frequency, and $f_{0}$ is the local Maxwellian distribution function given the gas temperature at this point in space. This is also called "relaxation time approximation".

## General equation (for a mixture)

For a mixture of chemical species labelled by indices $i=1,2,3,\dots ,n$ the equation for species i is

${\frac {\partial f_{i}}{\partial t}}+{\frac {\mathbf {p} _{i}}{m_{i}}}\cdot \nabla f_{i}+\mathbf {F} \cdot {\frac {\partial f_{i}}{\partial \mathbf {p} _{i}}}=\left({\frac {\partial f_{i}}{\partial t}}\right)_{\text{coll}},$

where *fi* = *fi*(**r**, **p***i*, *t*), and the collision term is

$\left({\frac {\partial f_{i}}{\partial t}}\right)_{\mathrm {coll} }(\mathbf {r} ,\mathbf {p} _{i},t)=\sum _{j=1}^{n}\iint g_{ij}I_{ij}(g_{ij},\Omega )[f'_{i}f'_{j}-f_{i}f_{j}]\,d\Omega \,d^{3}\mathbf {p'} ,$

where *f′* = *f′*(**p′***i*, *t*), the magnitude of the relative velocities is

$g_{ij}=\left|{\frac {\mathbf {p} _{i}}{m_{i}}}-{\frac {\mathbf {p} _{j}}{m_{j}}}\right|=\left|{\frac {\mathbf {p} '_{i}}{m_{i}}}-{\frac {\mathbf {p} '_{j}}{m_{j}}}\right|,$

and *Iij* is the differential cross-section, as before, between particles *i* and *j*. The integration is over the momentum components in the integrand (which are labelled *i* and *j*). The sum of integrals describes the entry and exit of particles of species *i* in or out of the phase-space element.

## Applications and extensions

### Conservation equations

The Boltzmann equation can be used to derive the fluid dynamic conservation laws for mass, charge, momentum, and energy. For a fluid consisting of only one kind of particle, the number density n is given by $n=\int f\,d^{3}\mathbf {p} .$

The average value of any function *A* is $\langle A\rangle ={\frac {1}{n}}\int Af\,d^{3}\mathbf {p} .$

Since the conservation equations involve tensors, the Einstein summation convention will be used where repeated indices in a product indicate summation over those indices. Thus $\mathbf {x} \mapsto x_{i}$ and $\mathbf {p} \mapsto p_{i}=mv_{i}$ , where $v_{i}$ is the particle velocity vector. Define $A(p_{i})$ as some function of momentum $p_{i}$ only, whose total value is conserved in a collision. Assume also that the force $F_{i}$ is a function of position only, and that *f* is zero for $p_{i}\to \pm \infty$ . Multiplying the Boltzmann equation by *A* and integrating over momentum yields four terms, which, using integration by parts, can be expressed as

$\int A{\frac {\partial f}{\partial t}}\,d^{3}\mathbf {p} ={\frac {\partial }{\partial t}}(n\langle A\rangle ),$

$\int {\frac {p_{j}A}{m}}{\frac {\partial f}{\partial x_{j}}}\,d^{3}\mathbf {p} ={\frac {1}{m}}{\frac {\partial }{\partial x_{j}}}(n\langle Ap_{j}\rangle ),$

$\int AF_{j}{\frac {\partial f}{\partial p_{j}}}\,d^{3}\mathbf {p} =-nF_{j}\left\langle {\frac {\partial A}{\partial p_{j}}}\right\rangle ,$

$\int A\left({\frac {\partial f}{\partial t}}\right)_{\text{coll}}\,d^{3}\mathbf {p} ={\frac {\partial }{\partial t}}_{\text{coll}}(n\langle A\rangle )=0,$

where the last term is zero, since *A* is conserved in a collision. The values of *A* correspond to moments of velocity $v_{i}$ (and momentum $p_{i}$ , as they are linearly dependent).

#### Zeroth moment

Letting $A=m(v_{i})^{0}=m$ , the mass of the particle, the integrated Boltzmann equation becomes the conservation of mass equation: ${\frac {\partial }{\partial t}}\rho +{\frac {\partial }{\partial x_{j}}}(\rho V_{j})=0,$ where $\rho =mn$ is the mass density, and $V_{i}=\langle v_{i}\rangle$ is the average fluid velocity.

#### First moment

Letting $A=m(v_{i})^{1}=p_{i}$ , the momentum of the particle, the integrated Boltzmann equation becomes the conservation of momentum equation:

${\frac {\partial }{\partial t}}(\rho V_{i})+{\frac {\partial }{\partial x_{j}}}(\rho V_{i}V_{j}+P_{ij})-nF_{i}=0,$

where $P_{ij}=\rho \langle (v_{i}-V_{i})(v_{j}-V_{j})\rangle$ is the pressure tensor (the viscous stress tensor plus the hydrostatic pressure).

#### Second moment

Letting $A={\frac {m(v_{i})^{2}}{2}}={\frac {p_{i}p_{i}}{2m}}$ , the kinetic energy of the particle, the integrated Boltzmann equation becomes the conservation of energy equation:

${\frac {\partial }{\partial t}}\left(u+{\tfrac {1}{2}}\rho V_{i}V_{i}\right)+{\frac {\partial }{\partial x_{j}}}\left(uV_{j}+{\tfrac {1}{2}}\rho V_{i}V_{i}V_{j}+J_{qj}+P_{ij}V_{i}\right)-nF_{i}V_{i}=0,$

where ${\textstyle u={\tfrac {1}{2}}\rho \langle (v_{i}-V_{i})(v_{i}-V_{i})\rangle }$ is the kinetic thermal energy density, and ${\textstyle J_{qi}={\tfrac {1}{2}}\rho \langle (v_{i}-V_{i})(v_{k}-V_{k})(v_{k}-V_{k})\rangle }$ is the heat flux vector.

### Hamiltonian mechanics

In Hamiltonian mechanics, the Boltzmann equation is often written more generally as ${\hat {\mathbf {L} }}[f]=\mathbf {C} [f],$ where **L** is the Liouville operator (note that the Liouville operator is defined via the Hamiltonian in the linked article rather than forces) describing the evolution of a phase space volume and **C** is the collision operator. The non-relativistic form of **L** is ${\hat {\mathbf {L} }}_{\mathrm {NR} }={\frac {\partial }{\partial t}}+{\frac {\mathbf {p} }{m}}\cdot \nabla +\mathbf {F} \cdot {\frac {\partial }{\partial \mathbf {p} }}\,.$

### Quantum theory and violation of particle number conservation

It is possible to write down relativistic quantum Boltzmann equations for relativistic quantum systems in which the number of particles is not conserved in collisions. This has several applications in physical cosmology, including the formation of the light elements in Big Bang nucleosynthesis, the production of dark matter and baryogenesis. It is not a priori clear that the state of a quantum system can be characterized by a classical phase space density *f*. However, for a wide class of applications a well-defined generalization of *f* exists which is the solution of an effective Boltzmann equation that can be derived from first principles of quantum field theory.

### General relativity and astronomy

The Boltzmann equation is of use in galactic dynamics. A galaxy, under certain assumptions, may be approximated as a continuous fluid; its mass distribution is then represented by *f*; in galaxies, physical collisions between the stars are very rare, and the effect of *gravitational collisions* can be neglected for times far longer than the age of the universe.

Its generalization in general relativity is ${\hat {\mathbf {L} }}_{\mathrm {GR} }[f]=p^{\alpha }{\frac {\partial f}{\partial x^{\alpha }}}-\Gamma _{\beta \gamma }^{\alpha }p^{\beta }p^{\gamma }{\frac {\partial f}{\partial p^{\alpha }}}=C[f],$ where Γαβγ is the Christoffel symbol of the second kind (this assumes there are no external forces, so that particles move along geodesics in the absence of collisions), with the important subtlety that the density is a function in mixed contravariant-covariant (*xi*, *pi*) phase space as opposed to fully contravariant (*xi*, *pi*) phase space.

In physical cosmology the fully covariant approach has been used to study the cosmic microwave background radiation. More generically the study of processes in the early universe often attempt to take into account the effects of quantum mechanics and general relativity. In the very dense medium formed by the primordial plasma after the Big Bang, particles are continuously created and annihilated. In such an environment quantum coherence and the spatial extension of the wavefunction can affect the dynamics, making it questionable whether the classical phase space distribution *f* that appears in the Boltzmann equation is suitable to describe the system. In many cases it is, however, possible to derive an effective Boltzmann equation for a generalized distribution function from first principles of quantum field theory. This includes the formation of the light elements in Big Bang nucleosynthesis, the production of dark matter and baryogenesis.

## Solving the equation

Exact solutions to the Boltzmann equations have been proven to exist in some cases; this analytical approach provides insight, but is not generally usable in practical problems. Assuming a specific inverse power law between interacting particles, fully closed-form solutions to boundary value problems involving gross, spatially homogenous rates of deformation can be found and studied analytically.

Instead, numerical methods (including finite elements and lattice Boltzmann methods) are generally used to find approximate solutions to the various forms of the Boltzmann equation. Example applications range from hypersonic aerodynamics in rarefied gas flows to plasma flows. An application of the Boltzmann equation in electrodynamics is the calculation of the electrical conductivity - the result is in leading order identical with the semiclassical result.

Close to local equilibrium, solution of the Boltzmann equation can be represented by an asymptotic expansion in powers of Knudsen number (the Chapman–Enskog expansion). The first two terms of this expansion give the Euler equations and the Navier–Stokes equations. The higher terms have singularities. The problem of developing mathematically the limiting processes, which lead from the atomistic view (represented by Boltzmann's equation) to the laws of motion of continua, is an important part of Hilbert's sixth problem.

## Limitations and further uses of the Boltzmann equation

The Boltzmann equation is valid only under several assumptions. For instance, the particles are assumed to be pointlike, i.e. without having a finite size. There exists a generalization of the Boltzmann equation that is called the Enskog equation. The collision term is modified in Enskog equations such that particles have a finite size, for example they can be modelled as spheres having a fixed radius.

No further degrees of freedom besides translational motion are assumed for the particles. If there are internal degrees of freedom, the Boltzmann equation has to be generalized and might possess inelastic collisions.

Many real fluids like liquids or dense gases have besides the features mentioned above more complex forms of collisions, there will be not only binary, but also ternary and higher order collisions. These must be derived by using the BBGKY hierarchy.

Boltzmann-like equations are also used for the movement of cells. Since cells are composite particles that carry internal degrees of freedom, the corresponding generalized Boltzmann equations must have inelastic collision integrals. Such equations can describe invasions of cancer cells in tissue, morphogenesis, and chemotaxis-related effects.

## Long-time derivation of the Boltzmann equation from Newtonian mechanics

In 2024, Yu Deng, Zaher Hani, and Xiao Ma established a major extension of Lanford's theorem by proving that the Boltzmann equation can be rigorously derived from the Newtonian mechanics of a dilute gas of hard spheres for *practically unlimited time intervals*. This result extends the 1975 breakthrough by Oscar Lanford, which was restricted to very short times, and provides a complete microscopic-to-mesoscopic derivation valid as long as the corresponding Boltzmann equation admits a classical solution. This work addresses a key aspect of Hilbert's sixth problem by rigorously linking particle-level Newtonian dynamics with the mesoscopic kinetic description, and contributes to understanding how macroscopic irreversibility emerges from time-reversible microscopic laws.

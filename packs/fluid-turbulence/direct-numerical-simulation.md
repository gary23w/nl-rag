---
title: "Direct numerical simulation"
source: https://en.wikipedia.org/wiki/Direct_numerical_simulation
domain: fluid-turbulence
license: CC-BY-SA-4.0
tags: fluid turbulence, turbulence modeling, large eddy simulation, direct numerical simulation
fetched: 2026-07-02
---

# Direct numerical simulation

A **direct numerical simulation** (**DNS**) is a simulation in computational fluid dynamics (CFD) in which the Navier–Stokes equations are numerically solved without any turbulence model. This means that the whole range of spatial and temporal scales of the turbulence must be resolved. All the spatial scales of the turbulence must be resolved in the computational mesh, from the smallest dissipative scales (Kolmogorov microscales), up to the integral scale L , associated with the motions containing most of the kinetic energy. The Kolmogorov scale, $\eta$ , is given by

$\eta =(\nu ^{3}/\varepsilon )^{1/4}$

where $\nu$ is the kinematic viscosity and $\varepsilon$ is the rate of kinetic energy dissipation. On the other hand, the integral scale depends usually on the spatial scale of the boundary conditions.

To satisfy these resolution requirements, the number of points N along a given mesh direction with increments h , must be

$Nh>L,\,$

so that the integral scale is contained within the computational domain, and also

$h\leq \eta ,\,$

so that the Kolmogorov scale can be resolved.

Since

$\varepsilon \approx {u'}^{3}/L,$

where $u'$ is the root mean square (RMS) of the velocity, the previous relations imply that a three-dimensional DNS requires a number of mesh points $N^{3}$ satisfying

$N^{3}\geq \mathrm {Re} ^{9/4}=\mathrm {Re} ^{2.25}$

where $\mathrm {Re}$ is the turbulent Reynolds number:

$\mathrm {Re} ={\frac {u'L}{\nu }}.$

Hence, the memory storage requirement in a DNS grows very fast with the Reynolds number. In addition, given the very large memory necessary, the integration of the solution in time must be done by an explicit method. This means that in order to be accurate, the integration, for most discretization methods, must be done with a time step, $\Delta t$ , small enough such that a fluid particle moves only a fraction of the mesh spacing h in each step. That is,

$C={\frac {u'\Delta t}{h}}<1$

( C is here the Courant number). The total time interval simulated is generally proportional to the turbulence time scale $\tau$ given by

$\tau ={\frac {L}{u'}}.$

Combining these relations, and the fact that h must be of the order of $\eta$ , the number of time-integration steps must be proportional to $L/(C\eta )$ . On the other hand, from the definitions for $\mathrm {Re}$ , $\eta$ and L given above, it follows that

${\frac {L}{\eta }}\sim \mathrm {Re} ^{3/4},$

and consequently, the number of time steps grows also as a power law of the Reynolds number.

One can estimate that the number of floating-point operations required to complete the simulation is proportional to the number of mesh points and the number of time steps, and in conclusion, the number of operations grows as $\mathrm {Re} ^{3}$ .

Therefore, the computational cost of DNS is very high, even at low Reynolds numbers. For the Reynolds numbers encountered in most industrial applications, the computational resources required by a DNS would exceed the capacity of the most powerful computers currently available. However, direct numerical simulation is a useful tool in fundamental research in turbulence. Using DNS it is possible to perform "numerical experiments", and extract from them information difficult or impossible to obtain in the laboratory, allowing a better understanding of the physics of turbulence. Also, direct numerical simulations are useful in the development of turbulence models for practical applications, such as sub-grid scale models for large eddy simulation (LES) and models for methods that solve the Reynolds-averaged Navier–Stokes equations (RANS). This is done by means of "a priori" tests, in which the input data for the model is taken from a DNS simulation, or by "a posteriori" tests, in which the results produced by the model are compared with those obtained by DNS.

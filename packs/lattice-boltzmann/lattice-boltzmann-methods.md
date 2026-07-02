---
title: "Lattice Boltzmann methods"
source: https://en.wikipedia.org/wiki/Lattice_Boltzmann_methods
domain: lattice-boltzmann
license: CC-BY-SA-4.0
tags: lattice boltzmann method, boltzmann equation, kinetic theory of gases, lattice gas automaton
fetched: 2026-07-02
---

# Lattice Boltzmann methods

The **lattice Boltzmann methods (LBM)**, originated from the lattice gas automata (LGA) method (Hardy-Pomeau-Pazzis and Frisch-Hasslacher-Pomeau models), is a class of computational fluid dynamics (CFD) methods for fluid simulation. Instead of solving the Navier–Stokes equations directly, a fluid density on a lattice is simulated with streaming and collision (relaxation) processes. The method is versatile as the model fluid can straightforwardly be made to mimic common fluid behaviour like vapour/liquid coexistence, and so fluid systems such as liquid droplets can be simulated. Also, fluids in complex environments such as porous media can be straightforwardly simulated, whereas with complex boundaries other CFD methods can be hard to work with.

## Algorithm

Unlike CFD methods that solve the conservation equations of macroscopic properties (i.e., mass, momentum, and energy) numerically, LBM models the fluid consisting of fictive particles, and such particles perform consecutive propagation and collision processes over a discrete lattice. Due to its particulate nature and local dynamics, LBM has several advantages over other conventional CFD methods, especially in dealing with complex boundaries, incorporating microscopic interactions, and parallelization of the algorithm. A different interpretation of the lattice Boltzmann equation is that of a discrete-velocity Boltzmann equation. The numerical methods of solution of the system of partial differential equations then give rise to a discrete map, which can be interpreted as the propagation and collision of fictitious particles.

In an algorithm, there are collision and streaming steps. These evolve the density of the fluid $\rho ({\vec {x}},t)$ , for ${\vec {x}}$ the position and t the time. As the fluid is on a lattice, the density has a number of components $f_{i},i=0,\ldots ,a$ equal to the number of lattice vectors connected to each lattice point. As an example, the lattice vectors for a simple lattice used in simulations in two dimensions is shown here. This lattice is usually denoted D2Q9, for two dimensions and nine vectors: four vectors along north, east, south and west, plus four vectors to the corners of a unit square, plus a vector with both components zero. Then, for example vector ${\vec {e}}_{4}=(0,-1)$ , i.e., it points due south and so has no x component but a y component of $-1$ . So one of the nine components of the total density at the central lattice point, $f_{4}({\vec {x}},t)$ , is that part of the fluid at point ${\vec {x}}$ moving due south, at a speed in lattice units of one.

Then the steps that evolve the fluid in time are:

**The collision step**

For the Bhatnagar Gross and Krook (BGK) model, which leads relaxation to equilibrium via collisions between the molecules of a fluid, we have

$f_{i}^{\ast }({\vec {x}},t)=f_{i}({\vec {x}},t)+{\frac {f_{i}^{eq}({\vec {x}},t)-f_{i}({\vec {x}},t)}{\tau _{f}}}\,\!$

,

where $f_{i}^{\ast }({\vec {x}},t)$ is the new lattice density, and $f_{i}^{eq}({\vec {x}},t)$ is the equilibrium density along direction *i* which can be expressed by using a Taylor expansion (see below, in Mathematical equations for simulations):

$f_{i}^{eq}=\omega _{i}\rho \left(1+{\frac {3{\vec {e}}_{i}\cdot {\vec {u}}}{c^{2}}}+{\frac {9({\vec {e}}_{i}\cdot {\vec {u}})^{2}}{2c^{4}}}-{\frac {3({\vec {u}}\cdot {\vec {u}})}{2c^{2}}}\right)$

.

The model assumes that the fluid locally relaxes to equilibrium over a characteristic timescale $\tau _{f}$ . This timescale determines the kinematic viscosity, the larger it is, the larger is the kinematic viscosity.

**The streaming step**

$f_{i}({\vec {x}}+{\vec {e}}_{i}\delta _{t},t+\delta _{t})=f_{i}^{\ast }({\vec {x}},t)\,\!$

As $f_{i}^{\ast }({\vec {x}},t)$ is, by definition, the fluid density at point ${\vec {x}}$ at time t , that is moving at a velocity of ${\vec {e}}_{i}$ per time step, then at the next time step $t+\delta _{t}$ it will have flowed to point ${\vec {x}}+{\vec {e}}_{i}\delta _{t}$ .

## Advantages

- The LBM was designed from scratch to run efficiently on massively parallel architectures, ranging from inexpensive embedded FPGAs and DSPs up to GPUs and heterogeneous clusters and supercomputers (even with a slow interconnection network). It enables complex physics and sophisticated algorithms. Efficiency leads to a qualitatively new level of understanding since it allows solving problems that previously could not be approached (or only with insufficient accuracy).
- The method originates from a molecular description of a fluid and can directly incorporate physical terms stemming from a knowledge of the interaction between molecules. Hence it is an indispensable instrument in fundamental research, as it keeps the cycle between the elaboration of a theory and the formulation of a corresponding numerical model short.
- Automated data pre-processing and lattice generation in a time that accounts for a small fraction of the total simulation.
- Parallel data analysis, post-processing and evaluation.
- Fully resolved multi-phase flow with small droplets and bubbles.
- Fully resolved flow through complex geometries and porous media.
- Complex, coupled flow with heat transfer and chemical reactions.

## Limitations and development

As with Navier–Stokes based CFD, LBM methods have been successfully coupled with thermal-specific solutions to enable heat transfer (solids-based conduction, convection and radiation) simulation capability. For multiphase/multicomponent models, the interface thickness is usually large and the density ratio across the interface is small when compared with real fluids. Recently this problem has been resolved by Yuan and Schaefer who improved on models by Shan and Chen, Swift, and He, Chen, and Zhang. They were able to reach density ratios of 1000:1 by simply changing the equation of state. It has been proposed to apply Galilean Transformation to overcome the limitation of modelling high-speed fluid flows. The fast advancements of this method had also successfully simulated microfluidics, However, as of now, LBM is still limited in simulating high Knudsen number flows where Monte Carlo methods are instead used, and high-Mach number flows in aerodynamics are still difficult for LBM, and a consistent thermo-hydrodynamic scheme is absent.

## Development from the LGA method

LBM originated from the lattice gas automata (LGA) method, which can be considered as a simplified fictitious molecular dynamics model in which space, time, and particle velocities are all discrete. For example, in the 2-dimensional FHP Model each lattice node is connected to its neighbors by 6 lattice velocities on a triangular lattice; there can be either 0 or 1 particles at a lattice node moving with a given lattice velocity. After a time interval, each particle will move to the neighboring node in its direction; this process is called the propagation or streaming step. When more than one particle arrives at the same node from different directions, they collide and change their velocities according to a set of collision rules. Streaming steps and collision steps alternate. Suitable collision rules should conserve the particle number (mass), momentum, and energy before and after the collision. LGA suffer from several innate defects for use in hydrodynamic simulations: lack of Galilean invariance for fast flows, statistical noise and poor Reynolds number scaling with lattice size. LGA are, however, well suited to simplify and extend the reach of reaction diffusion and molecular dynamics models.

The main motivation for the transition from LGA to LBM was the desire to remove the statistical noise by replacing the Boolean particle number in a lattice direction with its ensemble average, the so-called density distribution function. Accompanying this replacement, the discrete collision rule is also replaced by a continuous function known as the collision operator. In the LBM development, an important simplification is to approximate the collision operator with the Bhatnagar-Gross-Krook (BGK) relaxation term. This lattice BGK (LBGK) model makes simulations more efficient and allows flexibility of the transport coefficients. On the other hand, it has been shown that the LBM scheme can also be considered as a special discretized form of the continuous Boltzmann equation. From Chapman-Enskog theory, one can recover the governing continuity and Navier–Stokes equations from the LBM algorithm.

## Lattices and the D*n*Q*m* classification

Lattice Boltzmann models can be operated on a number of different lattices, both cubic and triangular, and with or without rest particles in the discrete distribution function.

A popular way of classifying the different methods by lattice is the D*n*Q*m* scheme. Here "D*n*" stands for "*n* dimensions", while "Q*m*" stands for "*m* speeds". For example, D3Q15 is a 3-dimensional lattice Boltzmann model on a cubic grid, with rest particles present. Each node has a crystal shape and can deliver particles to 15 nodes: each of the 6 neighboring nodes that share a surface, the 8 neighboring nodes sharing a corner, and itself. (The D3Q15 model does not contain particles moving to the 12 neighboring nodes that share an edge; adding those would create a "D3Q27" model.)

Real quantities as space and time need to be converted to lattice units prior to simulation. Nondimensional quantities, like the Reynolds number, remain the same.

## Lattice units conversion

In most Lattice Boltzmann simulations $\delta _{x}\,\!$ is the basic unit for lattice spacing, so if the domain of length $L\,\!$ has $N\,\!$ lattice units along its entire length, the space unit is simply defined as $\delta _{x}=L/N\,\!$ . Speeds in lattice Boltzmann simulations are typically given in terms of the speed of sound. The discrete time unit can therefore be given as $\delta _{t}={\frac {\delta _{x}}{C_{s}}}\,\!$ , where the denominator $C_{s}$ is the physical speed of sound.

For small-scale flows (such as those seen in porous media mechanics), operating with the true speed of sound can lead to unacceptably short time steps. It is therefore common to raise the lattice Mach number to something much larger than the real Mach number, and compensating for this by raising the viscosity as well in order to preserve the Reynolds number.

## Simulation of mixtures

Simulating multiphase/multicomponent flows has always been a challenge to conventional CFD because of the moving and deformable interfaces. More fundamentally, the interfaces between different phases (liquid and vapor) or components (e.g., oil and water) originate from the specific interactions among fluid molecules. Therefore, it is difficult to implement such microscopic interactions into the macroscopic Navier–Stokes equation. However, in LBM, the particulate kinetics provides a relatively easy and consistent way to incorporate the underlying microscopic interactions by modifying the collision operator. Several LBM multiphase/multicomponent models have been developed. Here phase separations are generated automatically from the particle dynamics and no special treatment is needed to manipulate the interfaces as in traditional CFD methods. Successful applications of multiphase/multicomponent LBM models can be found in various complex fluid systems, including interface instability, bubble/droplet dynamics, wetting on solid surfaces, interfacial slip, and droplet electrohydrodynamic deformations.

A lattice Boltzmann model for simulation of gas mixture combustion capable of accommodating significant density variations at low-Mach number regime has been recently proposed.

To this respect, it is worth to notice that, since LBM deals with a larger set of fields (as compared to conventional CFD), the simulation of reactive gas mixtures presents some additional challenges in terms of memory demand as far as large detailed combustion mechanisms are concerned. Those issues may be addressed, though, by resorting to systematic model reduction techniques.

## Thermal lattice-Boltzmann method

Currently (2009), a thermal lattice-Boltzmann method (TLBM) falls into one of three categories: the multi-speed approach, the passive scalar approach, and the thermal energy distribution.

## Derivation of Navier–Stokes equation from discrete LBE

Starting with the discrete lattice Boltzmann equation (also referred to as LBGK equation due to the collision operator used). We first do a 2nd-order Taylor series expansion about the left side of the LBE. This is chosen over a simpler 1st-order Taylor expansion as the discrete LBE cannot be recovered. When doing the 2nd-order Taylor series expansion, the zero derivative term and the first term on the right will cancel, leaving only the first and second derivative terms of the Taylor expansion and the collision operator:

$f_{i}({\vec {x}}+{\vec {e}}_{i}\delta _{t},t+\delta _{t})=f_{i}({\vec {x}},t)+{\frac {\delta _{t}}{\tau _{f}}}(f_{i}^{eq}-f_{i}).$

For simplicity, write $f_{i}({\vec {x}},t)$ as $f_{i}$ . The slightly simplified Taylor series expansion is then as follows, where ":" is the colon product between dyads:

${\frac {\partial f_{i}}{\partial t}}+{\vec {e}}_{i}\cdot \nabla f_{i}+\left({\frac {1}{2}}{\vec {e}}_{i}{\vec {e}}_{i}:\nabla \nabla f_{i}+{\vec {e}}_{i}\cdot \nabla {\frac {\partial f_{i}}{\partial t}}+{\frac {1}{2}}{\frac {\partial ^{2}f_{i}}{\partial t^{2}}}\right)={\frac {1}{\tau }}(f_{i}^{eq}-f_{i}).$

By expanding the particle distribution function into equilibrium and non-equilibrium components and using the Chapman-Enskog expansion, where K is the Knudsen number, the Taylor-expanded LBE can be decomposed into different magnitudes of order for the Knudsen number in order to obtain the proper continuum equations:

$f_{i}=f_{i}^{\text{eq}}+Kf_{i}^{\text{neq}},$

$f_{i}^{\text{neq}}=f_{i}^{(1)}+Kf_{i}^{(2)}+O(K^{2}).$

The equilibrium and non-equilibrium distributions satisfy the following relations to their macroscopic variables (these will be used later, once the particle distributions are in the "correct form" in order to scale from the particle to macroscopic level):

$\rho =\sum _{i}f_{i}^{\text{eq}},$

$\rho {\vec {u}}=\sum _{i}f_{i}^{\text{eq}}{\vec {e}}_{i},$

$0=\sum _{i}f_{i}^{(k)}\qquad {\text{for }}k=1,2,$

$0=\sum _{i}f_{i}^{(k)}{\vec {e}}_{i}.$

The Chapman-Enskog expansion is then:

${\frac {\partial }{\partial t}}=K{\frac {\partial }{\partial t_{1}}}+K^{2}{\frac {\partial }{\partial t_{2}}}\qquad {\text{for }}t_{2}({\text{diffusive time-scale}})\ll t_{1}({\text{convective time-scale}}),$

${\frac {\partial }{\partial x}}=K{\frac {\partial }{\partial x_{1}}}.$

By substituting the expanded equilibrium and non-equilibrium into the Taylor expansion and separating into different orders of K , the continuum equations are nearly derived.

For order $K^{0}$ :

${\frac {\partial f_{i}^{\text{eq}}}{\partial t_{1}}}+{\vec {e}}_{i}\nabla _{1}f_{i}^{\text{eq}}=-{\frac {f_{i}^{(1)}}{\tau }}.$

For order $K^{1}$ :

${\frac {\partial f_{i}^{(1)}}{\partial t_{1}}}+{\frac {\partial f_{i}^{\text{eq}}}{\partial t_{2}}}+{\vec {e}}_{i}\nabla f_{i}^{(1)}+{\frac {1}{2}}{\vec {e}}_{i}{\vec {e}}_{i}:\nabla \nabla f_{i}^{\text{eq}}+{\vec {e}}_{i}\cdot \nabla {\frac {\partial f_{i}^{\text{eq}}}{\partial t_{1}}}+{\frac {1}{2}}{\frac {\partial ^{2}f_{i}^{\text{eq}}}{\partial t_{1}^{2}}}=-{\frac {f_{i}^{(2)}}{\tau }}.$

Then, the second equation can be simplified with some algebra and the first equation into the following:

${\frac {\partial f_{i}^{\text{eq}}}{\partial t_{2}}}+\left(1-{\frac {1}{2\tau }}\right)\left[{\frac {\partial f_{i}^{(1)}}{\partial t_{1}}}+{\vec {e}}_{i}\nabla _{1}f_{i}^{(1)}\right]=-{\frac {f_{i}^{(2)}}{\tau }}.$

Applying the relations between the particle distribution functions and the macroscopic properties from above, the mass and momentum equations are achieved:

${\frac {\partial \rho }{\partial t}}+\nabla \cdot \rho {\vec {u}}=0,$

${\frac {\partial \rho {\vec {u}}}{\partial t}}+\nabla \cdot \Pi =0.$

The momentum flux tensor $\Pi$ has the following form then:

$\Pi _{xy}=\sum _{i}{\vec {e}}_{ix}{\vec {e}}_{iy}\left[f_{i}^{eq}+\left(1-{\frac {1}{2\tau }}\right)f_{i}^{(1)}\right],$

where ${\vec {e}}_{ix}{\vec {e}}_{iy}$ is shorthand for the square of the sum of all the components of ${\vec {e}}_{i}$ (i. e. $\textstyle \left(\sum _{x}{\vec {e}}_{ix}\right)^{2}=\sum _{x}\sum _{y}{\vec {e}}_{ix}{\vec {e}}_{iy}$ ), and the equilibrium particle distribution with second order to be comparable to the Navier–Stokes equation is:

$f_{i}^{\text{eq}}=\omega _{i}\rho \left(1+{\frac {{\vec {e}}_{i}{\vec {u}}}{c_{s}^{2}}}+{\frac {({\vec {e}}_{i}{\vec {u}})^{2}}{2c_{s}^{4}}}-{\frac {{\vec {u}}^{2}}{2c_{s}^{2}}}\right).$

The equilibrium distribution is only valid for small velocities or small Mach numbers. Inserting the equilibrium distribution back into the flux tensor leads to:

$\Pi _{xy}^{(0)}=\sum _{i}{\vec {e}}_{ix}{\vec {e}}_{iy}f_{i}^{eq}=p\delta _{xy}+\rho u_{x}u_{y},$

$\Pi _{xy}^{(1)}=\left(1-{\frac {1}{2\tau }}\right)\sum _{i}{\vec {e}}_{ix}{\vec {e}}_{iy}f_{i}^{(1)}=\nu \left(\nabla _{x}\left(\rho {\vec {u}}_{y}\right)+\nabla _{y}\left(\rho {\vec {u}}_{x}\right)\right).$

Finally, the Navier–Stokes equation is recovered under the assumption that density variation is small:

$\rho \left({\frac {\partial {\vec {u}}_{x}}{\partial t}}+\nabla _{y}\cdot {\vec {u}}_{x}{\vec {u}}_{y}\right)=-\nabla _{x}p+\nu \nabla _{y}\cdot \left(\nabla _{x}\left(\rho {\vec {u}}_{y}\right)+\nabla _{y}\left(\rho {\vec {u}}_{x}\right)\right).$

This derivation follows the work of Chen and Doolen.

## Mathematical equations for simulations

The continuous Boltzmann equation is an evolution equation for a single particle probability distribution function $f({\vec {x}},{\vec {e}}_{i},t)$ and the internal energy density distribution function $g({\vec {x}},{\vec {e}}_{i},t)$ (He et al.) are each respectively:

$\partial _{t}f+({\vec {e}}\cdot \nabla )f+F\partial _{v}f=\Omega (f),$

$\partial _{t}g+({\vec {e}}\cdot \nabla )g+G\partial _{v}f=\Omega (g),$

where $g({\vec {x}},{\vec {e}}_{i},t)$ is related to $f({\vec {x}},{\vec {e}}_{i},t)$ by

$g({\vec {x}},{\vec {e}}_{i},t)={\frac {({\vec {e}}-{\vec {u}})^{2}}{2}}f({\vec {x}},{\vec {e}}_{i},t),$

F is an external force, $\Omega$ is a collision integral, and ${\vec {e}}$ (also labeled by ${\vec {\xi }}$ in literature) is the microscopic velocity. The external force F is related to temperature external force G by the relation below. A typical test for one's model is the Rayleigh–Bénard convection for G .

$F={\frac {{\vec {G}}\cdot ({\vec {e}}-{\vec {u}})}{RT}}f^{\text{eq}},$

${\vec {G}}=\beta g_{0}(T-T_{avg}){\vec {k}}.$

Macroscopic variables such as density $\rho$ , velocity ${\vec {u}}$ , and temperature T can be calculated as the moments of the density distribution function:

$\rho =\int f\,d{\vec {e}},$

$\rho {\vec {u}}=\int {\vec {e}}f\,d{\vec {e}},$

${\frac {\rho DRT}{2}}=\rho \epsilon =\int g\,d{\vec {e}}.$

The lattice Boltzmann method discretizes this equation by limiting space to a lattice and the velocity space to a discrete set of microscopic velocities (i. e. ${\vec {e}}_{i}=({\vec {e}}_{ix},{\vec {e}}_{iy})$ ). The microscopic velocities in D2Q9, D3Q15, and D3Q19 for example are given as:

${\vec {e}}_{i}=c\times {\begin{cases}(0,0)&i=0\\(1,0),(0,1),(-1,0),(0,-1)&i=1,2,3,4\\(1,1),(-1,1),(-1,-1),(1,-1)&i=5,6,7,8\\\end{cases}}$

${\vec {e}}_{i}=c\times {\begin{cases}(0,0,0)&i=0\\(\pm 1,0,0),(0,\pm 1,0),(0,0,\pm 1)&i=1,2,...,5,6\\(\pm 1,\pm 1,\pm 1)&i=7,8,...,13,14\\\end{cases}}$

${\vec {e}}_{i}=c\times {\begin{cases}(0,0,0)&i=0\\(\pm 1,0,0),(0,\pm 1,0),(0,0,\pm 1)&i=1,2,...,5,6\\(\pm 1,\pm 1,0),(\pm 1,0,\pm 1),(0,\pm 1,\pm 1)&i=7,8,...,17,18\\\end{cases}}$

The single-phase discretized Boltzmann equation for mass density and internal energy density are:

$f_{i}({\vec {x}}+{\vec {e}}_{i}\delta _{t},t+\delta _{t})-f_{i}({\vec {x}},t)+F_{i}=\Omega (f),$

$g_{i}({\vec {x}}+{\vec {e}}_{i}\delta _{t},t+\delta _{t})-g_{i}({\vec {x}},t)+G_{i}=\Omega (g).$

The collision operator is often approximated by a BGK collision operator under the condition it also satisfies the conservation laws:

$\Omega (f)={\frac {1}{\tau _{f}}}(f_{i}^{\text{eq}}-f_{i}),$

$\Omega (g)={\frac {1}{\tau _{g}}}(g_{i}^{\text{eq}}-g_{i}).$

In the collision operator $f_{i}^{\text{eq}}$ is the discrete, equilibrium particle probability distribution function. In D2Q9 and D3Q19, it is shown below for an incompressible flow in continuous and discrete form where *D*, *R*, and *T* are the dimension, universal gas constant, and absolute temperature respectively. The partial derivation for the continuous to discrete form is provided through a simple derivation to second order accuracy.

$f^{\text{eq}}={\frac {\rho }{(2\pi RT)^{D/2}}}e^{-{\frac {({\vec {e}}-{\vec {u}})^{2}}{2RT}}}$

$={\frac {\rho }{(2\pi RT)^{D/2}}}e^{-{\frac {({\vec {e}})^{2}}{2RT}}}e^{{\frac {{\vec {e}}{\vec {u}}}{RT}}-{\frac {{\vec {u}}^{2}}{2RT}}}$

$={\frac {\rho }{(2\pi RT)^{D/2}}}e^{-{\frac {({\vec {e}})^{2}}{2RT}}}\left(1+{\frac {{\vec {e}}{\vec {u}}}{RT}}+{\frac {({\vec {e}}{\vec {u}})^{2}}{2(RT)^{2}}}-{\frac {{\vec {u}}^{2}}{2RT}}+...\right)$

Letting $c={\sqrt {3RT}}$ yields the final result:

$f_{i}^{eq}=\omega _{i}\rho \left(1+{\frac {3{\vec {e}}_{i}{\vec {u}}}{c^{2}}}+{\frac {9({\vec {e}}_{i}{\vec {u}})^{2}}{2c^{4}}}-{\frac {3({\vec {u}})^{2}}{2c^{2}}}\right)$

$g^{eq}={\frac {\rho ({\vec {e}}-{\vec {u}})^{2}}{2(2\pi RT)^{D/2}}}e^{-{\frac {({\vec {e}}-{\vec {u}})^{2}}{2RT}}}$

$\omega _{i}={\begin{cases}4/9&i=0\\1/9&i=1,2,3,4\\1/36&i=5,6,7,8\\\end{cases}}$

$\omega _{i}={\begin{cases}1/3&i=0\\1/18&i=1,2,...,5,6\\1/36&i=7,8,...,17,18\\\end{cases}}$

As much work has already been done on a single-component flow, the following TLBM will be discussed. The multicomponent/multiphase TLBM is also more intriguing and useful than simply one component. To be in line with current research, define the set of all components of the system (i. e. walls of porous media, multiple fluids/gases, etc.) $\Psi$ with elements $\sigma _{j}$ .

$f_{i}^{\sigma }({\vec {x}}+{\vec {e}}_{i}\delta _{t},t+\delta _{t})-f_{i}^{\sigma }({\vec {x}},t)+F_{i}={\frac {1}{\tau _{f}^{\sigma }}}(f_{i}^{\sigma ,eq}(\rho ^{\sigma },v^{\sigma })-f_{i}^{\sigma })$

The relaxation parameter, $\tau _{f}^{\sigma _{j}}\,\!$ , is related to the kinematic viscosity, $\nu _{f}^{\sigma _{j}}\,\!$ , by the following relationship:

$\nu _{f}^{\sigma _{j}}=(\tau _{f}^{\sigma _{j}}-0.5)c_{s}^{2}\delta _{t}.$

The moments of the $f_{i}\,\!$ give the local conserved quantities. The density is given by

$\rho =\sum _{\sigma }\sum _{i}f_{i}\,\!$

$\rho \epsilon =\sum _{i}g_{i}\,\!$

$\rho ^{\sigma }=\sum _{i}f_{i}^{\sigma }\,\!$

and the weighted average velocity, ${\vec {u'}}\,\!$ , and the local momentum are given by

${\vec {u'}}=\left(\sum _{\sigma }{\frac {\rho ^{\sigma }{\vec {u^{\sigma }}}}{\tau _{f}^{\sigma }}}\right)/\left(\sum _{\sigma }{\frac {\rho ^{\sigma }}{\tau _{f}^{\sigma }}}\right)$

$\rho ^{\sigma }{\vec {u^{\sigma }}}=\sum _{i}f_{i}^{\sigma }{\vec {e}}_{i}.$

$v^{\sigma }={\vec {u'}}+{\frac {\tau _{f}^{\sigma }}{\rho ^{\sigma }}}{\vec {F}}^{\sigma }$

In the above equation for the equilibrium velocity $v^{\sigma }\,\!$ , the ${\vec {F}}^{\sigma }\,\!$ term is the interaction force between a component and the other components. It is still the subject of much discussion as it is typically a tuning parameter that determines how fluid-fluid, fluid-gas, etc. interact. Frank et al. list current models for this force term. The commonly used derivations are Gunstensen chromodynamic model, Swift's free energy-based approach for both liquid/vapor systems and binary fluids, He's intermolecular interaction-based model, the Inamuro approach, and the Lee and Lin approach.

The following is the general description for ${\vec {F}}^{\sigma }\,\!$ as given by several authors.

${\vec {F}}^{\sigma }=-\psi ^{\sigma }({\vec {x}})\sum _{\sigma _{j}}H^{\sigma \sigma _{j}}({\vec {x}},{\vec {x}}')\sum _{i}\psi ^{\sigma _{j}}({\vec {x}}+{\vec {e}}_{i}){\vec {e}}_{i}\,\!$

$\psi ({\vec {x}})\,\!$ is the effective mass and $H({\vec {x}},{\vec {x}}')\,\!$ is Green's function representing the interparticle interaction with ${\vec {x}}'\,\!$ as the neighboring site. Satisfying $H({\vec {x}},{\vec {x}}')=H({\vec {x}}',{\vec {x}})\,\!$ and where $H({\vec {x}},{\vec {x}}')>0\,\!$ represents repulsive forces. For D2Q9 and D3Q19, this leads to

$H^{\sigma \sigma _{j}}({\vec {x}},{\vec {x}}')={\begin{cases}h^{\sigma \sigma _{j}}&\left|{\vec {x}}-{\vec {x}}'\right|\leq c\\0&\left|{\vec {x}}-{\vec {x}}'\right|>c\\\end{cases}}$

$H^{\sigma \sigma _{j}}({\vec {x}},{\vec {x}}')={\begin{cases}h^{\sigma \sigma _{j}}&\left|{\vec {x}}-{\vec {x}}'\right|=c\\h^{\sigma \sigma _{j}}/2&\left|{\vec {x}}-{\vec {x}}'\right|={\sqrt {2c}}\\0&{\text{otherwise}}\\\end{cases}}$

The effective mass as proposed by Shan and Chen uses the following effective mass for a *single-component, multiphase system*. The equation of state is also given under the condition of a single component and multiphase.

$\psi ({\vec {x}})=\psi (\rho ^{\sigma })=\rho _{0}^{\sigma }\left[1-e^{(-\rho ^{\sigma }/\rho _{0}^{\sigma })}\right]\,\!$

$p=c_{s}^{2}\rho +c_{0}h[\psi ({\vec {x}})]^{2}\,\!$

So far, it appears that $\rho _{0}^{\sigma }\,\!$ and $h^{\sigma \sigma _{j}}\,\!$ are free constants to tune but once plugged into the system's equation of state(EOS), they must satisfy the thermodynamic relationships at the critical point such that $(\partial P/\partial {\rho })_{T}=(\partial ^{2}P/\partial {\rho ^{2}})_{T}=0\,\!$ and $p=p_{c}\,\!$ . For the EOS, $c_{0}\,\!$ is 3.0 for D2Q9 and D3Q19 while it equals 10.0 for D3Q15.

It was later shown by Yuan and Schaefer that the effective mass density needs to be changed to simulate multiphase flow more accurately. They compared the Shan and Chen (SC), Carnahan-Starling (C–S), van der Waals (vdW), Redlich–Kwong (R–K), Redlich–Kwong Soave (RKS), and Peng–Robinson (P–R) EOS. Their results revealed that the SC EOS was insufficient and that C–S, P–R, R–K, and RKS EOS are all more accurate in modeling multiphase flow of a single component.

For the popular isothermal Lattice Boltzmann methods these are the only conserved quantities. Thermal models also conserve energy and therefore have an additional conserved quantity:

$\rho \theta +\rho uu=\sum _{i}f_{i}{\vec {e}}_{i}{\vec {e}}_{i}.$

## Unstructured grids

Normally, the lattice Boltzmann methods is implemented on regular grids, However the use of unstructured grid can help with solving complex boundaries, unstructured grids are made of triangles or tetrahedra with variations.

Assuming $\Omega ^{j}$ is a volume made by all barycenters of tetrahedra, faces and edges connected to vertex ${\boldsymbol {v}}^{j}$ , the discrete velocity density function:

$f_{i}({\boldsymbol {v}}^{j},t+\delta t)=f_{i}({\boldsymbol {v}}^{j},t)-\delta t\sum _{k}S_{i}^{jk}f_{i}({\boldsymbol {v}}^{k},t)-{\delta t \over \tau }\sum _{k}C^{jk}(f_{i}({\boldsymbol {v}}^{k},t)-f_{i}^{eq}({\boldsymbol {v}}^{k}))$

where ${\boldsymbol {v}}^{k}$ are position of a vertex and its neighbors, and:

$C^{jk}={1 \over V^{j}}\int _{\Omega ^{j}}w_{k}({\boldsymbol {x}})d\Omega$

$S_{i}^{jk}={1 \over V^{j}}\oint _{\partial \Omega ^{j}}({\vec {e_{i}}}{\vec {n}})w_{k}({\boldsymbol {x}})d\Omega$

where $w_{k}({\boldsymbol {x}})$ is wights of a linear interpolation of ${\boldsymbol {x}}$ by vertices of triangle or tetrahedra that ${\boldsymbol {x}}$ lies within.

## Applications

During the last years, the LBM has proven to be a powerful tool for solving problems at different length and time scales. Some of the applications of LBM include:

- Porous Media flows
- Biomedical Flows
- Earth sciences (Soil filtration).
- Energy Sciences (Fuel Cells).

## Example implementation

This is a barebone implementation of LBM on a 100x100 grid, Using Python:

```mw
# This is a fluid simulator using the lattice Boltzmann method.
# Using D2Q9 and periodic boundary, and used no external library.
# It generates two ripples at 50,50 and 50,40.
# Reference: Erlend Magnus Viggen's Master thesis, "The Lattice Boltzmann Method with Applications in Acoustics".
# For Wikipedia under CC-BY-SA license.
import math

# Define some utilities
def sum(a):
    s = 0
    for e in a:
        s = s + e
    return s

# Weights in D2Q9
Weights = [1 / 36, 1 / 9, 1 / 36, 1 / 9, 4 / 9, 1 / 9, 1 / 36, 1 / 9, 1 / 36]
# Discrete velocity vectors
DiscreteVelocityVectors = [
    [-1, 1],
    [0, 1],
    [1, 1],
    [-1, 0],
    [0, 0],
    [1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
]

# A Field2D class
class Field2D:
    def __init__(self, res: int):
        self.field = []
        for b in range(res):
            fm = []
            for a in range(res):
                fm.append([0, 0, 0, 0, 1, 0, 0, 0, 0])
            self.field.append(fm[:])
        self.res = res

    # This visualize the simulation, can only be used in a terminal
    @staticmethod
    def VisualizeField(a, sc, res):
        stringr = ""
        for u in range(res):
            row = ""
            for v in range(res):
                n = int(u * a.res / res)
                x = int(v * a.res / res)
                vx = velocityField[n][x][0]
                vy = velocityField[n][x][1]
                r = max(0, min(255, int(127 + sc * vx)))
                g = max(0, min(255, int(127 + sc * vy)))
                col = "\033[38;2;{0};{1};{2}m██".format(r, g, 0)
                row = row + col
            print(row)
            stringr = stringr + row + "\n"
        return stringr

    # Momentum of the field
    def Momentum(self, x, y):
        return velocityField[y][x][0] * sum(self.field[y][x]), velocityField[y][x][
            1
        ] * sum(self.field[y][x])

# Resolution of the simulation
res = 100
a = Field2D(res)
# The velocity field
velocityField = []
for DummyVariable in range(res):
    DummyList = []
    for DummyVariable2 in range(res):
        DummyList.append([0, 0])
    velocityField.append(DummyList[:])
# The density field
DensityField = []
for DummyVariable in range(res):
    DummyList = []
    for DummyVariable2 in range(res):
        DummyList.append(1)
    DensityField.append(DummyList[:])
# Set initial condition
DensityField[50][50] = 2
DensityField[40][50] = 2
# Maximum solving steps
MaxSteps = 120
# The speed of sound, specifically 1/sqrt(3) ~ 0.57
SpeedOfSound = 1 / math.sqrt(3)
# time relaxation constant
TimeRelaxationConstant = 0.5
# Solve
for s in range(MaxSteps):
    # Collision Step
    df = Field2D(res)
    for y in range(res):
        for x in range(res):
            for v in range(9):
                Velocity = a.field[y][x][v]
                FirstTerm = Velocity
                # The Flow Velocity
                FlowVelocity = velocityField[y][x]
                Dotted = (
                    FlowVelocity[0] * DiscreteVelocityVectors[v][0]
                    + FlowVelocity[1] * DiscreteVelocityVectors[v][1]
                )
                # #The taylor expainsion of equilibrium term
                taylor = (
                    1
                    + ((Dotted) / (SpeedOfSound**2))
                    + ((Dotted**2) / (2 * SpeedOfSound**4))
                    - (
                        (FlowVelocity[0] ** 2 + FlowVelocity[1] ** 2)
                        / (2 * SpeedOfSound**2)
                    )
                )
                # The current density
                density = DensityField[y][x]
                # The equilibrium
                equilibrium = density * taylor * Weights[v]
                SecondTerm = (equilibrium - Velocity) / TimeRelaxationConstant
                df.field[y][x][v] = FirstTerm + SecondTerm
    # Streaming Step
    for y in range(0, res):
        for x in range(0, res):
            for v in range(9):
                # Target, the lattice point this iteration is solving
                TargetY = y + DiscreteVelocityVectors[v][1]
                TargetX = x + DiscreteVelocityVectors[v][0]
                # Peiodic Boundary
                if TargetY == res and TargetX == res:
                    a.field[TargetY - res][TargetX - res][v] = df.field[y][x][v]
                elif TargetX == res:
                    a.field[TargetY][TargetX - res][v] = df.field[y][x][v]
                elif TargetY == res:
                    a.field[TargetY - res][TargetX][v] = df.field[y][x][v]
                elif TargetY == -1 and TargetX == -1:
                    a.field[TargetY + res][TargetX + res][v] = df.field[y][x][v]
                elif TargetX == -1:
                    a.field[TargetY][TargetX + res][v] = df.field[y][x][v]
                elif TargetY == -1:
                    a.field[TargetY + res][TargetX][v] = df.field[y][x][v]
                else:
                    a.field[TargetY][TargetX][v] = df.field[y][x][v]
    # Calculate macroscopic variables
    for y in range(res):
        for x in range(res):
            # Recompute Density Field
            DensityField[y][x] = sum(a.field[y][x])
            # Recompute Flow Velocity
            FlowVelocity = [0, 0]
            for DummyVariable in range(9):
                FlowVelocity[0] = (
                    FlowVelocity[0]
                    + DiscreteVelocityVectors[DummyVariable][0]
                    * a.field[y][x][DummyVariable]
                )
            for DummyVariable in range(9):
                FlowVelocity[1] = (
                    FlowVelocity[1]
                    + DiscreteVelocityVectors[DummyVariable][1]
                    * a.field[y][x][DummyVariable]
                )
            FlowVelocity[0] = FlowVelocity[0] / DensityField[y][x]
            FlowVelocity[1] = FlowVelocity[1] / DensityField[y][x]
            # Insert to Velocity Field
            velocityField[y][x] = FlowVelocity
    # Visualize
    Field2D.VisualizeField(a, 5000, 100)
```

---
title: "Knudsen number"
source: https://en.wikipedia.org/wiki/Knudsen_number
domain: lattice-boltzmann
license: CC-BY-SA-4.0
tags: lattice boltzmann method, boltzmann equation, kinetic theory of gases, lattice gas automaton
fetched: 2026-07-02
---

# Knudsen number

The **Knudsen number** (**Kn**) is a dimensionless number defined as the ratio of the molecular mean free path length to a representative physical length scale. This length scale could be, for example, the radius of a body in a fluid. The number is named after Danish physicist Martin Knudsen (1871–1949).

The Knudsen number helps determine whether statistical mechanics or the continuum mechanics formulation of fluid dynamics should be used to model a situation. If the Knudsen number is near or greater than one, the mean free path of a molecule is comparable to a length scale of the problem, and the continuum assumption of fluid mechanics is no longer a good approximation. In such cases, statistical methods should be used.

## Definition

The Knudsen number is a dimensionless number defined as:

$\mathrm {Kn} \ ={\frac {\lambda }{L}},$

where:

- $\lambda$ = mean free path [L1],
- L = representative physical length scale [L1].

The representative length scale considered, L , may correspond to various physical traits of a system, but most commonly relates to a *gap length* over which thermal transport or mass transport occurs through a gas phase. This is the case in porous and granular materials, where the thermal transport through a gas phase depends highly on its pressure and the consequent mean free path of molecules in this phase. For a Boltzmann gas, the mean free path may be readily calculated, so that:

$\mathrm {Kn} \ ={\frac {k_{\text{B}}T}{{\sqrt {2}}\pi d^{2}pL}}={\frac {k_{\text{B}}}{{\sqrt {2}}\pi d^{2}\rho R_{s}L}},$

where:

- $k_{\text{B}}$ is the Boltzmann constant (1.380649×10−23 J/K in SI units) [M1 L2 T−2 Θ−1],
- T is the thermodynamic temperature [Θ1],
- d is the particle hard-shell diameter [L1],
- p is the static pressure [M1 L−1 T−2],
- $R_{s}$ is the specific gas constant [L2 T−2 Θ−1] (287.05 J/(kg K) for air),
- $\rho$ is the density [M1 L−3].

If the temperature is increased, but the *volume* kept constant, then the Knudsen number (and the mean free path) doesn't change (for an ideal gas). In this case, the density stays the same. If the temperature is increased, and the *pressure* kept constant, then the gas expands and therefore its density decreases. In this case, the mean free path increases and so does the Knudsen number. Hence, it may be helpful to keep in mind that the mean free path (and therefore the Knudsen number) is really dependent on the thermodynamic variable density (proportional to the reciprocal of density), and only indirectly on temperature and pressure.

For particle dynamics in the atmosphere, and assuming standard temperature and pressure, i.e. 0 °C and 1 atm, we have $\lambda$ ≈ 8×10−8 m (80 nm).

## Relationship to Mach and Reynolds numbers in gases

The Knudsen number can be related to the Mach number and the Reynolds number.

Using the dynamic viscosity: $\mu ={\frac {1}{2}}\rho {\bar {c}}\lambda ,$

with the average molecule speed (from Maxwell–Boltzmann distribution): ${\bar {c}}={\sqrt {\frac {8k_{\text{B}}T}{\pi m}}},$

the mean free path is determined as follows: $\lambda ={\frac {\mu }{\rho }}{\sqrt {\frac {\pi m}{2k_{\text{B}}T}}}.$

Dividing through by *L* (some characteristic length), the Knudsen number is obtained: $\mathrm {Kn} \ ={\frac {\lambda }{L}}={\frac {\mu }{\rho L}}{\sqrt {\frac {\pi m}{2k_{\text{B}}T}}},$

where:

- ${\bar {c}}$ is the average molecular speed from the Maxwell–Boltzmann distribution [L1 T−1],
- *T* is the thermodynamic temperature [Θ1],
- *μ* is the dynamic viscosity [M1 L−1 T−1],
- *m* is the molecular mass [M1],
- *k*B is the Boltzmann constant [M1 L2 T−2 Θ−1],
- $\rho$ is the density [M1 L−3].

The dimensionless Mach number can be written as: $\mathrm {Ma} ={\frac {U_{\infty }}{c_{\text{s}}}},$

where the speed of sound is given by: $c_{\text{s}}={\sqrt {\frac {\gamma RT}{M}}}={\sqrt {\frac {\gamma k_{\text{B}}T}{m}}},$

where:

- *U∞* is the freestream speed [L1 T−1],
- *R* is the Universal gas constant (in SI, 8.31447215 J K−1 mol−1) [M1 L2 T−2 Θ−1 mol−1],
- *M* is the molar mass [M1 mol−1],
- $\gamma$ is the ratio of specific heats [1].

The dimensionless Reynolds number can be written as: $\mathrm {Re} ={\frac {\rho U_{\infty }L}{\mu }}.$

Dividing the Mach number by the Reynolds number:

${\frac {\mathrm {Ma} }{\mathrm {Re} }}={\frac {U_{\infty }/c_{\text{s}}}{\rho U_{\infty }L/\mu }}={\frac {\mu }{\rho Lc_{\text{s}}}}={\frac {\mu }{\rho L{\sqrt {\frac {\gamma k_{\text{B}}T}{m}}}}}={\frac {\mu }{\rho L}}{\sqrt {\frac {m}{\gamma k_{\text{B}}T}}}$

and by multiplying by ${\sqrt {\frac {\gamma \pi }{2}}}$ yields the Knudsen number:

${\frac {\mu }{\rho L}}{\sqrt {\frac {m}{\gamma k_{\text{B}}T}}}{\sqrt {\frac {\gamma \pi }{2}}}={\frac {\mu }{\rho L}}{\sqrt {\frac {\pi m}{2k_{\text{B}}T}}}=\mathrm {Kn} .$

The Mach, Reynolds and Knudsen numbers are therefore related by:

$\mathrm {Kn} \ ={\frac {\mathrm {Ma} }{\mathrm {Re} }}{\sqrt {\frac {\gamma \pi }{2}}}.$

## Application

The Knudsen number can be used to determine the rarefaction of a flow:

- $\mathrm {Kn} <0.01$ : Continuum flow
- $0.01<\mathrm {Kn} <0.1$ : Slip flow
- $0.1<\mathrm {Kn} <10$ : Transitional flow
- $\mathrm {Kn} >10$ : Free molecular flow

This regime classification is empirical and problem dependent but has proven useful to adequately model flows.

Problems with high Knudsen numbers include the calculation of the motion of a dust particle through the lower atmosphere and the motion of a satellite through the exosphere. One of the most widely used applications for the Knudsen number is in microfluidics and MEMS device design where flows range from continuum to free-molecular. In recent years, it has been applied in other disciplines such as transport in porous media, e.g., petroleum reservoirs. Movements of fluids in situations with a high Knudsen number are said to exhibit Knudsen flow, also called free molecular flow.

Airflow around an aircraft such as an airliner has a low Knudsen number, making it firmly in the realm of continuum mechanics. Using the Knudsen number an adjustment for Stokes' law can be used in the Cunningham correction factor, this is a drag force correction due to slip in small particles (i.e. *d**p* < 5 μm). The flow of water through a nozzle will usually be a situation with a low Knudsen number.

Mixtures of gases with different molecular masses can be partly separated by sending the mixture through small holes of a thin wall because the numbers of molecules that pass through a hole is proportional to the pressure of the gas and inversely proportional to its molecular mass. The technique has been used to separate isotopic mixtures, such as uranium, using porous membranes. It has also been successfully demonstrated for use in hydrogen production from water.

The Knudsen number also plays an important role in thermal conduction in gases. For insulation materials, for example, where gases are contained under low pressure, the Knudsen number should be as high as possible to ensure low thermal conductivity.

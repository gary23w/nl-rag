---
title: "Free-energy perturbation"
source: https://en.wikipedia.org/wiki/Free_energy_perturbation
domain: pharmacophore-modeling
license: CC-BY-SA-4.0
tags: pharmacophore feature, 3d model, hydrogen bond donor, steric
fetched: 2026-07-02
---

# Free-energy perturbation

(Redirected from

Free energy perturbation

)

**Free-energy perturbation** (**FEP**) is an alchemical method based on statistical mechanics that is used in computational chemistry for computing free-energy differences from molecular dynamics or Metropolis Monte Carlo simulations. It is widely used to compute the free energy difference between two states, state **A** and state **B.**

The FEP method was introduced by Robert W. Zwanzig in 1954. According to the free-energy perturbation method, the free-energy difference for going from state **A** to state **B** is obtained from the following equation, known as the *Zwanzig equation*:

$\Delta F(\mathbf {A} \to \mathbf {B} )=F_{\mathbf {B} }-F_{\mathbf {A} }=-k_{\text{B}}T\ln \left\langle \exp \left(-{\frac {E_{\mathbf {B} }-E_{\mathbf {A} }}{k_{\text{B}}T}}\right)\right\rangle _{\mathbf {A} },$

where *T* is the temperature, *k*B is the Boltzmann constant, and the angular brackets denote an average over a simulation run for state **A**. In practice, one runs a normal simulation for state **A**, but each time a new configuration is accepted, the energy for state **B** is also computed. The difference between states **A** and **B** may be in the atom types involved, in which case the Δ*F* obtained is for "mutating" one molecule onto another, or it may be a difference of geometry, in which case one obtains a free-energy map along one or more reaction coordinates. This free-energy map is also known as a *potential of mean force* (PMF).

Free-energy perturbation calculations only converge properly when the difference between the two states is small enough (the phase space of the two states overlap). In practice, the perturbation is divided into a series of smaller, discrete intermediate FEP windows defined by the coupling parameter $\lambda$ . A value of $\lambda$ = 0 represent 100% state **A,** and $\lambda$ = 1 represent 100% state **B**. In any particular window, we have the effective potential energy function $U_{m}=(1-\lambda _{m})U_{A}+\lambda _{m}U_{B}$ , which is the linear combination of the initial potential **A** and final **B.** Stepwise varying $\lambda$ from 0 to 1 creates an "alchemical" pathway of transformation between state **A** and **B** through non-physical intermediate states.

Since there is no need for constant communication between the simulation for one window and the next, the process can be trivially parallelized by running each window on a different CPU, in what is known as an "embarrassingly parallel" setup.

## Application

FEP calculations have been used for studying host–guest binding energetics, pKa predictions, solvent effects on reactions, and enzymatic reactions. Other applications are the virtual screening of ligands in drug discovery, *in silico* mutagenesis studies and antibody affinity maturation. For the study of reactions it is often necessary to involve a quantum-mechanical (QM) representation of the reaction center because the molecular mechanics (MM) force fields used for FEP simulations cannot handle breaking bonds. A hybrid method that has the advantages of both QM and MM calculations is called QM/MM.

Umbrella sampling is another free-energy calculation technique that is typically used for calculating the free-energy change associated with a change in "position" coordinates as opposed to "chemical" coordinates, although umbrella sampling can also be used for a chemical transformation when the "chemical" coordinate is treated as a dynamic variable (as in the case of the Lambda dynamics approach of Kong and Brooks). An alternative to free-energy perturbation for computing potentials of mean force in chemical space is thermodynamic integration. Another alternative, which is probably more efficient, is the Bennett acceptance ratio method. Adaptations to FEP exist which attempt to apportion free-energy changes to subsections of the chemical structure.

## Thermodynamic Cycle

Since free energy is a state function, the total free energy change between two states are independent of the path taken. Using FEP calculations and closed thermodynamic cycles, it is possible to calculate the relative change in free energy, for example comparing two ligands A and B binding to a target substrate. From this we can calculate the change in binding free energy as

$\Delta \Delta A_{bind}=\Delta A_{bind}^{B}-\Delta A_{bind}^{A}=\Delta A_{A\rightarrow B}^{bound}-\Delta A_{A\rightarrow B}^{unbound}$

## Software

FEP methods have been implemented in several molecular dynamics software packages. Below is a short list of some of the most common programs:

- Flare FEP
- FEP+
- AMBER
- BOSS
- CHARMM
- Desmond
- GROMACS
- OpenMM
- MacroModel
- MOLARIS
- NAMD
- Tinker
- Q
- QUELO

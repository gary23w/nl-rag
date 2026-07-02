---
title: "Complete active space"
source: https://en.wikipedia.org/wiki/Complete_active_space
domain: ab-initio-methods
license: CC-BY-SA-4.0
tags: ab initio quantum chemistry, complete active space, multi-configurational scf, variational method chemistry
fetched: 2026-07-02
---

# Complete active space

In quantum chemistry, a **complete active space** is a type of classification of molecular orbitals. Spatial orbitals are classified as belonging to three classes:

- *core*, always hold two electrons
- *active*, partially occupied orbitals
- *virtual*, always hold zero electrons

This classification allows one to develop a set of Slater determinants for the description of the wavefunction as a linear combination of these determinants. Based on the freedom left for the occupation in the active orbitals, a certain number of electrons are allowed to populate all the active orbitals in appropriate combinations, developing a finite-size space of determinants. The resulting wavefunction is of multireference nature, and is blessed by additional properties if compared to other selection schemes.

The active classification can theoretically be extended to all the molecular orbitals, to obtain a full CI treatment. In practice, this choice is limited, due to the high computational cost needed to optimize a large CAS wavefunction on medium and large molecular systems.

A Complete Active Space wavefunction is used to obtain a first approximation of the so-called static correlation, which represents the contribution needed to describe bond dissociation processes correctly. This requires a wavefunction that includes a set of electronic configurations with high and very similar importance. Dynamic correlation, representing the contribution to the energy brought by the instantaneous interaction between electrons, is normally small and can be recovered with good accuracy by means of perturbative evaluations, such as CASPT2 and NEVPT.

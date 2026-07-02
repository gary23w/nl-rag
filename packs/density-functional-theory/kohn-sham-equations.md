---
title: "Kohn–Sham equations"
source: https://en.wikipedia.org/wiki/Kohn%E2%80%93Sham_equations
domain: density-functional-theory
license: CC-BY-SA-4.0
tags: density functional theory, kohn-sham equations, hohenberg-kohn theorems, pseudopotential
fetched: 2026-07-02
---

# Kohn–Sham equations

The **Kohn-Sham equations** are a set of mathematical equations used in quantum mechanics to simplify the complex problem of understanding how electrons behave in atoms and molecules. They introduce fictitious non-interacting electrons and use them to find the most stable arrangement of electrons, which helps scientists understand and predict the properties of matter at the atomic and molecular scale.

## Description

In physics and quantum chemistry, specifically density functional theory, the **Kohn–Sham equation** is the non-interacting Schrödinger equation (more clearly, Schrödinger-like equation) of a fictitious system (the "**Kohn–Sham system**") of non-interacting particles (typically electrons) that generate the same density as any given system of interacting particles.

In the Kohn–Sham theory the introduction of the noninteracting kinetic energy functional Ts into the energy expression leads, upon functional differentiation, to a collection of one-particle equations whose solutions are the Kohn–Sham orbitals.

The Kohn–Sham equation is defined by a local effective (fictitious) external potential in which the non-interacting particles move, typically denoted as *vs*(**r**) or *v*eff(**r**), called the **Kohn–Sham potential**. If the particles in the Kohn–Sham system are non-interacting fermions (non-fermion density functional theory has been studied), the Kohn–Sham wavefunction is a single Slater determinant constructed from a set of orbitals that are the lowest-energy solutions to $\left(-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+v_{\text{eff}}(\mathbf {r} )\right)\varphi _{i}(\mathbf {r} )=\varepsilon _{i}\varphi _{i}(\mathbf {r} ).$

This eigenvalue equation is the typical representation of the **Kohn–Sham equations**. Here *εi* is the orbital energy of the corresponding Kohn–Sham orbital $\varphi _{i}$ , and the density for an *N*-particle system is

$\rho (\mathbf {r} )=\sum _{i}^{N}|\varphi _{i}(\mathbf {r} )|^{2}.$

## History

The Kohn–Sham equations are named after Walter Kohn and Lu Jeu Sham, who introduced the concept at the University of California, San Diego, in 1965.

Kohn received a Nobel Prize in Chemistry in 1998 for the Kohn–Sham equations and other work related to density functional theory (DFT).

## Kohn–Sham potential

In Kohn–Sham density functional theory, the total energy of a system is expressed as a functional of the charge density as

$E[\rho ]=T_{s}[\rho ]+\int d\mathbf {r} \,v_{\text{ext}}(\mathbf {r} )\rho (\mathbf {r} )+E_{\text{H}}[\rho ]+E_{\text{xc}}[\rho ],$

where *Ts* is the **Kohn–Sham kinetic energy**, which is expressed in terms of the Kohn–Sham orbitals as

$T_{s}[\rho ]=\sum _{i=1}^{N}\int d\mathbf {r} \,\varphi _{i}^{*}(\mathbf {r} )\left(-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\right)\varphi _{i}(\mathbf {r} ),$

*v*ext is the external potential acting on the interacting system (at minimum, for a molecular system, the electron–nuclei interaction), *EH* is the Hartree (or Coulomb) energy

$E_{\text{H}}[\rho ]={\frac {e^{2}}{2}}\int d\mathbf {r} \int d\mathbf {r} '\,{\frac {\rho (\mathbf {r} )\rho (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}},$

and *E*xc is the exchange–correlation energy. The Kohn–Sham equations are found by varying the total energy expression with respect to a set of *Kohn-Sham orbitals* subject to the constraint that they are orthogonal, this yields a time-independent Schrödinger equation with a scalar potential equal to the Kohn–Sham potential

$v_{\text{eff}}(\mathbf {r} )=v_{\text{ext}}(\mathbf {r} )+e^{2}\int {\frac {\rho (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\,d\mathbf {r} '+{\frac {\delta E_{\text{xc}}[\rho ]}{\delta \rho (\mathbf {r} )}},$

where the last term

$v_{\text{xc}}(\mathbf {r} )\equiv {\frac {\delta E_{\text{xc}}[\rho ]}{\delta \rho (\mathbf {r} )}},$

is the exchange–correlation potential. This term, and the corresponding energy expression, are the only unknowns in the Kohn–Sham approach to density functional theory. An approximation that does not vary the orbitals is Harris functional theory.

The Kohn–Sham orbital energies *εi*, in general, have little physical meaning (see Koopmans' theorem). The sum of the orbital energies is related to the total energy as

$E=\sum _{i}^{N}\varepsilon _{i}-E_{\text{H}}[\rho ]+E_{\text{xc}}[\rho ]-\int {\frac {\delta E_{\text{xc}}[\rho ]}{\delta \rho (\mathbf {r} )}}\rho (\mathbf {r} )\,d\mathbf {r} .$

Because the orbital energies are non-unique in the more general restricted open-shell case, this equation only holds true for specific choices of orbital energies (see Koopmans' theorem).

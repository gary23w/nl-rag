---
title: "Linear combination of atomic orbitals"
source: https://en.wikipedia.org/wiki/Linear_combination_of_atomic_orbitals
domain: molecular-orbital-theory
license: CC-BY-SA-4.0
tags: molecular orbital theory, atomic orbitals, bond order, frontier orbitals
fetched: 2026-07-02
---

# Linear combination of atomic orbitals

A **linear combination of atomic orbitals** (**LCAO**) is a quantum superposition of atomic orbitals and a technique for calculating molecular orbitals in quantum chemistry. In quantum mechanics, electron configurations of atoms are described as wavefunctions. In a mathematical sense, these wave functions are the basis set of functions, the basis functions, which describe the electrons of a given atom. In chemical reactions, orbital wavefunctions are modified, i.e. the electron cloud shape is changed, according to the type of atoms participating in the chemical bond.

It was introduced in 1929 by Sir John Lennard-Jones with the description of bonding in the diatomic molecules of the first main row of the periodic table, but had been used earlier by Linus Pauling for H2+.

## Mathematical description

An initial assumption is that the number of molecular orbitals is equal to the number of atomic orbitals included in the linear expansion. In a sense, *n* atomic orbitals combine to form *n* molecular orbitals, which can be numbered *i* = 1 to *n* and which may not all be the same. The expression (linear expansion) for the *i* th molecular orbital would be:

$\ \phi _{i}=c_{1i}\chi _{1}+c_{2i}\chi _{2}+c_{3i}\chi _{3}+\cdots +c_{ni}\chi _{n}$

or

$\ \phi _{i}=\sum _{r}c_{ri}\chi _{r}$

where $\ \phi _{i}$ is a molecular orbital represented as the sum of *n* atomic orbitals $\ \chi _{r}$ , each multiplied by a corresponding coefficient $\ c_{ri}$ , and *r* (numbered 1 to *n*) represents which atomic orbital is combined in the term. The coefficients are the weights of the contributions of the n atomic orbitals to the molecular orbital. The Hartree–Fock method is used to obtain the coefficients of the expansion. The orbitals are thus expressed as linear combinations of basis functions, and the basis functions are single-electron functions which may or may not be centered on the nuclei of the component atoms of the molecule. In either case the basis functions are usually also referred to as atomic orbitals (even though only in the former case this name seems to be adequate). The atomic orbitals used are typically those of hydrogen-like atoms since these are known analytically i.e. Slater-type orbitals but other choices are possible such as the Gaussian functions from standard basis sets or the pseudo-atomic orbitals from plane-wave pseudopotentials.

By minimizing the total energy of the system, an appropriate set of coefficients of the linear combinations is determined. This quantitative approach is now known as the Hartree–Fock method. However, since the development of computational chemistry, the LCAO method often refers not to an actual optimization of the wave function but to a qualitative discussion which is very useful for predicting and rationalizing results obtained via more modern methods. In this case, the shape of the molecular orbitals and their respective energies are deduced approximately from comparing the energies of the atomic orbitals of the individual atoms (or molecular fragments) and applying some recipes known as level repulsion and the like. The graphs that are plotted to make this discussion clearer are called correlation diagrams. The required atomic orbital energies can come from calculations or directly from experiment via Koopmans' theorem.

This is done by using the symmetry of the molecules and orbitals involved in bonding, and thus is sometimes called *symmetry adapted linear combination* (SALC). The first step in this process is assigning a point group to the molecule. Each operation in the point group is performed upon the molecule. The number of bonds that are unmoved is the character of that operation. This reducible representation is decomposed into the sum of irreducible representations. These irreducible representations correspond to the symmetry of the orbitals involved.

Molecular orbital diagrams provide simple qualitative LCAO treatment. The Hückel method, the extended Hückel method and the Pariser–Parr–Pople method, provide some quantitative theories.

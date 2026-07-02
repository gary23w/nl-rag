---
title: "Roothaan equations"
source: https://en.wikipedia.org/wiki/Roothaan_equations
domain: hartree-fock
license: CC-BY-SA-4.0
tags: hartree-fock method, self-consistent field, slater determinant, roothaan equations
fetched: 2026-07-02
---

# Roothaan equations

The **Roothaan equations** are a representation of the Hartree–Fock equation in a non orthonormal basis set which can be of Gaussian-type or Slater-type. It applies to closed-shell molecules or atoms where all molecular orbitals or atomic orbitals, respectively, are doubly occupied. This is generally called restricted Hartree–Fock theory.

The method was developed independently by Clemens C. J. Roothaan and George G. Hall in 1951, and is thus sometimes called the *Roothaan-Hall equations*. The Roothaan equations can be written in a form resembling generalized eigenvalue problem, although they are not a standard eigenvalue problem because they are nonlinear:

$\mathbf {F} \mathbf {C} =\mathbf {S} \mathbf {C} \mathbf {\epsilon }$

where F is the Fock matrix (which depends on the coefficients C due to electron-electron interactions), C is a matrix of coefficients, S is the overlap matrix of the basis functions, and $\epsilon$ is the (diagonal, by convention) matrix of orbital energies. In the case of an orthonormalised basis set the overlap matrix, S, reduces to the identity matrix. These equations are essentially a special case of a Galerkin method applied to the Hartree–Fock equation using a particular basis set.

In contrast to the Hartree–Fock equations - which are integro-differential equations - the Roothaan–Hall equations have a matrix-form. Therefore, they can be solved using standard techniques.

---
title: "Roe solver"
source: https://en.wikipedia.org/wiki/Roe_solver
domain: finite-volume-method
license: CC-BY-SA-4.0
tags: finite volume method, godunov scheme, riemann solver, flux limiter
fetched: 2026-07-02
---

# Roe solver

The **Roe approximate Riemann solver**, devised by Phil Roe, is an approximate Riemann solver based on the Godunov scheme and involves finding an estimate for the intercell numerical flux or Godunov flux $F_{i+{\frac {1}{2}}}$ at the interface between two computational cells $U_{i}$ and $U_{i+1}$ , on some discretised space-time computational domain.

## Roe scheme

### Quasi-linear hyperbolic system

A non-linear system of hyperbolic partial differential equations representing a set of conservation laws in one spatial dimension can be written in the form

${\frac {\partial {\boldsymbol {U}}}{\partial t}}+{\frac {\partial {\boldsymbol {F}}({\boldsymbol {U}})}{\partial x}}=0.$

Applying the chain rule to the second term we get the quasi-linear hyperbolic system

${\frac {\partial {\boldsymbol {U}}}{\partial t}}+A({\boldsymbol {U}}){\frac {\partial {\boldsymbol {U}}}{\partial x}}=0,$

where A is the Jacobian matrix of the flux vector ${\boldsymbol {F}}({\boldsymbol {U}})$ .

### Roe matrix

The Roe method consists of finding a matrix ${\tilde {A}}({\boldsymbol {U}}_{i},{\boldsymbol {U}}_{i+1})$ that is assumed constant between two cells. The Riemann problem can then be solved as a truly linear hyperbolic system at each cell interface. The Roe matrix must obey the following conditions:

- Diagonalizable with real eigenvalues: ensures that the new linear system is truly hyperbolic.
- Consistency with the exact jacobian: when ${\boldsymbol {U}}_{i},{\boldsymbol {U}}_{i+1}\rightarrow {\boldsymbol {U}}$ we demand that ${\tilde {A}}({\boldsymbol {U}}_{i},{\boldsymbol {U}}_{i+1})=A({\boldsymbol {U}})$
- Conserving: ${\boldsymbol {F}}_{i+1}-{\boldsymbol {F}}_{i}={\tilde {A}}({\boldsymbol {U}}_{i+1}-{\boldsymbol {U}}_{i})$

Phil Roe introduced a method of parameter vectors to find such a matrix for some systems of conservation laws.

### Intercell flux

Once the Roe matrix corresponding to the interface between two cells is found, the intercell flux is given by solving the quasi-linear system as a truly linear system.

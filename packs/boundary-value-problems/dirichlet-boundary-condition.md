---
title: "Dirichlet boundary condition"
source: https://en.wikipedia.org/wiki/Dirichlet_boundary_condition
domain: boundary-value-problems
license: CC-BY-SA-4.0
tags: boundary value problem, dirichlet boundary condition, neumann boundary condition, shooting method
fetched: 2026-07-02
---

# Dirichlet boundary condition

In mathematics, the **Dirichlet** **boundary condition** is imposed on an ordinary or partial differential equation, such that the values that the solution takes along the boundary of the domain are fixed. The question of finding solutions to such equations is known as the Dirichlet problem. In the sciences and engineering, a Dirichlet boundary condition may also be referred to as a **fixed boundary condition** or **boundary condition of the first type**. It is named after Peter Gustav Lejeune Dirichlet (1805–1859).

In finite-element analysis, the *essential* or Dirichlet boundary condition is defined by weighted-integral form of a differential equation. The dependent unknown *u in the same form as the weight function w* appearing in the boundary expression is termed a *primary variable*, and its specification constitutes the *essential* or Dirichlet boundary condition.

## Examples

### ODE

For an ordinary differential equation, for instance, $y''+y=0,$ the Dirichlet boundary conditions on the interval [*a*,*b*] take the form $y(a)=\alpha ,\quad y(b)=\beta ,$ where α and β are given numbers.

### PDE

For a partial differential equation, for example, $\nabla ^{2}y+y=0,$ where $\nabla ^{2}$ denotes the Laplace operator, the Dirichlet boundary conditions on a domain Ω ⊂ **R***n* take the form $y(x)=f(x)\quad \forall x\in \partial \Omega ,$ where f is a known function defined on the boundary ∂Ω.

### Applications

For example, the following would be considered Dirichlet boundary conditions:

- In mechanical engineering and civil engineering (beam theory), where one end of a beam is held at a fixed position in space.
- In heat transfer, where a surface is held at a fixed temperature.
- In electrostatics, where a node of a circuit is held at a fixed voltage.
- In fluid dynamics, the no-slip condition for viscous fluids states that at a solid boundary, the fluid will have zero velocity relative to the boundary.

## Other boundary conditions

Many other boundary conditions are possible, including the Cauchy boundary condition and the mixed boundary condition. The latter is a combination of the Dirichlet and Neumann conditions.

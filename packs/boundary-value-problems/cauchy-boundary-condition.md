---
title: "Cauchy boundary condition"
source: https://en.wikipedia.org/wiki/Cauchy_boundary_condition
domain: boundary-value-problems
license: CC-BY-SA-4.0
tags: boundary value problem, dirichlet boundary condition, neumann boundary condition, shooting method
fetched: 2026-07-02
---

# Cauchy boundary condition

In mathematics, a **Cauchy** (French: [koʃi]) **boundary condition** augments an ordinary differential equation or a partial differential equation with conditions that the solution must satisfy on the boundary; ideally so as to ensure that a unique solution exists. A Cauchy boundary condition specifies both the function value and normal derivative on the boundary of the domain. This corresponds to imposing both a Dirichlet and a Neumann boundary condition. It is named after the prolific 19th-century French mathematical analyst Augustin-Louis Cauchy.

## Second-order ordinary differential equations

Cauchy boundary conditions are simple and common in second-order ordinary differential equations,

$y''(s)=f{\big (}y(s),y'(s),s{\big )},$

where, in order to ensure that a unique solution $y(s)$ exists, one may specify the value of the function y and the value of the derivative $y'$ at a given point $s=a$ , i.e.,

$y(a)=\alpha ,$

and

$y'(a)=\beta ,$

where a is a boundary or initial point. Since the parameter s is usually time, Cauchy conditions can also be called *initial value conditions* or *initial value data* or simply *Cauchy data*. An example of such a situation is Newton's laws of motion, where the acceleration $y''$ depends on position y , velocity $y'$ , and the time s ; here, Cauchy data corresponds to knowing the initial position and velocity.

## Partial differential equations

For partial differential equations, Cauchy boundary conditions specify both the function and the normal derivative on the boundary. To make things simple and concrete, consider a second-order differential equation in the plane

$A(x,y)\psi _{xx}+B(x,y)\psi _{xy}+C(x,y)\psi _{yy}=F(x,y,\psi ,\psi _{x},\psi _{y}),$

where $\psi (x,y)$ is the unknown solution, $\psi _{x}$ denotes derivative of $\psi$ with respect to x etc. The functions $A,B,C,F$ specify the problem.

We now seek a $\psi$ that satisfies the partial differential equation in a domain $\Omega$ , which is a subset of the $xy$ plane, and such that the Cauchy boundary conditions

$\psi (x,y)=\alpha (x,y),\quad \mathbf {n} \cdot \nabla \psi =\beta (x,y)$

hold for all boundary points $(x,y)\in \partial \Omega$ . Here $\mathbf {n} \cdot \nabla \psi$ is the derivative in the direction of the normal to the boundary. The functions $\alpha$ and $\beta$ are the Cauchy data.

Notice the difference between a Cauchy boundary condition and a Robin boundary condition. In the former, we specify both the function and the normal derivative. In the latter, we specify a weighted average of the two.

We would like boundary conditions to ensure that exactly one (unique) solution exists, but for second-order partial differential equations, it is not as simple to guarantee existence and uniqueness as it is for ordinary differential equations. Cauchy data are most immediately relevant for hyperbolic problems (for example, the wave equation) on open domains (for example, the half plane).

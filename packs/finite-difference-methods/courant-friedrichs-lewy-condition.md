---
title: "Courant–Friedrichs–Lewy condition"
source: https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Courant–Friedrichs–Lewy condition

In mathematics, the **convergence condition by Courant–Friedrichs–Lewy** (CFL) is a necessary condition for convergence while solving certain partial differential equations (usually hyperbolic PDEs) numerically. It arises in the numerical analysis of explicit time integration schemes, when these are used for the numerical solution. As a consequence, the time step must be less than a certain upper bound, given a fixed spatial increment, in many explicit time-marching computer simulations; otherwise, the simulation produces incorrect or unstable results. The condition is named after Richard Courant, Kurt Friedrichs, and Hans Lewy who described it in their 1928 paper.

## Heuristic description

The principle behind the condition is that, for example, if a wave is moving across a discrete spatial grid and we want to compute its amplitude at discrete time steps of equal duration, then this duration must be less than the time for the wave to travel to adjacent grid points. As a corollary, when the grid point separation is reduced, the upper limit for the time step also decreases. In essence, the numerical domain of dependence of any point in space and time (as determined by initial conditions and the parameters of the approximation scheme) must include the analytical domain of dependence (wherein the initial conditions have an effect on the exact value of the solution at that point) to assure that the scheme can access the information required to form the solution.

## Statement

To make a reasonably formally precise statement of the condition, it is necessary to define the following quantities:

- *Spatial coordinate*: one of the coordinates of the physical space in which the problem is posed
- *Spatial dimension of the problem*: the number n of spatial dimensions, i.e., the number of spatial coordinates of the physical space where the problem is posed. Typical values are $n=1$ , $n=2$ and $n=3$ .
- *Time*: the coordinate, acting as a parameter, which describes the evolution of the system, distinct from the spatial coordinates

The spatial coordinates and the time are discrete-valued independent variables, which are placed at regular distances called the *interval length* and the *time step*, respectively. Using these names, the CFL condition relates the length of the time step to a function of the interval lengths of each spatial coordinate and of the maximum speed that information can travel in the physical space.

Operatively, the CFL condition is commonly prescribed for those terms of the finite-difference approximation of general partial differential equations that model the advection phenomenon.

### The one-dimensional case

For the one-dimensional case, the continuous-time model equation (that is usually solved for w ) is:

${\frac {\partial w}{\partial t}}+u{\frac {\partial w}{\partial x}}=0.$

The CFL condition then has the following form:

$C={\frac {u\,\Delta t}{\Delta x}}\leq C_{\max }$

where:

- the dimensionless number C is called the **Courant number**,
- u is the magnitude of the velocity (whose dimension is length/time)
- $\Delta t$ is the time step (whose dimension is time)
- $\Delta x$ is the length interval (whose dimension is length).

The value of $C_{\max }$ changes with the method used to solve the discretised equation, especially depending on whether the method is explicit or implicit. If an explicit (time-marching) solver is used then typically $C_{\max }=1$ . Implicit (matrix) solvers are usually less sensitive to numerical instability and so larger values of $C_{\max }$ may be tolerated.

### The two and general *n*-dimensional case

In the two-dimensional case, the CFL condition becomes

$C={\frac {u_{x}\,\Delta t}{\Delta x}}+{\frac {u_{y}\,\Delta t}{\Delta y}}\leq C_{\max }$

with the obvious meanings of the symbols involved. By analogy with the two-dimensional case, the general CFL condition for the n -dimensional case is the following one:

$C=\Delta t\left(\sum _{i=1}^{n}{\frac {u_{i}}{\Delta x_{i}}}\right)\leq C_{\max }.$

The interval length is not required to be the same for each spatial variable $\Delta x_{i},i=1,\ldots ,n$ . This "degree of freedom" can be used to somewhat optimize the value of the time step for a particular problem, by varying the values of the different interval to keep it not too small.

### The case where *w* is a vector

In the cases above w was a scalar. The vector form of the first order hyperbolic PDE is

${\frac {\partial {\bf {w}}}{\partial t}}+{\bf {\underline {A}}}{\frac {\partial {\bf {w}}}{\partial x}}=0.$

where ${\bf {w}}\in \mathbb {R} ^{N}$ is a vector of arbitrary dimension N and ${\bf {\underline {A}}}\in \mathbb {R} ^{N}\times \mathbb {R} ^{N}$ is accordingly a matrix of order N . In this case the CFL condition is

${\frac {\Delta t}{\Delta x}}\leq {\frac {1}{|\lambda |_{\max }}}C_{\max }$

where $|\lambda |_{\max }$ is the magnitude of the largest eigenvalue of the matrix ${\bf {\underline {A}}}$ . The extension to multiple dimensions follows the logic described above.

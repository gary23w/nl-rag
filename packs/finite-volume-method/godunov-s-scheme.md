---
title: "Godunov's scheme"
source: https://en.wikipedia.org/wiki/Godunov%27s_scheme
domain: finite-volume-method
license: CC-BY-SA-4.0
tags: finite volume method, godunov scheme, riemann solver, flux limiter
fetched: 2026-07-02
---

# Godunov's scheme

In numerical analysis and computational fluid dynamics, **Godunov's scheme** is a conservative numerical scheme, suggested by Sergei Godunov in 1959, for solving partial differential equations. One can think of this method as a conservative finite volume method which solves exact, or approximate Riemann problems at each inter-cell boundary. In its basic form, Godunov's method is first order accurate in both space and time, yet can be used as a base scheme for developing higher-order methods.

## Basic scheme

Following the classical finite volume method framework, we seek to track a finite set of discrete unknowns, $Q_{i}^{n}={\frac {1}{\Delta x}}\int _{x_{i-1/2}}^{x_{i+1/2}}q(t^{n},x)\,dx$ where the $x_{i-1/2}=x_{\text{low}}+\left(i-1/2\right)\Delta x$ and $t^{n}=n\Delta t$ form a discrete set of points for the hyperbolic problem: $q_{t}+(f(q))_{x}=0,$ where the indices t and x indicate the derivatives in time and space, respectively. If we integrate the hyperbolic problem over a control volume $[x_{i-1/2},x_{i+1/2}],$ we obtain a method of lines (MOL) formulation for the spatial cell averages: ${\frac {\partial }{\partial t}}Q_{i}(t)=-{\frac {1}{\Delta x}}\left(f(q(t,x_{i+1/2}))-f(q(t,x_{i-1/2}))\right),$ which is a classical description of the first order, upwinded finite volume method.

Exact time integration of the above formula from time $t=t^{n}$ to time $t=t^{n+1}$ yields the exact update formula: $Q_{i}^{n+1}=Q_{i}^{n}-{\frac {1}{\Delta x}}\int _{t^{n}}^{t^{n+1}}\left(f(q(t,x_{i+1/2}))-f(q(t,x_{i-1/2}))\right)\,dt.$

Godunov's method replaces the time integral of each $\int _{t^{n}}^{t^{n+1}}f(q(t,x_{i-1/2}))\,dt$ with a forward Euler method which yields a fully discrete update formula for each of the unknowns $Q_{i}^{n}$ . That is, we approximate the integrals with $\int _{t^{n}}^{t^{n+1}}f(q(t,x_{i-1/2}))\,dt\approx \Delta tf^{\downarrow }\left(Q_{i-1}^{n},Q_{i}^{n}\right),$ where $f^{\downarrow }\left(q_{l},q_{r}\right)$ is an approximation to the exact solution of the Riemann problem. For consistency, one assumes that $f^{\downarrow }(q_{l},q_{r})=f(q_{l})\quad {\text{ if }}\quad q_{l}=q_{r},$ and that $f^{\downarrow }$ is increasing in the first argument, and decreasing in the second argument. For scalar problems where $f'(q)>0$ , one can use the simple Upwind scheme, which defines $f^{\downarrow }(q_{l},q_{r})=f(q_{l})$ .

The full Godunov scheme requires the definition of an approximate, or an exact Riemann solver, but in its most basic form, is given by: $Q_{i}^{n+1}=Q_{i}^{n}-\lambda \left({\hat {f}}_{i+1/2}^{n}-{\hat {f}}_{i-1/2}^{n}\right),\quad \lambda ={\frac {\Delta t}{\Delta x}},\quad {\hat {f}}_{i-1/2}^{n}=f^{\downarrow }\left(Q_{i-1}^{n},Q_{i}^{n}\right)$

## Linear problem

In the case of a linear problem, where $f(q)=aq$ , and without loss of generality, we'll assume that $a>0$ , the upwinded Godunov method yields: $Q_{i}^{n+1}=Q_{i}^{n}-\nu \left(Q_{i}^{n}-Q_{i-1}^{n}\right),\quad \nu =a{\frac {\Delta t}{\Delta x}},$ which yields the classical first-order, upwinded Finite Volume scheme whose stability requires $\nu =\left|a{\frac {\Delta t}{\Delta x}}\right|\leq 1$ .

## Three-step algorithm

Following Hirsch, the scheme involves three distinct steps to obtain the solution at $t=(n+1)\Delta t\,$ from the known solution at ${t=n\Delta t}\,$ , as follows:

1. Define piecewise constant approximation of the solution at ${t=(n+1)\Delta t}\,$ . Since the piecewise constant approximation is an average of the solution over the cell of size ${\Delta x}\,$ , the spatial error is of order ${\Delta x}\,$ , and hence the resulting scheme will be first-order accurate in space. Note that this approximation corresponds to a finite volume method representation whereby the discrete values represent averages of the state variables over the cells. Exact relations for the averaged cell values can be obtained from the integral conservation laws.
2. Obtain the solution for the local Riemann problem at the cell interfaces. This is the only physical step of the whole procedure. The discontinuities at the interfaces are resolved in a superposition of waves satisfying locally the conservation equations. The original Godunov method is based upon the exact solution of the Riemann problems. However, approximate solutions can be applied as an alternative.
3. Average the state variables after a time interval ${\Delta t}\,$ . The state variables obtained after Step 2 are averaged over each cell defining a new piecewise constant approximation resulting from the wave propagation during the time interval ${\Delta t}\,$ . To be consistent, the time interval ${\Delta t}\,$ should be limited such that the waves emanating from an interface do not interact with waves created at the adjacent interfaces. Otherwise the situation inside a cell would be influenced by interacting Riemann problems. This leads to the CFL condition $|a_{\max }|\Delta t<\Delta x/2\,$ where $|a_{\max }|\,$ is the maximum wave speed obtained from the cell eigenvalue(s) of the local *Jacobian matrix*.

The first and third steps are solely of a numerical nature and can be considered as a *projection stage*, independent of the second, physical step, the *evolution stage*. Therefore, they can be modified without influencing the physical input, for instance by replacing the piecewise constant approximation by a piecewise linear variation inside each cell, leading to the definition of second-order space-accurate schemes, such as the MUSCL scheme.

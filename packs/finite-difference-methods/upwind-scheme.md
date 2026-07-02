---
title: "Upwind scheme"
source: https://en.wikipedia.org/wiki/Upwind_scheme
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Upwind scheme

In computational physics, the term advection scheme refers to a class of numerical discretization methods for solving hyperbolic partial differential equations. In the so-called upwind schemes *typically*, the so-called upstream variables are used to calculate the derivatives in a flow field. That is, derivatives are estimated using a set of data points biased to be more "upwind" of the query point, with respect to the direction of the flow. Historically, the origin of upwind methods can be traced back to the work of Courant, Isaacson, and Rees who proposed the CIR method.

## Model equation

To illustrate the method, consider the following one-dimensional linear advection equation ${\frac {\partial u}{\partial t}}+a{\frac {\partial u}{\partial x}}=0$ which describes a wave propagating along the x -axis with a velocity a . This equation is also a mathematical model for one-dimensional linear advection. Consider a typical grid point i in the domain. In a one-dimensional domain, there are only two directions associated with point i – left (towards negative infinity) and right (towards positive infinity). If a is positive, the traveling wave solution of the equation above propagates towards the right, the left side is called the *upwind* side and the right side is the *downwind* side. Similarly, if a is negative the traveling wave solution propagates towards the left, the left side is called *downwind* side and right side is the *upwind* side. If the finite difference scheme for the spatial derivative, $\partial u/\partial x$ contains more points in the upwind side, the scheme is called an **upwind-biased** or simply an **upwind scheme**.

## First-order upwind scheme

The simplest upwind scheme possible is the first-order upwind scheme. It is given by

| ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}+a{\frac {u_{i}^{n}-u_{i-1}^{n}}{\Delta x}}=0\quad {\text{for}}\quad a>0$ |   | 1 |
|---|---|---|

| ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}+a{\frac {u_{i+1}^{n}-u_{i}^{n}}{\Delta x}}=0\quad {\text{for}}\quad a<0$ |   | 2 |
|---|---|---|

where n refers to the t dimension and i refers to the x dimension. (By comparison, a central difference scheme in this scenario would look like ${\frac {u_{i}^{n+1}-u_{i}^{n}}{\Delta t}}+a{\frac {u_{i+1}^{n}-u_{i-1}^{n}}{2\Delta x}}=0,$ regardless of the sign of a .)

### Compact form

Defining ${\begin{aligned}a^{+}&=\max(a,0)\,,&a^{-}&={\text{min}}(a,0),\\[1ex]u_{x}^{-}&={\frac {u_{i}^{n}-u_{i-1}^{n}}{\Delta x}}\,,&u_{x}^{+}&={\frac {u_{i+1}^{n}-u_{i}^{n}}{\Delta x}}\end{aligned}}$ the two conditional equations (**1**) and (**2**) can be combined and written in a compact form as

| $u_{i}^{n+1}=u_{i}^{n}-\Delta t\left[a^{+}u_{x}^{-}+a^{-}u_{x}^{+}\right]$ |   | 3 |
|---|---|---|

Equation (3) is a general way of writing any upwind-type schemes.

### Stability

The upwind scheme is stable if the following Courant–Friedrichs–Lewy condition (CFL) is satisfied.

$c=\left|{\frac {a\Delta t}{\Delta x}}\right|\leq 1\quad {\text{ and }}\quad 0\leq a.$

A Taylor series analysis of the upwind scheme discussed above will show that it is first-order accurate in space and time. Modified wavenumber analysis shows that the first-order upwind scheme introduces severe numerical diffusion/dissipation in the solution where large gradients exist due to necessity of high wavenumbers to represent sharp gradients.

## Second-order upwind scheme

The spatial accuracy of the first-order upwind scheme can be improved by including 3 data points instead of just 2, which offers a more accurate finite difference stencil for the approximation of spatial derivative. For the second-order upwind scheme, $u_{x}^{-}$ becomes the 3-point backward difference in equation (**3**) and is defined as $u_{x}^{-}={\frac {3u_{i}^{n}-4u_{i-1}^{n}+u_{i-2}^{n}}{2\Delta x}}$ and $u_{x}^{+}$ is the 3-point forward difference, defined as $u_{x}^{+}={\frac {-u_{i+2}^{n}+4u_{i+1}^{n}-3u_{i}^{n}}{2\Delta x}}$ This scheme is less diffusive compared to the first-order accurate scheme and is called linear upwind differencing (LUD) scheme.

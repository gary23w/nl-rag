---
title: "Lax–Wendroff method"
source: https://en.wikipedia.org/wiki/Lax%E2%80%93Wendroff_method
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Lax–Wendroff method

The **Lax–Wendroff method**, named after Peter Lax and Burton Wendroff, is a numerical method for the solution of hyperbolic partial differential equations, based on finite differences. It is second-order accurate in both space and time. This method is an example of explicit time integration where the function that defines the governing equation is evaluated at the current time.

## Definition

Suppose one has an equation of the following form: ${\frac {\partial u(x,t)}{\partial t}}+{\frac {\partial f(u(x,t))}{\partial x}}=0$ where x and t are independent variables, and the initial state, *u*(*x*, 0) is given.

### Linear case

In the linear case, where *f*(*u*) = *Au*, and *A* is a constant, $u_{i}^{n+1}=u_{i}^{n}-{\frac {\Delta t}{2\Delta x}}A\left[u_{i+1}^{n}-u_{i-1}^{n}\right]+{\frac {\Delta t^{2}}{2\Delta x^{2}}}A^{2}\left[u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n}\right].$ Here n refers to the t dimension and i refers to the x dimension. This linear scheme can be extended to the general non-linear case in different ways. One of them is letting $A(u)=f'(u)={\frac {\partial f}{\partial u}}$

### Non-linear case

The conservative form of Lax-Wendroff for a general non-linear equation is then: $u_{i}^{n+1}=u_{i}^{n}-{\frac {\Delta t}{2\Delta x}}\left[f(u_{i+1}^{n})-f(u_{i-1}^{n})\right]+{\frac {\Delta t^{2}}{2\Delta x^{2}}}\left[A_{i+1/2}\left(f(u_{i+1}^{n})-f(u_{i}^{n})\right)-A_{i-1/2}\left(f(u_{i}^{n})-f(u_{i-1}^{n})\right)\right].$ where $A_{i\pm 1/2}$ is the Jacobian matrix evaluated at ${\textstyle {\frac {1}{2}}(u_{i}^{n}+u_{i\pm 1}^{n})}$ .

## Jacobian free methods

To avoid the Jacobian evaluation, use a two-step procedure.

### Richtmyer method

What follows is the Richtmyer two-step Lax–Wendroff method. The first step in the Richtmyer two-step Lax–Wendroff method calculates values for *f*(*u*(*x*, *t*)) at half time steps, *t**n* + 1/2 and half grid points, *x**i* + 1/2. In the second step values at *t**n* + 1 are calculated using the data for *t**n* and *t**n* + 1/2.

First (Lax) steps: $u_{i+1/2}^{n+1/2}={\frac {1}{2}}(u_{i+1}^{n}+u_{i}^{n})-{\frac {\Delta t}{2\,\Delta x}}(f(u_{i+1}^{n})-f(u_{i}^{n})),$ $u_{i-1/2}^{n+1/2}={\frac {1}{2}}(u_{i}^{n}+u_{i-1}^{n})-{\frac {\Delta t}{2\,\Delta x}}(f(u_{i}^{n})-f(u_{i-1}^{n})).$

Second step: $u_{i}^{n+1}=u_{i}^{n}-{\frac {\Delta t}{\Delta x}}\left[f(u_{i+1/2}^{n+1/2})-f(u_{i-1/2}^{n+1/2})\right].$

### MacCormack method

Another method of this same type was proposed by MacCormack. MacCormack's method uses first forward differencing and then backward differencing:

First step: $u_{i}^{*}=u_{i}^{n}-{\frac {\Delta t}{\Delta x}}(f(u_{i+1}^{n})-f(u_{i}^{n})).$ Second step: $u_{i}^{n+1}={\frac {1}{2}}(u_{i}^{n}+u_{i}^{*})-{\frac {\Delta t}{2\Delta x}}\left[f(u_{i}^{*})-f(u_{i-1}^{*})\right].$

Alternatively, First step: $u_{i}^{*}=u_{i}^{n}-{\frac {\Delta t}{\Delta x}}(f(u_{i}^{n})-f(u_{i-1}^{n})).$ Second step: $u_{i}^{n+1}={\frac {1}{2}}(u_{i}^{n}+u_{i}^{*})-{\frac {\Delta t}{2\Delta x}}\left[f(u_{i+1}^{*})-f(u_{i}^{*})\right].$

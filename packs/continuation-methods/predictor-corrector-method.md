---
title: "Predictor–corrector method"
source: https://en.wikipedia.org/wiki/Predictor%E2%80%93corrector_method
domain: continuation-methods
license: CC-BY-SA-4.0
tags: numerical continuation, homotopy continuation, bifurcation theory, predictor-corrector method
fetched: 2026-07-02
---

# Predictor–corrector method

In numerical analysis, **predictor–corrector methods** belong to a class of algorithms designed to integrate ordinary differential equations – to find an unknown function that satisfies a given differential equation. All such algorithms proceed in two steps:

1. The initial, "prediction" step, starts from a function fitted to the function-values and derivative-values at a preceding set of points to extrapolate ("anticipate") this function's value at a subsequent, new point.
2. The next, "corrector" step refines the initial approximation by using the *predicted* value of the function and *another method* to interpolate that unknown function's value at the **same** subsequent point.

## Predictor–corrector methods for solving ODEs

When considering the numerical solution of ordinary differential equations (ODEs), a predictor–corrector method typically uses an explicit method for the predictor step and an implicit method for the corrector step.

### Example: Euler method with the trapezoidal rule

A simple predictor–corrector method (known as Heun's method) can be constructed from the Euler method (an explicit method) and the trapezoidal rule (an implicit method).

Consider the differential equation

$y'=f(t,y),\quad y(t_{0})=y_{0},$

and denote the step size by h .

First, the predictor step: starting from the current value $y_{i}$ , calculate an initial guess value ${\tilde {y}}_{i+1}$ via the Euler method,

${\tilde {y}}_{i+1}=y_{i}+hf(t_{i},y_{i}).$

Next, the corrector step: improve the initial guess using trapezoidal rule,

$y_{i+1}=y_{i}+{\tfrac {1}{2}}h{\bigl (}f(t_{i},y_{i})+f(t_{i+1},{\tilde {y}}_{i+1}){\bigr )}.$

That value is used as the next step.

### PEC mode and PECE mode

There are different variants of a predictor–corrector method, depending on how often the corrector method is applied. The Predict–Evaluate–Correct–Evaluate (PECE) mode refers to the variant in the above example:

${\begin{aligned}{\tilde {y}}_{i+1}&=y_{i}+hf(t_{i},y_{i}),\\y_{i+1}&=y_{i}+{\tfrac {1}{2}}h{\bigl (}f(t_{i},y_{i})+f(t_{i+1},{\tilde {y}}_{i+1}){\bigr )}.\end{aligned}}$

It is also possible to evaluate the function *f* only once per step by using the method in Predict–Evaluate–Correct (PEC) mode:

${\begin{aligned}{\tilde {y}}_{i+1}&=y_{i}+hf(t_{i},{\tilde {y}}_{i}),\\y_{i+1}&=y_{i}+{\tfrac {1}{2}}h{\bigl (}f(t_{i},{\tilde {y}}_{i})+f(t_{i+1},{\tilde {y}}_{i+1}){\bigr )}.\end{aligned}}$

Additionally, the corrector step can be repeated in the hope that this achieves an even better approximation to the true solution. If the corrector method is run twice, this yields the PECECE mode:

${\begin{aligned}{\tilde {y}}_{i+1}&=y_{i}+hf(t_{i},y_{i}),\\{\hat {y}}_{i+1}&=y_{i}+{\tfrac {1}{2}}h{\bigl (}f(t_{i},y_{i})+f(t_{i+1},{\tilde {y}}_{i+1}){\bigr )},\\y_{i+1}&=y_{i}+{\tfrac {1}{2}}h{\bigl (}f(t_{i},y_{i})+f(t_{i+1},{\hat {y}}_{i+1}){\bigr )}.\end{aligned}}$

The PECEC mode has one fewer function evaluation than PECECE mode.

More generally, if the corrector is run *k* times, the method is in P(EC)*k* or P(EC)*k*E mode. If the corrector method is iterated until it converges, this could be called PE(CE)∞.

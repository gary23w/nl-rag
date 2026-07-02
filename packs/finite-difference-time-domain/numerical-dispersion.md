---
title: "Numerical dispersion"
source: https://en.wikipedia.org/wiki/Numerical_dispersion
domain: finite-difference-time-domain
license: CC-BY-SA-4.0
tags: finite-difference time-domain, yee lattice, absorbing boundary condition, numerical dispersion
fetched: 2026-07-02
---

# Numerical dispersion

In computational mathematics, **numerical dispersion** is a difficulty with computer simulations of continua (such as fluids) wherein the simulated medium exhibits a higher dispersivity than the true medium. This phenomenon can be particularly egregious when the system should not be dispersive at all, for example a fluid acquiring some spurious dispersion in a numerical model. It occurs whenever the dispersion relation for the finite difference approximation is nonlinear. For these reasons, it is often seen as a numerical error. Numerical dispersion is often identified, linked and compared with numerical diffusion, another artifact of similar origin.

## Explanation

In simulations, time and space are divided into discrete grids and the continuous differential equations of motion (such as the Navier–Stokes equation) are discretized into finite-difference equations; these discrete equations are in general unidentical to the original differential equations, so the simulated system behaves differently than the intended physical system. The amount and character of the difference depends on the system being simulated and the type of discretization that is used.

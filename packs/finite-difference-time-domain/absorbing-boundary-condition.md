---
title: "Absorbing boundary condition"
source: https://en.wikipedia.org/wiki/Absorbing_boundary_condition
domain: finite-difference-time-domain
license: CC-BY-SA-4.0
tags: finite-difference time-domain, yee lattice, absorbing boundary condition, numerical dispersion
fetched: 2026-07-02
---

# Absorbing boundary condition

In numerical analysis of wave problems, **absorbing boundary conditions**, **non-reflecting boundary conditions** or **transmitting boundaries** are artificial boundary conditions applied at the edges of a finite computational domain to allow outgoing waves to pass out of the grid without generating reflections.

In many physical problems, such as acoustics, electromagnetics, and fluid dynamics, waves naturally propagate into an infinite or semi-infinite space. However, numerical methods like finite difference or finite element methods require a finite, truncated grid to remain computationally feasible. Without an effective absorbing boundary condition, waves reaching the artificial boundary of the simulation would reflect back into the interior, causing non-physical interference and spurious echoes that contaminate the results.

## Background and history

A perfect absorbing boundary condition would be nonlocal, meaning that the behavior at one point on the boundary depends on the history of the wave field at all other points on the boundary. While mathematically exact, these non-local conditions are often too computationally expensive for large-scale simulations. Consequently, most practical absorbing boundary conditions utilize local approximations based on the differential properties of the wave field. Beyond purely mathematical boundary operators, many implementations utilize material absorbers such as the perfectly matched layer, which simulate an artificial physical region where waves are gradually attenuated through absorptive properties before they reach the simulation's edge.

Early absorbing boundary conditions, adopted until the 1970s, were based on the application of Sommerfeld radiation condition; these are denoted as the zeroth-order boundary conditions. From the late 1970s to the mid-1980s, low-order absorbing boundary conditions, such as Bayliss–Turkel and Engquist–Majda absorbing boundary conditions were introduced. The 1990s saw the introduction of perfectly matched layers, as well as higher-order local boundary conditions.

## List of absorbing boundary conditions

- Ang–Newmark boundary condition
- Bayliss–Turkel radiation boundary condition
- Complementary operator method
- Grote–Keller nonreflecting boundary condition
- Higdon's absorbing boundary condition
- Engquist–Majda absorbing boundary condition
  - Generalized Trefethen–Halpern absorbing boundary condition
  - Mur absorbing boundary condition
- Liao–Wong absorbing boundary condition
- Lysmer–Kuhlemeyer boundary condition
- Perfectly matched layer

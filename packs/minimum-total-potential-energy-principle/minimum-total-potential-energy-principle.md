---
title: "Minimum total potential energy principle"
source: https://en.wikipedia.org/wiki/Minimum_total_potential_energy_principle
domain: minimum-total-potential-energy-principle
license: CC-BY-SA-4.0
tags: minimum total potential energy principle
fetched: 2026-07-04
---

# Minimum total potential energy principle

The **minimum total potential energy principle** is a fundamental concept used in physics and engineering. It dictates that at low temperatures a structure or body shall deform or displace to a position that (locally) minimizes the total potential energy, with the lost potential energy being converted into kinetic energy (specifically heat).

## Some examples

- A free proton and free electron will tend to combine to form the lowest energy state (the ground state) of a hydrogen atom, the most stable configuration. This is because that state's energy is 13.6 electron volts (eV) lower than when the two particles separated by an infinite distance. The dissipation in this system takes the form of spontaneous emission of electromagnetic radiation, which increases the entropy of the surroundings.
- A rolling ball will end up stationary at the bottom of a hill, the point of minimum potential energy. The reason is that as it rolls downward under the influence of gravity, friction produced by its motion transfers energy in the form of heat to the surroundings with an attendant increase in entropy.
- A protein folds into the state of lowest potential energy. In this case, the dissipation takes the form of vibration of atoms within or adjacent to the protein.

## Structural mechanics

The total potential energy, ${\boldsymbol {\Pi }}$ , is the sum of the elastic strain energy, **U**, stored in the deformed body and the potential energy, **V**, associated to the applied forces:

| ${\boldsymbol {\Pi }}=\mathbf {U} +\mathbf {V}$ |   | 1 |
|---|---|---|

This energy is at a stationary position when an infinitesimal variation from such position involves no change in energy:

| $\delta {\boldsymbol {\Pi }}=\delta (\mathbf {U} +\mathbf {V} )=0$ |   | 2 |
|---|---|---|

The principle of minimum total potential energy may be derived as a special case of the virtual work principle for elastic systems subject to conservative forces.

The equality between external and internal virtual work (due to virtual displacements) is:

| $\int _{S_{t}}\delta \ \mathbf {u} ^{T}\mathbf {T} dS+\int _{V}\delta \ \mathbf {u} ^{T}\mathbf {f} dV=\int _{V}\delta {\boldsymbol {\epsilon }}^{T}{\boldsymbol {\sigma }}dV$ |   | 3 |
|---|---|---|

where

- $\mathbf {u}$ = vector of displacements
- $\mathbf {T}$ = vector of distributed forces acting on the part $S_{t}$ of the surface
- $\mathbf {f}$ = vector of body forces

In the special case of elastic bodies, the right-hand-side of (**3**) can be taken to be the change, $\delta \mathbf {U}$ , of elastic strain energy **U** due to infinitesimal variations of real displacements. In addition, when the external forces are conservative forces, the left-hand-side of (**3**) can be seen as the change in the potential energy function **V** of the forces. The function **V** is defined as: $\mathbf {V} =-\int _{S_{t}}\mathbf {u} ^{T}\mathbf {T} dS-\int _{V}\mathbf {u} ^{T}\mathbf {f} dV$ where the minus sign implies a loss of potential energy as the force is displaced in its direction. With these two subsidiary conditions, **Equation 3** becomes: $-\delta \ \mathbf {V} =\delta \ \mathbf {U}$ This leads to (**2**) as desired. The variational form of (**2**) is often used as the basis for developing the finite element method in structural mechanics.

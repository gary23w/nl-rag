---
title: "Boussinesq approximation (buoyancy)"
source: https://en.wikipedia.org/wiki/Boussinesq_approximation_(buoyancy)
domain: ocean-modeling
license: CC-BY-SA-4.0
tags: ocean general circulation model, physical oceanography, thermohaline circulation, ekman transport
fetched: 2026-07-02
---

# Boussinesq approximation (buoyancy)

In fluid dynamics, the **Boussinesq approximation** (pronounced [businɛsk], named for Joseph Valentin Boussinesq) is used in the field of buoyancy-driven flow (also known as natural convection). It ignores density differences except where they appear in terms multiplied by g, the acceleration due to gravity. The essence of the Boussinesq approximation is that the difference in inertia is negligible but gravity is sufficiently strong to make the specific weight appreciably different between the two fluids. The existence of sound waves in a Boussinesq fluid is not possible as sound is the result of density fluctuations within a fluid.

Boussinesq flows are common in nature (such as atmospheric fronts, oceanic circulation, katabatic winds), industry (dense gas dispersion, fume cupboard ventilation), and the built environment (natural ventilation, central heating). The approximation can be used to simplify the equations describing such flows, whilst still describing the flow behaviour to a high degree of accuracy.

## Formulation

The Boussinesq approximation is applied to problems where the fluid varies in temperature (or composition) from one place to another, driving a flow of fluid and heat transfer (or mass transfer). The fluid satisfies conservation of mass, conservation of momentum and conservation of energy. In the Boussinesq approximation, variations in fluid properties other than density ρ are ignored, and density only appears when it is multiplied by g, the gravitational acceleration. If **u** is the local velocity of a parcel of fluid, the continuity equation for conservation of mass is

${\frac {\partial \rho }{\partial t}}+\nabla \cdot \left(\rho \mathbf {u} \right)=0.$

If density variations are ignored, this reduces to

| $\nabla \cdot \mathbf {u} =0.$ |   | 1 |
|---|---|---|

The general expression for conservation of momentum of an incompressible, Newtonian fluid (the Navier–Stokes equations) is

${\frac {\partial \mathbf {u} }{\partial t}}+\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+\nu \nabla ^{2}\mathbf {u} +{\frac {1}{\rho }}\mathbf {F} ,$

where ν (nu) is the kinematic viscosity and **F** is the sum of any body forces such as gravity. In this equation, density variations are assumed to have a fixed part and another part that has a linear dependence on temperature:

$\rho =\rho _{0}-\alpha \rho _{0}(T-T_{0}),$

where α is the coefficient of thermal expansion. The Boussinesq approximation states that the density variation is only important in the buoyancy term.

If $F=\rho \mathbf {g}$ is the gravitational body force, the resulting conservation equation is

| ${\frac {\partial \mathbf {u} }{\partial t}}+\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} =-{\frac {1}{\rho _{0}}}\nabla (p-\rho _{0}\mathbf {g} \cdot \mathbf {z} )+\nu \nabla ^{2}\mathbf {u} -\mathbf {g} \alpha (T-T_{0}).$ |   | 2 |
|---|---|---|

In the equation for heat flow in a temperature gradient, the heat capacity per unit volume, $\rho C_{p}$ , is assumed constant and the dissipation term is ignored. The resulting equation is

| ${\frac {\partial T}{\partial t}}+\mathbf {u} \cdot \nabla T={\frac {k}{\rho C_{p}}}\nabla ^{2}T+{\frac {J}{\rho C_{p}}},$ |   | 3 |
|---|---|---|

where J is the rate per unit volume of internal heat production and k is the thermal conductivity.

The three numbered equations are the basic convection equations in the Boussinesq approximation.

## Advantages

The advantage of the approximation arises because when considering a flow of, say, warm and cold water of density *ρ*1 and *ρ*2 one needs only to consider a single density ρ: the difference Δ*ρ* = *ρ*1 − *ρ*2 is negligible. Dimensional analysis shows that, under these circumstances, the only sensible way that acceleration due to gravity g should enter into the equations of motion is in the reduced gravity g′ where

$g'=g{\frac {\rho _{1}-\rho _{2}}{\rho }}.$

(Note that the denominator may be either density without affecting the result because the change would be of order ⁠ $g\left({\tfrac {\Delta \rho }{\rho }}\right)^{2}$ ⁠.) The most generally used dimensionless number would be the Richardson number and Rayleigh number.

The mathematics of the flow is therefore simpler because the density ratio ⁠*ρ*1/*ρ*2⁠, a dimensionless number, does not affect the flow; the Boussinesq approximation states that it may be assumed to be exactly one.

## Inversions

One feature of Boussinesq flows is that they look the same when viewed upside-down, provided that the identities of the fluids are reversed. The Boussinesq approximation is *inaccurate* when the dimensionless density difference ⁠Δ*ρ*/*ρ*⁠ is approximately 1, i.e. Δ*ρ* ≈ *ρ*.

For example, consider an open window in a warm room. The warm air inside is less dense than the cold air outside, which flows into the room and down towards the floor. Now imagine the opposite: a cold room exposed to warm outside air. Here the air flowing in moves up toward the ceiling. If the flow is Boussinesq (and the room is otherwise symmetrical), then viewing the cold room upside down is exactly the same as viewing the warm room right-way-round. This is because the only way density enters the problem is via the reduced gravity g′ which undergoes only a sign change when changing from the warm room flow to the cold room flow.

An example of a non-Boussinesq flow is bubbles rising in water. The behaviour of air bubbles rising in water is very different from the behaviour of water falling in air: in the former case rising bubbles tend to form hemispherical shells, while water falling in air splits into raindrops (at small length scales surface tension enters the problem and confuses the issue).

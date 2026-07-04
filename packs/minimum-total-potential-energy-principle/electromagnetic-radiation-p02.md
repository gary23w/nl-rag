---
title: "Electromagnetic radiation (part 2/2)"
source: https://en.wikipedia.org/wiki/Electromagnetic_radiation
domain: minimum-total-potential-energy-principle
license: CC-BY-SA-4.0
tags: minimum total potential energy principle
fetched: 2026-07-04
part: 2/2
---

## Derivation from electromagnetic theory

Electromagnetic waves are predicted by the classical laws of electricity and magnetism, known as Maxwell's equations. There are nontrivial solutions of the homogeneous Maxwell's equations (without charges or currents), describing *waves* of changing electric and magnetic fields. Beginning with Maxwell's equations in free space:

| $\nabla \cdot \mathbf {E} =0$ |   | 1 |
|---|---|---|

| $\nabla \times \mathbf {E} =-{\frac {\partial \mathbf {B} }{\partial t}}$ |   | 2 |
|---|---|---|

| $\nabla \cdot \mathbf {B} =0$ |   | 3 |
|---|---|---|

| $\nabla \times \mathbf {B} =\mu _{0}\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}$ |   | 4 |
|---|---|---|

where

- $\mathbf {E}$ and $\mathbf {B}$ are the electric field (measured in V/m or N/C) and the magnetic field (measured in T or Wb/m2), respectively;
- $\nabla \cdot \mathbf {X}$ yields the divergence and $\nabla \times \mathbf {X}$ the curl of a vector field $\mathbf {X}$ ;
- ${\frac {\partial \mathbf {B} }{\partial t}}$ and ${\frac {\partial \mathbf {E} }{\partial t}}$ are partial derivatives (rate of change in time, with location fixed) of the magnetic and electric field;
- $\mu _{0}$ is the permeability of a vacuum (4π × 10−7 H/m), and $\varepsilon _{0}$ is the permittivity of a vacuum (8.85 × 10−12 F/m);

Besides the trivial solution $\mathbf {E} =\mathbf {B} =\mathbf {0}$ , useful solutions can be derived with the following vector identity, valid for all vectors $\mathbf {A}$ in some vector field: $\nabla \times \left(\nabla \times \mathbf {A} \right)=\nabla \left(\nabla \cdot \mathbf {A} \right)-\nabla ^{2}\mathbf {A} .$ Taking the curl of the second Maxwell's equation (**2**) yields:

| $\nabla \times \left(\nabla \times \mathbf {E} \right)=\nabla \times \left(-{\frac {\partial \mathbf {B} }{\partial t}}\right)$ |   | 5 |
|---|---|---|

Evaluating the left hand side of (**5**) with the above identity and simplifying using (**1**), yields:

| $\nabla \times \left(\nabla \times \mathbf {E} \right)=\nabla \left(\nabla \cdot \mathbf {E} \right)-\nabla ^{2}\mathbf {E} =-\nabla ^{2}\mathbf {E} .$ |   | 6 |
|---|---|---|

Evaluating the right hand side of (**5**) by exchanging the sequence of derivatives and inserting the fourth Maxwell's equation (**4**), yields:

| $\nabla \times \left(-{\frac {\partial \mathbf {B} }{\partial t}}\right)=-{\frac {\partial }{\partial t}}\left(\nabla \times \mathbf {B} \right)=-\mu _{0}\varepsilon _{0}{\frac {\partial ^{2}\mathbf {E} }{\partial t^{2}}}$ |   | 7 |
|---|---|---|

Combining (**6**) and (**7**) again, gives a vector-valued differential equation for the electric field, solving the homogeneous Maxwell's equations:

$\nabla ^{2}\mathbf {E} =\mu _{0}\varepsilon _{0}{\frac {\partial ^{2}\mathbf {E} }{\partial t^{2}}}$

Taking the curl of the fourth Maxwell's equation (**4**) results in a similar differential equation for a magnetic field solving the homogeneous Maxwell's equations:

$\nabla ^{2}\mathbf {B} =\mu _{0}\varepsilon _{0}{\frac {\partial ^{2}\mathbf {B} }{\partial t^{2}}}.$

Both differential equations have the form of the general wave equation for waves propagating with speed $c_{0},$ where f is a function of time and location, which gives the amplitude of the wave at some time at a certain location: $\nabla ^{2}f={\frac {1}{{c_{0}}^{2}}}{\frac {\partial ^{2}f}{\partial t^{2}}}$ This is also written as: $\Box f=0$ where $\Box$ denotes the so-called d'Alembert operator, which in Cartesian coordinates is given as: $\Box =\nabla ^{2}-{\frac {1}{{c_{0}}^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}={\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {\partial ^{2}}{\partial y^{2}}}+{\frac {\partial ^{2}}{\partial z^{2}}}-{\frac {1}{{c_{0}}^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}\$

Comparing the terms for the speed of propagation, yields in the case of the electric and magnetic fields: $c_{0}={\frac {1}{\sqrt {\mu _{0}\varepsilon _{0}}}}.$

This is the speed of light in vacuum. Thus Maxwell's equations connect the vacuum permittivity $\varepsilon _{0}$ , the vacuum permeability $\mu _{0}$ , and the speed of light, *c*0, via the above equation. This relationship had been discovered by Wilhelm Eduard Weber and Rudolf Kohlrausch prior to the development of Maxwell's electrodynamics, however Maxwell was the first to produce a field theory consistent with waves traveling at the speed of light.

These are only two equations versus the original four, so more information pertains to these waves hidden within Maxwell's equations. A generic vector wave for the electric field has the form $\mathbf {E} =\mathbf {E} _{0}f{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)}$ Here, $\mathbf {E} _{0}$ is a constant vector, f is any second differentiable function, ${\hat {\mathbf {k} }}$ is a unit vector in the direction of propagation, and ${\mathbf {x} }$ is a position vector. $f{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)}$ is a generic solution to the wave equation. In other words, $\nabla ^{2}f{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)}={\frac {1}{{c_{0}}^{2}}}{\frac {\partial ^{2}}{\partial t^{2}}}f{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)},$ for a generic wave traveling in the ${\hat {\mathbf {k} }}$ direction.

From the first of Maxwell's equations, we get $\nabla \cdot \mathbf {E} ={\hat {\mathbf {k} }}\cdot \mathbf {E} _{0}f'{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)}=0$ Thus, $\mathbf {E} \cdot {\hat {\mathbf {k} }}=0$ which implies that the electric field is orthogonal to the direction the wave propagates. The second of Maxwell's equations yields the magnetic field, namely, $\nabla \times \mathbf {E} ={\hat {\mathbf {k} }}\times \mathbf {E} _{0}f'{\left({\hat {\mathbf {k} }}\cdot \mathbf {x} -c_{0}t\right)}=-{\frac {\partial \mathbf {B} }{\partial t}}$ Thus, $\mathbf {B} ={\frac {1}{c_{0}}}{\hat {\mathbf {k} }}\times \mathbf {E}$ The remaining equations will be satisfied by this choice of $\mathbf {E} ,\mathbf {B}$ .

The electric and magnetic field waves in the far-field travel at the speed of light. They have a special restricted orientation and proportional magnitudes, $E_{0}=c_{0}B_{0}$ , which can be seen immediately from the Poynting vector. The electric field, magnetic field, and direction of wave propagation are all orthogonal, and the wave propagates in the same direction as $\mathbf {E} \times \mathbf {B}$ . Also **E** and **B** far-fields in free space, which as wave solutions depend primarily on these two Maxwell's equations to remain in phase with each other. This is guaranteed since the generic wave solution is first order in both space and time, and the curl operator on one side of these equations results in first-order spatial derivatives of the wave solution, while the time-derivative on the other side of the equations, which gives the other field, is first-order in time, resulting in the same phase shift for both fields in each mathematical operation.

From the viewpoint of an electromagnetic wave traveling forward, the electric field might be oscillating up and down, while the magnetic field oscillates right and left. This picture can be rotated with the electric field oscillating right and left and the magnetic field oscillating down and up. This is a different solution that is traveling in the same direction. This arbitrariness in the orientation with respect to propagation direction is known as polarization. On a quantum level, it is described as photon polarization. The direction of the polarization is defined as the direction of the electric field.

More general forms of the second-order wave equations given above are available, allowing for both non-vacuum propagation media and sources. Many competing derivations exist, all with varying levels of approximation and intended applications. One very general example is a form of the electric field equation, which was factorized into a pair of explicitly directional wave equations, and then efficiently reduced into a single uni-directional wave equation by means of a simple slow-evolution approximation.

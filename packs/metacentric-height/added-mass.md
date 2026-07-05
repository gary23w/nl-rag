---
title: "Added mass"
source: https://en.wikipedia.org/wiki/Added_mass
domain: metacentric-height
license: CC-BY-SA-4.0
tags: metacentric height
fetched: 2026-07-05
---

# Added mass

In fluid mechanics, **added mass** or **virtual mass** is the inertia added to a system because an accelerating or decelerating body must move (or deflect) some volume of surrounding fluid as it moves through it. Added mass is a common issue because the object and surrounding fluid cannot occupy the same physical space simultaneously. For simplicity this can be modeled as some volume of fluid moving with the object, though in reality "all" the fluid will be accelerated, to various degrees.

The dimensionless **added mass coefficient** is the added mass divided by the displaced fluid mass – i.e. divided by the fluid density times the volume of the body. In general, the added mass is a second-order tensor, relating the fluid acceleration vector to the resulting force vector on the body.

## Background

Friedrich Wilhelm Bessel proposed the concept of added mass in 1828 to describe the motion of a pendulum in a fluid. The period of such a pendulum increased relative to its period in a vacuum (even after accounting for buoyancy effects), indicating that the surrounding fluid increased the effective mass of the system.

The concept of added mass is arguably the first example of renormalization in physics. The concept can also be thought of as a classical physics analogue of the quantum mechanical concept of quasiparticles. It is, however, not to be confused with relativistic mass increase.

It is often erroneously stated that the added mass is determined by the momentum of the fluid. That this is not the case, it becomes clear when considering the case of the fluid in a large box, where the fluid momentum is exactly zero at every moment of time. The added mass is actually determined by the quasi-momentum: the added mass times the body acceleration is equal to the time derivative of the fluid quasi-momentum.

## Virtual mass force

Unsteady forces due to a change of the relative velocity of a body submerged in a fluid can be divided into two parts: the virtual mass effect and the Basset force.

The origin of the force is that the fluid will gain kinetic energy at the expense of the work done by an accelerating submerged body.

It can be shown that the virtual mass force, for a spherical particle submerged in an inviscid, incompressible fluid is

$\mathbf {F} ={\frac {\rho _{\mathrm {c} }V_{\mathrm {p} }}{2}}\left({\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}-{\frac {\mathrm {d} \mathbf {v} }{\mathrm {d} t}}\right),$

where bold symbols denote vectors, $\mathbf {u}$ is the fluid flow velocity, $\mathbf {v}$ is the spherical particle velocity, $\rho _{\mathrm {c} }$ is the mass density of the fluid (continuous phase), $V_{\mathrm {p} }$ is the volume of the particle, and D/D*t* denotes the material derivative.

The origin of the notion "virtual mass" becomes evident when we take a look at the momentum equation for the particle.

$m_{\mathrm {p} }{\frac {\mathrm {d} \mathbf {v} }{\mathrm {d} t}}=\sum \mathbf {F} +{\frac {\rho _{\mathrm {c} }V_{\mathrm {p} }}{2}}\left({\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}-{\frac {\mathrm {d} \mathbf {v} }{\mathrm {d} t}}\right),$

where $\sum \mathbf {F}$ is the sum of all other force terms on the particle, such as gravity, pressure gradient, drag, lift, Basset force, etc.

Moving the derivative of the particle velocity from the right hand side of the equation to the left we get

$\left(m_{\mathrm {p} }+{\frac {\rho _{\mathrm {c} }V_{\mathrm {p} }}{2}}\right){\frac {\mathrm {d} \mathbf {v} }{\mathrm {d} t}}=\sum \mathbf {F} +{\frac {\rho _{\mathrm {c} }V_{\mathrm {p} }}{2}}{\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}},$

so the particle is accelerated as if it had an added mass of half the fluid it displaces, and there is also an additional force contribution on the right hand side due to acceleration of the fluid.

## Applications

The added mass can be incorporated into most physics equations by considering an effective mass as the sum of the mass and added mass. This sum is commonly known as the "virtual mass".

A simple formulation of the added mass for a spherical body permits Newton's classical second law to be written in the form

$F=m\,a$

becomes

$F=(m+m_{\text{added}})\,a.$

One can show that the added mass for a sphere (of radius r ) is ${\tfrac {2}{3}}\pi r^{3}\rho _{\text{fluid}}$ , which is *half* the volume of the sphere times the density of the fluid. For a general body, the added mass becomes a tensor (referred to as the induced mass tensor), with components depending on the direction of motion of the body. Not all elements in the added mass tensor will have dimension mass, some will be mass × length and some will be mass × length2.

All bodies accelerating in a fluid will be affected by added mass, but since the added mass is dependent on the density of the fluid, the effect is often neglected for dense bodies falling in much less dense fluids. For situations where the density of the fluid is comparable to or greater than the density of the body, the added mass can often be greater than the mass of the body and neglecting it can introduce significant errors into a calculation.

For example, a spherical air bubble rising in water has a mass of ${\tfrac {4}{3}}\pi r^{3}\rho _{\text{air}}$ but an added mass of ${\tfrac {2}{3}}\pi r^{3}\rho _{\text{water}}.$ Since water is approximately 800 times denser than air (at RTP), the added mass in this case is approximately 400 times the mass of the bubble.

### Naval architecture

These principles also apply to ships, submarines, and offshore platforms. In the marine industry, added mass is referred to as hydrodynamic added mass. In ship design, the energy required to accelerate the added mass must be taken into account when performing a sea keeping analysis. For ships, the added mass can easily reach one fourth or one third of the mass of the ship and therefore represents a significant inertia, in addition to frictional and wavemaking drag forces.

For certain geometries freely sinking through a column of water, hydrodynamic added mass associated with the sinking body can be much larger than the mass of the object. This situation can occur, for instance, when the sinking body has a large flat surface with its normal vector pointed in the direction of motion (downward). A substantial amount of kinetic energy is released when such an object is abruptly decelerated (e.g., due to an impact with the seabed).

In the offshore industry hydrodynamic added mass of different geometries are the subject of considerable investigation. These studies typically are required as input to subsea dropped object risk assessments (studies focused on quantifying risk of dropped object impacts to subsea infrastructure). As hydrodynamic added mass can make up a significant proportion of a sinking object's total mass at the instant of impact, it significantly influences the design resistance considered for subsea protection structures.

Proximity to a boundary (or another object) can influence the quantity of hydrodynamic added mass. This means that added mass depends on both the object geometry and its proximity to a boundary. For floating bodies (e.g., ships/vessels) this means that the response of the floating body (i.e., due to wave action) is altered in finite water depths (the effect is virtually nonexistent in deep water). The specific depth (or proximity to a boundary) at which the hydrodynamic added mass is affected depends on the body's geometry and location and shape of a boundary (e.g., a dock, seawall, bulkhead, or the seabed).

The hydrodynamic added mass associated with a freely sinking object near a boundary is similar to that of a floating body. In general, hydrodynamic added mass increases as the distance between a boundary and a body decreases. This characteristic is important when planning subsea installations or predicting the motion of a floating body in shallow water conditions.

### Aeronautics

In aircraft (other than lighter-than-air balloons and blimps), the added mass is not usually taken into account because the density of the air is so small.

### Hydraulic structures

Hydraulic structures like weirs or locks often contain moveable steel structures like valves or gates, which are submerged under water. These steel structures are often constructed with thin steel plates mounted on girders. When the steel structures are accelerated or decelerated, substantial amounts of water are moved, too. This added mass must e.g. be taken into account when designing the drive systems for these steel structures.

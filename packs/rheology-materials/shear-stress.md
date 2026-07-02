---
title: "Shear stress"
source: https://en.wikipedia.org/wiki/Shear_stress
domain: rheology-materials
license: CC-BY-SA-4.0
tags: viscoelasticity, shear stress, flow behavior, storage modulus
fetched: 2026-07-02
---

# Shear stress

**Shear stress** (often denoted by **τ**, Greek: tau) is the component of stress coplanar with a material cross section. It arises from the shear force, the component of force vector parallel to the material cross section. *Normal stress*, on the other hand, arises from the force vector component perpendicular to the material cross section on which it acts.

## General shear stress

The formula to calculate average shear stress τ or force per unit area is $\tau ={F \over A},$ where F is the force applied and A is the cross-sectional area.

## Other forms

### Wall shear stress

**Wall shear stress** expresses the retarding force (per unit area) from a wall in the layers of a fluid flowing next to the wall. It is defined as: $\tau _{w}:=\mu \left.{\frac {\partial u}{\partial y}}\right|_{y=0},$ where μ is the dynamic viscosity, u is the flow velocity, and y is the distance from the wall.

It is used, for example, in the description of arterial blood flow, where there is evidence that it affects the atherogenic process.

### Pure

Pure shear stress is related to pure shear strain, denoted γ, by the equation $\tau =\gamma G,$ where G is the shear modulus of the isotropic material, given by $G={\frac {E}{2(1+\nu )}}.$ Here, E is Young's modulus and ν is Poisson's ratio.

### Beam shear

Beam shear is defined as the internal shear stress of a beam caused by the shear force applied to the beam: $\tau :={\frac {fQ}{Ib}},$ where

- f is the total shear force at the location in question,
- Q is the statical moment of area,
- b is the thickness (width) in the material perpendicular to the shear, and
- I is the moment of inertia of the entire cross-sectional area.

The beam shear formula is also known as Zhuravskii shear stress formula after Dmitrii Ivanovich Zhuravskii, who derived it in 1855.

### Semi-monocoque shear

Shear stresses within a semi-monocoque structure may be calculated by idealizing the cross-section of the structure into a set of stringers (carrying only axial loads) and webs (carrying only shear flows). Dividing the shear flow by the thickness of a given portion of the semi-monocoque structure yields the shear stress. Thus, the maximum shear stress will occur either in the web of maximum shear flow or minimum thickness.

Constructions in soil can also fail due to shear; e.g., the weight of an earth-filled dam or dike may cause the subsoil to collapse, like a small landslide.

### Impact shear

The maximum shear stress created in a solid round bar subject to impact is given by the equation $\tau =2{\sqrt {\frac {UG}{V}}},$ where

- U is the change in kinetic energy,
- G is the shear modulus, and
- V is the volume of the rod.

Furthermore,

*U* = *U*rotating + *U*applied,

where

- *U*rotating = ⁠1/2⁠*Iω*2,
- *U*applied = *Tθ*displaced,
- I is the mass moment of inertia, and
- ω is the angular speed.

### Shear stress in fluids

Any real fluids (liquids and gases included) moving along a solid boundary will incur a shear stress at that boundary. The no-slip condition dictates that the speed of the fluid at the boundary (relative to the boundary) is zero, although at some height from the boundary, the flow speed must equal that of the fluid. The region between these two points is named the boundary layer. For all Newtonian fluids in laminar flow, the shear stress is proportional to the strain rate in the fluid, where the viscosity is the constant of proportionality. For non-Newtonian fluids, the viscosity is not constant. The shear stress is imparted onto the boundary as a result of this loss of velocity.

For a Newtonian fluid, the shear stress at a surface element parallel to a flat plate at the point y is given by $\tau (y)=\mu {\frac {\partial u}{\partial y}},$ where

- μ is the dynamic viscosity of the flow,
- u is the flow velocity along the boundary, and
- y is the height above the boundary.

Specifically, the wall shear stress is defined as $\tau _{\mathrm {w} }:=\tau (y=0)=\mu \left.{\frac {\partial u}{\partial y}}\right|_{y=0}~.$ Newton's constitutive law, for any general geometry (including the flat plate above mentioned), states that shear tensor (a second-order tensor) is proportional to the flow velocity gradient (the velocity is a vector, so its gradient is a second-order tensor): ${\boldsymbol {\tau }}(\mathbf {u} )=\mu {\boldsymbol {\nabla }}\mathbf {u} .$ The constant of proportionality is named *dynamic viscosity*. For an isotropic Newtonian flow, it is a scalar, while for anisotropic Newtonian flows, it can be a second-order tensor. The fundamental aspect is that for a Newtonian fluid, the dynamic viscosity is independent of flow velocity (i.e., the shear stress constitutive law is *linear*), while for non-Newtonian flows this is not true, and one should allow for the modification ${\boldsymbol {\tau }}(\mathbf {u} )=\mu (\mathbf {u} ){\boldsymbol {\nabla }}\mathbf {u} .$ This no longer Newton's law but a generic tensorial identity: one can always find an expression of the viscosity as function of the flow velocity given any expression of the shear stress as function of the flow velocity. On the other hand, given a shear stress as function of the flow velocity, it represents a Newtonian flow only if it can be expressed as a constant for the gradient of the flow velocity. The constant one finds in this case is the dynamic viscosity of the flow.

## Measurement with sensors

### Diverging fringe shear stress sensor

This relationship can be exploited to measure the wall shear stress. If a sensor could directly measure the gradient of the velocity profile at the wall, then multiplying by the dynamic viscosity would yield the shear stress. Such a sensor was demonstrated by A. A. Naqwi and W. C. Reynolds. The interference pattern generated by sending a beam of light through two parallel slits forms a network of linearly diverging fringes that seem to originate from the plane of the two slits (see double-slit experiment). As a particle in a fluid passes through the fringes, a receiver detects the reflection of the fringe pattern. The signal can be processed, and from the fringe angle, the height and velocity of the particle can be extrapolated. The measured value of the wall velocity gradient is independent of the fluid properties, and as a result does not require calibration. Recent advancements in the micro-optic fabrication technologies have made it possible to use integrated diffractive optical elements to fabricate diverging fringe shear stress sensors usable both in air and liquid.

### Micro-pillar shear-stress sensor

A further measurement technique is that of slender wall-mounted micro-pillars made of the flexible polymer polydimethylsiloxane, which bend in reaction to the applying drag forces in the vicinity of the wall. The sensor thereby belongs to the indirect measurement principles relying on the relationship between near-wall velocity gradients and the local wall-shear stress.

### Electro-diffusional method

The electro-diffusional method measures the wall shear rate in the liquid phase from microelectrodes under limiting diffusion current conditions. A potential difference between an anode of a broad surface (usually located far from the measuring area) and the small working electrode acting as a cathode leads to a fast redox reaction. The ion disappearance occurs only on the microprobe active surface, causing the development of the diffusion boundary layer, in which the fast electro-diffusion reaction rate is controlled only by diffusion. The resolution of the convective-diffusive equation in the near-wall region of the microelectrode lead to analytical solutions relying the characteristics length of the microprobes, the diffusional properties of the electrochemical solution, and the wall shear rate.

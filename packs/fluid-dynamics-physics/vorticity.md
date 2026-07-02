---
title: "Vorticity"
source: https://en.wikipedia.org/wiki/Vorticity
domain: fluid-dynamics-physics
license: CC-BY-SA-4.0
tags: fluid dynamics, reynolds number, boundary layer, compressible flow
fetched: 2026-07-02
---

# Vorticity

In continuum mechanics, **vorticity** is a pseudovector (or axial vector) field that describes the local spinning motion of a continuum near some point (the tendency of something to rotate), as would be seen by an observer located at that point and traveling along with the flow. It is an important quantity in the dynamical theory of fluids and provides a convenient framework for understanding a variety of complex flow phenomena, such as the generation of lift on wings.

Mathematically, the vorticity ${\boldsymbol {\omega }}$ is the curl of the flow velocity $\mathbf {v}$ :

${\boldsymbol {\omega }}\equiv \nabla \times \mathbf {v} \,,$

where $\nabla$ is the nabla operator. Conceptually, ${\boldsymbol {\omega }}$ could be determined by marking parts of a continuum in a small neighborhood of the point in question, and watching their *relative* displacements as they move along the flow. The vorticity ${\boldsymbol {\omega }}$ would be twice the mean angular velocity vector of those particles relative to their center of mass, oriented according to the right-hand rule. By its own definition, the vorticity vector is a solenoidal field since $\nabla \cdot {\boldsymbol {\omega }}=0.$

In a two-dimensional flow, ${\boldsymbol {\omega }}$ is always perpendicular to the plane of the flow, and can therefore be considered a scalar field.

The dynamics of vorticity are fundamentally linked to drag through the Josephson-Anderson relation.

## Mathematical definition and properties

Mathematically, the vorticity of a three-dimensional flow is a pseudovector field, usually denoted by ${\boldsymbol {\omega }}$ , defined as the curl of the velocity field $\mathbf {v}$ describing the continuum motion. In Cartesian coordinates:

${\begin{aligned}{\boldsymbol {\omega }}=\nabla \times \mathbf {v} =\left({\dfrac {\partial v_{z}}{\partial y}}-{\dfrac {\partial v_{y}}{\partial z}},{\dfrac {\partial v_{x}}{\partial z}}-{\dfrac {\partial v_{z}}{\partial x}},{\dfrac {\partial v_{y}}{\partial x}}-{\dfrac {\partial v_{x}}{\partial y}}\right)\,.\end{aligned}}$

We may also express this in index notation as $\omega _{i}=\varepsilon _{ijk}{\frac {\partial v_{k}}{\partial x_{j}}}$ . In words, the vorticity tells how the velocity vector changes when one moves by an infinitesimal distance in a direction perpendicular to it.

In a two-dimensional flow where the velocity is independent of the z -coordinate and has no z -component, the vorticity vector is always parallel to the z -axis, and therefore can be expressed as a scalar field multiplied by a constant unit vector ${\hat {z}}$ :

${\begin{aligned}{\boldsymbol {\omega }}=\nabla \times \mathbf {v} =\left({\frac {\partial v_{y}}{\partial x}}-{\frac {\partial v_{x}}{\partial y}}\right)\mathbf {e} _{z}\,.\end{aligned}}$

The vorticity is also related to the flow's circulation (line integral of the velocity) along a closed path by the (classical) Stokes' theorem. Namely, for any infinitesimal surface element *C* with normal direction $\mathbf {n}$ and area $dA$ , the circulation $d\Gamma$ along the perimeter of C is the dot product ${\boldsymbol {\omega }}\cdot (\mathbf {n} \,dA)$ where ${\boldsymbol {\omega }}$ is the vorticity at the center of C .

Since vorticity is an axial vector, it can be associated with a second-order antisymmetric tensor ${\boldsymbol {\Omega }}$ (the so-called vorticity or rotation tensor), which is said to be the dual of ${\boldsymbol {\omega }}$ . The relation between the two quantities, in index notation, are given by

$\Omega _{ij}={\frac {1}{2}}\varepsilon _{ijk}\omega _{k},\qquad \omega _{i}=\varepsilon _{ijk}\Omega _{jk}$

where $\varepsilon _{ijk}$ is the three-dimensional Levi-Civita tensor. The vorticity tensor is simply the antisymmetric part of the tensor $\nabla \mathbf {v}$ , i.e.,

${\boldsymbol {\Omega }}={\frac {1}{2}}\left[(\nabla \mathbf {v} )^{T}-\nabla \mathbf {v} \right]\quad {\text{or}}\quad \Omega _{ij}={\frac {1}{2}}\left({\frac {\partial v_{j}}{\partial x_{i}}}-{\frac {\partial v_{i}}{\partial x_{j}}}\right).$

## Examples

In a mass of continuum that is rotating like a rigid body, the vorticity is twice the angular velocity vector of that rotation. This is the case, for example, in the central core of a Rankine vortex.

The vorticity may be nonzero even when all particles are flowing along straight and parallel pathlines, if there is shear (that is, if the flow speed varies across streamlines). For example, in the laminar flow within a pipe with constant cross section, all particles travel parallel to the axis of the pipe; but faster near that axis, and practically stationary next to the walls. The vorticity will be zero on the axis, and maximum near the walls, where the shear is largest.

Conversely, a flow may have zero vorticity even though its particles travel along curved trajectories. An example is the ideal irrotational vortex, where most particles rotate about some straight axis, with speed inversely proportional to their distances to that axis. A small parcel of continuum that does not straddle the axis will be rotated in one sense but sheared in the opposite sense, in such a way that their mean angular velocity *about their center of mass* is zero.

| Example flows: |   |   |
|---|---|---|
|   |   |   |
| Rigid-body-like vortex *v* ∝ *r* | Parallel flow with shear | Irrotational vortex *v* ∝ ⁠1/*r*⁠ |
| where v is the velocity of the flow, r is the distance to the center of the vortex and ∝ indicates proportionality. Absolute velocities around the highlighted point: |   |   |
|   |   |   |
| Relative velocities (magnified) around the highlighted point |   |   |
|   |   |   |
| Vorticity ≠ 0 | Vorticity ≠ 0 | Vorticity = 0 |

Another way to visualize vorticity is to imagine that, instantaneously, a tiny part of the continuum becomes solid and the rest of the flow disappears. If that tiny new solid particle is rotating, rather than just moving with the flow, then there is vorticity in the flow. In the figure below, the left subfigure demonstrates no vorticity, and the right subfigure demonstrates existence of vorticity.

## Evolution

The evolution of the vorticity field in time is described by the vorticity equation, which can be derived from the Navier–Stokes equations.

In many real flows where the viscosity can be neglected (more precisely, in flows with high Reynolds number), the vorticity field can be modeled by a collection of discrete vortices, the vorticity being negligible everywhere except in small regions of space surrounding the axes of the vortices. This is true in the case of two-dimensional potential flow (i.e. two-dimensional zero viscosity flow), in which case the flowfield can be modeled as a complex-valued field on the complex plane.

Vorticity is useful for understanding how ideal potential flow solutions can be perturbed to model real flows. In general, the presence of viscosity causes a diffusion of vorticity away from the vortex cores into the general flow field; this flow is accounted for by a diffusion term in the vorticity transport equation.

## Vortex lines and vortex tubes

A **vortex line** or **vorticity line** is a line which is everywhere tangent to the local vorticity vector. Vortex lines are defined by the relation

${\frac {dx}{\omega _{x}}}={\frac {dy}{\omega _{y}}}={\frac {dz}{\omega _{z}}}\,,$

where ${\boldsymbol {\omega }}=(\omega _{x},\omega _{y},\omega _{z})$ is the vorticity vector in Cartesian coordinates.

A **vortex tube** is the surface in the continuum formed by all vortex lines passing through a given (reducible) closed curve in the continuum. The 'strength' of a vortex tube (also called **vortex flux**) is the integral of the vorticity across a cross-section of the tube, and is the same everywhere along the tube (because vorticity has zero divergence). It is a consequence of Helmholtz's theorems (or equivalently, of Kelvin's circulation theorem) that in an inviscid fluid the 'strength' of the vortex tube is also constant with time. Viscous effects introduce frictional losses and time dependence.

In a three-dimensional flow, vorticity (as measured by the volume integral of the square of its magnitude) can be intensified when a vortex line is extended — a phenomenon known as vortex stretching. This phenomenon occurs in the formation of a bathtub vortex in outflowing water, and the build-up of a tornado by rising air currents.

## Vorticity meters

### Rotating-vane vorticity meter

A rotating-vane vorticity meter was invented by Russian hydraulic engineer A. Ya. Milovich (1874–1958). In 1913 he proposed a cork with four blades attached as a device qualitatively showing the magnitude of the vertical projection of the vorticity and demonstrated a motion-picture photography of the float's motion on the water surface in a model of a river bend.

Rotating-vane vorticity meters are commonly shown in educational films on continuum mechanics (famous examples include the NCFMF's "Vorticity" and "Fundamental Principles of Flow" by Iowa Institute of Hydraulic Research).

## Specific sciences

### Aeronautics

In aerodynamics, the lift distribution over a finite wing may be approximated by assuming that each spanwise segment of the wing has a semi-infinite trailing vortex behind it. It is then possible to solve for the strength of the vortices using the criterion that there be no flow induced through the surface of the wing. This procedure is called the vortex panel method of computational fluid dynamics. The strengths of the vortices are then summed to find the total approximate circulation about the wing. According to the Kutta–Joukowski theorem, lift per unit of span is the product of circulation, airspeed, and air density.

### Atmospheric sciences

The **relative vorticity** is the vorticity relative to the Earth induced by the air velocity field. This air velocity field is often modeled as a two-dimensional flow parallel to the ground, so that the relative vorticity vector is generally scalar rotation quantity perpendicular to the ground. Vorticity is positive when – looking down onto the Earth's surface – the wind turns counterclockwise. In the northern hemisphere, positive vorticity is called cyclonic rotation, and negative vorticity is anticyclonic rotation; the nomenclature is reversed in the Southern Hemisphere.

The **absolute vorticity** is computed from the air velocity relative to an inertial frame, and therefore includes a term due to the Earth's rotation, the Coriolis parameter.

The **potential vorticity** is absolute vorticity divided by the vertical spacing between levels of constant (potential) temperature (or entropy). The absolute vorticity of an air mass will change if the air mass is stretched (or compressed) in the vertical direction, but the potential vorticity is conserved in an adiabatic flow. As adiabatic flow predominates in the atmosphere, the potential vorticity is useful as an approximate tracer of air masses in the atmosphere over the timescale of a few days, particularly when viewed on levels of constant entropy.

The barotropic vorticity equation is the simplest way for forecasting the movement of Rossby waves (that is, the troughs and ridges of 500 hPa geopotential height) over a limited amount of time (a few days). In the 1950s, the first successful programs for numerical weather forecasting utilized that equation.

In modern numerical weather forecasting models and general circulation models (GCMs), vorticity may be one of the predicted variables, in which case the corresponding time-dependent equation is a prognostic equation.

Related to the concept of vorticity is the helicity $H(t)$ , defined as

$H(t)=\int _{V}\mathbf {v} \cdot {\boldsymbol {\omega }}\,dV$

where the integral is over a given volume V . In atmospheric science, helicity of the air motion is important in forecasting supercells and the potential for tornadic activity.

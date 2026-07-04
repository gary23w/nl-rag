---
title: "Flow velocity"
source: https://en.wikipedia.org/wiki/Flow_velocity
domain: chapman-jouguet-condition
license: CC-BY-SA-4.0
tags: chapman–jouguet condition
fetched: 2026-07-04
---

# Flow velocity

In continuum mechanics the **flow velocity** in fluid dynamics, also **macroscopic velocity** in statistical mechanics, or **drift velocity** in electromagnetism, is a vector field used to mathematically describe the motion of a continuum. The length of the flow velocity vector is scalar, the ***flow speed***. It is also called **velocity field**; when evaluated along a line, it is called a **velocity profile** (as in, e.g., law of the wall).

## Definition

The flow velocity ***u*** of a fluid is a vector field

$\mathbf {u} =\mathbf {u} (\mathbf {x} ,t),$

which gives the velocity of an *element of fluid* at a position $\mathbf {x} \,$ and time $t.\,$

The flow speed *q* is the length of the flow velocity vector

$q=\|\mathbf {u} \|$

and is a scalar field.

## Uses

The flow velocity of a fluid effectively describes everything about the motion of a fluid. Many physical properties of a fluid can be expressed mathematically in terms of the flow velocity. Some common examples follow:

### Steady flow

The flow of a fluid is said to be *steady* if $\mathbf {u}$ does not vary with time. That is if

${\frac {\partial \mathbf {u} }{\partial t}}=0.$

### Incompressible flow

If a fluid is incompressible the divergence of $\mathbf {u}$ is zero:

$\nabla \cdot \mathbf {u} =0.$

That is, if $\mathbf {u}$ is a solenoidal vector field.

### Irrotational flow

A flow is *irrotational* if the curl of $\mathbf {u}$ is zero:

$\nabla \times \mathbf {u} =0.$

That is, if $\mathbf {u}$ is an irrotational vector field.

A flow in a simply-connected domain which is irrotational can be described as a potential flow, through the use of a velocity potential $\Phi ,$ with $\mathbf {u} =\nabla \Phi .$ If the flow is both irrotational and incompressible, the Laplacian of the velocity potential must be zero: $\Delta \Phi =0.$

### Vorticity

The *vorticity*, $\omega$ , of a flow can be defined in terms of its flow velocity by

$\omega =\nabla \times \mathbf {u} .$

If the vorticity is zero, the flow is irrotational.

## The velocity potential

If an irrotational flow occupies a simply-connected fluid region then there exists a scalar field $\phi$ such that

$\mathbf {u} =\nabla \mathbf {\phi } .$

The scalar field $\phi$ is called the velocity potential for the flow. (See Irrotational vector field.)

## Bulk velocity

In many engineering applications the local flow velocity $\mathbf {u}$ vector field is not known in every point and the only accessible velocity is the **bulk velocity** or **average flow velocity** ${\bar {u}}$ (with the usual dimension of length per time), defined as the quotient between the volume flow rate ${\dot {V}}$ (with dimension of cubed length per time) and the cross sectional area A (with dimension of square length):

${\bar {u}}={\frac {\dot {V}}{A}}$

.

---
title: "Euler's equations (rigid body dynamics)"
source: https://en.wikipedia.org/wiki/Euler's_equations_(rigid_body_dynamics)
domain: rigid-body-dynamics-physics
license: CC-BY-SA-4.0
tags: rigid body dynamics, moment of inertia, gyroscopic precession, rotational motion
fetched: 2026-07-02
---

# Euler's equations (rigid body dynamics)

In classical mechanics, **Euler's rotation equations** are a vectorial quasilinear first-order ordinary differential equation describing the rotation of a rigid body, using a rotating reference frame with angular velocity ω whose axes are fixed to the body. They are named in honour of Leonhard Euler.

In the absence of applied torques, one obtains the Euler top. When the torques are due to gravity, there are special cases when the motion of the top is integrable.

## Formulation

Their general vector form is

$\mathbf {I} {\dot {\boldsymbol {\omega }}}+{\boldsymbol {\omega }}\times \left(\mathbf {I} {\boldsymbol {\omega }}\right)=\mathbf {M} .$

where *M* is the applied torques and *I* is the inertia matrix. The vector ${\dot {\boldsymbol {\omega }}}$ is the angular acceleration. Again, note that all quantities are defined in the rotating reference frame.

In orthogonal principal axes of inertia coordinates the equations become

${\begin{aligned}I_{1}\,{\dot {\omega }}_{1}+(I_{3}-I_{2})\,\omega _{2}\,\omega _{3}&=M_{1}\\I_{2}\,{\dot {\omega }}_{2}+(I_{1}-I_{3})\,\omega _{3}\,\omega _{1}&=M_{2}\\I_{3}\,{\dot {\omega }}_{3}+(I_{2}-I_{1})\,\omega _{1}\,\omega _{2}&=M_{3}\end{aligned}}$

where *Mk* are the components of the applied torques, *Ik* are the principal moments of inertia and ω*k* are the components of the angular velocity.

## Derivation

In an inertial frame of reference (subscripted "in"), Euler's second law states that the time derivative of the angular momentum **L** equals the applied torque:

${\frac {d\mathbf {L} _{\text{in}}}{dt}}=\mathbf {M} _{\text{in}}$

For point particles such that the internal forces are central forces, this may be derived using Newton's second law. For a rigid body, one has the relation between angular momentum and the moment of inertia **I**in given as

$\mathbf {L} _{\text{in}}=\mathbf {I} _{\text{in}}{\boldsymbol {\omega }}$

In the inertial frame, the differential equation is not always helpful in solving for the motion of a general rotating rigid body, as both **I**in and **ω** can change during the motion. One may instead change to a coordinate frame fixed in the rotating body, in which the moment of inertia tensor is constant. Using a reference frame such as that at the center of mass, the frame's position drops out of the equations. In any rotating reference frame, the time derivative must be replaced so that the equation becomes

$\left({\frac {d\mathbf {L} }{dt}}\right)_{\mathrm {rot} }+{\boldsymbol {\omega }}\times \mathbf {L} =\mathbf {M}$

and so the cross product arises, see time derivative in rotating reference frame. The vector components of the torque in the inertial and the rotating frames are related by $\mathbf {M} _{\text{in}}=\mathbf {Q} \mathbf {M} ,$ where $\mathbf {Q}$ is the rotation tensor (not rotation matrix), an orthogonal tensor related to the angular velocity vector by ${\boldsymbol {\omega }}\times {\boldsymbol {u}}={\dot {\mathbf {Q} }}\mathbf {Q} ^{-1}{\boldsymbol {u}}$ for any vector **u**. Now $\mathbf {L} =\mathbf {I} {\boldsymbol {\omega }}$ is substituted and the time derivatives are taken in the rotating frame, while realizing that the particle positions and the inertia tensor does not depend on time. This leads to the general vector form of Euler's equations which are valid in such a frame

$\mathbf {I} {\dot {\boldsymbol {\omega }}}+{\boldsymbol {\omega }}\times \left(\mathbf {I} {\boldsymbol {\omega }}\right)=\mathbf {M} .$

The equations are also derived from Newton's laws in the discussion of the resultant torque.

More generally, by the tensor transform rules, any rank-2 tensor $\mathbf {T}$ has a time-derivative $\mathbf {\dot {T}}$ such that for any vector $\mathbf {u}$ , one has $\mathbf {\dot {T}} \mathbf {u} ={\boldsymbol {\omega }}\times (\mathbf {T} \mathbf {u} )-\mathbf {T} ({\boldsymbol {\omega }}\times \mathbf {u} )$ . This yields the Euler's equations by plugging in ${\frac {d}{dt}}\left(\mathbf {I} {\boldsymbol {\omega }}\right)=\mathbf {M} .$

### Principal axes form

When choosing a frame so that its axes are aligned with the principal axes of the inertia tensor, its component matrix is diagonal, which further simplifies calculations. As described in the moment of inertia article, the angular momentum **L** can then be written

$\mathbf {L} =L_{1}\mathbf {e} _{1}+L_{2}\mathbf {e} _{2}+L_{3}\mathbf {e} _{3}=\sum _{i=1}^{3}I_{i}\omega _{i}\mathbf {e} _{i}$

Also in some frames not tied to the body can it be possible to obtain such simple (diagonal tensor) equations for the rate of change of the angular momentum. Then **ω** must be the angular velocity for rotation of that frames axes instead of the rotation of the body. It is however still required that the chosen axes are still principal axes of inertia. The resulting form of the Euler rotation equations is useful for rotation-symmetric objects that allow some of the principal axes of rotation to be chosen freely.

## Special case solutions

### Torque-free precessions

Torque-free precessions are non-trivial solution for the situation where the torque on the right hand side is zero. When **I** is not constant in the external reference frame (i.e. the body is moving and its inertia tensor is not constantly diagonal) then **I** cannot be pulled through the derivative operator acting on **L**. In this case **I**(*t*) and **ω**(*t*) do change together in such a way that the derivative of their product is still zero. This motion can be visualized by Poinsot's construction.

## Generalized Euler equations

The Euler equations can be generalized to any simple Lie algebra. The original Euler equations come from fixing the Lie algebra to be ${\mathfrak {so}}(3)$ , with generators ${t_{1},t_{2},t_{3}}$ satisfying the relation $[t_{a},t_{b}]=\epsilon _{abc}t_{c}$ . Then if ${\boldsymbol {\omega }}(t)=\sum _{a}\omega _{a}(t)t_{a}$ (where t is a time coordinate, not to be confused with basis vectors $t_{a}$ ) is an ${\mathfrak {so}}(3)$ -valued function of time, and $\mathbf {I} =\mathrm {diag} (I_{1},I_{2},I_{3})$ (with respect to the Lie algebra basis), then the (untorqued) original Euler equations can be written $\mathbf {I} {\dot {\boldsymbol {\omega }}}=[\mathbf {I} {\boldsymbol {\omega }},{\boldsymbol {\omega }}].$ To define $\mathbf {I}$ in a basis-independent way, it must be a self-adjoint map on the Lie algebra ${\mathfrak {g}}$ with respect to the invariant bilinear form on ${\mathfrak {g}}$ . This expression generalizes readily to an arbitrary simple Lie algebra, say in the standard classification of simple Lie algebras.

The Euler equations for rigid body dynamics can be derived from the Euler–Arnold equation, a class of partial differential equations (PDEs) that describe the geodesic flow on infinite-dimensional Lie groups equipped with right-invariant metrics. Also, the Euler equations of fluid dynamics can be derived from the same Euler-Arnold equation.

This can also be viewed as a Lax pair formulation of the generalized Euler equations, suggesting their integrability.

---
title: "Angular displacement"
source: https://en.wikipedia.org/wiki/Angular_displacement
domain: angular-displacement
license: CC-BY-SA-4.0
tags: angular displacement
fetched: 2026-07-05
---

# Angular displacement

The **angular displacement** (symbol *θ*, *ϑ*, or *φ*) – also called **angle of rotation**, **rotational displacement**, or **rotary displacement** – of a physical body is the angle (with the unit radian, degree, turn, etc.) through which the body has rotated (revolved or spun) around a centre of rotation or axis of rotation. Angular displacement may be signed, indicating the direction of rotation (e.g., clockwise versus counterclockwise); it may also be greater (in absolute value) than a full turn if the rotation was.

## Context

When a body with orientation rotates about an axis, the motion of the orientation must be taken into account, such as how the yaw, pitch and roll of a plane all result in different, new orientations. Each part of the object experiences circular motion as it undergoes the rotation.

The simplest case is that of the rigid body in which the object itself does not change. Precisely, this is when the distances between all the particles remain constant throughout the body's motion, as opposed to it having internally moving parts parts or accumulating or releasing parts of itself. Many real bodies are approximated as rigid bodies, such as airplanes in flight simulations.

## Example

In the example illustrated to the left (or above in some mobile versions), a particle or body P is at a fixed distance *r* from the origin, *O*, rotating counterclockwise. It becomes important to then represent the position of particle P in terms of its polar coordinates (*r*, *θ*). In this particular example, the value of *θ* is changing, while the value of the radius remains the same. (In rectangular coordinates (*x*, *y*) both *x* and *y* vary with time.) As the particle moves along the circle, it travels an arc length *s*, which becomes related to the angular position through the relationship:

$s=r\theta .$

## Definition and units

Angular displacement may be expressed with the unit radian or degree. Using the radian provides a very simple relationship between distance traveled around the circle (*circular arc length*) and the distance *r* from the centre (*radius*):

$\theta ={\frac {s}{r}}\mathrm {rad}$

For example, if a body rotates 360° around a circle of radius *r*, the angular displacement is given by the distance traveled around the circumference - which is 2π*r* - divided by the radius: $\theta ={\frac {2\pi r}{r}}$ which easily simplifies to: $\theta =2\pi$ . Therefore, 1 revolution is $2\pi$ radians.

The above definition is part of the International System of Quantities (ISQ), formalized in the international standard ISO 80000-3 (Space and time), and adopted in the International System of Units (SI).

Angular displacement may be signed, indicating the sense of rotation (e.g., clockwise); it may also be greater (in absolute value) than a full turn. In the ISQ/SI, angular displacement is used to define the *number of revolutions*, *N* = θ/(2π rad), a ratio and hence a quantity of dimension one.

## In three dimensions

In three dimensions, angular displacement is an entity with a direction and a magnitude. The direction specifies the axis of rotation, which always exists by virtue of the Euler's rotation theorem; the magnitude specifies the rotation in radians about that axis (using the right-hand rule to determine direction). This entity is called an axis-angle.

Despite having direction and magnitude, angular displacement is not a vector because it does not obey the commutative law for addition. Nevertheless, when dealing with infinitesimal rotations, second order infinitesimals can be discarded and in this case commutativity appears.

### Rotation matrices

Several ways to describe rotations exist, like rotation matrices or Euler angles. See charts on SO(3) for others.

Given that any frame in the space can be described by a rotation matrix, the displacement among them can also be described by a rotation matrix. Being $A_{0}$ and $A_{f}$ two matrices, the angular displacement matrix between them can be obtained as ⁠ $\Delta A=A_{f}A_{0}^{-1}$ ⁠. When this product is performed having a very small difference between both frames we will obtain a matrix close to the identity.

In the limit, we will have an infinitesimal rotation matrix.

### Infinitesimal rotation matrices

An infinitesimal rotation matrix or differential rotation matrix is a matrix representing an infinitely small rotation.

While a rotation matrix is an orthogonal matrix $R^{\mathsf {T}}=R^{-1}$ representing an element of $\mathrm {SO} (n)$ (the special orthogonal group), the differential of a rotation is a skew-symmetric matrix $A^{\mathsf {T}}=-A$ in the tangent space ${\mathfrak {so}}(n)$ (the special orthogonal Lie algebra), which is not itself a rotation matrix.

An infinitesimal rotation matrix has the form

$I+d\theta \,A,$

where I is the identity matrix, $d\theta$ is vanishingly small, and ⁠ $A\in {\mathfrak {so}}(n)$ ⁠.

For example, if ⁠ $A=L_{x}$ ⁠, representing an infinitesimal three-dimensional rotation about the x-axis, a basis element of ⁠ ${\mathfrak {so}}(3)$ ⁠, then

$L_{x}={\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix}},$

and

$I+d\theta L_{x}={\begin{bmatrix}1&0&0\\0&1&-d\theta \\0&d\theta &1\end{bmatrix}}.$

The computation rules for infinitesimal rotation matrices are the usual ones except that infinitesimals of second order are dropped. With these rules, these matrices do not satisfy all the same properties as ordinary finite rotation matrices under the usual treatment of infinitesimals. It turns out that *the order in which infinitesimal rotations are applied is irrelevant*.

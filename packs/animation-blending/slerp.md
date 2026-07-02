---
title: "Spherical linear interpolation"
source: https://en.wikipedia.org/wiki/Slerp
domain: animation-blending
license: CC-BY-SA-4.0
tags: animation blending, animation blend tree, keyframe interpolation, spherical linear interpolation
fetched: 2026-07-02
---

# Spherical linear interpolation

(Redirected from

Slerp

)

In geometry, **spherical linear interpolation**, commonly abbreviated **slerp**, is a function which interpolates between two points on a sphere, such that spherical distance from the starting point varies uniformly with the interpolation parameter. In computer graphics, it was popularized by Ken Shoemake for animating three-dimensional rotations, represented as quaternions on an abstract 3-sphere. When the interpolation parameter represents time, spherical linear interpolation results in a constant-speed motion along a great circle arc between the endpoints or a smooth and uniform variation between two three-dimensional rotations.

## Geometric slerp

Slerp has a geometric formula independent of quaternions, and independent of the dimension of the space in which the arc is embedded. This formula, a symmetric weighted sum credited to Glenn Davis, is based on the fact that any point on the curve must be a linear combination of the ends. Let *p*0 and *p*1 be the first and last points of the arc, and let *t* be the parameter, 0 ≤ *t* ≤ 1. Compute Ω as the angle subtended by the arc, so that cos Ω = *p*0 ⋅ *p*1, the *n*-dimensional dot product of the unit vectors from the origin to the ends. The geometric formula is then

$\operatorname {slerp} (p_{0},p_{1};t)={\frac {\sin {[(1-t)\Omega }]}{\sin \Omega }}p_{0}+{\frac {\sin[t\Omega ]}{\sin \Omega }}p_{1}.$

The symmetry lies in the fact that slerp(*p*0, *p*1; *t*) = slerp(*p*1, *p*0; 1 − *t*). In the limit as Ω → 0, this formula reduces to the corresponding symmetric formula for linear interpolation,

$\operatorname {slerp} (p_{0},p_{1};t)=(1-t)p_{0}+tp_{1}.$

A slerp path is, in fact, the spherical geometry equivalent of a path along a line segment in the plane; a great circle is a spherical geodesic.

More familiar than the general slerp formula is the case when the end vectors are perpendicular, in which case the formula is *p*0cos *θ* + *p*1sin *θ*. Letting *θ* = *t*π/2, and applying the trigonometric identity cos *θ* = sin(π/2 − *θ*), this becomes the slerp formula. The factor of 1/sin Ω in the general formula is a normalization, since a vector *p*1 at an angle of Ω to *p*0 projects onto the perpendicular ⊥*p*0 with a length of only sin Ω.

Some special cases of slerp admit more efficient calculation. When a circular arc is to be drawn into a raster image, the preferred method is some variation of Bresenham's circle algorithm. Evaluation at the special parameter values 0 and 1 trivially yields *p*0 and *p*1, respectively; and bisection, evaluation at ⁠1/2⁠, simplifies to (*p*0 + *p*1)/2, normalized. Another special case, common in animation, is evaluation with fixed ends and equal parametric steps. If *p**k*−1 and *p**k* are two consecutive values, and if *c* is twice their dot product (constant for all steps), then the next value, *p**k*+1, is the reflection *p**k*+1 = *cp**k* − *p**k*−1.

## Quaternion slerp

When slerp is applied to unit quaternions, the quaternion path maps to a path through 3D rotations in a standard way. The effect is a rotation with uniform angular velocity around a fixed rotation axis. When the initial end point is the identity quaternion, slerp gives a segment of a one-parameter subgroup of both the Lie group of 3D rotations, SO(3), and its universal covering group of unit quaternions, *S*3. Slerp gives a straightest and shortest path between its quaternion end points, and maps to a rotation through an angle of 2Ω. However, because the covering is double (*q* and −*q* map to the same rotation), the rotation path may turn either the "short way" (less than 180°) or the "long way" (more than 180°). Long paths can be prevented by negating one end if the dot product, cos Ω, is negative, thus ensuring that −90° ≤ Ω ≤ 90°.

Slerp also has expressions in terms of quaternion algebra, all using exponentiation. Real powers of a quaternion are defined in terms of the quaternion exponential function, written as *e**q* and given by the power series equally familiar from calculus, complex analysis and matrix algebra:

$e^{q}=1+q+{\frac {q^{2}}{2}}+{\frac {q^{3}}{6}}+\cdots +{\frac {q^{n}}{n!}}+\cdots .$

Writing a unit quaternion *q* in versor form, cos Ω + **v** sin Ω, with **v** a unit 3-vector, and noting that the quaternion square **v**2 equals −1 (implying a quaternion version of Euler's formula), we have *e* **v**Ω = *q*, and *q**t* = cos *t*Ω + **v** sin *t*Ω. The identification of interest is *q* = *q*1*q*0−1, so that the real part of *q* is cos Ω, the same as the geometric dot product used above. Here are four equivalent quaternion expressions for slerp.

${\begin{aligned}\operatorname {slerp} (q_{0},q_{1},t)&=q_{0}(q_{0}^{-1}q_{1})^{t}\\[6pt]&=q_{1}(q_{1}^{-1}q_{0})^{1-t}\\[6pt]&=(q_{0}q_{1}^{-1})^{1-t}q_{1}\\[6pt]&=(q_{1}q_{0}^{-1})^{t}q_{0}\end{aligned}}$

The derivative of slerp(*q*0, *q*1; *t*) with respect to *t*, assuming the ends are fixed, is log(*q*1*q*0−1) times the function value, where the quaternion natural logarithm in this case yields half the 3D angular velocity vector. The initial tangent vector is parallel transported to each tangent along the curve; thus the curve is, indeed, a geodesic.

In the tangent space at any point on a quaternion slerp curve, the inverse of the exponential map transforms the curve into a line segment. Slerp curves not extending through a point fail to transform into lines in that point's tangent space.

Quaternion slerps are commonly used to construct smooth animation curves by mimicking affine constructions like the de Casteljau algorithm for Bézier curves. Since the sphere is not an affine space, familiar properties of affine constructions may fail, though the constructed curves may otherwise be entirely satisfactory. For example, the de Casteljau algorithm may be used to split a curve in affine space; this does not work on a sphere.

The two-valued slerp can be extended to interpolate among many unit quaternions, but the extension loses the fixed execution-time of the slerp algorithm.

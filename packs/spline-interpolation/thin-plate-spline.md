---
title: "Thin plate spline"
source: https://en.wikipedia.org/wiki/Thin_plate_spline
domain: spline-interpolation
license: CC-BY-SA-4.0
tags: spline interpolation, cubic hermite spline, smoothing spline, thin plate spline
fetched: 2026-07-02
---

# Thin plate spline

**Thin plate splines** (**TPS**) are a spline-based technique for data interpolation and smoothing. They were introduced to geometric design by Duchon. They are an important special case of a polyharmonic spline. Robust Point Matching (RPM) is a common extension and shortly known as the TPS-RPM algorithm.

## Physical analogy

The name *thin plate spline* refers to a physical analogy involving the bending of a plate or thin sheet of metal. Just as the metal has rigidity, the TPS fit resists bending also, implying a penalty involving the smoothness of the fitted surface. In the physical setting, the deflection is in the z direction, orthogonal to the plane. In order to apply this idea to the problem of coordinate transformation, one interprets the lifting of the plate as a displacement of the x or y coordinates within the plane. In 2D cases, given a set of K corresponding control points (knots), the TPS warp is described by $2(K+3)$ parameters which include 6 global affine motion parameters and $2K$ coefficients for correspondences of the control points. These parameters are computed by solving a linear system, in other words, TPS has a closed-form solution.

## Smoothness measure

The TPS arises from consideration of the integral of the square of the second derivative—this forms its smoothness measure. In the case where x is two dimensional, for interpolation, the TPS fits a mapping function $f(x)$ between corresponding point-sets $\{y_{i}\}$ and $\{x_{i}\}$ that minimizes the following energy function:

$E_{\mathrm {tps} }(f)=\sum _{i=1}^{K}\|y_{i}-f(x_{i})\|^{2}$

The smoothing variant, correspondingly, uses a tuning parameter $\lambda$ to control the rigidity of the deformation, balancing the aforementioned criterion with the measure of goodness of fit, thus minimizing:

$E_{\mathrm {tps} ,\mathrm {smooth} }(f)=\sum _{i=1}^{K}\|y_{i}-f(x_{i})\|^{2}+\lambda \iint \left[\left({\frac {\partial ^{2}f}{\partial x_{1}^{2}}}\right)^{2}+2\left({\frac {\partial ^{2}f}{\partial x_{1}\partial x_{2}}}\right)^{2}+\left({\frac {\partial ^{2}f}{\partial x_{2}^{2}}}\right)^{2}\right]{\textrm {d}}x_{1}\,{\textrm {d}}x_{2}$

For this variational problem, it can be shown that there exists a unique minimizer f . The finite element discretization of this variational problem, the method of elastic maps, is used for data mining and nonlinear dimensionality reduction. In simple words, "the first term is defined as the error measurement term and the second regularisation term is a penalty on the smoothness of f ." It is in a general case needed to make the mapping unique.

## Radial basis function

The thin plate spline has a natural representation in terms of radial basis functions. Given a set of control points $\{c_{i},i=1,2,\ldots ,K\}$ , a radial basis function defines a spatial mapping which maps any location x in space to a new location $f(x)$ , represented by

$f(x)=\sum _{i=1}^{K}w_{i}\varphi (\left\|x-c_{i}\right\|)$

where $\left\|\cdot \right\|$ denotes the usual Euclidean norm and $\{w_{i}\}$ is a set of mapping coefficients. The TPS corresponds to the radial basis kernel $\varphi (r)=r^{2}\log r$ .

### Spline

Suppose the points are in 2 dimensions ( $D=2$ ). One can use *homogeneous coordinates* for the point-set where a point $y_{i}$ is represented as a vector $(1,y_{ix},y_{iy})$ . The unique minimizer f is parameterized by $\alpha$ which consists of two matrices d and c ( $\alpha =\{d,c\}$ ).

$f_{tps}(z,\alpha )=f_{tps}(z,d,c)=z\cdot d+\phi (z)\cdot c=z\cdot d+\sum _{i=1}^{K}\phi _{i}(z)c_{i}$

where d is a $(D+1)\times (D+1)$ matrix representing the affine transformation (hence z is a $1\times (D+1)$ vector) and c is a $K\times (D+1)$ warping coefficient matrix representing the non-affine deformation. The kernel function $\phi (z)$ is a $1\times K$ vector for each point z , where each entry $\phi _{i}(z)=\|z-x_{i}\|^{2}\log \|z-x_{i}\|$ . Note that for TPS, the control points $\{c_{i}\}$ are chosen to be the same as the set of points to be warped $\{x_{i}\}$ , so we already use $\{x_{i}\}$ in the place of the control points.

If one substitutes the solution for f , $E_{tps}$ becomes:

$E_{tps}(d,c)=\|Y-Xd-\Phi c\|^{2}+\lambda c^{T}\Phi c$

where Y and X are just concatenated versions of the point coordinates $y_{i}$ and $x_{i}$ , and $\Phi$ is a $(K\times K)$ matrix formed from the $\phi (\|x_{i}-x_{j}\|)$ . Each row of each newly formed matrix comes from one of the original vectors. The matrix $\Phi$ represents the TPS kernel. Loosely speaking, the TPS kernel contains the information about the point-set's internal structural relationships. When it is combined with the warping coefficients c , a non-rigid warping is generated.

A nice property of the TPS is that it can always be decomposed into a global affine and a local non-affine component. Consequently, the TPS smoothness term is solely dependent on the non-affine components. This is a desirable property, especially when compared to other splines, since the global pose parameters included in the affine transformation are not penalized.

## Applications

TPS has been widely used as the non-rigid transformation model in image alignment and shape matching. An additional application is the analysis and comparisons of archaeological findings in 3D and was implemented for triangular meshes in the GigaMesh Software Framework.

The thin plate spline has a number of properties which have contributed to its popularity:

1. It produces smooth surfaces, which are infinitely differentiable.
2. There are no free parameters that need manual tuning.
3. It has closed-form solutions for both warping and parameter estimation.
4. There is a physical explanation for its energy function.

However, note that splines already in one dimension can cause severe "overshoots". In 2D such effects can be much more critical, because TPS are not objective.

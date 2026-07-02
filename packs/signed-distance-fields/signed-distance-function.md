---
title: "Signed distance function"
source: https://en.wikipedia.org/wiki/Signed_distance_function
domain: signed-distance-fields
license: CC-BY-SA-4.0
tags: signed distance field, sdf raymarching, distance transform rendering, sdf isosurface
fetched: 2026-07-02
---

# Signed distance function

In mathematics and its applications, the **signed distance function** or **signed distance field** (**SDF**) is the orthogonal distance of a given point *x* to the boundary of a set Ω in a metric space (such as the surface of a geometric shape), with the sign determined by whether or not *x* is in the interior of Ω. The function has positive values at points *x* inside Ω, it decreases in value as *x* approaches the boundary of Ω where the signed distance function is zero, and it takes negative values outside of Ω. However, the alternative convention is also sometimes taken instead (i.e., negative inside Ω and positive outside). The concept also sometimes goes by the name **oriented distance function/field**.

## Definition

Let Ω be a subset of a metric space *X* with metric *d*, and $\partial \Omega$ be its boundary. The distance between a point x of *X* and the subset $\partial \Omega$ of X is defined as usual as

$d(x,\partial \Omega )=\inf _{y\in \partial \Omega }d(x,y),$

where $\inf$ denotes the infimum.

The *signed distance function* from a point x of X to $\Omega$ is defined by

$f(x)={\begin{cases}d(x,\partial \Omega )&{\text{if }}x\in \Omega \\-d(x,\partial \Omega )&{\text{if }}\,x\notin \Omega \\0&{\text{if }}\,x\in \partial \Omega .\end{cases}}$

## Properties in Euclidean space

If Ω is a subset of the Euclidean space **R***n* with piecewise smooth boundary, then the signed distance function is differentiable almost everywhere, and its gradient satisfies the eikonal equation

$|\nabla f|=1.$

If the boundary of Ω is *C**k* for *k* ≥ 2 (see Differentiability classes) then *d* is *C**k* on points sufficiently close to the boundary of Ω. In particular, ***on*** the boundary *f* satisfies

$\nabla f(x)=N(x),$

where *N* is the inward normal vector field. The signed distance function is thus a differentiable extension of the normal vector field. In particular, the Hessian of the signed distance function on the boundary of Ω gives the Weingarten map.

If, further, Γ is a region sufficiently close to the boundary of Ω that *f* is twice continuously differentiable on it, then there is an explicit formula involving the Weingarten map *W**x* for the Jacobian of changing variables in terms of the signed distance function and nearest boundary point. Specifically, if *T*(*∂*Ω, *μ*) is the set of points within distance *μ* of the boundary of Ω (i.e. the tubular neighbourhood of radius *μ*), and *g* is an absolutely integrable function on Γ, then

$\int _{T(\partial \Omega ,\mu )}g(x)\,dx=\int _{\partial \Omega }\int _{-\mu }^{\mu }g(u+\lambda N(u))\,\det(I-\lambda W_{u})\,d\lambda \,dS_{u},$

where det denotes the determinant and *dS**u* indicates that we are taking the surface integral.

## Algorithms

Algorithms for calculating the signed distance function include the efficient fast marching method, fast sweeping method and the more general level-set method.

For voxel rendering, a fast algorithm for calculating the SDF in taxicab geometry uses summed-area tables.

## Applications

Signed distance functions are applied, for example, in real-time rendering, for instance the method of SDF ray marching, and computer vision.

SDF has been used to describe object geometry in real-time rendering, usually in a raymarching context, starting in the mid 2000s. By 2007, Valve was using SDFs to render large pixel-size (or high DPI) smooth fonts with GPU acceleration in its games. Valve's method is not perfect as it runs in raster space in order to avoid the computational complexity of solving the problem in the (continuous) vector space. The rendered text often loses sharp corners. In 2014, an improved method was presented by Behdad Esfahbod. Behdad's GLyphy approximates the font's Bézier curves with arc splines, accelerated by grid-based discretization techniques (which culls too-far-away points) to run in real time.

A modified version of SDF was introduced as a loss function to minimise the error in interpenetration of pixels while rendering multiple objects. In particular, for any pixel that does not belong to an object, if it lies outside the object in rendition, no penalty is imposed; if it does, a positive value proportional to its distance inside the object is imposed.

$f(x)={\begin{cases}0&{\text{if }}\,x\in \Omega ^{c}\\d(x,\partial \Omega )&{\text{if }}\,x\in \Omega \end{cases}}$

In 2020, the FOSS game engine Godot 4.0 received SDF-based real-time global illumination (SDFGI), that became a compromise between more realistic voxel-based GI and baked GI. Its core advantage is that it can be applied to infinite space, which allows developers to use it for open-world games.

In 2023, the authors of the Zed text editor announced a GPUI framework that draws all UI elements using the GPU at 120 fps. The work makes use of Inigo Quilez's list of geometric primitives in SDF, Figma co-founder Evan Wallace's Gaussian blur in SDF, and a new rounded rectangle SDF.

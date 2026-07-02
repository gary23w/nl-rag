---
title: "Control point (mathematics)"
source: https://en.wikipedia.org/wiki/Control_point_(mathematics)
domain: nurbs-surfaces
license: CC-BY-SA-4.0
tags: nurbs surface, non-uniform rational b-spline, nurbs control point, b-spline surface modeling
fetched: 2026-07-02
---

# Control point (mathematics)

In computer-aided geometric design a **control point** is a member of a set of points used to determine the shape of a spline curve or, more generally, a surface or higher-dimensional object.

For Bézier curves, it has become customary to refer to the ⁠ d ⁠-vectors ⁠ $\mathbf {p} _{i}$ ⁠ in a parametric representation ${\textstyle \sum _{i}\mathbf {p} _{i}\phi _{i}}$ of a curve or surface in ⁠ d ⁠-space as **control points**, while the scalar-valued functions ⁠ $\phi _{i}$ ⁠, defined over the relevant parameter domain, are the corresponding *weight* or *blending functions*. Some would reasonably insist, in order to give intuitive geometric meaning to the word "control", that the blending functions form a partition of unity, i.e., that the ⁠ $\phi _{i}$ ⁠ are nonnegative and sum to one. This property implies that the curve lies within the convex hull of its control points. This is the case for Bézier's representation of a polynomial curve as well as for the B-spline representation of a spline curve or tensor-product spline surface.

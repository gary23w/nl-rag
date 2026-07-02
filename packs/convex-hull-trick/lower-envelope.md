---
title: "Lower envelope"
source: https://en.wikipedia.org/wiki/Lower_envelope
domain: convex-hull-trick
license: CC-BY-SA-4.0
tags: convex hull trick, dynamic programming optimization, lower envelope of lines, monotone stack
fetched: 2026-07-02
---

# Lower envelope

In mathematics, the **lower envelope** or **pointwise minimum** of a finite set of functions is the pointwise minimum of the functions, the function whose value at every point is the minimum of the values of the functions in the given set. The concept of a lower envelope can also be extended to partial functions by taking the minimum only among functions that have values at the point. The **upper envelope** or **pointwise maximum** is defined symmetrically. For an infinite set of functions, the same notions may be defined using the infimum in place of the minimum, and the supremum in place of the maximum.

For continuous functions from a given class, the lower or upper envelope is a piecewise function whose pieces are from the same class. For functions of a single real variable whose graphs have a bounded number of intersection points, the complexity of the lower or upper envelope can be bounded using Davenport–Schinzel sequences, and these envelopes can be computed efficiently by a divide-and-conquer algorithm that computes and then merges the envelopes of subsets of the functions.

For convex functions or quasiconvex functions, the upper envelope is again convex or quasiconvex. The lower envelope is not, but can be replaced by the lower convex envelope to obtain an operation analogous to the lower envelope that maintains convexity. The upper and lower envelopes of Lipschitz functions preserve the property of being Lipschitz. However, the lower and upper envelope operations do not necessarily preserve the property of being a continuous function.

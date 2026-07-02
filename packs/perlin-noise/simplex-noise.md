---
title: "Simplex noise"
source: https://en.wikipedia.org/wiki/Simplex_noise
domain: perlin-noise
license: CC-BY-SA-4.0
tags: perlin noise, simplex noise, gradient noise, value noise
fetched: 2026-07-02
---

# Simplex noise

**Simplex noise** is the result of an *n*-dimensional noise function comparable to Perlin noise ("classic" noise) but with fewer directional artifacts, in higher dimensions, and a lower computational overhead. Ken Perlin designed the algorithm in 2001 to address the limitations of his classic noise function, especially in higher dimensions.

The advantages of simplex noise over Perlin noise:

- Simplex noise has lower computational complexity and requires fewer multiplications.
- Simplex noise scales to higher dimensions (4D, 5D) with much less computational cost: the complexity is $O(n^{2})$ for n dimensions instead of the $O(n\,2^{n})$ of classic noise.
- Simplex noise has no noticeable directional artifacts (is visually isotropic), though noise generated for different dimensions is visually distinct (e.g. 2D noise has a different look than 2D slices of 3D noise, and it looks increasingly worse for higher dimensions).
- Simplex noise has a well-defined and continuous gradient (almost) everywhere that can be computed quite cheaply.
- Simplex noise is easy to implement in hardware.

Whereas Perlin noise interpolates between the gradients at the surrounding hypergrid end points (i.e., northeast, northwest, southeast and southwest in 2D), simplex noise divides the space into simplices (i.e., n -dimensional triangles). This reduces the number of data points. While a hypercube in n dimensions has $2^{n}$ corners, a simplex in n dimensions has only $n+1$ corners. The triangles are equilateral in 2D, but in higher dimensions the simplices are only approximately regular. For example, the tiling in the 3D case of the function is an orientation of the tetragonal disphenoid honeycomb.

Simplex noise is useful for computer graphics applications, where noise is usually computed over 2, 3, 4, or possibly 5 dimensions. For higher dimensions, *n*-spheres around *n*-simplex corners are not densely enough packed, reducing the support of the function and making it zero in large portions of space.

## Algorithm detail

Simplex noise is most commonly implemented as a two-, three-, or four-dimensional function, but can be defined for any number of dimensions. An implementation typically involves four steps: coordinate skewing, simplicial subdivision, gradient selection, and kernel summation.

### Coordinate skewing

An input coordinate is transformed using the formula

$x'=x+(x+y+\cdots )\cdot F,$

$y'=y+(x+y+\cdots )\cdot F,$

$\cdots ,$

where

$F={\frac {{\sqrt {n+1}}-1}{n}}.$

This has the effect of placing the coordinate on an *A* n* lattice, which is essentially the vertex arrangement of a hypercubic honeycomb that has been squashed along its main diagonal until the distance between the points (0, 0, ..., 0) and (1, 1, ..., 1) becomes equal to the distance between the points (0, 0, ..., 0) and (1, 0, ..., 0).

The resulting coordinate (*x*', *y*', ...) is then used in order to determine which skewed unit hypercube cell the input point lies in, (*xb*' = floor(*x*'), *yb*' = floor(*y*'), ...), and its internal coordinates (*xi*' = *x*' − *xb*', *yi*' = *y*' − *yb*', ...).

### Simplicial subdivision

Once the above is determined, the values of the internal coordinate (*xi*', *yi*', ...) are sorted in decreasing order, to determine which skewed Schläfli orthoscheme simplex the point lies in. Then the resulting simplex is composed of the vertices corresponding to an ordered edge traversal from (0, 0, ..., 0) to (1, 1, ..., 1), of which there are *n*! possibilities, each of which corresponds to a single permutation of the coordinate. In other words, start with the zero coordinate and successively add-ones starting in the value corresponding to the largest internal coordinate's value, ending with the smallest.

For example, the point (0.4, 0.5, 0.3) would lie inside the simplex with vertices (0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1). The *yi*' coordinate is the largest, so it is added first. It is then followed by the *xi*' coordinate, and finally *zi*'.

### Gradient selection

Each simplex vertex is added back to the skewed hypercube's base coordinate and hashed into a pseudo-random gradient direction. The hash can be implemented in numerous ways, though most often uses a permutation table or a bit manipulation scheme.

Care should be taken in the selection of the set of gradients to include, to keep directional artifacts to a minimum.

### Kernel summation

The contribution from each of the *n* + 1 vertices of the simplex is factored in by a summation of radially symmetric kernels centered around each vertex. First, the unskewed coordinate of each of the vertices is determined using the inverse formula

$x=x'-(x'+y'+\cdots )\cdot G,$

$y=y'-(x'+y'+\cdots )\cdot G,$

$\cdots ,$

where

$G={\frac {1-1/{\sqrt {n+1}}}{n}}.$

This point is subtracted from the input coordinate to obtain the unskewed displacement vector. This unskewed displacement vector is used for two purposes:

- To compute the extrapolated gradient value using a dot product.
- To determine *d*2, the squared distance to the point.

From there, each vertex's summed kernel contribution is determined using the expression

${\big (}\max(0,r^{2}-d^{2}){\big )}^{4}\cdot {\big (}\langle \Delta x,\Delta y,\dots \rangle \cdot \langle \operatorname {grad} x,\operatorname {grad} y,\dots \rangle {\big )},$

where *r*2 is usually set to either 0.5 or 0.6: the value 0.5 ensures no discontinuities, whereas 0.6 may increase visual quality in applications for which the discontinuities are not noticeable; 0.6 was used in Ken Perlin's original reference implementation.

## Legal status

Uses of implementations in *3D and higher* for *textured image synthesis* were covered by U.S. patent 6,867,776, if the algorithm were implemented using the specific techniques described in any of the patent claims, which expired on January 8, 2022.

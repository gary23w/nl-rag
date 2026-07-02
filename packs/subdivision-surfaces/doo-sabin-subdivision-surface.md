---
title: "Doo–Sabin subdivision surface"
source: https://en.wikipedia.org/wiki/Doo%E2%80%93Sabin_subdivision_surface
domain: subdivision-surfaces
license: CC-BY-SA-4.0
tags: subdivision surface, catmull clark subdivision, loop subdivision surface, doo sabin subdivision
fetched: 2026-07-02
---

# Doo–Sabin subdivision surface

In 3D computer graphics, a **Doo–Sabin subdivision surface** is a type of subdivision surface based on a generalization of *bi-quadratic* uniform B-splines, whereas Catmull-Clark was based on generalized *bi-cubic* uniform B-splines. The subdivision refinement algorithm was developed in 1978 by Daniel Doo and Malcolm Sabin.

The Doo-Sabin process generates one new face at each original vertex, ⁠ n ⁠ new faces along each original edge, and ⁠ $n^{2}$ ⁠ new faces at each original face. A primary characteristic of the Doo–Sabin subdivision method is the creation of four faces and four edges (*valence* 4) around every new vertex in the refined mesh. A drawback is that the faces created at the original vertices may be triangles or n-gons that are not necessarily coplanar.

## Evaluation

Doo–Sabin surfaces are defined recursively. Like all subdivision procedures, each refinement iteration, following the procedure given, replaces the current mesh with a "smoother", more refined mesh. In subdivision terminology, Doo-Sabin is a dual quadrilateral scheme: unlike Catmull-Clark, its topological refinement step splits vertices rather than faces. After many iterations, the surface will gradually converge onto a smooth limit surface. Later work has noted that classical Doo-Sabin subdivision can exhibit shape defects near extraordinary points; for convex input meshes these include flatness at the extraordinary point and nearby oscillation.

Just as for Catmull–Clark surfaces, Doo–Sabin limit surfaces can also be *evaluated directly* without any recursive refinement, by means of the technique of Jos Stam. The solution is, however, not as computationally efficient as for Catmull–Clark surfaces because the Doo–Sabin subdivision matrices are not (in general) diagonalizable.

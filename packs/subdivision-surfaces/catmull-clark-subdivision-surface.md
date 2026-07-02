---
title: "Catmull–Clark subdivision surface"
source: https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface
domain: subdivision-surfaces
license: CC-BY-SA-4.0
tags: subdivision surface, catmull clark subdivision, loop subdivision surface, doo sabin subdivision
fetched: 2026-07-02
---

# Catmull–Clark subdivision surface

The **Catmull–Clark** algorithm is a technique used in 3D computer graphics to create curved surfaces by using subdivision surface modeling. It was devised by Edwin Catmull and Jim Clark in 1978 as a generalization of bi-cubic *uniform* B-spline surfaces to arbitrary topology.

In 2005/06, Edwin Catmull, together with Tony DeRose and Jos Stam, received an Academy Award for Technical Achievement for their invention and application of subdivision surfaces. DeRose wrote about "efficient, fair interpolation" and character animation. Stam described a technique for a direct evaluation of the limit surface without recursion.

## Recursive evaluation

Catmull–Clark surfaces are defined recursively, using the following *refinement scheme.*

Start with a mesh of an arbitrary polyhedron. All the vertices in this mesh shall be called *original points*.

- For each face, add a *face point*
  - Set each face point to be the average of all *original points* for the respective face
- For each edge, add an *edge point*.
  - Set each edge point to be the average of the two neighbouring face points *(A,F)* and the two endpoints of the edge *(M,E)* ${\frac {A+F+M+E}{4}}$
- For each *original point* (*P)*, take the average (*F)* of all *n* (recently created) face points for faces touching *P*, and take the average *(R)* of all *n* edge midpoints for original edges touching *P*, where each edge midpoint is the average of its two endpoint vertices (not to be confused with new *edge points* above). (Note that from the perspective of a vertex *P*, the number of edges neighboring *P* is also the number of adjacent faces, hence *n*)
  - Move each *original point* to the new *vertex point* ${\frac {F+2R+(n-3)P}{n}}$ (This is the barycenter of *P*, *R* and *F* with respective weights (*n* − 3), 2 and 1)
- Form edges and faces in the new mesh
  - Connect each new *face point* to the new *edge points* of all original edges defining the original face
  - Connect each new *vertex point* to the new *edge points* of all original edges incident on the original vertex
  - Define new faces as enclosed by edges

### Properties

The new mesh will consist only of quadrilaterals, which in general will *not* be planar. The new mesh will generally look "smoother" (i.e. less "jagged" or "pointy") than the old mesh. Repeated subdivision results in meshes that are more and more rounded.

The arbitrary-looking barycenter formula was chosen by Catmull and Clark based on the aesthetic appearance of the resulting surfaces rather than on a mathematical derivation, although they do go to great lengths to rigorously show that the method converges to bicubic B-spline surfaces.

It can be shown that the limit surface obtained by this refinement process is $G^{1}$ (tangent plane) continuous at extraordinary vertices (valence not equal to 4) and ${\mathcal {C}}^{2}$ continuous at regular points (valence equal to 4). (when *n* indicates how many derivatives are continuous, we speak of ${\mathcal {C}}^{n}$ continuity). After one iteration, the number of extraordinary points on the surface remains constant.

## Exact evaluation

The limit surface of Catmull–Clark subdivision surfaces can also be evaluated directly, without any recursive refinement. This can be accomplished by means of the technique of Jos Stam (1998). This method reformulates the recursive refinement process into a matrix exponential problem, which can be solved directly by means of matrix diagonalization.

## Extensions

### Semi-sharp creases

Catmull–Clark surfaces were extended to support semi-sharp creases by using different subdivision rules for a fixed number of iterations determined by a sharpness value. This approach, introduced by Tony DeRose et al. in 1998, allows for a controllable transition from sharp to smooth subdivision rules.

## Software using the algorithm

- 3ds Max
- 3D-Coat
- AC3D
- Anim8or
- AutoCAD
- Blender
- Carrara
- CATIA (Imagine and Shape)
- CGAL
- Cheetah3D
- Cinema4D
- Clara.io
- Creo (Freestyle)
- Daz Studio, 2.0
- DeleD Community Edition
- DeleD Designer
- Hammer
- Hexagon
- Houdini
- LightWave 3D, version 9
- Makehuman
- Maya
- Metasequoia
- MODO
- Mudbox
- Power Surfacing add-in for SolidWorks
- Pixar's OpenSubdiv
- PRMan
- Realsoft3D
- Remo 3D
- Rhinoceros 3D - Grasshopper 3D Plugin - Weaverbird Plugin
- Silo
- SketchUp - Requires a Plugin.
- Softimage XSI
- Strata 3D CX
- Wings 3D
- Zbrush

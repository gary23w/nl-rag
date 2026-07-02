---
title: "Unit cell"
source: https://en.wikipedia.org/wiki/Unit_cell
domain: crystallography
license: CC-BY-SA-4.0
tags: crystallography lattices, crystal system, bravais lattice, space group
fetched: 2026-07-02
---

# Unit cell

In geometry, biology, mineralogy and solid state physics, a **unit cell** is a repeating unit formed by the vectors spanning the points of a lattice. Despite its suggestive name, the unit cell (unlike a unit vector, for example) does not necessarily have unit size, or even a particular size at all. Rather, the primitive cell is the closest analogy to a unit vector, since it has a determined size for a given lattice and is the basic building block from which larger cells are constructed. Geometrically, this is a special case of a fundamental domain of a group (the translation symmetries) acting on a topological space (Euclidean space).

The concept is used particularly in describing crystal structure in two and three dimensions, though it makes sense in all dimensions. A lattice can be characterized by the geometry of its unit cell, which is a section of the tiling (a parallelogram or parallelepiped) that generates the whole tiling using only translations.

There are two special cases of the unit cell: the **primitive cell** and the **conventional cell**. The primitive cell is a unit cell corresponding to a single lattice point, it is the smallest possible unit cell. In some cases, the full symmetry of a crystal structure is not obvious from the primitive cell, in which cases a conventional cell may be used. A conventional cell (which may or may not be primitive) is a unit cell with the full symmetry of the lattice and may include more than one lattice point. The conventional unit cells are parallelotopes in *n* dimensions.

## Primitive cell

A primitive cell is a unit cell that contains exactly one lattice point. For unit cells generally, lattice points that are shared by n cells are counted as ⁠1/n⁠ of the lattice points contained in each of those cells; so for example a primitive unit cell in three dimensions which has lattice points only at its eight vertices is considered to contain ⁠1/8⁠ of each of them. An alternative conceptualization is to consistently pick only one of the n lattice points to belong to the given unit cell (so the other n-1 lattice points belong to adjacent unit cells).

The *primitive translation vectors* *a*→1, *a*→2, *a*→3 span a lattice cell of smallest volume for a particular three-dimensional lattice, and are used to define a crystal translation vector

${\vec {T}}=u_{1}{\vec {a}}_{1}+u_{2}{\vec {a}}_{2}+u_{3}{\vec {a}}_{3},$

where *u*1, *u*2, *u*3 are integers, translation by which leaves the lattice invariant. That is, for a point in the lattice **r**, the arrangement of points appears the same from **r′** = **r** + *T*→ as from **r**.

Since the primitive cell is defined by the primitive axes (vectors) *a*→1, *a*→2, *a*→3, the volume *V*p of the primitive cell is given by the parallelepiped from the above axes as

$V_{\mathrm {p} }=\left|{\vec {a}}_{1}\cdot ({\vec {a}}_{2}\times {\vec {a}}_{3})\right|.$

Usually, primitive cells in two and three dimensions are chosen to take the shape parallelograms and parallelepipeds, with an atom at each corner of the cell. This choice of primitive cell is not unique, but volume of primitive cells will always be given by the expression above.

### Wigner–Seitz cell

In addition to the parallelepiped primitive cells, for every Bravais lattice there is another kind of primitive cell called the Wigner–Seitz cell. In the Wigner–Seitz cell, the lattice point is at the center of the cell, and for most Bravais lattices, the shape is not a parallelogram or parallelepiped. This is a type of Voronoi cell. The Wigner–Seitz cell of the reciprocal lattice in momentum space is called the Brillouin zone.

## Conventional cell

For each particular lattice, a conventional cell has been chosen on a case-by-case basis by crystallographers based on convenience of calculation. These conventional cells may have additional lattice points located in the middle of the faces or body of the unit cell. The number of lattice points, as well as the volume of the conventional cell is an integer multiple (1, 2, 3, or 4) of that of the primitive cell.

## Two dimensions

For any 2-dimensional lattice, the unit cells are parallelograms, which in special cases may have orthogonal angles, equal lengths, or both. Four of the five two-dimensional Bravais lattices are represented using conventional primitive cells, as shown below.

| Conventional primitive cell |   |   |   |   |
|---|---|---|---|---|
| Shape name | Parallelogram | Rectangle | Square | Rhombus |
| Bravais lattice | Primitive Oblique | Primitive Rectangular | Primitive Square | Primitive Hexagonal |

The centered rectangular lattice also has a primitive cell in the shape of a rhombus, but in order to allow easy discrimination on the basis of symmetry, it is represented by a conventional cell which contains two lattice points.

| Primitive cell |   |
|---|---|
| Shape name | Rhombus |
| Conventional cell |   |
| Bravais lattice | Centered Rectangular |

## Three dimensions

For any 3-dimensional lattice, the conventional unit cells are parallelepipeds, which in special cases may have orthogonal angles, or equal lengths, or both. Seven of the fourteen three-dimensional Bravais lattices are represented using conventional primitive cells, as shown below.

| Conventional primitive cell |   |   |   |   |   |   | (Hexagonal) |
|---|---|---|---|---|---|---|---|
| Shape name | Parallelepiped | Oblique rectangular prism | Rectangular cuboid | Square cuboid | Trigonal trapezohedron | Cube | Right rhombic prism |
| Bravais lattice | Primitive Triclinic | Primitive Monoclinic | Primitive Orthorhombic | Primitive Tetragonal | Primitive Rhombohedral | Primitive Cubic | Primitive Hexagonal |

The other seven Bravais lattices (known as the centered lattices) also have primitive cells in the shape of a parallelepiped, but in order to allow easy discrimination on the basis of symmetry, they are represented by conventional cells which contain more than one lattice point.

| Primitive cell |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Shape name | Oblique rhombic prism | Right rhombic prism |   |   |   |   |   |
| Conventional cell |   |   |   |   |   |   |   |
| Bravais lattice | Base-centered Monoclinic | Base-centered Orthorhombic | Body-centered Orthorhombic | Face-centered Orthorhombic | Body-centered Tetragonal | Body-centered Cubic | Face-centered Cubic |

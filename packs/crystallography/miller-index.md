---
title: "Miller index"
source: https://en.wikipedia.org/wiki/Miller_index
domain: crystallography
license: CC-BY-SA-4.0
tags: crystallography lattices, crystal system, bravais lattice, space group
fetched: 2026-07-02
---

# Miller index

**Miller indices** form a notation system in crystallography for lattice planes in crystal (Bravais) lattices.

In particular, a family of lattice planes of a given (direct) Bravais lattice is determined by three integers h, k, and l, the *Miller indices*. They are written (*hkl*), and denote the family of (parallel) lattice planes (of the given Bravais lattice) orthogonal to $\mathbf {g} _{hk\ell }=h\mathbf {b} _{1}+k\mathbf {b} _{2}+\ell \mathbf {b} _{3},$ where **b***i* are the basis or primitive translation vectors of the reciprocal lattice for the given Bravais lattice. (Note that the plane is not always orthogonal to the linear combination of direct or original lattice vectors $h\mathbf {a} _{1}+k\mathbf {a} _{2}+\ell \mathbf {a} _{3}$ because the direct lattice vectors need not be mutually orthogonal.) This is based on the fact that a reciprocal lattice vector **g** (the vector indicating a reciprocal lattice point from the reciprocal lattice origin) is the wavevector of a plane wave in the Fourier series of a spatial function (e.g., electronic density function) which periodicity follows the original Bravais lattice, so wavefronts of the plane wave are coincident with parallel lattice planes of the original lattice. Since a measured scattering vector in X-ray crystallography, $\Delta \mathbf {k} =\mathbf {k} _{\mathrm {out} }-\mathbf {k} _{\mathrm {in} }$ with **k**out as the outgoing (scattered from a crystal lattice) X-ray wavevector and **k**in as the incoming (toward the crystal lattice) X-ray wavevector, is equal to a reciprocal lattice vector **g** as stated by the Laue equations, the measured scattered X-ray peak at each measured scattering vector Δ**k** is marked by *Miller indices*.

By convention, negative integers are written with a bar, as in 3 for −3. The integers are usually written in lowest terms, i.e. their greatest common divisor should be 1. Miller indices are also used to designate reflections in X-ray crystallography. In this case the integers are not necessarily in lowest terms, and can be thought of as corresponding to planes spaced such that the reflections from adjacent planes would have a phase difference of exactly one wavelength (2π), regardless of whether there are atoms on all these planes or not.

There are also several related notations:

- the notation {*hkl*} denotes the set of all planes that are equivalent to (*hkl*) by the symmetry of the lattice.

In the context of crystal *directions* (not planes), the corresponding notations are:

- [*hkl*], with square instead of round brackets, denotes a direction in the basis of the *direct* lattice vectors instead of the reciprocal lattice; and
- similarly, the notation ⟨*hkl*⟩ denotes the set of all directions that are equivalent to [*hkl*] by symmetry.

Note, for Laue–Bragg interferences

- hkl lacks any bracketing when designating a reflection

Miller indices were introduced in 1839 by the British mineralogist William Hallowes Miller, although an almost identical system (*Weiss parameters*) had already been used by German mineralogist Christian Samuel Weiss since 1817. The method was also historically known as the Millerian system, and the indices as Millerian, although this is now rare.

The Miller indices are defined with respect to any choice of unit cell and not only with respect to primitive basis vectors, as is sometimes stated.

## Definition

There are two equivalent ways to define the meaning of the Miller indices: via a point in the reciprocal lattice, or as the inverse intercepts along the lattice vectors. Both definitions are given below. In either case, one needs to choose the three lattice vectors **a**1, **a**2, and **a**3 that define the unit cell (note that the conventional unit cell may be larger than the primitive cell of the Bravais lattice, as the examples below illustrate). Given these, the three primitive reciprocal lattice vectors are also determined (denoted **b**1, **b**2, and **b**3).

Then, given the three Miller indices h, k, l, (*hkl*) denotes planes orthogonal to the reciprocal lattice vector: $\mathbf {g} _{hk\ell }=h\mathbf {b} _{1}+k\mathbf {b} _{2}+\ell \mathbf {b} _{3}.$ That is, (*hkl*) simply indicates a normal to the planes in the basis of the primitive reciprocal lattice vectors. Because the coordinates are integers, this normal is itself always a reciprocal lattice vector. The requirement of lowest terms means that it is the *shortest* reciprocal lattice vector in the given direction.

Equivalently, (*hkl*) denotes a plane that intercepts the three points **a**1/*h*, **a**2/*k*, and **a**3/*l*, or some multiple thereof. That is, the Miller indices are proportional to the *inverses* of the intercepts of the plane, in the basis of the lattice vectors. If one of the indices is zero, it means that the planes do not intersect that axis (the intercept is "at infinity").

Considering only (*hkl*) planes intersecting one or more lattice points (the *lattice planes*), the perpendicular distance d between adjacent lattice planes is related to the (shortest) reciprocal lattice vector orthogonal to the planes by the formula: $d={\frac {2\pi }{|\mathbf {g} _{hk\ell }|}}.$

The related notation [*hkl*] denotes the *direction*: $h\mathbf {a} _{1}+k\mathbf {a} _{2}+\ell \mathbf {a} _{3}.$ That is, it uses the direct lattice basis instead of the reciprocal lattice. Note that [*hkl*] is *not* generally normal to the (*hkl*) planes, except in a cubic lattice as described below.

## Cubic structures

For the special case of simple cubic crystals, the lattice vectors are orthogonal and of equal length (usually denoted a), as are those of the reciprocal lattice. Thus, in this common case, the Miller indices (*hkl*) and [*hkl*] both simply denote normals/directions in Cartesian coordinates.

For cubic crystals with lattice constant a, the spacing d between adjacent (*hkl*) lattice planes is (from above) $d_{hk\ell }={\frac {a}{\sqrt {h^{2}+k^{2}+\ell ^{2}}}}.$

Because of the symmetry of cubic crystals, it is possible to change the place and sign of the integers and have equivalent directions and planes:

- Indices in *angle brackets* such as ⟨100⟩ denote a *family* of directions which are equivalent due to symmetry operations, such as [100], [010], [001] or the negative of any of those directions.
- Indices in *curly brackets* or *braces* such as {100} denote a family of plane normals which are equivalent due to symmetry operations, much the way angle brackets denote a family of directions.

For face-centered cubic and body-centered cubic lattices, the primitive lattice vectors are not orthogonal. However, in these cases the Miller indices are conventionally defined relative to the lattice vectors of the cubic supercell and hence are again simply the Cartesian directions.

## Hexagonal and rhombohedral structures

For hexagonal and rhombohedral lattice systems, the **Bravais–Miller** system is typically used, which uses four indices (*h* *k* *i* *l*) that obey the constraint $h+k+i=0.$ Here h, k and l are identical to the corresponding Miller indices, and i is a redundant index.

This four-index scheme for labeling planes in a hexagonal lattice makes permutation symmetries apparent. For example, the similarity between (110) ≡ (1120) and (120) ≡ (1210) is more obvious when the redundant index is shown.

In the figure at right, the (001) plane has a 3-fold symmetry: it remains unchanged by a rotation of 1/3 (2π/3 rad, 120°). The [100], [010] and the [110] directions are really similar. If S is the intercept of the plane with the [110] axis, then $i={\frac {1}{S}}.$

There are also *ad hoc* schemes (e.g. in the transmission electron microscopy literature) for indexing hexagonal *lattice vectors* (rather than reciprocal lattice vectors or planes) with four indices. However they do not operate by similarly adding a redundant index to the regular three-index set.

For example, the reciprocal lattice vector (*hkl*) as suggested above can be written in terms of reciprocal lattice vectors as $h\mathbf {b} _{1}+k\mathbf {b} _{2}+\ell \mathbf {b} _{3}.$ For hexagonal crystals this may be expressed in terms of direct-lattice basis-vectors **a**1, **a**2 and **a**3 as

$h\mathbf {b} _{1}+k\mathbf {b} _{2}+\ell \mathbf {b} _{3}={\frac {2}{3a^{2}}}(2h+k)\mathbf {a} _{1}+{\frac {2}{3a^{2}}}(h+2k)\mathbf {a} _{2}+{\frac {1}{c^{2}}}(\ell )\mathbf {a} _{3}.$

Hence zone indices of the direction perpendicular to plane (*hkl*) are, in suitably normalized triplet form, simply $\left[2h+k,\ h+2k,\ {\tfrac {3}{2}}\ell \left({\tfrac {a}{c}}\right)^{2}\right].$ When *four indices* are used for the zone normal to plane (*hkl*), however, the literature often uses $\left[h,\ k,\ -h-k,\ {\tfrac {3}{2}}\ell \left({\tfrac {a}{c}}\right)^{2}\right]$ instead. Thus as you can see, four-index zone indices in square or angle brackets sometimes mix a single direct-lattice index on the right with reciprocal-lattice indices (normally in round or curly brackets) on the left.

And, note that for hexagonal interplanar distances, they take the form $d_{hk\ell }={\frac {a}{\sqrt {{\tfrac {4}{3}}\left(h^{2}+k^{2}+hk\right)+{\tfrac {a^{2}}{c^{2}}}\ell ^{2}}}}$ However, in general: $d_{hkl}={\frac {2\pi }{\sqrt {h^{2}{\textbf {b}}_{1}^{2}+k^{2}{\textbf {b}}_{2}^{2}+l^{2}{\textbf {b}}_{3}^{2}+2hk{\textbf {b}}_{1}{\textbf {b}}_{2}\cos \gamma ^{*}+2kl{\textbf {b}}_{2}{\textbf {b}}_{3}\cos \alpha ^{*}+2lh{\textbf {b}}_{1}{\textbf {b}}_{3}\cos \beta ^{*}}}}$

## Crystallographic planes and directions

Crystallographic directions are lines linking nodes (atoms, ions or molecules) of a crystal. Similarly, crystallographic planes are *planes* linking nodes. Some directions and planes have a higher density of nodes; these dense planes have an influence on the behavior of the crystal:

- optical properties: in condensed matter, light "jumps" from one atom to the other with the Rayleigh scattering; the velocity of light thus varies according to the directions, whether the atoms are close or far; this gives the birefringence
- adsorption and reactivity: adsorption and chemical reactions can occur at atoms or molecules on crystal surfaces, these phenomena are thus sensitive to the density of nodes;
- surface tension: the condensation of a material means that the atoms, ions or molecules are more stable if they are surrounded by other similar species; the surface tension of an interface thus varies according to the density on the surface
  - Pores and crystallites tend to have straight grain boundaries following dense planes
  - cleavage
- dislocations (plastic deformation)
  - the dislocation core tends to spread on dense planes (the elastic perturbation is "diluted"); this reduces the friction (Peierls–Nabarro force), the sliding occurs more frequently on dense planes;
  - the perturbation carried by the dislocation (Burgers vector) is along a dense direction: the shift of one node in a dense direction is a lesser distortion;
  - the dislocation line tends to follow a dense direction, the dislocation line is often a straight line, a dislocation loop is often a polygon.

For all these reasons, it is important to determine the planes and thus to have a notation system.

## Non-integer Miller indices

Ordinarily, Miller indices are always integers by definition, and this constraint is physically significant. To understand this, suppose that we allow a plane (*abc*) where the Miller "indices" a, b and c (defined as above) are not necessarily integers.

### Lattice planes

If a, b and c have rational ratios, then the same family of planes can be written in terms of integer indices (*hkl*) by scaling a, b and c appropriately: divide by the largest of the three numbers, and then multiply by the least common denominator. Thus, integer Miller indices implicitly include indices with all rational ratios. The reason why planes where the components (in the reciprocal-lattice basis) have rational ratios are of special interest is that these are the lattice planes: they are the only planes whose intersections with the crystal are 2d-periodic.

### Quasicrystals

For a plane (*abc*) where a, b and c have irrational ratios, on the other hand, the intersection of the plane with the crystal is *not* periodic. It forms an aperiodic pattern known as a quasicrystal. This construction corresponds precisely to the standard "cut-and-project" method of defining a quasicrystal, using a plane with irrational-ratio Miller indices. (Although many quasicrystals, such as the Penrose tiling, are formed by "cuts" of periodic lattices in more than three dimensions, involving the intersection of more than one such hyperplane.)

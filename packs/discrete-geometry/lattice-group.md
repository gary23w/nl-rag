---
title: "Lattice (group)"
source: https://en.wikipedia.org/wiki/Lattice_(group)
domain: discrete-geometry
license: CC-BY-SA-4.0
tags: discrete geometry, sphere packing, kissing number, geometric lattice
fetched: 2026-07-02
---

# Lattice (group)

In geometry and group theory, a **lattice** in the real coordinate space $\mathbb {R} ^{n}$ is an infinite set of points in this space with these properties:

- Coordinate-wise addition or subtraction of two points in the lattice produces another lattice point.
- The lattice points are all separated by some minimum distance.
- Every point in the space is within some maximum distance of a lattice point.

One of the simplest examples of a lattice is the square lattice, which consists of all points $(a,b)$ in the plane whose coordinates are both integers, and its higher-dimensional analogues the integer lattices $\mathbb {Z} ^{n}$ .

Closure under addition and subtraction means that a lattice must be a subgroup of the additive group of the points in the space. The requirements of minimum and maximum distance can be summarized by saying that a lattice is a Delone set.

More abstractly, a lattice can be described as a free abelian group of dimension n which spans the vector space ⁠ $\mathbb {R} ^{n}$ ⁠. For any basis of ⁠ $\mathbb {R} ^{n}$ ⁠, the subgroup of all linear combinations with integer coefficients of the basis vectors forms a lattice, and every lattice can be formed from a basis in this way. A lattice may be viewed as a regular tiling of a space by a primitive cell.

Lattices have many significant applications in pure mathematics, particularly in connection to Lie algebras, number theory and group theory. They also arise in applied mathematics in connection with coding theory, in percolation theory to study connectivity arising from small-scale interactions, cryptography because of conjectured computational hardness of several lattice problems, and occur frequently in the physical sciences. For instance, in materials science and solid-state physics, a lattice is a synonym for a crystalline structure, a 3-dimensional array of regularly spaced points coinciding in special cases with the atom or molecule positions in a crystal. More generally, lattice models are studied in physics, often by the techniques of computational physics.

## Symmetry considerations and examples

A lattice is the symmetry group of discrete translational symmetry in *n* directions. A pattern with this lattice of translational symmetry cannot have more, but may have less symmetry than the lattice itself. As a group (dropping its geometric structure) a lattice is a finitely generated free abelian group, and thus isomorphic to ⁠ $\mathbb {Z} ^{n}$ ⁠.

A lattice in the sense of a 3-dimensional array of regularly spaced points coinciding with e.g. the atom or molecule positions in a crystal, or more generally, the orbit of a group action under translational symmetry, is a translation of the translation lattice: a coset, which need not contain the origin, and therefore need not be a lattice in the previous sense.

A simple example of a lattice in $\mathbb {R} ^{n}$ is the subgroup ⁠ $\mathbb {Z} ^{n}$ ⁠. More complicated examples include the E8 lattice, which is a lattice in ⁠ $\mathbb {R} ^{8}$ ⁠, and the Leech lattice in ⁠ $\mathbb {R} ^{24}$ ⁠. The period lattice in $\mathbb {R} ^{2}$ is central to the study of elliptic functions, developed in nineteenth century mathematics; it generalizes to higher dimensions in the theory of abelian functions. Lattices called root lattices are important in the theory of simple Lie algebras; for example, the E8 lattice is related to a Lie algebra that goes by the same name.

## Lattice basis tiling space

A lattice $\Lambda$ in $\mathbb {R} ^{n}$ thus has the form

$\Lambda ={\biggl \{}\sum _{i=1}^{n}a_{i}v_{i}\mathbin {\bigg \vert } a_{i}\in \mathbb {Z} {\biggr \}},$

where ${\textstyle \{v_{1},v_{2},\ldots ,v_{n}\}}$ is a basis for ⁠ $\mathbb {R} ^{n}$ ⁠, whose column-vectors form an *n* x *n* matrix *M*. Any other basis ${\textstyle \{v_{1}',v_{2}',\ldots ,v_{n}'\}}$ with matrix *M'* is related by an automorphism of the group $\Lambda \cong \mathbb {Z} ^{n}$ , meaning $M'=AM$ for an integer transition matrix $A\in \mathrm {GL} _{n}(\mathbb {Z} )$ having $\det(A)=\pm 1$ .

A lattice fills the whole of $\mathbb {R} ^{n}$ with equal tiles, copies of the *n*-dimensional parallelepiped spanned by the basis vectors, known as the *fundamental domain* or *primitive cell* of the lattice. The *n*-dimensional volume of this fundamental domain is sometimes called the **covolume** of the lattice: it is invariant for any basis, and may be computed as $d(\Lambda )=|\det(M)|$ . (If the *n*-dimensional lattice *$\Lambda$* lies in a higher-dimensional space $\mathbb {R} ^{m}$ , its basis forms an *m* x *n* matrix whose volume can be computed using the Gram matrix: $d(\Lambda )={\sqrt {\det M^{t}M}}$ .) A lattice with $d(\Lambda )=1$ is called unimodular.

## Lattice points in convex sets

Minkowski's theorem relates the number ⁠ $\mathrm {d} (\Lambda )$ ⁠, or more generally the volume of a symmetric convex set S , to the number of lattice points contained in ⁠ S ⁠. For a polytope whose vertices are elements of the lattice, the number of lattice points it contains is described by the polytope's Ehrhart polynomial. Formulas for some of the coefficients of this polynomial involve ⁠ $\mathrm {d} (\Lambda )$ ⁠ as well.

## Computational lattice problems

Computational lattice problems have many applications in computer science. For example, the Lenstra–Lenstra–Lovász lattice basis reduction algorithm (LLL) has been used in the cryptanalysis of many public-key encryption schemes, and many lattice-based cryptographic schemes are known to be secure under the assumption that certain lattice problems are computationally difficult.

## Lattices in two dimensions: detailed discussion

There are five 2D lattice types as given by the crystallographic restriction theorem. Below, the wallpaper group of the lattice $\Lambda$ is given in IUCr notation, Orbifold notation, and Coxeter notation, along with a wallpaper diagram showing the symmetry domains. Note that a pattern with this lattice of translational symmetry cannot have more, but may have less symmetry than the lattice itself. A full list of subgroups is available. For example, below the hexagonal/triangular lattice is given twice, with full 6-fold and a half 3-fold reflectional symmetry. If the symmetry group of a pattern contains an *n*-fold rotation then the lattice has *n*-fold symmetry for even *n* and 2*n*-fold for odd *n*.

| cmm, (2*22), [∞,2+,∞] | p4m, (*442), [4,4] | p6m, (*632), [6,3] |
|---|---|---|
| **rhombic lattice** also **centered rectangular lattice** *isosceles triangular* | **square lattice** *right isosceles triangular* | **hexagonal lattice** (equilateral triangular lattice) |
| pmm, *2222, [∞,2,∞] | p2, 2222, [∞,2,∞]+ | p3m1, (*333), [3[3]] |
| **rectangular lattice** also **centered rhombic lattice** *right triangular* | **oblique lattice** *scalene triangular* | **equilateral triangular lattice** (hexagonal lattice) |

For the classification of a given lattice, start with one point and take a nearest second point. For the third point, not on the same line, consider its distances to both points. Among the points for which the smaller of these two distances is least, choose a point for which the larger of the two is least. (Not logically equivalent but in the case of lattices giving the same result is just "Choose a point for which the larger of the two is least".)

The five cases correspond to the triangle being equilateral, right isosceles, right, isosceles, and scalene. In a rhombic lattice, the shortest distance may either be a diagonal or a side of the rhombus, i.e., the line segment connecting the first two points may or may not be one of the equal sides of the isosceles triangle. This depends on the smaller angle of the rhombus being less than 60° or between 60° and 90°.

The general case is known as a period lattice. The vectors {**p**,**q**} are a generator pair or a basis of the lattice $\Lambda$ . Instead of {**p**, **q**} we can also take the basis {**p**, **p** − **q**}, or in general {*a***p** + *b***q** **,** *c***p** + *d***q**} for integers *a*,*b*,*c*,*d* forming an integer transition matrix $T={\bigl (}{\begin{smallmatrix}a&b\\c&d\end{smallmatrix}}{\bigr )}$ of unit determinant, meaning $\det T=ad-bc=\pm 1$ . This ensures that **p** and **q** themselves are integer linear combinations of the other two vectors. (The transition matrix T lies in $\mathrm {GL} _{2}(\mathbb {Z} )$ , the automorphism group of the lattice $L\cong \mathbb {Z} ^{2}$ , which is a double cover of the well-studied modular group $\mathrm {SL} _{2}(\mathbb {Z} )$ .)

Each basis pair {**p**, **q**} defines a parallelogram, all with the same area given by the magnitude of the cross product **p** x **q**. This parallelogram is a fundamental parallelogram of the translation symmetries, i.e. a fundamental domain or primitive cell.

The basis vectors {**p,q**} can be represented by complex numbers. Up to changing the scaling of the lattice and rotating it, the pair {**p,q**} can be represented by their complex number quotient: if we fix two standard lattice points 0 and 1 in the complex plane, the lattice shape is determined by the third lattice point *z = p*/*q*. A change of basis is represented by the modular group $\mathrm {SL} _{2}(\mathbb {Z} )$ , which acts on the complex plane by linear fractional transformations, generated by the two operations $T:z\mapsto z+1$ , shifting to a different third point in the same grid, and $S:z\mapsto -1/z$ , choosing a different side of the triangle as reference side 0–1. The figure shows the action of the modular group acting on the complex plane $\mathbb {C}$ (not to be confused with the lattice translating the real plane $\mathbb {R} ^{2}$ ). Each "curved triangle" in the image is a fundamental domain of the modular group, contain one complex number for each 2D lattice $\Lambda$ up to scaling and rotation. The grey area is a standard fundamental domain, corresponding to the canonical representation of $\Lambda$ with 0 and 1 being two lattice points that are closest to each other; duplication is avoided by including only half of the boundary. The rhombic lattices are represented by the points on the boundary, with the hexagonal lattice as vertex, and *i* for the square lattice. The rectangular lattices are at the imaginary axis, and the remaining area represents the parallelogram lattices, with the mirror image of a parallelogram represented by the mirror image in the imaginary axis.

## Lattices in three dimensions

The 14 lattice types in 3D are called **Bravais lattices**. They are characterized by their space group. 3D patterns with translational symmetry of a particular type cannot have more, but may have less, symmetry than the lattice itself.

## Lattices in complex space

A lattice in $\mathbb {C} ^{n}$ is a discrete subgroup of $\mathbb {C} ^{n}$ which spans $\mathbb {C} ^{n}$ as a real vector space. As the dimension of $\mathbb {C} ^{n}$ as a real vector space is equal to ⁠ $2n$ ⁠, a lattice in $\mathbb {C} ^{n}$ will be a free abelian group of rank ⁠ $2n$ ⁠.

For example, the Gaussian integers $\mathbb {Z} [i]=\mathbb {Z} +i\mathbb {Z}$ form a lattice in ⁠ $\mathbb {C} =\mathbb {C} ^{1}$ ⁠, as $(1,i)$ is a basis of $\mathbb {C}$ over ⁠ $\mathbb {R}$ ⁠.

## In Lie groups

More generally, a **lattice** Γ in a Lie group *G* is a discrete subgroup, such that the quotient *G*/Γ is of finite measure, for the measure on it inherited from Haar measure on *G* (left-invariant, or right-invariant—the definition is independent of that choice). That will certainly be the case when *G*/Γ is compact, but that sufficient condition is not necessary, as is shown by the case of the modular group in SL2(**R**), which is a lattice but where the quotient isn't compact (it has *cusps*). There are general results stating the existence of lattices in Lie groups.

A lattice is said to be **uniform** or **cocompact** if *G*/Γ is compact; otherwise the lattice is called **non-uniform**.

## Lattices in general vector spaces

While we normally consider $\mathbb {Z}$ lattices in $\mathbb {R} ^{n}$ this concept can be generalized to any finite-dimensional vector space over any field. This can be done as follows:

Let *K* be a field, let *V* be an *n*-dimensional *K*-vector space, let $B=\{\mathbf {v} _{1},\ldots ,\mathbf {v} _{n}\}$ be a *K*-basis for *V* and let *R* be a ring contained within *K*. Then the *R* lattice ${\mathcal {L}}$ in *V* generated by *B* is given by:

${\mathcal {L}}={\biggl \{}\sum _{i=1}^{n}a_{i}\mathbf {v} _{i}\mathbin {\bigg \vert } a_{i}\in R{\biggr \}}.$

In general, different bases *B* will generate different lattices. However, if the transition matrix T between the bases is in $\mathrm {GL} _{n}(R)$ – the general linear group of R (in simple terms this means that all the entries of T are in R and all the entries of $T^{-1}$ are in R – which is equivalent to saying that the determinant of *T* is in $R^{*}$ – the unit group of elements in *R* with multiplicative inverses) then the lattices generated by these bases will be isomorphic since *T* induces an isomorphism between the two lattices.

Important cases of such lattices occur in number theory with *K* a *p*-adic field and T the *p*-adic integers.

For a vector space which is also an inner product space, the dual lattice can be concretely described by the set

${\mathcal {L}}^{*}=\{\mathbf {v} \in V\mid \langle \mathbf {v} ,\mathbf {x} \rangle \in R\,{\text{ for all }}\,\mathbf {x} \in {\mathcal {L}}\},$

or equivalently as

${\mathcal {L}}^{*}=\{\mathbf {v} \in V\mid \langle \mathbf {v} ,\mathbf {v} _{i}\rangle \in R,\ i=1,...,n\}.$

## Saturated lattices

A **primitive element** of a lattice is an element $v\in \Lambda$ that is not a positive integer multiple of another element in the lattice. If $\Lambda$ has basis $\{v_{1},\ldots ,v_{n}\}$ , we can identify it with the standard lattice $\Lambda \cong \mathbb {Z} ^{n}$ via $a_{1}v_{1}+\cdots a_{n}v_{n}\mapsto (a_{1},\ldots ,a_{n})$ ; then a vector $v=(a_{1},\ldots ,a_{n})$ is primitive whenever ${\tfrac {1}{d}}v\notin \mathbb {Z} ^{n}$ for any integer $d>1$ , which is equivalent to the coordinates being coprime, $\gcd(a_{1},\ldots ,a_{n})=1$ . Every one-dimensional sublattice $\Gamma \subset \Lambda$ has a primitive generator which is unique up to sign.

More generally, consider an $\ell$ -dimensional sublattice $\Gamma \subset \mathbb {Z} ^{n}$ with a basis $\{v_{1},\ldots ,v_{\ell }\}$ whose column vectors form a matrix $M\in \mathrm {M} _{n\times \ell }(\mathbb {Z} )$ . We say $\Gamma$ is a **saturated sublattice** whenever any of the following equivalent conditions holds:

- $\Gamma =V\cap \mathbb {Z} ^{n}$ for some $\ell$ -dimensional $\mathbb {Q}$ -linear subspace $V\subset \mathbb {Q} ^{n}$
- For every $v\in \mathbb {Z} ^{n}$ and integer $d>1$ , we have $dv\in \Gamma$ only when $v\in \Gamma$ .
- The quotient group $\mathbb {Z} ^{n}/\Gamma$ is a free abelian group, without torsion.
- $\mathbb {Z} ^{n}=\Gamma \oplus \Gamma ^{\perp }$ , where $\Gamma ^{\perp }$ is the orthogonal subspace in $\mathbb {Z} ^{n}$ with respect to the standard dot product.
- The basis matrix $M\in \mathrm {M} _{n\times \ell }(\mathbb {Z} )$ possesses an integer left inverse $N\in \mathrm {M} _{\ell \times n}(\mathbb {Z} )$ with $NM=\mathrm {Id} _{n}$ .
- The Smith normal form of M has only 1's on the main diagonal.
- The maximal minors of M are coprime: $\gcd\{\Delta _{I}(M)\}=1$ , where I runs over all *n*-element subsets of $\{1,\ldots ,m\}$ .

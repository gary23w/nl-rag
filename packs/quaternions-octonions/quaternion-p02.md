---
title: "Quaternion (part 2/2)"
source: https://en.wikipedia.org/wiki/Quaternion
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
part: 2/2
---

## Quaternions as the even part of Cl3,0(ℝ)

The usefulness of quaternions for geometrical computations can be generalised to other dimensions by identifying the quaternions as the even part $\operatorname {Cl} _{3,0}^{+}(\mathbb {R} )$ of the Clifford algebra $\operatorname {Cl} _{3,0}(\mathbb {R} ).$ This is an associative multivector algebra built up from fundamental basis elements *σ*1, *σ*2, *σ*3 using the product rules

$\sigma _{1}^{2}=\sigma _{2}^{2}=\sigma _{3}^{2}=1,$ $\sigma _{m}\sigma _{n}=-\sigma _{n}\sigma _{m}\qquad (m\neq n).$

If these fundamental basis elements are taken to represent vectors in 3D space, then it turns out that the *reflection* of a vector r in a plane perpendicular to a unit vector w can be written:

$r^{\prime }=-w\,r\,w.$

Two reflections make a rotation by an angle twice the angle between the two reflection planes, so

$r^{\prime \prime }=\sigma _{2}\sigma _{1}\,r\,\sigma _{1}\sigma _{2}$

corresponds to a rotation of 180° in the plane containing *σ*1 and *σ*2. This is very similar to the corresponding quaternion formula,

$r^{\prime \prime }=-\mathbf {k} \,r\,\mathbf {k} .$

Indeed, the two structures $\operatorname {Cl} _{3,0}^{+}(\mathbb {R} )$ and $\mathbb {H}$ are isomorphic. One natural identification is

$1\mapsto 1,\quad \mathbf {i} \mapsto -\sigma _{2}\sigma _{3},\quad \mathbf {j} \mapsto -\sigma _{3}\sigma _{1},\quad \mathbf {k} \mapsto -\sigma _{1}\sigma _{2},$

and it is straightforward to confirm that this preserves the Hamilton relations

$\mathbf {i} ^{2}=\mathbf {j} ^{2}=\mathbf {k} ^{2}=\mathbf {i\,j\,k} =-1.$

In this picture, so-called "vector quaternions" (that is, pure imaginary quaternions) correspond not to vectors but to bivectors – quantities with magnitudes and orientations associated with particular 2D *planes* rather than 1D *directions*. The relation to complex numbers becomes clearer, too: in 2D, with two vector directions *σ*1 and *σ*2, there is only one bivector basis element *σ*1*σ*2, so only one imaginary. But in 3D, with three vector directions, there are three bivector basis elements *σ*2*σ*3, *σ*3*σ*1, *σ*1*σ*2, so three imaginaries.

This reasoning extends further. In the Clifford algebra $\operatorname {Cl} _{4,0}(\mathbb {R} ),$ there are six bivector basis elements, since with four different basic vector directions, six different pairs and therefore six different linearly independent planes can be defined. Rotations in such spaces using these generalisations of quaternions, called rotors, can be very useful for applications involving homogeneous coordinates. But it is only in 3D that the number of basis bivectors equals the number of basis vectors, and each bivector can be identified as a pseudovector.

There are several advantages for placing quaternions in this wider setting:

- Rotors are a natural part of geometric algebra and easily understood as the encoding of a double reflection.
- In geometric algebra, a rotor and the objects it acts on live in the same space. This eliminates the need to change representations and to encode new data structures and methods, which is traditionally required when augmenting linear algebra with quaternions.
- Rotors are universally applicable to any element of the algebra, not just vectors and other quaternions, but also lines, planes, circles, spheres, rays, and so on.
- In the conformal model of Euclidean geometry, rotors allow the encoding of rotation, translation and scaling in a single element of the algebra, universally acting on any element. In particular, this means that rotors can represent rotations around an arbitrary axis, whereas quaternions are limited to an axis through the origin.
- Rotor-encoded transformations make interpolation particularly straightforward.
- Rotors carry over naturally to pseudo-Euclidean spaces, for example, the Minkowski space of special relativity. In such spaces rotors can be used to efficiently represent Lorentz boosts, and to interpret formulas involving the gamma matrices.

For further detail about the geometrical uses of Clifford algebras, see Geometric algebra.


## Brauer group

The quaternions are "essentially" the only (non-trivial) central simple algebra (CSA) over the real numbers, in the sense that every CSA over the real numbers is Brauer equivalent to either the real numbers or the quaternions. Explicitly, the Brauer group of the real numbers consists of two classes, represented by the real numbers and the quaternions, where the Brauer group is the set of all CSAs, up to equivalence relation of one CSA being a matrix ring over another. By the Artin–Wedderburn theorem (specifically, Wedderburn's part), CSAs are all matrix algebras over a division algebra, and thus the quaternions are the only non-trivial division algebra over the real numbers.

CSAs – finite dimensional rings over a field, which are simple algebras (have no non-trivial 2-sided ideals, just as with fields) whose center is exactly the field – are a noncommutative analog of extension fields, and are more restrictive than general ring extensions. The fact that the quaternions are the only non-trivial CSA over the real numbers (up to equivalence) may be compared with the fact that the complex numbers are the only non-trivial finite field extension of the real numbers.

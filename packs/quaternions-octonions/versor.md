---
title: "Versor"
source: https://en.wikipedia.org/wiki/Versor
domain: quaternions-octonions
license: CC-BY-SA-4.0
tags: quaternion algebra, octonion algebra, cayley-dickson construction, spatial rotation
fetched: 2026-07-02
---

# Versor

In mathematics, a **versor** is a quaternion whose norm is one, also known as a **unit quaternion**. Each versor has the form

$\ u=\exp(a\mathbf {r} )=\cos a+\mathbf {r} \sin a,\qquad \mathbf {r} ^{2}=-1,\qquad a\in [0,\pi ]\ ,$

where the condition $\ \mathbf {r} ^{2}=-1\$ means that $\ \mathbf {r} \$ is an algebraic imaginary unit. There is a sphere of imaginary units in the quaternions. Note that the expression for a versor is just Euler's formula for the imaginary unit $\ \mathbf {r} ~.$ If $\ a={\tfrac {\pi }{2}}\$ (when $\ a\$ is a right angle), then $\ u=\mathbf {r} \ ,$ and it is called a *right versor*.

The mapping $\ q\ \longmapsto \ u^{-1}q\ u\$ corresponds to 3-dimensional rotation, and has the angle $\ 2\ a\$ about the axis $\ \mathbf {r} \$ in axis–angle representation.

The collection of versors, with quaternion multiplication, forms a group, and appears as a 3-sphere in the 4-dimensional quaternion algebra.

## Presentation on 3- and 2-spheres

Sir William Rowan Hamilton wrote the **versor** of a quaternion $\ q\$ as the symbol $\ \mathbf {U} \ q~.$ He was then able to display the general quaternion in polar coordinate form

$\ q\ =\ \mathbf {T} \ \!q~~\mathbf {U} \ \!q\ ,$

where $\ \mathbf {T} \ \!q\$ is Hamilton's notation for the norm of $\ q\$ (in modern notation $\ \mathbf {T} \ \!q=\|q\|$ ). The norm of a versor is always equal to one; hence they occupy the unit 3-sphere in $\ \mathbb {H} \$ . Examples of versors include the eight elements of the quaternion group. Of particular importance are the right versors, which have angle $\ {\tfrac {\pi }{2}}~.$ These versors have zero scalar part, and so are vectors of length one (unit vectors). The right versors form a sphere of square roots of −1 in the quaternion algebra. The generators **i**, **j**, and **k** are examples of right versors, as well as their additive inverses. Other versors include the twenty-four Hurwitz quaternions that have the norm 1 and form vertices of a 24-cell polychoron.

Hamilton defined a quaternion as the quotient of two vectors. A versor can be defined as the quotient of two unit vectors. For any fixed plane Π the quotient of two unit vectors lying in Π depends only on the angle (directed) between them, the same a as in the unit vector–angle representation of a versor explained above. That's why it may be natural to understand corresponding versors as directed arcs that connect pairs of unit vectors and lie on a great circle formed by intersection of Π with the unit sphere, where the plane Π passes through the origin. Arcs of the same direction and length (or, the same, subtended angle in radians) are equipollent and correspond to the same versor.

Such an arc, although lying in the three-dimensional space, does not represent a path of a point rotating as described with the sandwiched product with the versor. Indeed, it represents the left multiplication action of the versor on quaternions that preserves the plane Π and the corresponding great circle of 3-vectors. The 3-dimensional rotation defined by the versor has the angle two times the arc's subtended angle, and preserves the same plane. It is a rotation about the corresponding vector **r**, that is perpendicular to Π.

On three unit vectors, Hamilton writes

$q=\beta :\alpha =\mathrm {OB:OA} \qquad$

and

$q'=\gamma :\beta =\mathrm {OC:OB} \qquad$

imply

$q'q=\gamma :\alpha =\mathrm {OC:OA} ~.$

Multiplication of versors corresponds to the (non-commutative) "addition" of great circle arcs on the unit sphere. Any pair of great circles either is the same circle or has two intersection points. Hence, one can always move the point B and the corresponding vector to one of these points such that the beginning of the second arc will be the same as the end of the first arc.

The facility with which versors express elliptic geometry or rotations in 3-space is due to the parametric representation of the factors. Take a generic spherical triangle ABC with angles a, b, and c as the sides opposite the capital vertex. One uses unit vectors perpendicular to the plane of each side of the triangle, say r, s, and t . Then the sides of the triangle are equipollent to a great circle arc represented by versors:

$\ \operatorname {arc} \mathrm {AB} =\exp(c\ r)\ ,\qquad \operatorname {arc} \mathrm {BC} =\exp(a\ s)\ ,\qquad \operatorname {arc} \mathrm {AC} =\exp(b\ t)\ ,$

each expanded by Euler's formula since each of the squares of r, s and t is minus one. Since

$\ \exp(b\ t)=\exp(c\ r)\times \exp(a\ s)\ ,$

the versor product corresponds to addition of spherical arcs.

The geometry of elliptic space has been described as the space of versors.

### Representation of SO(3)

The orthogonal group in three dimensions, rotation group SO(3), is frequently interpreted with versors via the inner automorphism $\ q\mapsto u^{-1}q\ u\$ where u is a versor. Indeed, if

$\ u=\exp(a\ \mathbf {r} )\$

and vector

s

is perpendicular to

r

,

then

$u^{-1}\mathbf {s} \ u\ =\ \mathbf {s} \ \cos(2\ a)\ +\ \mathbf {s} \ \mathbf {r} \ \sin(2\ a)\$

by calculation. The plane $\ \{\ x+y\ \mathbf {r} \ :\ (x,y)\in \mathbb {R} ^{2}\ \}\subset \mathbb {H} \$ is isomorphic to $\ \mathbb {C} \$ and the inner automorphism, by commutativity, reduces to the identity mapping there. Since quaternions can be interpreted as an algebra of two complex dimensions, the rotation action can also be viewed through the special unitary group SU(2).

For a fixed **r**, versors of the form $\ \exp(a\ \mathbf {r} )\$ where $\ a\in \left(-\pi ,\pi \ \right]\ ,$ form a subgroup isomorphic to the circle group. Orbits of the left multiplication action of this subgroup are fibers of a fiber bundle over the 2-sphere, known as Hopf fibration in the case **r** = **i**  ; other vectors give isomorphic, but not identical fibrations. Lyons (2003) gives an elementary introduction to quaternions to elucidate the Hopf fibration as a mapping on unit quaternions. He writes "the fibers of the Hopf map are circles in S3 ".

Versors have been used to represent rotations of the Bloch sphere with quaternion multiplication.

### Elliptic space

The facility of versors illustrate elliptic geometry, in particular elliptic space, a three-dimensional realm of rotations. The versors are the points of this elliptic space, though they refer to rotations in 4-dimensional Euclidean space. Given two fixed versors u and v, the mapping $\ q\mapsto u\ q\ v\$ is an *elliptic motion*. If one of the fixed versors is 1, then the motion is a *Clifford translation* of the elliptic space, named after William Kingdon Clifford who was a proponent of the space. An elliptic line through versor u is $\ \{\ u\ \exp(a\ \mathbf {r} )\ :\ 0\leq a<\pi \ \}~.$ Parallelism in the space is expressed by Clifford parallels. One of the methods of viewing elliptic space uses the Cayley transform to map the versors to $\ \mathbb {R} ^{3}~.$

### Subgroups

The set of all versors, with their multiplication as quaternions, forms a continuous group *G*. For a fixed pair $\ \{-\mathbf {r} ,+\mathbf {r} \ \}\$ of right versors, $\ G_{1}=\{\ \exp(a\ \mathbf {r} )\ :\ a\in \mathbb {R} \ \}\$ is a one-parameter subgroup that is isomorphic to the circle group.

Next consider the finite subgroups, beyond the quaternion group Q8:

As noted by Hurwitz, the 16 quaternions $\ {\tfrac {\ 1\ }{2}}\left(\pm \mathbf {1} \pm \mathbf {i} \pm \mathbf {j} \pm \mathbf {k} \right)\$ all have norm one, so they are in *G*. Joined with Q8, these unit Hurwitz quaternions form a group *G*2 of order 24 called the binary tetrahedral group. The group elements, taken as points on S3, form a 24-cell.

By a process of bitruncation of the 24-cell, the 48-cell on *G* is obtained, and these versors multiply as the binary octahedral group.

Another subgroup is formed by 120 icosians which multiply in the manner of the binary icosahedral group.

## Hyperbolic versor

A hyperbolic versor is a generalization of quaternionic versors to indefinite orthogonal groups, such as Lorentz group. It is defined as a quantity of the form

$\exp(a\mathbf {r} )=\cosh a+\mathbf {r} \sinh a~~$

where

$~~\mathbf {r} ^{2}=+1~.$

Such elements arise in split algebras, for example split-complex numbers or split-quaternions. It was the algebra of tessarines discovered by James Cockle in 1848 that first provided hyperbolic versors. In fact, Cockle wrote the above equation (with **j** in place of **r**) when he found that the tessarines included the new type of imaginary element.

This versor was used by Homersham Cox (1882/1883) in relation to quaternion multiplication. The primary exponent of hyperbolic versors was Alexander Macfarlane, as he worked to shape quaternion theory to serve physical science. He saw the modelling power of hyperbolic versors operating on the split-complex number plane, and in 1891 he introduced hyperbolic quaternions to extend the concept to 4-space. Problems in that algebra led to use of biquaternions after 1900. In a widely seen review, Macfarlane wrote:

... the root of a quadratic equation may be versor in nature or scalar in nature. If it is versor in nature, then the part affected by the radical involves the axis perpendicular to the plane of reference, and this is so, whether the radical involves the square root of minus one or not. In the former case the versor is circular, in the latter hyperbolic.

Today the concept of a one-parameter group subsumes the concepts of versor and hyperbolic versor as the terminology of Sophus Lie has replaced that of Hamilton and Macfarlane. In particular, for each **r** such that **r r** = +1 or **r r** = −1, the mapping $a\mapsto \exp(a\,\mathbf {r} )$ takes the real line to a group of hyperbolic or ordinary versors. In the ordinary case, when **r** and **−r** are antipodes on a sphere, the one-parameter groups have the same points but are oppositely directed. In physics, this aspect of rotational symmetry is termed a doublet.

Robb (1911) defined the parameter *rapidity*, which specifies a change in frame of reference. This *rapidity* parameter corresponds to the real variable in a one-parameter group of hyperbolic versors. With the further development of special relativity the action of a hyperbolic versor came to be called a Lorentz boost.

## Lie theory

Sophus Lie was less than a year old when Hamilton first described quaternions, but Lie's name has become associated with all groups generated by exponentiation. The set of versors with their multiplication has been denoted Sl(1,q) by Gilmore (1974). Sl(1,q) is the special linear group of one dimension over quaternions, the "special" indicating that all elements are of norm one. The group is isomorphic to SU(2,c), a special unitary group, a frequently used designation since quaternions and versors are sometimes considered archaic for group theory. The special orthogonal group SO(3,r) of rotations in three dimensions is closely related: it is a 2:1 homomorphic image of SU(2,c).

The subspace $\ \{\ x\ \mathbf {i} +y\ \mathbf {j} +z\ \mathbf {k} ~:~x,\ y,\ z\in \mathbb {R} \ \}\subset \mathbb {H} \$ is called the Lie algebra of the group of versors. The commutator $\ {\bigl [}\ u\ ,v\ {\bigr ]}\ \equiv \ u\ v-v\ u\ ,$ is double the cross product of two vectors, which forms the multiplication operation in the Lie algebra. The close relation to SU(1,c) and SO(3,r) is evident in the isomorphism of their Lie algebras.

Lie groups that contain hyperbolic versors include the group on the unit hyperbola and the special unitary group SU(1,1).

## Etymology

The word is derived from Latin *versari* = "to turn" with the suffix *-or* forming a noun from the verb (i.e. *versor* = "the turner"). It was introduced by William Rowan Hamilton in the 1840s in the context of his quaternion theory.

## Versors in geometric algebra

The term "versor" is generalised in geometric algebra to indicate a member R of the algebra that can be expressed as the product of invertible vectors, $R=v_{1}v_{2}\cdots v_{k}$ .

Just as a quaternion versor u can be used to represent a rotation of a quaternion q with mapping $q\mapsto u^{-1}qu$ , so can a versor R in Geometric Algebra be used to represent the result of k reflections on a member A of the algebra with mapping $A\mapsto (-1)^{k}RAR^{-1}$ .

A rotation can be considered the result of two reflections, so it turns out a quaternion versor u can be identified as a 2-versor $R=v_{1}v_{2}$ in the geometric algebra of three real dimensions ${\mathcal {G}}(3,0)$ .

In a departure from Hamilton's definition, multivector versors are not required to have unit norm, just to be invertible. Normalisation can still be useful however, so it is convenient to designate versors as *unit versors* in a geometric algebra if $R{\tilde {R}}=\pm 1$ , where the tilde denotes reversion of the versor.

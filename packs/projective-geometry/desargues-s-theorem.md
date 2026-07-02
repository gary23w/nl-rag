---
title: "Desargues's theorem"
source: https://en.wikipedia.org/wiki/Desargues's_theorem
domain: projective-geometry
license: CC-BY-SA-4.0
tags: projective geometry, projective plane, homogeneous coordinates, desargues theorem
fetched: 2026-07-02
---

# Desargues's theorem

In projective geometry, **Desargues's theorem**, named after Girard Desargues, states:

Two

triangles

are in

perspective

axially

if and only if

they are in perspective

centrally

.

Two triangles are in perspective axially if corresponding sides of the triangles, when extended, meet at points on a line, called the *axis of perspectivity*. Two triangles are in perspective centrally if the lines which run through corresponding vertices of the triangles meet at a point, called the *center of perspectivity*. Desargues's theorem states that the truth of the first condition is necessary and sufficient for the truth of the second.

This intersection theorem is true in the usual Euclidean plane but special care needs to be taken in exceptional cases, as when a pair of sides are parallel, so that their "point of intersection" recedes to infinity. Commonly, to remove these exceptions, mathematicians "complete" the Euclidean plane by adding points at infinity, following Jean-Victor Poncelet. This results in a projective plane.

Desargues's theorem is true for the real projective plane and for any projective space defined arithmetically from a field or division ring; that includes any projective space of dimension greater than two or in which Pappus's theorem holds. However, there are many "non-Desarguesian planes", in which Desargues's theorem is false.

## Formulation

Denote the three vertices of one triangle by *a*, *b* and *c*, and those of the other triangle by *A*, *B* and *C*. Let the vertices of separate triangles be connected by lines. Then lines *ab* and *AB* meet in a first point, lines *ac* and *AC* meet in a second point, and lines *bc* and *BC* meet in a third point. *Axial perspectivity* means these three points all lie on a common line called the *axis of perspectivity*. *Central perspectivity* means that the three lines *Aa*, *Bb* and *Cc* are concurrent, at a point called the *center of perspectivity*.

## History

Desargues never published this theorem, but it appeared in an appendix entitled *Universal Method of M. Desargues for Using Perspective* (*Manière universelle de M. Desargues pour practiquer la perspective*) to a practical book on the use of perspective published in 1648 by his friend and pupil Abraham Bosse (1602–1676).

## Coordinatization

The importance of Desargues's theorem in abstract projective geometry is due especially to the fact that a projective space satisfies that theorem if and only if it is isomorphic to a projective space defined over a field or division ring.

## Projective versus affine spaces

In an affine space such as the Euclidean plane a similar statement is true, but only if one lists various exceptions involving parallel lines. Desargues's theorem is therefore one of the simplest geometric theorems whose natural home is in projective rather than affine space.

## Self-duality

By definition, two triangles are perspective if and only if they are in perspective centrally (or, equivalently according to this theorem, in perspective axially). Note that perspective triangles need not be similar.

Under the standard duality of plane projective geometry (where points correspond to lines and collinearity of points corresponds to concurrency of lines), the statement of Desargues's theorem is self-dual: axial perspectivity is translated into central perspectivity and vice versa. The Desargues configuration (below) is a self-dual configuration.

This self-duality in the statement is due to the usual modern way of writing the theorem. Historically, the theorem only read, "In a projective space, a pair of centrally perspective triangles is axially perspective" and the dual of this statement was called the converse of Desargues's theorem and was always referred to by that name.

## Proof of Desargues's theorem

Desargues's theorem holds for projective space of any dimension over any field or division ring, and also holds for abstract projective spaces of dimension at least 3. In dimension 2 the planes for which it holds are called Desarguesian planes and are the same as the planes that can be given coordinates over a division ring. There are also many non-Desarguesian planes where Desargues's theorem does not hold.

### Three-dimensional proof

Desargues's theorem is true for any projective space of dimension at least 3, and more generally for any projective space that can be embedded in a space of dimension at least 3.

Desargues's theorem can be stated as follows:

If lines

Aa

,

Bb

and

Cc

are concurrent (meet at a point), then

the points

AB

∩

ab

,

AC

∩

ac

and

BC

∩

bc

are

collinear

.

The points *A*, *B*, *a* and *b* are coplanar (lie in the same plane) because of the assumed concurrency of *Aa* and *Bb*. Therefore, the lines *AB* and *ab* belong to the same plane and must intersect. Further, if the two triangles lie on different planes, then the point *AB* ∩ *ab* belongs to both planes. By a symmetric argument, the points *AC* ∩ *ac* and *BC* ∩ *bc* also exist and belong to the planes of both triangles. Since these two planes intersect in more than one point, their intersection is a line that contains all three points.

This proves Desargues's theorem if the two triangles are not contained in the same plane. If they are in the same plane, Desargues's theorem can be proved by choosing a point not in the plane, using this to lift the triangles out of the plane so that the argument above works, and then projecting back into the plane. The last step of the proof fails if the projective space has dimension less than 3, as in this case it is not possible to find a point not in the plane.

Monge's theorem also asserts that three points lie on a line, and has a proof using the same idea of considering it in three rather than two dimensions and writing the line as an intersection of two planes.

### Two-dimensional proof

As there are non-Desarguesian projective planes in which Desargues's theorem is not true, some extra conditions need to be met in order to prove it. These conditions usually take the form of assuming the existence of sufficiently many collineations of a certain type, which in turn leads to showing that the underlying algebraic coordinate system must be a division ring (skewfield).

## Relation to Pappus's theorem

Pappus's hexagon theorem states that, if a hexagon *AbCaBc* is drawn in such a way that vertices *a*, *b* and *c* lie on a line and vertices *A*, *B* and *C* lie on a second line, then each two opposite sides of the hexagon lie on two lines that meet in a point and the three points constructed in this way are collinear. A plane in which Pappus's theorem is universally true is called *Pappian*. Hessenberg (1905) showed that Desargues's theorem can be deduced from three applications of Pappus's theorem.

The converse of this result is not true, that is, not all Desarguesian planes are Pappian. Satisfying Pappus's theorem universally is equivalent to having the underlying coordinate system be commutative. A plane defined over a non-commutative division ring (a division ring that is not a field) would therefore be Desarguesian but not Pappian. However, due to Wedderburn's little theorem, which states that all *finite* division rings are fields, all *finite* Desarguesian planes are Pappian. There is no known completely geometric proof of this fact, although Bamberg & Penttila (2015) give a proof that uses only "elementary" algebraic facts (rather than the full strength of Wedderburn's little theorem).

## The Desargues configuration

The ten lines involved in Desargues's theorem (six sides of triangles, the three lines *Aa*, *Bb* and *Cc*, and the axis of perspectivity) and the ten points involved (the six vertices, the three points of intersection on the axis of perspectivity, and the center of perspectivity) are so arranged that each of the ten lines passes through three of the ten points, and each of the ten points lies on three of the ten lines. Those ten points and ten lines make up the Desargues configuration, an example of a projective configuration. Although Desargues's theorem chooses different roles for these ten lines and points, the Desargues configuration itself is more symmetric: *any* of the ten points may be chosen to be the center of perspectivity, and that choice determines which six points will be the vertices of triangles and which line will be the axis of perspectivity.

## The little Desargues theorem

This restricted version states that if two triangles are perspective from a point on a given line, and two pairs of corresponding sides also meet on this line, then the third pair of corresponding sides meet on the line as well. Thus, it is the specialization of Desargues's Theorem to only the cases in which the center of perspectivity lies on the axis of perspectivity.

A Moufang plane is a projective plane in which the little Desargues theorem is valid for every line.

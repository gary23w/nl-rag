---
title: "Geometric algebra (part 2/2)"
source: https://en.wikipedia.org/wiki/Geometric_algebra
domain: clifford-algebra
license: CC-BY-SA-4.0
tags: clifford algebra, geometric algebra, spinor field, gamma matrices
fetched: 2026-07-02
part: 2/2
---

## Geometric interpretation in the vector space model

### Projection and rejection

For any vector a and any invertible vector ⁠ m ⁠,

$a=amm^{-1}=(a\cdot m+a\wedge m)m^{-1}=a_{\|m}+a_{\perp m},$

where the **projection** of a onto m (or the parallel part) is

$a_{\|m}=(a\cdot m)m^{-1}$

and the **rejection** of a from m (or the orthogonal part) is

$a_{\perp m}=a-a_{\|m}=(a\wedge m)m^{-1}.$

Using the concept of a ⁠ k ⁠-blade ⁠ B ⁠ as representing a subspace of ⁠ V ⁠ and every multivector ultimately being expressed in terms of vectors, this generalizes to projection of a general multivector onto any invertible ⁠ k ⁠-blade ⁠ B ⁠ as

${\mathcal {P}}_{B}(A)=(A\;\rfloor \;B)\;\rfloor \;B^{-1},$

with the rejection being defined as

${\mathcal {P}}_{B}^{\perp }(A)=A-{\mathcal {P}}_{B}(A).$

The projection and rejection generalize to null blades B by replacing the inverse $B^{-1}$ with the pseudoinverse $B^{+}$ with respect to the contractive product. The outcome of the projection coincides in both cases for non-null blades. For null blades ⁠ B ⁠, the definition of the projection given here with the first contraction rather than the second being onto the pseudoinverse should be used, as only then is the result necessarily in the subspace represented by ⁠ B ⁠. The projection generalizes through linearity to general multivectors ⁠ A ⁠. The projection is not linear in ⁠ B ⁠ and does not generalize to objects ⁠ B ⁠ that are not blades.

### Reflection

Simple reflections in a hyperplane are readily expressed in the algebra through conjugation with a single vector. These serve to generate the group of general rotoreflections and rotations.

The reflection $c'$ of a vector c along a vector ⁠ m ⁠, or equivalently in the hyperplane orthogonal to ⁠ m ⁠, is the same as negating the component of a vector parallel to ⁠ m ⁠. The result of the reflection will be

$c'={-c_{\|m}+c_{\perp m}}={-(c\cdot m)m^{-1}+(c\wedge m)m^{-1}}={(-m\cdot c-m\wedge c)m^{-1}}=-mcm^{-1}$

This is not the most general operation that may be regarded as a reflection when the dimension ⁠ $n\geq 4$ ⁠. A general reflection may be expressed as the composite of any odd number of single-axis reflections. Thus, a general reflection $a'$ of a vector a may be written

$a\mapsto a'=-MaM^{-1},$

where

$M=pq\cdots r$

and

$M^{-1}=(pq\cdots r)^{-1}=r^{-1}\cdots q^{-1}p^{-1}.$

If we define the reflection along a non-null vector m of the product of vectors as the reflection of every vector in the product along the same vector, we get for any product of an odd number of vectors that, by way of example,

$(abc)'=a'b'c'=(-mam^{-1})(-mbm^{-1})(-mcm^{-1})=-ma(m^{-1}m)b(m^{-1}m)cm^{-1}=-mabcm^{-1}\,$

and for the product of an even number of vectors that

$(abcd)'=a'b'c'd'=(-mam^{-1})(-mbm^{-1})(-mcm^{-1})(-mdm^{-1})=mabcdm^{-1}.$

Using the concept of every multivector ultimately being expressed in terms of vectors, the reflection of a general multivector A using any reflection versor M may be written

$A\mapsto M\alpha (A)M^{-1},$

where $\alpha$ is the automorphism of reflection through the origin of the vector space (⁠ $v\mapsto -v$ ⁠) extended through linearity to the whole algebra.

### Rotations

If we have a product of vectors $R=a_{1}a_{2}\cdots a_{r}$ then we denote the reverse as

${\widetilde {R}}=a_{r}\cdots a_{2}a_{1}.$

As an example, assume that $R=ab$ we get

$R{\widetilde {R}}=abba=ab^{2}a=a^{2}b^{2}=ba^{2}b=baab={\widetilde {R}}R.$

Scaling R so that $R{\widetilde {R}}=1$ then

$(Rv{\widetilde {R}})^{2}=Rv^{2}{\widetilde {R}}=v^{2}R{\widetilde {R}}=v^{2}$

so $Rv{\widetilde {R}}$ leaves the length of v unchanged. We can also show that

$(Rv_{1}{\widetilde {R}})\cdot (Rv_{2}{\widetilde {R}})=v_{1}\cdot v_{2}$

so the transformation $Rv{\widetilde {R}}$ preserves both length and angle. It therefore can be identified as a rotation or rotoreflection; R is called a rotor if it is a proper rotation (as it is if it can be expressed as a product of an even number of vectors) and is an instance of what is known in GA as a *versor*.

There is a general method for rotating a vector involving the formation of a multivector of the form $R=e^{-B\theta /2}$ that produces a rotation $\theta$ in the plane and with the orientation defined by a ⁠ 2 ⁠-blade ⁠ B ⁠.

Rotors are a generalization of quaternions to ⁠ n ⁠-dimensional spaces.


## Examples and applications

### Hypervolume of a parallelotope spanned by vectors

For vectors ⁠ a ⁠ and ⁠ b ⁠ spanning a parallelogram we have

$a\wedge b=((a\wedge b)b^{-1})b=a_{\perp b}b$

with the result that ⁠ $a\wedge b$ ⁠ is linear in the product of the "altitude" and the "base" of the parallelogram, that is, its area.

Similar interpretations are true for any number of vectors spanning an ⁠ n ⁠-dimensional parallelotope; the exterior product of vectors ⁠ $a_{1},a_{2},\ldots ,a_{n}$ ⁠, that is ⁠ $\textstyle \bigwedge _{i=1}^{n}a_{i}$ ⁠, has a magnitude equal to the volume of the ⁠ n ⁠-parallelotope. An ⁠ n ⁠-vector does not necessarily have a shape of a parallelotope – this is a convenient visualization. It could be any shape, although the volume equals that of the parallelotope.

### Intersection of a line and a plane

We may define the line parametrically by ⁠ $p=t+\alpha \ v$ ⁠, where ⁠ p ⁠ and ⁠ t ⁠ are position vectors for points P and T and ⁠ v ⁠ is the direction vector for the line.

Then

$B\wedge (p-q)=0$

and

$B\wedge (t+\alpha v-q)=0$

so

$\alpha ={\frac {B\wedge (q-t)}{B\wedge v}}$

and

$p=t+\left({\frac {B\wedge (q-t)}{B\wedge v}}\right)v.$

### Rotating systems

A rotational quantity such as torque or angular momentum is described in geometric algebra as a bivector. Suppose a circular path in an arbitrary plane containing orthonormal vectors ⁠ ${\widehat {u}}$ ⁠ and ⁠ ${\widehat {\ \!v}}$ ⁠ is parameterized by angle.

$\mathbf {r} =r({\widehat {u}}\cos \theta +{\widehat {\ \!v}}\sin \theta )=r{\widehat {u}}(\cos \theta +{\widehat {u}}{\widehat {\ \!v}}\sin \theta )$

By designating the unit bivector of this plane as the imaginary number

${i}={\widehat {u}}{\widehat {\ \!v}}={\widehat {u}}\wedge {\widehat {\ \!v}}$

$i^{2}=-1$

this path vector can be conveniently written in complex exponential form

$\mathbf {r} =r{\widehat {u}}e^{i\theta }$

and the derivative with respect to angle is

${\frac {d\mathbf {r} }{d\theta }}=r{\widehat {u}}ie^{i\theta }=\mathbf {r} i.$

For example, torque is generally defined as the magnitude of the perpendicular force component times distance, or work per unit angle. Thus the torque, the rate of change of work ⁠ W ⁠ with respect to angle, due to a force ⁠ F ⁠, is

$\tau ={\frac {dW}{d\theta }}=F\cdot {\frac {dr}{d\theta }}=F\cdot (\mathbf {r} i).$

Rotational quantities are represented in vector calculus in three dimensions using the cross product. Together with a choice of an oriented volume form ⁠ I ⁠, these can be related to the exterior product with its more natural geometric interpretation of such quantities as a bivectors by using the dual relationship

$a\times b=-I(a\wedge b).$

Unlike the cross product description of torque, ⁠ $\tau =\mathbf {r} \times F$ ⁠, the geometric algebra description does not introduce a vector in the normal direction; a vector that does not exist in two and that is not unique in greater than three dimensions. The unit bivector describes the plane and the orientation of the rotation, and the sense of the rotation is relative to the angle between the vectors ⁠ ${\widehat {u}}$ ⁠ and ⁠ ${\widehat {\ \!v}}$ ⁠.


## Geometric calculus

Geometric calculus extends the formalism to include differentiation and integration including differential geometry and differential forms.

Essentially, the vector derivative is defined so that the GA version of Green's theorem is true,

$\int _{A}dA\,\nabla f=\oint _{\partial A}dx\,f$

and then one can write

$\nabla f=\nabla \cdot f+\nabla \wedge f$

as a geometric product, effectively generalizing Stokes' theorem (including the differential form version of it).

In 1D when ⁠ A ⁠ is a curve with endpoints ⁠ a ⁠ and ⁠ b ⁠, then

$\int _{A}dA\,\nabla f=\oint _{\partial A}dx\,f$

reduces to

$\int _{a}^{b}dx\,\nabla f=\int _{a}^{b}dx\cdot \nabla f=\int _{a}^{b}df=f(b)-f(a)$

or the fundamental theorem of integral calculus.

Also developed are the concept of vector manifold and geometric integration theory (which generalizes differential forms).


## History

### Before the 20th century

Although the connection of geometry with algebra dates as far back at least to Euclid's *Elements* in the third century B.C. (see Greek geometric algebra), GA in the sense used in this article was not developed until 1844, when it was used in a *systematic way* to describe the geometrical properties and *transformations* of a space. In that year, Hermann Grassmann introduced the idea of a geometrical algebra in full generality as a certain calculus (analogous to the propositional calculus) that encoded all of the geometrical information of a space. Grassmann's algebraic system could be applied to a number of different kinds of spaces, the chief among them being Euclidean space, affine space, and projective space. Following Grassmann, in 1878 William Kingdon Clifford examined Grassmann's algebraic system alongside the quaternions of William Rowan Hamilton in (Clifford 1878). From his point of view, the quaternions described certain *transformations* (which he called *rotors*), whereas Grassmann's algebra described certain *properties* (or *Strecken* such as length, area, and volume). His contribution was to define a new product – the *geometric product* – on an existing Grassmann algebra, which realized the quaternions as living within that algebra. Subsequently, Rudolf Lipschitz in 1886 generalized Clifford's interpretation of the quaternions and applied them to the geometry of rotations in ⁠ n ⁠ dimensions. Later these developments would lead other 20th-century mathematicians to formalize and explore the properties of the Clifford algebra.

Nevertheless, another revolutionary development of the 19th-century would completely overshadow the geometric algebras: that of vector analysis, developed independently by Josiah Willard Gibbs and Oliver Heaviside. Vector analysis was motivated by James Clerk Maxwell's studies of electromagnetism, and specifically the need to express and manipulate conveniently certain differential equations. Vector analysis had a certain intuitive appeal compared to the rigors of the new algebras. Physicists and mathematicians alike readily adopted it as their geometrical toolkit of choice, particularly following the influential 1901 textbook *Vector Analysis* by Edwin Bidwell Wilson, following lectures of Gibbs.

In more detail, there have been three approaches to geometric algebra: quaternionic analysis, initiated by Hamilton in 1843 and geometrized as rotors by Clifford in 1878; geometric algebra, initiated by Grassmann in 1844; and vector analysis, developed out of quaternionic analysis in the late 19th century by Gibbs and Heaviside. The legacy of quaternionic analysis in vector analysis can be seen in the use of ⁠ i ⁠, ⁠ j ⁠, ⁠ k ⁠ to indicate the basis vectors of ⁠ $\mathbf {R} ^{3}$ ⁠: it is being thought of as the purely imaginary quaternions. From the perspective of geometric algebra, the even subalgebra of the Space Time Algebra is isomorphic to the GA of 3D Euclidean space and quaternions are isomorphic to the even subalgebra of the GA of 3D Euclidean space, which unifies the three approaches.

### 20th century and present

Progress on the study of Clifford algebras quietly advanced through the twentieth century, although largely due to the work of abstract algebraists such as Élie Cartan, Hermann Weyl and Claude Chevalley. The *geometrical* approach to geometric algebras has seen a number of 20th-century revivals. In mathematics, Emil Artin's *Geometric Algebra* discusses the algebra associated with each of a number of geometries, including affine geometry, projective geometry, symplectic geometry, and orthogonal geometry. In physics, geometric algebras have been revived as a "new" way to do classical mechanics and electromagnetism, together with more advanced topics such as quantum mechanics and gauge theory. David Hestenes reinterpreted the Pauli and Dirac matrices as vectors in ordinary space and spacetime, respectively, and has been a primary contemporary advocate for the use of geometric algebra.

In computer graphics and robotics, geometric algebras have been revived in order to efficiently represent rotations and other transformations. For applications of GA in robotics (screw theory, kinematics and dynamics using versors), computer vision, control and neural computing (geometric learning) see Bayro (2010).

---
title: "Exterior algebra (part 2/2)"
source: https://en.wikipedia.org/wiki/Exterior_algebra
domain: exterior-algebra
license: CC-BY-SA-4.0
tags: exterior algebra, differential form, wedge product, exterior derivative
fetched: 2026-07-02
part: 2/2
---

## Applications

### Oriented volume in affine space

The natural setting for (oriented) k -dimensional volume and exterior algebra is affine space. This is also the intimate connection between exterior algebra and differential forms, as to integrate we need a 'differential' object to measure infinitesimal volume. If $\mathbb {A}$ is an affine space over the vector space ⁠ V ⁠, and a (simplex) collection of ordered $k+1$ points $A_{0},A_{1},...,A_{k}$ , we can define its oriented k -dimensional volume as the exterior product of vectors $A_{0}A_{1}\wedge A_{0}A_{2}\wedge \cdots \wedge A_{0}A_{k}={}$ $(-1)^{j}A_{j}A_{0}\wedge A_{j}A_{1}\wedge A_{j}A_{2}\wedge \cdots \wedge A_{j}A_{k}$ (using concatenation $PQ$ to mean the displacement vector from point P to Q ); if the order of the points is changed, the oriented volume changes by a sign, according to the parity of the permutation. In ⁠ n ⁠-dimensional space, the volume of any n -dimensional simplex is a scalar multiple of any other.

The sum of the $(k-1)$ -dimensional oriented areas of the boundary simplexes of a ⁠ k ⁠-dimensional simplex is zero, as for the sum of vectors around a triangle or the oriented triangles bounding the tetrahedron in the previous section.

The vector space structure on $\textstyle \bigwedge (V)$ generalises addition of vectors in ⁠ V ⁠: we have $(u_{1}+u_{2})\wedge v=u_{1}\wedge v+u_{2}\wedge v$ and similarly a *k*-blade $v_{1}\wedge \dots \wedge v_{k}$ is linear in each factor.

### Linear algebra

In applications to linear algebra, the exterior product provides an abstract algebraic manner for describing the determinant and the minors of a matrix. For instance, it is well known that the determinant of a square matrix is equal to the volume of the parallelotope whose sides are the columns of the matrix (with a sign to track orientation). This suggests that the determinant can be *defined* in terms of the exterior product of the column vectors. Likewise, the *k* × *k* minors of a matrix can be defined by looking at the exterior products of column vectors chosen *k* at a time. These ideas can be extended not just to matrices but to linear transformations as well: the determinant of a linear transformation is the factor by which it scales the oriented volume of any given reference parallelotope. So the determinant of a linear transformation can be defined in terms of what the transformation does to the top exterior power. The action of a transformation on the lesser exterior powers gives a basis-independent way to talk about the minors of the transformation.

### Physics

In physics, many quantities are naturally represented by alternating operators. For example, if the motion of a charged particle is described by velocity and acceleration vectors in four-dimensional spacetime, then normalization of the velocity vector requires that the electromagnetic force must be an alternating operator on the velocity. Its six degrees of freedom are identified with the electric and magnetic fields.

### Electromagnetic field

In Einstein's theories of relativity, the electromagnetic field is generally given as a differential 2-form $F=dA$ in 4-space or as the equivalent alternating tensor field $F_{ij}=A_{[i,j]}=A_{[i;j]},$ the electromagnetic tensor. Then $dF=ddA=0$ or the equivalent Bianchi identity $F_{[ij,k]}=F_{[ij;k]}=0.$ None of this requires a metric.

Adding the Lorentz metric and an orientation provides the Hodge star operator $\star$ and thus makes it possible to define $J={\star }d{\star }F$ or the equivalent tensor divergence $J^{i}=F_{,j}^{ij}=F_{;j}^{ij}$ where $F^{ij}=g^{ik}g^{jl}F_{kl}.$

### Linear geometry

The decomposable *k*-vectors have geometric interpretations: the bivector $u\wedge v$ represents the plane spanned by the vectors, "weighted" with a number, given by the area of the oriented parallelogram with sides u and ⁠ v ⁠. Analogously, the 3-vector $u\wedge v\wedge w$ represents the spanned 3-space weighted by the volume of the oriented parallelepiped with edges ⁠ u ⁠, ⁠ v ⁠, and ⁠ w ⁠.

### Projective geometry

Decomposable *k*-vectors in $\textstyle \bigwedge ^{\!k}(V)$ correspond to weighted *k*-dimensional linear subspaces of ⁠ V ⁠. In particular, the Grassmannian of *k*-dimensional subspaces of ⁠ V ⁠, denoted ⁠ $\operatorname {Gr} _{k}(V)$ ⁠, can be naturally identified with an algebraic subvariety of the projective space $\textstyle \mathbf {P} {\bigl (}\bigwedge ^{\!k}(V){\bigr )}$ . This is called the Plücker embedding, and the image of the embedding can be characterized by the Plücker relations.

### Differential geometry

The exterior algebra has notable applications in differential geometry, where it is used to define differential forms. Differential forms are mathematical objects that evaluate the length of vectors, areas of parallelograms, and volumes of higher-dimensional bodies, so they can be integrated over curves, surfaces and higher dimensional manifolds in a way that generalizes the line integrals and surface integrals from calculus. A differential form at a point of a differentiable manifold is an alternating multilinear form on the tangent space at the point. Equivalently, a differential form of degree *k* is a linear functional on the *k*th exterior power of the tangent space. As a consequence, the exterior product of multilinear forms defines a natural exterior product for differential forms. Differential forms play a major role in diverse areas of differential geometry.

An alternate approach defines differential forms in terms of germs of functions.

In particular, the exterior derivative gives the exterior algebra of differential forms on a manifold the structure of a differential graded algebra. The exterior derivative commutes with pullback along smooth mappings between manifolds, and it is therefore a natural differential operator. The exterior algebra of differential forms, equipped with the exterior derivative, is a cochain complex whose cohomology is called the de Rham cohomology of the underlying manifold and plays a vital role in the algebraic topology of differentiable manifolds.

### Representation theory

In representation theory, the exterior algebra is one of the two fundamental Schur functors on the category of vector spaces, the other being the symmetric algebra. Together, these constructions are used to generate the irreducible representations of the general linear group (see *Fundamental representation*).

### Superspace

The exterior algebra over the complex numbers is the archetypal example of a superalgebra, which plays a fundamental role in physical theories pertaining to fermions and supersymmetry. A single element of the exterior algebra is called a **supernumber** or Grassmann number. The exterior algebra itself is then just a one-dimensional superspace: it is just the set of all of the points in the exterior algebra. The topology on this space is essentially the weak topology, the open sets being the cylinder sets. An *n*-dimensional superspace is just the ⁠ n ⁠-fold product of exterior algebras.

### Lie algebra homology

Let L be a Lie algebra over a field ⁠ K ⁠, then it is possible to define the structure of a chain complex on the exterior algebra of ⁠ L ⁠. This is a ⁠ K ⁠-linear mapping

$\partial \colon {\textstyle \bigwedge ^{\!p+1}}(L)\to {\textstyle \bigwedge ^{\!p}}(L)$

defined on decomposable elements by

$\partial (x_{1}\wedge \cdots \wedge x_{p+1})={\frac {1}{p+1}}\sum _{j<\ell }(-1)^{j+\ell +1}[x_{j},x_{\ell }]\wedge x_{1}\wedge \cdots \wedge {\hat {x}}_{j}\wedge \cdots \wedge {\hat {x}}_{\ell }\wedge \cdots \wedge x_{p+1}.$

The Jacobi identity holds if and only if ⁠ ${1}$ ⁠, and so this is a necessary and sufficient condition for an anticommutative nonassociative algebra L to be a Lie algebra. Moreover, in that case $\textstyle \bigwedge (L)$ is a chain complex with boundary operator ⁠ $\partial$ ⁠. The homology associated to this complex is the Lie algebra homology.

### Homological algebra

The exterior algebra is the main ingredient in the construction of the Koszul complex, a fundamental object in homological algebra.


## History

The exterior algebra was first introduced by Hermann Grassmann in 1844 under the blanket term of *Ausdehnungslehre*, or *Theory of Extension*. This referred more generally to an algebraic (or axiomatic) theory of extended quantities and was one of the early precursors to the modern notion of a vector space. Saint-Venant also published similar ideas of exterior calculus for which he claimed priority over Grassmann.

The algebra itself was built from a set of rules, or axioms, capturing the formal aspects of Cayley and Sylvester's theory of multivectors. It was thus a *calculus*, much like the propositional calculus, except focused exclusively on the task of formal reasoning in geometrical terms. In particular, this new development allowed for an *axiomatic* characterization of dimension, a property that had previously only been examined from the coordinate point of view.

The import of this new theory of vectors and multivectors was lost to mid-19th-century mathematicians, until being thoroughly vetted by Giuseppe Peano in 1888. Peano's work also remained somewhat obscure until the turn of the century, when the subject was unified by members of the French geometry school (notably Henri Poincaré, Élie Cartan, and Gaston Darboux) who applied Grassmann's ideas to the calculus of differential forms.

A short while later, Alfred North Whitehead, borrowing from the ideas of Peano and Grassmann, introduced his universal algebra. This then paved the way for the 20th-century developments of abstract algebra by placing the axiomatic notion of an algebraic system on a firm logical footing.

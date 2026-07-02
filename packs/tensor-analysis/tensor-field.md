---
title: "Tensor field"
source: https://en.wikipedia.org/wiki/Tensor_field
domain: tensor-analysis
license: CC-BY-SA-4.0
tags: tensor calculus, covariant derivative, metric tensor, christoffel symbols
fetched: 2026-07-02
---

# Tensor field

In mathematics and physics, a **tensor field** is a function assigning a tensor to each point of a region of a mathematical space (typically a Euclidean space or manifold) or of a physical space, in which case the field quantity acquires a unit of measurement. Tensor fields are used in differential geometry, algebraic geometry, general relativity, in the analysis of stress and strain in material object, and in numerous applications in the physical sciences. As a tensor is a generalization of a scalar (a pure number representing a value, for example speed) and a vector (a magnitude and a direction, like velocity), a tensor field is a generalization of a *scalar field* and a *vector field* that assigns, respectively, a scalar or vector to each point of space. If a tensor A is defined on a vector fields set X(M) over a module M, we call A a tensor field on M. A tensor field, in common usage, is often referred to in the shorter form "tensor". For example, the *Riemann curvature tensor* refers a tensor *field*, as it associates a tensor to each point of a Riemannian manifold, a topological space.

## Definition

Let M be a manifold, for instance the Euclidean space $\mathbb {R} ^{n}$ .

> **Definition.** A **tensor field** of type $(p,q)$ is a section
> 
> $T\ \in \ \Gamma (M,V^{\otimes p}\otimes (V^{*})^{\otimes q})$
> 
> where $V=TM$ to be the tangent bundle of M (whose sections are called vector fields or contravariant vector fields in physics) and $V^{*}=T^{*}M$ is its dual bundle, the cotangent space (whose sections are called 1 forms, or covariant vector fields in physics), and $\otimes$ is the tensor product of vector bundles.

Equivalently, a tensor field is a collection of elements $T_{x}\in V_{x}^{\otimes p}\otimes (V_{x}^{*})^{\otimes q}$ for every point $x\in M$ , where $\otimes$ now denotes the tensor product of vectors spaces, such that it constitutes a smooth map $T:M\rightarrow V^{\otimes p}\otimes (V^{*})^{\otimes q}$ . The elements $T_{x}$ are called tensors.

Locally in a coordinate neighbourhood U with coordinates $x^{1},\ldots x^{n}$ we have a local basis (Vielbein) of vector fields $\partial _{1}={\frac {\partial }{\partial x^{1}}}\ldots \partial _{n}={\frac {\partial }{\partial x^{n}}}$ , and a dual basis of 1 forms $dx^{1},\ldots dx^{n}$ so that $dx^{i}(\partial _{j})=\partial _{j}x^{i}=\delta _{j}^{i}$ . In the coordinate neighbourhood U we then have $T_{x}=T_{j_{1},\ldots ,j_{q}}^{i_{1},\ldots i_{p}}(x^{1},\ldots ,x^{n})\partial _{i_{1}}\otimes \cdots \otimes \partial _{i_{p}}\otimes dx^{j_{1}}\otimes \cdots \otimes dx^{j_{q}}$ where here and below we use Einstein summation conventions. Note that if we choose different coordinate system $y^{1}\ldots y^{n}$ then ${\frac {\partial }{\partial x^{i}}}={\frac {\partial y^{k}}{\partial x^{i}}}{\frac {\partial }{\partial y^{k}}}$ and $dx^{j}={\frac {\partial x^{j}}{\partial y^{\ell }}}dy^{\ell }$ where the coordinates $(x^{1},\ldots ,x^{n})$ can be expressed in the coordinates $(y^{1},\ldots y^{n}$ and vice versa, so that

${\begin{aligned}T_{x}&=T_{j_{1},\ldots ,j_{q}}^{i_{1},\ldots i_{p}}(x^{1},\ldots ,x^{n}){\frac {\partial }{\partial x^{i_{1}}}}\otimes \cdots \otimes {\frac {\partial }{\partial x^{i_{p}}}}\otimes dx^{j_{1}}\otimes \cdots \otimes dx^{j_{q}}\\&=T_{j_{1},\ldots ,j_{q}}^{i_{1},\ldots i_{p}}(x^{1},\ldots ,x^{n}){\frac {\partial y^{k_{1}}}{\partial x^{i_{1}}}}\cdots {\frac {\partial y^{k_{p}}}{\partial x^{i_{p}}}}{\frac {\partial x^{j_{1}}}{\partial y^{\ell _{1}}}}\cdots {\frac {\partial x^{j_{q}}}{\partial y^{\ell _{q}}}}{\frac {\partial }{\partial y^{k_{1}}}}\otimes \cdots \otimes {\frac {\partial }{\partial y^{k_{p}}}}\otimes dy^{\ell _{1}}\otimes \cdots \otimes dy^{\ell _{q}}\\&=T_{\ell _{1},\cdots \ell _{q}}^{k_{1},\ldots ,k_{p}}(y^{1},\ldots y^{n}){\frac {\partial }{\partial y^{k_{1}}}}\otimes \cdots \otimes {\frac {\partial }{\partial y^{k_{p}}}}\otimes dy^{\ell _{1}}\otimes \cdots \otimes dy^{\ell _{q}}\\\end{aligned}}$ i.e. $T_{\ell _{1},\cdots \ell _{q}}^{k_{1},\ldots ,k_{p}}(y^{1},\ldots y^{n})=T_{j_{1},\ldots ,j_{q}}^{i_{1},\ldots i_{p}}(x^{1},\ldots ,x^{n}){\frac {\partial y^{k_{1}}}{\partial x^{i_{1}}}}\cdots {\frac {\partial y^{k_{p}}}{\partial x^{i_{p}}}}{\frac {\partial x^{j_{1}}}{\partial y^{\ell _{1}}}}\cdots {\frac {\partial x^{j_{q}}}{\partial y^{\ell _{q}}}}$ The system of indexed functions $T_{j_{1},\ldots ,j_{q}}^{i_{1},\ldots i_{p}}(x^{1},\ldots ,x^{n})$ (one system for each choice of coordinate system) connected by transformations as above are the tensors in the definitions below.

**Remark** One can, more generally, take V to be any vector bundle on M , and $V^{*}$ its dual bundle. In that case can be a more general topological space. These sections are called tensors of V or tensors for short if no confusion is possible .

## Geometric introduction

Intuitively, a vector field is best visualized as an "arrow" attached to each point of a region, with variable length and direction. One example of a vector field on a curved space is a weather map showing horizontal wind velocity at each point of the Earth's surface.

Now consider more complicated fields. For example, if the manifold is Riemannian, then it has a metric field g , such that given any two vectors $v,w$ at point x , their inner product is $g_{x}(v,w)$ . The field g could be given in matrix form, but it depends on a choice of coordinates. It could instead be given as an ellipsoid of radius 1 at each point, which is coordinate-free. Applied to the Earth's surface, this is Tissot's indicatrix.

In general, we want to specify tensor fields in a coordinate-independent way: It should exist independently of latitude and longitude, or whatever particular "cartographic projection" we are using to introduce numerical coordinates.

## Via coordinate transitions

Following Schouten (1951) and McConnell (1957), the concept of a tensor relies on a concept of a reference frame (or coordinate system), which may be fixed (relative to some background reference frame), but in general may be allowed to vary within some class of transformations of these coordinate systems.

For example, coordinates belonging to the *n*-dimensional real coordinate space $\mathbb {R} ^{n}$ may be subjected to arbitrary affine transformations:

$x^{k}\mapsto A_{j}^{k}x^{j}+a^{k}$

(with *n*-dimensional indices, summation implied). A covariant vector, or covector, is a system of functions $v_{k}$ that transforms under this affine transformation by the rule

$v_{k}\mapsto v_{i}A_{k}^{i}.$

The list of Cartesian coordinate basis vectors $\mathbf {e} _{k}$ transforms as a covector, since under the affine transformation $\mathbf {e} _{k}\mapsto A_{k}^{i}\mathbf {e} _{i}$ . A contravariant vector is a system of functions $v^{k}$ of the coordinates that, under such an affine transformation undergoes a transformation

$v^{k}\mapsto (A^{-1})_{j}^{k}v^{j}.$

This is precisely the requirement needed to ensure that the quantity $v^{k}\mathbf {e} _{k}$ is an invariant object that does not depend on the coordinate system chosen. More generally, the coordinates of a tensor of valence (*p*,*q*) have *p* upper indices and *q* lower indices, with the transformation law being

${T^{i_{1}\cdots i_{p}}}_{j_{1}\cdots j_{q}}\mapsto A_{i'_{1}}^{i_{1}}\cdots A_{i'_{p}}^{i_{p}}{T^{i'_{1}\cdots i'_{p}}}_{j'_{1}\cdots j'_{q}}(A^{-1})_{j_{1}}^{j'_{1}}\cdots (A^{-1})_{j_{q}}^{j'_{q}}.$

The concept of a tensor field may be obtained by specializing the allowed coordinate transformations to be smooth (or differentiable, analytic, etc.). A covector field is a function $v_{k}$ of the coordinates that transforms by the Jacobian of the transition functions (in the given class). Likewise, a contravariant vector field $v^{k}$ transforms by the inverse Jacobian.

## Tensor bundles

A tensor bundle is a fiber bundle where the fiber is a tensor product of any number of copies of the tangent space and/or cotangent space of the base space, which is a manifold. As such, the fiber is a vector space and the tensor bundle is a special kind of vector bundle.

The vector bundle is a natural idea of "vector space depending continuously (or smoothly) on parameters" – the parameters being the points of a manifold *M*. For example, a *vector space of one dimension depending on an angle* could look like a Möbius strip or alternatively like a cylinder. Given a vector bundle *V* over *M*, the corresponding field concept is called a *section* of the bundle: for *m* varying over *M*, a choice of vector

v

m

in

V

m

,

where *Vm* is the vector space "at" *m*.

Since the tensor product concept is independent of any choice of basis, taking the tensor product of two vector bundles on *M* is routine. Starting with the tangent bundle (the bundle of tangent spaces) the whole apparatus explained at component-free treatment of tensors carries over in a routine way – again independently of coordinates, as mentioned in the introduction.

We therefore can give a definition of **tensor field**, namely as a section of some tensor bundle. (There are vector bundles that are not tensor bundles: the Möbius band for instance.) This is then guaranteed geometric content, since everything has been done in an intrinsic way. More precisely, a tensor field assigns to any given point of the manifold a tensor in the space

$V\otimes \cdots \otimes V\otimes V^{*}\otimes \cdots \otimes V^{*},$

where *V* is the tangent space at that point and *V*∗ is the cotangent space. See also tangent bundle and cotangent bundle.

Given two tensor bundles *E* → *M* and *F* → *M*, a linear map *A*: Γ(*E*) → Γ(*F*) from the space of sections of *E* to sections of *F* can be considered itself as a tensor section of $\scriptstyle E^{*}\otimes F$ if and only if it satisfies *A*(*fs*) = *fA*(*s*), for each section *s* in Γ(*E*) and each smooth function *f* on *M*. Thus a tensor section is not only a linear map on the vector space of sections, but a *C*∞(*M*)-linear map on the module of sections. This property is used to check, for example, that even though the Lie derivative and covariant derivative are not tensors, the torsion and curvature tensors built from them are.

## Notation

The notation for tensor fields can sometimes be confusingly similar to the notation for tensor spaces. Thus, the tangent bundle *TM* = *T*(*M*) might sometimes be written as

$T_{0}^{1}(M)=T(M)=TM$

to emphasize that the tangent bundle is the range space of the (1,0) tensor fields (i.e., vector fields) on the manifold *M*. This should not be confused with the very similar looking notation

$T_{0}^{1}(V)$

;

in the latter case, we just have one tensor space, whereas in the former, we have a tensor space defined for each point in the manifold *M*.

Curly (script) letters are sometimes used to denote the set of infinitely-differentiable tensor fields on *M*. Thus,

${\mathcal {T}}_{n}^{m}(M)$

are the sections of the (*m*,*n*) tensor bundle on *M* that are infinitely-differentiable. A tensor field is an element of this set.

## Tensor fields as multilinear forms

There is another more abstract (but often useful) way of characterizing tensor fields on a manifold *M*, which makes tensor fields into honest tensors (i.e. *single* multilinear mappings), though of a different type (although this is *not* usually why one often says "tensor" when one really means "tensor field"). First, we may consider the set of all smooth (*C*∞) vector fields on *M*, ${\mathfrak {X}}(M):={\mathcal {T}}_{0}^{1}(M)$ (see the section on notation above) as a single space – a module over the ring of smooth functions, *C*∞(*M*), by pointwise scalar multiplication. The notions of multilinearity and tensor products extend easily to the case of modules over any commutative ring.

As a motivating example, consider the space $\Omega ^{1}(M)={\mathcal {T}}_{1}^{0}(M)$ of smooth covector fields (1-forms), also a module over the smooth functions. These act on smooth vector fields to yield smooth functions by pointwise evaluation, namely, given a covector field *ω* and a vector field *X*, we define

${\tilde {\omega }}(X)(p):=\omega (p)(X(p)).$

Because of the pointwise nature of everything involved, the action of ${\tilde {\omega }}$ on *X* is a *C*∞(*M*)-linear map, that is,

${\tilde {\omega }}(fX)(p)=\omega (p)((fX)(p))=\omega (p)(f(p)X(p))=f(p)\omega (p)(X(p))=(f\omega )(p)(X(p))=(f{\tilde {\omega }})(X)(p)$

for any *p* in *M* and smooth function *f*. Thus we can regard covector fields not just as sections of the cotangent bundle, but also linear mappings of vector fields into functions. By the double-dual construction, vector fields can similarly be expressed as mappings of covector fields into functions (namely, we could start "natively" with covector fields and work up from there).

In a complete parallel to the construction of ordinary single tensors (not tensor fields!) on *M* as multilinear maps on vectors and covectors, we can regard general (*k*,*l*) tensor fields on *M* as *C*∞(*M*)-multilinear maps defined on *k* copies of ${\mathfrak {X}}(M)$ and *l* copies of $\Omega ^{1}(M)$ into *C*∞(*M*).

Now, given any arbitrary mapping *T* from a product of *k* copies of ${\mathfrak {X}}(M)$ and *l* copies of $\Omega ^{1}(M)$ into *C*∞(*M*), it turns out that it arises from a tensor field on *M* if and only if it is multilinear over *C*∞(*M*). Namely *C*∞(*M*)-module of tensor fields of type $(k,l)$ over *M* is canonically isomorphic to *C*∞(*M*)-module of *C*∞(*M*)-multilinear forms

$\underbrace {\Omega ^{1}(M)\times \ldots \times \Omega ^{1}(M)} _{l\ \mathrm {times} }\times \underbrace {{\mathfrak {X}}(M)\times \ldots \times {\mathfrak {X}}(M)} _{k\ \mathrm {times} }\to C^{\infty }(M).$

This kind of multilinearity implicitly expresses the fact that we're really dealing with a pointwise-defined object, i.e. a tensor field, as opposed to a function which, even when evaluated at a single point, depends on all the values of vector fields and 1-forms simultaneously.

A frequent example application of this general rule is showing that the Levi-Civita connection, which is a mapping of smooth vector fields $(X,Y)\mapsto \nabla _{X}Y$ taking a pair of vector fields to a vector field, does not define a tensor field on *M*. This is because it is only $\mathbb {R}$ -linear in *Y* [in place of full *C*∞(*M*)-linearity, it satisfies the *Leibniz rule,* $\nabla _{X}(fY)=(Xf)Y+f\nabla _{X}Y$ ]. Nevertheless, it must be stressed that even though it is not a tensor field, it still qualifies as a geometric object with a component-free interpretation.

## Applications

The curvature tensor is discussed in differential geometry and the stress–energy tensor is important in physics, and these two tensors are related by Einstein's theory of general relativity.

In electromagnetism, the electric and magnetic fields are combined into an electromagnetic tensor field.

Differential forms, used in defining integration on manifolds, are a type of tensor field.

## Tensor calculus

In theoretical physics and other fields, differential equations posed in terms of tensor fields provide a very general way to express relationships that are both geometric in nature (guaranteed by the tensor nature) and conventionally linked to differential calculus. Even to formulate such equations requires a fresh notion, the covariant derivative. This handles the formulation of variation of a tensor field *along* a vector field. The original *absolute differential calculus* notion, which was later called *tensor calculus*, led to the isolation of the geometric concept of connection.

## Twisting by a line bundle

An extension of the tensor field idea incorporates an extra line bundle *L* on *M*. If *W* is the tensor product bundle of *V* with *L*, then *W* is a bundle of vector spaces of just the same dimension as *V*. This allows one to define the concept of **tensor density**, a 'twisted' type of tensor field. A *tensor density* is the special case where *L* is the bundle of *densities on a manifold*, namely the determinant bundle of the cotangent bundle. (To be strictly accurate, one should also apply the absolute value to the transition functions – this makes little difference for an orientable manifold.) For a more traditional explanation see the tensor density article.

One feature of the bundle of densities (again assuming orientability) *L* is that *L**s* is well-defined for real number values of *s*; this can be read from the transition functions, which take strictly positive real values. This means for example that we can take a *half-density*, the case where *s* = ⁠1/2⁠. In general we can take sections of *W*, the tensor product of *V* with *L**s*, and consider **tensor density fields** with weight *s*.

Half-densities are applied in areas such as defining integral operators on manifolds, and geometric quantization.

## Flat case

When *M* is a Euclidean space and all the fields are taken to be invariant by translations by the vectors of *M*, we get back to a situation where a tensor field is synonymous with a tensor 'sitting at the origin'. This does no great harm, and is often used in applications. As applied to tensor densities, it *does* make a difference. The bundle of densities cannot seriously be defined 'at a point'; and therefore a limitation of the contemporary mathematical treatment of tensors is that tensor densities are defined in a roundabout fashion.

## Cocycles and chain rules

As an advanced explanation of the *tensor* concept, one can interpret the chain rule in the multivariable case, as applied to coordinate changes, also as the requirement for self-consistent concepts of tensor giving rise to tensor fields.

Abstractly, we can identify the chain rule as a 1-cocycle. It gives the consistency required to define the tangent bundle in an intrinsic way. The other vector bundles of tensors have comparable cocycles, which come from applying functorial properties of tensor constructions to the chain rule itself; this is why they also are intrinsic (read, 'natural') concepts.

What is usually spoken of as the 'classical' approach to tensors tries to read this backwards – and is therefore a heuristic, *post hoc* approach rather than truly a foundational one. Implicit in defining tensors by how they transform under a coordinate change is the kind of self-consistency the cocycle expresses. The construction of tensor densities is a 'twisting' at the cocycle level. Geometers have not been in any doubt about the *geometric* nature of tensor *quantities*; this kind of descent argument justifies abstractly the whole theory.

## Generalizations

### Tensor densities

The concept of a tensor field can be generalized by considering objects that transform differently. An object that transforms as an ordinary tensor field under coordinate transformations, except that it is also multiplied by the determinant of the Jacobian of the inverse coordinate transformation to the *w*th power, is called a tensor density with weight *w*. Invariantly, in the language of multilinear algebra, one can think of tensor densities as multilinear maps taking their values in a density bundle such as the (1-dimensional) space of *n*-forms (where *n* is the dimension of the space), as opposed to taking their values in just **R**. Higher "weights" then just correspond to taking additional tensor products with this space in the range.

A special case are the scalar densities. Scalar 1-densities are especially important because it makes sense to define their integral over a manifold. They appear, for instance, in the Einstein–Hilbert action in general relativity. The most common example of a scalar 1-density is the volume element, which in the presence of a metric tensor *g* is the square root of its determinant in coordinates, denoted ${\sqrt {\det g}}$ . The metric tensor is a covariant tensor of order 2, and so its determinant scales by the square of the coordinate transition:

$\det(g')=\left(\det {\frac {\partial x}{\partial x'}}\right)^{2}\det(g),$

which is the transformation law for a scalar density of weight +2.

More generally, any tensor density is the product of an ordinary tensor with a scalar density of the appropriate weight. In the language of vector bundles, the determinant bundle of the tangent bundle is a line bundle that can be used to 'twist' other bundles *w* times. While locally the more general transformation law can indeed be used to recognise these tensors, there is a global question that arises, reflecting that in the transformation law one may write either the Jacobian determinant, or its absolute value. Non-integral powers of the (positive) transition functions of the bundle of densities make sense, so that the weight of a density, in that sense, is not restricted to integer values. Restricting to changes of coordinates with positive Jacobian determinant is possible on orientable manifolds, because there is a consistent global way to eliminate the minus signs; but otherwise the line bundle of densities and the line bundle of *n*-forms are distinct. For more on the intrinsic meaning, see *Density on a manifold*.

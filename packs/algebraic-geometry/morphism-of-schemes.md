---
title: "Morphism of schemes"
source: https://en.wikipedia.org/wiki/Morphism_of_schemes
domain: algebraic-geometry
license: CC-BY-SA-4.0
tags: algebraic geometry, algebraic variety, zariski topology, scheme theory
fetched: 2026-07-02
---

# Morphism of schemes

In algebraic geometry, a **morphism of schemes** generalizes a morphism of algebraic varieties just as a scheme generalizes an algebraic variety. It is, by definition, a morphism in the category of schemes.

A morphism of algebraic stacks generalizes a morphism of schemes.

## Definition

By definition, a morphism of schemes is just a morphism of locally ringed spaces. Isomorphisms are defined accordingly.

A scheme, by definition, has open affine charts and thus a morphism of schemes can also be described in terms of such charts (compare the definition of morphism of varieties). Let ƒ:*X*→*Y* be a morphism of schemes. If *x* is a point of *X*, since ƒ is continuous, there are open affine subsets *U* = Spec *A* of *X* containing *x* and *V* = Spec *B* of *Y* such that ƒ(*U*) ⊆ *V*. Then ƒ: *U* → *V* is a morphism of affine schemes and thus is induced by some ring homomorphism *B* → *A* (cf. #Affine case.) In fact, one can use this description to "define" a morphism of schemes; one says that ƒ:*X*→*Y* is a morphism of schemes if it is locally induced by ring homomorphisms between coordinate rings of affine charts.

- **Note**: It would not be desirable to define a morphism of schemes as a morphism of ringed spaces. One trivial reason is that there is an example of a ringed-space morphism between affine schemes that is not induced by a ring homomorphism (for example, a morphism of ringed spaces: $\operatorname {Spec} k(x)\to \operatorname {Spec} k[y]_{(y)}=\{\eta =(0),s=(y)\}$

that sends the unique point to

s

and that comes with

$k[y]_{(y)}\to k(x),\,y\mapsto x$

). More conceptually, the definition of a morphism of schemes needs to capture "

Zariski-local

nature" or

localization of rings

;

this point of view (i.e., a local-ringed space) is essential for a generalization (

topos

).

Let *f* : *X* → *Y* be a morphism of schemes with ${\displaystyle \phi$ . Then, for each point *x* of *X*, the homomorphism on the stalks:

${\displaystyle \phi$

is a local ring homomorphism: i.e., $\phi ({\mathfrak {m}}_{f(x)})\subseteq {\mathfrak {m}}_{x}$ and so induces an injective homomorphism of residue fields

$\phi :k(f(x))\hookrightarrow k(x)$

.

(In fact, φ maps th *n*-th power of a maximal ideal to the *n*-th power of the maximal ideal and thus induces the map between the (Zariski) cotangent spaces.)

For each scheme *X*, there is a natural morphism

$\theta :X\to \operatorname {Spec} \Gamma (X,{\mathcal {O}}_{X}),$

which is an isomorphism if and only if *X* is affine; θ is obtained by gluing *U* → target which come from restrictions to open affine subsets *U* of *X*. This fact can also be stated as follows: for any scheme *X* and a ring *A*, there is a natural bijection:

$\operatorname {Mor} (X,\operatorname {Spec} (A))\cong \operatorname {Hom} (A,\Gamma (X,{\mathcal {O}}_{X})).$

(Proof: The map $\phi \mapsto \operatorname {Spec} (\phi )\circ \theta$ from the right to the left is the required bijection. In short, θ is an adjunction.)

Moreover, this fact (adjoint relation) can be used to characterize an affine scheme: a scheme *X* is affine if and only if for each scheme *S*, the natural map

$\operatorname {Mor} (S,X)\to \operatorname {Hom} (\Gamma (X,{\mathcal {O}}_{X}),\Gamma (S,{\mathcal {O}}_{S}))$

is bijective. (Proof: if the maps are bijective, then $\operatorname {Mor} (-,X)\simeq \operatorname {Mor} (-,\operatorname {Spec} \Gamma (X,{\mathcal {O}}_{X}))$ and *X* is isomorphic to $\operatorname {Spec} \Gamma (X,{\mathcal {O}}_{X})$ by Yoneda's lemma; the converse is clear.)

## A morphism as a relative scheme

Fix a scheme *S*, called a **base scheme**. Then a morphism $p:X\to S$ is called a scheme over *S* or an *S*-scheme; the idea of the terminology is that it is a scheme *X* together with a map to the base scheme *S*. For example, a vector bundle *E* → *S* over a scheme *S* is an *S*-scheme.

An *S*-morphism from *p*:*X* →*S* to *q*:*Y* →*S* is a morphism ƒ:*X* →*Y* of schemes such that *p* = *q* ∘ ƒ. Given an *S*-scheme $X\to S$ , viewing *S* as an *S*-scheme over itself via the identity map, an *S*-morphism $S\to X$ is called a ***S*-section** or just a **section**.

All the *S*-schemes form a category: an object in the category is an *S*-scheme and a morphism in the category an *S*-morphism. (This category is the slice category of the category of schemes with the base object *S*.)

## Affine case

Let $\varphi :B\to A$ be a ring homomorphism and let

${\begin{cases}\varphi ^{a}:\operatorname {Spec} A\to \operatorname {Spec} B,\\{\mathfrak {p}}\mapsto \varphi ^{-1}({\mathfrak {p}})\end{cases}}$

be the induced map. Then

- $\varphi ^{a}$ is continuous.
- If $\varphi$ is surjective, then $\varphi ^{a}$ is a homeomorphism onto its image.
- For every ideal *I* of *A*, ${\overline {\varphi ^{a}(V(I))}}=V(\varphi ^{-1}(I)).$
- $\varphi ^{a}$ has dense image if and only if the kernel of $\varphi$ consists of nilpotent elements. (Proof: the preceding formula with *I* = 0.) In particular, when *B* is reduced, $\varphi ^{a}$ has dense image if and only if $\varphi$ is injective.

Let *f*: Spec *A* → Spec *B* be a morphism of schemes between affine schemes with the pullback map $\varphi$ : *B* → *A*. That it is a morphism of locally ringed spaces translates to the following statement: if $x={\mathfrak {p}}_{x}$ is a point of Spec *A*,

${\mathfrak {p}}_{f(x)}=\varphi ^{-1}({\mathfrak {p}}_{x})$

.

(Proof: In general, ${\mathfrak {p}}_{x}$ consists of *g* in *A* that has zero image in the residue field *k*(*x*); that is, it has the image in the maximal ideal ${\mathfrak {m}}_{x}$ . Thus, working in the local rings, $g(f(x))=0\Rightarrow \varphi (g)\in \varphi ({\mathfrak {m}}_{f(x))})\subseteq {\mathfrak {m}}_{x}\Rightarrow g\in \varphi ^{-1}({\mathfrak {m}}_{x})$ . If $g(f(x))\neq 0$ , then g is a unit element and so $\varphi (g)$ is a unit element.)

Hence, each ring homomorphism *B* → *A* defines a morphism of schemes Spec *A* → Spec *B* and, conversely, all morphisms between them arise this fashion.

## Examples

### Basic ones

- Let *R* be a field or $\mathbb {Z} .$ For each *R*-algebra *A*, to specify an element of *A*, say *f* in *A*, is to give a *R*-algebra homomorphism $R[t]\to A$ such that $t\mapsto f$ . Thus, $A=\operatorname {Hom} _{R-{\text{alg}}}(R[t],A)$ . If *X* is a scheme over *S* = Spec *R*, then taking $A=\Gamma (X,{\mathcal {O}}_{X})$ and using the fact Spec is a right adjoint to the global section functor, we get $\Gamma (X,{\mathcal {O}}_{X})=\operatorname {Mor} _{S}(X,\mathbb {A} _{S}^{1})$ where $\mathbb {A} _{S}^{1}=\operatorname {Spec} (R[t])$ . Note the equality is that of rings.
- Similarly, for any *S*-scheme *X*, there is the identification of the multiplicative groups: $\Gamma (X,{\mathcal {O}}_{X}^{*})=\operatorname {Mor} _{S}(X,\mathbb {G} _{m})$ where $\mathbb {G} _{m}=\operatorname {Spec} (R[t,t^{-1}])$ is the multiplicative group scheme.
- Many examples of morphisms come from families parameterized by some base space. For example, ${\text{Proj}}\left({\frac {\mathbb {C} [x,y][a,b,c]}{(ax^{2}+bxy+cy^{2})}}\right)\to {\text{Proj}}(\mathbb {C} [a,b,c])=\mathbb {P} _{a,b,c}^{2}$ is a projective morphism of projective varieties where the base space parameterizes quadrics in $\mathbb {P} ^{1}$ .

### Graph morphism

Given a morphism of schemes $f:X\to Y$ over a scheme *S*, the morphism $X\to X\times _{S}Y$ to the fiber product induced by the identity $1_{X}:X\to X$ and *f* is called the **graph morphism** of *f*. The graph morphism of the identity is called the diagonal morphism.

## Types of morphisms

### Finite type

Morphisms of finite type are one of the basic tools for constructing families of varieties. A morphism $f:X\to S$ is of finite type if there exists a cover $\operatorname {Spec} (A_{i})\to S$ such that the fibers $X\times _{S}\operatorname {Spec} (A_{i})$ can be covered by finitely many affine schemes $\operatorname {Spec} (B_{ij})$ making the induced ring morphisms $A_{i}\to B_{ij}$ into finite-type morphisms. A typical example of a finite-type morphism is a family of schemes. For example,

$\operatorname {Spec} \left({\frac {\mathbb {Z} [x,y,z]}{(x^{n}+zy^{n},z^{5}-1)}}\right)\to \operatorname {Spec} \left({\frac {\mathbb {Z} [z]}{(z^{5}-1)}}\right)$

is a morphism of finite type. A simple non-example of a morphism of finite-type is $\operatorname {Spec} (k[x_{1},x_{2},x_{3},\ldots ]))\to \operatorname {Spec} (k)$ where k is a field. Another is an infinite disjoint union

$\coprod ^{\infty }X\to X$

### Closed immersion

A morphism of schemes $i:Z\to X$ is a **closed immersion** if the following conditions hold:

1. i defines a homeomorphism of Z onto its image
2. $i^{\#}:{\mathcal {O}}_{X}\to i_{*}{\mathcal {O}}_{Z}$ is surjective.

This condition is equivalent to the following: given an affine open $\operatorname {Spec} (R)=U\subseteq X$ there exists an ideal $I\subseteq R$ such that $i^{-1}(U)=\operatorname {Spec} (R/I)$ .

#### Examples

Of course, any (graded) quotient $R/I$ defines a subscheme of $\operatorname {Spec} (R)$ ( $\operatorname {Proj} (R)$ ). Consider the quasi-affine scheme $\mathbb {A} ^{2}-\{0\}$ and the subset of the x -axis contained in X . Then if we take the open subset $\operatorname {Spec} (k[x,y,y^{-1}])$ the ideal sheaf is $(x)$ while on the affine open $\operatorname {Spec} (k[x,y,x^{-1}])$ there is no ideal since the subset does not intersect this chart.

### Separated

Separated morphisms define families of schemes which are analogous to Hausdorff topological spaces. For example, given a separated morphism $X\to S$ in ${\text{Sch}}/\mathbb {C}$ the associated analytic spaces $X(\mathbb {C} )^{an}\to S(\mathbb {C} )^{an}$ are both Hausdorff. We say a morphism of schemes $f:X\to S$ is separated if the diagonal morphism $\Delta _{X/S}:X\to X\times _{S}X$ is a closed immersion. In topology, an analogous condition for a space X to be Hausdorff is if the diagonal set

$\Delta =\{(x,x)\in X\times X\}$

is a closed subset of $X\times X$ . Nevertheless, most schemes are not Hausdorff as topological spaces, as the Zariski topology is in general highly non-Hausdorff.

#### Examples

Most morphisms encountered in scheme theory will be separated. For example, consider the affine scheme

$X=\operatorname {Spec} \left({\frac {\mathbb {C} [x,y]}{(f)}}\right)$

over $\operatorname {Spec} (\mathbb {C} ).$ Since the product scheme is

$X\times _{\mathbb {C} }X=\operatorname {Spec} \left({\frac {\mathbb {C} [x,y]}{(f)}}\otimes _{\mathbb {C} }{\frac {\mathbb {C} [x,y]}{(f)}}\right)$

the ideal defining the diagonal is generated by

$x\otimes 1-1\otimes x,y\otimes 1-1\otimes y$

showing the diagonal scheme is affine and closed. This same computation can be used to show that projective schemes are separated as well.

#### Non-examples

The only time care must be taken is when gluing together a family of schemes. For example, if we take the diagram of inclusions

${\begin{matrix}\operatorname {Spec} (R[x,x^{-1}])&&\\&\searrow &\\&&\operatorname {Spec} (R[x])\\&\nearrow &\\\operatorname {Spec} (R[x,x^{-1}])&&\end{matrix}}$

then we get the scheme-theoretic analogue of the classical line with two-origins.

### Proper

A morphism $f:X\to S$ is called proper if it is

1. separated
2. of finite type
3. universally closed.

The last condition means that given a morphism $S'\to S$ the base change morphism $S'\times _{S}X$ is a closed immersion. Most known examples of proper morphisms are in fact projective; but, examples of proper varieties which are not projective can be found using toric geometry.

### Projective

Projective morphisms define families of projective varieties over a fixed base scheme. Note that there are two definitions: Hartshorne's which states that a morphism $f:X\to S$ is called projective if there exists a closed immersion $X\to \mathbb {P} _{S}^{n}=\mathbb {P} ^{n}\times S$ and the EGA definition which states that a scheme $X\in {\text{Sch}}/S$ is projective if there is a quasi-coherent ${\mathcal {O}}_{S}$ -module of finite type such that there is a closed immersion $X\to \mathbb {P} _{S}({\mathcal {E}})$ . The second definition is useful because an exact sequence of ${\mathcal {O}}_{S}$ -modules can be used to define projective morphisms.

#### Projective morphism over a point

A projective morphism $f:X\to \{*\}$ defines a projective scheme. For example,

${\text{Proj}}\left({\frac {\mathbb {C} [x,y,z]}{(x^{n}+y^{n}-z^{n})}}\right)\to \operatorname {Spec} (\mathbb {C} )$

defines a projective curve of genus $(n-1)(n-1)/2$ over $\mathbb {C}$ .

#### Family of projective hypersurfaces

If we let $S=\mathbb {A} _{t}^{1}$ then the projective morphism

${\underline {\operatorname {Proj} }}_{S}\left({\frac {{\mathcal {O}}_{S}[x_{0},x_{1},x_{2},x_{3},x_{4}]}{\left(x_{0}^{5}+\cdots +x_{4}^{5}-tx_{0}x_{1}x_{2}x_{3}x_{4}\right)}}\right)\to S$

defines a family of Calabi-Yau manifolds which degenerate.

#### Lefschetz pencil

Another useful class of examples of projective morphisms are Lefschetz pencils: they are projective morphisms $\pi :X\to \mathbb {P} _{k}^{1}=\operatorname {Proj} (k[s,t])$ over some field k . For example, given smooth hypersurfaces $X_{1},X_{2}\subseteq \mathbb {P} _{k}^{n}$ defined by the homogeneous polynomials $f_{1},f_{2}$ there is a projective morphism

${\underline {\operatorname {Proj} }}_{\mathbb {P} ^{1}}\left({\frac {{\mathcal {O}}_{\mathbb {P} ^{1}}[x_{0},\ldots ,x_{n}]}{(sf_{1}+tf_{2})}}\right)\to \mathbb {P} ^{1}$

giving the pencil.

#### EGA projective

A nice classical example of a projective scheme is by constructing projective morphisms which factor through rational scrolls. For example, take $S=\mathbb {P} ^{1}$ and the vector bundle ${\mathcal {E}}={\mathcal {O}}_{S}\oplus {\mathcal {O}}_{S}\oplus {\mathcal {O}}_{S}(3)$ . This can be used to construct a $\mathbb {P} ^{2}$ -bundle $\mathbb {P} _{S}({\mathcal {E}})$ over S . If we want to construct a projective morphism using this sheaf we can take an exact sequence, such as

${\mathcal {O}}_{S}(-d)\oplus {\mathcal {O}}_{S}(-e)\to {\mathcal {E}}\to {\mathcal {O}}_{X}\to 0$

which defines the structure sheaf of the projective scheme X in $\mathbb {P} _{S}({\mathcal {E}}).$

### Flat

#### Intuition

Flat morphisms have an algebraic definition but have a very concrete geometric interpretation: flat families correspond to families of varieties which vary "continuously". For example,

$\operatorname {Spec} \left({\frac {\mathbb {C} [x,y,t]}{(xy-t))}}\right)\to \operatorname {Spec} (\mathbb {C} [t])$

is a family of smooth affine quadric curves which degenerate to the normal crossing divisor

$\operatorname {Spec} \left({\frac {\mathbb {C} [x,y]}{(xy)}}\right)$

at the origin.

#### Properties

One important property that a flat morphism must satisfy is that the dimensions of the fibers should be the same. A simple non-example of a flat morphism then is a blowup since the fibers are either points or copies of some $\mathbb {P} ^{n}$ .

#### Definition

Let $f:X\to S$ be a morphism of schemes. We say that f is flat at a point $x\in X$ if the induced morphism ${\mathcal {O}}_{f(x)}\to {\mathcal {O}}_{x}$ yields an exact functor $-\otimes _{{\mathcal {O}}_{f(x)}}{\mathcal {O}}_{x}.$ Then, f is **flat** if it is flat at every point of X . It is also **faithfully flat** if it is a surjective morphism.

#### Non-example

Using our geometric intuition it obvious that

$f:\operatorname {Spec} (\mathbb {C} [x,y]/(xy))\to \operatorname {Spec} (\mathbb {C} [x])$

is not flat since the fiber over 0 is $\mathbb {A} ^{1}$ with the rest of the fibers are just a point. But, we can also check this using the definition with local algebra: Consider the ideal ${\mathfrak {p}}=(x)\in \operatorname {Spec} (\mathbb {C} [x,y]/(xy)).$ Since $f({\mathfrak {p}})=(x)\in \operatorname {Spec} (\mathbb {C} [x])$ we get a local algebra morphism

$f_{\mathfrak {p}}:\left(\mathbb {C} [x]\right)_{(x)}\to \left(\mathbb {C} [x,y]/(xy)\right)_{(x)}$

If we tensor

$0\to \mathbb {C} [x]_{(x)}{\overset {\cdot x}{\longrightarrow }}\mathbb {C} [x]_{(x)}$

with $(\mathbb {C} [x,y]/(xy))_{(x)}$ , the map

$(\mathbb {C} [x,y]/(xy)))_{(x)}{\xrightarrow {\cdot x}}(\mathbb {C} [x,y]/(xy))_{(x)}$

has a non-zero kernel due the vanishing of $xy$ . This shows that the morphism is not flat.

### Unramified

A morphism $f:X\to Y$ of affine schemes is unramified if $\Omega _{X/Y}=0$ . We can use this for the general case of a morphism of schemes $f:X\to Y$ . We say that f is unramified at $x\in X$ if there is an affine open neighborhood $x\in U$ and an affine open $V\subseteq Y$ such that $f(U)\subseteq V$ and $\Omega _{U/V}=0.$ Then, the morphism is unramified if it is unramified at every point in X .

#### Geometric example

One example of a morphism which is flat and generically unramified, except for at a point, is

$\operatorname {Spec} \left({\frac {\mathbb {C} [t,x]}{(x^{n}-t)}}\right)\to \operatorname {Spec} (\mathbb {C} [t])$

We can compute the relative differentials using the sequence

${\frac {\mathbb {C} [t,x]}{(x^{n}-t)}}\otimes _{\mathbb {C} [t]}\mathbb {C} [t]dt\to \left({\frac {\mathbb {C} [t,x]}{(x^{n}-t)}}dt\oplus {\frac {\mathbb {C} [t,x]}{(x^{n}-t)}}dx\right)/(nx^{n-1}dx-dt)\to \Omega _{X/Y}\to 0$

showing

$\Omega _{X/Y}\cong \left({\frac {\mathbb {C} [t,x]}{(x^{n}-t)}}dx\right)/(x^{n-1}dx)\neq 0$

if we take the fiber $t=0$ , then the morphism is ramified since

$\Omega _{X_{0}/\mathbb {C} }=\left({\frac {\mathbb {C} [x]}{x^{n}}}dx\right)/(x^{n-1}dx)$

otherwise we have

$\Omega _{X_{\alpha }/\mathbb {C} }=\left({\frac {\mathbb {C} [x]}{(x^{n}-\alpha )}}dx\right)/(x^{n-1}dx)\cong {\frac {\mathbb {C} [x]}{(\alpha )}}dx\cong 0$

showing that it is unramified everywhere else.

### Étale

A morphism of schemes $f:X\to Y$ is called **étale** if it is flat and unramfied. These are the algebro-geometric analogue of covering spaces. The two main examples to think of are covering spaces and finite separable field extensions. Examples in the first case can be constructed by looking at branched coverings and restricting to the unramified locus.

## Morphisms as points

By definition, if *X*, *S* are schemes (over some base scheme or ring *B*), then a morphism from *S* to *X* (over *B*) is an *S*-point of *X* and one writes:

$X(S)=\{f\mid f:S\to X{\text{ over }}B\}$

for the set of all *S*-points of *X*. This notion generalizes the notion of solutions to a system of polynomial equations in classical algebraic geometry. Indeed, let *X* = Spec(*A*) with $A=B[t_{1},\dots ,t_{n}]/(f_{1},\dots ,f_{m})$ . For a *B*-algebra *R*, to give an *R*-point of *X* is to give an algebra homomorphism *A* →*R*, which in turn amounts to giving a homomorphism

$B[t_{1},\dots ,t_{n}]\to R,\,t_{i}\mapsto r_{i}$

that kills *f**i*'s. Thus, there is a natural identification:

$X(\operatorname {Spec} R)=\{(r_{1},\dots ,r_{n})\in R^{n}|f_{1}(r_{1},\dots ,r_{n})=\cdots =f_{m}(r_{1},\dots ,r_{n})=0\}.$

**Example**: If *X* is an *S*-scheme with structure map π: *X* → *S*, then an *S*-point of *X* (over *S*) is the same thing as a section of π.

In category theory, Yoneda's lemma says that, given a category *C*, the contravariant functor

$C\to {\mathcal {P}}(C)=\operatorname {Fct} (C^{\text{op}},\mathbf {Sets} ),\,X\mapsto \operatorname {Mor} (-,X)$

is fully faithful (where ${\mathcal {P}}(C)$ means the category of presheaves on *C*). Applying the lemma to *C* = the category of schemes over *B*, this says that a scheme over *B* is determined by its various points.

It turns out that in fact it is enough to consider *S*-points with only affine schemes *S*, precisely because schemes and morphisms between them are obtained by gluing affine schemes and morphisms between them. Because of this, one usually writes *X*(*R*) = *X*(Spec *R*) and view *X* as a functor from the category of commutative *B*-algebras to **Sets**.

**Example**: Given *S*-schemes *X*, *Y* with structure maps *p*, *q*,

$(X\times _{S}Y)(R)=X(R)\times _{S(R)}Y(R)=\{(x,y)\in X(R)\times Y(R)\mid p(x)=q(y)\}$

.

**Example**: With *B* still denoting a ring or scheme, for each *B*-scheme *X*, there is a natural bijection

$\mathbf {P} _{B}^{n}(X)=$

{ the isomorphism classes of line bundles

L

on

X

together with

n

+ 1 global sections generating

L

. };

in fact, the sections *s**i* of *L* define a morphism $X\to \mathbf {P} _{B}^{n},\,x\mapsto (s_{0}(x):\dots :s_{n}(x))$ . (See also Proj construction#Global Proj.)

**Remark**: The above point of view (which goes under the name functor of points and is due to Grothendieck) has had a significant impact on the foundations of algebraic geometry. For example, working with a category-valued (pseudo-)functor instead of a set-valued functor leads to the notion of a stack, which allows one to keep track of morphisms between points (i.e., morphisms between morphisms).

## Rational map

A rational map of schemes is defined in the same way for varieties. Thus, a rational map from a reduced scheme *X* to a separated scheme *Y* is an equivalence class of a pair $(U,f_{U})$ consisting of an open dense subset *U* of *X* and a morphism $f_{U}:U\to Y$ . If *X* is irreducible, a rational function on *X* is, by definition, a rational map from *X* to the affine line $\mathbb {A} ^{1}$ or the projective line $\mathbb {P} ^{1}.$

A rational map is dominant if and only if it sends the generic point to the generic point.

A ring homomorphism between function fields need not induce a dominant rational map (even just a rational map). For example, Spec *k*[*x*] and Spec *k*(*x*) and have the same function field (namely, *k*(*x*)) but there is no rational map from the former to the latter. However, it is true that any inclusion of function fields of algebraic varieties induces a dominant rational map (see morphism of algebraic varieties#Properties.)

---
title: "Ring (mathematics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Ring_(mathematics)
domain: ring-theory
license: CC-BY-SA-4.0
tags: ring theory, commutative ring, ring ideal, polynomial ring
fetched: 2026-07-02
part: 2/2
---

## Special kinds of rings

### Domains

A nonzero ring with no nonzero zero-divisors is called a domain. A commutative domain is called an integral domain. The most important integral domains are principal ideal domains, PIDs for short, and fields. A principal ideal domain is an integral domain in which every ideal is principal. An important class of integral domains that contain a PID is a unique factorization domain (UFD), an integral domain in which every nonunit element is a product of prime elements (an element is prime if it generates a prime ideal.) The fundamental question in algebraic number theory is on the extent to which the ring of (generalized) integers in a number field, where an "ideal" admits prime factorization, fails to be a PID.

Among theorems concerning a PID, the most important one is the structure theorem for finitely generated modules over a principal ideal domain. The theorem may be illustrated by the following application to linear algebra. Let V be a finite-dimensional vector space over a field k and *f* : *V* → *V* a linear map with minimal polynomial q. Then, since *k*[*t*] is a unique factorization domain, q factors into powers of distinct irreducible polynomials (that is, prime elements): $q=p_{1}^{e_{1}}\ldots p_{s}^{e_{s}}.$

Letting $t\cdot v=f(v),$ we make V a *k*[*t*]-module. The structure theorem then says V is a direct sum of cyclic modules, each of which is isomorphic to the module of the form $k[t]/\left(p_{i}^{k_{j}}\right).$ Now, if $p_{i}(t)=t-\lambda _{i},$ then such a cyclic module (for pi) has a basis in which the restriction of f is represented by a Jordan matrix. Thus, if, say, k is algebraically closed, then all pi's are of the form *t* – *λi* and the above decomposition corresponds to the Jordan canonical form of f.

In algebraic geometry, UFDs arise because of smoothness. More precisely, a point in a variety (over a perfect field) is smooth if the local ring at the point is a regular local ring. A regular local ring is a UFD.

The following is a chain of class inclusions that describes the relationship between rings, domains and fields:

rngs

⊃

rings

⊃

commutative rings

⊃

integral domains

⊃

integrally closed domains

⊃

GCD domains

⊃

unique factorization domains

⊃

principal ideal domains

⊃

Euclidean domains

⊃

fields

⊃

algebraically closed fields

### Division ring

A division ring is a ring such that every non-zero element is a unit. A commutative division ring is a field. A prominent example of a division ring that is not a field is the ring of quaternions. Any centralizer in a division ring is also a division ring. In particular, the center of a division ring is a field. It turned out that every *finite* domain (in particular finite division ring) is a field; in particular commutative (the Wedderburn's little theorem).

Every module over a division ring is a free module (has a basis); consequently, much of linear algebra can be carried out over a division ring instead of a field.

The study of conjugacy classes figures prominently in the classical theory of division rings; see, for example, the Cartan–Brauer–Hua theorem.

A cyclic algebra, introduced by L. E. Dickson, is a generalization of a quaternion algebra.

### Semisimple rings

A *semisimple module* is a direct sum of simple modules. A *semisimple ring* is a ring that is semisimple as a left module (or right module) over itself.

#### Examples

- A division ring is semisimple (and simple).
- For any division ring D and positive integer n, the matrix ring M*n*(*D*) is semisimple (and simple).
- For a field k and finite group G, the group ring *kG* is semisimple if and only if the characteristic of k does not divide the order of G (Maschke's theorem).
- Clifford algebras are semisimple.

The Weyl algebra over a field is a simple ring, but it is not semisimple. The same holds for a ring of differential operators in many variables.

#### Properties

Any module over a semisimple ring is semisimple. (Proof: A free module over a semisimple ring is semisimple and any module is a quotient of a free module.)

For a ring R, the following are equivalent:

- R is semisimple.
- R is artinian and semiprimitive.
- R is a finite direct product ${\textstyle \prod _{i=1}^{r}\operatorname {M} _{n_{i}}(D_{i})}$ where each *n**i* is a positive integer, and each *D**i* is a division ring (Artin–Wedderburn theorem).

Semisimplicity is closely related to separability. A unital associative algebra A over a field k is said to be separable if the base extension $A\otimes _{k}F$ is semisimple for every field extension *F* / *k*. If A happens to be a field, then this is equivalent to the usual definition in field theory (cf. separable extension.)

### Central simple algebra and Brauer group

For a field k, a k-algebra is central if its center is k and is simple if it is a simple ring. Since the center of a simple k-algebra is a field, any simple k-algebra is a central simple algebra over its center. In this section, a central simple algebra is assumed to have finite dimension. Also, we mostly fix the base field; thus, an algebra refers to a k-algebra. The matrix ring of size n over a ring R will be denoted by *R**n*.

The Skolem–Noether theorem states any automorphism of a central simple algebra is inner.

Two central simple algebras A and B are said to be *similar* if there are integers n and m such that $A\otimes _{k}k_{n}\approx B\otimes _{k}k_{m}.$ Since $k_{n}\otimes _{k}k_{m}\simeq k_{nm},$ the similarity is an equivalence relation. The similarity classes [*A*] with the multiplication $[A][B]=\left[A\otimes _{k}B\right]$ form an abelian group called the Brauer group of k and is denoted by Br(*k*). By the Artin–Wedderburn theorem, a central simple algebra is the matrix ring of a division ring; thus, each similarity class is represented by a unique division ring.

For example, Br(*k*) is trivial if k is a finite field or an algebraically closed field (more generally quasi-algebraically closed field; cf. Tsen's theorem). $\operatorname {Br} (\mathbb {R} )$ has order 2 (a special case of the theorem of Frobenius). Finally, if k is a nonarchimedean local field (for example, ⁠ $\mathbb {Q} _{p}$ ⁠), then $\operatorname {Br} (k)=\mathbb {Q} /\mathbb {Z}$ through the invariant map.

Now, if F is a field extension of k, then the base extension $-\otimes _{k}F$ induces Br(*k*) → Br(*F*). Its kernel is denoted by Br(*F* / *k*). It consists of [*A*] such that $A\otimes _{k}F$ is a matrix ring over F (that is, A is split by F.) If the extension is finite and Galois, then Br(*F* / *k*) is canonically isomorphic to $H^{2}\left(\operatorname {Gal} (F/k),k^{*}\right).$

Azumaya algebras generalize the notion of central simple algebras to a commutative local ring.

### Valuation ring

If K is a field, a valuation v is a group homomorphism from the multiplicative group *K*∗ to a totally ordered abelian group G such that, for any *f*, *g* in K with *f* + *g* nonzero, *v*(*f* + *g*) ≥ min{*v*(*f*), *v*(*g*)}. The valuation ring of v is the subring of K consisting of zero and all nonzero f such that *v*(*f*) ≥ 0.

Examples:

- The field of formal Laurent series $k(\!(t)\!)$ over a field k comes with the valuation v such that *v*(*f*) is the least degree of a nonzero term in f; the valuation ring of v is the formal power series ring $k[\![t]\!].$
- More generally, given a field k and a totally ordered abelian group G, let $k(\!(G)\!)$ be the set of all functions from G to k whose supports (the sets of points at which the functions are nonzero) are well ordered. It is a field with the multiplication given by convolution: $(f*g)(t)=\sum _{s\in G}f(s)g(t-s).$ It also comes with the valuation v such that *v*(*f*) is the least element in the support of f. The subring consisting of elements with finite support is called the group ring of G (which makes sense even if G is not commutative). If G is the ring of integers, then we recover the previous example (by identifying f with the series whose nth coefficient is *f*(*n*).)


## Rings with extra structure

A ring may be viewed as an abelian group (by using the addition operation), with extra structure: namely, ring multiplication. In the same way, there are other mathematical objects which may be considered as rings with extra structure. For example:

- An associative algebra is a ring that is also a vector space over a field such that the scalar multiplication is compatible with the ring multiplication. For instance, the set of n-by-n matrices over the real field ⁠ $\mathbb {R}$ ⁠ has dimension *n*2 as a real vector space.
- A ring R is a topological ring if its set of elements R is given a topology which makes the addition map ( $+:R\times R\to R$ ) and the multiplication map ⋅ : *R* × *R* → *R* to be both continuous as maps between topological spaces (where *X* × *X* inherits the product topology or any other product in the category). For example, n-by-n matrices over the real numbers could be given either the Euclidean topology, or the Zariski topology, and in either case one would obtain a topological ring.
- A λ-ring is a commutative ring R together with operations *λ**n*: *R* → *R* that are like nth exterior powers: $\lambda ^{n}(x+y)=\sum _{0}^{n}\lambda ^{i}(x)\lambda ^{n-i}(y).$

For example,

⁠

$\mathbb {Z}$

⁠

is a λ-ring with

$\lambda ^{n}(x)={\binom {x}{n}},$

the

binomial coefficients

. The notion plays a central rule in the algebraic approach to the

Riemann–Roch theorem

.

- A totally ordered ring is a ring with a total ordering that is compatible with ring operations.


## Some examples of the ubiquity of rings

Many different kinds of mathematical objects can be fruitfully analyzed in terms of some associated ring.

### Cohomology ring of a topological space

To any topological space X one can associate its integral cohomology ring

$H^{*}(X,\mathbb {Z} )=\bigoplus _{i=0}^{\infty }H^{i}(X,\mathbb {Z} ),$

a graded ring. There are also homology groups $H_{i}(X,\mathbb {Z} )$ of a space, and indeed these were defined first, as a useful tool for distinguishing between certain pairs of topological spaces, like the spheres and tori, for which the methods of point-set topology are not well-suited. Cohomology groups were later defined in terms of homology groups in a way which is roughly analogous to the dual of a vector space. To know each individual integral homology group is essentially the same as knowing each individual integral cohomology group, because of the universal coefficient theorem. However, the advantage of the cohomology groups is that there is a natural product, which is analogous to the observation that one can multiply pointwise a k-multilinear form and an l-multilinear form to get a (*k* + *l*)-multilinear form.

The ring structure in cohomology provides the foundation for characteristic classes of fiber bundles, intersection theory on manifolds and algebraic varieties, Schubert calculus and much more.

### Burnside ring of a group

To any group is associated its Burnside ring which uses a ring to describe the various ways the group can act on a finite set. The Burnside ring's additive group is the free abelian group whose basis is the set of transitive actions of the group and whose addition is the disjoint union of the action. Expressing an action in terms of the basis is decomposing an action into its transitive constituents. The multiplication is easily expressed in terms of the representation ring: the multiplication in the Burnside ring is formed by writing the tensor product of two permutation modules as a permutation module. The ring structure allows a formal way of subtracting one action from another. Since the Burnside ring is contained as a finite index subring of the representation ring, one can pass easily from one to the other by extending the coefficients from integers to the rational numbers.

### Representation ring of a group ring

To any group ring or Hopf algebra is associated its representation ring or "Green ring". The representation ring's additive group is the free abelian group whose basis are the indecomposable modules and whose addition corresponds to the direct sum. Expressing a module in terms of the basis is finding an indecomposable decomposition of the module. The multiplication is the tensor product. When the algebra is semisimple, the representation ring is just the character ring from character theory, which is more or less the Grothendieck group given a ring structure.

### Function field of an irreducible algebraic variety

To any irreducible algebraic variety is associated its function field. The points of an algebraic variety correspond to valuation rings contained in the function field and containing the coordinate ring. The study of algebraic geometry makes heavy use of commutative algebra to study geometric concepts in terms of ring-theoretic properties. Birational geometry studies maps between the subrings of the function field.

### Face ring of a simplicial complex

Every simplicial complex has an associated face ring, also called its Stanley–Reisner ring. This ring reflects many of the combinatorial properties of the simplicial complex, so it is of particular interest in algebraic combinatorics. In particular, the algebraic geometry of the Stanley–Reisner ring was used to characterize the numbers of faces in each dimension of simplicial polytopes.


## Category-theoretic description

Every ring can be thought of as a monoid in **Ab**, the category of abelian groups (thought of as a monoidal category under the tensor product of ⁠ $\mathbb {Z}$ ⁠-modules). The monoid action of a ring R on an abelian group is simply an R-module. Essentially, an R-module is a generalization of the notion of a vector space – where rather than a vector space over a field, one has a "vector space over a ring".

Let (*A*, +) be an abelian group and let End(*A*) be its endomorphism ring (see above). Note that, essentially, End(*A*) is the set of all morphisms of A, where if f is in End(*A*), and g is in End(*A*), the following rules may be used to compute *f* + *g* and *f* ⋅ *g*:

${\begin{aligned}&(f+g)(x)=f(x)+g(x)\\&(f\cdot g)(x)=f(g(x)),\end{aligned}}$

where + as in *f*(*x*) + *g*(*x*) is addition in A, and function composition is denoted from right to left. Therefore, associated to any abelian group, is a ring. Conversely, given any ring, (*R*, +, **⋅** ), (*R*, +) is an abelian group. Furthermore, for every r in R, right (or left) multiplication by r gives rise to a morphism of (*R*, +), by right (or left) distributivity. Let *A* = (*R*, +). Consider those endomorphisms of A, that "factor through" right (or left) multiplication of R. In other words, let End*R*(*A*) be the set of all morphisms m of A, having the property that *m*(*r* ⋅ *x*) = *r* ⋅ *m*(*x*). It was seen that every r in R gives rise to a morphism of A: right multiplication by r. It is in fact true that this association of any element of R, to a morphism of A, as a function from R to End*R*(*A*), is an isomorphism of rings. In this sense, therefore, any ring can be viewed as the endomorphism ring of some abelian X-group (by X-group, it is meant a group with X being its set of operators). In essence, the most general form of a ring, is the endomorphism group of some abelian X-group.

Any ring can be seen as a preadditive category with a single object. It is therefore natural to consider arbitrary preadditive categories to be generalizations of rings. And indeed, many definitions and theorems originally given for rings can be translated to this more general context. Additive functors between preadditive categories generalize the concept of ring homomorphism, and ideals in additive categories can be defined as sets of morphisms closed under addition and under composition with arbitrary morphisms.


## Generalization

Algebraists have defined structures more general than rings by weakening or dropping some of ring axioms.

### Rng

A rng is the same as a ring, except that the existence of a multiplicative identity is not assumed.

### Nonassociative ring

A nonassociative ring is an algebraic structure that satisfies all of the ring axioms except the associative property and the existence of a multiplicative identity. A notable example is a Lie algebra. There exists some structure theory for such algebras that generalizes the analogous results for Lie algebras and associative algebras.

### Semiring

A semiring (sometimes *rig*) is obtained by weakening the assumption that (*R*, +) is an abelian group to the assumption that (*R*, +) is a commutative monoid, and adding the axiom that 0 ⋅ *a* = *a* ⋅ 0 = 0 for all *a* in R (since it no longer follows from the other axioms).

Examples:

- the non-negative integers $\{0,1,2,\ldots \}$ with ordinary addition and multiplication;
- the tropical semiring.


## Other ring-like objects

### Ring object in a category

Let C be a category with finite products. Let pt denote a terminal object of C (an empty product). A **ring object** in C is an object R equipped with morphisms $R\times R\;{\stackrel {a}{\to }}\,R$ (addition), $R\times R\;{\stackrel {m}{\to }}\,R$ (multiplication), $\operatorname {pt} {\stackrel {0}{\to }}\,R$ (additive identity), $R\;{\stackrel {i}{\to }}\,R$ (additive inverse), and $\operatorname {pt} {\stackrel {1}{\to }}\,R$ (multiplicative identity) satisfying the usual ring axioms. Equivalently, a ring object is an object R equipped with a factorization of its functor of points $h_{R}=\operatorname {Hom} (-,R):C^{\operatorname {op} }\to \mathbf {Sets}$ through the category of rings: $C^{\operatorname {op} }\to \mathbf {Rings} {\stackrel {\textrm {forgetful}}{\longrightarrow }}\mathbf {Sets} .$

### Ring scheme

In algebraic geometry, a **ring scheme** over a base scheme S is a ring object in the category of S-schemes. One example is the ring scheme W*n* over ⁠ $\operatorname {Spec} \mathbb {Z}$ ⁠, which for any commutative ring A returns the ring W*n*(*A*) of p-isotypic Witt vectors of length n over A.

### Ring spectrum

In algebraic topology, a ring spectrum is a spectrum X together with a multiplication $\mu :X\wedge X\to X$ and a unit map *S* → *X* from the sphere spectrum S, such that the ring axiom diagrams commute up to homotopy. In practice, it is common to define a ring spectrum as a monoid object in a good category of spectra such as the category of symmetric spectra.

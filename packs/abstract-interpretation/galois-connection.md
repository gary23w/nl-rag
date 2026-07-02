---
title: "Galois connection"
source: https://en.wikipedia.org/wiki/Galois_connection
domain: abstract-interpretation
license: CC-BY-SA-4.0
tags: abstract interpretation, galois connection, abstract domain, widening operator
fetched: 2026-07-02
---

# Galois connection

In mathematics, especially in order theory, a **Galois connection** is a particular correspondence (typically) between two partially ordered sets (posets). Galois connections find applications in various mathematical theories. They generalize the fundamental theorem of Galois theory about the correspondence between subgroups and subfields, discovered by the French mathematician Évariste Galois.

A Galois connection can also be defined on preordered sets or classes; this article presents the common case of posets. The literature contains two closely related notions of "Galois connection". In this article, we will refer to them as **(monotone) Galois connections** and **antitone Galois connections**.

A Galois connection is rather weak compared to an order isomorphism between the involved posets, but every Galois connection gives rise to an isomorphism of certain sub-posets, as will be explained below. The term **Galois correspondence** is sometimes used to mean a bijective *Galois connection*; this is simply an order isomorphism (or dual order isomorphism, depending on whether we take monotone or antitone Galois connections).

## Definitions

### (Monotone) Galois connection

Let (*A*, ≤) and (*B*, ≤) be two partially ordered sets. A *monotone Galois connection* between these posets consists of two monotone functions, *F* : *A* → *B* and *G* : *B* → *A*, such that for all a in A and b in B, we have

F

(

a

) ≤

b

if and only if

a

≤

G

(

b

)

.

In this situation, F is called the **lower adjoint** of G and G is called the **upper adjoint** of *F*. Mnemonically, the upper/lower terminology refers to where the function application appears relative to ≤. The term "adjoint" refers to the fact that monotone Galois connections are special cases of pairs of adjoint functors in category theory as discussed further below. Other terminology encountered here is **left adjoint** (respectively **right adjoint**) for the lower (respectively upper) adjoint.

An essential property of a Galois connection is that an upper/lower adjoint of a Galois connection *uniquely* determines the other:

F

(

a

)

is the least element

~

b

with

a

≤

G

(

~

b

)

, and

G

(

b

)

is the largest element

~

a

with

F

(

~

a

) ≤

b

.

A consequence of this is that if F or G is bijective then each is the inverse of the other, i.e. *F* = *G* −1.

Given a Galois connection with lower adjoint F and upper adjoint G, we can consider the compositions *GF* : *A* → *A*, known as the associated closure operator, and *FG* : *B* → *B*, known as the associated kernel operator. Both are monotone and idempotent, and we have *a* ≤ *GF*(*a*) for all a in A and *FG*(*b*) ≤ *b* for all b in B.

A **Galois insertion** of B into A is a Galois connection in which the kernel operator FG is the identity on B, and hence G is an order isomorphism of B onto the set of closed elements GF [A] of A.

### Antitone Galois connection

The above definition is common in many applications today, and prominent in lattice and domain theory. However the original notion in Galois theory is slightly different. In this alternative definition, a Galois connection is a pair of *antitone*, i.e. order-reversing, functions *F* : *A* → *B* and *G* : *B* → *A* between two posets A and B, such that

b

≤

F

(

a

)

if and only if

a

≤

G

(

b

)

.

The symmetry of F and G in this version erases the distinction between upper and lower, and the two functions are then called **polarities** rather than adjoints. Each polarity uniquely determines the other, since

F

(

a

)

is the largest element

b

with

a

≤

G

(

b

)

, and

G

(

b

)

is the largest element

a

with

b

≤

F

(

a

)

.

The compositions *GF* : *A* → *A* and *FG* : *B* → *B* are the associated closure operators; they are monotone idempotent maps with the property *a* ≤ *GF*(*a*) for all a in A and *b* ≤ *FG*(*b*) for all b in B.

The implications of the two definitions of Galois connections are very similar, since an antitone Galois connection between A and B is just a monotone Galois connection between A and the order dual *B*op of B. All of the below statements on Galois connections can thus easily be converted into statements about antitone Galois connections.

## Examples

### Bijections

The bijection of a pair of functions $f:X\to Y$ and $g:Y\to X,$ each other's inverse, forms a (trivial) Galois connection, as follows. Because the equality relation is reflexive, transitive and antisymmetric, it is, trivially, a partial order, making $(X,=)$ and $(Y,=)$ partially ordered sets. Since $f(x)=y$ if and only if $x=g(y),$ we have a Galois connection.

### Monotone Galois connections

#### Floor; ceiling

A monotone Galois connection between $\mathbb {Z} ,$ the set of integers, and $\mathbb {R} ,$ the set of real numbers, each with its usual ordering, is given by the usual embedding function of the integers into the reals and the floor function truncating a real number to the greatest integer less than or equal to it. The embedding of integers is customarily done implicitly, but to show the Galois connection we make it explicit. So let $F:\mathbb {Z} \to \mathbb {R}$ denote the embedding function, with $F(n)=n\in \mathbb {R} ,$ while $G:\mathbb {R} \to \mathbb {Z}$ denotes the floor function, so $G(x)=\lfloor x\rfloor .$ The equivalence $F(n)\leq x~\Leftrightarrow ~n\leq G(x)$ then translates to

$n\leq x~\Leftrightarrow ~n\leq \lfloor x\rfloor .$

This is valid because the variable n is restricted to the integers. The well-known properties of the floor function, such as $\lfloor x+n\rfloor =\lfloor x\rfloor +n,$ can be derived by elementary reasoning from this Galois connection.

The dual orderings give another monotone Galois connection, now with the ceiling function:

$x\leq n~\Leftrightarrow ~\lceil x\rceil \leq n.$

#### Power set; implication and conjunction

For an order-theoretic example, let U be some set, and let A and B both be the power set of U, ordered by inclusion. Pick a fixed subset L of U. Then the maps F and G, where *F*(*M* ) = *L* ∩ *M*, and *G*(*N* ) = *N* ∪ (*U* \ *L*), form a monotone Galois connection, with F being the lower adjoint. A similar Galois connection whose lower adjoint is given by the meet (infimum) operation can be found in any Heyting algebra. Especially, it is present in any Boolean algebra, where the two mappings can be described by *F*(*x*) = (*a* ∧ *x*) and *G*(*y*) = (*y* ∨ ¬*a*) = (*a* ⇒ *y*). In logical terms: "implication from a" is the upper adjoint of "conjunction with a".

#### Lattices

Further interesting examples for Galois connections are described in the article on completeness properties. Roughly speaking, the usual functions ∨ and ∧ are lower and upper adjoints to the diagonal map *X* → *X* × *X*. The least and greatest elements of a partial order are given by lower and upper adjoints to the unique function *X* → {1}. Going further, even complete lattices can be characterized by the existence of suitable adjoints. These considerations give some impression of the ubiquity of Galois connections in order theory.

#### Transitive group actions

Let G act transitively on X and pick some point x in X. Consider

${\mathcal {B}}=\{B\subseteq X:x\in B;\forall g\in G,gB=B\ \mathrm {or} \ gB\cap B=\emptyset \},$

the set of **blocks** containing x. Further, let ${\mathcal {G}}$ consist of the subgroups of G containing the stabilizer of x.

Then, the correspondence ${\mathcal {B}}\to {\mathcal {G}}$ :

$B\mapsto H_{B}=\{g\in G:gx\in B\}$

is a monotone, one-to-one Galois connection. As a corollary, one can establish that doubly transitive actions have no blocks other than the trivial ones (singletons or the whole of X): this follows from the stabilizers being maximal in G in that case. See Doubly transitive group for further discussion.

#### Image and inverse image

If  *f* : *X* → *Y* is a function, then for any subset M of X we can form the image *F*(*M* ) =  *f* *M* = { *f* (*m*) | *m* ∈ *M*} and for any subset N of Y we can form the inverse image *G*(*N* ) =  *f* −1*N* = {*x* ∈ *X* |  *f* (*x*) ∈ *N*}. Then F and G form a monotone Galois connection between the power set of X and the power set of Y, both ordered by inclusion ⊆. There is a further adjoint pair in this situation: for a subset M of X, define *H*(*M*) = {*y* ∈ *Y* |  *f* −1{*y*} ⊆ *M*}. Then G and H form a monotone Galois connection between the power set of Y and the power set of X. In the first Galois connection, G is the upper adjoint, while in the second Galois connection it serves as the lower adjoint.

In the case of a quotient map between algebraic objects (such as groups), this connection is called the lattice theorem: subgroups of G connect to subgroups of *G*/*N*, and the closure operator on subgroups of G is given by *H* = *HN*.

#### Span and closure

Pick some mathematical object X that has an underlying set, for instance a group, ring, vector space, etc. For any subset S of X, let *F*(*S* ) be the smallest subobject of X that contains S, i.e. the subgroup, subring or subspace generated by S. For any subobject U of X, let *G*(*U* ) be the underlying set of U. (We can even take X to be a topological space, let *F*(*S* ) the closure of S, and take as "subobjects of X" the closed subsets of X.) Now F and G form a monotone Galois connection between subsets of X and subobjects of X, if both are ordered by inclusion. F is the lower adjoint.

#### Syntax and semantics

A very general comment of William Lawvere is that *syntax and semantics* are adjoint: take A to be the set of all logical theories (axiomatizations) reverse ordered by strength, and B the power set of the set of all mathematical structures. For a theory *T* ∈ *A*, let Mod(*T* ) be the set of all structures that satisfy the axioms T ; for a set of mathematical structures *S* ∈ *B*, let Th(*S* ) be the minimum of the axiomatizations that approximate S (in first-order logic, this is the set of sentences that are true in all structures in S). We can then say that S is a subset of Mod(*T* ) if and only if Th(*S* ) logically entails T: the "semantics functor" Mod and the "syntax functor" Th form a monotone Galois connection, with semantics being the upper adjoint.

### Antitone Galois connections

#### Galois theory

The motivating example comes from Galois theory: suppose *L*/*K* is a field extension. Let A be the set of all subfields of L that contain K, ordered by inclusion ⊆. If E is such a subfield, write Gal(*L*/*E*) for the group of field automorphisms of L that hold E fixed. Let B be the set of subgroups of Gal(*L*/*K*), ordered by inclusion ⊆. For such a subgroup G, define Fix(*G*) to be the field consisting of all elements of L that are held fixed by all elements of G. Then the maps *E* ↦ Gal(*L*/*E*) and *G* ↦ Fix(*G*) form an antitone Galois connection.

#### Algebraic topology: covering spaces

Analogously, given a path-connected topological space X, there is an antitone Galois connection between subgroups of the fundamental group *π*1(*X*) and path-connected covering spaces of X. In particular, if X is semi-locally simply connected, then for every subgroup G of *π*1(*X*), there is a covering space with G as its fundamental group.

#### Linear algebra: annihilators and orthogonal complements

Given an inner product space V, we can form the orthogonal complement *F*(*X* ) of any subspace X of V. This yields an antitone Galois connection between the set of subspaces of V and itself, ordered by inclusion; both polarities are equal to F.

Given a vector space V and a subset X of V we can define its annihilator *F*(*X* ), consisting of all elements of the dual space *V* ∗ of V that vanish on X. Similarly, given a subset Y of *V* ∗, we define its annihilator *G*(*Y* ) = {*x* ∈ *V* | *φ*(*x*) = 0 ∀*φ* ∈ *Y* }. This gives an antitone Galois connection between the subsets of V and the subsets of *V* ∗.

#### Algebraic geometry

In algebraic geometry, the relation between sets of polynomials and their zero sets is an antitone Galois connection.

Fix a natural number n and a field K and let A be the set of all subsets of the polynomial ring *K*[*X*1, ..., *Xn*] ordered by inclusion ⊆, and let B be the set of all subsets of *K* *n* ordered by inclusion ⊆. If S is a set of polynomials, define the variety of zeros as

$V(S)=\{x\in K^{n}:f(x)=0{\mbox{ for all }}f\in S\},$

the set of common zeros of the polynomials in S. If U is a subset of *K**n*, define *I*(*U* ) as the ideal of polynomials vanishing on U, that is

$I(U)=\{f\in K[X_{1},\dots ,X_{n}]:f(x)=0{\mbox{ for all }}x\in U\}.$

Then V and *I* form an antitone Galois connection.

The closure on *K* *n* is the closure in the Zariski topology, and if the field K is algebraically closed, then the closure on the polynomial ring is the radical of ideal generated by S.

More generally, given a commutative ring R (not necessarily a polynomial ring), there is an antitone Galois connection between radical ideals in the ring and Zariski closed subsets of the affine variety Spec(*R*).

More generally, there is an antitone Galois connection between ideals in the ring and subschemes of the corresponding affine variety.

#### Connections on power sets arising from binary relations

Suppose X and Y are arbitrary sets and a binary relation R over X and Y is given. For any subset M of X, we define *F*(*M* ) = {*y* ∈ *Y* | *mRy* ∀*m* ∈ *M* }. Similarly, for any subset N of Y, define *G*(*N* ) = {*x* ∈ *X* | *xRn* ∀*n* ∈ *N* }. Then F and G yield an antitone Galois connection between the power sets of X and Y, both ordered by inclusion ⊆.

Up to isomorphism *all* antitone Galois connections between power sets arise in this way. This follows from the "Basic Theorem on Concept Lattices". Theory and applications of Galois connections arising from binary relations are studied in formal concept analysis. That field uses Galois connections for mathematical data analysis. Many algorithms for Galois connections can be found in the respective literature, e.g., in.

The general concept lattice in its primitive version incorporates both the monotone and antitone Galois connections to furnish its upper and lower bounds of nodes for the concept lattice, respectively.

## Properties

In the following, we consider a (monotone) Galois connection  *f* = ( *f* ∗,  *f*∗), where  *f* ∗ : *A* → *B* is the lower adjoint as introduced above. Some helpful and instructive basic properties can be obtained immediately. By the defining property of Galois connections,  *f* ∗(*x*) ≤  *f* ∗(*x*) is equivalent to *x* ≤  *f*∗( *f* ∗(*x*)), for all x in A. By a similar reasoning (or just by applying the duality principle for order theory), one finds that  *f* ∗( *f*∗(*y*)) ≤ *y*, for all y in B. These properties can be described by saying the composite  *f* ∗∘ *f*∗ is *deflationary*, while  *f*∗∘ *f* ∗ is *inflationary* (or *extensive*).

Now consider *x*, *y* ∈ *A* such that *x* ≤ *y*. Then using the above one obtains *x* ≤  *f*∗( *f* ∗(*y*)). Applying the basic property of Galois connections, one can now conclude that  *f* ∗(*x*) ≤  *f* ∗(*y*). But this just shows that  *f* ∗ preserves the order of any two elements, i.e. it is monotone. Again, a similar reasoning yields monotonicity of  *f*∗. Thus monotonicity does not have to be included in the definition explicitly. However, mentioning monotonicity helps to avoid confusion about the two alternative notions of Galois connections.

Another basic property of Galois connections is the fact that  *f*∗( *f* ∗( *f*∗(*x*))) =  *f*∗(*x*), for all x in B. Clearly we find that

f

∗

(

f

∗

(

f

∗

(

x

))) ≥

f

∗

(

x

)

.

because  *f*∗∘ *f* ∗ is inflationary as shown above. On the other hand, since  *f* ∗∘ *f*∗ is deflationary, while  *f*∗ is monotonic, one finds that

f

∗

(

f

∗

(

f

∗

(

x

))) ≤

f

∗

(

x

)

.

This shows the desired equality. Furthermore, we can use this property to conclude that

f

∗

(

f

∗

(

f

∗

(

f

∗

(

x

)))) =

f

∗

(

f

∗

(

x

))

and

f

∗

(

f

∗

(

f

∗

(

f

∗

(

x

)))) =

f

∗

(

f

∗

(

x

))

i.e.,  *f* ∗∘ *f*∗ and  *f*∗∘ *f* ∗ are idempotent.

It can be shown (see Blyth or Erné for proofs) that a function  *f*  is a lower (respectively upper) adjoint if and only if  *f*  is a residuated mapping (respectively residual mapping). Therefore, the notion of residuated mapping and monotone Galois connection are essentially the same.

## Closure operators and Galois connections

The above findings can be summarized as follows: for a Galois connection, the composite  *f*∗∘ *f* ∗ is monotone (being the composite of monotone functions), inflationary, and idempotent. This states that  *f*∗∘ *f* ∗ is in fact a closure operator on A. Dually,  *f* ∗∘ *f*∗ is monotone, deflationary, and idempotent. Such mappings are sometimes called **kernel operators**. In the context of frames and locales, the composite  *f*∗∘ *f* ∗ is called the **nucleus** induced by  *f* . Nuclei induce frame homomorphisms; a subset of a locale is called a sublocale if it is given by a nucleus.

Conversely, any closure operator c on some poset A gives rise to the Galois connection with lower adjoint  *f* ∗ being just the corestriction of c to the image of c (i.e. as a surjective mapping the closure system *c*(*A*)). The upper adjoint  *f*∗ is then given by the inclusion of *c*(*A*) into A, that maps each closed element to itself, considered as an element of A. In this way, closure operators and Galois connections are seen to be closely related, each specifying an instance of the other. Similar conclusions hold true for kernel operators.

The above considerations also show that closed elements of A (elements x with  *f*∗( *f* ∗(*x*)) = *x*) are mapped to elements within the range of the kernel operator  *f* ∗∘ *f*∗, and vice versa.

## Existence and uniqueness of Galois connections

Another important property of Galois connections is that lower adjoints preserve all suprema that exist within their domain. Dually, upper adjoints preserve all existing infima. From these properties, one can also conclude monotonicity of the adjoints immediately. The adjoint functor theorem for order theory states that the converse implication is also valid in certain cases: especially, any mapping between complete lattices that preserves all suprema is the lower adjoint of a Galois connection.

In this situation, an important feature of Galois connections is that one adjoint uniquely determines the other. Hence one can strengthen the above statement to guarantee that any supremum-preserving map between complete lattices is the lower adjoint of a unique Galois connection. The main property to derive this uniqueness is the following: For every x in A,  *f* ∗(*x*) is the least element y of B such that *x* ≤  *f*∗(*y*). Dually, for every y in B,  *f*∗(*y*) is the greatest x in A such that  *f* ∗(*x*) ≤ *y*. The existence of a certain Galois connection now implies the existence of the respective least or greatest elements, no matter whether the corresponding posets satisfy any completeness properties. Thus, when one upper adjoint of a Galois connection is given, the other upper adjoint can be defined via this same property.

On the other hand, some monotone function  *f*  is a lower adjoint if and only if each set of the form {*x* ∈ *A* |  *f* (*x*) ≤ *b*}, for b in B, contains a greatest element. Again, this can be dualized for the upper adjoint.

## Galois connections as morphisms

Galois connections also provide an interesting class of mappings between posets which can be used to obtain categories of posets. Especially, it is possible to compose Galois connections: given Galois connections ( *f* ∗,  *f*∗) between posets A and B and (*g*∗, *g*∗) between B and C, the composite (*g*∗ ∘  *f* ∗,  *f*∗ ∘ *g*∗) is also a Galois connection. When considering categories of complete lattices, this can be simplified to considering just mappings preserving all suprema (or, alternatively, infima). Mapping complete lattices to their duals, these categories display auto duality, that are quite fundamental for obtaining other duality theorems. More special kinds of morphisms that induce adjoint mappings in the other direction are the morphisms usually considered for frames (or locales).

## Connection to category theory

Every partially ordered set can be viewed as a category in a natural way: there is a unique morphism from *x* to *y* if and only if *x* ≤ *y*. A monotone Galois connection is then nothing but a pair of adjoint functors between two categories that arise from partially ordered sets. In this context, the upper adjoint is the *right adjoint* while the lower adjoint is the *left adjoint*. However, this terminology is avoided for Galois connections, since there was a time when posets were transformed into categories in a dual fashion, i.e. with morphisms pointing in the opposite direction. This led to a complementary notation concerning left and right adjoints, which today is ambiguous.

### Adjoint functor theorem for posets

Let $f:L\rightarrow P$ be a monotone function from a complete lattice to a poset. Then the following are equivalent:

1. f preserves all meet,
2. f has a left adjoint.

And similarly: f preserves all join if and only if f has an right adjoint.

## Applications in the theory of programming

Galois connections may be used to describe many forms of abstraction in the theory of abstract interpretation of programming languages.

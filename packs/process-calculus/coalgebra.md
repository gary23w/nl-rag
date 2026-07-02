---
title: "Coalgebra"
source: https://en.wikipedia.org/wiki/Coalgebra
domain: process-calculus
license: CC-BY-SA-4.0
tags: process calculus, bisimulation equivalence, weak bisimulation, observational equivalence
fetched: 2026-07-02
---

# Coalgebra

In mathematics, **coalgebras** or **cogebras** are structures that are dual (in the category-theoretic sense of reversing arrows) to unital associative algebras. The axioms of unital associative algebras can be formulated in terms of commutative diagrams. Turning all arrows around, one obtains the axioms of coalgebras. Every coalgebra, by (vector space) duality, gives rise to an algebra, but not in general the other way. In finite dimensions, this duality goes in both directions (see below).

Coalgebras occur naturally in a number of contexts (for example, representation theory, universal enveloping algebras and group schemes).

There are also **F-coalgebras**, with important applications in computer science.

## Informal discussion

One frequently recurring example of coalgebras occurs in representation theory, and in particular, in the representation theory of the rotation group. A primary task, of practical use in physics, is to obtain combinations of systems with different states of angular momentum and spin. For this purpose, one uses the Clebsch–Gordan coefficients. Given two systems $A,B$ with angular momenta $j_{A}$ and $j_{B}$ , a particularly important task is to find the total angular momentum $j_{A}+j_{B}$ given the combined state $|A\rangle \otimes |B\rangle$ . This is provided by the total angular momentum operator, which extracts the needed quantity from each side of the tensor product. It can be written as an "external" tensor product

$\mathbf {J} \equiv \mathbf {j} \otimes 1+1\otimes \mathbf {j} .$

The word "external" appears here, in contrast to the "internal" tensor product of a tensor algebra. A tensor algebra comes with a tensor product (the internal one); it can also be equipped with a second tensor product, the "external" one, or the coproduct, having the form above. That they are two different products is emphasized by recalling that the internal tensor product of a vector and a scalar is just simple scalar multiplication. The external product keeps them separated. In this setting, the coproduct is the map

$\Delta :J\to J\otimes J$

that takes

$\Delta :\mathbf {j} \mapsto \mathbf {j} \otimes 1+1\otimes \mathbf {j} .$

For this example, J can be taken to be one of the spin representations of the rotation group, with the fundamental representation being the common-sense choice. This coproduct can be lifted to all of the tensor algebra, by a simple lemma that applies to free objects: the tensor algebra is a free algebra, therefore, any homomorphism defined on a subset can be extended to the entire algebra. Examining the lifting in detail, one observes that the coproduct behaves as the shuffle product, essentially because the two factors above, the left and right $\mathbf {j}$ must be kept in sequential order during products of multiple angular momenta (rotations are not commutative).

The peculiar form of having the $\mathbf {j}$ appear only once in the coproduct, rather than (for example) defining $\mathbf {j} \mapsto \mathbf {j} \otimes \mathbf {j}$ is in order to maintain linearity: for this example, (and for representation theory in general), the coproduct *must* be linear. As a general rule, the coproduct in representation theory is reducible; the factors are given by the Littlewood–Richardson rule. (The Littlewood–Richardson rule conveys the same idea as the Clebsch–Gordan coefficients, but in a more general setting.)

The formal definition of the coalgebra, below, abstracts away this particular special case, and its requisite properties, into a general setting.

## Formal definition

Formally, a coalgebra over a field *K* is a vector space *C* over *K* together with *K*-linear maps Δ: *C* → *C* ⊗ *C* and ε: *C* → *K* such that

1. $(\mathrm {id} _{C}\otimes \Delta )\circ \Delta =(\Delta \otimes \mathrm {id} _{C})\circ \Delta$
2. $(\mathrm {id} _{C}\otimes \varepsilon )\circ \Delta =\mathrm {id} _{C}=(\varepsilon \otimes \mathrm {id} _{C})\circ \Delta$ .

(Here ⊗ refers to the tensor product over *K* and id is the identity function.)

Equivalently, the following two diagrams commute:

In the first diagram, *C* ⊗ (*C* ⊗ *C*) is identified with (*C* ⊗ *C*) ⊗ *C*; the two are naturally isomorphic. Similarly, in the second diagram the naturally isomorphic spaces *C*, *C* ⊗ *K* and *K* ⊗ *C* are identified.

The first diagram is the dual of the one expressing associativity of algebra multiplication (called the **coassociativity** of the comultiplication); the second diagram is the dual of the one expressing the existence of a multiplicative identity. Accordingly, the map Δ is called the **comultiplication** (or **coproduct**) of *C* and ε is the **counit** of *C*.

## Examples

Take an arbitrary set *S* and form the *K*-vector space *C* = *K*(*S*) with basis *S*, as follows. The elements of this vector space *C* are those functions from *S* to *K* that map all but finitely many elements of *S* to zero; identify the element *s* of *S* with the function that maps *s* to 1 and all other elements of *S* to 0. Define

Δ(

s

) =

s

⊗

s

and ε(

s

) = 1 for all

s

in

S

.

By linearity, both Δ and ε can then uniquely be extended to all of *C*. The vector space *C* becomes a coalgebra with comultiplication Δ and counit ε.

As a second example, consider the polynomial ring *K*[*X*] in one indeterminate *X*. This becomes a coalgebra (the **divided power coalgebra**) if for all *n* ≥ 0 one defines:

$\Delta (X^{n})=\sum _{k=0}^{n}{\dbinom {n}{k}}X^{k}\otimes X^{n-k},$

$\varepsilon (X^{n})={\begin{cases}1&{\mbox{if }}n=0\\0&{\mbox{if }}n>0.\end{cases}}$

Again, because of linearity, this suffices to define Δ and ε uniquely on all of *K*[*X*]. Now *K*[*X*] is both a unital associative algebra and a coalgebra, and the two structures are compatible. Objects like this are called bialgebras, and in fact most of the important coalgebras considered in practice are bialgebras.

Examples of coalgebras include the tensor algebra, the exterior algebra, Hopf algebras and Lie bialgebras. Unlike the polynomial case above, none of these are commutative. Therefore, the coproduct becomes the shuffle product, rather than the divided power structure given above. The shuffle product is appropriate, because it preserves the order of the terms appearing in the product, as is needed by non-commutative algebras.

The singular homology of a topological space forms a graded coalgebra whenever the Künneth isomorphism holds, e.g. if the coefficients are taken to be a field.

If *C* is the *K*-vector space with basis {*s*, *c*}, consider Δ: *C* → *C* ⊗ *C* is given by

Δ(

s

) =

s

⊗

c

+

c

⊗

s

Δ(

c

) =

c

⊗

c

−

s

⊗

s

and ε: *C* → *K* is given by

ε(

s

) = 0

ε(

c

) = 1.

In this situation, (*C*, Δ, ε) is a coalgebra known as **trigonometric coalgebra**.

For a locally finite poset *P* with set of intervals *J*, define the **incidence coalgebra** *C* with *J* as basis. The comultiplication and counit are defined as

$\Delta [x,z]=\sum _{y\in [x,z]}[x,y]\otimes [y,z]{\text{ for }}x\leq z\ .$

$\varepsilon [x,y]={\begin{cases}1&{\text{if }}x=y,\\0&{\text{if }}x\neq y.\end{cases}}$

The intervals of length zero correspond to points of *P* and are group-like elements.

## Finite dimensions

In finite dimensions, the duality between algebras and coalgebras is closer: the dual of a finite-dimensional (unital associative) algebra is a coalgebra, while the dual of a finite-dimensional coalgebra is a (unital associative) algebra. In general, the dual of an algebra may not be a coalgebra.

The key point is that in finite dimensions, (*A* ⊗ *A*)∗ and *A*∗ ⊗ *A*∗ are isomorphic.

To distinguish these: in general, algebra and coalgebra are dual *notions* (meaning that their axioms are dual: reverse the arrows), while for finite dimensions, they are also dual *objects* (meaning that a coalgebra is the dual object of an algebra and conversely).

If *A* is a *finite-dimensional* unital associative *K*-algebra, then its *K*-dual *A*∗ consisting of all *K*-linear maps from *A* to *K* is a coalgebra. The multiplication of *A* can be viewed as a linear map *A* ⊗ *A* → *A*, which when dualized yields a linear map *A*∗ → (*A* ⊗ *A*)∗. In the finite-dimensional case, (*A* ⊗ *A*)∗ is naturally isomorphic to *A*∗ ⊗ *A*∗, so this defines a comultiplication on *A*∗. The counit of *A*∗ is given by evaluating linear functionals at 1.

## Sweedler notation

When working with coalgebras, a certain notation for the comultiplication simplifies the formulas considerably and has become quite popular. Given an element *c* of the coalgebra (*C*, Δ, ε), there exist elements *c*(*i* ) (1) and *c*(*i* ) (2) in *C* such that

$\Delta (c)=\sum _{i}c_{(1)}^{(i)}\otimes c_{(2)}^{(i)}.$

Note that neither the number of terms in this sum, nor the exact values of each $c_{(1)}^{(i)}$ or $c_{(2)}^{(i)}$ , are uniquely determined by c ; there is only a promise that there are finitely many terms, and that the full sum of all these terms $c_{(1)}^{(i)}\otimes c_{(2)}^{(i)}$ have the right value $\Delta (c)$ .

In *Sweedler's notation*, (so named after Moss Sweedler), this is abbreviated to

$\Delta (c)=\sum _{(c)}c_{(1)}\otimes c_{(2)}.$

The fact that ε is a counit can then be expressed with the following formula

$c=\sum _{(c)}\varepsilon (c_{(1)})c_{(2)}=\sum _{(c)}c_{(1)}\varepsilon (c_{(2)}).\;$

Here it is understood that the sums have the same number of terms, and the same lists of values for $c_{(1)}$ and $c_{(2)}$ , as in the previous sum for $\Delta (c)$ .

The coassociativity of Δ can be expressed as

$\sum _{(c)}c_{(1)}\otimes \left(\sum _{(c_{(2)})}(c_{(2)})_{(1)}\otimes (c_{(2)})_{(2)}\right)=\sum _{(c)}\left(\sum _{(c_{(1)})}(c_{(1)})_{(1)}\otimes (c_{(1)})_{(2)}\right)\otimes c_{(2)}.$

In Sweedler's notation, both of these expressions are written as

$\sum _{(c)}c_{(1)}\otimes c_{(2)}\otimes c_{(3)}.$

Some authors omit the summation symbols as well; in this sumless Sweedler notation, one writes

$\Delta (c)=c_{(1)}\otimes c_{(2)}$

and

$c=\varepsilon (c_{(1)})c_{(2)}=c_{(1)}\varepsilon (c_{(2)}).\;$

Whenever a variable with lowered and parenthesized index is encountered in an expression of this kind, a summation symbol for that variable is implied.

## Further concepts and facts

A coalgebra (*C*, Δ, *ε*) is called **co-commutative** if $\sigma \circ \Delta =\Delta$ , where σ: *C* ⊗ *C* → *C* ⊗ *C* is the *K*-linear map defined by *σ*(*c* ⊗ *d*) = *d* ⊗ *c* for all *c*, *d* in *C*. In Sweedler's sumless notation, *C* is co-commutative if and only if

$c_{(1)}\otimes c_{(2)}=c_{(2)}\otimes c_{(1)}$

for all *c* in *C*. (It's important to understand that the implied summation is significant here: it is not required that all the summands are pairwise equal, only that the sums are equal, a much weaker requirement.)

A **group-like element** (or **set-like element**) is an element *x* such that Δ(*x*) = *x* ⊗ *x* and *ε*(*x*) = 1. Contrary to what this naming convention suggests the group-like elements do not always form a group and in general they only form a set. The group-like elements of a Hopf algebra do form a group. A **primitive element** is an element *x* that satisfies Δ(*x*) = *x* ⊗ 1 + 1 ⊗ *x*. The primitive elements of a Hopf algebra form a Lie algebra.

If (*C*1, Δ1, *ε*1) and (*C*2, Δ2, *ε*2) are two coalgebras over the same field *K*, then a **coalgebra morphism** from *C*1 to *C*2 is a *K*-linear map *f* : *C*1 → *C*2 such that $(f\otimes f)\circ \Delta _{1}=\Delta _{2}\circ f$ and $\varepsilon _{2}\circ f=\varepsilon _{1}$ . In Sweedler's sumless notation, the first of these properties may be written as:

$f(c_{(1)})\otimes f(c_{(2)})=f(c)_{(1)}\otimes f(c)_{(2)}.$

The composition of two coalgebra morphisms is again a coalgebra morphism, and the coalgebras over *K* together with this notion of morphism form a category.

A linear subspace *I* in *C* is called a **coideal** if *I* ⊆ ker(*ε*) and Δ(*I*) ⊆ *I* ⊗ *C* + *C* ⊗ *I*. In that case, the quotient space *C*/*I* becomes a coalgebra in a natural fashion.

A subspace *D* of *C* is called a **subcoalgebra** if Δ(*D*) ⊆ *D* ⊗ *D*; in that case, *D* is itself a coalgebra, with the restriction of ε to *D* as counit.

The kernel of every coalgebra morphism *f* : *C*1 → *C*2 is a coideal in *C*1, and the image is a subcoalgebra of *C*2. The common isomorphism theorems are valid for coalgebras, so for instance *C*1/ker(*f*) is isomorphic to im(*f*).

If *A* is a finite-dimensional unital associative *K*-algebra, then *A*∗ is a finite-dimensional coalgebra, and indeed every finite-dimensional coalgebra arises in this fashion from some finite-dimensional algebra (namely from the coalgebra's *K*-dual). Under this correspondence, the commutative finite-dimensional algebras correspond to the cocommutative finite-dimensional coalgebras. So in the finite-dimensional case, the theories of algebras and of coalgebras are dual; studying one is equivalent to studying the other. However, relations diverge in the infinite-dimensional case: while the *K*-dual of every coalgebra is an algebra, the *K*-dual of an infinite-dimensional algebra need not be a coalgebra.

Every coalgebra is the sum of its finite-dimensional subcoalgebras, something that is not true for algebras. Abstractly, coalgebras are generalizations, or duals, of finite-dimensional unital associative algebras.

Corresponding to the concept of representation for algebras is a **corepresentation** or comodule.

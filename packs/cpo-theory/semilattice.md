---
title: "Semilattice"
source: https://en.wikipedia.org/wiki/Semilattice
domain: cpo-theory
license: CC-BY-SA-4.0
tags: complete partial order, directed-complete partial order, chain-complete poset, least upper bound
fetched: 2026-07-02
---

# Semilattice

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, a **join-semilattice** (or **upper semilattice**) is a partially ordered set that has a join (a least upper bound) for any nonempty finite subset. Dually, a **meet-semilattice** (or **lower semilattice**) is a partially ordered set which has a meet (or greatest lower bound) for any nonempty finite subset. Every join-semilattice is a meet-semilattice in the inverse order and vice versa.

Semilattices can also be defined algebraically: join and meet are associative, commutative, idempotent binary operations, and any such operation induces a partial order (and the respective inverse order) such that the result of the operation for any two elements is the least upper bound (or greatest lower bound) of the elements with respect to this partial order.

A lattice is a partially ordered set that is both a meet- and join-semilattice with respect to the same partial order. Algebraically, a lattice is a set with two associative, commutative, idempotent binary operations linked by corresponding absorption laws.

## Order-theoretic definition

A set *S* partially ordered by the binary relation ≤ is a *meet-semilattice* if

For all elements

x

and

y

of

S

, the

greatest lower bound

of the set

{

x

,

y

}

exists.

The greatest lower bound of the set {*x*, *y*} is called the meet of *x* and *y*, denoted *x* ∧ *y*.

Replacing "greatest lower bound" with "least upper bound" results in the dual concept of a *join-semilattice*. The least upper bound of {*x*, *y*} is called the join of *x* and *y*, denoted *x* ∨ *y*. Meet and join are binary operations on *S*. A simple induction argument shows that the existence of all possible pairwise suprema (infima), as per the definition, implies the existence of all non-empty finite suprema (infima).

A join-semilattice is **bounded** if it has a least element, the join of the empty set. Dually, a meet-semilattice is **bounded** if it has a greatest element, the meet of the empty set.

Other properties may be assumed; see the article on completeness in order theory for more discussion on this subject. That article also discusses how we may rephrase the above definition in terms of the existence of suitable Galois connections between related posets—an approach of special interest for category theoretic investigations of the concept.

## Algebraic definition

A *meet-semilattice* is an algebraic structure $\langle S,\land \rangle$ consisting of a set *S* with a binary operation ∧, called **meet**, such that for all members *x*, *y*, and *z* of *S*, the following identities hold:

**Associativity**

x

∧ (

y

∧

z

) = (

x

∧

y

) ∧

z

**Commutativity**

x

∧

y

=

y

∧

x

**Idempotency**

x

∧

x

=

x

A meet-semilattice $\langle S,\land \rangle$ is **bounded** if *S* includes an identity element 1 such that *x* ∧ 1 = *x* for all *x* in *S*.

If the symbol ∨, called **join**, replaces ∧ in the definition just given, the structure is called a *join-semilattice*. One can be ambivalent about the particular choice of symbol for the operation, and speak simply of *semilattices*.

A semilattice is a commutative, idempotent semigroup; i.e., a commutative band. A bounded semilattice is an idempotent commutative monoid.

A partial order is induced on a meet-semilattice by setting *x* ≤ *y* whenever *x* ∧ *y* = *x*. For a join-semilattice, the order is induced by setting *x* ≤ *y* whenever *x* ∨ *y* = *y*. In a bounded meet-semilattice, the identity 1 is the greatest element of *S*. Similarly, an identity element in a join semilattice is a least element.

## Connection between the two definitions

An order theoretic meet-semilattice ⟨*S*, ≤⟩ gives rise to a binary operation ∧ such that ⟨*S*, ∧⟩ is an algebraic meet-semilattice. Conversely, the meet-semilattice ⟨*S*, ∧⟩ gives rise to a binary relation ≤ that partially orders *S* in the following way: for all elements *x* and *y* in *S*, *x* ≤ *y* if and only if *x* = *x* ∧ *y*.

The relation ≤ introduced in this way defines a partial ordering from which the binary operation ∧ may be recovered. Conversely, the order induced by the algebraically defined semilattice ⟨*S*, ∧⟩ coincides with that induced by ≤.

Hence the two definitions may be used interchangeably, depending on which one is more convenient for a particular purpose. A similar conclusion holds for join-semilattices and the dual ordering ≥.

## Examples

Semilattices are employed to construct other order structures, or in conjunction with other completeness properties.

- A lattice is both a join- and a meet-semilattice. The interaction of these two semilattices via the absorption law is what truly distinguishes a lattice from a semilattice.
- The compact elements of an algebraic lattice, under the induced partial ordering, form a bounded join-semilattice.
- By induction on the number of elements, any non-empty finite meet semilattice has a least element and any non-empty finite join semilattice has a greatest element. (In neither case will the semilattice necessarily be bounded.)
- A totally ordered set is a distributive lattice, hence in particular a meet-semilattice and join-semilattice: any two distinct elements have a greater and lesser one, which are their meet and join.
  - A well-ordered set is further a *bounded* join-semilattice, as the set as a whole has a least element, hence it is bounded.
    - The natural numbers $\mathbb {N}$ , with their usual order ≤, are a bounded join-semilattice, with least element 0, although they have no greatest element: they are the smallest infinite well-ordered set.
- Any single-rooted tree (with the single root as the least element) of height $\leq \omega$ is a (generally unbounded) meet-semilattice. Consider for example the set of finite words over some alphabet, ordered by the prefix order. It has a least element (the empty word), which is an annihilator element of the meet operation, but no greatest (identity) element.
- A Scott domain is a meet-semilattice.
- Membership in any set *L* can be taken as a model of a semilattice with base set *L*, because a semilattice captures the essence of set extensionality. Let *a* ∧ *b* denote *a* ∈ *L* & *b* ∈ *L*. Two sets differing only in one or both of the:

1. Order in which their members are listed;
2. Multiplicity of one or more members,

are in fact the same set. Commutativity and associativity of

∧

assure (1),

idempotence

, (2). This semilattice is the

free semilattice

over

L

.

It is not bounded by

L

,

because a set is not a member of itself.

- Classical extensional mereology defines a join-semilattice, with join read as binary fusion. This semilattice is bounded from above by the world individual.
- Given a set *S*, the collection of partitions $\xi$ of *S* is a join-semilattice. In fact, the partial order is given by $\xi \leq \eta$ if $\forall Q\in \eta ,\exists P\in \xi$ such that $Q\subset P$ and the join of two partitions is given by $\xi \vee \eta =\{P\cap Q\mid P\in \xi \ \land \ Q\in \eta \}$ . This semilattice is bounded, with the least element being the singleton partition $\{S\}$ .

## Semilattice morphisms

The above algebraic definition of a semilattice suggests a notion of morphism between two semilattices. Given two join-semilattices (*S*, ∨) and (*T*, ∨), a homomorphism of (join-) semilattices is a function *f*: *S* → *T* such that

f

(

x

∨

y

) =

f

(

x

) ∨

f

(

y

).

Hence *f* is just a homomorphism of the two semigroups associated with each semilattice. If *S* and *T* both include a least element 0, then *f* should also be a monoid homomorphism, i.e. we additionally require that

f

(0) = 0.

In the order-theoretic formulation, these conditions just state that a homomorphism of join-semilattices is a function that preserves binary joins and least elements, if such there be. The obvious dual—replacing ∧ with ∨ and 0 with 1—transforms this definition of a join-semilattice homomorphism into its meet-semilattice equivalent.

Any semilattice homomorphism is necessarily monotone with respect to the associated ordering relation.

## Equivalence with algebraic lattices

There is a well-known equivalence between the category ${\mathcal {S}}$ of join-semilattices with zero with $(\vee ,0)$ -homomorphisms and the category ${\mathcal {A}}$ of algebraic lattices with compactness-preserving complete join-homomorphisms, as follows. With a join-semilattice S with zero, we associate its ideal lattice $\operatorname {Id} \ S$ . With a $(\vee ,0)$ -homomorphism $f\colon S\to T$ of $(\vee ,0)$ -semilattices, we associate the map $\operatorname {Id} \ f\colon \operatorname {Id} \ S\to \operatorname {Id} \ T$ , that with any ideal I of S associates the ideal of T generated by $f(I)$ . This defines a functor $\operatorname {Id} \colon {\mathcal {S}}\to {\mathcal {A}}$ . Conversely, with every algebraic lattice A we associate the $(\vee ,0)$ -semilattice $K(A)$ of all compact elements of A , and with every compactness-preserving complete join-homomorphism $f\colon A\to B$ between algebraic lattices we associate the restriction $K(f)\colon K(A)\to K(B)$ . This defines a functor $K\colon {\mathcal {A}}\to {\mathcal {S}}$ . The pair $(\operatorname {Id} ,K)$ defines a category equivalence between ${\mathcal {S}}$ and ${\mathcal {A}}$ .

## Distributive semilattices

Surprisingly, there is a notion of "distributivity" applicable to semilattices, even though distributivity conventionally requires the interaction of two binary operations. This notion requires but a single operation, and generalizes the distributivity condition for lattices. A join-semilattice is **distributive** if for all *a*, *b*, and *x* with *x* ≤ *a* ∨ *b* there exist *a'* ≤ *a* and *b'* ≤ *b* such that *x* = *a'* ∨ *b'*. Distributive meet-semilattices are defined dually. These definitions are justified by the fact that any distributive join-semilattice in which binary meets exist is a distributive lattice. See the entry distributivity (order theory).

A join-semilattice is distributive if and only if the lattice of its ideals (under inclusion) is distributive.

## Complete semilattices

Nowadays, the term "complete semilattice" has no generally accepted meaning, and various mutually inconsistent definitions exist. If completeness is taken to require the existence of all infinite joins, or all infinite meets, whichever the case may be, as well as finite ones, this immediately leads to partial orders that are in fact complete lattices. For why the existence of all possible infinite joins entails the existence of all possible infinite meets (and vice versa), see the entry completeness (order theory).

Nevertheless, the literature on occasion still takes complete join- or meet-semilattices to be complete lattices. In this case, "completeness" denotes a restriction on the scope of the homomorphisms. Specifically, a complete join-semilattice requires that the homomorphisms preserve all joins, but contrary to the situation we find for completeness properties, this does not require that homomorphisms preserve all meets. On the other hand, we can conclude that every such mapping is the lower adjoint of some Galois connection. The corresponding (unique) upper adjoint will then be a homomorphism of complete meet-semilattices. This gives rise to a number of useful categorical dualities between the categories of all complete semilattices with morphisms preserving all meets or joins, respectively.

Another usage of "complete meet-semilattice" refers to a bounded complete cpo. A complete meet-semilattice in this sense is arguably the "most complete" meet-semilattice that is not necessarily a complete lattice. Indeed, a complete meet-semilattice has all *non-empty* meets (which is equivalent to being bounded complete) and all directed joins. If such a structure has also a greatest element (the meet of the empty set), it is also a complete lattice. Thus a complete semilattice turns out to be "a complete lattice possibly lacking a top". This definition is of interest specifically in domain theory, where bounded complete algebraic cpos are studied as Scott domains. Hence Scott domains have been called *algebraic semilattices*.

Cardinality-restricted notions of completeness for semilattices have been rarely considered in the literature.

## Free semilattices

This section presupposes some knowledge of category theory. In various situations, free semilattices exist. For example, the forgetful functor from the category of join-semilattices (and their homomorphisms) to the category of sets (and functions) admits a left adjoint. Therefore, the free join-semilattice **F**(*S*) over a set *S* is constructed by taking the collection of all non-empty *finite* subsets of *S*, ordered by subset inclusion. Clearly, *S* can be embedded into **F**(*S*) by a mapping *e* that takes any element *s* in *S* to the singleton set {*s*}. Then any function *f* from a *S* to a join-semilattice *T* (more formally, to the underlying set of *T*) induces a unique homomorphism *f'* between the join-semilattices **F**(*S*) and *T*, such that *f* = *f'* ○ *e*. Explicitly, *f'* is given by ${\textstyle f'(A)=\bigvee \{f(s)|s\in A\}.}$ Now the obvious uniqueness of *f'* suffices to obtain the required adjunction—the morphism-part of the functor **F** can be derived from general considerations (see adjoint functors). The case of free meet-semilattices is dual, using the opposite subset inclusion as an ordering. For join-semilattices with bottom, we just add the empty set to the above collection of subsets.

In addition, semilattices often serve as generators for free objects within other categories. Notably, both the forgetful functors from the category of frames and frame-homomorphisms, and from the category of distributive lattices and lattice-homomorphisms, have a left adjoint.

---
title: "Gelfand representation"
source: https://en.wikipedia.org/wiki/Gelfand_representation
domain: operator-algebras
license: CC-BY-SA-4.0
tags: operator algebra, von neumann algebra, banach algebra, gelfand representation
fetched: 2026-07-02
---

# Gelfand representation

In mathematics, the **Gelfand representation** in functional analysis (named after I. M. Gelfand) is either of two things:

- a way of representing commutative Banach algebras as algebras of continuous functions;
- the fact that for commutative C*-algebras, this representation is an isometric isomorphism.

In the former case, one may regard the Gelfand representation as a far-reaching generalization of the Fourier transform of an integrable function. In the latter case, the Gelfand–Naimark representation theorem is one avenue in the development of spectral theory for normal operators, and generalizes the notion of diagonalizing a normal matrix.

## Historical remarks

One of Gelfand's original applications (and one which historically motivated much of the study of Banach algebras) was to give a much shorter and more conceptual proof of a celebrated lemma of Norbert Wiener (see the citation below), characterizing the elements of the group algebras *L*1(**R**) and $\ell ^{1}({\mathbf {Z} })$ whose translates span dense subspaces in the respective algebras.

## The model algebra

For any locally compact Hausdorff topological space *X*, the space *C*0(*X*) of continuous complex-valued functions on *X* which vanish at infinity is in a natural way a commutative C*-algebra:

- The algebra structure over the complex numbers is obtained by considering the pointwise operations of addition and multiplication.
- The involution is pointwise complex conjugation.
- The norm is the uniform norm on functions.

The importance of *X* being locally compact and Hausdorff is that this turns *X* into a completely regular space. In such a space every closed subset of *X* is the common zero set of a family of continuous complex-valued functions on *X*, allowing one to recover the topology of *X* from *C*0(*X*).

Note that *C*0(*X*) is unital if and only if *X* is compact, in which case *C*0(*X*) is equal to *C*(*X*), the algebra of all continuous complex-valued functions on *X*.

## Gelfand representation of a commutative Banach algebra

Let A be a commutative Banach algebra, defined over the field $\mathbb {C}$ of complex numbers. A non-zero algebra homomorphism (a multiplicative linear functional) $\Phi \colon A\to \mathbb {C}$ is called a *character* of A ; the set of all characters of A is denoted by $\Phi _{A}$ .

It can be shown that every character on A is automatically continuous, and hence $\Phi _{A}$ is a subset of the space $A^{*}$ of continuous linear functionals on A ; moreover, when equipped with the relative weak-* topology, $\Phi _{A}$ turns out to be locally compact and Hausdorff. (This follows from the Banach–Alaoglu theorem.) The space $\Phi _{A}$ is compact (in the topology just defined) if and only if the algebra A has an identity element.

Given $a\in A$ , one defines the function ${\widehat {a}}:\Phi _{A}\to {\mathbb {C} }$ by ${\widehat {a}}(\phi )=\phi (a)$ . The definition of $\Phi _{A}$ and the topology on it ensure that ${\widehat {a}}$ is continuous and vanishes at infinity, and that the map $a\mapsto {\widehat {a}}$ defines a norm-decreasing, unit-preserving algebra homomorphism from A to $C_{0}(\Phi _{A})$ . This homomorphism is the *Gelfand representation of A*, and ${\widehat {a}}$ is the *Gelfand transform* of the element a . In general, the representation is neither injective nor surjective.

In the case where A has an identity element, there is a bijection between $\Phi _{A}$ and the set of maximal ideals in A (this relies on the Gelfand–Mazur theorem). As a consequence, the kernel of the Gelfand representation $A\to C_{0}(\Phi _{A})$ may be identified with the Jacobson radical of A . Thus the Gelfand representation is injective if and only if A is (Jacobson) semisimple.

### Examples

The Banach space $A=L^{1}(\mathbb {R} )$ is a Banach algebra under the convolution, the group algebra of $\mathbb {R}$ . Then $\Phi _{A}$ is homeomorphic to $\mathbb {R}$ and the Gelfand transform of $f\in L^{1}(\mathbb {R} )$ is the Fourier transform ${\tilde {f}}$ . Similarly, with $A=L^{1}(\mathbb {R} _{+})$ , the group algebra of the multiplicative reals, the Gelfand transform is the Mellin transform.

For $A=\ell ^{\infty }$ , the representation space is the Stone–Čech compactification $\beta \mathbb {N}$ . More generally, if X is a completely regular Hausdorff space, then the representation space of the Banach algebra of bounded continuous functions is the Stone–Čech compactification of X .

## The C*-algebra case

As motivation, consider the special case *A* = *C*0(*X*). Given *x* in *X*, let $\varphi _{x}\in A^{*}$ be pointwise evaluation at *x*, i.e. $\varphi _{x}(f)=f(x)$ . Then $\varphi _{x}$ is a character on *A*, and it can be shown that all characters of *A* are of this form; a more precise analysis shows that we may identify Φ*A* with *X*, not just as sets but as topological spaces. The Gelfand representation is then an isomorphism

$C_{0}(X)\to C_{0}(\Phi _{A}).\$

### The spectrum of a commutative C*-algebra

The **spectrum** or **Gelfand space** of a commutative C*-algebra *A*, denoted *Â*, consists of the set of *non-zero* *-homomorphisms from *A* to the complex numbers. Elements of the spectrum are called **characters** on *A*. (It can be shown that every algebra homomorphism from *A* to the complex numbers is automatically a *-homomorphism, so that this definition of the term 'character' agrees with the one above.)

In particular, the spectrum of a commutative C*-algebra is a locally compact Hausdorff space: In the unital case, i.e. where the C*-algebra has a multiplicative unit element 1, all characters *f* must be unital, i.e. *f*(1) is the complex number one. This excludes the zero homomorphism. So *Â* is closed under weak-* convergence and the spectrum is actually *compact*. In the non-unital case, the weak-* closure of *Â* is *Â* ∪ {0}, where 0 is the zero homomorphism, and the removal of a single point from a compact Hausdorff space yields a locally compact Hausdorff space.

Note that *spectrum* is an overloaded word. It also refers to the spectrum σ(*x*) of an element *x* of an algebra with unit 1, that is the set of complex numbers *r* for which *x* − *r* 1 is not invertible in *A*. For unital C*-algebras, the two notions are connected in the following way: σ(*x*) is the set of complex numbers *f*(*x*) where *f* ranges over Gelfand space of *A*. Together with the spectral radius formula, this shows that *Â* is a subset of the unit ball of *A** and as such can be given the relative weak-* topology. This is the topology of pointwise convergence. A net {*f**k*}*k* of elements of the spectrum of *A* converges to *f* if and only if for each *x* in *A*, the net of complex numbers {*f**k*(*x*)}*k* converges to *f*(*x*).

If *A* is a separable C*-algebra, the weak-* topology is metrizable on bounded subsets. Thus the spectrum of a separable commutative C*-algebra *A* can be regarded as a metric space. So the topology can be characterized via convergence of sequences.

Equivalently, σ(*x*) is the range of γ(*x*), where γ is the Gelfand representation.

### Statement of the commutative Gelfand–Naimark theorem

Let *A* be a commutative C*-algebra and let *X* be the spectrum of *A*. Let

$\gamma :A\to C_{0}(X)$

be the Gelfand representation defined above.

**Theorem**. The Gelfand map γ is an isometric *-isomorphism from *A* onto *C*0(*X*).

See the Arveson reference below.

The spectrum of a commutative C*-algebra can also be viewed as the set of all maximal ideals *m* of *A*, with the hull-kernel topology. (See the earlier remarks for the general, commutative Banach algebra case.) For any such *m* the quotient algebra *A/m* is one-dimensional (by the Gelfand-Mazur theorem), and therefore any *a* in *A* gives rise to a complex-valued function on *Y*.

In the case of C*-algebras with unit, the spectrum map gives rise to a contravariant functor from the category of commutative C*-algebras with unit and unit-preserving continuous *-homomorphisms, to the category of compact Hausdorff spaces and continuous maps. This functor is one half of a contravariant equivalence between these two categories (its adjoint being the functor that assigns to each compact Hausdorff space *X* the C*-algebra *C*0(*X*)). In particular, given compact Hausdorff spaces *X* and *Y*, then *C*(*X*) is isomorphic to *C*(*Y*) (as a C*-algebra) if and only if *X* is homeomorphic to *Y*.

The 'full' Gelfand–Naimark theorem is a result for arbitrary (abstract) noncommutative C*-algebras *A*, which though not quite analogous to the Gelfand representation, does provide a concrete representation of *A* as an algebra of operators.

## Applications

One of the most significant applications is the existence of a continuous functional calculus for normal elements in C*-algebra *A*: An element *x* is normal if and only if *x* commutes with its adjoint *x**, or equivalently if and only if it generates a commutative C*-algebra C*(*x*). By the Gelfand isomorphism applied to C*(*x*) this is *-isomorphic to an algebra of continuous functions on a locally compact space. This observation leads almost immediately to:

**Theorem**. Let *A* be a C*-algebra with identity and *x* a normal element of *A*. Then there is a *-morphism *f* → *f*(*x*) from the algebra of continuous functions on the spectrum σ(*x*) into *A* such that

- It maps 1 to the multiplicative identity of *A*;
- It maps the identity function on the spectrum to *x*.

This allows us to apply continuous functions to bounded normal operators on Hilbert space.

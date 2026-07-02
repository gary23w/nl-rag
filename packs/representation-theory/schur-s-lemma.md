---
title: "Schur's lemma"
source: https://en.wikipedia.org/wiki/Schur's_lemma
domain: representation-theory
license: CC-BY-SA-4.0
tags: representation theory, group representation, character theory, irreducible representation
fetched: 2026-07-02
---

# Schur's lemma

In mathematics, **Schur's lemma** is an elementary but useful statement in representation theory of groups and algebras. In the group case it says that if *M* and *N* are two finite-dimensional irreducible representations of a group *G* and *φ* is a linear map from *M* to *N* that commutes with the action of the group, then either *φ* is invertible, or *φ* = 0. An important special case occurs when *M* = *N*, i.e. *φ* is a self-map; in particular, for representations over an algebraically closed field (e.g. $\mathbb {C}$ ), any element of the center of a group must act as a scalar operator (a scalar multiple of the identity) on *M*. The lemma is named after Issai Schur who used it to prove the Schur orthogonality relations and develop the basics of the representation theory of finite groups. Schur's lemma admits generalisations to Lie groups and Lie algebras, the most common of which are due to Jacques Dixmier and Daniel Quillen.

## Representation theory of groups

Representation theory is the study of homomorphisms from a group, *G*, into the general linear group *GL*(*V*) of a vector space *V*; i.e., into the group of automorphisms of *V*. (Let us here restrict ourselves to the case when the underlying field of *V* is $\mathbb {C}$ , the field of complex numbers.) Such a homomorphism is called a representation of *G* on *V*. A representation on *V* is a special case of a group action on *V*, but rather than permit any arbitrary bijections (permutations) of the underlying set of *V*, we restrict ourselves to invertible *linear* transformations.

Let *ρ* be a representation of *G* on *V*. It may be the case that *V* has a subspace, *W*, such that for every element *g* of *G*, the invertible linear map *ρ*(*g*) preserves or fixes *W*, so that (*ρ*(*g*))(*w*) is in *W* for every *w* in *W*, and (*ρ*(*g*))(*v*) is not in *W* for any *v* not in *W*. In other words, every linear map *ρ*(*g*): *V*→*V* is also an automorphism of *W*, *ρ*(*g*): *W*→*W*, when its domain is restricted to *W*. We say *W* is *stable* under *G*, or stable under the action of *G*. It is clear that if we consider *W* on its own as a vector space, then there is an obvious representation of *G* on *W*—the representation we get by restricting each map *ρ*(*g*) to *W*. When *W* has this property, we call *W* with the given representation a *subrepresentation* of *V*. Every representation of *G* has itself and the zero vector space as trivial subrepresentations. A representation of *G* with no non-trivial subrepresentations is called an *irreducible representation*. Irreducible representations – like the prime numbers, or like the simple groups in group theory – are the building blocks of representation theory. Many of the initial questions and theorems of representation theory deal with the properties of irreducible representations.

Just as we are interested in homomorphisms between groups, and in continuous maps between topological spaces, we are also interested in certain functions between representations of *G*. Let *V* and *W* be vector spaces, and let $\rho _{V}$ and $\rho _{W}$ be representations of *G* on *V* and *W* respectively. Then we define a *G*-linear map *f* from *V* to *W* to be a linear map from *V* to *W* that is equivariant under the action of *G*; that is, for every *g* in *G*, $\rho _{W}(g)\circ f=f\circ \rho _{V}(g)$ . In other words, we require that *f* commutes with the action of *G*. *G*-linear maps are the morphisms in the category of representations of *G*.

Schur's Lemma is a theorem that describes what *G*-linear maps can exist between two irreducible representations of *G*.

### Statement and Proof of the Lemma

**Theorem** *(Schur's Lemma)*: Let *V* and *W* be vector spaces; and let $\rho _{V}$ and $\rho _{W}$ be irreducible representations of *G* on *V* and *W* respectively.

1. If V and W are not isomorphic, then there are no nontrivial *G*-linear maps between them.
2. If $V=W$ finite-dimensional over an algebraically closed field (e.g. $\mathbb {C}$ ); and if $\rho _{V}=\rho _{W}$ , then the only nontrivial *G*-linear maps are the identity, and scalar multiples of the identity. (A scalar multiple of the identity is sometimes called a *homothety.*)

**Proof:** Suppose f is a nonzero *G*-linear map from V to W . We will prove that V and W are isomorphic. Let $V'$ be the kernel, or null space, of f in V , described as $V'=\{x\in V|f(x)=0\}$ . $V'$ is a subspace of V as it is nonempty (contains the zero vector), and is closed.

By the assumption that f is *G*-linear, for every g in G and choice of x in $V'$ , $f((\rho _{V}(g))(x))=(\rho _{W}(g))(f(x))=(\rho _{W}(g))(0)=0$ . But saying that $f(\rho _{V}(g)(x))=0$ is the same as saying that $\rho _{V}(g)(x)$ is in the null space of $f:V\rightarrow W$ . So $V'$ is stable under the action of *G*; it is a subrepresentation. Since by assumption V is irreducible, $V'$ must be zero; so f is injective.

By an identical argument we will show f is also surjective; since $f((\rho _{V}(g))(x))=(\rho _{W}(g))(f(x))$ , we can conclude that for arbitrary choice of $f(x)$ in the image of f , $\rho _{W}(g)$ sends $f(x)$ somewhere else in the image of f ; in particular it sends it to the image of $\rho _{V}(g)x$ . So the image of $f(x)$ is a subspace $W'$ of W stable under the action of G , so it is a subrepresentation and f must be zero or surjective. By assumption it is not zero, so it is surjective, in which case it is an isomorphism.

In the event that $V=W$ finite-dimensional over an algebraically closed field and they have the same representation, let $\lambda$ be an eigenvalue of f . (An eigenvalue exists for every linear transformation on a finite-dimensional vector space over an algebraically closed field.) Let $f'=f-\lambda I$ . Then if x is an eigenvector of f corresponding to $\lambda ,f'(x)=0$ . It is clear that $f'$ is a *G*-linear map, because the sum or difference of *G*-linear maps is also *G*-linear. Then we return to the above argument, where we used the fact that a map was *G*-linear to conclude that the kernel is a subrepresentation, and is thus either zero or equal to all of V ; because it is not zero (it contains x ) it must be all of *V* and so $f'$ is trivial, so $f=\lambda I$ .

### Corollary of Schur's Lemma

An important corollary of Schur's lemma follows from the observation that we can often build explicitly G -linear maps between representations by "averaging" over the action of individual group elements on some fixed linear operator. In particular, given any irreducible representation, such objects will satisfy the assumptions of Schur's lemma, hence be scalar multiples of the identity. More precisely:

**Corollary**: Using the same notation from the previous theorem, let h be a linear mapping of *V* into *W*, and set $h_{0}={\frac {1}{|G|}}\sum _{g\in G}(\rho _{W}(g))^{-1}h\rho _{V}(g).$ Then,

1. If V and W are not isomorphic, then $h_{0}=0$ .
2. If $V=W$ is finite-dimensional over an algebraically closed field (e.g. $\mathbb {C}$ ); and if $\rho _{V}=\rho _{W}$ , then $h_{0}=I\,\mathrm {Tr} [h]/n$ , where *n* is the dimension of *V*. That is, $h_{0}$ is a homothety of ratio $\mathrm {Tr} [h]/n$ .

**Proof:** Let us first show that $h_{0}$ is a G-linear map, i.e., $\rho _{W}(g)\circ h_{0}=h_{0}\circ \rho _{V}(g)$ for all $g\in G$ . Indeed, consider that

${\begin{aligned}(\rho _{W}(g'))^{-1}h_{0}\rho _{V}(g')&={\frac {1}{|G|}}\sum _{g\in G}(\rho _{W}(g'))^{-1}(\rho _{W}(g))^{-1}h\rho _{V}(g)\rho _{V}(g')\\&={\frac {1}{|G|}}\sum _{g\in G}(\rho _{W}(g\circ g'))^{-1}h\rho _{V}(g\circ g')\\&=h_{0}\end{aligned}}$

Now applying the previous theorem, for case 1, it follows that $h_{0}=0$ , and for case 2, it follows that $h_{0}$ is a scalar multiple of the identity matrix (i.e., $h_{0}=\mu I$ ). To determine the scalar multiple $\mu$ , consider that

$\mathrm {Tr} [h_{0}]={\frac {1}{|G|}}\sum _{g\in G}\mathrm {Tr} [(\rho _{V}(g))^{-1}h\rho _{V}(g)]=\mathrm {Tr} [h]$

It then follows that $\mu =\mathrm {Tr} [h]/n$ .

This result has numerous applications. For example, in the context of quantum information science, it is used to derive results about complex projective t-designs. In the context of molecular orbital theory, it is used to restrict atomic orbital interactions based on the molecular symmetry.

## Formulation in the language of modules

**Theorem:** Let $M,N$ be two simple modules over a ring R . Then any homomorphism $f\colon M\to N$ of R -modules is either zero or an isomorphism. In particular, the endomorphism ring of a simple module is a division ring.

**Proof:** Consider the kernel and image of f : since $\ker(f)\subseteq M,\mathrm {im} (f)\subseteq N$ are submodules of simple modules, by definition they are either zero or equal to $M,N$ respectively. In particular, we have that either $\ker(f)=M$ , meaning that f is the zero morphism, or that $\ker(f)=0$ , meaning that f is injective. In the latter case, the first isomorphism theorem tells us furthermore that $\mathrm {im} (f)\cong M/\ker(f)\cong M$ is not trivial and thus $\mathrm {im} (f)=N$ : this shows that f is in addition surjective, hence bijective and thus an isomorphism of R -modules.

The group version is a special case of the module version, since any representation of a group *G* can equivalently be viewed as a module over the group ring of *G*.

Schur's lemma is frequently applied in the following particular case. Suppose that *R* is an algebra over a field *k* and the vector space *M* = *N* is a simple module of *R*. Then Schur's lemma says that the endomorphism ring of the module *M* is a division algebra over *k*. If *M* is finite-dimensional, this division algebra is finite-dimensional. If *k* is the field of complex numbers, the only option is that this division algebra is the complex numbers. Thus the endomorphism ring of the module *M* is "as small as possible". In other words, the only linear transformations of *M* that commute with all transformations coming from *R* are scalar multiples of the identity.

More generally, if R is an algebra over an algebraically closed field k and M is a simple R -module satisfying $\dim _{k}(M)<\#k$ (the cardinality of k ), then $\operatorname {End} _{R}(M)=k$ . So in particular, if R is an algebra over an uncountable algebraically closed field k and M is a simple module that is at most countably-dimensional, the only linear transformations of M that commute with all transformations coming from R are scalar multiples of the identity.

When the field is not algebraically closed, the case where the endomorphism ring is as small as possible is still of particular interest. A simple module over a k -algebra is said to be absolutely simple if its endomorphism ring is isomorphic to k . This is in general stronger than being irreducible over the field k , and implies the module is irreducible even over the algebraic closure of k .

### Application to central characters

**Definition:** Let R be a k -algebra. An R -module M is said to have *central character* $\chi :Z(R)\to k$ (here, $Z(R)$ is the center of R ) if for every $m\in M,z\in Z(R)$ there is $n\in \mathbb {N}$ such that $(z-\chi (z))^{n}m=0$ , i.e. if every $m\in M$ is a generalized eigenvector of z with eigenvalue $\chi (z)$ .

If $\operatorname {End} _{R}(M)=k$ , say in the case sketched above, every element of $Z(R)$ acts on M as an R -endomorphism and hence as a scalar. Thus, there is a ring homomorphism $\chi :Z(R)\to k$ such that $(z-\chi (z))m=0$ for all $z\in Z(R),m\in M$ . In particular, M has central character $\chi$ .

If $R=U({\mathfrak {g}}),k=\mathbb {C}$ is the universal enveloping algebra of a Lie algebra, a central character is also referred to as an infinitesimal character and the previous considerations show that if ${\mathfrak {g}}$ is finite-dimensional (so that $R=U({\mathfrak {g}})$ is countable-dimensional), then every simple ${\mathfrak {g}}$ -module has an infinitesimal character.

In the case where $k=\mathbb {C} ,R=\mathbb {C} [G]$ is the group algebra of a finite group G , the same conclusion follows. Here, the center of R consists of elements of the shape $\sum _{g\in G}a(g)g$ where $a:G\to \mathbb {C}$ is a class function, i.e. invariant under conjugation. Since the set of class functions is spanned by the characters $\chi _{\pi }$ of the irreducible representations $\pi \in {\hat {G}}$ , the central character is determined by what it maps $u_{\pi }:={\frac {1}{\#G}}\sum _{g\in G}\chi _{\pi }(g)g$ to (for all $\pi \in {\hat {G}}$ ). Since all $u_{\pi }$ are idempotent, they are each mapped either to 0 or to 1, and since $u_{\pi }u_{\pi '}=0$ for two different irreducible representations, only one $u_{\pi }$ can be mapped to 1: the one corresponding to the module M .

## Representations of Lie groups and Lie algebras

We now describe Schur's lemma as it is usually stated in the context of representations of Lie groups and Lie algebras. There are three parts to the result.

First, suppose that $V_{1}$ and $V_{2}$ are irreducible representations of a Lie group or Lie algebra over any field and that $\phi :V_{1}\rightarrow V_{2}$ is an intertwining map. Then $\phi$ is either zero or an isomorphism.

Second, if V is an irreducible representation of a Lie group or Lie algebra over an *algebraically closed* field and $\phi :V\rightarrow V$ is an intertwining map, then $\phi$ is a scalar multiple of the identity map.

Third, suppose $V_{1}$ and $V_{2}$ are irreducible representations of a Lie group or Lie algebra over an *algebraically closed* field and $\phi _{1},\phi _{2}:V_{1}\rightarrow V_{2}$ are nonzero intertwining maps. Then $\phi _{1}=\lambda \phi _{2}$ for some scalar $\lambda$ .

A simple corollary of the second statement is that every complex irreducible representation of an abelian group is one-dimensional.

### Application to the Casimir element

Suppose ${\mathfrak {g}}$ is a Lie algebra and $U({\mathfrak {g}})$ is the universal enveloping algebra of ${\mathfrak {g}}$ . Let ${\displaystyle \pi$ be an irreducible representation of ${\mathfrak {g}}$ over an algebraically closed field. The universal property of the universal enveloping algebra ensures that $\pi$ extends to a representation of $U({\mathfrak {g}})$ acting on the same vector space. It follows from the second part of Schur's lemma that if x belongs to the center of $U({\mathfrak {g}})$ , then $\pi (x)$ must be a multiple of the identity operator. In the case when ${\mathfrak {g}}$ is a complex semisimple Lie algebra, an important example of the preceding construction is the one in which x is the (quadratic) Casimir element C . In this case, $\pi (C)=\lambda _{\pi }I$ , where $\lambda _{\pi }$ is a constant that can be computed explicitly in terms of the highest weight of $\pi$ . The action of the Casimir element plays an important role in the proof of complete reducibility for finite-dimensional representations of semisimple Lie algebras.

## Generalization to non-simple modules

The one-module version of Schur's lemma admits generalizations for modules M that are not necessarily simple. They express relations between the module-theoretic properties of M and the properties of the endomorphism ring of M .

**Theorem** (Lam 2001, §19): A module is said to be **strongly indecomposable** if its endomorphism ring is a local ring. For a module M of finite length, the following properties are equivalent:

- M is indecomposable;
- M is strongly indecomposable;
- Every endomorphism of M is either nilpotent or invertible.

Schur's lemma cannot be reversed in general, however, since there exist modules that are not simple but whose endomorphism algebra is a division ring. Such modules are necessarily indecomposable and so cannot exist over semisimple rings, such as the complex group ring of a finite group. However, even over the ring of integers, the module of rational numbers has an endomorphism ring that is a division ring, specifically the field of rational numbers. Even for group rings, there are examples when the characteristic of the field divides the order of the group: the Jacobson radical of the projective cover of the one-dimensional representation of the alternating group A5 over the finite field with three elements F3 has F3 as its endomorphism ring.

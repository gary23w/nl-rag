---
title: "Bott periodicity theorem"
source: https://en.wikipedia.org/wiki/Bott_periodicity_theorem
domain: k-theory
license: CC-BY-SA-4.0
tags: topological k-theory, algebraic k-theory, grothendieck group, vector bundle
fetched: 2026-07-02
---

# Bott periodicity theorem

In mathematics, the **Bott periodicity theorem** describes a periodicity in the homotopy groups of classical groups, discovered by Raoul Bott (1957, 1959), which proved to be of foundational significance for much further research, in particular in K-theory of stable complex vector bundles, as well as the stable homotopy groups of spheres. Bott periodicity can be formulated in numerous ways, with the periodicity in question always appearing as a period-2 phenomenon, with respect to dimension, for the theory associated to the unitary group. See for example topological K-theory.

There are corresponding period-8 phenomena for the matching theories, (real) KO-theory and (quaternionic) KSp-theory, associated to the real orthogonal group and the quaternionic symplectic group, respectively. The J-homomorphism is a homomorphism from the homotopy groups of orthogonal groups to stable homotopy groups of spheres, which causes the period 8 Bott periodicity to be visible in the stable homotopy groups of spheres.

## Statement of result

Bott showed that if $U(\infty )$ is defined as the direct limit of the unitary groups $U(n)$ , then its homotopy groups are periodic with period 2:

$\pi _{i}(U(\infty ))\simeq \pi _{i+2}(U(\infty ))$

for $i\geq 0$ , and its first two homotopy groups are as follows:

${\begin{aligned}\pi _{0}(U(\infty ))&\simeq 0\\\pi _{1}(U(\infty ))&\simeq \mathbb {Z} .\end{aligned}}$

The "real" or "orthogonal" version of the Bott periodicity theorem, about the direct limit of the orthogonal groups $O(n)$ , says that

$\pi _{i}(O(\infty ))\simeq \pi _{i+8}(O(\infty ))$

for $i\geq 0$ , and its first 8 homotopy groups are as follows:

${\begin{aligned}\pi _{0}(O(\infty ))&\simeq \mathbb {Z} _{2}\\\pi _{1}(O(\infty ))&\simeq \mathbb {Z} _{2}\\\pi _{2}(O(\infty ))&\simeq 0\\\pi _{3}(O(\infty ))&\simeq \mathbb {Z} \\\pi _{4}(O(\infty ))&\simeq 0\\\pi _{5}(O(\infty ))&\simeq 0\\\pi _{6}(O(\infty ))&\simeq 0\\\pi _{7}(O(\infty ))&\simeq \mathbb {Z} \end{aligned}}$

## Context and significance

The context of Bott periodicity is that the homotopy groups of spheres, which would be expected to play the basic part in algebraic topology by analogy with homology theory, have proved elusive (and the theory is complicated). The subject of stable homotopy theory was conceived as a simplification, by introducing the suspension (smash product with a circle) operation, and seeing what (roughly speaking) remained of homotopy theory once one was allowed to suspend both sides of an equation as many times as one wished. The stable theory was still hard to compute with, in practice.

What Bott periodicity offered was an insight into some highly non-trivial spaces, with central status in topology because of the connection of their cohomology with characteristic classes, for which all the (*unstable*) homotopy groups could be calculated. These spaces are the (infinite, or *stable*) unitary, orthogonal and symplectic groups *U*, *O* and Sp. In this context, *stable* refers to taking the union (also known as the direct limit) of the sequence of inclusions

$U(1)\subset U(2)\subset \cdots \subset U=\bigcup _{k=1}^{\infty }U(k)$

and similarly for *O* and Sp. Note that Bott's use of the word *stable* in the title of his seminal paper refers to these stable classical groups and not to stable homotopy groups.

The important connection of Bott periodicity with the stable homotopy groups of spheres $\pi _{n}^{S}$ comes via the so-called stable *J*-homomorphism from the (unstable) homotopy groups of the (stable) classical groups to these stable homotopy groups $\pi _{n}^{S}$ . Originally described by George W. Whitehead, it became the subject of the famous Adams conjecture (1963) which was finally resolved in the affirmative by Daniel Quillen (1971).

Bott's original results may be succinctly summarized in:

**Corollary:** The (unstable) homotopy groups of the (infinite) classical groups are periodic:

${\begin{aligned}\pi _{k}(U)&=\pi _{k+2}(U)\\\pi _{k}(O)&=\pi _{k+4}(\operatorname {Sp} )\\\pi _{k}(\operatorname {Sp} )&=\pi _{k+4}(O)&&k=0,1,\ldots \end{aligned}}$

**Note:** The second and third of these isomorphisms intertwine to give the 8-fold periodicity results:

${\begin{aligned}\pi _{k}(O)&=\pi _{k+8}(O)\\\pi _{k}(\operatorname {Sp} )&=\pi _{k+8}(\operatorname {Sp} ),&&k=0,1,\ldots \end{aligned}}$

## Loop spaces and classifying spaces

For the theory associated to the infinite unitary group, *U*, the space *BU* is the classifying space for stable complex vector bundles (a Grassmannian in infinite dimensions). One formulation of Bott periodicity describes the twofold loop space, $\Omega ^{2}BU$ of *BU*. Here, $\Omega$ is the loop space functor, right adjoint to suspension and left adjoint to the classifying space construction. Bott periodicity states that this double loop space is essentially *BU* again; more precisely, $\Omega ^{2}BU\simeq \mathbb {Z} \times BU$ is essentially (that is, homotopy equivalent to) the union of a countable number of copies of *BU*. An equivalent formulation is $\Omega ^{2}U\simeq U.$

Either of these has the immediate effect of showing why (complex) topological *K*-theory is a 2-fold periodic theory.

In the corresponding theory for the infinite orthogonal group, *O*, the space *BO* is the classifying space for stable real vector bundles. In this case, Bott periodicity states that, for the 8-fold loop space, $\Omega ^{8}BO\simeq \mathbb {Z} \times BO$ or equivalently, $\Omega ^{8}O\simeq O,$

which yields the consequence that *KO*-theory is an 8-fold periodic theory. Also, for the infinite symplectic group, Sp, the space BSp is the classifying space for stable quaternionic vector bundles, and Bott periodicity states that $\Omega ^{8}\operatorname {BSp} \simeq \mathbb {Z} \times \operatorname {BSp} ;$ or equivalently $\Omega ^{8}\operatorname {Sp} \simeq \operatorname {Sp} .$

Thus both topological real *K*-theory (also known as *KO*-theory) and topological quaternionic *K*-theory (also known as KSp-theory) are 8-fold periodic theories.

## Geometric model of loop spaces

One elegant formulation of Bott periodicity makes use of the observation that there are natural embeddings (as closed subgroups) between the classical groups. The loop spaces in Bott periodicity are then homotopy equivalent to the symmetric spaces of successive quotients, with additional discrete factors of **Z**.

Over the complex numbers:

$U\times U\subset U\subset U\times U.$

Over the real numbers and quaternions:

$O\times O\subset O\subset U\subset \operatorname {Sp} \subset \operatorname {Sp} \times \operatorname {Sp} \subset \operatorname {Sp} \subset U\subset O\subset O\times O.$

These sequences corresponds to sequences in Clifford algebras – see classification of Clifford algebras; over the complex numbers:

$\mathbb {C} \oplus \mathbb {C} \subset \mathbb {C} \subset \mathbb {C} \oplus \mathbb {C} .$

Over the real numbers and quaternions:

$\mathbb {R} \oplus \mathbb {R} \subset \mathbb {R} \subset \mathbb {C} \subset \mathbb {H} \subset \mathbb {H} \oplus \mathbb {H} \subset \mathbb {H} \subset \mathbb {C} \subset \mathbb {R} \subset \mathbb {R} \oplus \mathbb {R} ,$

where the division algebras indicate "matrices over that algebra".

As they are 2-periodic/8-periodic, they can be arranged in a circle, where they are called the **Bott periodicity clock** and **Clifford algebra clock**.

The Bott periodicity results then refine to a sequence of homotopy equivalences:

For complex *K*-theory:

${\begin{aligned}\Omega U&\simeq \mathbb {Z} \times BU=\mathbb {Z} \times U/(U\times U)\\\Omega (\mathbb {Z} \times BU)&\simeq U=(U\times U)/U\end{aligned}}$

For real and quaternionic *KO*- and KSp-theories:

${\begin{aligned}\Omega (\mathbb {Z} \times BO)&\simeq O=(O\times O)/O&\Omega (\mathbb {Z} \times \operatorname {BSp} )&\simeq \operatorname {Sp} =(\operatorname {Sp} \times \operatorname {Sp} )/\operatorname {Sp} \\\Omega O&\simeq O/U&\Omega \operatorname {Sp} &\simeq \operatorname {Sp} /U\\\Omega (O/U)&\simeq U/\operatorname {Sp} &\Omega (\operatorname {Sp} /U)&\simeq U/O\\\Omega (U/\operatorname {Sp} )&\simeq \mathbb {Z} \times \operatorname {BSp} =\mathbb {Z} \times \operatorname {Sp} /(\operatorname {Sp} \times \operatorname {Sp} )&\Omega (U/O)&\simeq \mathbb {Z} \times BO=\mathbb {Z} \times O/(O\times O)\end{aligned}}$

The resulting spaces are homotopy equivalent to the classical reductive symmetric spaces, and are the successive quotients of the terms of the Bott periodicity clock. These equivalences immediately yield the Bott periodicity theorems.

The specific spaces are, (for groups, the principal homogeneous space is also listed):

| Loop space | Quotient | Cartan's label | Description |
|---|---|---|---|
| $\Omega ^{0}$ | $\mathbb {Z} \times O/(O\times O)$ | BDI | Real Grassmannian |
| $\Omega ^{1}$ | $O=(O\times O)/O$ |   | Orthogonal group (real Stiefel manifold) |
| $\Omega ^{2}$ | $O/U$ | DIII | space of complex structures compatible with a given orthogonal structure |
| $\Omega ^{3}$ | $U/\mathrm {Sp}$ | AII | space of quaternionic structures compatible with a given complex structure |
| $\Omega ^{4}$ | $\mathbb {Z} \times \mathrm {Sp} /(\mathrm {Sp} \times \mathrm {Sp} )$ | CII | Quaternionic Grassmannian |
| $\Omega ^{5}$ | $\mathrm {Sp} =(\mathrm {Sp} \times \mathrm {Sp} )/\mathrm {Sp}$ |   | Symplectic group (quaternionic Stiefel manifold) |
| $\Omega ^{6}$ | $\mathrm {Sp} /U$ | CI | complex Lagrangian Grassmannian |
| $\Omega ^{7}$ | $U/O$ | AI | Lagrangian Grassmannian |

## Proofs

Bott's original proof (Bott 1959) used Morse theory, which Bott (1956) had used earlier to study the homology of Lie groups. Many different proofs have been given.

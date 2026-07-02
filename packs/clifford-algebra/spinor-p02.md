---
title: "Spinor (part 2/2)"
source: https://en.wikipedia.org/wiki/Spinor
domain: clifford-algebra
license: CC-BY-SA-4.0
tags: clifford algebra, geometric algebra, spinor field, gamma matrices
fetched: 2026-07-02
part: 2/2
---

## Summary in low dimensions

- In 1 dimension (a trivial example), the single spinor representation is formally Majorana, a real 1-dimensional representation that does not transform.
- In 2 Euclidean dimensions, the left-handed and the right-handed Weyl spinor are 1-component complex representations, i.e. complex numbers that get multiplied by *e*±*iφ*/2 under a rotation by angle *φ*.
- In 3 Euclidean dimensions, the single spinor representation is 2-dimensional and quaternionic. The existence of spinors in 3 dimensions follows from the isomorphism of the groups SU(2) ≅ Spin(3) that allows us to define the action of Spin(3) on a complex 2-component column (a spinor); the generators of SU(2) can be written as Pauli matrices.
- In 4 Euclidean dimensions, the corresponding isomorphism is Spin(4) ≅ SU(2) × SU(2). There are two inequivalent quaternionic 2-component Weyl spinors and each of them transforms under one of the SU(2) factors only.
- In 5 Euclidean dimensions, the relevant isomorphism is Spin(5) ≅ USp(4) ≅ Sp(2) that implies that the single spinor representation is 4-dimensional and quaternionic.
- In 6 Euclidean dimensions, the isomorphism Spin(6) ≅ SU(4) guarantees that there are two 4-dimensional complex Weyl representations that are complex conjugates of one another.
- In 7 Euclidean dimensions, the single spinor representation is 8-dimensional and real; no isomorphisms to a Lie algebra from another series (A or C) exist from this dimension on.
- In 8 Euclidean dimensions, there are two Weyl–Majorana real 8-dimensional representations that are related to the 8-dimensional real vector representation by a special property of Spin(8) called triality.
- In *d* + 8 dimensions, the number of distinct irreducible spinor representations and their reality (whether they are real, pseudoreal, or complex) mimics the structure in *d* dimensions, but their dimensions are 16 times larger; this allows one to understand all remaining cases. See Bott periodicity.
- In spacetimes with *p* spatial and *q* time-like directions, the dimensions viewed as dimensions over the complex numbers coincide with the case of the (*p* + *q*)-dimensional Euclidean space, but the reality projections mimic the structure in |*p* − *q*| Euclidean dimensions. For example, in 3 + 1 dimensions there are two non-equivalent Weyl complex (like in 2 dimensions) 2-component (like in 4 dimensions) spinors, which follows from the isomorphism SL(2, ℂ) ≅ Spin(3,1).

| Metric signature | Weyl, complex | Conjugacy | Dirac, complex | Majorana–Weyl, real | Majorana, real |   |   |
|---|---|---|---|---|---|---|---|
| Left-handed | Right-handed | Left-handed | Right-handed |   |   |   |   |
| (2,0) | 1 | 1 | Mutual | 2 | – | – | 2 |
| (1,1) | 1 | 1 | Self | 2 | 1 | 1 | 2 |
| (3,0) | – | – | – | 2 | – | – | – |
| (2,1) | – | – | – | 2 | – | – | 2 |
| (4,0) | 2 | 2 | Self | 4 | – | – | – |
| (3,1) | 2 | 2 | Mutual | 4 | – | – | 4 |
| (5,0) | – | – | – | 4 | – | – | – |
| (4,1) | – | – | – | 4 | – | – | – |
| (6,0) | 4 | 4 | Mutual | 8 | – | – | 8 |
| (5,1) | 4 | 4 | Self | 8 | – | – | – |
| (7,0) | – | – | – | 8 | – | – | 8 |
| (6,1) | – | – | – | 8 | – | – | – |
| (8,0) | 8 | 8 | Self | 16 | 8 | 8 | 16 |
| (7,1) | 8 | 8 | Mutual | 16 | – | – | 16 |
| (9,0) | – | – | – | 16 | – | – | 16 |
| (8,1) | – | – | – | 16 | – | – | 16 |

### Reality type and signature

One source of confusion is that the words *real*, *complex*, and *quaternionic* are used in two closely related but not identical senses: they may refer to the ground field of a chosen Clifford module, or to the **type** (also called the Schur type) of an irreducible spin representation. For the spin group, the second notion is the useful one.

Let S be an irreducible complex spin representation of $\operatorname {Spin} (p,q)$ . Then S is said to be

- **of real type** if there is a $\operatorname {Spin} (p,q)$ -equivariant antilinear map $J:S\to S$ with $J^{2}=+1$ ;
- **of quaternionic type** (or *pseudoreal*) if there is such a map with $J^{2}=-1$ ;
- **of complex type** if no such equivariant antilinear map exists, equivalently if S and its complex conjugate ${\overline {S}}$ are inequivalent.

When S is of real type, the fixed-point set of J gives a real form of the representation; this is the algebraic origin of Majorana conditions. When S is of quaternionic type, the representation carries an invariant quaternionic structure but no invariant real structure on an irreducible complex module.

The reason for the mod-8 pattern is that spinors are naturally modules for the **even Clifford algebra** $\mathrm {C} \ell _{p,q}^{0}$ . If S is an irreducible real $\mathrm {C} \ell _{p,q}^{0}$ -module, then by Schur's lemma its commuting algebra $\operatorname {End} _{\mathrm {C} \ell _{p,q}^{0}}(S)$ is a finite-dimensional real division algebra. By the Frobenius theorem, it is therefore isomorphic to exactly one of $\mathbb {R} ,\qquad \mathbb {C} ,\qquad \mathbb {H} .$ These three possibilities are precisely the real, complex, and quaternionic types. Using the standard identification of even Clifford algebras with Clifford algebras in one lower dimension, together with Bott periodicity, one finds that the type depends only on $p-q{\pmod {8}}$ .

| Dimension $n=p+q$ | $p-q{\pmod {8}}$ | Irreducible complex spin representation(s) | Type | Consequence |
|---|---|---|---|---|
| odd | 1, 7 | S | real | S admits an invariant real structure |
| odd | 3, 5 | S | quaternionic | S admits an invariant quaternionic structure |
| even | 0 | $S^{+},S^{-}$ | real | each Weyl representation admits a real structure; Majorana–Weyl spinors are possible |
| even | 2, 6 | $S^{+},S^{-}$ | complex | $S^{-}\cong {\overline {S^{+}}}$ ; a single Weyl representation is neither real nor quaternionic |
| even | 4 | $S^{+},S^{-}$ | quaternionic | each Weyl representation admits an invariant quaternionic structure |

Thus, for example, spinors in 3-dimensional Euclidean space are quaternionic, Weyl spinors in 4-dimensional Euclidean space are quaternionic, Weyl spinors in Lorentzian signature $(3,1)$ are complex conjugates of one another, Weyl spinors in split signature $(1,1)$ are real, and 8-dimensional Euclidean Weyl spinors are real.

A common source of apparent disagreement between tables in the literature is that some authors classify irreducible modules for the full real Clifford algebra $\mathrm {C} \ell _{p,q}$ , while others classify spin representations of $\operatorname {Spin} (p,q)$ . Since the spin group sits in the even Clifford algebra, these two tables differ by a shift of one step in the mod-8 pattern.

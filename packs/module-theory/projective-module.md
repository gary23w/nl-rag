---
title: "Projective module"
source: https://en.wikipedia.org/wiki/Projective_module
domain: module-theory
license: CC-BY-SA-4.0
tags: module theory, projective module, injective module, flat module
fetched: 2026-07-02
---

# Projective module

In mathematics, particularly in algebra, the class of **projective modules** enlarges the class of free modules (that is, modules with basis vectors) over a ring, keeping some of the main properties of free modules. Various equivalent characterizations of these modules appear below.

Every free module is a projective module, but the converse fails to hold over some rings, such as Dedekind rings that are not principal ideal domains. However, every projective module is a free module if the ring is a principal ideal domain such as the integers, or a (multivariate) polynomial ring over a field (this is the Quillen–Suslin theorem).

Projective modules were first introduced in 1956 in the influential book *Homological Algebra* by Henri Cartan and Samuel Eilenberg.

## Definitions

### Lifting property

The usual category theoretical definition is in terms of the property of *lifting* that carries over from free to projective modules: a module *P* is projective if and only if for every surjective module homomorphism *f* : *N* ↠ *M* and every module homomorphism *g* : *P* → *M*, there exists a module homomorphism *h* : *P* → *N* such that *fh* = *g*. (We don't require the lifting homomorphism *h* to be unique; this is not a universal property.)

The advantage of this definition of "projective" is that it can be carried out in categories more general than module categories: we don't need a notion of "free object". It can also be dualized, leading to injective modules. The lifting property may also be rephrased as *every morphism from P to M factors through every epimorphism to M*. Thus, by definition, projective modules are precisely the projective objects in the category of *R*-modules.

### Split-exact sequences

A module *P* is projective if and only if every short exact sequence of modules of the form

$0\rightarrow A\rightarrow B\rightarrow P\rightarrow 0$

is a split exact sequence. That is, for every surjective module homomorphism *f* : *B* ↠ *P* there exists a **section map**, that is, a module homomorphism *h* : *P* → *B* such that *fh* = id*P*. In that case, *h*(*P*) is a direct summand of *B*, *h* is an isomorphism from *P* to *h*(*P*), and *hf* is a projection on the summand *h*(*P*). Equivalently,

$B=\operatorname {Im} (h)\oplus \operatorname {Ker} (f)\ \ {\text{ where }}\operatorname {Ker} (f)\cong A\ {\text{ and }}\operatorname {Im} (h)\cong P.$

### Direct summands of free modules

A module *P* is projective if and only if there is another module *Q* such that the direct sum of *P* and *Q* is a free module.

### Exactness

An *R*-module *P* is projective if and only if the covariant functor Hom(*P*, -): *R*-**Mod** → **Ab** is an exact functor, where *R*-**Mod** is the category of left *R*-modules and **Ab** is the category of abelian groups. When the ring *R* is commutative, **Ab** is advantageously replaced by *R*-**Mod** in the preceding characterization. This functor is always left exact, but, when *P* is projective, it is also right exact. This means that *P* is projective if and only if this functor preserves epimorphisms (surjective homomorphisms), or if it preserves finite colimits.

### Dual basis

A module *P* is projective if and only if there exists a set $\{a_{i}\in P\mid i\in I\}$ and a set $\{f_{i}\in \mathrm {Hom} (P,R)\mid i\in I\}$ such that for every *x* in *P*, *f**i*(*x*) is only nonzero for finitely many *i*, and $x=\sum f_{i}(x)a_{i}$ .

## Elementary examples and properties

The following properties of projective modules are quickly deduced from any of the above (equivalent) definitions of projective modules:

- Direct sums and direct summands of projective modules are projective.
- If *e* = *e*2 is an idempotent in the ring *R*, then *Re* is a projective left module over *R*.

Let $R=R_{1}\times R_{2}$ be the direct product of two rings $R_{1}$ and $R_{2},$ which is a ring with operations defined componentwise. Let $e_{1}=(1,0)$ and $e_{2}=(0,1).$ Then $e_{1}$ and $e_{2}$ are idempotents, and belong to the centre of $R.$ The two-sided ideals $Re_{1}$ and $Re_{2}$ are projective modules, since their direct sum (as R-modules) equals the free R-module R. However, if $R_{1}$ and $R_{2}$ are nontrivial, then they are not free as modules over R . For instance $\mathbb {Z} /2\mathbb {Z}$ is projective but not free over $\mathbb {Z} /6\mathbb {Z}$ .

## Relation to other module-theoretic properties

The relation of projective modules to free and flat modules is subsumed in the following diagram of module properties:

(Module properties in commutative algebra)

The left-to-right implications are true over any ring, although some authors define torsion-free modules only over a domain. The right-to-left implications are true over the rings labeling them. There may be other rings over which they are true. For example, the implication labeled "local ring or PID" is also true for (multivariate) polynomial rings over a field: this is the Quillen–Suslin theorem.

### Projective vs. free modules

Any free module is projective. The converse is true in the following cases:

- if *R* is a field or skew field: *any* module is free in this case.
- if the ring *R* is a principal ideal domain. For example, this applies to *R* = **Z** (the integers), so an abelian group is projective if and only if it is a free abelian group. The reason is that any submodule of a free module over a principal ideal domain is free.
- if the ring *R* is a local ring. This fact is the basis of the intuition of "locally free = projective". This fact is easy to prove for finitely generated projective modules. In general, it is due to Kaplansky (1958); see Kaplansky's theorem on projective modules.

In general though, projective modules need not be free:

- Over a direct product of rings *R* × *S* where *R* and *S* are nonzero rings, both *R* × 0 and 0 × *S* are non-free projective modules.
- Over a Dedekind domain a non-principal ideal is always a projective module that is not a free module.
- Over a matrix ring M*n*(*R*), the natural module *R**n* is projective but is not free when *n* > 1.
- Over a semisimple ring, *every* module is projective, but a nonzero proper left (or right) ideal is not a free module. Thus the only semisimple rings for which all projectives are free are division rings.

The difference between free and projective modules is, in a sense, measured by the algebraic *K*-theory group *K*0(*R*); see below.

### Projective vs. flat modules

Every projective module is flat. The converse is in general not true: the abelian group **Q** is a **Z**-module that is flat, but not projective.

Conversely, a finitely related flat module is projective.

Govorov (1965) and Lazard (1969) proved that a module *M* is flat if and only if it is a direct limit of finitely-generated free modules.

In general, the precise relation between flatness and projectivity was established by Raynaud & Gruson (1971) (see also Drinfeld (2006) and Braunling, Groechenig & Wolfson (2016)) who showed that a module *M* is projective if and only if it satisfies the following conditions:

- *M* is flat,
- *M* is a direct sum of countably generated modules,
- *M* satisfies a certain Mittag-Leffler-type condition.

This characterization can be used to show that if $R\to S$ is a faithfully flat map of commutative rings and M is an R -module, then M is projective if and only if $M\otimes _{R}S$ is projective. In other words, the property of being projective satisfies faithfully flat descent.

## The category of projective modules

Submodules of projective modules need not be projective; a ring *R* for which every submodule of a projective left module is projective is called left hereditary.

Quotients of projective modules also need not be projective, for example **Z**/*n* is a quotient of **Z**, but not torsion-free, hence not flat, and therefore not projective.

The category of finitely generated projective modules over a ring is an exact category. (See also algebraic K-theory).

## Projective resolutions

Given a module, *M*, a **projective resolution** of *M* is an infinite exact sequence of modules

⋅

⋅

⋅

→

P

n

→

⋅

⋅

⋅

→

P

2

→

P

1

→

P

0

→

M

→ 0,

with all the *P**i* s projective. Every module possesses a projective resolution. In fact a **free resolution** (resolution by free modules) exists. The exact sequence of projective modules may sometimes be abbreviated to *P*(*M*) → *M* → 0 or *P*• → *M* → 0. A classic example of a projective resolution is given by the Koszul complex of a regular sequence, which is a free resolution of the ideal generated by the sequence.

The *length* of a finite resolution is the index *n* such that *P**n* is nonzero and *P**i* = 0 for *i* greater than *n*. If *M* admits a finite projective resolution, the minimal length among all finite projective resolutions of *M* is called its **projective dimension** and denoted pd(*M*). If *M* does not admit a finite projective resolution, then by convention the projective dimension is said to be infinite. As an example, consider a module *M* such that pd(*M*) = 0. In this situation, the exactness of the sequence 0 → *P*0 → *M* → 0 indicates that the arrow in the center is an isomorphism, and hence *M* itself is projective.

## Projective modules over commutative rings

Projective modules over commutative rings have nice properties.

The localization of a projective module is a projective module over the localized ring. A projective module over a local ring is free. Thus a projective module is *locally free* (in the sense that its localization at every prime ideal is free over the corresponding localization of the ring). The converse is true for finitely generated modules over Noetherian rings: a finitely generated module over a commutative Noetherian ring is locally free if and only if it is projective.

However, there are examples of finitely generated modules over a non-Noetherian ring that are locally free and not projective. For instance, a Boolean ring has all of its localizations isomorphic to **F**2, the field of two elements, so any module over a Boolean ring is locally free, but there are some non-projective modules over Boolean rings. One example is *R*/*I* where *R* is a direct product of countably many copies of **F**2 and *I* is the direct sum of countably many copies of **F**2 inside of *R*. The *R*-module *R*/*I* is locally free since *R* is Boolean (and it is finitely generated as an *R*-module too, with a spanning set of size 1), but *R*/*I* is not projective because *I* is not a principal ideal. (If a quotient module *R*/*I*, for any commutative ring *R* and ideal *I*, is a projective *R*-module then *I* is principal.)

However, it is true that for finitely presented modules *M* over a commutative ring *R* (in particular if *M* is a finitely generated *R*-module and *R* is Noetherian), the following are equivalent.

1. M is flat.
2. M is projective.
3. $M_{\mathfrak {m}}$ is free as $R_{\mathfrak {m}}$ -module for every maximal ideal ${\mathfrak {m}}$ of *R*.
4. $M_{\mathfrak {p}}$ is free as $R_{\mathfrak {p}}$ -module for every prime ideal ${\mathfrak {p}}$ of *R*.
5. There exist $f_{1},\ldots ,f_{n}\in R$ generating the unit ideal such that $M[f_{i}^{-1}]$ is free as $R[f_{i}^{-1}]$ -module for each *i*.
6. ${\widetilde {M}}$ is a locally free sheaf on the affine scheme $\operatorname {Spec} R$ (where ${\widetilde {M}}$ is the sheaf associated to *M*.)

Moreover, if *R* is a Noetherian integral domain, then, by Nakayama's lemma, these conditions are equivalent to

- The dimension of the $k({\mathfrak {p}})$ -vector space $M\otimes _{R}k({\mathfrak {p}})$ is the same for all prime ideals ${\mathfrak {p}}$ of *R,* where $k({\mathfrak {p}})$ is the residue field at ${\mathfrak {p}}$ . That is to say, *M* has constant rank (as defined below).

Let *A* be a commutative ring. If *B* is a (possibly non-commutative) *A*-algebra that is a finitely generated projective *A*-module containing *A* as a subring, then *A* is a direct factor of *B*.

### Rank

Let *P* be a finitely generated projective module over a commutative ring *R* and *X* be the spectrum of *R*. The *rank* of *P* at a prime ideal ${\mathfrak {p}}$ in *X* is the rank of the free $R_{\mathfrak {p}}$ -module $P_{\mathfrak {p}}$ . It is a locally constant function on *X*. In particular, if *X* is connected (that is if *R* has no other idempotents than 0 and 1), then *P* has constant rank.

## Vector bundles and locally free modules

A basic motivation of the theory is that projective modules (at least over certain commutative rings) are analogues of vector bundles. This can be made precise for the ring of continuous real-valued functions on a compact Hausdorff space, as well as for the ring of smooth functions on a smooth manifold (see Serre–Swan theorem that says a finitely generated projective module over the space of smooth functions on a compact manifold is the space of smooth sections of a smooth vector bundle).

Vector bundles are *locally free*. If there is some notion of "localization" that can be carried over to modules, such as the usual localization of a ring, one can define locally free modules, and the projective modules then typically coincide with the locally free modules.

## Projective modules over a polynomial ring

The Quillen–Suslin theorem, which solves Serre's problem, is another deep result: if *K* is a field, or more generally a principal ideal domain, and *R* = *K*[*X*1,...,*X**n*] is a polynomial ring over *K*, then every projective module over *R* is free. This problem was first raised by Serre with *K* a field (and the modules being finitely generated). Bass settled it for non-finitely generated modules, and Quillen and Suslin independently and simultaneously treated the case of finitely generated modules.

Since every projective module over a principal ideal domain is free, one might ask this question: if *R* is a commutative ring such that every (finitely generated) projective *R*-module is free, then is every (finitely generated) projective *R*[*X*]-module free? The answer is *no*. A counterexample occurs with *R* equal to the local ring of the curve *y*2 = *x*3 at the origin. Thus the Quillen–Suslin theorem could never be proved by a simple induction on the number of variables.

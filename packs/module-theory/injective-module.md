---
title: "Injective module"
source: https://en.wikipedia.org/wiki/Injective_module
domain: module-theory
license: CC-BY-SA-4.0
tags: module theory, projective module, injective module, flat module
fetched: 2026-07-02
---

# Injective module

In mathematics, especially in the area of abstract algebra known as module theory, an **injective module** is a module *Q* that shares certain desirable properties with the **Z**-module **Q** of all rational numbers. Specifically, if *Q* is a submodule of some other module, then it is already a direct summand of that module; also, given a submodule of a module *Y*, any module homomorphism from this submodule to *Q* can be extended to a homomorphism from all of *Y* to *Q*. This concept is dual to that of projective modules. Injective modules were introduced in (Baer 1940) and are discussed in some detail in the textbook (Lam 1999, §3).

Injective modules have been heavily studied, and a variety of additional notions are defined in terms of them: Injective cogenerators are injective modules that faithfully represent the entire category of modules. Injective resolutions measure how far from injective a module is in terms of the injective dimension and represent modules in the derived category. Injective hulls are maximal essential extensions, and turn out to be minimal injective extensions. Over a Noetherian ring, every injective module is uniquely a direct sum of indecomposable modules, and their structure is well understood. An injective module over one ring may be not injective over another, but there are well-understood methods of changing rings which handle special cases. Rings which are themselves injective modules have a number of interesting properties and include rings such as group rings of finite groups over fields. Injective modules include divisible groups and are generalized by the notion of injective objects in category theory.

## Definition

A left module Q over the ring R is injective if it satisfies one (and therefore all) of the following equivalent conditions:

- If Q is a submodule of some other left R -module M , then there exists another submodule K of M such that M is the internal direct sum of Q and K , i.e. $Q+K=M$ and $Q\cap K=\{0\}$ .
- Any short exact sequence $0\rightarrow Q\rightarrow M\rightarrow K\rightarrow 0$ of left R -modules splits.
- If X and Y are left R -modules, $f:X\rightarrow Y$ is an injective module homomorphism and $g:X\rightarrow Q$ is an arbitrary module homomorphism, then there exists a module homomorphism $h:Y\rightarrow Q$ such that $hf=g$ , i.e. such that the following diagram commutes:

- The contravariant Hom functor $\operatorname {Hom} (-,Q)$ from the category of left R -modules to the category of abelian groups is exact.

Injective right R -modules are defined analogously.

## Examples

### First examples

Trivially, the zero module $\{0\}$ is injective.

Given a field k , every k -vector space Q is an injective k -module. Reason: if Q is a subspace of V , we can find a basis of Q and extend it to a basis of V . The new extending basis vectors span a subspace K of V and V is the internal direct sum of Q and K . Note that the direct complement K of Q is not uniquely determined by Q , and likewise the extending map h in the above definition is typically not unique.

The rationals $\mathbb {Q}$ (with addition) form an injective abelian group (i.e. an injective $\mathbb {Z}$ -module). The factor group $\mathbb {Q} /\mathbb {Z}$ and the circle group are also injective $\mathbb {Z}$ -modules. The factor group $\mathbb {Z} /n\mathbb {Z}$ for $n>1$ is injective as a $\mathbb {Z} /n\mathbb {Z}$ -module, but *not* injective as an abelian group.

### Commutative examples

More generally, for any integral domain *R* with field of fractions *K*, the *R*-module *K* is an injective *R*-module, and indeed the smallest injective *R*-module containing *R*. For any Dedekind domain, the quotient module *K*/*R* is also injective, and its indecomposable summands are the localizations $R_{\mathfrak {p}}/R$ for the nonzero prime ideals ${\mathfrak {p}}$ . The zero ideal is also prime and corresponds to the injective *K*. In this way there is a 1-1 correspondence between prime ideals and indecomposable injective modules.

A particularly rich theory is available for commutative noetherian rings due to Eben Matlis, (Lam 1999, §3I). Every injective module is uniquely a direct sum of indecomposable injective modules, and the indecomposable injective modules are uniquely identified as the injective hulls of the quotients *R*/*P* where *P* varies over the prime spectrum of the ring. The injective hull of *R*/*P* as an *R*-module is canonically an *R**P* module, and is the *R**P*-injective hull of *R*/*P*. In other words, it suffices to consider local rings. The endomorphism ring of the injective hull of *R*/*P* is the completion ${\hat {R}}_{P}$ of *R* at *P*.

Two examples are the injective hull of the **Z**-module **Z**/*p***Z** (the Prüfer group), and the injective hull of the *k*[*x*]-module *k* (the ring of inverse polynomials). The latter is easily described as *k*[*x*,*x*−1]/*xk*[*x*]. This module has a basis consisting of "inverse monomials", that is *x*−*n* for *n* = 0, 1, 2, …. Multiplication by scalars is as expected, and multiplication by *x* behaves normally except that *x*·1 = 0. The endomorphism ring is simply the ring of formal power series.

### Artinian examples

If *G* is a finite group and *k* a field with characteristic 0, then one shows in the theory of group representations that any subrepresentation of a given one is already a direct summand of the given one. Translated into module language, this means that all modules over the group algebra *kG* are injective. If the characteristic of *k* is not zero, the following example may help.

If *A* is a unital associative algebra over the field *k* with finite dimension over *k*, then Hom*k*(−, *k*) is a duality between finitely generated left *A*-modules and finitely generated right *A*-modules. Therefore, the finitely generated injective left *A*-modules are precisely the modules of the form Hom*k*(*P*, *k*) where *P* is a finitely generated projective right *A*-module. For symmetric algebras, the duality is particularly well-behaved and projective modules and injective modules coincide.

For any Artinian ring, just as for commutative rings, there is a 1-1 correspondence between prime ideals and indecomposable injective modules. The correspondence in this case is perhaps even simpler: a prime ideal is an annihilator of a unique simple module, and the corresponding indecomposable injective module is its injective hull. For finite-dimensional algebras over fields, these injective hulls are finitely-generated modules (Lam 1999, §3G, §3J).

#### Computing injective hulls

If R is a Noetherian ring and ${\mathfrak {p}}$ is a prime ideal, set $E=E(R/{\mathfrak {p}})$ as the injective hull. The injective hull of $R/{\mathfrak {p}}$ over the Artinian ring $R/{\mathfrak {p}}^{k}$ can be computed as the module $(0:_{E}{\mathfrak {p}}^{k})$ . It is a module of the same length as $R/{\mathfrak {p}}^{k}$ . In particular, for the standard graded ring $R_{\bullet }=k[x_{1},\ldots ,x_{n}]_{\bullet }$ and ${\mathfrak {p}}=(x_{1},\ldots ,x_{n})$ , $E=\oplus _{i}{\text{Hom}}(R_{i},k)$ is an injective module, giving the tools for computing the indecomposable injective modules for artinian rings over k .

#### Self-injectivity

An Artin local ring $(R,{\mathfrak {m}},K)$ is injective over itself if and only if $soc(R)$ is a 1-dimensional vector space over K . This implies every local Gorenstein ring which is also Artin is injective over itself since has a 1-dimensional socle. A simple non-example is the ring $R=\mathbb {C} [x,y]/(x^{2},xy,y^{2})$ which has maximal ideal $(x,y)$ and residue field $\mathbb {C}$ . Its socle is $\mathbb {C} \cdot x\oplus \mathbb {C} \cdot y$ , which is 2-dimensional. The residue field has the injective hull ${\text{Hom}}_{\mathbb {C} }(\mathbb {C} \cdot x\oplus \mathbb {C} \cdot y,\mathbb {C} )$ .

### Modules over Lie algebras

For a Lie algebra ${\mathfrak {g}}$ over a field k of characteristic 0, the category of modules ${\mathcal {M}}({\mathfrak {g}})$ has a relatively straightforward description of its injective modules. Using the universal enveloping algebra any injective ${\mathfrak {g}}$ -module can be constructed from the ${\mathfrak {g}}$ -module

> ${\text{Hom}}_{k}(U({\mathfrak {g}}),V)$

for some k -vector space V . Note this vector space has a ${\mathfrak {g}}$ -module structure from the injection

> ${\mathfrak {g}}\hookrightarrow U({\mathfrak {g}})$

In fact, every ${\mathfrak {g}}$ -module has an injection into some ${\text{Hom}}_{k}(U({\mathfrak {g}}),V)$ and every injective ${\mathfrak {g}}$ -module is a direct summand of some ${\text{Hom}}_{k}(U({\mathfrak {g}}),V)$ .

## Theory

### Structure theorem for commutative Noetherian rings

Over a commutative Noetherian ring R , every injective module is a direct sum of indecomposable injective modules and every indecomposable injective module is the injective hull of the residue field at a prime ${\mathfrak {p}}$ . That is, for an injective $I\in {\text{Mod}}(R)$ , there is an isomorphism

> $I\cong \bigoplus _{i}E(R/{\mathfrak {p}}_{i})$

where $E(R/{\mathfrak {p}}_{i})$ are the injective hulls of the modules $R/{\mathfrak {p}}_{i}$ . In addition, if I is the injective hull of some module M then the ${\mathfrak {p}}_{i}$ are the associated primes of M .

### Submodules, quotients, products, and sums, Bass-Papp Theorem

Any product of (even infinitely many) injective modules is injective; conversely, if a direct product of modules is injective, then each module is injective (Lam 1999, p. 61). Every direct sum of finitely many injective modules is injective. In general, submodules, factor modules, or infinite direct sums of injective modules need not be injective. Every submodule of every injective module is injective if and only if the ring is Artinian semisimple (Golan & Head 1991, p. 152); every factor module of every injective module is injective if and only if the ring is hereditary, (Lam 1999, Th. 3.22).

Bass-Papp Theorem states that every infinite direct sum of right (left) injective modules is injective if and only if the ring is right (left) Noetherian, (Lam 1999, p. 80-81, Th 3.46).

### Baer's criterion

In Baer's original paper, he proved a useful result, usually known as Baer's Criterion, for checking whether a module is injective: a left *R*-module *Q* is injective if and only if any homomorphism *g* : *I* → *Q* defined on a left ideal *I* of *R* can be extended to all of *R*.

Using this criterion, one can show that **Q** is an injective abelian group (i.e. an injective module over **Z**). More generally, an abelian group is injective if and only if it is divisible. More generally still: a module over a principal ideal domain is injective if and only if it is divisible (the case of vector spaces is an example of this theorem, as every field is a principal ideal domain and every vector space is divisible). Over a general integral domain, we still have one implication: every injective module over an integral domain is divisible.

Baer's criterion has been refined in many ways (Golan & Head 1991, p. 119), including a result of (Smith 1981) and (Vámos 1983) that for a commutative Noetherian ring, it suffices to consider only prime ideals *I*. The dual of Baer's criterion, which would give a test for projectivity, is false in general. For instance, the **Z**-module **Q** satisfies the dual of Baer's criterion but is not projective.

### Injective cogenerators

Maybe the most important injective module is the abelian group **Q**/**Z**. It is an injective cogenerator in the category of abelian groups, which means that it is injective and any other module is contained in a suitably large product of copies of **Q**/**Z**. So in particular, every abelian group is a subgroup of an injective one. It is quite significant that this is also true over any ring: every module is a submodule of an injective one, or "the category of left *R*-modules has enough injectives." To prove this, one uses the peculiar properties of the abelian group **Q**/**Z** to construct an injective cogenerator in the category of left *R*-modules.

For a left *R*-module *M*, the so-called "character module" *M*+ = Hom**Z**(*M*,**Q**/**Z**) is a right *R*-module that exhibits an interesting duality, not between injective modules and projective modules, but between injective modules and flat modules (Enochs & Jenda 2000, pp. 78–80). For any ring *R*, a left *R*-module is flat if and only if its character module is injective. If *R* is left noetherian, then a left *R*-module is injective if and only if its character module is flat.

### Injective hulls

The injective hull of a module is the smallest injective module containing the given one and was described in (Eckmann & Schopf 1953).

One can use injective hulls to define a minimal injective resolution (see below). If each term of the injective resolution is the injective hull of the cokernel of the previous map, then the injective resolution has minimal length.

### Injective resolutions

Every module *M* also has an injective resolution: an exact sequence of the form

0 →

M

→

I

0

→

I

1

→

I

2

→ ...

where the *I* *j* are injective modules. Injective resolutions can be used to define derived functors such as the Ext functor.

The *length* of a finite injective resolution is the first index *n* such that *I**n* is nonzero and *I**i* = 0 for *i* greater than *n*. If a module *M* admits a finite injective resolution, the minimal length among all finite injective resolutions of *M* is called its injective dimension and denoted id(*M*). If *M* does not admit a finite injective resolution, then by convention the injective dimension is said to be infinite. (Lam 1999, §5C) As an example, consider a module *M* such that id(*M*) = 0. In this situation, the exactness of the sequence 0 → *M* → *I*0 → 0 indicates that the arrow in the center is an isomorphism, and hence *M* itself is injective.

Equivalently, the injective dimension of *M* is the minimal integer (if there is such, otherwise ∞) *n* such that Ext*N* *A*(–,*M*) = 0 for all *N* > *n*.

### Indecomposables

Every injective submodule of an injective module is a direct summand, so it is important to understand indecomposable injective modules, (Lam 1999, §3F).

Every indecomposable injective module has a local endomorphism ring. A module is called a *uniform module* if every two nonzero submodules have nonzero intersection. For an injective module *M* the following are equivalent:

- *M* is indecomposable
- *M* is nonzero and is the injective hull of every nonzero submodule
- *M* is uniform
- *M* is the injective hull of a uniform module
- *M* is the injective hull of a uniform cyclic module
- *M* has a local endomorphism ring

Over a Noetherian ring, every injective module is the direct sum of (uniquely determined) indecomposable injective modules. Over a commutative Noetherian ring, this gives a particularly nice understanding of all injective modules, described in (Matlis 1958). The indecomposable injective modules are the injective hulls of the modules *R*/*p* for *p* a prime ideal of the ring *R*. Moreover, the injective hull *M* of *R*/*p* has an increasing filtration by modules *M**n* given by the annihilators of the ideals *p**n*, and *M**n*+1/*M**n* is isomorphic as finite-dimensional vector space over the quotient field *k*(*p*) of *R*/*p* to Hom*R*/*p*(*p**n*/*p**n*+1, *k*(*p*)).

### Change of rings

It is important to be able to consider modules over subrings or quotient rings, especially for instance polynomial rings. In general, this is difficult, but a number of results are known, (Lam 1999, p. 62).

Let *S* and *R* be rings, and *P* be a left-*R*, right-*S* bimodule that is flat as a left-*R* module. For any injective right *S*-module *M*, the set of module homomorphisms Hom*S*( *P*, *M* ) is an injective right *R*-module. The same statement holds of course after interchanging left- and right- attributes.

For instance, if *R* is a subring of *S* such that *S* is a flat *R*-module, then every injective *S*-module is an injective *R*-module. In particular, if *R* is an integral domain and *S* its field of fractions, then every vector space over *S* is an injective *R*-module. Similarly, every injective *R*[*x*]-module is an injective *R*-module.

In the opposite direction, a ring homomorphism $f:S\to R$ makes *R* into a left-*R*, right-*S* bimodule, by left and right multiplication. Being free over itself *R* is also flat as a left *R*-module. Specializing the above statement for *P = R*, it says that when *M* is an injective right *S*-module the coinduced module $f_{*}M=\mathrm {Hom} _{S}(R,M)$ is an injective right *R*-module. Thus, coinduction over *f* produces injective *R*-modules from injective *S*-modules.

For quotient rings *R*/*I*, the change of rings is also very clear. An *R*-module is an *R*/*I*-module precisely when it is annihilated by *I*. The submodule ann*I*(*M*) = { *m* in *M* : *im* = 0 for all *i* in *I* } is a left submodule of the left *R*-module *M*, and is the largest submodule of *M* that is an *R*/*I*-module. If *M* is an injective left *R*-module, then ann*I*(*M*) is an injective left *R*/*I*-module. Applying this to *R*=**Z**, *I*=*n***Z** and *M*=**Q**/**Z**, one gets the familiar fact that **Z**/*n***Z** is injective as a module over itself. While it is easy to convert injective *R*-modules into injective *R*/*I*-modules, this process does not convert injective *R*-resolutions into injective *R*/*I*-resolutions, and the homology of the resulting complex is one of the early and fundamental areas of study of relative homological algebra.

The textbook (Rotman 1979, p. 103) has an erroneous proof that localization preserves injectives, but a counterexample was given in (Dade 1981).

### Self-injective rings

Every ring with unity is a free module and hence is a projective as a module over itself, but it is rarer for a ring to be injective as a module over itself, (Lam 1999, §3B). If a ring is injective over itself as a right module, then it is called a right self-injective ring. Every Frobenius algebra is self-injective, but no integral domain that is not a field is self-injective. Every proper quotient of a Dedekind domain is self-injective.

A right Noetherian, right self-injective ring is called a quasi-Frobenius ring, and is two-sided Artinian and two-sided injective, (Lam 1999, Th. 15.1). An important module theoretic property of quasi-Frobenius rings is that the projective modules are exactly the injective modules.

## Generalizations and specializations

### Injective objects

One also talks about injective objects in categories more general than module categories, for instance in functor categories or in categories of sheaves of O*X*-modules over some ringed space (*X*,O*X*). The following general definition is used: an object *Q* of the category *C* is injective if for any monomorphism *f* : *X* → *Y* in *C* and any morphism *g* : *X* → *Q* there exists a morphism *h* : *Y* → *Q* with *hf* = *g*.

### Divisible groups

The notion of injective object in the category of abelian groups was studied somewhat independently of injective modules under the term divisible group. Here a **Z**-module *M* is injective if and only if *n*⋅*M* = *M* for every nonzero integer *n*. Here the relationships between flat modules, pure submodules, and injective modules is more clear, as it simply refers to certain divisibility properties of module elements by integers.

### Pure injectives

In relative homological algebra, the extension property of homomorphisms may be required only for certain submodules, rather than for all. For instance, a pure injective module is a module in which a homomorphism from a pure submodule can be extended to the whole module.

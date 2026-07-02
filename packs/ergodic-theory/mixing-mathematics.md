---
title: "Mixing (mathematics)"
source: https://en.wikipedia.org/wiki/Mixing_(mathematics)
domain: ergodic-theory
license: CC-BY-SA-4.0
tags: ergodic theory, measure-preserving system, ergodic theorem, topological entropy
fetched: 2026-07-02
---

# Mixing (mathematics)

In mathematics, **mixing** is an abstract concept originating from physics: the attempt to describe the irreversible thermodynamic process of mixing in the everyday world: e.g. mixing paint, mixing drinks, mixing metals.

The concept appears in ergodic theory—the study of stochastic processes and measure-preserving dynamical systems. Several different definitions for mixing exist, including *strong mixing*, *weak mixing* and *topological mixing*, with the last not requiring a measure to be defined. Some of the different definitions of mixing can be arranged in a hierarchical order; thus, strong mixing implies weak mixing. Furthermore, weak mixing (and thus also strong mixing) implies ergodicity: that is, every system that is weakly mixing is also ergodic (and so one says that mixing is a "stronger" condition than ergodicity).

## Informal explanation

The mathematical definition of mixing aims to capture the ordinary every-day process of mixing, such as mixing paints, drinks, cooking ingredients, industrial process mixing, smoke in a smoke-filled room, and so on. To provide the mathematical rigor, such descriptions begin with the definition of a measure-preserving dynamical system, written as ⁠ $(X,{\mathcal {A}},\mu ,T)$ ⁠.

The set X is understood to be the total space to be filled: the mixing bowl, the smoke-filled room, *etc.* The measure $\mu$ is understood to define the natural volume of the space X and of its subspaces. The collection of subspaces is denoted by ⁠ ${\mathcal {A}}$ ⁠, and the size of any given subset $A\subset X$ is ⁠ $\mu (A)$ ⁠; the size is its volume. Naively, one could imagine ${\mathcal {A}}$ to be the power set of ⁠ X ⁠; this doesn't quite work, as not all subsets of a space have a volume (famously, the Banach–Tarski paradox). Thus, conventionally, ${\mathcal {A}}$ consists of the measurable subsets—the subsets that do have a volume. It is always taken to be a Borel set—the collection of subsets that can be constructed by taking intersections, unions and set complements; these can always be taken to be measurable.

The time evolution of the system is described by a map $T:X\to X$ . Given some subset $A\subset X$ , its map $T(A)$ will in general be a deformed version of A – it is squashed or stretched, folded or cut into pieces. Mathematical examples include the baker's map and the horseshoe map, both inspired by bread-making. The set $T(A)$ must have the same volume as A ; the squashing/stretching does not alter the volume of the space, only its distribution. Such a system is "measure-preserving" (area-preserving, volume-preserving).

A formal difficulty arises when one tries to reconcile the volume of sets with the need to preserve their size under a map. The problem arises because, in general, several different points in the domain of a function can map to the same point in its range; that is, there may be $x\neq y$ with ⁠ $T(x)=T(y)$ ⁠. Worse, a single point $x\in X$ has no size. These difficulties can be avoided by working with the inverse map ⁠ $T^{-1}:{\mathcal {A}}\to {\mathcal {A}}$ ⁠; it will map any given subset $A\subset X$ to the parts that were assembled to make it: these parts are ⁠ $T^{-1}(A)\in {\mathcal {A}}$ ⁠. It has the important property of not "losing track" of where things came from. More strongly, it has the important property that *any* (measure-preserving) map ${\mathcal {A}}\to {\mathcal {A}}$ is the inverse of some map ⁠ $X\to X$ ⁠. The proper definition of a volume-preserving map is one for which $\mu (A)=\mu (T^{-1}(A))$ because $T^{-1}(A)$ describes all the pieces-parts that A came from.

One is now interested in studying the time evolution of the system. If a set $A\in {\mathcal {A}}$ eventually visits all of X over a long period of time (that is, if $\cup _{k=1}^{n}T^{k}(A)$ approaches all of X for large n ), the system is said to be ergodic. If every set A behaves in this way, the system is a conservative system, placed in contrast to a dissipative system, where some subsets A wander away, never to be returned to. An example would be water running downhill—once it's run down, it will never come back up again. The lake that forms at the bottom of this river can, however, become well-mixed. The hopf decomposition theorem states that every measure space can be split into two parts: the conservative part, and the dissipative part.

Mixing is a stronger statement than ergodicity. Mixing asks for this ergodic property to hold between any two sets ⁠ $A,B$ ⁠, and not just between some set A and ⁠ X ⁠. That is, given any two sets ⁠ $A,B\in {\mathcal {A}}$ ⁠, a system is said to be (topologically) mixing if there is an integer N such that, for all $A,B$ and ⁠ $n>N$ ⁠, one has that $T^{n}(A)\cap B\neq \varnothing$ . Here, $\cap$ denotes set intersection and $\varnothing$ is the empty set.

The above definition of topological mixing should be enough to provide an informal idea of mixing (it is equivalent to the formal definition, given below). However, it made no mention of the volume of A and ⁠ B ⁠, and, indeed, there is another definition that explicitly works with the volume. Several, actually; one has both strong mixing and weak mixing; they are inequivalent, although a strong mixing system is always weakly mixing. The measure-based definitions are not compatible with the definition of topological mixing: there are systems which are one, but not the other. The general situation remains cloudy: for example, given three sets ⁠ $A,B,C\in {\mathcal {A}}$ ⁠, one can define 3-mixing. As of 2020, it is not known if 2-mixing implies 3-mixing. (If one thinks of ergodicity as "1-mixing", then it is clear that 1-mixing does not imply 2-mixing; there are systems that are ergodic but not mixing.)

The concept of *strong mixing* is made in reference to the volume of a pair of sets. Consider, for example, a set A of colored dye that is being mixed into a cup of some sort of sticky liquid, say, corn syrup, or shampoo, or the like. Practical experience shows that mixing sticky fluids can be quite hard: there is usually some corner of the container where it is hard to get the dye mixed into. Pick as set B that hard-to-reach corner. The question of mixing is then, can A , after a long enough period of time, not only penetrate into B but also fill B with the same proportion as it does elsewhere?

One phrases the definition of strong mixing as the requirement that

$\lim _{n\to \infty }\mu \left(T^{-n}A\cap B\right)=\mu (A)\mu (B).$

The time parameter n serves to separate A and B in time, so that one is mixing A while holding the test volume B fixed. The product $\mu (A)\mu (B)$ is a bit more subtle. Imagine that the volume B is 10% of the total volume, and that the volume of dye A will also be 10% of the grand total. If A is uniformly distributed, then it is occupying 10% of B , which itself is 10% of the total, and so, in the end, after mixing, the part of A that is in B is 1% of the total volume. That is, $\mu \left({\mbox{after-mixing}}(A)\cap B\right)=\mu (A)\mu (B).$ This product-of-volumes has more than passing resemblance to Bayes' theorem in probabilities; this is not an accident, but rather a consequence that measure theory and probability theory are the same theory: they share the same axioms (the Kolmogorov axioms), even as they use different notation.

The reason for using $T^{-n}A$ instead of $T^{n}A$ in the definition is a bit subtle, but it follows from the same reasons why $T^{-1}A$ was used to define the concept of a measure-preserving map. When looking at how much dye got mixed into the corner B , one wants to look at where that dye "came from" (presumably, it was poured in at the top, at some time in the past). One must be sure that every place it might have "come from" eventually gets mixed into B .

## Mixing in dynamical systems

Let $(X,{\mathcal {A}},\mu ,T)$ be a measure-preserving dynamical system, with *T* being the time-evolution or shift operator. The system is said to be **strong mixing** if, for any $A,B\in {\mathcal {A}}$ , one has

$\lim _{n\to \infty }\mu \left(A\cap T^{-n}B\right)=\mu (A)\mu (B).$

For shifts parametrized by a continuous variable instead of a discrete integer *n*, the same definition applies, with $T^{-n}$ replaced by $T_{g}$ with *g* being the continuous-time parameter.

A dynamical system is said to be **weak mixing** if one has

$\lim _{n\to \infty }{\frac {1}{n}}\sum _{k=0}^{n-1}\left|\mu (A\cap T^{-k}B)-\mu (A)\mu (B)\right|=0.$

In other words, T is strong mixing if $\mu (A\cap T^{-n}B)-\mu (A)\mu (B)\to 0$ in the usual sense, weak mixing if

$\left|\mu (A\cap T^{-n}B)-\mu (A)\mu (B)\right|\to 0,$

in the Cesàro sense, and ergodic if $\mu \left(A\cap T^{-n}B\right)\to \mu (A)\mu (B)$ in the Cesàro sense. Hence, strong mixing implies weak mixing, which implies ergodicity. However, the converses are not true: There exist ergodic dynamical systems which are not weakly mixing, and weakly mixing dynamical systems which are not strongly mixing. The Chacon system was historically the first example given of a system that is weak mixing but not strong mixing.

**Theorem.** Weak mixing implies ergodicity.

**Proof.** If the action of the map decomposes into two components ⁠ $A,B$ ⁠, then we have ⁠ $\mu (T^{-n}(A)\cap B)=\mu (A\cap B)=\mu (\emptyset )=0$ ⁠, so weak mixing implies ⁠ $\vert \mu (A\cap B)-\mu (A)\mu (B)\vert =0$ ⁠, so one of $A,B$ has zero measure, and the other one has full measure.

### Covering families

Given a topological space, such as the unit interval (whether it has its end points or not), we can construct a measure on it by taking the open sets, then take their unions, complements, unions, complements, and so on to infinity, to obtain all the Borel sets. Next, we define a measure $\mu$ on the Borel sets, then add in all the subsets of measure-zero ("negligible sets"). This is how we obtain the Lebesgue measure and the Lebesgue measurable sets.

In most applications of ergodic theory, the underlying space is almost-everywhere isomorphic to an open subset of some $\mathbb {R} ^{n}$ , and so it is a Lebesgue measure space. Verifying strong-mixing can be simplified if we only need to check a smaller set of measurable sets.

A covering family ${\mathcal {C}}$ is a set of measurable sets, such that any open set is a *disjoint* union of sets in it. Compare this with base in topology, which is less restrictive as it allows non-disjoint unions.

**Theorem.** For Lebesgue measure spaces, if T is measure-preserving, and $\lim _{n}\mu (T^{-n}(A)\cap B)=\mu (A)\mu (B)$ for all $A,B$ in a covering family, then T is strong mixing.

**Proof.** Extend the mixing equation from all $A,B$ in the covering family, to all open sets by disjoint union, to all closed sets by taking the complement, to all measurable sets by using the regularity of Lebesgue measure to approximate any set with open and closed sets. Thus, $\lim _{n}\mu (T^{-n}(A)\cap B)=\mu (A)\mu (B)$ for all measurable ⁠ $A,B$ ⁠.

### *L*2 formulation

The properties of ergodicity, weak mixing and strong mixing of a measure-preserving dynamical system can also be characterized by the average of observables. By von Neumann's ergodic theorem, ergodicity of a dynamical system $(X,{\mathcal {A}},\mu ,T)$ is equivalent to the property that, for any function $f\in L^{2}(X,\mu )$ , the sequence $(f\circ T^{n})_{n\geq 0}$ converges strongly and in the sense of Cesàro to ⁠ $\int _{X}f\,d\mu$ ⁠, i.e.,

$\lim _{N\to \infty }\left\|{1 \over N}\sum _{n=0}^{N-1}f\circ T^{n}-\int _{X}f\,d\mu \right\|_{L^{2}(X,\mu )}=0.$

A dynamical system $(X,{\mathcal {A}},\mu ,T)$ is weakly mixing if, for any functions f and $g\in L^{2}(X,\mu ),$

$\lim _{N\to \infty }{1 \over N}\sum _{n=0}^{N-1}\left|\int _{X}f\circ T^{n}\cdot g\,d\mu -\int _{X}f\,d\mu \cdot \int _{X}g\,d\mu \right|=0.$

A dynamical system $(X,{\mathcal {A}},\mu ,T)$ is strongly mixing if, for any function ⁠ $f\in L^{2}(X,\mu )$ ⁠, the sequence $(f\circ T^{n})_{n\geq 0}$ converges weakly to ⁠ $\int _{X}f\,d\mu$ ⁠, i.e., for any function $g\in L^{2}(X,\mu ),$

$\lim _{n\to \infty }\int _{X}f\circ T^{n}\cdot g\,d\mu =\int _{X}f\,d\mu \cdot \int _{X}g\,d\mu .$

Since the system is assumed to be measure preserving, this last line is equivalent to saying that the covariance ⁠ $\lim _{n\to \infty }\operatorname {Cov} (f\circ T^{n},g)=0$ ⁠, so that the random variables $f\circ T^{n}$ and g become orthogonal as n grows. Actually, since this works for any function ⁠ g ⁠, one can informally see mixing as the property that the random variables $f\circ T^{n}$ and g become independent as n grows.

### Products of dynamical systems

Given two measured dynamical systems $(X,\mu ,T)$ and $(Y,\nu ,S),$ one can construct a dynamical system $(X\times Y,\mu \otimes \nu ,T\times S)$ on the Cartesian product by defining $(T\times S)(x,y)=(T(x),S(y)).$ We then have the following characterizations of weak mixing:

Proposition.

A dynamical system

$(X,\mu ,T)$

is weakly mixing

if and only if

, for any ergodic dynamical system

⁠

$(Y,\nu ,S)$

⁠

, the system

$(X\times Y,\mu \otimes \nu ,T\times S)$

is also ergodic.

Proposition.

A dynamical system

$(X,\mu ,T)$

is weakly mixing if and only if

$(X^{2},\mu \otimes \mu ,T\times T)$

is also ergodic. If this is the case, then

$(X^{2},\mu \otimes \mu ,T\times T)$

is also weakly mixing.

### Generalizations

The definition given above is sometimes called **strong 2-mixing**, to distinguish it from higher orders of mixing. A **strong 3-mixing system** may be defined as a system for which

$\lim _{m,n\to \infty }\mu (A\cap T^{-m}B\cap T^{-m-n}C)=\mu (A)\mu (B)\mu (C)$

holds for all measurable sets *A*, *B*, *C*. We can define **strong k-mixing** similarly. A system which is **strong** *k*-**mixing** for all *k* = 2,3,4,... is called **mixing of all orders**.

It is unknown whether strong 2-mixing implies strong 3-mixing. It is known that strong *m*-mixing implies ergodicity.

### Examples

Irrational rotations of the circle, and more generally irreducible translations on a torus, are ergodic but neither strongly nor weakly mixing with respect to the Lebesgue measure.

Many maps considered as chaotic are strongly mixing for some well-chosen invariant measure, including: the dyadic map, Arnold's cat map, horseshoe maps, Kolmogorov automorphisms, and the Anosov flow (the geodesic flow on the unit tangent bundle of compact manifolds of negative curvature.)

The dyadic map is "shift to left in binary". In general, for any $n\in \{2,3,\dots \}$ , the "shift to left in base ⁠ n ⁠" map $T(x)=nx{\bmod {1}}$ is strongly mixing on the covering family ⁠ $\left\{\left({\tfrac {k}{n^{s}}},{\tfrac {k+1}{n^{s}}}\right)\smallsetminus \mathbb {Q} :s\geq 0,\leq k<n^{s}\right\}$ ⁠, therefore it is strongly mixing on ⁠ $(0,1)\smallsetminus \mathbb {Q}$ ⁠, and therefore it is strongly mixing on ⁠ $[0,1]$ ⁠.

Similarly, for any finite or countable alphabet ⁠ $\Sigma$ ⁠, we can impose a discrete probability distribution on it, then consider the probability distribution on the "coin flip" space, where each "coin flip" can take results from ⁠ $\Sigma$ ⁠. We can either construct the singly-infinite space $\Sigma ^{\mathbb {N} }$ or the doubly-infinite space ⁠ $\Sigma ^{\mathbb {Z} }$ ⁠. In both cases, the **shift map** (one letter to the left) is strongly mixing, since it is strongly mixing on the covering family of cylinder sets. The Baker's map is isomorphic to a shift map, so it is strongly mixing.

## Topological mixing

A form of mixing may be defined without appeal to a measure, using only the topology of the system. A continuous map $f:X\to X$ is said to be **topologically transitive** if, for every pair of non-empty open sets $A,B\subset X$ , there exists an integer *n* such that

$f^{n}(A)\cap B\neq \varnothing$

where $f^{n}$ is the *n*th iterate of *f*. In the operator theory, a topologically transitive bounded linear operator (a continuous linear map on a topological vector space) is usually called hypercyclic operator.

A related idea is expressed by the wandering set, in fact a point is non wandering if

$\exists n>N\geq 0:f^{n}(U)\cap U\neq \varnothing$

I.e the nth image is not "too far away from", and "still intersects", the initial neighborhood U. In the previous case "it wanders" cause the set B can be any subset in $\Omega$

**Lemma:** If *X* is a complete metric space with no isolated point, then *f* is topologically transitive if and only if there exists a hypercyclic point $x\in X$ , that is, a point *x* such that its orbit $\{f^{n}(x):n\in \mathbb {N} \}$ is dense in *X*.

A system is said to be **topologically mixing** if, given open sets A and ⁠ B ⁠, there exists an integer *N*, such that, for all ⁠ $n>N$ ⁠, one has

$f^{n}(A)\cap B\neq \varnothing .$

For a continuous-time system, $f^{n}$ is replaced by the flow ⁠ $\varphi _{g}$ ⁠, with *g* being the continuous parameter, with the requirement that a non-empty intersection hold for all ⁠ $\Vert g\Vert >N$ ⁠.

A **weak topological mixing** is one that has no non-constant continuous (with respect to the topology) eigenfunctions of the shift operator.

Topological mixing neither implies, nor is implied by either weak or strong mixing: there are examples of systems that are weak mixing but not topologically mixing, and examples that are topologically mixing but not strong mixing.

## Mixing in stochastic processes

Let $(X_{t})_{-\infty <t<\infty }$ be a stochastic process on a probability space ⁠ $(\Omega ,{\mathcal {F}},\mathbb {P} )$ ⁠. The sequence space into which the process maps can be endowed with a topology, the product topology. The open sets of this topology are called cylinder sets. These cylinder sets generate a σ-algebra, the Borel σ-algebra; this is the smallest σ-algebra that contains the topology.

Define a function $\alpha$ , called the **strong mixing coefficient**, as

$\alpha (s)=\sup \left\{|\mathbb {P} (A\cap B)-\mathbb {P} (A)\mathbb {P} (B)|:-\infty <t<\infty ,A\in X_{-\infty }^{t},B\in X_{t+s}^{\infty }\right\}$

for all ⁠ $-\infty <s<\infty$ ⁠. The symbol $X_{a}^{b}$ , with $-\infty \leq a\leq b\leq \infty$ denotes a sub-σ-algebra of the σ-algebra; it is the set of cylinder sets that are specified between times *a* and *b*, i.e. the σ-algebra generated by ⁠ $\{X_{a},X_{a+1},\ldots ,X_{b}\}$ ⁠.

The process $(X_{t})_{-\infty <t<\infty }$ is said to be **strongly mixing** if $\alpha (s)\to 0$ as ⁠ $s\to \infty$ ⁠. That is to say, a strongly mixing process is such that, in a way that is uniform over all times t and all events, the events before time t and the events after time $t+s$ tend towards being independent as $s\to \infty$ ; more colloquially, the process, in a strong sense, forgets its history.

### Mixing in Markov processes

Suppose $(X_{t})$ were a stationary Markov process with stationary distribution $\mathbb {Q}$ and let $L^{2}(\mathbb {Q} )$ denote the space of Borel-measurable functions that are square-integrable with respect to the measure $\mathbb {Q}$ . Also let

${\mathcal {E}}_{t}\varphi (x)=\mathbb {E} [\varphi (X_{t})\mid X_{0}=x]$

denote the conditional expectation operator on $L^{2}(\mathbb {Q} ).$ Finally, let

$Z=\left\{\varphi \in L^{2}(\mathbb {Q} ):\int \varphi \,d\mathbb {Q} =0\right\}$

denote the space of square-integrable functions with mean zero.

The ***ρ*-mixing coefficients** of the process {*xt*} are

$\rho _{t}=\sup _{\varphi \in Z:\,\|\varphi \|_{2}=1}\|{\mathcal {E}}_{t}\varphi \|_{2}.$

The process is called ***ρ*-mixing** if these coefficients converge to zero as *t* → ∞, and “*ρ*-mixing with exponential decay rate” if *ρt* < *e*−*δt* for some *δ* > 0. For a stationary Markov process, the coefficients *ρt* may either decay at an exponential rate, or be always equal to one.

The ***α*-mixing coefficients** of the process {*xt*} are

$\alpha _{t}=\sup _{\varphi \in Z:\|\varphi \|_{\infty }=1}\|{\mathcal {E}}_{t}\varphi \|_{1}.$

The process is called ***α*-mixing** if these coefficients converge to zero as *t* → ∞, it is "*α*-mixing with exponential decay rate" if *αt* < *γe*−*δt* for some *δ* > 0, and it is ***α*-mixing with a sub-exponential decay rate** if *αt* < *ξ*(*t*) for some non-increasing function $\xi$ satisfying

${\frac {\ln \xi (t)}{t}}\to 0$

as ⁠ $t\to \infty$ ⁠.

The *α*-mixing coefficients are always smaller than the *ρ*-mixing ones: *αt* ≤ *ρt*, therefore if the process is *ρ*-mixing, it will necessarily be *α*-mixing too. However, when *ρt* = 1, the process may still be *α*-mixing, with sub-exponential decay rate.

The ***β*-mixing coefficients** are given by

$\beta _{t}=\int \sup _{0\leq \varphi \leq 1}\left|{\mathcal {E}}_{t}\varphi (x)-\int \varphi \,d\mathbb {Q} \right|\,d\mathbb {Q} .$

The process is called ***β*-mixing** if these coefficients converge to zero as *t* → ∞, it is ***β*-mixing with an exponential decay rate** if *βt* < *γe*−*δt* for some *δ* > 0, and it is ***β*-mixing with a sub-exponential decay rate** if *βtξ*(*t*) → 0 as *t* → ∞ for some non-increasing function $\xi$ satisfying

${\frac {\ln \xi (t)}{t}}\to 0$

as $t\to \infty$ .

A strictly stationary Markov process is *β*-mixing if and only if it is an aperiodic recurrent Harris chain. The *β*-mixing coefficients are always bigger than the *α*-mixing ones, so if a process is *β*-mixing it will also be *α*-mixing. There is no direct relationship between *β*-mixing and *ρ*-mixing: neither of them implies the other.

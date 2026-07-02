---
title: "Measure-preserving dynamical system"
source: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
domain: ergodic-theory
license: CC-BY-SA-4.0
tags: ergodic theory, measure-preserving system, ergodic theorem, topological entropy
fetched: 2026-07-02
---

# Measure-preserving dynamical system

In mathematics, a **measure-preserving dynamical system** is an object of study in the abstract formulation of dynamical systems, and ergodic theory in particular. Measure-preserving systems obey the Poincaré recurrence theorem, and are a special case of conservative systems. They provide the formal, mathematical basis for a broad range of physical systems, and, in particular, many systems from classical mechanics (in particular, most non-dissipative systems) as well as systems in thermodynamic equilibrium.

## Definition

A measure-preserving dynamical system is defined as a probability space and a measure-preserving transformation on it. In more detail, it is a system

$(X,{\mathcal {B}},\mu ,T)$

with the following structure:

- X is a set,
- ${\mathcal {B}}$ is a σ-algebra over X ,
- ${\displaystyle \mu$ is a probability measure, so that $\mu (X)=1$ , and $\mu (\varnothing )=0$ ,
- $T:X\rightarrow X$ is a measurable transformation which preserves the measure $\mu$ , i.e., $\forall A\in {\mathcal {B}}\;\;\mu (T^{-1}(A))=\mu (A)$ .

## Discussion

One may ask why the measure preserving transformation is defined in terms of the inverse $\mu (T^{-1}(A))=\mu (A)$ instead of the forward transformation $\mu (T(A))=\mu (A)$ . This can be understood intuitively.

Consider the typical measure on the unit interval $[0,1]$ , and a map $Tx=2x\mod 1={\begin{cases}2x{\text{ if }}x<1/2\\2x-1{\text{ if }}x>1/2\\\end{cases}}$ . This is the Bernoulli map. Now, distribute an even layer of paint on the unit interval $[0,1]$ , and then map the paint forward. The paint on the $[0,1/2]$ half is spread thinly over all of $[0,1]$ , and the paint on the $[1/2,1]$ half as well. The two layers of thin paint, layered together, recreates the exact same paint thickness.

More generally, the paint that would arrive at subset $A\subset [0,1]$ comes from the subset $T^{-1}(A)$ . For the paint thickness to remain unchanged (measure-preserving), the mass of incoming paint should be the same: $\mu (A)=\mu (T^{-1}(A))$ .

Consider a mapping ${\mathcal {T}}$ of power sets:

${\mathcal {T}}:P(X)\to P(X)$

Consider now the special case of maps ${\mathcal {T}}$ which preserve intersections, unions and complements (so that it is a map of Borel sets) and also sends X to X (because we want it to be conservative). Every such conservative, Borel-preserving map can be specified by some surjective map $T:X\to X$ by writing ${\mathcal {T}}(A)=T^{-1}(A)$ . Of course, one could also define ${\mathcal {T}}(A)=T(A)$ , but this is not enough to specify all such possible maps ${\mathcal {T}}$ . That is, conservative, Borel-preserving maps ${\mathcal {T}}$ cannot, in general, be written in the form ${\mathcal {T}}(A)=T(A);$ .

$\mu (T^{-1}(A))$ has the form of a pushforward, whereas $\mu (T(A))$ is generically called a pullback. Almost all properties and behaviors of dynamical systems are defined in terms of the pushforward. For example, the transfer operator is defined in terms of the pushforward of the transformation map T ; the measure $\mu$ can now be understood as an invariant measure; it is just the Frobenius–Perron eigenvector of the transfer operator (recall, the FP eigenvector is the largest eigenvector of a matrix; in this case it is the eigenvector which has the eigenvalue one: the invariant measure.)

There are two classification problems of interest. One, discussed below, fixes $(X,{\mathcal {B}},\mu )$ and asks about the isomorphism classes of a transformation map T . The other, discussed in transfer operator, fixes $(X,{\mathcal {B}})$ and T , and asks about maps $\mu$ that are measure-like. Measure-like, in that they preserve the Borel properties, but are no longer invariant; they are in general dissipative and so give insights into dissipative systems and the route to equilibrium.

In terms of physics, the measure-preserving dynamical system $(X,{\mathcal {B}},\mu ,T)$ often describes a physical system that is in equilibrium, for example, thermodynamic equilibrium. One might ask: how did it get that way? Often, the answer is by stirring, mixing, turbulence, thermalization or other such processes. If a transformation map T describes this stirring, mixing, etc. then the system $(X,{\mathcal {B}},\mu ,T)$ is all that is left, after all of the transient modes have decayed away. The transient modes are precisely those eigenvectors of the transfer operator that have eigenvalue less than one; the invariant measure $\mu$ is the one mode that does not decay away. The rate of decay of the transient modes are given by (the logarithm of) their eigenvalues; the eigenvalue one corresponds to infinite half-life.

## Informal example

The microcanonical ensemble from physics provides an informal example. Consider, for example, a fluid, gas or plasma in a box of width, length and height $w\times l\times h,$ consisting of N atoms. A single atom in that box might be anywhere, having arbitrary velocity; it would be represented by a single point in $w\times l\times h\times \mathbb {R} ^{3}.$ A given collection of N atoms would then be a *single point* somewhere in the space $(w\times l\times h)^{N}\times \mathbb {R} ^{3N}.$ The "ensemble" is the collection of all such points, that is, the collection of all such possible boxes (of which there are an uncountably-infinite number). This ensemble of all-possible-boxes is the space X above.

In the case of an ideal gas, the measure $\mu$ is given by the Maxwell–Boltzmann distribution. It is a product measure, in that if $p_{i}(x,y,z,v_{x},v_{y},v_{z})\,d^{3}x\,d^{3}p$ is the probability of atom i having position and velocity $x,y,z,v_{x},v_{y},v_{z}$ , then, for N atoms, the probability is the product of N of these. This measure is understood to apply to the ensemble. So, for example, one of the possible boxes in the ensemble has all of the atoms on one side of the box. One can compute the likelihood of this, in the Maxwell–Boltzmann measure. It will be enormously tiny, of order ${\mathcal {O}}\left(2^{-3N}\right).$ Of all possible boxes in the ensemble, this is a ridiculously small fraction.

The only reason that this is an "informal example" is because writing down the transition function T is difficult, and, even if written down, it is hard to perform practical computations with it. Difficulties are compounded if there are interactions between the particles themselves, like a van der Waals interaction or some other interaction suitable for a liquid or a plasma; in such cases, the invariant measure is no longer the Maxwell–Boltzmann distribution. The art of physics is finding reasonable approximations.

This system does exhibit one key idea from the classification of measure-preserving dynamical systems: two ensembles, having different temperatures, are inequivalent. The entropy for a given canonical ensemble depends on its temperature; as physical systems, it is "obvious" that when the temperatures differ, so do the systems. This holds in general: systems with different entropy are not isomorphic.

## Examples

Unlike the informal example above, the examples below are sufficiently well-defined and tractable that explicit, formal computations can be performed.

- μ could be the normalized angle measure dθ/2π on the unit circle, and *T* a rotation. See equidistribution theorem;
- the Bernoulli scheme;
- the interval exchange transformation;
- with the definition of an appropriate measure, a subshift of finite type;
- the base flow of a random dynamical system;
- the flow of a Hamiltonian vector field on the tangent bundle of a closed connected smooth manifold is measure-preserving (using the measure induced on the Borel sets by the symplectic volume form) by Liouville's theorem (Hamiltonian);
- for certain maps and Markov processes, the Krylov–Bogolyubov theorem establishes the existence of a suitable measure to form a measure-preserving dynamical system.

## Generalization to groups and monoids

The definition of a measure-preserving dynamical system can be generalized to the case in which *T* is not a single transformation that is iterated to give the dynamics of the system, but instead is a monoid (or even a group, in which case we have the action of a group upon the given probability space) of transformations *Ts* : *X* → *X* parametrized by *s* ∈ **Z** (or **R**, or **N** ∪ {0}, or [0, +∞)), where each transformation *Ts* satisfies the same requirements as *T* above. In particular, the transformations obey the rules:

- $T_{0}=\mathrm {id} _{X}:X\rightarrow X$ , the identity function on *X*;
- $T_{s}\circ T_{t}=T_{t+s}$ , whenever all the terms are well-defined;
- $T_{s}^{-1}=T_{-s}$ , whenever all the terms are well-defined.

The earlier, simpler case fits into this framework by defining *Ts* = *Ts* for *s* ∈ **N**.

## Homomorphisms

The concept of a homomorphism and an isomorphism may be defined.

Consider two dynamical systems $(X,{\mathcal {A}},\mu ,T)$ and $(Y,{\mathcal {B}},\nu ,S)$ . Then a mapping

$\varphi :X\to Y$

is a **homomorphism of dynamical systems** if it satisfies the following three properties:

1. The map $\varphi \$ is measurable.
2. For each $B\in {\mathcal {B}}$ , one has $\mu (\varphi ^{-1}B)=\nu (B)$ .
3. For $\mu$ -almost all $x\in X$ , one has $\varphi (Tx)=S(\varphi x)$ .

The system $(Y,{\mathcal {B}},\nu ,S)$ is then called a **factor** of $(X,{\mathcal {A}},\mu ,T)$ .

The map $\varphi \;$ is an **isomorphism of dynamical systems** if, in addition, there exists another mapping

$\psi :Y\to X$

that is also a homomorphism, which satisfies

1. for $\mu$ -almost all $x\in X$ , one has $x=\psi (\varphi x)$ ;
2. for $\nu$ -almost all $y\in Y$ , one has $y=\varphi (\psi y)$ .

Hence, one may form a category of dynamical systems and their homomorphisms.

## Generic points

A point *x* ∈ *X* is called a **generic point** if the orbit of the point is distributed uniformly according to the measure.

## Symbolic names and generators

Consider a dynamical system $(X,{\mathcal {B}},T,\mu )$ , and let *Q* = {*Q*1, ..., *Qk*} be a partition of *X* into *k* measurable pair-wise disjoint sets. Given a point *x* ∈ *X*, clearly *x* belongs to only one of the *Qi*. Similarly, the iterated point *Tnx* can belong to only one of the parts as well. The **symbolic name** of *x*, with regards to the partition *Q*, is the sequence of integers {*a**n*} such that

$T^{n}x\in Q_{a_{n}}.$

The set of symbolic names with respect to a partition is called the symbolic dynamics of the dynamical system. A partition *Q* is called a **generator** or **generating partition** if μ-almost every point *x* has a unique symbolic name.

## Operations on partitions

Given a partition Q = {*Q*1, ..., *Q**k*} and a dynamical system $(X,{\mathcal {B}},T,\mu )$ , define the *T*-pullback of *Q* as

$T^{-1}Q=\{T^{-1}Q_{1},\ldots ,T^{-1}Q_{k}\}.$

Further, given two partitions *Q* = {*Q*1, ..., *Qk*} and *R* = {*R*1, ..., *R**m*}, define their refinement as

$Q\vee R=\{Q_{i}\cap R_{j}\mid i=1,\ldots ,k,\ j=1,\ldots ,m,\ \mu (Q_{i}\cap R_{j})>0\}.$

With these two constructs, the *refinement of an iterated pullback* is defined as

${\begin{aligned}\bigvee _{n=0}^{N}T^{-n}Q&=\{Q_{i_{0}}\cap T^{-1}Q_{i_{1}}\cap \cdots \cap T^{-N}Q_{i_{N}}\\&{}\qquad {\mbox{ where }}i_{\ell }=1,\ldots ,k,\ \ell =0,\ldots ,N,\ \\&{}\qquad \qquad \mu \left(Q_{i_{0}}\cap T^{-1}Q_{i_{1}}\cap \cdots \cap T^{-N}Q_{i_{N}}\right)>0\}\\\end{aligned}}$

which plays crucial role in the construction of the measure-theoretic entropy of a dynamical system.

## Measure-theoretic entropy

The entropy of a partition ${\mathcal {Q}}$ is defined as

$H({\mathcal {Q}})=-\sum _{Q\in {\mathcal {Q}}}\mu (Q)\log \mu (Q).$

The measure-theoretic entropy of a dynamical system $(X,{\mathcal {B}},T,\mu )$ with respect to a partition *Q* = {*Q*1, ..., *Q**k*} is then defined as

$h_{\mu }(T,{\mathcal {Q}})=\lim _{N\rightarrow \infty }{\frac {1}{N}}H\left(\bigvee _{n=0}^{N}T^{-n}{\mathcal {Q}}\right).$

Finally, the **Kolmogorov–Sinai metric** or **measure-theoretic entropy** of a dynamical system $(X,{\mathcal {B}},T,\mu )$ is defined as

$h_{\mu }(T)=\sup _{\mathcal {Q}}h_{\mu }(T,{\mathcal {Q}}).$

where the supremum is taken over all finite measurable partitions. A theorem of Yakov Sinai in 1959 shows that the supremum is actually obtained on partitions that are generators. Thus, for example, the entropy of the Bernoulli process is log 2, since almost every real number has a unique binary expansion. That is, one may partition the unit interval into the intervals [0, 1/2) and [1/2, 1]. Every real number *x* is either less than 1/2 or not; and likewise so is the fractional part of 2*n**x*.

If the space *X* is compact and endowed with a topology, or is a metric space, then the topological entropy may also be defined.

If T is an ergodic, piecewise expanding, and Markov on $X\subset \mathbb {R}$ , and $\mu$ is absolutely continuous with respect to the Lebesgue measure, then we have the Rokhlin formula (section 4.3 and section 12.3 ): $h_{\mu }(T)=\int \ln |dT/dx|\mu (dx)$ This allows calculation of entropy of many interval maps, such as the logistic map.

Ergodic means that $T^{-1}(A)=A$ implies A has full measure or zero measure. Piecewise expanding and Markov means that there is a partition of X into finitely many open intervals, such that for some $\epsilon >0$ , $|T'|\geq 1+\epsilon$ on each open interval. Markov means that for each $I_{i}$ from those open intervals, either $T(I_{i})\cap I_{i}=\emptyset$ or $T(I_{i})\cap I_{i}=I_{i}$ .

## Classification and anti-classification theorems

One of the primary activities in the study of measure-preserving systems is their classification according to their properties. That is, let $(X,{\mathcal {B}},\mu )$ be a measure space, and let U be the set of all measure preserving systems $(X,{\mathcal {B}},\mu ,T)$ . An isomorphism $S\sim T$ of two transformations $S,T$ defines an equivalence relation ${\mathcal {R}}\subset U\times U.$ The goal is then to describe the relation ${\mathcal {R}}$ . A number of classification theorems have been obtained; but quite interestingly, a number of anti-classification theorems have been found as well. The anti-classification theorems state that there are more than a countable number of isomorphism classes, and that a countable amount of information is not sufficient to classify isomorphisms.

The first anti-classification theorem, due to Hjorth, states that if U is endowed with the weak topology, then the set ${\mathcal {R}}$ is not a Borel set. There are a variety of other anti-classification results. For example, replacing isomorphism with Kakutani equivalence, it can be shown that there are uncountably many non-Kakutani equivalent ergodic measure-preserving transformations of each entropy type.

These stand in contrast to the classification theorems. These include:

- Ergodic measure-preserving transformations with a pure point spectrum have been classified.
- Bernoulli shifts are classified by their metric entropy. See Ornstein theory for more.

**Krieger finite generator theorem** (Krieger 1970)—Given a dynamical system on a Lebesgue space of measure 1, where ${\textstyle T}$ is invertible, measure preserving, and ergodic.

If $h_{T}\leq \ln k$ for some integer k , then the system has a size- k generator.

If the entropy is exactly equal to $\ln k$ , then such a generator exists iff the system is isomorphic to the Bernoulli shift on k symbols with equal measures.

---
title: "Ergodicity"
source: https://en.wikipedia.org/wiki/Ergodicity
domain: markov-chain-monte-carlo-deep
license: CC-BY-SA-4.0
tags: Markov chain Monte Carlo, detailed balance, ergodicity, burn-in
fetched: 2026-07-02
---

# Ergodicity

In mathematics, especially in ergodic theory, **ergodicity** is a way of saying that a dynamical system behaves as one indivisible statistical system, rather than being composed of statistically distinguishable subsystems. More precisely, a measure-preserving dynamical system is ergodic if every invariant measurable set has either measure zero or full measure. Equivalently, the system cannot be decomposed, up to sets of measure zero, into two smaller invariant parts of positive measure.

Ergodic theorems relate this condition to the equality of time averages and space averages. Under suitable hypotheses, the time average of an observable along almost every orbit is equal to its space average. Ergodicity itself, however, is not the same as randomness, mixing, chaos, or the assertion that every individual orbit visits every part of the space.

Ergodicity may also be described in terms of ergodic measures: an invariant probability measure is ergodic if it cannot be decomposed into a nontrivial convex combination of other invariant probability measures.

Ergodic systems occur in many areas of physics, geometry, probability theory, and dynamical systems. The origins of the subject lie in statistical physics, where Ludwig Boltzmann formulated the ergodic hypothesis in connection with the foundations of statistical mechanics.

## Informal explanation and motivation

Ergodicity is a way of saying that a system has no hidden division into smaller statistically separate parts. If the system is observed for a long time, its long-run statistical behavior is governed by one invariant measure, rather than by a choice among several different invariant components.

### First example: coin tossing

A simple example comes from coin tossing. Suppose the same biased coin is tossed forever, with probability p of heads on each toss. The resulting stationary process is ergodic: apart from events of probability zero, there is no further permanent statistical label attached to the sequence. In particular, the long-run frequency of heads is p for almost every sequence.

By contrast, suppose that before any tosses are made, one of two coins is chosen at random: one coin has probability $p_{1}$ of heads, and the other has probability $p_{2}$ . The chosen coin is then tossed forever. This process is stationary, but it is not ergodic. The hidden choice of coin is an invariant fact about the whole infinite sequence, and it separates the process into two statistically different components.

In a measure-preserving dynamical system, this idea is expressed by saying that every invariant measurable set has either measure zero or full measure. Equivalently, the system cannot be decomposed, up to sets of measure zero, into two invariant parts of positive measure.

Ergodicity is related to the equality of time averages and space averages through ergodic theorems. It should not be confused with randomness, mixing, chaos, or the claim that every individual orbit visits every part of the space.

### Second example: irrational rotations of a circle

Another basic example comes from rotations of the circle. Let $R_{\alpha }$ be the rotation of the circle through the angle $2\pi \alpha$ radians. After n iterations, a point has been rotated by $2\pi n\alpha$ .

If $\alpha$ is rational, say $\alpha =p/q$ in lowest terms, then every point is periodic: after q iterations it returns to its original position. With respect to Lebesgue measure on the circle, this rotation is not ergodic. For example, the nonconstant function

$f(e^{i\theta })=\cos(q\theta )$

is invariant under the rotation, since replacing $\theta$ by $\theta +2\pi p/q$ does not change $\cos(q\theta )$ . The circle can thus be divided into smaller invariant pieces, such as $a<\cos(q\theta )<b$ .

If $\alpha$ is irrational, the orbit of every point is dense in the circle. In fact, the irrational rotation is ergodic with respect to Lebesgue measure: every measurable set that is invariant under the rotation has either measure zero or full measure. Thus the system has many different individual orbits, but it has no nontrivial measurable decomposition into invariant statistical components.

This example also shows that ergodicity is weaker than mixing. Irrational rotations are ergodic, but they are not mixing.

### Measurable sets and invariant events

In the measure-theoretic definition of ergodicity, the basic data are a measure space X , and a time-evolution of its points. In the coin-toss example, the state space may be taken to be the space of infinite sequences of outcomes, and the time evolution is the shift map on this space. In the rotation example, the state space is the circle, and the time evolution is repeated application of the rotation. Both are examples of discrete time dynamical systems. The elements of the space X are possible states of the system. A measurable set is a collection of states to which the theory assigns a measure, such as length, area, volume, or probability. The space X is equipped with a sigma-algebra ${\mathcal {B}}$ of sets that are allowed to be measured.

When X is a topological space, such as an interval, a circle, or a manifold, the usual choice is often the Borel sigma-algebra, generated by the open sets. In probability examples, measurable sets are events. For instance, in an infinite sequence of coin tosses, the event "the first toss is heads" is measurable, as is the event "the long-run frequency of heads exists and is equal to p ".

A set is invariant if membership in it is unchanged by the time evolution, up to sets of measure zero. For a transformation $T:X\to X$ , this is usually written as

$T^{-1}A=A$

or, more generally, denoting the symmetric difference of sets by $\Delta$ :

$\mu (T^{-1}A\triangle A)=0.$

A (discrete time) measure preserving system is thus the pair $(X,T)$ where X is a measure space and T is a measure-preserving transformation.

An invariant measurable set represents a statistical property of the state that persists under the dynamics. Ergodicity says that every such persistent measurable property is trivial: it holds either almost nowhere (i.e., only on a set of measure zero) or almost everywhere (i.e., everywhere except a set of measure zero).

### Physical motivation

The original motivation for ergodicity came from statistical mechanics. In classical mechanics, the state of a system is represented by a point in phase space: for example, the positions and momenta of all particles in a gas. The time evolution of the system moves this point through phase space.

For an isolated Hamiltonian system, the energy is conserved, so the motion is confined to an energy surface

$H(q,p)=E.$

Hamiltonian flow preserves the natural phase-space volume, called Liouville measure. After restricting to an energy surface, this gives the measure underlying the microcanonical ensemble.

The physical question was whether long-time averages along the actual motion of one system can be replaced by averages over the corresponding energy surface. For an observable f , this asks whether a time average such as

$\lim _{T\to \infty }{1 \over T}\int _{0}^{T}f(\phi _{t}(x))\,dt$

agrees, for typical initial states x , representing the state of the large number of particles in the gas, with the average of f over the energy surface. The ergodic hypothesis was an early attempt to justify this replacement.

In modern measure-theoretic language, ergodicity does not mean that a trajectory literally passes through every point of the energy surface. Rather, it means that, relative to the chosen invariant measure, there is no further invariant measurable decomposition of the system into smaller statistical components. Under suitable hypotheses, ergodic theorems then imply the equality of time averages and space averages for many observables.

## History and etymology

The term *ergodic* is usually attributed to Ludwig Boltzmann and is commonly explained as a combination of the Greek words ἔργον (*ergon*, "work") and ὁδός (*hodos*, "path"). The exact historical development of the term is not entirely straightforward; it has also been connected with Boltzmann's term *ergomonode*, used in his work on statistical mechanics.

The concept arose in the attempt to justify the use of statistical methods in statistical mechanics. In that setting, one wants to relate time averages along the motion of a mechanical system to averages over a space of possible states. This motivation led to the ergodic hypothesis, according to which a mechanical system may, under suitable assumptions, be treated as if its long-time behavior samples the relevant state space.

The original physical form of the hypothesis was later replaced by more precise mathematical notions in ergodic theory, especially the measure-theoretic definition in terms of invariant measurable sets. In 1913, Michel Plancherel showed that one natural formulation of the classical mechanical ergodic hypothesis could not hold as originally stated.

## Ergodicity in physics and geometry

Ergodicity appears in several related settings in physics and geometry. In each case, one must specify both the state space and the invariant measure. The common measure-theoretic question is whether the system has nontrivial invariant measurable subsets.

### In statistical mechanics

In statistical mechanics, ergodicity is used to justify replacing long-time averages of observables by averages over an invariant ensemble. For isolated Hamiltonian systems, the relevant ensemble is usually the microcanonical ensemble on an energy surface. This is the setting of the classical ergodic hypothesis.

Rigorous proofs of ergodicity for realistic many-particle systems are difficult. Important mathematical examples come from dynamical billiards, where idealized particle collisions provide systems for which ergodicity can sometimes be proved.

### Simple dynamical systems

Basic examples of ergodic and non-ergodic systems occur already in low-dimensional dynamics. Irrational rotations of the circle are ergodic with respect to Lebesgue measure, but they are not mixing. Other standard examples include the baker's map, Arnold's cat map, Bernoulli shifts, and certain billiard systems. These examples illustrate different relations between ergodicity, mixing, entropy, and chaotic behavior.

### In geometry

Ergodic flows also arise naturally in geometry. A central example is the geodesic flow on a Riemannian manifold, usually considered on the unit tangent bundle with its natural invariant measure.

On a flat torus, motion in a fixed irrational direction is dense on the torus and is ergodic after restricting to that direction. The full geodesic flow on the unit tangent bundle is not ergodic, since the direction of motion is conserved. By contrast, the geodesic flow on a compact Riemannian manifold of negative curvature is ergodic with respect to the natural invariant measure. This provides one of the classical families of examples in ergodic theory and is closely related to Anosov flows.

Other geometric examples include horocycle flows, flows on translation surfaces, and billiard flows. In these settings, ergodicity concerns invariant measurable subsets of the appropriate phase space, not whether a single path literally passes through every point.

### In quantum mechanics

In quantum mechanics, the word ergodicity is used more cautiously, since quantum evolution is not described by point trajectories in classical phase space. Related notions appear in quantum chaos and in the quantum ergodicity theorem, which concerns the distribution of eigenfunctions in a semiclassical limit. These ideas are related to, but not identical with, classical measure-theoretic ergodicity.

## Definition for discrete-time systems

Ergodic measures provide one of the cornerstones with which ergodicity is generally discussed. A formal definition follows.

### Invariant measure

Let $(X,{\mathcal {B}})$ be a measurable space. If T is a measurable function from X to itself and $\mu$ a probability measure on $(X,{\mathcal {B}})$ , then a measure-preserving dynamical system is defined as a dynamical system for which $\mu {\mathord {\left(T^{-1}(A)\right)}}=\mu (A)$ for all $A\in {\mathcal {B}}$ . Such a T is said to preserve ${\displaystyle \mu$ equivalently, that $\mu$ is T -invariant.

### Ergodic measure

A measurable function T is said to be **$\mu$ -ergodic** or that **$\mu$ is an ergodic measure for T** if T preserves $\mu$ and the following condition holds:

For any

$A\in {\mathcal {B}}$

such that

$T^{-1}(A)=A$

either

$\mu (A)=0$

or

$\mu (A)=1$

.

In other words, there are no T -invariant subsets up to measure 0 (with respect to $\mu$ ).

Some authors relax the requirement that T preserves $\mu$ to the requirement that T is a non-singular transformation with respect to $\mu$ , meaning that N is a subset of measure zero if and only if $T^{-1}(N)$ is.

### Examples

The simplest example is when X is a finite set and $\mu$ is the normalized counting measure. Then a self-map of X preserves $\mu$ if and only if it is a bijection, and it is ergodic if and only if T has only one orbit (that is, for every $x,y\in X$ there exists $k\in \mathbb {N}$ such that $y=T^{k}(x)$ ). For example, if $X=\{1,2,\ldots ,n\}$ then the cycle $(1\,2\,\cdots \,n)$ is ergodic, but the permutation $(1\,2)(3\,4\,\cdots \,n)$ is not (it has the two invariant subsets $\{1,2\}$ and $\{3,4,\ldots ,n\}$ ).

### Equivalent formulations

The definition given above admits the following immediate reformulations:

- for every $A\in {\mathcal {B}}$ with $\mu {\mathord {\left(T^{-1}(A)\bigtriangleup A\right)}}=0$ we have $\mu (A)=0$ or $\mu (A)=1\,$ (where $\bigtriangleup$ denotes the symmetric difference);
- for every $A\in {\mathcal {B}}$ with positive measure we have ${\textstyle \mu {\mathord {\left(\bigcup _{n=1}^{\infty }T^{-n}(A)\right)}}=1}$ ;
- for every two sets $A,B\in {\mathcal {B}}$ of positive measure, there exists $n>0$ such that $\mu {\mathord {\left(\left(T^{-n}(A)\right)\cap B\right)}}>0$ ;
- Every measurable function $f:X\to \mathbb {R}$ with $f\circ T=f$ is constant on a subset of full measure.

Importantly for applications, the condition in the last characterisation can be restricted to square-integrable functions only:

- If $f\in L^{2}(X,\mu )$ and $f\circ T=f$ then f is constant almost everywhere.

### Further examples

#### Bernoulli shifts and subshifts

Let S be a finite set and $X=S^{\mathbb {Z} }$ with $\mu$ the product measure (each factor S being endowed with its normalized counting measure). Then the shift operator T defined by $T\left((s_{k})_{k\in \mathbb {Z} })\right)=(s_{k+1})_{k\in \mathbb {Z} }$ is $\mu$ -ergodic.

There are many more ergodic measures for the shift map T on X . Periodic sequences give finitely supported measures. More interestingly, there are infinitely-supported ones which are subshifts of finite type.

#### Irrational rotations

Let X be the unit circle $\{z\in \mathbb {C} ,\,|z|=1\}$ , with its Lebesgue measure $\mu$ . For any $\theta \in \mathbb {R}$ the rotation of X of angle $\theta$ is given by $T_{\theta }(z)=e^{2i\pi \theta }z$ . If $\theta =p/q$ is rational, then $T_{\theta }$ is not ergodic for Lebesgue measure; for example, the nonconstant function $z\mapsto z^{q}$ is invariant under the rotation. On the other hand, if $\theta$ is irrational then $T_{\theta }$ is ergodic.

#### Arnold's cat map

Let $X=\mathbb {R} ^{2}/\mathbb {Z} ^{2}$ be the 2-torus. Then any element $g\in \mathrm {SL} _{2}(\mathbb {Z} )$ defines a self-map of X since $g\left(\mathbb {Z} ^{2}\right)=\mathbb {Z} ^{2}$ . When ${\textstyle g=\left({\begin{array}{cc}2&1\\1&1\end{array}}\right)}$ one obtains the so-called Arnold's cat map, which is ergodic for the Lebesgue measure on the torus.

### Ergodic theorems

If $\mu$ is a probability measure on a space X which is ergodic for a transformation T the pointwise ergodic theorem of G. D. Birkhoff states that for every integrable function $f:X\to \mathbb {R}$ and for $\mu$ -almost every point $x\in X$ the time average on the orbit of x converges to the space average of f . Formally this means that $\lim _{k\to +\infty }\left({\frac {1}{k+1}}\sum _{i=0}^{k}f\left(T^{i}(x)\right)\right)=\int _{X}fd\mu .$

The mean ergodic theorem of J. von Neumann is a similar, weaker statement about averaged translates of square-integrable functions.

#### Dense orbits

For a continuous transformation of a second-countable topological space with a Borel probability measure $\mu$ , ergodicity implies that $\mu$ -almost every orbit is dense in the support of $\mu$ .

This is not an equivalence since for a transformation which is not uniquely ergodic, but for which there is an ergodic measure with full support $\mu _{0}$ , for any other ergodic measure $\mu _{1}$ the measure ${\textstyle {\frac {1}{2}}(\mu _{0}+\mu _{1})}$ is not ergodic for T but its orbits are dense in the support. Explicit examples can be constructed with shift-invariant measures.

The topological counterpart to ergodicity is a minimal dynamical system, in which the orbit of every point is dense.

#### Mixing

A measure-preserving system is called mixing if sets become asymptotically independent under iteration. Mixing implies ergodicity under standard hypotheses. The converse is not true, for example a rotation with irrational angle on the circle (which is ergodic per the examples above) is not mixing (for a sufficiently small interval its successive images will not intersect itself most of the time). Bernoulli shifts are mixing, and so is Arnold's cat map.

More precisely, a transformation T of a probability measure space $(X,\mu )$ is said to be mixing for the measure $\mu$ if for any measurable sets $A,B\subset X$ the following holds: $\lim _{n\to +\infty }\mu \left(T^{-n}A\cap B\right)=\mu (A)\mu (B)$

It is immediate that a mixing transformation is also ergodic (taking A to be a T -stable subset and B its complement).

This notion of mixing is sometimes called strong mixing, as opposed to weak mixing which means that $\lim _{n\to +\infty }{\frac {1}{n}}\sum _{k=1}^{n}\left|\mu (T^{-k}A\cap B)-\mu (A)\mu (B)\right|=0$

#### Entropy

Kolmogorov–Sinai entropy is another invariant of measure-preserving systems. It measures the average information produced by the dynamics, rather than whether the system decomposes into invariant measurable components. Thus entropy and ergodicity answer different questions: an ergodic system may have zero entropy, while positive entropy alone does not imply ergodicity unless one restricts to an ergodic component.

#### Proper ergodicity

The transformation T is said to be *properly ergodic* if it does not have an orbit of full measure. In the discrete case this means that the measure $\mu$ is not supported on a finite orbit of T .

## Definition for continuous-time dynamical systems

The definition is essentially the same for continuous-time dynamical systems as for a single transformation. Let $(X,{\mathcal {B}})$ be a measurable space and for each $t\in \mathbb {R} _{+}$ , then such a system is given by a family $T_{t}$ of measurable functions from X to itself, so that for any $t,s\in \mathbb {R} _{+}$ the relation $T_{s+t}=T_{s}\circ T_{t}$ holds (usually it is also asked that the orbit map from $\mathbb {R} _{+}\times X\to X$ is also measurable). If $\mu$ is a probability measure on $(X,{\mathcal {B}})$ then we say that **$T_{t}$ is $\mu$ -ergodic** or **$\mu$ is an ergodic measure for T** if each $T_{t}$ preserves $\mu$ and the following condition holds:

For any

$A\in {\mathcal {B}}$

, if for all

$t\in \mathbb {R} _{+}$

we have

$T_{t}^{-1}(A)\subset A$

then either

$\mu (A)=0$

or

$\mu (A)=1$

.

### Examples

As in the discrete case the simplest example is that of a transitive action, for instance the action on the circle given by $T_{t}(z)=e^{2i\pi t}z$ is ergodic for Lebesgue measure.

An example with infinitely many orbits is given by the flow along an irrational slope on the torus: let $X=\mathbb {S} ^{1}\times \mathbb {S} ^{1}$ and $\alpha \in \mathbb {R}$ . Let $T_{t}(z_{1},z_{2})=\left(e^{2i\pi t}z_{1},e^{2\alpha i\pi t}z_{2}\right)$ ; then if $\alpha \not \in \mathbb {Q}$ this is ergodic for the Lebesgue measure.

### Ergodic flows

Further examples of ergodic flows are:

- Certain billiards in convex Euclidean domains, such as Sinai billiards;
- the geodesic flow of a negatively curved Riemannian manifold of finite volume is ergodic (for the normalised volume measure);
- the horocycle flow on a hyperbolic manifold of finite volume is ergodic (for the normalised volume measure)

## Ergodicity in compact metric spaces

If X is a compact metric space it is naturally endowed with the σ-algebra of Borel sets. The additional structure coming from the topology then allows a much more detailed theory for ergodic transformations and measures on X .

### Functional analysis interpretation

A very powerful alternate characterization of ergodic measures can be given using the theory of Banach spaces. The signed Radon measures on X form a Banach space, of which the set ${\mathcal {P}}(X)$ of probability measures on X is a convex subset. Given a continuous transformation T of X , the subset ${\mathcal {P}}(X)^{T}$ of T -invariant measures is a closed convex subset, and a measure is ergodic for T if and only if it is an extreme point of this convex set.

#### Existence of ergodic measures

In the setting above, the Krylov–Bogolyubov argument shows that ${\mathcal {P}}(X)^{T}$ is nonempty. It is also compact and convex in the weak-* topology; hence by the Krein–Milman theorem it has extreme points. Therefore a continuous transformation of a compact metric space always admits ergodic measures.

#### Ergodic decomposition

In general an invariant measure need not be ergodic. In the compact metric setting, Choquet theory applied to the compact convex set ${\mathcal {P}}(X)^{T}$ of invariant probability measures implies that an invariant measure can be expressed as the barycenter of a probability measure supported on the set of ergodic measures. This is referred to as the *ergodic decomposition* of the measure.

#### Example

In the case of $X=\{1,\ldots ,n\}$ and $T=(1\,2)(3\,4\,\cdots \,n)$ the normalized counting measure is not ergodic. The ergodic measures for T are the uniform measures $\mu _{1},\mu _{2}$ supported on the subsets $\{1,2\}$ and $\{3,\ldots ,n\}$ , and every T -invariant probability measure can be written in the form $t\mu _{1}+(1-t)\mu _{2}$ for some $t\in [0,1]$ . In particular ${\textstyle {\frac {2}{n}}\mu _{1}+{\frac {n-2}{n}}\mu _{2}}$ is the ergodic decomposition of the normalized counting measure.

#### Continuous systems

The same functional-analytic interpretation applies to continuous actions of $\mathbb {R}$ or $\mathbb {R} _{+}$ on compact metric spaces, with invariant measures taken with respect to the corresponding flow or semigroup.

### Unique ergodicity

The transformation T is said to be **uniquely ergodic** if there is a unique T -invariant Borel probability measure $\mu$ on X .

In the examples considered above, irrational rotations of the circle are uniquely ergodic; shift maps are not.

## Probabilistic interpretation: ergodic processes

If $\left(X_{n}\right)_{n\geq 1}$ is a discrete-time stochastic process with state space S , its joint distribution defines a probability measure on the path space $S^{\mathbb {N} }$ . The process is stationary if this probability measure is invariant under the shift map

$\left(x_{n}\right)_{n\geq 1}\mapsto \left(x_{n+1}\right)_{n\geq 1}.$

A stationary process is said to be ergodic if this shift-invariant probability measure is ergodic. Equivalently, every shift-invariant event has probability zero or one. This is a particular case of the notions discussed above.

The simplest case is that of an independent and identically distributed process, which corresponds to a product measure on the path space and is ergodic for the shift map. Another important case is that of a stationary Markov chain, which is discussed in detail below.

A similar interpretation holds for continuous-time stochastic processes, though the construction of the measurable structure of the action is more complicated.

## Ergodicity of Markov chains

### The dynamical system associated with a Markov chain

Let S be a finite set. A Markov chain on S is defined by a matrix $P\in [0,1]^{S\times S}$ , where $P(s_{1},s_{2})$ is the transition probability from $s_{1}$ to $s_{2}$ , so for every $s\in S$ we have ${\textstyle \sum _{s'\in S}P(s,s')=1}$ . A stationary measure for P is a probability measure $\nu$ on S such that $\nu P=\nu$ ; that is,

$\sum _{s'\in S}\nu (s')P(s',s)=\nu (s)$

for all $s\in S$ .

Using this data we can define a probability measure $\mu _{\nu }$ on the path space $X=S^{\mathbb {Z} }$ with its product σ-algebra by giving the measures of cylinder sets as follows:

$\mu _{\nu }\{x\in S^{\mathbb {Z} }:x_{n}=s_{n},\ldots ,x_{m}=s_{m}\}=\nu (s_{n})P(s_{n},s_{n+1})\cdots P(s_{m-1},s_{m}).$

Stationarity of $\nu$ then means that the measure $\mu _{\nu }$ is invariant under the shift map

$T\left(\left(s_{k}\right)_{k\in \mathbb {Z} }\right)=\left(s_{k+1}\right)_{k\in \mathbb {Z} }.$

### Criterion for ergodicity

The measure $\mu _{\nu }$ is ergodic for the shift map if the associated finite Markov chain is irreducible, that is, if any state can be reached with positive probability from any other state in a finite number of steps.

For a finite irreducible Markov chain, there is a unique stationary measure. A stronger sufficient condition, often used to ensure convergence to the stationary measure, is that 1 be a simple eigenvalue of the matrix P and that all other eigenvalues of P in $\mathbb {C}$ have modulus less than 1 .

Note that in probability theory a finite Markov chain is often called ergodic if it is irreducible and aperiodic. Aperiodicity is not necessary for the associated shift-invariant measure $\mu _{\nu }$ to be ergodic; it is instead related to stronger convergence and mixing properties. Hence the notion of "ergodicity" for a Markov chain and the notion of ergodicity for the associated shift-invariant measure are closely related but not identical.

### Examples

#### Uniform transition matrix

If $P(s,s')=1/|S|$ for all $s,s'\in S$ , then the stationary measure on S is the uniform probability measure. The corresponding measure $\mu _{\nu }$ on $S^{\mathbb {Z} }$ is the product of uniform probability measures. This gives the Bernoulli shift example from above.

#### Non-ergodic Markov chains

Markov chains with more than one recurrent communicating class are not irreducible, and the associated stationary shift measures need not be ergodic. If $S_{1},S_{2}\subsetneq S$ are two distinct recurrent communicating classes, there are stationary measures $\nu _{1},\nu _{2}$ supported on $S_{1},S_{2}$ respectively. The corresponding shift-invariant measures on $S^{\mathbb {Z} }$ are ergodic on their separate components, but a nontrivial convex combination of them is not ergodic.

A very simple example is the chain on $S=\{1,2\}$ given by the matrix

$\left({\begin{array}{cc}1&0\\0&1\end{array}}\right),$

in which both states are absorbing.

#### A periodic chain

The Markov chain on $S=\{1,2\}$ given by the matrix

$\left({\begin{array}{cc}0&1\\1&0\end{array}}\right)$

is irreducible but periodic. Thus it is not ergodic in the aperiodic Markov-chain sense, although the associated measure $\mu$ on $\{1,2\}^{\mathbb {Z} }$ is ergodic for the shift map. However, the shift is not mixing for this measure. For the sets

$A=\{x\in \{1,2\}^{\mathbb {Z} }:x_{0}=1\}$

and

$B=\{x\in \{1,2\}^{\mathbb {Z} }:x_{0}=2\}$

we have ${\textstyle \mu (A)={\frac {1}{2}}=\mu (B)}$ , but

$\mu \left(T^{-n}A\cap B\right)={\begin{cases}{\frac {1}{2}}&{\text{if }}n{\text{ is odd}},\\0&{\text{if }}n{\text{ is even}}.\end{cases}}$

## Generalisations

The definition of ergodicity extends from a single transformation to group actions. Let G be a group acting measurably on a measure space $(X,{\mathcal {B}},\mu )$ . If the action preserves $\mu$ , meaning that

$\mu (g^{-1}A)=\mu (A)$

for every $g\in G$ and every $A\in {\mathcal {B}}$ , then the action is said to be ergodic if every measurable set A satisfying

$g^{-1}A=A$

for all $g\in G$ has either $\mu (A)=0$ or $\mu (X\setminus A)=0$ . Equivalently, every invariant measurable set is either null or conull.

The classical cases of a single invertible transformation and a continuous-time flow correspond to actions of $\mathbb {Z}$ and $\mathbb {R}$ , respectively. The same definition also applies to non-abelian groups.

There is also a nonsingular version. If the action does not preserve $\mu$ but preserves its measure class, so that null sets are carried to null sets, then $\mu$ is called quasi-invariant. In that setting, the action is called ergodic if every measurable set that is invariant modulo null sets is either null or conull.

Important examples include actions of semisimple Lie groups and their lattices, such as boundary actions on Furstenberg boundaries.

The same terminology is also used for measurable equivalence relations. A measurable equivalence relation is said to be ergodic if every saturated measurable subset is either null or conull.

### Representation-theoretic formulation

Ergodicity also has a representation-theoretic formulation. Let G be a group and let $\pi :G\to U({\mathcal {H}})$ be a unitary representation on a Hilbert space ${\mathcal {H}}$ . In this context, the representation is sometimes called ergodic if it has no nonzero invariant vectors, that is,

${\mathcal {H}}^{G}={v\in {\mathcal {H}}:\pi (g)v=v{\text{ for all }}g\in G}={0}.$

This condition can also be expressed in terms of matrix coefficients. For $x,y\in {\mathcal {H}}$ , define

$f_{x,y}(g)=\langle \pi (g)x,y\rangle .$

Matrix coefficients of unitary representations are weakly almost periodic. Since $WAP(G)$ has a unique invariant mean m , the representation is ergodic if and only if

$m(f_{x,y})=0$

for all $x,y\in {\mathcal {H}}$ . When G is compact, this invariant mean is integration with respect to normalized Haar measure, so the condition becomes

$\int _{G}\langle \pi (g)x,y\rangle \,dg=0$

for all $x,y\in {\mathcal {H}}$ .

This terminology is compatible with the usual notion of ergodicity for measure-preserving actions. Suppose that G acts on a probability space $(X,{\mathcal {B}},\mu )$ by measure-preserving transformations. The associated Koopman representation is the unitary representation of G on $L^{2}(X,\mu )$ defined by

$(U_{g}f)(x)=f(g^{-1}x).$

The action of G is ergodic if and only if the only G -invariant functions in $L^{2}(X,\mu )$ are the constant functions. Equivalently,

$L^{2}(X,\mu )^{G}=\mathbb {C} \mathbf {1} .$

Let $L_{0}^{2}(X,\mu )$ denote the orthogonal complement of the constant functions,

$L_{0}^{2}(X,\mu )=\left\{f\in L^{2}(X,\mu ):\int _{X}f\,d\mu =0\right\}.$

Then the action is ergodic if and only if the restricted Koopman representation on $L_{0}^{2}(X,\mu )$ is ergodic in the representation-theoretic sense, meaning that it has no nonzero invariant vector.

For a single invertible transformation T , this is the same statement for the unitary operator $U_{T}f=f\circ T^{-1}$ . In this language, ergodicity means that the eigenspace for the eigenvalue 1 consists only of the constant functions.

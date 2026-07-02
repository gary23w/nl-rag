---
title: "Compact space"
source: https://en.wikipedia.org/wiki/Compact_space
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Compact space

In mathematics, especially general topology and mathematical analysis, **compactness** is a property of a space that makes it behave in many ways like a finite set. For instance, on a finite set every infinite sequence must take some value infinitely often, by the pigeonhole principle. For subsets of Euclidean space, the analogous statement is sequential compactness: a set is compact if and only if every infinite sequence in the set has a subsequence that converges to a point of the set. Likewise, whereas every real-valued function on a finite set is bounded and attains its maximum and minimum, every continuous real-valued function on a compact space has these properties. For compact subsets of Euclidean space, this is the extreme value theorem.

Another basic property of finite sets is that every cover of a finite set by subsets has a finite subcover: one may choose, for each point of the finite set, a member of the cover containing it. The corresponding topological property is used to define compactness: a topological space is compact if every open cover has a finite subcover. In metric spaces this is equivalent to several other formulations, including sequential compactness, though these equivalences can fail in more general topological spaces. Thus every sequence in the closed unit interval [0,1] has a convergent subsequence with limit in [0,1], whereas this fails for spaces such as the open interval (0,1) and the real line. For subsets of Euclidean space, compactness is equivalent to being closed and bounded, by the Heine–Borel theorem. The property of compactness often allows local information to be combined into global conclusions. The term **compact set** may refer either to a compact topological space or, more commonly, to a subset of a topological space that is compact in the subspace topology.

Compactness was formally introduced by Maurice Fréchet in 1906 in work generalizing the Bolzano–Weierstrass theorem from sets of points to spaces of functions. Later, Pavel Alexandrov and Pavel Urysohn developed the open-cover formulation that is now standard in topology. Compactness plays a central role throughout mathematics; for example, continuous real-valued functions on compact spaces attain maxima and minima, and major results such as the Arzelà–Ascoli theorem and the Peano existence theorem depend on compactness.

## Historical development

In the 19th century, several disparate mathematical properties were understood that would later be seen as consequences of compactness. On the one hand, Bernard Bolzano (1817) had been aware that any bounded sequence of points (in the line or plane, for instance) has a subsequence that must eventually get arbitrarily close to some other point, called a limit point. Bolzano's proof relied on the method of bisection: the sequence was placed into an interval that was then divided into two equal parts, and a part containing infinitely many terms of the sequence was selected. The process could then be repeated by dividing the resulting smaller interval into smaller and smaller parts—until it closes down on the desired limit point. The full significance of Bolzano's theorem, and its method of proof, would not emerge until almost 50 years later when it was rediscovered by Karl Weierstrass.

In the 1880s, it became clear that results similar to the Bolzano–Weierstrass theorem could be formulated for spaces of functions rather than just numbers or geometrical points. The idea of regarding functions as themselves points of a generalized space dates back to the investigations of Giulio Ascoli and Cesare Arzelà. The culmination of their investigations, the Arzelà–Ascoli theorem, was a generalization of the Bolzano–Weierstrass theorem to families of continuous functions, the precise conclusion of which was that it was possible to extract a uniformly convergent sequence of functions from a suitable family of functions. The uniform limit of this sequence then played precisely the same role as Bolzano's "limit point". Towards the beginning of the twentieth century, results similar to that of Arzelà and Ascoli began to accumulate in the area of integral equations, as investigated by David Hilbert and Erhard Schmidt. For a certain class of Green's functions coming from solutions of integral equations, Schmidt had shown that a property analogous to the Arzelà–Ascoli theorem held in the sense of mean convergence – or convergence in what would later be dubbed a Hilbert space. This ultimately led to the notion of a compact operator as an offshoot of the general notion of a compact space. It was Maurice Fréchet who, in 1906, had distilled the essence of the Bolzano–Weierstrass property and coined the term *compactness* to refer to this general phenomenon (he used the term already in his 1904 paper which led to the famous 1906 thesis).

However, a different notion of compactness altogether had also slowly emerged at the end of the 19th century from the study of the continuum, which was seen as fundamental for the rigorous formulation of analysis. In 1870, Eduard Heine showed that a continuous function defined on a closed and bounded interval was in fact uniformly continuous. In the course of the proof, he made use of a lemma that from any countable cover of the interval by smaller open intervals, it was possible to select a finite number of these that also covered it. The significance of this lemma was recognized by Émile Borel (1895), and it was generalized to arbitrary collections of intervals by Pierre Cousin (1895) and Henri Lebesgue (1904). The Heine–Borel theorem, as the result is now known, is another special property possessed by closed and bounded sets of real numbers.

This property was significant because it allowed for the passage from local information about a set (such as the continuity of a function) to global information about the set (such as the uniform continuity of a function). This sentiment was expressed by Lebesgue (1904), who also exploited it in the development of the integral now bearing his name. Ultimately, the Russian school of point-set topology, under the direction of Pavel Alexandrov and Pavel Urysohn, formulated Heine–Borel compactness in a way that could be applied to the modern notion of a topological space. Alexandrov & Urysohn (1929) showed that the earlier version of compactness due to Fréchet, now called (relative) sequential compactness, under appropriate conditions followed from the version of compactness that was formulated in terms of the existence of finite subcovers. It was this notion of compactness that became the dominant one, because it was not only a stronger property, but it could be formulated in a more general setting with a minimum of additional technical machinery, as it relied only on the structure of the open sets in a space.

## Basic examples

Any finite space is compact; a finite subcover can be obtained by selecting, for each point, an open set containing it. A nontrivial example of a compact space is the (closed) unit interval [0,1] of real numbers. If one chooses an infinite number of distinct points in the unit interval, then there must be some accumulation point among these points in that interval. For instance, the odd-numbered terms of the sequence 1, ⁠1/2⁠, ⁠1/3⁠, ⁠3/4⁠, ⁠1/5⁠, ⁠5/6⁠, ⁠1/7⁠, ⁠7/8⁠, ... get arbitrarily close to 0, while the even-numbered ones get arbitrarily close to 1. The given example sequence shows the importance of including the boundary points of the interval, since the limit points must be in the space itself—an open (or half-open) interval of the real numbers is not compact. It is also crucial that the interval be bounded, since in the interval [0,∞), one could choose the sequence of points 0, 1, 2, 3, ..., of which no sub-sequence ultimately gets arbitrarily close to any given real number.

In two dimensions, closed disks are compact since for any infinite number of points sampled from a disk, some subset of those points must get arbitrarily close either to a point within the disc, or to a point on the boundary. Likewise, a circle in the plane is compact (easily seen by its being closed and bounded). However, an open disk is not compact, because a sequence of points can tend to the boundary—without getting arbitrarily close to any point in the interior. Likewise, spheres are compact, but a sphere missing a point is not since a sequence of points can still tend to the missing point, thereby not getting arbitrarily close to any point *within* the space. Lines and planes are not compact, since one can take a set of equally-spaced points in any given direction without approaching any point.

## Definitions

Various definitions of compactness may apply, depending on the level of generality. A subset of Euclidean space in particular is compact if and only if it is closed and bounded. This implies, by the Bolzano–Weierstrass theorem, that any infinite sequence from the set has a subsequence that converges to a point in the set. Various equivalent notions of compactness, such as sequential compactness and limit point compactness, can be developed in general metric spaces.

In contrast, the different notions of compactness are not equivalent in general topological spaces, and the most useful notion of compactness—originally called *bicompactness*—is defined using covers consisting of open sets (see *Open cover definition* below). That this form of compactness holds for closed and bounded subsets of Euclidean space is known as the Heine–Borel theorem. Compactness, when defined in this manner, often allows one to take information that is known locally—in a neighbourhood of each point of the space—and to extend it to information that holds globally throughout the space. An example of this phenomenon is Dirichlet's theorem, to which it was originally applied by Heine, that a continuous function on a compact interval is uniformly continuous; here, continuity is a local property of the function, and uniform continuity the corresponding global property.

### Open cover definition

Formally, a topological space X is called *compact* if every open cover of X has a finite subcover. That is, X is compact if for every collection C of open subsets of X such that

$X=\bigcup _{S\in C}S\ ,$

there is a **finite** subcollection F ⊆ C such that

$X=\bigcup _{S\in F}S\ .$

Some branches of mathematics such as algebraic geometry, typically influenced by the French school of Bourbaki, use the term *quasi-compact* for the general notion, and reserve the term *compact* for topological spaces that are both Hausdorff and *quasi-compact*. A compact set is sometimes referred to as a *compactum*, plural *compacta*.

### Compactness of subsets

A subset K of a topological space X is compact if for every arbitrary collection C of open subsets of X such that

$K\subseteq \bigcup _{S\in C}S\ ,$

there is a finite subcollection F ⊆ C such that

$K\subseteq \bigcup _{S\in F}S\ .$

Equivalently, K is compact as a subset of X if and only if the topological space K is compact in the subspace topology. In particular, if $K\subset Y\subset X$ , with subset Y equipped with the subspace topology, then K is compact in Y if and only if K is compact in X. Furthermore, the compactness of K as a subset of a topological space X is independent of the embedding, provided that the subspace topology on K is the same.

### Characterization

If X is a topological space then the following are equivalent:

1. X is compact; i.e., every open cover of X has a finite subcover.
2. X has a sub-base such that every cover of the space, by members of the sub-base, has a finite subcover (Alexander's sub-base theorem).
3. X is Lindelöf and countably compact.
4. Any collection of closed subsets of X with the finite intersection property has nonempty intersection.
5. Every net on X has a convergent subnet (see the article on nets for a proof).
6. Every filter on X has a convergent refinement.
7. Every net on X has a cluster point.
8. Every filter on X has a cluster point.
9. Every ultrafilter on X converges to at least one point.
10. Every infinite subset of X has a complete accumulation point.
11. For every topological space Y, the projection $X\times Y\to Y$ is a closed mapping (see proper map).
12. Every open cover linearly ordered by subset inclusion contains X.

Bourbaki defines a compact space (quasi-compact space) as a topological space where each filter has a cluster point (i.e., 8. in the above).

#### Euclidean space

For any subset A of Euclidean space, A is compact if and only if it is closed and bounded; this is the Heine–Borel theorem.

As a Euclidean space is a metric space, the conditions in the next subsection also apply to all of its subsets. Of all of the equivalent conditions, it is in practice easiest to verify that a subset is closed and bounded, for example, for a closed interval or closed n-ball.

#### Metric spaces

For any metric space (*X*, *d*), the following are equivalent (assuming countable choice):

1. (*X*, *d*) is compact.
2. (*X*, *d*) is complete and totally bounded (this is also equivalent to compactness for uniform spaces).
3. (*X*, *d*) is sequentially compact; that is, every sequence in X has a convergent subsequence whose limit is in X (this is also equivalent to compactness for first-countable uniform spaces).
4. (*X*, *d*) is limit point compact (also called weakly countably compact); that is, every infinite subset of X has at least one limit point in X.
5. (*X*, *d*) is countably compact; that is, every countable open cover of X has a finite subcover.
6. X is empty or (*X*, *d*) is the image of a continuous function from the Cantor set.
7. Every decreasing nested sequence of nonempty closed subsets *S*1 ⊇ *S*2 ⊇ ... in (*X*, *d*) has a nonempty intersection.
8. Every increasing nested sequence of proper open subsets *S*1 ⊆ *S*2 ⊆ ... in (*X*, *d*) fails to cover X.

A compact metric space (*X*, *d*) also satisfies the following properties:

1. Lebesgue's number lemma: For every open cover of X, there exists a number *δ* > 0 such that every subset of X of diameter < δ is contained in some member of the cover.
2. (*X*, *d*) is second-countable, separable and Lindelöf – these three conditions are equivalent for metric spaces. The converse is not true; e.g., a countable discrete space satisfies these three conditions, but is not compact.
3. X is closed and bounded (as a subset of any metric space whose restricted metric is d). The converse may fail for a non-Euclidean space; e.g. the real line equipped with the discrete metric is closed and bounded but not compact, as the collection of all singletons of the space is an open cover which admits no finite subcover. It is complete but not totally bounded.

#### Ordered spaces

For an ordered space (*X*, <) (i.e. a totally ordered set equipped with the order topology), the following are equivalent:

1. (*X*, <) is compact.
2. Every subset of X has a supremum (i.e. a least upper bound) in X.
3. Every subset of X has an infimum (i.e. a greatest lower bound) in X.
4. Every nonempty closed subset of X has a maximum and a minimum element.

An ordered space satisfying (any one of) these conditions is called a complete lattice.

In addition, the following are equivalent for all ordered spaces (*X*, <), and (assuming countable choice) are true whenever (*X*, <) is compact (the converse in general fails if (*X*, <) is not also metrizable):

1. Every sequence in (*X*, <) has a subsequence that converges in (*X*, <).
2. Every monotone increasing sequence in X converges to a unique limit in X.
3. Every monotone decreasing sequence in X converges to a unique limit in X.
4. Every decreasing nested sequence of nonempty closed subsets S1 ⊇ S2 ⊇ ... in (*X*, <) has a nonempty intersection.
5. Every increasing nested sequence of proper open subsets S1 ⊆ S2 ⊆ ... in (*X*, <) fails to cover X.

#### Characterization by continuous functions

Let X be a completely regular Hausdorff space and C(*X*) the ring of real-valued continuous functions on X. For each *p* ∈ *X*, the evaluation map $\operatorname {ev} _{p}\colon C(X)\to \mathbb {R}$ given by $\operatorname {ev} _{p}(f)=f(p)$ is a ring homomorphism. Its kernel $M_{p}=\ker(\operatorname {ev} _{p})$ is a maximal ideal, since by the first isomorphism theorem $C(X)/M_{p}\cong \mathbb {R} .$

For a completely regular Hausdorff space X, X is pseudocompact if and only if every maximal ideal M of C(*X*) is *real*, meaning that its residue field C(*X*)/*M* is isomorphic to $\mathbb {R} .$ Moreover, X is realcompact if and only if every real maximal ideal is of the form *M**p* for some *p* ∈ *X*. Consequently, X is compact if and only if every maximal ideal of C(*X*) is the kernel of an evaluation homomorphism.

If X is not pseudocompact, then C(*X*) has maximal ideals whose residue fields are proper ordered field extensions of $\mathbb {R}$ , often called *hyperreal* fields. In the framework of non-standard analysis, this corresponds to the following characterization of compactness: a topological space X is compact if and only if every point of the natural extension **X* is infinitely close to some point of X (that is, lies in the monad of a point of X).

#### Hyperreal definition

A space X is compact if its hyperreal extension **X* (constructed, for example, by the ultrapower construction) has the property that every point of **X* is infinitely close to some point of *X* ⊂ **X*. For example, an open real interval *X* = (0, 1) is not compact because its hyperreal extension *(0,1) contains infinitesimals, which are infinitely close to 0, which is not a point of X.

## Sufficient conditions

- A closed subset of a compact space is compact.
- The union of finitely many compact sets is compact.
- The image of a compact space under a continuous function is compact.
- The intersection of any non-empty collection of compact subsets of a Hausdorff space is compact (and closed).
  - If X is not Hausdorff, then the intersection of two compact subsets may fail to be compact.
- The product of any collection of compact spaces is compact. (This is Tychonoff's theorem, which is equivalent to the axiom of choice.)
- In a metrizable space, a subset is compact if and only if it is sequentially compact (assuming countable choice).
- A finite set endowed with any topology is compact.

## Properties of compact spaces

- A space in which every compact subset is closed is called a KC space.
  - A compact subset of a Hausdorff space X is closed.
  - If X is not Hausdorff, then a compact subset of X may fail to be a closed subset of X.
  - If X is not Hausdorff, then the closure of a compact set may fail to be compact.
  - If X is not Hausdorff, then it can still be the case that every compact subset is closed.
- In any topological vector space (TVS), a compact subset is complete. However, every non-Hausdorff TVS contains compact (and thus complete) subsets that are *not* closed.
- If A and B are disjoint compact subsets of a Hausdorff space X, then there exist disjoint open sets U and V in X such that *A* ⊆ *U* and *B* ⊆ *V*.
- A continuous bijection from a compact space into a Hausdorff space is a homeomorphism.
- A compact Hausdorff space is normal and regular.
- If a space X is compact and Hausdorff, then no finer topology on X is compact, and no coarser topology on X is Hausdorff.
- If a subset of a metric space (*X*, *d*) is compact, then it is d-bounded.

### Functions and compact spaces

Since the image of a compact space under a continuous function is compact, the extreme value theorem holds for such spaces: a continuous real-valued function on a nonempty compact space is bounded above and attains its supremum. (Slightly more generally, this is true for an upper semicontinuous function.) As a sort of converse to the above statements, the pre-image of a compact space under a proper map is compact.

### Compactifications

Every topological space X is an open dense subspace of a compact space having at most one point more than X, by the Alexandroff one-point compactification. By the same construction, every locally compact Hausdorff space X is an open dense subspace of a compact Hausdorff space having at most one point more than X.

### Ordered compact spaces

A nonempty compact subset of the real numbers has a greatest element and a least element.

Let X be a totally ordered set endowed with the order topology. Then X is compact if and only if X is a complete lattice (i.e., all subsets have suprema and infima).

## Examples

- Any finite topological space, including the empty set, is compact. More generally, any space with a finite topology (only finitely many open sets) is compact; this includes in particular the trivial topology.
- Any space carrying the cofinite topology is compact.
- Any locally compact Hausdorff space can be turned into a compact space by adding a single point to it, by means of Alexandroff one-point compactification. The one-point compactification of $\mathbb {R}$ is homeomorphic to the circle **S**1; the one-point compactification of $\mathbb {R} ^{2}$ is homeomorphic to the sphere **S**2. Using the one-point compactification, one can also easily construct compact spaces which are not Hausdorff, by starting with a non-Hausdorff space.
- The right order topology or left order topology on any bounded totally ordered set is compact. In particular, Sierpiński space is compact.
- No discrete space with an infinite number of points is compact. The collection of all singletons of the space is an open cover which admits no finite subcover. Finite discrete spaces are compact.
- In $\mathbb {R}$ carrying the lower limit topology, no uncountable set is compact.
- In the cocountable topology on an uncountable set, no infinite set is compact. Like the previous example, the space as a whole is not locally compact but is still Lindelöf.
- The closed unit interval [0, 1] is compact. This follows from the Heine–Borel theorem. The open interval (0, 1) is not compact: the open cover ${\textstyle \left({\frac {1}{n}},1-{\frac {1}{n}}\right)}$ for n = 3, 4, ...  does not have a finite subcover. Similarly, the set of *rational numbers* in the closed interval [0,1] is not compact: the sets of rational numbers in the intervals ${\textstyle \left[0,{\frac {1}{\pi }}-{\frac {1}{n}}\right]{\text{ and }}\left[{\frac {1}{\pi }}+{\frac {1}{n}},1\right]}$ cover all the rationals in [0, 1] for n = 4, 5, ...  but this cover does not have a finite subcover. Here, the sets are open in the subspace topology even though they are not open as subsets of  $\mathbb {R}$ .
- The set $\mathbb {R}$ of all real numbers is not compact as there is a cover of open intervals that does not have a finite subcover. For example, intervals (n − 1, n + 1) , where n takes all integer values in **Z**, cover $\mathbb {R}$ but there is no finite subcover.
- On the other hand, the extended real number line carrying the analogous topology *is* compact; note that the cover described above would never reach the points at infinity and thus would *not* cover the extended real line. In fact, the set has the homeomorphism to [−1, 1] of mapping each infinity to its corresponding unit and every real number to its sign multiplied by the unique number in the positive part of interval that results in its absolute value when divided by one minus itself, and since homeomorphisms preserve covers, the Heine-Borel property can be inferred.
- For every natural number n, the n-sphere is compact. Again from the Heine–Borel theorem, the closed unit ball of any finite-dimensional normed vector space is compact. This is not true for infinite dimensions; in fact, a normed vector space is finite-dimensional if and only if its closed unit ball is compact.
- On the other hand, the closed unit ball of the dual of a normed space is compact for the weak-* topology. (Alaoglu's theorem)
- The Cantor set is compact. In fact, every non-empty compact metric space is a continuous image of the Cantor set.
- Consider the set K of all functions *f* : **R** → [0, 1] from the real number line to the closed unit interval, and define a topology on K so that a sequence $\{f_{n}\}$ in K converges towards *f* ∈ *K* if and only if $\{f_{n}(x)\}$ converges towards *f*(*x*) for all real numbers x. The coarsest such topology, sometimes called the topology of pointwise convergence, is the product topology. With this topology, K is a compact topological space; this follows from the Tychonoff theorem.
- A subset of the Banach space of real-valued continuous functions on a compact Hausdorff space is relatively compact if and only if it is equicontinuous and pointwise bounded (Arzelà–Ascoli theorem).
- Consider the set K of all functions *f* : [0, 1] → [0, 1] satisfying the Lipschitz condition |*f*(*x*) − *f*(*y*)| ≤ |*x* − *y*| for all *x*, *y* ∈ [0,1]. Consider on K the metric induced by the uniform distance $d(f,g)=\sup _{x\in [0,1]}|f(x)-g(x)|.$ Then by the Arzelà–Ascoli theorem the space K is compact.
- The spectrum of any bounded linear operator on a Banach space is a nonempty compact subset of the complex numbers $\mathbb {C}$ . Conversely, any compact subset of $\mathbb {C}$ arises in this manner, as the spectrum of some bounded linear operator. For instance, a diagonal operator on the Hilbert space $\ell ^{2}$ may have any compact nonempty subset of $\mathbb {C}$ as spectrum.
- The space of Borel probability measures on a compact Hausdorff space is compact for the vague topology, by the Alaoglu theorem.
- A collection of probability measures on the Borel sets of Euclidean space is called *tight* if, for any positive epsilon, there exists a compact subset containing all but at most epsilon of the mass of each of the measures. Prokhorov's theorem then asserts that a collection of probability measures is relatively compact for the vague topology if and only if it is tight.

### Algebraic examples

- Every semisimple Lie group has a compact real form, which is a compact topological group; an example is the orthogonal group of a positive-definite quadratic form. They also have non-compact real forms, such as the special linear group or the Lorentz group.
- Since the p-adic integers are homeomorphic to the Cantor set, they form a compact set.
- Any global field *K* is a discrete additive subgroup of its adele ring, and the quotient space is compact. This was used in John Tate's thesis to allow harmonic analysis to be used in number theory.
- The spectrum of any commutative ring with the Zariski topology (that is, the set of all prime ideals) is compact, but never Hausdorff (except in trivial cases). In algebraic geometry, such topological spaces are examples of quasi-compact schemes, "quasi" referring to the non-Hausdorff nature of the topology.
- The spectrum of a Boolean algebra is compact, a fact which is part of the Stone representation theorem. Stone spaces, compact totally disconnected Hausdorff spaces, form the abstract framework in which these spectra are studied. Such spaces are also useful in the study of profinite groups.
- The structure space of a commutative unital Banach algebra is a compact Hausdorff space.
- The Hilbert cube is compact, again a consequence of Tychonoff's theorem.
- A profinite group (e.g. Galois group) is compact.

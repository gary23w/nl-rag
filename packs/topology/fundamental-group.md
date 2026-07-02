---
title: "Fundamental group"
source: https://en.wikipedia.org/wiki/Fundamental_group
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Fundamental group

In the mathematical field of algebraic topology, the **fundamental group** of a topological space is the group of the equivalence classes under homotopy of the loops contained in the space. It records information about the basic shape, or holes, of the topological space. The fundamental group is the first and simplest homotopy group. The fundamental group is a homotopy invariant—topological spaces that are homotopy equivalent (or the stronger case of homeomorphic) have isomorphic fundamental groups. The fundamental group of a topological space X is denoted by $\pi _{1}(X)$ .

## Intuition

Start with a space (for example, a surface), and some point in it, and all the loops both starting and ending at this point—paths that start at this point, wander around and eventually return to the starting point. Two loops can be combined in an obvious way: travel along the first loop, then along the second. Two loops are considered equivalent if one can be deformed into the other without breaking. The set of all such loops with this method of combining and this equivalence between them is the fundamental group for that particular space.

## History

Henri Poincaré defined the fundamental group in 1895 in his paper "Analysis situs". The concept emerged in the theory of Riemann surfaces, in the work of Bernhard Riemann, Poincaré, and Felix Klein. It describes the monodromy properties of complex-valued functions, as well as providing a complete topological classification of closed surfaces.

## Definition

Throughout this article, X is a topological space. A typical example is a surface such as the one depicted at the right. Moreover, $x_{0}$ is a point in X called the *base-point*. (As is explained below, its role is rather auxiliary.) The idea of the definition of the homotopy group is to measure how many (broadly speaking) curves on X can be deformed into each other. The precise definition depends on the notion of the homotopy of loops, which is explained first.

### Homotopy of loops

Given a topological space X , a *loop based at $x_{0}$* is defined to be a continuous function (also known as a continuous map)

$\gamma \colon [0,1]\to X$

such that the starting point $\gamma (0)$ and the end point $\gamma (1)$ are both equal to $x_{0}$ .

A *homotopy* is a continuous interpolation between two loops. More precisely, a homotopy between two loops $\gamma ,\gamma '\colon [0,1]\to X$ (based at the same point $x_{0}$ ) is a continuous map $h\colon [0,1]\times [0,1]\to X,$ such that

- $h(0,t)=x_{0}$ for all $t\in [0,1]$ , that is, the starting point of the homotopy is $x_{0}$ for all t (which is often thought of as a time parameter).
- $h(1,t)=x_{0}$ for all $t\in [0,1]$ , that is, similarly the end point stays at $x_{0}$ for all t .
- $h(r,0)=\gamma (r)$ , $h(r,1)=\gamma '(r)$ for all $r\in [0,1]$ .

If such a homotopy h exists, $\gamma$ and $\gamma '$ are said to be *homotopic*. The relation " $\gamma$ is homotopic to $\gamma '$ " is an equivalence relation so that the set of equivalence classes can be considered: $\pi _{1}(X,x_{0}):=\{{\text{all loops }}\gamma {\text{ based at }}x_{0}\}/{\text{homotopy}}.$ This set (with the group structure described below) is called the *fundamental group* of the topological space X at the base point $x_{0}$ . The purpose of considering the equivalence classes of loops up to homotopy, as opposed to the set of all loops (the so-called loop space of X ) is that the latter, while being useful for various purposes, is a rather big and unwieldy object. By contrast the above quotient is, in many cases, more manageable and computable.

### Group structure

By the above definition, $\pi _{1}(X,x_{0})$ is just a set. It becomes a group (and therefore deserves the name fundamental *group*) using the concatenation of loops. More precisely, given two loops $\gamma _{0},\gamma _{1}$ , their product is defined as the loop

$\gamma _{0}\cdot \gamma _{1}\colon [0,1]\to X$

$(\gamma _{0}\cdot \gamma _{1})(t)={\begin{cases}\gamma _{0}(2t)&0\leq t\leq {\tfrac {1}{2}}\\\gamma _{1}(2t-1)&{\tfrac {1}{2}}\leq t\leq 1.\end{cases}}$

Thus the loop $\gamma _{0}\cdot \gamma _{1}$ first follows the loop $\gamma _{0}$ with "twice the speed" and then follows $\gamma _{1}$ with "twice the speed".

The product of two homotopy classes of loops $[\gamma _{0}]$ and $[\gamma _{1}]$ is then defined as $[\gamma _{0}\cdot \gamma _{1}]$ . It can be shown that this product does not depend on the choice of representatives and therefore gives a well-defined operation on the set $\pi _{1}(X,x_{0})$ . This operation turns $\pi _{1}(X,x_{0})$ into a group. Its neutral element is the equivalence (homotopy) class of the constant loop, which stays at $x_{0}$ for all times t (i.e. this class consists of all loops that can be continuously deformed into the constant loop; intuitively speaking of all the loops that do not "wrap around a hole"). The inverse of a (homotopy class of a) loop is the same loop, but traversed in the opposite direction (which is in a different homotopy class). More formally,

$\gamma ^{-1}(t):=\gamma (1-t).$

Given three based loops $\gamma _{0},\gamma _{1},\gamma _{2},$ the product

$(\gamma _{0}\cdot \gamma _{1})\cdot \gamma _{2}$

is the concatenation of these loops, traversing $\gamma _{0}$ and then $\gamma _{1}$ with quadruple speed, and then $\gamma _{2}$ with double speed. By comparison,

$\gamma _{0}\cdot (\gamma _{1}\cdot \gamma _{2})$

traverses the same paths (in the same order), but $\gamma _{0}$ with double speed, and $\gamma _{1},\gamma _{2}$ with quadruple speed. Thus, because of the differing speeds, the two paths are not identical. The associativity axiom

$[\gamma _{0}]\cdot \left([\gamma _{1}]\cdot [\gamma _{2}]\right)=\left([\gamma _{0}]\cdot [\gamma _{1}]\right)\cdot [\gamma _{2}]$

therefore crucially depends on the fact that paths are considered up to homotopy. Indeed, both above composites are homotopic, for example, to the loop that traverses all three loops $\gamma _{0},\gamma _{1},\gamma _{2}$ with triple speed. The set of based loops up to homotopy, equipped with the above operation therefore does turn $\pi _{1}(X,x_{0})$ into a group.

### Dependence of the base point

Although the fundamental group in general depends on the choice of base point, it turns out that, up to isomorphism, this choice makes no difference as long as the space X is path-connected: more precisely, one obtains an isomorphism by pre- and post-concatenating with a path between the two basepoints. This isomorphism is, in general, not unique: it depends on the choice of path up to homotopy. However changing the path results in changing the isomorphism between the two fundamental groups only by composition with an inner automorphism. It is therefore customary to write $\pi _{1}(X)$ instead of $\pi _{1}(X,x_{0})$ when the choice of basepoint does not matter.

## Concrete examples

This section lists some basic examples of fundamental groups. To begin with, in Euclidean space ( $\mathbb {R} ^{n}$ ) or any convex subset of $\mathbb {R} ^{n},$ there is only one homotopy class of loops, and the fundamental group is therefore the trivial group with one element. More generally, any star domain – and yet more generally, any contractible space – has a trivial fundamental group. Thus, the fundamental group does not distinguish between such spaces.

### The 2-sphere

A path-connected space whose fundamental group is trivial is called simply connected. For example, the 2-sphere $S^{2}=\left\{(x,y,z)\in \mathbb {R} ^{3}\mid x^{2}+y^{2}+z^{2}=1\right\}$ depicted on the right, and also all the higher-dimensional spheres, are simply-connected. The figure illustrates a homotopy contracting one particular loop to the constant loop. This idea can be adapted to all loops $\gamma$ such that there is a point $(x,y,z)\in S^{2}$ that is *not* in the image of $\gamma .$ However, since there are loops such that $\gamma ([0,1])=S^{2}$ (constructed from the Peano curve, for example), a complete proof requires more careful analysis with tools from algebraic topology, such as the Seifert–van Kampen theorem or the cellular approximation theorem.

### The circle

The circle (also known as the 1-sphere)

$S^{1}=\left\{(x,y)\in \mathbb {R} ^{2}\mid x^{2}+y^{2}=1\right\}$

is not simply connected. Instead, each homotopy class consists of all loops that wind around the circle a given number of times (which can be positive or negative, depending on the direction of winding). The product of a loop that winds around m times and another that winds around n times is a loop that winds around $m+n$ times. Therefore, the fundamental group of the circle is isomorphic to $(\mathbb {Z} ,+),$ the additive group of integers. This fact can be used to give proofs of the Brouwer fixed point theorem and the Borsuk–Ulam theorem in dimension 2.

### The figure eight

The fundamental group of the figure eight is the free group on two letters. The idea to prove this is as follows: choosing the base point to be the point where the two circles meet (dotted in black in the picture at the right), any loop $\gamma$ can be decomposed as $\gamma =a^{n_{1}}b^{m_{1}}\cdots a^{n_{k}}b^{m_{k}}$ where a and b are the two loops winding around each half of the figure as depicted, and the exponents $n_{1},\dots ,n_{k},m_{1},\dots ,m_{k}$ are integers. Unlike $\pi _{1}(S^{1})$ , the fundamental group of the figure eight is *not* abelian: the two ways of composing a and b are not homotopic to each other: $[a]\cdot [b]\neq [b]\cdot [a]$

More generally, the fundamental group of a bouquet of r circles is the free group on r letters.

The fundamental group of a wedge sum of two path connected spaces X and Y can be computed as the free product of the individual fundamental groups: $\pi _{1}(X\vee Y)\cong \pi _{1}(X)*\pi _{1}(Y)$ This generalizes the above observations since the figure eight is the wedge sum of two circles.

The fundamental group of the plane punctured at n points is also the free group with n generators. The i -th generator is the class of the loop that goes around the i -th puncture without going around any other punctures.

### Graphs

The fundamental group can be defined for discrete structures too. In particular, consider a connected graph $G=(V,E)$ , with a designated vertex $v_{0}$ in V . The loops in G are the cycles that start and end at $v_{0}$ . Let T be a spanning tree of G . Every simple loop in G contains exactly one edge in $E\setminus T$ ; every loop in G is a concatenation of such simple loops. Therefore, the fundamental group of a graph is a free group, in which the number of generators is exactly the number of edges in $E\setminus T$ . This number equals $|E|-|V|+1$ .

For example, suppose G has 16 vertices arranged in 4 rows of 4 vertices each, with edges connecting vertices that are adjacent horizontally or vertically. Then G has 24 edges overall, and the number of edges in each spanning tree is 16 − 1 = 15, so the fundamental group of G is the free group with 9 generators. Note that G has 9 "holes", similarly to a bouquet of 9 circles, which has the same fundamental group.

### Knot groups

*Knot groups* are by definition the fundamental group of the complement of a knot K embedded in $\mathbb {R} ^{3}$ . For example, the knot group of the trefoil knot is known to be the braid group $B_{3}$ , which gives another example of a non-abelian fundamental group. The Wirtinger presentation explicitly describes knot groups in terms of generators and relations based on a diagram of the knot. Therefore, knot groups have some usage in knot theory to distinguish between knots: if $\pi _{1}(\mathbb {R} ^{3}\setminus K)$ is not isomorphic to some other knot group $\pi _{1}(\mathbb {R} ^{3}\setminus K')$ of another knot $K'$ , then K cannot be transformed into $K'$ . Thus the trefoil knot cannot be continuously transformed into the circle (also known as the unknot), since the latter has knot group $\mathbb {Z}$ . There are, however, knots that cannot be deformed into each other, but have isomorphic knot groups.

### Oriented surfaces

The fundamental group of a genus-*n* orientable surface can be computed in terms of generators and relations as $\left\langle A_{1},B_{1},\ldots ,A_{n},B_{n}\left|A_{1}B_{1}A_{1}^{-1}B_{1}^{-1}\cdots A_{n}B_{n}A_{n}^{-1}B_{n}^{-1}\right.\right\rangle .$

This includes the torus, being the case of genus 1, whose fundamental group is $\left\langle A_{1},B_{1}\left|A_{1}B_{1}A_{1}^{-1}B_{1}^{-1}\right.\right\rangle \cong \mathbb {Z} ^{2}.$

### Topological groups

The fundamental group of a topological group X (with respect to the base point being the neutral element) is always commutative. In particular, the fundamental group of a Lie group is commutative. In fact, the group structure on X endows $\pi _{1}(X)$ with another group structure: given two loops $\gamma$ and $\gamma '$ in X , another loop $\gamma \star \gamma '$ can defined by using the group multiplication in X :

$(\gamma \star \gamma ')(x)=\gamma (x)\cdot \gamma '(x).$

This binary operation $\star$ on the set of all loops is *a priori* independent from the one described above. However, the Eckmann–Hilton argument shows that it does in fact agree with the above concatenation of loops, and moreover that the resulting group structure is abelian.

An inspection of the proof shows that, more generally, $\pi _{1}(X)$ is abelian for any H-space X , i.e., the multiplication need not have an inverse, nor does it have to be associative. For example, this shows that the fundamental group of a loop space of another topological space Y , $X=\Omega (Y),$ is abelian. Related ideas lead to Heinz Hopf's computation of the cohomology of a Lie group.

## Functoriality

If $f\colon X\to Y$ is a continuous map, $x_{0}\in X$ and $y_{0}\in Y$ with $f(x_{0})=y_{0},$ then every loop in X with base point $x_{0}$ can be composed with f to yield a loop in Y with base point $y_{0}.$ This operation is compatible with the homotopy equivalence relation and with composition of loops. The resulting group homomorphism, called the induced homomorphism, is written as $\pi (f)$ or, more commonly,

$f_{*}\colon \pi _{1}(X,x_{0})\to \pi _{1}(Y,y_{0}).$

This mapping from continuous maps to group homomorphisms is compatible with composition of maps and identity morphisms. In the parlance of category theory, the formation of associating to a topological space its fundamental group is therefore a functor

${\begin{aligned}\pi _{1}\colon \mathbf {Top} _{*}&\to \mathbf {Grp} \\(X,x_{0})&\mapsto \pi _{1}(X,x_{0})\end{aligned}}$

from the category of topological spaces together with a base point to the category of groups. It turns out that this functor does not distinguish maps that are homotopic relative to the base point: if $f,g:X\to Y$ are continuous maps with $f(x_{0})=g(x_{0})=y_{0}$ , and f and g are homotopic relative to $\{x_{0}\}$ , then $f_{*}=g_{*}$ . As a consequence, two homotopy equivalent path-connected spaces have isomorphic fundamental groups:

$X\simeq Y\implies \pi _{1}(X,x_{0})\cong \pi _{1}(Y,y_{0}).$

For example, the inclusion of the circle in the punctured plane

$S^{1}\subset \mathbb {R} ^{2}\setminus \{0\}$

is a homotopy equivalence and therefore yields an isomorphism of their fundamental groups.

The fundamental group functor takes products to products and coproducts to coproducts. That is, if X and Y are path connected, then

$\pi _{1}(X\times Y,(x_{0},y_{0}))\cong \pi _{1}(X,x_{0})\times \pi _{1}(Y,y_{0})$

and if they are also locally contractible, then

$\pi _{1}(X\vee Y)\cong \pi _{1}(X)*\pi _{1}(Y).$

(In the latter formula, $\vee$ denotes the wedge sum of pointed topological spaces, and * the free product of groups.) The latter formula is a special case of the Seifert–van Kampen theorem, which states that the fundamental group functor takes pushouts along inclusions to pushouts.

## Abstract results

As was mentioned above, computing the fundamental group of even relatively simple topological spaces tends to be not entirely trivial, but requires some methods of algebraic topology.

### Relationship to first homology group

The abelianization of the fundamental group can be identified with the first homology group of the space.

A special case of the Hurewicz theorem asserts that the first singular homology group $H_{1}(X)$ is, colloquially speaking, the closest approximation to the fundamental group by means of an abelian group. In more detail, mapping the homotopy class of each loop to the homology class of the loop gives a group homomorphism

$\pi _{1}(X)\to H_{1}(X)$

from the fundamental group of a topological space X to its first singular homology group $H_{1}(X).$ This homomorphism is not in general an isomorphism since the fundamental group may be non-abelian, but the homology group is, by definition, always abelian. This difference is, however, the only one: if X is path-connected, this homomorphism is surjective and its kernel is the commutator subgroup of the fundamental group, so that $H_{1}(X)$ is isomorphic to the abelianization of the fundamental group.

### Gluing topological spaces

Generalizing the statement above, for a family of path connected spaces $X_{i},$ the fundamental group ${\textstyle \pi _{1}\left(\bigvee _{i\in I}X_{i}\right)}$ is the free product of the fundamental groups of the $X_{i}.$ This fact is a special case of the Seifert–van Kampen theorem, which allows to compute, more generally, fundamental groups of spaces that are glued together from other spaces. For example, the 2-sphere $S^{2}$ can be obtained by gluing two copies of slightly overlapping half-spheres along a neighborhood of the equator. In this case the theorem yields $\pi _{1}(S^{2})$ is trivial, since the two half-spheres are contractible and therefore have trivial fundamental group. The fundamental groups of surfaces, as mentioned above, can also be computed using this theorem.

In the parlance of category theory, the theorem can be concisely stated by saying that the fundamental group functor takes pushouts (in the category of topological spaces) along inclusions to pushouts (in the category of groups).

### Coverings

Given a topological space B , a continuous map

$f:E\to B$

is called a *covering* or E is called a *covering space* of B if every point b in B admits an open neighborhood U such that there is a homeomorphism between the preimage of U and a disjoint union of copies of U (indexed by some set I ),

$\varphi :\bigsqcup _{i\in I}U\to f^{-1}(U)$

in such a way that $f\circ \varphi$ is the standard projection map $\bigsqcup _{i\in I}U\to U.$

#### Universal covering

A covering is called a universal covering if E is, in addition to the preceding condition, simply connected. It is universal in the sense that all other coverings can be constructed by suitably identifying points in E . Knowing a universal covering

$p:{\widetilde {X}}\to X$

of a topological space X is helpful in understanding its fundamental group in several ways: first, $\pi _{1}(X)$ identifies with the group of deck transformations, i.e., the group of homeomorphisms $\varphi :{\widetilde {X}}\to {\widetilde {X}}$ that commute with the map to X , i.e., $p\circ \varphi =p.$ Another relation to the fundamental group is that $\pi _{1}(X,x)$ can be identified with the fiber $p^{-1}(x).$ For example, the map

$p:\mathbb {R} \to S^{1},\,t\mapsto \exp(2\pi it)$

(or, equivalently, $\pi :\mathbb {R} \to \mathbb {R} /\mathbb {Z} ,\ t\mapsto [t]$ ) is a universal covering. The deck transformations are the maps $t\mapsto t+n$ for $n\in \mathbb {Z} .$ This is in line with the identification $p^{-1}(1)=\mathbb {Z} ,$ in particular this proves the above claim $\pi _{1}(S^{1})\cong \mathbb {Z} .$

Any path connected, locally path connected and locally simply connected topological space X admits a universal covering. An abstract construction proceeds analogously to the fundamental group by taking pairs $(x,\gamma )$ , where x is a point in X and $\gamma$ is a homotopy class of paths from $x_{0}$ to x . The passage from a topological space to its universal covering can be used in understanding the geometry of X . For example, the uniformization theorem shows that any simply connected Riemann surface is (isomorphic to) either $S^{2},$ $\mathbb {C} ,$ or the upper half-plane. General Riemann surfaces then arise as quotients of group actions on these three surfaces.

The quotient of a free action of a discrete group G on a simply connected space Y has fundamental group

$\pi _{1}(Y/G)\cong G.$

As an example, the real n -dimensional real projective space $\mathbb {R} \mathrm {P} ^{n}$ is obtained as the quotient of the n -dimensional unit sphere $S^{n}$ by the antipodal action of the group $\mathbb {Z} /2$ sending $x\in S^{n}$ to $-x.$ As $S^{n}$ is simply connected for $n\geq 2$ , it is a universal cover of $\mathbb {R} \mathrm {P} ^{n}$ in these cases, which implies $\pi _{1}(\mathbb {R} \mathrm {P} ^{n})\cong \mathbb {Z} /2$ for $n\geq 2$ .

#### Lie groups

Let G be a connected, simply connected compact Lie group, for example, the special unitary group ${\text{SU}}(n)$ , and let $\Gamma$ be a finite subgroup of G . Then the homogeneous space $X=G/\Gamma$ has fundamental group $\Gamma$ , which acts by right multiplication on the universal covering space G . Among the many variants of this construction, one of the most important is given by locally symmetric spaces $X=\Gamma \setminus G/K$ , where

- G is a non-compact simply connected, connected Lie group (often semisimple),
- K is a maximal compact subgroup of G
- $\Gamma$ is a discrete countable torsion-free subgroup of G .

In this case the fundamental group is $\Gamma$ and the universal covering space $G/K$ is actually contractible (by the Cartan decomposition for Lie groups).

As an example take $G={\text{SL}}(2,\mathbb {R} )$ , $K={\text{SO}}(2)$ and $\Gamma$ any torsion-free congruence subgroup of the modular group ${\text{SL}}(2,\mathbb {Z} )$ .

From the explicit realization, it also follows that the universal covering space of a path connected topological group H is again a path connected topological group G . Moreover, the covering map is a continuous open homomorphism of G onto H with kernel $\Gamma$ , a closed discrete normal subgroup of G :

$1\to \Gamma \to G\to H\to 1.$

Since G is a connected group with a continuous action by conjugation on a discrete group $\Gamma$ , it must act trivially, so that $\Gamma$ has to be a subgroup of the center of G . In particular $\pi _{1}(H)=\Gamma$ is an abelian group; this can also easily be seen directly without using covering spaces. The group G is called the *universal covering group* of H .

As the universal covering group suggests, there is an analogy between the fundamental group of a topological group and the center of a group; this is elaborated at Lattice of covering groups.

### Fibrations

*Fibrations* provide a very powerful means to compute homotopy groups. A fibration f the so-called *total space*, and the base space B has, in particular, the property that all its fibers $f^{-1}(b)$ are homotopy equivalent and therefore can not be distinguished using fundamental groups (and higher homotopy groups), provided that B is path-connected. Therefore, the space E can be regarded as a "twisted product" of the base space B and the fiber $F=f^{-1}(b).$ The great importance of fibrations to the computation of homotopy groups stems from a long exact sequence

$\dots \to \pi _{2}(B)\to \pi _{1}(F)\to \pi _{1}(E)\to \pi _{1}(B)\to \pi _{0}(F)\to \pi _{0}(E)$

provided that B is path-connected. The term $\pi _{2}(B)$ is the second homotopy group of B , which is defined to be the set of homotopy classes of maps from $S^{2}$ to B , in direct analogy with the definition of $\pi _{1}.$

If E happens to be path-connected and simply connected, this sequence reduces to an isomorphism

$\pi _{1}(B)\cong \pi _{0}(F)$

which generalizes the above fact about the universal covering (which amounts to the case where the fiber F is also discrete). If instead F happens to be connected and simply connected, it reduces to an isomorphism

$\pi _{1}(E)\cong \pi _{1}(B).$

What is more, the sequence can be continued at the left with the higher homotopy groups $\pi _{n}$ of the three spaces, which gives some access to computing such groups in the same vein.

#### Classical Lie groups

Such fiber sequences can be used to inductively compute fundamental groups of compact classical Lie groups such as the special unitary group $\mathrm {SU} (n),$ with $n\geq 2.$ This group acts transitively on the unit sphere $S^{2n-1}$ inside $\mathbb {C} ^{n}=\mathbb {R} ^{2n}.$ The stabilizer of a point in the sphere is isomorphic to $\mathrm {SU} (n-1).$ It then can be shown that this yields a fiber sequence

$\mathrm {SU} (n-1)\to \mathrm {SU} (n)\to S^{2n-1}.$

Since $n\geq 2,$ the sphere $S^{2n-1}$ has dimension at least 3, which implies

$\pi _{1}(S^{2n-1})\cong \pi _{2}(S^{2n-1})=1.$

The long exact sequence then shows an isomorphism

$\pi _{1}(\mathrm {SU} (n))\cong \pi _{1}(\mathrm {SU} (n-1)).$

Since $\mathrm {SU} (1)$ is a single point, so that $\pi _{1}(\mathrm {SU} (1))$ is trivial, this shows that $\mathrm {SU} (n)$ is simply connected for all $n.$

The fundamental group of noncompact Lie groups can be reduced to the compact case, since such a group is homotopic to its maximal compact subgroup. These methods give the following results:

| Compact classical Lie group *G* | Non-compact Lie group | $\pi _{1}$ |
|---|---|---|
| special unitary group $\mathrm {SU} (n)$ | $\mathrm {SL} (n,\mathbb {C} )$ | 1 |
| unitary group $\mathrm {U} (n)$ | $\mathrm {GL} (n,\mathbb {C} ),\mathrm {Sp} (n,\mathbb {R} )$ | $\mathbb {Z}$ |
| special orthogonal group $\mathrm {SO} (n)$ | $\mathrm {SO} (n,\mathbb {C} )$ | $\mathbb {Z} /2$ for $n\geq 3$ and $\mathbb {Z}$ for $n=2$ |
| compact symplectic group $\mathrm {Sp} (n)$ | $\mathrm {Sp} (n,\mathbb {C} )$ | 1 |

A second method of computing fundamental groups applies to all connected compact Lie groups and uses the machinery of the maximal torus and the associated root system. Specifically, let T be a maximal torus in a connected compact Lie group $K,$ and let ${\mathfrak {t}}$ be the Lie algebra of $T.$ The exponential map

$\exp :{\mathfrak {t}}\to T$

is a fibration and therefore its kernel $\Gamma \subset {\mathfrak {t}}$ identifies with $\pi _{1}(T).$ The map

$\pi _{1}(T)\to \pi _{1}(K)$

can be shown to be surjective with kernel given by the set I of integer linear combination of coroots. This leads to the computation

$\pi _{1}(K)\cong \Gamma /I.$

This method shows, for example, that any connected compact Lie group for which the associated root system is of type $G_{2}$ is simply connected. Thus, there is (up to isomorphism) only one connected compact Lie group having Lie algebra of type $G_{2}$ ; this group is simply connected and has trivial center.

## Edge-path group of a simplicial complex

When the topological space is homeomorphic to a simplicial complex, its fundamental group can be described explicitly in terms of generators and relations.

If X is a connected simplicial complex, an *edge-path* in X is defined to be a chain of vertices connected by edges in X . Two edge-paths are said to be *edge-equivalent* if one can be obtained from the other by successively switching between an edge and the two opposite edges of a triangle in X . If v is a fixed vertex in X , an *edge-loop* at v is an edge-path starting and ending at v . The **edge-path group** $E(X,v)$ is defined to be the set of edge-equivalence classes of edge-loops at v , with product and inverse defined by concatenation and reversal of edge-loops.

The edge-path group is naturally isomorphic to $\pi _{1}(|X|,v)$ , the fundamental group of the geometric realisation $|X|$ of X . Since it depends only on the 2-skeleton $X^{2}$ of X (that is, the vertices, edges, and triangles of X ), the groups $\pi _{1}(|X|,v)$ and $\pi _{1}(|X^{2}|,v)$ are isomorphic.

The edge-path group can be described explicitly in terms of generators and relations. If T is a maximal spanning tree in the 1-skeleton of X , then $E(X,v)$ is canonically isomorphic to the group with generators (the oriented edge-paths of X not occurring in T ) and relations (the edge-equivalences corresponding to triangles in X ). A similar result holds if T is replaced by any simply connected—in particular contractible—subcomplex of X . This often gives a practical way of computing fundamental groups and can be used to show that every finitely presented group arises as the fundamental group of a finite simplicial complex. It is also one of the classical methods used for topological surfaces, which are classified by their fundamental groups.

The *universal covering space* of a finite connected simplicial complex X can also be described directly as a simplicial complex using edge-paths. Its vertices are pairs $(w,\gamma )$ where w is a vertex of X and γ is an edge-equivalence class of paths from v to w . The k -simplices containing $(w,\gamma )$ correspond naturally to the k -simplices containing w . Each new vertex u of the k -simplex gives an edge $wu$ and hence, by concatenation, a new path $\gamma _{u}$ from v to u . The points $(w,\gamma )$ and $(u,\gamma _{u})$ are the vertices of the "transported" simplex in the universal covering space. The edge-path group acts naturally by concatenation, preserving the simplicial structure, and the quotient space is just X .

It is well known that this method can also be used to compute the fundamental group of an arbitrary topological space. This was doubtless known to Eduard Čech and Jean Leray and explicitly appeared as a remark in a paper by André Weil; various other authors such as Lorenzo Calabi, Wu Wen-tsün, and Nodar Berikashvili have also published proofs. In the simplest case of a compact space X with a finite open covering in which all non-empty finite intersections of open sets in the covering are contractible, the fundamental group can be identified with the edge-path group of the simplicial complex corresponding to the nerve of the covering.

## Realizability

- Every group can be realized as the fundamental group of a connected CW-complex of dimension 2 (or higher). As noted above, though, only free groups can occur as fundamental groups of 1-dimensional CW-complexes (that is, graphs).
- Every finitely presented group can be realized as the fundamental group of a compact, connected, smooth manifold of dimension 4 (or higher). But there are severe restrictions on which groups occur as fundamental groups of low-dimensional manifolds. For example, no free abelian group of rank 4 or higher can be realized as the fundamental group of a manifold of dimension 3 or less. It can be proved that every group can be realized as the fundamental group of a compact Hausdorff space if and only if there is no measurable cardinal.

### Higher homotopy groups

Roughly speaking, the fundamental group detects the 1-dimensional hole structure of a space, but not higher-dimensional holes such as for the 2-sphere. Such "higher-dimensional holes" can be detected using the higher homotopy groups $\pi _{n}(X)$ , which are defined to consist of homotopy classes of (basepoint-preserving) maps from $S^{n}$ to X . For example, the Hurewicz theorem implies that for all $n\geq 1$ the n -th homotopy group of the *n*-sphere is

$\pi _{n}(S^{n})=\mathbb {Z} .$

As was mentioned in the above computation of $\pi _{1}$ of classical Lie groups, higher homotopy groups can be relevant even for computing fundamental groups.

### Loop space

The set of based loops (as is, i.e. not taken up to homotopy) in a pointed space X , endowed with the compact open topology, is known as the loop space, denoted $\Omega X.$ The fundamental group of X is in bijection with the set of path components of its loop space:

$\pi _{1}(X)\cong \pi _{0}(\Omega X).$

### Fundamental groupoid

The *fundamental groupoid* is a variant of the fundamental group that is useful in situations where the choice of a base point $x_{0}\in X$ is undesirable. It is defined by first considering the category of paths in $X,$ i.e., continuous functions

$\gamma \colon [0,r]\to X$

,

where r is an arbitrary non-negative real number. Since the length r is variable in this approach, such paths can be concatenated as is (i.e., not up to homotopy) and therefore yield a category. Two such paths $\gamma ,\gamma '$ with the same endpoints and length r , resp. r ' are considered equivalent if there exist real numbers $u,v\geqslant 0$ such that $r+u=r'+v$ and $\gamma _{u},\gamma '_{v}\colon [0,r+u]\to X$ are homotopic relative to their end points, where $\gamma _{u}(t)={\begin{cases}\gamma (t),&t\in [0,r]\\\gamma (r),&t\in [r,r+u].\end{cases}}$

The category of paths up to this equivalence relation is denoted $\Pi (X).$ Each morphism in $\Pi (X)$ is an isomorphism, with inverse given by the same path traversed in the opposite direction. Such a category is called a groupoid. It reproduces the fundamental group since

$\pi _{1}(X,x_{0})=\mathrm {Hom} _{\Pi (X)}(x_{0},x_{0})$

.

More generally, one can consider the fundamental groupoid on a set A of base points, chosen according to the geometry of the situation; for example, in the case of the circle, which can be represented as the union of two connected open sets whose intersection has two components, one can choose one base point in each component. The van Kampen theorem admits a version for fundamental groupoids which gives, for example, another way to compute the fundamental group(oid) of $S^{1}.$

### Local systems

Generally speaking, representations may serve to exhibit features of a group by its actions on other mathematical objects, often vector spaces. Representations of the fundamental group have a very geometric significance: any *local system* (i.e., a sheaf ${\mathcal {F}}$ on X with the property that locally in a sufficiently small neighborhood U of any point on X , the restriction of F is a constant sheaf of the form ${\mathcal {F}}|_{U}=\mathbb {Q} ^{n}$ ) gives rise to the so-called monodromy representation, a representation of the fundamental group on an n -dimensional $\mathbb {Q}$ -vector space. Conversely, any such representation on a path-connected space X arises in this manner. This equivalence of categories between representations of $\pi _{1}(X)$ and local systems is used, for example, in the study of differential equations, such as the Knizhnik–Zamolodchikov equations.

### Étale fundamental group

In algebraic geometry, the so-called étale fundamental group is used as a replacement for the fundamental group. Since the Zariski topology on an algebraic variety or scheme X is much coarser than, say, the topology of open subsets in $\mathbb {R} ^{n},$ it is no longer meaningful to consider continuous maps from an interval to X . Instead, the approach developed by Grothendieck consists in constructing $\pi _{1}^{\text{et}}$ by considering all finite étale covers of X . These serve as an algebro-geometric analogue of coverings with finite fibers.

This yields a theory applicable in situations where no great generality classical topological intuition whatsoever is available, for example for varieties defined over a finite field. Also, the étale fundamental group of a field is its (absolute) Galois group. On the other hand, for smooth varieties X over the complex numbers, the étale fundamental group retains much of the information inherent in the classical fundamental group: the former is the profinite completion of the latter.

### Fundamental group of algebraic groups

The fundamental group of a root system is defined in analogy to the computation for Lie groups. This allows to define and use the fundamental group of a semisimple linear algebraic group G , which is a useful basic tool in the classification of linear algebraic groups.

### Fundamental group of simplicial sets

The homotopy relation between 1-simplices of a simplicial set X is an equivalence relation if X is a Kan complex but not necessarily so in general. Thus, $\pi _{1}$ of a Kan complex can be defined as the set of homotopy classes of 1-simplices. The fundamental group of an arbitrary simplicial set X are defined to be the homotopy group of its topological realization, $|X|,$ i.e., the topological space obtained by gluing topological simplices as prescribed by the simplicial set structure of X .

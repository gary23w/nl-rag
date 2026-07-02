---
title: "Topological space"
source: https://en.wikipedia.org/wiki/Topological_space
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Topological space

In mathematics, a **topological space** is, roughly speaking, a space in which closeness is defined but cannot necessarily be measured by a numeric distance. More specifically, a topological space is a set whose elements are called points, along with an additional structure called a topology, which can be defined as a set of neighbourhoods for each point that satisfy some axioms formalizing the concept of closeness. There are several equivalent definitions of a topology, the most commonly used of which is the definition through open sets.

A topological space is the most general type of a mathematical space that allows for the definition of limits, continuity, and connectedness. Common types of topological spaces include Euclidean spaces, metric spaces and manifolds.

Although very general, the concept of topological spaces is fundamental, and used in virtually every branch of modern mathematics. The study of topological spaces in their own right is called general topology (or point-set topology).

## History

> A curved surface is said to possess continuous curvature at one of its points A, if the direction of all the straight lines drawn from A to points of the surface at an infinitesimal distance from A are deflected infinitesimally from one and the same plane passing through A.

—

Carl Friedrich Gauss

,

Gauss 1827

Around 1735, Leonhard Euler discovered the formula $V-E+F=2$ relating the number of vertices ( V ), edges ( E ) and faces ( F ) of a convex polyhedron, and hence of a planar graph. The study and generalization of this formula, specifically by Cauchy (1789–1857) and L'Huilier (1750–1840), boosted the study of topology. In 1827, Carl Friedrich Gauss published *General investigations of curved surfaces*, which in section 3 defines the curved surface in a similar manner to the modern topological understanding.

Yet, "until Riemann's work in the early 1850s, surfaces were always dealt with from a local point of view (as parametric surfaces) and topological issues were never considered". " Möbius and Jordan seem to be the first to realize that the main problem about the topology of (compact) surfaces is to find invariants (preferably numerical) to decide the equivalence of surfaces, that is, to decide whether two surfaces are homeomorphic or not."

The subject is clearly defined by Felix Klein in his "Erlangen Program" (1872): the geometry invariants of arbitrary continuous transformation, a kind of geometry. The term "topology" was introduced by Johann Benedict Listing in 1847, although he had used the term in correspondence some years earlier instead of previously used "Analysis situs". The foundation of this science, for a space of any dimension, was created by Henri Poincaré. His first article on this topic appeared in 1894. In the 1930s, James Waddell Alexander II and Hassler Whitney first expressed the idea that a surface is a topological space that is locally like a Euclidean plane.

Topological spaces were first defined by Felix Hausdorff in 1914 in his seminal "Principles of Set Theory". Metric spaces had been defined earlier in 1906 by Maurice Fréchet, though it was Hausdorff who popularised the term "metric space" (German: *metrischer Raum*).

## Definitions

The utility of the concept of a *topology* is shown by the fact that there are several equivalent definitions of this mathematical structure. Thus one chooses the axiomatization suited for the application. The most commonly used is that in terms of *open sets*, but perhaps more intuitive is that in terms of *neighbourhoods* and so this is given first.

### Definition via neighbourhoods

This axiomatization is due to Felix Hausdorff. Let X be a (possibly empty) set. The elements of X are usually called *points*, though they can be any mathematical object. Let ${\mathcal {N}}$ be a function assigning to each x (point) in X a non-empty collection ${\mathcal {N}}(x)$ of subsets of $X.$ The elements of ${\mathcal {N}}(x)$ will be called *neighbourhoods* of x with respect to ${\mathcal {N}}$ (or, simply, *neighbourhoods of x*). The function ${\mathcal {N}}$ is called a neighbourhood topology if the axioms below are satisfied; and then X with ${\mathcal {N}}$ is called a **topological space**.

1. If N is a neighbourhood of x (i.e., $N\in {\mathcal {N}}(x)$ ), then $x\in N.$ In other words, each point of the set X belongs to every one of its neighbourhoods with respect to ${\mathcal {N}}.$
2. If N is a subset of X and includes a neighbourhood of $x,$ then N is a neighbourhood of $x.$ I.e., every superset of a neighbourhood of a point $x\in X$ is again a neighbourhood of $x.$
3. The intersection of two neighbourhoods of x is a neighbourhood of $x.$
4. Any neighbourhood N of x includes a neighbourhood M of x such that N is a neighbourhood of each point of $M.$

The first three axioms for neighbourhoods have a clear meaning. The fourth axiom has a very important use in the structure of the theory, that of linking together the neighbourhoods of different points of $X.$

A standard example of such a system of neighbourhoods is for the real line $\mathbb {R} ,$ where a subset N of $\mathbb {R}$ is defined to be a *neighbourhood* of a real number x if it includes an open interval containing $x.$

Given such a structure, a subset U of X is defined to be **open** if U is a neighbourhood of all points in $U.$ The open sets then satisfy the axioms given below in the next definition of a topological space. Conversely, when given the open sets of a topological space, the neighbourhoods satisfying the above axioms can be recovered by defining N to be a neighbourhood of x if N includes an open set U such that $x\in U.$

### Definition via open sets

A *topology* on a set X may be defined as a collection $\tau$ of subsets of X, called **open sets** and satisfying the following axioms:

1. The empty set and X itself belong to $\tau .$
2. Any arbitrary (finite or infinite) union of members of $\tau$ belongs to $\tau .$
3. The intersection of any finite number of members of $\tau$ belongs to $\tau .$

As this definition of a topology is the most commonly used, the set $\tau$ of the open sets is commonly called a **topology** on $X.$

A subset $C\subseteq X$ is said to be *closed* in $(X,\tau )$ if its complement $X\setminus C$ is an open set. Note that from this definition, it follows that the empty set and X are simultaneously open *and* closed – that is, the two sets are complements of one another, while each of them is, itself, open. In general, any subset of X with this property is said to be *clopen.*

#### Examples of topologies

1. Given $X=\{1,2,3,4\},$ the trivial or *indiscrete* topology on X is the family $\tau =\{\{\},\{1,2,3,4\}\}=\{\varnothing ,X\}$ consisting of only the two subsets of X required by the axioms forms a topology on $X.$
2. Given $X=\{1,2,3,4\},$ the family $\tau =\{\varnothing ,\{2\},\{1,2\},\{2,3\},\{1,2,3\},X\}$ of six subsets of X forms another topology of $X.$
3. Given $X=\{1,2,3,4\},$ the discrete topology on X is the power set of $X,$ which is the family $\tau =\wp (X)$ consisting of all possible subsets of $X.$ In this case the topological space $(X,\tau )$ is called a *discrete space*.
4. Given $X=\mathbb {Z} ,$ the set of integers, the family $\tau$ of all finite subsets of the integers plus $\mathbb {Z}$ itself is *not* a topology, because (for example) the union of all finite sets not containing zero is not finite and therefore not a member of the family of finite sets. The union of all finite sets not containing zero is also not all of $\mathbb {Z} ,$ and so it cannot be in $\tau .$

### Definition via closed sets

Using de Morgan's laws, the above axioms defining open sets become axioms defining **closed sets**:

1. The empty set and X are closed.
2. The intersection of any collection of closed sets is also closed.
3. The union of any finite number of closed sets is also closed.

Using these axioms, another way to define a topological space is as a set X together with a collection $\tau$ of closed subsets of $X.$ Thus the sets in the topology $\tau$ are the closed sets, and their complements in X are the open sets.

### Other definitions

There are many other equivalent ways to define a topological space: in other words the concepts of neighbourhood, or that of open or closed sets can be reconstructed from other starting points and satisfy the correct axioms.

Another way to define a topological space is by using the Kuratowski closure axioms, which define the closed sets as the fixed points of an operator on the power set of $X.$

A net is a generalisation of the concept of sequence. A topology is completely determined if for every net in X the set of its accumulation points is specified.

## Comparison of topologies

Many topologies can be defined on a set to form a topological space. When every open set of a topology $\tau _{1}$ is also open for a topology $\tau _{2},$ one says that $\tau _{2}$ is *finer* than $\tau _{1},$ and $\tau _{1}$ is *coarser* than $\tau _{2}.$ A proof that relies only on the existence of certain open sets will also hold for any finer topology, and similarly a proof that relies only on certain sets not being open applies to any coarser topology. The terms *larger* and *smaller* are sometimes used in place of finer and coarser, respectively. The terms *stronger* and *weaker* are also used in the literature, but with little agreement on the meaning, so one should always be sure of an author's convention when reading.

The collection of all topologies on a given fixed set X forms a complete lattice: if $F=\left\{\tau _{\alpha }:\alpha \in A\right\}$ is a collection of topologies on $X,$ then the meet of F is the intersection of $F,$ and the join of F is the meet of the collection of all topologies on X that contain every member of $F.$

## Continuous functions

A function $f:X\to Y$ between topological spaces is called continuous if for every $x\in X$ and every neighbourhood N of $f(x)$ there is a neighbourhood M of x such that $f(M)\subseteq N.$ This relates easily to the usual definition in analysis. Equivalently, f is continuous if the inverse image of every open set is open. This is an attempt to capture the intuition that there are no "jumps" or "separations" in the function. A homeomorphism is a bijection that is continuous and whose inverse is also continuous. Two spaces are called *homeomorphic* if there exists a homeomorphism between them. From the standpoint of topology, homeomorphic spaces are essentially identical.

In category theory, one of the fundamental categories is **Top**, which denotes the category of topological spaces whose objects are topological spaces and whose morphisms are continuous functions. The attempt to classify the objects of this category (up to homeomorphism) by invariants has motivated areas of research, such as homotopy theory, homology theory, and K-theory.

## Examples of topological spaces

A given set may have many different topologies. If a set is given a different topology, it is viewed as a different topological space. Any set can be given the discrete topology in which every subset is open. The only convergent sequences or nets in this topology are those that are eventually constant. Also, any set can be given the trivial topology (also called the indiscrete topology), in which only the empty set and the whole space are open. Every sequence and net in this topology converges to every point of the space. This example shows that in general topological spaces, limits of sequences need not be unique. However, often topological spaces must be Hausdorff spaces where limit points are unique.

There exist numerous topologies on any given finite set. Such spaces are called finite topological spaces. Finite spaces are sometimes used to provide examples or counterexamples to conjectures about topological spaces in general.

Any set can be given the cofinite topology in which the open sets are the empty set and the sets whose complement is finite. This is the smallest T1 topology on any infinite set.

Any set can be given the cocountable topology, in which a set is defined as open if it is either empty or its complement is countable. When the set is uncountable, this topology serves as a counterexample in many situations.

The real line can also be given the lower limit topology. Here, the basic open sets are the half open intervals $[a,b).$ This topology on $\mathbb {R}$ is strictly finer than the Euclidean topology defined above; a sequence converges to a point in this topology if and only if it converges from above in the Euclidean topology. This example shows that a set may have many distinct topologies defined on it.

If $\gamma$ is an ordinal number, then the set $\gamma =[0,\gamma )$ may be endowed with the order topology generated by the intervals $(\alpha ,\beta ),$ $[0,\beta ),$ and $(\alpha ,\gamma )$ where $\alpha$ and $\beta$ are elements of $\gamma .$

Every manifold has a natural topology since it is locally Euclidean. Similarly, every simplex and every simplicial complex inherits a natural topology from .

The Sierpiński space is the simplest non-discrete topological space. It has important relations to the theory of computation and semantics.

### Topology from other topologies

Every subset of a topological space can be given the subspace topology in which the open sets are the intersections of the open sets of the larger space with the subset. For any indexed family of topological spaces, the product can be given the product topology, which is generated by the inverse images of open sets of the factors under the projection mappings. For example, in finite products, a basis for the product topology consists of all products of open sets. For infinite products, there is the additional requirement that in a basic open set, all but finitely many of its projections are the entire space. This construction is a special case of an initial topology.

A quotient space is defined as follows: if X is a topological space and Y is a set, and if $f:X\to Y$ is a surjective function, then the quotient topology on Y is the collection of subsets of Y that have open inverse images under $f.$ In other words, the quotient topology is the finest topology on Y for which f is continuous. A common example of a quotient topology is when an equivalence relation is defined on the topological space $X.$ The map f is then the natural projection onto the set of equivalence classes. This construction is a special case of a final topology.

### Metric spaces

Metric spaces embody a metric, a precise notion of distance between points.

Every metric space can be given a metric topology, in which the basic open sets are open balls defined by the metric. This is the standard topology on any normed vector space. On a finite-dimensional vector space this topology is the same for all norms.

There are many ways of defining a topology on $\mathbb {R} ,$ the set of real numbers. The standard topology on $\mathbb {R}$ is generated by the open intervals. The set of all open intervals forms a base or basis for the topology, meaning that every open set is a union of some collection of sets from the base. In particular, this means that a set is open if there exists an open interval of non zero radius about every point in the set. More generally, the Euclidean spaces $\mathbb {R} ^{n}$ can be given a topology. In the **usual topology** on $\mathbb {R} ^{n}$ the basic open sets are the open balls. Similarly, $\mathbb {C} ,$ the set of complex numbers, and $\mathbb {C} ^{n}$ have a standard topology in which the basic open sets are open balls.

### Topology from algebraic structure

For any algebraic objects we can introduce the discrete topology, under which the algebraic operations are continuous functions. For any such structure that is not finite, we often have a natural topology compatible with the algebraic operations, in the sense that the algebraic operations are still continuous. This leads to concepts such as topological groups, topological rings, topological fields and topological vector spaces over the latter. Local fields are topological fields important in number theory.

The Zariski topology is defined algebraically on the spectrum of a ring or an algebraic variety. On $\mathbb {R} ^{n}$ or $\mathbb {C} ^{n},$ the closed sets of the Zariski topology are the solution sets of systems of polynomial equations.

### Topological spaces with order structure

- **Spectral**: A space is *spectral* if and only if it is the prime spectrum of a ring (Hochster theorem).
- **Specialization preorder**: In a space the *specialization preorder* (or *canonical preorder*) is defined by $x\leq y$ if and only if $\operatorname {cl} \{x\}\subseteq \operatorname {cl} \{y\},$ where $\operatorname {cl}$ denotes an operator satisfying the Kuratowski closure axioms.

### Topology from other structure

If $\Gamma$ is a filter on a set X then $\{\varnothing \}\cup \Gamma$ is a topology on $X.$

Many sets of linear operators in functional analysis are endowed with topologies that are defined by specifying when a particular sequence of functions converges to the zero function.

A linear graph has a natural topology that generalizes many of the geometric aspects of graphs with vertices and edges.

Outer space of a free group $F_{n}$ consists of the so-called "marked metric graph structures" of volume 1 on $F_{n}.$

## Classification of topological spaces

Topological spaces can be broadly classified, up to homeomorphism, by their topological properties. A topological property is a property of spaces that is invariant under homeomorphisms. To prove that two spaces are not homeomorphic it is sufficient to find a topological property not shared by them. Examples of such properties include connectedness, compactness, and various separation axioms. For algebraic invariants see algebraic topology.

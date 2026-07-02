---
title: "Connected space"
source: https://en.wikipedia.org/wiki/Connected_space
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Connected space

Connected and disconnected subspaces of

R

²

From top to bottom: red space

A

, pink space

B

, yellow space

C

and orange space

D

are all

connected spaces

, whereas green space

E

(made of

subsets

E

1

, E

2

, E

3

, and E

4

) is

disconnected

. Furthermore,

A

and

B

are also

simply connected

(

genus

0), while

C

and

D

are not:

C

has genus 1 and

D

has genus 4.

In topology and related branches of mathematics, a **connected space** is a topological space that cannot be represented as the union of two or more disjoint non-empty open subsets. Connectedness is one of the principal topological properties that distinguish topological spaces.

A subset of a topological space X is a *connected set* if it is a connected space when viewed as a subspace of X .

Some related but stronger conditions are path connected, simply connected, and n -connected. Another related notion is *locally connected*, which neither implies nor follows from connectedness.

## Definition

A topological space X is said to be *disconnected* if it is the union of two disjoint non-empty open sets. Otherwise, X is said to be *connected*. A subset of a topological space is said to be connected if it is connected under its subspace topology. Some authors exclude the empty set (with its unique topology) as a connected space, but this article does not follow that practice.

**Proposition**—For a topological space X , the following conditions are equivalent:

1. X is connected, that is, it cannot be divided into two disjoint non-empty open sets.
2. The only subsets of X which are both open and closed (clopen sets) are X and the empty set.
3. The only subsets of X with empty boundary are X and the empty set.
4. X cannot be written as the union of two non-empty separated sets (sets for which each is disjoint from the other's closure).
5. All continuous functions from X to $\{0,1\}$ are constant, where $\{0,1\}$ is the two-point space endowed with the discrete topology.
6. All discrete-valued continuous maps on *X* are constant.

Historically this modern formulation of the notion of connectedness (in terms of no partition of X into two separated sets) first appeared (independently) with N.J. Lennes, Frigyes Riesz, and Felix Hausdorff at the beginning of the 20th century. See (Wilder 1978) for details.

Connectedness defines an equivalence relation in the following sense: given two points $x,y$ in a topological space X , we write $x\sim y$ if $x,y$ belong to the same connected subset. Then this $\sim$ is an equivalence relation.

### Connected components

Given some point x in a topological space $X,$ the union of any collection of connected subsets such that each contains x will once again be a connected subset. The *connected component of a point* x in X is the union of all connected subsets of X that contain $x;$ it is the unique largest (with respect to $\subseteq$ ) connected subset of X that contains $x.$ The maximal connected subsets (ordered by inclusion $\subseteq$ ) of a non-empty topological space are called the *connected components* of the space. The components of a topological space X form a partition of  X : they are disjoint, non-empty and their union is the whole space. In fact, a connected component is the same as an equivalence class when two points are equivalent if they belong to the same connected subset (see § Formal definition).

Every component is a closed subset of the original space. It follows that, in the case where their number is finite, each component is also an open subset. However, if their number is infinite, this might not be the case; for instance, the connected components of the set of the rational numbers are the one-point sets (singletons), which are not open. Proof: Any two distinct rational numbers $q_{1}<q_{2}$ are in different components. Take an irrational number $q_{1}<r<q_{2},$ and then set $A=\{q\in \mathbb {Q} :q<r\}$ and $B=\{q\in \mathbb {Q} :q>r\}.$ Then $(A,B)$ is a separation of $\mathbb {Q} ,$ and $q_{1}\in A,q_{2}\in B$ . Thus each component is a one-point set.

Let $\Gamma _{x}$ be the connected component of x in a topological space $X,$ and $\Gamma _{x}'$ be the intersection of all clopen sets containing x (called quasi-component of x ). Then $\Gamma _{x}\subset \Gamma '_{x}$ where the equality holds if X is compact Hausdorff or locally connected.

### Disconnected spaces

A space in which all components are one-point sets is called *totally disconnected*. Related to this property, a space X is called *totally separated* if, for any two distinct elements x and y of X , there exist disjoint open sets U containing x and V containing y such that X is the union of U and V . Clearly, any totally separated space is totally disconnected, but the converse does not hold. For example, take two copies of the rational numbers $\mathbb {Q}$ , and identify them at every point except zero. The resulting space, with the quotient topology, is totally disconnected. However, by considering the two copies of zero, one sees that the space is not totally separated. In fact, it is not even Hausdorff, and the condition of being totally separated is strictly stronger than the condition of being Hausdorff.

## Examples

- The closed interval $[0,2)$ in the standard subspace topology is connected; although it can, for example, be written as the union of $[0,1)$ and $[1,2),$ the second set is not open in the chosen topology of $[0,2).$
- The union of $[0,1)$ and $(1,2]$ is disconnected; both of these intervals are open in the standard topological space $[0,1)\cup (1,2].$
- $(0,1)\cup \{3\}$ is disconnected.
- The space $X=\{a,b\}$ with the indiscrete topology is connected, since its only open sets are $\varnothing$ and X .
- The subspace $Y=[-1,0)\cup (0,1]\subset \mathbb {R}$ is not connected. Indeed, the sets $[-1,0)$ and $(0,1]$ are nonempty, disjoint, and open in the subspace topology on Y , and together form a separation of Y .
- A convex subset of $\mathbb {R} ^{n}$ is connected; it is actually simply connected.
- A Euclidean plane excluding the origin, $(0,0),$ is connected, but is not simply connected. The three-dimensional Euclidean space without the origin is connected, and even simply connected. In contrast, the one-dimensional Euclidean space without the origin is not connected.
- A Euclidean plane with a straight line removed is not connected since it consists of two half-planes.
- $\mathbb {R}$ , the space of real numbers with the usual topology, is connected.
- The Sorgenfrey line is disconnected.
- If even a single point is removed from $\mathbb {R}$ , the remainder is disconnected. However, if even a countable infinity of points are removed from $\mathbb {R} ^{n}$ , where $n\geq 2,$ the remainder is connected. If $n\geq 3$ , then $\mathbb {R} ^{n}$ remains simply connected after removal of countably many points.
- Any topological vector space, e.g. any Hilbert space or Banach space, over a connected field (such as $\mathbb {R}$ or $\mathbb {C}$ ), is simply connected.
- Every discrete topological space with at least two elements is disconnected, in fact such a space is totally disconnected. The simplest example is the discrete two-point space.
- On the other hand, a finite set might be connected. For example, the spectrum of a discrete valuation ring consists of two points and is connected. It is an example of a Sierpiński space.
- The Cantor set is totally disconnected; since the set contains uncountably many points, it has uncountably many components.
- If a space X is homotopy equivalent to a connected space, then X is itself connected.
- The topologist's sine curve is an example of a set that is connected but is neither path connected nor locally connected.
- The general linear group $\operatorname {GL} (n,\mathbb {R} )$ (that is, the group of n -by- n real, invertible matrices) consists of two connected components: the one with matrices of positive determinant and the other of negative determinant. In particular, it is not connected. In contrast, $\operatorname {GL} (n,\mathbb {C} )$ is connected. More generally, the set of invertible bounded operators on a complex Hilbert space is connected.
- The spectra of commutative local ring and integral domains are connected. More generally, the following are equivalent
  1. The spectrum of a commutative ring R is connected
  2. Every finitely generated projective module over R has constant rank.
  3. R has no idempotent $\neq 0,1$ (i.e., R is not a product of two rings in a nontrivial way).

An example of a space that is not connected is a plane with an infinite line deleted from it. Other examples of disconnected spaces (that is, spaces which are not connected) include the plane with an annulus removed, as well as the union of two disjoint closed disks, where all examples of this paragraph bear the subspace topology induced by two-dimensional Euclidean space.

## Path connectedness

A *path-connected space* is a stronger notion of connectedness, requiring the structure of a path. A *path* from a point x to a point y in a topological space X is a continuous function f from the unit interval $[0,1]$ to X with $f(0)=x$ and $f(1)=y$ . A *path-component* of X is an equivalence class of X under the equivalence relation which makes x equivalent to y if and only if there is a path from x to y . The space X is said to be *path-connected* (or *pathwise connected* or $\mathbf {0}$ *-connected*) if there is exactly one path-component.

Equivalently, a path-component of X is a maximal path-connected subset of X (to see the equivalence, note a path-component in the previous sense is path-connected).

Every path-connected space is connected. The converse is not always true: examples of connected spaces that are not path-connected include the extended long line $L^{*}$ and the topologist's sine curve.

Subsets of the real line $\mathbb {R}$ are connected if and only if they are path-connected; these subsets are the intervals and rays of $\mathbb {R}$ . Also, open subsets of $\mathbb {R} ^{n}$ or $\mathbb {C} ^{n}$ are connected if and only if they are path-connected. Additionally, connectedness and path-connectedness are the same for finite topological spaces.

## Arc connectedness

A space X is said to be *arc-connected* or *arcwise connected* if any two topologically distinguishable points can be joined by an arc, which is an embedding $f:[0,1]\to X$ . An *arc-component* of X is a maximal arc-connected subset of X ; or equivalently an equivalence class of the equivalence relation of whether two points can be joined by an arc or by a path whose points are topologically indistinguishable.

Every Hausdorff space that is path-connected is also arc-connected; more generally this is true for a $\Delta$ -Hausdorff space, which is a space where each image of a path is closed. An example of a space which is path-connected but not arc-connected is given by the line with two origins; its two copies of 0 can be connected by a path but not by an arc.

Intuition for path-connected spaces does not readily transfer to arc-connected spaces. Let X be the line with two origins. The following are facts whose analogues hold for path-connected spaces, but do not hold for arc-connected spaces:

- Continuous image of arc-connected space may not be arc-connected: for example, a quotient map from an arc-connected space to its quotient with countably many (at least 2) topologically distinguishable points cannot be arc-connected due to too small cardinality.
- Arc-components may not be disjoint. For example, X has two overlapping arc-components.
- Arc-connected product space may not be a product of arc-connected spaces. For example, $X\times \mathbb {R}$ is arc-connected, but X is not.
- Arc-components of a product space may not be products of arc-components of the marginal spaces. For example, $X\times \mathbb {R}$ has a single arc-component, but X has two arc-components.
- If arc-connected subsets have a non-empty intersection, then their union may not be arc-connected. For example, the arc-components of X intersect, but their union is not arc-connected.

## Local connectedness

A topological space is said to be *locally connected* at a point x if every neighbourhood of x contains a connected open neighbourhood. It is *locally connected* if it has a base of connected sets. It can be shown that a space X is locally connected if and only if every component of every open set of X is open.

Similarly, a topological space is said to be *locally path-connected* if it has a base of path-connected sets. An open subset of a locally path-connected space is connected if and only if it is path-connected. This generalizes the earlier statement about $\mathbb {R} ^{n}$ and $\mathbb {C} ^{n}$ , each of which is locally path-connected. More generally, any topological manifold is locally path-connected.

Locally connected does not imply connected, nor does locally path-connected imply path connected. A simple example of a locally connected (and locally path-connected) space that is not connected (or path-connected) is the union of two separated intervals in $\mathbb {R}$ , such as $(0,1)\cup (2,3)$ .

A classic example of a connected space that is not locally connected is the so-called topologist's sine curve, defined as $T=\{(0,0)\}\cup \left\{\left(x,\sin \left({\tfrac {1}{x}}\right)\right):x\in (0,1]\right\}$ , with the Euclidean topology induced by inclusion in $\mathbb {R} ^{2}$ .

## Set operations

The intersection of connected sets is not necessarily connected.

The union of connected sets is not necessarily connected, as can be seen by considering $X=(0,1)\cup (1,2)$ .

Each ellipse is a connected set, but the union is not connected, since it can be partitioned into two disjoint open sets U and V .

This means that, if the union X is disconnected, then the collection $\{X_{i}\}$ can be partitioned into two sub-collections, such that the unions of the sub-collections are disjoint and open in X (see picture). This implies that in several cases, a union of connected sets *is* necessarily connected. In particular:

1. If the common intersection of all sets is not empty ( ${\textstyle \bigcap X_{i}\neq \emptyset }$ ), then obviously they cannot be partitioned to collections with disjoint unions. Hence the union of connected sets with non-empty intersection is connected.
2. If the intersection of each pair of sets is not empty ( $\forall i,j:X_{i}\cap X_{j}\neq \emptyset$ ) then again they cannot be partitioned to collections with disjoint unions, so their union must be connected.
3. If the sets can be ordered as a "linked chain", i.e. indexed by integer indices and $\forall i:X_{i}\cap X_{i+1}\neq \emptyset$ , then again their union must be connected.
4. If the sets are pairwise-disjoint and the quotient space $X/\{X_{i}\}$ is connected, then X must be connected. Otherwise, if $U\cup V$ is a separation of X then $q(U)\cup q(V)$ is a separation of the quotient space (since $q(U),q(V)$ are disjoint and open in the quotient space).

The set difference of connected sets is not necessarily connected. However, if $X\supseteq Y$ and their difference $X\setminus Y$ is disconnected (and thus can be written as a union of two open sets $X_{1}$ and $X_{2}$ ), then the union of Y with each such component is connected (i.e. $Y\cup X_{i}$ is connected for all i ).

Proof

By contradiction, suppose $Y\cup X_{1}$ is not connected. So it can be written as the union of two disjoint open sets, e.g. $Y\cup X_{1}=Z_{1}\cup Z_{2}$ . Because Y is connected, it must be entirely contained in one of these components, say $Z_{1}$ , and thus $Z_{2}$ is contained in $X_{1}$ . Now we know that: $X=\left(Y\cup X_{1}\right)\cup X_{2}=\left(Z_{1}\cup Z_{2}\right)\cup X_{2}=\left(Z_{1}\cup X_{2}\right)\cup \left(Z_{2}\cap X_{1}\right)$ The two sets in the last union are disjoint and open in X , so there is a separation of X , contradicting the fact that X is connected.

## Theorems

- **Main theorem of connectedness**: Let X and Y be topological spaces and let $f:X\rightarrow Y$ be a continuous function. If X is (path-)connected then the image $f(X)$ is (path-)connected. This result can be considered a generalization of the intermediate value theorem.
- Every path-connected space is connected.
- In a locally path-connected space, every open connected set is path-connected.
- Every locally path-connected space is locally connected.
- A locally path-connected space is path-connected if and only if it is connected.
- The closure of a connected subset is connected. Furthermore, any subset between a connected subset and its closure is connected.
- The connected components are always closed (but in general not open)
- The connected components of a locally connected space are also open.
- The connected components of a space are disjoint unions of the path-connected components (which in general are neither open nor closed).
- Every quotient of a connected (resp. locally connected, path-connected, locally path-connected) space is connected (resp. locally connected, path-connected, locally path-connected).
- Every product of a family of connected (resp. path-connected) spaces is connected (resp. path-connected).
- Every open subset of a locally connected (resp. locally path-connected) space is locally connected (resp. locally path-connected).
- Every manifold is locally path-connected.
- Arc-wise connected space is path connected, but path-wise connected space may not be arc-wise connected
- Continuous image of arc-wise connected set is arc-wise connected.

## Graphs

Graphs have path connected subsets, namely those subsets for which every pair of points has a path of edges joining them. However, it is not always possible to find a topology on the set of points which induces the same connected sets. The 5-cycle graph (and any n -cycle with $n>3$ odd) is one such example.

As a consequence, a notion of connectedness can be formulated independently of the topology on a space. To wit, there is a category of connective spaces consisting of sets with collections of connected subsets satisfying connectivity axioms; their morphisms are those functions which map connected sets to connected sets (Muscat & Buhagiar 2006). Topological spaces and graphs are special cases of connective spaces; indeed, the finite connective spaces are precisely the finite graphs.

However, every graph can be canonically made into a topological space, by treating vertices as points and edges as copies of the unit interval (see topological graph theory#Graphs as topological spaces). Then one can show that the graph is connected (in the graph theoretical sense) if and only if it is connected as a topological space.

## Stronger forms of connectedness

There are stronger forms of connectedness for topological spaces, for instance:

- If there exist no two disjoint non-empty open sets in a topological space X , X must be connected, and thus hyperconnected spaces are also connected.
- Since a simply connected space is, by definition, also required to be path connected, any simply connected space is also connected. If the "path connectedness" requirement is dropped from the definition of simple connectivity, a simply connected space does not need to be connected.
- Yet stronger versions of connectivity include the notion of a contractible space. Every contractible space is path connected and thus also connected.

In general, any path connected space must be connected but there exist connected spaces that are not path connected. The deleted comb space furnishes such an example, as does the above-mentioned topologist's sine curve.

## Weaker forms

A well-chained space is a metric space in which two arbitrary points can be connected by a chain of points that are arbitrarily close. While any well-chained set X is connected, the converse isn't true (an example being $\mathbb {Q}$ ).

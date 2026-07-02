---
title: "Metric space (part 2/2)"
source: https://en.wikipedia.org/wiki/Metric_(mathematics)
domain: metrics-cardinality
license: CC-BY-SA-4.0
tags: metric cardinality, label dimensions explosion, time series count, tag value blowup
fetched: 2026-07-02
part: 2/2
---

## Generalizations of metric spaces

There are several notions of spaces which have less structure than a metric space, but more than a topological space.

- Uniform spaces are spaces in which distances are not defined, but uniform continuity is.
- Approach spaces are spaces in which point-to-set distances are defined, instead of point-to-point distances. They have particularly good properties from the point of view of category theory.
- Continuity spaces are a generalization of metric spaces and posets that can be used to unify the notions of metric spaces and domains.

There are also numerous ways of relaxing the axioms for a metric, giving rise to various notions of generalized metric spaces. These generalizations can also be combined. The terminology used to describe them is not completely standardized. Most notably, in functional analysis pseudometrics often come from seminorms on vector spaces, and so it is natural to call them "semimetrics". This conflicts with the use of the term in topology.

### Extended metrics

Some authors define metrics so as to allow the distance function d to attain the value ∞, i.e. distances are non-negative numbers on the extended real number line. Such a function is also called an *extended metric* or "∞-metric". Every extended metric can be replaced by a real-valued metric that is topologically equivalent. This can be done using a subadditive monotonically increasing bounded function which is zero at zero, e.g. $d'(x,y)=d(x,y)/(1+d(x,y))$ or $d''(x,y)=\min(1,d(x,y))$ .

### Metrics valued in structures other than the real numbers

The requirement that the metric take values in $[0,\infty )$ can be relaxed to consider metrics with values in other structures, including:

- Ordered fields, yielding the notion of a generalised metric.
- More general directed sets. In the absence of an addition operation, the triangle inequality does not make sense and is replaced with an ultrametric inequality. This leads to the notion of a *generalized ultrametric*.

These generalizations still induce a uniform structure on the space.

### Pseudometrics

A *pseudometric* on X is a function $d:X\times X\to \mathbb {R}$ which satisfies the axioms for a metric, except that instead of the second (identity of indiscernibles) only $d(x,x)=0$ for all *x* is required. In other words, the axioms for a pseudometric are:

1. $d(x,y)\geq 0$
2. $d(x,x)=0$
3. $d(x,y)=d(y,x)$
4. $d(x,z)\leq d(x,y)+d(y,z)$ .

In some contexts, pseudometrics are referred to as *semimetrics* because of their relation to seminorms.

### Quasimetrics

Occasionally, a **quasimetric** is defined as a function that satisfies all axioms for a metric with the possible exception of symmetry. The name of this generalisation is not entirely standardized.

1. $d(x,y)\geq 0$
2. $d(x,y)=0\iff x=y$
3. $d(x,z)\leq d(x,y)+d(y,z)$

Quasimetrics are common in real life. For example, given a set X of mountain villages, the typical walking times between elements of X form a quasimetric because travel uphill takes longer than travel downhill. Another example is the length of car rides in a city with one-way streets: here, a shortest path from point A to point B goes along a different set of streets than a shortest path from B to A and may have a different length.

A quasimetric on the reals can be defined by setting $d(x,y)={\begin{cases}x-y&{\text{if }}x\geq y,\\1&{\text{otherwise.}}\end{cases}}$ The 1 may be replaced, for example, by infinity or by $1+{\sqrt {y-x}}$ or any other subadditive function of *y*-*x*. This quasimetric describes the cost of modifying a metal stick: it is easy to reduce its size by filing it down, but it is difficult or impossible to grow it.

Given a quasimetric on X, one can define an R-ball around x to be the set $\{y\in X|d(x,y)\leq R\}$ . As in the case of a metric, such balls form a basis for a topology on X, but this topology need not be metrizable. For example, the topology induced by the quasimetric on the reals described above is the (reversed) Sorgenfrey line.

### Metametrics or partial metrics

In a *metametric*, all the axioms of a metric are satisfied except that the distance between identical points is not necessarily zero. In other words, the axioms for a metametric are:

1. $d(x,y)\geq 0$
2. $d(x,y)=0\implies x=y$
3. $d(x,y)=d(y,x)$
4. $d(x,z)\leq d(x,y)+d(y,z).$

Metametrics appear in the study of Gromov hyperbolic metric spaces and their boundaries. The *visual metametric* on such a space satisfies $d(x,x)=0$ for points x on the boundary, but otherwise $d(x,x)$ is approximately the distance from *x* to the boundary. Metametrics were first defined by Jussi Väisälä. In other work, a function satisfying these axioms is called a *partial metric* or a *dislocated metric*.

### Semimetrics

A **semimetric** on X is a function $d:X\times X\to \mathbb {R}$ that satisfies the first three axioms, but not necessarily the triangle inequality:

1. $d(x,y)\geq 0$
2. $d(x,y)=0\iff x=y$
3. $d(x,y)=d(y,x)$

Some authors work with a weaker form of the triangle inequality, such as:

| $d(x,z)\leq \rho \,(d(x,y)+d(y,z))$ | ρ-relaxed triangle inequality |
|---|---|
| $d(x,z)\leq \rho \,\max\{d(x,y),d(y,z)\}$ | ρ-inframetric inequality |

The ρ-inframetric inequality implies the ρ-relaxed triangle inequality (assuming the first axiom), and the ρ-relaxed triangle inequality implies the 2ρ-inframetric inequality. Semimetrics satisfying these equivalent conditions have sometimes been referred to as *quasimetrics*, *nearmetrics* or **inframetrics**.

The ρ-inframetric inequalities were introduced to model round-trip delay times in the internet. The triangle inequality implies the 2-inframetric inequality, and the ultrametric inequality is exactly the 1-inframetric inequality.

### Premetrics

Relaxing the last three axioms leads to the notion of a **premetric**, i.e. a function satisfying the following conditions:

1. $d(x,y)\geq 0$
2. $d(x,x)=0$

This is not a standard term. Sometimes it is used to refer to other generalizations of metrics such as pseudosemimetrics or pseudometrics; in translations of Russian books it sometimes appears as "prametric". A premetric that satisfies symmetry, i.e. a pseudosemimetric, is also called a distance.

Any premetric gives rise to a topology as follows. For a positive real r , the r -ball centered at a point p is defined as

$B_{r}(p)=\{x|d(x,p)<r\}.$

A set is called *open* if for any point *p* in the set there is an r -ball centered at *p* which is contained in the set. Every premetric space is a topological space, and in fact a sequential space. In general, the r -balls themselves need not be open sets with respect to this topology. As for metrics, the distance between two sets A and *B*, is defined as

$d(A,B)={\underset {x\in A,y\in B}{\inf }}d(x,y).$

This defines a premetric on the power set of a premetric space. If we start with a (pseudosemi-)metric space, we get a pseudosemimetric, i.e. a symmetric premetric. Any premetric gives rise to a preclosure operator $cl$ as follows:

$cl(A)=\{x|d(x,A)=0\}.$

### Pseudoquasimetrics

The prefixes *pseudo-*, *quasi-* and *semi-* can also be combined, e.g., a **pseudoquasimetric** (sometimes called **hemimetric**) relaxes both the indiscernibility axiom and the symmetry axiom and is simply a premetric satisfying the triangle inequality. For pseudoquasimetric spaces the open r -balls form a basis of open sets. A very basic example of a pseudoquasimetric space is the set $\{0,1\}$ with the premetric given by $d(0,1)=1$ and $d(1,0)=0.$ The associated topological space is the Sierpiński space.

Sets equipped with an extended pseudoquasimetric were studied by William Lawvere as "generalized metric spaces". From a categorical point of view, the extended pseudometric spaces and the extended pseudoquasimetric spaces, along with their corresponding nonexpansive maps, are the best behaved of the metric space categories. One can take arbitrary products and coproducts and form quotient objects within the given category. If one drops "extended", one can only take finite products and coproducts. If one drops "pseudo", one cannot take quotients.

Lawvere also gave an alternate definition of such spaces as enriched categories. The ordered set $(\mathbb {R} ,\geq )$ can be seen as a category with one morphism $a\to b$ if $a\geq b$ and none otherwise. Using + as the tensor product and 0 as the identity makes this category into a monoidal category $R^{*}$ . Every (extended pseudoquasi-)metric space $(M,d)$ can now be viewed as a category $M^{*}$ enriched over $R^{*}$ :

- The objects of the category are the points of M.
- For every pair of points x and y such that $d(x,y)<\infty$ , there is a single morphism which is assigned the object $d(x,y)$ of $R^{*}$ .
- The triangle inequality and the fact that $d(x,x)=0$ for all points x derive from the properties of composition and identity in an enriched category.
- Since $R^{*}$ is a poset, all diagrams that are required for an enriched category commute automatically.

### Metrics on multisets

The notion of a metric can be generalized from a distance between two elements to a number assigned to a multiset of elements. A multiset is a generalization of the notion of a set in which an element can occur more than once. Define the multiset union $U=XY$ as follows: if an element x occurs m times in X and n times in Y then it occurs *m* + *n* times in U. A function d on the set of nonempty finite multisets of elements of a set M is a metric if

1. $d(X)=0$ if all elements of X are equal and $d(X)>0$ otherwise (positive definiteness)
2. $d(X)$ depends only on the (unordered) multiset X (symmetry)
3. $d(XY)\leq d(XZ)+d(ZY)$ (triangle inequality)

By considering the cases of axioms 1 and 2 in which the multiset X has two elements and the case of axiom 3 in which the multisets X, Y, and Z have one element each, one recovers the usual axioms for a metric. That is, every multiset metric yields an ordinary metric when restricted to sets of two elements.

A simple example is the set of all nonempty finite multisets X of integers with $d(X)=\max(X)-\min(X)$ . More complex examples are information distance in multisets; and normalized compression distance (NCD) in multisets.

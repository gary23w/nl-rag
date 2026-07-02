---
title: "Normed vector space"
source: https://en.wikipedia.org/wiki/Normed_vector_space
domain: functional-analysis
license: CC-BY-SA-4.0
tags: functional analysis, hilbert space, banach space, linear operator
fetched: 2026-07-02
---

# Normed vector space

In mathematics, a **normed vector space** or **normed space** is a vector space, typically over the real or complex numbers, on which a norm is defined. A norm is a generalization of the intuitive notion of "length" in the physical world. If V is a vector space over K , where K is a field equal to $\mathbb {R}$ or to $\mathbb {C}$ , then a norm on V is a map $V\to \mathbb {R}$ , typically denoted by $\lVert \cdot \rVert$ , satisfying the following four axioms:

1. Non-negativity: for every $x\in V$ , $\;\lVert x\rVert \geq 0$ .
2. Positive definiteness: for every $x\in V$ , $\;\lVert x\rVert =0$ if and only if x is the zero vector.
3. Absolute homogeneity: for every $\lambda \in K$ and $x\in V$ , $\lVert \lambda x\rVert =|\lambda |\,\lVert x\rVert$
4. Triangle inequality: for every $x\in V$ and $y\in V$ , $\|x+y\|\leq \|x\|+\|y\|.$

If V is a real or complex vector space as above, and $\lVert \cdot \rVert$ is a norm on V , then the ordered pair $(V,\lVert \cdot \rVert )$ is called a normed vector space. If it is clear from context which norm is intended, then it is common to denote the normed vector space simply by V .

A norm induces a distance, called its *(norm) induced metric*, by the formula $d(x,y)=\|y-x\|.$ which makes any normed vector space into a metric space and a topological vector space. If this metric space is complete then the normed space is a *Banach space*. Every normed vector space can be "uniquely extended" to a Banach space, which makes normed spaces intimately related to Banach spaces. Every Banach space is a normed space but the converse is not true. For example, the set of the finite sequences of real numbers can be normed with the Euclidean norm, but it is not complete for this norm.

An inner product space is a normed vector space whose norm is the square root of the inner product of a vector and itself. The Euclidean norm of a Euclidean vector space is a special case that allows defining Euclidean distance by the formula $d(A,B)=\|{\overrightarrow {AB}}\|.$

The study of normed spaces and Banach spaces is a fundamental part of functional analysis, a major subfield of mathematics.

## Definition

A **normed vector space** is a vector space equipped with a norm. A **seminormed vector space** is a vector space equipped with a seminorm.

A useful variation of the triangle inequality is $\|x-y\|\geq |\|x\|-\|y\||$ for any vectors x and $y.$

This also shows that a vector norm is a (uniformly) continuous function.

Property 3 depends on a choice of norm $|\alpha |$ on the field of scalars. When the scalar field is $\mathbb {R}$ (or more generally a subset of $\mathbb {C}$ ), this is usually taken to be the ordinary absolute value, but other choices are possible. For example, for a vector space over $\mathbb {Q}$ one could take $|\alpha |$ to be the p -adic absolute value.

## Topological structure

If $(V,\|\,\cdot \,\|)$ is a normed vector space, the norm $\|\,\cdot \,\|$ induces a metric (a notion of *distance*) and therefore a topology on $V.$ This metric is defined in the natural way: the distance between two vectors $\mathbf {u}$ and $\mathbf {v}$ is given by $\|\mathbf {u} -\mathbf {v} \|.$ This topology is precisely the weakest topology which makes $\|\,\cdot \,\|$ continuous and which is compatible with the linear structure of V in the following sense:

1. The vector addition $\,+\,:V\times V\to V$ is jointly continuous with respect to this topology. This follows directly from the triangle inequality.
2. The scalar multiplication $\,\cdot \,:\mathbb {K} \times V\to V,$ where $\mathbb {K}$ is the underlying scalar field of $V,$ is jointly continuous. This follows from the triangle inequality and homogeneity of the norm.

Similarly, for any seminormed vector space we can define the distance between two vectors $\mathbf {u}$ and $\mathbf {v}$ as $\|\mathbf {u} -\mathbf {v} \|.$ This turns the seminormed space into a pseudometric space (notice this is weaker than a metric) and allows the definition of notions such as continuity and convergence. To put it more abstractly every seminormed vector space is a topological vector space and thus carries a topological structure which is induced by the semi-norm.

Of special interest are complete normed spaces, which are known as *Banach spaces*. Every normed vector space V sits as a dense subspace inside some Banach space; this Banach space is essentially uniquely defined by V and is called the *completion* of $V.$

Two norms on the same vector space are called *equivalent* if they define the same topology. On a finite-dimensional vector space (but not infinite-dimensional vector spaces), all norms are equivalent (although the resulting metric spaces need not be the same) And since any Euclidean space is complete, we can thus conclude that all finite-dimensional normed vector spaces are Banach spaces.

A normed vector space V is locally compact if and only if the unit ball $B=\{x:\|x\|\leq 1\}$ is compact, which is the case if and only if V is finite-dimensional; this is a consequence of Riesz's lemma. (In fact, a more general result is true: a topological vector space is locally compact if and only if it is finite-dimensional. The point here is that we don't assume the topology comes from a norm.)

The topology of a seminormed vector space has many nice properties. Given a neighbourhood system ${\mathcal {N}}(0)$ around 0 we can construct all other neighbourhood systems as ${\mathcal {N}}(x)=x+{\mathcal {N}}(0):=\{x+N:N\in {\mathcal {N}}(0)\}$ with $x+N:=\{x+n:n\in N\}.$

Moreover, there exists a neighbourhood basis for the origin consisting of absorbing and convex sets. As this property is very useful in functional analysis, generalizations of normed vector spaces with this property are studied under the name locally convex spaces.

A norm (or seminorm) $\|\cdot \|$ on a topological vector space $(X,\tau )$ is continuous if and only if the topology $\tau _{\|\cdot \|}$ that $\|\cdot \|$ induces on X is coarser than $\tau$ (meaning, $\tau _{\|\cdot \|}\subseteq \tau$ ), which happens if and only if there exists some open ball B in $(X,\|\cdot \|)$ (such as maybe $\{x\in X:\|x\|<1\}$ for example) that is open in $(X,\tau )$ (said different, such that $B\in \tau$ ).

## Normable spaces

A topological vector space $(X,\tau )$ is called **normable** if there exists a norm $\|\cdot \|$ on X such that the canonical metric $(x,y)\mapsto \|y-x\|$ induces the topology $\tau$ on $X.$ The following theorem is due to Kolmogorov:

**Kolmogorov's normability criterion**: A Hausdorff topological vector space is normable if and only if there exists a convex, von Neumann bounded neighborhood of $0\in X.$

A product of a family of normable spaces is normable if and only if only finitely many of the spaces are non-trivial (that is, $\neq \{0\}$ ). Furthermore, the quotient of a normable space X by a closed vector subspace C is normable, and if in addition X 's topology is given by a norm $\|\,\cdot ,\|$ then the map $X/C\to \mathbb {R}$ given by ${\textstyle x+C\mapsto \inf _{c\in C}\|x+c\|}$ is a well defined norm on $X/C$ that induces the quotient topology on $X/C.$

Furthermore, X is finite-dimensional if and only if $X_{\sigma }^{\prime }$ is normable (here $X_{\sigma }^{\prime }$ denotes $X^{\prime }$ endowed with the weak-* topology).

The topology $\tau$ of the Fréchet space $C^{\infty }(K),$ as defined in the article on spaces of test functions and distributions, is defined by a countable family of norms but it is *not* a normable space because there does not exist any norm $\|\cdot \|$ on $C^{\infty }(K)$ such that the topology that this norm induces is equal to $\tau .$

Even if a metrizable topological vector space has a topology that is defined by a family of norms, then it may nevertheless still fail to be normable space (meaning that its topology can not be defined by any *single* norm). An example of such a space is the Fréchet space $C^{\infty }(K),$ whose definition can be found in the article on spaces of test functions and distributions, because its topology $\tau$ is defined by a countable family of norms but it is *not* a normable space because there does not exist any norm $\|\cdot \|$ on $C^{\infty }(K)$ such that the topology this norm induces is equal to $\tau .$ In fact, the topology of a locally convex space X can be a defined by a family of *norms* on X if and only if there exists *at least one* continuous norm on $X.$

## Linear maps and dual spaces

The most important maps between two normed vector spaces are the continuous linear maps. Together with these maps, normed vector spaces form a category.

The norm is a continuous function on its vector space. All linear maps between finite-dimensional vector spaces are also continuous.

An *isometry* between two normed vector spaces is a linear map f which preserves the norm (meaning $\|f(\mathbf {v} )\|=\|\mathbf {v} \|$ for all vectors $\mathbf {v}$ ). Isometries are always continuous and injective. A surjective isometry between the normed vector spaces V and W is called an *isometric isomorphism*, and V and W are called *isometrically isomorphic*. Isometrically isomorphic normed vector spaces are identical for all practical purposes.

When speaking of normed vector spaces, we augment the notion of dual space to take the norm into account. The dual $V^{\prime }$ of a normed vector space V is the space of all *continuous* linear maps from V to the base field (the complexes or the reals) — such linear maps are called "functionals". The norm of a functional $\varphi$ is defined as the supremum of $|\varphi (\mathbf {v} )|$ where $\mathbf {v}$ ranges over all unit vectors (that is, vectors of norm 1 ) in $V.$ This turns $V^{\prime }$ into a normed vector space. An important theorem about continuous linear functionals on normed vector spaces is the Hahn–Banach theorem.

## Normed spaces as quotient spaces of seminormed spaces

The definition of many normed spaces (in particular, Banach spaces) involves a seminorm defined on a vector space and then the normed space is defined as the quotient space by the subspace of elements of seminorm zero. For instance, with the $L^{p}$ spaces, the function defined by $\|f\|_{p}=\left(\int |f(x)|^{p}\;dx\right)^{1/p}$ is a seminorm on the vector space of all functions on which the Lebesgue integral on the right hand side is defined and finite. However, the seminorm is equal to zero for any function supported on a set of Lebesgue measure zero. These functions form a subspace which we "quotient out", making them equivalent to the zero function.

## Finite product spaces

Given n seminormed spaces $\left(X_{i},q_{i}\right)$ with seminorms $q_{i}:X_{i}\to \mathbb {R} ,$ denote the product space by $X:=\prod _{i=1}^{n}X_{i}$ where vector addition defined as $\left(x_{1},\ldots ,x_{n}\right)+\left(y_{1},\ldots ,y_{n}\right):=\left(x_{1}+y_{1},\ldots ,x_{n}+y_{n}\right)$ and scalar multiplication defined as $\alpha \left(x_{1},\ldots ,x_{n}\right):=\left(\alpha x_{1},\ldots ,\alpha x_{n}\right).$

Define a new function $q:X\to \mathbb {R}$ by $q\left(x_{1},\ldots ,x_{n}\right):=\sum _{i=1}^{n}q_{i}\left(x_{i}\right),$ which is a seminorm on $X.$ The function q is a norm if and only if all $q_{i}$ are norms.

More generally, for each real $p\geq 1$ the map $q:X\to \mathbb {R}$ defined by $q\left(x_{1},\ldots ,x_{n}\right):=\left(\sum _{i=1}^{n}q_{i}\left(x_{i}\right)^{p}\right)^{\frac {1}{p}}$ is a semi norm. For each p this defines the same topological space.

A straightforward argument involving elementary linear algebra shows that the only finite-dimensional seminormed spaces are those arising as the product space of a normed space and a space with trivial seminorm. Consequently, many of the more interesting examples and applications of seminormed spaces occur for infinite-dimensional vector spaces.

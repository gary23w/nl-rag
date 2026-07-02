---
title: "Fixed point (mathematics)"
source: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
domain: dynamical-systems
license: CC-BY-SA-4.0
tags: dynamical system, phase space, limit cycle, ergodic theory
fetched: 2026-07-02
---

# Fixed point (mathematics)

In mathematics, a **fixed point** (sometimes shortened to **fixpoint**), also known as an **invariant point**, is a value that does not change under a given transformation. Specifically, for functions, a fixed point is an element that is mapped to itself by the function. Any set of fixed points of a transformation is also an invariant set.

## Fixed point of a function

Formally, c is a fixed point of a function f if c belongs to both the domain and the codomain of f, and *f*(*c*) = *c*. In particular, f cannot have any fixed point if its domain is disjoint from its codomain. If *f* is defined on the real numbers, it corresponds, in graphical terms, to a curve in the Euclidean plane, and each fixed-point *c* corresponds to an intersection of the curve with the line *y* = *x*, cf. picture.

For example, if *f* is defined on the real numbers by $f(x)=x^{2}-3x+4,$ then 2 is a fixed point of *f*, because *f*(2) = 2.

Not all functions have fixed points: for example, *f*(*x*) = *x* + 1 has no fixed points because *x* + 1 is never equal to *x* for any real number.

## Fixed point iteration

In numerical analysis, *fixed-point iteration* is a method of computing fixed points of a function. Specifically, given a function f with the same domain and codomain, a point $x_{0}$ in the domain of f , the fixed-point iteration is

$x_{n+1}=f(x_{n}),\,n=0,1,2,\dots$

which gives rise to the sequence $x_{0},x_{1},x_{2},\dots$ of iterated function applications $x_{0},f(x_{0}),f(f(x_{0})),\dots$ which is hoped to converge to a point x . If f is continuous, then one can prove that the obtained x is a fixed point of f .

The notions of attracting fixed points, repelling fixed points, and periodic points are defined with respect to fixed-point iteration.

## Fixed-point theorems

A fixed-point theorem is a result saying that at least one fixed point exists, under some general condition.

For example, the Banach fixed-point theorem (1922) gives a general criterion guaranteeing that, if it is satisfied, fixed-point iteration will always converge to a fixed point.

The Brouwer fixed-point theorem (1911) says that any continuous function from the closed unit ball in *n*-dimensional Euclidean space to itself must have a fixed point, but it doesn't describe how to find the fixed point.

The Lefschetz fixed-point theorem (and the Nielsen fixed-point theorem) from algebraic topology give a way to count fixed points.

## Fixed point of a group action

In algebra, for a group *G* acting on a set *X* with a group action $\cdot$ , *x* in *X* is said to be a fixed point of *g* if $g\cdot x=x$ .

The fixed-point subgroup $G^{f}$ of an automorphism *f* of a group *G* is the subgroup of *G*: $G^{f}=\{g\in G\mid f(g)=g\}.$

Similarly, the fixed-point subring $R^{f}$ of an automorphism *f* of a ring *R* is the subring of the fixed points of *f*, that is, $R^{f}=\{r\in R\mid f(r)=r\}.$

In Galois theory, the set of the fixed points of a set of automorphisms of a field is called the fixed field of the set of automorphisms.

## Topological fixed point property

A topological space X is said to have the fixed point property (FPP) if for any continuous function

$f\colon X\to X$

there exists $x\in X$ such that $f(x)=x$ .

The FPP is a topological invariant, i.e., it is preserved by any homeomorphism. The FPP is also preserved by any retraction.

According to the Brouwer fixed-point theorem, every compact and convex subset of a Euclidean space has the FPP. Compactness alone does not imply the FPP, and convexity is not even a topological property, so it makes sense to ask how to topologically characterize the FPP. In 1932 Borsuk asked whether compactness together with contractibility could be a necessary and sufficient condition for the FPP to hold. The problem was open for 20 years until the conjecture was disproved by Kinoshita, who found an example of a compact contractible space without the FPP.

## Fixed points of partial orders

In domain theory, the notion and terminology of fixed points is generalized to a partial order. Let ≤ be a partial order over a set *X* and let *f*: *X* → *X* be a function over *X*. Then a **prefixed point** (also spelled **pre-fixed point**, sometimes shortened to **prefixpoint** or **pre-fixpoint**) of *f* is any *p* such that *f*(*p*) ≤ *p*. Analogously, a *postfixed point* of *f* is any *p* such that *p* ≤ *f*(*p*). The opposite usage occasionally appears. Malkis justifies the definition presented here as follows: "since *f* is *before* the inequality sign in the term *f*(*x*) ≤ *x*, such *x* is called a *pre*fix point." A fixed point is a point that is both a prefixpoint and a postfixpoint. Prefixpoints and postfixpoints have applications in theoretical computer science.

### Least fixed point

In order theory, the least fixed point of a function from a partially ordered set (poset) to itself is the fixed point which is less than each other fixed point, according to the order of the poset. A function need not have a least fixed point, but if it does then the least fixed point is unique.

One way to express the Knaster–Tarski theorem is to say that a monotone function on a complete lattice has a least fixed point that coincides with its least prefixpoint (and similarly its greatest fixed point coincides with its greatest postfixpoint).

## Fixed-point combinator

In combinatory logic for computer science, a fixed-point combinator is a higher-order function ${\mathsf {fix}}$ that returns a fixed point of its argument function, if one exists. Formally, if the function *f* has one or more fixed points, then

$\operatorname {\mathsf {fix}} f=f(\operatorname {\mathsf {fix}} f).$

## Fixed-point logics

In mathematical logic, fixed-point logics are extensions of classical predicate logic that have been introduced to express recursion. Their development has been motivated by descriptive complexity theory and their relationship to database query languages, in particular to Datalog.

## Applications

In many fields, equilibria or stability are fundamental concepts that can be described in terms of fixed points. Some examples follow.

- In projective geometry, a fixed point of a projectivity has been called a **double point**.
- In economics, a Nash equilibrium of a game is a fixed point of the game's best response correspondence. John Nash exploited the Kakutani fixed-point theorem for his seminal paper that won him the Nobel prize in economics.
- In physics, more precisely in the theory of phase transitions, *linearization* near an *unstable* fixed point has led to Wilson's Nobel prize-winning work inventing the renormalization group, and to the mathematical explanation of the term "critical phenomenon."
- Programming language compilers use fixed point computations for program analysis, for example in data-flow analysis, which is often required for code optimization. They are also the core concept used by the generic program analysis method abstract interpretation.
- In type theory, the fixed-point combinator allows definition of recursive functions in the untyped lambda calculus.
- The vector of PageRank values of all web pages is the fixed point of a linear transformation derived from the World Wide Web's link structure.
- The stationary distribution of a Markov chain is the fixed point of the one step transition probability function.
- Fixed points are used to finding formulas for iterated functions.

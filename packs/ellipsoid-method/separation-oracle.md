---
title: "Separation oracle"
source: https://en.wikipedia.org/wiki/Separation_oracle
domain: ellipsoid-method
license: CC-BY-SA-4.0
tags: ellipsoid method, khachiyan algorithm, separation oracle, polynomial time optimization
fetched: 2026-07-02
---

# Separation oracle

A **separation oracle** (also called a **cutting-plane oracle**) is a concept in the mathematical theory of convex optimization. It is a method to describe a convex set that is given as an input to an optimization algorithm. Separation oracles are used as input to ellipsoid methods.

## Definition

Let *K* be a convex and compact set in R*n*. A **strong separation oracle for *K*** is an oracle (black box) that, given a vector *y* in R*n*, returns one of the following:

- Assert that *y* is in *K*.
- Find a hyperplane that separates *y* from *K*: a vector **a** in R*n*, such that $a\cdot y>a\cdot x$ for all *x* in *K*.

A strong separation oracle is completely accurate, and thus may be hard to construct. For practical reasons, a weaker version is considered, which allows for small errors in the boundary of *K* and the inequalities. Given a small error tolerance *d*>0, we say that:

- A vector *y* is *d-near K* if its Euclidean distance from *K* is at most *d*;
- A vector *y* is *d-deep in K* if it is in *K*, and its Euclidean distance from any point in outside K is at least *d*.

The weak version also considers *rational* numbers, which have a representation of finite length, rather than arbitrary real numbers. A **weak separation oracle for *K*** is an oracle that, given a vector *y* in Q*n* and a rational number *d*>0, returns one of the following:

- Assert that *y* is *d*-near *K*;
- Find a vector **a** in Q*n*, normalized such that its maximum element is 1, such that $a\cdot y+d\geq a\cdot x$ for all *x* that are *d*-deep in *K*.

## Implementation

A special case of a convex set is a set represented by linear inequalities: *$K=\{x|Ax\leq b\}$ .*Such a set is called a convex *polytope*. A strong separation oracle for a convex polytope can be implemented, but its run-time depends on the input format.

### Representation by inequalities

If the matrix *A* and the vector *b* are given as input, so that *$K=\{x|Ax\leq b\}$*, then a strong separation oracle can be implemented as follows. Given a point *y*, compute *$Ay$*:

- If the outcome is at most *b*, then *y* is in *K* by definition;
- Otherwise, there is at least one row *c* of *A*, such that $c\cdot y$ is larger than the corresponding value in *b*; this row c gives us the separating hyperplane, as $c\cdot y>b\geq c\cdot x$ for all *x* in *K*.

This oracle runs in polynomial time as long as the number of constraints is polynomial.

### Representation by vertices

Suppose the set of vertices of *K* is given as an input, so that *$K={\text{conv}}(v_{1},\ldots ,v_{k})=$* the convex hull of its vertices. Then, deciding whether *y* is in *K* requires to check whether *y* is a convex combination of the input vectors, that is, whether there exist coefficients *z*1,...,*zk* such that:

- $z_{1}\cdot v_{1}+\cdots +z_{k}\cdot v_{k}=y$ ;
- $0\leq z_{i}\leq 1$ for all *i* in 1,...,*k*.

This is a linear program with *k* variables and *n* equality constraints (one for each element of *y*). If *y* is not in *K*, then the above program has no solution, and the separation oracle needs to find a vector *c* such that

- $c\cdot y>c\cdot v_{i}$ for all *i* in 1,...,*k*.

Note that the two above representations can be very different in size: it is possible that a polytope can be represented by a small number of inequalities, but has exponentially many vertices (for example, an *n*-dimensional cube). Conversely, it is possible that a polytope has a small number of vertices, but requires exponentially many inequalities (for example, the convex hull of the 2*n* vectors of the form (0,...,±1,...,0).

### Problem-specific representation

In some linear optimization problems, even though the number of constraints is exponential, one can still write a custom separation oracle that works in polynomial time. Some examples are:

- The minimum-cost arborescence problem: given a weighted directed graph and a vertex *r* in it, find a subgraph of minimum cost that contains a directed path from *r* to any other vertex. The problem can be presented as an LP with a constraint for each subset of vertices, which is an exponential number of constraints. However, a separation oracle can be implemented using *n*-1 applications of the minimum cut procedure.
- The maximum independent set problem. It can be approximated by an LP with a constraint for every odd-length cycle. While there are exponentially-many such cycles, a separation oracle that works in polynomial time can be implemented by just finding an odd cycle of minimum length, which can be done in polynomial time.
- The dual of the configuration linear program for the bin packing problem. It can be approximated by an LP with a constraint for each feasible configuration. While there are exponentially-many such cycles, a separation oracle that works in pseudopolynomial time can be implemented by solving a knapsack problem. This is used by the Karmarkar-Karp bin packing algorithms.

### Non-linear sets

Let *f* be a convex function on R*n*. The set *$K=\{(x,t)|f(x)\leq t\}$* is a convex set in R*n*+1. Given an evaluation oracle for *f* (a black box that returns the value of *f* for every given point), one can easily check whether a vector (*y*, *t*) is in *K*. In order to get a separation oracle, we need also an oracle to evaluate the subgradient of *f*. Suppose some vector (*y*, *s*) is not in *K*, so *f*(*y*) > *s*. Let *g* be the subgradient of *f* at *y* (*g* is a vector in R*n*)*.* Denote *$c:=(g,-1)$*.Then, *$c\cdot (y,s)=g\cdot y-s>g\cdot y-f(y)$*, and for all (*x*, *t*) in *K*: *$c\cdot (x,t)=g\cdot x-t\leq g\cdot x-f(x)$*. By definition of a subgradient: *$f(x)\geq f(y)+g\cdot (x-y)$* for all *x* in R*n*. Therefore, *$g\cdot y-f(y)\geq g\cdot x-f(x)$*, so *$c\cdot (y,s)>c\cdot (x,t)$ ,* and *c* represents a separating hyperplane.

## Usage

A strong separation oracle can be given as an input to the ellipsoid method for solving a linear program. Consider the linear program *${\text{maximize}}~~c\cdot x~~{\text{subject to}}~~Ax\leq b,x\geq 0$*. The ellipsoid method maintains an ellipsoid that initially contains the entire feasible domain $Ax\leq b$ . At each iteration *t*, it takes the center $x_{t}$ of the current ellipsoid, and sends it to the separation oracle:

- If the oracle says that $x_{t}$ is feasible (that is, contained in the set *$Ax\leq b$*), then we do an "optimality cut" at $x_{t}$ : we cut from the ellipsoid all points *x* for which $c\cdot x<c\cdot x_{t}$ . These points are definitely not optimal.
- If the oracle says that $x_{t}$ is infeasible, then it typically returns a specific constraint that is violated by $x_{t}$ , that is, a row $a_{j}$ in the matrix A, such that $a_{j}\cdot x_{t}>b_{j}$ . Since $a_{j}\cdot x\leq b_{j}$ for all feasible *x*, this implies that $a_{j}\cdot x_{t}>a_{j}\cdot x$ for all feasible *x*. Then, we do a "feasibility cut" at $x_{t}$ : we cut from the ellipsoid all points **y** for which $a_{j}\cdot y>a_{j}\cdot x_{t}$ . These points are definitely not feasible.

After making a cut, we construct a new, smaller ellipsoid, that contains the remaining region. It can be shown that this process converges to an approximate solution, in time polynomial in the required accuracy.

## Converting a weak oracle to a strong oracle

Given a weak separation oracle for a *polyhedron*, it is possible to construct a strong separation oracle by a careful method of rounding, or by diophantine approximations.

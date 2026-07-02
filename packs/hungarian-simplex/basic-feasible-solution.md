---
title: "Basic feasible solution"
source: https://en.wikipedia.org/wiki/Basic_feasible_solution
domain: hungarian-simplex
license: CC-BY-SA-4.0
tags: transportation simplex, network simplex method, min cost flow simplex, basic feasible solution
fetched: 2026-07-02
---

# Basic feasible solution

In the theory of linear programming, a **basic feasible solution** (**BFS**) is a solution with a minimal set of non-zero variables. Geometrically, each BFS corresponds to a vertex of the polyhedron of feasible solutions. If there exists an optimal solution, then there exists an optimal BFS. Hence, to find an optimal solution, it is sufficient to consider the BFS-s. This fact is used by the simplex algorithm, which essentially travels from one BFS to another until an optimal solution is found.

## Definitions

### Preliminaries: equational form with linearly-independent rows

For the definitions below, we first present the linear program in the so-called *equational form*:

maximize

${\textstyle \mathbf {c^{T}} \mathbf {x} }$

subject to

$A\mathbf {x} =\mathbf {b}$

and

$\mathbf {x} \geq 0$

where:

- $\mathbf {c^{T}}$ and $\mathbf {x}$ are vectors of size *n* (the number of variables);
- $\mathbf {b}$ is a vector of size *m* (the number of constraints);
- A is an *m*-by-*n* matrix;
- $\mathbf {x} \geq 0$ means that all variables are non-negative.

Any linear program can be converted into an equational form by adding slack variables.

As a preliminary clean-up step, we verify that:

- The system $A\mathbf {x} =\mathbf {b}$ has at least one solution (otherwise the whole LP has no solution and there is nothing more to do);
- All *m* rows of the matrix A are linearly independent, i.e., its rank is *m* (otherwise we can just delete redundant rows without changing the LP).

### Feasible solution

A **feasible solution** of the LP is any vector $\mathbf {x} \geq 0$ such that $A\mathbf {x} =\mathbf {b}$ . We assume that there is at least one feasible solution. If *m* = *n*, then there is only one feasible solution. Typically *m* < *n*, so the system $A\mathbf {x} =\mathbf {b}$ has many solutions; each such solution is called a **feasible solution** of the LP.

### Basis

A **basis** of the LP is a nonsingular submatrix of *A,* with all *m* rows and only *m*<*n* columns.

Sometimes, the term **basis** is used not for the submatrix itself, but for the set of indices of its columns. Let *B* be a subset of *m* indices from {1,...,*n*}. Denote by $A_{B}$ the square *m*-by-*m* matrix made of the *m* columns of A indexed by *B*. If $A_{B}$ is nonsingular, the columns indexed by *B* are a basis of the column space of A . In this case, we call *B* **a basis of the LP.**

Since the rank of A is *m*, it has at least one basis; since A has *n* columns, it has at most ${\binom {n}{m}}$ bases.

### Basic feasible solution

Given a basis *B*, we say that a feasible solution $\mathbf {x}$ is a **basic feasible solution with basis B** if all its non-zero variables are indexed by *B*, that is, for all $j\not \in B:~~x_{j}=0$ .

## Properties

1. A BFS is determined only by the constraints of the LP (the matrix A and the vector $\mathbf {b}$ ); it does not depend on the optimization objective.

2. By definition, a BFS has at most *m* non-zero variables and at least *n*-*m* zero variables. A BFS can have less than *m* non-zero variables; in that case, it can have many different bases, all of which contain the indices of its non-zero variables.

3. A feasible solution $\mathbf {x}$ is basic if-and-only-if the columns of the matrix $A_{K}$ are linearly independent, where *K* is the set of indices of the non-zero elements of $\mathbf {x}$ .

4. Each basis determines a unique BFS: for each basis *B* of *m* indices, there is at most one BFS $\mathbf {x_{B}}$ with basis *B*. This is because $\mathbf {x_{B}}$ must satisfy the constraint $A_{B}\mathbf {x_{B}} =b$ , and by definition of basis the matrix $A_{B}$ is non-singular, so the constraint has a unique solution:

> $\mathbf {x_{B}} ={A_{B}}^{-1}\cdot b$

The opposite is not true: each BFS can come from many different bases. If the unique solution of $\mathbf {x_{B}} ={A_{B}}^{-1}\cdot b$ satisfies the non-negativity constraints $\mathbf {x_{B}} \geq 0$ , then *B* is called a **feasible basis**.

5. If a linear program has an optimal solution (i.e., it has a feasible solution, and the set of feasible solutions is bounded), then it has an optimal BFS. This is a consequence of the Bauer maximum principle: the objective of a linear program is convex; the set of feasible solutions is convex (it is an intersection of hyperspaces); therefore the objective attains its maximum in an extreme point of the set of feasible solutions.

Since the number of BFS-s is finite and bounded by ${\binom {n}{m}}$ , an optimal solution to any LP can be found in finite time by just evaluating the objective function in all ${\binom {n}{m}}$ BFS-s. This is not the most efficient way to solve an LP; the simplex algorithm examines the BFS-s in a much more efficient way.

## Examples

Consider a linear program with the following constraints:

${\begin{aligned}x_{1}+5x_{2}+3x_{3}+4x_{4}+6x_{5}&=14\\x_{2}+3x_{3}+5x_{4}+6x_{5}&=7\\\forall i\in \{1,\ldots ,5\}:x_{i}&\geq 0\end{aligned}}$

The matrix *A* is:

$A={\begin{pmatrix}1&5&3&4&6\\0&1&3&5&6\end{pmatrix}}~~~~~\mathbf {b} =(14~~7)$

Here, *m*=2 and there are 10 subsets of 2 indices, however, not all of them are bases: the set {3,5} is not a basis since columns 3 and 5 are linearly dependent.

The set *B*={2,4} is a basis, since the matrix $A_{B}={\begin{pmatrix}5&4\\1&5\end{pmatrix}}$ is non-singular.

The unique BFS corresponding to this basis is $x_{B}=(0~~2~~0~~1~~0)$ .

## Geometric interpretation

The set of all feasible solutions is an intersection of hyperspaces. Therefore, it is a convex polyhedron. If it is bounded, then it is a convex polytope. Each BFS corresponds to a vertex of this polytope.

## Basic feasible solutions for the dual problem

As mentioned above, every basis *B* defines a unique basic feasible solution $\mathbf {x_{B}} ={A_{B}}^{-1}\cdot b$ . In a similar way, each basis defines a solution to the dual linear program:

minimize

${\textstyle \mathbf {b^{T}} \mathbf {y} }$

subject to

$A^{T}\mathbf {y} \geq \mathbf {c}$

.

The solution is $\mathbf {y_{B}} ={A_{B}^{T}}^{-1}\cdot c$ .

## Finding an optimal BFS

There are several methods for finding a BFS that is also optimal.

### Using the simplex algorithm

In practice, the easiest way to find an optimal BFS is to use the simplex algorithm. It keeps, at each point of its execution, a "current basis" *B* (a subset of *m* out of *n* variables), a "current BFS", and a "current tableau". The tableau is a representation of the linear program where the basic variables are expressed in terms of the non-basic ones: ${\begin{aligned}x_{B}&=p+Qx_{N}\\z&=z_{0}+r^{T}x_{N}\end{aligned}}$ where $x_{B}$ is the vector of *m* basic variables, $x_{N}$ is the vector of *n* non-basic variables, and z is the maximization objective. Since non-basic variables equal 0, the current BFS is p , and the current maximization objective is $z_{0}$ .

If all coefficients in r are negative, then $z_{0}$ is an optimal solution, since all variables (including all non-basic variables) must be at least 0, so the second line implies $z\leq z_{0}$ .

If some coefficients in r are positive, then it may be possible to increase the maximization target. For example, if $x_{5}$ is non-basic and its coefficient in r is positive, then increasing it above 0 may make z larger. If it is possible to do so without violating other constraints, then the increased variable becomes basic (it "enters the basis"), while some basic variable is decreased to 0 to keep the equality constraints and thus becomes non-basic (it "exits the basis").

If this process is done carefully, then it is possible to guarantee that z increases until it reaches an optimal BFS.

### Converting any optimal solution to an optimal BFS

In the worst case, the simplex algorithm may require exponentially many steps to complete. There are algorithms for solving an LP in weakly-polynomial time, such as the ellipsoid method; however, they usually return optimal solutions that are not basic.

However, Given any optimal solution to the LP, it is easy to find an optimal feasible solution that is also *basic*.

### Finding a basis that is both primal-optimal and dual-optimal

A basis *B* of the LP is called **dual-optimal** if the solution $\mathbf {y_{B}} ={A_{B}^{T}}^{-1}\cdot c$ is an optimal solution to the dual linear program, that is, it minimizes ${\textstyle \mathbf {b^{T}} \mathbf {y} }$ . In general, a primal-optimal basis is not necessarily dual-optimal, and a dual-optimal basis is not necessarily primal-optimal (in fact, the solution of a primal-optimal basis may even be unfeasible for the dual, and vice versa).

If both $\mathbf {x_{B}} ={A_{B}}^{-1}\cdot b$ is an optimal BFS of the primal LP, and $\mathbf {y_{B}} ={A_{B}^{T}}^{-1}\cdot c$ is an optimal BFS of the dual LP, then the basis *B* is called **PD-optimal**. Every LP with an optimal solution has a PD-optimal basis, and it is found by the Simplex algorithm. However, its run-time is exponential in the worst case. Nimrod Megiddo proved the following theorems:

- There exists a strongly polynomial time algorithm that inputs an optimal solution to the primal LP *and* an optimal solution to the dual LP, and returns an optimal basis.
- If there exists a strongly polynomial time algorithm that inputs an optimal solution to *only* the primal LP (or only the dual LP) and returns an optimal basis, then there exists a strongly-polynomial time algorithm for solving any linear program (the latter is a famous open problem).

Megiddo's algorithms can be executed using a tableau, just like the simplex algorithm. Megiddo in co-work with Beling proposed also fast algorithm which uses the fast matrix multiplication algorithms .

---
title: "Dantzig–Wolfe decomposition"
source: https://en.wikipedia.org/wiki/Dantzig–Wolfe_decomposition
domain: simplex-method-pivoting
license: CC-BY-SA-4.0
tags: simplex method, pivot rule, bland rule, revised simplex
fetched: 2026-07-02
---

# Dantzig–Wolfe decomposition

**Dantzig–Wolfe decomposition** is an algorithm for solving (mixed integer) linear programming problems by exploiting their structure. It was originally developed by George Dantzig and Philip Wolfe and initially published in 1960. Many texts on linear programming have sections dedicated to discussing this decomposition algorithm. Dantzig–Wolfe decomposition can be used to improve the tractability of large-scale linear programs or create a tighter linear relaxation of mixed integer linear programs.

## Explanation using column generation

The Dantzig-Wolfe decomposition considers the following initial linear program.

${\begin{aligned}\min ~~&c^{T}x\\{\text{subject to}}~~&Ax\leq a\\&Bx\leq b\\&x\in \mathbb {R} \end{aligned}}$

The decomposition starts by reformulating the problem. the constraint $Bx\leq b$ is equivalently reformulating by writing x as a convex combination of points satisfying $Bx\leq b$ . This leads to the following linear program.

${\begin{aligned}\min ~~&c^{T}x\\{\text{subject to}}~~&Ax\leq a\\&x=\sum _{i}\lambda _{i}x_{i}\\&\sum _{i}\lambda _{i}=1\\&x\in \mathbb {R} ,~\lambda _{i}\in \mathbb {R} ^{+}\end{aligned}}$ or equivalently ${\begin{aligned}\min ~~&c^{T}\sum _{i}\lambda _{i}x_{i}\\{\text{subject to}}~~&A\sum _{i}\lambda _{i}x_{i}\leq a\\&\sum _{i}\lambda _{i}=1\\&\lambda _{i}\in \mathbb {R} ^{+}\end{aligned}}$

Here the new variables $\lambda _{i}$ represent the coefficient in the convex combination, and the coefficients $x_{i}$ represent the points satisfying $Bx\leq b$ . In order to be exact, the formulation needs to contain one variable $\lambda _{i}$ for each extreme point of the polyhedron induced by $Bx\leq b$ . This is because every point of a non-empty, bounded convex polyhedron can be represented as a convex combination of its extreme points. This leads to an intractable number of variables.

In order to be able to solve this new formulation containing an intractable number of variables, one use the column generation algorithm. This leads to an iterative algorithm where a couple $(\lambda _{i},x_{i})$ is generated at every iteration.

**Remarque:** if the initial problem contains several constraints $Ax\leq a$ , $Bx\leq b$ , $Cx\leq c$ ... each of these constraints can be independently reformulated with the Dantzig-Wolfe method. This leads to independent sub-problems in the column generation algorithm. This fact is especially useful when the matrix constraint of the initial problem has a form of block diagonal structure.

The whole algorithm can be summarized as follows.

1. Initialize the reformulated problem (P) with a small subset of the points $x_{i}$ and their corresponding variables $\lambda _{i}$ ;
2. Find an optimal solution $x^{*}$ of (P);
3. Search for a point $x_{i}$ satisfying $Bx\leq b$ whose addition to (P) may improve the value of the optimal solution $x^{*}$ ;
4. If such a point exists, add it to (P) and go to Step 2;
5. Otherwise $x^{*}$ is optimal : stop.

It can be visualized as follows.

|   |   |
|---|---|
|   |   |

## Exploiting special structure

The main use case for the Dantzig–Wolfe decomposition is when the constraint matrix of the linear program has the following 'almost diagonal' structure visualized below.

Here, the set of constraints *D* is usually be identified as "connecting", "coupling", or "complicating" constraints. Meanwhile each constraint block *$F_{i}$* is going to be reformulated using the Dantig-Wolfe method. This leads to one sub-problem for each block $F_{i}$ .

The two main reasons why the Dantzig-Wolfe method works especially well in this case are the following. First, each block $F_{i}$ only applies to a subset of the variables. This means the corresponding sub-problem will be a lot smaller than the original problem (less constraints **and** less variables) which means it can be solved faster. Second, although the sub-problem can always be solved independently, in the case of a diagonal structure the sub-problems are usually less linked. Indeed, suppose that $F_{1}$ and $F_{2}$ share a variable $x_{1}$ , then they have to 'agree' on the value of $x_{1}$ . This means every time the $F_{1}$ sub-problem proposes a new point with a different value for $x_{1}$ , the $F_{2}$ sub-problem also has to generate a new point with an agreeing value for $x_{1}$ . This slows down the overall process.

## Implementation

There are examples of the implementation of Dantzig–Wolfe decomposition available in the closed source AMPL and GAMS mathematical modeling software. There are general, parallel, and fast implementations available as open-source software, including some provided by JuMP and the GNU Linear Programming Kit.

The algorithm can be implemented such that the subproblems are solved in parallel, since their solutions are completely independent. When this is the case, there are options for the master program as to how the columns should be integrated into the master. The master may wait until each subproblem has completed and then incorporate all columns that improve the objective or it may choose a smaller subset of those columns. Another option is that the master may take only the first available column and then stop and restart all of the subproblems with new objectives based upon the incorporation of the newest column.

Another design choice for implementation involves columns that exit the basis at each iteration of the algorithm. Those columns may be retained, immediately discarded, or discarded via some policy after future iterations (for example, remove all non-basic columns every 10 iterations).

A (2001) computational evaluation of Dantzig-Wolfe in general and Dantzig-Wolfe and parallel computation is the PhD thesis by J. R. Tebboth

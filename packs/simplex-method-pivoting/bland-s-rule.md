---
title: "Bland's rule"
source: https://en.wikipedia.org/wiki/Bland's_rule
domain: simplex-method-pivoting
license: CC-BY-SA-4.0
tags: simplex method, pivot rule, bland rule, revised simplex
fetched: 2026-07-02
---

# Bland's rule

In mathematical optimization, **Bland's rule** (also known as **Bland's algorithm**, **Bland's anti-cycling rule** or **Bland's pivot rule**) is an algorithmic refinement of the simplex method for linear optimization.

With Bland's rule, the simplex algorithm solves feasible linear optimization problems without cycling.

The original simplex algorithm starts with an arbitrary basic feasible solution, and then changes the basis in order to decrease the minimization target and find an optimal solution. Usually, the target indeed decreases in every step, and thus after a bounded number of steps an optimal solution is found. However, there are examples of degenerate linear programs, on which the original simplex algorithm cycles forever. It gets stuck at a basic feasible solution (a corner of the feasible polytope) and changes bases in a cyclic way without decreasing the minimization target.

Such cycles are avoided by Bland's rule for choosing a column to enter and a column to leave the basis.

Bland's rule was developed by Robert G. Bland while he was a research fellow at the Center for Operations Research and Econometrics in Belgium.

## Algorithm

One uses Bland's rule during an iteration of the simplex method to decide first what column (known as the *entering variable*) and then row (known as the *leaving variable*) in the tableau to pivot on. Assuming that the problem is to minimize the objective function, the algorithm is loosely defined as follows:

1. Choose the lowest-numbered (i.e., leftmost) nonbasic column with a negative (reduced) cost.
2. Now among the rows, choose the one with the lowest ratio between the (transformed) right-hand side and the coefficient in the pivot tableau where the coefficient is greater than zero. If the minimum ratio is shared by several rows, choose the row with the lowest-numbered column (variable) basic in it.

It can be formally proven that, with Bland's selection rule, the simplex algorithm never cycles; therefore, it is guaranteed to terminate within a bounded time.

While Bland's pivot rule is theoretically important, from a practical perspective, it is quite inefficient and takes a long time to converge (for example, the simplex method applied to the Klee-Minty cube). In practice, other pivot rules are used, and cycling rarely happens.

## Extensions to oriented matroids

In the abstract setting of oriented matroids, Bland's rule cycles on some examples. A restricted class of oriented matroids on which Bland's rule avoids cycling has been termed "Bland oriented matroids" by Jack Edmonds. Another pivoting rule, the criss-cross algorithm, avoids cycles on all oriented-matroid linear-programs.

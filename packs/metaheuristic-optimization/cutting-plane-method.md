---
title: "Cutting-plane method"
source: https://en.wikipedia.org/wiki/Cutting-plane_method
domain: metaheuristic-optimization
license: CC-BY-SA-4.0
tags: simulated annealing, genetic algorithm, ant colony optimization, cutting plane method
fetched: 2026-07-02
---

# Cutting-plane method

In mathematical optimization, the **cutting-plane method** is any of a variety of optimization methods that iteratively refine a feasible set or objective function by means of linear inequalities, termed *cuts*. Such procedures are commonly used to find integer solutions to mixed integer linear programming (MILP) problems, as well as to solve general, not necessarily differentiable convex optimization problems. The use of cutting planes to solve MILP was introduced by Ralph E. Gomory.

Cutting plane methods for MILP work by solving a non-integer linear program, the linear relaxation of the given integer program. The theory of Linear Programming dictates that under mild assumptions (if the linear program has an optimal solution, and if the feasible region does not contain a line), one can always find an extreme point or a corner point that is optimal. The obtained optimum is tested for being an integer solution. If it is not, there is guaranteed to exist a linear inequality that *separates* the optimum from the convex hull of the true feasible set. Finding such an inequality is the *separation problem*, and such an inequality is a *cut*. A cut can be added to the relaxed linear program. Then, the current non-integer solution is no longer feasible to the relaxation. This process is repeated until an optimal integer solution is found.

Cutting-plane methods for general convex continuous optimization and variants are known under various names: Kelley's method, Kelley–Cheney–Goldstein method, and bundle methods. They are popularly used for non-differentiable convex minimization, where a convex objective function and its subgradient can be evaluated efficiently but usual gradient methods for differentiable optimization can not be used. This situation is most typical for the concave maximization of Lagrangian dual functions. Another common situation is the application of the Dantzig–Wolfe decomposition to a structured optimization problem in which formulations with an exponential number of variables are obtained. Generating these variables on demand by means of delayed column generation is identical to performing a cutting plane on the respective dual problem.

## History

Cutting planes were proposed by Ralph Gomory in the 1950s as a method for solving integer programming and mixed-integer programming problems. However, most experts, including Gomory himself, considered them to be impractical due to numerical instability, as well as ineffective because many rounds of cuts were needed to make progress towards the solution. Things turned around when in the mid-1990s Gérard Cornuéjols and co-workers showed them to be very effective in combination with branch-and-bound (called branch-and-cut) and ways to overcome numerical instabilities. Nowadays, all commercial MILP solvers use Gomory cuts in one way or another. Gomory cuts are very efficiently generated from a simplex tableau, whereas many other types of cuts are either expensive or even NP-hard to separate. Among other general cuts for MILP, most notably lift-and-project dominates Gomory cuts.

## Gomory's cut

Let an integer programming problem be formulated (in canonical form) as:

${\begin{aligned}{\text{Maximize }}&c^{T}x\\{\text{Subject to }}&Ax\leq b,\\&x\geq 0,\,x_{i}{\text{ all integers}}.\end{aligned}}$

where A is a matrix and b , c is a vector. The vector x is unknown and is to be found in order to maximize the objective while respecting the linear constraints.

### General idea

The method proceeds by first dropping the requirement that the xi be integers and solving the associated relaxed linear programming problem to obtain a basic feasible solution. Geometrically, this solution will be a vertex of the convex polytope consisting of all feasible points. If this vertex is not an integer point then the method finds a hyperplane with the vertex on one side and all feasible integer points on the other. This is then added as an additional linear constraint to exclude the vertex found, creating a modified linear program. The new program is then solved and the process is repeated until an integer solution is found.

### Step 1: solving the relaxed linear program

Using the simplex method to solve a linear program produces a set of equations of the form

$x_{i}+\sum _{j}{\bar {a}}_{i,j}x_{j}={\bar {b}}_{i}$

where *xi* is a basic variable and the *xj'*s are the nonbasic variables (i.e. the basic solution which is an optimal solution to the relaxed linear program is $x_{i}={\bar {b}}_{i}$ and $x_{j}=0$ ). We write coefficients ${\bar {b}}_{i}$ and ${\bar {a}}_{i,j}$ with a bar to denote the last tableau produced by the simplex method. These coefficients are different from the coefficients in the matrix A and the vector b.

### Step 2: Find a linear constraint

Consider now a basic variable $x_{i}$ which is not an integer. Rewrite the above equation so that the integer parts are added on the left side and the fractional parts are on the right side:

$x_{i}+\sum _{j}\lfloor {\bar {a}}_{i,j}\rfloor x_{j}-\lfloor {\bar {b}}_{i}\rfloor ={\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor -\sum _{j}({\bar {a}}_{i,j}-\lfloor {\bar {a}}_{i,j}\rfloor )x_{j}.$

For any integer point in the feasible region, the left side is an integer since all the terms $x_{i}$ , $x_{j}$ , $\lfloor {\bar {a}}_{i,j}\rfloor$ , $\lfloor {\bar {b}}_{i}\rfloor$ are integers. The right side of this equation is strictly less than 1: indeed, ${\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor$ is strictly less than 1 while $-\sum _{j}({\bar {a}}_{i,j}-\lfloor {\bar {a}}_{i,j}\rfloor )x_{j}$ is negative. Therefore the common value must be less than or equal to 0. So the inequality

${\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor -\sum _{j}({\bar {a}}_{i,j}-\lfloor {\bar {a}}_{i,j}\rfloor )x_{j}\leq 0$

must hold for any integer point in the feasible region. Furthermore, non-basic variables are equal to 0s in any basic solution and if *xi* is not an integer for the basic solution *x*,

${\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor -\sum _{j}({\bar {a}}_{i,j}-\lfloor {\bar {a}}_{i,j}\rfloor )x_{j}={\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor >0.$

### Conclusion

So the inequality above excludes the basic feasible solution and thus is a cut with the desired properties. More precisely, ${\bar {b}}_{i}-\lfloor {\bar {b}}_{i}\rfloor -\sum _{j}({\bar {a}}_{i,j}-\lfloor {\bar {a}}_{i,j}\rfloor )x_{j}$ is negative for any integer point in the feasible region, and strictly positive for the basic feasible (non integer) solution of the relaxed linear program. Introducing a new slack variable xk for this inequality, a new constraint is added to the linear program, namely

$x_{k}+\sum _{j}(\lfloor {\bar {a}}_{i,j}\rfloor -{\bar {a}}_{i,j})x_{j}=\lfloor {\bar {b}}_{i}\rfloor -{\bar {b}}_{i},\,x_{k}\geq 0,\,x_{k}{\mbox{ an integer}}.$

## Convex optimization

Cutting plane methods are also applicable in nonlinear programming. The underlying principle is to approximate the feasible region of a nonlinear (convex) program by a finite set of closed half spaces and to solve a sequence of approximating linear programs.

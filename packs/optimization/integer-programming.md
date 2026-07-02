---
title: "Integer programming"
source: https://en.wikipedia.org/wiki/Integer_programming
domain: optimization
license: CC-BY-SA-4.0
tags: mathematical optimization, linear programming, convex optimization, simplex, lagrange multiplier
fetched: 2026-07-02
---

# Integer programming

An **integer programming**, also known as **integer optimization**, problem is a mathematical optimization or feasibility program in which some or all of the variables are restricted to be integers. In many settings the term refers to **integer linear programming** (ILP), in which the objective function and the constraints (other than the integer constraints) are linear.

Integer programming is NP-complete (the difficult part is showing the NP membership). In particular, the special case of 0–1 integer linear programming, in which unknowns are binary, and only the restrictions must be satisfied, is one of Karp's 21 NP-complete problems.

If some decision variables are not discrete, the problem is known as a **mixed-integer programming** problem.

## Canonical and standard form for ILPs

Integer linear programs can be expressed either in *canonical form* or *standard form* (both as defined below), which are different from each other. An integer linear program in canonical form is expressed thus (note that it is the $\mathbf {x}$ vector which is to be decided):

${\begin{aligned}&{\underset {\mathbf {x} \in \mathbb {Z} ^{n}}{\text{maximize}}}&&\mathbf {c} ^{\mathrm {T} }\mathbf {x} \\&{\text{subject to}}&&A\mathbf {x} \leq \mathbf {b} ,\\&&&\mathbf {x} \geq \mathbf {0} \end{aligned}}$

and an ILP in standard form is expressed as

${\begin{aligned}&{\underset {\mathbf {x} \in \mathbb {Z} ^{n}}{\text{maximize}}}&&\mathbf {c} ^{\mathrm {T} }\mathbf {x} \\&{\text{subject to}}&&A\mathbf {x} +\mathbf {s} =\mathbf {b} ,\\&&&\mathbf {s} \geq \mathbf {0} ,\\&&&\mathbf {x} \geq \mathbf {0} ,\end{aligned}}$

where $\mathbf {c} \in \mathbb {R} ^{n},\mathbf {b} \in \mathbb {R} ^{m}$ are vectors and $A\in \mathbb {R} ^{m\times n}$ is a matrix. As with linear programs, ILPs not in standard form can be converted to standard form by eliminating inequalities, introducing slack variables ( $\mathbf {s}$ ) and replacing variables that are not sign-constrained with the difference of two sign-constrained variables.

## Example

The plot on the right shows the following problem.

${\begin{aligned}{\underset {x,y\in \mathbb {Z} }{\text{maximize}}}\quad &y\\{\text{subject to}}\quad &-x+y\leq 1\\&3x+2y\leq 12\\&2x+3y\leq 12\\&x,y\geq 0\end{aligned}}$

The feasible integer points are shown in red, and the red dashed lines indicate their convex hull, which is the smallest convex polyhedron that contains all of these points. The blue lines together with the coordinate axes define the polyhedron of the LP relaxation, which is given by the inequalities without the integrality constraint. The goal of the optimization is to move the black dashed line as far upward while still touching the polyhedron. The optimal solutions of the integer problem are the points $(1,2)$ and $(2,2)$ that both have an objective value of 2. The unique optimum of the relaxation is $(1.8,2.8)$ with objective value of 2.8. If the solution of the relaxation is rounded to the nearest integers, it is not feasible for the ILP. See projection into simplex

## Proof of NP-hardness

The following is a reduction from minimum vertex cover to integer programming that will serve as the proof of NP-hardness.

Let $G=(V,E)$ be an undirected graph. Define a linear program as follows:

${\begin{aligned}\min \sum _{v\in V}y_{v}\\y_{v}+y_{u}&\geq 1&&\forall u,v\in E\\y_{v}&\in \mathbb {Z_{0}^{+}} &&\forall v\in V\end{aligned}}$

Any feasible solution to the integer program will be nonzero on a subset of vertices. The first constraint implies that at least one end point of every edge is included in this subset. Therefore, the solution describes a vertex cover. Additionally given some vertex cover C, $y_{v}$ can be set to 1 for any $v\in C$ and to 0 for any $v\not \in C$ thus giving us a feasible solution to the integer program. Thus we can conclude that if we minimize the sum of $y_{v}$ we have also found the minimum vertex cover.

## Variants

**Mixed-integer linear programming** (**MILP**) involves problems in which only some of the variables, $x_{i}$ , are constrained to be integers, while other variables are allowed to be non-integers.

**Zero–one linear programming** (or **binary integer programming**) involves problems in which the variables are restricted to be either 0 or 1. Any bounded integer variable can be expressed as a combination of binary variables. For example, given an integer variable, $0\leq x\leq U$ , the variable can be expressed using $\lfloor \log _{2}U\rfloor +1$ binary variables:

$x=x_{1}+2x_{2}+4x_{3}+\cdots +2^{\lfloor \log _{2}U\rfloor }x_{\lfloor \log _{2}U\rfloor +1}.$

## Applications

There are two main reasons for using integer variables when modeling problems as a linear program:

1. Some integer variables represent quantities that can only be integer. For example, it is not possible to build 3.7 cars.
2. Other integer variables represent decisions (e.g. whether to include an edge in a graph) and so should only take on the value 0 or 1.

These considerations occur frequently in practice and so integer linear programming can be used in many applications areas, some of which are briefly described below.

### Production planning

Mixed-integer programming has many applications in industrial productions, including job-shop modelling. One important example happens in agricultural production planning and involves determining production yield for several crops that can share resources (e.g. land, labor, capital, seeds, fertilizer, etc.). A possible objective is to maximize the total production, without exceeding the available resources. In some cases, this can be expressed in terms of a linear program, but the variables must be constrained to be integer.

### Scheduling

These problems involve service and vehicle scheduling in transportation networks. For example, a problem may involve assigning buses or subways to individual routes so that a timetable can be met, and also to equip them with drivers. Here binary decision variables indicate whether a bus or subway is assigned to a route and whether a driver is assigned to a particular train or subway. The zero–one programming technique has been successfully applied to solve a project selection problem in which projects are mutually exclusive and/or technologically interdependent.

### Territorial partitioning

Territorial partitioning or districting problems consist of partitioning a geographical region into districts in order to plan some operations while considering different criteria or constraints. Some requirements for this problem are: contiguity, compactness, balance or equity, respect of natural boundaries, and socio-economic homogeneity. Some applications for this type of problem include: political districting, school districting, health services districting and waste management districting.

### Telecommunications networks

The goal of these problems is to design a network of lines to install so that a predefined set of communication requirements are met and the total cost of the network is minimal. This requires optimizing both the topology of the network along with setting the capacities of the various lines. In many cases, the capacities are constrained to be integer quantities. Usually there are, depending on the technology used, additional restrictions that can be modeled as linear inequalities with integer or binary variables.

### Cellular networks

The task of frequency planning in GSM mobile networks involves distributing available frequencies across the antennas so that users can be served and interference is minimized between the antennas. This problem can be formulated as an integer linear program in which binary variables indicate whether a frequency is assigned to an antenna.

### Other applications

- Cash flow matching
- Energy system optimization
- UAV guidance
- Transit map layouting

## Algorithms

The naive way to solve an ILP is to simply remove the constraint that **x** is integer, solve the corresponding LP (called the LP relaxation of the ILP), and then round the entries of the solution to the LP relaxation. But, not only may this solution not be optimal, it may not even be feasible; that is, it may violate some constraint.

### Using total unimodularity

While in general the solution to LP relaxation will not be guaranteed to be integral, if the ILP has the form $\max \mathbf {c} ^{\mathrm {T} }\mathbf {x}$ such that $A\mathbf {x} =\mathbf {b}$ where A and $\mathbf {b}$ have all integer entries and A is totally unimodular, then every basic feasible solution is integral. Consequently, the solution returned by the simplex algorithm is guaranteed to be integral. To show that every basic feasible solution is integral, let $\mathbf {x}$ be an arbitrary basic feasible solution . Since $\mathbf {x}$ is feasible, we know that $A\mathbf {x} =\mathbf {b}$ . Let $\mathbf {x} _{0}=[x_{n_{1}},x_{n_{2}},\cdots ,x_{n_{j}}]$ be the elements corresponding to the basis columns for the basic solution $\mathbf {x}$ . By definition of a basis, there is some square submatrix B of A with linearly independent columns such that $B\mathbf {x} _{0}=\mathbf {b}$ .

Since the columns of B are linearly independent and B is square, B is nonsingular, and therefore by assumption, B is unimodular and so $\det(B)=\pm 1$ . Also, since B is nonsingular, it is invertible and therefore $\mathbf {x} _{0}=B^{-1}\mathbf {b}$ . By definition, $B^{-1}={\frac {B^{\mathrm {adj} }}{\det(B)}}=\pm B^{\mathrm {adj} }$ . Here $B^{\mathrm {adj} }$ denotes the adjugate of B and is integral because B is integral. Therefore, ${\begin{aligned}&\Rightarrow B^{-1}=\pm B^{\mathrm {adj} }{\text{ is integral.}}\\&\Rightarrow \mathbf {x} _{0}=B^{-1}b{\text{ is integral.}}\\&\Rightarrow {\text{Every basic feasible solution is integral.}}\end{aligned}}$ Thus, if the matrix A of an ILP is totally unimodular, rather than use an ILP algorithm, the simplex method can be used to solve the LP relaxation and the solution will be integer.

### Exact algorithms

When the matrix A is not totally unimodular, there are a variety of algorithms that can be used to solve integer linear programs exactly. One class of algorithms are cutting plane methods, which work by solving the LP relaxation and then adding linear constraints that drive the solution towards being integer without excluding any integer feasible points.

Another class of algorithms are variants of the branch and bound method. For example, the branch and cut method that combines both branch and bound and cutting plane methods. Branch and bound algorithms have a number of advantages over algorithms that only use cutting planes. One advantage is that the algorithms can be terminated early and as long as at least one integral solution has been found, a feasible, although not necessarily optimal, solution can be returned. Further, the solutions of the LP relaxations can be used to provide a worst-case estimate of how far from optimality the returned solution is. Finally, branch and bound methods can be used to return multiple optimal solutions.

### Exact algorithms for a small number of variables

Suppose A is an *m*-by-*n* integer matrix and $\mathbf {b}$ is an *m*-by-1 integer vector. We focus on the feasibility problem, which is to decide whether there exists an *n*-by-1 vector $\mathbf {x}$ satisfying $A\mathbf {x} \leq \mathbf {b}$ .

Let *V* be the maximum absolute value of the coefficients in A and $\mathbf {b}$ . If *n* (the number of variables) is a fixed constant, then the feasibility problem can be solved in time polynomial in *m* and log *V*. This is trivial for the case *n*=1. The case *n*=2 was solved in 1981 by Herbert Scarf. The general case was solved in 1983 by Hendrik Lenstra, combining ideas by László Lovász and Peter van Emde Boas. Doignon's theorem asserts that an integer program is feasible whenever every subset of $2^{n}$ constraints is feasible; a method combining this result with algorithms for LP-type problems can be used to solve integer programs in time that is linear in m and fixed-parameter tractable (FPT) in *n*, but possibly doubly exponential in n , with no dependence on V .

In the special case of 0-1 ILP, Lenstra's algorithm is equivalent to complete enumeration: the number of all possible solutions is fixed (2*n*), and checking the feasibility of each solution can be done in time poly(*m*, log *V*). In the general case, where each variable can be an arbitrary integer, complete enumeration is impossible. Here, Lenstra's algorithm uses ideas from Geometry of numbers. It transforms the original problem into an equivalent one with the following property: either the existence of a solution $\mathbf {x}$ is obvious, or the value of $x_{n}$ (the *n*-th variable) belongs to an interval whose length is bounded by a function of *n*. In the latter case, the problem is reduced to a bounded number of lower-dimensional problems. The run-time complexity of the algorithm has been improved in several steps:

- The original algorithm of Lenstra had run-time $2^{O(n^{3})}\cdot (m\cdot \log V)^{O(1)}$ .
- Kannan presented an improved algorithm with run-time $n^{O(n)}\cdot (m\cdot \log V)^{O(1)}$ .
- Frank and Tardos presented an improved algorithm with run-time $n^{2.5n}\cdot 2^{O(n)}\cdot (m\cdot \log V)^{O(1)}$ .
- Dadush presented an improved algorithm with run-time $n^{n}\cdot 2^{O(n)}\cdot (m\cdot \log V)^{O(1)}$ .
- Reis and Rothvoss presented an improved algorithm with run-time $(\log n)^{O(n)}\cdot (m\cdot \log V)^{O(1)}$ .

These algorithms can also be used for **mixed integer linear programs** (MILP) - programs in which some variables are integer and some variables are real. The original algorithm of Lenstra has run-time $2^{O(n^{3})}\cdot poly(d,L)$ , where n is the number of integer variables, d is the number of continuous variables, and *L* is the binary encoding size of the problem. Using techniques from later algorithms, the factor $2^{O(n^{3})}$ can be improved to $2^{O(n\log n)}$ or to $n^{n}$ .

### Heuristic methods

Since integer linear programming is NP-hard, many problem instances are intractable and so heuristic methods must be used instead. For example, tabu search can be used to search for solutions to ILPs. To use tabu search to solve ILPs, moves can be defined as incrementing or decrementing an integer constrained variable of a feasible solution while keeping all other integer-constrained variables constant. The unrestricted variables are then solved for. Short-term memory can consist of previously tried solutions while medium-term memory can consist of values for the integer constrained variables that have resulted in high objective values (assuming the ILP is a maximization problem). Finally, long-term memory can guide the search towards integer values that have not previously been tried.

Other heuristic methods that can be applied to ILPs include

- Hill climbing
- Simulated annealing
- Reactive search optimization
- Ant colony optimization
- Hopfield neural networks

There are also a variety of other problem-specific heuristics, such as the k-opt heuristic for the traveling salesman problem. A disadvantage of heuristic methods is that if they fail to find a solution, it cannot be determined whether it is because there is no feasible solution or whether the algorithm simply was unable to find one. Further, it is usually impossible to quantify how close to optimal a solution returned by these methods are.

## Sparse integer programming

It is often the case that the matrix A that defines the integer program is *sparse*. In particular, this occurs when the matrix has a block structure, which is the case in many applications. The sparsity of the matrix can be measured as follows. The *graph* of A has vertices corresponding to columns of A , and two columns form an edge if A has a row where both columns have nonzero entries. Equivalently, the vertices correspond to variables, and two variables form an edge if they share an inequality. The *sparsity measure* d of A is the minimum of the tree-depth of the graph of A and the tree-depth of the graph of the transpose of A . Let a be the *numeric measure* of A defined as the maximum absolute value of any entry of A . Let n be the number of variables of the integer program. Then it was shown in 2018 that integer programming can be solved in strongly polynomial and fixed-parameter tractable time parameterized by a and d . That is, for some computable function f and some constant k , integer programming can be solved in time $f(a,d)n^{k}$ . In particular, the time is independent of the right-hand side b and objective function c . Moreover, in contrast to the classical result of Lenstra, where the number n of variables is a parameter, here the number n of variables is a variable part of the input.

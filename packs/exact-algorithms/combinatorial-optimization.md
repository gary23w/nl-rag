---
title: "Combinatorial optimization"
source: https://en.wikipedia.org/wiki/Combinatorial_optimization
domain: exact-algorithms
license: CC-BY-SA-4.0
tags: exact algorithm, branch and bound, branch and cut, dynamic programming over subsets
fetched: 2026-07-02
---

# Combinatorial optimization

**Combinatorial optimization** is a subfield of mathematical optimization that consists of finding an optimal object from a finite set of objects, where the set of feasible solutions is discrete or can be reduced to a discrete set. Typical combinatorial optimization problems are the travelling salesman problem ("TSP"), the minimum spanning tree problem ("MST"), and the knapsack problem. In many such problems, such as the ones previously mentioned, exhaustive search is not tractable, and so specialized algorithms that quickly rule out large parts of the search space or approximation algorithms must be resorted to instead.

Combinatorial optimization is related to operations research, algorithm theory, and computational complexity theory. It has important applications in several fields, including artificial intelligence, machine learning, auction theory, software engineering, VLSI, applied mathematics and theoretical computer science.

## Applications

Basic applications of combinatorial optimization include, but are not limited to:

- Logistics
- Supply chain optimization
- Developing the best airline network of spokes and destinations
- Deciding which taxis in a fleet to route to pick up fares
- Determining the optimal way to deliver packages
- Allocating jobs to people optimally
- Designing water distribution networks
- Earth science problems (e.g. reservoir flow-rates)

## Methods

There is a large amount of literature on polynomial-time algorithms for certain special classes of discrete optimization. A considerable amount of it is unified by the theory of linear programming. Some examples of combinatorial optimization problems that are covered by this framework are shortest paths and shortest-path trees, flows and circulations, spanning trees, matching, and matroid problems.

For NP-complete discrete optimization problems, current research literature includes the following topics:

- polynomial-time exactly solvable special cases of the problem at hand (e.g. fixed-parameter tractable problems)
- algorithms that perform well on "random" instances (e.g. for the traveling salesman problem)
- approximation algorithms that run in polynomial time and find a solution that is close to optimal
- parameterized approximation algorithms that run in FPT time and find a solution close to the optimum
- solving real-world instances that arise in practice and do not necessarily exhibit the worst-case behavior of in NP-complete problems (e.g. real-world TSP instances with tens of thousands of nodes).

Combinatorial optimization problems can be viewed as searching for the best element of some set of discrete items; therefore, in principle, any sort of search algorithm or metaheuristic can be used to solve them. Widely applicable approaches include branch-and-bound (an exact algorithm which can be stopped at any point in time to serve as heuristic), branch-and-cut (uses linear optimisation to generate bounds), dynamic programming (a recursive solution construction with limited search window) and tabu search (a greedy-type swapping algorithm). However, generic search algorithms are not guaranteed to find an optimal solution first, nor are they guaranteed to run quickly (in polynomial time). Since some discrete optimization problems are NP-complete, such as the traveling salesman (decision) problem, this is expected unless P=NP.

For each combinatorial optimization problem, there is a corresponding decision problem that asks whether there is a feasible solution for some particular measure $m_{0}$ . For example, if there is a graph G which contains vertices u and v , an optimization problem might be "find a path from u to v that uses the fewest edges". This problem might have an answer of, say, 4. A corresponding decision problem would be "is there a path from u to v that uses 10 or fewer edges?" This problem can be answered with a simple 'yes' or 'no'.

The field of approximation algorithms deals with algorithms to find near-optimal solutions to hard problems. The usual decision version is then an inadequate definition of the problem since it only specifies acceptable solutions. Even though we could introduce suitable decision problems, the problem is then more naturally characterized as an optimization problem.

## NP optimization problem

An *NP-optimization problem* (NPO) is a combinatorial optimization problem with the following additional conditions. Note that the below referred polynomials are functions of the size of the respective functions' inputs, not the size of some implicit set of input instances.

- the size of every feasible solution $y\in f(x)$ , where $f(x)$ denotes the set of feasible solutions to instance x , is polynomially bounded in the size of the given instance x ,
- the languages of valid instances $\{\,x\,\mid \,x\in I\,\}$ and of valid instance–solution pairs $\{\,(x,y)\,\mid \,y\in f(x)\,\}$ can be recognized in polynomial time, and
- The measure $m(x,y)$ of a solution y to problem x is polynomial-time computable.

This implies that the corresponding decision problem is in NP. In computer science, interesting optimization problems usually have the above properties and are therefore NPO problems. A problem is additionally called a P-optimization (PO) problem, if there exists an algorithm which finds optimal solutions in polynomial time. Often, when dealing with the class NPO, one is interested in optimization problems for which the decision versions are NP-complete. Note that hardness relations are always with respect to some reduction. Due to the connection between approximation algorithms and computational optimization problems, reductions which preserve approximation in some respect are for this subject preferred than the usual Turing and Karp reductions. An example of such a reduction would be L-reduction. For this reason, optimization problems with NP-complete decision versions are not necessarily called NPO-complete.

NPO is divided into the following subclasses according to their approximability:

- *NPO(I)*: Equals FPTAS. Contains the Knapsack problem.
- *NPO(II)*: Equals PTAS. Contains the Makespan scheduling problem.
- *NPO(III)*: The class of NPO problems that have polynomial-time algorithms which computes solutions with a cost at most *c* times the optimal cost (for minimization problems) or a cost at least $1/c$ of the optimal cost (for maximization problems). In Hromkovič's book *Algorithms for Hard Problems*, excluded from this class are all NPO(II)-problems save if P=NP. Without the exclusion, equals APX. Contains MAX-SAT and metric TSP.
- *NPO(IV)*: The class of NPO problems with polynomial-time algorithms approximating the optimal solution by a ratio that is polynomial in a logarithm of the size of the input. In Hromkovič's book, all NPO(III)-problems are excluded from this class unless P=NP. Contains the set cover problem.
- *NPO(V)*: The class of NPO problems with polynomial-time algorithms approximating the optimal solution by a ratio bounded by some function on n. In Hromkovic's book, all NPO(IV)-problems are excluded from this class unless P=NP. Contains the TSP and clique problem.

An NPO problem is called *polynomially bounded* (PB) if, for every instance x and for every solution $y\in f(x)$ , the measure $m(x,y)$ is bounded by a polynomial function of the size of x . The class NPOPB is the class of NPO problems that are polynomially-bounded.

## Specific problems

- Assignment problem
- Bin packing problem
- Chinese postman problem
- Closure problem
- Constraint satisfaction problem
- Cutting stock problem
- Dominating set problem
- Integer programming
- Job shop scheduling
- Knapsack problem
- Metric k-center / vertex k-center problem
- Minimum relevant variables in linear system
- Minimum spanning tree
- Nurse scheduling problem
- Ring star problem
- Set cover problem
- Talent scheduling
- Traveling salesman problem
- Vehicle rescheduling problem
- Vehicle routing problem
- Weapon target assignment problem

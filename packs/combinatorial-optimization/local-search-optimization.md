---
title: "Local search (optimization)"
source: https://en.wikipedia.org/wiki/Local_search_(optimization)
domain: combinatorial-optimization
license: CC-BY-SA-4.0
tags: combinatorial optimization, branch and bound, simulated annealing, genetic algorithm
fetched: 2026-07-02
---

# Local search (optimization)

In computer science, **local search** is a heuristic method for solving computationally hard optimization problems. Local search can be used on problems that can be formulated as finding a solution that maximizes a criterion among a number of candidate solutions. Local search algorithms move from solution to solution in the space of candidate solutions (the *search space*) by applying local changes, until a solution deemed optimal is found or a time bound is elapsed.

Local search algorithms are widely applied to numerous hard computational problems, including problems from computer science (particularly artificial intelligence), mathematics, operations research, engineering, and bioinformatics. Examples of local search algorithms are WalkSAT, the 2-opt algorithm for the traveling salesman problem and the Metropolis–Hastings algorithm.

While it is sometimes possible to substitute gradient descent for a local search algorithm, gradient descent is not in the same family: although it is an iterative method for local optimization, it relies on an objective function’s gradient rather than an explicit exploration of the solution space.

## Examples

Some problems where local search has been applied are:

1. The vertex cover problem, in which a solution is a vertex cover of a graph, and the target is to find a solution with a minimal number of nodes
2. The traveling salesman problem, in which a solution is a cycle containing all nodes of the graph and the target is to minimize the total length of the cycle
3. The Boolean satisfiability problem, in which a candidate solution is a truth assignment, and the target is to maximize the number of clauses satisfied by the assignment; in this case, the final solution is of use only if it satisfies *all* clauses
4. The nurse scheduling problem where a solution is an assignment of nurses to shifts which satisfies all established constraints
5. The *k*-medoid clustering problem and other related facility location problems for which local search offers the best known approximation ratios from a worst-case perspective
6. The Hopfield Neural Networks problem involves finding stable configurations in Hopfield network.

## Description

Most problems can be formulated in terms of a search space and target in several different ways. For example, for the traveling salesman problem a solution can be a route visiting all cities and the goal is to find the shortest route. But a solution can also be a path, and being a cycle is part of the target.

A local search algorithm starts from a candidate solution and then iteratively moves to a neighboring solution; a neighborhood being the set of all potential solutions that differ from the current solution by the minimal possible extent. This requires a neighborhood relation to be defined on the search space. As an example, the neighborhood of vertex cover is another vertex cover only differing by one node. For Boolean satisfiability, the neighbors of a Boolean assignment are those that have a single variable in an opposite state. The same problem may have multiple distinct neighborhoods defined on it; local optimization with neighborhoods that involve changing up to *k* components of the solution is often referred to as **k-opt**.

Typically, every candidate solution has more than one neighbor solution; the choice of which one to select is taken using only information about the solutions in the neighborhood of the current assignment, hence the name *local* search. When the choice of the neighbor solution is done by taking the one locally maximizing the criterion, i.e.: a greedy search, the metaheuristic takes the name hill climbing. When no improving neighbors are present, local search is stuck at a locally optimal point. This local-optima problem can be cured by using restarts (repeated local search with different initial conditions), randomization, or more complex schemes based on iterations, like iterated local search, on memory, like reactive search optimization, on memory-less stochastic modifications, like simulated annealing.

Local search does not provide a guarantee that any given solution is optimal. The search can terminate after a given time bound or when the best solution found thus far has not improved in a given number of steps. Local search is an anytime algorithm; it can return a valid solution even if it's interrupted at any time after finding the first valid solution. Local search is typically an approximation or incomplete algorithm because the search may stop even if the current best solution found is not optimal. This can happen even if termination happens because the current best solution could not be improved, as the optimal solution can lie far from the neighborhood of the solutions crossed by the algorithm.

Schuurman & Southey propose three measures of effectiveness for local search (depth, mobility, and coverage):

- depth: the cost of the current (best) solution;
- mobility: the ability to rapidly move to different areas of the search space (whilst keeping the cost low);
- coverage: how systematically the search covers the search space, the maximum distance between any unexplored assignment and all visited assignments.

They hypothesize that local search algorithms work well, not because they have some understanding of the search space but because they quickly move to promising regions, and explore the search space at low depths as quickly, broadly, and systematically as possible.

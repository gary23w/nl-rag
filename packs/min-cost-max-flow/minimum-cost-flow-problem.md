---
title: "Minimum-cost flow problem"
source: https://en.wikipedia.org/wiki/Minimum-cost_flow_problem
domain: min-cost-max-flow
license: CC-BY-SA-4.0
tags: minimum cost flow, min cost max flow, successive shortest path, cost scaling
fetched: 2026-07-02
---

# Minimum-cost flow problem

The **minimum-cost flow problem** (**MCFP**) is an optimization and decision problem to find the cheapest possible way of sending a certain amount of flow through a flow network. A typical application of this problem involves finding the best delivery route from a factory to a warehouse where the road network has some capacity and cost associated. The minimum cost flow problem is one of the most fundamental among all flow and circulation problems because most other such problems can be cast as a minimum cost flow problem and also that it can be solved efficiently using the network simplex algorithm.

## Definition

A flow network is a directed graph $G=(V,E)$ with a source vertex $s\in V$ and a sink vertex $t\in V$ , where each edge $(u,v)\in E$ has capacity $c(u,v)>0$ , flow $f(u,v)$ and cost $a(u,v)$ , with most minimum-cost flow algorithms supporting edges with negative costs. The cost of sending this flow along an edge $(u,v)$ is $f(u,v)\cdot a(u,v)$ . The problem requires an amount of flow d to be sent from source s to sink t .

The definition of the problem is to minimize the **total cost** of the flow over all edges:

$\sum _{(u,v)\in E}a(u,v)\cdot f(u,v)$

with the constraints

| **Capacity constraints**: | $\,f(u,v)\leq c(u,v)$ |
|---|---|
| **Skew symmetry**: | $\,f(u,v)=-f(v,u)$ |
| **Flow conservation**: | $\,\sum _{w\in V}f(u,w)=0{\text{ for all }}u\neq s,t$ |
| **Required flow**: | $\,\sum _{w\in V}f(s,w)=d{\text{ and }}\sum _{w\in V}f(w,t)=d$ |

## Relation to other problems

A variation of this problem is to find a flow which is maximum, but has the lowest cost among the maximum flow solutions. This could be called a minimum-cost maximum-flow problem and is useful for finding minimum cost maximum matchings.

With some solutions, finding the minimum cost maximum flow instead is straightforward. If not, one can find the maximum flow by performing a binary search on d .

A related problem is the minimum cost circulation problem, which can be used for solving minimum cost flow. The minimum cost circulation problem has no source and sink; instead it has costs and lower and upper bounds on each edge, and seeks flow amounts within the given bounds that balance the flow at each vertex and minimize the sum over edges of cost times flow. Any minimum-cost flow instance can be converted into a minimum cost circulation instance by setting the lower bound on all edges to zero, and then making an extra edge from the sink t to the source s , with capacity $c(t,s)=d$ and lower bound $l(t,s)=d$ , forcing the total flow from s to t to also be d .

The following problems are special cases of the minimum cost flow problem (we provide brief sketches of each applicable reduction, in turn):

- Shortest path problem (single-source). Require that a feasible solution to the minimum cost flow problem sends one unit of flow from a designated source s to a designated sink t . Give all edges infinite capacity.
- Maximum flow problem. Choose a large demand d (large enough to exceed the maximum flow; for instance, the sum of capacities out of the source vertex) Set the costs of all edges in the maximum flow instance to zero, and introduce a new edge from source to sink with unit cost and capacity d .
- Assignment problem. Suppose that each partite set in the bipartition has n vertices, and denote the bipartition by $(X,Y)$ . Give each $x\in X$ supply $1/n$ and give each $y\in Y$ demand $1/n$ . Each edge is to have unit capacity.

## Solutions

The minimum cost flow problem can be solved by linear programming, since we optimize a linear function, and all constraints are linear.

Apart from that, many combinatorial algorithms exist. Some of them are generalizations of maximum flow algorithms, others use entirely different approaches.

Well-known fundamental algorithms (they have many variations):

- *Cycle canceling*: a general primal method.
- *Cut canceling*: a general dual method.
- *Minimum mean cycle canceling*: a simple strongly polynomial algorithm.
- *Successive shortest path* and *capacity scaling*: dual methods, which can be viewed as the generalization of the Ford–Fulkerson algorithm.
- *Cost scaling*: a primal-dual approach, which can be viewed as the generalization of the push-relabel algorithm.
- *Network simplex algorithm*: a specialized version of the linear programming simplex method.
- *Out-of-kilter algorithm* by D. R. Fulkerson

### Cycle canceling algorithms

These algorithms are iterative and like the Ford–Fulkerson algorithm they define a residual graph. If there is flow $f(u,v)$ on arc $e=(u,v)$ , then its residual capacity is defined to be $c(e)-f(e)$ and its residual cost is $a(e)$ . The reverse arc (which has negative flow value) has a negative cost $-a(e)$ . The algorithms then start with an arbitrary feasible flow and iteratively improve the cost of the solution by pushing flow around negative-cost cycles. In the *Minimum mean cycle canceling*, the algorithm selects a cycle that has minimum mean cost (the ratio of the total cycle cost to the number of arcs). Such a cycle can be found in polynomial time (by binary search using the Bellman-Ford algorithm) and the total number of iterations has been proven to be polynomial.

## Application

### Minimum weight bipartite matching

Given a bipartite graph *G* = (*A* ∪ *B*, *E*), the goal is to find the maximum cardinality matching in *G* that has minimum cost. Let *w*: *E* → *R* be a weight function on the edges of *E*. The minimum weight bipartite matching problem or assignment problem is to find a perfect matching *M* ⊆ *E* whose total weight is minimized. The idea is to reduce this problem to a network flow problem.

Let *G′* = (*V′* = *A* ∪ *B*, *E′* = *E*). Assign the capacity of all the edges in *E′* to 1. Add a source vertex *s* and connect it to all the vertices in *A′* and add a sink vertex *t* and connect all vertices inside group *B′* to this vertex. The capacity of all the new edges is 1 and their costs is 0. It is proved that there is minimum weight perfect bipartite matching in *G* if and only if there a minimum cost flow in *G′*.

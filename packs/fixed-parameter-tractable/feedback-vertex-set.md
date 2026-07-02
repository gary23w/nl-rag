---
title: "Feedback vertex set"
source: https://en.wikipedia.org/wiki/Feedback_vertex_set
domain: fixed-parameter-tractable
license: CC-BY-SA-4.0
tags: fixed parameter tractable, bounded search tree, iterative compression, color coding technique
fetched: 2026-07-02
---

# Feedback vertex set

In the mathematical discipline of graph theory, a **feedback vertex set** (FVS) of a graph is a set of vertices whose removal leaves a graph without cycles ("removal" means deleting the vertex and all edges adjacent to it). Equivalently, each FVS contains at least one vertex of any cycle in the graph. The **feedback vertex set number** of a graph is the size of a smallest FVS. Whether there exists a **feedback vertex set of size at most k** is an NP-complete problem; it was among the first problems shown to be NP-complete. It has wide applications in operating systems, database systems, and VLSI chip design.

## Definition

The FVS decision problem is as follows:

INSTANCE: An (undirected or directed)

graph

$G=(V,E)$

and a positive integer

k

.

QUESTION: Is there a subset

$X\subseteq V$

with

$|X|\leq k$

such that, when all vertices of

X

and their adjacent edges are deleted from

G

, the remainder is

cycle-free

?

The graph $G[V\setminus X]$ that remains after removing X from G is an induced forest (resp. an induced directed acyclic graph in the case of directed graphs). Thus, finding a minimum FVS in a graph is equivalent to finding a maximum induced forest (resp. maximum induced directed acyclic graph in the case of directed graphs).

## NP-completeness

Karp (1972) showed that finding a feedback vertex set of size $\leq k$ in *directed* graphs is NP-complete. The problem remains NP-complete on directed graphs with maximum in-degree and out-degree two, and on directed planar graphs with maximum in-degree and out-degree three.

Karp's reduction also implies the NP-completeness of the feedback vertex set problem on *undirected* graphs, where the problem stays NP-complete on graphs of maximum degree four. The feedback vertex set problem can be solved in polynomial time on graphs of maximum degree at most three, using an algorithm based on the matroid parity problem.

## Exact algorithms

The corresponding NP optimization problem of finding the size of a minimum feedback vertex set can be solved in time *O*(1.7347*n*), where *n* is the number of vertices in the graph. This algorithm actually computes a maximum induced forest, and when such a forest is obtained, its complement is a minimum feedback vertex set. The number of minimal feedback vertex sets in a graph is bounded by *O*(1.8638*n*). The directed feedback vertex set problem can still be solved in time *O**(1.9977*n*), where *n* is the number of vertices in the given directed graph. The parameterized versions of the directed and undirected problems are both fixed-parameter tractable.

In undirected graphs of maximum degree three, the feedback vertex set problem can be solved in polynomial time, by transforming it into an instance of the matroid parity problem for linear matroids.

The special case of finding all feedback vertices in a directed graph (vertices that lie on every directed cycle) can be solved in linear time using a DFS-based algorithm by Garey and Tarjan.

## Approximation

The undirected problem is APX-complete. This follows from the following facts.

- The APX-completeness of the vertex cover problem;
- The existence of an approximation preserving L-reduction from the vertex cover problem to it;
- Existing constant-factor approximation algorithms.

The best known approximation algorithm on undirected graphs is by a factor of two.

By contrast, the directed version of the problem appears to be much harder to approximate. Under the unique games conjecture, an unproven but commonly used computational hardness assumption, it is NP-hard to approximate the problem to within any constant factor in polynomial time. The same hardness result was originally proven for the closely related feedback arc set problem, but since the feedback arc set problem and feedback vertex set problem in directed graphs are reducible to one another while preserving solution sizes, it also holds for the latter.

## Bounds

According to the Erdős–Pósa theorem, the size of a minimum feedback vertex set is within a logarithmic factor of the maximum number of vertex-disjoint cycles in the given graph.

- Instead of vertices, one can consider a *feedback edge set* - a set of edges in an undirected graph, whose removal makes the graph acyclic. The size of a smallest feedback edge set in a graph is called the **circuit rank** of the graph. In contrast to the FVS number, the circuit rank can be easily computed: it is $|E|-|V|+|C|$ , where C is the set of connected components of the graph. The problem of finding a smallest feedback edge set is equivalent to finding a spanning forest, which can be done in polynomial time.
- The analogous concept in a directed graph is the **feedback arc set** (FAS) - a set of directed arcs whose removal makes the graph acyclic. Finding a smallest FAS is an NP-hard problem.

## Applications

- In operating systems, feedback vertex sets play a prominent role in the study of deadlock recovery. In the wait-for graph of an operating system, each directed cycle corresponds to a deadlock situation. In order to resolve all deadlocks, some blocked processes have to be aborted. A minimum feedback vertex set in this graph corresponds to a minimum number of processes that one needs to abort.
- The feedback vertex set problem has applications in VLSI chip design.
- Another application is in complexity theory. Some computational problems on graphs are NP-hard in general, but can be solved in polynomial time for graphs with bounded FVS number. Some examples are graph isomorphism and the path reconfiguration problem.

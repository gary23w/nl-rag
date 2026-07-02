---
title: "Multigraph"
source: https://en.wikipedia.org/wiki/Multigraph
domain: hierholzer
license: CC-BY-SA-4.0
tags: hierholzer algorithm, euler tour construction, edge traversal, closed walk
fetched: 2026-07-02
---

# Multigraph

In mathematics, and more specifically in graph theory, a **multigraph** is a graph which is permitted to have multiple edges (also called *parallel edges*), that is, edges that have the same end nodes. Thus two vertices may be connected by more than one edge.

There are 2 distinct notions of multiple edges:

- *Edges without own identity*: The identity of an edge is defined solely by the two nodes it connects. In this case, the term "multiple edges" means that the same edge can occur several times between these two nodes.
- *Edges with own identity*: Edges are primitive entities just like nodes. When multiple edges connect two nodes, these are different edges.

A multigraph is different from a hypergraph, which is a graph in which an edge can connect any number of nodes, not just two.

For some authors, the terms *pseudograph* and *multigraph* are synonymous. For others, a **pseudograph** is a multigraph that is permitted to have loops.

## Undirected multigraph (edges without own identity)

A multigraph *G* is an ordered pair *G* := (*V*, *E*) with

- *V* a set of *vertices* or *nodes*,
- *E* a multiset of unordered pairs of vertices, called *edges* or *lines*.

## Undirected multigraph (edges with own identity)

A multigraph *G* is an ordered triple *G* := (*V*, *E*, *r*) with

- *V* a set of *vertices* or *nodes*,
- *E* a set of *edges* or *lines*,
- *r* : *E* → {{*x*,*y*} : *x*, *y* ∈ *V*}, assigning to each edge an unordered pair of endpoint nodes.

Some authors allow multigraphs to have loops, that is, an edge that connects a vertex to itself, while others call these **pseudographs**, reserving the term multigraph for the case with no loops.

## Directed multigraph (edges without own identity)

A **multidigraph** is a directed graph which is permitted to have *multiple arcs,* i.e., arcs with the same source and target nodes. A multidigraph *G* is an ordered pair *G* := (*V*, *A*) with

- *V* a set of *vertices* or *nodes*,
- *A* a multiset of ordered pairs of vertices called *directed edges*, *arcs* or *arrows*.

A **mixed multigraph** *G* := (*V*, *E*, *A*) may be defined in the same way as a mixed graph.

## Directed multigraph (edges with own identity)

A multidigraph or quiver *G* is an ordered 4-tuple *G* := (*V*, *A*, *s*, *t*) with

- *V* a set of *vertices* or *nodes*,
- *A* a set of *edges* or *lines*,
- $s:A\rightarrow V$ , assigning to each edge its source node,
- $t:A\rightarrow V$ , assigning to each edge its target node.

This notion might be used to model the possible flight connections offered by an airline. In this case the multigraph would be a directed graph with pairs of directed parallel edges connecting cities to show that it is possible to fly both *to* and *from* these locations.

In category theory a small category can be defined as a multidigraph (with edges having their own identity) equipped with an associative composition law and a distinguished self-loop at each vertex serving as the left and right identity for composition. For this reason, in category theory the term *graph* is standardly taken to mean "multidigraph", and the underlying multidigraph of a category is called its **underlying digraph**.

## Labeling

Multigraphs and multidigraphs also support the notion of graph labeling, in a similar way. However, there is no unity in terminology in this case.

The definitions of **labeled multigraphs** and **labeled multidigraphs** are similar, and we define only the latter ones here.

*Definition 1*: A labeled multidigraph is a labeled graph with *labeled* arcs.

Formally: A labeled multidigraph G is a multigraph with *labeled* vertices and arcs. Formally it is an 8-tuple $G=(\Sigma _{V},\Sigma _{A},V,A,s,t,\ell _{V},\ell _{A})$ where

- V is a set of vertices and A is a set of arcs.
- $\Sigma _{V}$ and $\Sigma _{A}$ are finite alphabets of the available vertex and arc labels,
- $s\colon A\rightarrow \ V$ and $t\colon A\rightarrow \ V$ are two maps indicating the *source* and *target* vertex of an arc,
- $\ell _{V}\colon V\rightarrow \Sigma _{V}$ and $\ell _{A}\colon A\rightarrow \Sigma _{A}$ are two maps describing the labeling of the vertices and arcs.

*Definition 2*: A labeled multidigraph is a labeled graph with multiple *labeled* arcs, i.e. arcs with the same end vertices and the same arc label (note that this notion of a labeled graph is different from the notion given by the article graph labeling).

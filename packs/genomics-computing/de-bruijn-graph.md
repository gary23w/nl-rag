---
title: "De Bruijn graph"
source: https://en.wikipedia.org/wiki/De_Bruijn_graph
domain: genomics-computing
license: CC-BY-SA-4.0
tags: genomics computing, dna sequencing, genome assembly, de bruijn graph
fetched: 2026-07-02
---

# De Bruijn graph

In graph theory, an n-dimensional **De Bruijn graph** of m symbols is a directed graph representing overlaps between sequences of symbols. It has mn vertices, consisting of all possible length-n sequences of the given symbols; the same symbol may appear multiple times in a sequence. For a set of m symbols *S* = {*s*1, …, *s**m*}, the set of vertices is:

$V=S^{n}=\{(s_{1},\dots ,s_{1},s_{1}),(s_{1},\dots ,s_{1},s_{2}),\dots ,(s_{1},\dots ,s_{1},s_{m}),(s_{1},\dots ,s_{2},s_{1}),\dots ,(s_{m},\dots ,s_{m},s_{m})\}.$

If one of the vertices can be expressed as another vertex by shifting all its symbols by one place to the left and adding a new symbol at the end of this vertex, then the latter has a directed edge to the former vertex. Thus the set of arcs (that is, directed edges) is

$E=\{((t_{1},t_{2},\dots ,t_{n}),(t_{2},\dots ,t_{n},s_{j})):t_{i}\in S,1\leq i\leq n,1\leq j\leq m\}.$

Although De Bruijn graphs are named after Nicolaas Govert de Bruijn, they were invented independently by both de Bruijn and I. J. Good. Much earlier, Camille Flye Sainte-Marie implicitly used their properties.

## Properties

- If *n* = 1, then the condition for any two vertices forming an edge holds vacuously, and hence all the vertices are connected, forming a total of *m*2 edges.
- Each vertex has exactly m incoming and m outgoing edges.
- Each n-dimensional De Bruijn graph is the line digraph of the (*n* − 1)-dimensional De Bruijn graph with the same set of symbols.
- Each De Bruijn graph is Eulerian and Hamiltonian. The Euler cycles and Hamiltonian cycles of these graphs (equivalent to each other via the line graph construction) are De Bruijn sequences.

The line graph construction of the three smallest binary De Bruijn graphs is depicted below. As can be seen in the illustration, each vertex of the n-dimensional De Bruijn graph corresponds to an edge of the (*n* − 1)-dimensional De Bruijn graph, and each edge in the n-dimensional De Bruijn graph corresponds to a two-edge path in the (*n* − 1)-dimensional De Bruijn graph.

## Dynamical systems

Binary De Bruijn graphs can be drawn in such a way that they resemble objects from the theory of dynamical systems, such as the Lorenz attractor:

Binary De Bruijn graph

Lorenz attractor

This analogy can be made rigorous: the n-dimensional m-symbol De Bruijn graph is a model of the Bernoulli map

$x\mapsto mx\ {\bmod {\ }}1.$

The Bernoulli map (also called the 2*x* mod 1 map for *m* = 2) is an ergodic dynamical system, which can be understood to be a single shift of a m-adic number. The trajectories of this dynamical system correspond to walks in the De Bruijn graph, where the correspondence is given by mapping each real x in the interval [0,1) to the vertex corresponding to the first n digits in the base-m representation of x. Equivalently, walks in the De Bruijn graph correspond to trajectories in a one-sided subshift of finite type.

Embeddings resembling this one can be used to show that the binary De Bruijn graphs have queue number 2 and that they have book thickness at most 5.

## Uses

- Some grid network topologies are De Bruijn graphs.
- The distributed hash table protocol Koorde uses a De Bruijn graph.
- In bioinformatics, De Bruijn graphs are used for *de novo* assembly of sequencing reads into a genome. Instead of the complete De Bruijn graphs described above that contain all possible k-mers, de novo sequence assemblers make use of De Bruijn subgraphs that contain only the k-mers observed in a sequencing dataset.
- In time series forecasting, De Bruijn graphs have been adapted to encode temporal patterns by mapping discrete subsequences (n-grams) of observations to graph nodes. This enables the modeling of sequential dependencies in symbolic or discretized time series data. Multivariate De Bruijn graphs extend this idea by jointly encoding patterns across multiple correlated variables, allowing for the representation of complex inter-variable temporal dynamics in multivariate time series.

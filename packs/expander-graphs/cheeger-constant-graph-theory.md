---
title: "Cheeger constant (graph theory)"
source: https://en.wikipedia.org/wiki/Cheeger_constant_(graph_theory)
domain: expander-graphs
license: CC-BY-SA-4.0
tags: expander graph, spectral gap, cheeger inequality, ramanujan graph
fetched: 2026-07-02
---

# Cheeger constant (graph theory)

In mathematics, the **Cheeger constant** (also **Cheeger number** or **isoperimetric number**) of a graph is a numerical measure of whether or not a graph has a "bottleneck". The Cheeger constant as a measure of "bottleneckedness" is of great interest in many areas: for example, constructing well-connected networks of computers, card shuffling. The graph theoretical notion originated after the Cheeger isoperimetric constant of a compact Riemannian manifold.

The Cheeger constant is named after the mathematician Jeff Cheeger.

## Definition

Let G be an undirected finite graph with vertex set *V*(*G*) and edge set *E*(*G*). For a collection of vertices *A* ⊆ *V*(*G*), let ∂*A* denote the collection of all edges going from a vertex in A to a vertex outside of A (sometimes called the *edge boundary* of A):

${\displaystyle \partial A:=\{\{x,y\}\in E(G)\$

Note that the edges are unordered, i.e., $\{x,y\}=\{y,x\}$ . The **Cheeger constant** of G, denoted *h*(*G*), is defined by

${\displaystyle h(G):=\min \left\{{\frac {|\partial A|}{|A|}}\$

The Cheeger constant is strictly positive if and only if G is a connected graph. Intuitively, if the Cheeger constant is small but positive, then there exists a "bottleneck", in the sense that there are two "large" sets of vertices with "few" links (edges) between them. The Cheeger constant is "large" if any possible division of the vertex set into two subsets has "many" links between those two subsets.

## Example: computer networking

In applications to theoretical computer science, one wishes to devise network configurations for which the Cheeger constant is high (at least, bounded away from zero) even when |*V*(*G*)| (the number of computers in the network) is large.

For example, consider a ring network of *N* ≥ 3 computers, thought of as a graph GN. Number the computers 1, 2, ..., *N* clockwise around the ring. Mathematically, the vertex set and the edge set are given by:

${\begin{aligned}V(G_{N})&=\{1,2,\cdots ,N-1,N\}\\E(G_{N})&={\big \{}\{1,2\},\{2,3\},\cdots ,\{N-1,N\},\{N,1\}{\big \}}\end{aligned}}$

Take A to be a collection of $\left\lfloor {\tfrac {N}{2}}\right\rfloor$ of these computers in a connected chain:

$A=\left\{1,2,\cdots ,\left\lfloor {\tfrac {N}{2}}\right\rfloor \right\}.$

So,

$\partial A=\left\{\left\{\left\lfloor {\tfrac {N}{2}}\right\rfloor ,\left\lfloor {\tfrac {N}{2}}\right\rfloor +1\right\},\{N,1\}\right\},$

and

${\frac {|\partial A|}{|A|}}={\frac {2}{\left\lfloor {\tfrac {N}{2}}\right\rfloor }}\to 0{\mbox{ as }}N\to \infty .$

This example provides an upper bound for the Cheeger constant *h*(*GN*), which also tends to zero as *N* → ∞. Consequently, we would regard a ring network as highly "bottlenecked" for large N, and this is highly undesirable in practical terms. We would only need one of the computers on the ring to fail, and network performance would be greatly reduced. If two non-adjacent computers were to fail, the network would split into two disconnected components.

## Cheeger inequalities

The Cheeger constant is especially important in the context of expander graphs as it is a way to measure the edge expansion of a graph. The so-called Cheeger inequalities relate the eigenvalue gap of a graph with its Cheeger constant. More explicitly, for $G\neq K_{1},K_{2},K_{3}$ , we have

$2h(G)\geq \lambda \geq {\frac {h^{2}(G)}{2\Delta (G)}}$

in which $\Delta (G)$ is the maximum degree for the nodes in G and $\lambda$ is the spectral gap of the Laplacian matrix of the graph. The Cheeger inequality is a fundamental result and motivation for spectral graph theory.

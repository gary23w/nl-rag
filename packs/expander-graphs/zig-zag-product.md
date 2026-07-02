---
title: "Zig-zag product"
source: https://en.wikipedia.org/wiki/Zig-zag_product
domain: expander-graphs
license: CC-BY-SA-4.0
tags: expander graph, spectral gap, cheeger inequality, ramanujan graph
fetched: 2026-07-02
---

# Zig-zag product

In graph theory, the **zig-zag product** of regular graphs $G,H$ , denoted by $G\circ H$ , is a binary operation which takes a large graph ( G ) and a small graph ( H ) and produces a graph that approximately inherits the size of the large one but the degree of the small one. An important property of the zig-zag product is that if H is a good expander, then the expansion of the resulting graph is only slightly worse than the expansion of G .

Roughly speaking, the zig-zag product $G\circ H$ replaces each vertex of G with a copy (cloud) of H , and connects the vertices by moving a small step (zig) inside a cloud, followed by a big step (zag) between two clouds, and finally performs another small step inside the destination cloud. More specifically, the start and endpoints for each edge are at the beginning and end of this "zig-zag-zig" process starting at the points in the replacement product of the two graphs.

The zigzag product was introduced by Reingold, Vadhan & Wigderson (2000). When the zig-zag product was first introduced, it was used for the explicit construction of constant degree expanders and extractors. Later on, the zig-zag product was used in computational complexity theory to prove that symmetric logspace and logspace are equal (Reingold 2008).

## Definition

Let G be a D -regular graph on $[N]$ with rotation map $\mathrm {Rot} _{G}$ and let H be a d -regular graph on $[D]$ with rotation map $\mathrm {Rot} _{H}$ . The zig-zag product $G\circ H$ is defined to be the $d^{2}$ -regular graph on $[N]\times [D]$ whose rotation map $\mathrm {Rot} _{G\circ H}$ is as follows: $\mathrm {Rot} _{G\circ H}((v,a),(i,j))$ :

1. Let $(a',i')=\mathrm {Rot} _{H}(a,i)$ .
2. Let $(w,b')=\mathrm {Rot} _{G}(v,a')$ .
3. Let $(b,j')=\mathrm {Rot} _{H}(b',j)$ .
4. Output $((w,b),(j',i'))$ .

## Properties

### Reduction of the degree

It is immediate from the definition of the zigzag product that it transforms a graph G to a new graph which is $d^{2}$ -regular. Thus if G is a significantly larger than H , the zigzag product will reduce the degree of G . Roughly speaking, by amplifying each vertex of G into a cloud of the size of H the product in fact splits the edges of each original vertex between the vertices of the cloud that replace it.

### Spectral gap preservation

The expansion of a graph can be measured by its spectral gap, with an important property of the zigzag product the preservation of the spectral gap. That is, if H is a “good enough” expander (has a large spectral gap) then the expansion of the zigzag product is close to the original expansion of G .

Formally: Define a $(N,D,\lambda )$ -graph as any D -regular graph on N vertices, whose second largest eigenvalue (of the associated random walk) has absolute value at most $\lambda$ .

Let $G_{1}$ be a $(N_{1},D_{1},\lambda _{1})$ -graph and $G_{2}$ be a $(D_{1},D_{2},\lambda _{2})$ -graph, then $G_{1}\circ G_{2}$ is a $(N_{1}\cdot D_{1},D_{2}^{2},f(\lambda _{1},\lambda _{2}))$ -graph, where $f(\lambda _{1},\lambda _{2})<\lambda _{1}+\lambda _{2}+\lambda _{2}^{2}$ .

### Connectivity preservation

The zigzag product $G\circ H$ operates separately on each connected component of G .

Formally speaking, given two graphs: G , a D -regular graph on $[N]$ and H , a d -regular graph on $[D]$ - if $S\subseteq [N]$ is a connected component of G then $G|_{S}\circ H=G\circ H|_{S\times D}$ , where $G|_{S}$ is the subgraph of G induced by S (i.e., the graph on S which contains all of the edges in G between vertices in S ).

## Applications

### Construction of constant degree expanders

In 2002 Omer Reingold, Salil Vadhan, and Avi Wigderson gave a simple, explicit combinatorial construction of constant-degree expander graphs. The construction is iterative, and needs as a basic building block a single, expander of constant size. In each iteration the zigzag product is used in order to generate another graph whose size is increased but its degree and expansion remains unchanged. This process continues, yielding arbitrarily large expanders.

From the properties of the zigzag product mentioned above, we see that the product of a large graph with a small graph, inherits a size similar to the large graph, and degree similar to the small graph, while preserving its expansion properties from both, thus enabling to increase the size of the expander without deleterious effects.

### Solving the undirected s-t connectivity problem in logarithmic space

In 2005 Omer Reingold introduced an algorithm that solves the undirected st-connectivity problem, the problem of testing whether there is a path between two given vertices in an undirected graph, using only logarithmic space. The algorithm relies heavily on the zigzag product.

Roughly speaking, in order to solve the undirected s-t connectivity problem in logarithmic space, the input graph is transformed, using a combination of powering and the zigzag product, into a constant-degree regular graph with a logarithmic diameter. The power product increases the expansion (hence reduces the diameter) at the price of increasing the degree, and the zigzag product is used to reduce the degree while preserving the expansion.

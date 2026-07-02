---
title: "Circular layout"
source: https://en.wikipedia.org/wiki/Circular_layout
domain: chord-diagrams
license: CC-BY-SA-4.0
tags: chord diagram, circos plot, circular layout, relationship matrix
fetched: 2026-07-02
---

# Circular layout

In graph drawing, a **circular layout** is a style of drawing that places the vertices of a graph on a circle, often evenly spaced so that they form the vertices of a regular polygon.

## Applications

Circular layouts are a good fit for communications network topologies such as star or ring networks, and for the cyclic parts of metabolic networks. For graphs with a known Hamiltonian cycle, a circular layout allows the cycle to be depicted as the circle, and in this way circular layouts form the basis of the LCF notation for Hamiltonian cubic graphs.

A circular layout may be used on its own for an entire graph drawing, but it also may be used as the layout for smaller clusters of vertices within a larger graph drawing, such as its biconnected components, clusters of genes in a gene interaction graph, or natural subgroups within a social network. If multiple vertex circles are used in this way, other methods such as force-directed graph drawing may be used to arrange the clusters.

One advantage of a circular layout in some of these applications, such as bioinformatics or social network visualization, is its neutrality: by placing all vertices at equal distances from each other and from the center of the drawing, none is given a privileged position, countering the tendency of viewers to perceive more centrally located nodes as being more important.

## Edge style

The edges of the drawing may be depicted as chords of the circle, as circular arcs (possibly perpendicular to the vertex circle, so that the edges model lines of the Poincaré disk model of hyperbolic geometry), or as other types of curve.

The visual distinction between the inside and the outside of the vertex circle in a circular layout may be used to separate two different styles of edge drawing. For instance, a circular drawing algorithm of Gansner & Koren (2007) uses edge bundling within the circle, together with some edges that are not bundled, drawn outside the circle.

For circular layouts of regular graphs, with edges drawn both inside and outside as circular arcs, the angle of incidence of one of these arcs with the vertex circle is the same at both ends of the arc, a property that simplifies the optimization of the angular resolution of the drawing.

## Number of crossings

Several authors have studied the problem of finding a permutation of the vertices of a circular layout that minimizes the number of edge crossings when all edges are drawn inside the vertex circle. This number of crossings is zero only for outerplanar graphs. For other graphs, it may be optimized or reduced separately for each biconnected component of the graph before combining the solutions, as these components may be drawn so that they do not interact. In general, minimizing the number of crossings is NP-complete.

Shahrokhi et al. (1995) described an approximation algorithm based on balanced cuts or edge separators, subsets of few edges whose removal disconnects the given graph into two subgraphs with approximately equal numbers of vertices. After finding an approximate cut, their algorithm arranges the two subgraphs on each side of the cut recursively, without considering the additional crossings formed by the edges that cross the cut. They prove that the number of crossings occurring in the resulting layout, on a graph G with n vertices, is $O{\Bigl (}{\bigl (}\rho \log n{\bigr )}^{2}\cdot {\bigl (}C+\sum _{v\in V(G)}\deg(v)^{2}{\bigr )}{\Bigr )},$ where C is the optimal number of crossings and $\rho$ is the approximation ratio of the balanced cut algorithm used by this layout method. Their work cites a paper by Fan Chung and Shing-Tung Yau from 1994 that claimed $\rho =O(1)$ , but this was later found to have an erroneous proof. Instead, the best approximation known for the balanced cut problem has $\rho =O({\sqrt {\log n}})$ , giving this circular layout algorithm an approximation ratio of $O(\log ^{3}n)$ on graphs that have a large number of crossings relative to their vertex degrees.

Heuristic methods for reducing the crossing complexity have also been devised, based e.g. on a careful vertex insertion order and on local optimization. A circular layout may also be used to maximize the number of crossings. In particular, choosing a random permutation for the vertices causes each possible crossing to occur with probability 1/3, so the expected number of crossings is within a factor of three of the maximum number of crossings among all possible layouts. Derandomizing this method gives a deterministic approximation algorithm with approximation ratio three.

## Other optimization criteria

Along with crossings, circular versions of problems of optimizing the lengths of edges in a circular layout, the angular resolution of the crossings, or the cutwidth (the maximum number of edges that connects one arc of the circle to the opposite arc) have also been considered, but many of these problems are NP-complete.

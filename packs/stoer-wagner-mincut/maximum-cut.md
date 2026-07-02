---
title: "Maximum cut"
source: https://en.wikipedia.org/wiki/Maximum_cut
domain: stoer-wagner-mincut
license: CC-BY-SA-4.0
tags: stoer wagner algorithm, global minimum cut, maximum adjacency ordering, undirected mincut
fetched: 2026-07-02
---

# Maximum cut

In a graph, a **maximum cut** is a cut whose size is at least the size of any other cut. That is, it is a partition of the graph's vertices into two complementary sets S and T, such that the number of edges between S and T is as large as possible. Finding such a cut is known as the **max-cut problem**.

The problem can be stated simply as follows. One wants a subset S of the vertex set such that the number of edges between S and the complementary subset is as large as possible. Equivalently, one wants a bipartite subgraph of the graph with as many edges as possible.

There is a more general version of the problem called **weighted max-cut**, where each edge is associated with a real number, its weight, and the objective is to maximize the total weight of the edges between S and its complement rather than the number of the edges. The weighted max-cut problem allowing both positive and negative weights can be trivially transformed into a weighted minimum cut problem by flipping the sign in all weights.

## Lower bounds

Edwards obtained the following two lower bounds for maximum cuts on a graph G with n vertices and m edges:

- For arbitrary graphs, the maximum cut is at least $\displaystyle \left\lceil {\frac {m}{2}}+{\sqrt {{\frac {m}{8}}+{\frac {1}{64}}}}-{\frac {1}{8}}\right\rceil .$
- For connected graphs, it is at least $\displaystyle {\frac {m}{2}}+{\frac {n-1}{4}}.$

The bound for connected graphs is often called the Edwards–Erdős bound as Erdős conjectured it. Edwards proved the Edwards-Erdős bound using the probabilistic method; Crowston et al. proved the bound using linear algebra and analysis of pseudo-boolean functions.

The Edwards-Erdős bound extends to the **Balanced Subgraph Problem** (**BSP**) on signed graphs *G* = (*V*, *E*, *s*), i.e. graphs where each edge is assigned + or –. For a partition of V into subsets U and W, an edge xy is balanced if either *s*(*xy*) = + and x and y are in the same subset, or *s*(*xy*) = – and x and y are different subsets. BSP aims at finding a partition with the maximum number *b*(*G*) of balanced edges in G. The Edwards-Erdős gives a lower bound on *b*(*G*) for every connected signed graph G. Edwards's bound for arbitrary graphs was improved for special classes of graphs: triangle-free graphs, graphs of given maximum degree, H-free graphs, etc.

Poljak and Turzik extended the Edwards-Erdős bound to weighted maximum cuts: the weight of a maximum cut is at least ${\frac {w(G)}{2}}+{\frac {w(T_{min})}{4}},$ where *w*(*G*) and *w*(*T*min) are the weights of G and its minimum weight spanning tree *T*min. Gutin and Yeo obtained a number of lower bounds for weighted Max-Cut extending the Poljak-Turzik bound for arbitrary weighted graphs and bounds for special classes of weighted graphs.

## Computational complexity

The following decision problem related to maximum cuts has been studied widely in theoretical computer science:

Given a graph

G

and an integer

k

, determine whether there is a cut of size at least

k

in

G

.

This problem is known to be NP-complete. It is easy to see that the problem is in NP: a *yes* answer is easy to prove by presenting a large enough cut. The NP-completeness of the problem can be shown, for example, by a reduction from maximum 2-satisfiability (a restriction of the maximum satisfiability problem). The weighted version of the decision problem was one of Karp's 21 NP-complete problems; Karp showed the NP-completeness by a reduction from the partition problem.

The canonical optimization variant of the above decision problem is usually known as the *Maximum-Cut Problem* or *Max-Cut* and is defined as:

Given a graph

G

, find a maximum cut.

The optimization variant is known to be NP-Hard. The opposite problem, that of finding a minimum cut is known to be efficiently solvable via the Ford–Fulkerson algorithm.

## Algorithms

### Polynomial-time algorithms

As the maximum cut problem is NP-hard, no polynomial-time algorithms for Max-Cut in general graphs are known.

However, in planar graphs, the maximum cut problem is dual to the route inspection problem (the problem of finding a shortest tour that visits each edge of a graph at least once), in the sense that the edges that do not belong to a maximum cut-set of a graph *G* are the duals of the edges that are doubled in an optimal inspection tour of the dual graph of *G*. The optimal inspection tour forms a self-intersecting curve that separates the plane into two subsets, the subset of points for which the winding number of the curve is even and the subset for which the winding number is odd; these two subsets form a cut that includes all of the edges whose duals appear an odd number of times in the tour. The route inspection problem may be solved in polynomial time, and this duality allows the maximum cut problem to also be solved in polynomial time for planar graphs. The Maximum-Bisection problem is known however to be NP-hard.

More generally, whenever maximum cuts can be found in polynomial time for certain classes of graphs, the algorithms for this problem can be extended to the 2- and 3-clique-sums of graphs in these classes. This allows the planar graph algorithm to be extended to certain broader families of graphs closed under graph minors and having the structure of clique-sums of planar graphs and graphs of bounded size. A minor-closed family of graphs has this clique-sum structure exactly when its forbidden minors include a graph with crossing number at most one.

### Approximation algorithms

The Max-Cut Problem is APX-hard, meaning that there is no polynomial-time approximation scheme (PTAS), arbitrarily close to the optimal solution, for it, unless P = NP. Thus, every known polynomial-time approximation algorithm achieves an approximation ratio strictly less than one.

There is a simple randomized 0.5-approximation algorithm: for each vertex flip a coin to decide to which half of the partition to assign it. In expectation, half of the edges are cut edges. This algorithm can be derandomized with the method of conditional probabilities; therefore there is a simple deterministic polynomial-time 0.5-approximation algorithm as well. One such algorithm starts with an arbitrary partition of the vertices of the given graph $G=(V,E)$ and repeatedly moves one vertex at a time from one side of the partition to the other, improving the solution at each step, until no more improvements of this type can be made. The number of iterations is at most $|E|$ because the algorithm improves the cut by at least one edge at each step. When the algorithm terminates, at least half of the edges incident to every vertex belong to the cut, for otherwise moving the vertex would improve the cut. Therefore, the cut includes at least $|E|/2$ edges.

The polynomial-time approximation algorithm for Max-Cut with the best known approximation ratio is a method by Goemans and Williamson using a semidefinite program (which can be derived from the first level of the sum of squares hierarchy) and randomized rounding. It achieves an approximation ratio $\alpha \approx 0.878,$ where

$\displaystyle \alpha ={\frac {2}{\pi }}\min _{0\leq \theta \leq \pi }{\frac {\theta }{1-\cos \theta }}.$

If the unique games conjecture is true, this is the best possible approximation ratio for maximum cut. Without such unproven assumptions, it has been proven to be NP-hard to approximate the max-cut value with an approximation ratio better than ${\tfrac {16}{17}}\approx 0.941$ .

Dunning et al. provide an extended analysis of 10 heuristics for this problem, including open-source implementation.

### Parameterized algorithms and kernelization

While it is trivial to prove that the problem of finding a cut of size at least (the parameter) *k* is fixed-parameter tractable (FPT), it is much harder to show fixed-parameter tractability for the problem of deciding whether a graph *G* has a cut of size at least the Edwards-Erdős lower bound (see Lower bounds above) plus (the parameter) *k*. Crowston et al. proved that the problem can be solved in time $8^{k}O(n^{4})$ and admits a kernel of size $O(k^{5})$ . They also extended the fixed-parameter tractability result to the Balanced Subgraph Problem (BSP, see Lower bounds above) and improved the kernel size to $O(k^{3})$ (holds also for BSP). Etscheid and Mnich improved the fixed-parameter tractability result for BSP to $8^{k}O(m)$ and the kernel-size result to $O(k)$ vertices.

Weighted maximum cuts can be found in polynomial time in graphs of bounded treewidth. That is, when parameterized by treewidth rather than by the cut size, the weighted maximum cut problem is fixed-parameter tractable. It remains fixed-parameter tractable for sm-width, another graph width parameter intermediate between treewidth and clique-width. However, under standard assumptions in parameterized complexity, it is not fixed-parameter tractable for clique-width.

## Applications

### Machine learning

Treating its nodes as features and its edges as distances, the max cut algorithm divides a graph in two well-separated subsets. In other words, it can be naturally applied to perform binary classification. Compared to more common classification algorithms, it does not require a feature space, only the distances between elements within.

### Theoretical physics

In statistical physics and disordered systems, the Max Cut problem is equivalent to minimizing the Hamiltonian of a spin glass model, most simply the Ising model. For the Ising model on a graph G and only nearest-neighbor interactions, the Hamiltonian is $H[s]=-\sum _{ij\in E(G)}J_{ij}s_{i}s_{j}.$

Here each vertex *i* of the graph is a spin site that can take a spin value $s_{i}=\pm 1.$ A spin configuration partitions $V(G)$ into two sets, those with spin up $V^{+}$ and those with spin down $V^{-}.$ We denote with $\delta (V^{+})$ the set of edges that connect the two sets. We can then rewrite the Hamiltonian as ${\begin{aligned}H[s]&=-\sum _{ij\in E(V^{+})}J_{ij}-\sum _{ij\in E(V^{-})}J_{ij}+\sum _{ij\in \delta (V^{+})}J_{ij}\\&=-\sum _{ij\in E(G)}J_{ij}+2\sum _{ij\in \delta (V^{+})}J_{ij}\\&=C+2\sum _{ij\in \delta (V^{+})}J_{ij}.\end{aligned}}$

Minimizing this energy is equivalent to the min-cut problem or by setting the graph weights as $w_{ij}=-J_{ij},$ the max-cut problem.

### Circuit design

The max cut problem has applications in VLSI design.

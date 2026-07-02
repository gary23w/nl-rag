---
title: "Planted clique"
source: https://en.wikipedia.org/wiki/Planted_clique
domain: average-case-complexity
license: CC-BY-SA-4.0
tags: average case complexity, distributional problem, planted clique problem, smoothed analysis
fetched: 2026-07-02
---

# Planted clique

In computational complexity theory, a **planted clique** or **hidden clique** in an undirected graph is a clique formed from another graph by selecting a subset of vertices and adding edges between each pair of vertices in the subset. The **planted clique problem** is the algorithmic problem of distinguishing random graphs from graphs that have a planted clique. This is a variation of the clique problem; it may be solved in quasi-polynomial time but is conjectured not to be solvable in polynomial time for intermediate values of the clique size. The conjecture that no polynomial time solution exists is called the **planted clique conjecture**; it has been used as a computational hardness assumption.

## Definition

A clique in a graph is a subset of vertices, all of which are adjacent to each other. A planted clique is a clique created from another graph by adding edges between all pairs of a selected subset of vertices.

The planted clique problem can be formalized as a decision problem over a random distribution on graphs, parameterized by two numbers, n (the number of vertices), and k (the size of the clique). These parameters may be used to generate a graph, by the following random process:

1. Create an Erdős–Rényi random graph on n vertices by choosing independently for each pair of vertices whether to include an edge connecting that pair, with probability 1/2 for each pair.
2. Decide whether or not to add a clique to the graph, with probability 1/2; if not, return the graph formed in step 1.
3. Choose randomly a subset of k of the n vertices and add an edge (if one is not already present) between each pair of the selected vertices.

The problem is then to determine algorithmically whether one of the graphs resulting from this process contains a clique of at least k vertices.

### Upper and lower bounds

There exists a function $f(n)\sim 2\log _{2}n$ such that asymptotically almost surely, the size of the largest clique in an n-vertex random graph is either $f(n)$ or $f(n)+1$ , and there exists some constant c such that the expected number of cliques of size $\geq f(n)-c$ converges to infinity. Consequently, one should expect that the planting a clique of size $\sim 2\log _{2}n$ cannot be detected with high probability.

By the central limit theorem, the vertex degrees of the random graph would be distributed close to a standard normal distribution with mean ${\frac {n}{2}}$ and standard deviation ${\frac {\sqrt {n}}{2}}$ . Consequently, when k is on the order of ${\sqrt {n}}$ it would create a detectable change in the shape of the distribution. Namely, if you plot out the vertex degree distribution, it would look like a deformed bell curve. Therefore, the most interesting range of values for the parameter k is between these two values,

$2\log _{2}n\ll k\ll {\sqrt {n}}.$

## Algorithms

### Large cliques

For sufficiently large values of the parameter k, the planted clique problem can be solved (with high probability) in polynomial time.

Kučera (1995) observes that, when $k=\Omega ({\sqrt {n\log n}})$ then almost surely all vertices of the planted clique have higher degree than all vertices outside the clique, making the clique very easy to find. He describes a modification to the random process for generating planted clique instances, that makes the vertex degrees more uniform even for large values of k, but shows that despite this modification the planted clique may still be found quickly.

Alon, Krivelevich & Sudakov (1998) prove for $k>10{\sqrt {n}}$ a planted clique can be found with high probability by the following method:

1. Compute the eigenvector of the adjacency matrix corresponding to its second highest eigenvalue.
2. Select the k vertices whose coordinates in this eigenvector have the largest absolute values.
3. Return the set of vertices that are adjacent to at least 3/4 of the selected vertices.

They show how to modify this technique so that it continues to work whenever k is at least proportional to some multiple of the square root of the number of vertices. Large planted cliques can also be found using semidefinite programming. A combinatorial technique based on randomly sampling vertices can achieve the same bound on k and runs in linear time.

### Quasipolynomial time

It is also possible to solve the planted clique problem, regardless of the choice of k, in quasi-polynomial time. Because the largest clique in a random graph typically has size near 2 log2 *n*, a planted clique of size k (if it exists) can be found with high probability by the following method:

1. Loop through all sets S of $\min(k,3\log _{2}n)$ vertices.
2. For each choice of S, test whether S is a clique. If it is, and $|S|=k$ , return S. Otherwise, find the set T of vertices that are adjacent to all vertices in S. If $|T|\geq k$ , return T.

The running time of this algorithm is quasipolynomial, because there are quasipolynomially many choices of S to loop over. This method is guaranteed to try a set S that is a subset of the planted clique; with high probability, the set T will consist only of other members of the planted clique.

## As a hardness assumption

There are two versions of the planted clique conjecture: one based on finding the clique (search) and one based on determining if a clique exists (decision). The search conjecture states that no polynomial time algorithm can find (with high probability) a clique of size k << $n^{0.5}$ in a random graph with n nodes and a hidden clique of size k .

The decision conjecture is more subtle. Suppose we are given two n node random graphs, exactly one of which has a planted clique, but we don't know which. On average, a random graph with a planted clique will have more edges than a purely random graph, since the act of planting a clique of size k is expected to add $\Theta (k^{2})$ edges. Therefore, we can correctly determine which of the two graphs contains the planted clique with probability $1/2+\Theta (k^{2}/n)$ by simply counting the number of edges in each graph. The decision planted clique conjecture states that this is essentially optimal: it postulates that no polynomial time algorithm can distinguish between the two graphs with probability higher than $1/2+\Theta (k^{2}/n)$ .

Hazan & Krauthgamer (2011) used the assumption that finding planted cliques is hard as a computational hardness assumption to prove that, if so, it is also hard to approximate the best Nash equilibrium in a two-player game. The planted clique conjecture has also been used as a hardness assumption to show the difficulty of property testing k-independence of random distributions, finding clusters in social networks, and machine learning.

---
title: "Eigenvector centrality"
source: https://en.wikipedia.org/wiki/Eigenvector_centrality
domain: pagerank-algorithm
license: CC-BY-SA-4.0
tags: pagerank algorithm, link analysis, power iteration, markov chain
fetched: 2026-07-02
---

# Eigenvector centrality

In graph theory, **eigenvector centrality** (also called **eigencentrality** or **prestige score**) is a measure of the influence of a node in a connected network. Relative scores are assigned to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes. A high eigenvector score means that a node is connected to many nodes who themselves have high scores.

Google's PageRank and the Katz centrality are variants of the eigenvector centrality.

## Using the adjacency matrix to find eigenvector centrality

For a given graph $G:=(V,E)$ with $|V|$ vertices let $A=(a_{v,t})$ be the adjacency matrix, i.e. $a_{v,t}=1$ if vertex v is linked to vertex t , and $a_{v,t}=0$ otherwise. The relative centrality score, $x_{v}$ , of vertex v can be defined as:

$x_{v}={\frac {1}{\lambda }}\sum _{t\in M(v)}x_{t}={\frac {1}{\lambda }}\sum _{t\in V}a_{v,t}x_{t}$

where $M(v)$ is the set of neighbors of v and $\lambda$ is a constant. With a small rearrangement this can be rewritten in vector notation as the eigenvector equation

$\mathbf {Ax} =\lambda \mathbf {x}$

In general, there will be many different eigenvalues $\lambda$ for which a non-zero eigenvector solution exists. However, the connectedness assumption and the additional requirement that all the entries in the eigenvector be non-negative imply (by the Perron–Frobenius theorem) that only the greatest eigenvalue results in the desired centrality measure. The $v^{\text{th}}$ component of the related eigenvector then gives the relative centrality score of the vertex v in the network. The eigenvector is only defined up to a common factor, so only the ratios of the centralities of the vertices are well defined. To define an absolute score, one must normalise the eigenvector e.g. such that the sum over all vertices is 1 or the total number of vertices *n*. Power iteration is one of many eigenvalue algorithms that may be used to find this dominant eigenvector. Furthermore, this can be generalized so that the entries in *A* can be real numbers representing connection strengths, as in a stochastic matrix.

## Normalized eigenvector centrality scoring

Google's PageRank is based on the normalized eigenvector centrality, or normalized prestige, combined with a random jump assumption. The PageRank of a node v has recursive dependence on the PageRank of other nodes that point to it. The normalized adjacency matrix *N* is defined as: $N(u,v)={\begin{cases}{1 \over \operatorname {od} (u)},&{\text{if }}(u,v)\in E\\0,&{\text{if }}(u,v)\not \in E\end{cases}}$ where $od(u)$ is the out-degree of node u , or in vector form:

$\mathbf {N} =\mathbf {diag} (\mathbf {Ae} )^{-1}\mathbf {A}$

,

where $\mathbf {e}$ is the vector of ones, and $\mathbf {diag} (\mathbf {x} )$ is the diagonal matrix of vector $\mathbf {x}$ . $\mathbf {N}$ is a row-stochastic matrix.

The normalized eigenvector prestige score is defined as:

$p(v)=\sum _{u}{N^{T}(v,u)\cdot p(u)},$

or in vector form,

$\mathbf {p} =\mathbf {N} ^{T}\mathbf {p} .$

## Applications

Eigenvector centrality is a measure of the influence a node has on a network. If a node is pointed to by many nodes (which also have high eigenvector centrality) then that node will have high eigenvector centrality.

The earliest use of eigenvector centrality is by Edmund Landau in an 1895 paper on scoring chess tournaments.

More recently, researchers across many fields have analyzed applications, manifestations, and extensions of eigenvector centrality in a variety of domains:

- Eigenvector centrality is the unique measure satisfying certain natural axioms for a ranking system.
- In neuroscience, the eigenvector centrality of a neuron in a model neural network has been found to correlate with its relative firing rate.
- Eigenvector centrality and related concepts have been used to model opinion influence in sociology and economics, as in the DeGroot learning model.
- The definition of eigenvector centrality has been extended to multiplex and multilayer networks through the concept of versatility
- In a study using data from the Philippines, researchers showed how political candidates' families had disproportionately high eigenvector centrality in local intermarriage networks.
- Eigenvector centrality has been extensively applied to study economic outcomes, including cooperation in social networks. In economic public goods problems, a person's eigenvector centrality can be interpreted as how much that person's preferences influence an efficient social outcome.

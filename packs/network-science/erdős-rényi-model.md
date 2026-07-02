---
title: "Erdős–Rényi model"
source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model
domain: network-science
license: CC-BY-SA-4.0
tags: network science, scale-free network, small-world network, community structure
fetched: 2026-07-02
---

# Erdős–Rényi model

In the mathematical field of graph theory, the **Erdős–Rényi model**s are two closely related models for generating random graphs and the evolution of a random network. These models are named after Hungarian mathematicians Paul Erdős and Alfréd Rényi, who introduced one of the models in 1959. Edgar Gilbert introduced the other model contemporaneously with and independently of Erdős and Rényi. In the model of Erdős and Rényi, all graphs on a fixed vertex set with a fixed number of edges are equally likely. In the model introduced by Gilbert, also called the **Erdős–Rényi–Gilbert model**, each edge has a fixed probability of being present or absent, independently of the other edges. These models can be used in the probabilistic method to prove the existence of graphs satisfying various properties, or to provide a rigorous definition of what it means for a property to hold for almost all graphs.

## Definition

There are two closely related variants of the Erdős–Rényi random graph model.

- In the $G(n,M)$ model, a graph is chosen uniformly at random from the collection of all graphs which have n nodes and M edges. The nodes are considered to be labeled, meaning that graphs obtained from each other by permuting the vertices are considered to be distinct. For example, in the $G(3,2)$ model, there are three two-edge graphs on three labeled vertices (one for each choice of the middle vertex in a two-edge path), and each of these three graphs is included with probability ${\tfrac {1}{3}}$ .
- In the $G(n,p)$ model, a graph is constructed by connecting labeled nodes randomly. Each edge is included in the graph with probability p , independently from every other edge. Equivalently, the probability for generating each graph that has n nodes and M edges is $p^{M}(1-p)^{{n \choose 2}-M}.$ The parameter p in this model can be thought of as a weighting function; as p increases from 0 to 1 , the model becomes more and more likely to include graphs with more edges and less and less likely to include graphs with fewer edges. In particular, the case $p={\tfrac {1}{2}}$ corresponds to the case where all $2^{\binom {n}{2}}$ graphs on n vertices are chosen with equal probability.

The behavior of random graphs are often studied in the case where n , the number of vertices, tends to infinity. Although p and M can be fixed in this case, they can also be functions depending on n . For example, the statement that almost every graph in $G(n,2\ln(n)/n)$ is connected means that, as n tends to infinity, the probability that a graph on n vertices with edge probability $2\ln(n)/n$ is connected tends to 1 .

## Comparison between the two models

The expected number of edges in *G*(*n*, *p*) is ${\tbinom {n}{2}}p$ , with a standard deviation asymptotic to $s(n)=n{\sqrt {p(1-p)}}$ . Therefore, a rough heuristic is that if some property of *G*(*n*, *M*) with $M={\tbinom {n}{2}}p$ does not significantly change in behavior if *M* is changed by up to *s*(*n*), then *G*(*n*, *p*) should share that behavior.

This is formalized in a result of Łuczak. Suppose that *P* is a graph property such that for every sequence *M* = *M*(*n*) with $|M-{\tbinom {n}{2}}p|=O(s(n))$ , the probability that a graph sampled from *G*(*n*, *M*) has property *P* tends to *a* as *n* → ∞. Then the probability that *G*(*n*, *p*) has property *P* also tends to *a*.

Implications in the other direction are less reliable, but a partial converse (also shown by Łuczak) is known when *P* is monotone with respect to the subgraph ordering (meaning that if *A* is a subgraph of *B* and *B* satisfies *P*, then *A* will satisfy *P* as well). Let $\varepsilon (n)\gg s(n)/n^{3}$ , and suppose that a monotone property *P* is true of both *G*(*n*, *p* – *ε*) and *G*(*n*, *p* + *ε*) with a probability tending to the same constant *a* as *n* → ∞. Then the probability that $G(n,{\tbinom {n}{2}}p)$ has property *P* also tends to *a*.

For example, both directions of equivalency hold if *P* is the property of being connected, or if *P* is the property of containing a Hamiltonian cycle. However, properties that are not monotone (e.g. the property of having an even number of edges) or that change too rapidly (e.g. the property of having at least ${\tfrac {1}{2}}{\tbinom {n}{2}}$ edges) may behave differently in the two models.

In practice, the *G*(*n*, *p*) model is the one more commonly used today, in part due to the ease of analysis allowed by the independence of the edges.

## Properties of *G*(*n*, *p*)

With the notation above, a graph in *G*(*n*, *p*) has on average ${\tbinom {n}{2}}p$ edges. The distribution of the degree of any particular vertex is binomial:

$P(\deg(v)=k)={n-1 \choose k}p^{k}(1-p)^{n-1-k},$

where *n* is the total number of vertices in the graph. Since

$P(\deg(v)=k)\to {\frac {(np)^{k}\mathrm {e} ^{-np}}{k!}}\quad {\text{ as }}n\to \infty {\text{ and }}np={\text{constant}},$

this distribution is Poisson for large *n* and *np* = const.

In a 1960 paper, Erdős and Rényi described the behavior of *G*(*n*, *p*) very precisely for various values of *p*. Their results included that:

- If *np* < 1, then a graph in *G*(*n*, *p*) will almost surely have no connected components of size larger than O(log(*n*)).
- If *np* = 1, then a graph in *G*(*n*, *p*) will almost surely have a largest component whose size is of order *n*2/3.
- If *np* → *c* > 1, where *c* is a constant, then a graph in *G*(*n*, *p*) will almost surely have a unique giant component containing a positive fraction of the vertices. No other component will contain more than O(log(*n*)) vertices.
- If $p<{\tfrac {(1-\varepsilon )\ln n}{n}}$ , then a graph in *G*(*n*, *p*) will almost surely contain isolated vertices, and thus be disconnected.
- If $p>{\tfrac {(1+\varepsilon )\ln n}{n}}$ , then a graph in *G*(*n*, *p*) will almost surely be connected.

Thus ${\tfrac {\ln n}{n}}$ is a sharp threshold for the connectedness of *G*(*n*, *p*).

Further properties of the graph can be described almost precisely as *n* tends to infinity. For example, there is a *k*(*n*) (approximately equal to 2log2(*n*)) such that the largest clique in *G*(*n*, 0.5) has almost surely either size *k*(*n*) or *k*(*n*) + 1.

Thus, even though finding the size of the largest clique in a graph is NP-complete, the size of the largest clique in a "typical" graph (according to this model) is very well understood.

Edge-dual graphs of Erdos-Renyi graphs are graphs with nearly the same degree distribution, but with degree correlations and a significantly higher clustering coefficient.

## Relation to percolation

In percolation theory one examines a finite or infinite graph and removes edges (or links) randomly. Thus the Erdős–Rényi process is in fact unweighted link percolation on the complete graph. (One refers to percolation in which nodes and/or links are removed with heterogeneous weights as weighted percolation). As percolation theory has much of its roots in physics, much of the research done was on the lattices in Euclidean spaces. The transition at *np* = 1 from giant component to small component has analogs for these graphs, but for lattices the transition point is difficult to determine. Physicists often refer to study of the complete graph as a mean field theory. Thus the Erdős–Rényi process is the mean-field case of percolation.

Some significant work was also done on percolation on random graphs. From a physicist's point of view this would still be a mean-field model, so the justification of the research is often formulated in terms of the robustness of the graph, viewed as a communication network. Given a random graph of *n* ≫ 1 nodes with an average degree  $\langle k\rangle$ . Remove randomly a fraction $1-p'$ of nodes and leave only a fraction $p'$ from the network. There exists a critical percolation threshold $p'_{c}={\tfrac {1}{\langle k\rangle }}$ below which the network becomes fragmented while above $p'_{c}$ a giant connected component of order *n* exists. The relative size of the giant component, *P*∞, is given by

$P_{\infty }=p'[1-\exp(-\langle k\rangle P_{\infty })].\,$

## Caveats

Both of the two major assumptions of the *G*(*n*, *p*) model (that edges are independent and that each edge is equally likely) may be inappropriate for modeling certain real-life phenomena. Erdős–Rényi graphs have low clustering, unlike many social networks. Some modeling alternatives include Barabási–Albert model and Watts and Strogatz model. These alternative models are not percolation processes, but instead represent a growth and rewiring model, respectively. Another alternative family of random graph models, capable of reproducing many real-life phenomena, are exponential random graph models.

## History

The *G*(*n*, *p*) model was first introduced by Edgar Gilbert in a 1959 paper studying the connectivity threshold mentioned above. The *G*(*n*, *M*) model was introduced by Erdős and Rényi in their 1959 paper. As with Gilbert, their first investigations were as to the connectivity of *G*(*n*, *M*), with the more detailed analysis following in 1960.

## Continuum limit representation of critical *G*(*n*, *p*)

A continuum limit of the graph was obtained when p is of order $1/n$ . Specifically, consider the sequence of graphs $G_{n}:=G(n,1/n+\lambda n^{-{\frac {4}{3}}})$ for $\lambda \in \mathbb {R}$ . The limit object can be constructed as follows:

- First, generate a diffusion $W^{\lambda }(t):=W(t)+\lambda t-{\frac {t^{2}}{2}}$ where W is a standard Brownian motion.
- From this process, we define the reflected process $R^{\lambda }(t):=W^{\lambda }(t)-\inf \limits _{s\in [0,t]}W^{\lambda }(s)$ . This process can be seen as containing many successive excursion (not quite a Brownian excursion, see ). Because the drift of $W^{\lambda }$ is dominated by $-{\frac {t^{2}}{2}}$ , these excursions become shorter and shorter as $t\to +\infty$ . In particular, they can be sorted in order of decreasing lengths: we can partition $\mathbb {R}$ into intervals $(C_{i})_{i\in \mathbb {N} }$ of decreasing lengths such that $R^{\lambda }$ restricted to $C_{i}$ is a Brownian excursion for any $i\in \mathbb {N}$ .
- Now, consider an excursion $(e(s))_{s\in [0,1]}$ . Construct a random graph as follows:
  - Construct a real tree $T_{e}$ (see Brownian tree).
  - Consider a Poisson point process $\Xi$ on $[0,1]\times \mathbb {R} _{+}$ with unit intensity. To each point $(x,s)\in \Xi$ such that $x\leq e(s)$ , corresponds an underlying internal node and a leaf of the tree $T_{e}$ . Identifying the two vertices, the tree $T_{e}$ becomes a graph $\Gamma _{e}$

Applying this procedure, one obtains a sequence of random infinite graphs of decreasing sizes: $(\Gamma _{i})_{i\in \mathbb {N} }$ . The theorem states that this graph corresponds in a certain sense to the limit object of $G_{n}$ as $n\to +\infty$ .

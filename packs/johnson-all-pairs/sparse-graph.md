---
title: "Dense graph"
source: https://en.wikipedia.org/wiki/Sparse_graph
domain: johnson-all-pairs
license: CC-BY-SA-4.0
tags: johnson algorithm, all pairs shortest path, reweighting technique, sparse graph
fetched: 2026-07-02
---

# Dense graph

(Redirected from

Sparse graph

)

In mathematics, a **dense graph** is a graph in which the number of edges is close to the maximal number of edges (where every pair of vertices is connected by one edge). The opposite, a graph with only a few edges, is a **sparse graph**. The distinction of what constitutes a dense or sparse graph is ill-defined, and is often represented by 'roughly equal to' statements. Due to this, the way that density is defined often depends on the context of the problem.

## Graph density

Consider a simple graph $(V,E)$ where V is the set of vertices and E is the set of edges. We write $|V|$ to denote the number of vertices, and $|E|$ to denote the number of edges. The **graph density** of the simple graph $(V,E)$ is defined to be the ratio of the number of edges |*E*| with respect to the maximum possible edges.

For undirected simple graphs, the graph density is:

$D={\frac {|E|}{\binom {|V|}{2}}}={\frac {2|E|}{|V|(|V|-1)}}$

For directed, simple graphs, the maximum possible edges is twice that of undirected graphs (as there are two directions to an edge) so the density is:

$D={\frac {|E|}{2{\binom {|V|}{2}}}}={\frac {|E|}{|V|(|V|-1)}}$

The maximum number of edges for an undirected graph is ${\binom {|V|}{2}}={\frac {|V|(|V|-1)}{2}}$ , so the maximal density is 1 (for complete graphs) and the minimal density is 0.

For families of graphs of increasing size, one often calls them sparse if $D\rightarrow 0$ as $|V|\rightarrow \infty$ . Sometimes, in computer science, a more restrictive definition of sparse is used like $|E|=O(|V|\log |V|)$ or even $|E|=O(|V|)$ . In this same context, a dense graph may be defined as any graph where |*E*| is "close" to $|V|^{2}$ .

## Upper density

*Upper density* is an extension of the concept of graph density defined above from finite graphs to infinite graphs. Intuitively, an infinite graph has arbitrarily large finite subgraphs with any density less than its upper density, and does not have arbitrarily large finite subgraphs with density greater than its upper density. Formally, the upper density of a graph G is the infimum of the values α such that the finite subgraphs of G with density α have a bounded number of vertices. It can be shown using the Erdős–Stone theorem that the upper density can only be 1 or one of the superparticular ratios 0, ⁠1/2⁠, ⁠2/3⁠, ⁠3/4⁠, ⁠4/5⁠, … ⁠*n*/*n* + 1⁠

## Sparse and tight graphs

Lee & Streinu (2008) and Streinu & Theran (2009) define a graph as being (*k*, *l*)-sparse if every nonempty subgraph with n vertices has at most *kn* − *l* edges, and (*k*, *l*)-tight if it is (*k*, *l*)-sparse and has exactly *kn* − *l* edges. Thus trees are exactly the (1,1)-tight graphs, forests are exactly the (1,1)-sparse graphs, and graphs with arboricity k are exactly the (*k*,*k*)-sparse graphs. Pseudoforests are exactly the (1,0)-sparse graphs, and the Laman graphs arising in rigidity theory are exactly the (2,3)-tight graphs.

Other graph families not characterized by their sparsity can also be described in this way. For instance the facts that any planar graph with n vertices has at most 3*n* – 6 edges (except for graphs with fewer than 3 vertices), and that any subgraph of a planar graph is planar, together imply that the planar graphs are (3,6)-sparse. However, not every (3,6)-sparse graph is planar. Similarly, outerplanar graphs are (2,3)-sparse and planar bipartite graphs are (2,4)-sparse.

Streinu and Theran show that testing (*k*,*l*)-sparsity may be performed in polynomial time when k and l are integers and 0 ≤ *l* < 2*k*.

For a graph family, the existence of k and l such that the graphs in the family are all (*k*,*l*)-sparse is equivalent to the graphs in the family having bounded degeneracy or having bounded arboricity. More precisely, it follows from a result of Nash-Williams (1964) that the graphs of arboricity at most a are exactly the (*a*,*a*)-sparse graphs. Similarly, the graphs of degeneracy at most d are $\left(d,{\binom {d+1}{2}}\right)$ -sparse graphs.

## Sparse and dense classes of graphs

Nešetřil & Ossona de Mendez (2010) considered that the sparsity/density dichotomy makes it necessary to consider infinite graph classes instead of single graph instances. They defined *somewhere dense* graph classes as those classes of graphs for which there exists a threshold *t* such that every complete graph appears as a *t*-subdivision in a subgraph of a graph in the class. To the contrary, if such a threshold does not exist, the class is *nowhere dense*.

The classes of graphs with bounded degeneracy and of nowhere dense graphs are both included in the biclique-free graphs, graph families that exclude some complete bipartite graph as a subgraph.

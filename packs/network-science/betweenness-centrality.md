---
title: "Betweenness centrality"
source: https://en.wikipedia.org/wiki/Betweenness_centrality
domain: network-science
license: CC-BY-SA-4.0
tags: network science, scale-free network, small-world network, community structure
fetched: 2026-07-02
---

# Betweenness centrality

In graph theory, **betweenness centrality** is a measure of centrality in a graph based on shortest paths. Betweenness centrality measures how frequently a node appears on the shortest path between other nodes in the graph. For every pair of vertices in a connected graph, there exists at least one shortest path between the vertices, that is, there exists at least one path such that either the number of edges that the path passes through (for unweighted graphs) or the sum of the weights of the edges (for weighted graphs) is minimized.

Betweenness centrality was devised as a general measure of centrality:. It applies to a wide range of problems in network theory, including problems related to social networks, biology, transport, and scientific cooperation. Although earlier authors had intuitively described centrality in terms of betweenness, Freeman (1977) gave the first formal definition of betweenness centrality.

Betweenness centrality has wide application in network theory; it measures the extent to which nodes lie between one another. For example, in a telecommunications network, a node with higher betweenness centrality would have more control over the network because more information flows through it.

## Definition

The betweenness centrality of a node v is given by the expression:

$g(v)=\sum _{s\neq v\neq t}{\frac {\sigma _{st}(v)}{\sigma _{st}}}$

where $\sigma _{st}$ is the total number of shortest paths from node s to node t and $\sigma _{st}(v)$ is the number of those paths that pass through v (not where v is an end point).

The betweenness centrality of a node scales with the number of pairs of nodes as suggested by the summation indices. Therefore, the calculation may be rescaled by dividing through by the number of pairs of nodes not including v , so that $g\in [0,1]$ . The division is done by $(N-1)(N-2)$ for directed graphs and $(N-1)(N-2)/2$ for undirected graphs, where N is the number of nodes in the giant component. Note that this scales for the highest possible value, where one node is crossed by every single shortest path. This is often not the case, and a normalization can be performed without a loss of precision

${\mbox{normal}}(g(v))={\frac {g(v)-\min(g)}{\max(g)-\min(g)}}$

which results in:

$\max({\mbox{normal}})=1$

$\min({\mbox{normal}})=0$

Note that this will always be a scaling from a smaller range into a larger range, so no precision is lost.

## Weighted networks

In a weighted network the links connecting the nodes are no longer treated as binary interactions, but are weighted in proportion to their capacity, influence, frequency, etc., which adds another dimension of heterogeneity within the network beyond the topological effects. A node's strength in a weighted network is given by the sum of the weights of its adjacent edges.

$s_{i}=\sum _{j=1}^{N}a_{ij}w_{ij}$

With $a_{ij}$ and $w_{ij}$ being adjacency and weight matrices between nodes i and j , respectively. Analogous to the power law distribution of degree found in scale free networks, the strength of a given node follows a power law distribution as well.

$s(k)\approx k^{\beta }$

A study of the average value $s(b)$ of the strength for vertices with betweenness b shows that the functional behavior can be approximated by a scaling form:

$s(b)\approx b^{\alpha }$

## Percolation centrality

Percolation centrality is a version of weighted betweenness centrality, but it considers the 'state' of the source and target nodes of each shortest path in calculating this weight. Percolation of a 'contagion' occurs in complex networks in a number of scenarios. For example, viral or bacterial infection can spread over social networks of people, known as contact networks. The spread of disease can also be considered at a higher level of abstraction, by contemplating a network of towns or population centres, connected by road, rail or air links. Computer viruses can spread over computer networks. Rumours or news about business offers and deals can also spread via social networks of people. In all of these scenarios, a 'contagion' spreads over the links of a complex network, altering the 'states' of the nodes as it spreads, either recoverably or otherwise. For example, in an epidemiological scenario, individuals go from 'susceptible' to 'infected' state as the infection spreads. The states the individual nodes can take in the above examples could be binary (such as received/not received a piece of news), discrete (susceptible/infected/recovered), or even continuous (such as the proportion of infected people in a town), as the contagion spreads. The common feature in all these scenarios is that the spread of contagion results in the change of node states in networks. Percolation centrality (PC) was proposed with this in mind, which specifically measures the importance of nodes in terms of aiding the percolation through the network. This measure was proposed by Piraveenan, Prokopenko & Hossain (2013).

Percolation centrality is defined for a given node, at a given time, as the proportion of 'percolated paths' that go through that node. A 'percolated path' is a shortest path between a pair of nodes, where the source node is percolated (e.g., infected). The target node can be percolated or non-percolated, or in a partially percolated state.

$PC^{t}(v)={\frac {1}{N-2}}\sum _{s\neq v\neq r}{\frac {\sigma _{sr}(v)}{\sigma _{sr}}}{\frac {{x^{t}}_{s}}{{\sum {[{x^{t}}_{i}}]}-{x^{t}}_{v}}}$

where $\sigma _{sr}$ is total number of shortest paths from node s to node r and $\sigma _{sr}(v)$ is the number of those paths that pass through v . The percolation state of the node i at time t is denoted by ${x^{t}}_{i}$ and two special cases are when ${x^{t}}_{i}=0$ which indicates a non-percolated state at time t whereas when ${x^{t}}_{i}=1$ which indicates a fully percolated state at time t . The values in between indicate partially percolated states ( e.g., in a network of townships, this would be the percentage of people infected in that town).

The attached weights to the percolation paths depend on the percolation levels assigned to the source nodes, based on the premise that the higher the percolation level of a source node is, the more important are the paths that originate from that node. Nodes which lie on shortest paths originating from highly percolated nodes are therefore potentially more important to the percolation. The definition of PC may also be extended to include target node weights as well. Percolation centrality calculations run in $O(|V||E|)$ time with an efficient implementation adapted from Brandes' algorithm. If the calculation needs to consider target node weights, the worst case time is $O(|V|^{3})$ .

## Algorithms

Calculating the betweenness and closeness centralities of all the vertices in a graph involves calculating the shortest paths between all pairs of vertices on a graph, which takes $\Theta (|V|^{3})$ time with the Floyd–Warshall algorithm, modified to not only find one but count all shortest paths between two nodes. On a sparse graph, Johnson's algorithm or Brandes' algorithm may be more efficient, both taking $O(|V|^{2}\log |V|+|V||E|)$ time. On unweighted graphs, calculating betweenness centrality takes $O(|V||E|)$ time using Brandes' algorithm.

In calculating betweenness and closeness centralities of all vertices in a graph, it is assumed that graphs are undirected and connected with the allowance of loops and multiple edges. When specifically dealing with network graphs, often graphs are without loops or multiple edges to maintain simple relationships (where edges represent connections between two people or vertices). In this case, using Brandes' algorithm will divide final centrality scores by 2 to account for each shortest path being counted twice.

Another algorithm generalizes the Freeman's betweenness computed on geodesics and Newman's betweenness computed on all paths, by introducing a hyper-parameter controlling the trade-off between exploration and exploitation. The time complexity is the number of edges times the number of nodes in the graph.

### Approximations

Because exact computation of betweenness centrality can be expensive on large graphs, a number of approximation algorithms have been proposed. Many methods estimate betweenness by sampling shortest paths between randomly selected pairs of vertices instead of enumerating all shortest paths.

Riondato and Kornaropoulos proposed a shortest-path sampling algorithm with probabilistic error guarantees based on Vapnik–Chervonenkis theory. Later methods such as ABRA and SILVAN used progressive sampling strategies and Rademacher averages to adaptively determine the number of sampled shortest paths needed to achieve a target accuracy.

KADABRA is an adaptive approximation algorithm that combines shortest-path sampling with bidirectional breadth-first search and confidence interval estimation.

Local heuristics have also been proposed as computationally inexpensive alternatives. Ego betweenness computes the betweenness of a vertex within its ego network, consisting only of the vertex, its neighbors, and the edges among those neighbors. Other lightweight proxy measures, such as the local clustering coefficient-dependent degree centrality (LCCDC), use only local structural properties such as degree and the clustering coefficient to estimate the relative importance of vertices.

## Applications

In social network analysis, betweenness centrality can have different implications. From a macroscopic perspective, bridging positions or "structural holes" (indicated by high betweenness centrality) reflect power, because they allow the person on the bridging position to exercise control (e.g., decide whether to share information or not) over the persons it connects between. From the microscopic perspective of ego networks (i.e., only considering first-degree connections), in online social networks a high betweenness centrality coincides with nominations of closest friends (i.e., strong interpersonal ties), because it reflects social capital investments into the relationship when distant social circles (e.g., family and university) are bridged (often resulting from an introduction by ego).

### River networks

Betweenness centrality has been used to analyze the topological complexity of river networks as well as their use in maritime trade.

*Betweenness centrality* is related to a network's connectivity, in so much as high betweenness vertices have the potential to disconnect graphs if removed (see cut set).

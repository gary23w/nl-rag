---
title: "Edge disjoint shortest pair algorithm"
source: https://en.wikipedia.org/wiki/Edge_disjoint_shortest_pair_algorithm
domain: suurballe-disjoint-paths
license: CC-BY-SA-4.0
tags: suurballe algorithm, disjoint paths, edge disjoint routing, network survivability
fetched: 2026-07-02
---

# Edge disjoint shortest pair algorithm

**Edge disjoint shortest pair algorithm** is an algorithm in computer network routing. The algorithm is used for generating the shortest pair of edge disjoint paths between a given pair of vertices. For an undirected graph G(V, E), it is stated as follows:

1. Run the shortest path algorithm for the given pair of vertices
2. Replace each edge of the shortest path (equivalent to two oppositely directed arcs) by a single arc directed towards the source vertex
3. Make the length of each of the above arcs negative
4. Run the shortest path algorithm *(Note: the algorithm should accept negative costs)*
5. Erase the overlapping edges of the two paths found, and reverse the direction of the remaining arcs on the first shortest path such that each arc on it is directed towards the destination vertex now. The desired pair of paths results.

In lieu of the general purpose Ford's shortest path algorithm valid for negative arcs present anywhere in a graph (with nonexistent negative cycles), Bhandari provides two different algorithms, either one of which can be used in Step 4. One algorithm is a slight modification of the traditional Dijkstra's algorithm, and the other called the Breadth-First-Search (BFS) algorithm is a variant of the Moore's algorithm. Because the negative arcs are only on the first shortest path, no negative cycle arises in the transformed graph (Steps 2 and 3). In a nonnegative graph, the modified Dijkstra algorithm reduces to the traditional Dijkstra's algorithm, and can therefore be used in Step 1 of the above algorithm (and similarly, the BFS algorithm).

## The Modified Dijkstra Algorithm

Source:

G = (V, E) d(i) – the distance of vertex i (i∈V) from source vertex A; it is the sum of arcs in a possible path from vertex A to vertex i. Note that d(A)=0; P(i) – the predecessor of vertex i on the same path. Z – the destination vertex

Step 1.

```
Start with d(A) = 0,
d(i)     = l (Ai), if i∈ΓA;  Γi ≡ set of neighbor vertices of vertex i, l(ij) = length of arc from vertex i to vertex j.
      
         = ∞, otherwise.       
Assign S = V-{A}, where V is the set of vertices in the given graph.
Assign P(i) = A, ∀i∈S.
```

Step 2.

```
a) Find j∈S such that d(j) = min d(i), i∈S.
b) Set S = S – {j}.
c) If j = Z (the destination vertex), END; otherwise go to Step 3.
```

Step 3.

```
∀i∈Γj, if d(j) + l(ji) < d(i),
a) set d(i) = d(j) + l(ji), P(i) = j.
b) S = S ∪{i}
Go to Step 2.
```

## Example

The main steps of the edge-disjoint shortest pair algorithm are illustrated below:

Figure A shows the given undirected graph G(V, E) with edge weights.

Figure B displays the calculated shortest path  ABCZ from A to Z (in bold lines).

Figure C shows the reversal of the arcs of the shortest path and their negative weights.

Figure D displays the shortest path ADCBZ from A to Z determined in the new transformed. graph of Figure C (this is determined using the modified Dijkstra algorithm (or the BFS algorithm) valid for such negative arcs; there are never any negative cycles in such a transformed graph).

Figure E displays the determined shortest path ADCBZ in the original graph.

Figure F displays the determined shortest pair of edge-disjoint paths (ABZ, ADCZ) found after erasing the edge BC common to paths ABCZ and ADCBZ, and grouping the remaining edges suitably.

## Discussion

In a nonnegative graph, the modified Dijkstra algorithm functions as the traditional Dijkstra algorithm. In a graph characterized by vertices with degrees of O(d) (d<|V|), the efficiency is O(d|V|), being O(|V|2), in the worst case, as in the traditional Dijkstra's case.

In the transformed graph of the edge disjoint shortest pair algorithm, which contains negative arcs, a given vertex previously "permanently" labeled in Step 2a of the modified Dijkstra algorithm may be revisited and relabeled in Step 3a, and inserted back in vertex set S (Step 3b). The efficiency of the modified Dijkstra in such a transformed graph becomes O(d2|V|), being O(|V|3) in the worst case. Most graphs of practical interest are usually sparse, possessing vertex degrees of O(1), in which case the efficiency of the modified Dijkstra algorithm applied to the transformed graph becomes O(|V|) (or, equivalently, O(|E|)). The edge-disjoint shortest pair algorithm then becomes comparable in efficiency to the Suurballe's algorithm, which in general is of O(|V|2) due to an extra graph transformation that reweights the graph to avoid negative cost arcs, allowing Dijkstra's algorithm to be used for both shortest path steps. The reweighting requires building the entire shortest path tree rooted at the source vertex. By circumventing this additional graph transformation, and using the modified Dijkstra algorithm instead, Bhandari's approach results in a simplified version of the edge disjoint shortest pair algorithm without sacrificing much in efficiency at least for sparse graphs. The ensuing simple form further lends itself to easy extensions to K (>2) disjoint paths algorithms and their variations such as partially disjoint paths when complete disjointness does not exist, and also to graphs with constraints encountered by a practicing networking professional in the more complicated real-life networks.

The vertex disjoint version of the above edge-disjoint shortest pair of paths algorithm is obtained by splitting each vertex (except for the source and destination vertices) of the first shortest path in Step 3 of the algorithm, connecting the split vertex pair by a zero weight arc (directed towards the source vertex), and replacing any incident edge with two oppositely directed arcs, one incident on the vertex of the split pair (closer to the source vertex) and the other arc emanating from the other vertex. The K (>2) versions are similarly obtained, e.g., the vertices of the shortest edge disjoint pair of paths (except for the source and destination vertices) are split, with the vertices in each split pair connected to each other with arcs of zero weight as well as the external edges in a similar manner[8][9]. The algorithms presented for undirected graphs also extend to directed graphs, and apply in general to any problem (in any technical discipline) that can be modeled as a graph of vertices and edges (or arcs).

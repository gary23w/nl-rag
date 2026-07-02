---
title: "Floyd–Warshall algorithm"
source: https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
domain: floyd-warshall-algorithm
license: CC-BY-SA-4.0
tags: floyd warshall algorithm, all pairs shortest path, dynamic programming, transitive closure
fetched: 2026-07-02
---

# Floyd–Warshall algorithm

In computer science, the **Floyd–Warshall algorithm** (also known as **Floyd's algorithm**, the **Roy–Warshall algorithm**, the **Roy–Floyd algorithm**, or the **WFI algorithm**) is an algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights) of shortest paths between all pairs of vertices. Although it does not return details of the paths themselves, it is possible to reconstruct the paths with simple modifications to the algorithm. Versions of the algorithm can also be used for finding the transitive closure of a relation, or (in connection with the Schulze voting system) widest paths between all pairs of vertices in a weighted graph.

## History and naming

The Floyd–Warshall algorithm is an example of dynamic programming, and was published in its currently recognized form by Robert Floyd in 1962. However, it is essentially the same as algorithms previously published by Bernard Roy in 1959 and also by Stephen Warshall in 1962 for finding the transitive closure of a graph, and is closely related to Kleene's algorithm (published in 1956) for converting a deterministic finite automaton into a regular expression, with the difference being the use of a min-plus semiring. The modern formulation of the algorithm as three nested for-loops was first described by Peter Ingerman, also in 1962.

## Algorithm

The Floyd–Warshall algorithm compares many possible paths through the graph between each pair of vertices. It is guaranteed to find all shortest paths and is able to do this with $\Theta (|V|^{3})$ comparisons in a graph, even though there may be $\Theta (|V|^{2})$ edges in the graph. It does so by incrementally improving an estimate on the shortest path between two vertices, until the estimate is optimal.

Consider a graph G with vertices V numbered 1 through  N . Further consider a function $\mathrm {shortestPath} (i,j,k)$ that returns the length of the shortest possible path (if one exists) from i to j using vertices only from the set $\{1,2,\ldots ,k\}$ as intermediate points along the way. Now, given this function, our goal is to find the length of the shortest path from each i to each j using *any* vertex in $\{1,2,\ldots ,N\}$ . By definition, this is the value $\mathrm {shortestPath} (i,j,N)$ , which we will find recursively.

Observe that $\mathrm {shortestPath} (i,j,k)$ must be less than or equal to $\mathrm {shortestPath} (i,j,k-1)$ : we have *more* flexibility if we are allowed to use the vertex k . If $\mathrm {shortestPath} (i,j,k)$ is in fact less than $\mathrm {shortestPath} (i,j,k-1)$ , then there must be a path from i to j using the vertices $\{1,2,\ldots ,k\}$ that is shorter than any such path that does not use the vertex k . Since there are no negative cycles this path can be decomposed as:

(1) a path from

i

to

k

that uses the vertices

$\{1,2,\ldots ,k-1\}$

, followed by

(2) a path from

k

to

j

that uses the vertices

$\{1,2,\ldots ,k-1\}$

.

And of course, these must be a *shortest* such path (or several of them), otherwise we could further decrease the length. In other words, we have arrived at the recursive formula:

$\mathrm {shortestPath} (i,j,k)=$

$\mathrm {min} {\Big (}\mathrm {shortestPath} (i,j,k-1),$

$\mathrm {shortestPath} (i,k,k-1)+\mathrm {shortestPath} (k,j,k-1){\Big )}$

.

The base case is given by

$\mathrm {shortestPath} (i,j,0)=w(i,j),$

where $w(i,j)$ denotes the weight of the edge from i to j if one exists and ∞ (infinity) otherwise.

These formulas are the heart of the Floyd–Warshall algorithm. The algorithm works by first computing $\mathrm {shortestPath} (i,j,k)$ for all $(i,j)$ pairs for $k=0$ , then $k=1$ , then $k=2$ , and so on. This process continues until $k=N$ , and we have found the shortest path for all $(i,j)$ pairs using any intermediate vertices. Pseudocode for this basic version follows.

### Pseudocode

```
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u, v) do
    dist[u][v] = w(u, v)  // The weight of the edge (u, v)
for each vertex v do
    dist[v][v] = 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j]
                dist[i][j] = dist[i][k] + dist[k][j]
            end if
```

Note: A common mistake in implementing the Floyd–Warshall algorithm is to misorder the triply nested loops (The correct order is `KIJ`). The incorrect `IJK` and `IKJ` algorithms do not give correct solutions for some instance. However, we can prove that if these are repeated three times, we obtain the correct solutions.

## Example

The algorithm above is executed on the graph on the left below:

Prior to the first recursion of the outer loop, labeled *k* = 0 above, the only known paths correspond to the single edges in the graph. At *k* = 1, paths that go through the vertex 1 are found: in particular, the path [2,1,3] is found, replacing the path [2,3] which has fewer edges but is longer (in terms of weight). At *k* = 2, paths going through the vertices {1,2} are found. The red and blue boxes show how the path [4,2,1,3] is assembled from the two known paths [4,2] and [2,1,3] encountered in previous iterations, with 2 in the intersection. The path [4,2,3] is not considered, because [2,1,3] is the shortest path encountered so far from 2 to 3. At *k* = 3, paths going through the vertices {1,2,3} are found. Finally, at *k* = 4, all shortest paths are found.

The distance matrix at each iteration of k, with the updated distances in **bold**, will be:

| *k* = 0 | j |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |   |
| i | 1 | 0 | ∞ | −2 | ∞ |
| 2 | 4 | 0 | 3 | ∞ |   |
| 3 | ∞ | ∞ | 0 | 2 |   |
| 4 | ∞ | −1 | ∞ | 0 |   |

| *k* = 1 | j |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |   |
| i | 1 | 0 | ∞ | −2 | ∞ |
| 2 | 4 | 0 | **2** | ∞ |   |
| 3 | ∞ | ∞ | 0 | 2 |   |
| 4 | ∞ | −1 | ∞ | 0 |   |

| *k* = 2 | j |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |   |
| i | 1 | 0 | ∞ | −2 | ∞ |
| 2 | 4 | 0 | 2 | ∞ |   |
| 3 | ∞ | ∞ | 0 | 2 |   |
| 4 | **3** | −1 | **1** | 0 |   |

| *k* = 3 | j |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |   |
| i | 1 | 0 | ∞ | −2 | **0** |
| 2 | 4 | 0 | 2 | **4** |   |
| 3 | ∞ | ∞ | 0 | 2 |   |
| 4 | 3 | −1 | 1 | 0 |   |

| *k* = 4 | j |   |   |   |   |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |   |
| i | 1 | 0 | **−1** | −2 | 0 |
| 2 | 4 | 0 | 2 | 4 |   |
| 3 | **5** | **1** | 0 | 2 |   |
| 4 | 3 | −1 | 1 | 0 |   |

## Behavior with negative cycles

A negative cycle is a cycle whose edges sum to a negative value. There is no shortest path between any pair of vertices i , j which form part of a negative cycle, because path-lengths from i to j can be arbitrarily small (negative). For numerically meaningful output, the Floyd–Warshall algorithm assumes that there are no negative cycles. Nevertheless, if there are negative cycles, the Floyd–Warshall algorithm can be used to detect them. The intuition is as follows:

- The Floyd–Warshall algorithm iteratively revises path lengths between all pairs of vertices $(i,j)$ , including where $i=j$ ;
- Initially, the length of the path $(i,i)$ is zero;
- A path $[i,k,\ldots ,i]$ can only improve upon this if it has length less than zero, i.e. denotes a negative cycle;
- Thus, after the algorithm, $(i,i)$ will be negative if there exists a negative-length path from i back to i .

Hence, to detect negative cycles using the Floyd–Warshall algorithm, one can inspect the diagonal of the path matrix, and the presence of a negative number indicates that the graph contains at least one negative cycle. However, when a negative cycle is present, during the execution of the algorithm exponentially large numbers on the order of $\Omega (6^{n}\cdot w_{max})$ can appear, where $w_{max}$ is the largest absolute value edge weight in the graph. To avoid integer underflow problems, one should check for a negative cycle within the innermost for loop of the algorithm.

## Path reconstruction

The Floyd–Warshall algorithm typically only provides the lengths of the paths between all pairs of vertices. With simple modifications, it is possible to create a method to reconstruct the actual path between any two endpoint vertices. While one may be inclined to store the actual path from each vertex to each other vertex, this is not necessary, and in fact, is very costly in terms of memory. Instead, we can use the shortest-path tree, which can be calculated for each node in $\Theta (|E|)$ time using $\Theta (|V|)$ memory, and allows us to efficiently reconstruct a directed path between any two connected vertices.

### Pseudocode

The array `prev[u][v]` holds the penultimate vertex on the path from `u` to `v` (except in the case of `prev[v][v]`, where it always contains `v` even if there is no self-loop on `v`):

```
let dist be a 
  
    
      
        
          |
        
        V
        
          |
        
        ×
        
          |
        
        V
        
          |
        
      
    
    {\displaystyle |V|\times |V|}
  
 array of minimum distances initialized to 
  
    
      
        ∞
      
    
    {\displaystyle \infty }
  
 (infinity)
let prev be a 
  
    
      
        
          |
        
        V
        
          |
        
        ×
        
          |
        
        V
        
          |
        
      
    
    {\displaystyle |V|\times |V|}
  
 array of vertex indices initialized to null

procedure FloydWarshallWithPathReconstruction() is
    for each edge (u, v) do
        dist[u][v] = w(u, v)  // The weight of the edge (u, v)
        prev[u][v] = u
    for each vertex v do
        dist[v][v] = 0
        prev[v][v] = v
    for k from 1 to |V| do // standard Floyd-Warshall implementation
        for i from 1 to |V|
            for j from 1 to |V|
                if dist[i][j] > dist[i][k] + dist[k][j] then
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]
```

```
procedure Path(u, v) is
    if prev[u][v] = null then
        return []
    path = [v]
    while u ≠ v do
        v = prev[u][v]
        path.prepend(v)
    return path
```

## Time complexity

Let n be $|V|$ , the number of vertices. To find all $n^{2}$ of $\mathrm {shortestPath} (i,j,k)$ (for all i and j ) from those of $\mathrm {shortestPath} (i,j,k-1)$ requires $\Theta (n^{2})$ operations. Since we begin with $\mathrm {shortestPath} (i,j,0)=\mathrm {edgeCost} (i,j)$ and compute the sequence of n matrices $\mathrm {shortestPath} (i,j,1)$ , $\mathrm {shortestPath} (i,j,2)$ , $\ldots$ , $\mathrm {shortestPath} (i,j,n)$ , each having a cost of $\Theta (n^{2})$ , the total time complexity of the algorithm is $n\cdot \Theta (n^{2})=\Theta (n^{3})$ .

## Applications and generalizations

The Floyd–Warshall algorithm can be used to solve the following problems:

- Transitive closure of directed graphs (Warshall's algorithm). In Warshall's original formulation of the algorithm, the graph is unweighted and represented by a Boolean adjacency matrix. Then the addition operation is replaced by logical conjunction (AND) and the minimum operation by logical disjunction (OR).
- Finding a regular expression denoting the regular language accepted by a finite automaton (Kleene's algorithm, a closely related generalization of the Floyd–Warshall algorithm)
- Inversion of real matrices (Gauss–Jordan algorithm)
- Optimal routing. In this application one is interested in finding the path with the maximum flow between two vertices. This means that, rather than taking minima as in the pseudocode above, one instead takes maxima. The edge weights represent fixed constraints on flow. Path weights represent bottlenecks; so the addition operation above is replaced by the minimum operation.
- Fast computation of Pathfinder networks.
- Widest paths/Maximum bandwidth paths
- Computing canonical form of difference bound matrices (DBMs)
- Computing the similarity between graphs
- Transitive closure in AND/OR/threshold graphs.

## Implementations

Implementations are available for many programming languages.

- For C++, in the boost::graph library
- For C#, at QuikGraph
- For C#, at QuickGraphPCL (A fork of QuickGraph with better compatibility with projects using Portable Class Libraries.)
- For Java, in the Apache Commons Graph library
- For JavaScript, in the Cytoscape library
- For Julia, in the Graphs.jl package
- For MATLAB, in the Matlab_bgl Archived 2013-08-17 at the Wayback Machine package
- For Perl, in the Graph module
- For Python, in the SciPy library (module scipy.sparse.csgraph) or NetworkX library
- For R, in packages e1071 and Rfast
- For C, a pthreads, parallelized, implementation including a SQLite interface to the data at floydWarshall.h

## Comparison with other shortest path algorithms

For graphs with non-negative edge weights, Dijkstra's algorithm can be used to find all shortest paths from a *single* vertex with running time $\Theta (|E|+|V|\log |V|)$ . Thus, running Dijkstra starting at *each* vertex takes time $\Theta (|E||V|+|V|^{2}\log |V|)$ . Since $|E|=O(|V|^{2})$ , this yields a worst-case running time of repeated Dijkstra of $O(|V|^{3})$ . While this matches the asymptotic worst-case running time of the Floyd-Warshall algorithm, the constants involved matter quite a lot. When a graph is dense (i.e., $|E|\approx |V|^{2}$ ), the Floyd-Warshall algorithm tends to perform better in practice. When the graph is sparse (i.e., $|E|$ is significantly smaller than $|V|^{2}$ ), Dijkstra tends to dominate.

For sparse graphs with negative edges but no negative cycles, Johnson's algorithm can be used, with the same asymptotic running time as the repeated Dijkstra approach.

There are also known algorithms using fast matrix multiplication to speed up all-pairs shortest path computation in dense graphs, but these typically make extra assumptions on the edge weights (such as requiring them to be small integers). In addition, because of the high constant factors in their running time, they would only provide a speedup over the Floyd–Warshall algorithm for very large graphs.

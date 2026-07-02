---
title: "Blossom algorithm"
source: https://en.wikipedia.org/wiki/Blossom_algorithm
domain: hopcroft-karp-algorithm
license: CC-BY-SA-4.0
tags: hopcroft karp algorithm, bipartite matching, augmenting path, maximum cardinality matching
fetched: 2026-07-02
---

# Blossom algorithm

In graph theory, the **blossom algorithm** is an algorithm for constructing maximum matchings on graphs. The algorithm was developed by Jack Edmonds in 1961, and published in 1965. Given a general graph *G* = (*V*, *E*), the algorithm finds a matching M such that each vertex in V is incident with at most one edge in M and |*M*| is maximized. The matching is constructed by iteratively improving an initial empty matching along augmenting paths in the graph. Unlike bipartite matching, the key new idea is that an odd-length cycle in the graph (blossom) is contracted to a single vertex, with the search continuing iteratively in the contracted graph.

The algorithm runs in time *O*(|*E*||*V*|2), where |*E*| is the number of edges of the graph and |*V*| is its number of vertices. A better running time of $O(|E|{\sqrt {|V|}})$ for the same task can be achieved with the more complicated algorithm of Micali and Vazirani.

A major reason that the blossom algorithm is important is that it gave the first proof that a maximum-size matching could be found using a polynomial amount of computation time. Another reason is that it led to a linear programming polyhedral description of the matching polytope, yielding an algorithm for min-*weight* matching. As elaborated by Alexander Schrijver, further significance of the result comes from the fact that this was the first polytope whose proof of integrality "does not simply follow just from total unimodularity, and its description was a breakthrough in polyhedral combinatorics."

## Augmenting paths

Given *G* = (*V*, *E*) and a matching M of G, a vertex v is **exposed** if no edge of M is incident with v. A path in G is an **alternating path**, if its edges are alternately not in M and in M (or in M and not in M). An **augmenting path** P is an alternating path that starts and ends at two distinct exposed vertices. Note that the number of unmatched edges in an augmenting path is greater by one than the number of matched edges, and hence the total number of edges in an augmenting path is odd. A **matching augmentation** along an augmenting path P is the operation of replacing M with a new matching

$M_{1}=M\oplus P=(M\setminus P)\cup (P\setminus M)$

.

(Augmentation along a path)

By Berge's lemma, matching M is maximum if and only if there is no M-augmenting path in G. Hence, either a matching is maximum, or it can be augmented. Thus, starting from an initial matching, we can compute a maximum matching by augmenting the current matching with augmenting paths as long as we can find them, and return whenever no augmenting paths are left. We can formalize the algorithm as follows:

```
   INPUT:  Graph G, initial matching M on G
   OUTPUT: maximum matching M* on G
A1 function find_maximum_matching(G, M) : M*
A2     P ← find_augmenting_path(G, M)
A3     if P is non-empty then
A4         return find_maximum_matching(G, augment M along P)
A5     else
A6         return M
A7     end if
A8 end function
```

We still have to describe how augmenting paths can be found efficiently. The subroutine to find them uses blossoms and contractions.

## Blossoms and contractions

Given *G* = (*V*, *E*) and a matching M of G, a *blossom* B is a cycle in G consisting of 2*k* + 1 edges of which exactly k belong to M, and where one of the vertices v of the cycle (the *base*) is such that there exists an alternating path of even length (the *stem*) from v to an exposed vertex w.

***Finding Blossoms:***

- Traverse the graph starting from an exposed vertex.
- Starting from that vertex, label it as an outer vertex **o**.
- Alternate the labeling between vertices being inner **i** and outer **o** such that no two adjacent vertices have the same label.
- If we end up with two adjacent vertices labeled as outer **o** then we have an odd-length cycle and hence a blossom.

Define the **contracted graph** G' as the graph obtained from G by contracting every edge of B, and define the **contracted matching** M' as the matching of G' corresponding to M.

(Example of a blossom)

G' has an M'-augmenting path if and only if G has an M-augmenting path, and that any M'-augmenting path P' in G' can be **lifted** to an M-augmenting path in G by undoing the contraction by B so that the segment of P' (if any) traversing through vB is replaced by an appropriate segment traversing through B. In more detail:

- if P' traverses through a segment *u* → *vB* → *w* in G', then this segment is replaced with the segment *u* → ( *u'* → … → *w'* ) → *w* in G, where blossom vertices u' and w' and the side of B, ( *u'* → … → *w'* ), going from u' to w' are chosen to ensure that the new path is still alternating (u' is exposed with respect to $M\cap B$ , $\{w',w\}\in E\setminus M$ ).

(Path lifting when P' traverses through vB, two cases depending on the direction we need to choose to reach vB)

- if P' has an endpoint vB, then the path segment *u* → *vB* in G' is replaced with the segment *u* → ( *u'* → … → *v'* ) in G, where blossom vertices u' and v' and the side of B, ( *u'* → … → *v'* ), going from u' to v' are chosen to ensure that the path is alternating (v' is exposed, $\{u',u\}\in E\setminus M$ ).

(Path lifting when P' ends at vB, two cases depending on the direction we need to choose to reach vB)

Thus blossoms can be contracted and search performed in the contracted graphs. This reduction is at the heart of Edmonds' algorithm.

## Finding an augmenting path

The search for an augmenting path uses an auxiliary data structure consisting of a forest F whose individual trees correspond to specific portions of the graph G. In fact, the forest F is the same that would be used to find maximum matchings in bipartite graphs (without need for shrinking blossoms). In each iteration the algorithm either (1) finds an augmenting path, (2) finds a blossom and recurses onto the corresponding contracted graph, or (3) concludes there are no augmenting paths. The auxiliary structure is built by an incremental procedure discussed next.

The construction procedure considers vertices v and edges e in G and incrementally updates F as appropriate. If v is in a tree T of the forest, we let *`root(v)`* denote the root of T. If both u and v are in the same tree T in F, we let *`distance(u,v)`* denote the length of the unique path from u to v in T.

```
    INPUT:  Graph G, matching M on G
    OUTPUT: augmenting path P in G or empty path if none found
B01 function find_augmenting_path(G, M) : P
B02    F ← empty forest
B03    unmark all vertices and edges in G, mark all edges of M
B05    for each exposed vertex v do
B06        create a singleton tree { v } and add the tree to F
B07    end for
B08    while there is an unmarked vertex v in F with distance(v, root(v)) even do
B09        while there exists an unmarked edge e = { v, w } do
B10            if w is not in F then
                   // w is matched, so add e and w's matched edge to F
B11                x ← vertex matched to w in M
B12                add edges { v, w } and { w, x } to the tree of v
B13            else
B14                if distance(w, root(w)) is odd then
                       // Do nothing.
B15                else
B16                    if root(v) ≠ root(w) then
                           // Report an augmenting path in F 
  
    
      
        ∪
      
    
    {\displaystyle \cup }
  
 { e }.
B17                        P ← path (root(v) → ... → v) → (w → ... → root(w))
B18                        return P
B19                    else
                           // Contract a blossom in G and look for the path in the contracted graph.
B20                        B ← blossom formed by e and edges on the path v → w in T
B21                        G’, M’ ← contract G and M by B
B22                        P’ ← find_augmenting_path(G’, M’)
B23                        P ← lift P’ to G
B24                        return P
B25                    end if
B26                end if
B27            end if
B28            mark edge e
B29        end while
B30        mark vertex v
B31    end while
B32    return empty path
B33 end function
```

### Examples

The following four figures illustrate the execution of the algorithm. Dashed lines indicate edges that are currently not present in the forest. First, the algorithm processes an out-of-forest edge that causes the expansion of the current forest (lines B10 – B12).

(Forest expansion on line B10)

Next, it detects a blossom and contracts the graph (lines B20 – B21).

(Blossom contraction on line B21)

Finally, it locates an augmenting path P′ in the contracted graph (line B22) and lifts it to the original graph (line B23). Note that the ability of the algorithm to contract blossoms is crucial here; the algorithm cannot find P in the original graph directly because only out-of-forest edges between vertices at even distances from the roots are considered on line B17 of the algorithm.

(Detection of augmenting path P′ in G′ on line B17)

(Lifting of P′ to corresponding augmenting path in G on line B25)

### Analysis

The forest F constructed by the `find_augmenting_path()` function is an alternating forest.

- a tree T in G is an **alternating tree** with respect to M, if
  - T contains exactly one exposed vertex r called the tree root
  - every vertex at an odd distance from the root has exactly two incident edges in T, and
  - all paths from r to leaves in T have even lengths, their odd edges are not in M and their even edges are in M.
- a forest F in G is an **alternating forest** with respect to M, if
  - its connected components are alternating trees, and
  - every exposed vertex in G is a root of an alternating tree in F.

Each iteration of the loop starting at line B09 either adds to a tree T in F (line B10) or finds an augmenting path (line B17) or finds a blossom (line B20). It is easy to see that the running time is $O(|E||V|^{2})$ .

## Parallelization

The Blossom algorithm is difficult to parallelize for several reasons. First, blossom contraction and lifting recursively change the graph structure, creating sequential dependencies between different stages of the search. Second, a standard search iteration usually finds only one augmenting path, increasing the matching size by one at a time and requiring many iterations on large graphs. Third, the algorithm maintains dynamic structures, including alternating trees and contracted graphs, that are repeatedly updated during execution. In a parallel implementation, these updates may require synchronization and can introduce data races. These factors have made efficient parallel implementations of the Blossom algorithm highly challenging.

X-Blossom provides an effective parallel solution for computing maximum matchings in general graphs and directly addresses these challenges. It first introduces a new recursion-free Blossom algorithm. In the traditional algorithm, a blossom is contracted during the search and later lifted when an augmenting path is found. By contrast, the recursion-free algorithm eliminates this contraction-and-lifting process. The key observation is that, when constructing an augmenting path, preserving the full recursive contraction history is unnecessary. The essential information is the appropriate even-length path through the blossom structure. Thus, instead of contracting a blossom and later expanding it, the recursion-free algorithm records the even-length path from each relevant vertex on a blossom cycle to the base of the blossom. When an augmenting path passes through the blossom, the recorded path is used to reconstruct the corresponding path in the original graph, as shown in the figure below. This representation preserves the effect of blossom handling while keeping the graph structure static during the search.

This recursion-free variant exposes a critical opportunity for massive parallelization. Since the graph is not recursively modified by contraction and lifting, multiple valid vertices in the current search forest can be examined concurrently. X-Blossom uses this property to identify multiple vertex-disjoint augmenting paths in a single search iteration, allowing the matching size to increase by more than one per iteration.

In its implementation, X-Blossom further replaces alternating-tree structures with a path table. This table records even-length paths for vertices, regardless of whether they belong to a blossom. As a result, the algorithm avoids repeatedly constructing and deconstructing alternating trees and contracted graphs. This reduces path-tracing overhead and makes the algorithm more suitable for parallel execution. Experiments reported in the X-Blossom study showed that its recursion-free design significantly improves the sequential performance, and its parallel version achieves speedups and scalability on multicore platforms across both real-world and synthetic datasets.

## Bipartite matching

When G is bipartite, there are no odd cycles in G. In that case, blossoms will never be found and one can simply remove lines B20 – B24 of the algorithm. The algorithm thus reduces to the standard algorithm to construct maximum cardinality matchings in bipartite graphs where we repeatedly search for an augmenting path by a simple graph traversal: this is for instance the case of the Ford–Fulkerson algorithm.

## Weighted matching

The matching problem can be generalized by assigning weights to edges in G and asking for a matching of maximum total weight: this is known as the maximum weight matching problem. This problem can be solved by a combinatorial algorithm that uses the unweighted blossom algorithm as a subroutine. Efficient, polynomial-time algorithms for this problem are available in several software libraries, including NetworkX, LEDA, and the LEMON graph library.

---
title: "Edmonds–Karp algorithm"
source: https://en.wikipedia.org/wiki/Edmonds–Karp_algorithm
domain: edmonds-karp-algorithm
license: CC-BY-SA-4.0
tags: edmonds karp algorithm, maximum flow, breadth first search, shortest augmenting path
fetched: 2026-07-02
---

# Edmonds–Karp algorithm

In computer science, the **Edmonds–Karp algorithm** is an implementation of the Ford–Fulkerson method for computing the maximum flow in a flow network in $O(|V||E|^{2})$ time. The algorithm was first published by Yefim Dinitz in 1970, and independently published by Jack Edmonds and Richard Karp in 1972. Dinitz's algorithm includes additional techniques that reduce the running time to $O(|V|^{2}|E|)$ .

## Algorithm

The algorithm is identical to the Ford–Fulkerson algorithm, except that the search order when finding the augmenting path is defined. The path found must be a shortest path that has available capacity. This can be found by a breadth-first search, where we apply a weight of 1 to each edge. The running time of $O(|V||E|^{2})$ is found by showing that each augmenting path can be found in $O(|E|)$ time, that every time at least one of the E edges becomes saturated (an edge which has the maximum possible flow), that the distance from the saturated edge to the source along the augmenting path must be longer than last time it was saturated, and that the length is at most $|V|$ . Another property of this algorithm is that the length of the shortest augmenting path increases monotonically. A proof outline using these properties is as follows:

The proof first establishes that distance of the shortest path from the source node s to any non-sink node v in a residual flow network increases monotonically after each augmenting iteration (Lemma 1, proven below). Then, it shows that each of the $|E|$ edges can be critical at most ${\frac {|V|}{2}}$ times for the duration of the algorithm, giving an upper-bound of $O\left({\frac {|V||E|}{2}}\right)=O(|V||E|)$ augmenting iterations. Since each iteration takes $O(|E|)$ time (bounded by the time for finding the shortest path using Breadth-First-Search), the total running time of Edmonds-Karp is $O(|V||E|^{2})$ as required.

To prove Lemma 1, one can use proof by contradiction by assuming that there is an augmenting iteration that causes the shortest path distance from s to v to *decrease*. Let f be the flow before such an augmentation and $f'$ be the flow after. Denote the minimum distance in a residual flow network ⁠ $G_{f}$ ⁠ from nodes $u,v$ as $\delta _{f}(u,v)$ . One can derive a contradiction by showing that $\delta _{f}(s,v)\leq \delta _{f'}(s,v)$ , meaning that the shortest path distance between source node s and non-sink node v did not in fact decrease.

## Pseudocode

```
algorithm EdmondsKarp is
    input:
        graph   (graph[v] should be the list of edges coming out of vertex v in the
                 original graph and their corresponding constructed reverse edges
                 which are used for push-back flow.
                 Each edge should have a capacity 'cap', flow, source 's' and sink 't' 
                 as parameters, as well as a pointer to the reverse edge 'rev'.)
        s       (Source vertex)
        t       (Sink vertex)
    output:
        flow    (Value of maximum flow)
    
    flow := 0   (Initialize flow to zero)
    repeat
        (Run a breadth-first search (bfs) to find the shortest s-t path.
         We use 'pred' to store the edge taken to get to each vertex,
         so we can recover the path afterwards)
        q := queue()
        q.push(s)
        pred := array(graph.length)
        while not empty(q) and pred[t] = null
            cur := q.pop()
            for Edge e in graph[cur] do
                if pred[e.t] = null and e.t ≠ s and e.cap > e.flow then
                    pred[e.t] := e
                    q.push(e.t)

        if not (pred[t] = null) then
            (We found an augmenting path.
             See how much flow we can send) 
            df := ∞
            for (e := pred[t]; e ≠ null; e := pred[e.s]) do
                df := min(df, e.cap - e.flow)
            (And update edges by that amount)
            for (e := pred[t]; e ≠ null; e := pred[e.s]) do
                e.flow  := e.flow + df
                e.rev.flow := e.rev.flow - df
            flow := flow + df

    until pred[t] = null  (i.e., until no augmenting path was found)
    return flow
```

## Example

Given a network of seven nodes, source A, sink G, and capacities as shown below:

In the pairs $f/c$ written on the edges, f is the current flow, and c is the capacity. The residual capacity from u to v is $c_{f}(u,v)=c(u,v)-f(u,v)$ , the total capacity, minus the flow that is already used. If the net flow from u to v is negative, it *contributes* to the residual capacity.

| Path | Capacity | Resulting network |
|---|---|---|
| $A,D,E,G$ | ${\begin{aligned}&\min(c_{f}(A,D),c_{f}(D,E),c_{f}(E,G))\\=&\min(3-0,2-0,1-0)\\=&\min(3,2,1)=1\end{aligned}}$ |   |
| $A,D,F,G$ | ${\begin{aligned}&\min(c_{f}(A,D),c_{f}(D,F),c_{f}(F,G))\\=&\min(3-1,6-0,9-0)\\=&\min(2,6,9)=2\end{aligned}}$ |   |
| $A,B,C,D,F,G$ | ${\begin{aligned}&\min(c_{f}(A,B),c_{f}(B,C),c_{f}(C,D),c_{f}(D,F),c_{f}(F,G))\\=&\min(3-0,4-0,1-0,6-2,9-2)\\=&\min(3,4,1,4,7)=1\end{aligned}}$ |   |
| $A,B,C,E,D,F,G$ | ${\begin{aligned}&\min(c_{f}(A,B),c_{f}(B,C),c_{f}(C,E),c_{f}(E,D),c_{f}(D,F),c_{f}(F,G))\\=&\min(3-1,4-1,2-0,0-(-1),6-3,9-3)\\=&\min(2,3,2,1,3,6)=1\end{aligned}}$ |   |

Notice how the length of the augmenting path found by the algorithm (in red) never decreases. The paths found are the shortest possible. The flow found is equal to the capacity across the minimum cut in the graph separating the source and the sink. There is only one minimal cut in this graph, partitioning the nodes into the sets $\{A,B,C,E\}$ and $\{D,F,G\}$ , with the capacity

$c(A,D)+c(C,D)+c(E,G)=3+1+1=5.\$

---
title: "Iterative deepening depth-first search"
source: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
domain: depth-first-search-algorithm
license: CC-BY-SA-4.0
tags: depth first search, graph traversal, backtracking search, stack data structure
fetched: 2026-07-02
---

# Iterative deepening depth-first search

In computer science, **iterative deepening search** or more specifically **iterative deepening depth-first search** (IDS or IDDFS) is a state space/graph search strategy in which a depth-limited version of depth-first search is run repeatedly with increasing depth limits until the goal is found. IDDFS is optimal, meaning that it finds the shallowest goal. Since it visits all the nodes in the search tree down to depth d before visiting any nodes at depth $d+1$ , the cumulative order in which nodes are first visited is effectively the same as in breadth-first search. However, IDDFS uses much less memory.

## Algorithm for directed graphs

The following pseudocode shows IDDFS implemented in terms of a recursive depth-limited DFS (called DLS) for directed graphs. This implementation of IDDFS does not account for already-visited nodes.

```
function IDDFS(root) is
    for depth from 0 to ∞ do
        found, remaining ← DLS(root, depth)
        if found ≠ null then
            return found
        else if not remaining then
            return null

function DLS(node, depth) is
    if depth = 0 then
        if node is a goal then
            return (node, true)
        else
            return (null, true)    (Not found, but may have children)

    else if depth > 0 then
        any_remaining ← false
        foreach child of node do
            found, remaining ← DLS(child, depth−1)
            if found ≠ null then
                return (found, true)   
            if remaining then
                any_remaining ← true    (At least one node found at depth, let IDDFS deepen)
        return (null, any_remaining)
```

If the goal node is found by DLS, IDDFS will return it without looking deeper. Otherwise, if at least one node exists at that level of depth, the *remaining* flag will let IDDFS continue.

2-tuples are useful as return value to signal IDDFS to continue deepening or stop, in case tree depth and goal membership are unknown *a priori*. Another solution could use sentinel values instead to represent *not found* or *remaining level* results.

## Properties

IDDFS achieves breadth-first search's completeness (when the branching factor is finite) using depth-first search's space-efficiency. If a solution exists, it will find a solution path with the fewest arcs.

Iterative deepening visits states multiple times, and it may seem wasteful. However, if IDDFS explores a search tree to depth d , most of the total effort is in exploring the states at depth d . Relative to the number of states at depth d , the cost of repeatedly visiting the states above this depth is always small.

The main advantage of IDDFS in game tree searching is that the earlier searches tend to improve the commonly used heuristics, such as the killer heuristic and alpha–beta pruning, so that a more accurate estimate of the score of various nodes at the final depth search can occur, and the search completes more quickly since it is done in a better order. For example, alpha–beta pruning is most efficient if it searches the best moves first.

A second advantage is the responsiveness of the algorithm. Because early iterations use small values for d , they execute extremely quickly. This allows the algorithm to supply early indications of the result almost immediately, followed by refinements as d increases. When used in an interactive setting, such as in a chess-playing program, this facility allows the program to play at any time with the current best move found in the search it has completed so far. This can be phrased as each depth of the search *co*recursively producing a better approximation of the solution, though the work done at each step is recursive. This is not possible with a traditional depth-first search, which does not produce intermediate results.

## Asymptotic analysis

### Time complexity

The time complexity of IDDFS in a (well-balanced) tree works out to be the same as breadth-first search, i.e. $O(b^{d})$ , where b is the branching factor and d is the depth of the goal.

#### Proof

In an iterative deepening search, the nodes at depth d are expanded once, those at depth $d-1$ are expanded twice, and so on up to the root of the search tree, which is expanded $d+1$ times. So the total number of expansions in an iterative deepening search is

$b^{d}+2b^{d-1}+3b^{d-2}+\cdots +(d-1)b^{2}+db+(d+1)=\sum _{i=0}^{d}(d+1-i)b^{i}$

where $b^{d}$ is the number of expansions at depth d , $2b^{d-1}$ is the number of expansions at depth $d-1$ , and so on. Factoring out $b^{d}$ gives

$b^{d}(1+2b^{-1}+3b^{-2}+\cdots +(d-1)b^{2-d}+db^{1-d}+(d+1)b^{-d})$

Now let $x={\frac {1}{b}}=b^{-1}$ . Then we have

$b^{d}(1+2x+3x^{2}+\cdots +(d-1)x^{d-2}+dx^{d-1}+(d+1)x^{d})$

This is less than the infinite series

$b^{d}(1+2x+3x^{2}+4x^{3}+\cdots )=b^{d}\left(\sum _{n=1}^{\infty }nx^{n-1}\right)$

which converges to

$b^{d}(1-x)^{-2}=b^{d}{\frac {1}{(1-x)^{2}}}$

, for

$abs(x)<1$

That is, we have

$b^{d}(1+2x+3x^{2}+\cdots +(d-1)x^{d-2}+dx^{d-1}+(d+1)x^{d})\leq b^{d}(1-x)^{-2}$ , for $abs(x)<1$

Since $(1-x)^{-2}$ or $\left(1-{\frac {1}{b}}\right)^{-2}$ is a constant independent of d (the depth), if $b>1$ (i.e., if the branching factor is greater than 1), the running time of the depth-first iterative deepening search is $O(b^{d})$ .

#### Example

For $b=10$ and $d=5$ the number is

$\sum _{i=0}^{5}(5+1-i)10^{i}=6+50+400+3000+20000+100000=123456$

All together, an iterative deepening search from depth 1 all the way down to depth d expands only about $11\%$ more nodes than a single breadth-first or depth-limited search to depth d , when $b=10$ .

The higher the branching factor, the lower the overhead of repeatedly expanded states, but even when the branching factor is 2, iterative deepening search only takes about twice as long as a complete breadth-first search. This means that the time complexity of iterative deepening is still $O(b^{d})$ .

### Space complexity

The space complexity of IDDFS is $O(d)$ , where d is the depth of the goal.

#### Proof

Since IDDFS, at any point, is engaged in a depth-first search, it need only store a stack of nodes which represents the branch of the tree it is expanding. Since it finds a solution of optimal length, the maximum depth of this stack is d , and hence the maximum amount of space is $O(d)$ .

In general, iterative deepening is the preferred search method when there is a large search space and the depth of the solution is not known.

## Example

For the following graph:

a depth-first search starting at A, assuming that the left edges in the shown graph are chosen before right edges, and assuming the search remembers previously-visited nodes and will not repeat them (since this is a small graph), will visit the nodes in the following order: A, B, D, F, E, C, G. The edges traversed in this search form a Trémaux tree, a structure with important applications in graph theory.

Performing the same search without remembering previously visited nodes results in visiting nodes in the order A, B, D, F, E, A, B, D, F, E, etc. forever, caught in the A, B, D, F, E cycle and never reaching C or G.

Iterative deepening prevents this loop and will reach the following nodes on the following depths, assuming it proceeds left-to-right as above:

- Depth 0: A
- Depth 1: A, B, C, E

(Iterative deepening has now seen C, when a conventional depth-first search did not.)

- Depth 2: A, B, D, F, C, G, E, F

(It still sees C, but that it came later. Also it sees E via a different path, and loops back to F twice.)

- Depth 3: A, B, D, F, E, C, G, E, F, B

For this graph, as more depth is added, the two cycles "ABFE" and "AEFB" will simply get longer before the algorithm gives up and tries another branch.

Similar to iterative deepening is a search strategy called iterative lengthening search that works with increasing path-cost limits instead of depth-limits. It expands nodes in the order of increasing path cost; therefore the first goal it encounters is the one with the cheapest path cost. But iterative lengthening incurs substantial overhead that makes it less useful than iterative deepening.

Iterative deepening A* is a best-first search that performs iterative deepening based on "f"-values similar to the ones computed in the A* algorithm.

### Bidirectional IDDFS

IDDFS has a bidirectional counterpart, which alternates two searches: one starting from the source node and moving along the directed arcs, and another one starting from the target node and proceeding along the directed arcs in opposite direction (from the arc's head node to the arc's tail node). The search process first checks that the source node and the target node are same, and if so, returns the trivial path consisting of a single source/target node. Otherwise, the forward search process expands the child nodes of the source node (set A ), the backward search process expands the parent nodes of the target node (set B ), and it is checked whether A and B intersect. If so, a shortest path is found. Otherwise, the search depth is incremented and the same computation takes place.

One limitation of the algorithm is that the shortest path consisting of an odd number of arcs will not be detected. Suppose we have a shortest path $\langle s,u,v,t\rangle .$ When the depth will reach two hops along the arcs, the forward search will proceed from u to v , and the backward search will proceed from v to u . Pictorially, the search frontiers will go through each other, and instead a suboptimal path consisting of an even number of arcs will be returned. This is illustrated in the below diagrams:

What comes to space complexity, the algorithm colors the deepest nodes in the forward search process in order to detect existence of the middle node where the two search processes meet.

Additional difficulty of applying bidirectional IDDFS is that if the source and the target nodes are in different strongly connected components, say, $s\in S,t\in T$ , if there is no arc leaving S and entering T , the search will never terminate.

#### Time and space complexities

The running time of bidirectional IDDFS is given by

$2\sum _{k=0}^{n/2}b^{k}$

and the space complexity is given by

$b^{n/2},$

where n is the number of nodes in the shortest $s,t$ -path. Since the running time complexity of iterative deepening depth-first search is $\sum _{k=0}^{n}b^{k}$ , the speedup is roughly

${\frac {\sum _{k=0}^{n}b^{k}}{2\sum _{k=0}^{n/2}b^{k}}}={\frac {\frac {1-b^{n+1}}{1-b}}{2{\frac {1-b^{n/2+1}}{1-b}}}}={\frac {1-b^{n+1}}{2(1-b^{n/2+1})}}={\frac {b^{n+1}-1}{2(b^{n/2+1}-1)}}\approx {\frac {b^{n+1}}{2b^{n/2+1}}}=\Theta (b^{n/2}).$

#### Pseudocode

```
function Find-Shortest-Path(s, t) is
   if s = t then
       return <s>
   (B, F, Vf, Vb) := (empty stack, ∅, ∅, ∅)
   (Δ, lf, lb) := (0, 0, 0)
   forever do
       (F, Vf) := (∅, ∅)
       Depth-Limited-Search-Forward(s, Δ, F, Vf)
       if |Vf| = lf then
           return nil
       (lf, Vb) := (|Vf|, ∅)
       μ := Depth-Limited-Search-Backward(t, Δ, B, F, Vb)
       if μ 
  
    
      
        ≠
      
    
    {\displaystyle \neq }
  
 nil then
           return Build-Path(s, μ, B, G)
       Vb := ∅
       μ := Depth-Limited-Search-Backward(t, Δ + 1, B, F, Vb)
       if μ 
  
    
      
        ≠
      
    
    {\displaystyle \neq }
  
 nil then
           return Build-Path(s, μ, B, G)
       if |Bb| = lb  then
           return nil
       (lb, Δ) := (|Vb|, Δ + 1)
```

```
function Build-Path(s, μ, B) is
    π := Find-Shortest-Path(s, μ) (Recursively compute the path to the relay node)
    Pop(B)
    return π 
  
    
      
        ∘
      
    
    {\displaystyle \circ }
  
 B (Append the stack starting from its top.)
```

```
function Depth-Limited-Search-Forward(u, Δ, F, V) is
    if u ∈ V then
        return
    V := V ∪ {u}
    if Δ = 0 then
        F := F ∪ {u} (Mark u as a frontier node.)
        return
    foreach child of u do
        Depth-Limited-Search-Forward(child, Δ − 1, F, V)
```

```
function Depth-Limited-Search-Backward(u, Δ, B, F, V) is
    if u ∈ V then
        return nil
    Push(B, u)
    if Δ = 0 then
        if u ∈ F  then
            return u (Reached the marked node, use it as a relay node)
        Pop(B)
        return nil
    V := V ∪ {u}
    foreach parent of u do
        μ := Depth-Limited-Search-Backward(parent, Δ − 1, B, F, V)
        if μ 
  
    
      
        ≠
      
    
    {\displaystyle \neq }
  
 nil then
            return μ
    Pop(B)
    return nil
```

---
title: "Dominator (graph theory)"
source: https://en.wikipedia.org/wiki/Dominator_(graph_theory)
domain: static-single-assignment
license: CC-BY-SA-4.0
tags: static single assignment, phi function, dominance frontier, SSA form
fetched: 2026-07-02
---

# Dominator (graph theory)

|   |
|---|

| 1 | dom | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 2 | dom |   | 2 | 3 | 4 | 5 | 6 |
| 3 | dom |   |   | 3 |   |   |   |
| 4 | dom |   |   |   | 4 |   |   |
| 5 | dom |   |   |   |   | 5 |   |
| 6 | dom |   |   |   |   |   | 6 |
| Corresponding domination relation: Grey nodes are not strictly dominated Red nodes are immediately dominated |   |   |   |   |   |   |   |

In computer science, a node d of a control-flow graph **dominates** a node n if every path from the *entry node* to n must go through d. Notationally, this is written as *d* dom *n* (or sometimes *d* ≫ *n*). By definition, every node dominates itself.

There are a number of related concepts:

- A node d *strictly dominates* a node n if d dominates n and d does not equal n.
- The *immediate dominator* or **idom** of a node n is the unique node that strictly dominates n but does not strictly dominate any other node that strictly dominates n. Every node reachable from the entry node has an immediate dominator (except the entry node).
- The *dominance frontier* of a node d is the set of all nodes ni such that d dominates an immediate predecessor of ni, but d does not strictly dominate ni. It is the set of nodes where d's dominance stops.
- A *dominator tree* is a tree where each node's children are those nodes it immediately dominates. The start node is the root of the tree.

## History

Dominance was first introduced by Reese T. Prosser in a 1959 paper on analysis of flow diagrams. Prosser did not present an algorithm for computing dominance, which had to wait ten years for Edward S. Lowry and C. W. Medlock. Ron Cytron *et al.* rekindled interest in dominance in 1989 when they applied it to the problem of efficiently computing the placement of φ functions, which are used in static single assignment form.

## Applications

Dominators, and dominance frontiers particularly, have applications in compilers for computing static single assignment form. A number of compiler optimizations can also benefit from dominators. The flow graph in this case comprises basic blocks.

Dominators play a crucial role in control flow analysis by identifying the program behaviors that are relevant to a specific statement or operation, which helps in optimizing and simplifying the control flow of programs for analysis.

Automatic parallelization benefits from postdominance frontiers. This is an efficient method of computing control dependence, which is critical to the analysis.

Memory usage analysis can benefit from the dominator tree to easily find leaks and identify high memory usage.

In hardware systems, dominators are used for computing signal probabilities for test generation, estimating switching activities for power and noise analysis, and selecting cut points in equivalence checking. In software systems, they are used for reducing the size of the test set in structural testing techniques such as statement and branch coverage.

## Algorithms

Let $n_{0}$ be the source node on the Control-flow graph. The dominators of a node n are given by the maximal solution to the following data-flow equations:

$\operatorname {Dom} (n)={\begin{cases}\left\{n\right\}&{\mbox{ if }}n=n_{0}\\\left\{n\right\}\cup \left(\bigcap _{p\in {\text{preds}}(n)}^{}\operatorname {Dom} (p)\right)&{\mbox{ if }}n\neq n_{0}\end{cases}}$

The dominator of the start node is the start node itself. The set of dominators for any other node n is the intersection of the set of dominators for all predecessors p of n . The node n is also in the set of dominators for n .

An algorithm for the direct solution is:

```
 // dominator of the start node is the start itself
 Dom(n0) = {n0}
 // for all other nodes, set all nodes as the dominators
 for each n in N - {n0}
     Dom(n) = N;
 // iteratively eliminate nodes that are not dominators
 while changes in any Dom(n)
     for each n in N - {n0}:
         Dom(n) = {n} union with intersection over Dom(p) for all p in pred(n)
```

The direct solution is quadratic in the number of nodes, or O(*n*2). Lengauer and Tarjan developed an algorithm which is almost linear, and in practice, except for a few artificial graphs, the algorithm and a simplified version of it are as fast or faster than any other known algorithm for graphs of all sizes and its advantage increases with graph size.

Keith D. Cooper, Timothy J. Harvey, and Ken Kennedy of Rice University describe an algorithm that essentially solves the above data flow equations but uses well engineered data structures to improve performance.

## Postdominance

Analogous to the definition of dominance above, a node *z* is said to **post-dominate** a node *n* if all paths to the exit node of the graph starting at *n* must go through *z*. Similarly, the **immediate post-dominator** of a node *n* is the postdominator of *n* that doesn't strictly postdominate any other strict postdominators of *n*.

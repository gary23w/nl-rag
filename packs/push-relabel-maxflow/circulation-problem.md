---
title: "Circulation problem"
source: https://en.wikipedia.org/wiki/Circulation_problem
domain: push-relabel-maxflow
license: CC-BY-SA-4.0
tags: push relabel algorithm, preflow maximum flow, height function, goldberg tarjan
fetched: 2026-07-02
---

# Circulation problem

The **circulation problem** and its variants are a generalisation of network flow problems, with the added constraint of a lower bound on edge flows, and with **flow conservation** also being required for the source and sink (i.e. there are no special nodes). In variants of the problem, there are multiple commodities flowing through the network, and a cost on the flow.

## Definition

Given flow network $G(V,E)$ with:

$l(v,w)$

, lower bound on flow from node

v

to node

w

,

$u(v,w)$

, upper bound on flow from node

v

to node

w

,

$c(v,w)$

, cost of a unit of flow on

$(v,w)$

and the constraints:

$l(v,w)\leq f(v,w)\leq u(v,w)$

,

$\sum _{w\in V}f(u,w)=0$

(flow cannot appear or disappear in nodes).

Finding a flow assignment satisfying the constraints gives a solution to the given circulation problem.

In the minimum cost variant of the problem, minimize

$\sum _{(v,w)\in E}c(v,w)\cdot f(v,w).$

### Multi-commodity circulation

In a multi-commodity circulation problem, you also need to keep track of the flow of the individual commodities:

| $\,f_{i}(v,w)$ | The flow of commodity i from v to w . |
|---|---|
| $\,f(v,w)=\sum _{i}f_{i}(v,w)$ | The total flow. |

There is also a lower bound on each flow of commodity.

| $\,l_{i}(v,w)\leq f_{i}(v,w)$ |
|---|

The conservation constraint must be upheld individually for the commodities:

$\ \sum _{w\in V}f_{i}(u,w)=0.$

## Solution

For the circulation problem, many polynomial algorithms have been developed (e.g., Edmonds–Karp algorithm, 1972; Tarjan 1987-1988). Tardos found the first strongly polynomial algorithm.

For the case of multiple commodities, the problem is NP-complete for integer flows. For fractional flows, it is solvable in polynomial time, as one can formulate the problem as a linear program.

Below are given some problems, and how to solve them with the general circulation setup given above.

- Minimum cost multi-commodity circulation problem - Using all constraints given above.
- Minimum cost circulation problem - Use a single commodity
- Multi-commodity circulation - Solve without optimising cost.
- Simple circulation - Just use one commodity, and no cost.
- Multi-commodity flow - If $K_{i}(s_{i},t_{i},d_{i})$ denotes a demand of $d_{i}$ for commodity i from $s_{i}$ to $t_{i}$ , create an edge $(t_{i},s_{i})$ with $l_{i}(t_{i},s_{i})=u(t_{i},s_{i})=d_{i}$ for all commodities i . Let $l_{i}(u,v)=0$ for all other edges.
- Minimum cost multi-commodity flow problem - As above, but minimize the cost.
- Minimum cost flow problem - As above, with 1 commodity.
- Maximum flow problem - Set all costs to 0, and add an edge from the sink t to the source s with $l(t,s)=0$ , $u(t,s)=$ ∞ and $c(t,s)=-1$ .
- Minimum cost maximum flow problem - First find the maximum flow amount m . Then solve with $l(t,s)=u(t,s)=m$ and $c(t,s)=0$ .
- Single-source shortest path - Let $l(u,v)=0$ and $c(u,v)=1$ for all edges in the graph, and add an edge $(t,s)$ with $l(t,s)=u(t,s)=1$ and $c(t,s)=0$ .
- All-pairs shortest path - Let all capacities be unlimited, and find a flow of 1 for $v(v-1)/2$ commodities, one for each pair of nodes.

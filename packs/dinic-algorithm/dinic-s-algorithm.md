---
title: "Dinic's algorithm"
source: https://en.wikipedia.org/wiki/Dinic's_algorithm
domain: dinic-algorithm
license: CC-BY-SA-4.0
tags: dinic algorithm, maximum flow, blocking flow, level graph
fetched: 2026-07-02
---

# Dinic's algorithm

**Dinic's algorithm** or **Dinitz's algorithm** is a strongly polynomial algorithm for computing the maximum flow in a flow network, conceived in 1970 by Israeli (formerly Soviet) computer scientist Yefim Dinitz. The algorithm runs in $O(|V|^{2}|E|)$ time and is similar to the Edmonds–Karp algorithm, which runs in $O(|V||E|^{2})$ time, in that it uses shortest augmenting paths. The introduction of the concepts of the *level graph* and *blocking flow* enable Dinic's algorithm to achieve its performance.

## History

Dinitz invented the algorithm in January 1969, as a master's student in Georgy Adelson-Velsky's group. A few decades later, he would recall:

> In Adel'son-Vel'sky's Algorithms class, the lecturer had a habit of giving the problem to be discussed at the next meeting as an exercise to students. The DA was invented in response to such an exercise. At that time, the author was not aware of the basic facts regarding [the Ford–Fulkerson algorithm]….
> 
> ⋮ Ignorance sometimes has its merits. Very probably, DA would not have been invented then, if the idea of possible saturated edge desaturation had been known to the author.

In 1970, Dinitz published a description of the algorithm in *Doklady Akademii Nauk SSSR*. In 1974, Shimon Even and (his then Ph.D. student) Alon Itai at the Technion in Haifa were very curious and intrigued by Dinitz's algorithm as well as Alexander V. Karzanov's related idea of blocking flow. However it was hard for them to decipher these two papers, each being limited to four pages to meet the restrictions of journal *Doklady Akademii Nauk SSSR*. Even did not give up, and after three days of effort managed to understand both papers except for the layered network maintenance issue. Over the next couple of years, Even gave lectures on "Dinic's algorithm", mispronouncing the name of the author while popularizing it. Even and Itai also contributed to this algorithm by combining BFS and DFS, which is how the algorithm is now commonly presented.

For about 10 years of time after the Ford–Fulkerson algorithm was invented, it was unknown if it could be made to terminate in polynomial time in the general case of irrational edge capacities. This caused a lack of any known polynomial-time algorithm to solve the max flow problem in generic cases. Dinitz's algorithm and the Edmonds–Karp algorithm (published in 1972) both independently showed that in the Ford–Fulkerson algorithm, if each augmenting path is the shortest one, then the length of the augmenting paths is non-decreasing and the algorithm always terminates.

## Definition

Let $G=((V,E),c,f,s,t)$ be a network with $c(u,v)$ and $f(u,v)$ the capacity and the flow of the edge $(u,v)$ , respectively.

The

residual capacity

is a mapping

$c_{f}\colon V\times V\to R^{+}$

defined as,

1. if $(u,v)\in E$ , $c_{f}(u,v)=c(u,v)-f(u,v)$
2. if $(v,u)\in E$ , $c_{f}(u,v)=f(v,u)$
3. $c_{f}(u,v)=0$ otherwise.

The

residual graph

is an unweighted graph

$G_{f}=((V,E_{f}),c_{f}|_{E_{f}},s,t)$

, where

$E_{f}=\{(u,v)\in V\times V\colon \;c_{f}(u,v)>0\}$

.

An

augmenting path

is an

s

–

t

path in the residual graph

$G_{f}$

.

Define

$\operatorname {dist} (v)$

to be the length of the shortest path from

s

to

v

in

$G_{f}$

. Then the

level graph

of

$G_{f}$

is the graph

$G_{L}=((V,E_{L}),c_{f}|_{E_{L}},s,t)$

, where

$E_{L}=\{(u,v)\in E_{f}\colon \;\operatorname {dist} (v)=\operatorname {dist} (u)+1\}$

.

A

blocking flow

is an

s

–

t

flow

$f'$

such that the graph

$G'=((V,E_{L}'),s,t)$

with

$E_{L}'=\{(u,v)\colon \;f'(u,v)<c_{f}|_{E_{L}}(u,v)\}$

contains no

s

–

t

path.

## Algorithm

**Dinic's Algorithm**

Input

: A network

$G=((V,E),c,s,t)$

.

Output

: An

s

–

t

flow

f

of maximum value.

1. Set $f(e)=0$ for each $e\in E$ .
2. Construct $G_{L}$ from $G_{f}$ of G . If $\operatorname {dist} (t)=\infty$ , stop and output f .
3. Find a blocking flow $f'$ in $G_{L}$ .
4. Augment flow f by $f'$ and go back to step 2.

## Analysis

It can be shown that the number of layers in each blocking flow increases by at least 1 each time and thus there are at most $|V|-1$ blocking flows in the algorithm. For each of them:

- the level graph $G_{L}$ can be constructed by breadth-first search in $O(E)$ time
- a blocking flow in the level graph $G_{L}$ can be found in $O(VE)$ time

with total running time $O(E+VE)=O(VE)$ for each layer. As a consequence, the running time of Dinic's algorithm is $O(V^{2}E)$ .

Using a data structure called dynamic trees, the running time of finding a blocking flow in each phase can be reduced to $O(E\log V)$ and therefore the running time of Dinic's algorithm can be improved to $O(VE\log V)$ .

### Special cases

In networks with unit capacities, a much stronger time bound holds. Each blocking flow can be found in $O(E)$ time, and it can be shown that the number of phases does not exceed $O({\sqrt {E}})$ and $O(V^{2/3})$ . Thus the algorithm runs in $O(\min\{V^{2/3},E^{1/2}\}E)$ time.

In networks that arise from the bipartite matching problem, the number of phases is bounded by $O({\sqrt {V}})$ , therefore leading to the $O({\sqrt {V}}E)$ time bound. The resulting algorithm is also known as Hopcroft–Karp algorithm. More generally, this bound holds for any *unit network* — a network in which each vertex, except for source and sink, either has a single entering edge of capacity one, or a single outgoing edge of capacity one, and all other capacities are arbitrary integers.

## Example

The following is a simulation of Dinic's algorithm. In the level graph $G_{L}$ , the vertices with labels in red are the values $\operatorname {dist} (v)$ . The paths in blue form a blocking flow.

|   | G | $G_{f}$ | $G_{L}$ |
|---|---|---|---|
| 1. |   |   |   |
|   | The blocking flow consists of $\{s,1,3,t\}$ with 4 units of flow, $\{s,1,4,t\}$ with 6 units of flow, and $\{s,2,4,t\}$ with 4 units of flow. Therefore, the blocking flow is of 14 units and the value of flow $\|f\|$ is 14. Note that each augmenting path in the blocking flow has *3* edges. |   |   |
| 2. |   |   |   |
|   | The blocking flow consists of $\{s,2,4,3,t\}$ with 5 units of flow. Therefore, the blocking flow is of 5 units and the value of flow $\|f\|$ is 14 + 5 = 19. Note that each augmenting path has 4 edges. |   |   |
| 3. |   |   |   |
|   | Since t cannot be reached in $G_{f}$ , the algorithm terminates and returns a flow with maximum value of 19. Note that in each blocking flow, the number of edges in the augmenting path increases by at least 1. |   |   |

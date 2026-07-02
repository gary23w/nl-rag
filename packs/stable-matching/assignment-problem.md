---
title: "Assignment problem"
source: https://en.wikipedia.org/wiki/Assignment_problem
domain: stable-matching
license: CC-BY-SA-4.0
tags: stable matching, gale shapley algorithm, stable marriage problem, hospital residents problem
fetched: 2026-07-02
---

# Assignment problem

The **assignment problem** is a fundamental combinatorial optimization problem. In its most general form, the problem is as follows:

The problem instance has a number of

agents

and a number of

tasks

. Any agent can be assigned to perform any task, incurring some

cost

that may vary depending on the agent-task assignment. It is required to perform as many tasks as possible by assigning at most one agent to each task and at most one task to each agent, in such a way that the

total cost

of the assignment is minimized.

Alternatively, describing the problem using graph theory:

The assignment problem consists of finding, in a

weighted

bipartite graph

, a

matching

of maximum size, in which the sum of weights of the edges is minimum.

If the numbers of agents and tasks are equal, then the problem is called **balanced assignment**, and the graph-theoretic version is called **minimum-cost perfect matching**. Otherwise, it is called **unbalanced assignment**.

If the total cost of the assignment for all tasks is equal to the sum of the costs for each agent (or the sum of the costs for each task, which is the same thing in this case), then the problem is called **linear assignment**. Commonly, when speaking of the *assignment problem* without any additional qualification, then the *linear balanced assignment problem* is meant.

## Examples

Suppose that a taxi firm has three taxis (the agents) available, and three customers (the tasks) wishing to be picked up as soon as possible. The firm prides itself on speedy pickups, so for each taxi the "cost" of picking up a particular customer will depend on the time taken for the taxi to reach the pickup point. This is a *balanced assignment* problem. Its solution is whichever combination of taxis and customers results in the least total cost.

Now, suppose that there are *four* taxis available, but still only three customers. This is an *unbalanced assignment* problem. One way to solve it is to invent a fourth dummy task, perhaps called "sitting still doing nothing", with a cost of 0 for the taxi assigned to it. This reduces the problem to a balanced assignment problem, which can then be solved in the usual way and still give the best solution to the problem.

Similar adjustments can be done in order to allow more tasks than agents, tasks to which multiple agents must be assigned (for instance, a group of more customers than will fit in one taxi), or maximizing profit rather than minimizing cost.

## Formal definition

The formal definition of the **assignment problem** (or **linear assignment problem**) is

Given two sets,

A

and

T

, together with a

weight function

C

:

A

×

T

→

R

. Find a

bijection

f

:

A

→

T

such that the

cost function

:

$\sum _{a\in A}C(a,f(a))$

is minimized.

Usually the weight function is viewed as a square real-valued matrix *C*, so that the cost function is written down as:

$\sum _{a\in A}C_{a,f(a)}$

The problem is "linear" because the cost function to be optimized as well as all the constraints contain only linear terms.

## Algorithms

A naive solution for the assignment problem is to check all the assignments and calculate the cost of each one. This may be very inefficient since, with *n* agents and *n* tasks, there are *n*! (factorial of *n*) different assignments.

Another naive solution is to greedily assign the pair with the smallest cost first, and remove the vertices; then, among the remaining vertices, assign the pair with the smallest cost; and so on. This algorithm may yield a non-optimal solution. For example, suppose there are two tasks and two agents with costs as follows:

- Alice: Task 1 = 1, Task 2 = 2.
- George: Task 1 = 5, Task 2 = 8.

The greedy algorithm would assign Task 1 to Alice and Task 2 to George, for a total cost of 9, but the reverse assignment has a total cost of 7.

Fortunately, there are many algorithms for finding the optimal assignment in time polynomial in *n*. The assignment problem is a special case of the transportation problem, which is a special case of the minimum cost flow problem, which in turn is a special case of a linear program. While it is possible to solve any of these problems using the simplex algorithm, or in worst-case polynomial time using the ellipsoid method, each specialization has a smaller solution space and thus more efficient algorithms designed to take advantage of its special structure.

### Balanced assignment

In the balanced assignment problem, both parts of the bipartite graph have the same number of vertices, denoted by *n*.

One of the first polynomial-time algorithms for balanced assignment was the Hungarian algorithm. It is a *global* algorithm – it is based on improving a matching along augmenting paths (alternating paths between unmatched vertices). Its run-time complexity, when using Fibonacci heaps, is $O(mn+n^{2}\log n)$ , where *m* is the number of edges. This is currently the fastest run-time of a strongly polynomial algorithm for this problem. Some variants of the Hungarian algorithm also benefit from parallel computing, including GPU acceleration. If all weights are integers, then the run-time can be improved to $O(mn+n^{2}\log \log n)$ , but the resulting algorithm is only weakly polynomial. If the weights are integers, and all weights are at most *C* (where *C*>1 is some integer), then the problem can be solved in $O(m{\sqrt {n}}\log(n\cdot C))$ weakly-polynomial time in a method called *weight scaling*.

In addition to the global methods, there are *local methods* which are based on finding local updates (rather than full augmenting paths). These methods have worse asymptotic runtime guarantees, but they often work better in practice. These algorithms are called auction algorithms, push-relabel algorithms, or preflow-push algorithms. Some of these algorithms were shown to be equivalent.

Some of the local methods assume that the graph admits a *perfect matching*; if this is not the case, then some of these methods might run forever. A simple technical way to solve this problem is to extend the input graph to a *complete bipartite graph,* by adding artificial edges with very large weights. These weights should exceed the weights of all existing matchings, to prevent appearance of artificial edges in the possible solution.

As shown by Mulmuley, Vazirani and Vazirani, the problem of minimum weight perfect matching is converted to finding minors in the adjacency matrix of a graph. Using the isolation lemma, a minimum weight perfect matching in a graph can be found with probability at least 1⁄2. For a graph with *n* vertices, it requires $O(\log ^{2}(n))$ time.

### Unbalanced assignment

In the unbalanced assignment problem, the larger part of the bipartite graph has *n* vertices and the smaller part has *r*<*n* vertices. There is also a constant *s* which is at most the cardinality of a maximum matching in the graph. The goal is to find a minimum-cost matching of size exactly *s*. The most common case is the case in which the graph admits a one-sided-perfect matching (i.e., a matching of size *r*), and *s*=*r*.

Unbalanced assignment can be reduced to a balanced assignment. The naive reduction is to add $n-r$ new vertices to the smaller part and connect them to the larger part using edges of cost 0. However, this requires $n(n-r)$ new edges. A more efficient reduction is called the *doubling technique*. Here, a new graph *G'* is built from two copies of the original graph *G*: a forward copy *Gf* and a backward copy *Gb.* The backward copy is "flipped", so that, in each side of *G'*, there are now *n*+*r* vertices. Between the copies, we need to add two kinds of linking edges:

- Large-to-large: from each vertex in the larger part of *Gf*, add a zero-cost edge to the corresponding vertex in *Gb*.
- Small-to-small: if the original graph does not have a one-sided-perfect matching, then from each vertex in the smaller part of *Gf*, add a very-high-cost edge to the corresponding vertex in *Gb*.

All in all, at most $n+r$ new edges are required. The resulting graph always has a perfect matching of size $n+r$ . A minimum-cost perfect matching in this graph must consist of minimum-cost maximum-cardinality matchings in *Gf* and *Gb.* The main problem with this doubling technique is that there is no speed gain when $r\ll n$ .

Instead of using reduction, the unbalanced assignment problem can be solved by directly generalizing existing algorithms for balanced assignment. The Hungarian algorithm can be generalized to solve the problem in $O(ms+s^{2}\log r)$ strongly-polynomial time. In particular, if *s*=*r* then the runtime is $O(mr+r^{2}\log r)$ . If the weights are integers, then Thorup's method can be used to get a runtime of $O(ms+s^{2}\log \log r)$ .

### Solution by linear programming

The assignment problem can be solved by presenting it as a linear program. For convenience we will present the maximization problem. Each edge (*i*,*j*), where *i* is in A and *j* is in T, has a weight ${\textstyle w_{ij}}$ . For each edge ⁠ $(i,j)$ ⁠ we have a variable ${\textstyle x_{ij}}$ . The variable is 1 if the edge is contained in the matching and 0 otherwise, so we set the domain constraints: $0\leq x_{ij}\leq 1{\text{ for }}i,j\in A,T,\,$ $x_{ij}\in \mathbb {Z} {\text{ for }}i,j\in A,T.$

The total weight of the matching is: $\sum _{(i,j)\in A\times T}w_{ij}x_{ij}$ . The goal is to find a maximum-weight perfect matching.

To guarantee that the variables indeed represent a perfect matching, we add constraints saying that each vertex is adjacent to exactly one edge in the matching, i.e., ${\begin{aligned}\sum _{j\in T}x_{ij}&=1{\text{ for }}i\in A\\\sum _{i\in A}x_{ij}&=1{\text{ for }}j\in T\end{aligned}}$

All in all we have the following LP:

${\begin{aligned}{\text{maximize}}&\sum _{(i,j)\in A\times T}w_{ij}x_{ij}\\{\text{subject to}}&\sum _{j\in T}x_{ij}=1{\text{ for }}i\in A,\,\sum _{i\in A}x_{ij}=1{\text{ for }}j\in T\\&0\leq x_{ij}\leq 1{\text{ for }}i,j\in A,T\\&x_{ij}\in \mathbb {Z} {\text{ for }}i,j\in A,T\end{aligned}}$ This is an integer linear program. However, we can solve it without the integrality constraints (i.e., drop the last constraint), using standard methods for solving continuous linear programs. While this formulation allows also fractional variable values, in this special case, the LP always has an optimal solution where the variables take integer values. This is because the constraint matrix of the fractional LP is totally unimodular – it satisfies the four conditions of Hoffman and Gale.

### Other methods and approximation algorithms

Other approaches for the assignment problem exist and are reviewed by Duan and Pettie (see Table II). Their work proposes an approximation algorithm for the assignment problem (and the more general maximum-weight matching problem), which runs in linear time for any fixed error bound.

## Many-to-many assignment

In the basic assignment problem, each agent is assigned to at most one task and each task is assigned to at most one agent. In the **many-to-many assignment problem**, each agent *i* may take up to *ci* tasks (*ci* is called the agent's *capacity*), and each task *j* may be taken by up to *dj* agents simultaneously (*dj* is called the task's *capacity*). If the sums of capacities in both sides are equal ( $\sum _{i}c_{i}=\sum _{j}d_{j}$ ), then the problem is *balanced*, and the goal is to find a perfect matching (assign exactly *ci* tasks to each agent *i* and exactly *dj* agents to each task *j*) such that the total cost is as small as possible.

The problem can be solved by reduction to the minimum cost network flow problem. Construct a flow network with the following layers:

- Layer 1: One source-node **s**.
- Layer 2: a node for each agent. There is an arc from **s** to each agent *i*, with cost 0 and capacity *ci* .
- Level 3: a node for each task. There is an arc from each agent *i* to each task *j*, with the corresponding cost, and capacity 1.
- Level 4: One sink-node **t**. There is an arc from each task to **t**, with cost 0 and capacity *dj*.

An integral maximum flow of minimum cost can be found in polynomial time; see network flow problem. Every integral maximum flow in this network corresponds to a matching in which at most *ci* tasks are assigned to each agent *i* and at most *dj* agents are assigned to each task *j* (in the balanced case, exactly *ci* tasks are assigned to *i* and exactly *dj* agents are assigned to *j*). A min-cost maximum flow corresponds to a min-cost assignment.

## Generalization

When phrased as a graph theory problem, the assignment problem can be extended from bipartite graphs to arbitrary graphs. The corresponding problem, of finding a matching in a weighted graph where the sum of weights is maximized, is called the maximum-weight matching problem.

Another generalization of the assignment problem is extending the number of sets to be matched from two to many. So that rather than matching agents to tasks, the problem is extended to matching agents to tasks to time intervals to locations. This results in Multidimensional assignment problem.

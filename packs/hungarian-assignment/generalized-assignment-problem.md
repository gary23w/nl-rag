---
title: "Generalized assignment problem"
source: https://en.wikipedia.org/wiki/Generalized_assignment_problem
domain: hungarian-assignment
license: CC-BY-SA-4.0
tags: hungarian algorithm, assignment problem, kuhn munkres method, cost matrix
fetched: 2026-07-02
---

# Generalized assignment problem

In applied mathematics, the maximum **generalized assignment problem** is a problem in combinatorial optimization. This problem is a generalization of the assignment problem in which both tasks and agents have a size. Moreover, the size of each task might vary from one agent to the other.

This problem in its most general form is as follows: There are a number of agents and a number of tasks. Any agent can be assigned to perform any task, incurring some cost and profit that may vary depending on the agent-task assignment. Moreover, each agent has a budget and the sum of the costs of tasks assigned to it cannot exceed this budget. It is required to find an assignment in which all agents do not exceed their budget and total profit of the assignment is maximized.

## In special cases

In the special case in which all the agents' budgets and all tasks' costs are equal to 1, this problem reduces to the assignment problem. When the costs and profits of all tasks do not vary between different agents, this problem reduces to the multiple knapsack problem. If there is a single agent, then, this problem reduces to the knapsack problem.

## Explanation of definition

In the following, we have *n* kinds of items, $a_{1}$ through $a_{n}$ and *m* kinds of bins $b_{1}$ through $b_{m}$ . Each bin $b_{i}$ is associated with a budget $t_{i}$ . For a bin $b_{i}$ , each item $a_{j}$ has a profit $p_{ij}$ and a weight $w_{ij}$ . A solution is an assignment from items to bins. A feasible solution is a solution in which for each bin $b_{i}$ the total weight of assigned items is at most $t_{i}$ . The solution's profit is the sum of profits for each item-bin assignment. The goal is to find a maximum profit feasible solution.

Mathematically the generalized assignment problem can be formulated as an integer program:

${\begin{aligned}{\text{maximize }}&\sum _{i=1}^{m}\sum _{j=1}^{n}p_{ij}x_{ij}.\\{\text{subject to }}&\sum _{j=1}^{n}w_{ij}x_{ij}\leq t_{i}&&i=1,\ldots ,m;\\&\sum _{i=1}^{m}x_{ij}\leq 1&&j=1,\ldots ,n;\\&x_{ij}\in \{0,1\}&&i=1,\ldots ,m,\quad j=1,\ldots ,n;\end{aligned}}$

## Complexity

The generalized assignment problem is NP-hard. However, there are linear-programming relaxations which give a $(1-1/e)$ -approximation.

## Greedy approximation algorithm

For the problem variant in which not every item must be assigned to a bin, there is a family of algorithms for solving the GAP by using a combinatorial translation of any algorithm for the knapsack problem into an approximation algorithm for the GAP.

Using any $\alpha$ -approximation algorithm ALG for the knapsack problem, it is possible to construct a ( $\alpha +1$ )-approximation for the generalized assignment problem in a greedy manner using a residual profit concept. The algorithm constructs a schedule in iterations, where during iteration j a tentative selection of items to bin $b_{j}$ is selected. The selection for bin $b_{j}$ might change as items might be reselected in a later iteration for other bins. The residual profit of an item $x_{i}$ for bin $b_{j}$ is $p_{ij}$ if $x_{i}$ is not selected for any other bin or $p_{ij}$ – $p_{ik}$ if $x_{i}$ is selected for bin $b_{k}$ .

Formally: We use a vector T to indicate the tentative schedule during the algorithm. Specifically, $T[i]=j$ means the item $x_{i}$ is scheduled on bin $b_{j}$ and $T[i]=-1$ means that item $x_{i}$ is not scheduled. The residual profit in iteration j is denoted by $P_{j}$ , where $P_{j}[i]=p_{ij}$ if item $x_{i}$ is not scheduled (i.e. $T[i]=-1$ ) and $P_{j}[i]=p_{ij}-p_{ik}$ if item $x_{i}$ is scheduled on bin $b_{k}$ (i.e. $T[i]=k$ ).

Formally:

Set

$T[i]=-1{\text{ for }}i=1\ldots n$

For

$j=1,\ldots ,m$

do:

Call ALG to find a solution to bin

$b_{j}$

using the residual profit function

$P_{j}$

. Denote the selected items by

$S_{j}$

.

Update

T

using

$S_{j}$

, i.e.,

$T[i]=j$

for all

$i\in S_{j}$

.

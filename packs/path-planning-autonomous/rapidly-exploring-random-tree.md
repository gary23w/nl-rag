---
title: "Rapidly exploring random tree"
source: https://en.wikipedia.org/wiki/Rapidly_exploring_random_tree
domain: path-planning-autonomous
license: CC-BY-SA-4.0
tags: motion planning, rapidly exploring random tree, occupancy grid, trajectory optimization
fetched: 2026-07-02
---

# Rapidly exploring random tree

A visualization of an RRT graph after 45 and 390 iterations

An animation of an RRT starting from iteration 0 to 10000

A **rapidly exploring random tree** (RRT) is an algorithm designed to efficiently search nonconvex, high-dimensional spaces by randomly building a space-filling tree. The tree is constructed incrementally from samples drawn randomly from the search space and is inherently biased to grow towards large unsearched areas of the problem. RRTs were developed by Steven M. LaValle and James J. Kuffner Jr. They easily handle problems with obstacles and differential constraints (nonholonomic and kinodynamic) and have been widely used in autonomous robotic motion planning.

RRTs can be viewed as a technique to generate open-loop trajectories for nonlinear systems with state constraints. An RRT can also be considered as a Monte-Carlo method to bias search into the largest Voronoi regions of a graph in a configuration space. Some variations can even be considered stochastic fractals.

RRTs can be used to compute approximate control policies to control high dimensional nonlinear systems with state and action constraints.

## Description

An RRT grows a tree rooted at the starting configuration by using random samples from the search space. As each sample is drawn, a connection is attempted between it and the nearest state in the tree. If the connection is feasible (passes entirely through free space and obeys any constraints), this results in the addition of the new state to the tree. With uniform sampling of the search space, the probability of expanding an existing state is proportional to the size of its Voronoi region. As the largest Voronoi regions belong to the states on the frontier of the search, this means that the tree preferentially expands towards large unsearched areas.

The length of the connection between the tree and a new state is frequently limited by a growth factor. If the random sample is further from its nearest state in the tree than this limit allows, a new state at the maximum distance from the tree along the line to the random sample is used instead of the random sample itself. The random samples can then be viewed as controlling the direction of the tree growth while the growth factor determines its rate. This maintains the space-filling bias of the RRT while limiting the size of the incremental growth.

RRT growth can be biased by increasing the probability of sampling states from a specific area. Most practical implementations of RRTs make use of this to guide the search towards the planning problem goals. This is accomplished by introducing a small probability of sampling the goal to the state sampling procedure. The higher this probability, the more greedily the tree grows towards the goal.

## Algorithm

For a general configuration space *C*, the algorithm in pseudocode is as follows:

```
Algorithm BuildRRT
    Input: Initial configuration qinit, number of vertices in RRT K, incremental distance Δq
    Output: RRT graph G

    G.init(qinit)
    for k = 1 to K do
        qrand ← RAND_CONF()
        qnear ← NEAREST_VERTEX(qrand, G)
        qnew ← NEW_CONF(qnear, qrand, Δq)
        G.add_vertex(qnew)
        G.add_edge(qnear, qnew)
    return G
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

In the algorithm above, "**RAND_CONF**" grabs a random configuration *q**rand* in *C*. This may be replaced with a function "**RAND_FREE_CONF**" that uses samples in *C**free*, while rejecting those in *C**obs* using some collision detection algorithm.

"**NEAREST_VERTEX**" is a function that runs through all vertices *v* in graph *G*, calculates the distance between *q**rand* and *v* using some measurement function thereby returning the nearest vertex.

"**NEW_CONF**" selects a new configuration *q**new* by moving an incremental distance *Δq* from *q**near* in the direction of *q**rand*. (According to in holonomic problems, this should be omitted and *q**rand* used instead of *q**new*.)

## Variants and improvements for motion planning

It has been shown that, under 'mild technical conditions', the cost of the best path in the RRT converges almost surely to a non-optimal value. For that reason, it is desirable to find variants of the RRT that converges to an optimum, like RRT*. Below follows is a list of RRT*-based methods (starting with RRT* itself). Not all of the derived methods do themselves converge to an optimum, though.

- Rapidly exploring random graph (RRG) and RRT*, a variant of RRT that converges towards an optimal solution

- LQR-RRT, a kinodynamic variant for complex or underactuated dynamics

- RRT**+**, a family of RRT-based planners aiming to generate solutions for high-dimensional systems in real-time, by progressively searching in lower-dimensional subspaces.

- RRT*-Smart, a method for accelerating the convergence rate of RRT* by using path optimization (in a similar fashion to Theta*) and intelligent sampling (by biasing sampling towards path vertices, which – after path optimization – are likely to be close to obstacles)

- A*-RRT and A*-RRT*, a two-phase motion planning method that uses a graph search algorithm to search for an initial feasible path in a low-dimensional space (not considering the complete state space) in a first phase, avoiding hazardous areas and preferring low-risk routes, which is then used to focus the RRT* search in the continuous high-dimensional space in a second phase

- RRT*FN, RRT* with a fixed number of nodes, which randomly removes a leaf node in the tree in every iteration

- RRT*-AR, sampling-based alternate routes planning

- Informed RRT*, improves the convergence speed of RRT* by introducing a heuristic, similar to the way in which A* improves upon Dijkstra's algorithm

- Real-Time RRT* (RT-RRT*), a variant of RRT* and informed RRT* that uses an online tree rewiring strategy that allows the tree root to move with the agent without discarding previously sampled paths, in order to obtain real-time path-planning in a dynamic environment such as a computer game

- RRTX and RRT#, optimization of RRT* for dynamic environments

- Theta*-RRT, a two-phase motion planning method similar to A*-RRT* that uses a hierarchical combination of any-angle search with RRT motion planning for fast trajectory generation in environments with complex nonholonomic constraints

- RRT* FND, extension of RRT* for -dynamic environments
- RRT-GPU, three-dimensional RRT implementation that utilizes hardware acceleration

- APF-RRT, a combination of RRT planner with Artificial Potential Fields method that simplify the replanning task

- CERRT, a RRT planner modeling uncertainty, which is reduced exploiting contacts
- MVRRT*, Minimum violation RRT*, an algorithm that finds the shortest route that minimizes the level of unsafety (the "cost" of the environment rules that have been violated, e.g. traffic laws)

- RRT-Blossom, RRT planner for highly constrained environments.

- RRV, efficiently expand the tree around obstacles and through narrow passages, using dominant eigenvectors around tree nodes.

- RBT, uses simple distance computations in the workspace to expand the tree instead of expensive collision check.

- TB-RRT, Time-based RRT algorithm for rendezvous planning of two dynamic systems.

- RRdT*, a RRT*-based planner that uses multiple local trees to actively balances the exploration and exploitation of the space by performing local sampling.

- Tri-RRT-Connect, Triangular inequality-based rewiring method with RRT-Connect algorithm to bring it closer to the optimum.

- RRT-Rope, a method for fast near-optimal path planning using a deterministic shortening approach, very effective in open and large environments.

- Parti-game directed RRTs (PDRRTs), a method that combines RRTs with the parti-game method to refine the search where it is needed (for example around obstacles) to be able to plan faster and solve more motion planning problems than RRT

- Closed-loop rapidly exploring random (CL-RRT), an extension of RRT that samples an input to a stable closed-loop system consisting of the vehicle and a controller

- Adaptively informed trees (AIT*) and effort informed trees (EIT*)

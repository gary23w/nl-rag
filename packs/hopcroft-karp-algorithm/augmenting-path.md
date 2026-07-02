---
title: "Flow network"
source: https://en.wikipedia.org/wiki/Augmenting_path
domain: hopcroft-karp-algorithm
license: CC-BY-SA-4.0
tags: hopcroft karp algorithm, bipartite matching, augmenting path, maximum cardinality matching
fetched: 2026-07-02
---

# Flow network

(Redirected from

Augmenting path

)

In graph theory, a **flow network** (also known as a **transportation network**) is a directed graph where each edge has a **capacity** and each edge receives a flow. The amount of flow on an edge cannot exceed the capacity of the edge. Often in operations research, a directed graph is called a **network**, the vertices are called **nodes** and the edges are called **arcs**. A flow must satisfy the restriction that the amount of flow into a node equals the amount of flow out of it, unless it is a **source**, which has only outgoing flow, or **sink**, which has only incoming flow. A flow network can be used to model traffic in a computer network, circulation with demands, fluids in pipes, currents in an electrical circuit, or anything similar in which something travels through a network of nodes. As such, efficient algorithms for solving network flows can also be applied to solve problems that can be reduced to a flow network, including survey design, airline scheduling, image segmentation, and the matching problem.

## Definition

A **network** is a directed graph *G* = (*V*, *E*) with a non-negative **capacity** function *c* for each edge, and without multiple arcs (i.e. edges with the same source and target nodes). Without loss of generality, we may assume that if (*u*, *v*) ∈ *E*, then (*v*, *u*) is also a member of E. Additionally, if (*v*, *u*) ∉ *E* then we may add (*v*, *u*) to E and then set the *c*(*v*, *u*) = 0.

If two nodes in G are distinguished – one as the source s and the other as the sink t – then (*G*, *c*, *s*, *t*) is called a **flow network**.

## Flows

Flow functions model the net flow of units between pairs of nodes, and are useful when asking questions such as *what is the maximum number of units that can be transferred from the source node s to the sink node t?* The amount of flow between two nodes is used to represent the net amount of units being transferred from one node to the other.

The **excess** function *x**f* : *V* → ℝ represents the net flow entering a given node u (i.e. the sum of the flows entering u) and is defined by $x_{f}(u)=\sum _{w\in V}f(w,u)-\sum _{w\in V}f(u,w).$ A node u is said to be **active** if *x**f* (*u*) > 0 (i.e. the node u consumes flow), **deficient** if *x**f* (*u*) < 0 (i.e. the node u produces flow), or **conserving** if *x**f* (*u*) = 0. In flow networks, the source s is deficient, and the sink t is active. Pseudo-flows, feasible flows, and pre-flows are all examples of flow functions.

A

pseudo-flow

is a function

f

of each edge in the network that satisfies the following two constraints for all nodes

u

and

v

:

- *Skew symmetry constraint*: The flow on an arc from u to v is equivalent to the negation of the flow on the arc from v to u, that is: *f* (*u*, *v*) = −*f* (*v*, *u*). The sign of the flow indicates the flow's direction.
- *Capacity constraint*: An arc's flow cannot exceed its capacity, that is: *f* (*u*, *v*) ≤ *c*(*u*, *v*).

A

pre-flow

is a pseudo-flow that, for all

v

∈

V

\{

s

}

, satisfies the additional constraint:

- *Non-deficient flows*: The net flow *entering* the node v is non-negative, except for the source, which "produces" flow. That is: *x**f* (*v*) ≥ 0 for all *v* ∈ *V* \{*s*}.

A

feasible flow

, or just a

flow

, is a pseudo-flow that, for all

v

∈

V

\{

s

,

t

}

, satisfies the additional constraint:

- *Flow conservation constraint*: The total net flow entering a node v is zero for all nodes in the network except the source s and the sink t, that is: *x**f* (*v*) = 0 for all *v* ∈ *V* \{*s*, *t*}. In other words, for all nodes in the network except the source s and the sink t, the total sum of the incoming flow of a node is equal to its outgoing flow (i.e. $\sum _{(u,v)\in E}f(u,v)=\sum _{(v,z)\in E}f(v,z)$ , for each vertex *v* ∈ *V* \{*s*, *t*}).

The **value** |*f*| of a feasible flow f for a network, is the net flow into the sink t of the flow network, that is: |*f*| = *x**f* (*t*). Note, the flow value in a network is also equal to the total outgoing flow of source s, that is: |*f*| = −*x**f* (*s*). Also, if we define *A* as a set of nodes in *G* such that *s* ∈ *A* and *t* ∉ *A*, the flow value is equal to the total net flow going out of A (i.e. |*f*| = *f* out(*A*) − *f* in(*A*)). The flow value in a network is the total amount of flow from s to t.

## Concepts useful to flow problems

### Flow decomposition

Flow decomposition is a process of breaking down a given flow into a collection of path flows and cycle flows. Every flow through a network can be decomposed into one or more paths and corresponding quantities, such that each edge in the flow equals the sum of all quantities of paths that pass through it. Flow decomposition is a powerful tool in optimization problems to maximize or minimize specific flow parameters.

### Adding arcs and flows

We do not use multiple arcs within a network because we can combine those arcs into a single arc. To combine two arcs into a single arc, we add their capacities and their flow values, and assign those to the new arc:

- Given any two nodes u and v, having two arcs from u to v with capacities *c*1(*u,v*) and *c*2(*u,v*) respectively is equivalent to considering only a single arc from u to v with a capacity equal to *c*1(*u,v*)+*c*2(*u,v*).
- Given any two nodes u and v, having two arcs from u to v with pseudo-flows *f*1(*u,v*) and *f*2(*u,v*) respectively is equivalent to considering only a single arc from u to v with a pseudo-flow equal to *f*1(*u,v*)+*f*2(*u,v*).

Along with the other constraints, the skew symmetry constraint must be remembered during this step to maintain the direction of the original pseudo-flow arc. Adding flow to an arc is the same as adding an arc with the capacity of zero.

### Residuals

The **residual capacity** of an arc e with respect to a pseudo-flow f is denoted *c**f*, and it is the difference between the arc's capacity and its flow. That is, *c**f* (*e*) = *c*(*e*) − *f*(*e*). From this we can construct a **residual network**, denoted *G**f* (*V*, *E**f*), with a capacity function *c**f* which models the amount of *available* capacity on the set of arcs in *G* = (*V*, *E*). More specifically, capacity function *c**f* of each arc (*u*, *v*) in the residual network represents the amount of flow which can be transferred from u to v given the current state of the flow within the network.

This concept is used in Ford–Fulkerson algorithm which computes the maximum flow in a flow network.

Note that there can be an unsaturated path (a path with available capacity) from u to v in the residual network, even though there is no such path from u to v in the original network. Since flows in opposite directions cancel out, *decreasing* the flow from v to u is the same as *increasing* the flow from u to v.

### Augmenting paths

An **augmenting path** is a path (*u*1, *u*2, ..., *u**k*) in the residual network, where *u*1 = *s*, *u**k* = *t*, and for all *u**i*, *u**i* + 1 (*c**f* (*u**i*, *u**i* + 1) > 0) (1 ≤ i < k). More simply, an augmenting path is an available flow path from the source to the sink. A network is at maximum flow if and only if there is no augmenting path in the residual network *G**f*.

The **bottleneck** is the minimum residual capacity of all the edges in a given augmenting path. See example explained in the "Example" section of this article. The flow network is at maximum flow if and only if it has a bottleneck with a value equal to zero. If any augmenting path exists, its bottleneck weight will be greater than 0. In other words, if there is a bottleneck value greater than 0, then there is an augmenting path from the source to the sink. However, we know that if there is any augmenting path, then the network is not at maximum flow, which in turn means that, if there is a bottleneck value greater than 0, then the network is not at maximum flow.

The term "augmenting the flow" for an augmenting path means updating the flow f of each arc in this augmenting path to equal the capacity *c* of the bottleneck. Augmenting the flow corresponds to pushing additional flow along the augmenting path until there is no remaining available residual capacity in the bottleneck.

### Multiple sources and/or sinks

Sometimes, when modeling a network with more than one source, a **supersource** is introduced to the graph. This consists of a vertex connected to each of the sources with edges of infinite capacity, so as to act as a global source. A similar construct for sinks is called a **supersink**.

## Example

In Figure 1 you see a flow network with source labeled s, sink t, and four additional nodes. The flow and capacity is denoted $f/c$ . Notice how the network upholds the capacity constraint and flow conservation constraint. The total amount of flow from s to t is 5, which can be easily seen from the fact that the total outgoing flow from s is 5, which is also the incoming flow to t. By the skew symmetry constraint, from c to a is -2 because the flow from a to c is 2.

In Figure 2 you see the residual network for the same given flow. Notice how there is positive residual capacity on some edges where the original capacity is zero in Figure 1, for example for the edge $(d,c)$ . This network is not at maximum flow. There is available capacity along the paths $(s,a,c,t)$ , $(s,a,b,d,t)$ and $(s,a,b,d,c,t)$ , which are then the augmenting paths.

The bottleneck of the $(s,a,c,t)$ path is equal to $\min(c(s,a)-f(s,a),c(a,c)-f(a,c),c(c,t)-f(c,t))$ $=\min(c_{f}(s,a),c_{f}(a,c),c_{f}(c,t))$ $=\min(5-3,3-2,2-1)$ $=\min(2,1,1)=1$ .

## Applications

Picture a series of water pipes, fitting into a network. Each pipe is of a certain diameter, so it can only maintain a flow of a certain amount of water. Anywhere that pipes meet, the total amount of water coming into that junction must be equal to the amount going out, otherwise we would quickly run out of water, or we would have a buildup of water. We have a water inlet, which is the source, and an outlet, the sink. A flow would then be one possible way for water to get from source to sink so that the total amount of water coming out of the outlet is consistent. Intuitively, the total flow of a network is the rate at which water comes out of the outlet.

Flows can pertain to people or material over transportation networks, or to electricity over electrical distribution systems. For any such physical network, the flow coming into any intermediate node needs to equal the flow going out of that node. This conservation constraint is equivalent to Kirchhoff's current law.

Flow networks also find applications in ecology: flow networks arise naturally when considering the flow of nutrients and energy between different organisms in a food web. The mathematical problems associated with such networks are quite different from those that arise in networks of fluid or traffic flow. The field of ecosystem network analysis, developed by Robert Ulanowicz and others, involves using concepts from information theory and thermodynamics to study the evolution of these networks over time.

## Classifying flow problems

The simplest and most common problem using flow networks is to find what is called the maximum flow, which provides the largest possible total flow from the source to the sink in a given graph. There are many other problems which can be solved using max flow algorithms, if they are appropriately modeled as flow networks, such as bipartite matching, the assignment problem and the transportation problem. Maximum flow problems can be solved in polynomial time with various algorithms (see table). The max-flow min-cut theorem states that finding a maximal network flow is equivalent to finding a cut of minimum capacity that separates the source and the sink, where a cut is the division of vertices such that the source is in one division and the sink is in another.

| Inventor(s) | Year | Time complexity (with *n* nodes and *m* arcs) |
|---|---|---|
| Dinic's algorithm | 1970 | *O*(*mn*2) |
| Edmonds–Karp algorithm | 1972 | *O*(*m*2*n*) |
| MPM (Malhotra, Pramodh-Kumar, and Maheshwari) algorithm | 1978 | *O*(*n*3) |
| Push–relabel algorithm (Goldberg & Tarjan) | 1988 | *O*(*n*2*m*) |
| James B. Orlin | 2013 | *O*(*mn*) |
| Li Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg, Sushant Sachdeva | 2022 | $O(m^{1+o(1)})$ |

In a multi-commodity flow problem, you have multiple sources and sinks, and various "commodities" which are to flow from a given source to a given sink. This could be for example various goods that are produced at various factories, and are to be delivered to various given customers through the *same* transportation network.

In a minimum cost flow problem, each edge $u,v$ has a given cost $k(u,v)$ , and the cost of sending the flow $f(u,v)$ across the edge is $f(u,v)\cdot k(u,v)$ . The objective is to send a given amount of flow from the source to the sink, at the lowest possible price.

In a circulation problem, you have a lower bound $\ell (u,v)$ on the edges, in addition to the upper bound $c(u,v)$ . Each edge also has a cost. Often, flow conservation holds for *all* nodes in a circulation problem, and there is a connection from the sink back to the source. In this way, you can dictate the total flow with $\ell (t,s)$ and $c(t,s)$ . The flow *circulates* through the network, hence the name of the problem.

In a **network with gains** or **generalized network** each edge has a **gain**, a real number (not zero) such that, if the edge has gain *g*, and an amount *x* flows into the edge at its tail, then an amount *gx* flows out at the head.

In a **source localization problem**, an algorithm tries to identify the most likely source node of information diffusion through a partially observed network. This can be done in linear time for trees and cubic time for arbitrary networks and has applications ranging from tracking mobile phone users to identifying the originating source of disease outbreaks.

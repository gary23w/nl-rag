---
title: "Max-flow min-cut theorem"
source: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
domain: dinic-algorithm
license: CC-BY-SA-4.0
tags: dinic algorithm, maximum flow, blocking flow, level graph
fetched: 2026-07-02
---

# Max-flow min-cut theorem

In computer science and optimization theory, the **max-flow min-cut theorem** states that in a flow network, the maximum amount of flow passing from the *source* to the *sink* is equal to the total weight of the edges in a minimum cut, i.e., the smallest total weight of the edges which if removed would disconnect the source from the sink.

For example, imagine a network of pipes carrying water from a reservoir (the source) to a city (the sink). Each pipe has a capacity representing the maximum amount of water that can flow through it per unit of time. The max-flow min-cut theorem tells us that the maximum amount of water that can reach the city is limited by the smallest total capacity of any set of pipes that, if cut, would completely isolate the reservoir from the city. This smallest total capacity is the min-cut. So, if there's a bottleneck in the pipe network, represented by a small min-cut, that bottleneck will determine the overall maximum flow of water to the city.

This is a special case of the duality theorem for linear programs and can be used to derive Menger's theorem and the Kőnig–Egerváry theorem.

## Definitions and statement

The theorem equates two quantities: the maximum flow through a network, and the minimum capacity of a cut of the network. To state the theorem, each of these notions must first be defined.

### Network

A **network** consists of

- a finite directed graph *G* = (*V*, *E*), where *V* denotes the finite set of vertices and *E* ⊆ *V*×*V* is the set of directed edges;
- a **source** *s* ∈ *V* and a **sink** *t* ∈ *V*;
- a **capacity** function, which is a mapping $c:E\to \mathbb {R} ^{+}$ denoted by cuv or *c*(*u*, *v*) for (*u*,*v*) ∈ *E*. It represents the maximum amount of flow that can pass through an edge.

### Flows

A **flow** through a network is a mapping $f:E\to \mathbb {R} ^{+}$ denoted by $f_{uv}$ or $f(u,v)$ , subject to the following two constraints:

1. **Capacity Constraint**: For every edge $(u,v)\in E$ , $f_{uv}\leq c_{uv}.$
2. **Conservation of Flows**: For each vertex v apart from s and t (i.e. the source and sink, respectively), the following equality holds: $\sum \nolimits _{\{u:(u,v)\in E\}}f_{uv}=\sum \nolimits _{\{w:(v,w)\in E\}}f_{vw}.$

A flow can be visualized as a physical flow of a fluid through the network, following the direction of each edge. The capacity constraint then says that the volume flowing through each edge per unit time is less than or equal to the maximum capacity of the edge, and the conservation constraint says that the amount that flows into each vertex equals the amount flowing out of each vertex, apart from the source and sink vertices.

The **value** of a flow is defined by

$|f|=\sum \nolimits _{\{v:(s,v)\in E\}}f_{sv}=\sum \nolimits _{\{v:(v,t)\in E\}}f_{vt},$

where as above s is the source and t is the sink of the network. In the fluid analogy, it represents the amount of fluid entering the network at the source. Because of the conservation axiom for flows, this is the same as the amount of flow leaving the network at the sink.

The maximum flow problem asks for the largest flow on a given network.

> **Maximum Flow Problem.** Maximize $|f|$ , that is, to route as much flow as possible from s to t .

### Cuts

The other half of the max-flow min-cut theorem refers to a different aspect of a network: the collection of cuts. An **s-t cut** *C* = (*S*, *T*) is a partition of V such that *s* ∈ *S* and *t* ∈ *T*. That is, an *s*-*t* cut is a division of the vertices of the network into two parts, with the source in one part and the sink in the other. The **cut-set** $X_{C}$ of a cut C is the set of edges that connect the source part of the cut to the sink part:

${\displaystyle X_{C}:=\{(u,v)\in E\$

Thus, if all the edges in the cut-set of C are removed, then no positive flow is possible, because there is no path in the resulting graph from the source to the sink.

The **capacity** of an *s-t cut* is the sum of the capacities of the edges in its cut-set,

$c(S,T)=\sum \nolimits _{(u,v)\in X_{C}}c_{uv}=\sum \nolimits _{(i,j)\in E}c_{ij}d_{ij},$

where $d_{ij}=1$ if $i\in S$ and $j\in T$ , 0 otherwise.

There are typically many cuts in a graph, but cuts with smaller weights are often more difficult to find.

Minimum s-t Cut Problem.

Minimize

c

(

S

,

T

)

, that is, determine

S

and

T

such that the capacity of the s-t cut is minimal.

### Main theorem

In the above situation, one can prove that the value of any flow through a network is less than or equal to the capacity of any *s-t* cut, and that furthermore a flow with maximal value and a cut with minimal capacity exist. The main theorem links the maximum flow value with the minimum cut capacity of the network.

Max-flow min-cut theorem.

The maximum value of an s-t flow is equal to the minimum capacity over all s-t cuts.

## Example

The figure on the right shows a flow in a network. The numerical annotation on each arrow, in the form *f*/*c*, indicates the flow (*f*) and the capacity (*c*) of the arrow. The flows emanating from the source total five (2+3=5), as do the flows into the sink (2+3=5), establishing that the flow's value is 5.

One *s*-*t* cut with value 5 is given by *S*={*s*,*p*} and *T*={*o*, *q*, *r*, *t*}. The capacities of the edges that cross this cut are 3 and 2, giving a cut capacity of 3+2=5. (The arrow from *o* to *p* is not considered, as it points from *T* back to *S*.)

The value of the flow is equal to the capacity of the cut, showing that the flow is a maximal flow and the cut is a minimal cut.

Note that the flow through each of the two arrows that connect *S* to *T* is at full capacity; this is always the case: a minimal cut represents a 'bottleneck' of the system.

## Linear program formulation

The max-flow problem and min-cut problem can be formulated as two primal-dual linear programs.

|   | Max-flow (Primal) | Min-cut (Dual) |
|---|---|---|
| **variables** | $f_{uv}$ $\forall (u,v)\in E$ *[two variables per edge, one in each direction]* | $d_{uv}$ $\forall (u,v)\in E$ *[a variable per edge]* $z_{v}$ $\forall v\in V\setminus \{s,t\}$ *[a variable per non-terminal node]* |
| **objective** | maximize $\sum \nolimits _{v:(s,v)\in E}f_{sv}$ *[max total flow from source]* | minimize $\sum \nolimits _{(u,v)\in E}c_{uv}d_{uv}$ *[min total capacity of edges in cut]* |
| **constraints** | subject to ${\begin{aligned}f_{uv}&\leq c_{uv}&&\forall (u,v)\in E\\\sum _{u}f_{uv}-\sum _{w}f_{vw}&=0&&v\in V\setminus \{s,t\}\end{aligned}}$ *[a constraint per edge and a constraint per non-terminal node]* | subject to ${\begin{aligned}d_{uv}-z_{u}+z_{v}&\geq 0&&\forall (u,v)\in E,u\neq s,v\neq t\\d_{sv}+z_{v}&\geq 1&&\forall (s,v)\in E,v\neq t\\d_{ut}-z_{u}&\geq 0&&\forall (u,t)\in E,u\neq s\\d_{st}&\geq 1&&{\text{if }}(s,t)\in E\end{aligned}}$ *[a constraint per edge]* |
| **sign constraints** | ${\begin{aligned}f_{uv}&\geq 0&&\forall (u,v)\in E\\\end{aligned}}$ | ${\begin{aligned}d_{uv}&\geq 0&&\forall (u,v)\in E\\z_{v}&\in \mathbb {R} &&\forall v\in V\setminus \{s,t\}\end{aligned}}$ |

The max-flow LP is straightforward. The dual LP is obtained using the algorithm described in dual linear program: the variables and sign constraints of the dual correspond to the constraints of the primal, and the constraints of the dual correspond to the variables and sign constraints of the primal. The resulting LP requires some explanation. The interpretation of the variables in the min-cut LP is:

$d_{uv}={\begin{cases}1,&{\text{if }}u\in S{\text{ and }}v\in T{\text{ (the edge }}uv{\text{ is in the cut) }}\\0,&{\text{otherwise}}\end{cases}}$

$z_{v}={\begin{cases}1,&{\text{if }}v\in S\\0,&{\text{otherwise}}\end{cases}}$

The minimization objective sums the capacity over all the edges that are contained in the cut.

The constraints guarantee that the variables indeed represent a legal cut:

- The constraints $d_{uv}-z_{u}+z_{v}\geq 0$ (equivalent to $d_{uv}\geq z_{u}-z_{v}$ ) guarantee that, for non-terminal nodes *u,v*, if *u* is in *S* and *v* is in *T*, then the edge (*u*,*v*) is counted in the cut ( $d_{uv}\geq 1$ ).
- The constraints $d_{sv}+z_{v}\geq 1$ (equivalent to $d_{sv}\geq 1-z_{v}$ ) guarantee that, if *v* is in *T*, then the edge *(s,v)* is counted in the cut (since *s* is by definition in *S*).
- The constraints $d_{ut}-z_{u}\geq 0$ (equivalent to $d_{ut}\geq z_{u}$ ) guarantee that, if *u* is in *S*, then the edge *(u,t)* is counted in the cut (since *t* is by definition in *T*).

Note that, since this is a minimization problem, we do not have to guarantee that an edge is *not* in the cut - we only have to guarantee that each edge that should be in the cut, is summed in the objective function.

The equality in the **max-flow min-cut theorem** follows from the strong duality theorem in linear programming, which states that if the primal program has an optimal solution, *x**, then the dual program also has an optimal solution, *y**, such that the optimal values formed by the two solutions are equal.

## Application

### Cederbaum's maximum flow theorem

The maximum flow problem can be formulated as the maximization of the electrical current through a network composed of nonlinear resistive elements. In this formulation, the limit of the current  *I*in between the input terminals of the electrical network as the input voltage *V*in approaches $\infty$ , is equal to the weight of the minimum-weight cut set.

$\lim _{V_{\text{in}}\to \infty }(I_{in})=\min _{X_{C}}\sum _{(u,v)\in X_{C}}c_{uv}$

### Generalized max-flow min-cut theorem

In addition to edge capacity, consider there is capacity at each vertex, that is, a mapping $c:V\to \mathbb {R} ^{+}$ denoted by *c*(*v*), such that the flow  *f*  has to satisfy not only the capacity constraint and the conservation of flows, but also the vertex capacity constraint

$\forall v\in V\setminus \{s,t\}:\qquad \sum \nolimits _{\{u\in V\mid (u,v)\in E\}}f_{uv}\leq c(v).$

In other words, the amount of *flow* passing through a vertex cannot exceed its capacity. Define an *s-t cut* to be the set of vertices and edges such that for any path from *s* to *t*, the path contains a member of the cut. In this case, the *capacity of the cut* is the sum of the capacity of each edge and vertex in it.

In this new definition, the **generalized max-flow min-cut theorem** states that the maximum value of an s-t flow is equal to the minimum capacity of an s-t cut in the new sense.

### Menger's theorem

In the undirected edge-disjoint paths problem, we are given an undirected graph *G* = (*V*, *E*) and two vertices s and t, and we have to find the maximum number of edge-disjoint s-t paths in G.

**Menger's theorem** states that the maximum number of edge-disjoint s-t paths in an undirected graph is equal to the minimum number of edges in an s-t cut-set.

### Project selection problem

In the project selection problem, there are n projects and m machines. Each project pi yields revenue *r*(*pi*) and each machine qj costs *c*(*qj*) to purchase. We want to select a subset of the project, and purchase a subset of the machines, to maximize the total profit (revenue of the selected projects minus cost of the purchased machines). We must obey the following constraint: each project specifies a set of machines which must be purchased if the project is selected. (Each machine, once purchased, can be used by any selected project.)

To solve the problem, let P be the set of projects *not* selected and Q be the set of machines purchased, then the problem can be formulated as,

$\max\{g\}=\sum _{i}r(p_{i})-\sum _{p_{i}\in P}r(p_{i})-\sum _{q_{j}\in Q}c(q_{j}).$

Since the first term does not depend on the choice of P and Q, this maximization problem can be formulated as a minimization problem instead, that is,

$\min\{g'\}=\sum _{p_{i}\in P}r(p_{i})+\sum _{q_{j}\in Q}c(q_{j}).$

The above minimization problem can then be formulated as a minimum-cut problem by constructing a network, where the source is connected to the projects with capacity *r*(*pi*), and the sink is connected by the machines with capacity *c*(*qj*). An edge (*pi*, *qj*) with *infinite* capacity is added if project pi requires machine qj. The s-t cut-set represents the projects and machines in P and Q respectively. By the max-flow min-cut theorem, one can solve the problem as a maximum flow problem.

The figure on the right gives a network formulation of the following project selection problem:

|   | Project *r*(*pi*) | Machine *c*(*qj*) |   |
|---|---|---|---|
| 1 | 100 | 200 | Project 1 requires machines 1 and 2. |
| 2 | 200 | 100 | Project 2 requires machine 2. |
| 3 | 150 | 50 | Project 3 requires machine 3. |

The minimum capacity of an s-t cut is 250 and the sum of the revenue of each project is 450; therefore the maximum profit *g* is 450 − 250 = 200, by selecting projects *p*2 and *p*3.

The idea here is to 'flow' each project's profits through the 'pipes' of its machines. If we cannot fill the pipe from a machine, the machine's return is less than its cost, and the min cut algorithm will find it cheaper to cut the project's profit edge instead of the machine's cost edge.

### Image segmentation problem

In the image segmentation problem, there are n pixels. Each pixel i can be assigned a foreground value  fi or a background value bi. There is a penalty of pij if pixels i, j are adjacent and have different assignments. The problem is to assign pixels to foreground or background such that the sum of their values minus the penalties is maximum.

Let P be the set of pixels assigned to foreground and Q be the set of points assigned to background, then the problem can be formulated as,

$\max\{g\}=\sum _{i\in P}f_{i}+\sum _{i\in Q}b_{i}-\sum _{i\in P,j\in Q\lor j\in P,i\in Q}p_{ij}.$

This maximization problem can be formulated as a minimization problem instead, that is,

$\min\{g'\}=\sum _{i\in P,j\in Q\lor j\in P,i\in Q}p_{ij}.$

The above minimization problem can be formulated as a minimum-cut problem by constructing a network where the source (orange node) is connected to all the pixels with capacity  fi, and the sink (purple node) is connected by all the pixels with capacity bi. Two edges (i, j) and (j, i) with pij capacity are added between two adjacent pixels. The s-t cut-set then represents the pixels assigned to the foreground in P and pixels assigned to background in Q.

## History

An account of the discovery of the theorem was given by Ford and Fulkerson in 1962:

"Determining a maximal steady state flow from one point to another in a network subject to capacity limitations on arcs ... was posed to the authors in the spring of 1955 by T.E. Harris, who, in conjunction with General F. S. Ross (Ret.) had formulated a simplified model of railway traffic flow, and pinpointed this particular problem as the central one suggested by the model. It was not long after this until the main result, Theorem 5.1, which we call the max-flow min-cut theorem, was conjectured and established. A number of proofs have since appeared."

## Proof

Let *G* = (*V*, *E*) be a network (directed graph) with s and t being the source and the sink of G respectively.

Consider the flow  *f*  computed for G by Ford–Fulkerson algorithm. In the residual graph (*Gf* ) obtained for G (after the final flow assignment by Ford–Fulkerson algorithm), define two subsets of vertices as follows:

1. A: the set of vertices reachable from s in Gf
2. Ac: the set of remaining vertices i.e. V − A

**Claim.** value( *f* ) = *c*(*A*, *Ac*), where the **capacity** of an *s-t cut* is defined by

$c(S,T)=\sum \nolimits _{(u,v)\in S\times T}c_{uv}$

.

Now, we know, $value(f)=f_{out}(A)-f_{in}(A)$ for any subset of vertices, A. Therefore, for value( *f* ) = *c*(*A*, *Ac*) we need:

- All *outgoing edges* from the cut must be **fully saturated**.
- All *incoming edges* to the cut must have **zero flow**.

To prove the above claim we consider two cases:

- In G, there exists an *outgoing edge* $(x,y),x\in A,y\in A^{c}$ such that it is not saturated, i.e.,  *f* (*x*, *y*) < *cxy*. This implies, that there exists a **forward edge** from x to y in Gf, therefore there exists a path from s to y in Gf, which is a contradiction. Hence, any outgoing edge (*x*, *y*) is fully saturated.

- In G, there exists an *incoming edge* $(y,x),x\in A,y\in A^{c}$ such that it carries some non-zero flow, i.e.,  *f* (*y*, *x*) > 0. This implies, that there exists a **backward edge** from x to y in Gf, therefore there exists a path from s to y in Gf, which is again a contradiction. Hence, any incoming edge (*y*, *x*) must have zero flow.

Both of the above statements prove that the capacity of cut obtained in the above described manner is equal to the flow obtained in the network. Also, the flow was obtained by Ford-Fulkerson algorithm, so it is the max-flow of the network as well.

Also, since any flow in the network is always less than or equal to capacity of every cut possible in a network, the above described cut is also the min-cut which obtains the max-flow.

A corollary from this proof is that the maximum flow through any set of edges in a cut of a graph is equal to the minimum capacity of all previous cuts.

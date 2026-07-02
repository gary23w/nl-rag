---
title: "Push–relabel maximum flow algorithm"
source: https://en.wikipedia.org/wiki/Push–relabel_maximum_flow_algorithm
domain: push-relabel-maxflow
license: CC-BY-SA-4.0
tags: push relabel algorithm, preflow maximum flow, height function, goldberg tarjan
fetched: 2026-07-02
---

# Push–relabel maximum flow algorithm

In mathematical optimization, the **push–relabel algorithm** (alternatively, **preflow–push algorithm**) is an algorithm for computing maximum flows in a flow network. The name "push–relabel" comes from the two basic operations used in the algorithm. Throughout its execution, the algorithm maintains a "preflow" and gradually converts it into a maximum flow by moving flow locally between neighboring nodes using *push* operations under the guidance of an admissible network maintained by *relabel* operations. In comparison, the Ford–Fulkerson algorithm performs global augmentations that send flow following paths from the source all the way to the sink.

The push–relabel algorithm is considered one of the most efficient maximum flow algorithms. The generic algorithm has a strongly polynomial *O*(*V* 2*E*) time complexity, which is asymptotically more efficient than the *O*(*VE* 2) Edmonds–Karp algorithm. Specific variants of the algorithms achieve even lower time complexities. The variant based on the highest label node selection rule has *O*(*V* 2√*E*) time complexity and is generally regarded as the benchmark for maximum flow algorithms. Subcubic *O*(*VE*log(*V* 2/*E*)) time complexity can be achieved using dynamic trees, although in practice it is less efficient.

The push–relabel algorithm has been extended to compute minimum cost flows. The idea of distance labels has led to a more efficient augmenting path algorithm, which in turn can be incorporated back into the push–relabel algorithm to create a variant with even higher empirical performance.

## History

A preflow is a flow in which the total amount flowing into a vertex may be greater than the total amount flowing out of it, allowing an algorithm to change the flow on a single arc. This idea was originally conceived by Alexander V. Karzanov and was published in 1974 in Soviet Mathematical Dokladi 15. This pre-flow algorithm also used a push operation; however, it used distances in the auxiliary network to determine where to push the flow instead of a labeling system.

The push-relabel algorithm was designed by Andrew V. Goldberg and Robert Tarjan. The algorithm was initially presented in November 1986 in STOC '86: Proceedings of the eighteenth annual ACM symposium on Theory of computing, and then officially in October 1988 as an article in the *Journal of the ACM*. Both papers detail a generic form of the algorithm terminating in *O*(*V* 2*E*) along with a *O*(*V* 3) sequential implementation, a *O*(*VE* log(*V* 2/*E*)) implementation using dynamic trees, and parallel/distributed implementation. As explained in, Goldberg–Tarjan introduced distance labels by incorporating them into the parallel maximum flow algorithm of Yossi Shiloach and Uzi Vishkin.

## Concepts

### Definitions and notations

Let:

- *G* = (*V*, *E*) be a *network* with *capacity function* *c*: *V* × *V* → ℝ∞,
- *F* = (*G*, *c*, *s*, *t*) a *flow network*, where *s* ∈ *V* and *t* ∈ *V* (with s ≠ t) are chosen *source* and *sink* vertices respectively,
- *f* : *V* × *V* → ℝ denote a *pre-flow* in F,
- *x**f* : *V* → ℝ denote the *excess* function with respect to the flow f, defined by *x**f* (*u*) = Σ*v* ∈ *V* *f* (*v*, *u*) − Σ*v* ∈ *V* *f* (*u*, *v*),
- *c**f* : *V* × *V* → ℝ∞ denote the *residual capacity function* with respect to the flow f, defined by *c**f* (*e*) = *c*(*e*) − *f* (*e*),
- *E**f* ⊂ *E* being the edges where *f* < *c*,

and

- *G**f* (*V*, *E**f* ) denote the *residual network* of G with respect to the flow f.

The push–relabel algorithm uses a nonnegative integer valid **labeling function** which makes use of *distance labels*, or *heights*, on nodes to determine which arcs should be selected for the push operation. This labeling function is denoted by 𝓁 : *V* → ℕ. This function must satisfy the following conditions in order to be considered valid:

Valid labeling

:

𝓁(

u

) ≤ 𝓁(

v

) + 1

for all

(

u

,

v

) ∈

E

f

Source condition

:

𝓁(

s

) = |

V

|

Sink conservation

:

𝓁(

t

) = 0

In the algorithm, the label values of s and t are fixed. 𝓁(*u*) is a lower bound of the unweighted distance from u to t in *G**f*  if t is reachable from u. If u has been disconnected from t, then 𝓁(*u*) − | *V* | is a lower bound of the unweighted distance from u to s. As a result, if a valid labeling function exists, there are no *s*-*t* paths in *G**f*  because no such paths can be longer than | *V* | − 1.

An arc (*u*, *v*) ∈ *E**f*  is called **admissible** if 𝓁(*u*) = 𝓁(*v*) + 1. The **admissible network** *G̃**f* (*V*, *Ẽ**f* ) is composed of the set of arcs *e* ∈ *E**f*  that are admissible. The admissible network is acyclic.

For a fixed flow *f*, a vertex *v ∉*{*s, t*} is called **active** if it has positive excess with respect to *f*, i.e., *x**f* (*u*) > 0.

### Operations

#### Initialization

The algorithm starts by creating a residual graph, initializing the preflow values to zero and performing a set of saturating push operations on residual arcs (*s*, *v*) exiting the source, where *v* ∈ *V* \ {*s*}. Similarly, the labels are initialized such that the label at the source is the number of nodes in the graph, 𝓁(*s*) = | *V* |, and all other nodes are given a label of zero. Once the initialization is complete the algorithm repeatedly performs either the push or relabel operations against active nodes until no applicable operation can be performed.

#### Push

The push operation applies on an admissible out-arc (*u*, *v*) of an active node u in *G**f*. It moves min{*x**f* (*u*), *c**f* (*u*,*v*)} units of flow from u to v.

```
push(u, v):
    assert xf[u] > 0 and 𝓁[u] == 𝓁[v] + 1
    Δ = min(xf[u], c[u][v] - f[u][v])
    f[u][v] += Δ
    f[v][u] -= Δ
    xf[u] -= Δ
    xf[v] += Δ
```

A push operation that causes *f* (*u*, *v*) to reach *c*(*u*, *v*) is called a **saturating push** since it uses up all the available capacity of the residual arc. Otherwise, all of the excess at the node is pushed across the residual arc. This is called an **unsaturating** or **non-saturating push**.

#### Relabel

The relabel operation applies on an active node u which is neither the source nor the sink without any admissible out-arcs in *Gf*. It modifies 𝓁(*u*) to be the minimum value such that an admissible out-arc is created. Note that this always increases 𝓁(*u*) and never creates a steep arc, which is an arc (*u*, *v*) such that *c**f* (*u*, *v*) > 0, and 𝓁(*u*) > 𝓁(*v*) + 1.

```
relabel(u):
    assert xf[u] > 0 and 𝓁[u] <= 𝓁[v] for all v such that cf[u][v] > 0
    𝓁[u] = 1 + min(𝓁[v] for all v such that cf[u][v] > 0)
```

#### Effects of push and relabel

After a push or relabel operation, 𝓁 remains a valid labeling function with respect to f.

For a push operation on an admissible arc (*u*, *v*), it may add an arc (*v*, *u*) to *Ef*, where 𝓁(*v*) = 𝓁(*u*) − 1 ≤ 𝓁(*u*) + 1; it may also remove the arc (*u*, *v*) from *E**f*, where it effectively removes the constraint 𝓁(*u*) ≤ 𝓁(*v*) + 1.

To see that a relabel operation on node u preserves the validity of 𝓁(*u*), notice that this is trivially guaranteed by definition for the out-arcs of *u* in *G**f*. For the in-arcs of u in *G**f*, the increased 𝓁(*u*) can only satisfy the constraints less tightly, not violate them.

## The generic push–relabel algorithm

The generic push–relabel algorithm is used as a proof of concept only and does not contain implementation details on how to select an active node for the push and relabel operations. This generic version of the algorithm will terminate in *O*(*V*2*E*).

Since 𝓁(*s*) = | *V* |, 𝓁(*t*) = 0, and there are no paths longer than | *V* | − 1 in *G**f*, in order for 𝓁(*s*) to satisfy the valid labeling condition s must be disconnected from t. At initialisation, the algorithm fulfills this requirement by creating a pre-flow f that saturates all out-arcs of s, after which 𝓁(*v*) = 0 is trivially valid for all *v* ∈ *V* \ {*s*, *t*}. After initialisation, the algorithm repeatedly executes an applicable push or relabel operation until no such operations apply, at which point the pre-flow has been converted into a maximum flow.

```
generic-push-relabel(G, c, s, t):
    create a pre-flow f that saturates all out-arcs of s
    let 𝓁[s] = |V|
    let 𝓁[v] = 0 for all v ∈ V \ {s}
    while there is an applicable push or relabel operation do
        execute the operation
```

### Correctness

The algorithm maintains the condition that 𝓁 is a valid labeling during its execution. This can be proven true by examining the effects of the push and relabel operations on the label function 𝓁. The relabel operation increases the label value by the associated minimum plus one which will always satisfy the 𝓁(*u*) ≤ 𝓁(*v*) + 1 constraint. The push operation can send flow from u to v if 𝓁(*u*) = 𝓁(*v*) + 1. This may add (*v*, *u*) to *G**f*  and may delete (*u*, *v*) from *G**f* . The addition of (*v*, *u*) to *G**f*  will not affect the valid labeling since 𝓁(*v*) = 𝓁(*u*) − 1. The deletion of (*u*, *v*) from *G**f*  removes the corresponding constraint since the valid labeling property 𝓁(*u*) ≤ 𝓁(*v*) + 1 only applies to residual arcs in *G**f* .

If a preflow f and a valid labeling 𝓁 for f exists then there is no augmenting path from s to t in the residual graph *G**f* . This can be proven by contradiction based on inequalities which arise in the labeling function when supposing that an augmenting path does exist. If the algorithm terminates, then all nodes in *V* \ {*s*, *t*} are not active. This means all *v* ∈ *V* \ {*s*, *t*} have no excess flow, and with no excess the preflow f obeys the flow conservation constraint and can be considered a normal flow. This flow is the maximum flow according to the max-flow min-cut theorem since there is no augmenting path from s to t.

Therefore, the algorithm will return the maximum flow upon termination.

### Time complexity

In order to bound the time complexity of the algorithm, we must analyze the number of push and relabel operations which occur within the main loop. The numbers of relabel, saturating push and nonsaturating push operations are analyzed separately.

In the algorithm, the relabel operation can be performed at most (2| *V* | − 1)(| *V* | − 2) < 2| *V* |2 times. This is because the labeling 𝓁(*u*) value for any node *u* can never decrease, and the maximum label value is at most 2| *V* | − 1 for all nodes. This means the relabel operation could potentially be performed 2| *V* | − 1 times for all nodes *V* \ {*s*, *t*} (i.e. | *V* | − 2). This results in a bound of *O*(*V* 2) for the relabel operation.

Each saturating push on an admissible arc (*u*, *v*) removes the arc from *G**f* . For the arc to be reinserted into *G**f*  for another saturating push, v must first be relabeled, followed by a push on the arc (*v*, *u*), then u must be relabeled. In the process, 𝓁(*u*) increases by at least two. Therefore, there are *O*(*V*) saturating pushes on (*u*, *v*), and the total number of saturating pushes is at most 2| *V* || *E* |. This results in a time bound of *O*(*VE*) for the saturating push operations.

Bounding the number of nonsaturating pushes can be achieved via a potential argument. We use the potential function Φ = Σ[*u* ∈ *V* ∧ *x**f* (*u*) > 0] 𝓁(*u*) (i.e. Φ is the sum of the labels of all active nodes). It is obvious that Φ is 0 initially and stays nonnegative throughout the execution of the algorithm. Both relabels and saturating pushes can increase Φ. However, the value of Φ must be equal to 0 at termination since there cannot be any remaining active nodes at the end of the algorithm's execution. This means that over the execution of the algorithm, the nonsaturating pushes must make up the difference of the relabel and saturating push operations in order for Φ to terminate with a value of 0. The relabel operation can increase Φ by at most (2| *V* | − 1)(| *V* | − 2). A saturating push on (*u*, *v*) activates v if it was inactive before the push, increasing Φ by at most 2| *V* | − 1. Hence, the total contribution of all saturating pushes operations to Φ is at most (2| *V* | − 1)(2| *V* || *E* |). A nonsaturating push on (*u*, *v*) always deactivates u, but it can also activate v as in a saturating push. As a result, it decreases Φ by at least 𝓁(*u*) − 𝓁(*v*) = 1. Since relabels and saturating pushes increase Φ, the total number of nonsaturating pushes must make up the difference of (2| *V* | − 1)(| *V* | − 2) + (2| *V* | − 1)(2| *V* || *E* |) ≤ 4| *V* |2| *E* |. This results in a time bound of *O*(*V* 2*E*) for the nonsaturating push operations.

In sum, the algorithm executes *O*(*V* 2) relabels, *O*(*VE*) saturating pushes and *O*(*V* 2*E*) nonsaturating pushes. Data structures can be designed to pick and execute an applicable operation in *O*(1) time. Therefore, the time complexity of the algorithm is *O*(*V* 2*E*).

### Example

The following is a sample execution of the generic push-relabel algorithm, as defined above, on the following simple network flow graph diagram.

Initial flow network graph

Final maximum flow network graph

In the example, the *h* and *e* values denote the label 𝓁 and excess *x**f* , respectively, of the node during the execution of the algorithm. Each residual graph in the example only contains the residual arcs with a capacity larger than zero. Each residual graph may contain multiple iterations of the *perform operation* loop.

| Algorithm Operation(s) | Residual Graph |
|---|---|
| Initialise the residual graph by setting the preflow to values 0 and initialising the labeling. | (Step 1) |
| Initial saturating push is performed across all preflow arcs out of the source, s. | (Step 2) |
| Node a is relabeled in order to push its excess flow towards the sink, t. The excess at a is then pushed to b then d in two subsequent saturating pushes; which still leaves a with some excess. |   |
| (Step 3) |   |
| Once again, a is relabeled in order to push its excess along its last remaining positive residual (i.e. push the excess back to s). The node a is then removed from the set of active nodes. |   |
| (Step 4) |   |
| Relabel b and then push its excess to t and c. | (Step 5) |
| Relabel c and then push its excess to d. | (Step 6) |
| Relabel d and then push its excess to t. | (Step 7) |
| This leaves the node b as the only remaining active node, but it cannot push its excess flow towards the sink. Relabel b and then push its excess towards the source, s, via the node a. |   |
| (Step 8) |   |
| Push the last bit of excess at a back to the source, s. There are no remaining active nodes. The algorithm terminates and returns the maximum flow of the graph (as seen above). |   |
| (Step 9) |   |

The example (but with initial flow of 0) can be run here interactively.

## Practical implementations

While the generic push–relabel algorithm has *O*(*V* 2*E*) time complexity, efficient implementations achieve *O*(*V* 3) or lower time complexity by enforcing appropriate rules in selecting applicable push and relabel operations. The empirical performance can be further improved by heuristics.

### "Current-arc" data structure and discharge operation

The "current-arc" data structure is a mechanism for visiting the in- and out-neighbors of a node in the flow network in a static circular order. If a singly linked list of neighbors is created for a node, the data structure can be as simple as a pointer into the list that steps through the list and rewinds to the head when it runs off the end.

Based on the "current-arc" data structure, the discharge operation can be defined. A discharge operation applies on an active node and repeatedly pushes flow from the node until it becomes inactive, relabeling it as necessary to create admissible arcs in the process.

```
discharge(u):
    while xf[u] > 0 do
        if current-arc[u] has run off the end of neighbors[u] then
            relabel(u)
            rewind current-arc[u]
        else
            let (u, v) = current-arc[u]
            if (u, v) is admissible then
                push(u, v)
            let current-arc[u] point to the next neighbor of u
```

Finding the next admissible edge to push on has $O(1)$ amortized complexity. The current-arc pointer only moves to the next neighbor when the edge to the current neighbor is saturated or non-admissible, and neither of these two properties can change until the active node u is relabelled. Therefore, when the pointer runs off, there are no admissible unsaturated edges and we have to relabel the active node u , so having moved the pointer $O(V)$ times is paid for by the $O(V)$ relabel operation.

### Active node selection rules

Definition of the discharge operation reduces the push–relabel algorithm to repeatedly selecting an active node to discharge. Depending on the selection rule, the algorithm exhibits different time complexities. For the sake of brevity, we ignore s and t when referring to the nodes in the following discussion.

#### FIFO selection rule

The FIFO push–relabel algorithm organizes the active nodes into a queue. The initial active nodes can be inserted in arbitrary order. The algorithm always removes the node at the front of the queue for discharging. Whenever an inactive node becomes active, it is appended to the back of the queue.

The algorithm has *O*(*V* 3) time complexity.

#### Relabel-to-front selection rule

The relabel-to-front push–relabel algorithm organizes all nodes into a linked list and maintains the invariant that the list is topologically sorted with respect to the admissible network. The algorithm scans the list from front to back and performs a discharge operation on the current node if it is active. If the node is relabeled, it is moved to the front of the list, and the scan is restarted from the front.

The algorithm also has *O*(*V* 3) time complexity.

#### Highest label selection rule

The highest-label push–relabel algorithm organizes all nodes into buckets indexed by their labels. The algorithm always selects an active node with the largest label to discharge.

The algorithm has $O(V^{2}{\sqrt {E}})$ time complexity. If the lowest-label selection rule is used instead, the time complexity becomes *O*(*V* 2*E*).

### Implementation techniques

Although in the description of the generic push–relabel algorithm above, 𝓁(*u*) is set to zero for each node *u* other than s and t at the beginning, it is preferable to perform a backward breadth-first search from t to compute exact labels.

The algorithm is typically separated into two phases. Phase one computes a maximum pre-flow by discharging only active nodes whose labels are below n. Phase two converts the maximum preflow into a maximum flow by returning excess flow that cannot reach t to s. It can be shown that phase two has *O*(*VE*) time complexity regardless of the order of push and relabel operations and is therefore dominated by phase one. Alternatively, it can be implemented using flow decomposition.

Heuristics are crucial to improving the empirical performance of the algorithm. Two commonly used heuristics are the gap heuristic and the global relabeling heuristic. The gap heuristic detects gaps in the labeling function. If there is a label 0 < 𝓁*'* < | *V* | for which there is no node u such that 𝓁(*u*) = 𝓁*'*, then any node u with 𝓁*'* < 𝓁(*u*) < | *V* | has been disconnected from t and can be relabeled to (| *V* | + 1) immediately. The global relabeling heuristic periodically performs backward breadth-first search from t in *G**f*  to compute the exact labels of the nodes. Both heuristics skip unhelpful relabel operations, which are a bottleneck of the algorithm and contribute to the ineffectiveness of dynamic trees.

## Sample implementations

C

implementation

```mw
#include <stdlib.h>
#include <stdio.h>

#define NODES 6
#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define INFINITE 10000000

void push(const int * const * C, int ** F, int *excess, int u, int v) {
  int send = MIN(excess[u], C[u][v] - F[u][v]);
  F[u][v] += send;
  F[v][u] -= send;
  excess[u] -= send;
  excess[v] += send;
}

void relabel(const int * const * C, const int * const * F, int *height, int u) {
  int v;
  int min_height = INFINITE;
  for (v = 0; v < NODES; v++) {
    if (C[u][v] - F[u][v] > 0) {
      min_height = MIN(min_height, height[v]);
      height[u] = min_height + 1;
    }
  }
};

void discharge(const int * const * C, int ** F, int *excess, int *height, int *seen, int u) {
  while (excess[u] > 0) {
    if (seen[u] < NODES) {
      int v = seen[u];
      if ((C[u][v] - F[u][v] > 0) && (height[u] > height[v])) {
        push(C, F, excess, u, v);
      } else {
        seen[u] += 1;
      }
    } else {
      relabel(C, F, height, u);
      seen[u] = 0;
    }
  }
}

void moveToFront(int i, int *A) {
  int temp = A[i];
  int n;
  for (n = i; n > 0; n--) {
    A[n] = A[n-1];
  }
  A[0] = temp;
}

int pushRelabel(const int * const * C, int ** F, int source, int sink) {
  int *excess, *height, *list, *seen, i, p;

  excess = (int *) calloc(NODES, sizeof(int));
  height = (int *) calloc(NODES, sizeof(int));
  seen = (int *) calloc(NODES, sizeof(int));

  list = (int *) calloc((NODES-2), sizeof(int));

  for (i = 0, p = 0; i < NODES; i++){
    if ((i != source) && (i != sink)) {
      list[p] = i;
      p++;
    }
  }

  height[source] = NODES;
  excess[source] = INFINITE;
  for (i = 0; i < NODES; i++)
    push(C, F, excess, source, i);

  p = 0;
  while (p < NODES - 2) {
    int u = list[p];
    int old_height = height[u];
    discharge(C, F, excess, height, seen, u);
    if (height[u] > old_height) {
      moveToFront(p, list);
      p = 0;
    } else {
      p += 1;
    }
  }
  int maxflow = 0;
  for (i = 0; i < NODES; i++)
    maxflow += F[source][i];

  free(list);

  free(seen);
  free(height);
  free(excess);

  return maxflow;
}

void printMatrix(const int * const * M) {
  int i, j;
  for (i = 0; i < NODES; i++) {
    for (j = 0; j < NODES; j++)
      printf("%d\t",M[i][j]);
    printf("\n");
  }
}

int main(void) {
  int **flow, **capacities, i;
  flow = (int **) calloc(NODES, sizeof(int*));
  capacities = (int **) calloc(NODES, sizeof(int*));
  for (i = 0; i < NODES; i++) {
    flow[i] = (int *) calloc(NODES, sizeof(int));
    capacities[i] = (int *) calloc(NODES, sizeof(int));
  }

  // Sample graph
  capacities[0][1] = 2;
  capacities[0][2] = 9;
  capacities[1][2] = 1;
  capacities[1][3] = 0;
  capacities[1][4] = 0;
  capacities[2][4] = 7;
  capacities[3][5] = 7;
  capacities[4][5] = 4;

  printf("Capacity:\n");
  printMatrix(capacities);

  printf("Max Flow:\n%d\n", pushRelabel(capacities, flow, 0, 5));

  printf("Flows:\n");
  printMatrix(flow);

  return 0;
}
```

Python

implementation

```mw
def relabel_to_front(C, source: int, sink: int) -> int:
    """Push–relabel maximum flow algorithm."""
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for _ in range(n)]
    # residual capacity from u to v is C[u][v] - F[u][v]

    height = [0] * n  # height of node
    excess = [0] * n  # flow into node minus flow from node
    seen = [0] * n  # neighbours seen since last relabel
    # node "queue"
    nodelist = [i for i in range(n) if i != source and i != sink]

    def push(u, v):
        send = min(excess[u], C[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        # Find smallest new height making a push possible,
        # if such a push is possible at all.
        min_height = ∞
        for v in range(n):
            if C[u][v] - F[u][v] > 0:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        while excess[u] > 0:
            if seen[u] < n:  # check next neighbour
                v = seen[u]
                if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:  # we have checked all neighbours. must relabel
                relabel(u)
                seen[u] = 0

    height[source] = n  # longest path from source to sink is less than n long
    excess[source] = ∞  # send as much flow as possible to neighbours of source
    for v in range(n):
        push(source, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))  # move to front of list
            p = 0  # start from front of list
        else:
            p += 1

    return sum(F[source])
```

R {base}

implementation

```mw
# (HL) Push-relabel maximum flow algorithm.
# Active node selection rule: highest label.
# R {base}.

push <- function(u, v) {
  d <- min(excess[u], rGraph[u, v])
  rGraph[u, v] <<- rGraph[u, v] - d   # Forward edge, no flow.
  rGraph[v, u] <<- rGraph[v, u] + d   # Backward edge, previous routed flow,
  excess[u]    <<- excess[u]    - d   # that can be undone.
  excess[v]    <<- excess[v]    + d
  pushCtr      <<- pushCtr + 1L
  stopifnot(pushCtr <= nV^2 * sqrt(nE))
}

relabel <- function(u) {
  height[u] <<- height[u] + 1L
  relabCtr  <<- relabCtr  + 1L
}

# Discharge vertex u ≠ {s, t} via the residual network graph.
# An edge (u, v) is called admissible if height[u] == height[v] + 1.
discharge <- function(u) {
  neighbours <- which(rGraph[u, ] > 0)
  admisible  <- neighbours[which(height[u] == height[neighbours] + 1L)]
  for (v in admisible) {
    push(u, v)
    if (excess[u] == 0) break
  }
  if (excess[u] > 0) relabel(u)
}

# Preflow: flow with conservation constraints relaxed: inflow ≥ outflow.
# Move excess flow over admissible edges toward the sink.
# Global data eCap, rGraph, excess, height. Indexed by 1-based vertex id.
pushRelabel <- function(source, sink) {
  rGraph <<- eCap                     # Residual network graph.
  excess <<-                          # Inflow minus outflow (≥ 0).
    height <<- rep(0L, nV)            # Label (𝓁) value.

  height[source] <<- nV
  excess[source] <<- Inf
  relabCtr <<- pushCtr <<- 0L         # Count relabel, push.

  # Push excess from source.
  sourceOut <- which(rGraph[source, ] > 0)
  for (i in sourceOut) push(source, i)

  # Main Loop. Select highest label with positive excess,
  # from all nodes except source and sink, then discharge.
  nlist  <- setdiff(seq(from = 1, to = nV, by = 1), c(source, sink))
  while ((active <- nlist[which(excess[nlist] > 0)]) |> length() > 0) {
    u <- active[which(height[active] == max(height[active]))][1]
    discharge(u)
  }
  # All excess flow has been sent to the sink.
  return(sum((eCap - rGraph)[source, ]))
}

# Tournament graph, n = 4, max flow = n - 1.
eCap <- matrix(1L, 4, 4); diag(eCap) <- 0L
colnames(eCap) <-
  c("s", seq(2, length.out = ncol(eCap) - 2), "t") # Source is 1, sink is n.
print(list("Capacity matrix" = eCap), max = 1600)

# Calculate the maximum flow between source and sink.
nV <- ncol(eCap)                      # Vertices.
nE <- sum(eCap > 0)                   # Edges.
system.time(maxFlow <- pushRelabel(source = 1L, sink = nV))
print(paste("V E =", nV, nE, "maxFlow =", maxFlow))
print(paste("Relabel =", relabCtr, "Push =", pushCtr))

# Check, flow matrix is skew-symmetric.
# Check, flow exiting source (=1) equals flow entering sink (=nV).
flow <- eCap - rGraph
stopifnot((((flow) == -t(flow)) |> all()))
stopifnot(rowSums(flow)[1] == colSums(flow)[nV])

# Weighted adjacency matrix of the final maximum flow network graph.
mxFlow <- pmax(flow, 0)
print(list("Residual network graph" = rGraph))
print(list("Maximum flow" = mxFlow))
```

---
title: "Stoer–Wagner algorithm"
source: https://en.wikipedia.org/wiki/Stoer–Wagner_algorithm
domain: stoer-wagner-mincut
license: CC-BY-SA-4.0
tags: stoer wagner algorithm, global minimum cut, maximum adjacency ordering, undirected mincut
fetched: 2026-07-02
---

# Stoer–Wagner algorithm

In graph theory, the **Stoer–Wagner algorithm** is a recursive algorithm to solve the minimum cut problem in undirected weighted graphs with non-negative weights. It was proposed by Mechthild Stoer and Frank Wagner in 1995. The essential idea of this algorithm is to shrink the graph by merging the most intensive vertices, until the graph only contains two combined vertex sets. At each phase, the algorithm finds the minimum s - t cut for two vertices s and t chosen at its will. Then the algorithm shrinks the edge between s and t to search for non s - t cuts. The minimum cut found in all phases will be the minimum weighted cut of the graph.

A **cut** is a partition of the vertices of a graph into two non-empty, disjoint subsets. A minimum cut is a cut for which the size or weight of the cut is not larger than the size of any other cut. For an unweighted graph, the minimum cut would simply be the cut with the least edges. For a weighted graph, the sum of all edges' weight on the cut determines whether it is a minimum cut. In practice, the minimum cut problem is always discussed with the maximum flow problem, to explore the maximum capacity of a network, since the minimum cut is a bottleneck in a graph or network.

## Stoer–Wagner minimum cut algorithm

Let $G=(V,E,w)$ be a weighted undirected graph. Suppose that $s,t\in V$ . The cut is called an s - t cut if exactly one of s or t is in S . The minimal cut of G that is also an s - t cut is called the s - t min-cut of G .

This algorithm starts by finding an s and a t in V , and an s-t min-cut $(S,T)$ of G . For any pair $\left\{s,t\right\}$ , there are two possible situations: either $(S,T)$ is a global min-cut of G , or s and t belong to the same side of the global min-cut of G . Therefore, the global min-cut can be found by checking the graph $G\cup \{st\}/\left\{s,t\right\}$ , which is the graph after merging vertices s and t into a new vertex $st$ . During the merging, if s and t are connected by an edge then this edge disappears. If s and t both have edges to some vertex v , then the weight of the edge from the new vertex $st$ to v is $w(s,v)+w(t,v)$ . The algorithm is described as:

```
MinimumCutPhase
  
    
      
        (
        G
        ,
        w
        ,
        a
        )
      
    
    {\displaystyle (G,w,a)}
  

    
  
    
      
        A
        ←
        
          {
          a
          }
        
      
    
    {\displaystyle A\gets \left\{a\right\}}
  

    while 
  
    
      
         
        A
        ≠
        V
      
    
    {\displaystyle \ A\neq V}
  

        add to 
  
    
      
        A
      
    
    {\displaystyle A}
  
 the most tightly connected vertex
    end
    store the cut in which the last remaining vertex is by itself (the "cut-of-the-phase") 
    shrink 
  
    
      
        G
      
    
    {\displaystyle G}
  
 by merging the two vertices (s, t) added last (the value of "cut-of-the-phase" is the value of minimum s, t cut.)

MinimumCut
  
    
      
        (
        G
        ,
        w
        ,
        a
        )
      
    
    {\displaystyle (G,w,a)}
  

    while 
  
    
      
        
          |
        
        V
        
          |
        
        >
        1
      
    
    {\displaystyle |V|>1}
  

        MinimumCutPhase
  
    
      
        (
        G
        ,
        w
        ,
        a
        )
      
    
    {\displaystyle (G,w,a)}
  

        if the cut-of-the-phase is lighter than the current minimum cut
            then store the cut-of-the-phase as the current minimum cut
```

The algorithm works in phases. In the MinimumCutPhase, the subset A of the graphs vertices grows starting with an arbitrary single vertex until A is equal to V . In each step, the vertex which is outside of A , but most tightly connected with A is added to the set A . This procedure can be formally shown as: add vertex $z\notin A$ such that $w(A,z)=\max\{w(A,y)\mid y\notin A\}$ , where $w(A,y)$ is the sum of the weights of all the edges between A and y . So, in a single phase, a pair of vertices s and t , and a min $s{\text{-}}t$ cut C is determined. After one phase of the MinimumCutPhase, the two vertices are merged as a new vertex, and edges from the two vertices to a remaining vertex are replaced by an edge weighted by the sum of the weights of the previous two edges. Edges joining the merged nodes are removed. If there is a minimum cut of G separating s and t , the C is a minimum cut of G . If not, then the minimum cut of G must have s and t on a same side. Therefore, the algorithm would merge them as one node. In addition, the MinimumCut would record and update the global minimum cut after each MinimumCutPhase. After $n-1$ phases, the minimum cut can be determined.

### Example

This section refers to Figs. 1–6 in the original paper.

The graph in step 1 shows the original graph G and randomly selects node 2 as the starting node for this algorithm. In the MinimumCutPhase, set A only has node 2, the heaviest edge is edge (2,3), so node 3 is added into set A . Next, set A contains node 2 and node 3, the heaviest edge is (3,4), thus node 4 is added to set A . By following this procedure, the last two nodes are node 5 and node 1, which are s and t in this phase. By merging them into node 1+5, the new graph is as shown in step 2. In this phase, the weight of cut is 5, which is the summation of edges (1,2) and (1,5). Right now, the first loop of MinimumCut is completed.

In step 2, starting from node 2, the heaviest edge is (2,1+5), thus node 1+5 is put in set A . The next heaviest edges is (2,3) or (1+5,6), we choose (1+5,6) thus node 6 is added to the set. Then we compare edge (2,3) and (6,7) and choose node 3 to put in set A . The last two nodes are node 7 and node 8. Therefore, merge edge (7,8). The minimum cut is 5, so remain the minimum as 5.

The following steps repeat the same operations on the merged graph, until there is only one edge in the graph, as shown in step 7. The global minimum cut has edge (2,3) and edge (6,7), which is detected in step 5.

## Proof of correctness

To prove the correctness of this algorithm, we need to prove that the cut given by MinimumCutPhase is in fact a minimum $s{\text{-}}t$ cut of the graph, where s and t are the two vertices last added in the phase. Therefore, a lemma is shown below:

> **Lemma 1**: MinimumCutPhase returns a minimum $s{\text{-}}t$ -cut of G .

Let $C=(X,{\overline {X}})$ be an arbitrary $s{\text{-}}t$ cut, and $CP$ be the cut given by the phase. We must show that $W(C)\geq W(CP)$ . Observe that a single run of MinimumCutPhase gives us an ordering of all the vertices in the graph (where a is the first and s and t are the two vertices added last in the phase). We say the vertex v is active if v and the vertex added just before v are in opposite sides of the cut. We prove the lemma by induction on the set of active vertices. We define $A_{v}$ as the set of vertices added to A before v , and $C_{v}$ to be the set of edges in C with both of their ends in $A_{v}\cup \{v\}$ , i.e. $C_{v}\subseteq C$ is the cut induced by $A_{v}\cup \{v\}$ . We prove, for each active vertex v ,

> $w(A_{v},v)\leq w(C_{v})$

Let $v_{0}$ be the first active vertex. By the definition of these two quantities, $w(A_{v_{0}},v_{0})$ and $w(C_{v_{0}})$ are equivalent. $A_{v_{0}}$ is simply all vertices added to A before $v_{0}$ , and the edges between these vertices and $v_{0}$ are the edges that cross the cut C . Therefore, as shown above, for active vertices v and u , with v added to A before u :

> $w(A_{u},u)=w(A_{v},u)+w(A_{u}-A_{v},u)$

> $w(A_{u},u)\leq w(C_{v})+w(A_{u}-A_{v},u)$ by induction, $w(A_{v},u)\leq w(A_{v},v)\leq w(C_{v})$

> $w(A_{u},u)\leq w(C_{u})$ since $w(A_{u}-A_{v},u)$ contributes to $w(C_{u})$ but not to $w(C_{v})$ (and other edges are of non-negative weights)

Thus, since t is always an active vertex since the last cut of the phase separates s from t by definition, for any active vertex t :

> $w(A_{t},t)\leq w(C_{t})=w(C)$

Therefore, the cut of the phase is at most as heavy as C .

## Time complexity

The running time of the algorithm **MinimumCut** is equal to the added running time of the $|V|-1$ runs of **MinimumCutPhase**, which is called on graphs with decreasing number of vertices and edges.

For the **MinimumCutPhase**, a single run of it needs at most $O(|E|+|V|\log |V|)$ time.

Therefore, the overall running time should be the product of two phase complexity, which is $O(|V||E|+|V|^{2}\log |V|)$ .

For the further improvement, the key is to make it easy to select the next vertex to be added to the set A , the most tightly connected vertex. During execution of a phase, all vertices that are not in A reside in a priority queue based on a key field. The key of a vertex V is the sum of the weights of the edges connecting it to the current A , that is, $w(A,v)$ . Whenever a vertex v is added to A we have to perform an update of the queue. v has to be deleted from the queue, and the key of every vertex w not in A , connected to v has to be increased by the weight of the edge $vw$ , if it exists. As this is done exactly once for every edge, overall we have to perform $|V|$ ExtractMax and $|E|$ IncreaseKey operations. By using the Fibonacci heap we can perform an ExtractMax operation in $O(\log |V|)$ amortized time and an IncreaseKey operation in $O(1)$ amortized time. Thus, the time we need for this key step that dominates the rest of the phase, is $O(|E|+|V|\log |V|)$ .

## Example code

Below is a concise C++ implementation of the Stoer–Wagner algorithm.

```mw
// Adjacency matrix implementation of Stoer–Wagner min cut algorithm.
//
// Running time:
//     O(|V|^3)

#include <bits/stdc++.h>
using namespace std;

pair<int, vector<int>> globalMinCut(vector<vector<int>> mat) {
    pair<int, vector<int>> best = {INT_MAX, {}};
    int n = mat.size();
    vector<vector<int>> co(n);

    for (int i = 0; i < n; i++)
        co[i] = {i};

    for (int ph = 1; ph < n; ph++) {
        vector<int> w = mat[0];
        size_t s = 0, t = 0;
        for (int it = 0; it < n - ph; it++) { // O(V^2) -> O(E log V) with prio. queue
            w[t] = INT_MIN;
            s = t, t = max_element(w.begin(), w.end()) - w.begin();
            for (int i = 0; i < n; i++) w[i] += mat[t][i];
        }
        best = min(best, {w[t] - mat[t][t], co[t]});
        co[s].insert(co[s].end(), co[t].begin(), co[t].end());
        for (int i = 0; i < n; i++) mat[s][i] += mat[t][i];
        for (int i = 0; i < n; i++) mat[i][s] = mat[s][i];
        mat[0][t] = INT_MIN;
    }

    return best;
}
```

```mw
const int maxn = 550;
const int inf = 1000000000;
int n, r;
int edge[maxn][maxn], dist[maxn];
bool vis[maxn], bin[maxn];

void init()
{
    memset(edge, 0, sizeof(edge));
    memset(bin, false, sizeof(bin));
}

int contract( int &s, int &t )          // Find s,t
{
    memset(dist, 0, sizeof(dist));
    memset(vis, false, sizeof(vis));
    int i, j, k, mincut, maxc;

    for (i = 1; i <= n; i++)
    {
        k = -1; maxc = -1;
        for (j = 1; j <= n; j++)if (!bin[j] && !vis[j] && dist[j] > maxc)
        {
            k = j;  maxc = dist[j];
        }
        if (k == -1) return mincut;
        s = t;  t = k;
        mincut = maxc;
        vis[k] = true;
        for (j = 1; j <= n; j++) if (!bin[j] && !vis[j])  
            dist[j] += edge[k][j];
    }

    return mincut;  
}

int Stoer_Wagner()  
{  
    int mincut, i, j, s, t, ans;  

    for (mincut = inf, i = 1; i < n; i++)  
    {  
        ans = contract(s, t);
        bin[t] = true;
        if (mincut > ans) mincut = ans;
        if (mincut == 0) return 0;
        for (j = 1; j <= n; j++) if (!bin[j])
            edge[s][j] = (edge[j][s] += edge[j][t]);
    }

    return mincut;
}
```

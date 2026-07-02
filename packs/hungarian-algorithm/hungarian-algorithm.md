---
title: "Hungarian algorithm"
source: https://en.wikipedia.org/wiki/Hungarian_algorithm
domain: hungarian-algorithm
license: CC-BY-SA-4.0
tags: hungarian algorithm, assignment problem, bipartite matching, combinatorial optimization
fetched: 2026-07-02
---

# Hungarian algorithm

The **Hungarian algorithm** or **Hungarian method** is a combinatorial optimization algorithm that solves the assignment problem in polynomial time and which anticipated later primal–dual methods. It was developed and published in 1955 by Harold Kuhn, who gave it the name "Hungarian method" because the algorithm was largely based on the earlier works of two Hungarian mathematicians, Dénes Kőnig and Jenő Egerváry. However, in 2006 it was discovered that Carl Gustav Jacobi had solved the assignment problem in the 19th century, and the solution had been published posthumously in 1890 in Latin.

James Munkres reviewed the algorithm in 1957 and observed that it is (strongly) polynomial. Since then the algorithm has been known also as the **Kuhn–Munkres algorithm** or **Munkres assignment algorithm**. The time complexity of the original algorithm was $O(n^{4})$ , however Edmonds and Karp, and independently Tomizawa, noticed that it can be modified to achieve an $O(n^{3})$ running time. Ford and Fulkerson extended the method to general maximum flow problems in form of the Ford–Fulkerson algorithm.

## The problem

### Example

In this simple example, there are three workers: Alice, Bob and Carol. One of them has to clean the bathroom, another sweep the floors and the third washes the windows, but they each demand different pay for the various tasks. The problem is to find the lowest-cost way to assign the jobs. The problem can be represented in a matrix of the costs of the workers doing the jobs. For example:

| TaskWorker | Clean bathroom | Sweep floors | Wash windows |
|---|---|---|---|
| Alice | **$8** | $4 | $7 |
| Bob | $5 | $2 | **$3** |
| Carol | $9 | **$4** | $8 |

The Hungarian method, when applied to the above table, would give the minimum cost: this is $15, achieved by having Alice clean the bathroom, Carol sweep the floors, and Bob wash the windows. This can be confirmed using brute force:

| CleanSweep | Alice | Bob | Carol |
|---|---|---|---|
| Alice | — | $17 | $16 |
| Bob | $18 | — | $18 |
| Carol | **$15** | $16 | — |

(the unassigned person washes the windows)

### Matrix formulation

In the matrix formulation, we are given an *n*×*n* matrix, where the element in the *i*-th row and *j*-th column represents the cost of assigning the *j*-th job to the *i*-th worker. We have to find an assignment of the jobs to the workers, such that each job is assigned to one worker and each worker is assigned one job, such that the total cost of assignment is minimum.

This can be expressed as permuting the rows of a cost matrix *C* to minimize the trace of a matrix,

$\min _{P}\operatorname {Tr} (PC)\;,$

where *P* is a permutation matrix. (Equivalently, the columns can be permuted using *CP*.)

If the goal is to find the assignment that yields the *maximum* cost, the problem can be solved by negating the cost matrix *C*.

### Bipartite graph formulation

The algorithm can equivalently be described by formulating the problem using a bipartite graph. We have a complete bipartite graph $G=(S,T;E)$ with n worker vertices (S) and n job vertices (T), and the edges (E) each have a cost $c(i,j)$ . We want to find a perfect matching with a minimum total cost.

## The algorithm in terms of bipartite graphs

Let us call a function $y:(S\cup T)\to \mathbb {R}$ a **potential** if $y(i)+y(j)\leq c(i,j)$ for each $i\in S,j\in T$ .

The *value* of potential y is the sum of the potential over all vertices:

$\sum _{v\in S\cup T}y(v)$

.

The cost of each perfect matching is at least the value of each potential. This can be seen by first noticing that the total cost of the matching is the sum of costs of all edges it contains. The cost of each edge is at least the sum of potentials of its endpoints. Since the matching is perfect, each vertex is an endpoint of exactly one edge. Hence, the total cost is at least the total potential.

The Hungarian method finds a perfect matching and a potential such that the matching cost equals the potential value. This proves that both of them are optimal. In fact, the Hungarian method finds a perfect matching of **tight edges**: an edge $ij$ is called tight for a potential y if $y(i)+y(j)=c(i,j)$ . Let us denote the subgraph of **tight** edges by $G_{y}$ . The cost of a perfect matching in $G_{y}$ (if there is one) equals the value of y.

During the algorithm we maintain a potential y and an orientation of $G_{y}$ (denoted by ${\overrightarrow {G_{y}}}$ ) which has the property that the edges oriented from T to S form a matching M. Initially, y is 0 everywhere, and all edges are oriented from S to T (so M is empty). In each step, either we modify y so that its value increases, or modify the orientation to obtain a matching with more edges. We maintain the invariant that all the edges of M are tight. We are done if M is a perfect matching.

In a general step, let $R_{S}\subseteq S$ and $R_{T}\subseteq T$ be the vertices not covered by M (so $R_{S}$ consists of the vertices in S with no incoming edge and $R_{T}$ consists of the vertices in T with no outgoing edge). Let Z be the set of vertices reachable in ${\overrightarrow {G_{y}}}$ from $R_{S}$ by a directed path. This can be computed by breadth-first search.

If $R_{T}\cap Z$ is nonempty, then reverse the orientation of all edges along a directed path in ${\overrightarrow {G_{y}}}$ from $R_{S}$ to $R_{T}$ . Thus the size of the corresponding matching increases by 1.

If $R_{T}\cap Z$ is empty, then let

${\displaystyle \Delta$

Δ is well defined because at least one such edge $ij$ must exist whenever the matching is not yet of maximum possible size (see the following section); it is positive because there are no tight edges between $Z\cap S$ and $T\setminus Z$ . Increase y by Δ on the vertices of $Z\cap S$ and decrease y by Δ on the vertices of $Z\cap T$ . The resulting y is still a potential, and although the graph $G_{y}$ changes, it still contains M (see the next subsections). We orient the new edges from S to T. By the definition of Δ the set Z of vertices reachable from $R_{S}$ increases (note that the number of tight edges does not necessarily increase). If the vertex added to $Z\cap T$ is unmatched (that is, it is also in $R_{T}$ ), then at the next iteration the graph will have an augmenting path.

We repeat these steps until M is a perfect matching, in which case it gives a minimum cost assignment. The running time of this version of the method is $O(n^{4})$ : M is augmented n times, and in a phase where M is unchanged, there are at most n potential changes (since Z increases every time). The time sufficient for a potential change is $O(n^{2})$ .

### Proof that the algorithm makes progress

We must show that as long as the matching is not of maximum possible size, the algorithm is always able to make progress — that is, to either increase the number of matched edges, or tighten at least one edge. It suffices to show that at least one of the following holds at every step:

- M is of maximum possible size.
- $G_{y}$ contains an augmenting path.
- G contains a **loose-tailed path**: a path from some vertex in $R_{S}$ to a vertex in $T\setminus Z$ that consists of any number (possibly zero) of tight edges followed by a single loose edge. The trailing loose edge of a loose-tailed path is thus from $Z\cap S$ , guaranteeing that Δ is well defined.

If M is of maximum possible size, we are of course finished. Otherwise, by Berge's lemma, there must exist an augmenting path P with respect to M in the underlying graph G. However, this path may not exist in $G_{y}$ : Although every even-numbered edge in P is tight by the definition of M, odd-numbered edges may be loose and thus absent from $G_{y}$ . One endpoint of P is in $R_{S}$ , the other in $R_{T}$ ; w.l.o.g., suppose it begins in $R_{S}$ . If every edge on P is tight, then it remains an augmenting path in $G_{y}$ and we are done. Otherwise, let $uv$ be the first loose edge on P. If $v\notin Z$ then we have found a loose-tailed path and we are done. Otherwise, v is reachable from some other path Q of tight edges from a vertex in $R_{S}$ . Let $P_{v}$ be the subpath of P beginning at v and continuing to the end, and let $P'$ be the path formed by traveling along Q until a vertex on $P_{v}$ is reached, and then continuing to the end of $P_{v}$ . Observe that $P'$ is an augmenting path in G with at least one fewer loose edge than P. P can be replaced with $P'$ and this reasoning process iterated (formally, using induction on the number of loose edges) until either an augmenting path in $G_{y}$ or a loose-tailed path in G is found.

### Proof that adjusting the potential *y* leaves *M* unchanged

To show that every edge in M remains after adjusting y, it suffices to show that for an arbitrary edge in M, either both of its endpoints, or neither of them, are in Z. To this end let $vu$ be an edge in M from T to S. It is easy to see that if v is in Z then u must be too, since every edge in M is tight. Now suppose, toward contradiction, that $u\in Z$ but $v\notin Z$ . u itself cannot be in $R_{S}$ because it is the endpoint of a matched edge, so there must be some directed path of tight edges from a vertex in $R_{S}$ to u. This path must avoid v, since that is by assumption not in Z, so the vertex immediately preceding u in this path is some other vertex $v'\in T$ . $v'u$ is a tight edge from T to S and is thus in M. But then M contains two edges that share the vertex u, contradicting the fact that M is a matching. Thus every edge in M has either both endpoints or neither endpoint in Z.

### Proof that y remains a potential

To show that y remains a potential after being adjusted, it suffices to show that no edge has its total potential increased beyond its cost. This is already established for edges in M by the preceding paragraph, so consider an arbitrary edge uv from S to T. If $y(u)$ is increased by Δ, then either $v\in Z\cap T$ , in which case $y(v)$ is decreased by Δ, leaving the total potential of the edge unchanged, or $v\in T\setminus Z$ , in which case the definition of Δ guarantees that $y(u)+y(v)+\Delta \leq c(u,v)$ . Thus y remains a potential.

## The algorithm in *O*(*n*3) time

Suppose there are J jobs and W workers ( $J\leq W$ ). We describe how to compute for each prefix of jobs the minimum total cost to assign each of these jobs to distinct workers. Specifically, we add the j th job and update the total cost in time $O(jW)$ , yielding an overall time complexity of $O\left(\sum _{j=1}^{J}jW\right)=O(J^{2}W)$ . Note that this is better than $O(W^{3})$ when the number of jobs is small relative to the number of workers.

### Adding the j-th job in *O*(*jW*) time

We use the same notation as the previous section, though we modify their definitions as necessary. Let $S_{j}$ denote the set of the first j jobs and T denote the set of all workers.

Before the j th step of the algorithm, we assume that we have a matching on $S_{j-1}\cup T$ that matches all jobs in $S_{j-1}$ and potentials y satisfying the following condition: the matching is tight with respect to the potentials, and the potentials of all unmatched workers are zero, and the potentials of all matched workers are non-positive. Note that such potentials certify the optimality of the matching.

During the j th step, we add the j th job to $S_{j-1}$ to form $S_{j}$ and initialize $Z=\{j\}$ . At all times, every vertex in Z will be reachable from the j th job in $G_{y}$ . While Z does not contain a worker that has not been assigned a job, let

${\displaystyle \Delta$

and $w_{\text{next}}$ denote any w at which the minimum is attained. After adjusting the potentials in the way described in the previous section, there is now a tight edge from Z to $w_{\text{next}}$ .

- If $w_{\text{next}}$ is unmatched, then we have an augmenting path in the subgraph of tight edges from j to $w_{\text{next}}$ . After toggling the matching along this path, we have now matched the first j jobs, and this procedure terminates.
- Otherwise, we add $w_{\text{next}}$ and the job matched with it to Z .

Adjusting potentials takes $O(W)$ time. Recomputing $\Delta$ and $w_{\text{next}}$ after changing the potentials and Z also can be done in $O(W)$ time. Case 1 can occur at most $j-1$ times before case 2 occurs and the procedure terminates, yielding the overall time complexity of $O(jW)$ .

### Implementation in C++

For convenience of implementation, the code below adds an additional worker $w_{W}$ such that $y(w_{W})$ stores the negation of the sum of all $\Delta$ computed so far. After the j th job is added and the matching updated, the cost of the current matching equals the sum of all $\Delta$ computed so far, or $-y(w_{W})$ .

This code is adapted from e-maxx :: algo.

```mw
/**
 * Solution to https://open.kattis.com/problems/cordonbleu using Hungarian
 * algorithm.
 */
import std;

using std::integral;
using std::istream;
using std::numeric_limits;
using std::pair;
using std::stringstream;
using std::string_view;
using std::vector;

constexpr string_view SAMPLE_INPUT = R"(
2 2
1 0
0 -1
-1 1
2 -1
0 0)";

/**
 * @brief Performs the Hungarian algorithm.
 *
 * Given J jobs and W workers (J <= W), computes the minimum cost to assign each
 * prefix of jobs to distinct workers.
 *
 * @tparam T a type large enough to represent integers on the order of J *
 * max(|C|)
 * @param C a matrix of dimensions JxW such that C[j][w] = cost to assign j-th
 * job to w-th worker (possibly negative)
 *
 * @return a vector of length J, with the j-th entry equaling the minimum cost
 * to assign the first j + 1 jobs to distinct workers
 */
template <integral T> 
vector<T> hungarian(const vector<vector<T>>& C) {
    auto lessThan = []<integral T>(T& a, const T& b) -> bool { 
        return b < a ? a = b, true : false; 
    }
    const int J = static_cast<int>(C.size());
    const int W = static_cast<int>(C[0].size());
    contract_assert(J <= W);
    // job[w] = job assigned to w-th worker, or -1 if no job assigned
    // note: a W-th worker was added for convenience
    vector<int> job(W + 1, -1);
    vector<T> ys(J); 
    vector<T> yt(W + 1);  // potentials
    // -yt[W] will equal the sum of all deltas
    vector<T> answers;
    const T inf = numeric_limits<T>::max();
    for (int jCur = 0; jCur < J; ++jCur) {
        // assign jCur-th job
        int wCur = W;
        job[wCur] = jCur;
        // min reduced cost over edges from Z to worker w
        vector<T> minTo(W + 1, inf);
        vector<int> prev(W + 1, -1); // previous worker on alternating path
        vector<bool> inZ(W + 1); // whether worker is in Z
        while (job[wCur] != -1) {
            // runs at most jCur + 1 times
            inZ[wCur] = true;
            const int j = job[wCur];
            T delta = inf;
            int wNext;
            for (int w = 0; w < W; ++w) {
                if (!inZ[w]) {
                    if (ckmin(minTo[w], C[j][w] - ys[j] - yt[w])) {
                        prev[w] = wCur;
                    }
                    if (ckmin(delta, minTo[w])) {
                        wNext = w;
                    }
                }
            }
            // delta will always be nonnegative,
            // except possibly during the first time this loop runs
            // if any entries of C[jCur] are negative
            for (int w = 0; w <= W; ++w) {
                if (inZ[w]) {
                    ys[job[w]] += delta;
                    yt[w] -= delta;
                } else {
                    minTo[w] -= delta;
                }
            }
            wCur = wNext;
        }
        // update assignments along alternating path
        for (int w; wCur != W; wCur = w) {
            job[wCur] = job[w = prev[wCur]];
        }
        answers.push_back(-yt[W]);
    }
    return answers;
}

/**
 * @brief solves https://open.kattis.com/problems/cordonbleu
 */
int cordonBleu(istream& is) {
    int N;
    int M;
    is >> N >> M;
    vector<pair<int, int>> B(N);
    vector<pair<int, int>> C(M);
    vector<pair<int, int>> bottles(N);
    vector<pair<int, int>> couriers(M);
    for (auto& [a, b]: bottles) {
        is >> a >> b;
    }
    for (auto& [c, d]: couriers) {
        is >> a >> d;
    }
    pair<int, int> rest;
    std::cin >> rest.first >> rest.second;
    vector<vector<int>> costs(N, vector<int>(N + M - 1));
    auto dist = [&](const pair<int, int>& x, const pair<int, int>& y) -> int {
        return std::abs(x.first - y.first) + std::abs(x.second - y.second);
    };
    for (int b = 0; b < N; ++b) {
        for (int c = 0; c < M; ++c) { // courier -> bottle -> restaurant
            costs[b][c] = dist(couriers[c], bottles[b]) + dist(bottles[b], rest);
        }
        for (int c = 0; c < N - 1; ++c) { // restaurant -> bottle -> restaurant
            costs[b][c + M] = 2 * dist(bottles[b], rest);
        }
    }
    return hungarian(costs).back();
}

/**
 * @brief Entry point into the program.
 *
 * @return The return code of the program.
 */
int main() {
    stringstream sampleInput1(SAMPLE_INPUT);

    std::println(stderr, "{}", cordonBleu(sampleInput1)); // 5
    std::println("{}", cordonBleu(std::cin));
}
// https://godbolt.org/z/Wen35833G
```

## Connection to successive shortest paths

The Hungarian algorithm can be seen to be equivalent to the successive shortest path algorithm for minimum cost flow, where the reweighting technique from Johnson's algorithm is used to find the shortest paths. The implementation from the previous section is rewritten below in such a way as to emphasize this connection; it can be checked that the potentials h for workers $0\dots W-1$ are equal to the potentials y from the previous solution up to a constant offset. When the graph is sparse (there are only M allowed job, worker pairs), it is possible to optimize this algorithm to run in $O(JM+J^{2}\log W)$ time by using a Fibonacci heap to determine $w_{\text{next}}$ instead of iterating over all W workers to find the one with minimum distance (alluded to here).

```mw
template <typename T> 
vector<T> hungarian(const vector<vector<T>>& C) {
    auto lessThan = []<integral T>(T& a, const T& b) -> bool { 
        return b < a ? a = b, true : false; 
    }
    const int J = static_cast<int>(C.size()); 
    const int W = static_cast<int>(C[0].size());
    contract_assert(J <= W);
    // job[w] = job assigned to w-th worker, or -1 if no job assigned
    // note: a W-th worker was added for convenience
    vector<int> job(W + 1, -1);
    vector<T> h(W); // Johnson potentials
    vector<T> answers;
    T ansCur = 0;
    const T inf = numeric_limits<T>::max();
    // assign jCur-th job using Dijkstra with potentials
    for (int jCur = 0; jCur < J; ++jCur) {
        int wCur = W; // unvisited worker with minimum distance
        job[wCur] = jCur;
        vector<T> dist(W + 1, inf); // Johnson-reduced distances
        dist[W] = 0;
        vector<bool> vis(W + 1); // whether visited yet
        vector<int> prev(W + 1, -1); // previous worker on shortest path
        while (job[wCur] != -1) { // Dijkstra step: pop min worker from heap
            T minDist = inf;
            vis[wCur] = true;
            int wNext = -1; // next unvisited worker with minimum distance
            // consider extending shortest path by wCur -> job[wCur] -> w
            for (int w = 0; w < W; ++w) {
                if (!vis[w]) {
                    // sum of reduced edge weights wCur -> job[wCur] -> w
                    T edge = C[job[wCur]][w] - h[w];
                    if (wCur != W) {
                        edge -= C[job[wCur]][wCur] - h[wCur];
                        contract_assert(edge >= 0); // consequence of Johnson potentials
                    }
                    if (lessThan(dist[w], dist[wCur] + edge)) {
                        prev[w] = wCur;
                    }
                    if (lessThan(minDist, dist[w])) {
                        wNext = w;
                    }
                }
            }
            wCur = wNext;
        }
        for (int w = 0; w < W; ++w) { // update potentials
            lessThan(dist[w], dist[wCur]);
            h[w] += dist[w];
        }
        ansCur += h[wCur];
        for (int w; wCur != W; wCur = w) {
            job[wCur] = job[w = prev[wCur]];
        }
        answers.push_back(ansCur);
    }
    return answers;
}
```

## Matrix interpretation

This variant of the algorithm follows the formulation given by Flood, and later described more explicitly by Munkres, who proved it runs in ${\mathcal {O}}(n^{4})$ time. Instead of keeping track of the potentials of the vertices, the algorithm operates only on a matrix:

$a_{ij}:=c(i,j)-y(i)-y(j)$

where $c(i,j)$ is the original cost matrix and $y(i),y(j)$ are the potentials from the graph interpretation. Changing the potentials corresponds to adding or subtracting from rows or columns of this matrix. The algorithm starts with $a_{ij}=c(i,j)$ . As such, it can be viewed as taking the original cost matrix and modifying it.

Given n workers and tasks, the problem is written in the form of an n×n cost matrix

| a1 | a2 | a3 | a4 |
|---|---|---|---|
| b1 | b2 | b3 | b4 |
| c1 | c2 | c3 | c4 |
| d1 | d2 | d3 | d4 |

where a, b, c and d are workers who have to perform tasks 1, 2, 3 and 4. a1, a2, a3, and a4 denote the penalties incurred when worker "a" does task 1, 2, 3, and 4 respectively.

The problem is equivalent to assigning each worker a unique task such that the total penalty is minimized. Note that each task can only be worked on by one worker.

### Step 1

**For each row, its minimum element is subtracted from every element in that row.** This causes all elements to have nonnegative values. Therefore, an assignment with a total penalty of 0 is by definition a minimum assignment.

This also leads to at least one zero in each row. As such, a naive greedy algorithm can attempt to assign all workers a task with a penalty of zero. This is illustrated below.

| 0 | a2 | a3 | a4 |
|---|---|---|---|
| b1 | b2 | b3 | 0 |
| c1 | 0 | c3 | c4 |
| d1 | d2 | 0 | d4 |

The zeros above would be the assigned tasks.

Worst-case there are n! combinations to try, since multiple zeroes can appear in a row if multiple elements are the minimum. So at some point this naive algorithm should be short circuited.

### Step 2

Sometimes it may turn out that the matrix at this stage cannot be used for assigning, as is the case for the matrix below.

| 0 | a2 | 0 | a4 |
|---|---|---|---|
| b1 | 0 | b3 | 0 |
| 0 | c2 | c3 | c4 |
| 0 | d2 | d3 | d4 |

To overcome this, we repeat the above procedure for all columns (i.e. **the minimum element in each column is subtracted from all the elements in that column**) and then check if an assignment with penalty 0 is possible.

In most situations this will give the result, but if it is still not possible then we need to keep going.

### Step 3

**All zeros in the matrix must be covered by marking as few rows and/or columns as possible.** Steps 3 and 4 form *one way* to accomplish this.

For each row, try to assign an arbitrary zero. Assigned tasks are represented by starring a zero. Note that assignments can't be in the same row or column.

- We assign the first zero of Row 1. The second zero of Row 1 can't be assigned.
- We assign the first zero of Row 2. The second zero of Row 2 can't be assigned.
- Zeros on Row 3 and Row 4 can't be assigned, because they are on the same column as the zero assigned on Row 1.

We could end with another assignment if we choose another ordering of the rows and columns.

| 0* | a2 | 0 | a4 |
|---|---|---|---|
| b1 | 0* | b3 | 0 |
| 0 | c2 | c3 | c4 |
| 0 | d2 | d3 | d4 |

### Step 4

Cover all columns containing a (starred) zero.

| × | × |   |   |   |
|---|---|---|---|---|
| 0* | a2 | 0 | a4 |   |
| b1 | 0* | b3 | 0 |   |
| 0 | c2 | c3 | c4 |   |
| 0 | d2 | d3 | d4 |   |

Find a non-covered zero and prime it (mark it with a prime symbol). If no such zero can be found, meaning all zeroes are covered, skip to step 5.

- If the zero is on the same row as a starred zero, cover the corresponding row, and uncover the column of the starred zero.
- Then, GOTO "Find a non-covered zero and prime it."
  - Here, the second zero of Row 1 is uncovered. Because there is another zero starred on Row 1, we cover Row 1 and uncover Column 1.
  - Then, the second zero of Row 2 is uncovered. We cover Row 2 and uncover Column 2.

|   | × |   |   |   |
|---|---|---|---|---|
| 0* | a2 | 0' | a4 | × |
| b1 | 0* | b3 | 0 |   |
| 0 | c2 | c3 | c4 |   |
| 0 | d2 | d3 | d4 |   |

|   |   |   |   |   |
|---|---|---|---|---|
| 0* | a2 | 0' | a4 | × |
| b1 | 0* | b3 | 0' | × |
| 0 | c2 | c3 | c4 |   |
| 0 | d2 | d3 | d4 |   |

- Else the non-covered zero has no assigned zero on its row. We make a path starting from the zero by performing the following steps:
  1. Substep 1: Find a starred zero on the corresponding column. If there is one, go to Substep 2, else, stop.
  2. Substep 2: Find a primed zero on the corresponding row (there should always be one). Go to Substep 1.

The zero on Row 3 is uncovered. We add to the path the first zero of Row 1, then the second zero of Row 1, then we are done.

|   |   |   |   |   |
|---|---|---|---|---|
| 0* | a2 | 0' | a4 | × |
| b1 | 0* | b3 | 0' | × |
| 0' | c2 | c3 | c4 |   |
| 0 | d2 | d3 | d4 |   |

- (Else branch continued) For all zeros encountered during the path, star primed zeros and unstar starred zeros.
  - As the path begins and ends by a primed zero when swapping starred zeros, we have assigned one more zero.

| 0 | a2 | 0* | a4 |
|---|---|---|---|
| b1 | 0* | b3 | 0 |
| 0* | c2 | c3 | c4 |
| 0 | d2 | d3 | d4 |

- (Else branch continued) Unprime all primed zeroes and uncover all lines.
- Repeat the previous steps (continue looping until the above "skip to step 5" is reached).
  - We cover columns 1, 2 and 3. The second zero on Row 2 is uncovered, so we cover Row 2 and uncover Column 2:

| × |   | × |   |   |
|---|---|---|---|---|
| 0 | a2 | 0* | a4 |   |
| b1 | 0* | b3 | 0' | × |
| 0* | c2 | c3 | c4 |   |
| 0 | d2 | d3 | d4 |   |

All zeros are now covered with a minimal number of rows and columns.

The aforementioned detailed description is *just one way* to draw the minimum number of lines to cover all the 0s. Other methods work as well.

### Step 5

If the number of starred zeros is n (or in the general case $min(n,m)$ , where n is the number of people and m is the number of jobs), the algorithm terminates. See the Result subsection below on how to interpret the results.

Otherwise, find the lowest uncovered value. Subtract this from every uncovered element and add it to every element covered by two lines. Go back to step 4.

This is equivalent to subtracting a number from all rows which are not covered and adding the same number to all columns which are covered. These operations do not change optimal assignments.

### Result

If following this specific version of the algorithm, the starred zeros form the minimum assignment.

From Kőnig's theorem, the minimum number of lines (minimum vertex cover) will be n (the size of maximum matching). Thus, when n lines are required, minimum cost assignment can be found by looking at only zeroes in the matrix.

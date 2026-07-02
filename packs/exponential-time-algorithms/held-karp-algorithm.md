---
title: "Held–Karp algorithm"
source: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
domain: exponential-time-algorithms
license: CC-BY-SA-4.0
tags: exponential time algorithm, exponential time hypothesis, held karp algorithm, measure and conquer
fetched: 2026-07-02
---

# Held–Karp algorithm

The **Held–Karp algorithm**, also called the **Bellman–Held–Karp algorithm**, is a dynamic programming algorithm proposed in 1962 independently by Bellman and by Held and Karp to solve the traveling salesman problem (TSP), in which the input is a distance matrix between a set of cities, and the goal is to find a minimum-length tour that visits each city exactly once before returning to the starting point. It finds the exact solution to this problem, and to several related problems including the Hamiltonian cycle problem, in exponential time.

## Algorithm description and motivation

Number the cities $1,2,\ldots ,n$ , with 1 designated arbitrarily as a "starting" city (since the solution to TSP is a Hamiltonian cycle, the choice of starting city doesn't matter). The Held–Karp algorithm begins by calculating, for each set of cities $S\subseteq \{2,\ldots ,n\}$ and every city $e\neq 1$ not contained in S , the shortest one-way path from 1 to e that passes through every city in S in some order (but not through any other cities). Denote this distance $g(S,e)$ , and write $d(u,v)$ for the length of the direct edge from u to v . We'll compute values of $g(S,e)$ starting with the smallest sets S and finishing with the largest.

When S has two or fewer elements, then calculating $g(S,e)$ requires looking at one or two possible shortest paths. For example, $g(\emptyset ,e)$ is simply $d(1,e)$ , and $g(\{2\},3)$ is just the length of $1\rightarrow 2\rightarrow 3$ . Likewise, $g(\{2,3\},4)$ is the length of either $1\rightarrow 2\rightarrow 3\rightarrow 4$ or $1\rightarrow 3\rightarrow 2\rightarrow 4$ , whichever is shorter.

Once S contains three or more cities, the number of paths through S rises quickly, but only a few such paths need to be examined to find the shortest. For instance, if $1\rightarrow 2\rightarrow 3\rightarrow 4$ is shorter than $1\rightarrow 3\rightarrow 2\rightarrow 4$ , then $1\rightarrow 2\rightarrow 3\rightarrow 4\rightarrow 5$ must be shorter than $1\rightarrow 3\rightarrow 2\rightarrow 4\rightarrow 5$ , and the length of $1\rightarrow 3\rightarrow 2\rightarrow 4\rightarrow 5$ is not a possible value of $g(\{2,3,4\},5)$ . Similarly, if the shortest path from 1 through $\{2,3,4\}$ to 5 is $1\rightarrow 4\rightarrow 3\rightarrow 2\rightarrow 5$ , and the shortest path from 1 through $\{2,3,4,5\}$ to 6 ends with the edge $5\rightarrow 6$ , then the whole path from 1 to 6 must be $1\rightarrow 4\rightarrow 3\rightarrow 2\rightarrow 5\rightarrow 6$ , and not any of the other five paths created by visiting $\{2,3,4\}$ in a different order.

More generally, suppose $S=\{s_{1},\ldots ,s_{k}\}$ is a set of k cities. For every integer $1\leq i\leq k$ , write $S_{i}=S\setminus \{s_{i}\}=\{s_{1},\ldots ,s_{i-1},s_{i+1},\ldots ,s_{k}\}$ for the set created by removing $s_{i}$ from S . Then if the shortest path from 1 through S to e has $s_{i}$ as its second-to-last city, then removing the final edge from this path must give the shortest path from 1 to $s_{i}$ through $S_{i}$ . This means there are only k possible shortest paths from 1 to e through S , one for each possible second-to-last city $s_{i}$ with length $g(S_{i},s_{i})+d(s_{i},e)$ , and $g(S,e)=\min _{1\leq i\leq k}g(S_{i},s_{i})+d(s_{i},e)$ .

This stage of the algorithm finishes when $g(\{2,\ldots ,i-1,i+1,\ldots ,n\},i)$ is known for every integer $2\leq i\leq n$ , giving the shortest distance from city 1 to city i that passes through every other city. The much shorter second stage adds these distances to the edge lengths $d(i,1)$ to give $n-1$ possible shortest cycles, and then finds the shortest.

The shortest path itself (and not just its length), finally, may be reconstructed by storing alongside $g(S,e)$ the label of the second-to-last city on the path from 1 to e through S , raising space requirements by only a constant factor.

## Algorithmic complexity

The Held–Karp algorithm has exponential time complexity $\Theta (2^{n}n^{2})$ , significantly better than the superexponential performance $\Theta (n!)$ of a brute-force algorithm. Held–Karp, however, requires $\Theta (n2^{n})$ space to hold all computed values of the function $g(S,e)$ , while brute force needs only $\Theta (n^{2})$ space to store the graph itself.

### Time

Computing one value of $g(S,e)$ for a k -element subset S of $\{2,\ldots ,n\}$ requires finding the shortest of k possible paths, each found by adding a known value of g and an edge length from the original graph; that is, it requires time proportional to k . There are ${\textstyle {\binom {n-1}{k}}}$ k -element subsets of $\{2,\ldots ,n\}$ ; and each subset gives $n-k-1$ possible values of e . Computing all values of $g(S,e)$ where $|S|=k$ thus requires time ${\textstyle k(n-k-1){\binom {n-1}{k}}=(n-1)(n-2){\binom {n-3}{k-1}}}$ , for a total time across all subset sizes ${\textstyle (n-1)(n-2)\sum _{k=1}^{n-2}{\binom {n-3}{k-1}}=(n-1)(n-2)2^{n-3}=\Theta (n^{2}2^{n})}$ . The second stage of the algorithm, finding a complete cycle from $n-1$ candidates, takes $\Theta (n)$ time and does not affect asymptotic performance.

For undirected graphs, the algorithm can be stopped early after the ${\textstyle k=\lfloor {\frac {n-1}{2}}\rfloor }$ step, and finding the minimum ${\textstyle g(S,e)+g(S^{c}\setminus \{1,e\},e)}$ for every ${\textstyle \{(S,e):|S|=\lfloor {\frac {n-1}{2}}\rfloor ,e\in S^{c}\setminus \{1\}\}}$ , where ${\textstyle S^{c}}$ is the complement set of ${\textstyle S}$ . This is analogous to a bidirectional search starting at ${\textstyle 1}$ and meeting at midpoint ${\textstyle e}$ . However, this is a constant factor improvement and does not affect asymptotic performance.

### Space

Storing all values of $g(S,e)$ for subsets of size k requires keeping ${\textstyle (n-k-1){\binom {n-1}{k}}=(n-1){\binom {n-2}{k}}}$ values. A complete table of values of $g(S,e)$ thus requires space ${\textstyle \sum _{k=0}^{n-2}(n-1){\binom {n-2}{k}}=(n-1)2^{n}=\Theta (n2^{n})}$ . This assumes that ${\textstyle n}$ is sufficiently small enough such that ${\textstyle S}$ can be stored as a bitmask of constant multiple of machine words, rather than an explicit k-tuple.

If only the length of the shortest cycle is needed, not the cycle itself, then space complexity can be improved somewhat by noting that calculating $g(S,e)$ for a S of size k requires only values of g for subsets of size $k-1$ . Keeping only the ${\textstyle (n-1)\left[{\binom {n-2}{k-1}}+{\binom {n-2}{k}}\right]}$ values of $g(S,e)$ where S has size either $k-1$ or k reduces the algorithm's maximum space requirements, attained when ${\textstyle k=\left\lfloor {\frac {n}{2}}\right\rfloor }$ , to $\Theta ({\sqrt {n}}2^{n})$ .

## Pseudocode

Source:

```
function algorithm TSP (G, n) is
    for k := 2 to n do
        g({k}, k) := d(1, k)
    end for

    for s := 2 to n−1 do
        for all S ⊆ {2, ..., n}, |S| = s do
            for all k ∈ S do
                g(S, k) := minm≠k,m∈S [g(S\{k}, m) + d(m, k)]
            end for
        end for
    end for

    opt := mink≠1 [g({2, 3, ..., n}, k) + d(k, 1)]
    return (opt)
end function
```

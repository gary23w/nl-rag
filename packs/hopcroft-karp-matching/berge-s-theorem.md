---
title: "Berge's theorem"
source: https://en.wikipedia.org/wiki/Berge's_theorem
domain: hopcroft-karp-matching
license: CC-BY-SA-4.0
tags: hopcroft karp algorithm, bipartite matching, augmenting path, maximum matching
fetched: 2026-07-02
---

# Berge's theorem

In graph theory, **Berge's theorem** states that a matching *M* in a graph *G* is maximum (contains the largest possible number of edges) if and only if there is no **augmenting path** (a path that starts and ends on free (unmatched) vertices, and alternates between edges in and not in the matching) with *M*.

It was proven by French mathematician Claude Berge in 1957 (though already observed by Petersen in 1891 and Kőnig in 1931).

## Proof

To prove Berge's theorem, we first need a lemma. Take a graph *G* and let *M* and *M′* be two matchings in *G*. Let *G′* be the resultant graph from taking the symmetric difference of *M* and *M′*; i.e. (*M* - *M′*) ∪ (*M′* - *M*). *G′* will consist of connected components that are one of the following:

1. An isolated vertex.
2. An even cycle whose edges alternate between *M* and *M′*.
3. A path whose edges alternate between *M* and *M′*, with distinct endpoints.

The lemma can be proven by observing that each vertex in *G′* can be incident to at most 2 edges: one from *M* and one from *M′*. Graphs where every vertex has degree less than or equal to 2 must consist of either isolated vertices, cycles, and paths. Furthermore, each path and cycle in *G′* must alternate between *M* and *M′*. In order for a cycle to do this, it must have an equal number of edges from *M* and *M′*, and therefore be of even length.

Let us now prove the contrapositive of Berge's theorem: *G* has a matching larger than *M* if and only if *G* has an augmenting path. Clearly, an augmenting path *P* of *G* can be used to produce a matching *M′* that is larger than *M* — just take *M′* to be the symmetric difference of *P* and *M* (*M′* contains exactly those edges of *G* that appear in exactly one of *P* and *M*). Hence, the reverse direction follows.

For the forward direction, let *M′* be a matching in *G* larger than *M*. Consider *D*, the symmetric difference of *M* and *M′*. Observe that *D* consists of paths and even cycles (as observed by the earlier lemma). Since *M′* is larger than *M*, *D* contains a component that has more edges from *M′* than *M*. Such a component is a path in *G* that starts and ends with an edge from *M′*, so it is an augmenting path.

## Corollaries

### Corollary 1

Let *M* be a maximum matching and consider an alternating chain such that the edges in the path alternates between being and not being in *M*. If the alternating chain is a cycle or a path of even length starting on an unmatched vertex, then a new maximum matching *M′* can be found by interchanging the edges found in *M* and not in *M*. For example, if the alternating chain is (*m*1, *n*1, *m*2, *n*2, ...), where *m*i ∈ *M* and *n*i ∉ *M*, interchanging them would make all *n*i part of the new matching and make all *m*i not part of the matching.

### Corollary 2

An edge is considered "free" if it belongs to a maximum matching but does not belong to all maximum matchings. An edge *e* is free if and only if, in an arbitrary maximum matching *M*, edge *e* belongs to an even alternating path starting at an unmatched vertex or to an alternating cycle. By the first corollary, if edge *e* is part of such an alternating chain, then a new maximum matching, *M′*, must exist and *e* would exist either in *M* or *M′*, and therefore be free. Conversely, if edge *e* is free, then *e* is in some maximum matching *M* but not in *M′*. Since *e* is not part of both *M* and *M′*, it must still exist after taking the symmetric difference of *M* and *M′*. The symmetric difference of *M* and *M′* results in a graph consisting of isolated vertices, even alternating cycles, and alternating paths. Suppose to the contrary that *e* belongs to some odd-length path component. But then one of *M* and *M′* must have one fewer edge than the other in this component, meaning that the component as a whole is an augmenting path with respect to that matching. By the original lemma, then, that matching (whether *M* or *M′*) cannot be a maximum matching, which contradicts the assumption that both *M* and *M′* are maximum. So, since *e* cannot belong to any odd-length path component, it must either be in an alternating cycle or an even-length alternating path.

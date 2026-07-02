---
title: "Savitch's theorem"
source: https://en.wikipedia.org/wiki/Savitch's_theorem
domain: space-complexity-classes
license: CC-BY-SA-4.0
tags: space complexity, savitch theorem, space hierarchy theorem, reachability problem
fetched: 2026-07-02
---

# Savitch's theorem

In computational complexity theory, **Savitch's theorem**, proved by Walter Savitch in 1970, gives a relationship between deterministic and non-deterministic space complexity. It states that for any space-constructable function $f\in \Omega (\log(n))$ ,

${\mathsf {NSPACE}}\left(f\left(n\right)\right)\subseteq {\mathsf {DSPACE}}\left(f\left(n\right)^{2}\right).$

In other words, if a nondeterministic Turing machine can solve a problem using $f(n)$ space, a deterministic Turing machine can solve the same problem in the square of that space bound. Although it seems that nondeterminism may produce exponential gains in time (as formalized in the unproven exponential time hypothesis), Savitch's theorem shows that it has a markedly more limited effect on space requirements.

The theorem can be relativized. That is, for any oracle, replacing every "Turing machine" with "oracle Turing machine" would still result in a theorem.

## Proof

The proof relies on an algorithm for STCON, the problem of determining whether there is a path between two vertices in a directed graph, which runs in $O\left((\log n)^{2}\right)$ space for n vertices. The basic idea of the algorithm is to solve recursively a somewhat more general problem, testing the existence of a path from a vertex s to another vertex t that uses at most k edges, for a parameter k given as input. STCON is a special case of this problem where k is set large enough to impose no restriction on the paths (for instance, equal to the total number of vertices in the graph, or any larger value). To test for a k -edge path from s to t , a deterministic algorithm can iterate through all vertices u , and recursively search for paths of half the length from s to u and from u to t . This algorithm can be expressed in pseudocode (in Python syntax) as follows:

```mw
def stcon(s, t) -> bool:
    """Test whether a path of any length exists from s to t"""
    return k_edge_path(s, t, n)  # n is the number of vertices

def k_edge_path(s, t, k) -> bool:
    """Test whether a path of length at most k exists from s to t"""
    if k == 0:
        return s == t
    if k == 1:
        return s == t or (s, t) in edges
    for u in vertices:
        if k_edge_path(s, u, floor(k / 2)) and k_edge_path(u, t, ceil(k / 2)):
            return True
    return False
```

Because each recursive call halves the parameter k , the number of levels of recursion is $\lceil \log _{2}n\rceil$ . Each level requires $O(\log n)$ bits of storage for its function arguments and local variables: k and the vertices s , t , and u require $\lceil \log _{2}n\rceil$ bits each. The total auxiliary space complexity is thus $O\left((\log n)^{2}\right)$ . The input graph is considered to be represented in a separate read-only memory and does not contribute to this auxiliary space bound. Alternatively, it may be represented as an implicit graph. Although described above in the form of a program in a high-level language, the same algorithm may be implemented with the same asymptotic space bound on a Turing machine.

This algorithm can be applied to an implicit graph whose vertices represent the configurations of a nondeterministic Turing machine and its tape, running within a given space bound $f(n)$ . The edges of this graph represent the nondeterministic transitions of the machine, s is set to the initial configuration of the machine, and t is set to a special vertex representing all accepting halting states. In this case, the algorithm returns true when the machine has a nondeterministic accepting path, and false otherwise. The number of configurations in this graph is $O(2^{f(n)})$ , from which it follows that applying the algorithm to this implicit graph uses space $O(f(n)^{2})$ . Thus by deciding connectivity in a graph representing nondeterministic Turing machine configurations, one can decide membership in the language recognized by that machine, in space proportional to the square of the space used by the Turing machine.

## Corollaries

Some important corollaries of the theorem include:

**PSPACE = NPSPACE**

That is, the languages that can be recognized by deterministic polynomial-space Turing machines and nondeterministic polynomial-space Turing machines are the same. This follows directly from the fact that the square of a polynomial function is still a polynomial function.

It is believed that a similar relationship does not exist between the polynomial time complexity classes,

P

and

NP

, although this is still an

open question

.

**NL ⊆ L2**

That is, all languages that can be solved nondeterministically in logarithmic space can be solved deterministically in the complexity class

${\mathsf {\color {Blue}L}}^{2}={\mathsf {DSPACE}}\left(\left(\log n\right)^{2}\right).$

This follows from the fact that STCON is

NL-complete

.

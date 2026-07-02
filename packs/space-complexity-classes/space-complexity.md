---
title: "Space complexity"
source: https://en.wikipedia.org/wiki/Space_complexity
domain: space-complexity-classes
license: CC-BY-SA-4.0
tags: space complexity, savitch theorem, space hierarchy theorem, reachability problem
fetched: 2026-07-02
---

# Space complexity

The **space complexity** of an algorithm or a data structure is the amount of memory space required to solve an instance of the computational problem as a function of characteristics of the input. It is the memory required by an algorithm until it executes completely. This includes the memory space used by its inputs, called **input space**, and any other (auxiliary) memory it uses during execution, which is called **auxiliary space**.

Similar to time complexity, space complexity is often expressed asymptotically in big *O* notation, such as $O(n),$ $O(n\log n),$ $O(n^{\alpha }),$ $O(2^{n}),$ etc., where n is a characteristic of the input influencing space complexity.

## Space complexity classes

Analogously to time complexity classes DTIME(f(n)) and NTIME(f(n)), the complexity classes DSPACE(f(n)) and NSPACE(f(n)) are the sets of languages that are decidable by deterministic (respectively, non-deterministic) Turing machines that use $O(f(n))$ space. The complexity classes PSPACE and NPSPACE allow f to be any polynomial, analogously to P and NP. That is, ${\mathsf {PSPACE}}=\bigcup _{c\in \mathbb {Z} ^{+}}{\mathsf {DSPACE}}(n^{c})$ and ${\mathsf {NPSPACE}}=\bigcup _{c\in \mathbb {Z} ^{+}}{\mathsf {NSPACE}}(n^{c})$

## Relationships between classes

The space hierarchy theorem states that, for all space-constructible functions $f(n),$ there exists a problem that can be solved by a machine with $f(n)$ memory space, but cannot be solved by a machine with asymptotically less than $f(n)$ space.

The following containments between complexity classes hold. ${\mathsf {DTIME}}(f(n))\subseteq {\mathsf {DSPACE}}(f(n))\subseteq {\mathsf {NSPACE}}(f(n))\subseteq {\mathsf {DTIME}}\left(2^{O(f(n))}\right)$

Furthermore, Savitch's theorem gives the reverse containment that if $f\in \Omega (\log(n)),$ ${\mathsf {NSPACE}}(f(n))\subseteq {\mathsf {DSPACE}}\left((f(n))^{2}\right).$

As a direct corollary, ${\mathsf {PSPACE}}={\mathsf {NPSPACE}}.$ This result is surprising because it suggests that non-determinism can reduce the space necessary to solve a problem only by a small amount. In contrast, the exponential time hypothesis conjectures that for time complexity, there can be an exponential gap between deterministic and non-deterministic complexity.

The Immerman–Szelepcsényi theorem states that, again for $f\in \Omega (\log(n)),$ ${\mathsf {NSPACE}}(f(n))$ is closed under complementation. This shows another qualitative difference between time and space complexity classes, as nondeterministic time complexity classes are not believed to be closed under complementation; for instance, it is conjectured that NP ≠ co-NP.

## LOGSPACE

L or LOGSPACE is the set of problems that can be solved by a deterministic Turing machine using only $O(\log n)$ memory space with regards to input size. Even a single counter that can index the entire n -bit input requires $\log n$ space, so LOGSPACE algorithms can maintain only a constant number of counters or other variables of similar bit complexity.

LOGSPACE and other sub-linear space complexity is useful when processing large data that cannot fit into a computer's RAM. They are related to Streaming algorithms, but only restrict how much memory can be used, while streaming algorithms have further constraints on how the input is fed into the algorithm. This class also sees use in the field of pseudorandomness and derandomization, where researchers consider the open problem of whether L = RL.

The corresponding nondeterministic space complexity class is NL.

## Auxiliary space complexity

The term **auxiliary space** refers to space other than that consumed by the input. Auxiliary space complexity could be formally defined in terms of a Turing machine with a separate *input tape* which cannot be written to, only read, and a conventional working tape which can be written to. The auxiliary space complexity is then defined (and analyzed) via the working tape. For example, consider the depth-first search of a balanced binary tree with n nodes: its auxiliary space complexity is $\Theta (\log n).$

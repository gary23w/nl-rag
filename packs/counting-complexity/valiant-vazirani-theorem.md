---
title: "Valiant–Vazirani theorem"
source: https://en.wikipedia.org/wiki/Valiant%E2%80%93Vazirani_theorem
domain: counting-complexity
license: CC-BY-SA-4.0
tags: counting complexity, permanent computation, toda theorem, counting problem
fetched: 2026-07-02
---

# Valiant–Vazirani theorem

The **Valiant–Vazirani theorem** is a theorem in computational complexity theory stating that if there is a polynomial time algorithm for Unambiguous-SAT, then NP = RP. It was proven by Leslie Valiant and Vijay Vazirani in their paper titled *NP is as easy as detecting unique solutions* published in 1986.

The Valiant–Vazirani theorem implies that the Boolean satisfiability problem, which is NP-complete, remains a computationally hard problem even if the input instances are promised to have at most one satisfying assignment.

## Proof outline

Unambiguous-SAT is the promise problem of deciding whether a given Boolean formula that has at most one satisfying assignment is unsatisfiable or has exactly one satisfying assignment. In the first case, an algorithm for Unambiguous-SAT should reject, and in the second it should accept the formula. If the formula has more than one satisfying assignment, then there is no condition on the behavior of the algorithm. The promise problem Unambiguous-SAT can be decided by a nondeterministic Turing machine that has at most one accepting computation path, thus it belongs to the promise version of the complexity class UP (the class UP as such is only defined for languages).

The proof of the Valiant–Vazirani theorem consists of a probabilistic reduction that given a formula *F* in *n* variables, outputs a sequence of formulas *G*0,...,*Gn* such that:

- Every satisfying assignment of any *Gi* also satisfies *F*. Thus, if *F* is unsatisfiable, then all *Gi*, *i* ≤ *n*, are unsatisfiable.
- If *F* is satisfiable, then with probability at least 1/4, some *Gi* has a unique satisfying assignment.

The idea of the reduction is to successively intersect the solution space of the formula *F* with *n* random linear hyperplanes in $\mathbb {F} _{2}^{n}$ .

As a consequence (not needed for the **NP** = **RP** argument, but of independent interest), if we choose one of the *Gi* at random, we obtain a randomized reduction with one-sided error from SAT to Unambiguous-SAT that succeeds with probability at least Ω(1/*n*). That is, if *F* is unsatisfiable, the output formula is always unsatisfiable, and if *F* is satisfiable, then the output formula has a unique satisfying assignment with probability Ω(1/*n*).

Now, assuming Unambiguous-SAT is solvable by a polynomial time algorithm *A*, we obtain an **RP** algorithm for SAT by running *A* on *Gi* for each *i* ≤ *n*. If *F* is unsatisfiable, then *A* rejects all *Gi* as they are unsatisfiable, whereas if *F* is satisfiable, then *A* accepts some *Gi* with probability at least 1/4. (We can improve the acceptance probability by repeating the reduction several times.)

More generally, this argument shows unconditionally that **NP** is included in **RPpromiseUP**.

An alternative proof is based on the isolation lemma by Mulmuley, Vazirani, and Vazirani. They consider a more general setting, and applied to the setting here this gives an isolation probability of only $\Omega (1/n^{8})$ .

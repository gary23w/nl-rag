---
title: "Immerman–Szelepcsényi theorem"
source: https://en.wikipedia.org/wiki/Immerman%E2%80%93Szelepcs%C3%A9nyi_theorem
domain: space-complexity-classes
license: CC-BY-SA-4.0
tags: space complexity, savitch theorem, space hierarchy theorem, reachability problem
fetched: 2026-07-02
---

# Immerman–Szelepcsényi theorem

In computational complexity theory, the **Immerman–Szelepcsényi theorem** states that nondeterministic space complexity classes are closed under complementation. It was proven independently by Neil Immerman and Róbert Szelepcsényi in 1987, for which they shared the 1995 Gödel Prize. In its general form the theorem states that NSPACE(*s*(*n*)) = co-NSPACE(*s*(*n*)) for any function *s*(*n*) ≥ log *n*. The result is equivalently stated as NL = co-NL; although this is the special case when *s*(*n*) = log *n*, it implies the general theorem by a standard padding argument. The result solved the second LBA problem.

In other words, if a nondeterministic machine can solve a problem, another machine with the same resource bounds can solve its complement problem (with the *yes* and *no* answers reversed) in the same asymptotic amount of space. No similar result is known for the time complexity classes, and indeed it is conjectured that NP is not equal to co-NP.

The principle used to prove the theorem has become known as inductive counting. It has also been used to prove other theorems in computational complexity, including the closure of LOGCFL under complementation and the existence of error-free randomized logspace algorithms for USTCON.

## Proof

We prove here that NL = co-NL. The theorem is obtained from this special case by a padding argument.

The st-connectivity problem asks, given a digraph *G* and two vertices *s* and *t*, whether there is a directed path from *s* to *t* in *G*. This problem is NL-complete, therefore its complement *st-non-connectivity* is co-NL-complete. It suffices to show that *st-non-connectivity* is in NL. This proves co-NL ⊆ NL, and by complementation, NL ⊆ co-NL.

We fix a digraph *G*, a source vertex *s*, and a target vertex *t*. We denote by *R**k* the set of vertices which are reachable from *s* in at most *k* steps. Note that if *t* is reachable from *s*, it is reachable in at most *n-1* steps, where *n* is the number of vertices, therefore we are reduced to testing whether *t* ∉ *R**n-1*.

We remark that *R*0 = { *s* }, and *R**k*+1 is the set of vertices *v* which are either in *R**k*, or the target of an edge *w* → *v* where *w* is in *R**k*. This immediately gives an algorithm to decide *t* ∈ *R**n*, by successively computing *R**1*, …, *R**n*. However, this algorithm uses too much space to solve the problem in NL, since storing a set *R**k* requires one bit per vertex.

The crucial idea of the proof is that instead of computing *R**k*+1 from *R**k*, it is possible to compute the *size* of *R**k*+1 from the *size* of *R**k*, with the help of non-determinism. We iterate over vertices and increment a counter for each vertex that is found to belong to *R**k*+1. The problem is how to determine whether *v* ∈ *R**k*+1 for a given vertex *v*, when we only have the size of *R**k* available.

To this end, we iterate over vertices *w*, and for each *w*, we non-deterministically *guess* whether *w* ∈ *R**k*. If we guess *w* ∈ *R**k*, and *v* = *w* or there is an edge *w* → *v*, then we determine that *v* belongs to *R**k*+1. If this fails for all vertices *w*, then *v* does not belong to *R**k*+1.

Thus, the computation that determines whether *v* belongs to *R**k*+1 splits into branches for the different guesses of which vertices belong to *R**k*. A mechanism is needed to make all of these branches abort (reject immediately), except the one where all the guesses were correct. For this, when we have made a “yes-guess” that *w* ∈ *R**k*, we *check* this guess, by non-deterministically looking for a path from *s* to *w* of length at most *k*. If this check fails, we abort the current branch. If it succeeds, we increment a counter of “yes-guesses”. On the other hand, we do not check the “no-guesses” that *w* ∉ *R**k* (this would require solving *st-non-connectivity*, which is precisely the problem that we are solving in the first place). However, at the end of the loop over *w*, we check that the counter of “yes-guesses” matches the size of *R**k*, which we know. If there is a mismatch, we abort. Otherwise, all the “yes-guesses” were correct, and there was exactly the right number of them, thus all “no-guesses” were correct as well.

This concludes the computation of the size of *R**k*+1 from the size of *R**k*. Iteratively, we compute the sizes of *R*1, *R*2, …, *R**n-2*. Finally, we check whether *t* ∈ *R**n-1*, which is possible from the size of *R**n*-2 by the sub-algorithm that is used inside the computation of the size of *R**k*+1.

The following pseudocode summarizes the algorithm:

```
function verify_reachable(G, s, w, k)
    // Verifies that w ∈ Rk. If this is not the case, aborts
    // the current computation branch, rejecting the input.
    if s = w then
        return
    c ← s
    repeat k times
        // Aborts if there is no edge from c, otherwise
        // non-deterministically branches
        guess an edge c → d in G
        c ← d
        if c = w then
            return
    // We did not guess a path.
    reject

function is_reachable(G, s, v, k, S)
    // Assuming that Rk has size S, determines whether v ∈ Rk+1.
    reachable ← false
    yes_guesses ← 0 // counter of yes-guesses w ∈ Rk
    for each vertex w of G do
        // Guess whether w ∈ Rk
        guess a boolean b
        if b then
            verify_reachable(G, s, w, k)
            yes_guesses += 1
            if v = w or there is an edge w → v in G then
                reachable ← true
    if yes_guesses ≠ S then
        reject // wrong number of yes-guesses
    return reachable

function st_non_connectivity(G, s, t)
    n ← vertex_count(G)
    // Size of Rk, initially 1 because R0 = {s}
    S ← 1
    for k from 0 to n-3 do
        S' ← 0 // size of Rk+1
        for each vertex v of G do
            if is_reachable(G, s, v, k, S) then
                S' += 1
        S ← S'
    return not is_reachable(G, s, t, n-2, S)
```

## Logspace hierarchy

As a corollary, in the same article, Immerman proved that, using descriptive complexity's equality between NL and FO(Transitive Closure), the logarithmic hierarchy, i.e. the languages decided by an alternating Turing machine in logarithmic space with a bounded number of alternations, is the same class as NL.

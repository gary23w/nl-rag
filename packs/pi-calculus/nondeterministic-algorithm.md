---
title: "Nondeterministic algorithm"
source: https://en.wikipedia.org/wiki/Nondeterministic_algorithm
domain: pi-calculus
license: CC-BY-SA-4.0
tags: pi-calculus, process calculus, name passing, mobile process
fetched: 2026-07-02
---

# Nondeterministic algorithm

In computer science and computer programming, a **nondeterministic algorithm** is an algorithm that, even for the same input, can exhibit different behaviors on different runs, as opposed to a deterministic algorithm.

Different models of computation give rise to different reasons that an algorithm may be non-deterministic, and different ways to evaluate its performance or correctness:

- A concurrent algorithm can perform differently on different runs due to a race condition. This can happen even with a single-threaded algorithm when it interacts with resources external to it. In general, such an algorithm is considered to perform correctly only when *all* possible runs produce the desired results.
- A probabilistic algorithm's behavior depends on a random number generator called by the algorithm. These are subdivided into Las Vegas algorithms, for which (like concurrent algorithms) all runs must produce correct output, and Monte Carlo algorithms which are allowed to fail or produce incorrect results with low probability. The performance of such an algorithm is often measured probabilistically, for instance using an analysis of its expected time.
- In computational complexity theory, nondeterminism is often modeled using an explicit mechanism for making a nondeterministic choice, such as in a nondeterministic Turing machine. For these models, a nondeterministic algorithm is considered to perform correctly when, for each input, *there exists* a run that produces the desired result, even when other runs produce incorrect results. This existential power makes nondeterministic algorithms of this sort more efficient than known deterministic algorithms for many problems. The P versus NP problem encapsulates this conjectured greater efficiency available to nondeterministic algorithms. Algorithms of this sort are used to define complexity classes based on nondeterministic time and nondeterministic space complexity. They may be simulated using nondeterministic programming, a method for specifying nondeterministic algorithms and searching for the choices that lead to a correct run, often using a backtracking search.

## History

Explicit algorithms using randomness were considered before formalizing the concept of nondeterminism in computer science. In 1917, Henry C. Pocklington introduced a randomized algorithm known as Pocklington's algorithm for efficiently finding square roots modulo prime numbers. In the 1930s, Enrico Fermi experimented with the Monte Carlo method while studying neutron diffusion, but he did not publish this work. Scientists at the Los Alamos National Laboratory in the 1940s and 50s developed and implemented the concept leading to the first publications concerned with Monte Carlo algorithms.

Michael O. Rabin and Dana Scott introduced and formalized nondeterministic finite automatons (NFA) in 1959. In that paper they show the equivalence to deterministic finite automatons (DFA) in terms of the ability to recognize languages. They also apply them to Turing machines (TM) thereby introducing nondeterministic Turing machines (NTM). Using NFAs they could reprove in a more streamlined way certain closure properties of regular languages previously established by Stephen C. Kleene and others.

The term *nondeterministic algorithm* was used by Robert W. Floyd as early as 1967. The paper uses the graphical language of flow charts which is a different way to formalize algorithms compared to automata or Turing machines and at that time was closer to the practice of programming on electronic computers.

In philosophy ideas revolving around determinism vs. free will go back at least to ancient Greece. It is worth noting that nondeterminacy as a concept in computer science refers to a rather limited choice between previously explicitly defined, often only finitely many options in each computational step, while in philosophy the possible options do not necessarily have to be laid out or formally defined beforehand. In particular because of this additional property nondeterminism in computer science constitutes a new development compared to nondeterminism in traditional philosophy.

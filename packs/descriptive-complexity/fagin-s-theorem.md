---
title: "Fagin's theorem"
source: https://en.wikipedia.org/wiki/Fagin's_theorem
domain: descriptive-complexity
license: CC-BY-SA-4.0
tags: descriptive complexity, second order logic, fagin theorem, finite model theory
fetched: 2026-07-02
---

# Fagin's theorem

**Fagin's theorem** is the oldest result of descriptive complexity theory, a branch of computational complexity theory that characterizes complexity classes in terms of logic-based descriptions of their problems rather than by the behavior of algorithms for solving those problems. The theorem states that the set of all properties expressible in existential second-order logic is precisely the complexity class NP.

It was proven by Ronald Fagin in 1973 in his doctoral thesis, and appears in his 1974 paper. The arity required by the second-order formula was improved (in one direction) by James Lynch in 1981, and several results of Étienne Grandjean have provided tighter bounds on nondeterministic random-access machines.

## Example

For example, consider the problem of deciding if a graph is 3-colorable. This is NP-complete. By Fagin’s theorem, there is a second order existential formula $\phi$ , such that a graph is 3-colorable if and only if the graph, as a finite model for $\phi$ , semantically implies $\phi$ . Explicitly, here is one such formula:

> (∃A, B, C)(∀v)[(A(v) ∨ B(v) ∨ C(v)) ∧ (∀w)(E(v, w) → ¬(A(v) ∧ A(w)) ∧ ¬(B(v) ∧ B(w)) ∧ ¬(C(v) ∧ C(w)))]

In this formula, A, B, or C are to be interpreted as the sets of vertices colored with the 3 colors, and E(v, w) is to be interpreted as saying the vertices v, w share an edge. The formula then states that no two adjacent vertices have the same color.

Note that there is no need to explicitly enforce each vertex to have *exactly* 1 color, just at least 1 color. Since, if we allow more than 1 color per vertex, and no two adjacent vertices have the same color, then we certainly can have each vertex to have exactly 1 color, and still no two adjacent vertices have the same color.

## Proof

The 1999 textbook by Immerman provides a detailed proof of the theorem. A sketch is given here.

It is straightforward to show that every existential second-order formula can be recognized in NP, by nondeterministically choosing the value of all existentially-qualified variables, so the main part of the proof is to show that every language in NP can be described by an existential second-order formula. To do so, one can use second-order existential quantifiers to arbitrarily choose a computation tableau. In more detail, for every timestep of an execution trace of a non-deterministic Turing machine, this tableau encodes the state of the Turing machine, its position in the tape, the contents of every tape cell, and which nondeterministic choice the machine makes at that step. A first-order formula can constrain this encoded information so that it describes a valid execution trace, one in which the tape contents and Turing machine state and position at each timestep follow from the previous timestep.

A key lemma used in the proof is that it is possible to encode a linear order of length $n^{k}$ (such as the linear orders of timesteps and tape contents at any timestep) as a $2k$ -ary relation R on a universe A of size n . One way to achieve this is to choose a linear ordering L of A and then define R to be the lexicographical ordering of k -tuples from A with respect to L .

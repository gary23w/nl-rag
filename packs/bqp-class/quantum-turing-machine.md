---
title: "Quantum Turing machine"
source: https://en.wikipedia.org/wiki/Quantum_Turing_machine
domain: bqp-class
license: CC-BY-SA-4.0
tags: bounded error quantum polynomial, quantum turing machine, shor algorithm, grover algorithm
fetched: 2026-07-02
---

# Quantum Turing machine

A **quantum Turing machine** (**QTM**) or **universal quantum computer** is an abstract machine used to model the effects of a quantum computer. It provides a simple model that captures all of the power of quantum computation—that is, any quantum algorithm can be expressed formally as a particular quantum Turing machine. However, the computationally equivalent quantum circuit is a more common model.

Quantum Turing machines can be related to classical and probabilistic Turing machines in a framework based on transition matrices. That is, a matrix can be specified whose product with the matrix representing a classical or probabilistic machine provides the quantum probability matrix representing the quantum machine. This was shown by Lance Fortnow.

## Informal sketch

Unsolved problem in physics

Is a

universal quantum computer

sufficient to

efficiently

simulate

an arbitrary physical system?

More unsolved problems in physics

A way of understanding the quantum Turing machine (QTM) is that it generalizes the classical Turing machine (TM) in the same way that the quantum finite automaton (QFA) generalizes the deterministic finite automaton (DFA). In essence, the internal states of a classical TM are replaced by pure or mixed states in a Hilbert space; the transition function is replaced by a collection of unitary matrices that map the Hilbert space to itself.

That is, a classical Turing machine is described by a 7-tuple $M=\langle Q,\Gamma ,b,\Sigma ,\delta ,q_{0},F\rangle$ . See the formal definition of a Turing Machine for a more in-depth understanding of each of the elements in this tuple.

For a three-tape quantum Turing machine (one tape holding the input, a second tape holding intermediate calculation results, and a third tape holding output):

- The set of states Q is replaced by a Hilbert space.
- The tape alphabet symbols $\Gamma$ are likewise replaced by a Hilbert space (usually a different Hilbert space than the set of states).
- The blank symbol $b\in \Gamma$ is an element of the Hilbert space.
- The input and output symbols $\Sigma$ are usually taken as a discrete set, as in the classical system; thus, neither the input nor output to a quantum machine need be a quantum system itself.
- The transition function $\delta :\Sigma \times Q\otimes \Gamma \to \Sigma \times Q\otimes \Gamma \times \{L,R\}$ is a generalization of a semiautomaton and is understood to be a collection of unitary matrices that are automorphisms of the Hilbert space Q .
- The initial state $q_{0}\in Q$ may be either a mixed state or a pure state.
- The set F of *final* or *accepting states* is a linear subspace of the Hilbert space Q .

The above is merely a sketch of a quantum Turing machine, rather than its formal definition, as it leaves vague several important details: for example, how often a measurement is performed; see for example, the difference between a measure-once and a measure-many QFA. This question of measurement affects the way in which writes to the output tape are defined.

## History

In 1980 and 1982, physicist Paul Benioff published articles that first described a quantum-mechanical model of Turing machines. A 1985 article written by Oxford University physicist David Deutsch further developed the idea of quantum computers by suggesting that quantum gates could function in a similar fashion to traditional digital computing binary logic gates.

Iriyama, Ohya, and Volovich have developed a model of a *linear quantum Turing machine* (LQTM). This is a generalization of a classical QTM that has mixed states and that allows irreversible transition functions. These allow the representation of quantum measurements without classical outcomes.

A *quantum Turing machine with postselection* was defined by Scott Aaronson, who showed that the class of polynomial time on such a machine (PostBQP) is equal to the classical complexity class PP.

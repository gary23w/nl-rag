---
title: "Reachability problem"
source: https://en.wikipedia.org/wiki/Reachability_problem
domain: network-verification
license: CC-BY-SA-4.0
tags: network verification, formal verification, model checking, reachability analysis
fetched: 2026-07-02
---

# Reachability problem

**Reachability** is a fundamental problem which can be formulated as follows: *Given a computational system with a set of allowed rules or transformations, decide whether a certain state of a system is reachable from a given initial state of the system.* It appears in several different contexts: finite- and infinite-state concurrent systems, cellular automata and Petri nets, program analysis, discrete and continuous systems, time critical systems, hybrid systems, rewriting systems, probabilistic and parametric systems, and open systems modelled as games.

Variants of the reachability problem may result from additional constraints on the initial or final states, specific requirement for reachability paths as well as for iterative reachability or changing the questions into analysis of winning strategies in infinite games or unavoidability of some dynamics.

Typically, for a fixed system description given in some form (reduction rules, systems of equations, logical formulas, etc.) a reachability problem consists of checking whether a given set of target states can be reached starting from a fixed set of initial states. The set of target states can be represented explicitly or via some implicit representation (e.g., a system of equations, a set of minimal elements with respect to some ordering on the states). Sophisticated quantitative and qualitative properties can often be reduced to basic reachability questions. Decidability and complexity boundaries, algorithmic solutions, and efficient heuristics are all important aspects to be considered in this context. Algorithmic solutions are often based on different combinations of exploration strategies, symbolic manipulations of sets of states, decomposition properties, or reduction to linear programming problems, and they often benefit from approximations, abstractions, accelerations and extrapolation heuristics. Ad hoc solutions as well as solutions based on general purpose constraint solvers and deduction engines are often combined in order to balance efficiency and flexibility.

## Variants of reachability problems

### Finite explicit graph

The reachability problem in an oriented graph described explicitly is NL-complete. Reingold, in a 2008 article, proved that the reachability problem for a non-oriented graph is in LOGSPACE.

In model checking, reachability corresponds to a property of liveliness.

### Finite implicit graph

In planning, more precisely in classical planning, one is interested in knowing if one can attain a state from an initial state from a description of actions. The description of actions defines a graph of implicit states, which is of exponential size in the size of the description.

In symbolic model checking, the model (the underlying graph) is described with the aid of a symbolic representation such as binary decision diagrams.

### Petri nets

The reachability problem in a Petri net is decidable. Since 1976, it is known that this problem is EXPSPACE-hard. There are results on how much to implement this problem in practice. In 2018, the problem was shown to be a nonelementary problem. In 2022 it was shown to be complete for Ackermann function time complexity.

### Vector addition systems

In 2022 reachability in vector addition systems was shown to be Ackermann-complete and therefore a nonelementary problem.

## International Conference on Reachability Problems (RP)

The International Conference on Reachability Problems series, previously known as Workshop on Reachability Problems, is an annual academic conference which gathers together researchers from diverse disciplines and backgrounds interested in reachability problems that appear in algebraic structures, computational models, hybrid systems, infinite games, logic and verification. The workshop tries to fill the gap between results obtained in different fields but sharing common mathematical structure or conceptual difficulties.

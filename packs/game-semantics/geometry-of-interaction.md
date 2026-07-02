---
title: "Geometry of interaction"
source: https://en.wikipedia.org/wiki/Geometry_of_interaction
domain: game-semantics
license: CC-BY-SA-4.0
tags: game semantics, dialogical logic, full abstraction, strategy (game theory)
fetched: 2026-07-02
---

# Geometry of interaction

In proof theory, the **Geometry of Interaction** (GoI) was introduced by Jean-Yves Girard shortly after his work on linear logic. In linear logic, proofs can be seen as various kinds of networks as opposed to the flat tree structures of sequent calculus. To distinguish the real proof nets from all the possible networks, Girard devised a criterion involving trips in the network. Trips can in fact be seen as some kind of operator acting on the proof. Drawing from this observation, Girard described directly this operator from the proof and has given a formula, the so-called *execution formula*, encoding the process of cut elimination at the level of operators. Subsequent constructions by Girard proposed variants in which proofs are represented as flows, or operators in von Neumann algebras. Those models were later generalised by Seiller's Interaction Graphs models.

One of the first significant applications of GoI was a better analysis of Lamping's algorithm for optimal reduction for the lambda calculus. GoI had a strong influence on game semantics for linear logic and PCF.

Beyond the dynamic interpretation of proofs, geometry of interaction constructions provide models of linear logic, or fragments thereof. This aspect has been extensively studied by Seiller under the name of linear realisability, a version of realizability accounting for linearity.

GoI has been applied to deep compiler optimisation for lambda calculi. A bounded version of GoI dubbed **the Geometry of Synthesis** has been used to compile higher-order programming languages directly into static circuits.

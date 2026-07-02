---
title: "Wireworld"
source: https://en.wikipedia.org/wiki/Wireworld
domain: cellular-automata
license: CC-BY-SA-4.0
tags: cellular automaton, game of life, elementary cellular automaton, rule 110
fetched: 2026-07-02
---

# Wireworld

**Wireworld**, alternatively **WireWorld**, is a cellular automaton first proposed by Brian Silverman in 1987, as part of his program Phantom Fish Tank. It subsequently became more widely known as a result of an article in the "Computer Recreations" column of *Scientific American*. Wireworld is particularly suited to simulating transistors, and is Turing-complete.

## Rules

A Wireworld cell can be in one of four different states, usually numbered 0–3 in software, modeled by colors in the examples here:

1. empty (black),
2. electron head (blue),
3. electron tail (red),
4. conductor (yellow).

As in all cellular automata, time proceeds in discrete steps called generations (sometimes "gens" or "ticks"). Cells behave as follows:

- empty → empty,
- electron head → electron tail,
- electron tail → conductor,
- conductor → electron head if exactly one or two of the neighbouring cells are electron heads, otherwise remains conductor.

Wireworld uses what is called the Moore neighborhood, which means that in the rules above, neighbouring means one cell away (range value of one) in any direction, both orthogonal and diagonal.

These simple rules can be used to construct logic gates (see below).

## Applications

Entities built within Wireworld universes include Langton's ant (allowing any Langton's ant pattern to be built within Wireworld) and the Wireworld computer, a Turing-complete computer implemented as a cellular automaton.

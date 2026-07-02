---
title: "Fault model"
source: https://en.wikipedia.org/wiki/Fault_model
domain: design-for-test
license: CC-BY-SA-4.0
tags: design for test, test pattern generation, fault model, built-in self-test
fetched: 2026-07-02
---

# Fault model

A **fault model** is an engineering model of something that could go wrong in the construction or operation of a piece of equipment. From the model, the designer or user can then predict the consequences of this particular fault. Fault models can be used in almost all branches of engineering.

## Basic fault models

Basic **fault models** in digital circuits include:

- Static faults, which give incorrect values at any speed and sensitized by performing only one operation:
  - The stuck-at fault model. A signal, or gate output, is stuck at a 0 or 1 value, independent of the inputs to the circuit.
  - The bridging fault model. Two signals are connected together when they should not be. Depending on the logic circuitry employed, this may result in a *wired-OR* or *wired-AND* logic function. Since there are *O(n^2)* potential bridging faults, they are normally restricted to signals that are physically adjacent in the design.
  - The transistor faults. This model is used to describe faults for CMOS logic gates. At transistor level, a transistor could be stuck-short or stuck-open. In stuck-short, a transistor behaves as if it always conducts (or stuck-on), and stuck-open is when a transistor never conducts current (or stuck-off). Stuck-short produces a short between VDD and VSS.
  - The open fault model. Here a wire is assumed broken, and one or more inputs are disconnected from the output that drives them. As with bridging faults, the resulting behavior depends on the circuit implementation.
- Dynamic faults, only at-speed and are sensitized by performing multiple operations sequentially:
  - The transition delay fault (or transition fault) model, where the signal eventually assumes the correct value, but more slowly (or rarely, more quickly) than normal.
  - Small-delay-defect model

## Fault assumption

A fault model falls under one of the following assumptions:

- Single fault assumption: Only one fault occurs in a circuit. if we define *k* possible fault types in our fault model, the circuit has *n* signal lines; by single fault assumption, the total number of single faults is *k×n*.
- Multiple fault assumption: Multiple faults might occur in a circuit.

## Fault collapsing

There are two main ways for collapsing fault sets into smaller sets.

### Equivalence collapsing

It is possible that two or more faults produce same faulty behavior for all input patterns. These faults are called equivalent faults. Any single fault from the set of equivalent faults can represent the whole set. In this case, much less than k×n fault tests are required for a circuit with n signal line. removing equivalent faults from entire set of faults is called fault collapsing. fault collapsing significantly decreases the number of faults to check.

In the example diagram, red faults are equivalent to the faults that being pointed to with the arrows, so those red faults can be removed from the circuit. In this case, the fault collapse ratio is 12/20.

### Dominance collapsing

Fault F is called dominant to F' if all tests of F' detects F. In this case, F can be removed from the fault list. If F dominates F' and F' dominates F, then these two faults are equivalent.

In the example, a NAND gate has been shown, the set of all input values that can test output's SA0 is {00,01,10}. the set of all input values that can check first input's SA1 is {01}. In this case, output SA0 fault is dominant and can be removed from fault list.

### Functional collapsing

Two faults are functionally equivalent if they produce identical faulty functions or we can say, two faults are functionally equivalent if we can not distinguish them at primary outputs (PO) with any input test vector.

## In aerospace contexts

A fault model in an aerospace context is a set of structured information which helps users or systems to identify and isolate a problem that occurs on an engine, line-replaceable unit (LRU), or auxiliary power unit (APU) during a flight. Associated with this fault model may be a suggested repair procedure along with references to aircraft maintenance manuals (~ Light maintenance manual).

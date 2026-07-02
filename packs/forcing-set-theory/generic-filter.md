---
title: "Generic filter"
source: https://en.wikipedia.org/wiki/Generic_filter
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Generic filter

In the mathematical field of set theory, a **generic filter** is a kind of object used in the theory of forcing, a technique used for many purposes, but especially to establish the independence of certain propositions from certain formal theories, such as ZFC. For example, Paul Cohen used forcing to establish that ZFC, if consistent, cannot prove the continuum hypothesis, which states that there are exactly $\aleph _{1}$ real numbers. In the contemporary re-interpretation of Cohen's proof, it proceeds by constructing a generic filter that codes more than $\aleph _{1}$ reals, without changing the value of $\aleph _{1}$ .

Formally, let *P* be a partially ordered set, and let *F* be a filter on *P*; that is, *F* is a subset of *P* such that:

1. *F* is nonempty
2. If *p*, *q* ∈ *P* and *p* ≤ *q* and *p* is an element of *F*, then *q* is an element of *F* (*F* is closed upward)
3. If *p* and *q* are elements of *F*, then there is an element *r* of *F* such that *r* ≤ *p* and *r* ≤ *q* (*F* is downward directed)

Now if *D* is a collection of dense open subsets of *P*, in the topology whose basic open sets are all sets of the form {*q*∈*P* | *q* ≤ *p*} for particular *p* in *P*, then *F* is said to be ***D*-generic** if *F* meets all sets in *D*; that is,

$F\cap E\neq \varnothing ,\,$

for all

E

∈

D

.

Similarly, if *M* is a transitive model of ZFC (or some sufficient fragment of ZFC), with *P* an element of *M* (partially ordered by ∈), then *F* is said to be ***M*-generic**, or sometimes **generic over *M***, if *F* meets all dense open subsets of *P* that are elements of *M*.

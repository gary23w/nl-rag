---
title: "Power domains"
source: https://en.wikipedia.org/wiki/Powerdomain
domain: denotational-domains
license: CC-BY-SA-4.0
tags: domain theory, directed-complete partial order, continuous function, algebraic lattice
fetched: 2026-07-02
---

# Power domains

(Redirected from

Powerdomain

)

In denotational semantics and domain theory, **power domains** are domains of nondeterministic and concurrent computations.

The idea of power domains for functions is that a nondeterministic function may be described as a deterministic set-valued function, where the set contains all values the nondeterministic function can take for a given argument. For concurrent systems, the idea is to express the set of all possible computations.

Roughly speaking, a power domain is a domain whose elements are certain subsets of a domain. Taking this approach naively, though, often gives rise to domains that don't quite have the desired properties, and so one is led to increasingly complicated notions of the power domain. There are three common variants: the Plotkin, upper, and lower power domains. One way to understand these concepts is as free models of theories of nondeterminism.

For most of this article we use the terms "domain" and "continuous function" quite loosely, meaning respectively some kind of ordered structure and some kind of limit-preserving function. This flexibility is genuine; for example, in some concurrent systems it is natural to impose the condition that every message sent must eventually be delivered. However, the limit of a chain of approximations in which a message was not delivered, would be a completed computation in which the message was never delivered!

A modern reference to this subject is the chapter by Abramsky and Jung [1994]. Older references include those of Plotkin [1983, Chapter 8] and Smyth [1978].

## Power domains as free models of theories of non-determinism

Domain theorists have come to understand power domains abstractly as free models for theories of non-determinism. Just as the finite-powerset construction is the free semilattice, the powerdomain constructions should be understood abstractly as free models of theories of non-determinism. By changing the theories of non-determinism, different power domains arise.

The abstract characterisation of powerdomains is often the easiest way to work with them, because explicit descriptions are so intricate. (One exception is the Hoare powerdomain, which has a rather straightforward description.)

### Theories of non-determinism

We recall three theories of non-determinism. They are variations of the theory of semilattices. The theories are not algebraic theories in the conventional sense, because some involve the order of the underlying domain.

All theories have one sort *X*, and one binary operation ∪. The idea is that the operation ∪: *X* × *X* → *X* takes two combinations and returns the non-deterministic choice of them.

The **Plotkin powertheory** (after Gordon Plotkin) has the following axioms:

- Idempotency: *x* ∪ *x* = *x*
- Commutativity: *x* ∪ *y* = *y* ∪ *x*
- Associativity: (*x* ∪ *y*) ∪ *z* = *x* ∪ (*y* ∪ *z*)

The **lower** (or **Hoare**, after Tony Hoare) powertheory consists of the Plotkin powertheory augmented with the inequality

- *x* ≤ *x* ∪ *y*.

The **upper** (or **Smyth**, after M. B. Smyth) powertheory consists of the Plotkin powertheory augmented with the inequality

- *x* ∪ *y* ≤ *x*.

### Models of the powertheories

A model of the Plotkin powertheory is a continuous semilattice: it is a semilattice whose carrier is a domain and for which the operation is continuous. Note that the operator need not be a meet or join for the order of the domain. A morphism of continuous semilattices is a continuous function between their carriers that is also a semilattice homomorphism.

Models of the lower powertheory are called inflationary semilattices; there is an additional requirement that the operator behave somewhat like a join for the order. For the upper powertheory, models are called deflationary semilattices; here, the operator behaves somewhat like a meet.

### Power domains as free models

Let *D* be a domain. The Plotkin powerdomain on *D* is the free model of the Plotkin powertheory over *D*. It is defined to be (when it exists) a model *P*(*D*) of the Plotkin powertheory (i.e. a continuous semilattice) equipped with a continuous function *D* → *P*(*D*) such that for any other continuous semilattice *L* and continuous function *D* → *L*, there is a unique continuous semilattice homomorphism *P*(*D*) → *L* making the evident diagram commute.

Other powerdomains are defined abstractly in a similar manner.

## Explicit descriptions of power domains

Let *D* be a domain. The lower power domain can be defined by

- *P*[*D*] = {closure[*A*] | Ø ∈ *A* ⊆ *D*} where

closure

[

A

] = {

d

∈

D

| ∃

X

⊆

D

,

X

directed

,

d

=

$\vee$

X

,

and

∀

x

∈

X

∃

a

∈

A

x

≤

a

}.

In other words, *P*[*D*] is the collection of downward-closed subsets of *D* that are also closed under existing least upper bounds of directed sets in *D*. Note that while the ordering on *P*[*D*] is given by the subset relation, least upper bounds do not in general coincide with unions.

It is important to check which properties of domains are preserved by the power domain constructions. For example, the Hoare powerdomain of an ω-complete domain is again ω-complete.

## Power domains for concurrency and Actors

### Clinger's power domain

Clinger [1981] constructed a power domain for the actor model building on the base domain of Actor event diagrams, which is incomplete. See Clinger's model.

### Timed diagrams power domain

Hewitt [2006] constructed a power domain for the actor model (which is technically simpler and easier to understand than Clinger's model) building on a base domain of timed Actor event diagrams, which is complete. The idea is to attach an arrival time for each message received by an Actor. See Timed Diagrams Model.

## Connections with topology and the Vietoris space

Domains can be understood as topological spaces, and, in this setting, the power domain constructions can be connected with the *space of subsets* construction introduced by Leopold Vietoris. See, for instance, [Smyth 1983].

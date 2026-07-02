---
title: "Newman's lemma"
source: https://en.wikipedia.org/wiki/Diamond_lemma
domain: confluence-rewriting
license: CC-BY-SA-4.0
tags: confluence property, Church-Rosser theorem, local confluence, Newman's lemma
fetched: 2026-07-02
---

# Newman's lemma

(Redirected from

Diamond lemma

)

In theoretical computer science, specifically in term rewriting, **Newman's lemma**, also commonly called the **diamond lemma**, is a criterion to prove that an abstract rewriting system is confluent. It states that local confluence is a sufficient condition for confluence, provided that the system is also terminating. This is useful since local confluence is usually easier to verify than confluence.

The lemma was originally proved by Max Newman in 1942. A considerably simpler proof (given below) was proposed by Gérard Huet. A number of other proofs exist.

## Statement and proof

The lemma is purely combinatorial and applies to any relation. Owing to the context where it is commonly applied, it is stated below in the terminology of abstract rewriting systems (this is simply a set whose elements are called terms, equipped with a relation $\to$ called reduction, and see the corresponding article for definitions of termination, confluence, local confluence and normal forms).

**Newman's lemma** ()—If an abstract rewriting system is terminating and locally confluent, then it is confluent, and every term has a *unique* normal form.

Proof

Because $\to$ is terminating, we can perform well-founded induction on u along $\to$ . We prove that every diagram

can be extended to a diagram

where the dotted arrows represent sequences of arbitrarily many reductions by $\to$ .

Base case: If $u=v$ or $u=w$ , this is trivial.

Inductive step: Otherwise, we have at least one reduction on each side:

By local confluence, this diagram can be extended to:

then by induction hypothesis on $v_{0}$ :

and finally, by induction hypothesis on $w_{0}$ :

## Eriksson's polygon property lemma

A related result was shown by Kimmo Eriksson in 1993. Recall that an abstract rewriting system is locally confluent if for any two reductions $a\to b$ and $a\to c$ , there exists d such that $b\to ^{*}d$ and $c\to ^{*}d$ . If additionally it is required that the reduction chains $b\to ^{*}d$ and $c\to ^{*}d$ have the same length, then the system is said to have the **polygon property**. Examples of rewriting systems with the polygon property include bubble sort and the chip-firing game.

**Eriksson's polygon property lemma** ()—If an abstract rewriting system is terminating and has the polygon property, then it is confluent, *and* every terminating chain of reductions from a given state has the same length.

Proof

By Newman's lemma, the system is confluent, and every element has a unique normal form. For each element u , define $rl(u)$ be the length of the *shortest* reduction chain from u to its normal form.

Induct on $rl(u)$ . If $rl(u)=0$ , then u is already in normal form. Otherwise, $rl(u)\geq 1$ , and we apply the polygonal property and the induction hypothesis.

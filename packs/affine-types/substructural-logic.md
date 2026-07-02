---
title: "Substructural logic"
source: https://en.wikipedia.org/wiki/Substructural_logic
domain: affine-types
license: CC-BY-SA-4.0
tags: affine type system, affine logic, move semantics, borrow checker
fetched: 2026-07-02
---

# Substructural logic

In logic, a **substructural logic** is a logic lacking one of the usual structural rules (e.g. of classical and intuitionistic logic), such as weakening, contraction, exchange or associativity. Two of the more significant substructural logics are relevance logic and linear logic.

## Examples

In a sequent calculus, one writes each line of a proof as

$\Gamma \vdash \Sigma$

.

Here the structural rules are rules for rewriting the LHS of the sequent, denoted Γ, initially conceived of as a finite string (sequence) of propositions. The standard interpretation of this string is as conjunction: we expect to read

${\mathcal {A}},{\mathcal {B}}\vdash {\mathcal {C}}$

as the sequent notation for

(

A

and

B

)

implies

C

.

Here we are taking the RHS Σ to be a single proposition *C* (which is the intuitionistic style of sequent); but everything applies equally to the general case, since all the manipulations are taking place to the left of the turnstile symbol $\vdash$ .

Since conjunction is a commutative and associative operation, the formal setting-up of sequent theory normally includes **structural rules** for rewriting the sequent Γ accordingly—for example for deducing

${\mathcal {B}},{\mathcal {A}}\vdash {\mathcal {C}}$

from

${\mathcal {A}},{\mathcal {B}}\vdash {\mathcal {C}}$

.

There are further structural rules corresponding to the *idempotent* and *monotonic* properties of conjunction: from

$\Gamma ,{\mathcal {A}},{\mathcal {A}},\Delta \vdash {\mathcal {C}}$

we can deduce

$\Gamma ,{\mathcal {A}},\Delta \vdash {\mathcal {C}}$

.

Also from

$\Gamma ,{\mathcal {A}},\Delta \vdash {\mathcal {C}}$

one can deduce, for any *B*,

$\Gamma ,{\mathcal {A}},{\mathcal {B}},\Delta \vdash {\mathcal {C}}$

.

Linear logic, in which duplicated hypotheses 'count' differently from single occurrences, leaves out both of these rules, while relevant (or relevance) logics merely leaves out the latter rule, on the ground that *B* is clearly irrelevant to the conclusion.

The above are basic examples of structural rules. It is not that these rules are contentious, when applied in conventional propositional calculus. They occur naturally in proof theory, and were first noticed there (before receiving a name).

## Premise composition

There are numerous ways to compose premises (and in the multiple-conclusion case, conclusions as well). One way is to collect them into a set. But since e.g. {a,a} = {a} we have contraction for free if premises are sets. We also have associativity and permutation (or commutativity) for free as well, among other properties. In substructural logics, typically premises are not composed into sets, but rather they are composed into more fine-grained structures, such as trees or multisets (sets that distinguish multiple occurrences of elements) or sequences of formulae. For example, in linear logic, since contraction fails, the premises must be composed in something at least as fine-grained as multisets.

## History

Substructural logic is a relatively young field. The first conference on the topic was held in October 1990 in Tübingen, as "Logics with Restricted Structural Rules". During the conference, Kosta Došen proposed the term "substructural logics", which is now in use today.

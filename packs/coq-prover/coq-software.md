---
title: "Rocq"
source: https://en.wikipedia.org/wiki/Coq_(software)
domain: coq-prover
license: CC-BY-SA-4.0
tags: coq proof assistant, coq prover, gallina coq, rocq prover
fetched: 2026-07-02
---

# Rocq

(Redirected from

Coq (software)

)

The **Rocq Prover** (formerly named **Coq**) is an interactive theorem prover first released in 1989. It allows the expression of mathematical assertions, mechanical checking of proofs of these assertions, assists in finding formal proofs using proof automation routines and extraction of a certified program from the constructive proof of its formal specification.

Rocq works within the theory of the calculus of inductive constructions, a derivative of the calculus of constructions. Rocq is not an automated theorem prover but includes automatic theorem proving tactics (procedures) and various decision procedures.

The Association for Computing Machinery awarded Thierry Coquand, Gérard Huet, Christine Paulin-Mohring, Bruno Barras, Jean-Christophe Filliâtre, Hugo Herbelin, Chetan Murthy, Yves Bertot, and Pierre Castéran with the 2013 ACM Software System Award for Rocq (when it was named Coq).

## Overview

When viewed as a programming language, Rocq implements a dependently typed functional programming model; when viewed as a logical system, it implements a higher-order type theory. The development of Rocq has been supported since 1984 by French Institute for Research in Computer Science and Automation (INRIA), in collaboration with many other French and international research institutions. The development of Rocq was initiated by Gérard Huet and Thierry Coquand, and more than 200 people, mainly researchers, have contributed features to the core system since its inception. The implementation team has successively been coordinated by Gérard Huet, Christine Paulin-Mohring, Hugo Herbelin, and Matthieu Sozeau. Rocq is mainly implemented in OCaml with a bit of C. The core system can be extended by way of a plug-in mechanism.

Rocq provides a specification language named Gallina. Programs written in Gallina have the weak normalization property, implying that they always terminate. This is a distinctive property of the language, since infinite loops (non-terminating programs) are common in other programming languages.

As an example of a proof written in Rocq, consider a proof of a lemma which states that taking the successor of a natural number flips its parity. The fold-unfold tactic introduced by Danvy is used to help keep the proof simple.

```mw
From Stdlib Require Import Arith Nat Bool.

Fixpoint is_even (n : nat) : bool :=
  match n with
  | 0 => true
  | S n' => negb (is_even n')
  end.

Lemma is_even_0 :
  is_even 0 = true.
Proof. reflexivity. Qed.

Lemma is_even_S n :
  is_even (S n) = negb (is_even n).
Proof. reflexivity. Qed.

Lemma successor_flips_evenness n :
  is_even n = negb (is_even (S n)).
Proof.
  rewrite is_even_S.
  destruct (is_even n).
  * simpl. reflexivity.
  * simpl. reflexivity.
Qed.
```

This proof firsts import the definition of booleans and natural numbers from the standard library, and then defines a `is_even` which is a function returning whether a number is even. Then, three lemmas are proven about this function. The first just restate the defining equations of `is_even`, and since Rocq knows the equations their proof is very short. The last lemma is proven with a case distinction after first applying the second lemma; the star `*` demarks that a new sub-case starts there.

## Notable uses

### Four color theorem and SSReflect extension

Georges Gonthier of Microsoft Research in Cambridge, England and Benjamin Werner of INRIA used Rocq to create a surveyable proof of the four color theorem, which was completed in 2002. Their work led to the development of the SSReflect ("Small Scale Reflection") package, which was a significant extension to Rocq. Despite its name, most of the features added to Rocq by SSReflect are general-purpose features and are not limited to the computational reflective programming style of proof. These features include:

- Added convenient notations for irrefutable and refutable pattern matching, on inductive types with one or two constructors
- Implicit arguments for functions applied to zero arguments, which is useful when programming with higher-order functions
- Concise anonymous arguments
- An improved `set` tactic with more powerful matching
- Support for reflection

SSReflect is distributed as part of the main Rocq distribution since Coq 8.7.

## Other applications

- CompCert: an optimizing compiler for almost all of the C programming language which is largely programmed and proven correct in Rocq.
- Disjoint-set data structure: correctness proof in Rocq was published in 2007.
- Feit–Thompson theorem: formal proof using Rocq was completed in September 2012.
- Busy beaver: The value of the 5-state winning busy beaver was discovered by Heiner Marxen and Jürgen Buntrock in 1989, but only proved to be the winning fifth busy beaver — stylized as **BB(5)** — in 2024 using a proof in Rocq.

## Tactic language

In addition to constructing Gallina terms explicitly, Rocq supports the use of *tactics* written in the built-in language Ltac or in OCaml. These tactics automate the construction of proofs, carrying out trivial or obvious steps in proofs. Several tactics implement decision procedures for various theories. For example, the "ring" tactic decides the theory of equality modulo ring or semiring axioms via associative-commutative rewriting. For example, the following proof establishes a complex equality in the ring of integers in just one line of proof:

```mw
Require Import ZArith.
Open Scope Z_scope.
Goal forall a b c:Z,
    (a + b + c) ^ 2 =
     a * a + b ^ 2 + c * c + 2 * a * b + 2 * a * c + 2 * b * c.
  intros; ring.
Qed.
```

Built-in decision procedures are also available for the empty theory ("congruence"), propositional logic ("tauto"), quantifier-free linear integer arithmetic ("lia"), and linear rational/real arithmetic ("lra"). Further decision procedures have been developed as libraries, including one for Kleene algebras and another for certain geometric goals.

## Name

The old name **Coq** means 'rooster' in French and is a wordplay on the name of Thierry Coquand, *calculus of constructions* or *CoC*, and stems from a French tradition of naming research development tools after animals. Until 1991, Coquand was implementing a language named the *calculus of constructions* and it was simply called *CoC* then. In 1991, a new implementation based on the extended *calculus of inductive constructions* was begun and the name changed from *CoC* to *Coq* in an indirect reference to Coquand, who developed the *calculus of constructions* along with Gérard Huet and contributed to the *calculus of inductive constructions* with Christine Paulin-Mohring. On October 11, 2023, the development team announced that *Coq* would be renamed *The Rocq Prover* in coming months, and began updating the code base, website, and related tools. The official renaming happened with the release of Rocq 9.0 in March 2025. The new name refers to Inria Rocquencourt, where the system was developed first, and is related to the mythical bird Roc, which allows keeping the bird references from the prior name.

## Awards

- 2022 Open Science Award for Open Source Research Software in the category "Scientific and Technical"

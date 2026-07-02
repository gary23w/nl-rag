---
title: "Identity type"
source: https://en.wikipedia.org/wiki/Identity_type
domain: homotopy-type-theory
license: CC-BY-SA-4.0
tags: homotopy type theory, intuitionistic type theory, univalent foundations, identity type
fetched: 2026-07-02
---

# Identity type

In type theory, a branch of mathematics, the **identity type** represents the concept of equality. It is also known as **propositional equality** to differentiate it from "judgemental equality". Equality in type theory is a complex topic and has been the subject of research, such as the field of homotopy type theory.

## Comparison with Judgemental Equality

The identity type is one of 2 different notions of equality in type theory. The more fundamental notion is "judgemental equality", which is a judgement.

## Beyond Judgemental Equality

The identity type can do more than what judgemental equality can do. It can be used to show "for all $x,x+1=1+x$ ", which is impossible to show with judgemental equality. This is accomplished by using the eliminator (or "recursor") of the natural numbers, known as "R".

The "R" function lets us define a new function on the natural numbers. That new function "P" is defined to be "(λ x:nat . x+1 = 1+x)". The other arguments act like the parts of an induction proof. The argument "PZ : P 0" becomes the base case "0+1 = 1+0", which is the term "refl nat 1". The argument "PS : P n → P (S n)" becomes the inductive case. Essentially, this says that when "x+1 = 1+x" has "x" replaced with a canonical value, the expression will be the same as "refl nat (x+1)".

## Versions of the Identity Type

The identity type is complex and is the subject of research in type theory. While every version agrees on the constructor, "refl". Their properties and eliminator functions differ dramatically.

For "extensional" versions, any identity type can be converted into a judgemental equality. A computational version is known as "Axiom K" due to Thomas Streicher. These are not very popular lately.

## Complexity of Identity Type

Martin Hofmann and Thomas Streicher refuted the idea that type theory required all terms of the identity type to be the same.

A popular branches of research into the identity type are homotopy type theory and its cubical type theory.

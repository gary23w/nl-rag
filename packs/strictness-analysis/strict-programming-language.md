---
title: "Strict programming language"
source: https://en.wikipedia.org/wiki/Strict_programming_language
domain: strictness-analysis
license: CC-BY-SA-4.0
tags: strictness analysis, demand analysis, backwards analysis, call-by-value transformation
fetched: 2026-07-02
---

# Strict programming language

A **strict programming language** is a programming language that only allows strict functions (functions whose parameters must be evaluated completely before they may be called) to be defined by the user. A **non-strict programming language** allows the user to define non-strict functions, and hence may allow lazy evaluation. In most non-strict languages, the non-strictness extends to data constructors.

## Description

A strict programming language is a programming language which employs a strict programming paradigm, allowing only strict functions (functions whose parameters must be evaluated completely before they may be called) to be defined by the user. A non-strict programming language allows the user to define non-strict functions, and hence may allow lazy evaluation.

Non-strictness has several disadvantages which have prevented widespread adoption:

- Because of the uncertainty regarding if and when expressions will be evaluated, non-strict languages generally must be purely functional to be useful.
- All hardware architectures in common use are optimized for strict languages, so the best compilers for non-strict languages produce slower code than the best compilers for strict languages.
- Space complexity of non-strict programs is difficult to understand and predict.
- In many strict languages, some advantages of non-strict functions can be obtained through the use of macros or thunks.

Strict programming languages are often associated with eager evaluation, and non-strict languages with lazy evaluation, but other evaluation strategies are possible in each case. The terms "eager programming language" and "lazy programming language" are often used as synonyms for "strict programming language" and "non-strict programming language" respectively.

## Examples

Nearly all programming languages in common use today are strict. Examples include C#, Java, Perl (all versions, i.e., through versions 5 and 7), Python, Ruby, Common Lisp, and ML. Some strict programming languages include features that mimic laziness. Raku (formerly named Perl 6) has lazy lists, Python has generating functions, and Julia provides a macro system to build non-strict functions, as does Scheme.

Examples for non-strict languages are Haskell, R, Miranda, and Clean.

## Extension

In most non-strict languages, the non-strictness extends to data constructors. This allows conceptually infinite data structures (such as the list of all prime numbers) to be manipulated in the same way as ordinary finite data structures. It also allows for the use of very large but finite data structures such as the complete game tree of chess.

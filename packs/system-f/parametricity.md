---
title: "Parametricity"
source: https://en.wikipedia.org/wiki/Parametricity
domain: system-f
license: CC-BY-SA-4.0
tags: System F, polymorphic lambda calculus, second-order lambda calculus, impredicative polymorphism
fetched: 2026-07-02
---

# Parametricity

In programming language theory, **parametricity** is an abstract uniformity property enjoyed by parametrically polymorphic functions, which captures the intuition that all instances of a polymorphic function act the same way.

## Idea

Consider this example, based on a set *X* and the type *T*(*X*) = [*X* → *X*] of functions from *X* to itself. The higher-order function *twice**X* : *T*(*X*) → *T*(*X*) given by *twice**X*(*f*) = *f* ∘ *f*, is intuitively independent of the set *X*. The family of all such functions *twice**X*, parametrized by sets *X*, is called a "parametrically polymorphic function". We simply write **twice** for the entire family of these functions and write its type as $\forall$ *X*. *T*(*X*) → *T*(*X*). The individual functions *twice**X* are called the *components* or *instances* of the polymorphic function. Notice that all the component functions *twice**X* act "the same way" because they are given by the same rule. Other families of functions obtained by picking one arbitrary function from each *T*(*X*) → *T*(*X*) would not have such uniformity. They are called "*ad hoc* polymorphic functions". *Parametricity* is the abstract property enjoyed by the uniformly acting families such as **twice**, which distinguishes them from *ad hoc* families. With an adequate formalization of parametricity, it is possible to prove that the parametrically polymorphic functions of type $\forall$ *X*. *T*(*X*) → *T*(*X*) are one-to-one with natural numbers. The function corresponding to the natural number *n* is given by the rule *f* $\mapsto$ *f**n*, i.e., the polymorphic Church numeral for *n*. In contrast, the collection of all *ad hoc* families would be too large to be a set.

## History

The *parametricity theorem* was originally stated by John C. Reynolds, who called it the *abstraction theorem*. In his paper "Theorems for free!", Philip Wadler described an application of parametricity to derive theorems about parametrically polymorphic functions based on their types.

## Programming language implementation

Parametricity is the basis for many program transformations implemented in compilers for the programming language Haskell. These transformations were traditionally thought to be correct in Haskell because of Haskell's non-strict semantics. Despite being a lazy evaluation programming language, Haskell does support certain primitive operations, such as the operator `seq`—that enable so-called *selective strictness*, allowing evaluation to be forced for certain expressions. In their paper "Free theorems in the presence of *seq*", Patricia Johann and Janis Voigtlaender showed that because of the presence of these operations, the general parametricity theorem does not hold for Haskell programs; thus, these transformations are unsound in general.

## Dependent types

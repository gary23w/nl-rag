---
title: "Typed lambda calculus"
source: https://en.wikipedia.org/wiki/Typed_lambda_calculus
domain: lambda-cube
license: CC-BY-SA-4.0
tags: lambda cube, pure type system, calculus of constructions, higher-order logic
fetched: 2026-07-02
---

# Typed lambda calculus

In mathematics and computer science, a **typed lambda calculus** is a typed formalism that uses the lambda symbol ( $\lambda$ ) to denote anonymous function abstraction. In this context, types are usually objects of a syntactic nature that are assigned to lambda terms; the exact nature of a type depends on the calculus considered (see kinds below). From a certain point of view, typed lambda calculi can be seen as refinements of the untyped lambda calculus, but from another point of view, they can also be considered the more fundamental theory and *untyped lambda calculus* a special case with only one type.

Typed lambda calculi are foundational programming languages and are the base of typed functional programming languages such as ML and Haskell and, more indirectly, typed imperative programming languages. Typed lambda calculi play an important role in the design of type systems for programming languages; here, typability usually captures desirable properties of the program (e.g., the program will not cause a memory access violation).

Typed lambda calculi are closely related to mathematical logic and proof theory via the Curry–Howard isomorphism and they can be considered as the internal language of certain classes of categories. For example, the simply typed lambda calculus is the language of Cartesian closed categories (CCCs).

## Kinds of typed lambda calculi

Various typed lambda calculi have been studied. The simply typed lambda calculus has only one type constructor, the arrow $\to$ , and its only types are basic types and function types $\sigma \to \tau$ . System T extends the simply typed lambda calculus with a type of natural numbers and higher-order primitive recursion; in this system all functions provably computable in Peano arithmetic are definable. System F allows polymorphism by using universal quantification over all types; from a logical perspective it can describe all functions that are provably total in second-order logic. Lambda calculi with dependent types are the base of intuitionistic type theory, the calculus of constructions and the logical framework (LF), a pure lambda calculus with dependent types. Based on work by Berardi on pure type systems, Henk Barendregt proposed the lambda cube to systematize the relations of pure typed lambda calculi (including simply typed lambda calculus, System F, LF and the calculus of constructions).

Some typed lambda calculi introduce a notion of *subtyping*, i.e. if A is a subtype of B , then all terms of type A also have type B . Typed lambda calculi with subtyping are the simply typed lambda calculus with conjunctive types and System F<:.

All the systems mentioned so far, with the exception of the untyped lambda calculus, are *strongly normalizing*: all computations terminate. Therefore, they cannot describe all Turing-computable functions. As another consequence they are consistent as a logic, i.e. there are uninhabited types. There exist, however, typed lambda calculi that are not strongly normalizing. For example the dependently typed lambda calculus with a type of all types (Type : Type) is not normalizing due to Girard's paradox. This system is also the simplest pure type system, a formalism which generalizes the lambda cube. Systems with explicit recursion combinators, such as Plotkin's "Programming language for Computable Functions" (PCF), are not normalizing, but they are not intended to be interpreted as a logic. Indeed, PCF is a prototypical, typed functional programming language, where types are used to ensure that programs are well-behaved but not necessarily that they are terminating.

## Applications to programming languages

In computer programming, the routines (functions, procedures, methods) of strongly typed programming languages closely correspond to typed lambda expressions.

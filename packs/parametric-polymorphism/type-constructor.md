---
title: "Type constructor"
source: https://en.wikipedia.org/wiki/Type_constructor
domain: parametric-polymorphism
license: CC-BY-SA-4.0
tags: parametric polymorphism, type parameter, generic programming, type constructor
fetched: 2026-07-02
---

# Type constructor

In the area of mathematical logic and computer science known as type theory, a **type constructor** is a feature of a typed formal language that builds new types from old ones. Basic types are considered to be built using nullary type constructors. Some type constructors take another type as an argument, e.g., the constructors for product types, function types, power types and list types. New types can be defined by recursively composing type constructors.

For example, simply typed lambda calculus can be seen as a language with a single non-basic type constructor—the function type constructor. Product types can generally be considered "built-in" in typed lambda calculi via currying.

Abstractly, a type constructor is an *n*-ary **type operator** taking as argument zero or more types, and returning another type. Making use of currying, *n*-ary type operators can be (re)written as a sequence of applications of unary type operators. Therefore, we can view the type operators as a simply typed lambda calculus, which has only one basic type, usually denoted * , and pronounced "type", which is the type of all types in the underlying language, which are now called *proper types* in order to distinguish them from the types of the type operators in their own calculus, which are called *kinds*.

Type operators may bind type variables. For example, giving the structure of the simply-typed λ-calculus at the type level requires binding, or higher-order, type operators. These binding type operators correspond to the 2nd axis of the λ-cube, and type theories such as the simply-typed λ-calculus with type operators, λω. Combining type operators with the polymorphic λ-calculus (System F) yields System Fω.

Some functional programming languages make explicit use of type constructors. A notable example is Haskell, in which all `data` type declarations are considered to declare type constructors, and basic types (or nullary type constructors) are called type constants. Type constructors may also be considered as parametric polymorphic data types.

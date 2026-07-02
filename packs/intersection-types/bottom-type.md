---
title: "Bottom type"
source: https://en.wikipedia.org/wiki/Bottom_type
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Bottom type

In type theory, a theory within mathematical logic, the **bottom type** of a type system is the type that is a subtype of all other types.

Where such a type exists, it is often represented with the up tack (⊥) symbol.

## Relation with the empty type

When the bottom type is uninhabited, a function whose return type is bottom cannot return any value, not even the lone value of a unit type. In such a language, the bottom type may therefore be known as the **zero**, **never** or empty type which, in the Curry–Howard correspondence, corresponds to falsity.

However, when the bottom type is inhabited, it is then different from the empty type.

If a type system is sound, the bottom type is uninhabited and a term of bottom type represents a logical contradiction. In such systems, typically no distinction is drawn between the bottom type and the empty type, and the terms may be used interchangeably.

## Computer science applications

In subtyping systems, the bottom type is a subtype of all types. It is dual to the top type, which spans all possible values in a system.

If the bottom type is inhabited, its term(s) typically correspond to error conditions such as undefined behavior, infinite recursion, or unrecoverable errors.

In *Bounded Quantification with Bottom*, Pierce says that "Bot" has many uses:

1. In a language with exceptions, a natural type for the raise construct is *raise ∈ exception -> Bot*, and similarly for other control structures. Intuitively, Bot here is the type of computations that do not return an answer.
2. Bot is useful in typing the "leaf nodes" of polymorphic data structures. For example, List(Bot) is a good type for nil.
3. Bot is a natural type for the "null pointer" value (a pointer which does not point to any object) of languages like Java: in Java, the *null type* is the universal subtype of reference types. `null` is the only value of the null type; and it can be cast to any reference type. However, the null type is not a bottom type as described above, it is not a subtype of `int` and other primitive types.
4. A type system including both Top and Bot seems to be a natural target for type inference, allowing the constraints on an omitted type parameter to be captured by a pair of bounds: we write S<:X<:T to mean "the value of X must lie somewhere between S and T." In such a scheme, a completely unconstrained parameter is bounded below by Bot and above by Top.

## In programming languages

Most commonly used languages don't have a way to denote the bottom type. There are a few notable exceptions.

- In Haskell, the bottom type is called `Void`.
- In Common Lisp the type `NIL`, contains no values and is a subtype of every type. The type named `NIL` is sometimes confused with the type named `NULL`, which has one value, namely the symbol `NIL` itself.
- In Scala, the bottom type is denoted as `Nothing`. Besides its use for functions that just throw exceptions or otherwise don't return normally, it's also used for covariant parameterized types. For example, Scala's List is a covariant type constructor, so `List[Nothing]` is a subtype of `List[A]` for all types A. So Scala's `Nil`, the object for marking the end of a list of any type, belongs to the type `List[Nothing]`.
- In Rust, the bottom type is called the never type and is denoted by `!`. It is present in the type signature of functions guaranteed to never return, for example by calling `panic!()` or looping forever. It is also the type of certain control-flow keywords, such as `break` and `return`, which do not produce a value but are nonetheless usable as expressions.
- In C and C++, there is no bottom type, but a function which does not return is annotated with `[[noreturn]]`, on a function that returns `void`.
- In Ceylon, the bottom type is `Nothing`. It is comparable to `Nothing` in Scala and represents the intersection of all other types as well as an empty set.
- In Julia, the bottom type is `Union{}`.
- In TypeScript, the bottom type is `never`.
- In JavaScript with Closure Compiler annotations, the bottom type is `!Null` (literally, a non-null member of the `Null` unit type).
- In PHP, the bottom type is `never`.
- In Python's optional static type annotations, the general bottom type is `typing.Never` (introduced in version 3.11), while `typing.NoReturn` (introduced in version 3.5) can be used as the return type of non-returning functions specifically (and doubled as the general bottom type prior to the introduction of `Never`).
- In Kotlin, the bottom type is `Nothing`.
- In D, the bottom type is `noreturn`.
- In Dart, since version 2.12 with the sound null safety update, the `Never` type was introduced as the bottom type. Before that, the bottom type used to be `Null`.

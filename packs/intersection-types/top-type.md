---
title: "Any type"
source: https://en.wikipedia.org/wiki/Top_type
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Any type

(Redirected from

Top type

)

In type theory and computer science, type systems include a ***top*, *universal*,** or ***any* type** (often represented with the down tack (**⊤**) symbol), which includes all other types as subtypes. The top type is sometimes called also ***universal* type**, or **universal supertype** as all other types in the type system of interest are subtypes of it. In object-oriented languages, it is often called **Object**, as it represents all possible objects.

The top type contrasts with the bottom type, or the *universal subtype*, which every other type is the supertype of. The bottom type is a type that contains no subtypes at all.

## Support in programming languages

Several typed programming languages provide explicit support for the top type.

In statically-typed languages, there are two different, often confused, concepts when discussing the top type.

1. A *universal base class* or other item at the top of a runtime *class hierarchy* (often relevant in object-oriented programming) or *type hierarchy*; it is often possible to create objects with this (runtime) type, or it could be found when one examines the type hierarchy programmatically, in languages that support it
2. A (compile time) *static type* in the code whose variables can be assigned any value (or a subset thereof, like any object pointer value), similar to dynamic typing

The first concept often implies the second, i.e., if a universal base class exists, then a variable that can point to an object of this class can also point to an object of any class. However, several languages have types in the second regard above (e.g., `void*` in C, `id` in Objective-C, `interface {}` in Go), static types which variables can accept any object value, but which do not reflect real runtime types that an object can have in the type system, so are not top types in the first regard.

In dynamically-typed languages, the second concept does not exist (any value can be assigned to any variable anyway), so only the first (class hierarchy) is discussed. This article tries to stay with the first concept when discussing top types, but also mention the second concept in languages where it is significant.

| Name | Languages |
|---|---|
| `Object` | Smalltalk, JavaScript and some others. |
| `java.lang.Object` | Java. Often written without the package prefix, as `Object` (because `java.lang` is implicitly imported). Also, it is *not* a supertype of the primitive types; however, since Java 1.5, autoboxing allows implicit or explicit type conversion of a primitive value to `Object`, e.g., `((Object)42).toString()` |
| `System.Object` | C#, Visual Basic (.NET), and other .NET framework languages |
| `std::any` | C++ since C++17 |
| `object.Object` | D |
| `std::any::Any` | Rust |
| `object` | Python since unifying `type` and `class` in version 2.2 (new-style objects only; old-style objects in 2.x lack this as a base class). A new typing module introduces type `Any` which is compatible with any type and vice versa |
| `TObject` | Object Pascal |
| `t` | Lisp, many dialects such as Common Lisp |
| `kotlin.Any?` | Kotlin |
| `scala.Any` | Scala, Swift, Julia, Python |
| `ANY` | Eiffel |
| `UNIVERSAL` | Perl 5 |
| `Variant` | Visual Basic up to version 6, D |
| `interface{}` or `any` | Go |
| `BasicObject` | Ruby |
| `any` and `unknown` | TypeScript (with `unknown` having been introduced in version 3.0) |
| `mixed` | PHP (as of version 8.0) |

The following object-oriented languages have no universal base class:

- C++ and Rust have no universal class like `Object`.
- Objective-C. It is possible to create a new base class by not specifying a parent class for a class, although this is highly unusual. `Object` is conventionally used as the base class in the original Objective-C runtimes. In the OpenStep and Cocoa Objective-C libraries, `NSObject` is conventionally the universal base class. The top type for pointers to objects is `id`.
- Swift. It is possible to create a new base class by not specifying a parent class for a class. The protocol `Any` can accept any type.

### Other languages

Languages that are not object-oriented usually have no universal supertype, or subtype polymorphism support.

While Haskell purposefully lacks subtyping, it has several other forms of polymorphism including parametric polymorphism. The most generic type class parameter is an unconstrained parameter `a` (without a type class constraint). In Rust, `<T: ?Sized>` is the most generic parameter (`<T>` is not, as it implies the `Sized` trait by default).

`std::any` (in C++) and `std::any::Any` (in Rust) are not actually top types in the type-system, but rather type-erased containers, from which the data is obtained through downcasting (or *type refinement*).

`std.variant.Variant` in D behaves like an any type, but rather than being a root of an inheritance tree, it is a tagged union of all types.

The top type is used as a *generic* type, more so in languages without parametric polymorphism. For example, before the introduction of generics to Java in Java 5, collection classes in the Java standard library (excluding Java arrays) held references of type `java.lang.Object`. In this way, any non-intrinsic type could be inserted into a collection. The top type is also often used to hold objects of unknown type. Java supports "wildcard type parameters", represented by `?`. For instance, `List<?>` denotes a list that can hold any type (but not null). Wildcards can be bounded, `List<? extends T>` and `List<? super T>` denote a list that can hold any type that inherits from/is an ancestor class of (respectively) type `T` (including `T` itself). Wildcards however cannot simultaneously have both upper and lower bounds.

The top type may also be seen as the implied type of non-statically typed languages. Languages with runtime typing often provide downcasting to allow discovering a more specific type for an object at runtime.

In C and C++, the *void pointer* type (`void*`) can accept any non-function pointer, even though the void type is not the universal type but the unit type. In C++, downcasting from `void*` cannot be done in a *safe* way, where failed downcasts are detected by the language runtime.

In languages with a structural type system, the empty structure serves as a top type. For example, objects in OCaml are structurally typed; the empty object type (the type of objects with no methods), `< >`, is the top type of object types. Any OCaml object can be explicitly upcasted to this type, although the result would be of no use. Go also uses structural typing; and all types implement the empty interface: `interface {}`, which has no methods, but may still be downcast back to a more specific type.

In Kotlin, the top type is `kotlin.Any?`, a nullable form of `kotlin.Any` (the top type that disallows `null`). Although `kotlin.Any` maps to `java.lang.Object` in the JVM, Kotlin enforces nullability while Java does not.

## In logic

The notion of *top* is also found in propositional calculus, linking to a formula which is true in every possible interpretation. It has a similar meaning in predicate calculus. In description logic, top is used to refer to the set of all concepts. This is intuitively like the use of the top type in programming languages. For example, in the Web Ontology Language (OWL), which supports several description logics, top corresponds to the class `owl:Thing`, where all classes are subclasses of `owl:Thing`. (the bottom type or empty set corresponds to `owl:Nothing`).

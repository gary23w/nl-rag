---
title: "Type class"
source: https://en.wikipedia.org/wiki/Type_class
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Type class

In computer science, a **type class** is a type system construct that supports ad hoc polymorphism in a programming language. This is achieved by adding constraints to type variables in parametrically polymorphic types. Such a constraint typically involves a type class `T` and a type variable `a`, and means that `a` can only be instantiated to a type whose members support the overloaded operations associated with `T`.

Type classes were first implemented in the language Haskell after first being proposed by Philip Wadler and Stephen Blott as an extension to `eqtypes` in Standard ML, and were originally conceived as a way of implementing overloaded arithmetic and equality operators in a principled fashion. In contrast with the "eqtypes" of Standard ML, overloading the equality operator through the use of type classes in Haskell does not need extensive modification of the compiler frontend or the underlying type system.

## Overview

Type classes are defined by specifying a set of function or constant names, together with their respective types, that must exist for every type that belongs to the class. In Haskell, types can be parameterized; a type class `Eq` intended to contain types that admit equality would be declared in the following way:

```mw
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
```

where `a` is one instance of the type class `Eq`, and `a` defines the function signatures for 2 functions (the equality and inequality functions), which each take 2 arguments of type `a` and return a Boolean.

The type variable `a` has kind * ( * is also known as `Type` in the latest Glasgow Haskell Compiler (GHC) release), meaning that the kind of `Eq` is

```mw
Eq :: Type -> Constraint
```

The declaration may be read as stating a "type `a` belongs to type class `Eq` if there are functions named `(==)`, and `(/=)`, of the appropriate types, defined on it". A programmer could then define a function `elem` (which determines if an element is in a list) in the following way:

```mw
elem :: Eq a => a -> [a] -> Bool
elem y []     = False
elem y (x:xs) = (x == y) || elem y xs
```

The function `elem` has the type `a -> [a] -> Bool` with the context `Eq a`, which constrains the types which `a` can range over to those `a` which belong to the `Eq` type class. (Haskell `=>` can be called a 'class constraint'.)

Any type `t` can be made a member of a given type class `C` by using an *instance declaration* that defines implementations of all of `C`'s methods for the given type `t`. For example, if a new data type `t` is defined, this new type can be made an instance of `Eq` by providing an equality function over values of type `t` in any way that is useful. Once this is done, the function `elem` can be used on `[t]`, that is, lists of elements of type `t`.

Type classes are different from classes in object-oriented programming languages. Specifically, `Eq` is not a type: there is no such thing as a *value* of type `Eq`.

Type classes are closely related to parametric polymorphism. For example, the type of `elem` as specified above would be the parametrically polymorphic type `a -> [a] -> Bool` were it not for the type class constraint "`Eq a =>`".

## Higher-kinded polymorphism

A type class need not take a type variable of kind `Type` but can take one of any kind. These type classes with higher kinds are sometimes called constructor classes (the constructors referred to are type constructors such as `Maybe`, rather than data constructors such as `Just`). An example is the `Monad` class:

```mw
class Monad m where
  return :: a -> m a
  (>>=)  :: m a -> (a -> m b) -> m b
```

That `m` is applied to a type variable indicates that it has kind `Type -> Type`, i.e., it takes a type and returns a type, the kind of `Monad` is thus:

```mw
Monad :: (Type -> Type) -> Constraint
```

## Multi-parameter type classes

Type classes permit multiple type parameters, and so type classes can be seen as relations on types. For example, in the GHC standard library, the class `IArray` expresses a general immutable array interface. In this class, the type class constraint `IArray a e` means that `a` is an array type that contains elements of type `e`. (This restriction on polymorphism is used to implement unboxed array types, for example.)

Like multimethods, multi-parameter type classes support calling different implementations of a method depending on the types of multiple arguments, and indeed return types. Multi-parameter type classes do not require searching for the method to call on every call at runtime; rather the method to call is first compiled and stored in the dictionary of the type class instance, just as with single-parameter type classes.

Haskell code that uses multi-parameter type classes is not portable as of the Haskell 98 standard, which is not the newest standard. The popular Haskell implementations, GHC and Hugs, support multi-parameter type classes.

## Functional dependencies

In Haskell, type classes have been refined to allow the programmer to declare functional dependencies between type parameters—a concept inspired from relational database theory. That is, the programmer can assert that a given assignment of some subset of the type parameters uniquely determines the remaining type parameters. For example, a general monad `m` which carries a state parameter of type `s` satisfies the type class constraint `Monad.State s m`. In this constraint, there is a functional dependency `m -> s`. This means that for a given monad `m` of type class `Monad.State`, the state type accessible from `m` is uniquely determined. This aids the compiler in type inference, as well as aiding the programmer in type-directed programming.

Simon Peyton Jones has objected to the introduction of functional dependencies in Haskell on grounds of complexity.

## Type classes and implicit parameters

Type classes and implicit parameters are very similar in nature, although not quite the same. A polymorphic function with a type class constraint such as:

```mw
sum :: Num a => [a] -> a
```

can be intuitively treated as a function that implicitly accepts an instance of `Num`:

```mw
sum_ :: Num_ a -> [a] -> a
```

The instance `Num_ a` is essentially a record that contains the instance definition of `Num a`. (This is in fact how type classes are implemented under the hood by the Glasgow Haskell Compiler.)

However, there is a crucial difference: implicit parameters are more *flexible*; different instances of `Num Int` can be passed. In contrast, type classes enforce the so-called *coherence* property, which requires that there should only be one unique choice of instance for any given type. The coherence property makes type classes somewhat antimodular, which is why orphan instances (instances that are defined in a module that neither contains the class nor the type of interest) are strongly discouraged. However, coherence adds another level of safety to a language, providing a guarantee that two disjoint parts of the same code will share the same instance.

As an example, an ordered set (of type `Set a`) requires a total ordering on the elements (of type `a`) to function. This can be evidenced by a constraint `Ord a`, which defines a comparison operator on the elements. However, there can be numerous ways to impose a total order. Since set algorithms are generally intolerant of changes in the ordering once a set has been constructed, passing an incompatible instance of `Ord a` to functions that operate on the set may lead to incorrect results (or crashes). Thus, enforcing coherence of `Ord a` in this particular scenario is crucial.

Instances (or "dictionaries") in Scala type classes are just ordinary values in the language, rather than a completely separate kind of entity. While these instances are by default supplied by finding appropriate instances in scope to be used as the implicit parameters for explicitly-declared implicit formal parameters, that they are ordinary values means that they can be supplied explicitly, to resolve ambiguity. As a result, Scala type classes do not satisfy the coherence property and are effectively a syntactic sugar for implicit parameters.

This is an example taken from the Cats documentation:

```mw
// A type class to provide textual representation
trait Show[A] {
  def show(f: A): String
}

// A polymorphic function that works only when there is an implicit 
// instance of Show[A] available
def log[A](a: A)(implicit s: Show[A]) = println(s.show(a))

// An instance for String
implicit val stringShow = new Show[String] {
  def show(s: String) = s
}

// The parameter stringShow was inserted by the compiler.
scala> log("a string")
a string
```

Rocq (formerly named *Coq*), version 8.2 onward, also supports type classes by inferring the appropriate instances. Recent versions of Agda 2 also provide a similar feature, called "instance arguments".

## Other approaches to operator overloading

In Standard ML, the mechanism of "equality types" corresponds roughly to Haskell's built-in type class `Eq`, but all equality operators are derived automatically by the compiler. The programmer's control of the process is limited to designating which type components in a structure are equality types and which type variables in a polymorphic type range over equality types.

SML's and OCaml's modules and functors can play a role similar to that of Haskell's type classes, the principal difference being the role of type inference, which makes type classes suitable for *ad hoc* polymorphism. The object oriented subset of OCaml is yet another approach which is somewhat comparable to the one of type classes.

An analogous notion for overloaded data (implemented in GHC) is that of type family.

In C++, notably C++20, has support for type classes using "concepts". As an illustration, the above mentioned Haskell example of typeclass `Eq` would be implemented as the following:

```mw
using std::convertible_to;

// equivalent to std::equality_comparable
template <typename T>
concept EqualityComparable = requires (T a, T b) {
    { a == b } -> convertible_to<bool>;
    { a != b } -> convertible_to<bool>;
};

// using concept EqualityComparable:
template <EqualityComparable T>
[[nodiscard]]
constexpr bool isEqual(const T& x, const T& y) noexcept {
    return x == y;
}
```

In Go, an interface can be seen as a type class, and is roughly equivalent to a C++ concept.

In Java and C#, interfaces are similar to type classes, defining an "interface" of methods to implement (see Java interfaces).

In Clean typeclasses are similar to Haskell, but have a slightly different syntax.

Rust supports traits, which are a limited form of type classes with coherence, and can also be seen as similar to interfaces.

Mercury has typeclasses, although they are not exactly the same as in Haskell.

In Scala, type classes are a programming idiom that can be implemented with existing language features such as implicit parameters, not a separate language feature per se. Because of the way they are implemented in Scala, it is possible to explicitly specify which type class instance to use for a type at a particular place in the code, in case of ambiguity. However, this is not necessarily a benefit as ambiguous type class instances can be error-prone.

The proof assistant Rocq has also supported type classes in recent versions. Unlike in ordinary programming languages, in Rocq, any laws of a type class (such as the monad laws) that are stated within the type class definition, must be mathematically proved of each type class instance before using them.

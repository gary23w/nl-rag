---
title: "Type variable"
source: https://en.wikipedia.org/wiki/Type_variable
domain: system-f
license: CC-BY-SA-4.0
tags: System F, polymorphic lambda calculus, second-order lambda calculus, impredicative polymorphism
fetched: 2026-07-02
---

# Type variable

In type theory and programming languages, a **type variable** is a mathematical variable ranging over types. Even in programming languages that allow mutable variables, a type variable remains an abstraction, in the sense that it does not correspond to some memory locations.

Programming languages that support parametric polymorphism make use of universally quantified type variables. Languages that support existential types make use of existentially quantified type variables. For example, the following OCaml code defines a polymorphic identity function that has a universally quantified type, which is printed by the interpreter on the second line:

```mw
# let id x = x;;
val id : 'a -> 'a = <fun>
```

In mathematical notation, the type of the function `id` is $\forall a.a\to a$ , where a is a type variable.

## Generic programming

In generic programming, a **type parameter** or **template parameter** is used to denote the type(s) that may be consumed. These type parameters are placeholders for types to be specified later, allowing for code to work with different types while remaining type-safe. Type parameters are typically written as a single capital letter.

```mw
interface List<E> {
    void add(E x);
    Iterator<E> iterator();
}

interface Map<K, V> {
    V put(K key, V value);
    V get(Object key);
}
```

In some languages, these can be specified to have default type parameters. For example, in C++:

```mw
template <typename T = int>
class Box {
private:
    T value;
public:
    explicit Box(T value):
        value{value} {}

    // ...
};

Box<double> b1(13.5);
Box<> b2(5); // This is Box<int>
```

Some languages additionally offer a form of constraining these type parameters, called type classes. C++ offers concepts and `requires` clauses, C#, Kotlin and Rust offer `where` clauses, while Java has `extends` and `super` qualifiers. Go interfaces also constrain a type such that it must implement certain methods.

```mw
using System;

public class MyGenericClass<T, U> 
    where T : IComparable<T>, allows ref struct
    where U : class, notnull, new()
{
    // ...
}
```

Additionally, Java offers wildcard type parameters to allow for variances of any parametrisations of a generic type. These are denoted `?`, for example `List<?>`. This exists in Kotlin as well, but denoted with `*` instead. In Rust, a generic type parameter can be left unspecified for the compiler to interpret using `_`, called an "inferred type" (for example `Vec<_>`).

In languages with dynamic typing, although type annotations may not be a core part of the language, some features may be provided to emulate them. For example, in Python, type variables can still be represented and specified using the class `typing.TypeVar`.

```mw
from typing import TypeVar

T: TypeVar = TypeVar('T')

def first_item(items: list[T]) -> T:
    return items[0]
```

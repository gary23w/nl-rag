---
title: "Type family"
source: https://en.wikipedia.org/wiki/Type_family
domain: parametric-polymorphism
license: CC-BY-SA-4.0
tags: parametric polymorphism, type parameter, generic programming, type constructor
fetched: 2026-07-02
---

# Type family

In computer science, a **type family** associates data types with other data types, using a type-level function defined by an open-ended collection of valid instances of input types and the corresponding output types.

Type families are a feature of some type systems that allow partial functions between types to be defined by pattern matching. This is in contrast to data type constructors, which define injective functions from all types of a particular kind to a new set of types, and type synonyms (a.k.a. typedef), which define functions from all types of a particular kind to another existing set of types using a single case.

Type families and type classes are closely related: normal type classes define partial functions from types to a collection of named *values* by pattern matching on the input types, while type families define partial functions from types to *types* by pattern matching on the input types. In fact, in many uses of type families there is a single type class which logically contains both values and types associated with each instance. A type family declared inside a type class is called an **associated type**.

Programming languages with support for type families or similar features include Haskell (with a common language extension), Standard ML (through its module system), Rust, Scala (under the name "abstract types"), and C++ (through use of typedefs in templates).

## Variations

The `TypeFamilies` extension in the Glasgow Haskell Compiler supports both *type synonym families* and *data families*. Type synonym families are the more flexible (but harder to type-check) form, permitting the types in the codomain of the type function to be any type whatsoever with the appropriate kind. Data families, on the other hand, restrict the codomain by requiring each instance to define a new type constructor for the function's result. This ensures that the function is injective, allowing clients' contexts to deconstruct the type family and obtain the original argument type.

## Motivation and examples

Type families are useful in abstracting patterns where a common "organization" or "structure" of types is repeated, but with different specific types in each case. Typical use cases include describing abstract data types like generic collections, or design patterns like model–view–controller.

### Self-optimizing abstract data types

One of the original motivations for the introduction of associated types was to allow abstract data types to be parameterized by their content type such that the data structure implementing the abstract type varies in a "self-optimizing" way. Normal algebraic data type parameters can only describe data structures that behave uniformly with respect to all argument types. Associated types, however, can describe a family of data structures that have a uniform interface but vary in implementation according to one or more type parameters. For example, using Haskell's associated types notation, we can declare a type class of valid array element types, with an associated data family representing an array of that element type:

```mw
class ArrayElem e where
    data Array e
    index :: Array e -> Int -> e
```

Instances can then be defined for this class, which define both the data structure used and the operations on the data structure in a single location. For efficiency, we might use a packed bit vector representation for arrays of Boolean values, while using a normal array data structure for integer values. The data structure for arrays of ordered pairs is defined recursively as a pair of arrays of each of the element types.

```mw
instance ArrayElem Bool where
    data Array Bool = BoolArray BitVector
    index (BoolArray ar) i = indexBitVector ar i
instance ArrayElem Int where
    data Array Int = IntArray UIntArr
    index (IntArray ar) i = indexUIntArr ar i
instance (ArrayElem a, ArrayElem b) => ArrayElem (a, b) where
    data Array (a, b) = PairArray (Array a) (Array b)
    index (PairArray ar br) = (index ar i, index br i)
```

With these definitions, when a client refers to an `Array (Int, Bool)`, an implementation is automatically selected using the defined instances.

### A class for collections

Inverting the previous example, we can also use type families to define a class for collection types, where the type function maps each collection type to its corresponding element type:

```mw
class Collects c where
    type Elem c
    empty :: c
    insert :: Elem c -> c -> c
    toList :: c -> [Elem c]
instance Collects [e] where
    type Elem [e] = e
    empty = []
    insert = (:)
    toList = id
instance Ord e => Collects (Set.Set e) where
    type Elem (Set.Set e) = e
    empty = Set.empty
    insert = Set.insert
    toList = Set.toList
```

In this example, the use of a type synonym family instead of a data family is essential, since multiple collection types may have the same element type.

## Comparison with functional dependencies

Functional dependencies are another type system feature that have similar uses to associated types. While an associated type adds a named type function mapping the enclosing type class's parameters to another type, a functional dependency lists the result type as another parameter of the type class and adds a constraint between the type parameters (e.g. "parameter *a* uniquely determines parameter *b*", written `a -> b`). The most common uses of functional dependencies can be directly converted to associated types and vice versa.

Type families are regarded as being generally easier to type-check than functional dependencies. Another advantage of associated types over functional dependencies is that the latter requires clients using the type class to state all of the dependent types in their contexts, including ones they do not use; since associated types do not require this, adding another associated type to the class requires updating only the class's instances, while clients can remain unchanged. The main advantages of functional dependencies over type families are in their added flexibility in handling a few unusual cases.

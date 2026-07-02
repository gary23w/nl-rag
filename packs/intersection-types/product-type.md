---
title: "Product type"
source: https://en.wikipedia.org/wiki/Product_type
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Product type

In programming languages and type theory, a **product** of *types* is another, compounded, type in a structure. The "operands" of the product are types, and the structure of a product type is determined by the fixed order of the operands in the product. An instance of a product type retains the fixed order, but otherwise may contain all possible instances of its primitive data types. The expression of an instance of a product type will be a tuple, and is called a "tuple type" of expression. A product of types is a direct product of two or more types.

If there are only two component types, it can be called a "pair type". For example, if two component types A and B are the set of all possible values of that type, the product type written $A\times B$ contains elements that are pairs $(a,b)$ , where a and b are instances of A and B respectively. The pair type is a special case of the dependent pair type, where the type B may depend on the instance picked from A .

In many languages, product types take the form of a record type, for which the components of a tuple can be accessed by label. In languages that have algebraic data types, as in most functional programming languages, algebraic data types with one constructor are isomorphic to a product type.

In the Curry–Howard correspondence, product types are associated with logical conjunction (AND) in logic.

The notion directly extends to the product of an arbitrary finite number of types (an n -ary product type), and in this case, it characterizes the expressions that behave as tuples of expressions of the corresponding types. A degenerate form of product type is the unit type: it is the product of no types.

In call-by-value programming languages, a product type can be interpreted as a set of pairs whose first component is a value in the first type and whose second component is a value in the second type. In short, it is a cartesian product and it corresponds to a product in the category of types.

Most functional programming languages have a primitive notion of product type. For instance, the product $T_{1}\times T_{2}\times ...\times T_{n}$ is written `T1 * T2 * ... * Tn` in ML and `(T1, T2, ..., Tn)` in Haskell. In both these languages, tuples are written `(v1, v2, ..., vn)` and the components of a tuple are extracted by pattern-matching. Additionally, many functional programming languages provide more general algebraic data types, which extend both product and sum types. Product types are the dual of sum types.

## Product types in programming languages

- C++ defines the class `std::tuple` (expressed `tuple<Ts...>` using variadic templates), and for the specific case of two elements defines `std::pair` (expressed `pair<T, U>`). `std::tuple` can be empty (`tuple<>`).
- C#/.NET Framework defines the class `System.Tuple`. There are specific instantiations for 1 to 8 elements. For the specific case of two elements (a pair), it uses `Tuple<T1, T2>`. In order to create a tuple with nine or more components, the final parameter `TRest` of `Tuple<T1, T2, T3, T4, T5, T6, T7, TRest>` is supplied as another tuple. For iterating over collections like dictionary types, the class `System.Collections.Generic.KeyValuePair` (expressed `KeyValuePair<TKey, TValue>`) is provided.
- Go does not have a tuple type, but can express multiple return values in a function as a sort of tuple.
- Haskell has a data type `Data.Tuple`.
- Java does not have a general tuple type, but JavaFX has a type `javafx.util.Pair` (expressed `Pair<K, V>`). For iterating over associative containers such as `java.util.Map`, a pair in the map is expressed as `Map.Entry<K, V>`.
- Kotlin does not have a general tuple type, but has classes `kotlin.Pair` (expressed `Pair<A, B>`) and `kotlin.Triple` (expressed `Triple<A, B, C>`).
- Python has a `tuple` collection which can be annotated as `typing.Tuple` (expressed `Tuple[T1, T2, ..., TN]`).
- Rust defines the primitive tuple type, expressed as `(T1, T2, ..., TN)`, and a pair is just `(T, U)`.
- Scala defines the class `scala.Tuple`, which supports between 2 and 22 objects as `scala.Tuple2` (expressed as `Tuple2[A, B]`) to `scala.Tuple22` (expressed as `Tuple22[A, B, ..., V]`).
- Swift expresses tuples as `(T1, T2, ..., TN)`.

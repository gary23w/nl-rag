---
title: "Intersection type"
source: https://en.wikipedia.org/wiki/Intersection_type
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Intersection type

In type theory, an **intersection type** can be allocated to values that can be assigned both the type $\sigma$ and the type $\tau$ . This value can be given the intersection type $\sigma \cap \tau$ in an intersection type system. Generally, if the ranges of values of two types overlap, then a value belonging to the *intersection* of the two ranges can be assigned the *intersection type* of these two types. Such a value can be safely passed as argument to functions expecting *either* of the two types. For example, in Java the class `Boolean` implements both the `Serializable` and the `Comparable` interfaces. Therefore, an object of type `Boolean` can be safely passed to functions expecting an argument of type `Serializable` and to functions expecting an argument of type `Comparable`.

Intersection types are composite data types. Similar to product types, they are used to assign several types to an object. However, product types are assigned to tuples, so that each tuple element is assigned a particular product type component. In comparison, underlying objects of intersection types are not necessarily composite. A restricted form of intersection types are refinement types.

Intersection types are useful for describing overloaded functions. For example, if `number => number` is the type of function taking a number as an argument and returning a number, and `string => string` is the type of function taking a string as an argument and returning a string, then the intersection of these two types can be used to describe (overloaded) functions that do one or the other, based on what type of input they are given.

Contemporary programming languages, including Ceylon, Flow, Java, Scala, TypeScript, and Whiley (see comparison of languages with intersection types), use intersection types to combine interface specifications and to express ad hoc polymorphism. Complementing parametric polymorphism, intersection types may be used to avoid class hierarchy pollution from cross-cutting concerns and reduce boilerplate code, as shown in the TypeScript example below.

The type theoretic study of intersection types is referred to as the intersection type discipline. Remarkably, program termination can be precisely characterized using intersection types. Consequently, type inference for infinite-intersection types is undecidable, but it is decidable for all finite rank intersection types.

## TypeScript example

TypeScript supports intersection types, improving expressiveness of the type system and reducing potential class hierarchy size, demonstrated as follows.

The following program code defines the classes `Chicken`, `Cow`, and `RandomNumberGenerator` that each have a method `produce` returning an object of either type `Egg`, `Milk`, or `number`. Additionally, the functions `eatEgg` and `drinkMilk` require arguments of type `Egg` and `Milk`, respectively.

```mw
class Egg {
    private kind: "Egg";
}

class Milk {
    private kind: "Milk";
}

// "Produces" a product
interface Producer<T> {
    produce(): T;
}

// produces eggs
class Chicken implements Producer<Egg> {
    produce(): Egg {
        return new Egg();
    }
}

// produces milk
class Cow implements Producer<Milk> {
    produce(): Milk {
        return new Milk();
    }
}

// produces a random number
class RandomNumberGenerator implements Producer<number> {
    produce(): number {
        return Math.random();
    }
}

// requires an egg
function eatEgg(egg: Egg): string {
    return "I ate an egg.";
}

// requires milk
function drinkMilk(milk: Milk): string {
    return "I drank some milk.";
}
```

The following program code defines the ad hoc polymorphic function `animalToFood` that invokes the member function `produce` of the given object `animal`. The function `animalToFood` has *two* type annotations, namely `((_: Chicken) => Egg)` and `((_: Cow) => Milk)`, connected via the intersection type constructor `&`. Specifically, `animalToFood` when applied to an argument of type `Chicken` returns an object of type `Egg`, and when applied to an argument of type `Cow` returns an object of type `Milk`. Ideally, `animalToFood` should not be applicable to any object having (possibly by chance) a `produce` method.

```mw
// given a chicken, produces an egg; given a cow, produces milk
const animalToFood: ((animal: Chicken) => Egg) & ((animal: Cow) => Milk) = (animal: any) => {
    return animal.produce();
};
```

Finally, the following program code demonstrates type safe use of the above definitions.

```mw
let chicken: Chicken = new Chicken();
let cow: Cow = new Cow();
let randomNumberGenerator: RandomNumberGenerator = new RandomNumberGenerator();

console.log(chicken.produce()); // Egg { }
console.log(cow.produce()); // Milk { }
console.log(randomNumberGenerator.produce()); // 0.2626353555444987

console.log(animalToFood(chicken)); // Egg { }
console.log(animalToFood(cow)); // Milk { }
// console.log(animalToFood(randomNumberGenerator)); // ERROR: Argument of type 'RandomNumberGenerator' is not assignable to parameter of type 'Cow'

console.log(eatEgg(animalToFood(chicken))); // I ate an egg.
// console.log(eatEgg(animalToFood(cow))); // ERROR: Argument of type 'Milk' is not assignable to parameter of type 'Egg'
console.log(drinkMilk(animalToFood(cow))); // I drank some milk.
// console.log(drinkMilk(animalToFood(chicken))); // ERROR: Argument of type 'Egg' is not assignable to parameter of type 'Milk'
```

The above program code has the following properties:

- Lines 1–3 create objects `chicken`, `cow`, and `randomNumberGenerator` of their respective type.
- Lines 5–7 print for the previously created objects the respective results (provided as comments) when invoking `produce`.
- Line 9 (resp. 10) demonstrates type safe use of the method `animalToFood` applied to `chicken` (resp. `cow`).
- Line 11, if uncommented, would result in a type error at compile time. Although the *implementation* of `animalToFood` could invoke the `produce` method of `randomNumberGenerator`, the *type annotation* of `animalToFood` disallows it. This is in accordance with the intended meaning of `animalToFood`.
- Line 13 (resp. 15) demonstrates that applying `animalToFood` to `chicken` (resp. `cow`) results in an object of type `Egg` (resp. `Milk`).
- Line 14 (resp. 16) demonstrates that applying `animalToFood` to `cow` (resp. `chicken`) does not result in an object of type `Egg` (resp. `Milk`). Therefore, if uncommented, line 14 (resp. 16) would result in a type error at compile time.

### Comparison to inheritance

The above minimalist example can be realized using inheritance, for instance by deriving the classes `Chicken` and `Cow` from a base class `Animal`. However, in a larger setting, this could be disadvantageous. Introducing new classes into a class hierarchy is not necessarily justified for cross-cutting concerns, or maybe outright impossible, for example when using an external library. Imaginably, the above example could be extended with the following classes:

- a class `Horse` that does not have a `produce` method;
- a class `Sheep` that has a `produce` method returning `Wool`;
- a class `Pig` that has a `produce` method, which can be used only once, returning `Meat`.

This may require additional classes (or interfaces) specifying whether a produce method is available, whether the produce method returns food, and whether the produce method can be used repeatedly. Overall, this may pollute the class hierarchy.

### Comparison to duck typing

The above minimalist example already shows that duck typing is less suited to realize the given scenario. While the class `RandomNumberGenerator` contains a `produce` method, the object `randomNumberGenerator` should not be a valid argument for `animalToFood`. The above example can be realized using duck typing, for instance by introducing a new field `argumentForAnimalToFood` to the classes `Chicken` and `Cow` signifying that objects of corresponding type are valid arguments for `animalToFood`. However, this would not only increase the size of the respective classes (especially with the introduction of more methods similar to `animalToFood`), but is also a non-local approach with respect to `animalToFood`.

### Comparison to function overloading

The above example can be realized using function overloading, for instance by implementing two methods `animalToFood(animal: Chicken): Egg` and `animalToFood(animal: Cow): Milk`. In TypeScript, such a solution is almost identical to the provided example. Other programming languages, such as Java, require distinct implementations of the overloaded method. This may lead to either code duplication or boilerplate code.

### Comparison to the visitor pattern

The above example can be realized using the visitor pattern. It would require each animal class to implement an `accept` method accepting an object implementing the interface `AnimalVisitor` (adding non-local boilerplate code). The function `animalToFood` would be realized as the `visit` method of an implementation of `AnimalVisitor`. Unfortunately, the connection between the input type (`Chicken` or `Cow`) and the result type (`Egg` or `Milk`) would be difficult to represent.

### Comparison with parametric polymorphism

Parametric polymorphism is conceptually equivalent to infinite intersection types.

Intersection types have been promoted as being "compositional" in contrast with the let-bound polymorphism of ML (a restricted form of parametric polymorphism) because intersection types have principal typings while ML's type system does not (not to be confused with principal types, which ML does enjoy). The lack of principal typings in ML translates into the need to evaluate some expressions before others in an ML program; essentially resulting in a data dependency at type-inference level in ML, in particular in `let` expressions. Consequently, intersection types have been proposed as a way to improve incremental compilation and/or gradual typing.

On the other hand, intersection types have been criticized for not being compositional in another sense, namely that in a putative system that uses only intersection types but has no parametric polymorphism, inferred types may depend on the local features of a module, which may compose badly with other modules unless whole program compilation happens at source level. As a trivial example, an identity function that is exposed through a public interface, e.g. exported by a module, ideally is parametrically polymorphic, so that it can be used with future types that the writer (of that function) doesn't yet know about. However, in a system that only has intersection types, such a function would be inferred to intersect at best over types existing when it is compiled.

### Limitations

On the one hand, intersection types *can* be used to locally annotate different types to a function without introducing new classes (or interfaces) to the class hierarchy. On the other hand, this approach *requires* all possible argument types and result types to be specified explicitly. If the behavior of a function can be specified precisely by either a unified interface, parametric polymorphism, or duck typing, then the verbose nature of intersection types is unfavorable. Therefore, intersection types should be considered complementary to existing specification methods.

## Dependent intersection type

A **dependent intersection type**, denoted $(x:\sigma )\cap \tau$ , is a dependent type in which the type $\tau$ may depend on the term variable x . In particular, if a term M has the dependent intersection type $(x:\sigma )\cap \tau$ , then the term M has *both* the type $\sigma$ and the type $\tau [x:=M]$ , where $\tau [x:=M]$ is the type which results from replacing all occurrences of the term variable x in $\tau$ by the term M .

### Scala example

Scala supports type declarations as object members. This allows a type of an object member to depend on the value of another member, which is called a *path-dependent type*. For example, the following program text defines a Scala trait `Witness`, which can be used to implement the singleton pattern.

```mw
trait Witness {
  type T
  val value: T {}
}
```

The above trait `Witness` declares the member `T`, which can be assigned a *type* as its value, and the member `value`, which can be assigned a value of type `T`. The following program text defines an object `booleanWitness` as instance of the above trait `Witness`. The object `booleanWitness` defines the type `T` as `Boolean` and the value `value` as `true`. For example, executing `System.out.println(booleanWitness.value)` prints `true` on the console.

```mw
object booleanWitness extends Witness {
  type T = Boolean
  val value = true
}
```

Let $\langle {\textsf {x}}:\sigma \rangle$ be the type (specifically, a record type) of objects having the member ${\textsf {x}}$ of type $\sigma$ . In the above example, the object `booleanWitness` can be assigned the dependent intersection type $(x:\langle {\textsf {T}}:{\text{Type}}\rangle )\cap \langle {\textsf {value}}:x.{\textsf {T}}\rangle$ . The reasoning is as follows. The object `booleanWitness` has the member `T` that is assigned the type `Boolean` as its value. Since `Boolean` is a type, the object `booleanWitness` has the type $\langle {\textsf {T}}:{\text{Type}}\rangle$ . Additionally, the object `booleanWitness` has the member `value` that is assigned the value `true` of type `Boolean`. Since the value of `booleanWitness.T` is `Boolean`, the object `booleanWitness` has the type $\langle {\textsf {value}}:{\textsf {booleanWitness.T}}\rangle$ . Overall, the object `booleanWitness` has the intersection type $\langle {\textsf {T}}:{\text{Type}}\rangle \cap \langle {\textsf {value}}:{\textsf {booleanWitness.T}}\rangle$ . Therefore, presenting self-reference as dependency, the object `booleanWitness` has the dependent intersection type $(x:\langle {\textsf {T}}:{\text{Type}}\rangle )\cap \langle {\textsf {value}}:x.{\textsf {T}}\rangle$ .

Alternatively, the above minimalistic example can be described using *dependent record types*. In comparison to dependent intersection types, dependent record types constitute a strictly more specialized type theoretic concept.

## Intersection of a type family

An **intersection of a type family**, denoted ${\textstyle \bigcap _{x:\sigma }\tau }$ , is a dependent type in which the type $\tau$ may depend on the term variable x . In particular, if a term M has the type ${\textstyle \bigcap _{x:\sigma }\tau }$ , then for *each* term N of type $\sigma$ , the term M has the type $\tau [x:=N]$ . This notion is also called *implicit Pi type*, observing that the argument N is not kept at term level.

## Comparison of languages with intersection types

| Language | Actively developed | Paradigm(s) | Status | Features |
|---|---|---|---|---|
| C# | Yes | Functional Imperative Object-oriented | Under discussion | Additionally, generic type parameters can have constraints that require their (monomorphized) type-arguments to implement multiple interfaces, whereupon the runtime type represented by the generic type parameter becomes an intersection-type of all listed interfaces. |
| Ceylon | No | Object-oriented | Supported | Type refinement Interface composition Subtyping in width |
| F# | Yes | Functional Imperative Object-oriented | Under discussion | ? |
| Flow | Yes | Functional Imperative Object-oriented Scripting | Supported | Type refinement Interface composition |
| Forsythe | No | Imperative | Supported | Function type intersection Distributive, co- and contravariant function type subtyping |
| Java | Yes | Imperative Object-oriented | Supported | Type refinement Interface composition Subtyping in width |
| PHP | Yes | Functional Imperative Object-oriented Scripting | Supported | Type refinement Interface composition |
| Scala | Yes | Functional Imperative Object-oriented | Supported | Type refinement Trait composition Subtyping in width |
| TypeScript | Yes | Functional Imperative Object-oriented Scripting | Supported | Arbitrary type intersection Interface composition Subtyping in width and depth |
| Whiley | Yes | Functional Imperative | Supported | ? |

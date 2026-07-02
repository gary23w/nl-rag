---
title: "Substructural type system"
source: https://en.wikipedia.org/wiki/Substructural_type_system
domain: linear-types
license: CC-BY-SA-4.0
tags: linear type system, linear logic, substructural type system, resource management
fetched: 2026-07-02
---

# Substructural type system

**Substructural type systems** are a family of type systems analogous to substructural logics where one or more of the structural rules are absent or only allowed under controlled circumstances. Such systems can constrain access to system resources such as files, locks, and memory by keeping track of changes of state and prohibiting invalid states.

## Different substructural type systems

Several type systems have emerged by discarding some of the structural rules of exchange, weakening, and contraction:

| Type systems | Exchange | Weakening | Contraction | Use |
|---|---|---|---|---|
| Ordered | —N/a | —N/a | —N/a | Exactly once, in the order it was introduced |
| Linear | Allowed | —N/a | —N/a | Exactly once |
| Affine | Allowed | Allowed | —N/a | At most once |
| Relevant | Allowed | —N/a | Allowed | At least once |
| Normal | Allowed | Allowed | Allowed | Arbitrarily |

### Ordered type system

*Ordered types* correspond to noncommutative logic where exchange, contraction and weakening are discarded. This can be used to model stack-based memory allocation (contrast with linear types which can be used to model heap-based memory allocation). Without the exchange property, an object may only be used when at the top of the modelled stack, after which it is popped off, resulting in every variable being used exactly once in the order it was introduced.

### Linear type systems

*Linear types* correspond to linear logic and ensure that objects are used exactly once. This allows the system to safely deallocate an object after its use, or to design software interfaces that guarantee a resource cannot be used once it has been closed or transitioned to a different state.

The Clean programming language makes use of uniqueness types (a variant of linear types) to help support concurrency, input/output, and in-place update of arrays.

Linear type systems allow references but not aliases. To enforce this, a reference goes out of scope after appearing on the right-hand side of an assignment, thus ensuring that only one reference to any object exists at once. Note that passing a reference as an argument to a function is a form of assignment, as the function parameter will be assigned the value inside the function, and therefore such use of a reference also causes it to go out of scope.

The single-reference property makes linear type systems suitable as programming languages for quantum computing, as it reflects the no-cloning theorem of quantum states. From the category theory point of view, no-cloning is a statement that there is no diagonal functor which could duplicate states; similarly, from the combinatory logic point of view, there is no K-combinator which can destroy states. From the lambda calculus point of view, a variable `x` can appear exactly once in a term.

Linear type systems are the internal language of closed symmetric monoidal categories, much in the same way that simply typed lambda calculus is the language of Cartesian closed categories. More precisely, one may construct functors between the category of linear type systems and the category of closed symmetric monoidal categories.

### Affine type systems

*Affine types* are a version of linear types allowing to *discard* (i.e. *not use*) a resource, corresponding to affine logic. An affine resource *can* be used *at most* once, while a linear one *must* be used *exactly* once.

### Relevant type system

*Relevant types* correspond to relevant logic which allows exchange and contraction, but not weakening, which translates to every variable being used at least once.

## The resource interpretation

The nomenclature offered by substructural type systems is useful to characterize resource management aspects of a language. Resource management is the aspect of language safety concerned with ensuring that each allocated resource is deallocated exactly once. Thus, **the resource interpretation** is only concerned with uses that transfer ownership – *moving*, where ownership is the responsibility to free the resource.

Uses that don't transfer ownership – *borrowing* – are not in scope of this interpretation, but *lifetime semantics* further restrict these uses to be between allocation and deallocation.

| Type | Disowning move | Obligatory move | Move quantification | Enforcible function call state machine |
|---|---|---|---|---|
| Normal | No | No | Any number of times | Topological ordering |
| Affine | Yes | No | At most once | Ordering |
| Linear | Yes | Yes | Exactly once | Ordering and completion |

### Resource-affine types

Under the resource interpretation, an *affine* type cannot be spent more than once.

As an example, the same variant of Hoare's vending machine can be expressed in English, logic and in Rust:

| English | Logic | Rust |
|---|---|---|
| A coin can buy you a piece of candy, a drink, or go out of scope. | Coin ⊸ Candy Coin ⊸ Drink Coin ⊸ ⊤ | fn buy_candy(_: Coin) -> Candy { Candy{} } fn buy_drink(_: Coin) -> Drink { Drink{} } |

What it means for Coin to be an affine type in this example (which it is unless it implements the Copy trait) is that trying to spend the same coin twice is an invalid program that the compiler is entitled to reject:

```mw
let coin = Coin {};
let candy = buy_candy(coin); // The lifetime of the coin variable ends here.
let drink = buy_drink(coin); // Compilation error: Use of moved variable that does not possess the Copy trait.
```

In other words, an affine type system can express the typestate pattern: Functions can consume and return an object wrapped in different types, acting like state transitions in a state machine that stores its state as a type in the caller's context – a *typestate*. An API can exploit this to statically enforce that its functions are called in a correct order.

What it doesn't mean, however, is that a variable can't be used without using it up:

```mw
// This function just borrows a coin: The ampersand means borrow.
fn validate(_: &Coin) -> Result<(), ()> { Ok(()) }

// The same coin variable can be used infinitely many times
// as long as it is not moved.
let coin = Coin {};
loop {
    validate(&coin)?;
}
```

What Rust is not able to express is a coin type that cannot go out of scope – that would take a linear type.

### Resource-linear types

Under the resource interpretation, a *linear* type not only *can* be moved, like an affine type, but *must* be moved – going out of scope is an invalid program.

```mw
{
    // Must be passed on, not dropped.
    let token = HotPotato {};

    // Suppose not every branch does away with it:
    if !queue.is_full() {
        queue.push(token);
    }

    // Compilation error: Holding an undroppable object as the scope ends.
}
```

An attraction with linear types is that destructors become regular functions that can take arguments, can fail and so on. This may for example avoid the need to keep state that is only used for destruction. A general advantage of passing function dependencies explicitly is that the order of function calls – destruction order – becomes statically verifiable in terms of the arguments' lifetimes. Compared to internal references, this does not require lifetime annotations as in Rust.

As with manual resource management, a practical problem is that any early return, as is typical of error handling, must achieve the same cleanup. This becomes pedantic in languages that have stack unwinding, where every function call is a potential early return. However, as a close analogy, the semantic of implicitly inserted destructor calls can be restored with deferred function calls.

### Resource-normal types

Under the resource interpretation, a *normal* type does not restrict how many times a variable can be moved from. C++ (specifically nondestructive move semantics) falls in this category.

```mw
auto coin = std::unique_ptr<Coin>();
auto candy = buy_candy(std::move(coin));
auto drink = buy_drink(std::move(coin)); // This is valid C++.
```

## Programming languages

The following programming languages support linear or affine types:

- ATS
- Clean
- Idris
- Mercury
- F*
- LinearML
- Alms
- Haskell with Glasgow Haskell Compiler (GHC) 9.0.1 or above
- Granule
- Rust
- Swift 5.9 and above

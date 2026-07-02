---
title: "Effect system"
source: https://en.wikipedia.org/wiki/Algebraic_effect
domain: koka-language
license: CC-BY-SA-4.0
tags: koka language, effect system, algebraic effect, microsoft research, continuation passing style
fetched: 2026-07-02
---

# Effect system

(Redirected from

Algebraic effect

)

In computing, an **effect system** is a formal system that describes the computational effects of computer programs, such as side effects. An effect system can be used to provide a compile-time check of the possible effects of the program.

The effect system extends the notion of type to have an "effect" component, which comprises an **effect kind** and a **region**. The effect kind describes *what* is being done, and the region describes *with what* (parameters) it is being done.

An effect system is typically an extension of a type system. The term "**type and effect system**" is sometimes used in this case. Often, a type of a value is denoted together with its effect as *type ! effect*, where both the type component and the effect component mention certain regions (for example, a type of a mutable memory cell is parameterized by the label of the memory region in which the cell resides). The term "algebraic effect" follows from the type system.

Effect systems may be used to prove the external purity of certain internally impure definitions: for example, if a function internally allocates and modifies a region of memory, but the function's type does not mention the region, then the corresponding effect may be erased from the function's effect.

## Examples

Some examples of the behaviors that can be described by effect systems include:

- Reading, writing or allocating memory: the effect kind is *read*, *write*, *allocate* or *free*, and the region is the point of the program where allocation was performed (i.e., each program point where allocation is performed is assigned a unique label, and region information is statically propagated along the dataflow). Most functions working with memory will actually be polymorphic in the region variable: for example, a function that swaps two locations in memory will have type `forall r1 r2, unit ! {read r1, read r2, write r1, write r2}`.
- Working with resources, such as files: for example, the effect kind may be *open*, *read* and *close*, and again, the region is the point of the program where the resource is opened.
- Control transfers with continuations and long jumps: the effect kind may be *goto* (i.e. the piece of code may perform a jump) and *comefrom* (i.e. the piece of code may be the target of a jump), and the region denotes the point of the program from which or to which the jump may be performed.

From a programmer's point of view, effects are useful as it allows for separating the implementation (*how*) of specific actions from the specification of what actions to perform. For example, an *ask name* effect can read from either the console, pop a window, or just return a default value. The control flow can be described as a blend of *yield* (in that the execution continues) and *throw* (in that an unhandled effect propagates down until handled).

## Implementations

### Core feature

- Koka is a statically typed functional programming language with algebraic effect handlers as a main feature.
- Eff is a statically typed functional programming language centered around algebraic effect handlers.
- Unison is a statically typed functional programming language with algebraic effect handlers (called "abilities" in the language) as a core part of the type system.
- Effekt is a research language centered around effect handlers and polymorphic effects.

### Full support

- Haskell is a statically typed functional programming language with several packages that allow for encoding of effects. However, Haskell is generally more focused on monads. The `runST` monad, for instance, effectively simulates a type and effect system, with "isolated regions of imperative programming". At type level, state isolation essentially stems from the deeper, rank-2 quantification over state in `runST`.

- OCaml introduced support for experimental effect handler primitives in version 5.0., high level syntax was added in OCaml 5.3 Note that, as of OCaml 5.4, OCaml's effects are not tracked at the type level.

### Partial support and prototypes

- Scala 3.1 is a statically typed, functional and object oriented programming language with experimental support for effects that is limited to exceptions, in the form of a `CanThrow` capability.
- Java is a statically typed, object-oriented programming language; its checked exceptions are a relatively limited example of an effect system. Only one effect kind — `throws` — is available, there is no way to resume with a value, and they cannot be used with functions (only methods) unless the function implements a custom `@FunctionalInterface`.

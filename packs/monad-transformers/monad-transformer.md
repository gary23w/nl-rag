---
title: "Monad transformer"
source: https://en.wikipedia.org/wiki/Monad_transformer
domain: monad-transformers
license: CC-BY-SA-4.0
tags: monad transformer, monad stack, kleisli category, free monad
fetched: 2026-07-02
---

# Monad transformer

In functional programming, a **monad transformer** is a type constructor which takes a monad as an argument and returns a monad as a result.

Monad transformers can be used to compose features encapsulated by monads – such as state, exception handling, and I/O – in a modular way. Typically, a monad transformer is created by generalising an existing monad; applying the resulting monad transformer to the identity monad yields a monad which is equivalent to the original monad (ignoring any necessary boxing and unboxing).

## Definition

A monad transformer consists of:

1. A type constructor `t` of kind `(* -> *) -> * -> *`
2. Monad operations `return` and `bind` (or an equivalent formulation) for all `t m` where `m` is a monad, satisfying the monad laws
3. An additional operation, `lift :: m a -> t m a`, satisfying the following laws: (the notation `bind` below indicates infix application):
  1. `lift . return = return`
  2. lift (m `bind` k) = (lift m) `bind` (lift . k)

## Examples

### The option monad transformer

Given any monad $\mathrm {M} \,A$ , the option monad transformer $\mathrm {M} \left(A^{?}\right)$ (where $A^{?}$ denotes the option type) is defined by:

${\begin{array}{ll}\mathrm {return$

### The exception monad transformer

Given any monad $\mathrm {M} \,A$ , the exception monad transformer $\mathrm {M} (A+E)$ (where E is the type of exceptions) is defined by:

${\begin{array}{ll}\mathrm {return$

### The reader monad transformer

Given any monad $\mathrm {M} \,A$ , the reader monad transformer $E\rightarrow \mathrm {M} \,A$ (where E is the environment type) is defined by:

${\begin{array}{ll}\mathrm {return$

### The state monad transformer

Given any monad $\mathrm {M} \,A$ , the state monad transformer $S\rightarrow \mathrm {M} (A\times S)$ (where S is the state type) is defined by:

${\begin{array}{ll}\mathrm {return$

### The writer monad transformer

Given any monad $\mathrm {M} \,A$ , the writer monad transformer $\mathrm {M} (W\times A)$ (where W is endowed with a monoid operation ∗ with identity element $\varepsilon$ ) is defined by:

${\begin{array}{ll}\mathrm {return$

### The continuation monad transformer

Given any monad $\mathrm {M} \,A$ , the continuation monad transformer maps an arbitrary type R into functions of type $(A\rightarrow \mathrm {M} \,R)\rightarrow \mathrm {M} \,R$ , where R is the result type of the continuation. It is defined by:

${\begin{array}{ll}\mathrm {return} \colon &A\rightarrow \left(A\rightarrow \mathrm {M} \,R\right)\rightarrow \mathrm {M} \,R\\&a\mapsto k\mapsto k\,a\\\mathrm {bind} \colon &\left(\left(A\rightarrow \mathrm {M} \,R\right)\rightarrow \mathrm {M} \,R\right)\rightarrow \left(A\rightarrow \left(B\rightarrow \mathrm {M} \,R\right)\rightarrow \mathrm {M} \,R\right)\rightarrow \left(B\rightarrow \mathrm {M} \,R\right)\rightarrow \mathrm {M} \,R\\&c\mapsto f\mapsto k\mapsto c\,\left(a\mapsto f\,a\,k\right)\\\mathrm {lift} \colon &\mathrm {M} \,A\rightarrow (A\rightarrow \mathrm {M} \,R)\rightarrow \mathrm {M} \,R\\&\mathrm {bind} \end{array}}$

Note that monad transformations are usually not commutative: for instance, applying the state transformer to the option monad yields a type $S\rightarrow \left(A\times S\right)^{?}$ (a computation which may fail and yield no final state), whereas the converse transformation has type $S\rightarrow \left(A^{?}\times S\right)$ (a computation which yields a final state and an optional return value).

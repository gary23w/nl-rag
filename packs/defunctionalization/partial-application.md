---
title: "Partial application"
source: https://en.wikipedia.org/wiki/Partial_application
domain: defunctionalization
license: CC-BY-SA-4.0
tags: defunctionalization transform, closure conversion, higher-order function, apply function
fetched: 2026-07-02
---

# Partial application

In computer science, **partial application** (or **partial function application**) refers to the process of fixing a number of arguments of a function, producing another function of smaller arity. Given a function $f\colon (X\times Y\times Z)\to N$ , we might fix (or 'bind') the first argument, producing a function of type ${\text{partial}}(f)\colon (Y\times Z)\to N$ . Evaluation of this function might be represented as $f_{\text{partial}}(2,3)$ . Note that the result of partial function application in this case is a function that takes two arguments. Partial application is sometimes incorrectly called currying, which is a related, but distinct concept.

## Motivation

Intuitively, partial function application says "if you fix the first arguments of the function, you get a function of the remaining arguments". For example, if function *div*(*x*,*y*) = *x*/*y*, then *div* with the parameter *x* fixed at 1 is another function: *div*1(*y*) = *div*(1,*y*) = 1/*y*. This is the same as the function *inv* that returns the multiplicative inverse of its argument, defined by *inv*(*y*) = 1/*y*.

The practical motivation for partial application is that very often the functions obtained by supplying some but not all of the arguments to a function are useful; for example, many languages have a function or operator similar to `plus_one`. Partial application makes it easy to define these functions, for example by creating a function that represents the addition operator with 1 bound as its first argument.

## Implementations

In languages such as ML, Haskell and F#, functions are defined in curried form by default. Supplying fewer than the total number of arguments is referred to as partial application.

In languages with first-class functions, one can define `curry`, `uncurry` and `papply` to perform currying and partial application explicitly. This might incur a greater run-time overhead due to the creation of additional closures, while Haskell can use more efficient techniques.

Scala implements optional partial application with placeholder, e.g. `def add(x: Int, y: Int) = {x+y}; add(1, _: Int)` returns an incrementing function. Scala also supports multiple parameter lists as currying, e.g. `def add(x: Int)(y: Int) = {x+y}; add(1) _`.

Clojure implements partial application using the `partial` function defined in its core library.

The C++ standard library provides `bind(function, args..)` to return a function object that is the result of partial application of the given arguments to the given function. Since C++20 the function `bind_front(function, args...)` is also provided which binds the first `sizeof...(args)` arguments of the function to the args. In contrast, `bind` allows binding any of the arguments of the function passed to it, not just the first ones. Alternatively, lambda expressions can be used:

```mw
int f(int a, int b);
auto f_partial = [](int a) { return f(a, 123); };
assert(f_partial(456) == f(456, 123) );
```

In Java, `MethodHandle.bindTo` partially applies a function to its first argument. Alternatively, since Java 8, lambdas can be used:

```mw
public static <A, B, R> Function<B, R> partialApply(BiFunction<A, B, R> biFunc, A value) {
    return b -> biFunc.apply(value, b);
}
```

In Raku, the `assuming` method creates a new function with fewer parameters.

The Python standard library module `functools` includes the `partial` function, allowing positional and named argument bindings, returning a new function.

In XQuery, an argument placeholder (`?`) is used for each non-fixed argument in a partial function application.

## Definitions

In the simply typed lambda calculus with function and product types (*λ*→,×) partial application, currying and uncurrying can be defined as

**`papply`**

(((

a

×

b

) →

c

) ×

a

) → (

b

→

c

) =

λ

(

f

,

x

).

λy

.

f

(

x

,

y

)

**`curry`**

((

a

×

b

) →

c

) → (

a

→ (

b

→

c

)) =

λf

.

λx

.

λy

.

f

(

x

,

y

)

**`uncurry`**

(

a

→ (

b

→

c

)) → ((

a

×

b

) →

c

) =

λf

.

λ

(

x

,

y

).

f x y

Note that `curry` `papply` = `curry`.

## Mathematical formulation and examples

Partial application can be a useful way to define several useful notions in mathematics.

Given sets $X,Y$ and Z , and a function $f:X\times Y\rightarrow Z$ , one can define the function

$f(\,\cdot \,,-):X\rightarrow (Y\rightarrow Z),$

where $(Y\rightarrow Z)$ is the set of functions $Y\rightarrow Z$ . The image of $x\in X$ under this map is $f(x,\,\cdot \,):Y\rightarrow Z$ . This is the function which sends $y\in Y$ to $f(x,y)$ . There are often structures on $X,Y,Z$ which mean that the image of $f(\,\cdot \,,-)$ restricts to some subset of functions $Y\rightarrow Z$ , as illustrated in the following examples.

### Group actions

A group action can be understood as a function $*:G\times X\rightarrow X$ . The partial evaluation $\rho :G\rightarrow {\text{Sym}}(X)\subset (X\rightarrow X)$ restricts to the group of bijections from X to itself. The group action axioms further ensure $\rho$ is a group homomorphism.

### Inner-products and canonical map to the dual

An inner-product on a vector space V over a field K is a map $\phi :V\times V\rightarrow K$ . The partial evaluation provides a canonical map to the dual vector space, $\phi (\,\cdot \,,-):V\rightarrow V^{*}\subset (V\rightarrow K)$ . If this is the inner-product of a Hilbert space, the Riesz representation theorem ensures this is an isomorphism.

### Cross-products and the adjoint map for Lie algebras

The partial application of the cross product $\times$ on $\mathbb {R} ^{3}$ is $\times (\,\cdot \,,-):\mathbb {R} ^{3}\mapsto {\text{End}}(\mathbb {R} ^{3})$ . The image of the vector $\mathbf {u}$ is a linear map $T_{\mathbf {u} }$ such that $T_{\mathbf {u} }(\mathbf {v} )=\mathbf {u} \times \mathbf {v}$ . The components of $T_{\mathbf {u} }$ can be found to be $(T_{\mathbf {u} })_{ij}=\epsilon _{ijk}u_{k}$ .

This is closely related to the adjoint map for Lie algebras. Lie algebras are equipped with a bracket $[\,\cdot \,,\,\cdot \,]:{\mathfrak {g}}\times {\mathfrak {g}}\rightarrow {\mathfrak {g}}$ . The partial application gives a map ${\text{ad}}:{\mathfrak {g}}\rightarrow {\text{End}}({\mathfrak {g}})$ . The axioms for the bracket ensure this map is a homomorphism of Lie algebras.

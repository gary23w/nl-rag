---
title: "Pure function"
source: https://en.wikipedia.org/wiki/Pure_function
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
---

# Pure function

In computer programming, a **pure function** is a function that has the following properties:

1. the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams, i.e., referential transparency), and
2. the function has no side effects (no mutation of non-local variables, mutable reference arguments or input/output streams).

## Examples

### Pure functions

The following examples of C++ functions are pure:

- `floor`, returning the floor of a number;
- `max`, returning the maximum of two values.
- the function *f*, defined as void f() { static std::atomic<unsigned int> x = 0; ++x; } The value of `x` can be only observed inside other invocations of `f()`, and as `f()` does not communicate the value of `x` to its environment, it is indistinguishable from function `void f() {}` that does nothing. Note that `x` is `std::atomic` so that modifications from multiple threads executing `f()` concurrently do not result in a data race, which has undefined behavior in C and C++.

### Impure functions

The following C++ functions are impure as they lack the above property 1:

- because of return value variation with a static variable int f() { static int x = 0; ++x; return x; }
- because of return value variation with a non-local variable int f() { return x; } For the same reason, e.g. the C++ library function `sin()` is not pure, since its result depends on the IEEE rounding mode which can be changed at runtime.
- because of return value variation with a mutable reference argument int f(int* x) { return *x; }
- because of return value variation with an input stream int f() { int x = 0; std::cin >> x; return x; }

The following C++ functions are impure as they lack the above property 2:

- because of mutation of a local static variable void f() { static int x = 0; ++x; }
- because of mutation of a non-local variable void f() { ++x; }
- because of mutation of a mutable reference argument void f(int* x) { ++*x; }
- because of mutation of an output stream void f() { std::cout << "Hello, world!" << std::endl; }

The following C++ functions are impure as they lack both the above properties 1 and 2:

- because of return value variation with a local static variable and mutation of a local static variable int f() { static int x = 0; ++x; return x; }
- because of return value variation with an input stream and mutation of an input stream int f() { int x = 0; std::cin >> x; return x; }

## I/O in pure functions

I/O is inherently impure: input operations undermine referential transparency, and output operations create side effects. Nevertheless, there is a sense in which a function can perform input or output and still be pure, if the sequence of operations on the relevant I/O devices is modeled explicitly as both an argument and a result, and I/O operations are taken to fail when the input sequence does not describe the operations actually taken since the program began execution.

The second point ensures that the only sequence usable as an argument must change with each I/O action; the first allows different calls to an I/O-performing function to return different results on account of the sequence arguments having changed.

The I/O monad is a programming idiom typically used to perform I/O in pure functional languages.

## Memoization

The outputs of a pure function can be cached in a look-up table. Any result that is returned from a given function is cached, and the next time the function is called with the same input parameters, the cached result is returned instead of computing the function again.

Memoization can be performed by wrapping the function in another function (wrapper function).

By means of memoization, the computational effort involved in the computations of the function itself can be reduced, at the cost of the overhead for managing the cache and an increase of memory requirements.

A C program for cached computation of factorial (`assert()` aborts with an error message if its argument is false; on a 32-bit machine, values beyond `fact(12)` cannot be represented.)

```mw
static int fact(int n) {
    return n <= 1 ? 1 : fact(n - 1) * n; 
}

int fact_wrapper(int n) {
    static int cache[13];
    assert(0 <= n && n < 13);
    if (cache[n] == 0)
        cache[n] = fact(n);
    return cache[n];
}
```

## Compiler optimizations

Functions that have just the above property 2 – that is, have no side effects – allow for compiler optimization techniques such as common subexpression elimination and loop optimization similar to arithmetic operators. A C++ example is the `length` method, returning the size of a string, which depends on the memory contents where the string points to, therefore lacking the above property 1. Nevertheless, in a single-threaded environment, the following C++ code

```mw
std::string s = "Hello, world!";
int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int l = 0;

for (int i = 0; i < 10; ++i) {
  l += s.length() + a[i];
}
```

can be optimized such that the value of `s.length()` is computed only once, before the loop.

Some programming languages allow for declaring a pure property to a function:

- In Fortran and D, the `pure` keyword can be used to declare a function to be just side-effect free (i.e. have just the above property 2). The compiler may be able to deduce property 1 on top of the declaration. See also: Fortran 95 language features § Pure procedures.
- In the GCC, the `pure` attribute specifies property 2, while the `const` attribute specifies a truly pure function with both properties.
- Languages offering compile-time function execution may require functions to be pure, sometimes with the addition of some other constraints. Examples include `constexpr` of C++ (both properties). See also: C++11 § constexpr – Generalized constant expressions.

## Unit testing

Since pure functions have identical return values for identical arguments, they are well suited to unit testing.

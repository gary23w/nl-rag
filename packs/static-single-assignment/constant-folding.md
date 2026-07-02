---
title: "Constant folding"
source: https://en.wikipedia.org/wiki/Constant_folding
domain: static-single-assignment
license: CC-BY-SA-4.0
tags: static single assignment, phi function, dominance frontier, SSA form
fetched: 2026-07-02
---

# Constant folding

**Constant folding** are related compiler optimizations used by many modern compilers that evaluate expressions whose values are known at compile time and replaces them with the computed result. For example, an expression such as `2 * 3` can be replaced by `6` before the program is run.

It is often used together with **constant propagation**, which substitutes variables whose values are known to be constant. An advanced form of constant propagation known as sparse conditional constant propagation can more accurately propagate constants and simultaneously remove dead code.

## Constant folding

Constant folding is the process of recognizing and evaluating constant expressions at compile time rather than computing them at runtime. Terms in constant expressions are typically simple literals, such as the integer literal `2`, but they may also be variables whose values are known at compile time. Consider the statement:

```mw
i = 320 * 200 * 32;
```

Most compilers would not actually generate two multiply instructions and a store for this statement. Instead, they identify constructs such as these and substitute the computed values at compile time (in this case, `2,048,000`).

Constant folding can make use of arithmetic identities. If `x` is numeric, the value of `0 * x` is zero even if the compiler does not know the value of `x`. (Note that this is not valid for IEEE floats, since `x` could be Infinity or NaN.)

Constant folding may apply to more than just numbers. Concatenation of string literals and constant strings can be constant folded. Code such as `"abc" + "def"` may be replaced with `"abcdef"`.

## Constant folding and cross compilation

Cross compilers have to ensure that the behaviour of the arithmetic operations on the host architecture matches that on the target architecture, as otherwise enabling constant folding will change the behaviour of the program. This is of particular importance in the case of floating point operations, whose precise implementation may vary widely.

## Constant propagation

Constant propagation is the process of substituting the values of known constants in expressions at compile time. Such constants include those defined above, as well as intrinsic functions applied to constant values. Consider the following pseudocode:

```mw
int x = 14;
int y = 7 - x / 2;
return y * (28 / x + 2);
```

Propagating x yields:

```mw
int x = 14;
int y = 7 - 14 / 2;
return y * (28 / 14 + 2);
```

Continuing to propagate yields the following (which would likely be further optimized by dead-code elimination of both x and y.)

```mw
int x = 14;
int y = 0;
return 0;
```

Constant propagation is implemented in compilers using reaching definition analysis results. If all a variable's reaching definitions are the same assignment - which assigns a same constant to the variable - then the variable will always have the same value, and can be replaced with the constant.

Constant propagation can also cause conditional branches to simplify to one or more unconditional statements, if the conditional expression can be evaluated to true or false at compile time to determine the only possible outcome.

## The optimizations in action

Constant folding and propagation are typically used together to achieve many simplifications and reductions, and their interleaved, iterative application continues until those effects cease.

Consider this unoptimized pseudocode returning a number unknown pending analysis:

```mw
int a = 30;
int b = 9 - (a / 5);
int c = b * 4;

if (c > 10) {
   c = c - 10;
}
return c * (60 / a);
```

Applying constant propagation once, followed by constant folding, yields:

```mw
int a = 30;
int b = 3;
int c = b * 4;

if (c > 10) {
   c = c - 10;
}
return c * 2;
```

Repeating both steps twice produces:

```mw
int a = 30;
int b = 3;
int c = 12;

if (true) {
   c = 2;
}
return c * 2;
```

Having replaced all uses of variables `a` and `b` with constants, the compiler's dead-code elimination applies to those variables, leaving:

```mw
int c = 12;

c = 2;

return c * 2;
```

(Boolean constructs vary among languages and compilers, but their details—such as the status, origin, and representation of true—do not affect these optimization principles.)

Traditional constant propagation produces no further optimization; it does not restructure programs.

However, a similar optimization, sparse conditional constant propagation, goes further by selecting the appropriate conditional branch, and removing the always-true conditional test. Thus, variable `c` becomes redundant, and only an operation on a constant remains:

```mw
return 4;
```

If that pseudocode constitutes a function body, the compiler knows the function evaluates to integer constant `4`, allowing replacement of calls to the function with `4`, and further increasing program efficiency.

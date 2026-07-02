---
title: "Fexpr"
source: https://en.wikipedia.org/wiki/Fexpr
domain: picolisp
license: CC-BY-SA-4.0
tags: picolisp language, lisp language, minimalism computing, interpreter computing, s expression
fetched: 2026-07-02
---

# Fexpr

In Lisp programming languages, a **fexpr** is a function whose operands are passed to it without being evaluated. When a fexpr is called, only the body of the fexpr is evaluated; no other evaluations take place except when explicitly initiated by the fexpr. In contrast, when an ordinary Lisp function is called, the operands are evaluated automatically, and only the results of these evaluations are provided to the function; and when a (traditional) Lisp macro is called, the operands are passed in unevaluated, but whatever result the macro function returns is automatically evaluated.

## Origin of the name "fexpr"

In early Lisp, the environment mapped each symbol to an association list, rather than directly to a value. Standard keys for these lists included two keys used to store a data value, to be looked up when the symbol occurred as an argument (APVAL and APVAL1); and four keys used to store a function, to be looked up when the symbol occurred as an operator. Of the function keys, SUBR indicated a compiled ordinary function, whose operands were evaluated and passed to it; FSUBR indicated a compiled special form, whose operands were passed unevaluated; EXPR indicated a user-defined ordinary function; and FEXPR indicated a user-defined special form. The only difference between a FEXPR and an EXPR was whether the operands were automatically evaluated.

In strict original usage, a FEXPR is therefore a user-defined function whose operands are passed unevaluated. However, in later usage the term *fexpr* may describe any first-class function whose operands are passed unevaluated, regardless of whether the function is primitive or user-defined.

| Key | Stores | Defined by | Function/Special form |
|---|---|---|---|
| APVAL | data value | — | — |
| APVAL1 | data value | — | — |
| SUBR | function | system | function |
| FSUBR | function | system | special-form |
| EXPR | function | user | function |
| FEXPR | function | user | special-form |

## Example

As a simple illustration of how fexprs work, here is a fexpr definition written in the Kernel programming language, which is similar to Scheme. (By convention in Kernel, the names of fexprs always start with $.)

```mw
($define! $f
   ($vau (x y z) e
      ($if (>=? (eval x e) 0)
           (eval y e)
           (eval z e))))
```

This definition provides a fexpr called $f, which takes three operands. When the fexpr is called, a local environment is created by extending the static environment where the fexpr was defined. Local bindings are then created: symbols x, y, and z are bound to the three operands of the call to the fexpr, and symbol e is bound to the dynamic environment from which the fexpr is being called. The body of the fexpr, ($if ...), is then evaluated in this local environment, and the result of that evaluation becomes the result of the call to the fexpr. The net effect is that the first operand is evaluated in the dynamic environment, and, depending on whether the result of that evaluation is non-negative, either the second or the third operand is evaluated and that result returned. The other operand, either the third or the second, is not evaluated.

This example is statically scoped: the local environment is an extension of the static environment. Before about 1980, the Lisp languages that supported fexprs were mainly dynamically scoped: the local environment was an extension of the dynamic environment, rather than of the static environment. However, it was still sometimes necessary to provide a local name for the dynamic environment, to avoid capturing the local parameter names.

## Mainstream use and deprecation

Fexpr support continued in Lisp 1.5, the last substantially standard dialect of Lisp before it fragmented into multiple languages. In the 1970s, the two dominant Lisp languages — MacLisp and Interlisp — both supported fexprs.

At the 1980 Conference on Lisp and Functional Programming, Kent Pitman presented a paper "Special Forms in Lisp" in which he discussed the advantages and disadvantages of macros and fexprs, and ultimately condemned fexprs. His central objection was that, in a Lisp dialect that allows fexprs, static analysis cannot determine generally whether an operator represents an ordinary function or a fexpr — therefore, static analysis cannot determine whether or not the operands will be evaluated. In particular, the compiler cannot tell whether a subexpression can be safely optimized, since the subexpression might be treated as unevaluated data at run-time.

> MACRO's offer an adequate mechanism for specifying special form definitions and ... FEXPR's do not. ... It is suggested that, in the design of future Lisp dialects, serious consideration should be given to the proposition that FEXPR's should be omitted from the language altogether.

Since the decline of MacLisp and Interlisp, the two Lisp languages that had risen to dominance by 1993 — Scheme and Common Lisp — do not support fexprs. newLISP does support fexprs, but calls them "macros". In Picolisp all built-in functions are fsubrs, while Lisp-level functions are exprs, fexprs, lexprs, or a mixture of those.

## Fexprs since 1980

Starting with Brian Smith's 3-Lisp in 1982, several experimental Lisp dialects have been devised to explore the limits of computational reflection. To support reflection, these Lisps support procedures that can reify various data structures related to the call to them — including the unevaluated operands of the call, which makes these procedures fexprs. By the late 1990s, fexprs had become associated primarily with computational reflection.

Some theoretical results on fexprs have been obtained. In 1993, John C. Mitchell used Lisp with fexprs as an example of a programming language whose source expressions cannot be formally abstract (because the concrete syntax of a source expression can always be extracted by a context in which it is an operand to a fexpr). In 1998, Mitchell Wand showed that adding a fexpr device to lambda calculus — a device that suppresses rewriting of operands — produces a formal system with a trivial equational theory, rendering it impossible to make source-to-source optimizations without a whole-program analysis. In 2007, John N. Shutt proposed an extension of lambda calculus that would model fexprs without suppressing rewriting of operands, potentially avoiding Wand's result.

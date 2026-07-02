---
title: "Curry (programming language)"
source: https://en.wikipedia.org/wiki/Curry_(programming_language)
domain: curry-language
license: CC-BY-SA-4.0
tags: curry language, functional logic programming, haskell language, lazy evaluation, narrowing algebraic
fetched: 2026-07-02
---

# Curry (programming language)

**Curry** is a declarative programming language, an implementation of the functional logic programming paradigm, and based on the Haskell language. It merges elements of functional and logic programming, including constraint programming integration.

It is nearly a superset of Haskell but does not support all language extensions of Haskell. In contrast to Haskell, Curry has built-in support for non-deterministic computations involving search.

## Foundations of functional logic programming

### Basic concepts

A functional program is a set of functions defined by equations or rules. A functional computation consists of replacing subexpressions by equal (with regard to the function definitions) subexpressions until no more replacements (or reductions) are possible and a value or normal form is obtained. For instance, consider the function double defined by

```
double x = x+x
```

The expression “double 1” is replaced by 1+1. The latter can be replaced by 2 if we interpret the operator “+” to be defined by an infinite set of equations, e.g., 1+1 = 2, 1+2 = 3, etc. In a similar way, one can evaluate nested expressions (where the subexpressions to be replaced are quoted):

```
'double (1+2)' → '(1+2)'+(1+2) → 3+'(1+2)' → '3+3' → 6
```

There is also another order of evaluation if we replace the arguments of operators from right to left:

```
'double (1+2)' → (1+2)+'(1+2)' → '(1+2)'+3 → '3+3' → 6
```

In this case, both derivations lead to the same result, a property known as confluence. This follows from a fundamental property of pure functional languages, termed referential transparency: the value of a computed result does not depend on the order or time of evaluation, due to the absence of side effects. This simplifies reasoning about, and maintaining, pure functional programs.

As many functional languages like Haskell do, Curry supports the definition of algebraic data types by enumerating their constructors. For instance, the type of Boolean values consists of the constructors True and False that are declared as follows:

```mw
data Bool = True | False
```

Functions on Booleans can be defined by pattern matching, i.e., by providing several equations for different argument values:

```mw
not True = False
not False = True
```

The principle of replacing equals by equals is still valid provided that the actual arguments have the required form, e.g.:

```
not '(not False)' → 'not True' → False
```

More complex data structures can be obtained by recursive data types. For instance, a list of elements, where the type of elements is arbitrary (denoted by the type variable a), is either the empty list “[]” or the non-empty list “x:xs” consisting of a first element x and a list xs:

```mw
data List a = [] | a : List a
```

The type “List a” is usually written as [a] and finite lists *x*1:*x*2:…:*x**n*:[] are written as [*x*1,*x*2,…,*x**n*]. We can define operations on recursive types by inductive definitions where pattern matching supports the convenient separation of the different cases. For instance, the concatenation operation “++” on polymorphic lists can be defined as follows (the optional type declaration in the first line specifies that “++” takes two lists as input and produces an output list, where all list elements are of the same unspecified type):

```mw
(++) :: [a] -> [a] -> [a] 
[] ++ ys = ys 
(x:xs) ++ ys = x : xs++ys
```

Beyond its application for various programming tasks, the operation “++” is also useful to specify the behavior of other functions on lists. For instance, the behavior of a function last that yields the last element of a list can be specified as follows: for all lists *xs* and elements *e,* last *xs* = *e* if ∃*ys*: *ys*++[*e*] = *xs.*

Based on this specification, one can define a function that satisfies this specification by employing logic programming features. Similarly to logic languages, functional logic languages provide search for solutions for existentially quantified variables. In contrast to pure logic languages, they support equation solving over nested functional expressions so that an equation like *ys*++[e] = [1,2,3] is solved by instantiating ys to the list [1,2] and *e* to the value 3. In Curry one can define the operation last as follows:

```mw
last xs | ys++[e] =:= xs = e where ys, e free
```

Here, the symbol “=:=” is used for equational constraints in order to provide a syntactic distinction from defining equations. Similarly, extra variables (i.e., variables not occurring in the left-hand side of the defining equation) are explicitly declared by “where … free” in order to provide some opportunities to detect bugs caused by typos. A conditional equation of the form *L* | *C* = *R* is applicable for reduction if its condition *C* has been solved. In contrast to purely functional languages where conditions are only evaluated to a Boolean value, functional logic languages support the solving of conditions by guessing values for the unknowns in the condition. Narrowing as discussed in the next section is used to solve this kind of conditions.

### Narrowing

Narrowing is a mechanism whereby a variable is bound to a value selected from among alternatives imposed by constraints. Each possible value is tried in some order, with the remainder of the program invoked in each case to determine the validity of the binding. Narrowing is an extension of logic programming, in that it performs a similar search, but can actually generate values as part of the search rather than just being limited to testing them.

Narrowing is useful because it allows a function to be treated as a relation: its value can be computed "in both directions". The Curry examples of the previous section illustrate this.

As noted in the prior section, narrowing can be thought of as reduction on a program term graph, and there are often many different ways (*strategies*) to reduce a given term graph. Antoy et al. proved in the 1990s that a particular narrowing strategy, *needed narrowing*, is optimal in the sense of doing a number of reductions to get to a "normal form" corresponding to a solution that is minimal among sound and complete strategies. Needed narrowing corresponds to a lazy strategy, in contrast to the SLD-resolution strategy of Prolog.

### Functional patterns

The rule defining last shown above expresses the fact that the actual argument must match the result of narrowing the expression ys++[e]. Curry can express this property also in the following more concise way:

```mw
last (ys++[e]) = e
```

Haskell does not allow such a declaration since the pattern in the left-hand side contains a defined function (++). Such a pattern is also called *functional pattern*. Functional patterns are enabled by the combined functional and logic features of Curry and support concise definitions of tasks requiring deep pattern matching in hierarchical data structures.

### Non-determinism

Since Curry is able to solve equations containing function calls with unknown values, its execution mechanism is based on non-deterministic computations, similarly to logic programming. This mechanism supports also the definition of *non-deterministic operations*, i.e., operations that delivers more than one result for a given input. The archetype of non-deterministic operations is the predefined infix operation ?, called *choice* operator, that returns one of its arguments. This operator is defined by the following rules:

```
x ? y = x
x ? y = y
```

Thus, the evaluation of the expression 0 ? 1 returns 0 as well as 1. Computing with non-deterministic operations and computing with free variables by narrowing has the same expressive power.

The rules defining ? show an important feature of Curry: all rules are tried in order to evaluate some operation. Hence, one can define by

```mw
insert x ys     = x : ys
insert x (y:ys) = y : insert x ys
```

an operation to insert an element into a list at an indeterminate position so that the operation perm defined by

```mw
perm []     = []
perm (x:xs) = insert x (perm xs)
```

returns any permutation of a given input list.

### Strategies

Due to the absence of side effects, a functional logic program can be executed with different strategies. To evaluate expressions, Curry uses a variant of the *needed narrowing* strategy which combines lazy evaluation with non-deterministic search strategies. In contrast to Prolog, which uses backtracking to search for solutions, Curry does not fix a particular search strategy. Hence, there are implementations of Curry, like KiCS2, where the user can easily select a search strategy, like depth-first search (backtracking), breadth-first search, iterative deepening, or parallel search.

## Implementations and programming tools

There are various implementations of Curry available. The most prominent representatives are the Portland Aachen Kiel Curry System PAKCS which compiles Curry programs into Prolog, the Kiel Curry System KiCS2 which compiles Curry programs into Haskell, the Münster Curry Compiler MCC, and Curry2Go which compiles Curry programs into Go programs and supports fair parallel search by mapping non-deterministic evaluations into light-weight processes (goroutines).

To support programming in Curry, there is a collection of Curry software packages, a Curry API search engine, a Curry language server providing IDE support, e.g., in Visual Studio Code, as well as various program documentation and analysis tools.

## Discussion and further reading

John Alan Robinson discussed in his invited CL2000 paper the integration of functional programming with logic programming where he wrote: "It is inexplicable that the two idioms have been kept apart for so long within the computational logic repertory. We need a single programming language in which both kinds of programming are possible and can be used in combination with each other." He surveyed different attempts and concluded that Curry is the "most promising one".

The textbook about principles and practice of programming languages contains a chapter on programming in Curry.

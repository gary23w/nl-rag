---
title: "First-class function"
source: https://en.wikipedia.org/wiki/First-class_function
domain: defunctionalization
license: CC-BY-SA-4.0
tags: defunctionalization transform, closure conversion, higher-order function, apply function
fetched: 2026-07-02
---

# First-class function

In computer science, a programming language is said to have **first-class functions** if it treats functions as first-class citizens. This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures. Some programming language theorists require support for anonymous functions (function literals) as well. In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type. The term was coined by Christopher Strachey in the context of "functions as first-class citizens" in the mid-1960s.

First-class functions are a necessity for the functional programming style, in which the use of higher-order functions is a standard practice. A simple example of a higher-ordered function is the *map* function, which takes, as its arguments, a function and a list, and returns the list formed by applying the function to each member of the list. For a language to support *map*, it must support passing a function as an argument.

There are certain implementation difficulties in passing functions as arguments or returning them as results, especially in the presence of non-local variables introduced in nested and anonymous functions. Historically, these were termed the *funarg problems*, the name coming from *function argument*. In early imperative languages these problems were avoided by either not supporting functions as result types (e.g. ALGOL 60, Pascal) or omitting nested functions and thus non-local variables (e.g. C). The early functional language Lisp took the approach of dynamic scoping, where non-local variables refer to the closest definition of that variable at the point where the function is executed, instead of where it was defined. Proper support for lexically scoped first-class functions was introduced in Scheme and requires handling references to functions as closures instead of bare function pointers, which in turn makes garbage collection a necessity.

## Concepts

In this section, we compare how particular programming idioms are handled in a functional language with first-class functions (Haskell) compared to an imperative language where functions are second-class citizens (C).

### Higher-order functions: passing functions as arguments

In languages where functions are first-class citizens, functions can be passed as arguments to other functions in the same way as other values (a function taking another function as argument is called a higher-order function). In the language Haskell:

```mw
map :: (a -> b) -> [a] -> [b]
map f []     = []
map f (x:xs) = f x : map f xs
```

Languages where functions are not first-class often still allow one to write higher-order functions through the use of features such as function pointers or delegates. In the language C:

```mw
void map(int (*f)(int), int x[], size_t n) {
    for (int i = 0; i < n; ++i) {
        x[i] = f(x[i]);
    }
}
```

There are a number of differences between the two approaches that are *not* directly related to the support of first-class functions. The Haskell sample operates on lists, while the C sample operates on arrays. Both are the most natural compound data structures in the respective languages and making the C sample operate on linked lists would have made it unnecessarily complex. This also accounts for the fact that the C function needs an additional parameter (giving the size of the array.) The C function updates the array in-place, returning no value, whereas in Haskell data structures are persistent (a new list is returned while the old is left intact.) The Haskell sample uses recursion to traverse the list, while the C sample uses iteration. Again, this is the most natural way to express this function in both languages, but the Haskell sample could easily have been expressed in terms of a fold and the C sample in terms of recursion. Finally, the Haskell function has a polymorphic type, as this is not supported by C we have fixed all type variables to the type constant `int`.

### Anonymous and nested functions

In languages supporting anonymous functions, we can pass such a function as an argument to a higher-order function:

```mw
main = map (\x -> 3 * x + 1) [1, 2, 3, 4, 5]
```

In a language which does not support anonymous functions, we have to bind it to a name instead:

```mw
int f(int x) {
    return 3 * x + 1;
}

int main() {
    int list[] = {1, 2, 3, 4, 5};
    map(f, list, 5);
}
```

### Non-local variables and closures

Once we have anonymous or nested functions, it becomes natural for them to refer to variables outside of their body (called *non-local variables*):

```mw
main = let a = 3
           b = 1
        in map (\x -> a * x + b) [1, 2, 3, 4, 5]
```

If functions are represented with bare function pointers, we can not know anymore how the value that is outside of the function's body should be passed to it, and because of that a closure needs to be built manually. Therefore we can not speak of "first-class" functions here.

```mw
typedef struct {
    int (*f)(int, int, int);
    int a;
    int b;
} Closure;

void map(Closure* closure, int x[], size_t n) {
    for (int i = 0; i < n; ++i) {
        x[i] = (closure->f)(closure->a, closure->b, x[i]);
    }
}

int f(int a, int b, int x) {
    return a * x + b;
}

void main() {
    int l[] = {1, 2, 3, 4, 5};
    int a = 3;
    int b = 1;
    Closure closure = {f, a, b};
    map(&closure, l, 5);
}
```

Also note that the `map` is now specialized to functions referring to two `int`s outside of their environment. This can be set up more generally, but requires more boilerplate code. If `f` would have been a nested function we would still have run into the same problem and this is the reason they are not supported in C.

### Higher-order functions: returning functions as results

When returning a function, we are in fact returning its closure. In the C example any local variables captured by the closure will go out of scope once we return from the function that builds the closure. Forcing the closure at a later point will result in undefined behaviour, possibly corrupting the stack. This is known as the upwards funarg problem.

### Assigning functions to variables

Assigning functions to variables and storing them inside (global) data structures potentially suffers from the same difficulties as returning functions.

```mw
f :: [[Integer] -> [Integer]]
f = let a = 3
        b = 1
     in [map (\x -> a * x + b), map (\x -> b * x + a)]
```

### Equality of functions

As one can test most literals and values for equality, it is natural to ask whether a programming language can support testing functions for equality. On further inspection, this question appears more difficult and one has to distinguish between several types of function equality:

**Extensional equality**

Two functions

f

and

g

are considered extensionally equal if they agree on their outputs for all inputs (∀

x

.

f

(

x

) =

g

(

x

)). Under this definition of equality, for example, any two implementations of a

stable sorting algorithm

, such as

insertion sort

and

merge sort

, would be considered equal. Deciding on extensional equality is

undecidable

in general and even for functions with finite domains often intractable. For this reason no programming language implements function equality as extensional equality.

**Intensional equality**

Under intensional equality, two functions

f

and

g

are considered equal if they have the same "internal structure". This kind of equality could be implemented in

interpreted languages

by comparing the

source code

of the function bodies (such as in Interpreted Lisp 1.5) or the

object code

in

compiled languages

. Intensional equality implies extensional equality (assuming the functions are deterministic and have no hidden inputs, such as the

program counter

or a mutable

global variable

.)

**Reference equality**

Given the impracticality of implementing extensional and intensional equality, most languages supporting testing functions for equality use reference equality. All functions or closures are assigned a unique identifier (usually the address of the function body or the closure) and equality is decided based on equality of the identifier. Two separately defined, but otherwise identical function definitions will be considered unequal. Referential equality implies intensional and extensional equality. Referential equality breaks

referential transparency

and is therefore not supported in

pure

languages, such as Haskell.

## Type theory

In type theory, the type of functions accepting values of type *A* and returning values of type *B* may be written as *A* → *B* or *B**A*. In the Curry–Howard correspondence, function types are related to logical implication; lambda abstraction corresponds to discharging hypothetical assumptions and function application corresponds to the modus ponens inference rule. Besides the usual case of programming functions, type theory also uses first-class functions to model associative arrays and similar data structures.

In category-theoretical accounts of programming, the availability of first-class functions corresponds to the closed category assumption. For instance, the simply typed lambda calculus corresponds to the internal language of Cartesian closed categories.

## Language support

Functional programming languages, such as Erlang, Scheme, ML, Haskell, F#, and Scala, all have first-class functions. When Lisp, one of the earliest functional languages, was designed, not all aspects of first-class functions were then properly understood, resulting in functions being dynamically scoped. The later Scheme and Common Lisp dialects do have lexically scoped first-class functions.

Many scripting languages, including Perl, Python, PHP, Lua, Tcl/Tk, JavaScript and Io, have first-class functions.

For imperative languages, a distinction has to be made between Algol and its descendants such as Pascal, the traditional C family, and the modern garbage-collected variants. The Algol family has allowed nested functions and higher-order taking function as arguments, but not higher-order functions that return functions as results (except Algol 68, which allows this). The reason for this was that it was not known how to deal with non-local variables if a nested-function was returned as a result (and Algol 68 produces runtime errors in such cases).

The C family allowed both passing functions as arguments and returning them as results, but avoided any problems by not supporting nested functions. (The gcc compiler allows them as an extension.) As the usefulness of returning functions primarily lies in the ability to return nested functions that have captured non-local variables, instead of top-level functions, these languages are generally not considered to have first-class functions.

Modern imperative languages often support garbage-collection making the implementation of first-class functions feasible. First-class functions have often only been supported in later revisions of the language, including C# 2.0 and Apple's Blocks extension to C, C++, and Objective-C. C++11 has added support for anonymous functions and closures to the language, but because of the non-garbage collected nature of the language, special care has to be taken for non-local variables in functions to be returned as results (see below).

Language

Higher-order functions

Nested functions

Non-local variables

Notes

Arguments

Results

Named

Anonymous

Closures

Partial application

Algol family

ALGOL 60

Yes

No

Yes

No

Downwards

No

Have

function types

.

ALGOL 68

Yes

Yes

Yes

Yes

Downwards

No

Pascal

Yes

No

Yes

No

Downwards

No

Ada

Yes

No

Yes

No

Downwards

No

Oberon

Yes

Non-nested only

Yes

No

Downwards

No

Delphi

Yes

Yes

Yes

2009

2009

No

C family

C

Yes

Yes

Yes in GNU C

Yes in Clang(

Blocks

)

Yes in Clang(

Blocks

)

No

Has

function pointers

.

C++

Yes

Yes

C++11

C++11

C++11

C++11

Has function pointers,

function objects

. (Also, see below.)

Explicit partial application possible with `std::bind`.

C#

Yes

Yes

7

2.0 / 3.0

2.0

3.0

Has

delegates

(2.0) and lambda expressions (3.0).

Objective-C

Yes

Yes

Using anonymous

2.0 + Blocks

2.0 + Blocks

No

Has function pointers.

Java

Yes

Yes

Using anonymous

Java 8

Java 8

Yes

Has

anonymous inner classes

.

Go

Yes

Yes

Using anonymous

Yes

Yes

Yes

Limbo

Yes

Yes

Yes

Yes

Yes

No

Newsqueak

Yes

Yes

Yes

Yes

Yes

No

Rust

Yes

Yes

Yes

Yes

Yes

Yes

Functional languages

Lisp

Syntax

Syntax

Yes

Yes

Common Lisp

No

(see below)

Scheme

Yes

Yes

Yes

Yes

Yes

SRFI 26

Julia

Yes

Yes

Yes

Yes

Yes

Yes

Clojure

Yes

Yes

Yes

Yes

Yes

Yes

ML

Yes

Yes

Yes

Yes

Yes

Yes

Haskell

Yes

Yes

Yes

Yes

Yes

Yes

jq

Yes

No

Yes

Expressions only

Downwards

No

Scala

Yes

Yes

Yes

Yes

Yes

Yes

Erlang

Yes

Yes

Yes

Yes

Yes

Yes

Elixir

Yes

Yes

Yes

Yes

Yes

Yes

F#

Yes

Yes

Yes

Yes

Yes

Yes

OCaml

Yes

Yes

Yes

Yes

Yes

Yes

Scripting languages

Io

Yes

Yes

Yes

Yes

Yes

No

JavaScript

Yes

Yes

Yes

Yes

Yes

ECMAScript 5

Partial application possible with user-land code on ES3

Lua

Yes

Yes

Yes

Yes

Yes

Yes

PHP

Yes

Yes

Using anonymous

5.3

5.3

No

Partial application possible with user-land code.

Perl

Yes

Yes

6

Yes

Yes

6

Python

Yes

Yes

Yes

Expressions only

Yes

2.5

(see below)

Ruby

Syntax

Syntax

Unscoped

Yes

Yes

1.9

(see below)

Other languages

Fortran

Yes

Yes

Yes

No

No

No

Maple

Yes

Yes

Yes

Yes

Yes

No

Mathematica

Yes

Yes

Yes

Yes

Yes

No

MATLAB

Yes

Yes

Yes

Yes

Yes

Yes

Partial application possible by automatic generation of new functions.

Smalltalk

Yes

Yes

Yes

Yes

Yes

Partial

Partial application possible through library.

Swift

Yes

Yes

Yes

Yes

Yes

Yes

**C++**

C++11

closures can capture non-local variables by copy construction, by reference (without extending their lifetime), or by

move construction

(the variable lives as long as the closure does). The first option is safe if the closure is returned but requires a copy and cannot be used to modify the original variable (which might not exist any more at the time the closure is called). The second option potentially avoids an expensive copy and allows to modify the original variable but is unsafe in case the closure is returned (see

dangling references

). The third option is safe if the closure is returned and does not require a copy but cannot be used to modify the original variable either.

**Java**

Java 8

closures can only capture final or "effectively final" non-local variables. Java's

function types

are represented as Classes. Anonymous functions take the type inferred from the context. Method references are limited. For more details, see

Anonymous function § Java limitations

.

**Lisp**

Lexically scoped

Lisp variants support closures.

Dynamically scoped

variants do not support closures or need a special construct to create closures.

In

Common Lisp

, the identifier of a function in the function namespace cannot be used as a reference to a first-class value. The special operator

function

must be used to retrieve the function as a value:

(function foo)

evaluates to a function object.

#'foo

exists as a shorthand notation. To apply such a function object, one must use the

funcall

function:

(funcall #'foo bar baz)

.

**Python**

Explicit partial application with

functools.partial

since version 2.5, and

operator.methodcaller

since version 2.6.

**Ruby**

The identifier of a regular "function" in Ruby (which is really a method) cannot be used as a value or passed. It must first be retrieved into a

Method

or

Proc

object to be used as first-class data. The syntax for calling such a function object differs from calling regular methods.

Nested method definitions do not actually nest the scope.

Explicit currying with

[1]

.

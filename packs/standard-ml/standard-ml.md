---
title: "Standard ML"
source: https://en.wikipedia.org/wiki/Standard_ML
domain: standard-ml
license: CC-BY-SA-4.0
tags: standard ml, sml language, sml/nj, ml programming language
fetched: 2026-07-02
---

# Standard ML

**Standard ML** (**SML**) is a general-purpose, high-level, modular, functional programming language with compile-time type checking and type inference. It is popular for writing compilers, for programming language research, and for developing theorem provers.

Standard ML is a modern dialect of ML, the language used in the Logic for Computable Functions (LCF) theorem-proving project. It is distinctive among widely used languages in that it has a formal specification, given as typing rules and operational semantics in *The Definition of Standard ML*, originally released in 1990, with a second and final revision being released in 1997.

## Language

Standard ML is a functional programming language with some impure features. Programs written in Standard ML consist of expressions in contrast to statements or commands, although some expressions of type unit are only evaluated for their side-effects.

### Functions

Like all functional languages, a key feature of Standard ML is the function, which is used for abstraction. The factorial function can be expressed as follows:

```mw
fun factorial n = 
    if n = 0 then 1 else n * factorial (n - 1)
```

### Type inference

An SML compiler must infer the static type `val factorial : int -> int` without user-supplied type annotations. It has to deduce that `n` is only used with integer expressions, and must therefore itself be an integer, and that all terminal expressions are integer expressions.

### Declarative definitions

The same function can be expressed with clausal function definitions where the *if*-*then*-*else* conditional is replaced with templates of the factorial function evaluated for specific values:

```mw
fun factorial 0 = 1
  | factorial n = n * factorial (n - 1)
```

### Imperative definitions

or iteratively:

```mw
fun factorial n = let val i = ref n and acc = ref 1 in
    while !i > 0 do (acc := !acc * !i; i := !i - 1); !acc
end
```

### Lambda functions

or as a lambda function:

```mw
val rec factorial = fn 0 => 1 | n => n * factorial (n - 1)
```

Here, the keyword `val` introduces a binding of an identifier to a value, `fn` introduces an anonymous function, and `rec` allows the definition to be self-referential.

### Local definitions

The encapsulation of an invariant-preserving tail-recursive tight loop with one or more accumulator parameters within an invariant-free outer function, as seen here, is a common idiom in Standard ML.

Using a local function, it can be rewritten in a more efficient tail-recursive style:

```mw
local
    fun loop (0, acc) = acc
      | loop (m, acc) = loop (m - 1, m * acc)
in
    fun factorial n = loop (n, 1)
end
```

### Type synonyms

A type synonym is defined with the keyword `type`. Here is a type synonym for points on a plane, and functions computing the distances between two points, and the area of a triangle with the given corners as per Heron's formula. (These definitions will be used in subsequent examples).

```mw
type loc = real * real

fun square (x : real) = x * x

fun dist (x, y) (x', y') =
    Math.sqrt (square (x' - x) + square (y' - y))

fun heron (a, b, c) = let
    val x = dist a b
    val y = dist b c
    val z = dist a c
    val s = (x + y + z) / 2.0
    in
        Math.sqrt (s * (s - x) * (s - y) * (s - z))
    end
```

### Algebraic datatypes

Standard ML provides strong support for algebraic datatypes (ADT). A data type can be thought of as a disjoint union of tuples (or a "sum of products"). They are easy to define and easy to use, largely because of pattern matching, and most Standard ML implementations' pattern-exhaustiveness checking and pattern redundancy checking.

In object-oriented programming languages, a disjoint union can be expressed as class hierarchies. However, in contrast to class hierarchies, ADTs are closed. Thus, the extensibility of ADTs is orthogonal to the extensibility of class hierarchies. Class hierarchies can be extended with new subclasses which implement the same interface, while the functions of ADTs can be extended for the fixed set of constructors. See expression problem.

A datatype is defined with the keyword `datatype`, as in:

```mw
datatype shape
    = Circle   of loc * real      (* center and radius *)
    | Square   of loc * real      (* upper-left corner and side length; axis-aligned *)
    | Triangle of loc * loc * loc (* corners *)
```

Note that a type synonym cannot be recursive; datatypes are necessary to define recursive constructors. (This is not at issue in this example.)

### Pattern matching

Patterns are matched in the order in which they are defined. C programmers can use tagged unions, dispatching on tag values, to do what ML does with datatypes and pattern matching. Nevertheless, while a C program decorated with appropriate checks will, in a sense, be as robust as the corresponding ML program, those checks will of necessity be dynamic; ML's static checks provide strong guarantees about the correctness of the program at compile time.

Function arguments can be defined as patterns as follows:

```mw
fun area (Circle (_, r)) = Math.pi * square r
  | area (Square (_, s)) = square s
  | area (Triangle p) = heron p (* see above *)
```

The so-called "clausal form" of function definition, where arguments are defined as patterns, is merely syntactic sugar for a case expression:

```mw
fun area shape = case shape of
    Circle (_, r) => Math.pi * square r
  | Square (_, s) => square s
  | Triangle p => heron p
```

#### Exhaustiveness checking

Pattern-exhaustiveness checking will make sure that each constructor of the datatype is matched by at least one pattern.

The following pattern is not exhaustive:

```mw
fun center (Circle (c, _)) = c
  | center (Square ((x, y), s)) = (x + s / 2.0, y + s / 2.0)
```

There is no pattern for the `Triangle` case in the `center` function. The compiler will issue a warning that the case expression is not exhaustive, and if a `Triangle` is passed to this function at runtime, `exception Match` will be raised.

#### Redundancy checking

The pattern in the second clause of the following (meaningless) function is redundant:

```mw
fun f (Circle ((x, y), r)) = x + y
  | f (Circle _) = 1.0
  | f _ = 0.0
```

Any value that would match the pattern in the second clause would also match the pattern in the first clause, so the second clause is unreachable. Therefore, this definition as a whole exhibits redundancy, and causes a compile-time warning.

The following function definition is exhaustive and not redundant:

```mw
val hasCorners = fn (Circle _) => false | _ => true
```

If control gets past the first pattern (`Circle`), we know the shape must be either a `Square` or a `Triangle`. In either of those cases, we know the shape has corners, so we can return `true` without discerning the actual shape.

### Higher-order functions

Functions can consume functions as arguments:

```mw
fun map f (x, y) = (f x, f y)
```

Functions can produce functions as return values:

```mw
fun constant k = (fn _ => k)
```

Functions can also both consume and produce functions:

```mw
fun compose (f, g) = (fn x => f (g x))
```

The function `List.map` from the basis library is one of the most commonly used higher-order functions in Standard ML:

```mw
fun map _ [] = []
  | map f (x :: xs) = f x :: map f xs
```

A more efficient implementation with tail-recursive `List.foldl`:

```mw
fun map f = List.rev o List.foldl (fn (x, acc) => f x :: acc) []
```

### Exceptions

Exceptions are raised with the keyword `raise` and handled with the pattern matching `handle` construct. The exception system can implement non-local exit; this optimization technique is suitable for functions like the following.

```mw
local
    exception Zero;
    val p = fn (0, _) => raise Zero | (a, b) => a * b
in
    fun prod xs = List.foldl p 1 xs handle Zero => 0
end
```

When `exception Zero` is raised, control leaves the function `List.foldl` altogether. Consider the alternative: the value 0 would be returned, it would be multiplied by the next integer in the list, the resulting value (inevitably 0) would be returned, and so on. The raising of the exception allows control to skip over the entire chain of frames and avoid the associated computation. Note the use of the underscore (`_`) as a wildcard pattern.

The same optimization can be obtained with a tail call.

```mw
local
    fun p a (0 :: _) = 0
      | p a (x :: xs) = p (a * x) xs
      | p a [] = a
in
    val prod = p 1
end
```

### Module system

Standard ML's advanced module system allows programs to be decomposed into hierarchically organized *structures* of logically related type and value definitions. Modules provide not only namespace control but also abstraction, in the sense that they allow the definition of abstract data types. Three main syntactic constructs comprise the module system: signatures, structures and functors.

#### Signatures

A *signature* is an interface, usually thought of as a type for a structure; it specifies the names of all entities provided by the structure, the arity of each type component, the type of each value component, and the signature of each substructure. The definitions of type components are optional; type components whose definitions are hidden are *abstract types*.

For example, the signature for a queue may be:

```mw
signature QUEUE = sig
    type 'a queue
    exception QueueError;
    val empty     : 'a queue
    val isEmpty   : 'a queue -> bool
    val singleton : 'a -> 'a queue
    val fromList  : 'a list -> 'a queue
    val insert    : 'a * 'a queue -> 'a queue
    val peek      : 'a queue -> 'a
    val remove    : 'a queue -> 'a * 'a queue
end
```

This signature describes a module that provides a polymorphic type `'a queue`, `exception QueueError`, and values that define basic operations on queues.

#### Structures

A *structure* is a module; it consists of a collection of types, exceptions, values and structures (called *substructures*) packaged together into a logical unit.

A queue structure can be implemented as follows:

```mw
structure TwoListQueue :> QUEUE = struct
    type 'a queue = 'a list * 'a list

    exception QueueError;

    val empty = ([], [])

    fun isEmpty ([], []) = true
      | isEmpty _ = false

    fun singleton a = ([], [a])

    fun fromList a = ([], a)

    fun insert (a, ([], [])) = singleton a
      | insert (a, (ins, outs)) = (a :: ins, outs)

    fun peek (_, []) = raise QueueError
      | peek (ins, outs) = List.hd outs

    fun remove (_, []) = raise QueueError
      | remove (ins, [a]) = (a, ([], List.rev ins))
      | remove (ins, a :: outs) = (a, (ins, outs))
end
```

This definition declares that `structure TwoListQueue` implements `signature QUEUE`. Furthermore, the *opaque ascription* denoted by `:>` states that any types which are not defined in the signature (i.e. `type 'a queue`) should be abstract, meaning that the definition of a queue as a pair of lists is not visible outside the module. The structure implements all of the definitions in the signature.

The types and values in a structure can be accessed with "dot notation":

```mw
val q : string TwoListQueue.queue = TwoListQueue.empty
val q' = TwoListQueue.insert (Real.toString Math.pi, q)
```

#### Functors

A *functor* is a function from structures to structures; that is, a functor accepts one or more arguments, which are usually structures of a given signature, and produces a structure as its result. Functors are used to implement generic data structures and algorithms.

One popular algorithm for breadth-first search of trees makes use of queues. Here is a version of that algorithm parameterized over an abstract queue structure:

```mw
(* after Okasaki, ICFP, 2000 *)
functor BFS (Q: QUEUE) = struct
  datatype 'a tree = E | T of 'a * 'a tree * 'a tree

  local
    fun bfsQ q = if Q.isEmpty q then [] else search (Q.remove q)
    and search (E, q) = bfsQ q
      | search (T (x, l, r), q) = x :: bfsQ (insert (insert q l) r)
    and insert q a = Q.insert (a, q)
  in
    fun bfs t = bfsQ (Q.singleton t)
  end
end

structure QueueBFS = BFS (TwoListQueue)
```

Within `functor BFS`, the representation of the queue is not visible. More concretely, there is no way to select the first list in the two-list queue, if that is indeed the representation being used. This data abstraction mechanism makes the breadth-first search truly agnostic to the queue's implementation. This is in general desirable; in this case, the queue structure can safely maintain any logical invariants on which its correctness depends behind the bulletproof wall of abstraction.

## Code examples

Snippets of SML code are most easily studied by entering them into an interactive top-level.

### Hello, world!

The following is a "Hello, World!" program:

| hello.sml |
|---|
| print "Hello, world!\n"; |
| sh |
| $ mlton hello.sml $ ./hello Hello, world! |

### Algorithms

#### Insertion sort

Insertion sort for `int list` (ascending) can be expressed concisely as follows:

```mw
fun insert (x, []) = [x] | insert (x, h :: t) = sort x (h, t)
and sort x (h, t) = if x < h then [x, h] @ t else h :: insert (x, t)
val insertionsort = List.foldl insert []
```

#### Mergesort

Here, the classic mergesort algorithm is implemented in three functions: split, merge and mergesort. Also note the absence of types, with the exception of the syntax `op ::` and `[]` which signify lists. This code will sort lists of any type, so long as a consistent ordering function `cmp` is defined. Using Hindley–Milner type inference, the types of all variables can be inferred, even complicated types such as that of the function `cmp`.

**Split**

`fun split` is implemented with a stateful closure which alternates between `true` and `false`, ignoring the input:

```mw
fun alternator {} = let val state = ref true
    in fn a => !state before state := not (!state) end

(* Split a list into near-halves which will either be the same length,
 * or the first will have one more element than the other.
 * Runs in O(n) time, where n = |xs|.
 *)
fun split xs = List.partition (alternator {}) xs
```

**Merge**

Merge uses a local function loop for efficiency. The inner `loop` is defined in terms of cases: when both lists are non-empty (`x :: xs`) and when one list is empty (`[]`).

This function merges two sorted lists into one sorted list. Note how the accumulator `acc` is built backwards, then reversed before being returned. This is a common technique, since `'a list` is represented as a linked list; this technique requires more clock time, but the asymptotics are not worse.

```mw
(* Merge two ordered lists using the order cmp.
 * Pre: each list must already be ordered per cmp.
 * Runs in O(n) time, where n = |xs| + |ys|.
 *)
fun merge cmp (xs, []) = xs
  | merge cmp (xs, y :: ys) = let
    fun loop (a, acc) (xs, []) = List.revAppend (a :: acc, xs)
      | loop (a, acc) (xs, y :: ys) =
        if cmp (a, y)
        then loop (y, a :: acc) (ys, xs)
        else loop (a, y :: acc) (xs, ys)
    in
        loop (y, []) (ys, xs)
    end
```

**Mergesort**

The main function:

```mw
fun ap f (x, y) = (f x, f y)

(* Sort a list in according to the given ordering operation cmp.
 * Runs in O(n log n) time, where n = |xs|.
 *)
fun mergesort cmp [] = []
  | mergesort cmp [x] = [x]
  | mergesort cmp xs = (merge cmp o ap (mergesort cmp) o split) xs
```

#### Quicksort

Quicksort can be expressed as follows. `fun part` is a closure that consumes an order operator `op <<`.

```mw
infix <<

fun quicksort (op <<) = let
    fun part p = List.partition (fn x => x << p)
    fun sort [] = []
      | sort (p :: xs) = join p (part p xs)
    and join p (l, r) = sort l @ p :: sort r
    in
        sort
    end
```

### Expression interpreter

Note the relative ease with which a small expression language can be defined and processed:

```mw
exception TyErr;

datatype ty = IntTy | BoolTy

fun unify (IntTy, IntTy) = IntTy
  | unify (BoolTy, BoolTy) = BoolTy
  | unify (_, _) = raise TyErr

datatype exp
    = True
    | False
    | Int of int
    | Not of exp
    | Add of exp * exp
    | If  of exp * exp * exp

fun infer True = BoolTy
  | infer False = BoolTy
  | infer (Int _) = IntTy
  | infer (Not e) = (assert e BoolTy; BoolTy)
  | infer (Add (a, b)) = (assert a IntTy; assert b IntTy; IntTy)
  | infer (If (e, t, f)) = (assert e BoolTy; unify (infer t, infer f))
and assert e t = unify (infer e, t)

fun eval True = True
  | eval False = False
  | eval (Int n) = Int n
  | eval (Not e) = if eval e = True then False else True
  | eval (Add (a, b)) = (case (eval a, eval b) of (Int x, Int y) => Int (x + y))
  | eval (If (e, t, f)) = eval (if eval e = True then t else f)

fun run e = (infer e; SOME (eval e)) handle TyErr => NONE
```

Example usage on well-typed and ill-typed expressions:

```mw
val SOME (Int 3) = run (Add (Int 1, Int 2)) (* well-typed *)
val NONE = run (If (Not (Int 1), True, False)) (* ill-typed *)
```

### Arbitrary-precision integers

The `IntInf` module provides arbitrary-precision integer arithmetic. Moreover, integer literals may be used as arbitrary-precision integers without the programmer having to do anything.

The following program implements an arbitrary-precision factorial function:

| fact.sml |
|---|
| fun fact n : IntInf.int = if n = 0 then 1 else n * fact (n - 1); fun printLine str = TextIO.output (TextIO.stdOut, str ^ "\n"); val () = printLine (IntInf.toString (fact 120)); |
| bash |
| $ mlton fact.sml $ ./fact 6689502913449127057588118054090372586752746333138029810295671352301 6335572449629893668741652719849813081576378932140905525344085894081 21859898481114389650005964960521256960000000000000000000000000000 |

### Partial application

Curried functions have many applications, such as eliminating redundant code. For example, a module may require functions of type `a -> b`, but it is more convenient to write functions of type `a * c -> b` where there is a fixed relationship between the objects of type `a` and `c`. A function of type `c -> (a * c -> b) -> a -> b` can factor out this commonality. This is an example of the adapter pattern.

In this example, `fun d` computes the numerical derivative of a given function `f` at point `x`:

```mw
- fun d delta f x = (f (x + delta) - f (x - delta)) / (2.0 * delta)
val d = fn : real -> (real -> real) -> real -> real
```

The type of `fun d` indicates that it maps a "float" onto a function with the type `(real -> real) -> real -> real`. This allows us to partially apply arguments, known as currying. In this case, function `d` can be specialised by partially applying it with the argument `delta`. A good choice for `delta` when using this algorithm is the cube root of the machine epsilon.

```mw
- val d' = d 1E~8;
val d' = fn : (real -> real) -> real -> real
```

The inferred type indicates that `d'` expects a function with the type `real -> real` as its first argument. We can compute an approximation to the derivative of $f(x)=x^{3}-x-1$ at $x=3$ . The correct answer is $f'(3)=27-1=26$ .

```mw
- d' (fn x => x * x * x - x - 1.0) 3.0;
val it = 25.9999996644 : real
```

## Libraries

### Standard

The Basis Library has been standardized and ships with most implementations. It provides modules for trees, arrays, and other data structures, and input/output and system interfaces.

### Third party

For numerical computing, a Matrix module exists (but is currently broken), https://www.cs.cmu.edu/afs/cs/project/pscico/pscico/src/matrix/README.html.

For graphics, cairo-sml is an open source interface to the Cairo graphics library. For machine learning, a library for graphical models exists.

## Implementations

Implementations of Standard ML include the following:

**Standard**

- HaMLet: a Standard ML interpreter that aims to be an accurate and accessible reference implementation of the standard
- MLton (mlton.org): a whole-program optimizing compiler which strictly conforms to the Definition and produces very fast code compared to other ML implementations, including backends for LLVM and C
- Moscow ML: a light-weight implementation, based on the Caml Light runtime engine which implements the full Standard ML language, including modules and much of the basis library
- Poly/ML: a full implementation of Standard ML that produces fast code and supports multicore hardware (via Portable Operating System Interface (POSIX) threads); its runtime system performs parallel garbage collection and online sharing of immutable substructures.
- Standard ML of New Jersey (smlnj.org): a full compiler, with associated libraries, tools, an interactive shell, and documentation with support for Concurrent ML
- SML.NET: a Standard ML compiler for the Common Language Runtime with extensions for linking with other .NET framework code
- ML Kit Archived 2016-01-07 at the Wayback Machine: an implementation based very closely on the Definition, integrating a garbage collector (which can be disabled) and region-based memory management with automatic inference of regions, aiming to support real-time applications

**Derivative**

- Alice: an interpreter for Standard ML by Saarland University with support for parallel programming using futures, lazy evaluation, distributed computing via remote procedure calls and constraint programming
- SML#: an extension of SML providing record polymorphism and C language interoperability. It is a conventional native compiler and its name is *not* an allusion to running on the .NET framework
- SOSML: an implementation written in TypeScript, supporting most of the SML language and select parts of the basis library

**Research**

- CakeML is a REPL version of ML with formally verified runtime and translation to assembler.
- Isabelle (Isabelle/ML Archived 2020-08-30 at the Wayback Machine) integrates parallel Poly/ML into an interactive theorem prover, with a sophisticated IDE (based on jEdit) for official Standard ML (SML'97), the Isabelle/ML dialect, and the proof language. Starting with Isabelle2016, there is also a source-level debugger for ML.
- Poplog implements a version of Standard ML, along with Common Lisp and Prolog, allowing mixed language programming; all are implemented in POP-11, which is compiled incrementally.
- TILT is a full certifying compiler for Standard ML which uses typed intermediate languages to optimize code and ensure correctness, and can compile to typed assembly language.

All of these implementations are open-source and freely available. Most are implemented themselves in Standard ML. There are no longer any commercial implementations; Harlequin, now defunct, once produced a commercial IDE and compiler called MLWorks which passed on to Xanalys and was later open-sourced after it was acquired by Ravenbrook Limited on April 26, 2013.

## Major projects using SML

The IT University of Copenhagen's entire enterprise architecture is implemented in around 100,000 lines of SML, including staff records, payroll, course administration and feedback, student project management, and web-based self-service interfaces.

The proof assistants HOL4, Isabelle, LEGO, and Twelf are written in Standard ML. It is also used by compiler writers and integrated circuit designers such as ARM.

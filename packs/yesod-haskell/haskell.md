---
title: "Haskell"
source: https://en.wikipedia.org/wiki/Haskell
domain: yesod-haskell
license: CC-BY-SA-4.0
tags: yesod haskell framework, type safe haskell web, haskell web framework, yesod template haskell
fetched: 2026-07-02
---

# Haskell

**Haskell** (/ˈhæskəl/) is a general-purpose, statically typed, purely functional programming language with type inference and lazy evaluation. Haskell pioneered several programming language features including type classes for type-safe operator overloading and monadic input/output (IO). It is named after logician Haskell Curry. Haskell's main implementation is the Glasgow Haskell Compiler (GHC).

Haskell's semantics are historically based on those of the Miranda programming language, which served to focus the efforts of the initial Haskell working group. The last formal specification of the language was made in July 2010, while the development of GHC continues to expand Haskell via language extensions.

Haskell is used in academia and industry. As of May 2021, Haskell was the 28th most popular programming language by Google searches for tutorials, and made up less than 1% of active users on the GitHub source code repository.

## History

After the release of Miranda by Research Software Ltd. in 1985, interest in lazy functional languages grew. By 1987, more than a dozen non-strict, purely functional programming languages existed. Miranda was the most widely used, but it was proprietary software. At the conference on Functional Programming Languages and Computer Architecture (FPCA '87) in Portland, Oregon, there was a strong consensus that a committee be formed to define an open standard for such languages. The committee's purpose was to consolidate existing functional languages into a common one to serve as a basis for future research in functional-language design.

### Haskell 1.0 to 1.4

Haskell was developed by a committee, attempting to bring together off-the-shelf solutions where possible.

Type classes were first proposed by Philip Wadler and Stephen Blott to address the ad hoc handling of equality types and arithmetic overloading in languages at the time.

In early versions of Haskell up until and including version 1.2, user interaction and input/output (IO) were handled by both streams-based and continuation-based mechanisms, which were widely considered unsatisfactory. In version 1.3, monadic IO was introduced, along with the generalisation of type classes to higher kinds (type constructors). Along with "do notation", which provides syntactic sugar for the `Monad` type class, this gave Haskell an effect system that maintained referential transparency and was convenient.

Another notable change in early versions was the moving of the "sequential evaluation" operation `seq` (which creates a data dependency between values, and is used in lazy languages to avoid excessive memory consumption) from a type class to a standard function to make refactoring more practical.

The first version of Haskell ("Haskell 1.0") was defined in 1990. The committee's efforts resulted in a series of language definitions (1.0, 1.1, 1.2, 1.3, and 1.4).

### Haskell 98

In late 1997, the series culminated in *Haskell 98*, intended to specify a stable, minimal, portable version of the language and an accompanying standard library for teaching, and as a base for future extensions. The committee expressly welcomed creating extensions and variants of Haskell 98 via adding and incorporating experimental features.

In February 1999, the Haskell 98 language standard was originally published as *The Haskell 98 Report*. In January 2003, a revised version was published as *Haskell 98 Language and Libraries: The Revised Report*. The language continues to evolve rapidly, with the Glasgow Haskell Compiler (GHC) implementation representing the current *de facto* standard.

### Haskell 2010

In early 2006, the process of defining a successor to the Haskell 98 standard, informally named *Haskell Prime*, began. This was intended to be an ongoing incremental process to revise the language definition, producing a new revision up to once per year. The first revision, named *Haskell 2010*, was announced in November 2009 and published in July 2010.

Haskell 2010 added several well-used and uncontroversial features previously enabled via compiler-specific flags.

- Hierarchical module names. Module names are allowed to consist of dot-separated sequences of capitalized identifiers, rather than only one such identifier. This lets modules be named in a hierarchical manner (e.g., `Data.List` instead of `List`), although technically modules are still in a single monolithic namespace. This extension was specified in an addendum to Haskell 98 and was in practice universally used.
- The foreign function interface (FFI) allows bindings to other programming languages. Only bindings to C are specified in the Report, but the design allows for other language bindings. To support this, data type declarations were permitted to contain no constructors, enabling robust nonce types for foreign data that could not be constructed in Haskell. This extension was also previously specified in an Addendum to the Haskell 98 Report and widely used.
- So-called *n*+*k* patterns (definitions of the form `fact (n+1) = (n+1) * fact n`) were no longer allowed. This syntactic sugar had misleading semantics, in which the code looked like it used the `(+)` operator, but in fact desugared to code using `(-)` and `(>=)`.
- The rules of type inference were relaxed to allow more programs to type check.
- Some syntax issues (changes in the formal grammar) were fixed: pattern guards were added, allowing pattern matching within guards; resolution of operator fixity was specified in a simpler way that reflected actual practice; an edge case in the interaction of the language's lexical syntax of operators and comments was addressed, and the interaction of do-notation and if-then-else was tweaked to eliminate unexpected syntax errors.
- The `LANGUAGE` pragma was specified. By 2010, dozens of extensions to the language were in wide use, and GHC (among other compilers) provided the `LANGUAGE` pragma to specify individual extensions with a list of identifiers. Haskell 2010 compilers are required to support the `Haskell2010` extension and are encouraged to support several others, which correspond to extensions added in Haskell 2010.

### Future standards

The next formal specification had been planned for 2020. On 29 October 2021, with GHC version 9.2.1, the GHC2021 extension was released. While this is not a formal language spec, it combines several stable, widely used GHC extensions to Haskell 2010.

## Features

Haskell features lazy evaluation, lambda expressions, pattern matching, list comprehension, type classes and type polymorphism. It is a purely functional programming language, which means that functions generally have no side effects. A distinct construct exists to represent side effects, orthogonal to the type of functions. A pure function can return a side effect that is subsequently executed, modeling the impure functions of other languages.

Haskell has a strong, static type system based on Hindley–Milner type inference. Its principal innovation in this area is type classes, originally conceived as a principled way to add overloading to the language, but since finding many more uses.

The construct that represents side effects is an example of a monad: a general framework which can model various computations such as error handling, nondeterminism, parsing and software transactional memory. They are defined as ordinary datatypes, but Haskell provides some syntactic sugar for their use.

Haskell has an open, published specification, and multiple implementations exist. Its main implementation, the Glasgow Haskell Compiler (GHC), is both an interpreter and native-code compiler that runs on most platforms. GHC is noted for its rich type system incorporating recent innovations such as generalized algebraic data types and type families. The Computer Language Benchmarks Game also highlights its high-performance implementation of concurrency and parallelism.

An active, growing community exists around the language, and more than 5,400 third-party open-source libraries and tools are available in the online package repository *Hackage*.

## Code examples

A "Hello, World!" program in Haskell (only the last line is strictly necessary):

```mw
module Main (main) where          -- not needed in interpreter, is the default in a module file

main :: IO ()                     -- the compiler can infer this type definition
main = putStrLn "Hello, World!"
```

The factorial function in Haskell, defined in a few different ways (the first line is the type annotation, which is optional and is the same for each implementation):

```mw
factorial :: (Integral a) => a -> a

-- Using recursion (with the "ifthenelse" expression)
factorial n = if n < 2
              then 1
              else n * factorial (n - 1)

-- Using recursion (with pattern matching)
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Using recursion (with guards)
factorial n
   | n < 2     = 1
   | otherwise = n * factorial (n - 1)

-- Using a list and the "product" function
factorial n = product [1..n]

-- Using fold (implements "product")
factorial n = foldl (*) 1 [1..n]

-- Point-free style
factorial = foldr (*) 1 . enumFromTo 1
```

Using Haskell's Fixed-point combinator allows this function to be written without any explicit recursion.

```mw
import Data.Function (fix)

factorial = fix fac
  where fac f x 
          | x < 2     = 1
          | otherwise = x * f (x - 1)
```

As the *Integer* type has arbitrary-precision, this code will compute values such as `factorial 100000` (a 456,574-digit number), with no loss of precision.

An implementation of an algorithm similar to quick sort over lists, where the first element is taken as the pivot:

```mw
-- Type annotation (optional, same for each implementation)
quickSort :: Ord a => [a] -> [a]

-- Using list comprehensions
quickSort []     = []                               -- The empty list is already sorted
quickSort (x:xs) = quickSort [a | a <- xs, a < x]   -- Sort the left part of the list
                   ++ [x] ++                        -- Insert pivot between two sorted parts
                   quickSort [a | a <- xs, a >= x]  -- Sort the right part of the list

-- Using filter
quickSort []     = []
quickSort (x:xs) = quickSort (filter (<x) xs)
                   ++ [x] ++
                   quickSort (filter (>=x) xs)
```

## Implementations

All listed implementations are distributed under open source licenses.

Implementations that fully or nearly comply with the Haskell 98 standard include:

- The Glasgow Haskell Compiler (GHC) compiles to native code on many different processor architectures, and to ANSI C, via one of two intermediate languages: C--, or in more recent versions, LLVM (formerly Low Level Virtual Machine) bitcode. GHC has become the *de facto* standard Haskell dialect. There are libraries (e.g., bindings to OpenGL) that work only with GHC. GHC was also distributed with the Haskell platform. GHC features an asynchronous runtime that also schedules threads across multiple CPU cores similar to the Go runtime.
- Jhc, a Haskell compiler written by John Meacham, emphasizes speed and efficiency of generated programs and exploring new program transformations.
  - Ajhc is a fork of Jhc.
- The Utrecht Haskell Compiler (UHC) is a Haskell implementation from Utrecht University. It supports almost all Haskell 98 features plus many experimental extensions. It is implemented using attribute grammars and is primarily used for research on generated type systems and language extensions.

Implementations no longer actively maintained include:

- The Haskell User's Gofer System (Hugs) is a bytecode interpreter. It was once one of the implementations used most widely, alongside the GHC compiler, but has now been mostly replaced by GHCi. It also comes with a graphics library.
- HBC is an early implementation supporting Haskell 1.4. It was implemented by Lennart Augustsson in, and based on, Lazy ML. It has not been actively developed for some time.
- nhc98 is a bytecode compiler focusing on minimizing memory use.
  - The York Haskell Compiler (Yhc) was a fork of nhc98, with the goals of being simpler, more portable and efficient, and integrating support for Hat, the Haskell tracer. It also had a JavaScript backend, allowing users to run Haskell programs in web browsers.

Implementations not fully Haskell 98 compliant, and using a variant Haskell language, include:

- Eta and Frege are dialects of Haskell targeting the Java virtual machine.
- Gofer is an educational dialect of Haskell, with a feature called *constructor classes*, developed by Mark Jones. It is supplanted by Haskell User's Gofer System (Hugs).
- Helium, a newer dialect of Haskell. The focus is on making learning easier via clearer error messages by disabling type classes as a default.

## Notable applications

- Agda is a proof assistant written in Haskell.
- Cabal is a tool for building and packaging Haskell libraries and programs.
- Darcs is a revision control system written in Haskell, with several innovative features, such as more precise control of patches to apply.
- Glasgow Haskell Compiler (GHC) is also often a testbed for advanced functional programming features and optimizations in other programming languages.
- Git-annex is a tool to manage (big) data files under Git version control. It also provides a distributed file synchronization system (git-annex assistant).
- Linspire Linux chose Haskell for system tools development.
- Pandoc is a tool to convert one markup format into another.
- Pugs is a compiler and interpreter for the programming language then named Perl 6, but since renamed Raku.
- TidalCycles is a domain special language for live coding musical patterns, embedded in Haskell.
- Xmonad is a window manager for the X Window System, written fully in Haskell.
- GarganText is a collaborative tool to map through semantic analysis texts on any web browser, written fully in Haskell and PureScript, which is used for instance in the research community to draw up state-of-the-art reports and roadmaps.

### Industry

- Bluespec SystemVerilog (BSV) is a language extension of Haskell, for designing electronics. It is an example of a domain-specific language embedded into Haskell. Further, Bluespec, Inc.'s tools are implemented in Haskell.
- Cryptol, a language and toolchain for developing and verifying cryptography algorithms, is implemented in Haskell.
- Facebook implements its anti-spam programs in Haskell, maintaining the underlying data access library as open-source software.
- The Cardano blockchain platform is implemented in Haskell.
- GitHub implemented Semantic, an open-source library to analyze, diff, and interpret untrusted source code for many languages, in Haskell.
- Standard Chartered's financial modelling language Mu is syntactic Haskell running on a strict runtime.
- seL4, the first formally verified microkernel, used Haskell as a prototyping language for the OS developer. At the same time, the Haskell code defined an executable specification with which to reason, for automatic translation by the theorem-proving tool. The Haskell code thus served as an intermediate prototype before final C refinement.
- Target stores' supply chain optimization software is written in Haskell.
- Co–Star
- Mercury Technologies' back end is written in Haskell.
- Anduril Industries uses Haskell for its Pulsar family of electronic warfare systems.

### Web

Notable web frameworks written for Haskell include:

- IHP
- Servant
- Snap
- Yesod

## Criticism

Jan-Willem Maessen, in 2002, and Simon Peyton Jones, in 2003, discussed problems associated with lazy evaluation while also acknowledging the theoretical motives for it. In addition to purely practical considerations such as improved performance, they note that lazy evaluation makes it more difficult for programmers to reason about the performance of their code (particularly its space use).

Bastiaan Heeren, Daan Leijen, and Arjan van IJzendoorn in 2003 also observed some stumbling blocks for Haskell learners: "The subtle syntax and sophisticated type system of Haskell are a double edged sword—highly appreciated by experienced programmers but also a source of frustration among beginners, since the generality of Haskell often leads to cryptic error messages." To address the error messages researchers from Utrecht University developed an advanced interpreter called Helium, which improved the user-friendliness of error messages by limiting the generality of some Haskell features. In particular it disables type classes by default.

Ben Lippmeier designed Disciple as a strict-by-default (lazy by explicit annotation) dialect of Haskell with a type-and-effect system, to address Haskell's difficulties in reasoning about lazy evaluation and in using traditional data structures such as mutable arrays. He argues (p. 20) that "destructive update furnishes the programmer with two important and powerful tools ... a set of efficient array-like data structures for managing collections of objects, and ... the ability to broadcast a new value to all parts of a program with minimal burden on the programmer."

Robert Harper, one of the authors of Standard ML, has given his reasons for not using Haskell to teach introductory programming. Among these are the difficulty of reasoning about resource use with non-strict evaluation, that lazy evaluation complicates the definition of datatypes and inductive reasoning, and the "inferiority" of Haskell's (old) class system compared to ML's module system.

Haskell's build tool, Cabal, has historically been criticized for poorly handling multiple versions of the same library, a problem known as "Cabal hell". The Stackage server and Stack build tool were made in response to these criticisms. Cabal has since addressed this problem by borrowing ideas from the package manager Nix, with the new approach becoming the default in 2019.

Clean is a close, slightly older relative of Haskell. Its biggest deviation from Haskell is in the use of uniqueness types instead of monads for input/output (I/O) and side effects.

A series of languages inspired by Haskell, but with different type systems, have been developed, including:

- Agda, a functional language with dependent types.
- Cayenne, with dependent types.
- Elm, a functional language to create web front-end apps, no support for user-defined or higher-kinded type classes or instances.
- Epigram, a functional language with dependent types suitable for proving properties of programs.
- Idris, a general purpose functional language with dependent types, developed at the University of St Andrews.
- PureScript transpiles to JavaScript.
- Ωmega, a strict language that allows introduction of new kinds, and programming at the type level.

Other related languages include:

- Curry, a functional/logic programming language based on Haskell.

Notable Haskell variants include:

- Generic Haskell, a version of Haskell with type system support for generic programming.
- Hume, a strict functional language for embedded systems based on processes as stateless automata over a sort of tuples of one element mailbox channels where the state is kept by feedback into the mailboxes, and a mapping description from outputs to channels as box wiring, with a Haskell-like expression language and syntax.

## Conferences and workshops

Haskell events have been regularly held concurrent with the International Conference on Functional Programming (ICFP) including workshops such as the Haskell Symposium (formerly the Haskell Workshop) and Commercial Users of Functional Programming. Other events include the Haskell Implementors Workshop, ZuriHac in Zurich, and Hac: The Haskell Hackathon.

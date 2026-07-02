---
title: "Fortress (programming language)"
source: https://en.wikipedia.org/wiki/Fortress_(programming_language)
domain: fortress-language
license: CC-BY-SA-4.0
tags: fortress language, sun microsystems, guy steele, high performance computing, parallel computing
fetched: 2026-07-02
---

# Fortress (programming language)

**Fortress** is a discontinued experimental programming language for high-performance computing, created by Sun Microsystems with funding from The Defense Advanced Research Projects Agency's (DARPA) High Productivity Computing Systems project. One of the language designers was Guy L. Steele Jr., whose prior work includes Scheme, Common Lisp, and Java.

## Design

The name *Fortress* was intended to connote a secure Fortran, i.e., "a language for high-performance computation that provides abstraction and type safety on par with modern programming language principles." Language features included implicit parallelism, Unicode support and concrete syntax similar to mathematical notation. The language was not designed to be similar to Fortran. Syntactically, it most resembles Scala, Standard ML, and Haskell. Fortress was designed from the outset to have multiple syntactic stylesheets. Source code can be rendered as ASCII text, in Unicode, or as a prettied image. This would allow for support of mathematical symbols and other symbols in the rendered output for easier reading. An emacs-based tool named *fortify* transforms ASCII-based Fortress source code into LaTeX output.

Fortress was also designed to be both highly parallel and have rich functionality contained within libraries, drawing from Java. For example, the `for` loop construct was a parallel operation, which would not necessarily iterate in a strictly linear manner, depending on the underlying implementation. However, the `for` construct was a library function and could be replaced by another version of the programmer's liking rather than being built into the language.

Fortress' designers made its syntax as close as possible to pseudocode and analyzed hundreds of computer science and mathematics papers, courses, books and journals using pseudocode to extract the common usage patterns of the English language and standard mathematical notation when used to represent algorithms in pseudocode. Then they made the compiler trying to maintain a one-to-one correspondence between pseudocode and executable Fortress.

## History

Fortress was one of three languages created with funding from the High Productivity Computing Systems project; the others were X10 from IBM and Chapel from Cray, Inc. In November 2006, when DARPA approved funding for the third phase of the HPCS project, X10 and Chapel were funded, but Fortress was not, leading to uncertainty about the future of Fortress.

In January 2007, Fortress was released as open-source. Version 1.0 of the Fortress Language Specification was released in April 2008, along with a compliant implementation targeting the Java virtual machine.

In July 2012, Steele announced that active development on Fortress would cease after a brief winding-down period, citing complications with using Fortress's type system on existing virtual machines.

## Example: Hello world!

This is the Fortress version of the archetypal "Hello, World!" program, as presented in the *Fortress Reference Card*:

```
component hello
export Executable
run() = println("Hello, World!")
end
```

The *export* statement makes the program executable and every executable program in Fortress must implement the *run()* function. The file where the program is saved for compilation must have the same name as the one specified in the initial *component* statement. The *println()* function is what outputs the "Hello, World!" words on the screen.

---
title: "Metaprogramming"
source: https://en.wikipedia.org/wiki/Metaprogramming
domain: hy-lisp
license: CC-BY-SA-4.0
tags: hy language, lisp language, python language, abstract syntax tree, macro computer science
fetched: 2026-07-02
---

# Metaprogramming

**Metaprogramming** is a computer programming technique in which computer programs have the ability to treat other programs as their data. It means that a program can be designed to read, generate, analyse, or transform other programs, and even modify itself, while running. In some cases, this allows programmers to minimize the number of lines of code to express a solution, in turn reducing development time. It also allows programs more flexibility to efficiently handle new situations with no recompiling.

Metaprogramming can be used to move computations from runtime to compile time, to generate code using compile time computations, and to enable self-modifying code. The ability of a programming language to be its own metalanguage allows reflective programming, and is termed *reflection*. Reflection is a valuable language feature to facilitate metaprogramming.

Metaprogramming was popular in the 1970s and 1980s using list processing languages such as Lisp. Lisp machine hardware gained some notice in the 1980s, and enabled applications that could process code. They were often used for artificial intelligence applications.

## Approaches

Metaprogramming enables developers to write programs and develop code that falls under the generic programming paradigm. Having the programming language itself as a first-class data type (as in Lisp, Prolog, SNOBOL, or Rebol) is also very useful; this is known as *homoiconicity*. Generic programming invokes a metaprogramming facility within a language by allowing one to write code without the concern of specifying data types since they can be supplied as parameters when used.

Metaprogramming usually works in one of three ways.

1. The first approach is to expose the internals of the runtime system (engine) to the programming code through application programming interfaces (APIs) like that for the .NET Common Intermediate Language (CIL) emitter.
2. The second approach is dynamic execution of expressions that contain programming commands, often composed from strings, but can also be from other methods using arguments or context, like JavaScript. Thus, "programs can write programs." Although both approaches can be used in the same language, most languages tend to lean toward one or the other.
3. The third approach is to step outside the language entirely. General purpose program transformation systems such as compilers, which accept language descriptions and carry out arbitrary transformations on those languages, are direct implementations of general metaprogramming. This allows metaprogramming to be applied to virtually any target language without regard to whether that target language has any metaprogramming abilities of its own. One can see this at work with Scheme and how it allows tackling some limits faced in C by using constructs that are part of the Scheme language to extend C.

Lisp is probably the quintessential language with metaprogramming facilities, both because of its historical precedence and because of the simplicity and power of its metaprogramming. In Lisp metaprogramming, the unquote operator (typically a comma) introduces code that is evaluated at program definition time rather than at run time. The metaprogramming language is thus identical to the host programming language, and existing Lisp routines can be directly reused for metaprogramming if desired. This approach has been implemented in other languages by incorporating an interpreter in the program, which works directly with the program's data. There are implementations of this kind for some common high-level languages, such as RemObjects’ Pascal Script for Object Pascal.

## Usages

### Code generation

A simple example of a metaprogram is this POSIX Shell script, which is an example of generative programming:

```mw
#!/bin/sh
# metaprogram
echo '#!/bin/sh' > program
for i in $(seq 992)
do
    echo "echo $i" >> program
done
chmod +x program
```

This script (or program) generates a new 993-line program that prints out the numbers 1–992. This is only an illustration of how to use code to write more code; it is not the most efficient way to print out a list of numbers. Nonetheless, a programmer can write and execute this metaprogram in less than a minute, and will have generated over 1000 lines of code in that amount of time.

A quine is a special kind of metaprogram that produces its own source code as its output. Quines are generally of recreational or theoretical interest only.

Not all metaprogramming involves generative programming. If programs are modifiable at runtime, or if incremental compiling is available (such as in C#, Forth, Frink, Groovy, JavaScript, Lisp, Elixir, Lua, Nim, Perl, PHP, Python, Rebol, Ruby, Rust, R, SAS, Smalltalk, and Tcl), then techniques can be used to perform metaprogramming without generating source code.

One style of generative approach is to employ domain-specific languages (DSLs). A fairly common example of using DSLs involves generative metaprogramming: lex and yacc, two tools used to generate lexical analysers and parsers, let the user describe the language using regular expressions and context-free grammars, and embed the complex algorithms required to efficiently parse the language.

### Code instrumentation

One usage of metaprogramming is to instrument programs in order to do dynamic program analysis.

## Challenges

Some argue that there is a sharp learning curve to make complete use of metaprogramming features. Since metaprogramming gives more flexibility and configurability at runtime, misuse or incorrect use of metaprogramming can result in unwarranted and unexpected errors that can be extremely difficult to debug to an average developer. It can introduce risks in the system and make it more vulnerable if not used with care. Some of the common problems, which can occur due to wrong use of metaprogramming are inability of the compiler to identify missing configuration parameters, invalid or incorrect data can result in unknown exception or different results. Due to this, some believe that only high-skilled developers should work on developing features which exercise metaprogramming in a language or platform and average developers must learn how to use these features as part of convention.

## Uses in programming languages

### Macro systems

- Lisp, most dialects
  - Clojure
  - Common Lisp
  - Racket
  - Scheme hygienic macros
- MacroML
- Template Haskell
- Scala
- Nim
- Rust
- Haxe
- Julia
- Elixir

### Macro assemblers

The IBM/360 and derivatives had powerful macro assembler facilities that were often used to generate complete assembly language programs or sections of programs (for different operating systems for instance). Macros provided with CICS transaction processing system had assembler macros that generated COBOL statements as a pre-processing step.

Other assemblers, such as MASM, also support macros.

### Metaclasses

Metaclasses are provided by the following programming languages:

- Common Lisp
- Python
- NIL
- Groovy
- Ruby
- Smalltalk
- Lua

### Template metaprogramming

- C, using X Macros
- C++, using templates
- D
- Common Lisp, Scheme and most Lisp dialects by using the quasiquote ("backquote") operator.
- Nim

### Staged metaprogramming

- MetaML
- MetaOCaml
- Scala natively or using the Lightweight Modular Staging Framework
- Terra

### Dependent types

Use of dependent types allows proving that generated code is never invalid. However, this approach is leading-edge and rarely found outside of research programming languages.

## Implementations

The list of notable metaprogramming systems is maintained at List of program transformation systems.

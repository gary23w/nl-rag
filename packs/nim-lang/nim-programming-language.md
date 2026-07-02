---
title: "Nim (programming language)"
source: https://en.wikipedia.org/wiki/Nim_(programming_language)
domain: nim-lang
license: CC-BY-SA-4.0
tags: nim language, nim lang, nimble, nim compiler
fetched: 2026-07-02
---

# Nim (programming language)

**Nim** is a general-purpose, multi-paradigm, statically typed, compiled, high-level system programming language. It was designed and developed by a team led by Andreas Rumpf. Nim aims to be "efficient, expressive, and elegant", and supports metaprogramming, functional, message passing, procedural, and object-oriented programming paradigms. Nim includes features such as compile-time code generation, algebraic data types, and a foreign function interface (FFI) for interfacing with C, C++, Objective-C, and JavaScript. It also supports compilation to these same languages as intermediate representations.

## Description

Nim is statically typed. It supports compile-time metaprogramming features such as syntactic macros and term rewriting macros. Term rewriting macros enable library implementations of common data structures, such as bignums and matrices, to be implemented efficiently and with syntactic integration, as if they were built-in language facilities. Iterators are supported and can be used as first class entities, as can functions, allowing for the use of functional programming methods. Object-oriented programming is supported by inheritance and multiple dispatch. Functions can be generic and overloaded, and generics are further enhanced by Nim's support for type classes. Operator overloading is also supported. Nim includes multiple tunable memory management strategies, including tracing garbage collection, reference counting, and fully manual systems, with the default being deterministic reference counting with optimizations via move semantics and cycle collection via trial deletion.

> [Nim] ... presents a most original design that straddles Pascal and Python and compiles to C code or JavaScript.

— Andrew Binstock, editor-in-chief of Dr. Dobb's Journal, 2014

As of August 2023, Nim compiles to C, C++, JavaScript, Objective-C, and LLVM.

## History

| Branch | Version | Release date |
|---|---|---|
| 0.x | Unsupported: 0.10.2 | 2014-12-29 |
| Unsupported: 0.11.2 | 2015-05-04 |   |
| Unsupported: 0.12.0 | 2015-10-27 |   |
| Unsupported: 0.13.0 | 2016-01-18 |   |
| Unsupported: 0.14.2 | 2016-06-09 |   |
| Unsupported: 0.15.2 | 2016-10-23 |   |
| Unsupported: 0.16.0 | 2017-01-08 |   |
| Unsupported: 0.17.2 | 2017-09-07 |   |
| Unsupported: 0.18.0 | 2018-03-01 |   |
| Unsupported: 0.19.6 | 2019-05-13 |   |
| Unsupported: 0.20.2 | 2019-06-17 |   |
| 1.0 | Unsupported: 1.0.0 | 2019-09-23 |
| Unsupported: 1.0.10 | 2020-10-27 |   |
| 1.2 | Unsupported: 1.2.0 | 2020-04-03 |
| Unsupported: 1.2.18 | 2022-02-09 |   |
| 1.4 | Unsupported: 1.4.0 | 2020-10-16 |
| Unsupported: 1.4.8 | 2021-05-25 |   |
| 1.6 | Unsupported: 1.6.0 | 2021-10-19 |
| Unsupported: 1.6.20 | 2024-04-16 |   |
| 2.0 | Unsupported: 2.0.0 | 2023-08-01 |
| Supported: 2.0.16 | 2025-04-22 |   |
| 2.2 | Unsupported: 2.2.0 | 2024-10-02 |
| Latest version: 2.2.10 | 2026-04-24 |   |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |
| For each 0.x branch, only the latest point release is listed. For later branches, the first and the latest point release is listed. |   |   |

Andreas Rumpf is the designer and original implementer of Nim. He received a diploma in computer science from the Technical University of Kaiserslautern, Germany. His research interests include hard real-time systems, embedded systems, compiler construction and artificial intelligence.

Nim's initial development was started in 2005 under the name *Nimrod* and was made public in 2008.

The first version of the Nim compiler was written in Pascal using the Free Pascal compiler. In 2008, a version of the compiler written in Nim was released. The compiler is free and open-source software, and is being developed by a community of volunteers working with Andreas Rumpf. The language was officially renamed from *Nimrod* to *Nim* with the release of version 0.10.2 in December 2014. On 23 September 2019, version 1.0 of Nim was released, signifying the maturing of the language and its toolchain. On 1 August 2023, version 2.0 of Nim was released, signifying the completion, stabilization of, and switch to the ARC/ORC memory model.

## Language design

### Syntax

The syntax of Nim resembles that of Python. Code blocks and nesting statements are identified through use of whitespace, according to the offside-rule. Many keywords are identical to their Python equivalents, which are mostly English keywords, whereas other programming languages usually use punctuation. With the goal of improving upon its influence languages, even though Nim supports indentation-based syntax like Python, it introduced additional flexibility. For example, a single statement may span multiple lines if a comma or binary operator is at the end of each line. Nim also supports user-defined operators.

Unlike Python, Nim implements (native) static typing. Nim's type system allows for easy type conversion, casting, and provides syntax for generic programming. Nim notably provides type classes which can stand in for multiple types, and provides several such type classes 'out of the box'. Type classes allow working with several types as if they were a single type. For example:

- `openarray` – Represents arrays of different sizes, sequences, and strings
- `SomeSignedInt` – Represents all the signed integer types
- `SomeInteger` – Represents all the Integer types, signed or not
- `SomeOrdinal` – Represents all the basic countable and ordered types, except of non integer number

This code sample demonstrates the use of typeclasses in Nim:

```mw
# Let's declare a function that takes any type of number and displays its double
# In Nim functions with side effect are called "proc"
proc timesTwo(i: SomeNumber) =
  echo i * 2
```

```mw
# Let's write another function that takes any ordinal type, and returns
# the double of the input in its original type, if it is a number;
# or returns the input itself otherwise.
# We use a generic Type(T), and precise that it can only be an Ordinal
func twiceIfIsNumber[T: SomeOrdinal](i: T): T =
  when T is SomeNumber: # A `when` is an `if` evaluated during compile time
    result = i * 2 # You can also write `return i * 2`
  else:
    # If the Ordinal is not a number it is converted to int,
    # multiplied by two, and reconverted to its based type
    result = (i.int * 2).T
```

```mw
echo twiceIfIsNumber(67) # Passes an int to the function
echo twiceIfIsNumber(67u8) # Passes an uint8
echo twiceIfIsNumber(true) # Passes a bool (Which is also an Ordinal)
```

### Influence

According to the language creator, Nim was conceived to combine the best parts of Ada typing system, Python flexibility, and powerful Lisp macro system.

Nim was influenced by specific characteristics of existing languages, including the following:

- Modula-3: traced vs untraced pointers
- Object Pascal: type safe bit sets (*set of char*), case statement syntax, various type names and filenames in the standard library
- Ada: subrange types, distinct type, safe variants – case objects
- C++: operator overloading, generic programming
- Python: Off-side rule
- Lisp: Macro system, AST manipulation, homoiconicity
- Oberon: export marker
- C#: async/await, lambda macros
- ParaSail: pointer-free programming

### Uniform function call syntax

Nim supports uniform function call syntax (UFCS) and identifier equality, which provides a large degree of flexibility in use.

For example, each of these lines print "hello world", just with different syntax:

```mw
echo "hello world"
echo("hello world")
"hello world".echo()
"hello world".echo
echo("hello", " world")
"hello".echo(" world")
"hello".echo " world"
```

### Identifier equality

Nim is almost fully style-insensitive; two identifiers are considered equal if they only differ by capitalization and underscores, as long as the first characters are identical. This is to enable a mixture of styles across libraries: one user can write a library using snake_case as a convention, and it can be used by a different user in a camelCase style without issue.

```mw
const useHttps = true
assert useHttps == useHttps
assert useHTTPS == useHttps
assert use_https == useHttps
```

### Stropping

The stropping feature allows the use of any name for variables or functions, even when the names are reserved words for keywords. An example of stropping is the ability to define a variable named `if`, without clashing with the keyword `if`. Nim's implementation of this is achieved via backticks, allowing any reserved word to be used as an identifier.

```mw
type Type = object
  `int`: int

let `object` = Type(`int`: 9)
assert `object` is Type
assert `object`.`int` == 9

var `var` = 42
let `let` = 8
assert `var` + `let` == 50

const `assert` = true
assert `assert`
```

## Compiler

The Nim compiler emits fast, optimized C code by default. It defers compiling-to-object code to an external C compiler to leverage existing compiler optimization and portability. Many C compilers are supported, including Clang, Microsoft Visual C++ (MSVC), MinGW, and GNU Compiler Collection (GCC). The Nim compiler can also emit C++, Objective-C, and JavaScript code to allow easy interfacing with application programming interfaces (APIs) written in those languages; developers can simply write in Nim, then compile to any supported language. This also allows writing applications for iOS and Android. There is also an unofficial LLVM backend, allowing use of the Nim compiler in a stand-alone way.

The Nim compiler is self-hosting, meaning it is written in the Nim language. The compiler supports cross-compiling, so it is able to compile software for any of the supported operating systems, no matter the development machine. This is useful for compiling applications for embedded systems, and for uncommon and obscure computer architectures.

### Compiler options

By default, the Nim compiler creates a *debug* build. With the option `-d:release` a *release* build can be created, which is optimized for speed and contains fewer runtime checks. With the option `-d:danger` all runtime checks can be disabled, if maximum speed is desired.

### Memory management

Nim supports multiple memory management strategies, including the following:

- `--mm:arc` – Automatic reference counting (ARC) with move semantics optimizations, offers a shared heap. It offers fully deterministic performance for hard realtime systems. Reference cycles may cause memory leaks: these may be dealt with by manually annotating `{.acyclic.}` pragmas or by using `--mm:orc`.
- `--mm:orc` – Same as `--mm:arc` but adds a cycle collector (the "O") based on "trial deletion". The cycle collector only analyzes types if they are potentially cyclic.
- `--mm:refc` – Standard deferred reference counting based garbage collector with a simple mark-and-sweep backup GC in order to collect cycles. Heaps are thread-local.
- `--mm:markAndSweep` – Simple mark-and-sweep based garbage collector. Heaps are thread-local.
- `--mm:boehm` – Boehm based garbage collector, it offers a shared heap.
- `--mm:go` – Go's garbage collector, useful for interoperability with Go. Offers a shared heap.
- `--mm:none` – No memory management strategy nor a garbage collector. Allocated memory is simply never freed, unless manually freed by the developer's code.

As of Nim 2.0, ORC is the default GC.

## Development tools

### Bundled

Many tools are bundled with the Nim install package, including:

#### Nimble

Nimble is the standard package manager used by Nim to package Nim modules. It was initially developed by Dominik Picheta, who is also a core Nim developer. Nimble has been included as Nim's official package manager since 27 October 2015, the v0.12.0 release.

Nimble packages are defined by `.nimble` files, which contain information about the package version, author, license, description, dependencies, and more. These files support a limited subset of the Nim syntax called NimScript, with the main limitation being the access to the FFI. These scripts allow changing of test procedure, or for custom tasks to be written.

The list of packages is stored in a JavaScript Object Notation (JSON) file which is freely accessible in the nim-lang/packages repository on GitHub. This JSON file provides Nimble with a mapping between the names of packages and their Git or Mercurial repository URLs.

Nimble comes with the Nim compiler. Thus, it is possible to test the Nimble environment by running: `nimble -v`. This command will reveal the version number, compiling date and time, and Git hash of nimble. Nimble uses the Git package, which must be available for Nimble to function properly. The Nimble command-line is used as an interface for installing, removing (uninstalling), and upgrading–patching module packages.

#### c2nim

c2nim is a source-to-source compiler (transcompiler or transpiler) meant to be used on C/C++ headers to help generate new Nim bindings. The output is human-readable Nim code that is meant to be edited by hand after the translation process.

#### koch

koch is a maintenance script that is used to build Nim, and provide HTML documentation.

#### nimgrep

nimgrep is a generic tool for manipulating text. It is used to search for regex, peg patterns, and contents of directories, and it can be used to replace tasks. It is included to assist with searching Nim's style-insensitive identifiers.

#### nimsuggest

nimsuggest is a tool that helps any source code editor query a `.nim` source file to obtain useful information like definition of symbols or suggestions for completions.

#### niminst

niminst is a tool to generate an installer for a Nim program. It creates .msi installers for Windows via Inno Setup, and install and uninstall scripts for Linux, macOS, and Berkeley Software Distribution (BSD).

#### nimpretty

nimpretty is a source code beautifier, used to format code according to the official Nim style guide.

#### Testament

Testament is an advanced automatic unit tests runner for Nim tests. Used in developing Nim, it offers process isolation tests, generates statistics about test cases, supports multiple targets and simulated Dry-Runs, has logging, can generate HTML reports, can skip tests from a file, and more.

### Other notable tools

Some notable tools not included in the Nim distribution include:

#### choosenim

choosenim was developed by Dominik Picheta, creator of the Nimble package manager, as a tool to enable installing and using multiple versions of the Nim compiler. It downloads any Nim stable or development compiler version from the command line, enabling easy switching between them.

#### nimpy

nimpy is a library that enables convenient Python integration in Nim programs.

#### pixie

pixie is a feature-rich 2D graphics library, similar to Cairo or the Skia. It uses SIMD acceleration to speed-up image manipulation drastically. It supports many image formats, blending, masking, blurring, and can be combined with the boxy library to do hardware accelerated rendering.

#### nimterop

nimterop is a tool focused on automating the creation of C/C++ wrappers needed for Nim's foreign function interface.

## Libraries

### Pure/impure libraries

Pure libraries are modules written in Nim only. They include no wrappers to access libraries written in other programming languages.

Impure libraries are modules of Nim code which depend on external libraries that are written in other programming languages such as C.

### Standard library

The Nim standard library includes modules for all basic tasks, including:

- System and core modules
- Collections and algorithms
- String handling
- Time handling
- Generic Operating System Services
- Math libraries
- Internet Protocols and Support
- Threading
- Parsers
- Docutils
- XML Processing
- XML and HTML code generator
- Hashing
- Database support (PostgreSQL, MySQL and SQLite)
- Wrappers (Win32 API, POSIX)

### Use of other libraries

A Nim program can use any library which can be used in a C, C++, or JavaScript program. Language bindings exist for many libraries, including GTK, Qt QML, wxWidgets, SDL 2, Raylib, Godot, UE5, Cairo, OpenGL, Vulkan, Windows API (WinAPI), zlib, libzip, OpenSSL and cURL. Nim works with databases PostgreSQL, MySQL, and SQLite.

Open source tools exist, of various degrees of support, that can be used to interface Nim with the languages Lua, Julia, Rust, C#, and Python, or transpile Nim to TypeScript.

## Examples

### Hello world

The "Hello, World!" program in Nim:

```mw
echo("Hello, World!")
# Procedures can be called with no parentheses
echo "Hello, World!"
```

Another version of "Hello World" can be accomplished by calling the `write` function with the `stdout` stream:

```mw
stdout.write("Hello, World!\n")
write(stdout, "Hello, World!\n")
```

### Fibonacci

Several implementations of the Fibonacci function, showcasing implicit returns, default parameters, iterators, recursion, and while loops:

```mw
proc fib(n: Natural): Natural =
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)
    
func fib2(n: int, a = 0, b = 1): int =
  if n == 0: a else: fib2(n-1, b, a+b)
  
iterator fib3: int =
  var a = 0
  var b = 1
  while true:
    yield a
    swap a, b
    b += a
```

### Factorial

Program to calculate the factorial of a positive integer using the iterative approach, showcasing try/catch error handling and for loops:

```mw
import std/strutils

var n = 0
try:
  stdout.write "Input positive integer number: "
  n = stdin.readline.parseInt
except ValueError:
  raise newException(ValueError, "You must enter a positive number")

var fact = 1
for i in 2..n:
  fact = fact * i

echo fact
```

Using the module math from Nim's standard library:

```mw
import std/math
echo fac(x)
```

### Reversing a string

A simple demonstration showing the implicit result variable and the use of iterators.

```mw
proc reverse(s: string): string =
  for i in countdown(s.high, 0):
    result.add s[i]

let str1 = "Reverse This!"
echo "Reversed: ", reverse(str1)
```

One of Nim's more exotic features is the implicit `result` variable. Every procedure in Nim with a non-void return type has an implicit result variable that represents the value to be returned. In the for loop we see an invocation of `countdown` which is an iterator. If an iterator is omitted, the compiler will attempt to use an `items` iterator, if one is defined for the type specified.

### Graphical user interface

Using GTK 3 with GObject introspection through the gintro module:

```mw
import gintro/[gtk, glib, gobject, gio]

proc appActivate(app: Application) =
  let window = newApplicationWindow(app)
  window.title = "GTK3 application with gobject introspection"
  window.defaultSize = (400, 400)
  showAll(window)

proc main =
  let app = newApplication("org.gtk.example")
  connect(app, "activate", appActivate)
  discard run(app)

main()
```

This code requires the gintro module to work, which is not part of the standard library. To install the module gintro and many others you can use the tool nimble, which comes as part of Nim. To install the gintro module with nimble you do the following:

```
nimble install gintro
```

## Programming paradigms

### Functional programming

Functional programming is supported in Nim through first-class functions and code without side effects via the `noSideEffect` pragma or the `func` keyword. Nim will perform side effect analysis and raise compiling errors for code that does not obey the contract of producing no side effects when compiled with the experimental feature `strictFuncs`, planned to become the default in later versions.

Contrary to purely functional programming languages, Nim is a multi-paradigm programming language, so functional programming restrictions are opt-in on a function-by-function basis.

#### First-class functions

Nim supports first-class functions by allowing functions to be stored in variables or passed anonymously as parameters to be invoked by other functions. The `std/sugar` module provides syntactic sugar for anonymous functions in type declarations and instantiation.

```mw
import std/[sequtils, sugar]

let powersOfTwo = @[1, 2, 4, 8, 16, 32, 64, 128, 256]

proc filter[T](s: openArray[T], pred: T -> bool): seq[T] =
  result = newSeq[T]()
  for i in 0 ..< s.len:
    if pred(s[i]):
      result.add(s[i])

echo powersOfTwo.filter(proc (x: int): bool = x > 32)
# syntactic sugar for the above, provided as a macro from std/sugar
echo powersOfTwo.filter(x => x > 32)

proc greaterThan32(x: int): bool = x > 32
echo powersOfTwo.filter(greaterThan32)
```

#### Side effects

Side effects of functions annotated with the `noSideEffect` pragma are checked, and the compiler will refuse to compile functions failing to meet those. Side effects in Nim include mutation, global state access or modification, asynchronous code, threaded code, and IO. Mutation of parameters may occur for functions taking parameters of `var` or `ref` type: this is expected to fail to compile with the currently-experimental `strictFuncs` in the future. The `func` keyword introduces a shortcut for a `noSideEffect` pragma.

```mw
func binarySearch[T](a: openArray[T]; elem: T): int
is short for...
proc binarySearch[T](a: openArray[T]; elem: T): int {.noSideEffect.}

{.experimental: "strictFuncs".}

type
  Node = ref object
    le, ri: Node
    data: string

func len(n: Node): int =
  # valid: len does not have side effects
  var it = n
  while it != nil:
    inc result
    it = it.ri

func mut(n: Node) =
  let m = n # is the statement that connected the mutation to the parameter
  m.data = "yeah" # the mutation is here
  # Error: 'mut' can have side effects
  # an object reachable from 'n' is potentially mutated
```

#### Function composition

Uniform function call syntax allows the chaining of arbitrary functions, perhaps best exemplified with the `std/sequtils` library.

```mw
import std/[sequtils, sugar]

let numbers = @[1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
# a and b are special identifiers in the foldr macro
echo numbers.filter(x => x > 3).deduplicate.foldr(a + b) # 30
```

#### Algebraic data types and pattern matching

Nim has support for product types via the `object` type, and for sum types via object variants: raw representations of tagged unions, with an enumerated type tag that must be safely matched upon before fields of variants can be accessed. These types can be composed algebraically. Structural pattern matching is available, but relegated to macros in various third-party libraries.

```mw
import std/tables

type
  Value = uint64
  Ident = string
  ExprKind = enum
    Literal, Variable, Abstraction, Application
  Expr = ref object
    case kind: ExprKind
    of Literal:
      litIdent: Value
    of Variable:
      varIdent: Ident
    of Abstraction:
      paramAbs: Ident
      funcAbs: Expr
    of Application:
      funcApp, argApp: Expr

func eval(expr: Expr, context: var Table[Ident, Value]): Value =
  case expr.kind
  of Literal:
    return expr.litIdent
  of Variable:
    return context[expr.varIdent]
  of Application:
    case expr.funcApp.kind
    of Abstraction:
      context[expr.funcApp.paramAbs] = expr.argApp.eval(context)
      return expr.funcAbs.eval(context)
    else:
      raise newException(ValueError, "Invalid expression!")
  else:
    raise newException(ValueError, "Invalid expression!")
```

### Object-oriented programming

Despite being primarily an imperative and functional language, Nim supports various features for enabling object-oriented paradigms.

#### Subtyping and inheritance

Nim supports limited inheritance by use of `ref objects` and the `of` keyword. To enable inheritance, any initial ("root") object must inherit from `RootObj`. Inheritance is of limited use within idiomatic Nim code: with the notable exception of Exceptions.

```mw
type Animal = ref object of RootObj
  name: string
  age: int
type Dog = ref object of Animal
type Cat = ref object of Animal

var animals: seq[Animal] = @[]
animals.add(Dog(name: "Sparky", age: 10))
animals.add(Cat(name: "Mitten", age: 10))

for a in animals:
  assert a of Animal
```

Subtyping relations can also be queried with the `of` keyword.

#### Method calls and encapsulation

Nim's uniform function call syntax enables calling ordinary functions with syntax similar to method call invocations in other programming languages. This is functional for "getters": and Nim also provides syntax for the creation of such "setters" as well. Objects may be made public on a per-field basis, providing for encapsulation.

```mw
type Socket* = ref object
  host: int # private, lacks export marker

# getter of host address
proc host*(s: Socket): int = s.host

# setter of host address
proc `host=`*(s: var Socket, value: int) =
  s.host = value

var s: Socket
new s
assert s.host == 0  # same as host(s), s.host()
s.host = 34         # same as `host=`(s, 34)
```

#### Dynamic dispatch

Static dispatch is preferred, more performant, and standard even among method-looking routines. Nonetheless, if dynamic dispatch is so desired, Nim provides the `method` keyword for enabling dynamic dispatch on reference types.

```mw
import std/strformat

type
  Person = ref object of RootObj
    name: string
  Student = ref object of Person
  Teacher = ref object of Person

method introduce(a: Person) =
  raise newException(CatchableError, "Method without implementation override")

method introduce(a: Student) =
  echo &"I am a student named {a.name}!"

method introduce(a: Teacher) =
  echo &"I am a teacher named {a.name}!"
  
let people: seq[Person] = @[Teacher(name: "Alice"), Student(name: "Bob")]
for person in people:
  person.introduce()
```

### Metaprogramming

#### Templates

Nim supports simple substitution on the abstract syntax tree via its templates.

```mw
template genType(name, fieldname: untyped, fieldtype: typedesc) =
  type
    name = object
      fieldname: fieldtype

genType(Test, foo, int)

var x = Test(foo: 4566)
echo(x.foo) # 4566
```

The `genType` is invoked at compile-time and a `Test` type is created.

#### Generics

Nim supports both constrained and unconstrained generic programming. Generics may be used in procedures, templates and macros. Unconstrained generic identifiers (`T` in this example) are defined after the routine's name in square brackets. Constrained generics can be placed on generic identifiers, or directly on parameters.

```mw
proc addThese[T](a, b: T): T = a + b
echo addThese(1, 2) # 3 (of int type)
echo addThese(uint8 1, uint8 2) # 3 (of uint8 type)

# we don't want to risk subtracting unsigned numbers!
proc subtractThese[T: SomeSignedInt | float](a, b: T): T = a - b
echo subtractThese(1, 2) # -1 (of int type)

import std/sequtils

# constrained generics can also be directly on the parameters
proc compareThese[T](a, b: string | seq[T]): bool =
  for (i, j) in zip(a, b):
    if i != j:
      return false
```

One can further clarify which types the procedure will accept by specifying a type class (in the example above, `SomeSignedInt`).

#### Macros

Macros can rewrite parts of the code at compile-time. Nim macros are powerful and can operate on the abstract syntax tree before or after semantic checking.

Here's a simple example that creates a macro to call code twice:

```mw
import std/macros

macro twice(arg: untyped): untyped =
  result = quote do:
    `arg`
    `arg`

twice echo "Hello world!"
```

The `twice` macro in this example takes the echo statement in the form of an abstract syntax tree as input. In this example we decided to return this syntax tree without any manipulations applied to it. But we do it twice, hence the name of the macro. The result is that the code gets rewritten by the macro to look like the following code at compile time:

```mw
echo "Hello world!"
echo "Hello world!"
```

### Foreign function interface (FFI)

Nim's FFI is used to call functions written in the other programming languages that it can compile to. This means that libraries written in C, C++, Objective-C, and JavaScript can be used in the Nim source code. One should be aware that both JavaScript and C, C++, or Objective-C libraries cannot be combined in the same program, as they are not as compatible with JavaScript as they are with each other. Both C++ and Objective-C are based on and compatible with C, but JavaScript is incompatible, as a dynamic, client-side web-based language.

The following program shows the ease with which external C code can be used directly in Nim.

```mw
proc printf(formatstr: cstring) {.header: "<stdio.h>", varargs.}

printf("%s %d\n", "foo", 5)
```

In this code the `printf` function is imported into Nim and then used.

Basic example using 'console.log' directly for the JavaScript compiling target:

```mw
proc log(args: any) {.importjs: "console.log(@)", varargs.}
log(42, "z", true, 3.14)
```

The JavaScript code produced by the Nim compiler can be executed with Node.js or a web browser.

### Parallelism

To activate threading support in Nim, a program should be compiled with `--threads:on` command line argument. Each thread has a separate garbage collected heap and sharing of memory is restricted, which helps with efficiency and stops race conditions by the threads.

```mw
import std/locks

var
  thr: array[0..4, Thread[tuple[a,b: int]]]
  L: Lock

proc threadFunc(interval: tuple[a,b: int]) {.thread.} =
  for i in interval.a..interval.b:
    acquire(L) # lock stdout
    echo i
    release(L)

initLock(L)

for i in 0..high(thr):
  createThread(thr[i], threadFunc, (i*10, i*10+5))
joinThreads(thr)
```

Nim also has a `channels` module that simplifies passing data between threads.

```mw
import std/os

type
  CalculationTask = object
    id*: int
    data*: int

  CalculationResult = object
    id*: int
    result*: int

var task_queue: Channel[CalculationTask]
var result_queue: Channel[CalculationResult]

proc workerFunc() {.thread.} =
  result_queue.open()

  while true:
    var task = task_queue.recv()
    result_queue.send(CalculationResult(id: task.id, result: task.data * 2))

var workerThread: Thread[void]
createThread(workerThread, workerFunc)

task_queue.open()
task_queue.send(CalculationTask(id: 1, data: 13))
task_queue.send(CalculationTask(id: 2, data: 37))

while true:
  echo "got result: ", repr(result_queue.recv())
```

### Concurrency

Asynchronous IO is supported either via the `asyncdispatch` module in the standard library or the external `chronos` library. Both libraries add async/await syntax via the macro system, without need for special language support. An example of an asynchronous HTTP server:

```mw
import std/[asynchttpserver, asyncdispatch]
# chronos could also be alternatively used in place of asyncdispatch,
# with no other changes.

var server = newAsyncHttpServer()
proc cb(req: Request) {.async.} =
  await req.respond(Http200, "Hello World")

waitFor server.serve(Port(8080), cb)
```

## Community

### Online

Nim has an active community on the self-hosted, self-developed official forum. Further, the project uses a Git repository, bug tracker, RFC tracker, and wiki hosted by GitHub, where the community engages with the language. There are also official online chat rooms, bridged between IRC, Matrix, Discord, Gitter, and Telegram.

### Conventions

The first Nim conference, NimConf, took place on 20 June 2020. It was held digitally due to COVID-19, with an open call for contributor talks in the form of YouTube videos. The conference began with language overviews by Nim developers Andreas Rumpf and Dominik Picheta. Presentation topics included talks about web frameworks, mobile development, Internet of things (IoT) devices, and game development, including a talk about writing Nim for Game Boy Advance. NimConf 2020 is available as a YouTube playlist. NimConf 2021 occurred the following year, was also held digitally, and included talks about game development, REPLs, real-time operating systems, Nim in the industry, object–relational mapping (ORM), fuzzing, language design, and graphics libraries.

In addition to official conferences, Nim has been featured at various other conventions. A presentation on Nim was given at the O'Reilly Open Source Convention (OSCON) in 2015. Four speakers represented Nim at FOSDEM 2020, including the creator of the language, Andreas Rumpf. At FOSDEM 2022, Nim hosted their own developer room virtually due to the COVID-19 pandemic. Talks were held on concurrency, embedded programming, programming for GPUs, entity-component systems, game development, rules engines, Python interop, and metaprogramming.

---
title: "Nim Manual (part 4/5)"
source: https://nim-lang.org/docs/manual.html
domain: nim-lang
license: CC-BY-SA-4.0
tags: nim language, nim lang, nimble, nim compiler
fetched: 2026-07-02
part: 4/5
---

# Nim Manual

Path names are syntactically either Nim identifiers or string literals. If the path name is not a valid Nim identifier it needs to be a string literal:

import "gfx/3d/somemodule"

A directory can also be a so-called "pseudo directory". They can be used to avoid ambiguity when there are multiple modules with the same path.

There are two pseudo directories:

1. std: The std pseudo directory is the abstract location of Nim's standard library. For example, the syntax import std / strutils is used to unambiguously refer to the standard library's strutils module.
2. pkg: The pkg pseudo directory is used to unambiguously refer to a Nimble package. However, for technical details that lie outside the scope of this document, its semantics are: *Use the search path to look for module name but ignore the standard library locations*. In other words, it is the opposite of std.

It is recommended and preferred but not currently enforced that all stdlib module imports include the std/ "pseudo directory" as part of the import name.

After the from keyword, a module name followed by an import to list the symbols one likes to use without explicit full qualification:

from std/strutils import `%` echo "$1" % "abc" echo strutils.replace("abc", "a", "z")

It's also possible to use from module import nil if one wants to import the module but wants to enforce fully qualified access to every symbol in module.

An export statement can be used for symbol forwarding so that client modules don't need to import a module's dependencies:

type MyObject* = object

import B export B.MyObject proc `$`*(x: MyObject): string = "my object"

import A var x: MyObject echo $x

When the exported symbol is another module, all of its definitions will be forwarded. One can use an except list to exclude some of the symbols.

Notice that when exporting, one needs to specify only the module name:

import foo/bar/baz export baz

Identifiers are valid from the point of their declaration until the end of the block in which the declaration occurred. The range where the identifier is known is the scope of the identifier. The exact scope of an identifier depends on the way it was declared.

The *scope* of a variable declared in the declaration part of a block is valid from the point of declaration until the end of the block. If a block contains a second block, in which the identifier is redeclared, then inside this block, the second declaration will be valid. Upon leaving the inner block, the first declaration is valid again. An identifier cannot be redefined in the same block, except if valid for procedure or iterator overloading purposes.

The field identifiers inside a tuple or object definition are valid in the following places:

- To the end of the tuple/object definition.
- Field designators of a variable of the given tuple/object type.
- In all descendant types of the object type.

All identifiers of a module are valid from the point of declaration until the end of the module. Identifiers from indirectly dependent modules are *not* available. The system module is automatically imported in every module.

If a module imports the same identifier from two different modules, the identifier is considered ambiguous, which can be resolved in the following ways:

- Qualifying the identifier as module.identifier resolves ambiguity between modules. (See below for the case that the module name itself is ambiguous.)
- Calling the identifier as a routine makes overload resolution take place, which resolves ambiguity in the case that one overload matches stronger than the others.
- Using the identifier in a context where the compiler can infer the type of the identifier resolves ambiguity in the case that one definition matches the type stronger than the others. var x*: string proc foo*(a: string) = echo "A: ", a var x*: int proc foo*(b: int) = echo "B: ", b import A, B foo("abc") foo(123) let inferred: proc (x: string) = foo foo("def") write(stdout, x) write(stdout, A.x) proc bar(a: int): int = a + 1 assert bar(x) == x + 1 var x = 4 write(stdout, x)

Modules can share their name, however, when trying to qualify an identifier with the module name the compiler will fail with ambiguous identifier error. One can qualify the identifier by aliasing the module.

proc fb* = echo "fizz"

proc fb* = echo "buzz"

import A/C import B/C C.fb()

import A/C as fizz import B/C fizz.fb()

A collection of modules in a file tree with an identifier.nimble file in the root of the tree is called a Nimble package. A valid package name can only be a valid Nim identifier and thus its filename is identifier.nimble where identifier is the desired package name. A module without a .nimble file is assigned the package identifier: unknown.

The distinction between packages allows diagnostic compiler messages to be scoped to the current project's package vs foreign packages.

The Nim compiler emits different kinds of messages: hint, warning, and error messages. An *error* message is emitted if the compiler encounters any static error.

Pragmas are Nim's method to give the compiler additional information / commands without introducing a massive number of new keywords. Pragmas are processed on the fly during semantic checking. Pragmas are enclosed in the special {. and .} curly brackets. Pragmas are also often used as a first implementation to play with a language feature before a nicer syntax to access the feature becomes available.

The deprecated pragma is used to mark a symbol as deprecated:

proc p() {.deprecated.} var x {.deprecated.}: char

This pragma can also take in an optional warning string to relay to developers.

proc thing(x: bool) {.deprecated: "use thong instead".}

The compileTime pragma is used to mark a proc or variable to be used only during compile-time execution. No code will be generated for it. Compile-time procs are useful as helpers for macros. Since version 0.12.0 of the language, a proc that uses system.NimNode within its parameter types is implicitly declared compileTime:

proc astHelper(n: NimNode): NimNode = result = n

Is the same as:

proc astHelper(n: NimNode): NimNode {.compileTime.} = result = n

compileTime variables are available at runtime too. This simplifies certain idioms where variables are filled at compile-time (for example, lookup tables) but accessed at runtime:

import std/macros var nameToProc {.compileTime.}: seq[(string, proc (): string {.nimcall.})] macro registerProc(p: untyped): untyped = result = newTree(nnkStmtList, p) let procName = p[0] let procNameAsStr = $p[0] result.add quote do: nameToProc.add((`procNameAsStr`, `procName`)) proc foo: string {.registerProc.} = "foo" proc bar: string {.registerProc.} = "bar" proc baz: string {.registerProc.} = "baz" doAssert nameToProc[2][1]() == "baz"

The noreturn pragma is used to mark a proc that never returns.

The acyclic pragma can be used for object types to mark them as acyclic even though they seem to be cyclic. This is an **optimization** for the garbage collector to not consider objects of this type as part of a cycle:

type Node = ref NodeObj NodeObj {.acyclic.} = object left, right: Node data: string

Or if we directly use a ref object:

type Node {.acyclic.} = ref object left, right: Node data: string

In the example, a tree structure is declared with the Node type. Note that the type definition is recursive and the GC has to assume that objects of this type may form a cyclic graph. The acyclic pragma passes the information that this cannot happen to the GC. If the programmer uses the acyclic pragma for data types that are in reality cyclic, this may result in memory leaks, but memory safety is preserved.

The final pragma can be used for an object type to specify that it cannot be inherited from. Note that inheritance is only available for objects that inherit from an existing object (via the object of SuperType syntax) or that have been marked as inheritable.

The shallow pragma affects the semantics of a type: The compiler is allowed to make a shallow copy. This can cause serious semantic issues and break memory safety! However, it can speed up assignments considerably, because the semantics of Nim require deep copying of sequences and strings. This can be expensive, especially if sequences are used to build a tree structure:

type NodeKind = enum nkLeaf, nkInner Node {.shallow.} = object case kind: NodeKind of nkLeaf: strVal: string of nkInner: children: seq[Node]

An object type can be marked with the pure pragma so that its type field which is used for runtime type identification is omitted. This used to be necessary for binary compatibility with other compiled languages.

An enum type can be marked as pure. Then access of its fields always requires full qualification.

A proc can be marked with the asmNoStackFrame pragma to tell the compiler it should not generate a stack frame for the proc. There are also no exit statements like return result; generated and the generated C function is declared as __declspec(naked) or __attribute__((naked)) (depending on the used C compiler).

**Note**: This pragma should only be used by procs which consist solely of assembler statements.

The error pragma is used to make the compiler output an error message with the given content. The compilation does not necessarily abort after an error though.

The error pragma can also be used to annotate a symbol (like an iterator or proc). The *usage* of the symbol then triggers a static error. This is especially useful to rule out that some operation is valid due to overloading and type conversions:

proc `==`(x, y: ptr int): bool {.error.}

The fatal pragma is used to make the compiler output an error message with the given content. In contrast to the error pragma, the compilation is guaranteed to be aborted by this pragma. Example:

when not defined(objc): {.fatal: "Compile this program with the objc command!".}

The warning pragma is used to make the compiler output a warning message with the given content. Compilation continues after the warning.

The hint pragma is used to make the compiler output a hint message with the given content. Compilation continues after the hint.

The line pragma can be used to affect line information of the annotated statement, as seen in stack backtraces:

template myassert*(cond: untyped, msg = "") = if not cond: {.line: instantiationInfo().}: raise newException(AssertionDefect, msg)

If the line pragma is used with a parameter, the parameter needs to be a tuple[filename: string, line: int]. If it is used without a parameter, system.instantiationInfo() is used.

The linearScanEnd pragma can be used to tell the compiler how to compile a Nim case statement. Syntactically it has to be used as a statement:

case myInt of 0: echo "most common case" of 1: {.linearScanEnd.} echo "second most common case" of 2: echo "unlikely: use branch table" else: echo "unlikely too: use branch table for ", myInt

In the example, the case branches 0 and 1 are much more common than the other cases. Therefore, the generated assembler code should test for these values first so that the CPU's branch predictor has a good chance to succeed (avoiding an expensive CPU pipeline stall). The other cases might be put into a jump table for O(1) overhead but at the cost of a (very likely) pipeline stall.

The linearScanEnd pragma should be put into the last branch that should be tested against via linear scanning. If put into the last branch of the whole case statement, the whole case statement uses linear scanning.

The computedGoto pragma can be used to tell the compiler how to compile a Nim case in a while true statement. Syntactically it has to be used as a statement inside the loop:

type MyEnum = enum enumA, enumB, enumC, enumD, enumE proc vm() = var instructions: array[0..100, MyEnum] instructions[2] = enumC instructions[3] = enumD instructions[4] = enumA instructions[5] = enumD instructions[6] = enumC instructions[7] = enumA instructions[8] = enumB instructions[12] = enumE var pc = 0 while true: {.computedGoto.} let instr = instructions[pc] case instr of enumA: echo "yeah A" of enumC, enumD: echo "yeah CD" of enumB: echo "yeah B" of enumE: break inc(pc) vm()

As the example shows, computedGoto is mostly useful for interpreters. If the underlying backend (C compiler) does not support the computed goto extension the pragma is simply ignored.

The immediate pragma is obsolete. See Typed vs untyped parameters.

Redefinition of template symbols with the same signature is allowed. This can be made explicit with the redefine pragma:

template foo: int = 1 echo foo() template foo: int {.redefine.} = 2 echo foo() template foo: int = 3

This is mostly intended for macro generated code.

The listed pragmas here can be used to override the code generation options for a proc/method/converter.

The implementation currently provides the following possible options (various others may be added later).

| pragma | allowed values | description |
|---|---|---|
| checks | on\|off | Turns the code generation for all runtime checks on or off. |
| boundChecks | on\|off | Turns the code generation for array bound checks on or off. |
| overflowChecks | on\|off | Turns the code generation for over- or underflow checks on or off. |
| nilChecks | on\|off | Turns the code generation for nil pointer checks on or off. |
| assertions | on\|off | Turns the code generation for assertions on or off. |
| warnings | on\|off | Turns the warning messages of the compiler on or off. |
| hints | on\|off | Turns the hint messages of the compiler on or off. |
| optimization | none\|speed\|size | Optimize the code for speed or size, or disable optimization. |
| patterns | on\|off | Turns the term rewriting templates/macros on or off. |
| callconv | cdecl\|... | Specifies the default calling convention for all procedures (and procedure types) that follow. |

Example:

{.checks: off, optimization: speed.}

The push/pop pragmas are very similar to the option directive, but are used to override the settings temporarily. Example:

{.push checks: off.} {.pop.}

push/pop can switch on/off some standard library pragmas, example:

{.push inline.} proc thisIsInlined(): int = 42 func willBeInlined(): float = 42.0 {.pop.} proc notInlined(): int = 9 {.push discardable, boundChecks: off, compileTime, noSideEffect, experimental.} template example(): string = "https://nim-lang.org" {.pop.} {.push deprecated, used, stackTrace: off.} proc sample(): bool = true {.pop.}

For third party pragmas, it depends on its implementation but uses the same syntax.

The register pragma is for variables only. It declares the variable as register, giving the compiler a hint that the variable should be placed in a hardware register for faster access. C compilers usually ignore this though and for good reasons: Often they do a better job without it anyway.

However, in highly specific cases (a dispatch loop of a bytecode interpreter for example) it may provide benefits.

The global pragma can be applied to a variable within a proc to instruct the compiler to store it in a global location and initialize it once at program startup.

proc isHexNumber(s: string): bool = var pattern {.global.} = re"[0-9a-fA-F]+" result = s.match(pattern)

When used within a generic proc, a separate unique global variable will be created for each instantiation of the proc. The order of initialization of the created global variables within a module is not defined, but all of them will be initialized after any top-level variables in their originating module and before any variable in a module that imports it.

Nim generates some warnings and hints that may annoy the user. A mechanism for disabling certain messages is provided: Each hint and warning message is associated with a symbol. This is the message's identifier, which can be used to enable or disable the message by putting it in brackets following the pragma:

{.hint[XDeclaredButNotUsed]: off.}

This is often better than disabling all warnings at once.

Nim produces a warning for symbols that are not exported and not used either. The used pragma can be attached to a symbol to suppress this warning. This is particularly useful when the symbol was generated by a macro:

template implementArithOps(T) = proc echoAdd(a, b: T) {.used.} = echo a + b proc echoSub(a, b: T) {.used.} = echo a - b implementArithOps(int) echoAdd 3, 5

used can also be used as a top-level statement to mark a module as "used". This prevents the "Unused import" warning:

when defined(nimHasUsed): {.used.}

The experimental pragma enables experimental language features. Depending on the concrete feature, this means that the feature is either considered too unstable for an otherwise stable release or that the future of the feature is uncertain (it may be removed at any time). See the experimental manual for more details.

Example:

import std/threadpool {.experimental: "parallel".} proc threadedEcho(s: string, i: int) = echo(s, " ", $i) proc useParallel() = parallel: for i in 0..4: spawn threadedEcho("echo in parallel", i) useParallel()

As a top-level statement, the experimental pragma enables a feature for the rest of the module it's enabled in. This is problematic for macro and generic instantiations that cross a module scope. Currently, these usages have to be put into a .push/pop environment:

proc useParallel*[T](unused: T) = {.push experimental: "parallel".} parallel: for i in 0..4: echo "echo in parallel" {.pop.}

import client useParallel(1)

This section describes additional pragmas that the current Nim implementation supports but which should not be seen as part of the language specification.

The bitsize pragma is for object field members. It declares the field as a bitfield in C/C++.

type mybitfield = object flag {.bitsize:1.}: cuint

generates:

struct mybitfield { unsigned int flag:1; };

Nim automatically determines the size of an enum. But when wrapping a C enum type, it needs to be of a specific size. The size pragma allows specifying the size of the enum type.

type EventType* {.size: sizeof(uint32).} = enum QuitEvent, AppTerminating, AppLowMemory doAssert sizeof(EventType) == sizeof(uint32)

When used for enum types, the size pragma accepts only the values 1, 2, 4 or 8.

The size pragma can also specify the size of an importc incomplete object type so that one can get the size of it at compile time even if it was declared without fields.

type AtomicFlag* {.importc: "atomic_flag", header: "<stdatomic.h>", size: 1.} = object static: echo sizeof(AtomicFlag)

The align pragma is for variables and object field members. It modifies the alignment requirement of the entity being declared. The argument must be a constant power of 2. Valid non-zero alignments that are weaker than other align pragmas on the same declaration are ignored. Alignments that are weaker than the alignment requirement of the type are ignored.

type sseType = object sseData {.align(16).}: array[4, float32] Data = object x: char cacheline {.align(128).}: array[128, char] proc main() = echo "sizeof(Data) = ", sizeof(Data), " (1 byte + 127 bytes padding + 128-byte array)" echo "alignment of sseType is ", alignof(sseType) var d {.align(2048).}: Data main()

This pragma has no effect on the JavaScript backend and may significantly increase memory usage with the --mm:refc option.

Since version 1.4 of the Nim compiler, there is a .noalias annotation for variables and parameters. It is mapped directly to C/C++'s restrict keyword and means that the underlying pointer is pointing to a unique location in memory, no other aliases to this location exist. It is *unchecked* that this alias restriction is followed. If the restriction is violated, the backend optimizer is free to miscompile the code. This is an **unsafe** language feature.

Ideally in later versions of the language, the restriction will be enforced at compile time. (This is also why the name noalias was chosen instead of a more verbose name like unsafeAssumeNoAlias.)

The volatile pragma is for variables only. It declares the variable as volatile, whatever that means in C/C++ (its semantics are not well-defined in C/C++).

**Note**: This pragma will not exist for the LLVM backend.

The nodecl pragma can be applied to almost any symbol (variable, proc, type, etc.) and is sometimes useful for interoperability with C: It tells Nim that it should not generate a declaration for the symbol in the C code. For example:

var EACCES {.importc, nodecl.}: cint

However, the header pragma is often the better alternative.

**Note**: This will not work for the LLVM backend.

The header pragma is very similar to the nodecl pragma: It can be applied to almost any symbol and specifies that it should not be declared and instead, the generated code should contain an #include:

type PFile {.importc: "FILE*", header: "<stdio.h>".} = distinct pointer

The header pragma always expects a string constant. The string constant contains the header file: As usual for C, a system header file is enclosed in angle brackets: <>. If no angle brackets are given, Nim encloses the header file in "" in the generated C code.

**Note**: This will not work for the LLVM backend.

The incompleteStruct pragma tells the compiler to not use the underlying C struct in a sizeof expression:

type DIR* {.importc: "DIR", header: "<dirent.h>", pure, incompleteStruct.} = object

The completeStruct pragma is a contract indicating that an importc type declaration contains all fields of the corresponding C type, allowing sizeof, alignof, and offsetof to be computed at compile-time.

By default, importc types are assumed to be incomplete (their size is unknown at compile-time). Use completeStruct when you need compile-time size information and can guarantee the Nim definition matches the C layout:

type InotifyEvent {.importc: "struct inotify_event", header: "<sys/inotify.h>", completeStruct.} = object wd: cint mask: uint32 cookie: uint32 len: uint32

If the Nim fields don't match the C struct, a static assertion will fail during C code generation.

Without completeStruct, attempting to use sizeof on an importc type at compile-time will error with "'sizeof' requires '.importc' types to be '.completeStruct'".

The compile pragma can be used to compile and link a C/C++ source file with the project:

This pragma can take three forms. The first is a simple file input:

{.compile: "myfile.cpp".}

The second form is a tuple where the second arg is the output name strutils formatter:

{.compile: ("file.c", "$1.o").}

**Note**: Nim computes a SHA1 checksum and only recompiles the file if it has changed. One can use the -f command-line option to force the recompilation of the file.

Since 1.4 the compile pragma is also available with this syntax:

{.compile("myfile.cpp", "--custom flags here").}

As can be seen in the example, this new variant allows for custom flags that are passed to the C compiler when the file is recompiled.

The link pragma can be used to link an additional file with the project:

{.link: "myfile.o".}

The passc pragma can be used to pass additional parameters to the C compiler like one would use the command-line switch --passc:

{.passc: "-Wall -Werror".}

Note that one can use gorge from the system module to embed parameters from an external command that will be executed during semantic analysis:

{.passc: gorge("pkg-config --cflags sdl").}

The localPassC pragma can be used to pass additional parameters to the C compiler, but only for the C/C++ file that is produced from the Nim module the pragma resides in:

{.localPassC: "-Wall -Werror".}

The passl pragma can be used to pass additional parameters to the linker like one would be using the command-line switch --passl:

{.passl: "-lSDLmain -lSDL".}

Note that one can use gorge from the system module to embed parameters from an external command that will be executed during semantic analysis:

{.passl: gorge("pkg-config --libs sdl").}

The emit pragma can be used to directly affect the output of the compiler's code generator. The code is then unportable to other code generators/backends. Its usage is highly discouraged! However, it can be extremely useful for interfacing with C++ or Objective C code.

Example:

{.emit: """ static int cvariable = 420; """.} {.push stackTrace:off.} proc embedsC() = var nimVar = 89 {.emit: ["""fprintf(stdout, "%d\n", cvariable + (int)""", nimVar, ");"].} {.pop.} embedsC()

nimbase.h defines NIM_EXTERNC C macro that can be used for extern "C" code to work with both nim c and nim cpp, e.g.:

proc foobar() {.importc:"$1".} {.emit: """ #include <stdio.h> NIM_EXTERNC void fun(){} """.}

Note:

For backward compatibility, if the argument to the

emit

statement is a single string literal, Nim symbols can be referred to via backticks. This usage is however deprecated.

For a top-level emit statement, the section where in the generated C/C++ file the code should be emitted can be influenced via the prefixes /*TYPESECTION*/ or /*VARSECTION*/ or /*INCLUDESECTION*/:

{.emit: """/*TYPESECTION*/ struct Vector3 { public: Vector3(): x(5) {} Vector3(float x_): x(x_) {} float x; }; """.} type Vector3 {.importcpp: "Vector3", nodecl} = object x: cfloat proc constructVector3(a: cfloat): Vector3 {.importcpp: "Vector3(@)", nodecl}

**Note**: c2nim can parse a large subset of C++ and knows about the importcpp pragma pattern language. It is not necessary to know all the details described here.

Similar to the importc pragma for C, the importcpp pragma can be used to import C++ methods or C++ symbols in general. The generated code then uses the C++ method calling syntax: obj->method(arg). In combination with the header and emit pragmas this allows *sloppy* interfacing with libraries written in C++:

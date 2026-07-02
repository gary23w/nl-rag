---
title: "Interprocedural optimization"
source: https://en.wikipedia.org/wiki/Interprocedural_optimization
domain: control-flow-analysis
license: CC-BY-SA-4.0
tags: control-flow analysis, control-flow graph, call graph, basic block
fetched: 2026-07-02
---

# Interprocedural optimization

**Interprocedural optimization** (**IPO**) is a collection of compiler techniques used in computer programming to improve performance in programs containing many frequently used functions of small or medium length. IPO differs from other compiler optimizations by analyzing the entire program as opposed to a single function or block of code.

IPO seeks to reduce or eliminate duplicate calculations and inefficient use of memory and to simplify iterative sequences such as loops. If a call to another routine occurs within a loop, IPO analysis may determine that it is best to inline that routine. Additionally, IPO may re-order the routines for better memory layout and locality.

IPO may also include typical compiler optimizations applied on a whole-program level, for example, dead code elimination (DCE), which removes code that is never executed. IPO also tries to ensure better use of constants. Modern compilers offer IPO as an option at compile-time. The actual IPO process may occur at any step between the human-readable source code and producing a finished executable binary program.

For languages that compile on a file-by-file basis, effective IPO across translation units (module files) requires knowledge of the "entry points" of the program so that a **whole program optimization** (**WPO**) can be run. In many cases, this is implemented as a **link-time optimization** (**LTO**) pass, because the whole program is visible to the linker.

## Analysis

The objective of any optimization for speed is to have the program run as swiftly as possible; the problem is that it is not possible for a compiler to correctly analyze a program and determine what it *will* do, much less what the programmer *intended* for it to do. By contrast, human programmers start at the other end with a purpose and attempt to produce a program that will achieve it, preferably without expending a lot of thought in the process.

For various reasons, including readability, programs are frequently broken up into a number of procedures that handle a few general cases. However, the generality of each procedure may result in wasted effort in specific usages. Interprocedural optimization represents an attempt at reducing this waste.

Suppose there is a procedure that evaluates `f(x)`, and that `f` is a pure function, and the code requests the result of `f(6)` and then later, `f(6)` again. This second evaluation is almost certainly unnecessary: the result could have instead been saved and referred to later. This simple optimization is foiled the moment that the implementation of `f(x)` becomes impure; that is, its execution involves references to parameters other than the explicit argument `6` that has been changed between the invocations, or side effects such as printing some message to a log, counting the number of evaluations, accumulating the CPU time consumed, preparing internal tables so that subsequent invocations for related parameters will be facilitated, and so forth. Losing these side effects via non-evaluation a second time may be acceptable, or they may not.

More generally, aside from optimization, the second reason to use procedures is to avoid duplication of code that would produce the same results, or almost the same results, each time the procedure is performed. A general approach to optimization would therefore be to reverse this: some or all invocations of a certain procedure are replaced by the respective code, with the parameters appropriately substituted. The compiler will then try to optimize the result.

## WPO and LTO

**Whole program optimization** (**WPO**) is the compiler optimization of a program using information about all the modules in the program. Normally, optimizations are performed on a per module, "compiland", basis; but this approach, while easier to write and test and less demanding of resources during the compilation itself, does not allow certainty about the safety of a number of optimizations such as aggressive inlining and thus cannot perform them even if they would actually turn out to be efficiency gains that do not change the semantics of the emitted object code.

**Link-time optimization** (**LTO**) is a type of program optimization performed by a compiler to a program at link time. Link time optimization is relevant in programming languages that compile programs on a file-by-file basis, and then link those files together (such as C and Fortran), rather than all at once (such as Java's just-in-time compilation (JIT)).

Once all files have been compiled separately into object files, traditionally, a compiler links (merges) the object files into a single file, the executable. However, in LTO as implemented by the GNU Compiler Collection (GCC) and LLVM, the compiler is able to dump its intermediate representation (IR), i.e. GIMPLE bytecode or LLVM bitcode, respectively, so that all the different compilation units that will go to make up a single executable can be optimized as a single module when the link finally happens. This expands the scope of interprocedural optimizations to encompass the whole program (or, rather, everything that is visible at link time). With link-time optimization, the compiler can apply various forms of interprocedural optimization to the whole program, allowing for deeper analysis, more optimization, and ultimately better program performance.

In practice, LTO does not always optimize the entire program—library functions, especially dynamically linked shared objects, are intentionally kept out to avoid excessive duplication and to allow for updating. Static linking does naturally lend to the concept of LTO, but it only works with library archives that contain IR objects as opposed to machine-code only object files. Due to performance concerns, not even the entire unit is always directly used—a program could be partitioned in a divide-and-conquer style LTO such as GCC's WHOPR. And of course, when the program being built is itself a library, the optimization would keep every externally-available (exported) symbol, without trying too hard at removing them as a part of DCE.

A much more limited form of WPO is still possible without LTO, as exemplified by GCC's `-fwhole-program` switch. This mode makes GCC assume that the module being compiled contains the entry point of the entire program, so that every other function in it is not externally used and can be safely optimized away. Since it only applies to a single module, it cannot truly encompass the whole program. It can be combined with LTO in the one-big-module sense, which is useful when the linker is not communicating back to GCC about what entry points or symbols are being used externally.

## History

For procedural languages like ALGOL, interprocedural analysis and optimization appear to have entered commercial practice in the early 1970s. IBM's PL/I Optimizing Compiler performed interprocedural analysis to understand the side effects of both procedure calls and exceptions (cast, in PL/I terms as "on conditions") and in papers by Fran Allen. Work on compilation of the APL programming language was necessarily interprocedural.

The techniques of interprocedural analysis and optimization were the subject of academic research in the 1980s and 1990s. They re-emerged into the commercial compiler world in the early 1990s with compilers from both Convex Computer Corporation (the "Application Compiler" for the Convex C4) and from Ardent (the compiler for the Ardent Titan). These compilers demonstrated that the technologies could be made sufficiently fast to be acceptable in a commercial compiler; subsequently interprocedural techniques have appeared in a number of commercial and non-commercial systems.

## Flags and implementation

### Unix-like

The GNU Compiler Collection has function inlining at all optimization levels. At `-O1` this only applies to those only called once (`-finline-functions-once`), at `-O2` this constraint is relaxed (`-finline-functions`). By default this is a single-file-only behavior, but with link-time optimization `-flto` it becomes whole program. Clang's command-line interface is similar to that of GCC, with the exception that there is no `-fwhole-program` option.

Object files produced by LTO contain a compiler-specific intermediate representation (IR) that is interpreted at link-time. To make sure this plays well with static libraries, newer GNU linkers have a "linker plugin" interface that allows the compiler to convert the object files into a machine code form when needed. This plugin also helps drive the LTO process in general. Alternatively, a "fat LTO" object can be produced to contain both machine code and the IR, but this takes more space.

Since both GCC and LLVM (clang) are able produce an IR from a variety of programming languages, link-time IPO can happen even across language boundaries. This is most commonly demonstrated with C and C++, but LLVM makes it possible for Rust and all other LLVM-based compilers too.

#### Non-LTO options

GCC and Clang perform IPO by default at optimization level 2. However, the degree of optimization is limited when LTO is disabled, as IPO can only happen within an object file and non-static functions can never be eliminated. The latter problem has a non-LTO solution: the `-fwhole-program` switch can be used to assume that only `main()` is non-static, i.e. visible from the outside.

Another non-LTO technique is "function sections" (`-ffunction-sections` in GCC and Clang). By placing each function into its own section in the object file, the linker can perform dead code removal without an IR by removing unreferenced sections (using the linker option `--gc-sections`). A similar option is available for variables, but it causes much worse code to be produced.

### Other

The Intel C/C++ compilers allow whole-program IPO. The flag to enable interprocedural optimizations for a single file is `-ip`, the flag to enable interprocedural optimization across all files in the program is `-ipo`.

The MSVC compiler, integrated into Visual Studio, also supports interprocedural optimization on the whole program.

A compiler-independent interface for enabling whole-program interprocedural optimizations is via the `INTERPROCEDURAL_OPTIMIZATION` property in CMake.

---
title: "Code generation (compiler)"
source: https://en.wikipedia.org/wiki/Code_generation_(compiler)
domain: compilers-and-parsing
license: CC-BY-SA-4.0
tags: compiler construction, parser generator, syntax analysis, lexer, lexical analysis, abstract syntax tree
fetched: 2026-07-02
---

# Code generation (compiler)

In computing, **code generation** is part of the process chain of a compiler, in which an intermediate representation of source code is converted into a form (e.g., machine code) that the target system can readily execute.

Sophisticated compilers typically perform multiple passes over various intermediate forms. This multi-stage process is used because many algorithms for code optimization are easier to apply one at a time, or because the input to one optimization relies on the completed processing performed by another optimization. This organization also facilitates the creation of a single compiler that can target multiple architectures, as only the last of the code generation stages (the *backend*) needs to change from target to target. (For more information on compiler design, see Compiler.)

The input to the code generator typically consists of a parse tree or an abstract syntax tree. The tree is converted into a linear sequence of instructions, usually in an intermediate language such as three-address code. Further stages of compilation may or may not be referred to as "code generation", depending on whether they involve a significant change in the representation of the program. (For example, a peephole optimization pass would not likely be called "code generation", although a code generator might incorporate a peephole optimization pass.)

## Major tasks

In addition to converting an intermediate representation into a linear sequence of machine instructions, a typical code generator tries to optimize the generated code.

Tasks which are typically part of a sophisticated compiler's "code generation" phase include:

- Instruction selection: which instructions to use.
- Instruction scheduling: in which order to put those instructions. Scheduling is a speed optimization that can critically affect pipelined machines.
- Register allocation: the allocation of variables to processor registers
- Debug data generation if required, so that the code can be debugged.

Instruction selection is typically carried out by doing a recursive postorder traversal on the abstract syntax tree, matching particular tree configurations against templates; for example, the tree `W := ADD(X,MUL(Y,Z))` might be transformed into a linear sequence of instructions by recursively generating the sequences for `t1 := X` and `t2 := MUL(Y,Z)`, and then emitting the instruction `ADD W, t1, t2`.

In a compiler that uses an intermediate language, there may be two instruction selection stages—one to convert the parse tree into intermediate code, and a second phase, much later, to convert the intermediate code into instructions from the instruction set of the target machine. This second phase does not require a tree traversal; it can be done linearly, and typically involves a simple replacement of intermediate-language operations with their corresponding opcodes. However, suppose the compiler is a language translator (for example, one that converts Java to C++). In that case, the second code-generation phase may involve *building* a tree from the linear intermediate code.

## Runtime code generation

When code generation occurs at runtime, as in just-in-time compilation (JIT), the entire process must be efficient with respect to space and time. For example, when regular expressions are interpreted and used to generate code at runtime, a non-deterministic finite-state machine is often generated instead of a deterministic one because the former can usually be created more quickly and occupies less memory space than the latter. Despite generally generating less efficient code, JIT code generation can take advantage of profiling information that is available only at runtime.

The fundamental task of taking input in one language and producing output in a non-trivially different language can be understood in terms of the core transformational operations of formal language theory. Consequently, some techniques initially developed for use in compilers have come to be employed in other ways. For example, YACC (Yet Another Compiler-Compiler) takes input in Backus–Naur form and converts it to a parser in C. Though it was initially created for automatic generation of a parser for a compiler, yacc is also often used to automate writing code that needs to be modified each time specifications are changed.

Many integrated development environments (IDEs) support some form of automatic source-code generation, often using algorithms in common with compiler code generators, although commonly less complicated. (See also: Program transformation and Data transformation.)

### Reflection

In general, a syntax and semantic analyzer tries to retrieve the program's structure from the source code, while a code generator uses this structural information (e.g., data types) to produce code. In other words, the former *adds* information while the latter *loses* some. One consequence of this information loss is that reflection becomes difficult or even impossible. To counter this problem, code generators often embed syntactic and semantic information and the code necessary for execution.

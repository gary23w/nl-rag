---
title: "Abstract syntax tree"
source: https://en.wikipedia.org/wiki/Abstract_syntax_tree
domain: unison-lang
license: CC-BY-SA-4.0
tags: unison language, content addressable storage, distributed computing, merkle tree, purely functional programming
fetched: 2026-07-02
---

# Abstract syntax tree

An **abstract syntax tree** (**AST**) is a data structure used in computer science to represent the structure of a program or code snippet. It is a tree representation of the abstract syntactic structure of text (often source code) written in a formal language. Each node of the tree denotes a construct occurring in the text. It is sometimes called just a **syntax tree**.

The syntax is "abstract" in the sense that it does not represent every detail appearing in the real syntax, but rather just the structural or content-related details. For instance, grouping parentheses are implicit in the tree structure, so these do not have to be represented as separate nodes. Likewise, a syntactic construct like an if-condition-then statement may be denoted by means of a single node with three branches.

This distinguishes abstract syntax trees from concrete syntax trees, traditionally designated parse trees. Parse trees are typically built by a parser during the source code translation and compiling process. Once built, additional information is added to the AST by means of subsequent processing, e.g., contextual analysis.

Abstract syntax trees are also used in program analysis and program transformation systems.

## Application in compilers

Abstract syntax trees are data structures widely used in compilers to represent the structure of program code. An AST is usually the result of the syntax analysis phase of a compiler. It often serves as an intermediate representation of the program through several stages that the compiler requires, and has a strong effect on the final output of the compiler.

### Motivation

An AST has several properties that aid in the additional steps of the compilation process:

- An AST can be edited and enhanced with information such as properties and annotations for every element it contains. Such editing and annotation is impossible with the source code of a program, since it would imply changing it.
- Compared to the source code, an AST does not include nonessential punctuation and delimiters (braces, semicolons, parentheses, etc.).
- An AST usually contains extra information about the program, due to the consecutive stages of analysis by the compiler. For example, it may store the position of each element in the source code, allowing the compiler to print useful error messages.

Languages are often ambiguous by nature. In order to avoid this ambiguity, programming languages are often specified as a context-free grammar (CFG). However, there are often aspects of programming languages that a CFG can't express, but are part of the language and are documented in its specification. These are details that require a context to determine their validity and behavior. For example, if a language allows new types to be declared, a CFG cannot predict the names of such types nor the way in which they should be used. Even if a language has a predefined set of types, enforcing proper usage usually requires some context. Another example is duck typing, where the type of an element can change depending on context. Operator overloading is yet another case where correct usage and final function are context-dependent.

### Design

The design of an AST is often closely linked with the design of a compiler and its expected features.

Core requirements include the following:

- Variable types must be preserved, as well as the location of each declaration in source code.
- The order of executable statements must be explicitly represented and well defined.
- Left and right components of binary operations must be stored and correctly identified.
- Identifiers and their assigned values must be stored for assignment statements.

These requirements can be used to design the data structure for the AST.

Some operations will always require two elements, such as the two terms for addition. However, some language constructs require an arbitrarily large number of children, such as argument lists passed to programs from the command shell. As a result, an AST used to represent code written in such a language has to also be flexible enough to allow for the quick addition of an unknown quantity of children.

To support compiler verification it should be possible to unparse an AST into source code form. The source code produced should be sufficiently similar to the original in appearance and identical in execution, upon recompilation. The AST is used intensively during semantic analysis, where the compiler checks for correct usage of the elements of the program and the language. The compiler also generates symbol tables based on the AST during semantic analysis. A complete traversal of the tree allows verification of the correctness of the program.

After verifying correctness, the AST serves as the base for code generation. The AST is often used to generate an intermediate representation (IR), sometimes called an intermediate language, for the code generation.

## Other usages

### AST differencing

AST differencing, or for short tree differencing, consists of computing the list of differences between two ASTs. This list of differences is typically called an edit script. The edit script directly refers to the AST of the code. For instance, an edit action may result in the addition of a new AST node representing a function.

### Clone detection

An AST is a powerful abstraction to perform code clone detection.

## Definition

### Arities

Let S be a set of *sorts*, an *arity is a tuple* $(s_{1},\dots ,s_{n},s)$ , for $s_{1},\dots ,s_{n},s\in S$ , also written as $(s_{1},\dots ,s_{n})s$ . More precisely, $\mathrm {Arity} (S):=\coprod _{n\in \mathbb {N} }S^{n+1}$ .

Let ${\mathcal {O}}=\{{\mathcal {O_{\alpha }}}\}_{\alpha \in \mathrm {Arity} (S)}$ be an $\mathrm {Arity} (S)$ -indexed family of disjoint sets of *operators*. If o is an operator arity $(s_{1},\dots ,s_{n})s$ we say that o has sort s and has n arguments of sorts $s_{1},\dots ,s_{n}$ .

### ASTs

Fix S be a finite set of sorts, and ${\mathcal {O}}$ an $\mathrm {Arity} (S)$ -indexed family of disjoint sets of *operators*. Let ${\mathcal {X}}=\{{\mathcal {X}}_{s}\}_{s\in S}$ be an S -indexed family of disjoint sets of variables. The family ${\mathcal {A}}[{\mathcal {X}}]=\{{\mathcal {A}}[{\mathcal {X}}]_{s}\}_{s\in S}$ of ***abstract syntax trees***, or ***AST***s, is the smallest S -indexed family of disjoint sets closed under the following conditions:

1. **Variables are ASTs:** if $x\in {\mathcal {X}}_{s}$ , then $x\in {\mathcal {A}}[{\mathcal {X}}]_{s}$ .
2. **Operators combine ASTs:** If o is an operator of arity $(s_{1},\dots ,s_{n})s$ , and $a_{i}\in {\mathcal {A}}[{\mathcal {X}}]_{s_{i}}$ for all $1\leq i\leq n$ , then $o(a_{1};\dots ;a_{n})\in {\mathcal {A}}[{\mathcal {X}}]_{s}$ .

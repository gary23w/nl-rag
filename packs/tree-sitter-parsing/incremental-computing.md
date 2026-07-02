---
title: "Incremental computing"
source: https://en.wikipedia.org/wiki/Incremental_computing
domain: tree-sitter-parsing
license: CC-BY-SA-4.0
tags: tree-sitter parser, incremental parsing, concrete syntax tree, editor syntax parsing
fetched: 2026-07-02
---

# Incremental computing

**Incremental computing**, also known as **incremental computation**, is a software feature which, whenever a piece of data changes, attempts to save time by only recomputing those outputs which depend on the changed data. When incremental computing is successful, it can be significantly faster than computing new outputs naively. For example, a spreadsheet software package might use incremental computation in its recalculation features, to update only those cells containing formulas which depend (directly or indirectly) on the changed cells.

An automated incremental computing tool is a specialised program analysis tool for optimization.

## Static versus dynamic

Incremental computing techniques can be broadly classified into two types of approaches:

*Static approaches* attempt to derive an incremental program from a conventional program P using, e.g., either manual design and refactoring, or automatic program transformations. These program transformations occur before any inputs or input changes are provided.

*Dynamic approaches* record information about executing program P on a particular input (I1) and use this information when the input changes (to I2) in order to update the output (from O1 to O2). The figure shows the relationship between program P, the change calculation function ΔP, which constitutes the core of the incremental program, and a pair of inputs and outputs, I1, O1 and I2, O2.

## Specialized versus general-purpose approaches

Some approaches to incremental computing are specialized, while others are general purpose. Specialized approaches require the programmer to explicitly specify the algorithms and data structures that will be used to preserve unchanged sub-calculations. General-purpose approaches, on the other hand, use language, compiler, or algorithmic techniques to give incremental behavior to otherwise non-incremental programs.

## Static methods

### Program derivatives

Given a computation $C=f(x_{1},x_{2},\dots x_{n})$ and a potential change $x_{j}:=\Delta _{x_{j}}$ , we can insert code before the change occurs (the pre-derivative) and after the change (the post-derivative) to update the value of C faster than rerunning f . Paige has written down a list of rules for formal differentiation of programs in SUBSETL.

### View maintenance

In database systems such as DBToaster, views are defined with relational algebra. *Incremental view maintenance* statically analyzes relational algebra to create update rules that quickly maintain the view in the presence of small updates, such as insertion of a row.

## Dynamic methods

Incremental computation can be achieved by building a dependency graph of all the data elements that may need to be recalculated, and their dependencies. The elements that need to be updated when a single element changes are given by the transitive closure of the dependency relation of the graph. In other words, if there is a path from the changed element to another element, the latter may be updated (depending on whether the change eventually reaches the element). The dependency graph may need to be updated as dependencies change, or as elements are added to, or removed from, the system. It is used internally by the implementation, and does not typically need to be displayed to the user.

Capturing dependencies across all possible values can be avoided by identifying subset of important values (e.g., aggregation results) across which dependencies can be tracked, and incrementally recomputing other dependent variables, hence balancing the amount of dependency information to be tracked with the amount of recomputation to be performed upon input change.

Partial evaluation can be seen as a method for automating the simplest possible case of incremental computing, in which an attempt is made to divide program data into two categories: which can vary based on the program's input, and which cannot (and the smallest unit of change is simply "all the data that can vary"). Partial evaluation can be combined with other incremental computing techniques.

With cycles in the dependency graph, a single pass through the graph may not be sufficient to reach a fixed point. In some cases, complete re-evaluation of a system is semantically equivalent to incremental evaluation, and may be more efficient in practice if not in theory.

## Existing systems

### Compiler and language support

- Automatic Incrementalization (also called "Self-Adjusting Computation", and "Adaptive Functional Programming"), Delta ML, Haskell Adaptive
- Cornell Synthesizer Generator
- IceDust - a custom domain-specific language.

### Frameworks and libraries

- Adapton - with implementations in several languages
- One-way Dataflow Constraints (Reactive Computation in C++)
- Differential Dataflow
- Jane Street Incremental
- Incremental Datalog (LogicBlox)
- Incremental Prolog (XSB)
- FSharp.Data.Adaptive
- Domain-Specific Approaches:
  - Incremental Type Checking.

## Applications

- Databases (view maintenance)
- Build systems
- Spreadsheets
- Development Environments
- Financial Computations
- Attribute Grammar Evaluation
- Graph Computations and Queries
- GUIs (e.g., React and DOM diffing)
- Scientific applications.

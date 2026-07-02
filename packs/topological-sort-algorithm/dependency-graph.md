---
title: "Dependency graph"
source: https://en.wikipedia.org/wiki/Dependency_graph
domain: topological-sort-algorithm
license: CC-BY-SA-4.0
tags: topological sorting, directed acyclic graph, kahn algorithm, dependency graph
fetched: 2026-07-02
---

# Dependency graph

In mathematics, computer science and digital electronics, a **dependency graph** is a directed graph representing dependencies of several objects towards each other. It is possible to derive an evaluation order or the absence of an evaluation order that respects the given dependencies from the dependency graph.

## Definition

Given a set of objects S and a transitive relation $R\subseteq S\times S$ with $(a,b)\in R$ modeling a dependency "*a* depends on *b*" ("*a* needs *b* evaluated first"), the dependency graph is a graph $G=(S,T)$ with $T\subseteq R$ the transitive reduction of *R*.

For example, assume a simple calculator. This calculator supports assignment of constant values to variables and assigning the sum of exactly two variables to a third variable. Given several equations like "*A* = *B*+*C*; *B* = 5+*D*; *C*=4; *D*=2;", then $S=\{A,B,C,D\}$ and $R=\{(A,B),(A,C),(B,D),(A,D)\}$ . You can derive this relation directly: *A* depends on *B* and *C*, because you can add two variables if and only if you know the values of both variables. Thus, *B* must be calculated before *A* can be calculated. Since *B* depends on *D* to be calculated, *A* must also depend on *D* to be calculated before it (hence the transitive property stated above). On the other hand, the values of *C* and *D* are known immediately, because they are number literals.

## Recognizing impossible evaluations

In a dependency graph, cycles of dependencies (also called **circular dependencies**) lead to a situation in which no valid evaluation order exists, because none of the objects in the cycle may be evaluated first. If a dependency graph does not have any circular dependencies, it forms a directed acyclic graph, and an evaluation order may be found by topological sorting. Most topological sorting algorithms are also capable of detecting cycles in their inputs; however, it may be desirable to perform cycle detection separately from topological sorting in order to provide appropriate handling for the detected cycles.

Assume the simple calculator from before. The equation system "*A*=*B*; *B*=*D*+*C*; *C*=*D*+*A*; *D*=12;" contains a circular dependency formed by *A*, *B* and *C*, as *B* must be evaluated before *A*, *C* must be evaluated before *B*, and *A* must be evaluated before *C*.

## Deriving an evaluation order

A **correct evaluation order** is a numbering $n:S\rightarrow \mathbb {N}$ of the objects that form the nodes of the dependency graph so that the following equation holds: $n(a)<n(b)\Rightarrow (a,b)\notin R$ with $a,b\in S$ . This means, if the numbering orders two elements a and b so that a will be evaluated before b , then a must not depend on b .

There can be more than one correct evaluation order. In fact, a correct numbering is a topological order, and any topological order is a correct numbering. Thus, any algorithm that derives a correct topological order derives a correct evaluation order.

Assume the simple calculator from above once more. Given the equation system "*A* = *B*+*C*; *B* = 5+*D*; *C*=4; *D*=2;", a correct evaluation order would be (*D*, *C*, *B*, *A*). However, (*C*, *D*, *B*, *A*) is a correct evaluation order as well.

## Monoid structure

An acyclic dependency graph corresponds to a trace of a trace monoid as follows:

- A function $\phi :S\to \Sigma$ labels each vertex with a symbol from the alphabet $\Sigma$
- There is an edge $a\to b$ or $b\to a$ if and only if $(\phi (a),\phi (b))$ is in the dependency relation D .
- Two graphs are considered to be equal if their labels and edges correspond.

Then the string consisting of the vertex labels ordered by a correct evaluation order corresponds to a string of a trace.

The monoidal operation $(S_{12},R_{12})=(S_{1},R_{1})\bullet (S_{2},R_{2})$ takes the disjoint union $S_{12}=S_{1}\sqcup S_{2}$ of two graphs' vertex sets, preserves the existing edges in each graph, and draws new edges from the first to the second where the dependency relation allows,

$R_{12}=R_{1}\sqcup R_{2}\sqcup \{(a,b)\mid a\in S_{1}\land b\in S_{2}\land (\phi (a),\phi (b))\in D\}$

The identity is the empty graph.

## Examples

Dependency graphs are used in:

- Automated software installers: They walk the graph looking for software packages that are required but not yet installed. The dependency is given by the coupling of the packages.
- Software build scripts such as Unix Make, Node npm install, php composer, Twitter bower install, or Apache Ant. They need to know what files have changed so only the correct files need to be recompiled.
- In compiler technology and formal language implementation:
  - Instruction scheduling: Dependency graphs are computed for the operands of assembly or intermediate instructions and used to determine an optimal order for the instructions.
  - Dead code elimination: If no side effected operation depends on a variable, this variable is considered dead and can be removed.
- Dynamic graph analytics: GraphBolt and KickStarter capture value dependencies for incremental computing when graph structure changes.
- Spreadsheet calculators. They need to derive a correct calculation order similar to that one in the example used in this article.
- Web Forms standards such as XForms to know what visual elements to update if data in the model changes.
- Video games, especially puzzle and adventure video games, which are frequently designed as a graph of dependent relationships between in-game actions.

Dependency graphs are one aspect of:

- Manufacturing plant types: Raw materials are processed into products via several dependent stages.
- Job shop scheduling: A collection of related theoretical problems in computer science.

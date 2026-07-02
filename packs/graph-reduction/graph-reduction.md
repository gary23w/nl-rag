---
title: "Graph reduction"
source: https://en.wikipedia.org/wiki/Graph_reduction
domain: graph-reduction
license: CC-BY-SA-4.0
tags: graph reduction, combinator graph reduction, spineless tagless G-machine, supercombinator compilation
fetched: 2026-07-02
---

# Graph reduction

In computer science, **graph reduction** implements an efficient version of non-strict evaluation, an evaluation strategy where the arguments to a function are not immediately evaluated. This form of non-strict evaluation is also known as lazy evaluation and used in functional programming languages. The technique was first developed by Chris Wadsworth in 1971.

## Motivation

A simple example of evaluating an arithmetic expression follows:

${\begin{aligned}&{}&&((2+2)+(2+2))+(3+3)\\&{}&=&((2+2)+(2+2))+6\\&{}&=&((2+2)+4)+6\\&{}&=&(4+4)+6\\&{}&=&8+6\\&{}&=&14\end{aligned}}$

The above reduction sequence employs a strategy known as outermost tree reduction. The same expression can be evaluated using innermost tree reduction, yielding the reduction sequence:

${\begin{aligned}&{}&&((2+2)+(2+2))+(3+3)\\&{}&=&((2+2)+4)+(3+3)\\&{}&=&(4+4)+(3+3)\\&{}&=&(4+4)+6\\&{}&=&8+6\\&{}&=&14\end{aligned}}$

Notice that the reduction order is made explicit by the addition of parentheses. This expression could also have been simply evaluated right to left, because addition is an associative operation.

Represented as a tree, the expression above looks like this:

This is where the term tree reduction comes from. When represented as a tree, we can think of innermost reduction as working from the bottom up, while outermost works from the top down.

The expression can also be represented as a directed acyclic graph, allowing sub-expressions to be shared:

As for trees, outermost and innermost reduction also applies to graphs. Hence we have **graph reduction**.

Now evaluation with outermost graph reduction can proceed as follows:

Notice that evaluation now only requires four steps. Outermost graph reduction is referred to as lazy evaluation and innermost graph reduction is referred to as eager evaluation.

## Combinator graph reduction

**Combinator graph reduction** is a fundamental implementation technique for functional programming languages, in which a program is converted into a combinator representation which is mapped to a directed graph data structure in computer memory, and program execution then consists of rewriting parts of this graph ("reducing" it) so as to move towards useful results.

## History

The concept of a graph reduction that allows evaluated values to be shared was first developed by Chris Wadsworth in his 1971 Ph.D. dissertation. This dissertation was cited by Peter Henderson and James H. Morris Jr. in 1976 paper, “A lazy evaluator” that introduced the notion of lazy evaluation. In 1976 David Turner incorporated lazy evaluation into SASL using combinators. SASL was an early functional programming language first developed by Turner in 1972.

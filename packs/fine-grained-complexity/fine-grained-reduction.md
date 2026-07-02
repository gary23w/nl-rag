---
title: "Fine-grained reduction"
source: https://en.wikipedia.org/wiki/Fine-grained_reduction
domain: fine-grained-complexity
license: CC-BY-SA-4.0
tags: fine grained complexity, fine grained reduction, strong exponential time hypothesis, 3sum conjecture
fetched: 2026-07-02
---

# Fine-grained reduction

In computational complexity theory, a **fine-grained reduction** is a transformation from one computational problem to another, used to relate the difficulty of improving the time bounds for the two problems. Intuitively, it provides a method for solving one problem efficiently by using the solution to the other problem as a subroutine. If problem A can be solved in time $a(n)$ and problem B can be solved in time $b(n)$ , then the existence of an $(a,b)$ -reduction from problem A to problem B implies that any significant speedup for problem B would also lead to a speedup for problem A .

## Definition

Let A and B be computational problems, specified as the desired output for each possible input. Let a and b both be time-constructible functions that take an integer argument n and produce an integer result. Usually, a and b are the time bounds for known or naive algorithms for the two problems, and often they are monomials such as $n^{2}$ .

Then A is said to be $(a,b)$ -reducible to B if, for every real number $\epsilon >0$ , there exists a real number $\delta >0$ and an algorithm that solves instances of problem A by transforming it into a sequence of instances of problem B , taking time $O{\bigl (}a(n)^{1-\delta }{\bigr )}$ for the transformation on instances of size n , and producing a sequence of instances whose sizes $n_{i}$ are bounded by $\sum _{i}b(n_{i})^{1-\epsilon }<a(n)^{1-\delta }$ .

An $(a,b)$ -reduction is given by the mapping from $\epsilon$ to the pair of an algorithm and $\delta$ .

## Speedup implication

Suppose A is $(a,b)$ -reducible to B , and there exists $\epsilon >0$ such that B can be solved in time $O{\bigl (}b(n)^{1-\epsilon }{\bigr )}$ . Then, with these assumptions, there also exists $\delta >0$ such that A can be solved in time $O{\bigl (}a(n)^{1-\delta }{\bigr )}$ . Namely, let $\delta$ be the value given by the $(a,b)$ -reduction, and solve A by applying the transformation of the reduction and using the fast algorithm for B for each resulting subproblem.

Equivalently, if A cannot be solved in time significantly faster than $a(n)$ , then B cannot be solved in time significantly faster than $b(n)$ .

## History

Fine-grained reductions were defined, in the special case that a and b are equal monomials, by Virginia Vassilevska Williams and Ryan Williams in 2010. They also showed the existence of $(n^{3},n^{3})$ -reductions between several problems including all-pairs shortest paths, finding the second-shortest path between two given vertices in a weighted graph, finding negative-weight triangles in weighted graphs, and testing whether a given distance matrix describes a metric space. According to their results, either all of these problems have time bounds with exponents less than three, or none of them do.

The term "fine-grained reduction" comes from later work by Virginia Vassilevska Williams in an invited presentation at the 10th International Symposium on Parameterized and Exact Computation.

Although the original definition of fine-grained reductions involved deterministic algorithms, the corresponding concepts for randomized algorithms and nondeterministic algorithms have also been considered.

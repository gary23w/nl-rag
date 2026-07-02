---
title: "Minimax approximation algorithm"
source: https://en.wikipedia.org/wiki/Minimax_approximation_algorithm
domain: approximation-theory
license: CC-BY-SA-4.0
tags: approximation theory, remez algorithm, pade approximant, minimax approximation
fetched: 2026-07-02
---

# Minimax approximation algorithm

A **minimax approximation algorithm** (or **L∞ approximation** or **uniform approximation**) is a method to find an approximation of a mathematical function that minimizes maximum error.

For example, given a function f defined on the interval $[a,b]$ and a degree bound n , a minimax polynomial approximation algorithm will find a polynomial p of degree at most n to minimize

$\max _{a\leq x\leq b}|f(x)-p(x)|.$

## Polynomial approximations

The Weierstrass approximation theorem states that every continuous function defined on a closed interval [a,b] can be uniformly approximated as closely as desired by a polynomial function. For practical work it is often desirable to minimize the maximum absolute or relative error of a polynomial fit for any given number of terms in an effort to reduce computational expense of repeated evaluation.

Polynomial expansions such as the Taylor series expansion are often convenient for theoretical work but less useful for practical applications. Truncated Chebyshev series, however, closely approximate the minimax polynomial.

One popular minimax approximation algorithm is the Remez algorithm.

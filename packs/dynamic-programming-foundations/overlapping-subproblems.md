---
title: "Overlapping subproblems"
source: https://en.wikipedia.org/wiki/Overlapping_subproblems
domain: dynamic-programming-foundations
license: CC-BY-SA-4.0
tags: dynamic programming, memoization technique, optimal substructure, bellman equation
fetched: 2026-07-02
---

# Overlapping subproblems

In computer science, a problem is said to have **overlapping subproblems** if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.

For example, the problem of computing the Fibonacci sequence exhibits overlapping subproblems. The problem of computing the *n*th Fibonacci number *F*(*n*), can be broken down into the subproblems of computing *F*(*n* − 1) and *F*(*n* − 2), and then adding the two. The subproblem of computing *F*(*n* − 1) can itself be broken down into a subproblem that involves computing *F*(*n* − 2). Therefore, the computation of *F*(*n* − 2) is reused, and the Fibonacci sequence thus exhibits overlapping subproblems.

A naive recursive approach to such a problem generally fails due to an exponential complexity. If the problem also shares an optimal substructure property, dynamic programming is a good way to work it out.

## Fibonacci sequence example

In the following two implementations for calculating fibonacci sequence, `fibonacci` uses regular recursion and `fibonacci_mem` uses memoization. `fibonacci_mem` is much more efficient as the value for any particular `n` is computed only once.

| def fibonacci(n): if n <= 1: return n return fibonacci(n - 1) + fibonacci(n - 2) def fibonacci_mem(n, cache): if n <= 1: return n if n in cache: return cache[n] cache[n] = fibonacci_mem(n - 1, cache) + fibonacci_mem(n - 2, cache) return cache[n] print(fibonacci_mem(5, {})) # 5 print(fibonacci(5)) # 5 |
|---|

When executed, the `fibonacci` function computes the value of some of the numbers in the sequence many times over, whereas `fibonacci_mem` reuses the value of `n` which was computed previously:

| Recursive Version | Memoization |
|---|---|
| f(5) = f(4) + f(3) = 5 \| \| \| f(3) = f(2) + f(1) = 2 \| \| \| \| \| f(1) = 1 \| \| \| f(2) = 1 \| f(4) = f(3) + f(2) = 3 \| \| \| f(2) = 1 \| f(3) = f(2) + f(1) = 2 \| \| \| f(1) = 1 \| f(2) = 1 | f(5) = f(4) + f(3) = 5 \| \| f(4) = f(3) + f(2) = 3 \| \| f(3) = f(2) + f(1) = 2 \| \| \| f(1) = 1 \| f(2) = 1 |

The difference in performance may appear minimal with an `n` value of 5; however, as `n` increases, the computational complexity of the original `fibonacci` function grows exponentially. In contrast, the `fibonacci_mem` version exhibits a more linear increase in complexity.

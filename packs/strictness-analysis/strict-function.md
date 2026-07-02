---
title: "Strict function"
source: https://en.wikipedia.org/wiki/Strict_function
domain: strictness-analysis
license: CC-BY-SA-4.0
tags: strictness analysis, demand analysis, backwards analysis, call-by-value transformation
fetched: 2026-07-02
---

# Strict function

In computer science and computer programming, a function f is said to be **strict** if, when applied to a non-terminating expression, it also fails to terminate. A **strict function** in the denotational semantics of programming languages is a function *f* where $f\left(\perp \right)=\perp$ . The entity $\perp$ , called *bottom*, denotes an expression that does not return a normal value, either because it loops endlessly or because it aborts due to an error such as division by zero. A function that is not strict is called **non-strict**. A strict programming language is one in which user-defined functions are always strict.

Intuitively, non-strict functions correspond to control structures. Operationally, a strict function is one that always evaluates its argument; a non-strict function is one that might not evaluate some of its arguments. Functions having more than one parameter can be strict or non-strict in each parameter independently, as well as *jointly strict* in several parameters simultaneously.

As an example, the `if-then-else` expression of many programming languages, called `?:` in languages inspired by C, may be thought of as a function of three parameters. This function is strict in its first parameter, since the function must know whether its first argument evaluates to true or to false before it can return; but it is non-strict in its second parameter, because (for example) `if(false, $\perp$ ,1) = 1`, as well as non-strict in its third parameter, because (for example) `if(true,2, $\perp$ ) = 2`. However, it is jointly strict in its second and third parameters, since `if(true, $\perp$ , $\perp$ ) = $\perp$` and `if(false, $\perp$ , $\perp$ ) = $\perp$`.

In a non-strict functional programming language, strictness analysis refers to any algorithm used to prove the strictness of a function with respect to one or more of its arguments. Such functions can be compiled to a more efficient calling convention, such as call by value, without changing the meaning of the enclosing program.

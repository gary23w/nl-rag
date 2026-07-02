---
title: "Ternary search"
source: https://en.wikipedia.org/wiki/Ternary_search
domain: binary-search-algorithm
license: CC-BY-SA-4.0
tags: binary search, sorted array, logarithmic search, search algorithm
fetched: 2026-07-02
---

# Ternary search

A **ternary search algorithm** is a technique in computer science for finding the minimum or maximum of a unimodal function.

## The function

Assume we are looking for a maximum of $f(x)$ and that we know the maximum lies somewhere between A and B . For the algorithm to be applicable, there must be some value x such that

- for all $a,b$ with $A\leq a<b\leq x$ , we have $f(a)<f(b)$ , and
- for all $a,b$ with $x\leq a<b\leq B$ , we have $f(a)>f(b)$ .

## Algorithm

Let $f(x)$ be a unimodal function on some interval $[l;r]$ . Take any two points $m_{1}$ and $m_{2}$ in this segment: $l<m_{1}<m_{2}<r$ . Then there are three possibilities:

- if $f(m_{1})<f(m_{2})$ , then the required maximum can not be located on the left side – $[l;m_{1}]$ . It means that the maximum further makes sense to look only in the interval $[m_{1};r]$
- if $f(m_{1})>f(m_{2})$ , that the situation is similar to the previous, up to symmetry. Now, the required maximum can not be in the right side – $[m_{2};r]$ , so go to the segment $[l;m_{2}]$
- if $f(m_{1})=f(m_{2})$ , then the search should be conducted in $[m_{1};m_{2}]$ , but this case can be attributed to any of the previous two (in order to simplify the code). Sooner or later the length of the segment will be a little less than a predetermined constant, and the process can be stopped.

choice points $m_{1}$ and $m_{2}$ :

- $m_{1}=l+(r-l)/3$
- $m_{2}=r-(r-l)/3$

**Run time order**

$T(n)=T(2n/3)+O(1)=\Theta (\log n)$

(by the

Master Theorem

)

### Recursive algorithm

```mw
def ternary_search(f, left, right, absolute_precision) -> float:
    """Left and right are the current bounds;
    the maximum is between them.
    """
    if abs(right - left) < absolute_precision:
        return (left + right) / 2

    left_third = (2 * left + right) / 3
    right_third = (left + 2 * right) / 3

    if f(left_third) < f(right_third):
        return ternary_search(f, left_third, right, absolute_precision)
    else:
        return ternary_search(f, left, right_third, absolute_precision)
```

### Iterative algorithm

```mw
def ternary_search(f, left, right, absolute_precision) -> float:
    """Find maximum of unimodal function f() within [left, right].
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while abs(right - left) >= absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third

    # Left and right are the current bounds; the maximum is between them
    return (left + right) / 2
```

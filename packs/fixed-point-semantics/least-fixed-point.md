---
title: "Least fixed point"
source: https://en.wikipedia.org/wiki/Least_fixed_point
domain: fixed-point-semantics
license: CC-BY-SA-4.0
tags: least fixed point, Kleene fixed-point theorem, Knaster-Tarski theorem, fixed-point combinator
fetched: 2026-07-02
---

# Least fixed point

In order theory, a branch of mathematics, the **least fixed point** (**lfp** or **LFP**, sometimes also **smallest fixed point**) of a function from a partially ordered set ("poset" for short) to itself is the fixed point which is less than each other fixed point, according to the order of the poset. A function need not have a least fixed point, but if it does, then the least fixed point is unique.

## Examples

With the usual order on the real numbers, the least fixed point of the real function *f*(*x*) = *x*2 is *x* = 0 (since the only other fixed point is 1 and 0 < 1). In contrast, *f*(*x*) = *x* + 1 has no fixed points at all, so has no least one, and *f*(*x*) = *x* has infinitely many fixed points, but has no least one.

Let $G=(V,A)$ be a directed graph and v be a vertex. The set of vertices accessible from v can be defined as the least fixed-point of the function $f:\wp (V)\to \wp (V)$ , defined as $f(X)=\{v\}\cup \{x\in V:{\text{ for some }}w\in X{\text{ there is an edge from }}w{\text{ to }}x\}.$ The set of vertices which are co-accessible from v is defined by a similar least fix-point. The strongly connected component of v is the intersection of those two least fixed-points.

Let $G=(V,\Sigma ,R,S_{0})$ be a context-free grammar. The set E of symbols which produces the empty string $\varepsilon$ can be obtained as the least fixed-point of the function $f:\wp (V)\to \wp (V)$ , defined as $f(X)=\{S\in V:\;S\in X{\text{ or }}(S\to \varepsilon )\in R{\text{ or }}(S\to S^{1}\dots S^{n})\in R{\text{ and }}S^{i}\in X{\text{, for all }}i\}$ , where $\wp (V)$ denotes the power set of V .

## Applications

Many fixed-point theorems yield algorithms for locating the least fixed point. Least fixed points often have desirable properties that arbitrary fixed points do not.

### Denotational semantics

In computer science, the *denotational semantics* approach uses least fixed points to obtain from a given program text a corresponding mathematical function, called its semantics. To this end, an artificial mathematical object, $\bot$ , is introduced, denoting the exceptional value "undefined". Given e.g. the program datatype `int`, its mathematical counterpart is defined as $\mathbb {Z} _{\bot }=\mathbb {Z} \cup \{\bot \};$ it is made a partially ordered set by defining $\bot \sqsubset n$ for each $n\in \mathbb {Z}$ and letting any two different members $n,m\in \mathbb {Z}$ be uncomparable w.r.t. $\sqsubset$ , see picture.

The semantics of a program definition `int f(int n){...}` is some mathematical function $f:\mathbb {Z} _{\bot }\to \mathbb {Z} _{\bot }.$ If the program definition `f` does not terminate for some input `n`, this can be expressed mathematically as $f(n)=\bot .$ The set of all mathematical functions is made partially ordered by defining $f\sqsubseteq g$ if, for each $n,$ the relation $f(n)\sqsubseteq g(n)$ holds, that is, if $f(n)$ is less defined or equal to $g(n).$ For example, the semantics of the expression `x+x/x` is less defined than that of `x+1`, since the former, but not the latter, maps 0 to $\bot ,$ and they agree otherwise.

Given some program text `f`, its mathematical counterpart is obtained as least fixed point of some mapping from functions to functions that can be obtained by "translating" `f`. For example, the C definition

```mw
int fact(int n) { if (n == 0) return 1; else return n * fact(n-1); }
```

is translated to a mapping

$F:(\mathbb {Z} _{\bot }\to \mathbb {Z} _{\bot })\to (\mathbb {Z} _{\bot }\to \mathbb {Z} _{\bot }),$

defined as

$(F(f))(n)={\begin{cases}1&{\text{if }}n=0,\\n\cdot f(n-1)&{\text{if }}n\neq \bot {\text{ and }}n\neq 0,\\\bot &{\text{if }}n=\bot .\\\end{cases}}$

The mapping F is defined in a non-recursive way, although `fact` was defined recursively. Under certain restrictions (see Kleene fixed-point theorem), which are met in the example, F necessarily has a least fixed point, $\operatorname {fact}$ , that is $(F(\operatorname {fact} ))(n)=\operatorname {fact} (n)$ for all $n\in \mathbb {Z} _{\bot }$ . It is possible to show that

$\operatorname {fact} (n)={\begin{cases}n!&{\text{if }}n\geq 0,\\\bot &{\text{if }}n<0{\text{ or }}n=\bot .\end{cases}}$

A larger fixed point of F is e.g. the function $\operatorname {fact} _{0},$ defined by

$\operatorname {fact} _{0}(n)={\begin{cases}n!&{\text{if }}n\geq 0,\\0&{\text{if }}n<0,\\\bot &{\text{if }}n=\bot ,\end{cases}}$

however, this function does not correctly reflect the behavior of the above program text for negative $n;$ e.g. the call `fact(-1)` will not terminate at all, let alone return `0`. Only the *least* fixed point, $\operatorname {fact} ,$ can reasonably be used as a mathematical program semantic.

### Descriptive complexity

Immerman and Vardi independently showed the descriptive complexity result that the polynomial-time computable properties of linearly ordered structures are definable in FO(LFP), i.e. in first-order logic with a least fixed point operator. However, FO(LFP) is too weak to express all polynomial-time properties of unordered structures (for instance that a structure has even size).

## Greatest fixed points

The greatest fixed point of a function can be defined analogously to the least fixed point, as the fixed point which is greater than any other fixed point, according to the order of the poset. In computer science, greatest fixed points are much less commonly used than least fixed points. Specifically, the posets found in domain theory usually do not have a greatest element, hence for a given function, there may be multiple, mutually incomparable maximal fixed points, and the greatest fixed point of that function may not exist. To address this issue, the *optimal fixed point* has been defined as the most-defined fixed point compatible with all other fixed points. The optimal fixed point always exists, and is the greatest fixed point if the greatest fixed point exists. The optimal fixed point allows formal study of recursive and corecursive functions that do not converge with the least fixed point. Unfortunately, whereas Kleene's recursion theorem shows that the least fixed point is effectively computable, the optimal fixed point of a computable function may be a non-computable function.

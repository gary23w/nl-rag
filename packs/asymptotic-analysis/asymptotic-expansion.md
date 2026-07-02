---
title: "Asymptotic expansion"
source: https://en.wikipedia.org/wiki/Asymptotic_expansion
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Asymptotic expansion

In mathematics, an **asymptotic expansion**, **asymptotic series** or **Poincaré expansion** (after Henri Poincaré) is a formal series of functions which has the property that truncating the series after a finite number of terms provides an approximation to a given function as the argument of the function tends towards a particular, often infinite, point. Investigations by Dingle (1973) revealed that the divergent part of an asymptotic expansion is latently meaningful, i.e. contains information about the exact value of the expanded function.

Poincaré and Stieltjes independently developed the theory of asymptotic expansions in 1886.

The most common type of asymptotic expansion is a power series in either positive or negative powers. Methods of generating such expansions include the Euler–Maclaurin summation formula and integral transforms such as the Laplace and Mellin transforms. Repeated integration by parts will often lead to an asymptotic expansion.

Since a *convergent* Taylor series fits the definition of asymptotic expansion as well, the phrase "asymptotic series" usually implies a *non-convergent* series. Despite non-convergence, the asymptotic expansion is useful when truncated to a finite number of terms. The approximation may provide benefits by being more mathematically tractable than the function being expanded, or by an increase in the speed of computation of the expanded function. Typically, the best approximation is given when the series is truncated at the smallest term. This way of optimally truncating an asymptotic expansion is known as **superasymptotics**. The error is then typically of the form ~ exp(−*c*/*ε*) where *ε* is the expansion parameter. The error is thus beyond all orders in the expansion parameter. It is possible to improve on the superasymptotic error, e.g. by employing resummation methods such as Borel resummation to the divergent tail. Such methods are often referred to as **hyperasymptotic approximations**.

See asymptotic analysis and big O notation for the notation used in this article.

## Formal definition

First we define an asymptotic scale, and then give the formal definition of an asymptotic expansion.

If $\varphi _{n}$ is a sequence of continuous functions of *asymptotic variable* ${\textstyle x}$ on some domain, and if L is a limit point of the domain, then the sequence constitutes an **asymptotic scale** if for every n,

$\varphi _{n+1}(x)=o(\varphi _{n}(x))\quad (x\to L)\ .$

Commonly, L is taken to be zero or infinity. In other words, a sequence of functions is an asymptotic scale if each function in the sequence grows strictly slower (in the limit ⁠ $x\to L$ ⁠) than the preceding function.

If f is a continuous function on the domain of the asymptotic scale, then *f* has a standard asymptotic expansion of order N with respect to the scale as a formal series

$\sum _{n=0}^{N}a_{n}\varphi _{n}(x)$

if

$f(x)-\sum _{n=0}^{N-1}a_{n}\varphi _{n}(x)=O(\varphi _{N}(x))\quad (x\to L)$

or the weaker condition

$f(x)-\sum _{n=0}^{N-1}a_{n}\varphi _{n}(x)=o(\varphi _{N-1}(x))\quad (x\to L)\$

is satisfied. Here, o is the little o notation. If one or the other holds for all ⁠ N ⁠, then we write

$f(x)\sim \sum _{n=0}^{\infty }a_{n}\varphi _{n}(x)\quad (x\to L)\ .$

In contrast to a convergent series for ⁠ f ⁠, wherein the series converges for any *fixed* x in the limit ⁠ $N\to \infty$ ⁠, one can think of the asymptotic series as converging for *fixed* N in the limit $x\to L$ (with L possibly infinite).

## Examples

- Gamma function (Stirling's approximation) ${\frac {e^{x}}{x^{x}{\sqrt {2\pi x}}}}\Gamma (x+1)\sim 1+{\frac {1}{12x}}+{\frac {1}{288x^{2}}}-{\frac {139}{51840x^{3}}}-\cdots \ (x\to \infty )$
- Exponential integral $xe^{x}E_{1}(x)\sim \sum _{n=0}^{\infty }{\frac {(-1)^{n}n!}{x^{n}}}\ (x\to \infty )$
- Logarithmic integral $\operatorname {li} (x)\sim {\frac {x}{\ln x}}\sum _{k=0}^{\infty }{\frac {k!}{(\ln x)^{k}}}$
- Riemann zeta function $\zeta (s)\sim \sum _{n=1}^{N}n^{-s}+{\frac {N^{1-s}}{s-1}}-{\frac {N^{-s}}{2}}+N^{-s}\sum _{m=1}^{\infty }{\frac {B_{2m}s^{\overline {2m-1}}}{(2m)!N^{2m-1}}}$ where $B_{2m}$ are Bernoulli numbers and $s^{\overline {2m-1}}$ is a rising factorial. This expansion is valid for all complex *s* and is often used to compute the zeta function by using a large enough value of *N*, for instance ⁠ $N>\vert s\vert$ ⁠.
- Error function ${\sqrt {\pi }}xe^{x^{2}}{\rm {erfc}}(x)\sim 1+\sum _{n=1}^{\infty }(-1)^{n}{\frac {(2n-1)!!}{(2x^{2})^{n}}}\ (x\to \infty )$ where (2*n* − 1)!! is the double factorial.

## Worked example

Asymptotic expansions often occur when an ordinary series is used in a formal expression that forces the taking of values outside of its domain of convergence. Thus, for example, one may start with the ordinary series

${\frac {1}{1-w}}=\sum _{n=0}^{\infty }w^{n}.$

The expression on the left is valid on the entire complex plane $w\neq 1$ , while the right hand side converges only for ⁠ $\vert w\vert <1$ ⁠. Multiplying by $e^{-w/t}$ and integrating both sides yields

$\int _{0}^{\infty }{\frac {e^{-{\frac {w}{t}}}}{1-w}}\,dw=\sum _{n=0}^{\infty }t^{n+1}\int _{0}^{\infty }e^{-u}u^{n}\,du,$

after the substitution $u=w/t$ on the right hand side. The integral on the left hand side, understood as a Cauchy principal value, can be expressed in terms of the exponential integral. The integral on the right hand side may be recognized as the gamma function. Evaluating both, one obtains the asymptotic expansion

$e^{-{\frac {1}{t}}}\operatorname {Ei} \left({\frac {1}{t}}\right)=\sum _{n=0}^{\infty }n!t^{n+1}.$

Here, the right hand side is clearly not convergent for any non-zero value of *t*. However, by truncating the series on the right to a finite number of terms, one may obtain a fairly good approximation to the value of $\operatorname {Ei} \left({\tfrac {1}{t}}\right)$ for sufficiently small *t*. Substituting $x=-{\tfrac {1}{t}}$ and noting that $\operatorname {Ei} (x)=-E_{1}(-x)$ results in the asymptotic expansion given earlier in this article.

### Integration by parts

Using integration by parts, we can obtain an explicit formula $\operatorname {Ei} (z)={\frac {e^{z}}{z}}\left(\sum _{k=0}^{n}{\frac {k!}{z^{k}}}+e_{n}(z)\right),\quad e_{n}(z)\equiv (n+1)!\ ze^{-z}\int _{-\infty }^{z}{\frac {e^{t}}{t^{n+2}}}\,dt$ For any fixed z , the absolute value of the error term $|e_{n}(z)|$ decreases, then increases. The minimum occurs at ⁠ $n\sim \vert z\vert$ ⁠, at which point $\textstyle \vert e_{n}(z)\vert \leq {\sqrt {\frac {2\pi }{\vert z\vert }}}e^{-\vert z\vert }$ . This bound is said to be "asymptotics beyond all orders".

## Properties

### Uniqueness for a given asymptotic scale

For a given asymptotic scale $\{\varphi _{n}(x)\}$ the asymptotic expansion of function $f(x)$ is unique. That is the coefficients $\{a_{n}\}$ are uniquely determined in the following way: ${\begin{aligned}a_{0}&=\lim _{x\to L}{\frac {f(x)}{\varphi _{0}(x)}}\\a_{1}&=\lim _{x\to L}{\frac {f(x)-a_{0}\varphi _{0}(x)}{\varphi _{1}(x)}}\\&\;\;\vdots \\a_{N}&=\lim _{x\to L}{\frac {f(x)-\sum _{n=0}^{N-1}a_{n}\varphi _{n}(x)}{\varphi _{N}(x)}}\end{aligned}}$ where L is the limit point of this asymptotic expansion (may be ⁠ $\pm \infty$ ⁠).

### Non-uniqueness for a given function

A given function $f(x)$ may have many asymptotic expansions (each with a different asymptotic scale).

### Subdominance

An asymptotic expansion may be an asymptotic expansion to more than one function.

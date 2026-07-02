---
title: "Uniform convergence"
source: https://en.wikipedia.org/wiki/Uniform_convergence
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
---

# Uniform convergence

In the mathematical field of analysis, **uniform convergence** is a mode of convergence of functions stronger than pointwise convergence. A sequence of functions $(f_{n})$ **converges uniformly** to a limiting function f if, roughly speaking, they **uniformly approximate** the function f over the whole domain, meaning that all but finitely many of the functions of the sequence lie in a uniform error bar of the original function. Graphically this means that, given any thin band around the graph of f , the graphs of all but finitely many of the functions $f_{n}$ lie within that thin band. This is in contrast to pointwise convergence, in which all but finitely many of the functions lie in a thin band at each point, but the finite set of functions which must be excluded in order for that to be the case varies from point to point.

The strength of uniform convergence makes it ideal in many applications, where pointwise convergence is not sufficient. For example, the uniform limit of a sequence of continuous functions is automatically continuous; the uniform limit of Riemann integrable functions is automatically Riemann integrable. With additional hypotheses, differentiability can be transferred to the limit function as well. The difference between uniform convergence and pointwise convergence was not fully appreciated early in the history of calculus, leading to instances of faulty reasoning. The concept was first formalized by Karl Weierstrass.

## History

In 1821 Augustin-Louis Cauchy published a proof that a convergent sum of continuous functions is always continuous, to which Niels Henrik Abel in 1826 found purported counterexamples in the context of Fourier series, arguing that Cauchy's proof had to be incorrect. Completely standard notions of convergence did not exist at the time, and Cauchy handled convergence using infinitesimal methods. When put into the modern language, what Cauchy proved is that a uniformly convergent sequence of continuous functions has a continuous limit. The failure of a merely pointwise-convergent limit of continuous functions to converge to a continuous function illustrates the importance of distinguishing between different types of convergence when handling sequences of functions.

The term uniform convergence was probably first used by Christoph Gudermann, in an 1838 paper on elliptic functions, where he employed the phrase "convergence in a uniform way" when the "mode of convergence" of a series ${\textstyle \sum _{n=1}^{\infty }f_{n}(x,\phi ,\psi )}$ is independent of the variables $\phi$ and $\psi .$ While he thought it a "remarkable fact" when a series converged in this way, he did not give a formal definition, nor use the property in any of his proofs.

Later Gudermann's pupil, Karl Weierstrass, who attended his course on elliptic functions in 1839–1840, coined the term *gleichmäßig konvergent* (German: *uniformly convergent*) which he used in his 1841 paper *Zur Theorie der Potenzreihen*, published in 1894. Independently, similar concepts were articulated by Philipp Ludwig von Seidel and George Gabriel Stokes. G. H. Hardy compares the three definitions in his paper "Sir George Stokes and the concept of uniform convergence" and remarks: "Weierstrass's discovery was the earliest, and he alone fully realized its far-reaching importance as one of the fundamental ideas of analysis."

Under the influence of Weierstrass and Bernhard Riemann this concept and related questions were intensely studied at the end of the 19th century by Hermann Hankel, Paul du Bois-Reymond, Ulisse Dini, Cesare Arzelà and others.

## Definition

We first define uniform convergence for real-valued functions, although the concept is readily generalized to functions mapping to metric spaces and, more generally, uniform spaces (see below).

Suppose E is a set and $(f_{n})_{n\in \mathbb {N} }$ is a sequence of real-valued functions defined on it. We say the sequence $(f_{n})_{n\in \mathbb {N} }$ is **uniformly convergent** on E with limit $f:E\to \mathbb {R}$ if for every $\varepsilon >0,$ there exists a natural number N such that for all $n\geq N$ and for all $x\in E$

${\bigl |}f_{n}(x)-f(x){\bigr |}<\varepsilon .$

The notation for uniform convergence of $f_{n}$ to f is not quite standardized and different authors have used a variety of symbols, including (in roughly decreasing order of popularity):

$f_{n}\rightrightarrows f,\quad {\underset {n\to \infty }{\mathrm {unif\ lim} }}f_{n}=f,\quad f_{n}{\overset {\mathrm {unif.} }{\longrightarrow }}f,\quad f=\mathrm {u} \!\!-\!\!\!\lim _{n\to \infty }f_{n}.$

Frequently, no special symbol is used, and authors simply write

$f_{n}\to f\quad \mathrm {uniformly}$

to indicate that convergence is uniform. (In contrast, the expression $f_{n}\to f$ on E without an adverb is taken to mean pointwise convergence on E : for all $x\in E$ , $f_{n}(x)\to f(x)$ as $n\to \infty$ .)

Since $\mathbb {R}$ is a complete metric space, the Cauchy criterion can be used to give an equivalent alternative formulation for uniform convergence: $(f_{n})_{n\in \mathbb {N} }$ converges uniformly on E (in the previous sense) if and only if for every $\varepsilon >0$ , there exists a natural number N such that

$x\in E,m,n\geq N\implies {\bigl |}f_{m}(x)-f_{n}(x){\bigr |}<\varepsilon$

.

In yet another equivalent formulation (derived by using the definition of limit and supremum), if we define

$d_{n}=\sup _{x\in E}{\bigl |}f_{n}(x)-f(x){\bigr |},$

then $f_{n}$ converges to f uniformly if and only if $d_{n}\to 0$ as $n\to \infty$ . Thus, we can characterize uniform convergence of $\textstyle (f_{n})_{n\in \mathbb {N} }$ on E as (simple) convergence of $(f_{n})_{n\in \mathbb {N} }$ in the function space $\mathbb {R} ^{E}$ with respect to the *uniform metric* (also called the supremum metric), defined by

$d(f,g)=\sup _{x\in E}{\bigl |}f(x)-g(x){\bigr |}.$

Symbolically,

$f_{n}\rightrightarrows f\iff d(f_{n},f)\to 0$

.

The sequence $(f_{n})_{n\in \mathbb {N} }$ is said to be **locally uniformly convergent** with limit f if E is a metric space and for every $x\in E$ , there exists an $r>0$ such that $(f_{n})$ converges uniformly on $B(x,r)\cap E$ where $B(x,r)$ is a ball centered at *x* with the radius *r*. It is clear that uniform convergence implies local uniform convergence, which implies pointwise convergence.

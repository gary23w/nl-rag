---
title: "Continued fraction"
source: https://en.wikipedia.org/wiki/Continued_fraction
domain: euclidean-gcd
license: CC-BY-SA-4.0
tags: euclidean algorithm, greatest common divisor, modular arithmetic, number theory
fetched: 2026-07-02
---

# Continued fraction

$b_{0}+{\cfrac {a_{1}}{b_{1}+{\cfrac {a_{2}}{b_{2}+{\cfrac {a_{3}}{b_{3}+\ddots }}}}}}$

An infinite continued fraction is defined by the sequences

$\{a_{i}\},\{b_{i}\}$

, for

$i=0,1,2,\ldots$

, with

$a_{0}=0$

.

A **continued fraction** is a mathematical expression written as a fraction whose denominator contains a sum involving another fraction, which may itself be a simple or a continued fraction. If this iteration (repetitive process) terminates with a simple fraction, the result is a **finite continued fraction**; if it continues indefinitely, the result is an **infinite continued fraction**. The special case in which all numerators $\{a_{i}\}$ (see image) are equal to one, and all denominators $\{b_{i}\}$ are positive integers, is referred to as a simple (or regular) continued fraction. Any positive rational number can be expressed as a finite simple continued fraction, and any positive irrational number can be expressed as an infinite simple continued fraction.

Different areas of mathematics use different terminology and notation for continued fractions. In number theory, the unqualified term *continued fraction* usually refers to simple continued fractions, whereas the general case is referred to as **generalized continued fractions**. In complex analysis and numerical analysis, the general case is usually referred to by the unqualified term *continued fraction*.

The numerators and denominators of continued fractions can be sequences $\{a_{i}\},\{b_{i}\}$ of numbers or functions.

## Formulation

A continued fraction is an expression of the form $x=b_{0}+{\cfrac {a_{1}}{b_{1}+{\cfrac {a_{2}}{b_{2}+{\cfrac {a_{3}}{b_{3}+{\cfrac {a_{4}}{b_{4}+\ddots \,}}}}}}}}$ where the *a**n* (*n* > 0) are the ***partial numerators***, the *b**n* are the ***partial denominators***, and the leading term *b*0 is called the *integer part* of the continued fraction.

The successive **convergents** of the continued fraction are formed by applying the **fundamental recurrence formulas**: ${\begin{aligned}x_{0}&={\frac {A_{0}}{B_{0}}}=b_{0},\\x_{1}&={\frac {A_{1}}{B_{1}}}={\frac {b_{1}b_{0}+a_{1}}{b_{1}}},\\x_{2}&={\frac {A_{2}}{B_{2}}}={\frac {b_{2}(b_{1}b_{0}+a_{1})+a_{2}b_{0}}{b_{2}b_{1}+a_{2}}},\ \dots \end{aligned}}$ where *A**n* is the numerator and *B**n* is the denominator, called *continuants*, of the *n*th convergent. They are given by the three-term recurrence relation ${\begin{aligned}A_{n}&=b_{n}A_{n-1}+a_{n}A_{n-2},\\B_{n}&=b_{n}B_{n-1}+a_{n}B_{n-2}\qquad {\text{for }}n\geq 1\end{aligned}}$ with initial values ${\begin{aligned}A_{-1}&=1,&A_{0}&=b_{0},\\B_{-1}&=0,&B_{0}&=1.\end{aligned}}$

If the sequence of convergents {*x**n*} approaches a limit, the continued fraction is convergent and has a definite value. If the sequence of convergents never approaches a limit, the continued fraction is divergent. It may diverge by oscillation (for example, the odd and even convergents may approach two different limits), or it may produce an infinite number of zero denominators *B**n*.

## History

The story of continued fractions begins with the Euclidean algorithm, a procedure for finding the greatest common divisor of two natural numbers *m* and *n*. That algorithm introduced the idea of dividing to extract a new remainder – and then dividing by the new remainder repeatedly.

Nearly two thousand years passed before Bombelli (1579) devised a technique for approximating the roots of quadratic equations with continued fractions in the mid-sixteenth century. Now the pace of development quickened. Just 24 years later, in 1613, Pietro Cataldi introduced the first formal notation for the generalized continued fraction. Cataldi represented a continued fraction as ${a_{0}\cdot }\,\&\,{\frac {n_{1}}{d_{1}\cdot }}\,\&\,{\frac {n_{2}}{d_{2}\cdot }}\,\&\,{\frac {n_{3}}{d_{3}}}$ with the dots indicating where the next fraction goes, and each & representing a modern plus sign.

Late in the seventeenth century John Wallis introduced the term "continued fraction" into mathematical literature. New techniques for mathematical analysis (Newton's and Leibniz's calculus) had recently come onto the scene, and a generation of Wallis' contemporaries put the new phrase to use.

In 1748 Euler published a theorem showing that a particular kind of continued fraction is equivalent to a certain very general infinite series. Euler's continued fraction formula is still the basis of many modern proofs of convergence of continued fractions.

In 1761, Johann Heinrich Lambert gave the first proof that π is irrational, by using the following continued fraction for tan *x*: $\tan(x)={\cfrac {x}{1+{\cfrac {-x^{2}}{3+{\cfrac {-x^{2}}{5+{\cfrac {-x^{2}}{7+{}\ddots }}}}}}}}$

Continued fractions can also be applied to problems in number theory, and are especially useful in the study of Diophantine equations. In the late eighteenth century Lagrange used continued fractions to construct the general solution of Pell's equation, thus answering a question that had fascinated mathematicians for more than a thousand years. Lagrange's discovery implies that the canonical continued fraction expansion of the square root of every non-square integer is periodic and that, if the period is of length *p* > 1, it contains a palindromic string of length *p* − 1.

In 1813 Gauss derived from complex-valued hypergeometric functions what are now called Gauss's continued fractions. They can be used to express many elementary functions and some more advanced functions (such as the Bessel functions), as continued fractions that are rapidly convergent almost everywhere in the complex plane.

## Notation

The long continued fraction expression displayed in the introduction is easy for an unfamiliar reader to interpret. However, it takes up a lot of space and can be difficult to typeset. So mathematicians have devised several alternative notations. One convenient way to express a generalized continued fraction sets each nested fraction on the same line, indicating the nesting by dangling plus signs in the denominators: $x=b_{0}+{\frac {a_{1}}{b_{1}+}}\,{\frac {a_{2}}{b_{2}+}}\,{\frac {a_{3}}{b_{3}+\cdots }}$

Sometimes the plus signs are typeset to vertically align with the denominators but not under the fraction bars: $x=b_{0}+{\frac {a_{1}}{b_{1}}}{{} \atop +}{\frac {a_{2}}{b_{2}}}{{} \atop +}{\frac {a_{3}}{b_{3}}}{{} \atop \!{}+\cdots }$

Pringsheim wrote a generalized continued fraction this way: $x=b_{0}+{{} \atop {{\big |}\!}}\!{\frac {a_{1}}{\,b_{1}\,}}\!{{\!{\big |}} \atop {}}+{{} \atop {{\big |}\!}}\!{\frac {a_{2}}{\,b_{2}\,}}\!{{\!{\big |}} \atop {}}+{{} \atop {{\big |}\!}}\!{\frac {a_{3}}{\,b_{3}\,}}\!{{\!{\big |}} \atop {}}+\cdots$

Carl Friedrich Gauss evoked the more familiar infinite product ∏ when he devised this notation: $x=b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}.$ Here, the "K" stands for *Kettenbruch*, the German word for "continued fraction". This is probably the most compact and convenient way to express continued fractions; however, it is not widely used by English typesetters. (Usually the K should be the same size as ∑ used for a sum or ∏ used for a product, but within this article K appears much smaller than those due to technical limitations.)

## Some elementary considerations

Here are some elementary results that are of fundamental importance in the further development of the analytic theory of continued fractions.

### Partial numerators and denominators

If one of the partial numerators *a**n*+1 is zero, the infinite continued fraction $b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}$ is really just a finite continued fraction with n fractional terms, and therefore a rational function of *a*1 to an and *b*0 to *b**n*+1. Such an object is of little interest from the point of view adopted in mathematical analysis, so it is usually assumed that all *ai* ≠ 0. There is no need to place this restriction on the partial denominators bi.

### The determinant formula

When the *n*th convergent of a continued fraction $x_{n}=b_{0}+{\underset {i=1}{\overset {n}{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}$ is expressed as a simple fraction *x**n* = ⁠*A**n*/*B**n*⁠ we can use the *determinant formula*

| $A_{n-1}B_{n}-A_{n}B_{n-1}=\left(-1\right)^{n}a_{1}a_{2}\cdots a_{n}=\prod _{i=1}^{n}(-a_{i})$ |   | 1 |
|---|---|---|

to relate the numerators and denominators of successive convergents *x**n* and *x**n* − 1 to one another. The proof for this can be easily seen by induction.

| Proof |
|---|
| **Base case** The case *n* = 1 results from a very simple computation. **Inductive step** Assume that (**1**) holds for *n* − 1. Then we need to see the same relation holding true for *n*. Substituting the value of *An* and *Bn* in (**1**) we obtain: ${\begin{aligned}&=b_{n}A_{n-1}B_{n-1}+a_{n}A_{n-1}B_{n-2}-b_{n}A_{n-1}B_{n-1}-a_{n}A_{n-2}B_{n-1}\\&=a_{n}(A_{n-1}B_{n-2}-A_{n-2}B_{n-1})\end{aligned}}$ which is true because of our induction hypothesis. $A_{n-1}B_{n}-A_{n}B_{n-1}=\left(-1\right)^{n}a_{1}a_{2}\cdots a_{n}=\prod _{i=1}^{n}(-a_{i})$ Specifically, if neither *B**n* nor *B**n* − 1 is zero (*n* > 0) we can express the difference between the (*n* − 1)th and *n*th convergents like this: $x_{n-1}-x_{n}={\frac {A_{n-1}}{B_{n-1}}}-{\frac {A_{n}}{B_{n}}}=\left(-1\right)^{n}{\frac {a_{1}a_{2}\cdots a_{n}}{B_{n}B_{n-1}}}={\frac {\prod _{i=1}^{n}(-a_{i})}{B_{n}B_{n-1}}}.$ |

### The equivalence transformation

If {*ci*} = {*c*1, *c*2, *c*3, ...} is any infinite sequence of non-zero complex numbers we can prove, by induction, that $b_{0}+{\cfrac {a_{1}}{b_{1}+{\cfrac {a_{2}}{b_{2}+{\cfrac {a_{3}}{b_{3}+{\cfrac {a_{4}}{b_{4}+\ddots \,}}}}}}}}=b_{0}+{\cfrac {c_{1}a_{1}}{c_{1}b_{1}+{\cfrac {c_{1}c_{2}a_{2}}{c_{2}b_{2}+{\cfrac {c_{2}c_{3}a_{3}}{c_{3}b_{3}+{\cfrac {c_{3}c_{4}a_{4}}{c_{4}b_{4}+\ddots \,}}}}}}}}$ where equality is understood as equivalence, which is to say that the successive convergents of the continued fraction on the left are exactly the same as the convergents of the fraction on the right.

The equivalence transformation is perfectly general, but two particular cases deserve special mention. First, if none of the ai are zero, a sequence {*ci*} can be chosen to make each partial numerator a 1: $b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}=b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {1}{c_{i}b_{i}}}$ where *c*1 = ⁠1/*a*1⁠, *c*2 = ⁠*a*1/*a*2⁠, *c*3 = ⁠*a*2/*a*1*a*3⁠, and in general *c**n*+1 = ⁠1/*a**n*+1*cn*⁠.

Second, if none of the partial denominators bi are zero we can use a similar procedure to choose another sequence {*di*} to make each partial denominator a 1: $b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}=b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {d_{i}a_{i}}{1}}$ where *d*1 = ⁠1/*b*1⁠ and otherwise *d**n*+1 = ⁠1/*bnb**n*+1⁠.

These two special cases of the equivalence transformation are enormously useful when the general convergence problem is analyzed.

### Notions of convergence

As mentioned in the introduction, the continued fraction $x=b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}$ converges if the sequence of convergents {*x**n*} tends to a finite limit. This notion of convergence is very natural, but it is sometimes too restrictive. It is therefore useful to introduce the notion of general convergence of a continued fraction. Roughly speaking, this consists in replacing the $\operatorname {K} _{i=n}^{\infty }{\tfrac {a_{i}}{b_{i}}}$ part of the fraction by *w**n*, instead of by 0, to compute the convergents. The convergents thus obtained are called *modified convergents*. We say that the continued fraction *converges generally* if there exists a sequence $\{w_{n}^{*}\}$ such that the sequence of modified convergents converges for all $\{w_{n}\}$ sufficiently distinct from $\{w_{n}^{*}\}$ . The sequence $\{w_{n}^{*}\}$ is then called an *exceptional sequence* for the continued fraction. See Chapter 2 of Lorentzen & Waadeland (1992) for a rigorous definition.

There also exists a notion of absolute convergence for continued fractions, which is based on the notion of absolute convergence of a series: a continued fraction is said to be *absolutely convergent* when the series $f=\sum _{n}\left(f_{n}-f_{n-1}\right),$ where $f_{n}=\operatorname {K} _{i=1}^{n}{\tfrac {a_{i}}{b_{i}}}$ are the convergents of the continued fraction, converges absolutely. The Śleszyński–Pringsheim theorem provides a sufficient condition for absolute convergence.

Finally, a continued fraction of one or more complex variables is *uniformly convergent* in an open neighborhood Ω when its convergents converge uniformly on Ω; that is, when for every *ε* > 0 there exists *M* such that for all *n* > *M*, for all $z\in \Omega$ , $|f(z)-f_{n}(z)|<\varepsilon .$

### Even and odd convergents

It is sometimes necessary to separate a continued fraction into its even and odd parts. For example, if the continued fraction diverges by oscillation between two distinct limit points *p* and *q*, then the sequence {*x*0, *x*2, *x*4, ...} must converge to one of these, and {*x*1, *x*3, *x*5, ...} must converge to the other. In such a situation it may be convenient to express the original continued fraction as two different continued fractions, one of them converging to *p*, and the other converging to *q*.

The formulas for the even and odd parts of a continued fraction can be written most compactly if the fraction has already been transformed so that all its partial denominators are unity. Specifically, if $x={\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{1}}$ is a continued fraction, then the even part *x*even and the odd part *x*odd are given by $x_{\text{even}}={\cfrac {a_{1}}{1+a_{2}-{\cfrac {a_{2}a_{3}}{1+a_{3}+a_{4}-{\cfrac {a_{4}a_{5}}{1+a_{5}+a_{6}-{\cfrac {a_{6}a_{7}}{1+a_{7}+a_{8}-\ddots }}}}}}}}$ and $x_{\text{odd}}=a_{1}-{\cfrac {a_{1}a_{2}}{1+a_{2}+a_{3}-{\cfrac {a_{3}a_{4}}{1+a_{4}+a_{5}-{\cfrac {a_{5}a_{6}}{1+a_{6}+a_{7}-{\cfrac {a_{7}a_{8}}{1+a_{8}+a_{9}-\ddots }}}}}}}}$ respectively. More precisely, if the successive convergents of the continued fraction *x* are {*x*1, *x*2, *x*3, ...}, then the successive convergents of *x*even as written above are {*x*2, *x*4, *x*6, ...}, and the successive convergents of *x*odd are {*x*1, *x*3, *x*5, ...}.

### Conditions for irrationality

If *a*1, *a*2,... and *b*1, *b*2,... are positive integers with *ak* ≤ *bk* for all sufficiently large *k*, then $x=b_{0}+{\underset {i=1}{\overset {\infty }{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}$ converges to an irrational limit.

### Fundamental recurrence formulas

The partial numerators and denominators of the fraction's successive convergents are related by the *fundamental recurrence formulas*: ${\begin{aligned}A_{-1}&=1&B_{-1}&=0\\A_{0}&=b_{0}&B_{0}&=1\\A_{n+1}&=b_{n+1}A_{n}+a_{n+1}A_{n-1}&B_{n+1}&=b_{n+1}B_{n}+a_{n+1}B_{n-1}\end{aligned}}$

The continued fraction's successive convergents are then given by $x_{n}={\frac {A_{n}}{B_{n}}}.$

These recurrence relations are due to John Wallis (1616–1703) and Leonhard Euler (1707–1783). These recurrence relations are simply a different notation for the relations obtained by Pietro Antonio Cataldi (1548-1626).

As an example, consider the simple continued fraction in canonical form that represents the golden ratio φ: $\varphi =1+{\cfrac {1}{1+{\cfrac {1}{1+{\cfrac {1}{1+{\cfrac {1}{1+\ddots \,}}}}}}}}$

Applying the fundamental recurrence formulas we find that the successive numerators *A**n* are {1, 2, 3, 5, 8, 13, ...} and the successive denominators *B**n* are {1, 1, 2, 3, 5, 8, ...}, the Fibonacci numbers. Since all the partial numerators in this example are equal to one, the determinant formula assures us that the absolute value of the difference between successive convergents approaches zero quite rapidly.

## Linear fractional transformations

A linear fractional transformation (LFT) is a complex function of the form $w=f(z)={\frac {az+b}{cz+d}},$ where z is a complex variable, and *a*, *b*, *c*, *d* are arbitrary complex constants such that *cz* + *d* ≠ 0. An additional restriction that *ad* ≠ *bc* is customarily imposed, to rule out the cases in which *w* = *f*(*z*) is a constant. The linear fractional transformation, also known as a Möbius transformation, has many fascinating properties. Four of these are of primary importance in developing the analytic theory of continued fractions.

- If *c* ≠ 0 the LFT has one or two fixed points. This can be seen by considering the equation $f(z)=z\Rightarrow az+b=cz^{2}+dz\Rightarrow cz^{2}+(d-a)z-b=0,$ which is clearly a quadratic equation in z. The roots of this equation are the fixed points of *f*(*z*). If the discriminant (*d* − *a*)2 + 4*bc* is zero the LFT fixes a single point; otherwise it has two fixed points.
- If *ad* ≠ *bc* the LFT is an invertible conformal mapping of the extended complex plane onto itself. In other words, this LFT has an inverse function $z=g(w)={\frac {{\phantom {+}}dw-b}{-cw+a}}$ such that *f*(*g*(*z*)) = *g*(*f*(*z*)) = *z* for every point z in the extended complex plane, and both f and g preserve angles and shapes at vanishingly small scales. From the form of *z* = *g*(*w*) we see that g is also an LFT.
- The composition of two different LFTs for which *ad* ≠ *bc* is itself an LFT for which *ad* ≠ *bc*. In other words, the set of all LFTs for which *ad* ≠ *bc* is closed under composition of functions. The collection of all such LFTs, together with the "group operation" composition of functions, is known as the automorphism group of the extended complex plane.
- If *a* = 0 the LFT reduces to $w=f(z)={\frac {b}{cz+d}},$ which is a very simple meromorphic function of z with one simple pole (at −⁠*d*/*c*⁠) and a residue equal to ⁠*b*/*c*⁠. (See also Laurent series.)

### The continued fraction as a composition of LFTs

Consider a sequence of simple linear fractional transformations ${\begin{aligned}\tau _{0}(z)&=b_{0}+z,\\[4px]\tau _{1}(z)&={\frac {a_{1}}{b_{1}+z}},\\[4px]\tau _{2}(z)&={\frac {a_{2}}{b_{2}+z}},\\[4px]\tau _{3}(z)&={\frac {a_{3}}{b_{3}+z}},\\&\;\vdots \end{aligned}}$

Here we use τ to represent each simple LFT, and we adopt the conventional circle notation for composition of functions. We also introduce a new symbol **Τ*n*** to represent the composition of *n* + 1 transformations τi; that is, ${\begin{aligned}{\boldsymbol {\mathrm {T} }}_{\boldsymbol {1}}(z)&=\tau _{0}\circ \tau _{1}(z)=\tau _{0}{\big (}\tau _{1}(z){\big )},\\{\boldsymbol {\mathrm {T} }}_{\boldsymbol {2}}(z)&=\tau _{0}\circ \tau _{1}\circ \tau _{2}(z)=\tau _{0}{\Big (}\tau _{1}{\big (}\tau _{2}(z){\big )}{\Big )},\end{aligned}}$ and so forth. By direct substitution from the first set of expressions into the second we see that ${\begin{aligned}{\boldsymbol {\mathrm {T} }}_{\boldsymbol {1}}(z)&=\tau _{0}\circ \tau _{1}(z)&=&\quad b_{0}+{\cfrac {a_{1}}{b_{1}+z}}\\[4px]{\boldsymbol {\mathrm {T} }}_{\boldsymbol {2}}(z)&=\tau _{0}\circ \tau _{1}\circ \tau _{2}(z)&=&\quad b_{0}+{\cfrac {a_{1}}{b_{1}+{\cfrac {a_{2}}{b_{2}+z}}}}\end{aligned}}$ and, in general, ${\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(z)=\tau _{0}\circ \tau _{1}\circ \tau _{2}\circ \cdots \circ \tau _{n}(z)=b_{0}+{\underset {i=1}{\overset {n}{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}$ where the last partial denominator in the finite continued fraction K is understood to be *bn* + *z*. And, since *bn* + 0 = *bn*, the image of the point *z* = 0 under the iterated LFT **Τ*n*** is indeed the value of the finite continued fraction with n partial numerators: ${\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(0)={\boldsymbol {\mathrm {T} }}_{\boldsymbol {n+1}}(\infty )=b_{0}+{\underset {i=1}{\overset {n}{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}.$

### A geometric interpretation

Defining a finite continued fraction as the image of a point under the iterated linear fractional transformation **Τ*n***(*z*) leads to an intuitively appealing geometric interpretation of infinite continued fractions.

The relationship $x_{n}=b_{0}+{\underset {i=1}{\overset {n}{\operatorname {K} }}}{\frac {a_{i}}{b_{i}}}={\frac {A_{n}}{B_{n}}}={\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(0)={\boldsymbol {\mathrm {T} }}_{\boldsymbol {n+1}}(\infty )$ can be understood by rewriting **Τ*n***(*z*) and **Τ*n*+1**(*z*) in terms of the fundamental recurrence formulas: ${\begin{aligned}{\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(z)&={\frac {(b_{n}+z)A_{n-1}+a_{n}A_{n-2}}{(b_{n}+z)B_{n-1}+a_{n}B_{n-2}}}&{\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(z)&={\frac {zA_{n-1}+A_{n}}{zB_{n-1}+B_{n}}};\\[6px]{\boldsymbol {\mathrm {T} }}_{\boldsymbol {n+1}}(z)&={\frac {(b_{n+1}+z)A_{n}+a_{n+1}A_{n-1}}{(b_{n+1}+z)B_{n}+a_{n+1}B_{n-1}}}&{\boldsymbol {\mathrm {T} }}_{\boldsymbol {n+1}}(z)&={\frac {zA_{n}+A_{n+1}}{zB_{n}+B_{n+1}}}.\end{aligned}}$

In the first of these equations the ratio tends toward ⁠*An*/*Bn*⁠ as z tends toward zero. In the second, the ratio tends toward ⁠*An*/*Bn*⁠ as z tends to infinity. This leads us to our first geometric interpretation. If the continued fraction converges, the successive convergents ⁠*An*/*Bn*⁠ are eventually arbitrarily close together. Since the linear fractional transformation **Τ*n***(*z*) is a continuous mapping, there must be a neighborhood of *z* = 0 that is mapped into an arbitrarily small neighborhood of **Τ*n***(0) = ⁠*An*/*Bn*⁠. Similarly, there must be a neighborhood of the point at infinity which is mapped into an arbitrarily small neighborhood of **Τ*n***(∞) = ⁠*A**n*−1/*B**n*−1⁠. So if the continued fraction converges the transformation **Τ*n***(*z*) maps both very small z and very large z into an arbitrarily small neighborhood of x, the value of the continued fraction, as n gets larger and larger.

For intermediate values of z, since the successive convergents are getting closer together we must have ${\frac {A_{n-1}}{B_{n-1}}}\approx {\frac {A_{n}}{B_{n}}}\quad \Rightarrow \quad {\frac {A_{n-1}}{A_{n}}}\approx {\frac {B_{n-1}}{B_{n}}}=k$ where k is a constant, introduced for convenience. But then, by substituting in the expression for **Τ*n***(*z*) we obtain ${\boldsymbol {\mathrm {T} }}_{\boldsymbol {n}}(z)={\frac {zA_{n-1}+A_{n}}{zB_{n-1}+B_{n}}}={\frac {A_{n}}{B_{n}}}\left({\frac {z{\frac {A_{n-1}}{A_{n}}}+1}{z{\frac {B_{n-1}}{B_{n}}}+1}}\right)\approx {\frac {A_{n}}{B_{n}}}\left({\frac {zk+1}{zk+1}}\right)={\frac {A_{n}}{B_{n}}}$ so that even the intermediate values of z (except when *z* ≈ −*k*−1) are mapped into an arbitrarily small neighborhood of x, the value of the continued fraction, as n gets larger and larger. Intuitively, it is almost as if the convergent continued fraction maps the entire extended complex plane into a single point.

Notice that the sequence {**Τ*n***} lies within the automorphism group of the extended complex plane, since each **Τ*n*** is a linear fractional transformation for which *ab* ≠ *cd*. And every member of that automorphism group maps the extended complex plane into itself: not one of the **Τ*n*** can possibly map the plane into a single point. Yet in the limit the sequence {**Τ*n***} defines an infinite continued fraction which (if it converges) represents a single point in the complex plane.

When an infinite continued fraction converges, the corresponding sequence {**Τ*n***} of LFTs "focuses" the plane in the direction of x, the value of the continued fraction. At each stage of the process a larger and larger region of the plane is mapped into a neighborhood of x, and the smaller and smaller region of the plane that's left over is stretched out ever more thinly to cover everything outside that neighborhood.

For divergent continued fractions, we can distinguish three cases:

1. The two sequences {**Τ2*n*−1**} and {**Τ2*n***} might themselves define two convergent continued fractions that have two different values, *x*odd and *x*even. In this case the continued fraction defined by the sequence {**Τ*n***} diverges by oscillation between two distinct limit points. And in fact this idea can be generalized: sequences {**Τ*n***} can be constructed that oscillate among three, or four, or indeed any number of limit points. Interesting instances of this case arise when the sequence {**Τ*n***} constitutes a subgroup of finite order within the group of automorphisms over the extended complex plane.
2. The sequence {**Τ*n***} may produce an infinite number of zero denominators Bi while also producing a subsequence of finite convergents. These finite convergents may not repeat themselves or fall into a recognizable oscillating pattern. Or they may converge to a finite limit, or even oscillate among multiple finite limits. No matter how the finite convergents behave, the continued fraction defined by the sequence {**Τ*n***} diverges by oscillation with the point at infinity in this case.
3. The sequence {**Τ*n***} may produce no more than a finite number of zero denominators Bi. while the subsequence of finite convergents dances wildly around the plane in a pattern that never repeats itself and never approaches any finite limit either.

Interesting examples of cases 1 and 3 can be constructed by studying the simple continued fraction $x=1+{\cfrac {z}{1+{\cfrac {z}{1+{\cfrac {z}{1+{\cfrac {z}{1+\ddots }}}}}}}}$ where z is any real number such that *z* < −⁠1/4⁠.

## Euler's continued fraction formula

Euler proved the following identity: $a_{0}+a_{0}a_{1}+a_{0}a_{1}a_{2}+\cdots +a_{0}a_{1}a_{2}\cdots a_{n}={\cfrac {a_{0}}{1-{\cfrac {a_{1}}{1+a_{1}-{\cfrac {a_{2}}{1+a_{2}-\cdots {\cfrac {a_{n}}{1+a_{n}}}}}}}}}.$

From this many other results can be derived, such as ${\frac {1}{u_{1}}}+{\frac {1}{u_{2}}}+{\frac {1}{u_{3}}}+\cdots +{\frac {1}{u_{n}}}={\cfrac {1}{u_{1}-{\cfrac {u_{1}^{2}}{u_{1}+u_{2}-{\cfrac {u_{2}^{2}}{u_{2}+u_{3}-\cdots {\cfrac {u_{n-1}^{2}}{u_{n-1}+u_{n}}}}}}}}},$ and ${\frac {1}{a_{0}}}+{\frac {x}{a_{0}a_{1}}}+{\frac {x^{2}}{a_{0}a_{1}a_{2}}}+\cdots +{\frac {x^{n}}{a_{0}a_{1}a_{2}\ldots a_{n}}}={\cfrac {1}{a_{0}-{\cfrac {a_{0}x}{a_{1}+x-{\cfrac {a_{1}x}{a_{2}+x-\cdots {\cfrac {a_{n-1}x}{a_{n}+x}}}}}}}}.$

Euler's formula connecting continued fractions and series is the motivation for the fundamental inequalities, and also the basis of elementary approaches to the convergence problem.

## Examples

### Transcendental functions and numbers

Here are two continued fractions that can be built via Euler's identity.

$e^{x}={\frac {x^{0}}{0!}}+{\frac {x^{1}}{1!}}+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+{\frac {x^{4}}{4!}}+\cdots =1+{\cfrac {x}{1-{\cfrac {1x}{2+x-{\cfrac {2x}{3+x-{\cfrac {3x}{4+x-\ddots }}}}}}}}$

$\log(1+x)={\frac {x^{1}}{1}}-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}-{\frac {x^{4}}{4}}+\cdots ={\cfrac {x}{1-0x+{\cfrac {1^{2}x}{2-1x+{\cfrac {2^{2}x}{3-2x+{\cfrac {3^{2}x}{4-3x+\ddots }}}}}}}}$

Here are additional generalized continued fractions:

$\arctan {\cfrac {x}{y}}={\cfrac {xy}{1y^{2}+{\cfrac {(1xy)^{2}}{3y^{2}-1x^{2}+{\cfrac {(3xy)^{2}}{5y^{2}-3x^{2}+{\cfrac {(5xy)^{2}}{7y^{2}-5x^{2}+\ddots }}}}}}}}={\cfrac {x}{1y+{\cfrac {(1x)^{2}}{3y+{\cfrac {(2x)^{2}}{5y+{\cfrac {(3x)^{2}}{7y+\ddots }}}}}}}}$

$e^{\frac {x}{y}}=1+{\cfrac {2x}{2y-x+{\cfrac {x^{2}}{6y+{\cfrac {x^{2}}{10y+{\cfrac {x^{2}}{14y+{\cfrac {x^{2}}{18y+\ddots }}}}}}}}}}\quad \Rightarrow \quad e^{2}=7+{\cfrac {2}{5+{\cfrac {1}{7+{\cfrac {1}{9+{\cfrac {1}{11+\ddots }}}}}}}}$

$\log \left(1+{\frac {x}{y}}\right)={\cfrac {x}{y+{\cfrac {1x}{2+{\cfrac {1x}{3y+{\cfrac {2x}{2+{\cfrac {2x}{5y+{\cfrac {3x}{2+\ddots }}}}}}}}}}}}={\cfrac {2x}{2y+x-{\cfrac {(1x)^{2}}{3(2y+x)-{\cfrac {(2x)^{2}}{5(2y+x)-{\cfrac {(3x)^{2}}{7(2y+x)-\ddots }}}}}}}}$

This last is based on an algorithm derived by Aleksei Nikolaevich Khovansky in the 1970s.

Example: the natural logarithm of 2 (= [0; 1, 2, 3, 1, 5, ⁠2/3⁠, 7, ⁠1/2⁠, 9, ⁠2/5⁠,..., 2*k* − 1, ⁠2/*k*⁠,...] ≈ 0.693147...): $\log 2=\log(1+1)={\cfrac {1}{1+{\cfrac {1}{2+{\cfrac {1}{3+{\cfrac {2}{2+{\cfrac {2}{5+{\cfrac {3}{2+\ddots }}}}}}}}}}}}={\cfrac {2}{3-{\cfrac {1^{2}}{9-{\cfrac {2^{2}}{15-{\cfrac {3^{2}}{21-\ddots }}}}}}}}$

#### π

Here are three of π's best-known generalized continued fractions, the first and third of which are derived from their respective arctangent formulas above by setting *x* = *y* = 1 and multiplying by 4. The Leibniz formula for π: $\pi ={\cfrac {4}{1+{\cfrac {1^{2}}{2+{\cfrac {3^{2}}{2+{\cfrac {5^{2}}{2+\ddots }}}}}}}}=\sum _{n=0}^{\infty }{\frac {4(-1)^{n}}{2n+1}}={\frac {4}{1}}-{\frac {4}{3}}+{\frac {4}{5}}-{\frac {4}{7}}+-\cdots$ converges slowly, requiring roughly 3 × 10*n* terms to achieve *n* correct decimal places.

The series derived by Nilakantha Somayaji: $\pi =3+{\cfrac {1^{2}}{6+{\cfrac {3^{2}}{6+{\cfrac {5^{2}}{6+\ddots }}}}}}=3-\sum _{n=1}^{\infty }{\frac {(-1)^{n}}{n(n+1)(2n+1)}}=3+{\frac {1}{1\cdot 2\cdot 3}}-{\frac {1}{2\cdot 3\cdot 5}}+{\frac {1}{3\cdot 4\cdot 7}}-+\cdots$ also converges quite slowly, requiring nearly 50 terms for five decimals and nearly 120 for six. Both converge sublinearly.

On the other hand: $\pi ={\cfrac {4}{1+{\cfrac {1^{2}}{3+{\cfrac {2^{2}}{5+{\cfrac {3^{2}}{7+\ddots }}}}}}}}=4-1+{\frac {1}{6}}-{\frac {1}{34}}+{\frac {16}{3145}}-{\frac {4}{4551}}+{\frac {1}{6601}}-{\frac {1}{38341}}+-\cdots$ converges linearly, adding at least three digits of precision per four terms, a pace slightly faster than the arcsine formula for π: $\pi =6\sin ^{-1}\left({\frac {1}{2}}\right)=\sum _{n=0}^{\infty }{\frac {3\cdot {\binom {2n}{n}}}{16^{n}(2n+1)}}={\frac {3}{16^{0}\cdot 1}}+{\frac {6}{16^{1}\cdot 3}}+{\frac {18}{16^{2}\cdot 5}}+{\frac {60}{16^{3}\cdot 7}}+\cdots \!$ which adds at least three decimal digits per five terms.

- **Note:** this continued fraction's rate of convergence *μ* tends to 3 − √8 ≈ 0.1715729, hence ⁠1/*μ*⁠ tends to 3 + √8 ≈ 5.828427, whose common logarithm is 0.7655... ≈ ⁠13/17⁠ > ⁠3/4⁠. The same ⁠1/*μ*⁠ = 3 + √8 (the silver ratio squared) also is observed in the *unfolded* general continued fractions of both the natural logarithm of 2 and the *n*th root of 2 (which works for any integer *n* > 1) if calculated using 2 = 1 + 1. For the *folded* general continued fractions of both expressions, the rate convergence μ = (3 − √8)2 = 17 − √288 ≈ 0.02943725, hence ⁠1/*μ*⁠ = (3 + √8)2 = 17 + √288 ≈ 33.97056, whose common logarithm is 1.531... ≈ ⁠26/17⁠ > ⁠3/2⁠, thus adding at least three digits per two terms. This is because the folded GCF folds each pair of fractions from the unfolded GCF into one fraction, thus doubling the convergence pace. The Manny Sardina reference further explains "folded" continued fractions.
- **Note:** Using the continued fraction for arctan ⁠*x*/*y*⁠ cited above with the best-known Machin-like formula provides an even more rapidly, although still linearly, converging expression: $\pi =16\tan ^{-1}{\cfrac {1}{5}}\,-\,4\tan ^{-1}{\cfrac {1}{239}}={\cfrac {16}{5+{\cfrac {1^{2}}{15+{\cfrac {2^{2}}{25+{\cfrac {3^{2}}{35+\ddots }}}}}}}}\,-\,{\cfrac {4}{239+{\cfrac {1^{2}}{717+{\cfrac {2^{2}}{1195+{\cfrac {3^{2}}{1673+\ddots }}}}}}}}.$

### Roots of positive numbers

The *n*th root of any positive number *z**m* can be expressed by restating *z* = *x**n* + *y*, resulting in ${\sqrt[{n}]{z^{m}}}={\sqrt[{n}]{\left(x^{n}+y\right)^{m}}}=x^{m}+{\cfrac {my}{nx^{n-m}+{\cfrac {(n-m)y}{2x^{m}+{\cfrac {(n+m)y}{3nx^{n-m}+{\cfrac {(2n-m)y}{2x^{m}+{\cfrac {(2n+m)y}{5nx^{n-m}+{\cfrac {(3n-m)y}{2x^{m}+\ddots }}}}}}}}}}}}$ which can be simplified, by folding each pair of fractions into one fraction, to ${\sqrt[{n}]{z^{m}}}=x^{m}+{\cfrac {2x^{m}\cdot my}{n(2x^{n}+y)-my-{\cfrac {(1^{2}n^{2}-m^{2})y^{2}}{3n(2x^{n}+y)-{\cfrac {(2^{2}n^{2}-m^{2})y^{2}}{5n(2x^{n}+y)-{\cfrac {(3^{2}n^{2}-m^{2})y^{2}}{7n(2x^{n}+y)-{\cfrac {(4^{2}n^{2}-m^{2})y^{2}}{9n(2x^{n}+y)-\ddots }}}}}}}}}}.$

The square root of *z* is a special case with *m* = 1 and *n* = 2: ${\sqrt {z}}={\sqrt {x^{2}+y}}=x+{\cfrac {y}{2x+{\cfrac {y}{2x+{\cfrac {3y}{6x+{\cfrac {3y}{2x+\ddots }}}}}}}}=x+{\cfrac {2x\cdot y}{2(2x^{2}+y)-y-{\cfrac {1\cdot 3y^{2}}{6(2x^{2}+y)-{\cfrac {3\cdot 5y^{2}}{10(2x^{2}+y)-\ddots }}}}}}$ which can be simplified by noting that ⁠5/10⁠ = ⁠3/6⁠ = ⁠1/2⁠: ${\sqrt {z}}={\sqrt {x^{2}+y}}=x+{\cfrac {y}{2x+{\cfrac {y}{2x+{\cfrac {y}{2x+{\cfrac {y}{2x+\ddots }}}}}}}}=x+{\cfrac {2x\cdot y}{2(2x^{2}+y)-y-{\cfrac {y^{2}}{2(2x^{2}+y)-{\cfrac {y^{2}}{2(2x^{2}+y)-\ddots }}}}}}.$

The square root can also be expressed by a periodic continued fraction, but the above form converges more quickly with the proper *x* and *y*.

#### Example 1

The cube root of two (21/3 or 3√2 ≈ 1.259921...) can be calculated in two ways:

Firstly, "standard notation" of *x* = 1, *y* = 1, and 2*z* − *y* = 3: ${\sqrt[{3}]{2}}=1+{\cfrac {1}{3+{\cfrac {2}{2+{\cfrac {4}{9+{\cfrac {5}{2+{\cfrac {7}{15+{\cfrac {8}{2+{\cfrac {10}{21+{\cfrac {11}{2+\ddots }}}}}}}}}}}}}}}}=1+{\cfrac {2\cdot 1}{9-1-{\cfrac {2\cdot 4}{27-{\cfrac {5\cdot 7}{45-{\cfrac {8\cdot 10}{63-{\cfrac {11\cdot 13}{81-\ddots }}}}}}}}}}.$

Secondly, a rapid convergence with *x* = 5, *y* = 3 and 2*z* − *y* = 253: ${\sqrt[{3}]{2}}={\cfrac {5}{4}}+{\cfrac {0.5}{50+{\cfrac {2}{5+{\cfrac {4}{150+{\cfrac {5}{5+{\cfrac {7}{250+{\cfrac {8}{5+{\cfrac {10}{350+{\cfrac {11}{5+\ddots }}}}}}}}}}}}}}}}={\cfrac {5}{4}}+{\cfrac {2.5\cdot 1}{253-1-{\cfrac {2\cdot 4}{759-{\cfrac {5\cdot 7}{1265-{\cfrac {8\cdot 10}{1771-\ddots }}}}}}}}.$

#### Example 2

Pogson's ratio (1001/5 or 5√100 ≈ 2.511886...), with *x* = 5, *y* = 75 and 2*z* − *y* = 6325: ${\sqrt[{5}]{100}}={\cfrac {5}{2}}+{\cfrac {3}{250+{\cfrac {12}{5+{\cfrac {18}{750+{\cfrac {27}{5+{\cfrac {33}{1250+{\cfrac {42}{5+\ddots }}}}}}}}}}}}={\cfrac {5}{2}}+{\cfrac {5\cdot 3}{1265-3-{\cfrac {12\cdot 18}{3795-{\cfrac {27\cdot 33}{6325-{\cfrac {42\cdot 48}{8855-\ddots }}}}}}}}.$

#### Example 3

The twelfth root of two (21/12 or 12√2 ≈ 1.059463...), using "standard notation": ${\sqrt[{12}]{2}}=1+{\cfrac {1}{12+{\cfrac {11}{2+{\cfrac {13}{36+{\cfrac {23}{2+{\cfrac {25}{60+{\cfrac {35}{2+{\cfrac {37}{84+{\cfrac {47}{2+\ddots }}}}}}}}}}}}}}}}=1+{\cfrac {2\cdot 1}{36-1-{\cfrac {11\cdot 13}{108-{\cfrac {23\cdot 25}{180-{\cfrac {35\cdot 37}{252-{\cfrac {47\cdot 49}{324-\ddots }}}}}}}}}}.$

#### Example 4

Equal temperament's perfect fifth (27/12 or 12√27 ≈ 1.498307...), with *m* = 7:

With "standard notation": ${\sqrt[{12}]{2^{7}}}=1+{\cfrac {7}{12+{\cfrac {5}{2+{\cfrac {19}{36+{\cfrac {17}{2+{\cfrac {31}{60+{\cfrac {29}{2+{\cfrac {43}{84+{\cfrac {41}{2+\ddots }}}}}}}}}}}}}}}}=1+{\cfrac {2\cdot 7}{36-7-{\cfrac {5\cdot 19}{108-{\cfrac {17\cdot 31}{180-{\cfrac {29\cdot 43}{252-{\cfrac {41\cdot 55}{324-\ddots }}}}}}}}}}.$

A rapid convergence with *x* = 3, *y* = −7153, and 2*z* − *y* = 219 + 312: ${\sqrt[{12}]{2^{7}}}={\cfrac {1}{2}}{\sqrt[{12}]{3^{12}-7153}}={\cfrac {3}{2}}-{\cfrac {0.5\cdot 7153}{4\cdot 3^{12}-{\cfrac {11\cdot 7153}{6-{\cfrac {13\cdot 7153}{12\cdot 3^{12}-{\cfrac {23\cdot 7153}{6-{\cfrac {25\cdot 7153}{20\cdot 3^{12}-{\cfrac {35\cdot 7153}{6-{\cfrac {37\cdot 7153}{28\cdot 3^{12}-{\cfrac {47\cdot 7153}{6-\ddots }}}}}}}}}}}}}}}}$

${\sqrt[{12}]{2^{7}}}={\cfrac {3}{2}}-{\cfrac {3\cdot 7153}{12(2^{19}+3^{12})+7153-{\cfrac {11\cdot 13\cdot 7153^{2}}{36(2^{19}+3^{12})-{\cfrac {23\cdot 25\cdot 7153^{2}}{60(2^{19}+3^{12})-{\cfrac {35\cdot 37\cdot 7153^{2}}{84(2^{19}+3^{12})-\ddots }}}}}}}}.$

More details on this technique can be found in *General Method for Extracting Roots using (Folded) Continued Fractions*.

## Higher dimensions

Another meaning for **generalized continued fraction** is a generalization to higher dimensions. For example, there is a close relationship between the simple continued fraction in canonical form for the irrational real number *α*, and the way integer lattice points in two dimensions lie to either side of the line *y* = *αx*. Generalizing this idea, one might ask about something related to lattice points in three or more dimensions. One reason to study this area is to quantify the mathematical coincidence idea; for example, for monomials in several real numbers, take the logarithmic form and consider how small it can be. Another reason is to find a possible solution to Hermite's problem.

There have been numerous attempts to construct a generalized theory. Notable efforts in this direction were made by Felix Klein (the Klein polyhedron), Georges Poitou and George Szekeres.

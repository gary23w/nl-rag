---
title: "Asymptotic analysis"
source: https://en.wikipedia.org/wiki/Asymptotic_analysis
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Asymptotic analysis

In mathematical analysis, **asymptotic analysis**, also known as **asymptotics**, is the development and application of methods that generate an approximate analytical solution to a mathematical problem when a variable or parameter assumes a value that is large, small or near a specified value.

An example of asymptotic analysis is function approximation. For example, the function ${\textstyle {\widetilde {y}}(x)=x}$ accurately approximates the function ${\textstyle y(x)=x+e^{-x}}$ for large positive ${\textstyle x}$ values (Figure 1). For any desired accuracy, there is a corresponding range of ${\textstyle x}$ values where this accuracy occurs. In this case, a chosen accuracy with a relative error of less than 1% occurs when the ${\textstyle x}$ values are greater than 3.4.

The prime number theorem is an example of an important asymptotic result. For any real number ${\textstyle x}$ , the prime counting function, denoted as ${\textstyle \operatorname {\pi } (x)}$ , is the number of prime numbers less than or equal to ${\textstyle x}$ . The function, ${\textstyle x/\ln(x)}$ , approximates the prime counting function for large numbers ${\textstyle x}$ . As in the preceding example, as the number ${\textstyle x}$ becomes increasingly larger, the approximating function becomes increasingly more accurate, leading to an increasingly smaller relative error. This asymptotic relationship is expressed using this notation: $\pi (x)\sim {\frac {x}{\ln(x)}}\quad (x\to \infty )$

Asymptotic analysis impacts on many areas of mathematics. Mathematicians use asymptotic analysis for computing function approximations, implicit functions, integrals, iterated functions, series summation, partial sums, solutions of difference equations. solutions of differential equations and properties of computer algorithms.

## Definition

Formally, given functions *f* (*x*) and *g*(*x*), we define a binary relation $f(x)\sim g(x)\quad ({\text{as }}x\to \infty )$ if and only if (de Bruijn 1981, §1.4) $\lim _{x\to \infty }{\frac {f(x)}{g(x)}}=1.$

The symbol ~ is the tilde. The relation is an equivalence relation on the set of functions of x; the functions f and g are said to be *asymptotically equivalent*. The domain of f and g can be any set for which the limit is defined: e.g. real numbers, complex numbers, positive integers.

The same notation is also used for other ways of passing to a limit: e.g. *x* → 0, *x* ↓ 0, |*x*| → 0. The way of passing to the limit is often not stated explicitly, if it is clear from the context.

Although the above definition is common in the literature, it is problematic if *g*(*x*) is zero infinitely often as x goes to the limiting value. For that reason, some authors use an alternative definition. The alternative definition, in little-o notation, is that *f* ~ *g* if and only if $f(x)=g(x)(1+o(1)).$

This definition is equivalent to the prior definition if *g*(*x*) is not zero in some neighbourhood of the limiting value.

## Properties

The zero function, ${\textstyle f(z)=0}$ , can never be equivalent to any other function.

The little-o relation has the *partial ordering property* defined as if ${\textstyle f(x)=o(g(x))}$ and ${\textstyle g(x)=o(h(x))}$ then ${\textstyle f(x)=o(h(x))}$ .

Asymptotic equivalence has reflexive,symmetric and transitive properties.

If these functions are equivalent, ${\textstyle f(x)\sim g(x)\,(x\to L)}$ , then the exponentiated functions to the real power ${\textstyle r}$ are also equivalent: $(f(x))^{r}\sim (g(x))^{r}\ (x\to L)$

If these functions are equivalent ${\textstyle f(x)\sim g(x)\,(x\to L)}$ , and these functions are equivalent ${\textstyle h(x)\sim k(x)\,(x\to L)}$ , then the quotients are equivalent: ${\frac {f(x)}{h(x)}}\sim {\frac {g(x)}{k(x)}}\ (x\to L)$ These properties allow asymptotically equivalent functions to be freely exchanged in many algebraic expressions.

Asymptotically equivalent functions remain asymptotically equivalent under integration if requirements related to convergence are met. There are more stringent requirements for asymptotically equivalent functions to remain asymptotically equivalent under differentiation.

## Examples of asymptotic formulas

- Factorial $n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}$ —this is Stirling's approximation
- Partition function For a positive integer *n*, the partition function, *p*(*n*), gives the number of ways of writing the integer *n* as a sum of positive integers, where the order of addends is not considered. $p(n)\sim {\frac {1}{4n{\sqrt {3}}}}e^{\pi {\sqrt {\frac {2n}{3}}}}$
- Airy function The Airy function, Ai(*x*), is a solution of the differential equation *y″* − *xy* = 0; it has many applications in physics. $\operatorname {Ai} (x)\sim {\frac {e^{-{\frac {2}{3}}x^{\frac {3}{2}}}}{2{\sqrt {\pi }}x^{1/4}}}$
- Hankel functions ${\begin{aligned}H_{\alpha }^{(1)}(z)&\sim {\sqrt {\frac {2}{\pi z}}}e^{i\left(z-{\frac {2\pi \alpha -\pi }{4}}\right)}\\H_{\alpha }^{(2)}(z)&\sim {\sqrt {\frac {2}{\pi z}}}e^{-i\left(z-{\frac {2\pi \alpha -\pi }{4}}\right)}\end{aligned}}$

## Asymptotic expansion

An asymptotic expansion of a function *f*(*x*) is in practice an expression of that function in terms of a series, the partial sums of which do not necessarily converge, but such that taking any initial partial sum provides an asymptotic formula for f. The idea is that successive terms provide an increasingly accurate description of the order of growth of f.

In symbols, it means we have $f\sim g_{1},$ but also $f-g_{1}\sim g_{2}$ and $f-g_{1}-\cdots -g_{k-1}\sim g_{k}$ for each fixed *k*. In view of the definition of the $\sim$ symbol, the last equation means $f-(g_{1}+\cdots +g_{k})=o(g_{k})$ in the little o notation, i.e., $f-(g_{1}+\cdots +g_{k})$ is much smaller than $g_{k}.$

The relation $f-g_{1}-\cdots -g_{k-1}\sim g_{k}$ takes its full meaning if $g_{k+1}=o(g_{k})$ for all *k*, which means the $g_{k}$ form an asymptotic scale. In that case, some authors may abusively write $f\sim g_{1}+\cdots +g_{k}$ to denote the statement $f-(g_{1}+\cdots +g_{k})=o(g_{k}).$ One should however be careful that this is not a standard use of the $\sim$ symbol, and that it does not correspond to the definition given in § Definition.

In the present situation, this relation $g_{k}=o(g_{k-1})$ actually follows from combining steps *k* and *k*−1; by subtracting $f-g_{1}-\cdots -g_{k-2}=g_{k-1}+o(g_{k-1})$ from $f-g_{1}-\cdots -g_{k-2}-g_{k-1}=g_{k}+o(g_{k}),$ one gets $g_{k}+o(g_{k})=o(g_{k-1}),$ i.e. $g_{k}=o(g_{k-1}).$

In case the asymptotic expansion does not converge, for any particular value of the argument there will be a particular partial sum which provides the best approximation and adding additional terms will decrease the accuracy. This optimal partial sum will usually have more terms as the argument approaches the limit value.

### Examples of asymptotic expansions

- Gamma function ${\frac {e^{x}}{x^{x}{\sqrt {2\pi x}}}}\Gamma (x+1)\sim 1+{\frac {1}{12x}}+{\frac {1}{288x^{2}}}-{\frac {139}{51840x^{3}}}-\cdots \ (x\to \infty )$
- Exponential integral $xe^{x}E_{1}(x)\sim \sum _{n=0}^{\infty }{\frac {(-1)^{n}n!}{x^{n}}}\ (x\to \infty )$
- Error function ${\sqrt {\pi }}xe^{x^{2}}\operatorname {erfc} (x)\sim 1+\sum _{n=1}^{\infty }(-1)^{n}{\frac {(2n-1)!!}{n!(2x^{2})^{n}}}\ (x\to \infty )$ where *m*!! is the double factorial.

### Worked example

Asymptotic expansions often occur when an ordinary series is used in a formal expression that forces the taking of values outside of its domain of convergence. For example, we might start with the formal power series ${\frac {1}{1-w}}=\sum _{n=0}^{\infty }w^{n}$

The expression on the left is valid on the entire complex plane $w\neq 1$ , while the right hand side converges only for $|w|<1$ . Multiplying by $e^{-w/t}$ and integrating both sides yields $\int _{0}^{\infty }{\frac {e^{-{\frac {w}{t}}}}{1-w}}\,dw=\sum _{n=0}^{\infty }t^{n+1}\int _{0}^{\infty }e^{-u}u^{n}\,du$

The integral on the left hand side can be expressed in terms of the exponential integral. The integral on the right hand side, after the substitution $u=w/t$ , may be recognized as the gamma function. Evaluating both, one obtains the asymptotic expansion $e^{-{\frac {1}{t}}}\operatorname {Ei} \left({\frac {1}{t}}\right)=\sum _{n=0}^{\infty }n!\;t^{n+1}$

Here, the right hand side is clearly not convergent for any non-zero value of *t*. However, by keeping *t* small, and truncating the series on the right to a finite number of terms, one may obtain a fairly good approximation to the value of $\operatorname {Ei} (1/t)$ . Substituting $x=-1/t$ and noting that $\operatorname {Ei} (x)=-E_{1}(-x)$ results in the asymptotic expansion given earlier in this article.

## Asymptotic distribution

In mathematical statistics, an asymptotic distribution is a hypothetical distribution that is in a sense the "limiting" distribution of a sequence of distributions. A distribution is an ordered set of random variables *Z**i* for *i* = 1, …, *n*, for some positive integer *n*. An asymptotic distribution allows *i* to range without bound, that is, *n* is infinite.

A special case of an asymptotic distribution is when the late entries go to zero—that is, the *Z**i* go to 0 as *i* goes to infinity. Some instances of "asymptotic distribution" refer only to this special case.

This is based on the notion of an asymptotic function which cleanly approaches a constant value (the *asymptote*) as the independent variable goes to infinity; "clean" in this sense meaning that for any desired closeness epsilon there is some value of the independent variable after which the function never differs from the constant by more than epsilon.

An asymptote is a straight line that a curve approaches but never meets or crosses. Informally, one may speak of the curve meeting the asymptote "at infinity" although this is not a precise definition. In the equation $y={\frac {1}{x}},$ *y* becomes arbitrarily small in magnitude as *x* increases.

## Applications

Asymptotic analysis is used in several mathematical sciences. In statistics, asymptotic theory provides limiting approximations of the probability distribution of sample statistics, such as the likelihood ratio statistic and the expected value of the deviance. Asymptotic theory does not provide a method of evaluating the finite-sample distributions of sample statistics, however. Non-asymptotic bounds are provided by methods of approximation theory.

Examples of applications are the following.

- In applied mathematics, asymptotic analysis is used to build numerical methods to approximate equation solutions.
- In mathematical statistics and probability theory, asymptotics are used in analysis of long-run or large-sample behaviour of random variables and estimators.
- In computer science, the analysis of algorithms evaluate the performance of algorithms and is expressed in terms of big O notation.
- The behavior of physical systems, an example being statistical mechanics.
- In accident analysis when identifying the causation of crash through count modeling with large number of crash counts in a given time and space.

Asymptotic analysis is a key tool for exploring the ordinary and partial differential equations which arise in the mathematical modelling of real-world phenomena. An illustrative example is the derivation of the boundary layer equations from the full Navier-Stokes equations governing fluid flow. In many cases, the asymptotic expansion is in power of a small parameter, ε: in the boundary layer case, this is the nondimensional ratio of the boundary layer thickness to a typical length scale of the problem. Indeed, applications of asymptotic analysis in mathematical modelling often center around a nondimensional parameter which has been shown, or assumed, to be small through a consideration of the scales of the problem at hand.

Asymptotic expansions typically arise in the approximation of certain integrals (Laplace's method, saddle-point method, method of steepest descent) or in the approximation of probability distributions (Edgeworth series). The Feynman graphs in quantum field theory are another example of asymptotic expansions which often do not converge.

### Asymptotic versus Numerical Analysis

De Bruijn illustrates the use of asymptotics in the following dialog between Dr. N.A., a numerical analyst, and Dr. A.A., an asymptotic analyst:

> N.A.: I want to evaluate my function $f(x)$ for large values of x , with a relative error of at most 1%.
> 
> A.A.: $f(x)=x^{-1}+\mathrm {O} (x^{-2})\qquad (x\to \infty )$ .
> 
> N.A.: I am sorry, I don't understand.
> 
> A.A.: $|f(x)-x^{-1}|<8x^{-2}\qquad (x>10^{4}).$
> 
> N.A.: But my value of x is only 100.
> 
> A.A.: Why did you not say so? My evaluations give
> 
> > $|f(x)-x^{-1}|<57000x^{-2}\qquad (x>100).$
> 
> N.A.: This is no news to me. I know already that $0<f(100)<1$ .
> 
> A.A.: I can gain a little on some of my estimates. Now I find that
> 
> > $|f(x)-x^{-1}|<20x^{-2}\qquad (x>100).$
> 
> N.A.: I asked for 1%, not for 20%.
> 
> A.A.: It is almost the best thing I possibly can get. Why don't you take larger values of x ?
> 
> N.A.: !!! I think it's better to ask my electronic computing machine.
> 
> Machine: f(100) = 0.01137 42259 34008 67153
> 
> A.A.: Haven't I told you so? My estimate of 20% was not far off from the 14% of the real error.
> 
> N.A.: !!! . . .  !
> 
> Some days later, Miss N.A. wants to know the value of f(1000), but her machine would take a month of computation to give the answer. She returns to her Asymptotic Colleague, and gets a fully satisfactory reply.

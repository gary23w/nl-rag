---
title: "Gamma function (part 2/2)"
source: https://en.wikipedia.org/wiki/Gamma_function
domain: functional-equations
license: CC-BY-SA-4.0
tags: functional equation, cauchy functional equation, recurrence relation, generating function
fetched: 2026-07-02
part: 2/2
---

## Applications

One author describes the gamma function as "Arguably, the most common special function, or the least 'special' of them. The other transcendental functions [...] are called 'special' because you could conceivably avoid some of them by staying away from many specialized mathematical topics. On the other hand, the gamma function $\Gamma (z)$ is most difficult to avoid."

### Integration problems

The gamma function finds application in such diverse areas as quantum physics, astrophysics and fluid dynamics. The gamma distribution, which is formulated in terms of the gamma function, is used in statistics to model a wide range of processes; for example, the time between occurrences of earthquakes.

The primary reason for the gamma function's usefulness in such contexts is the prevalence of expressions of the type ⁠ $f(t)e^{-g(t)}$ ⁠, which describe processes that decay exponentially in time or space. Integrals of such expressions can occasionally be solved in terms of the gamma function when no elementary solution exists. For example, if f is a power function and g is a linear function, a simple change of variables $u:=a\cdot t$ gives the evaluation $\int _{0}^{\infty }t^{b}\,e^{-at}\,dt={\frac {1}{a^{b}}}\int _{0}^{\infty }u^{b}\,e^{-u}\,d\left({\frac {u}{a}}\right)={\frac {\Gamma (b+1)}{a^{b+1}}}.$

The fact that the integration is performed along the entire positive real line might signify that the gamma function describes the cumulation of a time-dependent process that continues indefinitely, or the value might be the total of a distribution in an infinite space.

It is of course frequently useful to take limits of integration other than 0 and $\infty$ to describe the cumulation of a finite process, in which case the ordinary gamma function is no longer a solution; the solution is then called an incomplete gamma function. (The ordinary gamma function, obtained by integrating across the entire positive real line, is sometimes called the *complete gamma function* for contrast.)

An important category of exponentially decaying functions is that of Gaussian functions $ae^{-{\frac {(x-b)^{2}}{c^{2}}}}$ and integrals thereof, such as the error function. There are many interrelations between these functions and the gamma function; notably, the factor ${\sqrt {\pi }}$ obtained by evaluating ${\textstyle \Gamma \left({\frac {1}{2}}\right)}$ is the "same" as that found in the normalizing factor of the error function and the normal distribution.

The integrals discussed so far involve transcendental functions, but the gamma function also arises from integrals of purely algebraic functions. In particular, the arc lengths of ellipses and of the lemniscate, which are curves defined by algebraic equations, are given by elliptic integrals that in special cases can be evaluated in terms of the gamma function. The gamma function can also be used to calculate "volume" and "area" of n -dimensional hyperspheres.

### Calculating products

The gamma function's ability to generalize factorial products immediately leads to applications in many areas of mathematics; in combinatorics, and by extension in areas such as probability theory and the calculation of power series. Many expressions involving products of successive integers can be written as some combination of factorials, the most important example perhaps being that of the binomial coefficient. For example, for any complex numbers z and ⁠ n ⁠, with ⁠ $\vert z\vert <1$ ⁠, we can write $(1+z)^{n}=\sum _{k=0}^{\infty }{\frac {\Gamma (n+1)}{k!\Gamma (n-k+1)}}z^{k},$ which closely resembles the binomial coefficient when n is a non-negative integer, $(1+z)^{n}=\sum _{k=0}^{n}{\frac {n!}{k!(n-k)!}}z^{k}=\sum _{k=0}^{n}{\binom {n}{k}}z^{k}.$

The example of binomial coefficients motivates why the properties of the gamma function when extended to negative numbers are natural. A binomial coefficient gives the number of ways to choose k elements from a set of n elements; if ⁠ $k>n$ ⁠, there are of course no ways. If ⁠ $k>n$ ⁠, then $(n-k)!$ is the factorial of a negative integer and hence infinite if we use the gamma function definition of factorials—dividing by infinity gives the expected value of ⁠ 0 ⁠.

We can replace the factorial by a gamma function to extend any such formula to the complex numbers. Generally, this works for any product wherein each factor is a rational function of the index variable, by factoring the rational function into linear expressions. If P and Q are monic polynomials of degree m and n with respective roots $p_{1},\cdots ,p_{m}$ and ⁠ $q_{1},\cdots ,q_{m}$ ⁠, we have $\prod _{i=a}^{b}{\frac {P(i)}{Q(i)}}=\left(\prod _{j=1}^{m}{\frac {\Gamma (b-p_{j}+1)}{\Gamma (a-p_{j})}}\right)\left(\prod _{k=1}^{n}{\frac {\Gamma (a-q_{k})}{\Gamma (b-q_{k}+1)}}\right).$

If we have a way to calculate the gamma function numerically, it is very simple to calculate numerical values of such products. The number of gamma functions in the right-hand side depends only on the degree of the polynomials, so it does not matter whether $b-a$ equals 5 or 105. By taking the appropriate limits, the equation can also be made to hold even when the left-hand product contains zeros or poles.

By taking limits, certain rational products with infinitely many factors can be evaluated in terms of the gamma function as well. Due to the Weierstrass factorization theorem, analytic functions can be written as infinite products, and these can sometimes be represented as finite products or quotients of the gamma function. We have already seen one striking example: the reflection formula essentially represents the sine function as the product of two gamma functions. Starting from this formula, the exponential function as well as all the trigonometric and hyperbolic functions can be expressed in terms of the gamma function.

More functions yet, including the hypergeometric function and special cases thereof, can be represented by means of complex contour integrals of products and quotients of the gamma function, called Mellin–Barnes integrals.

### Analytic number theory

An application of the gamma function is the study of the Riemann zeta function. A fundamental property of the Riemann zeta function is its functional equation: $\Gamma \left({\frac {s}{2}}\right)\,\zeta (s)\,\pi ^{-{\frac {s}{2}}}=\Gamma \left({\frac {1-s}{2}}\right)\,\zeta (1-s)\,\pi ^{-{\frac {1-s}{2}}}.$

Among other things, this provides an explicit form for the analytic continuation of the zeta function to a meromorphic function in the complex plane and leads to an immediate proof that the zeta function has infinitely many so-called "trivial" zeros on the real line. Another powerful formula is $\zeta (s)\;\Gamma (s)=\int _{0}^{\infty }{\frac {t^{s}}{e^{t}-1}}\,{\frac {dt}{t}}.$

Both formulas were derived by Bernhard Riemann in his seminal 1859 paper "*Ueber die Anzahl der Primzahlen unter einer gegebenen Größe*" ("On the Number of Primes Less Than a Given Magnitude"), one of the milestones in the development of analytic number theory—the branch of mathematics that studies prime numbers using the tools of mathematical analysis.


## History

The gamma function has caught the interest of some of the most prominent mathematicians of all time. Its history, notably documented by Philip J. Davis in an article that won him the 1963 Chauvenet Prize, reflects many of the major developments within mathematics since the 18th century. In the words of Davis, "each generation has found something of interest to say about the gamma function. Perhaps the next generation will also."

### 18th century: Euler and Stirling

The problem of extending the factorial to non-integer arguments was apparently first considered by Daniel Bernoulli and Christian Goldbach in the 1720s. In particular, in a letter from Bernoulli to Goldbach dated 6 October 1729 Bernoulli introduced the product representation $x!=\lim _{n\to \infty }\left(n+1+{\frac {x}{2}}\right)^{x-1}\prod _{k=1}^{n}{\frac {k+1}{k+x}},$ which is well defined for real values of x other than the negative integers.

Leonhard Euler later gave two different definitions: the first was not his integral but an infinite product that is well defined for all complex numbers n other than the negative integers, $n!=\prod _{k=1}^{\infty }{\frac {\left(1+{\frac {1}{k}}\right)^{n}}{1+{\frac {n}{k}}}}\,,$ of which he informed Goldbach in a letter dated 13 October 1729. He wrote to Goldbach again on 8 January 1730, to announce his discovery of the integral representation $n!=\int _{0}^{1}(-\log s)^{n}\,ds,$ which is valid when the real part of the complex number ⁠ n ⁠ is strictly greater than $-1$ (i.e., ⁠ $\Re (n)>-1$ ⁠). By the change of variables ⁠ $t=-\ln s$ ⁠, this becomes the familiar Euler integral. Euler published his results in the paper "De progressionibus transcendentibus seu quarum termini generales algebraice dari nequeunt" ("On transcendental progressions, that is, those whose general terms cannot be given algebraically"), submitted to the St. Petersburg Academy on 28 November 1729. Euler further discovered some of the gamma function's important functional properties, including the reflection formula.

James Stirling, a contemporary of Euler, also attempted to find a continuous expression for the factorial and came up with what is now known as Stirling's formula. Although Stirling's formula gives a good estimate of ⁠ $n!$ ⁠, also for non-integers, it does not provide the exact value. Extensions of his formula that correct the error were given by Stirling himself and by Jacques Philippe Marie Binet.

### 19th century: Gauss, Weierstrass, and Legendre

Carl Friedrich Gauss rewrote Euler's product as $\Gamma (z)=\lim _{m\to \infty }{\frac {m^{z}m!}{z(z+1)(z+2)\cdots (z+m)}}$ and used this formula to discover new properties of the gamma function. Although Euler was a pioneer in the theory of complex variables, he does not appear to have considered the factorial of a complex number, as instead Gauss first did. Gauss also proved the multiplication theorem of the gamma function and investigated the connection between the gamma function and elliptic integrals.

Karl Weierstrass further established the role of the gamma function in complex analysis, starting from yet another product representation, $\Gamma (z)={\frac {e^{-\gamma z}}{z}}\prod _{k=1}^{\infty }\left(1+{\frac {z}{k}}\right)^{-1}e^{\frac {z}{k}},$ where $\gamma$ is the Euler–Mascheroni constant. Weierstrass originally wrote his product as one for ⁠ $\textstyle {\frac {1}{\Gamma }}$ ⁠, in which case it is taken over the function's zeros rather than its poles. Inspired by this result, he proved what is known as the Weierstrass factorization theorem—that any entire function can be written as a product over its zeros in the complex plane; a generalization of the fundamental theorem of algebra.

The name gamma function and the symbol $\Gamma$ were introduced by Adrien-Marie Legendre around 1811; Legendre also rewrote Euler's integral definition in its modern form. Although the symbol is an upper-case Greek gamma, there is no accepted standard for whether the function name should be written "gamma function" or "Gamma function" (some authors simply write "⁠ $\Gamma$ ⁠-function"). The alternative "pi function" notation $\Pi (z)=z!$ due to Gauss is sometimes encountered in older literature, but Legendre's notation is dominant in modern works.

It is justified to ask why we distinguish between the "ordinary factorial" and the gamma function by using distinct symbols, and particularly why the gamma function should be normalized to $\Gamma (n+1)=n!$ instead of simply using ⁠ $\Gamma (n)=n!$ ⁠. Consider that the notation for exponents, ⁠ $x^{n}$ ⁠, has been generalized from integers to complex numbers $x^{z}$ without any change. Legendre's motivation for the normalization is not known, and has been criticized as cumbersome by some (the 20th-century mathematician Cornelius Lanczos, for example, called it "void of any rationality" and would instead use ⁠ $z!$ ⁠). Legendre's normalization does simplify some formulae, but complicates others. From a modern point of view, the Legendre normalization of the gamma function is the integral of the additive character $e^{-x}$ against the multiplicative character $x^{z}$ with respect to the Haar measure ${\textstyle {\frac {dx}{x}}}$ on the Lie group ⁠ $\mathbb {R} ^{+}$ ⁠. Thus this normalization makes it clearer that the gamma function is a continuous analogue of a Gauss sum.

### 19th–20th centuries: characterizing the gamma function

It is somewhat problematic that a large number of definitions have been given for the gamma function. Although they describe the same function, it is not entirely straightforward to prove the equivalence. Stirling never proved that his extended formula corresponds exactly to Euler's gamma function; a proof was first given by Charles Hermite in 1900. Instead of finding a specialized proof for each formula, it would be desirable to have a general method of identifying the gamma function.

One way to prove equivalence would be to find a differential equation that characterizes the gamma function. Most special functions in applied mathematics arise as solutions to differential equations, whose solutions are unique. However, the gamma function does not appear to satisfy any simple differential equation. Otto Hölder proved in 1887 that the gamma function at least does not satisfy any *algebraic* differential equation by showing that a solution to such an equation could not satisfy the gamma function's recurrence formula, making it a transcendentally transcendental function. This result is known as Hölder's theorem.

A definite and generally applicable characterization of the gamma function was not given until 1922. Harald Bohr and Johannes Mollerup then proved what is known as the Bohr–Mollerup theorem: that the gamma function is the unique solution to the factorial recurrence relation that is positive and *logarithmically convex* for positive ⁠ z ⁠ and whose value at ⁠ 1 ⁠ is ⁠ 1 ⁠ (a function is logarithmically convex if its logarithm is convex). Another characterisation is given by the Wielandt theorem.

The Bohr–Mollerup theorem is useful because it is relatively easy to prove logarithmic convexity for any of the different formulas used to define the gamma function. Taking things further, instead of defining the gamma function by any particular formula, we can choose the conditions of the Bohr–Mollerup theorem as the definition, and then pick any formula we like that satisfies the conditions as a starting point for studying the gamma function. This approach was used by the Bourbaki group.

Borwein & Corless review three centuries of work on the gamma function.

### Reference tables and software

Although the gamma function can be calculated virtually as easily as any mathematically simpler function with a modern computer—even with a programmable pocket calculator—this was of course not always the case. Until the mid-20th century, mathematicians relied on hand-made tables; in the case of the gamma function, notably a table computed by Gauss in 1813 and one computed by Legendre in 1825.

Tables of complex values of the gamma function, as well as hand-drawn graphs, were given in *Tables of Functions With Formulas and Curves* by Jahnke and Emde, first published in Germany in 1909. According to Michael Berry, "the publication in J&E of a three-dimensional graph showing the poles of the gamma function in the complex plane acquired an almost iconic status."

There was in fact little practical need for anything but real values of the gamma function until the 1930s, when applications for the complex gamma function were discovered in theoretical physics. As electronic computers became available for the production of tables in the 1950s, several extensive tables for the complex gamma function were published to meet the demand, including a table accurate to 12 decimal places from the U.S. National Bureau of Standards.

Double-precision floating-point implementations of the gamma function and its logarithm are now available in most scientific computing software and special functions libraries, for example TK Solver, Matlab, GNU Octave, and the GNU Scientific Library. The gamma function was also added to the C standard library (math.h). Arbitrary-precision implementations are available in most computer algebra systems, such as Mathematica and Maple. PARI/GP, MPFR and MPFUN contain free arbitrary-precision implementations. In some software calculators, such the Windows Calculator and GNOME Calculator, the factorial function returns $\Gamma (x+1)$ when the input x is a non-integer value.

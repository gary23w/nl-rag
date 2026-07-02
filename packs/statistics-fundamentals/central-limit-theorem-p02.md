---
title: "Central limit theorem (part 2/2)"
source: https://en.wikipedia.org/wiki/Central_limit_theorem
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
part: 2/2
---

## Beyond the classical framework

Asymptotic normality, that is, convergence to the normal distribution after appropriate shift and rescaling, is a phenomenon much more general than the classical framework treated above, namely, sums of independent random variables (or vectors). New frameworks are revealed from time to time; no single unifying framework is available for now.

### Convex body

**Theorem**—There exists a sequence *εn* ↓ 0 for which the following holds. Let *n* ≥ 1, and let random variables *X*1, ..., *Xn* have a log-concave joint density f such that *f*(*x*1, ..., *xn*) = *f*(|*x*1|, ..., |*xn*|) for all *x*1, ..., *xn*, and E(*X*2 *k*) = 1 for all *k* = 1, ..., *n*. Then the distribution of

X 1 + ⋯ + X n n {\displaystyle {\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}} ({\displaystyle {\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}})

is εn-close to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) in the total variation distance.

These two εn-close distributions have densities (in fact, log-concave densities), thus, the total variance distance between them is the integral of the absolute value of the difference between the densities. Convergence in total variation is stronger than weak convergence.

An important example of a log-concave density is a function constant inside a given convex body and vanishing outside; it corresponds to the uniform distribution on the convex body, which explains the term "central limit theorem for convex bodies".

Another example: *f*(*x*1, ..., *xn*) = const · exp(−(|*x*1|*α* + ⋯ + |*xn*|*α*)*β*) where *α* > 1 and *αβ* > 1. If *β* = 1 then *f*(*x*1, ..., *xn*) factorizes into const · exp (−|*x*1|*α*) ... exp(−|*xn*|*α*), which means *X*1, ..., *Xn* are independent. In general, however, they are dependent.

The condition *f*(*x*1, ..., *xn*) = *f*(|*x*1|, ..., |*xn*|) ensures that *X*1, ..., *Xn* are of zero mean and uncorrelated; still, they need not be independent, nor even pairwise independent. By the way, pairwise independence cannot replace independence in the classical central limit theorem.

Here is a Berry–Esseen type result.

**Theorem**—Let *X*1, ..., *Xn* satisfy the assumptions of the previous theorem, then

| P ( a ≤ X 1 + ⋯ + X n n ≤ b ) − 1 2 π ∫ a b e − 1 2 t 2 d t | ≤ C n {\displaystyle \left|\mathbb {P} \left(a\leq {\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq {\frac {C}{n}}} ({\displaystyle \left|\mathbb {P} \left(a\leq {\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq {\frac {C}{n}}})

for all *a* < *b*; here C is a universal (absolute) constant. Moreover, for every *c*1, ..., *cn* ∈ **R** such that *c*2 1 + ⋯ + *c*2 *n* = 1,

| P ( a ≤ c 1 X 1 + ⋯ + c n X n ≤ b ) − 1 2 π ∫ a b e − 1 2 t 2 d t | ≤ C ( c 1 4 + ⋯ + c n 4 ) . {\displaystyle \left|\mathbb {P} \left(a\leq c_{1}X_{1}+\cdots +c_{n}X_{n}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq C\left(c_{1}^{4}+\dots +c_{n}^{4}\right).} ({\displaystyle \left|\mathbb {P} \left(a\leq c_{1}X_{1}+\cdots +c_{n}X_{n}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq C\left(c_{1}^{4}+\dots +c_{n}^{4}\right).})

The distribution of ⁠*X*1 + ⋯ + *Xn*/√*n*⁠ need not be approximately normal (in fact, it can be uniform). However, the distribution of *c*1*X*1 + ⋯ + *cnXn* is close to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) (in the total variation distance) for most vectors (*c*1, ..., *cn*) according to the uniform distribution on the sphere *c*2 1 + ⋯ + *c*2 *n* = 1.

### Lacunary trigonometric series

**Theorem (Salem–Zygmund)**—Let U be a random variable distributed uniformly on (0,2π), and *Xk* = *rk* cos(*nkU* + *ak*), where

- nk satisfy the lacunarity condition: there exists *q* > 1 such that *n**k* + 1 ≥ *qn**k* for all k,
- rk are such that r 1 2 + r 2 2 + ⋯ = ∞  and  r k 2 r 1 2 + ⋯ + r k 2 → 0 , {\displaystyle r_{1}^{2}+r_{2}^{2}+\cdots =\infty \quad {\text{ and }}\quad {\frac {r_{k}^{2}}{r_{1}^{2}+\cdots +r_{k}^{2}}}\to 0,} ({\displaystyle r_{1}^{2}+r_{2}^{2}+\cdots =\infty \quad {\text{ and }}\quad {\frac {r_{k}^{2}}{r_{1}^{2}+\cdots +r_{k}^{2}}}\to 0,})
- 0 ≤ *a**k* < 2π.

Then

X 1 + ⋯ + X k r 1 2 + ⋯ + r k 2 {\displaystyle {\frac {X_{1}+\cdots +X_{k}}{\sqrt {r_{1}^{2}+\cdots +r_{k}^{2}}}}} ({\displaystyle {\frac {X_{1}+\cdots +X_{k}}{\sqrt {r_{1}^{2}+\cdots +r_{k}^{2}}}}})

converges in distribution to N ( 0 , 1 2 ) {\textstyle {\mathcal {N}}{\big (}0,{\frac {1}{2}}{\big )}} ({\textstyle {\mathcal {N}}{\big (}0,{\frac {1}{2}}{\big )}}).

### Gaussian polytopes

**Theorem**—Let *A*1, ..., *A**n* be independent random points on the plane **R**2 each having the two-dimensional standard normal distribution. Let Kn be the convex hull of these points, and Xn the area of Kn Then

X n − E ⁡ ( X n ) Var ⁡ ( X n ) {\displaystyle {\frac {X_{n}-\operatorname {E} (X_{n})}{\sqrt {\operatorname {Var} (X_{n})}}}} ({\displaystyle {\frac {X_{n}-\operatorname {E} (X_{n})}{\sqrt {\operatorname {Var} (X_{n})}}}}) converges in distribution to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) as n tends to infinity.

The same also holds in all dimensions greater than 2.

The polytope Kn is called a Gaussian random polytope.

A similar result holds for the number of vertices (of the Gaussian polytope), the number of edges, and in fact, faces of all dimensions.

### Linear functions of orthogonal matrices

A linear function of a matrix **M** is a linear combination of its elements (with given coefficients), **M** ↦ tr(**AM**) where **A** is the matrix of the coefficients; see Trace (linear algebra)#Inner product.

A random orthogonal matrix is said to be distributed uniformly, if its distribution is the normalized Haar measure on the orthogonal group O(*n*,**R**); see Rotation matrix#Uniform random rotation matrices.

**Theorem**—Let **M** be a random orthogonal *n* × *n* matrix distributed uniformly, and **A** a fixed *n* × *n* matrix such that tr(**AA***) = *n*, and let *X* = tr(**AM**). Then the distribution of X is close to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) in the total variation metric up to ⁠2√3/*n* − 1⁠.

### Subsequences

**Theorem**—Let random variables *X*1, *X*2, ... ∈ *L*2(Ω) be such that *Xn* → 0 weakly in *L*2(Ω) and *X* *n* → 1 weakly in *L*1(Ω). Then there exist integers *n*1 < *n*2 < ⋯ such that

X n 1 + ⋯ + X n k k {\displaystyle {\frac {X_{n_{1}}+\cdots +X_{n_{k}}}{\sqrt {k}}}} ({\displaystyle {\frac {X_{n_{1}}+\cdots +X_{n_{k}}}{\sqrt {k}}}})

converges in distribution to N ( 0 , 1 ) {\textstyle {\mathcal {N}}(0,1)} ({\textstyle {\mathcal {N}}(0,1)}) as k tends to infinity.

### Random walk on a crystal lattice

The central limit theorem may be established for the simple random walk on a crystal lattice (an infinite-fold abelian covering graph over a finite graph), and is used for design of crystal structures.


## Applications and examples

A simple example of the central limit theorem is rolling many identical, unbiased dice. The distribution of the sum (or average) of the rolled numbers will be well approximated by a normal distribution. Since real-world quantities are often the balanced sum of many unobserved random events, the central limit theorem also provides a partial explanation for the prevalence of the normal probability distribution. It also justifies the approximation of large-sample statistics to the normal distribution in controlled experiments.

Comparison of probability density functions

p

(

k

)

for the sum of

n

fair 6-sided dice to show their convergence to a normal distribution with increasing

n

, in accordance to the central limit theorem. In the bottom-right graph, smoothed profiles of the previous graphs are rescaled, superimposed and compared with a normal distribution (black curve).

This figure demonstrates the central limit theorem. The sample means are generated using a random number generator, which draws numbers between 0 and 100 from a uniform probability distribution. It illustrates that increasing sample sizes result in the 500 measured sample means being more closely distributed about the population mean (50 in this case). It also compares the observed distributions with the distributions that would be expected for a normalized Gaussian distribution, and shows the

chi-squared

values that quantify the goodness of the fit (the fit is good if the reduced

chi-squared

value is less than or approximately equal to one). The input into the normalized Gaussian function is the mean of sample means (~50) and the mean sample standard deviation divided by the square root of the sample size (~28.87/

√

n

), which is called the standard deviation of the mean (since it refers to the spread of sample means).

### Regression

Regression analysis, and in particular ordinary least squares, specifies that a dependent variable depends according to some function upon one or more independent variables, with an additive error term. Various types of statistical inference on the regression assume that the error term is normally distributed. This assumption can be justified by assuming that the error term is actually the sum of many independent error terms; even if the individual error terms are not normally distributed, by the central limit theorem their sum can be well approximated by a normal distribution.

### Other illustrations

Given its importance to statistics, a number of papers and computer packages are available that demonstrate the convergence involved in the central limit theorem.


## History

Dutch mathematician Henk Tijms writes:

> The central limit theorem has an interesting history. The first version of this theorem was postulated by the French-born mathematician Abraham de Moivre who, in a remarkable article published in 1733, used the normal distribution to approximate the distribution of the number of heads resulting from many tosses of a fair coin. This finding was far ahead of its time, and was nearly forgotten until the famous French mathematician Pierre-Simon Laplace rescued it from obscurity in his monumental work *Théorie analytique des probabilités*, which was published in 1812. Laplace expanded De Moivre's finding by approximating the binomial distribution with the normal distribution. But as with De Moivre, Laplace's finding received little attention in his own time. It was not until the nineteenth century was at an end that the importance of the central limit theorem was discerned, when, in 1901, Russian mathematician Aleksandr Lyapunov defined it in general terms and proved precisely how it worked mathematically. Nowadays, the central limit theorem is considered to be the unofficial sovereign of probability theory.

Sir Francis Galton described the Central Limit Theorem in this way:

> I know of scarcely anything so apt to impress the imagination as the wonderful form of cosmic order expressed by the "Law of Frequency of Error". The law would have been personified by the Greeks and deified, if they had known of it. It reigns with serenity and in complete self-effacement, amidst the wildest confusion. The huger the mob, and the greater the apparent anarchy, the more perfect is its sway. It is the supreme law of Unreason. Whenever a large sample of chaotic elements are taken in hand and marshalled in the order of their magnitude, an unsuspected and most beautiful form of regularity proves to have been latent all along.

The actual term "central limit theorem" (in German: "zentraler Grenzwertsatz") was first used by George Pólya in 1920 in the title of a paper. Pólya referred to the theorem as "central" due to its importance in probability theory. According to Le Cam, the French school of probability interprets the word *central* in the sense that "it describes the behaviour of the centre of the distribution as opposed to its tails". The abstract of the paper *On the central limit theorem of calculus of probability and the problem of moments* by Pólya in 1920 translates as follows.

> The occurrence of the Gaussian probability density 1 = *e*−*x*2 in repeated experiments, in errors of measurements, which result in the combination of very many and very small elementary errors, in diffusion processes etc., can be explained, as is well-known, by the very same limit theorem, which plays a central role in the calculus of probability. The actual discoverer of this limit theorem is to be named Laplace; it is likely that its rigorous proof was first given by Tschebyscheff and its sharpest formulation can be found, as far as I am aware of, in an article by Liapounoff. ...

A thorough account of the theorem's history, detailing Laplace's foundational work, as well as Cauchy's, Bessel's and Poisson's contributions, is provided by Hald. Two historical accounts, one covering the development from Laplace to Cauchy, the second the contributions by von Mises, Pólya, Lindeberg, Lévy, and Cramér during the 1920s, are given by Hans Fischer. Le Cam describes a period around 1935. Bernstein presents a historical discussion focusing on the work of Pafnuty Chebyshev and his students Andrey Markov and Aleksandr Lyapunov that led to the first proofs of the CLT in a general setting.

A curious footnote to the history of the Central Limit Theorem is that a proof of a result similar to the 1922 Lindeberg CLT was the subject of Alan Turing's 1934 Fellowship Dissertation for King's College at the University of Cambridge. Only after submitting the work did Turing learn it had already been proved. Consequently, Turing's dissertation was not published.

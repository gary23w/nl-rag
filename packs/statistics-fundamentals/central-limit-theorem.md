---
title: "Central limit theorem"
source: https://en.wikipedia.org/wiki/Central_limit_theorem
domain: statistics-fundamentals
license: CC-BY-SA-4.0
tags: statistics fundamentals, probability, statistical inference, hypothesis testing, probability distribution
fetched: 2026-07-02
---

# Central limit theorem

In probability theory, the **central limit theorem** (**CLT**) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution. This holds even if the original variables themselves are not normally distributed. There are several versions of the CLT, each applying in the context of different conditions.

The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

This theorem has seen many changes during the formal development of probability theory. Previous versions of the theorem date back to 1811, but in its modern form it was only precisely stated in the 1920s.

In statistics, the CLT can be stated as: let $X_{1},X_{2},\dots ,X_{n}$ denote a statistical sample of size n from a population with expected value (average) $\mu$ and finite positive variance $\sigma ^{2}$ , and let ${\bar {X}}_{n}$ denote the sample mean (which is itself a random variable). Then the limit as $n\to \infty$ of the distribution of $({\bar {X}}_{n}-\mu ){\sqrt {n}}$ is a normal distribution with mean 0 and variance $\sigma ^{2}$ .

In other words, suppose that a large sample of observations is obtained, each observation being randomly produced in a way that does not depend on the values of the other observations, and the average (arithmetic mean) of the observed values is computed. If this procedure is performed many times, resulting in a collection of observed averages, the central limit theorem says that if the sample size is large enough, the probability distribution of these averages will closely approximate a normal distribution.

The central limit theorem has several variants. In its common form, the random variables must be independent and identically distributed (i.i.d.). This requirement can be weakened; convergence of the mean to the normal distribution also occurs for non-identical distributions or for non-independent observations if they comply with certain conditions.

The earliest version of this theorem, that the normal distribution may be used as an approximation to the binomial distribution, is the de Moivre–Laplace theorem.

## Independent sequences

### Classical CLT

Let $(X_{n})_{n\geq 1}$ be a sequence of i.i.d. random variables having a distribution with expected value given by $\mu$ and finite variance given by $\sigma ^{2}.$ Suppose we are interested in the sample average

${\bar {X}}_{n}\equiv {\frac {X_{1}+\cdots +X_{n}}{n}}.$

By the law of large numbers, the sample average converges almost surely (and therefore also converges in probability) to the expected value $\mu$ as $n\to \infty .$

The classical central limit theorem describes the size and the distributional form of the stochastic fluctuations around the deterministic number $\mu$ during this convergence. More precisely, it states that as n gets larger, the distribution of the normalized mean ${\sqrt {n}}({\bar {X}}_{n}-\mu )$ , i.e. the difference between the sample average ${\bar {X}}_{n}$ and its limit $\mu ,$ scaled by the factor ${\sqrt {n}}$ , approaches the normal distribution with mean 0 and variance $\sigma ^{2}.$ For large enough $n,$ the distribution of ${\bar {X}}_{n}$ gets arbitrarily close to the normal distribution with mean $\mu$ and variance $\sigma ^{2}/n.$

The usefulness of the theorem is that the distribution of ${\sqrt {n}}({\bar {X}}_{n}-\mu )$ approaches normality regardless of the shape of the distribution of the individual $X_{i}.$ Formally, the theorem can be stated as follows:

**Lindeberg–Lévy CLT**—Suppose $X_{1},X_{2},X_{3}\ldots$ is a sequence of i.i.d. random variables with $\operatorname {E} [X_{i}]=\mu$ and $\operatorname {Var} [X_{i}]=\sigma ^{2}<\infty .$ Then, as n approaches infinity, the random variables ${\sqrt {n}}({\bar {X}}_{n}-\mu )$ converge in distribution to a normal ${\mathcal {N}}(0,\sigma ^{2})$ :

${\sqrt {n}}\left({\bar {X}}_{n}-\mu \right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}\left(0,\sigma ^{2}\right).$

In the case $\sigma >0,$ convergence in distribution means that the cumulative distribution functions of ${\sqrt {n}}({\bar {X}}_{n}-\mu )$ converge pointwise to the cdf of the ${\mathcal {N}}(0,\sigma ^{2})$ distribution: for every real number $z,$

$\lim _{n\to \infty }\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]=\lim _{n\to \infty }\mathbb {P} \left[{\frac {{\sqrt {n}}({\bar {X}}_{n}-\mu )}{\sigma }}\leq {\frac {z}{\sigma }}\right]=\Phi \left({\frac {z}{\sigma }}\right),$

where $\Phi (z)$ is the standard normal cdf evaluated at $z.$ The convergence is uniform in z in the sense that

$\lim _{n\to \infty }\;\sup _{z\in \mathbb {R} }\;\left|\mathbb {P} \left[{\sqrt {n}}({\bar {X}}_{n}-\mu )\leq z\right]-\Phi \left({\frac {z}{\sigma }}\right)\right|=0~,$

where $\sup$ denotes the supremum (i.e. least upper bound) of the set.

### Lyapunov CLT

In this variant of the central limit theorem the random variables ${\textstyle X_{i}}$ have to be independent, but not necessarily identically distributed. The theorem also requires that random variables ${\textstyle \left|X_{i}\right|}$ have moments of some order ${\textstyle (2+\delta )}$ , and that the rate of growth of these moments is limited by the Lyapunov condition given below.

**Lyapunov CLT**—Suppose ${\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}$ is a sequence of independent random variables, each with finite expected value ${\textstyle \mu _{i}}$ and variance ${\textstyle \sigma _{i}^{2}}$ . Define

$s_{n}^{2}=\sum _{i=1}^{n}\sigma _{i}^{2}.$

If for some ${\textstyle \delta >0}$ , *Lyapunov's condition*

$\lim _{n\to \infty }\;{\frac {1}{s_{n}^{2+\delta }}}\,\sum _{i=1}^{n}\operatorname {E} \left[\left|X_{i}-\mu _{i}\right|^{2+\delta }\right]=0$

is satisfied, then a sum of ${\textstyle {\frac {X_{i}-\mu _{i}}{s_{n}}}}$ converges in distribution to a standard normal random variable, as ${\textstyle n}$ goes to infinity:

${\frac {1}{s_{n}}}\,\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}(0,1).$

In practice it is usually easiest to check Lyapunov's condition for ${\textstyle \delta =1}$ .

If a sequence of random variables satisfies Lyapunov's condition, then it also satisfies Lindeberg's condition. The converse implication, however, does not hold.

### Lindeberg (-Feller) CLT

In the same setting and with the same notation as above, the Lyapunov condition can be replaced with the following weaker one (from Lindeberg in 1920).

Suppose that for every ${\textstyle \varepsilon >0}$ ,

$\lim _{n\to \infty }{\frac {1}{s_{n}^{2}}}\sum _{i=1}^{n}\operatorname {E} \left[(X_{i}-\mu _{i})^{2}\cdot \mathbf {1} _{\left\{\left|X_{i}-\mu _{i}\right|>\varepsilon s_{n}\right\}}\right]=0$

where ${\textstyle \mathbf {1} _{\{\ldots \}}}$ is the indicator function. Then the distribution of the standardized sums

${\frac {1}{s_{n}}}\sum _{i=1}^{n}\left(X_{i}-\mu _{i}\right)$

converges towards the standard normal distribution ${\textstyle {\mathcal {N}}(0,1)}$ .

### CLT for the sum of a random number of random variables

Rather than summing an integer number n of random variables and taking $n\to \infty$ , the sum can be of a random number N of random variables, with conditions on N . For example, the following theorem is Corollary 4 of Robbins (1948). It assumes that N is asymptotically normal (Robbins also developed other conditions that lead to the same result).

**Robbins CLT**—Let $\{X_{i},i\geq 1\}$ be independent, identically distributed random variables with $E(X_{i})=\mu$ and ${\text{Var}}(X_{i})=\sigma ^{2}$ , and let $\{N_{n},n\geq 1\}$ be a sequence of non-negative integer-valued random variables that are independent of $\{X_{i},i\geq 1\}$ . Assume for each $n=1,2,\dots$ that $E(N_{n}^{2})<\infty$ and

${\frac {N_{n}-E(N_{n})}{\sqrt {{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)$

where $\xrightarrow {\,d\,}$ denotes convergence in distribution and ${\mathcal {N}}(0,1)$ is the normal distribution with mean 0, variance 1. Then

${\frac {\sum _{i=1}^{N_{n}}X_{i}-\mu E(N_{n})}{\sqrt {\sigma ^{2}E(N_{n})+\mu ^{2}{\text{Var}}(N_{n})}}}\xrightarrow {\quad d\quad } {\mathcal {N}}(0,1)$

### Multidimensional CLT

Proofs that use characteristic functions can be extended to cases where each individual ${\textstyle \mathbf {X} _{i}}$ is a random vector in ${\textstyle \mathbb {R} ^{k}}$ , with mean vector ${\textstyle {\boldsymbol {\mu }}=\operatorname {E} [\mathbf {X} _{i}]}$ and covariance matrix ${\textstyle \mathbf {\Sigma } }$ (among the components of the vector), and these random vectors are independent and identically distributed. The multidimensional central limit theorem states that when scaled, sums converge to a multivariate normal distribution. Summation of these vectors is done component-wise.

For $i=1,2,3,\ldots ,$ let

$\mathbf {X} _{i}={\begin{bmatrix}X_{i}^{(1)}\\\vdots \\X_{i}^{(k)}\end{bmatrix}}$

be independent random vectors. The sum of the random vectors $\mathbf {X} _{1},\ldots ,\mathbf {X} _{n}$ is

$\sum _{i=1}^{n}\mathbf {X} _{i}={\begin{bmatrix}X_{1}^{(1)}\\\vdots \\X_{1}^{(k)}\end{bmatrix}}+{\begin{bmatrix}X_{2}^{(1)}\\\vdots \\X_{2}^{(k)}\end{bmatrix}}+\cdots +{\begin{bmatrix}X_{n}^{(1)}\\\vdots \\X_{n}^{(k)}\end{bmatrix}}={\begin{bmatrix}\sum _{i=1}^{n}X_{i}^{(1)}\\\vdots \\\sum _{i=1}^{n}X_{i}^{(k)}\end{bmatrix}}$

and their average is

$\mathbf {{\bar {X}}_{n}} ={\begin{bmatrix}{\bar {X}}_{i}^{(1)}\\\vdots \\{\bar {X}}_{i}^{(k)}\end{bmatrix}}={\frac {1}{n}}\sum _{i=1}^{n}\mathbf {X} _{i}.$

Therefore,

${\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}\left[\mathbf {X} _{i}-\operatorname {E} \left(\mathbf {X} _{i}\right)\right]={\frac {1}{\sqrt {n}}}\sum _{i=1}^{n}(\mathbf {X} _{i}-{\boldsymbol {\mu }})={\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right).$

The multivariate central limit theorem states that

${\sqrt {n}}\left({\overline {\mathbf {X} }}_{n}-{\boldsymbol {\mu }}\right)\mathrel {\overset {d}{\longrightarrow }} {\mathcal {N}}_{k}(0,{\boldsymbol {\Sigma }}),$ where the covariance matrix ${\boldsymbol {\Sigma }}$ is equal to ${\boldsymbol {\Sigma }}={\begin{bmatrix}{\operatorname {Var} \left(X_{1}^{(1)}\right)}&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(1)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(1)}\right)&\operatorname {Var} \left(X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(2)},X_{1}^{(k)}\right)\\\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(2)}\right)&\operatorname {Var} \left(X_{1}^{(3)}\right)&\cdots &\operatorname {Cov} \left(X_{1}^{(3)},X_{1}^{(k)}\right)\\\vdots &\vdots &\vdots &\ddots &\vdots \\\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(1)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(2)}\right)&\operatorname {Cov} \left(X_{1}^{(k)},X_{1}^{(3)}\right)&\cdots &\operatorname {Var} \left(X_{1}^{(k)}\right)\\\end{bmatrix}}~.$

The multivariate central limit theorem can be proved using the Cramér–Wold theorem.

The rate of convergence is given by the following Berry–Esseen type result:

**Theorem**—Let $X_{1},\dots ,X_{n},\dots$ be independent $\mathbb {R} ^{d}$ -valued random vectors, each having mean zero. Write $S=\sum _{i=1}^{n}X_{i}$ and assume $\Sigma =\operatorname {Cov} [S]$ is invertible. Let $Z\sim {\mathcal {N}}(0,\Sigma )$ be a d -dimensional Gaussian with the same mean and same covariance matrix as S . Then for all convex sets $U\subseteq \mathbb {R} ^{d}$ ,

$\left|\mathbb {P} [S\in U]-\mathbb {P} [Z\in U]\right|\leq C\,d^{1/4}\gamma ~,$ where C is a universal constant, $\gamma =\sum _{i=1}^{n}\operatorname {E} \left[\left\|\Sigma ^{-1/2}X_{i}\right\|_{2}^{3}\right]$ , and $\|\cdot \|_{2}$ denotes the Euclidean norm on $\mathbb {R} ^{d}$ .

It is unknown whether the factor ${\textstyle d^{1/4}}$ is necessary.

## The generalized central limit theorem

The generalized central limit theorem (GCLT) was an effort of multiple mathematicians (Sergei Bernstein, Jarl Waldemar Lindeberg, Paul Lévy, William Feller, Andrey Kolmogorov, and others) over the period from 1920 to 1937. The first published complete proof of the GCLT was in 1937 by Paul Lévy in French. An English language version of the complete proof of the GCLT is available in the translation of Boris Vladimirovich Gnedenko and Kolmogorov's 1954 book.

The statement of the GCLT is as follows:

**Statement of GCLT**—A non-degenerate random variable Z is α-stable for some 0 < *α* ≤ 2 if and only if there is an independent, identically distributed sequence of random variables *X*1, *X*2, *X*3, ..., and constants *a**n* > 0, *b**n* ∈ ℝ with $a_{n}(X_{1}+\dots +X_{n})-b_{n}\to Z.$ Here, '→' means the sequence of random variable sums converges in distribution; i.e., the corresponding distributions satisfy *F**n*(*y*) → *F*(*y*) at all continuity points of F.

In other words, if sums of independent, identically distributed random variables converge in distribution to some Z, then Z must be a stable distribution.

## Dependent processes

### CLT under weak dependence

A useful generalization of a sequence of independent, identically distributed random variables is a mixing random process in discrete time; "mixing" means, roughly, that random variables temporally far apart from one another are nearly independent. Several kinds of mixing are used in ergodic theory and probability theory. See especially strong mixing (also called α-mixing) defined by ${\textstyle \alpha (n)\to 0}$ where ${\textstyle \alpha (n)}$ is so-called strong mixing coefficient.

A simplified formulation of the central limit theorem under strong mixing is:

**Theorem**—Suppose that ${\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}$ is stationary and $\alpha$ -mixing with ${\textstyle \alpha _{n}=O\left(n^{-5}\right)}$ and that ${\textstyle \operatorname {E} [X_{n}]=0}$ and ${\textstyle \operatorname {E} [X_{n}^{12}]<\infty }$ . Denote ${\textstyle S_{n}=X_{1}+\cdots +X_{n}}$ , then the limit

$\sigma ^{2}=\lim _{n\rightarrow \infty }{\frac {\operatorname {E} \left(S_{n}^{2}\right)}{n}}$

exists, and if ${\textstyle \sigma \neq 0}$ then ${\textstyle {\frac {S_{n}}{\sigma {\sqrt {n}}}}}$ converges in distribution to ${\textstyle {\mathcal {N}}(0,1)}$ .

In fact,

$\sigma ^{2}=\operatorname {E} \left(X_{1}^{2}\right)+2\sum _{k=1}^{\infty }\operatorname {E} \left(X_{1}X_{1+k}\right),$

where the series converges absolutely.

The assumption ${\textstyle \sigma \neq 0}$ cannot be omitted, since the asymptotic normality fails for ${\textstyle X_{n}=Y_{n}-Y_{n-1}}$ where ${\textstyle Y_{n}}$ are another stationary sequence.

There is a stronger version of the theorem: the assumption ${\textstyle \operatorname {E} \left[X_{n}^{12}\right]<\infty }$ is replaced with ${\textstyle \operatorname {E} \left[{\left|X_{n}\right|}^{2+\delta }\right]<\infty }$ , and the assumption ${\textstyle \alpha _{n}=O\left(n^{-5}\right)}$ is replaced with

$\sum _{n}\alpha _{n}^{\frac {\delta }{2(2+\delta )}}<\infty .$

Existence of such ${\textstyle \delta >0}$ ensures the conclusion. For encyclopedic treatment of limit theorems under mixing conditions see (Bradley 2007).

### Martingale difference CLT

**Theorem**—Let a martingale ${\textstyle M_{n}}$ satisfy

- ${\frac {1}{n}}\sum _{k=1}^{n}\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mid M_{1},\dots ,M_{k-1}\right]\to 1$ in probability as *n* → ∞,
- for every *ε* > 0, ${\frac {1}{n}}\sum _{k=1}^{n}{\operatorname {E} \left[\left(M_{k}-M_{k-1}\right)^{2}\mathbf {1} \left[|M_{k}-M_{k-1}|>\varepsilon {\sqrt {n}}\right]\right]}\to 0$ as *n* → ∞,

then ${\textstyle {\frac {M_{n}}{\sqrt {n}}}}$ converges in distribution to ${\textstyle {\mathcal {N}}(0,1)}$ as ${\textstyle n\to \infty }$ .

## Remarks

### Proof of classical CLT

The central limit theorem has a proof using characteristic functions. It is similar to the proof of the (weak) law of large numbers.

Assume ${\textstyle \{X_{1},\ldots ,X_{n},\ldots \}}$ are independent and identically distributed random variables, each with mean ${\textstyle \mu }$ and finite variance ${\textstyle \sigma ^{2}}$ . The sum ${\textstyle X_{1}+\cdots +X_{n}}$ has mean ${\textstyle n\mu }$ and variance ${\textstyle n\sigma ^{2}}$ . Consider the random variable

$Z_{n}={\frac {X_{1}+\cdots +X_{n}-n\mu }{\sqrt {n\sigma ^{2}}}}=\sum _{i=1}^{n}{\frac {X_{i}-\mu }{\sqrt {n\sigma ^{2}}}}=:\sum _{i=1}^{n}{\frac {1}{\sqrt {n}}}Y_{i},$

where the last step defines the new random variables ${\textstyle Y_{i}:={\frac {X_{i}-\mu }{\sigma }}}$ , each with zero mean and unit variance ( ${\textstyle \operatorname {var} (Y)=1}$ ). The characteristic function of ${\textstyle Z_{n}}$ is given by

${\begin{aligned}\varphi _{Z_{n}}\!(t)=\varphi _{\sum _{i=1}^{n}{{\frac {1}{\sqrt {n}}}Y_{i}}}\!(t)\ &=\ \varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\varphi _{Y_{2}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\cdots \varphi _{Y_{n}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\\[1ex]&=\ \left[\varphi _{Y_{1}}\!\!\left({\frac {t}{\sqrt {n}}}\right)\right]^{n},\end{aligned}}$

where the last step relies on the fact that all of the ${\textstyle Y_{i}}$ are identically distributed. The characteristic function of ${\textstyle Y_{1}}$ is, by Taylor's theorem, $\varphi _{Y_{1}}\!\left({\frac {t}{\sqrt {n}}}\right)=1-{\frac {t^{2}}{2n}}+o\!\left({\frac {t^{2}}{n}}\right),\quad \left({\frac {t}{\sqrt {n}}}\right)\to 0$

where ${\textstyle o(t^{2}/n)}$ is "little o notation" for some function of ${\textstyle t}$ that goes to zero more rapidly than ${\textstyle t^{2}/n}$ . By the limit of the exponential function ( ${\textstyle e^{x}=\lim _{n\to \infty }\left(1+{\frac {x}{n}}\right)^{n}}$ ), the characteristic function of $Z_{n}$ equals

$\varphi _{Z_{n}}(t)=\left(1-{\frac {t^{2}}{2n}}+o\left({\frac {t^{2}}{n}}\right)\right)^{n}\rightarrow e^{-{\frac {1}{2}}t^{2}},\quad n\to \infty .$

All of the higher order terms vanish in the limit ${\textstyle n\to \infty }$ . The right hand side equals the characteristic function of a standard normal distribution ${\textstyle {\mathcal {N}}(0,1)}$ , which implies through Lévy's continuity theorem that the distribution of ${\textstyle Z_{n}}$ will approach ${\textstyle {\mathcal {N}}(0,1)}$ as ${\textstyle n\to \infty }$ . Therefore, the sample average

${\bar {X}}_{n}={\frac {X_{1}+\cdots +X_{n}}{n}}$

is such that

${\frac {\sqrt {n}}{\sigma }}\left({\bar {X}}_{n}-\mu \right)=Z_{n}$

converges to the normal distribution ${\textstyle {\mathcal {N}}(0,1)}$ , from which the central limit theorem follows.

### Convergence to the limit

The central limit theorem gives only an asymptotic distribution. As an approximation for a finite number of observations, it provides a reasonable approximation only when close to the peak of the normal distribution; it requires a very large number of observations to stretch into the tails.

The convergence in the central limit theorem is uniform because the limiting cumulative distribution function is continuous. If the third central moment ${\textstyle \operatorname {E} \left[(X_{1}-\mu )^{3}\right]}$ exists and is finite, then the speed of convergence is at least on the order of ${\textstyle 1/{\sqrt {n}}}$ (see Berry–Esseen theorem). Stein's method can be used not only to prove the central limit theorem, but also to provide bounds on the rates of convergence for selected metrics.

The convergence to the normal distribution is monotonic, in the sense that the entropy of ${\textstyle Z_{n}}$ increases monotonically to that of the normal distribution.

The central limit theorem applies in particular to sums of independent and identically distributed discrete random variables. A sum of discrete random variables is still a discrete random variable, so that we are confronted with a sequence of discrete random variables whose cumulative probability distribution function converges towards a cumulative probability distribution function corresponding to a continuous variable (namely that of the normal distribution). This means that if we build a histogram of the realizations of the sum of n independent identical discrete variables, the piecewise-linear curve that joins the centers of the upper faces of the rectangles forming the histogram converges toward a Gaussian curve as n approaches infinity; this relation is known as de Moivre–Laplace theorem. The binomial distribution article details such an application of the central limit theorem in the simple case of a discrete variable taking only two possible values.

### Common misconceptions

Studies have shown that the central limit theorem is subject to several common but serious misconceptions, some of which appear in widely used textbooks. These include:

- The misconceived belief that the theorem applies to random sampling of any variable, rather than to the mean values (or sums) of iid random variables extracted from a population by repeated sampling. That is, the theorem assumes the random sampling produces a sampling distribution formed from different values of means (or sums) of such random variables.
- The misconceived belief that the theorem ensures that random sampling leads to the emergence of a normal distribution for sufficiently large samples of any random variable, regardless of the population distribution. In reality, such sampling asymptotically reproduces the properties of the population, an intuitive result underpinned by the Glivenko–Cantelli theorem.
- The misconceived belief that the theorem leads to a good approximation of a normal distribution for sample sizes greater than around 30, allowing reliable inferences regardless of the nature of the population. In reality, this empirical rule of thumb has no valid justification, and can lead to seriously flawed inferences. See Z-test for where the approximation holds.

### Relation to the law of large numbers

The law of large numbers as well as the central limit theorem are partial solutions to a general problem: "What is the limiting behavior of Sn as n approaches infinity?" In mathematical analysis, asymptotic series are one of the most popular tools employed to approach such questions.

Suppose we have an asymptotic expansion of ${\textstyle f(n)}$ :

$f(n)=a_{1}\varphi _{1}(n)+a_{2}\varphi _{2}(n)+O{\big (}\varphi _{3}(n){\big )}\qquad (n\to \infty ).$

Dividing both parts by *φ*1(*n*) and taking the limit will produce *a*1, the coefficient of the highest-order term in the expansion, which represents the rate at which *f*(*n*) changes in its leading term.

$\lim _{n\to \infty }{\frac {f(n)}{\varphi _{1}(n)}}=a_{1}.$

Informally, one can say: "*f*(*n*) grows approximately as *a*1*φ*1(*n*)". Taking the difference between *f*(*n*) and its approximation and then dividing by the next term in the expansion, we arrive at a more refined statement about *f*(*n*):

$\lim _{n\to \infty }{\frac {f(n)-a_{1}\varphi _{1}(n)}{\varphi _{2}(n)}}=a_{2}.$

Here one can say that the difference between the function and its approximation grows approximately as *a*2*φ*2(*n*). The idea is that dividing the function by appropriate normalizing functions, and looking at the limiting behavior of the result, can tell us much about the limiting behavior of the original function itself.

Informally, something along these lines happens when the sum, Sn, of independent identically distributed random variables, *X*1, ..., *Xn*, is studied in classical probability theory. If each Xi has finite mean μ, then by the law of large numbers, ⁠*Sn*/*n*⁠ → *μ*. If in addition each Xi has finite variance *σ*2, then by the central limit theorem,

${\frac {S_{n}-n\mu }{\sqrt {n}}}\to \xi ,$

where ξ is distributed as *N*(0,*σ*2). This provides values of the first two constants in the informal expansion

$S_{n}\approx \mu n+\xi {\sqrt {n}}.$

In the case where the Xi do not have finite mean or variance, convergence of the shifted and rescaled sum can also occur with different centering and scaling factors:

${\frac {S_{n}-a_{n}}{b_{n}}}\rightarrow \Xi ,$

or informally

$S_{n}\approx a_{n}+\Xi b_{n}.$

Distributions Ξ which can arise in this way are called *stable*. Clearly, the normal distribution is stable, but there are also other stable distributions, such as the Cauchy distribution, for which the mean or variance are not defined. The scaling factor bn may be proportional to nc, for any *c* ≥ ⁠1/2⁠; it may also be multiplied by a slowly varying function of n.

The law of the iterated logarithm specifies what is happening "in between" the law of large numbers and the central limit theorem. Specifically it says that the normalizing function √*n* log log *n*, intermediate in size between n of the law of large numbers and √*n* of the central limit theorem, provides a non-trivial limiting behavior.

### Alternative statements of the theorem

#### Density functions

The density of the sum of two or more independent variables is the convolution of their densities (if these densities exist). Thus the central limit theorem can be interpreted as a statement about the properties of density functions under convolution: the convolution of a number of density functions tends to the normal density as the number of density functions increases without bound. These theorems require stronger hypotheses than the forms of the central limit theorem given above. Theorems of this type are often called local limit theorems. See Petrov for a particular local limit theorem for sums of independent and identically distributed random variables.

#### Characteristic functions

Since the characteristic function of a convolution is the product of the characteristic functions of the densities involved, the central limit theorem has yet another restatement: the product of the characteristic functions of a number of density functions becomes close to the characteristic function of the normal density as the number of density functions increases without bound, under the conditions stated above. Specifically, an appropriate scaling factor needs to be applied to the argument of the characteristic function.

An equivalent statement can be made about Fourier transforms, since the characteristic function is essentially a Fourier transform.

### Calculating the variance

Let Sn be the sum of n random variables. Many central limit theorems provide conditions such that Sn/√Var(Sn) converges in distribution to *N*(0,1) (the normal distribution with mean 0, variance 1) as n → ∞. In some cases, it is possible to find a constant *σ*2 and function f(n) such that Sn/(σ√n⋅f(n)) converges in distribution to *N*(0,1) as n→ ∞.

**Lemma**—Suppose $X_{1},X_{2},\dots$ is a sequence of real-valued and strictly stationary random variables with $\operatorname {E} (X_{i})=0$ for all i , $g:[0,1]\to \mathbb {R}$ , and $S_{n}=\sum _{i=1}^{n}g\left({\tfrac {i}{n}}\right)X_{i}$ . Construct

$\sigma ^{2}=\operatorname {E} (X_{1}^{2})+2\sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})$

1. If $\sum _{i=1}^{\infty }\operatorname {E} (X_{1}X_{1+i})$ is absolutely convergent, $\left|\int _{0}^{1}g(x)g'(x)\,dx\right|<\infty$ , and $0<\int _{0}^{1}(g(x))^{2}dx<\infty$ then $\mathrm {Var} (S_{n})/(n\gamma _{n})\to \sigma ^{2}$ as $n\to \infty$ where $\gamma _{n}={\frac {1}{n}}\sum _{i=1}^{n}\left(g\left({\tfrac {i}{n}}\right)\right)^{2}$ .
2. If in addition $\sigma >0$ and $S_{n}/{\sqrt {\mathrm {Var} (S_{n})}}$ converges in distribution to ${\mathcal {N}}(0,1)$ as $n\to \infty$ then $S_{n}/(\sigma {\sqrt {n\gamma _{n}}})$ also converges in distribution to ${\mathcal {N}}(0,1)$ as $n\to \infty$ .

## Extensions

### Products of positive random variables

The logarithm of a product is simply the sum of the logarithms of the factors. Therefore, when the logarithm of a product of random variables that take only positive values approaches a normal distribution, the product itself approaches a log-normal distribution. Many physical quantities (especially mass or length, which are a matter of scale and cannot be negative) are the products of different random factors, so they follow a log-normal distribution. This multiplicative version of the central limit theorem is sometimes called Gibrat's law.

Whereas the central limit theorem for sums of random variables requires the condition of finite variance, the corresponding theorem for products requires the corresponding condition that the density function be square-integrable.

## Beyond the classical framework

Asymptotic normality, that is, convergence to the normal distribution after appropriate shift and rescaling, is a phenomenon much more general than the classical framework treated above, namely, sums of independent random variables (or vectors). New frameworks are revealed from time to time; no single unifying framework is available for now.

### Convex body

**Theorem**—There exists a sequence *εn* ↓ 0 for which the following holds. Let *n* ≥ 1, and let random variables *X*1, ..., *Xn* have a log-concave joint density f such that *f*(*x*1, ..., *xn*) = *f*(|*x*1|, ..., |*xn*|) for all *x*1, ..., *xn*, and E(*X*2 *k*) = 1 for all *k* = 1, ..., *n*. Then the distribution of

${\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}$

is εn-close to ${\textstyle {\mathcal {N}}(0,1)}$ in the total variation distance.

These two εn-close distributions have densities (in fact, log-concave densities), thus, the total variance distance between them is the integral of the absolute value of the difference between the densities. Convergence in total variation is stronger than weak convergence.

An important example of a log-concave density is a function constant inside a given convex body and vanishing outside; it corresponds to the uniform distribution on the convex body, which explains the term "central limit theorem for convex bodies".

Another example: *f*(*x*1, ..., *xn*) = const · exp(−(|*x*1|*α* + ⋯ + |*xn*|*α*)*β*) where *α* > 1 and *αβ* > 1. If *β* = 1 then *f*(*x*1, ..., *xn*) factorizes into const · exp (−|*x*1|*α*) ... exp(−|*xn*|*α*), which means *X*1, ..., *Xn* are independent. In general, however, they are dependent.

The condition *f*(*x*1, ..., *xn*) = *f*(|*x*1|, ..., |*xn*|) ensures that *X*1, ..., *Xn* are of zero mean and uncorrelated; still, they need not be independent, nor even pairwise independent. By the way, pairwise independence cannot replace independence in the classical central limit theorem.

Here is a Berry–Esseen type result.

**Theorem**—Let *X*1, ..., *Xn* satisfy the assumptions of the previous theorem, then

$\left|\mathbb {P} \left(a\leq {\frac {X_{1}+\cdots +X_{n}}{\sqrt {n}}}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq {\frac {C}{n}}$

for all *a* < *b*; here C is a universal (absolute) constant. Moreover, for every *c*1, ..., *cn* ∈ **R** such that *c*2 1 + ⋯ + *c*2 *n* = 1,

$\left|\mathbb {P} \left(a\leq c_{1}X_{1}+\cdots +c_{n}X_{n}\leq b\right)-{\frac {1}{\sqrt {2\pi }}}\int _{a}^{b}e^{-{\frac {1}{2}}t^{2}}\,dt\right|\leq C\left(c_{1}^{4}+\dots +c_{n}^{4}\right).$

The distribution of ⁠*X*1 + ⋯ + *Xn*/√*n*⁠ need not be approximately normal (in fact, it can be uniform). However, the distribution of *c*1*X*1 + ⋯ + *cnXn* is close to ${\textstyle {\mathcal {N}}(0,1)}$ (in the total variation distance) for most vectors (*c*1, ..., *cn*) according to the uniform distribution on the sphere *c*2 1 + ⋯ + *c*2 *n* = 1.

### Lacunary trigonometric series

**Theorem (Salem–Zygmund)**—Let U be a random variable distributed uniformly on (0,2π), and *Xk* = *rk* cos(*nkU* + *ak*), where

- nk satisfy the lacunarity condition: there exists *q* > 1 such that *n**k* + 1 ≥ *qn**k* for all k,
- rk are such that $r_{1}^{2}+r_{2}^{2}+\cdots =\infty \quad {\text{ and }}\quad {\frac {r_{k}^{2}}{r_{1}^{2}+\cdots +r_{k}^{2}}}\to 0,$
- 0 ≤ *a**k* < 2π.

Then

${\frac {X_{1}+\cdots +X_{k}}{\sqrt {r_{1}^{2}+\cdots +r_{k}^{2}}}}$

converges in distribution to ${\textstyle {\mathcal {N}}{\big (}0,{\frac {1}{2}}{\big )}}$ .

### Gaussian polytopes

**Theorem**—Let *A*1, ..., *A**n* be independent random points on the plane **R**2 each having the two-dimensional standard normal distribution. Let Kn be the convex hull of these points, and Xn the area of Kn Then

${\frac {X_{n}-\operatorname {E} (X_{n})}{\sqrt {\operatorname {Var} (X_{n})}}}$ converges in distribution to ${\textstyle {\mathcal {N}}(0,1)}$ as n tends to infinity.

The same also holds in all dimensions greater than 2.

The polytope Kn is called a Gaussian random polytope.

A similar result holds for the number of vertices (of the Gaussian polytope), the number of edges, and in fact, faces of all dimensions.

### Linear functions of orthogonal matrices

A linear function of a matrix **M** is a linear combination of its elements (with given coefficients), **M** ↦ tr(**AM**) where **A** is the matrix of the coefficients; see Trace (linear algebra)#Inner product.

A random orthogonal matrix is said to be distributed uniformly, if its distribution is the normalized Haar measure on the orthogonal group O(*n*,**R**); see Rotation matrix#Uniform random rotation matrices.

**Theorem**—Let **M** be a random orthogonal *n* × *n* matrix distributed uniformly, and **A** a fixed *n* × *n* matrix such that tr(**AA***) = *n*, and let *X* = tr(**AM**). Then the distribution of X is close to ${\textstyle {\mathcal {N}}(0,1)}$ in the total variation metric up to ⁠2√3/*n* − 1⁠.

### Subsequences

**Theorem**—Let random variables *X*1, *X*2, ... ∈ *L*2(Ω) be such that *Xn* → 0 weakly in *L*2(Ω) and *X* *n* → 1 weakly in *L*1(Ω). Then there exist integers *n*1 < *n*2 < ⋯ such that

${\frac {X_{n_{1}}+\cdots +X_{n_{k}}}{\sqrt {k}}}$

converges in distribution to ${\textstyle {\mathcal {N}}(0,1)}$ as k tends to infinity.

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
